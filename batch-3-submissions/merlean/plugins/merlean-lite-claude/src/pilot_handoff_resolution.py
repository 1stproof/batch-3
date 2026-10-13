"""Explicit supervisor continuation of one saved handoff; never review renewal."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import base64
import json
import pilot_review_exhaustion as exhaustion

AUTHORITY = 'explicit_supervisor_resume_original_main_no_review_renewal'
FIELDS = {'schema_version','authority','source_root','target_root','parent_manifest_sha256','problem_id',
          'handoff_sha256','source_stage','source_answer_sha256','original_main_session','candidate_sha256',
          'proof_document','exhaustion_ids','authorization_evidence'}

def read(path):
    return exhaustion.regular_bytes(Path(path))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def request(path, source, target):
    if path is None:
        return None
    path = Path(path)
    if not path.is_absolute() or path.resolve().is_relative_to(Path(source).resolve()) or path.resolve().is_relative_to(Path(target).resolve()):
        raise ValueError('handoff resolution must be explicitly supplied outside research roots')
    request_data = read(path)
    value = json.loads(request_data)
    if (not isinstance(value, dict) or set(value) != FIELDS or type(value['schema_version']) is not int or value['schema_version'] != 1
            or value['authority'] != AUTHORITY or value['source_root'] != str(Path(source).resolve())
            or value['target_root'] != str(Path(target).resolve())):
        raise ValueError('invalid explicit handoff resolution or fixed successor')
    ref = value['authorization_evidence']
    if not isinstance(ref, dict) or set(ref) != {'path','sha256'} or not isinstance(ref['path'], str):
        raise ValueError('external supervisor authorization evidence required')
    evidence_path = Path(ref['path'])
    if (not evidence_path.is_absolute() or evidence_path.resolve().is_relative_to(Path(source).resolve())
            or evidence_path.resolve().is_relative_to(Path(target).resolve())):
        raise ValueError('authorization evidence cannot be model-owned campaign content')
    data = read(evidence_path)
    if not data or sha(data) != ref['sha256']:
        raise ValueError('supervisor authorization evidence changed')
    return {'request': value, 'request_sha256': sha(request_data), 'authorization_sha256': sha(data),
            'request_bytes': base64.b64encode(request_data).decode(),
            'authorization_bytes': base64.b64encode(data).decode()}

def records(root, config):
    """Only host-frozen continuation checkpoint confers resolution provenance."""
    if 'operational_handoff_resolution_version' not in config:
        return []  # Legacy continuations acquire no unrelated file/path obligations.
    if type(config['operational_handoff_resolution_version']) is not int or config['operational_handoff_resolution_version'] != 1:
        raise ValueError('unsupported handoff resolution version')
    ref = config.get('continuation_checkpoint')
    if not ref:
        raise ValueError('handoff resolution lacks frozen checkpoint')
    if ref.get('path') != 'continuation-checkpoint.json':
        raise ValueError('invalid handoff resolution checkpoint path')
    data = read(Path(root)/ref['path'])
    if sha(data) != ref.get('sha256'):
        raise ValueError('handoff resolution checkpoint changed')
    values = json.loads(data).get('operational_handoff_resolutions', [])
    if not isinstance(values, list):
        raise ValueError('invalid handoff resolution lineage')
    seen = set()
    for value in values:
        if not isinstance(value, dict) or set(value) != {'request','request_sha256','authorization_sha256','request_bytes','authorization_bytes','receipt','lineage'}:
            raise ValueError('invalid handoff resolution record')
        req, receipt, lineage = value['request'], value['receipt'], value['lineage']
        try:
            request_data = base64.b64decode(value['request_bytes'], validate=True)
            authorization_data = base64.b64decode(value['authorization_bytes'], validate=True)
        except (ValueError, TypeError) as error:
            raise ValueError('invalid preserved resolution evidence') from error
        if (sha(request_data) != value['request_sha256'] or json.loads(request_data) != req
                or sha(authorization_data) != value['authorization_sha256']
                or req.get('authorization_evidence', {}).get('sha256') != value['authorization_sha256']):
            raise ValueError('preserved resolution authorization changed')
        if (not isinstance(req, dict) or set(req) != FIELDS or type(req['schema_version']) is not int or req['schema_version'] != 1 or req['authority'] != AUTHORITY
                or not isinstance(lineage, list) or not lineage or lineage[0] != req['target_root']
                or lineage[-1] != str(Path(root).resolve()) or len(set(lineage)) != len(lineage)
                or not isinstance(receipt, dict) or req['source_stage'] != receipt.get('source_stage')
                or req['source_answer_sha256'] != receipt.get('source_answer_sha256')
                or req['original_main_session'] != receipt.get('source_session')
                or req['candidate_sha256'] != receipt.get('candidate_sha256')
                or req['proof_document'] != receipt.get('proof_document')
                or req['exhaustion_ids'] != receipt.get('exhaustion_ids')
                or req['handoff_sha256'] in seen):
            raise ValueError('inconsistent handoff resolution lineage')
        seen.add(req['handoff_sha256'])
        folder = Path(root)/'campaign/problems'/req['problem_id']
        candidates = [folder/'operational-handoff.json', *folder.glob('operational-handoff-*.json')]
        if not any(p.is_file() and sha(read(p)) == req['handoff_sha256'] and json.loads(read(p)) == receipt for p in candidates):
            raise ValueError('resolved historical handoff receipt missing or changed')
        stage = Path(root)/'host/runtime'/req['source_stage']
        if (sha(read(stage/'stage.meta.json')) != receipt.get('source_meta_sha256')
                or sha(read(stage/'stage.answer.txt')) != req['source_answer_sha256']):
            raise ValueError('resolved historical handoff transport changed')
    return values

def covers(values, ident, receipt=None, stage=None):
    return any(v['request']['problem_id'] == ident and
        (v['receipt'] == receipt if receipt is not None else v['request']['source_stage'] == stage)
        for v in values)

def validate_new(pending, source, manifest, restored):
    if pending is None:
        return None
    import pilot_operational_handoff as handoff
    from pilot_candidate_contract import candidate_hash
    req = pending['request']; ident = req['problem_id']
    if req['parent_manifest_sha256'] != manifest or ident not in restored:
        raise ValueError('handoff resolution source seal/problem mismatch')
    saved = restored[ident]; folder = Path(source)/'campaign/problems'/ident
    paths = [folder/'operational-handoff.json', *folder.glob('operational-handoff-*.json')]
    paths = [p for p in paths if p.is_file() and sha(read(p)) == req['handoff_sha256']]
    if len(paths) != 1:
        raise ValueError('handoff resolution requires exact saved receipt')
    receipt = json.loads(read(paths[0])); calls = saved['calls']
    if not calls or calls[-1]['name'] != req['source_stage']:
        raise ValueError('resolution must bind latest completed original-main handoff')
    meta = calls[-1]
    raw, meta_sha = handoff.bound_answer(SimpleNamespace(session=saved['main_session']), meta)
    derived = exhaustion.derive(calls)
    matches = [r for r in derived if r['binding']['scientific'] == exhaustion.projection(saved['current'])]
    handoff.validate_request(SimpleNamespace(current=saved['current'], documents_enabled=lambda: True,
        document_current=lambda: {**saved['proof_document'], 'proof_markdown': saved['current']['proof_markdown']},
        active_stages=set()), raw, derived)
    progress = json.loads(read(folder/'host-progress.json'))
    expected_state = {k: exhaustion.digest(saved.get(k, [])) for k in
                      ('execution_history','local_verification_modules')}
    expected_state['route_scout_history'] = exhaustion.digest(progress.get('route_scout_history', []))
    expected_state['findings'] = exhaustion.digest(progress.get('open_findings', []))
    if (receipt.get('authority') != handoff.AUTHORITY or receipt.get('status') != 'supervisor_needed'
            or receipt.get('automatic_resume_authorized') is not False or receipt.get('self_report_not_scientific_verdict') is not True
            or receipt.get('request') != raw or raw.get('response_type') != handoff.KIND
            or receipt.get('source_meta_sha256') != meta_sha
            or receipt.get('source_answer_sha256') != meta.get('answer_sha256')
            or receipt.get('source_session') != saved['main_session']
            or receipt.get('candidate_sha256') != candidate_hash(saved['current'])
            or receipt.get('proof_document') != saved['proof_document']
            or receipt.get('preserved_state') != expected_state
            or receipt.get('exhaustion_ids') != sorted(r['id'] for r in matches)
            or not matches or any(r.get('required_material_delivered') is not True for r in matches)
            or any(exhaustion.moment(meta['start_utc']) <= exhaustion.moment(r['end_utc']) for r in matches)
            or req['source_stage'] != receipt.get('source_stage')
            or req['source_answer_sha256'] != receipt.get('source_answer_sha256')
            or req['original_main_session'] != receipt.get('source_session')
            or req['candidate_sha256'] != receipt.get('candidate_sha256')
            or req['proof_document'] != receipt.get('proof_document')
            or req['exhaustion_ids'] != receipt.get('exhaustion_ids')):
        raise ValueError('handoff resolution does not bind authenticated preserved state')
    return {**pending, 'receipt': receipt, 'lineage': [req['target_root']]}
