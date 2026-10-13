"""Exact, explicit reconciliation of a provenance-only quarantine prerequisite.

No model admission or scientific evidence exemption is granted by this module.
Historical capability, missing-delivery verdict, and consumed counters stay intact.
"""
import hashlib
import json
from pathlib import Path

import pilot_paper_delivery as delivery
from pilot_document_tools import audit_operations, allowed_event

KIND = 'paper-delivery-contract-reconciliation'
RULE = 'same-writer-quarantine-provenance-only-v1'
FILE = KIND + '.json'
LEGACY_GUIDANCE = 'SCOPED DOCUMENT TOOL INVOCATION: The tools are advertised directly in the mcp__merlean_documents namespace. Use a direct tool call with its JSON arguments: read_required_evidence({"page": 0}), read_artifact({"artifact_id": "an exact indexed ID", "sha256": "its exact indexed hash"}). Do not discover or invoke these tools through functions.exec, ALL_TOOLS, JavaScript, tool_search, shell, resource listing, patch tools, or subagents. Those calls are outside this stage contract. Read every declared required evidence page before positive review authority; optional documents remain need-driven. If a declared tool is unavailable, report that infrastructure limitation within the existing response contract; do not probe other tool surfaces.'
# The sole legacy producer whose admission omitted the deterministic suffix.
LEGACY_CODE = {
    'codex_transport.py':'83e855c69534a7d4db2be30b279cb18cac4f2941c43e2538b5ede12ae0c05a45',
    'pilot_document_tools.py':'8de335768c6ffce015e6d99d44d8ff432a43b414cbe01452173f36a7b2dab8ea',
    'pilot_paper.py':'3dd206e055de7c122ae1c60f3338aca70f227e42fa1aaf020e922ea60f2caaca',
    'pilot_paper_delivery.py':'b221b8558e3b55b28a27ec375c802de866b91b350c19fb1709ced30b7ed26426'}


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def binding(root, problem, stage_name, *, origin=None, producer_code_hashes=None):
    root = Path(root).resolve()
    config = delivery.read(root/'host-config.json')
    codes = producer_code_hashes if producer_code_hashes is not None else {k:config.get('code_hashes',{}).get(k) for k in LEGACY_CODE}
    if codes != LEGACY_CODE:raise ValueError('contract reconciliation requires the exact known legacy producer')
    original = delivery.load_request(root, config)
    if original is None or original['binding']['problem'] != problem:
        raise ValueError('contract reconciliation requires exact prior delivery authority')
    old, ledger, _, _, old_scope, mapped = delivery.binding(root, problem,
        original['binding']['stage'], origin=original['source_root'])
    if old != original['binding'] or ledger.get('stage') != 'reconstruct':
        raise ValueError('original rejected checkpoint or reconstruction stage changed')
    attempts = ledger.get('delivery_remediation_admissions', [])
    if len(attempts) != 1:
        raise ValueError('exact single consumed delivery admission required')
    admission = attempts[0]
    if (admission.get('name') != stage_name or admission.get('status') != 'admitted'
            or admission.get('authorization_sha256') != config['paper_delivery_remediation']['sha256']
            or admission.get('resume_session') != old['session_id']
            or admission.get('original_retrieval_progress') != old['retrieval_progress']):
        raise ValueError('consumed delivery admission identity changed')
    folder = root/'exam/papers'/problem
    draft = delivery.regular(folder/'unaccepted-reconstruction/draft.json', folder)
    if delivery.digest(draft) != old['files']['raw_answer']:
        raise ValueError('excluded quarantine is not the exact original same-writer response')
    if 'unaccepted-draft' in old_scope['readonly_artifacts']:
        raise ValueError('quarantine cannot replace original evidence')
    expected = {k:v for k,v in old_scope.items() if k not in ('producer','receipt_path')}
    expected.update(store_root=str(folder), main_session=old['session_id'],
        readonly_artifacts={**mapped, 'unaccepted-draft':{'path':str(draft),
            'sha256':delivery.digest(draft),'media_type':'application/json'}},
        required_artifact_ids=[*old_scope['required_artifact_ids'],'unaccepted-draft'],inline_artifact_ids=[])
    stage = root/'host/runtime'/stage_name
    names = {'meta':'stage.meta.json','raw_answer':'stage.answer.txt','parsed_answer':'stage.answer.json',
        'prompt':'stage.prompt.txt','capability':'document-capability.json',
        'events':'stage.events.jsonl','receipts':'document-operations.jsonl'}
    paths = {key:delivery.regular(stage/name,root) for key,name in names.items()}
    meta, scope = delivery.read(paths['meta']), delivery.read(paths['capability'])
    try:
        start,end=delivery.datetime.fromisoformat(meta['start_utc']),delivery.datetime.fromisoformat(meta['end_utc'])
        terminal=(start.tzinfo is not None and end.tzinfo is not None and end>=start
            and type(meta.get('pid')) is int and meta['pid']>1 and type(meta.get('exit_code')) is int)
    except (KeyError,TypeError,ValueError):terminal=False
    prompt=paths['prompt'].read_text()
    suffix='\n'+LEGACY_GUIDANCE
    if (not prompt.endswith(suffix) or prompt.count(suffix) != 1
            or hashlib.sha256(prompt[:-len(suffix)].encode()).hexdigest() != admission.get('prompt_sha256')
            or delivery.digest(draft) in prompt
            or 'Only the explicitly provided read_artifact tool is permitted.' not in prompt):
        raise ValueError('historical prompt does not match the exact defective legacy contract')
    coverage = {ident:True for ident in old_scope['required_artifact_ids']}
    coverage['unaccepted-draft'] = False
    if (not terminal or meta.get('name') != stage_name or meta.get('module') != 'paper-reconstruct'
            or meta.get('status') != 'completed' or meta.get('turn_completed') is not True
            or meta.get('model_actual') != 'gpt-6-astra' or meta.get('model_verified') is not True
            or meta.get('session_id') != old['session_id'] or meta.get('resume_session') != old['session_id']
            or delivery.digest(paths['raw_answer']) != meta.get('answer_sha256')
            or delivery.digest(paths['prompt']) != meta.get('prompt_sha256')
            or delivery.digest(paths['capability']) != meta.get('document_capability',{}).get('sha256')
            or delivery.scope_binding(scope) != delivery.scope_binding(expected)
            or delivery.scope_binding(scope) != admission.get('scope_sha256')
            or scope.get('producer') != {'stage':stage_name,'request_id':meta.get('request_id'),'session_id':old['session_id']}):
        raise ValueError('completed corrective response identity or exact scope changed')
    declared_folder=Path(origin or root)/'exam/papers'/problem
    for ident,ref in scope['readonly_artifacts'].items():
        declared=Path(ref['path'])
        if (not declared.is_absolute() or not declared.is_relative_to(declared_folder)
                or folder/declared.relative_to(declared_folder) != Path(expected['readonly_artifacts'][ident]['path'])):
            raise ValueError('corrective capability artifact path changed')
    records = [c for c in ledger['calls'] if c.get('name') == stage_name]
    if (len(records) != 1 or ledger['calls'][-1] is not records[0]
            or any(records[0].get(k) != meta.get(k) for k in ('status','session_id','answer_sha256','prompt_sha256'))):
        raise ValueError('corrective response differs from exact consumed history')
    # Re-run the original authoritative audit over saved complete-output hashes,
    # never infer model delivery from native preview diagnostics.
    expected.update(producer=scope['producer'], receipt_path=str(paths['receipts']))
    events = [json.loads(line)['event'] for line in paths['events'].read_text().splitlines()]
    events = [event for event in events if allowed_event(event, expected)]
    if events != meta.get('document_events'):
        raise ValueError('saved document events differ from completed response')
    receipts=[json.loads(line) for line in paths['receipts'].read_text().splitlines()]
    failed=[receipt for receipt in receipts if receipt.get('is_error')]
    for receipt in failed:
        # Use the same argument encoding as durable server receipts.
        from pilot_document_tools import encoded, digest as document_digest
        matches=[event['item'] for event in events if event.get('type')=='item.completed'
            and event['item'].get('tool')==receipt.get('tool')
            and document_digest(encoded(event['item'].get('arguments')).encode())==receipt.get('arguments_sha256')]
        if (len(failed)!=1 or len(matches)!=1 or receipt.get('tool')!='read_artifact'
                or matches[0].get('arguments')!={'artifact_id':'unaccepted-draft','sha256':'','start':0,'end':16000}
                or matches[0].get('result',{}).get('content')!=[{'type':'text','text':'Document operation refused: unknown artifact or mismatched exact hash'}]):
            raise ValueError('errored document operation is not the exact missing quarantine hash defect')
    persisted = meta.get('persisted_rollout_audit', {})
    if persisted.get('status') != 'verified':
        raise ValueError('persisted model output identity is not verified')
    audit = audit_operations(expected, events, persisted['tool_events'], old['session_id'],
                             persisted['tool_output_receipts'])
    if (audit != meta.get('document_audit') or audit.get('status') != 'PASS'
            or audit.get('errors') or audit.get('delivery_errors')
            or audit.get('complete_tool_outputs_delivered') is not True
            or audit.get('required_material_delivered') is not False
            or audit.get('required_artifact_coverage') != coverage):
        raise ValueError('every original source must be delivered; only quarantine reread may be missing')
    answer, _, error = delivery.extract_answer(paths['raw_answer'].read_text())
    if (error or not isinstance(answer,dict) or not isinstance(answer.get('tex'),str)
            or 'evidence_requests' in answer or answer != delivery.read(paths['parsed_answer'])):
        raise ValueError('completed candidate lacks its exact structured response')
    projected,attachments=project_candidate(answer)
    result = {'candidate_projection':{'answer_sha256':canonical(projected),'attachments':attachments},'problem':problem,'stage':stage_name,'session_id':old['session_id'],
        'producer_code_hashes':codes,'legacy_suffix_sha256':hashlib.sha256(suffix.encode()).hexdigest(),
        'original_request_sha256':config['paper_delivery_remediation']['sha256'],
        'original_binding':old,'admission':admission,'call_history_sha256':canonical(ledger['calls']),
        'files':{key:delivery.digest(path) for key,path in paths.items()},
        'required_artifact_coverage':coverage,'audit_sha256':canonical(audit),
        'excluded_provenance':{'artifact_id':'unaccepted-draft','sha256':delivery.digest(draft),
            'producing_stage':old['stage'],'same_writer':old['session_id'],'scientific_authority':False}}
    return result, answer, admission


def make_request(source, problem, stage, parent_manifest_sha256, *, authority):
    value, _, _ = binding(source, problem, stage)
    if not isinstance(authority,str) or not authority.strip() or not delivery.re.fullmatch(r'[0-9a-f]{64}',parent_manifest_sha256):
        raise ValueError('explicit contract authority and exact parent manifest required')
    return {'schema_version':1,'kind':KIND,'rule':RULE,'source_root':str(Path(source).resolve()),
        'parent_manifest_sha256':parent_manifest_sha256,'authority':authority,'model_admissions':0,'binding':value}


def validate_request(request, source, parent):
    if (not isinstance(request,dict) or type(request.get('schema_version')) is not int
            or type(request.get('model_admissions')) is not int):
        raise ValueError('contract authority requires exact integer schema and zero admissions')
    value=request.get('binding',{})
    expected=make_request(source,value.get('problem',''),value.get('stage',''),parent['manifest_sha256'],authority=request.get('authority'))
    if request != expected or request['source_root'] != parent['source_root']:
        raise ValueError('contract request differs from exact stopped parent')
    return request


def load_request(root, config):
    ref=config.get('paper_delivery_contract_reconciliation')
    if ref is None:return None
    if not isinstance(ref,dict) or ref.get('path') != FILE:
        raise ValueError('invalid contract reconciliation reference')
    path=delivery.regular(Path(root)/FILE,root)
    if delivery.digest(path) != ref.get('sha256'):raise ValueError('contract authority changed')
    request=delivery.read(path)
    if (type(request.get('schema_version')) is not int or request.get('schema_version') != 1 or request.get('kind') != KIND or request.get('rule') != RULE
            or type(request.get('model_admissions')) is not int or request['model_admissions'] != 0):
        raise ValueError('invalid zero-admission contract reconciliation')
    return request


def reconcile(engine, request):
    expected=request['binding']
    value, answer, admission=binding(engine.problem.pilot.root, engine.problem.ident,expected['stage'],origin=request['source_root'],producer_code_hashes=expected['producer_code_hashes'])
    if value != expected:raise delivery.DeliveryRecoveryRequired('completed contract bindings changed')
    projected,attachments=project_candidate(answer)
    delivery.validate_application(engine, projected, admission)
    preserve_attachments(engine, expected, attachments)
    receipt={'request_sha256':engine.problem.pilot.config['paper_delivery_contract_reconciliation']['sha256'],
        'stage':expected['stage'],'rule':RULE,'excluded_provenance':expected['excluded_provenance'],
        'historical_required_material_delivered':False,'model_admissions':0,
        'candidate_projection':expected['candidate_projection'],
        'authority':'candidate reconstruction only; normal scientific and paper gates remain'}
    prior=engine.ledger.get('delivery_contract_reconciliation')
    if prior is not None and prior != receipt:raise delivery.DeliveryRecoveryRequired('different contract reconciliation already recorded')
    engine.ledger['delivery_contract_reconciliation']=receipt
    progress=engine.ledger.get('retrieval_progress')
    if progress is not None:
        engine.ledger.setdefault('retrieval_history',[]).append({**progress,'closed_by_delivery_remediation':admission['name']})
        engine.ledger.pop('retrieval_progress')
    engine.save()
    return value['session_id'],projected


def visible_contract(scope):
    """Simple scoped IDs/pages; the host owns immutable version verification."""
    from pilot_document_tools import required_read_plan
    pages=required_read_plan(scope)
    return {'required_artifact_ids':list(scope['required_artifact_ids']),
        'mandatory_read_plan':[{k:v for k,v in page.items() if k != 'sha256'} for page in pages],
        'first_required_page':0,
        'instructions':'Use read_required_evidence page 0, then returned next_page until null. '
            'Alternatively use read_artifact with a listed artifact_id and optional start/end ranges; no hash is needed. '
            'Read all mandatory bytes before returning the candidate. The host checks the exact saved file version.',
        'authority':'delivery navigation only; no mathematical acceptance'}


def project_candidate(answer):
    from pilot_paper import WRITER_FILES
    artifacts=answer.get('artifacts',{})
    if not isinstance(artifacts,dict):raise ValueError('candidate artifacts must be an object')
    projected={**answer,'artifacts':{k:v for k,v in artifacts.items() if k in WRITER_FILES}}
    extras=[]
    for key in sorted(set(artifacts)-WRITER_FILES):
        value=artifacts[key]
        data=value if isinstance(value,str) else json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
        extras.append({'id':'attachment-'+hashlib.sha256(key.encode()).hexdigest(),
            'original_key':key,'value_type':type(value).__name__,
            'encoding':'UTF-8 literal string' if isinstance(value,str) else 'UTF-8 canonical JSON',
            'sha256':hashlib.sha256(data.encode()).hexdigest(),
            'authority':'untrusted writer-authored attachment; no host-state write or scientific acceptance'})
    return projected,extras


def preserve_attachments(engine, binding, attachments):
    directory=engine.root/'untrusted-author-attachments'
    if directory.is_symlink():raise delivery.DeliveryRecoveryRequired('attachment directory is a symlink')
    directory.mkdir(exist_ok=True)
    stage=engine.problem.pilot.host/'runtime'/binding['stage']
    raw=delivery.regular(stage/'stage.answer.txt',engine.problem.pilot.root).read_bytes()
    answer=delivery.read(stage/'stage.answer.json')
    files={'original-response.txt':raw,'manifest.json':(json.dumps(attachments,indent=2,sort_keys=True)+'\n').encode()}
    for item in attachments:
        value=answer['artifacts'][item['original_key']]
        data=(value if isinstance(value,str) else json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n').encode()
        if hashlib.sha256(data).hexdigest()!=item['sha256']:raise ValueError('attachment content changed')
        files[item['id']+'.txt']=data
    if set(p.name for p in directory.iterdir())-set(files):raise ValueError('unexpected candidate attachment file')
    for name,data in files.items():
        path=directory/name
        if path.is_symlink() or (path.exists() and (not path.is_file() or path.read_bytes()!=data)):
            raise delivery.DeliveryRecoveryRequired('preserved attachment differs from exact response')
        if not path.exists():path.write_bytes(data)


def raw_fidelity_material(engine):
    receipt=engine.ledger.get('delivery_contract_reconciliation')
    if receipt is None:return None
    binding={'stage':receipt['stage']}
    attachments=receipt['candidate_projection']['attachments']
    preserve_attachments(engine,binding,attachments)
    directory=engine.root/'untrusted-author-attachments'
    return {'authority':'UNTRUSTED original writer response and mechanically preserved attachments; independently audit every claim',
        'original_response':(directory/'original-response.txt').read_text(),
        'attachment_manifest':attachments,
        'attachments':{item['id']:(directory/(item['id']+'.txt')).read_text() for item in attachments}}
