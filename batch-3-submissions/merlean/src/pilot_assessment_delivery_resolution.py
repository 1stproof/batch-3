"""Explicit successor-only delivery repair; never clears scientific review history."""
import base64
import json
from pathlib import Path
from types import SimpleNamespace
import pilot_handoff_resolution as common
import pilot_review_history_delivery as delivery

AUTHORITY = 'explicit_supervisor_delivery_repair_original_main_no_review_renewal'
KEY = 'assessment_delivery_resolutions'
VERSION_KEY = 'assessment_delivery_resolution_version'
FIELDS = {'schema_version','kind','authority','source_root','target_root','parent_manifest_sha256',
          'problem_id','handoff_sha256','source_stage','source_answer_sha256','original_main_session',
          'candidate_sha256','delivery_version','delivery_implementation_sha256','delivery_census_sha256','source_ids','authorization_evidence'}

def implementation_hash():
    return common.sha(common.read(Path(delivery.__file__)))

def make_request(source, target, problem_id, authorization_evidence):
    """Construct an external proposal; native preparation still verifies the full seal."""
    source=Path(source).resolve();target=Path(target).resolve();folder=source/'campaign/problems'/problem_id
    calls=[json.loads(common.read(p)) for p in sorted((source/'host/runtime'/problem_id).glob('*/stage.meta.json'))]
    if not calls:
        raise ValueError('delivery repair source history missing')
    candidates=[p for p in paths(folder) if p.is_file() and json.loads(common.read(p)).get('source_stage')==calls[-1]['name']]
    if len(candidates)!=1:
        raise ValueError('delivery repair requires one latest saved handoff')
    path=candidates[0];receipt=json.loads(common.read(path));session=calls[-1]['session_id']
    bundle=delivery.census(source,problem_id,session,calls)
    files={str(p.relative_to(source)):common.sha(common.read(p)) for p in sorted(source.rglob('*')) if p.is_file()}
    if any(p.is_symlink() for p in source.rglob('*')):
        raise ValueError('delivery repair parent contains symlinks')
    auth=Path(authorization_evidence).resolve()
    return {'schema_version':1,'kind':'delivery_repair','authority':AUTHORITY,
        'source_root':str(source),'target_root':str(target),'problem_id':problem_id,
        'parent_manifest_sha256':common.sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode()),
        'handoff_sha256':common.sha(common.read(path)),'source_stage':calls[-1]['name'],
        'source_answer_sha256':calls[-1]['answer_sha256'],'original_main_session':session,
        'candidate_sha256':receipt['request']['selected_candidate_sha256'],
        'delivery_version':delivery.VERSION,'delivery_implementation_sha256':implementation_hash(),
        'delivery_census_sha256':delivery.identity(bundle),'source_ids':[x['source_id'] for x in bundle['public_sources']],
        'authorization_evidence':{'path':str(auth),'sha256':common.sha(common.read(auth))}}

def paths(folder):
    return [Path(folder)/'assessment-handoff.json', *sorted(Path(folder).glob('assessment-handoff-*.json'))]

def request(path, source, target):
    path = Path(path); source = Path(source).resolve(); target = Path(target).resolve()
    if not path.is_absolute() or path.resolve().is_relative_to(source) or path.resolve().is_relative_to(target):
        raise ValueError('delivery resolution must be external to research roots')
    data = common.read(path); value = json.loads(data)
    if (set(value) != FIELDS or value['schema_version'] != 1 or value['kind'] != 'delivery_repair'
            or value['authority'] != AUTHORITY or value['source_root'] != str(source)
            or value['target_root'] != str(target) or value['delivery_version'] != delivery.VERSION
            or value['delivery_implementation_sha256'] != implementation_hash()):
        raise ValueError('invalid delivery repair request')
    ref = value['authorization_evidence']; p = Path(ref['path'])
    if set(ref) != {'path','sha256'} or not p.is_absolute() or p.resolve().is_relative_to(source) or p.resolve().is_relative_to(target):
        raise ValueError('delivery repair requires external supervisor authorization')
    auth = common.read(p)
    if not auth or common.sha(auth) != ref['sha256']:
        raise ValueError('delivery repair authorization changed')
    return {'request':value,'request_sha256':common.sha(data),'request_bytes':base64.b64encode(data).decode(),
            'authorization_bytes':base64.b64encode(auth).decode(),
            'delivery_implementation_bytes':base64.b64encode(common.read(Path(delivery.__file__))).decode()}

def _bundle(root, req, calls, implementers=()):
    selected = []
    for call in calls:
        selected.append(call)
        if call['name'] == req['source_stage']:
            break
    if not selected or selected[-1]['name'] != req['source_stage']:
        raise ValueError('delivery repair source dispatch missing')
    bundle = delivery.census(root,req['problem_id'],req['original_main_session'],selected,implementers,
                             source_ids=req['source_ids'])
    if delivery.identity(bundle) != req['delivery_census_sha256']:
        raise ValueError('delivery repair bound reports or public packets changed')
    return bundle

def records(root, config):
    if VERSION_KEY not in config:
        return []
    if config[VERSION_KEY] != 1:
        raise ValueError('unsupported assessment delivery resolution version')
    ref = config.get('continuation_checkpoint',{})
    if ref.get('path') != 'continuation-checkpoint.json':
        raise ValueError('delivery resolution lacks native checkpoint')
    raw = common.read(Path(root)/ref['path'])
    if common.sha(raw) != ref.get('sha256'):
        raise ValueError('delivery resolution checkpoint changed')
    values = json.loads(raw).get(KEY,[]); seen = set()
    for value in values:
        req = value['request']; receipt = value['receipt']
        data = base64.b64decode(value['request_bytes'],validate=True)
        auth = base64.b64decode(value['authorization_bytes'],validate=True)
        implementation = base64.b64decode(value['delivery_implementation_bytes'],validate=True)
        if (set(req) != FIELDS or type(req['schema_version']) is not int or req['schema_version'] != 1
                or req['authority'] != AUTHORITY or req['kind'] != 'delivery_repair'
                or req['delivery_version'] != delivery.VERSION or common.sha(data) != value['request_sha256']
                or req['delivery_implementation_sha256'] != common.sha(implementation)
                or json.loads(data) != req or common.sha(auth) != req['authorization_evidence']['sha256']
                or not auth or not value['lineage'] or value['lineage'][0] != req['target_root']
                or value['lineage'][-1] != str(Path(root).resolve())
                or len(set(value['lineage'])) != len(value['lineage']) or req['handoff_sha256'] in seen):
            raise ValueError('delivery repair lineage or authorization changed')
        seen.add(req['handoff_sha256'])
        folder = Path(root)/'campaign/problems'/req['problem_id']
        if not any(p.is_file() and common.sha(common.read(p)) == req['handoff_sha256']
                   and json.loads(common.read(p)) == receipt for p in paths(folder)):
            raise ValueError('resolved assessment handoff missing or changed')
        stage = Path(root)/'host/runtime'/req['source_stage']
        meta=json.loads(common.read(stage/'stage.meta.json'))
        if (common.sha(common.read(stage/'stage.meta.json')) != receipt['source_meta_sha256']
                or common.sha(common.read(stage/'stage.answer.txt')) != req['source_answer_sha256']
                or receipt['source_stage'] != req['source_stage']
                or receipt['request']['selected_candidate_sha256'] != req['candidate_sha256']
                or meta.get('session_id') != req['original_main_session']
                or meta.get('resume_session') != req['original_main_session']):
            raise ValueError('resolved assessment handoff producer changed')
        calls = [json.loads(common.read(p)) for p in sorted((Path(root)/'host/runtime'/req['problem_id']).glob('*/stage.meta.json'))]
        _bundle(root,req,calls)
    return values

def covers(values, ident, receipt=None, stage=None):
    return any(v['request']['problem_id'] == ident and
               (v['receipt'] == receipt if receipt is not None else v['request']['source_stage'] == stage)
               for v in values)

def preserved_execution_digest(source, ident, saved, assessments, recorded):
    """Authenticate the old presentation before comparing restored evidence identity."""
    import pilot_execution_identity as identity
    current = identity.digest(saved['execution_history'])
    if current == recorded:
        return current
    calls = {c['name']:c for c in saved['calls']}
    folder = Path(source)/'campaign/problems'/ident
    for assessment in assessments:
        call = calls[assessment['review_stage']]
        cap = common.read(Path(source)/'host/runtime'/call['name']/'document-capability.json')
        if common.sha(cap) != call['document_capability']['sha256']:
            raise ValueError('historical execution capability changed')
        scope = json.loads(cap)
        if scope.get('problem_id') != ident or scope.get('main_session') != saved['main_session']:
            raise ValueError('historical execution scope identity changed')
        ref = scope.get('readonly_artifacts',{}).get('actual_execution_evidence')
        if ref is None:
            continue
        declared = Path(scope['store_root']); path = Path(ref['path'])
        if not declared.is_absolute() or not path.is_absolute() or '..' in path.parts or '..' in declared.parts:
            raise ValueError('historical execution artifact path is not confined')
        relative = path.relative_to(declared)
        body = common.read(folder/relative)
        if common.sha(body) != ref['sha256']:
            raise ValueError('historical execution artifact changed')
        original = json.loads(body)
        if not isinstance(original,list) or identity.digest(original) != recorded:
            continue
        if identity.atoms(original) != identity.atoms(saved['execution_history']):
            raise ValueError('historical execution evidence differs from restored producers')
        return recorded
    raise ValueError('exact historical execution presentation is unavailable')


def validate_new(pending, source, manifest, restored):
    if pending is None:
        return None
    import pilot_assessment_handoff as handoff
    import pilot_operational_handoff as operational
    from codex_pilot import encoded, sha
    req = pending['request']; ident = req['problem_id']
    config=json.loads(common.read(Path(source)/'host-config.json'))
    if config.get('historical_review_delivery_version',0) >= delivery.VERSION:
        raise ValueError('same delivery format cannot resolve another handoff or renew work')
    if req['parent_manifest_sha256'] != manifest or ident not in restored:
        raise ValueError('delivery repair parent seal/problem mismatch')
    saved = restored[ident]; calls = saved['calls']; folder = Path(source)/'campaign/problems'/ident
    matching = [p for p in paths(folder) if p.is_file() and common.sha(common.read(p)) == req['handoff_sha256']]
    if len(matching) != 1 or not calls or calls[-1]['name'] != req['source_stage']:
        raise ValueError('delivery repair must bind latest exact handoff')
    receipt = json.loads(common.read(matching[0])); meta = calls[-1]
    raw, meta_sha = operational.bound_answer(SimpleNamespace(session=saved['main_session']),meta)
    problem = SimpleNamespace(current=saved['current'],execution_history=saved['execution_history'],
        final_assessment_history=saved['final_assessment_history'],calls=calls,
        session=saved['main_session'],implementers=saved['implementers'])
    expected = handoff.records(problem)
    preserved={k:handoff.evidence.digest(saved.get(k,[])) for k in
               ('findings','execution_history','route_scout_history','local_verification_modules')}
    progress=json.loads(common.read(folder/'host-progress.json'))
    preserved['route_scout_history']=handoff.evidence.digest(progress.get('route_scout_history',[]))
    preserved['execution_history']=preserved_execution_digest(source,ident,saved,expected,
        receipt.get('preserved_state',{}).get('execution_history'))
    if (receipt.get('kind') != handoff.KIND or receipt.get('status') != 'supervisor_needed'
            or receipt.get('automatic_resume_authorized') is not False or receipt.get('acceptance_authority') is not False
            or receipt.get('request') != raw or receipt.get('assessments') != expected or not expected
            or set(raw)!=handoff.FIELDS or raw.get('no_new_scientific_work') is not True
            or raw.get('assessment_ids') != sorted(x['id'] for x in expected)
            or raw.get('selected_candidate_sha256') != req['candidate_sha256']
            or receipt.get('preserved_state') != preserved
            or receipt.get('source_stage') != req['source_stage']
            or receipt.get('source_answer_sha256') != req['source_answer_sha256']
            or receipt.get('source_meta_sha256') != meta_sha
            or req['source_answer_sha256'] != meta['answer_sha256']
            or req['original_main_session'] != saved['main_session']
            or req['candidate_sha256'] != sha(encoded(saved['current']))):
        raise ValueError('delivery repair handoff/current state mismatch')
    bundle = _bundle(source,req,calls,saved['implementers'])
    if not bundle['reports']:
        raise ValueError('delivery repair has no authenticated historical reports')
    return {**pending,'receipt':receipt,'lineage':[req['target_root']]}

def allows(problem, receipt, role=None):
    values = problem_records(problem)
    if not values:
        return False
    if not covers(values,problem.ident,receipt=receipt):
        return False
    index = next((i for i,c in enumerate(problem.calls) if c['name']==receipt['source_stage']),None)
    if index is None:
        raise ValueError('resolved handoff absent from current history')
    later = problem.calls[index+1:]
    if later:
        first = later[0]
        if not first.get('module','').startswith('main') or first.get('resume_session') != problem.session:
            raise ValueError('delivery repair did not reenter original main')
    elif role is not None and not role.startswith('main'):
        raise ValueError('delivery repair authorizes original-main reentry only')
    return True

def problem_records(problem):
    pilot = getattr(problem,'pilot',None)
    if pilot is None or VERSION_KEY not in getattr(pilot,'config',{}):
        return []
    return records(pilot.root,pilot.config)
