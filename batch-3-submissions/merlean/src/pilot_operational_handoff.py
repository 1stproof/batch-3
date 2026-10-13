"""Voluntary, evidence-bound operational stop; never new review or acceptance authority."""
from pathlib import Path
import json
import os
import re

from codex_transport import extract_answer
from pilot_candidate_contract import candidate_hash
import pilot_review_exhaustion as exhaustion

KIND = 'operational_handoff'
FIELDS = {'response_type', 'selected_candidate_sha256', 'exhaustion_ids', 'reason', 'no_new_scientific_work'}
FILE = 'operational-handoff.json'
AUTHORITY = 'supervisor_needed_no_dispatch_review_or_acceptance_authority'
GUIDANCE = (
    'An ordinary empty blocked_checkpoint continues research; it is not an operational stop. '
    'If the host discloses operational_handoff eligibility, you may voluntarily request a supervisor handoff '
    'when the remaining required review is operationally exhausted and you have no concrete new scientific work to submit. '
    'Return EXACTLY {"response_type":"operational_handoff","selected_candidate_sha256":"<current host hash>",'
    '"exhaustion_ids":["<all matching host IDs>"],"reason":"<nonempty operational explanation>",'
    '"no_new_scientific_work":true}. This declaration is your self-report, not proof that no useful work or mathematical gap exists. '
    'Never conceal a discovered gap or changed proof to request handoff: submit the complete candidate_update or legitimate '
    'scientific findings instead. A pending draft must be handled through the existing draft/submission contract. '
    'Handoff preserves all current artifacts and failed reviews and ends this problem partial for supervisor attention. '
    'It neither supplies a verdict, renews review admission, changes budgets, nor authorizes automatic resume. '
    'Do not manufacture a revision, finding, or retry request merely to escape an exhausted-review boundary.'
)


class OperationalHandoff(RuntimeError):
    def __init__(self, receipt):
        self.receipt = receipt
        super().__init__('explicit original-main operational handoff; supervisor resolution required')


def matching(problem, records):
    if not records or not getattr(problem, 'current', None):
        return []
    projection = exhaustion.projection(problem.current)
    return [record for record in records if record['binding']['scientific'] == projection]


def capability(problem):
    records = matching(problem, getattr(problem, 'review_exhaustions', []))
    eligible = bool(records) and all(r.get('required_material_delivered') is True for r in records)
    if not getattr(problem, 'session', None) or not problem.documents_enabled():
        eligible = False
    elif eligible:
        doc = problem.document_current()
        eligible = doc['status'] == 'submitted' and doc['proof_markdown'] == problem.current.get('proof_markdown')
    return {'eligible': eligible, 'current_candidate_sha256': candidate_hash(problem.current) if getattr(problem, 'current', None) else None,
            'matching_exhaustion_ids': sorted(r['id'] for r in records),
            'authority': AUTHORITY}


def validate_request(problem, raw, records):
    if (not isinstance(raw, dict) or set(raw) != FIELDS or raw.get('response_type') != KIND
            or raw.get('no_new_scientific_work') is not True
            or not isinstance(raw.get('reason'), str) or not raw['reason'].strip()):
        raise ValueError('operational_handoff requires exactly five canonical fields and literal true; no scientific or work fields')
    if raw['selected_candidate_sha256'] != candidate_hash(problem.current):
        raise ValueError('operational_handoff must select the exact current complete candidate')
    ids = raw['exhaustion_ids']
    if (not isinstance(ids, list) or not ids or any(not isinstance(x, str) or not re.fullmatch('[0-9a-f]{64}', x) for x in ids)
            or len(ids) != len(set(ids))):
        raise ValueError('operational_handoff requires distinct exact exhaustion IDs')
    matched = matching(problem, records)
    if sorted(ids) != sorted(r['id'] for r in matched) or not all(r.get('required_material_delivered') is True for r in matched):
        raise ValueError('operational_handoff does not bind current authenticated exhausted review and completed required delivery')
    if not problem.documents_enabled():
        raise ValueError('operational_handoff requires the canonical submitted proof document')
    doc = problem.document_current()
    if doc['status'] != 'submitted' or doc['proof_markdown'] != problem.current['proof_markdown']:
        raise ValueError('operational_handoff cannot bypass a pending or changed proof document')
    if getattr(problem, 'active_stages', set()):
        raise ValueError('operational_handoff requires this problem to have no active stage')
    return matched, {k: doc[k] for k in ('revision', 'manifest_sha256', 'proof_sha256', 'status')}


def bound_answer(problem, meta):
    if (meta.get('status') != 'completed' or not meta.get('module', '').startswith('main')
            or meta.get('session_id') != problem.session or meta.get('model_verified') is not True
            or meta.get('turn_completed') is not True or meta.get('document_audit', {}).get('required_material_delivered') is not True):
        raise ValueError('operational_handoff requires a completed verified original-main call with required delivery')
    stage, _, _, meta_sha = exhaustion.metadata(meta)
    text = exhaustion.regular_bytes(stage / 'stage.answer.txt')
    if exhaustion.hashlib.sha256(text).hexdigest() != meta.get('answer_sha256'):
        raise ValueError('operational_handoff source answer hash changed')
    raw, _, error = extract_answer(text.decode())
    if error or raw != json.loads(exhaustion.regular_bytes(stage / 'stage.answer.json')):
        raise ValueError('operational_handoff parsed source answer changed')
    return raw, meta_sha


def receipt_for(problem, raw, meta):
    calls = getattr(problem, 'calls', [])
    if not calls or calls[-1] != meta:
        raise ValueError('operational_handoff must be the latest authoritative call')
    actual, meta_sha = bound_answer(problem, meta)
    if raw != actual:
        raise ValueError('operational_handoff differs from authenticated original-main answer')
    records = exhaustion.synchronize(problem.folder, calls)
    matched, doc = validate_request(problem, raw, records)
    if any(exhaustion.moment(meta['start_utc']) <= exhaustion.moment(r['end_utc']) for r in matched):
        raise ValueError('operational_handoff main call must follow exhausted review')
    return {'schema_version': 1, 'authority': AUTHORITY, 'status': 'supervisor_needed',
            'source_stage': meta['name'], 'source_session': problem.session,
            'source_meta_sha256': meta_sha, 'source_answer_sha256': meta['answer_sha256'],
            'request': raw, 'candidate_sha256': candidate_hash(problem.current), 'proof_document': doc,
            'exhaustion_ids': sorted(r['id'] for r in matched),
            'preserved_state': {name: exhaustion.digest(getattr(problem, name, [])) for name in
                ('findings', 'execution_history', 'route_scout_history', 'local_verification_modules')},
            'self_report_not_scientific_verdict': True, 'automatic_resume_authorized': False}


def commit(problem, raw, meta):
    receipt = receipt_for(problem, raw, meta)
    problem.operational_handoff_pending = True
    path = Path(problem.folder) / FILE
    import pilot_handoff_resolution as resolution
    values = resolution.records(problem.pilot.root, problem.pilot.config) if hasattr(problem, 'pilot') and getattr(problem.pilot, 'config', {}).get('continuation_checkpoint') else []
    if path.is_file() and resolution.covers(values, getattr(problem, 'ident', None), receipt=json.loads(exhaustion.regular_bytes(path))):
        path = Path(problem.folder) / ('operational-handoff-' + meta['name'].split('/')[-1] + '.json')
    if path.is_symlink():
        raise ValueError('operational handoff receipt cannot be a symlink')
    if path.exists():
        if json.loads(exhaustion.regular_bytes(path)) != receipt:
            raise ValueError('operational handoff receipt or preserved state changed')
    else:
        # A crash during an exclusive write leaves a fail-closed invalid receipt,
        # never authority to dispatch another call. Never overwrite an old receipt.
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'w') as stream:
            json.dump(receipt, stream, ensure_ascii=False, indent=2)
            stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    raise OperationalHandoff(receipt)


def guard(problem):
    """No automatic reentry. Recover only a latest completed, valid original-main request."""
    if not hasattr(problem, 'folder'):
        if getattr(problem, 'operational_handoff_pending', False):
            raise ValueError('pending handoff has no problem store')
        return  # Lightweight legacy callers cannot carry a persisted handoff.
    import pilot_handoff_resolution as resolution
    try:
        values = resolution.records(problem.pilot.root, problem.pilot.config) if hasattr(problem, 'pilot') and getattr(problem.pilot, 'config', {}).get('continuation_checkpoint') else []
    except Exception:
        problem.operational_handoff_pending = True
        raise
    paths = [Path(problem.folder) / FILE, *Path(problem.folder).glob('operational-handoff-*.json')]
    for path in paths:
        if not (path.exists() or path.is_symlink()):
            continue
        problem.operational_handoff_pending = True
        saved = json.loads(exhaustion.regular_bytes(path))
        if resolution.covers(values, getattr(problem, 'ident', None), receipt=saved):
            problem.operational_handoff_pending = False
            continue
        problem.operational_handoff_pending = True
        calls = getattr(problem, 'calls', [])
        if not calls or saved.get('source_stage') != calls[-1].get('name'):
            raise ValueError('pending handoff source is missing or later call history exists')
        return commit(problem, saved.get('request'), calls[-1])
    calls = getattr(problem, 'calls', [])
    if not calls or calls[-1].get('status') != 'completed' or not calls[-1].get('module', '').startswith('main'):
        return
    meta = calls[-1]
    if resolution.covers(values, getattr(problem, 'ident', None), stage=meta.get('name')):
        problem.operational_handoff_pending = False
        return
    name = meta.get('name', '').split('/')[-1]
    if not re.fullmatch(r'[0-9]+-main[-a-z]*', name):
        return
    # Either copy can reveal a handoff, but only authenticated transport can
    # establish its request. Ordinary calls acquire no new acceptance checks.
    response_path = Path(problem.folder) / (name + '.json')
    copied = json.loads(exhaustion.regular_bytes(response_path)) if response_path.is_file() else None
    transported = None
    cap = meta.get('document_capability')
    if isinstance(cap, dict) and isinstance(cap.get('path'), str):
        text_path = Path(cap['path']).parent / 'stage.answer.txt'
        if text_path.is_file():
            transported, _, _ = extract_answer(exhaustion.regular_bytes(text_path).decode())
    if not any(isinstance(v, dict) and v.get('response_type') == KIND for v in (copied, transported)):
        return
    # A potentially pending request must never fall through to paper/dispatch
    # if transport authentication or the campaign copy is inconsistent.
    problem.operational_handoff_pending = True
    raw, _ = bound_answer(problem, meta)
    if copied is not None and copied != raw:
        raise ValueError('handoff campaign copy differs from authenticated transport')
    invalid = Path(problem.folder) / ('main-' + str(int(name.split('-')[0])) + '-invalid-contract.json')
    if invalid.is_file() and json.loads(exhaustion.regular_bytes(invalid)).get('raw_response') == raw:
        problem.operational_handoff_pending = False
        return  # Existing structural correction bound, not accepted handoff authority.
    return commit(problem, raw, meta)
