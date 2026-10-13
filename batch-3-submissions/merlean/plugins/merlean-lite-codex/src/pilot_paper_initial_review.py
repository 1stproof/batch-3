"""Resume an initial evidence-only source-review interruption without accepting it.

No historical coverage is inherited. The immediate successor must reread the
entire preserved scope, including exactly verified requested cache members.
"""
import copy
import json
from pathlib import Path

import pilot_document_tools as documents
import pilot_paper_delivery as delivery
import pilot_paper_read_delivery as reads
from pilot_public_sources import verify_public_source

require = reads.require


def authenticate(engine, call):
    root = engine.problem.pilot.root
    directory = engine.problem.pilot.host/'runtime'/call['name']
    names = ('stage.meta.json', 'stage.answer.txt', 'stage.answer.json', 'stage.prompt.txt',
             'document-capability.json', 'document-operations.jsonl', 'stage.events.jsonl')
    paths = {name: delivery.regular(directory/name, root) for name in names}
    meta = delivery.read(paths['stage.meta.json'])
    scope = delivery.read(paths['document-capability.json'])
    documents.validate_scope(scope)
    require(meta.get('name') == call['name'] and meta.get('module') == 'paper-'+engine.ledger['stage']
            and meta.get('status') == 'completed' and meta.get('turn_completed') is True
            and meta.get('model_actual') == 'gpt-6-astra' and meta.get('model_verified') is True
            and meta.get('fresh_session') is True and meta.get('resume_session') is None
            and isinstance(meta.get('session_id'), str) and meta['session_id']
            and not meta.get('protocol_errors') and meta.get('exit_code') == 0
            and meta.get('persisted_rollout_audit', {}).get('status') == 'verified',
            'initial reviewer transport is not authenticated')
    require(all(call.get(k) == meta.get(k) for k in
                ('name', 'status', 'session_id', 'answer_sha256', 'request_id', 'prompt_sha256')),
            'initial reviewer ledger differs from transport')
    require(delivery.digest(paths['stage.answer.txt']) == meta['answer_sha256']
            and delivery.digest(paths['stage.prompt.txt']) == meta['prompt_sha256']
            and delivery.digest(paths['document-capability.json']) == meta['document_capability']['sha256'],
            'initial reviewer transport bytes changed')
    answer, _, error = delivery.extract_answer(paths['stage.answer.txt'].read_text())
    require(not error and answer == delivery.read(paths['stage.answer.json'])
            and isinstance(answer, dict) and set(answer) == {'evidence_requests'}
            and isinstance(answer['evidence_requests'], list) and answer['evidence_requests']
            and all(isinstance(v, str) and v for v in answer['evidence_requests']),
            'initial reviewer did not return solely evidence requests')
    require(scope['producer'] == {'stage': call['name'], 'request_id': meta['request_id'], 'session_id': None}
            and scope['problem_id'] == engine.problem.ident and scope['mode'] == 'review'
            and scope['store_root'] == str(engine.root.resolve())
            and scope['original_sha256'] == delivery.digest(engine.snapshot/'input.txt')
            and scope['main_session'] == engine.ledger.get('writer_session'), 'initial reviewer scope identity changed')
    events = [json.loads(line)['event'] for line in paths['stage.events.jsonl'].read_text().splitlines()
              if 'event' in json.loads(line)]
    events = [event for event in events if documents.allowed_event(event, scope)]
    persisted = meta['persisted_rollout_audit']
    audit = documents.audit_operations(scope, events, persisted['tool_events'], meta['session_id'],
                                      persisted.get('tool_output_receipts', []))
    require(events == meta.get('document_events') and audit == meta.get('document_audit')
            and audit.get('status') == 'PASS' and audit.get('complete_tool_outputs_delivered') is True
            and not audit.get('errors') and not audit.get('delivery_errors')
            and audit.get('required_material_delivered') is False,
            'initial request raw delivery audit differs')
    forbidden = set(engine.ledger.get('writer_ids', [])) | {engine.ledger.get('writer_session'),
        getattr(engine.problem, 'session', None)} | set(getattr(engine.problem, 'implementers', []))
    forbidden.update(c.get('session_id') for c in getattr(engine.problem, 'calls', []))
    require(meta['session_id'] not in forbidden, 'initial source reviewer is not independent')
    return meta, answer, scope, {name: delivery.digest(path) for name, path in paths.items()}


def requested_scope(scope, requests):
    scope = copy.deepcopy(scope)
    unresolved = []
    store = Path(scope['store_root'])
    cache = Path(scope['public_source_store']) if 'public_source_store' in scope else None
    if cache is not None:
        require(cache in {store/'public-sources', store/'refs/public-sources'}
                and cache.resolve() == cache,
                'requested cache is outside the preserved host scope')
    for name in requests:
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts and str(relative) == name,
                'initial evidence request escapes its relative scope')
        if 'archive:'+name in scope['readonly_artifacts']:
            key = 'archive:'+name
            if key not in scope['required_artifact_ids']: scope['required_artifact_ids'].append(key)
            continue
        prefix = cache.relative_to(store) if cache is not None else None
        if prefix is None or not relative.is_relative_to(prefix):
            unresolved.append(name)
            continue
        parts = relative.relative_to(prefix).parts
        require(len(parts) >= 2, 'invalid requested source member')
        require(cache.is_dir(), 'requested cache source is unavailable')
        source = verify_public_source(cache, parts[0])
        require(source['status'] == 'downloaded', 'requested cache source is unavailable')
        member = '/'.join(parts[1:])
        members = source['members'] if member == 'raw' else [m for m in source['members'] if m['member'] == member]
        require(members, 'requested cache path has no verified readable members')
        for entry in members:
            path = delivery.regular(cache/parts[0]/entry['member'], cache)
            require(delivery.digest(path) == entry['sha256'], 'requested source hash changed')
            path.read_text(encoding='utf-8')
            key = 'requested-cache:'+str(path.relative_to(store))
            scope['readonly_artifacts'][key] = {'path': str(path), 'sha256': entry['sha256'], 'media_type': 'text/plain'}
            if key not in scope['required_artifact_ids']: scope['required_artifact_ids'].append(key)
    scope.pop('producer'); scope.pop('receipt_path')
    scope.pop('public_source_store', None)  # Successor exposes fixed text only; no fresh fetch/search.
    return scope, unresolved


def restore(engine, stage, writer):
    """Only the untouched first underdelivered request, never a verdict or retry."""
    progress = engine.ledger.get('retrieval_progress')
    if writer or stage not in reads.STAGES or stage != engine.ledger['stage'] or not progress:
        return False
    calls = []
    for call in reversed(engine.ledger['calls']):
        if not call.get('name', '').endswith('-'+stage): break
        calls.append(call)
    if len(calls) != 1 or progress.get('turns') != 1:
        return False
    call = calls[0]
    if call.get('document_audit', {}).get('required_material_delivered') is not False:
        return False
    meta, answer, scope, files = authenticate(engine, call)
    require(stage not in engine.ledger['completed'] and not engine.ledger.get('evidence_requests', {}).get(stage),
            'initial request was already processed')
    admissions = [a for a in engine.ledger['admissions'] if a.get('name') == call['name']]
    require(len(admissions) == 1 and admissions[0].get('stage') == stage
            and admissions[0].get('resume_session') is None, 'initial request admission changed')
    successor, unresolved = requested_scope(scope, answer['evidence_requests'])
    binding = {'call': call['name'], 'files_sha256': files, 'scope_sha256': delivery.scope_binding(successor),
               'evidence_requests': answer['evidence_requests'], 'unavailable_requests': unresolved}
    old = engine.ledger.get('initial_review_request')
    expected = {'stage':stage, 'session':meta['session_id'], 'turns':1, 'writer':False}
    require((old is None and progress == {**expected, 'session':None})
            or (old == binding and progress == expected), 'initial request checkpoint or budget changed')
    engine.reconciled_retrieval_calls = {call['name']}
    engine.next_call_number()  # All terminal ownership checks precede state changes.
    engine.ledger['initial_review_request'] = binding
    engine.ledger['retrieval_progress'] = expected
    if meta['session_id'] not in engine.ledger['reader_ids']:
        engine.ledger['reader_ids'].append(meta['session_id'])
    engine.initial_review_scope = successor
    engine.initial_review_unavailable = unresolved
    engine.initial_review_stage = stage
    engine.save()
    return True
