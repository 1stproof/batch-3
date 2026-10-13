"""One explicitly authorized full reread by an existing source reviewer.

The rejected review remains history. The correction consumes an existing turn,
uses the exact rejected scope, and cannot open another evidence-request loop.
"""
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime

import pilot_paper_delivery as delivery
import pilot_paper_read_delivery as reads

FILE = 'paper-review-recovery.json'
RULE = 'same-reviewer-fixed-scope-correction-v1'
require = reads.require


def ledger_binding(ledger):
    # Native continuation rebases only these live storage pointers.
    value = {k: v for k, v in ledger.items() if k not in
             {'snapshot', 'snapshot_manifest', 'best_available_tex', 'best_available_pdf',
              'operational_failure', 'recovery_required'}}
    value['snapshot_manifest_sha256'] = ledger['snapshot_manifest']['sha256']
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def binding(source, ident, saved):
    root = Path(source)
    paper = root/'exam/papers'/ident
    ledger = delivery.read(delivery.regular(paper/'paper-ledger.json', root))
    stage = ledger.get('stage')
    progress = ledger.get('retrieval_progress', {})
    require(stage in reads.STAGES and stage not in ledger.get('completed', [])
            and not ledger.get('paper_review_recovery_admissions'), 'not an untouched source-review delivery rejection')
    calls = []
    for call in reversed(ledger['calls']):
        if not re.fullmatch(r'[A-Za-z0-9_-]+/paper-\d+-'+re.escape(stage), call.get('name', '')):
            break
        calls.append(call)
    calls.reverse()
    require(2 <= len(calls) < 4 and progress == {'stage': stage, 'session': calls[-1].get('session_id'),
            'turns': len(calls), 'writer': False}, 'reviewer identity or original turn allowance differs')
    session = progress['session']
    require(session in ledger['reader_ids'] and session not in ledger['writer_ids']
            and session != ledger.get('writer_session')
            and session not in set(saved['implementers']) | {c.get('session_id') for c in saved['calls']},
            'reviewer is not independent of research and writing')
    bindings = []
    previous_scope = None
    for index, call in enumerate(calls):
        meta, answer, scope, files = reads.authenticated(root, paper, call['name'])
        require(all(call.get(k) == meta.get(k) for k in ('name', 'status', 'session_id', 'answer_sha256', 'request_id', 'prompt_sha256')),
                'reviewer ledger differs from authenticated transport')
        start, end = datetime.fromisoformat(meta['start_utc']), datetime.fromisoformat(meta['end_utc'])
        require(start.tzinfo and end.tzinfo and end >= start and type(meta.get('pid')) is int and meta['pid'] > 1
                and meta.get('exit_code') == 0 and meta['session_id'] == session
                and meta.get('resume_session') == (None if index == 0 else session)
                and meta.get('fresh_session') is (index == 0), 'reviewer terminal/session evidence differs')
        if previous_scope is not None:
            require(all(scope.get(k) == previous_scope.get(k) for k in ('mode', 'problem_id', 'original_sha256', 'main_session'))
                    and all(k in scope['readonly_artifacts'] and all(scope['readonly_artifacts'][k].get(field) == ref.get(field)
                    for field in ('sha256', 'media_type')) for k, ref in previous_scope['readonly_artifacts'].items())
                    and set(previous_scope['required_artifact_ids']) <= set(scope['required_artifact_ids']),
                    'rejected scope changed prior evidence')
        if index < len(calls)-1:
            receipt = reads.compute(root, paper, ledger, call['name'])
            require(set(answer) == {'evidence_requests'} and isinstance(answer['evidence_requests'], list)
                    and answer['evidence_requests'] and all(isinstance(v, str) for v in answer['evidence_requests']),
                    'predecessor is not an evidence request')
            if meta['document_audit']['required_material_delivered'] is not True:
                require(delivery.read(delivery.regular(root/'host/runtime'/call['name']/reads.FILE, root)) == receipt,
                        'predecessor lacks prospective delivery acceptance')
        else:
            require(meta['document_audit']['required_material_delivered'] is False
                    and 'evidence_requests' not in answer and not (root/'host/runtime'/call['name']/reads.FILE).exists(),
                    'latest review is not a historical completed underdelivery')
            require(all('archive:'+v in scope['required_artifact_ids'] for v in prior_answer['evidence_requests']),
                    'rejected scope omits requested sources')
        bindings.append({'name': call['name'], 'files_sha256': files})
        previous_scope, prior_answer = scope, answer
    require(scope.get('problem_id') == ident and scope.get('mode') == 'review'
            and scope['original_sha256'] == delivery.digest(root/'campaign/problems'/ident/'input.txt'), 'original problem scope changed')
    admissions = [a for a in ledger.get('admissions', []) if a.get('name') in {c['name'] for c in calls}]
    require(len(admissions) == len(calls) and all(a['name'] == c['name']
            and a.get('resume_session') == (None if i == 0 else session) for i, (a,c) in enumerate(zip(admissions,calls))),
            'retrieval admission history differs')
    return {'problem': ident, 'stage': stage, 'rejected_call': calls[-1]['name'], 'session_id': session,
            'retrieval_progress': progress, 'evidence_requests': ledger.get('evidence_requests', {}).get(stage, []), 'chain': bindings, 'scope_sha256': delivery.scope_binding(scope),
            'ledger_sha256': delivery.digest(paper/'paper-ledger.json'), 'ledger_state_sha256': ledger_binding(ledger)}


def make_request(source, target, reconciliation, problems, *, authority):
    from pilot_continuation import validate_and_load
    checkpoint = validate_and_load(Path(source), reconciliation=Path(reconciliation))
    return request_from_checkpoint(source, target, checkpoint, problems, authority=authority)


def request_from_checkpoint(source, target, checkpoint, problems, *, authority):
    source, target = Path(source).resolve(), Path(target).resolve()
    require(isinstance(authority, str) and authority.strip(), 'explicit reviewer correction authority required')
    require(isinstance(problems, list) and problems and len(problems) == len(set(problems))
            and set(problems) <= set(checkpoint['problems']), 'unknown or duplicate correction problem')
    require(not checkpoint['config'].get('paper_review_recovery'), 'reviewer correction authorization already exists')
    require(not target.exists() and target != source and not target.is_relative_to(source)
            and not source.is_relative_to(target), 'reviewer correction requires separate successor')
    require(checkpoint['config'].get('exam') and checkpoint['parent']['source_root'] == str(source), 'native stopped exam required')
    return {'schema_version': 1, 'rule': RULE, 'source_root': str(source), 'target_root': str(target),
            'parent_manifest_sha256': checkpoint['parent']['manifest_sha256'], 'authority': authority,
            'maximum_admissions_per_problem': 1, 'existing_turn_limit': 4,
            'problems': {ident: binding(source, ident, checkpoint['problems'][ident]) for ident in sorted(problems)}}


def validate_request(request, source, target, checkpoint):
    expected = request_from_checkpoint(source, target, checkpoint, list(request.get('problems', {})), authority=request.get('authority'))
    require(request == expected, 'reviewer correction differs from exact stopped checkpoint')


def load(root, config):
    ref = config.get('paper_review_recovery')
    if ref is None:
        return None
    require(ref.get('path') == FILE, 'invalid reviewer correction path')
    path = delivery.regular(Path(root)/FILE, root)
    require(delivery.digest(path) == ref.get('sha256'), 'reviewer correction authorization changed')
    value = delivery.read(path)
    require(value.get('rule') == RULE and value.get('maximum_admissions_per_problem') == 1
            and value.get('existing_turn_limit') == 4, 'reviewer correction rule or budget changed')
    return value


def applies(engine, request, stage):
    item = request['problems'].get(engine.problem.ident)
    if item is None or stage != item['stage']:
        return False
    attempts = engine.ledger.get('paper_review_recovery_admissions', [])
    if attempts and attempts[0].get('status') == 'completed-reconciled':
        # A later writer/reviewer dispatch ends this correction's application window.
        # Subsequent revised manuscripts require a fresh independent review.
        return engine.ledger['calls'][-1].get('name') == attempts[0]['name']
    return True


def preserved(engine, item):
    for call in item['chain']:
        for filename, digest in call['files_sha256'].items():
            path = delivery.regular(engine.problem.pilot.host/'runtime'/call['name']/filename, engine.problem.pilot.root)
            require(delivery.digest(path) == digest, 'preserved rejected reviewer history changed')


def fixed_scope(engine, item):
    _, _, scope, _ = reads.authenticated(engine.problem.pilot.root, engine.root, item['rejected_call'])
    require(delivery.scope_binding(scope) == item['scope_sha256'], 'rejected review scope changed')
    scope.pop('producer', None)
    scope.pop('receipt_path', None)
    quarantine = engine.root/'unaccepted-review'
    quarantine.mkdir(exist_ok=True)
    path = quarantine/(item['stage']+'.json')
    original = engine.problem.pilot.host/'runtime'/item['rejected_call']/'stage.answer.txt'
    if not path.exists():
        with path.open('xb') as stream:
            stream.write(original.read_bytes())
    require(delivery.digest(path) == delivery.digest(original), 'quarantined review changed')
    scope['readonly_artifacts']['unaccepted-review'] = {'path': str(path), 'sha256': delivery.digest(path), 'media_type': 'application/json'}
    scope['required_artifact_ids'].append('unaccepted-review')
    return scope


def finish(engine, item, admission):
    root = engine.problem.pilot.root
    for relative, digest in admission['before_files'].items():
        path = engine.root/relative
        require((delivery.digest(delivery.regular(path, engine.root)) if path.exists() else None) == digest,
                'manuscript or author evidence changed before corrective review application')
    meta, answer, scope, _ = reads.authenticated(root, engine.root, admission['name'])
    require(meta['session_id'] == item['session_id'] and meta.get('resume_session') == item['session_id']
            and meta.get('fresh_session') is False and meta['document_audit']['required_material_delivered'] is True
            and delivery.scope_binding(scope) == admission['scope_sha256']
            and meta.get('prompt_sha256') == admission['prompt_sha256']
            and 'evidence_requests' not in answer, 'corrective review did not fully reread its exact admitted scope')
    calls = [c for c in engine.ledger['calls'] if c.get('name') == admission['name']]
    require(len(calls) == 1 and (calls[0].get('status') == 'admitted' or calls[0] == meta), 'corrective ledger changed')
    progress = {**item['retrieval_progress'], 'turns': item['retrieval_progress']['turns']+1}
    closure = {**progress, 'closed_by_review_recovery': admission['name'],
               'evidence_requests': item['evidence_requests']}
    old = [v for v in engine.ledger.get('retrieval_history', []) if v.get('closed_by_review_recovery') == admission['name']]
    if engine.ledger.get('retrieval_progress') is not None:
        require(engine.ledger['retrieval_progress'] == progress and not old, 'corrective turn count changed')
        engine.ledger.setdefault('retrieval_history', []).append(closure)
        del engine.ledger['retrieval_progress']
    else:
        require(old == [closure], 'corrective closure missing or changed')
    requests = engine.ledger.get('evidence_requests', {}).get(item['stage'])
    if requests is not None:
        require(requests == item['evidence_requests'], 'original evidence request history changed')
        del engine.ledger['evidence_requests'][item['stage']]
    engine.ledger['calls'][engine.ledger['calls'].index(calls[0])] = meta
    admission['status'] = 'completed-reconciled'
    engine.reconciled_retrieval_calls = {c['name'] for c in item['chain']} | {admission['name']}
    engine.save()
    return meta['session_id'], answer


async def resume(engine, request, task):
    item = request['problems'][engine.problem.ident]
    preserved(engine, item)
    auth = engine.problem.pilot.config['paper_review_recovery']['sha256']
    attempts = engine.ledger.get('paper_review_recovery_admissions', [])
    if attempts:
        require(len(attempts) == 1 and attempts[0].get('authorization_sha256') == auth
                and attempts[0].get('original_retrieval_progress') == item['retrieval_progress'], 'reviewer correction already consumed')
        return finish(engine, item, attempts[0])
    require(ledger_binding(engine.ledger) == item['ledger_state_sha256']
            and engine.ledger.get('retrieval_progress') == item['retrieval_progress'], 'reviewer checkpoint changed before correction')
    scope = fixed_scope(engine, item)
    engine.reconciled_retrieval_calls = {c['name'] for c in item['chain']}
    engine.paper_review_recovery_admission = {**item, 'authorization_sha256': auth}
    instruction = ('EXPLICIT FULL-SCOPE DELIVERY CORRECTION. The preserved review is UNACCEPTED. '
        'Read EVERY required artifact completely in this turn, including unaccepted-review, using '
        'read_required_evidence page 0 and every next_page, or complete read_artifact ranges. '
        'Prior reads do not substitute for these mandatory rereads. Confirm or revise the review only '
        'after reading all fixed evidence. This consumes one remaining original turn. Return the '
        'complete review JSON; evidence_requests and additional automatic turns are forbidden.\n'+task)
    try:
        await engine._call_once(item['stage'], instruction,
            {'instructions': 'Read every fixed required artifact before returning the corrected review.'},
            resume=item['session_id'], writer=False, delivery_scope=scope)
    finally:
        del engine.paper_review_recovery_admission
    return finish(engine, item, engine.ledger['paper_review_recovery_admissions'][0])
