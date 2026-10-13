"""Append-only supersession of a verified canceled, never-started preparation.

The supported orchestrator's exclusive cancellation sidecar is the launch barrier.
These checks do not prevent arbitrary execution of an older frozen program.
"""
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tempfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def _path(value):
    if not isinstance(value, str):
        raise ValueError('reservation evidence requires canonical absolute paths')
    path = Path(value)
    if not path.is_absolute() or str(path) != value or path.resolve() != path:
        raise ValueError('reservation evidence requires canonical absolute paths without symlinks')
    return path


def _ref(ref):
    if not isinstance(ref, dict) or set(ref) != {'path', 'sha256'}:
        raise ValueError('reservation evidence requires path and sha256')
    path = _path(ref['path'])
    data = path.read_bytes()
    if digest(data) != ref['sha256']:
        raise ValueError('reservation evidence hash mismatch')
    value = json.loads(data)
    if not isinstance(value, dict):
        raise ValueError('reservation evidence requires an object')
    return path, value


def base_reservation(source):
    return source.parent / '.continuation-reservations' / (digest(str(source).encode()) + '.json')


def successor_path(reservation):
    return reservation.with_name(reservation.stem + '.successor.json')


def _files(root):
    paths = sorted(root.rglob('*'))
    if any(path.is_symlink() for path in paths):
        raise ValueError('cancelled preparation contains symlinks')
    return {str(path.relative_to(root)): digest(path.read_bytes()) for path in paths if path.is_file()}


def _empty_accounting(root):
    folder = root / 'host/accounting'
    if not folder.exists():
        return
    allowed = {'usage.sqlite3', 'usage.sqlite3-shm', 'usage.sqlite3-wal'}
    if {p.name for p in folder.iterdir()} - allowed or not (folder / 'usage.sqlite3').is_file():
        raise ValueError('cancelled preparation contains unexpected accounting artifacts')
    # Include the WAL without opening or modifying the preserved database/shm.
    with tempfile.TemporaryDirectory() as name:
        copy = Path(name)
        for path in folder.iterdir():
            shutil.copy2(path, copy / path.name)
        with closing(sqlite3.connect('file:' + str(copy / 'usage.sqlite3') + '?mode=ro', uri=True)) as connection:
            tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if (not {'calls', 'usage_events'} <= tables or 'codex_stages' in tables
                    or connection.execute('PRAGMA quick_check').fetchone() != ('ok',)
                    or any(connection.execute('SELECT COUNT(*) FROM ' + table).fetchone()[0]
                           for table in ('calls', 'usage_events'))):
                raise ValueError('cancelled preparation has accounting activity')


def validate_supersession(source, root, parent, supersession):
    """Revalidate exact cancellation evidence; no reservations or run files are written."""
    source, root = _path(str(source)), _path(str(root))
    path = _path(str(supersession))
    raw = path.read_bytes()
    receipt = json.loads(raw)
    fields = {'schema_version', 'kind', 'parent', 'parent_manifest_sha256', 'destination',
              'cancelled_root', 'cancelled_config_sha256', 'predecessor_reservation',
              'cancelled_inventory', 'cancelled_launch', 'checked_utc', 'model_dispatched'}
    if (not isinstance(receipt, dict) or set(receipt) != fields
            or type(receipt['schema_version']) is not int or receipt['schema_version'] != 1
            or receipt['kind'] != 'cancelled_unstarted_continuation_supersession'
            or receipt['model_dispatched'] is not False):
        raise ValueError('invalid cancelled-unstarted supersession schema')
    checked = datetime.fromisoformat(receipt['checked_utc'].replace('Z', '+00:00'))
    if checked.tzinfo is None or checked > datetime.now(timezone.utc):
        raise ValueError('invalid cancellation check timestamp')
    if (receipt['parent'] != str(source) or receipt['destination'] != str(root)
            or parent.get('source_root') != str(source)
            or receipt['parent_manifest_sha256'] != parent.get('manifest_sha256')):
        raise ValueError('supersession parent or destination mismatch')
    if (not isinstance(parent.get('files'), dict)
            or digest(json.dumps(parent['files'], sort_keys=True, separators=(',', ':')).encode()) != parent['manifest_sha256']
            or _files(source) != parent['files']):
        raise ValueError('supersession sealed parent file census changed')
    predecessor, reservation = _ref(receipt['predecessor_reservation'])
    if predecessor != base_reservation(source):
        raise ValueError('only the original canonical reservation may be superseded')
    cancelled = _path(receipt['cancelled_root'])
    if (cancelled == root or cancelled == source or cancelled.is_relative_to(source)
            or source.is_relative_to(cancelled) or root.is_relative_to(cancelled)
            or cancelled.is_relative_to(root)
            or reservation.get('parent') != str(source)
            or reservation.get('destination') != str(cancelled)
            or reservation.get('parent_manifest_sha256') != parent['manifest_sha256']):
        raise ValueError('supersession predecessor binding mismatch')
    _, inventory = _ref(receipt['cancelled_inventory'])
    launch_path, launch = _ref(receipt['cancelled_launch'])
    if launch_path != cancelled.with_name(cancelled.name + '.launch.json'):
        raise ValueError('cancellation launch barrier is not the canonical sidecar')
    for evidence in (inventory, launch):
        if (evidence.get('status') != 'cancelled_before_launch'
                or evidence.get('run_root') != str(cancelled)
                or evidence.get('model_dispatched') is not False
                or any(key in evidence for key in ('pid', 'host_pid', 'child_pid', 'probe_pid'))):
            raise ValueError('predecessor was not cancelled before launch')
    if any((cancelled / name).exists() for name in ('HOST-STARTED', 'pilot-result.json')) or cancelled.with_name(cancelled.name + '.host.log').exists():
        raise ValueError('cancelled preparation has host execution evidence')
    if not isinstance(inventory.get('files'), dict) or inventory['files'] != _files(cancelled):
        raise ValueError('cancelled preparation file census changed')
    config_path = cancelled / 'host-config.json'
    config = json.loads(config_path.read_bytes())
    saved_parent = json.loads((cancelled / 'continuation-parent.json').read_bytes())
    if (digest(config_path.read_bytes()) != receipt['cancelled_config_sha256']
            or config.get('continuation_parent') != str(source)
            or config.get('continuation_reservation') != str(predecessor)
            or saved_parent.get('source_root') != str(source)
            or saved_parent.get('manifest_sha256') != parent['manifest_sha256']
            or saved_parent.get('files') != parent.get('files')):
        raise ValueError('cancelled configuration or sealed parent differs')
    if _files(cancelled / 'host/runtime') != _files(source / 'host/runtime'):
        raise ValueError('cancelled preparation contains new transport stages')
    if any(p.name not in {'runtime', 'accounting'} for p in (cancelled / 'host').iterdir()):
        raise ValueError('cancelled preparation contains new host artifacts')
    _empty_accounting(cancelled)
    census = subprocess.run(['ps', '-axo', 'pid=,ppid=,pgid=,args='], check=True,
                            capture_output=True, text=True, timeout=10)
    for line in census.stdout.splitlines():
        fields = line.strip().split(None, 3)
        if len(fields) != 4 or any(not field.isdigit() for field in fields[:3]):
            raise ValueError('incomplete cancellation process census')
        if int(fields[0]) != os.getpid() and str(cancelled) in fields[3]:
            raise ValueError('live process references cancelled preparation')
    # Recheck durable exclusion and inventory after the process/database inspection.
    _ref(receipt['predecessor_reservation']); _ref(receipt['cancelled_launch'])
    if inventory['files'] != _files(cancelled):
        raise ValueError('cancelled preparation changed during validation')
    return {'path': str(path), 'sha256': digest(raw), 'predecessor': receipt['predecessor_reservation']}


def validate_start(root, config):
    """Prospective supported-launch guard; an existing successor always blocks its predecessor."""
    root = root.resolve()
    launch = root.with_name(root.name + '.launch.json')
    if launch.is_file() and json.loads(launch.read_bytes()).get('status') == 'cancelled_before_launch':
        raise ValueError('cancelled preparation cannot start')
    ref = config.get('continuation_reservation_receipt')
    if ref is None:
        return
    reservation, value = _ref(ref)
    source = _path(config['continuation_parent'])
    parent = json.loads((root / 'continuation-parent.json').read_bytes())
    if (str(reservation) != config.get('continuation_reservation')
            or value.get('parent') != str(source) or value.get('destination') != str(root)
            or value.get('parent_manifest_sha256') != parent.get('manifest_sha256')
            or successor_path(reservation).exists()):
        raise ValueError('continuation reservation is mismatched or superseded')
    supersession = config.get('continuation_reservation_supersession')
    if supersession is not None:
        path, _ = _ref(supersession)
        binding = validate_supersession(source, root, parent, path)
        if (reservation != successor_path(base_reservation(source))
                or value.get('supersession') != binding
                or binding['sha256'] != supersession['sha256']):
            raise ValueError('successor reservation binding mismatch')
    elif reservation != base_reservation(source) or 'supersession' in value:
        raise ValueError('unsupported continuation reservation chain')
