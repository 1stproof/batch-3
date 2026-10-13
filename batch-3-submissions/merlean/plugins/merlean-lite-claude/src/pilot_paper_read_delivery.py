"""Host receipts for complete reads across one bounded reviewer retrieval chain.

Raw transport audits remain per-call. Historical incomplete calls without this
prospective receipt never acquire acceptance during checkpoint restoration.
"""
import json
import re
from pathlib import Path

import pilot_document_tools as documents
import pilot_paper_delivery as delivery

FILE = 'paper-delivery.json'
RULE = 'same-reviewer-complete-artifacts-v1'
STAGES = {'raw-audit', 'proof-audit'}


def require(value, message):
    if not value:
        raise ValueError(message)


def authenticated(root, paper, name):
    """Recheck saved raw operations and exact model-visible result receipts."""
    root, paper = Path(root), Path(paper)
    require(re.fullmatch(r'[A-Za-z0-9_-]+/paper-\d+-(raw-audit|proof-audit)', name), 'invalid reviewer call')
    directory = root/'host/runtime'/name
    filenames = ('stage.meta.json', 'stage.answer.txt', 'stage.answer.json', 'stage.prompt.txt',
                 'document-capability.json', 'document-operations.jsonl', 'stage.events.jsonl')
    paths = {f: delivery.regular(directory/f, root) for f in filenames}
    meta, scope = delivery.read(paths['stage.meta.json']), delivery.read(paths['document-capability.json'])
    require(meta.get('name') == name and meta.get('module') == 'paper-'+name.split('paper-', 1)[1].split('-', 1)[1]
            and meta.get('status') == 'completed' and meta.get('turn_completed') is True
            and meta.get('model_actual') == 'gpt-6-astra' and meta.get('model_verified') is True
            and isinstance(meta.get('session_id'), str) and bool(meta['session_id'])
            and not meta.get('protocol_errors') and meta.get('persisted_rollout_audit', {}).get('status') == 'verified',
            'reviewer transport is not authenticated and complete')
    require(delivery.digest(paths['stage.answer.txt']) == meta.get('answer_sha256')
            and delivery.digest(paths['stage.prompt.txt']) == meta.get('prompt_sha256')
            and delivery.digest(paths['document-capability.json']) == meta.get('document_capability', {}).get('sha256'),
            'reviewer transport bytes changed')
    answer, _, error = delivery.extract_answer(paths['stage.answer.txt'].read_text())
    require(not error and isinstance(answer, dict) and answer == delivery.read(paths['stage.answer.json']), 'reviewer answer differs')
    require(scope.get('producer') == {'stage': name, 'request_id': meta.get('request_id'), 'session_id': meta.get('resume_session')},
            'reviewer capability producer changed')
    old_store = Path(scope['store_root'])
    for ref in scope['readonly_artifacts'].values():
        original = Path(ref['path'])
        require(old_store.is_absolute() and original.is_relative_to(old_store), 'reviewer scope escapes store')
        copied = delivery.regular(paper/original.relative_to(old_store), paper)
        require(delivery.digest(copied) == ref['sha256'], 'reviewer artifact bytes changed')
        ref['path'] = str(copied)
    if 'public_source_store' in scope:
        allowed = {str(old_store/'public-sources'): Path('public-sources'),
                   str(old_store/'refs/public-sources'): Path('refs/public-sources')}
        require(scope['public_source_store'] in allowed, 'public source store changed')
        scope['public_source_store'] = str(paper/allowed[scope['public_source_store']])
    scope['store_root'] = str(paper)
    scope['receipt_path'] = str(paths['document-operations.jsonl'])
    documents.validate_scope(scope)
    events = [json.loads(line)['event'] for line in paths['stage.events.jsonl'].read_text().splitlines()
              if 'event' in json.loads(line)]
    events = [event for event in events if documents.allowed_event(event, scope)]
    require(events == meta.get('document_events'), 'saved native document events differ')
    persisted = meta['persisted_rollout_audit']
    audit = documents.audit_operations(scope, events, persisted['tool_events'], meta['session_id'], persisted.get('tool_output_receipts', []))
    require(audit == meta.get('document_audit') and audit.get('status') == 'PASS'
            and audit.get('complete_tool_outputs_delivered') is True and not audit.get('errors')
            and not audit.get('delivery_errors'), 'raw reviewer delivery audit differs')
    return meta, answer, scope, {f: delivery.digest(p) for f, p in paths.items()}


def compute(root, paper, ledger, name):
    stage = name.split('paper-', 1)[1].split('-', 1)[1]
    require(stage in STAGES, 'coverage is limited to source reviewers')
    calls = ledger['calls']
    index = next(i for i, c in enumerate(calls) if c.get('name') == name)
    chain = []
    for call in reversed(calls[:index+1]):
        if not re.fullmatch(r'[A-Za-z0-9_-]+/paper-\d+-'+re.escape(stage), call.get('name', '')):
            break
        chain.append(call)
    chain.reverse()
    require(1 <= len(chain) <= 4 and len({c['name'] for c in chain}) == len(chain), 'invalid bounded reviewer chain')
    session, previous_scope, previous_requests, coverage, bindings = None, None, None, {}, []
    seen_requests = set()
    for position, call in enumerate(chain):
        meta, answer, scope, files = authenticated(root, paper, call['name'])
        require(all(call.get(k) == meta.get(k) for k in ('status', 'session_id', 'answer_sha256', 'request_id', 'prompt_sha256')),
                'reviewer ledger differs from raw transport')
        if session is None:
            session = meta['session_id']
            require(meta.get('fresh_session') is True and meta.get('resume_session') is None
                    and session not in ledger.get('writer_ids', []) and session != ledger.get('writer_session'),
                    'retrieval must begin with an independent fresh reviewer')
        else:
            require(meta.get('session_id') == session and meta.get('resume_session') == session
                    and meta.get('fresh_session') is False, 'retrieval reviewer changed')
            require(all(scope.get(k) == previous_scope.get(k) for k in ('mode', 'problem_id', 'original_sha256', 'main_session')),
                    'retrieval scope identity changed')
            require(all(key in scope['readonly_artifacts'] and all(scope['readonly_artifacts'][key].get(k) == ref.get(k)
                    for k in ('sha256', 'media_type')) for key, ref in previous_scope['readonly_artifacts'].items()),
                    'retrieval changed previously exposed bytes')
            require(set(previous_scope['required_artifact_ids']) <= set(scope['required_artifact_ids'])
                    and all('archive:'+item in scope['required_artifact_ids'] for item in previous_requests),
                    'evidence request was not delivered by its immediate successor')
        raw = meta['document_audit']['required_artifact_coverage']
        current = {key for key, complete in raw.items() if complete is True}
        inherited = {key for key in coverage if key in scope['required_artifact_ids']}
        complete = current | inherited
        require(set(scope['required_artifact_ids']) <= complete, 'reviewer still lacks complete required artifacts')
        bindings.append({'name': call['name'], 'files_sha256': files})
        result = {'rule': RULE, 'session_id': session, 'stage': stage, 'call': call['name'],
                  'chain': bindings.copy(), 'current_complete': sorted(current),
                  'inherited_complete': sorted(inherited-current),
                  'required_artifact_coverage': {key: key in complete for key in scope['required_artifact_ids']},
                  'required_material_delivered': True}
        if position < len(chain)-1:
            previous_requests = answer.get('evidence_requests')
            require(set(answer) == {'evidence_requests'} and isinstance(previous_requests, list) and previous_requests
                    and all(isinstance(v, str) for v in previous_requests) and not set(previous_requests) <= seen_requests,
                    'predecessor is not a novel explicit evidence request')
            if meta['document_audit']['required_material_delivered'] is not True:
                prior = delivery.regular(Path(root)/'host/runtime'/call['name']/FILE, root)
                require(delivery.read(prior) == result, 'predecessor lacks prospective delivery receipt')
            seen_requests.update(previous_requests)
        coverage = {key: scope['readonly_artifacts'][key]['sha256'] for key in complete}
        previous_scope = scope
    return result


def independent(engine, receipt):
    problem = engine.problem
    forbidden = set(getattr(problem, 'implementers', [])) | {getattr(problem, 'session', None)}
    forbidden.update(call.get('session_id') for call in getattr(problem, 'calls', [])
                     if not call.get('module', '').startswith('paper-'))
    require(receipt['session_id'] not in forbidden, 'reviewer collides with research identity')
    return receipt


def record(engine, name):
    result = independent(engine, compute(engine.problem.pilot.root, engine.root, engine.ledger, name))
    path = engine.problem.pilot.host/'runtime'/name/FILE
    with path.open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
    return True


def delivered(engine, meta):
    if meta.get('document_audit', {}).get('required_material_delivered') is True:
        return True
    path = engine.problem.pilot.host/'runtime'/meta['name']/FILE
    if not path.is_file():
        return False
    return delivery.read(delivery.regular(path, engine.problem.pilot.root)) == independent(engine, compute(
        engine.problem.pilot.root, engine.root, engine.ledger, meta['name']))
