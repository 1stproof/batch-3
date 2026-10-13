"""Host-published proof revisions; saves are not review or acceptance authority.

Only the current-pointer replacement publishes a revision. Human-readable proof.md
is a repairable view; reviewers and paper handoffs pin immutable revision bytes.
"""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import uuid


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode('utf-8')).hexdigest()


class ProofRevisionConflict(ValueError):
    pass


def _identity(problem_id, original_sha256, main_session):
    if (not isinstance(problem_id, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', problem_id)
            or not isinstance(original_sha256, str) or not re.fullmatch(r'[0-9a-f]{64}', original_sha256)
            or not isinstance(main_session, str) or not main_session.strip()):
        raise ValueError('proof document requires exact problem, original and main identity')
    return dict(problem_id=problem_id, original_sha256=original_sha256, main_session=main_session)


def _regular(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError('proof artifact must be a regular host-owned file')
    return path.read_bytes()


def _sync_directory(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _atomic(path, payload):
    if path.is_symlink():
        raise ValueError('proof publication refuses symlink views')
    fd, temporary = tempfile.mkstemp(prefix='.proof-write-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(payload); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
        _sync_directory(path.parent)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def _lock(root):
    import fcntl
    root = Path(root)
    if root.is_symlink():
        raise ValueError('proof store must be a real directory')
    root.mkdir(parents=True, exist_ok=True)
    lock = root / '.proof-document.lock'
    fd = os.open(lock, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield root
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)


def _revision(root, ref, identity):
    if (not isinstance(ref, dict) or set(ref) != {'revision', 'manifest_sha256'}
            or not isinstance(ref['revision'], str)
            or not re.fullmatch(r'r[0-9]+-[0-9a-f]{32}', ref['revision'])):
        raise ValueError('invalid immutable proof revision reference')
    directory = root / 'proof-revisions' / ref['revision']
    if directory.is_symlink() or directory.parent.is_symlink():
        raise ValueError('proof revisions cannot use symlinks')
    raw = _regular(directory / 'manifest.json')
    if digest(raw) != ref['manifest_sha256']:
        raise ValueError('proof revision manifest changed')
    manifest = json.loads(raw)
    if (manifest.get('schema_version') != 1 or manifest.get('identity') != identity
            or manifest.get('revision') != ref['revision']
            or manifest.get('status') not in ('draft', 'submitted')
            or set(manifest.get('files', {})) != ({'proof.md', 'candidate.json'} if manifest.get('status') == 'submitted' else {'proof.md'})):
        raise ValueError('proof revision identity or schema mismatch')
    payloads = {name: _regular(directory / name) for name in manifest['files']}
    if any(digest(payloads[name]) != bound for name, bound in manifest['files'].items()):
        raise ValueError('immutable proof revision content changed')
    proof = payloads['proof.md'].decode('utf-8')
    if not proof.strip():
        raise ValueError('empty proof document')
    candidate = json.loads(payloads['candidate.json']) if 'candidate.json' in payloads else None
    if candidate is not None and candidate.get('proof_markdown') != proof:
        raise ValueError('candidate and proof document differ')
    return {'revision': ref['revision'], 'manifest_sha256': ref['manifest_sha256'],
            'proof_sha256': manifest['files']['proof.md'], 'proof_markdown': proof,
            'status': manifest['status'], 'manifest': manifest, 'candidate': candidate,
            'proof_path': str(directory / 'proof.md')}


def _current(root, identity):
    pointer = root / 'proof-current.json'
    if not pointer.exists():
        if pointer.is_symlink():
            raise ValueError('unreadable proof pointer')
        return None
    ref = json.loads(_regular(pointer))
    if not isinstance(ref, dict) or set(ref) != {'schema_version', 'revision', 'manifest_sha256'} or ref['schema_version'] != 1:
        raise ValueError('invalid proof current pointer')
    return _revision(root, {k: ref[k] for k in ('revision', 'manifest_sha256')}, identity)


def read_current(store_root, *, problem_id, original_sha256, main_session):
    identity = _identity(problem_id, original_sha256, main_session)
    root = Path(store_root)
    if root.is_symlink():
        raise ValueError('proof store must be a real directory')
    current = _current(root, identity)
    if current is None:
        raise ValueError('proof document has not been initialized by the host')
    return current


def read_revision(store_root, ref, *, problem_id, original_sha256, main_session):
    return _revision(Path(store_root), ref, _identity(problem_id, original_sha256, main_session))


def _producer(producer, identity):
    if (not isinstance(producer, dict) or set(producer) != {'stage', 'request_id', 'session_id'}
            or any(not isinstance(v, str) or not v for v in producer.values())
            or producer['session_id'] != identity['main_session']):
        raise ValueError('proof save requires host-bound original-main producer')
    return dict(producer)


def _publish(root, identity, previous, proof, producer, candidate=None):
    if not isinstance(proof, str) or not proof.strip():
        raise ValueError('proof update requires nonempty full Markdown; partial drafts must state their gaps')
    _producer(producer, identity)
    sequence = previous['manifest']['sequence'] + 1 if previous else 1
    revision = f'r{sequence:08d}-' + uuid.uuid4().hex
    parent = ({k: previous[k] for k in ('revision', 'manifest_sha256')} if previous else None)
    last_submission = (parent if previous and previous['status'] == 'submitted'
                       else previous['manifest'].get('last_submission') if previous else None)
    content = {'proof.md': proof.encode('utf-8')}
    if candidate is not None:
        if (not isinstance(candidate, dict) or candidate.get('proof_markdown') != proof
                or not isinstance(candidate.get('ledger'), dict)):
            raise ValueError('submission requires exact proof and structured candidate ledger')
        content['candidate.json'] = encoded(candidate).encode('utf-8')
    manifest = {'schema_version': 1, 'revision': revision, 'sequence': sequence,
                'identity': identity, 'status': 'submitted' if candidate is not None else 'draft',
                'parent': parent, 'last_submission': last_submission,
                'producer': dict(producer), 'created_utc': datetime.now(timezone.utc).isoformat(),
                'files': {name: digest(raw) for name, raw in content.items()},
                'authority': 'authored_artifact_only_no_review_or_acceptance_authority'}
    revisions = root / 'proof-revisions'
    if revisions.is_symlink():
        raise ValueError('proof revision directory cannot be a symlink')
    revisions.mkdir(exist_ok=True)
    directory = revisions / revision
    directory.mkdir()  # Exclusive; incomplete orphan remains preserved on failure.
    for name, raw in {**content, 'manifest.json': encoded(manifest).encode('utf-8')}.items():
        with (directory / name).open('xb') as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    _sync_directory(directory); _sync_directory(revisions)
    ref = {'revision': revision, 'manifest_sha256': digest(encoded(manifest))}
    _revision(root, ref, identity)
    warning = None
    try:
        _atomic(root / 'proof-current.json', encoded({'schema_version': 1, **ref}).encode('utf-8'))
    except OSError as error:
        # rename may have committed before a directory fsync failure. Read back
        # the sole authority before reporting an ambiguous publication as failed.
        observed = _current(root, identity)
        if observed is None or observed['revision'] != revision:
            raise
        warning = {'type': type(error).__name__, 'message': str(error)}
    result = _refresh_view(root, _revision(root, ref, identity))
    if warning is not None:
        result['publication_warning'] = warning
    return result


def _refresh_view(root, current):
    # Publication has already committed. A view failure is never an unsaved draft.
    result = dict(current)
    try:
        _atomic(root / 'proof.md', current['proof_markdown'].encode('utf-8'))
        result['view_status'] = 'current'
    except (OSError, ValueError) as error:
        result['view_status'] = 'repair_required'
        result['view_error'] = {'type': type(error).__name__, 'message': str(error)}
    return result


def read_submission(store_root, *, problem_id, original_sha256, main_session):
    value = read_current(store_root, problem_id=problem_id,
                         original_sha256=original_sha256, main_session=main_session)
    if value['status'] == 'submitted':
        return value
    ref = value['manifest']['last_submission']
    if ref is None:
        raise ValueError('proof draft has no submitted candidate')
    submitted = read_revision(store_root, ref, problem_id=problem_id,
                              original_sha256=original_sha256, main_session=main_session)
    if submitted['status'] != 'submitted':
        raise ValueError('last submission reference is not a submitted candidate')
    return submitted


def save_draft(store_root, *, problem_id, original_sha256, main_session,
               expected_revision, proof_markdown, producer):
    identity = _identity(problem_id, original_sha256, main_session)
    with _lock(store_root) as root:
        current = _current(root, identity)
        if current is None or current['revision'] != expected_revision:
            raise ProofRevisionConflict('proof base revision changed; read current proof before saving')
        _producer(producer, identity)
        if current['proof_markdown'] == proof_markdown:
            return _refresh_view(root, current)
        return _publish(root, identity, current, proof_markdown, producer)


def submit(store_root, *, problem_id, original_sha256, main_session,
           expected_revision, candidate, producer):
    """Explicit final-response publication; never dispatches a reviewer or worker."""
    identity = _identity(problem_id, original_sha256, main_session)
    with _lock(store_root) as root:
        current = _current(root, identity)
        if (current['revision'] if current else None) != expected_revision:
            raise ProofRevisionConflict('proof submission base revision changed')
        _producer(producer, identity)
        if current and current['status'] == 'draft' and candidate.get('proof_markdown') != current['proof_markdown']:
            raise ProofRevisionConflict('submission must preserve the exact current authored draft')
        if current and current['status'] == 'submitted' and encoded(current['candidate']) == encoded(candidate):
            return _refresh_view(root, current)
        return _publish(root, identity, current, candidate.get('proof_markdown'), producer, candidate)


def repair_view(store_root, *, problem_id, original_sha256, main_session):
    identity = _identity(problem_id, original_sha256, main_session)
    with _lock(store_root) as root:
        current = _current(root, identity)
        if current is None:
            raise ValueError('proof document has not been initialized')
        return _refresh_view(root, current)


def paper_handoff(store_root, ref, *, problem_id, original_sha256, main_session, acceptance):
    """Pin the submitted Markdown as source evidence; no grade or TeX authority."""
    value = read_revision(store_root, ref, problem_id=problem_id,
                          original_sha256=original_sha256, main_session=main_session)
    if value['status'] != 'submitted':
        raise ValueError('paper handoff requires a submitted candidate revision')
    if (not isinstance(acceptance, dict) or acceptance.get('successful_complete') is not True
            or acceptance.get('status') != 'complete'
            or acceptance.get('answer_sha256') != value['proof_sha256']
            or not isinstance(acceptance.get('manifest'), str)
            or not re.fullmatch(r'[0-9a-f]{64}', acceptance.get('sha256', ''))):
        raise ValueError('paper source requires exact independently validated controller acceptance')
    return {'schema_version': 1, 'source_revision': dict(ref),
            'original_sha256': original_sha256, 'main_session': main_session,
            'proof': {'path': value['proof_path'], 'sha256': value['proof_sha256']},
            'candidate_sha256': value['manifest']['files']['candidate.json'],
            'acceptance': acceptance, 'gaps': value['candidate'].get('remaining_gaps', []),
            'authority': 'source_handoff_only_preserve_existing_paper_and_research_gates',
            'translation': 'Retain this immutable Markdown as source evidence; independently audit mathematical preservation in TeX.'}
