"""Authenticated request-only turns confer no evidence coverage or acceptance."""
import copy
import json
import os
import re
from pathlib import Path

import pilot_document_tools as documents
import pilot_paper_delivery as delivery
import pilot_paper_initial_review as initial

require = initial.require


def exact_stage(engine, call, stage):
    return re.fullmatch(re.escape(engine.problem.ident)+r'/paper-\d+-'+re.escape(stage),
                        call.get('name', '')) is not None


def authenticate(engine, call, stage, writer):
    require(exact_stage(engine, call, stage), 'request stage identity changed')
    require(stage == engine.ledger['stage'] or
            (writer and stage == 'repair-'+engine.ledger['stage']), 'request belongs to another semantic paper stage')
    directory = engine.problem.pilot.host/'runtime'/call['name']
    names = ('stage.meta.json', 'stage.answer.txt', 'stage.answer.json', 'stage.prompt.txt',
             'document-capability.json', 'document-operations.jsonl', 'stage.events.jsonl')
    paths = {name: delivery.regular(directory/name, engine.problem.pilot.root) for name in names}
    meta, scope = delivery.read(paths['stage.meta.json']), delivery.read(paths['document-capability.json'])
    require(meta.get('name') == call['name'] and meta.get('module') == 'paper-'+stage
            and meta.get('status') == 'completed' and meta.get('turn_completed') is True
            and meta.get('model_actual') == 'gpt-6-astra' and meta.get('model_verified') is True
            and isinstance(meta.get('session_id'), str) and meta['session_id']
            and meta.get('exit_code') == 0 and not meta.get('protocol_errors')
            and meta.get('persisted_rollout_audit', {}).get('status') == 'verified',
            'request transport is not authenticated')
    require(all(call.get(k) == meta.get(k) for k in
                ('status', 'session_id', 'answer_sha256', 'request_id', 'prompt_sha256')),
            'request ledger differs from transport')
    require(delivery.digest(paths['stage.answer.txt']) == meta.get('answer_sha256')
            and delivery.digest(paths['stage.prompt.txt']) == meta.get('prompt_sha256')
            and delivery.digest(paths['document-capability.json']) == meta.get('document_capability', {}).get('sha256'),
            'request transport bytes changed')
    answer, _, error = delivery.extract_answer(paths['stage.answer.txt'].read_text())
    require(not error and answer == delivery.read(paths['stage.answer.json'])
            and isinstance(answer, dict) and set(answer) == {'evidence_requests'}
            and isinstance(answer['evidence_requests'], list) and answer['evidence_requests']
            and all(isinstance(v, str) and v for v in answer['evidence_requests']),
            'response is not solely evidence requests')
    require(scope['producer'] == {'stage':call['name'], 'request_id':meta['request_id'], 'session_id':meta.get('resume_session')}
            and scope['problem_id'] == engine.problem.ident
            and scope['original_sha256'] == delivery.digest(engine.snapshot/'input.txt')
            and scope['main_session'] == (engine.ledger.get('writer_session') or 'paper-initial-reconstruction'), 'request scope identity changed')

    # Internal capability members rebase on native continuation. External
    # members were already explicitly host-scoped; authenticate those exact
    # canonical bytes, without deriving paths from the model's requests.
    old_store = Path(scope['store_root'])
    require(old_store.is_absolute() and old_store.resolve()==old_store, 'request store is not canonical')
    for ref in scope['readonly_artifacts'].values():
        original = Path(ref['path'])
        copied = (delivery.regular(engine.root/original.relative_to(old_store), engine.root)
                  if original.is_relative_to(old_store) else original)
        require(documents.digest(documents.regular_bytes(copied)) == ref['sha256'], 'request scoped bytes changed')
        ref['path'] = str(copied)
    if 'public_source_store' in scope:
        allowed = {str(old_store/'public-sources'):Path('public-sources'),
                   str(old_store/'refs/public-sources'):Path('refs/public-sources')}
        require(scope['public_source_store'] in allowed, 'request public source store changed')
        scope['public_source_store'] = str(engine.root/allowed[scope['public_source_store']])
    scope['store_root'] = str(engine.root)
    scope['receipt_path'] = str(paths['document-operations.jsonl'])
    documents.validate_scope(scope)
    events = [json.loads(line)['event'] for line in paths['stage.events.jsonl'].read_text().splitlines()
              if 'event' in json.loads(line)]
    events = [event for event in events if documents.allowed_event(event, scope)]
    persisted = meta['persisted_rollout_audit']
    audit = documents.audit_operations(scope, events, persisted['tool_events'], meta['session_id'],
                                      persisted.get('tool_output_receipts', []))
    require(events == meta.get('document_events') and audit == meta.get('document_audit')
            and audit.get('status') == 'PASS' and audit.get('complete_tool_outputs_delivered') is True
            and not audit.get('errors') and not audit.get('delivery_errors'), 'request raw delivery audit differs')
    session = meta['session_id']
    if writer:
        if stage != 'reconstruct':
            require(meta.get('resume_session')==engine.ledger.get('writer_session') and meta.get('fresh_session') is False,
                    'writer request must resume the original writer')
        require(session == engine.ledger.get('writer_session') or
                (stage == 'reconstruct' and (meta.get('fresh_session') is True or
                 session == engine.ledger.get('retrieval_progress', {}).get('session'))), 'request writer identity changed')
    else:
        forbidden = set(engine.ledger.get('writer_ids', [])) | {engine.ledger.get('writer_session'), getattr(engine.problem, 'session', None)}
        forbidden.update(getattr(engine.problem, 'implementers', []))
        forbidden.update(c.get('session_id') for c in getattr(engine.problem, 'calls', [])
                         if not c.get('module', '').startswith('paper-'))
        require(session not in forbidden, 'request reviewer is not independent')
    require((meta.get('resume_session') == session and meta.get('fresh_session') is False)
            or (meta.get('resume_session') is None and meta.get('fresh_session') is True), 'request session changed')
    admissions = [a for a in engine.ledger.get('admissions', []) if a.get('name') == call['name']]
    require(len(admissions) == 1 and admissions[0].get('stage') == stage
            and admissions[0].get('resume_session') == meta.get('resume_session'),
            'request admission session changed')
    return meta, answer, scope, {name:delivery.digest(path) for name,path in paths.items()}


def record(engine, stage, writer):
    call = engine.ledger['calls'][-1]
    meta, answer, scope, files = authenticate(engine, call, stage, writer)
    requests = answer['evidence_requests']
    for name in requests:
        relative=Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts and str(relative)==name,
                'evidence request escapes its relative scope')
    embedded = {}
    # Resolve only exact scoped aliases or immutable snapshot members. No live path reads.
    manifest = delivery.read(engine.snapshot/'manifest.json')['files']
    if stage == 'repair-raw-audit':
        for filename in ('raw-audit.json', 'raw-evidence.json'):
            path = engine.work/filename
            if path.exists():
                path = delivery.regular(path, engine.problem.pilot.root)
                path.read_text(encoding='utf-8')
                key = 'repair-diagnostic:'+filename
                scope['readonly_artifacts'][key] = {'path':str(path), 'sha256':delivery.digest(path), 'media_type':'application/json'}
                if key not in scope['required_artifact_ids']: scope['required_artifact_ids'].append(key)
    for name in requests:
        if writer and len(Path(name).parts)==2 and Path(name).parts[0]=='work' and 'stage-input' in scope['readonly_artifacts']:
            source=scope['readonly_artifacts']['stage-input']
            body=documents.regular_bytes(Path(source['path']))
            require(documents.digest(body)==source['sha256'], 'embedded request source bytes changed')
            try: payload=json.loads(body)
            except ValueError: payload={}
            from pilot_paper_efficiency import artifact_text
            member=artifact_text(payload,Path(name).name) if isinstance(payload,dict) else None
            if member is not None:
                require(isinstance(member,str), 'embedded request is not a text artifact')
                directory=engine.root/'input-artifacts'
                require(directory.resolve()==directory, 'embedded request directory contains aliases')
                directory.mkdir(exist_ok=True)
                data=member.encode('utf-8');path=directory/(documents.digest(data)+'.txt')
                if path.exists():
                    require(documents.regular_bytes(path)==data, 'embedded request member changed')
                else:
                    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
                    with os.fdopen(fd,'wb') as stream:
                        stream.write(data);stream.flush();os.fsync(stream.fileno())
                fixed={'path':str(path),'sha256':documents.digest(data),'media_type':'text/plain'}
                scope['readonly_artifacts']['archive:'+name]=fixed
                embedded[name]={'stage_input_sha256':source['sha256'],'member':Path(name).name,'sha256':fixed['sha256']}
        for key, ref in list(scope['readonly_artifacts'].items()):
            path = Path(ref['path'])
            if name == key or (path.is_relative_to(engine.root) and name == str(path.relative_to(engine.root))):
                scope['readonly_artifacts']['archive:'+name] = copy.deepcopy(ref)
        if name in manifest and 'archive:'+name not in scope['readonly_artifacts']:
            data = engine.snapshot_bytes(name)
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                continue  # Fixed provenance exists, but no readable text capability was supplied.
            if data.startswith((b'%PDF-', b'PK\x03\x04', b'\x1f\x8b')):
                continue
            scope['readonly_artifacts']['archive:'+name] = {'path':str(engine.snapshot/name),
                'sha256':manifest[name], 'media_type':'text/plain'}
    successor = scope
    unavailable = []
    for name in requests:
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts and str(relative) == name,
                'evidence request escapes its relative scope')
        try:
            current_scope = {**successor, 'producer':{}, 'receipt_path':''}
            if 'public_source_store' in scope:
                cache = Path(scope['public_source_store'])
                require(cache in {engine.root/'public-sources', engine.root/'refs/public-sources'}
                        and cache.resolve() == cache, 'requested cache is outside the preserved host scope')
                current_scope['public_source_store'] = str(cache)
                prefix = cache.relative_to(engine.root)
                if relative.is_relative_to(prefix):
                    parts = relative.relative_to(prefix).parts
                    require(len(parts) >= 2 and re.fullmatch(r'[0-9a-f]{64}', parts[0]), 'invalid requested source member')
                    receipt = cache/parts[0]/'receipt.json'
                    require(receipt.resolve() == receipt, 'requested source receipt contains symlinks')
                    if not receipt.exists():
                        unavailable.append(name)
                        continue
            successor, missing = initial.requested_scope(current_scope, [name])
            unavailable.extend(missing)
        except ValueError as error:
            if str(error) not in ('requested cache source is unavailable', 'requested cache path has no verified readable members'):
                raise
            unavailable.append(name)
    for key in ('producer', 'receipt_path', 'public_source_store'): successor.pop(key, None)
    binding = {'stage':stage, 'writer':writer, 'call':call['name'], 'session':meta['session_id'],
               'files_sha256':files, 'scope_sha256':delivery.scope_binding(successor),
               'evidence_requests':requests, 'unavailable_requests':unavailable}
    if embedded:
        binding['embedded_requests']=embedded
        binding['authority']='request-only routing; historical rejection and substantive gates unchanged'
    records = engine.ledger.setdefault('request_only_turns', [])
    old = next((r for r in records if r['call'] == call['name']), None)
    require(old is None or old == binding, 'saved request binding changed')
    chain_names = set()
    for prior in reversed(engine.ledger['calls'][:-1]):
        if not exact_stage(engine, prior, stage) or prior.get('session_id') != meta['session_id']: break
        chain_names.add(prior['name'])
    previous = {item for r in records if r['call'] in chain_names for item in r['evidence_requests']}
    require(not set(requests) <= previous, 'paper evidence request made no progress')
    if old is None: records.append(binding)
    current = engine.ledger.setdefault('evidence_requests', {}).setdefault(stage, [])
    current.extend(name for name in requests if name not in current)
    ids = engine.ledger['writer_ids' if writer else 'reader_ids']
    if meta['session_id'] not in ids: ids.append(meta['session_id'])
    engine.ledger['retrieval_progress']['session'] = meta['session_id']
    engine.request_only_scope = successor
    engine.request_only_stage = stage
    engine.request_only_unavailable = unavailable
    engine.save()
    return meta['session_id'], answer


def restore(engine, stage, writer):
    pending = engine.ledger.get('retrieval_progress')
    if not pending or pending.get('stage') != stage or pending.get('writer') is not writer:
        return False
    if (not writer and stage != 'proof-audit'
            and not any(r['stage'] == stage for r in engine.ledger.get('request_only_turns', []))):
        return False  # Existing independently receipted reviewer recovery retains its own contract.
    if not engine.ledger['calls']: return False
    call = engine.ledger['calls'][-1]
    if not exact_stage(engine, call, stage): return False
    if call.get('status') != 'completed': return False
    answer_path = engine.problem.pilot.host/'runtime'/call['name']/'stage.answer.json'
    if not answer_path.is_file(): return False
    answer = delivery.read(delivery.regular(answer_path, engine.problem.pilot.root))
    if not isinstance(answer, dict) or set(answer) != {'evidence_requests'}: return False
    chain = []
    for item in reversed(engine.ledger['calls']):
        if not exact_stage(engine, item, stage): break
        chain.append(item)
    require(pending['turns'] == len(chain) and 1 <= pending['turns'] <= 4,
            'request retrieval budget changed')
    session = pending.get('session')
    previous_session = None
    for item in reversed(chain):
        meta, _, _, _ = authenticate(engine, item, stage, writer)
        if previous_session is None and not writer:
            require(meta.get('fresh_session') is True and meta.get('resume_session') is None,
                    'reviewer request chain must start with a fresh independent session')
        if previous_session is not None:
            require(meta.get('resume_session') == previous_session and meta.get('fresh_session') is False,
                    'saved request chain changed session')
        require(session in (None, meta['session_id']), 'saved request session changed')
        session = meta['session_id']
        previous_session = session
    engine.reconciled_retrieval_calls = {item['name'] for item in chain}
    engine.next_call_number()
    record(engine, stage, writer)
    return True
