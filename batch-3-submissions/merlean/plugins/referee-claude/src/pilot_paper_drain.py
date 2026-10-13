"""Reconcile only the proven legacy zero-admission cooperative-drain marker."""
import hashlib
import json
from pathlib import Path
import re
from pilot_document_tools import regular_bytes


def reconcile(engine, stage, writer):
    ledger = engine.ledger
    pending = ledger.get('retrieval_progress')
    if not engine.restored_ledger or not writer or not isinstance(pending, dict):
        return False
    session = ledger.get('writer_session')
    if pending != {'stage':'repair-'+stage,'session':session,'turns':0,'writer':True}:
        return False
    def require(value, message):
        if not value:
            raise ValueError('unadmitted paper drain: '+message)
    require(stage == ledger['stage'] and bool(session) and session in ledger.get('writer_ids',[]), 'writer identity changed')
    stages = {stage,'repair-'+stage}
    require(not any(ledger.get('evidence_requests',{}).get(s) for s in stages), 'retrieval already requested evidence')
    pattern = re.compile(re.escape(engine.problem.ident)+r'/paper-\d+-(?:'+ '|'.join(re.escape(s) for s in stages)+')$')
    require(not any(pattern.fullmatch(str(c.get('name',''))) or c.get('stage') in stages
                    for c in ledger['calls']+ledger.get('admissions',[])), 'matching admission exists')
    namespace = engine.problem.pilot.host/'runtime'/engine.problem.ident
    require(not any(pattern.fullmatch(engine.problem.ident+'/'+p.name) for p in namespace.glob('paper-*')), 'matching transport exists')
    errors = ledger.get('errors',[])
    require(any(e.get('stage')==stage and e.get('type')=='DrainRequested'
                and e.get('message')=='paper pipeline preserved at cooperative drain' for e in errors), 'pipeline drain receipt missing')
    require(any(e.get('stage')=='contextual-repair' and e.get('type')=='DrainRequested'
                and e.get('message')=='host admission closed; preserve completed work and checkpoint before another launch' for e in errors), 'repair admission denial missing')
    candidates=[c for c in ledger['calls'] if c.get('name','').endswith('-reconstruct') and c.get('session_id')==session]
    require(len(candidates)==1,'original writer producer is ambiguous')
    call=candidates[0];directory=engine.problem.pilot.host/'runtime'/call['name']
    paths={name:directory/name for name in ['stage.meta.json','stage.answer.txt','stage.prompt.txt','document-capability.json']}
    data={name:regular_bytes(path) for name,path in paths.items()}
    meta=json.loads(data['stage.meta.json'])
    require(all(call.get(k)==meta.get(k) for k in ('name','status','session_id','answer_sha256','prompt_sha256','request_id')), 'writer ledger differs from transport')
    require(meta.get('status')=='completed' and meta.get('model_actual')=='gpt-6-astra'
            and meta.get('model_verified') is True and meta.get('turn_completed') is True
            and meta.get('fresh_session') is True and meta.get('resume_session') is None
            and meta.get('document_audit',{}).get('required_material_delivered') is True, 'writer producer is not authenticated')
    hashes={name:hashlib.sha256(body).hexdigest() for name,body in data.items()}
    require(hashes['stage.answer.txt']==meta.get('answer_sha256') and hashes['stage.prompt.txt']==meta.get('prompt_sha256')
            and hashes['document-capability.json']==meta.get('document_capability',{}).get('sha256'), 'writer bytes changed')
    engine.next_call_number()  # All historical stages must have terminal ownership evidence.
    ledger.setdefault('unadmitted_drain_reconciliations',[]).append({'schema_version':1,
        'kind':'legacy_zero_admission_drain','pending':dict(pending),'writer_stage':call['name'],
        'writer_files_sha256':hashes,'turns_consumed':0,'authority':'no admission or review renewal'})
    del ledger['retrieval_progress']
    engine.save()
    return True
