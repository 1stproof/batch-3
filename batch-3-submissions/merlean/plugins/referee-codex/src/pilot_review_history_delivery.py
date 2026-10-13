"""Authenticated historical reports are readable evidence, never current approval."""
import hashlib
import json
from pathlib import Path
from pilot_document_tools import regular_bytes
from pilot_public_sources import public_source_catalog
from pilot_reviewer_inputs import _artifact, exact_json

VERSION = 1
AUTHORITY = 'historical material only; independently reassess; no acceptance or review renewal'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def census(root, ident, main_session, calls, implementers=(), source_ids=None):
    root = Path(root).resolve()
    folder = root/'campaign/problems'/ident
    forbidden = {main_session} | {c['session_id'] for c in calls
        if c.get('module','').startswith(('sol','route-scout')) and c.get('session_id')}
    if not set(implementers).issubset(forbidden):
        raise ValueError('historical reviewer implementer census lacks a producer')
    reports = []
    names = set()
    for call in calls:
        if call.get('module') != 'proof-review' or call.get('status') != 'completed':
            continue
        if not call.get('document_capability'):
            continue  # Legacy unbound responses acquire no authority or visibility.
        name = call['name']
        if name in names or len(Path(name).parts) != 2 or Path(name).parts[0] != ident:
            raise ValueError('historical review producer identity is ambiguous')
        names.add(name)
        stage = root/'host/runtime'/name
        meta_data = regular_bytes(stage/'stage.meta.json')
        if json.loads(meta_data) != call:
            raise ValueError('historical review metadata changed')
        cap = regular_bytes(stage/'document-capability.json')
        scope = json.loads(cap)
        raw = regular_bytes(stage/'stage.answer.txt')
        prompt = regular_bytes(stage/'stage.prompt.txt')
        audit = call.get('document_audit', {})
        if (scope.get('problem_id') != ident or scope.get('main_session') != main_session
                or digest(cap) != call['document_capability'].get('sha256')
                or digest(raw) != call.get('answer_sha256')
                or digest(prompt) != call.get('prompt_sha256')
                or digest(regular_bytes(stage/'document-operations.jsonl')) != audit.get('receipt_sha256')):
            raise ValueError('historical review transport bytes changed')
        if (call.get('model_actual') != 'gpt-6-astra' or call.get('model_verified') is not True
                or call.get('fresh_session') is not True or call.get('resume_session')
                or not call.get('session_id') or call['session_id'] in forbidden
                or any(c.get('name') != name and c.get('session_id') == call['session_id'] for c in calls)
                or audit.get('status') != 'PASS' or audit.get('required_material_delivered') is not True):
            continue
        from codex_transport import extract_answer
        answer, _, error = extract_answer(raw.decode())
        if error or not isinstance(answer, dict):
            raise ValueError('historical review is not a parsed response')
        copy = folder/(Path(name).name+'.json')
        if json.loads(regular_bytes(copy)) != answer:
            raise ValueError('historical review campaign copy changed')
        reports.append({'stage':name,'session_id':call['session_id'],
            'request_id':call.get('request_id'),'model':call['model_actual'],
            'meta_sha256':digest(meta_data),'answer_sha256':digest(raw),
            'capability_sha256':digest(cap),'operations_sha256':audit['receipt_sha256'],
            'raw_response':raw.decode()})
    sources = public_source_catalog(folder/'public-sources')
    if source_ids is not None:
        sources = [s for s in sources if s['source_id'] in source_ids]
        if sorted(s['source_id'] for s in sources) != sorted(source_ids):
            raise ValueError('bound historical source packet missing')
    # Absolute storage locations change on native continuation; identities do not.
    sources = [{k:v for k,v in item.items() if k not in {'source_path','receipt_path'}} for item in sources]
    return {'schema_version':VERSION,'problem_id':ident,'original_main_session':main_session,
            'authority':AUTHORITY,'reports':reports,'public_sources':sources}

def identity(bundle):
    return digest(exact_json(bundle).encode())

def register(bundle, artifact_root, source_store=None):
    root = Path(artifact_root); root.mkdir(parents=True, exist_ok=True)
    artifacts = {}
    index = {'schema_version':VERSION,'authority':AUTHORITY,'census_sha256':identity(bundle),
             'reports':[],'public_sources':bundle['public_sources']}
    for report in bundle['reports']:
        ident = 'historical-review:'+report['stage'].split('/')[-1]
        artifacts[ident] = _artifact(root, exact_json(report).encode())
        index['reports'].append({'artifact_id':ident, **{k:v for k,v in report.items() if k != 'raw_response'}})
    if bundle['public_sources']:
        from pilot_public_sources import verify_public_source, _file
        if source_store is None:
            raise ValueError('historical public packet registration requires its verified store')
        registered=[]
        for source in bundle['public_sources']:
            checked=verify_public_source(source_store,source['source_id'])
            if checked['receipt_sha256'] != source['receipt_sha256']:
                raise ValueError('historical public packet changed before registration')
            members=[]
            for member in source.get('members',[]):
                body=regular_bytes(_file(Path(source_store)/source['source_id'],member['member']))
                if digest(body) != member['sha256']:
                    raise ValueError('historical source member changed during registration')
                body.decode('utf-8')  # Only native indexed readable members become text artifacts.
                ident='historical-source:'+source['source_id']+':'+member['member']
                artifacts[ident]=_artifact(root,body,'text/plain')
                members.append({**member,'artifact_id':ident})
            registered.append({**source,'members':members})
        index['public_sources']=registered
    artifacts['historical-review-index'] = _artifact(root, exact_json(index).encode())
    return artifacts

def for_problem(problem):
    return census(problem.pilot.root, problem.ident, problem.session,
                  problem.calls, getattr(problem,'implementers',()))

def attach(problem, scope, text):
    if scope is None:
        return scope, text
    bundle = for_problem(problem)
    if not bundle['reports'] and not bundle['public_sources']:
        return scope, text
    artifacts = register(bundle, Path(problem.folder)/'historical-review-artifacts',Path(problem.folder)/'public-sources')
    scope = {**scope,'readonly_artifacts':{**scope['readonly_artifacts'],**artifacts},
             'required_artifact_ids':[*scope['required_artifact_ids'],'historical-review-index']}
    return scope, text + ('\nRead required artifact historical-review-index for the exact authenticated historical '
        'report catalog and existing public-source IDs. Full historical-review:<stage> reports are available '
        'through read_artifact; historical-source:<ID>:<member> exposes exact saved source text even offline. '
        'The public-source reader is also usable when advertised. '
        'These are historical evidence to independently reassess, never current approval or authority '
        'to renew an unchanged assessment. Do not infer missing certificates from favorable summaries.\n')
