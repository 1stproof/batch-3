"""Repairable, deterministic human view of problem-local durable pilot evidence.

This module never supplies scientific, scheduling, dispatch, or acceptance authority.
It does not interpret proof text or follow source references outside the problem.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


MARKER = '<!-- merlean-generated-working-log:v1 -->'


def _hash(raw):
    return hashlib.sha256(raw).hexdigest()


def _order(path):
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', str(path))]


def _text(value):
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _literal(value):
    # Indentation prevents supplied Markdown/HTML from becoming document structure.
    return '\n'.join('    ' + line for line in _text(value).split('\n')) + '\n'


def _field(lines, record, key, label=None):
    if key in record:
        lines.extend([f'**{label or key.replace("_", " ").capitalize()}:**', _literal(record[key])])


class _Projection:
    def __init__(self, root):
        self.root = root
        self.sources = {}
        self.lines = [MARKER, '# Working log',
            'Reconstructed from durable records; this is not contemporaneous authored notes. '
            'Regeneration replaces this view. Raw records remain authoritative. This log grants '
            'no review, dispatch, grade, or acceptance authority.',
            'Model-reported work and review verdicts are reports, not independently confirmed results. '
            'Transport completion is not mathematical success. Missing timestamps and rationale '
            'are not inferred. Sections use recorded sequence order, not inferred chronology.',
            '`proof.md` remains the separate latest standalone proof. Continue to maintain authored '
            '`notes.md`/`ledger.md` and `failure-log.md`; use their prior lessons together with the '
            'underlying checkpoint records when resuming. This view does not replace that discipline.']

    def source(self, relative, pointer='', heading=None):
        path = self.root / relative
        if not path.exists() and not path.is_symlink():
            return None
        if heading:
            self.lines.append('### ' + heading)
        # Refuse links and special files, including links in nested directories.
        if any(parent.is_symlink() for parent in (path, *path.parents)
               if parent == self.root or self.root in parent.parents):
            self.lines.append('Source skipped: symbolic link in source path.')
            return None
        if not path.is_file():
            self.lines.append('Source skipped: not a regular file.')
            return None
        raw = path.read_bytes()
        self.sources[str(relative)] = raw
        self.binding(relative, raw, pointer)
        try:
            value = json.loads(raw)
        except (ValueError, UnicodeError):
            self.lines.append('Source is malformed JSON; preserved without interpretation.')
            return None
        if not isinstance(value, dict):
            self.lines.append('Legacy or malformed non-object record; preserved without interpretation.')
            return None
        return value

    def binding(self, relative, raw, pointer=''):
        self.lines.extend(['Source binding (problem-relative path, SHA-256, JSON pointer):',
            _literal({'path': str(relative), 'sha256': _hash(raw), 'pointer': pointer})])

    def fields(self, record, names):
        for key in names:
            _field(self.lines, record, key)

    def time(self, record):
        stamp = next((record[k] for k in ('created_utc', 'updated_utc', 'utc', 'end_utc', 'start_utc')
                      if isinstance(record.get(k), str) and record[k]), None)
        self.lines.extend(['**Recorded timestamp:**', _literal(stamp or 'not supplied by this record')])

    def work(self, record, key):
        work = record.get(key)
        if not isinstance(work, dict):
            self.lines.append('No structured research-work report supplied by this record.')
            return
        self.lines.append('**Model-reported attempt (unverified; fields from `' + key + '`):**')
        self.fields(work, ('objective', 'approach', 'work_performed', 'result', 'failed_approaches', 'next_step'))

    def records(self, parent, key, raw, names, *, times=False):
        rows = parent.get(key, [])
        if not isinstance(rows, list):
            self.lines.append('Malformed `' + key + '` collection; see source.')
            return
        for index, row in enumerate(rows):
            self.lines.append('### ' + key.replace('_', ' ').capitalize() + ' ' + str(index + 1))
            self.binding('host-progress.json', raw, '/' + key + '/' + str(index))
            if not isinstance(row, dict):
                self.lines.append('Legacy or malformed entry; see source.')
                continue
            if times:
                self.time(row)
            self.fields(row, names)

    def render(self):
        self.lines.append('## Authored research memory')
        for name in ('notes.md', 'ledger.md', 'failure-log.md'):
            path = self.root / name
            if path.is_file() and not path.is_symlink():
                self.lines.append(f'[{name}]({name}) — preserved authored record; SHA-256 `{_hash(path.read_bytes())}`.')
            else:
                self.lines.append(f'`{name}`: no regular authored file present; no content synthesized.')

        self.lines.append('## Current durable host snapshot and dispatch history')
        progress = self.source('host-progress.json')
        if progress is not None:
            raw = self.sources['host-progress.json']
            self.time(progress)
            self.fields(progress, ('phase', 'main_session'))
            self.records(progress, 'calls', raw, ('name', 'module', 'status', 'session_id', 'request_id',
                'answer_sha256', 'failure_kind', 'exit_code'), times=True)
            self.lines.append('### Saved response reports')
            calls = progress.get('calls', [])
            seen = set()
            for call in calls if isinstance(calls, list) else []:
                if not isinstance(call, dict) or not isinstance(call.get('name'), str):
                    continue
                label = call['name'].rsplit('/', 1)[-1]
                if not re.fullmatch(r'[0-9]+-[A-Za-z0-9_-]+', label) or label in seen:
                    continue
                seen.add(label)
                report = self.source(label + '.json', heading=label + ' — reported content, unverified')
                if report is not None:
                    self.fields(report, ('response_type', 'verdict', 'status', 'summary', 'gaps',
                        'proof_revision', 'selected_candidate_sha256', 'parse_error'))
                    if 'research_work' in report:
                        self.work(report, 'research_work')
            self.lines.append('## Remaining issues and operational errors (as recorded)')
            self.records(progress, 'open_findings', raw, ('id', 'status', 'severity', 'finding', 'summary',
                'description', 'statement', 'required_fix', 'rationale'))
            self.records(progress, 'errors', raw, ('type', 'stage', 'reason', 'error', 'details', 'retry_seconds'), times=True)
            self.lines.append('## Assessment outcomes (host reports, not revalidation)')
            self.records(progress, 'final_assessment_history', raw, ('binding_key', 'candidate_sha256',
                'status', 'attempts', 'protocol_epoch', 'authority', 'infrastructure_resume_of',
                'final_validation'), times=True)

        self.lines.append('## Main checkpoints and contract failures')
        paths = set(self.root.glob('main-*-checkpoint.json')) | set(self.root.glob('main-*-invalid-contract.json'))
        for path in sorted(paths, key=_order):
            record = self.source(path.name, heading=path.name)
            if record is None:
                continue
            self.time(record)
            self.fields(record, ('effective_candidate_sha256', 'request_key', 'actionable',
                'host_stop_reason', 'host_resume_reason', 'error', 'recovery_exhausted', 'acceptance_authority'))
            checkpoint = record.get('raw_checkpoint')
            if isinstance(checkpoint, dict):
                self.fields(checkpoint, ('response_type', 'selected_candidate_sha256', 'proof_revision',
                    'checkpoint_metadata', 'reason', 'review_request', 'proposed_work', 'unreviewed_findings'))
                self.work(checkpoint, 'research_work')

        self.lines.append('## Research continuation decisions')
        for path in sorted(self.root.glob('research-continuation-[0-9]*.json'), key=_order):
            record = self.source(path.name, heading=path.name)
            if record is None:
                continue
            self.time(record)
            self.fields(record, ('step', 'mode', 'reason', 'decision', 'rationale', 'bindings',
                'previous_receipt', 'authority'))
            self.work(record, 'last_research_work')
            self.lines.append('Full feedback and scientific context remain in the bound source; nested histories are not copied here.')

        self.lines.append('## Saved local probe outcomes (execution evidence, not theorem acceptance)')
        probes = self.root / 'probes'
        if not probes.is_symlink():
            for path in sorted(probes.glob('*/result.json'), key=_order):
                record = self.source(path.relative_to(self.root), heading=path.parent.name)
                if record is not None:
                    self.time(record)
                    self.fields(record, ('status', 'returncode', 'exit_code', 'timed_out', 'error'))
                    self.lines.append('Full stdout/stderr and source remain in this probe directory; diagnostics are not paraphrased.')

        self.lines.append('## Proof revision references (authored artifacts, no acceptance implied)')
        pointer = self.source('proof-current.json')
        if pointer is not None:
            self.fields(pointer, ('revision', 'manifest_sha256'))
        revisions = self.root / 'proof-revisions'
        if not revisions.is_symlink():
            for path in sorted(revisions.glob('*/manifest.json'), key=_order):
                record = self.source(path.relative_to(self.root), heading=path.parent.name)
                if record is not None:
                    self.time(record)
                    self.fields(record, ('revision', 'sequence', 'status', 'parent', 'last_submission', 'producer', 'files', 'authority'))
        handoff = self.source('paper-source-handoff.json', heading='Recorded paper source handoff')
        if handoff is not None:
            self.fields(handoff, ('source_revision', 'proof', 'candidate_sha256', 'acceptance', 'gaps', 'authority'))
        return '\n\n'.join(self.lines) + '\n'


def render(problem_folder):
    """Reconstruct a readable view without mutating any source or validating claims."""
    root = Path(problem_folder)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('working log requires an existing real problem directory')
    return _Projection(root).render()


def refresh(problem_folder):
    """Best-effort view publication; failures never affect research or acceptance.

    Existing non-generated working logs are preserved. No timestamp is fabricated;
    identical evidence is byte-idempotent, including after copying a continuation.
    """
    temporary = None
    try:
        root = Path(problem_folder)
        target = root / 'working-log.md'
        if target.is_symlink():
            return {'status': 'skipped', 'reason': 'working-log.md is a symbolic link'}
        old = target.read_bytes() if target.exists() else None
        if old is not None and not old.startswith((MARKER + '\n').encode()):
            return {'status': 'skipped', 'reason': 'preserved existing authored working-log.md'}
        payload = render(root).encode('utf-8')
        if old == payload:
            return {'status': 'unchanged', 'sha256': _hash(payload)}
        fd, temporary = tempfile.mkstemp(prefix='.working-log-', dir=root)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
        return {'status': 'updated', 'sha256': _hash(payload)}
    except Exception as error:
        # Deliberately isolated from scientific execution, including older schemas.
        return {'status': 'failed', 'reason': type(error).__name__ + ': ' + str(error)}
    finally:
        if temporary is not None:
            try:
                os.unlink(temporary)
            except OSError:
                pass
