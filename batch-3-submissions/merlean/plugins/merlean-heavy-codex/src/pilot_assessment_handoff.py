"""Voluntary attention at an authenticated completed-assessment boundary.

This is neither review exhaustion nor a mathematical verdict. No automatic
continuation or renewed assessment is authorized by this receipt.
"""
import json
from pathlib import Path
import pilot_review_exhaustion as evidence
import pilot_operational_handoff as handoff

KIND = 'assessment_handoff'
FILE = 'assessment-handoff.json'
FIELDS = {'response_type','selected_candidate_sha256','assessment_ids','reason','no_new_scientific_work'}
GUIDANCE = ('At an eligible completed-assessment boundary, keep main-owned lawful options: repair the proof, '
    'propose genuinely new authorized tasks or probes, or supply supported independent source/use-site evidence. '
    'Do not invent cosmetic revisions or repeat an administrative checkpoint to renew review. '
    'If you have no concrete new scientific work and need supervisor attention, voluntarily return exactly '
    '{"response_type":"assessment_handoff","selected_candidate_sha256":"<current hash>",'
    '"assessment_ids":["<all eligible host IDs>"],"reason":"<operational explanation>",'
    '"no_new_scientific_work":true}. This preserves every unresolved scientific finding; it does not '
    'claim the proof is correct, excuse missing authentication, renew any review, or stop other problems. '
    'The host will preserve this problem partial for explicit supervisor diagnosis, with no automatic reentry.')


def records(problem):
    from codex_pilot import assessment_key, sha, encoded
    if (not getattr(problem, 'current', None) or any(problem.current.get(k) for k in
            ('sol_tasks','python_probe','lean_probe','route_scout_tasks'))):
        return []
    key = assessment_key(problem.current, getattr(problem, 'execution_history', []))
    candidate = sha(encoded(problem.current)); result = []
    calls = {c['name']: c for c in getattr(problem, 'calls', [])}
    for item in getattr(problem, 'final_assessment_history', []):
        if (item.get('execution_identity_version') != 2 or item.get('status') != 'reviewed'
                or item.get('binding_key') != key or item.get('candidate_sha256') != candidate
                or (item.get('final_validation') or {}).get('successful_complete') is True):
            continue
        receipt = item.get('proof_receipt', {}); call = calls.get(receipt.get('name'))
        if not call or any(call.get(k) != receipt.get(k) for k in
                ('status','session_id','model_actual','model_verified','fresh_session','resume_session',
                 'prompt_sha256','answer_sha256','request_id')):
            raise ValueError('assessment handoff review provenance changed')
        if (call.get('status') != 'completed' or call.get('model_verified') is not True
                or call.get('fresh_session') is not True or call.get('resume_session')
                or call.get('model_actual') != 'gpt-6-astra'
                or call.get('session_id') in {getattr(problem,'session',None), *getattr(problem,'implementers',[])}
                or call.get('document_audit', {}).get('required_material_delivered') is not True):
            continue
        stage, _, _, meta_sha = evidence.metadata(call)
        raw = evidence.regular_bytes(stage/'stage.answer.txt')
        if evidence.hashlib.sha256(raw).hexdigest() != call.get('answer_sha256'):
            raise ValueError('assessment handoff review answer changed')
        from codex_transport import extract_answer
        review, _, error = extract_answer(raw.decode())
        if error or not isinstance(review,dict) or review.get('verdict') != 'INCOMPLETE':
            continue
        if (receipt.get('reviewed_candidate_sha256') != candidate
                or review.get('candidate_sha256') != candidate):
            raise ValueError('assessment handoff candidate binding changed')
        binding = {'kind':'completed_assessment', 'candidate_sha256':candidate,
            'binding_key':key, 'review_stage':call['name'], 'review_meta_sha256':meta_sha,
            'review_answer_sha256':call['answer_sha256'], 'end_utc':call['end_utc']}
        result.append({'id':evidence.digest(binding), **binding})
    return result


def capability(problem):
    values = records(problem)
    eligible = bool(values) and problem.documents_enabled()
    if eligible:
        doc = problem.document_current()
        eligible = doc['status']=='submitted' and doc['proof_markdown']==problem.current['proof_markdown']
    return {'eligible':eligible, 'assessment_ids':sorted(x['id'] for x in values) if eligible else [],
            'authority':'supervisor_attention_only_no_renewal_or_acceptance'}


def commit(problem, raw, meta):
    if not isinstance(raw,dict) or set(raw)!=FIELDS or raw.get('response_type')!=KIND:
        raise ValueError('invalid assessment handoff fields')
    actual, meta_sha = handoff.bound_answer(problem, meta)
    if actual != raw or not problem.calls or problem.calls[-1] != meta:
        raise ValueError('assessment handoff must bind latest original-main answer')
    from codex_pilot import sha, encoded
    values = records(problem); cap = capability(problem)
    if (not cap['eligible'] or raw.get('assessment_ids') != cap['assessment_ids']
            or raw.get('selected_candidate_sha256') != sha(encoded(problem.current))
            or raw.get('no_new_scientific_work') is not True
            or not isinstance(raw.get('reason'),str) or not raw['reason'].strip()
            or getattr(problem,'active_stages',set())
            or any(evidence.moment(meta['start_utc']) <= evidence.moment(x['end_utc']) for x in values)):
        raise ValueError('assessment handoff lacks exact current completed-assessment authority')
    receipt = {'schema_version':1,'status':'supervisor_needed','kind':KIND,
        'automatic_resume_authorized':False,'acceptance_authority':False,
        'source_stage':meta['name'],'source_meta_sha256':meta_sha,
        'source_answer_sha256':meta['answer_sha256'],'request':raw,'assessments':values,
        'preserved_state':{k:evidence.digest(getattr(problem,k,[])) for k in
            ('findings','execution_history','route_scout_history','local_verification_modules')}}
    path = Path(problem.folder)/FILE
    if path.exists():
        import pilot_assessment_delivery_resolution as resolution
        old = json.loads(evidence.regular_bytes(path))
        if old != receipt and resolution.allows(problem,old):
            path = Path(problem.folder)/('assessment-handoff-'+meta['name'].split('/')[-1]+'.json')
    if path.exists() or path.is_symlink():
        if json.loads(evidence.regular_bytes(path)) != receipt:
            raise ValueError('assessment handoff receipt changed')
    else:
        fd=evidence.os.open(path,evidence.os.O_WRONLY|evidence.os.O_CREAT|evidence.os.O_EXCL|evidence.os.O_NOFOLLOW,0o600)
        with evidence.os.fdopen(fd,'w') as stream:
            json.dump(receipt,stream,indent=2);stream.write('\n');stream.flush();evidence.os.fsync(stream.fileno())
    raise handoff.OperationalHandoff(receipt)


def guard(problem, role=None):
    if not hasattr(problem,'folder'):
        return
    import pilot_assessment_delivery_resolution as resolution
    calls=getattr(problem,'calls',[])
    for path in resolution.paths(problem.folder):
        if path.exists() or path.is_symlink():
            value=json.loads(evidence.regular_bytes(path))
            if resolution.allows(problem,value,role=role):
                continue
            if not calls or value.get('source_stage')!=calls[-1].get('name'):
                raise ValueError('assessment handoff missing source or later call exists')
            commit(problem,value.get('request'),calls[-1])
    resolved = resolution.problem_records(problem)
    if calls and resolved and resolution.covers(resolved,problem.ident,stage=calls[-1]['name']):
        return  # Exact local frozen receipt already authenticated, even without ancestors.
    if calls and calls[-1].get('status')=='completed' and calls[-1].get('module','').startswith('main'):
        # The raw answer is authoritative even if receipt publication crashed.
        meta=calls[-1];cap=meta.get('document_capability',{})
        copy_path=Path(problem.folder)/(meta['name'].split('/')[-1]+'.json')
        copied=json.loads(evidence.regular_bytes(copy_path)) if copy_path.is_file() else None
        if isinstance(copied,dict) and copied.get('response_type')==KIND and not cap.get('path'):
            raise ValueError('assessment handoff campaign copy lacks authenticated transport')
        if cap.get('path'):
            stage=Path(cap['path']).parent
            from codex_transport import extract_answer
            raw,_,error=extract_answer(evidence.regular_bytes(stage/'stage.answer.txt').decode())
            if (isinstance(copied,dict) and copied.get('response_type')==KIND and copied!=raw):
                raise ValueError('assessment handoff campaign copy differs from transport')
            if not error and isinstance(raw,dict) and raw.get('response_type')==KIND:
                resolved = resolution.problem_records(problem)
                if resolved and resolution.covers(resolved,problem.ident,stage=meta['name']):
                    return
                actual, _ = handoff.bound_answer(problem,meta)
                number = str(int(meta['name'].split('/')[-1].split('-')[0]))
                rejected = Path(problem.folder)/('main-'+number+'-invalid-contract.json')
                if rejected.is_file() and json.loads(evidence.regular_bytes(rejected)).get('raw_response')==actual:
                    return  # One existing host-recorded structural correction remains lawful.
                commit(problem,raw,meta)
