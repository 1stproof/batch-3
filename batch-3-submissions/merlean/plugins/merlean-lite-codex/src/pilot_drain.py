"""Future-host cooperative drain; no signals, cancellation, polling model or restart.

Use only in the controller's single asyncio loop and a host-only directory.
An admission is linearized when admission() polls then registers synchronously.
Request-file creation is NOT the closure boundary or final acknowledgment.
Admitted operations may finish; hold their admission through artifact/accounting
commit. This helper cannot retrofit a drain boundary onto an older running host.
"""
from __future__ import annotations

import asyncio
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
import uuid


def _now():
    return datetime.now(timezone.utc).isoformat()


def _hash(payload):
    return hashlib.sha256(payload).hexdigest()


def _save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(value, stream, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


class DrainRequested(RuntimeError):
    """Stop before a new launch; checkpoint existing completed work normally."""


class PilotDrain:
    """Host-local admission gate. Constructing it never authorizes a launch."""

    def __init__(self, host_directory):
        self.directory = Path(host_directory).resolve()
        self.request_path = self.directory / 'drain-request.json'
        self.closed_path = self.directory / 'drain-admission-closed.json'
        self.ack_path = self.directory / 'drain-ack.json'
        self.host_session_id = uuid.uuid4().hex
        self._loop = None
        self._active = {}
        self._closure = None
        # A removed request must not reopen previously closed admission after a
        # host restart. Prior state is evidence requiring reconciliation.
        if self.closed_path.exists() or self.ack_path.exists():
            self._closure = {'status': 'prior_drain_requires_reconciliation',
                             'closed_utc': _now(), 'host_session_id': self.host_session_id}

    def _same_loop(self):
        loop = asyncio.get_running_loop()
        if self._loop is None:
            self._loop = loop
        elif self._loop is not loop:
            raise RuntimeError('drain admission must use one host asyncio loop')

    @property
    def closed(self):
        return self._closure is not None

    @property
    def active_count(self):
        return len(self._active)

    def poll(self):
        """Observe an explicit request; fail closed if it cannot be validated."""
        self._same_loop()
        if self.closed:
            return True
        payload = None
        request = None
        error = None
        try:
            payload = self.request_path.read_bytes()
        except FileNotFoundError:
            if not self.request_path.is_symlink():
                return False
            error = 'FileNotFoundError: drain request target unreadable'
        except OSError as exc:
            error = type(exc).__name__ + ': request unreadable'
        if payload is not None:
            try:
                request = json.loads(payload)
                if (not isinstance(request, dict) or request.get('schema_version') != 1
                        or request.get('action') != 'drain'
                        or not isinstance(request.get('request_id'), str) or not request['request_id'].strip()
                        or not isinstance(request.get('reason'), str) or not request['reason'].strip()):
                    raise ValueError('schema_version=1, action=drain, request_id and reason required')
            except (ValueError, UnicodeError) as exc:
                error = type(exc).__name__ + ': invalid drain request'
                request = None
        self._closure = {'schema_version': 1, 'status': 'admission_closed',
            'host_session_id': self.host_session_id, 'host_pid': os.getpid(), 'closed_utc': _now(),
            'request_sha256': _hash(payload) if payload is not None else None,
            'request_id': request['request_id'] if request is not None else None,
            'reason': request['reason'] if request is not None else None, 'request_error': error,
            'admitted_operations_at_closure': list(self._active.values()),
            'drained': False,
            'boundary': 'Host observed request and closed admission synchronously; file creation was not acknowledgment.'}
        # Set closed before persistence so a filesystem failure cannot reopen it.
        _save(self.closed_path, self._closure)
        return True

    def check(self):
        """Call before retry waits or checkpoint transitions, without admission."""
        if self.poll():
            raise DrainRequested('host admission closed; preserve completed work and checkpoint before another launch')

    @contextmanager
    def admission(self, kind, label):
        """Register immediately before launch; no await between check and register.

        For queued stages, enter AFTER acquiring the concurrency semaphore.
        Exit only after the admitted operation has stopped and its artifacts and
        accounting are committed. Exceptions alone do not prove child exit;
        final acknowledgment separately requires host reconciliation evidence.
        """
        if kind not in {'stage', 'probe'} or not isinstance(label, str) or not label.strip():
            raise ValueError('stage/probe kind and nonempty operation label required')
        self.check()
        token = uuid.uuid4().hex
        self._active[token] = {'kind': kind, 'label': label, 'admitted_utc': _now()}
        try:
            yield token
        finally:
            self._same_loop()
            self._active.pop(token)

    def acknowledge(self, *, checkpoint_paths, result_path, reconciliation_path):
        """Record final drained state only after host tasks and children finish.

        The host must independently reconcile retained launches/processes and
        write a receipt with schema_version=1, this host_session_id,
        all_owned_children_stopped=true, active_children=[], pending_launches=[],
        and checked_utc. This helper never treats an exited admission as proof
        of process death. Checkpoints/result are committed host artifacts.
        """
        self._same_loop()
        if not self.poll() or self._closure.get('status') != 'admission_closed':
            raise ValueError('current host admission closure required')
        if self._active:
            raise ValueError('admitted operations still active; drain not complete')
        if self.ack_path.exists():
            raise FileExistsError('drain acknowledgment already exists')
        paths = list(checkpoint_paths)
        if not paths:
            raise ValueError('committed problem checkpoints required')

        def ref(path):
            resolved = Path(path).resolve()
            payload = resolved.read_bytes()
            return {'path': str(resolved), 'sha256': _hash(payload)}

        reconciliation = json.loads(Path(reconciliation_path).read_bytes())
        if not isinstance(reconciliation, dict):
            raise ValueError('current host owned-child reconciliation required')
        if (reconciliation.get('schema_version') != 1
                or reconciliation.get('host_session_id') != self.host_session_id
                or reconciliation.get('all_owned_children_stopped') is not True
                or reconciliation.get('active_children') != []
                or reconciliation.get('pending_launches') != []
                or not reconciliation.get('checked_utc')):
            raise ValueError('current host owned-child reconciliation required')
        try:
            checked = datetime.fromisoformat(reconciliation['checked_utc'].replace('Z', '+00:00'))
            closed = datetime.fromisoformat(self._closure['closed_utc'])
            if checked.tzinfo is None or checked < closed:
                raise ValueError('reconciliation must follow admission closure')
        except (TypeError, AttributeError, ValueError) as exc:
            raise ValueError('reconciliation must follow admission closure') from exc
        result = json.loads(Path(result_path).read_bytes())
        if not isinstance(result, dict) or not result.get('end_utc') or not isinstance(result.get('results'), list) or not result['results']:
            raise ValueError('committed terminal host result required')
        if any(not isinstance(item, dict) or item.get('status') not in {'complete', 'partial'} for item in result['results']):
            raise ValueError('committed terminal host result required')
        receipt = {'schema_version': 1, 'status': 'drained', 'drained': True,
            'host_session_id': self.host_session_id, 'acknowledged_utc': _now(),
            'admission_closed': ref(self.closed_path), 'request_id': self._closure['request_id'],
            'request_error': self._closure['request_error'], 'active_operations': 0,
            'checkpoints': [ref(path) for path in paths], 'terminal_result': ref(result_path),
            'owned_child_reconciliation': ref(reconciliation_path),
            'meaning': 'Admitted work committed and children reconciled; mathematical completion is determined by terminal results, not this receipt.'}
        _save(self.ack_path, receipt)
        return receipt
