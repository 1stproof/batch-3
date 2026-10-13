"""Explicit one-admission repair of a completed, unaccepted reconstruction.

Only delivery identity and exact saved bytes are checked here. The draft is not
accepted mathematics; normal reconstruction, readers and release gates still run.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from datetime import datetime

from codex_transport import extract_answer


class DeliveryRecoveryRequired(RuntimeError):
    """Missing delivery needs an exact explicit recovery, never a blind retry."""


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def regular(path, root):
    path, root = Path(path), Path(root).resolve()
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
        raise ValueError('delivery evidence is not a confined regular file')
    return path


def binding(root, problem, name, *, origin=None):
    """Bind only the observed failure shape; never infer an accepted writer."""
    root = Path(root).resolve()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', problem) or not re.fullmatch(re.escape(problem)+r'/paper-\d+-reconstruct', name):
        raise ValueError('delivery remediation is limited to one exact reconstruction')
    folder = root/'exam/papers'/problem
    stage = root/'host/runtime'/name
    ledger = read(regular(folder/'paper-ledger.json', root))
    paths = {key: regular(stage/file, root) for key,file in (
        ('meta','stage.meta.json'),('raw_answer','stage.answer.txt'),
        ('parsed_answer','stage.answer.json'),('prompt','stage.prompt.txt'),
        ('capability','document-capability.json'))}
    meta, capability = read(paths['meta']), read(paths['capability'])
    records=[call for call in ledger.get('calls',[]) if call.get('name')==name]
    if (len(records)!=1 or any(records[0].get(key)!=meta.get(key) for key in ('status','session_id','answer_sha256'))):
        raise ValueError('rejected response differs from preserved paper ledger')
    try:
        start,end=datetime.fromisoformat(meta['start_utc']),datetime.fromisoformat(meta['end_utc'])
        terminal=start.tzinfo is not None and end.tzinfo is not None and end>=start and type(meta.get('pid')) is int and meta['pid']>1 and type(meta.get('exit_code')) is int
    except (KeyError,TypeError,ValueError):terminal=False
    session = meta.get('session_id')
    audit = meta.get('document_audit', {})
    if (meta.get('name') != name or meta.get('module') != 'paper-reconstruct'
            or not terminal or meta.get('status') != 'completed' or meta.get('turn_completed') is not True
            or meta.get('model_actual') != 'gpt-6-astra' or meta.get('model_verified') is not True
            or not session or meta.get('resume_session') != session
            or session not in ledger.get('writer_ids', [])
            or audit.get('status') != 'PASS' or audit.get('required_material_delivered') is not False
            or audit.get('complete_tool_outputs_delivered') is not True
            or any(audit.get(key) for key in ('errors','delivery_errors'))
            or digest(paths['raw_answer']) != meta.get('answer_sha256')
            or digest(paths['prompt']) != meta.get('prompt_sha256')
            or digest(paths['capability']) != meta.get('document_capability', {}).get('sha256')):
        raise ValueError('not an authenticated same-writer completed delivery-only rejection')
    answer, _, error = extract_answer(paths['raw_answer'].read_text())
    if (error or not isinstance(answer, dict) or not isinstance(answer.get('tex'), str)
            or read(paths['parsed_answer']) != answer):
        raise ValueError('completed reconstruction lacks its exact structured unaccepted draft')
    if (capability.get('mode') != 'review' or capability.get('problem_id') != problem
            or capability.get('producer')!={'stage':name,'request_id':meta.get('request_id'),'session_id':session}):
        raise ValueError('original paper capability identity changed')
    if capability.get('original_sha256') != digest(regular(folder/'snapshot/input.txt',folder)):
        raise ValueError('paper capability original question changed')
    original_folder = Path(origin or root)/'exam/papers'/problem
    artifacts = capability.get('readonly_artifacts', {})
    required = capability.get('required_artifact_ids', [])
    if not required or 'stage-input' not in required or len(required) != len(set(required)) or not set(required).issubset(artifacts):
        raise ValueError('original mandatory artifact set is invalid')
    coverage=audit.get('required_artifact_coverage',{})
    if set(coverage)!=set(required) or any(type(value) is not bool for value in coverage.values()) or all(coverage.values()):
        raise ValueError('missing delivery census differs from original mandatory scope')
    mapped = {}
    for ident, ref in artifacts.items():
        declared = Path(ref['path'])
        if not declared.is_absolute() or not declared.is_relative_to(original_folder):
            raise ValueError('original artifact escapes paper storage')
        path = regular(folder/declared.relative_to(original_folder), folder)
        if digest(path) != ref['sha256']:
            raise ValueError('original delivery artifact changed')
        mapped[ident] = {**ref, 'path': str(path)}
    manifest = regular(folder/'snapshot/manifest.json', folder)
    original_progress=ledger.get('retrieval_progress')
    if original_progress is None:
        archived=[dict(item) for item in ledger.get('retrieval_history',[])
                  if item.get('stage')=='reconstruct' and item.get('session')==session
                  and any(a.get('name')==item.get('closed_by_delivery_remediation')
                          for a in ledger.get('delivery_remediation_admissions',[]))]
        if len(archived)!=1:raise ValueError('original consumed retrieval checkpoint is missing or ambiguous')
        original_progress=archived[0];original_progress.pop('closed_by_delivery_remediation')
    if (original_progress.get('stage')!='reconstruct' or original_progress.get('session')!=session
            or original_progress.get('writer') is not True
            or type(original_progress.get('turns')) is not int or not 1<=original_progress['turns']<=4):
        raise ValueError('original consumed retrieval checkpoint is invalid')
    prefix=ledger['calls'][:ledger['calls'].index(records[0])+1]
    history_hash=hashlib.sha256(json.dumps(prefix,sort_keys=True).encode()).hexdigest()
    result = {'problem':problem, 'stage':name, 'session_id':session,
        'files':{key:digest(path) for key,path in paths.items()},
        'snapshot_manifest_sha256':digest(manifest),'retrieval_progress':original_progress,
        'call_history_sha256':history_hash,'call_history_count':len(prefix),
        'required_artifacts':{ident:artifacts[ident]['sha256'] for ident in required}}
    return result, ledger, meta, answer, capability, mapped


def make_request(source, problem, stage, parent_manifest_sha256, *, authority):
    value, ledger, _, _, _, _ = binding(source, problem, stage)
    if (ledger.get('stage') != 'reconstruct' or ledger.get('completed')
            or ledger.get('writer_session') or ledger.get('delivery_remediation_admissions')
            or not ledger.get('calls') or ledger['calls'][-1].get('name') != stage):
        raise ValueError('delivery remediation requires the untouched rejected reconstruction checkpoint')
    if not isinstance(authority,str) or not authority.strip() or not re.fullmatch(r'[0-9a-f]{64}',parent_manifest_sha256):
        raise ValueError('explicit delivery authority and exact parent manifest are required')
    return {'schema_version':1,'kind':'paper-delivery-remediation','source_root':str(Path(source).resolve()),
        'parent_manifest_sha256':parent_manifest_sha256,'authority':authority,'maximum_admissions':1,'binding':value}


def validate_request(request, source, parent):
    if (not isinstance(request,dict) or type(request.get('schema_version')) is not int
            or type(request.get('maximum_admissions')) is not int):
        raise ValueError('delivery authorization must be an exact bounded object')
    value=request.get('binding',{})
    expected=make_request(source,value.get('problem',''),value.get('stage',''),
        parent['manifest_sha256'],authority=request.get('authority'))
    if request != expected or request['source_root'] != parent['source_root']:
        raise ValueError('delivery authorization differs from exact stopped parent and rejected response')
    return request


def load_request(root, config):
    ref=config.get('paper_delivery_remediation')
    if ref is None:return None
    if not isinstance(ref,dict) or ref.get('path') != 'paper-delivery-remediation.json':
        raise ValueError('invalid delivery authorization reference')
    path=regular(Path(root)/ref['path'], root)
    if digest(path) != ref.get('sha256'):raise ValueError('delivery authorization changed')
    request=read(path)
    if (request.get('schema_version')!=1 or request.get('kind')!='paper-delivery-remediation'
            or type(request.get('maximum_admissions')) is not int or request.get('maximum_admissions')!=1
            or not isinstance(request.get('binding'),dict)):
        raise ValueError('invalid bounded delivery authorization')
    return request


def prepare(engine, request):
    root=engine.problem.pilot.root
    expected=request['binding']
    value, ledger, meta, answer, capability, mapped = binding(root,engine.problem.ident,expected['stage'],origin=request['source_root'])
    if value != expected or engine.ledger['stage'] != 'reconstruct':
        raise DeliveryRecoveryRequired('saved delivery bindings differ; no fallback or new writer')
    # Preserve raw and parsed bytes as unaccepted data, never as paper.tex.
    directory=engine.root/'unaccepted-reconstruction';directory.mkdir(exist_ok=True)
    raw=Path(root)/'host/runtime'/expected['stage']/'stage.answer.txt'
    draft=directory/'draft.json'
    if draft.exists() and draft.read_bytes()!=raw.read_bytes():
        raise DeliveryRecoveryRequired('quarantined draft changed')
    if not draft.exists():draft.write_bytes(raw.read_bytes())
    engine.ledger['unaccepted_reconstruction']={'status':'UNACCEPTED','binding':expected,
        'draft_sha256':digest(draft),'path':str(draft),'acceptance_authority':False}
    engine.save()
    if 'unaccepted-draft' in mapped:
        raise DeliveryRecoveryRequired('original scope collides with quarantine artifact')
    scope={k:v for k,v in capability.items() if k not in ('producer','receipt_path')}
    scope.update(store_root=str(engine.root.resolve()),main_session=expected['session_id'],
        readonly_artifacts={**mapped,'unaccepted-draft':{'path':str(draft),'sha256':digest(draft),'media_type':'application/json'}},
        required_artifact_ids=[*capability['required_artifact_ids'],'unaccepted-draft'],inline_artifact_ids=[])
    return scope


def scope_binding(scope):
    value={key:scope.get(key) for key in ('mode','problem_id','original_sha256','main_session',
                                         'required_artifact_ids','inline_artifact_ids')}
    value['readonly_artifacts']={ident:{key:ref.get(key) for key in ('sha256','media_type')}
                                 for ident,ref in scope['readonly_artifacts'].items()}
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()


def reconcile_completed(engine, request, scope, admission):
    """Consume exact completed corrective work after a crash; never redispatch."""
    if admission.get('original_retrieval_progress')!=request['binding']['retrieval_progress']:
        raise DeliveryRecoveryRequired('consumed original retrieval checkpoint changed')
    stage=engine.problem.pilot.host/'runtime'/admission['name']
    if not (stage/'stage.meta.json').is_file():
        raise DeliveryRecoveryRequired('delivery admission has no terminal response; explicit process reconciliation required')
    meta=read(stage/'stage.meta.json')
    audit=meta.get('document_audit',{})
    if (meta.get('name')!=admission['name'] or meta.get('module')!='paper-reconstruct'
            or meta.get('status')!='completed' or meta.get('turn_completed') is not True
            or meta.get('model_actual')!='gpt-6-astra' or meta.get('model_verified') is not True
            or meta.get('session_id')!=request['binding']['session_id']
            or meta.get('resume_session')!=request['binding']['session_id']
            or audit.get('status')!='PASS' or audit.get('required_material_delivered') is not True
            or audit.get('complete_tool_outputs_delivered') is not True
            or any(audit.get(key) for key in ('errors','delivery_errors'))
            or digest(stage/'stage.prompt.txt')!=meta.get('prompt_sha256')
            or meta.get('prompt_sha256')!=admission.get('prompt_sha256')
            or digest(stage/'stage.answer.txt')!=meta.get('answer_sha256')
            or digest(stage/'document-capability.json')!=meta.get('document_capability',{}).get('sha256')):
        raise DeliveryRecoveryRequired('single delivery admission did not return an exact accepted-delivery response')
    actual=read(stage/'document-capability.json')
    if (scope_binding(actual)!=admission.get('scope_sha256') or scope_binding(scope)!=admission.get('scope_sha256')
            or actual.get('producer')!={'stage':admission['name'],'request_id':meta.get('request_id'),
                                        'session_id':request['binding']['session_id']}
            or audit.get('required_artifact_coverage')!={ident:True for ident in scope['required_artifact_ids']}):
        raise DeliveryRecoveryRequired('corrective delivery scope or producer changed')
    answer,_,error=extract_answer((stage/'stage.answer.txt').read_text())
    if error or not isinstance(answer,dict) or read(stage/'stage.answer.json')!=answer:
        raise DeliveryRecoveryRequired('completed corrective response is not exactly bound')
    validate_application(engine, answer, admission)
    records=[c for c in engine.ledger['calls'] if c['name']==admission['name']]
    if len(records)!=1:raise DeliveryRecoveryRequired('corrective admission identity is ambiguous')
    if records[0].get('status') not in ('admitted','completed'):
        raise DeliveryRecoveryRequired('corrective admission has incompatible terminal history')
    if records[0].get('status')=='completed' and any(records[0].get(key)!=meta.get(key) for key in ('session_id','answer_sha256','prompt_sha256')):
        raise DeliveryRecoveryRequired('completed corrective ledger changed')
    records[0].clear();records[0].update(meta)
    admission.update(status='completed-reconciled',answer_sha256=meta['answer_sha256'])
    engine.save()
    return meta['session_id'],answer


def validate_application(engine, answer, admission):
    # An interrupted application may only contain the before-state or exact new bytes.
    if not isinstance(answer.get('artifacts',{}),dict):
        raise DeliveryRecoveryRequired('corrective author artifacts are malformed')
    values={'paper.tex':answer.get('tex'),'raw-source.tex':answer.get('tex'),
        'work/evidence_assessment.md':answer.get('evidence_assessment'),
        'work/reconstruction_map.md':answer.get('reconstruction_map'),
        **{'work/'+name:value for name,value in answer.get('artifacts',{}).items()}}
    for name,before in admission['before_files'].items():
        path=engine.root/name
        current=digest(path) if path.is_file() else None
        value=values.get(name)
        data=(value if isinstance(value,str) else json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n') if value is not None else None
        after=hashlib.sha256(data.encode()).hexdigest() if data is not None else before
        if current not in (before,after):raise DeliveryRecoveryRequired('paper changed outside interrupted corrective application')
