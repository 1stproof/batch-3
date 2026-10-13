"""Explicit first-writer continuation on revised evidence, within existing turns.

Only a stopped, native-validated parent can authorize this successor operation.
Old snapshots, rejected output and counters remain history, never acceptance.
"""
import hashlib
import json
from pathlib import Path
import re
from types import SimpleNamespace

import pilot_paper_delivery as delivery

FILE = 'paper-recovery.json'
RULE = 'first-writer-revised-evidence-v1'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def binding(source, ident, saved):
    source = Path(source).resolve()
    require(re.fullmatch(r'[A-Za-z0-9_-]+', ident), 'invalid recovery problem')
    folder = source/'exam/papers'/ident
    ledger = delivery.read(delivery.regular(folder/'paper-ledger.json', source))
    calls = ledger.get('calls', [])
    require(len(calls) == 1 and ledger.get('stage') == 'reconstruct'
            and not ledger.get('completed') and not ledger.get('writer_ids')
            and not ledger.get('reader_ids') and not ledger.get('writer_session')
            and not ledger.get('delivery_remediation_admissions')
            and not ledger.get('paper_recovery_admissions'), 'not an untouched first-writer rejection')
    name = calls[0].get('name', '')
    require(re.fullmatch(re.escape(ident)+r'/paper-\d+-reconstruct', name), 'invalid rejected stage')
    stage = source/'host/runtime'/name
    paths = {key: delivery.regular(stage/file, source) for key, file in (
        ('meta', 'stage.meta.json'), ('raw', 'stage.answer.txt'), ('parsed', 'stage.answer.json'),
        ('prompt', 'stage.prompt.txt'), ('capability', 'document-capability.json'))}
    meta, capability = delivery.read(paths['meta']), delivery.read(paths['capability'])
    session = meta.get('session_id')
    from datetime import datetime
    start, end = datetime.fromisoformat(meta['start_utc']), datetime.fromisoformat(meta['end_utc'])
    audit = meta.get('document_audit', {})
    require(start.tzinfo and end.tzinfo and end >= start and type(meta.get('pid')) is int
            and meta['pid'] > 1 and type(meta.get('exit_code')) is int
            and meta.get('name') == name and meta.get('module') == 'paper-reconstruct'
            and meta.get('status') == 'completed' and meta.get('turn_completed') is True
            and meta.get('model_actual') == 'gpt-6-astra' and meta.get('model_verified') is True
            and isinstance(session, str) and session and meta.get('fresh_session') is True
            and meta.get('resume_session') is None
            and meta.get('persisted_rollout_audit', {}).get('status') == 'verified'
            and audit.get('status') == 'PASS' and audit.get('required_material_delivered') is False
            and audit.get('complete_tool_outputs_delivered') is True
            and not audit.get('errors') and not audit.get('delivery_errors'),
            'first-writer response is not an authenticated delivery-only rejection')
    require(all(calls[0].get(k) == meta.get(k) for k in
                ('name', 'status', 'session_id', 'answer_sha256', 'request_id', 'prompt_sha256')),
            'rejected ledger differs from transport')
    require(session not in set(saved['implementers']) | {c.get('session_id') for c in saved['calls']},
            'rejected writer collides with research identity')
    progress = {'stage': 'reconstruct', 'session': None, 'turns': 1, 'writer': True}
    require(ledger.get('retrieval_progress') == progress and len(ledger.get('admissions', [])) == 1
            and ledger['admissions'][0].get('name') == name
            and ledger['admissions'][0].get('resume_session') is None,
            'original first-turn budget or admission changed')
    require(delivery.digest(paths['raw']) == meta.get('answer_sha256')
            and delivery.digest(paths['prompt']) == meta.get('prompt_sha256')
            and delivery.digest(paths['capability']) == meta.get('document_capability', {}).get('sha256'),
            'rejected bytes changed')
    answer, _, error = delivery.extract_answer(paths['raw'].read_text())
    require(not error and isinstance(answer, dict) and isinstance(answer.get('tex'), str)
            and answer == delivery.read(paths['parsed']) and 'evidence_requests' not in answer,
            'rejected substantive draft missing')
    require(capability.get('producer') == {'stage': name, 'request_id': meta.get('request_id'), 'session_id': None}
            and capability.get('mode') == 'review' and capability.get('problem_id') == ident
            and capability.get('main_session') == 'paper-initial-reconstruction',
            'fresh capability producer changed')
    required = capability.get('required_artifact_ids', [])
    artifacts = capability.get('readonly_artifacts', {})
    require(required and 'stage-input' in required and len(required) == len(set(required))
            and set(required) <= set(artifacts)
            and audit.get('required_artifact_coverage') == {key: False for key in required},
            'first-writer original delivery census changed')
    # Only copied confined bytes may be exposed; declared historical absolute paths
    # are mapped relative to their exact old store, never read as external inputs.
    old_store = Path(capability['store_root'])
    mapped = {}
    for key, ref in artifacts.items():
        declared = Path(ref['path'])
        require(old_store.is_absolute() and declared.is_relative_to(old_store), 'old scope escapes store')
        relative = declared.relative_to(old_store)
        path = delivery.regular(folder/relative, folder)
        require(delivery.digest(path) == ref['sha256'], 'old source bytes changed')
        mapped[key] = {'path': str(relative), 'sha256': ref['sha256'], 'media_type': ref['media_type']}
    original = delivery.digest(source/'campaign/problems'/ident/'input.txt')
    require(capability.get('original_sha256') == original
            and delivery.digest(folder/'snapshot/input.txt') == original, 'original scope changed')
    proof = source/'campaign/problems'/ident/'proof-current.json'
    old_proof = folder/'snapshot/evidence/proof-current.json'
    require(saved.get('proof_document', {}).get('status') == 'submitted' and old_proof.is_file()
            and delivery.read(proof) != delivery.read(old_proof), 'no new submitted proof evidence')
    # Native replay proves current candidate provenance; require changed scientific
    # candidate bytes as well as a different pointer, not a renamed revision.
    old_snapshot = delivery.read(folder/'snapshot/snapshot.json')
    from codex_pilot import triage_binding
    require(triage_binding(old_snapshot.get('current', {})) != triage_binding(saved['current']),
            'unchanged research cannot renew paper delivery')
    return {'problem': ident, 'stage': name, 'session_id': session, 'retrieval_progress': progress,
            'files': {k: delivery.digest(p) for k, p in paths.items()},
            'ledger_sha256': delivery.digest(folder/'paper-ledger.json'),
            'old_snapshot_sha256': delivery.digest(folder/'snapshot/manifest.json'),
            'original_sha256': original, 'original_artifacts': mapped, 'required_artifacts': required,
            'proof_pointer_sha256': delivery.digest(proof),
            'current_candidate_sha256': hashlib.sha256(encoded(saved['current'])).hexdigest()}


def make_request(source, target, reconciliation, problems, *, authority):
    from pilot_continuation import validate_and_load
    checkpoint = validate_and_load(Path(source), reconciliation=Path(reconciliation))
    return request_from_checkpoint(source, target, checkpoint, problems, authority=authority)


def request_from_checkpoint(source, target, checkpoint, problems, *, authority):
    source, target = Path(source).resolve(), Path(target).resolve()
    require(isinstance(authority, str) and authority.strip(), 'explicit paper recovery authority required')
    require(isinstance(problems, list) and problems and len(problems) == len(set(problems))
            and set(problems) <= set(checkpoint['problems']), 'duplicate or unknown recovery problem')
    require(not target.exists() and target != source and not target.is_relative_to(source)
            and not source.is_relative_to(target), 'recovery requires separate new successor')
    require(checkpoint['config'].get('exam') and checkpoint['parent']['source_root'] == str(source),
            'native stopped exam checkpoint required')
    previous = {ident for old, _ in all_requests(source, checkpoint['config']) for ident in old['problems']}
    require(not previous.intersection(problems), 'problem already has a paper recovery authorization')
    return {'schema_version': 1, 'rule': RULE, 'source_root': str(source), 'target_root': str(target),
            'parent_manifest_sha256': checkpoint['parent']['manifest_sha256'], 'authority': authority,
            'maximum_admissions_per_problem': 1, 'existing_turn_limit': 4,
            'problems': {ident: binding(source, ident, checkpoint['problems'][ident]) for ident in sorted(problems)}}


def validate_request(request, source, target, checkpoint):
    expected = request_from_checkpoint(source, target, checkpoint, list(request.get('problems', {})),
                                       authority=request.get('authority'))
    require(request == expected, 'paper recovery request differs from exact stopped parent/target')


def all_requests(root, config):
    refs = list(config.get('paper_recovery_history', []))
    if config.get('paper_recovery') is not None:
        require(config['paper_recovery'].get('path') == FILE, 'invalid current recovery reference')
        refs.append(config['paper_recovery'])
    result, seen = [], set()
    for ref in refs:
        require(ref.get('path') == FILE or ref.get('path') == 'paper-recovery-history/'+str(ref.get('sha256'))+'.json',
                'invalid paper recovery reference')
        path = delivery.regular(Path(root)/ref['path'], Path(root))
        require(delivery.digest(path) == ref.get('sha256'), 'paper recovery authorization changed')
        request = delivery.read(path)
        require(request['rule'] == RULE and request['existing_turn_limit'] == 4
                and request['maximum_admissions_per_problem'] == 1, 'invalid recovery rule/budget')
        require(not seen.intersection(request['problems']), 'duplicate problem recovery authority')
        seen.update(request['problems'])
        result.append((request, ref))
    return result


def load(root, config, ident=None):
    values = all_requests(root, config)
    if ident is None:
        return values[-1][0] if values else None
    return next((request for request, _ in values if ident in request['problems']), None)


def authorization(root, config, ident):
    return next(ref['sha256'] for request, ref in all_requests(root, config) if ident in request['problems'])


def install(root, config, checkpoint, campaign):
    """Only prepare_continuation calls this, in its new successor before launch."""
    from pilot_exam import ExamRuntime
    root = Path(root)
    request = load(root, config)
    require(request['target_root'] == str(root.resolve()), 'wrong recovery successor')
    runtime = ExamRuntime(config['exam'])
    parent_state_path = Path(request['source_root'])/'campaign/state.json'
    require(delivery.digest(parent_state_path) == checkpoint['parent']['files']['campaign/state.json'],
            'authenticated parent research status changed')
    parent_state = delivery.read(parent_state_path)
    for ident, item in request['problems'].items():
        folder = runtime.paper_dir(ident)
        ledger = delivery.read(folder/'paper-ledger.json')
        require(delivery.digest(root/'campaign/problems'/ident/'proof-current.json') == item['proof_pointer_sha256'],
                'current proof changed before snapshot')
        saved = checkpoint['problems'][ident]
        if parent_state['problems'][ident].get('successful_complete') is True:
            carried = campaign.status()['problems'][ident]
            require(carried.get('successful_complete') is True
                    and carried.get('manifest') == parent_state['problems'][ident].get('manifest'),
                    'accepted research was not independently carried')
        problem = SimpleNamespace(ident=ident, folder=root/'campaign/problems'/ident,
            original_bytes=(root/'campaign/problems'/ident/'input.txt').read_bytes(),
            pilot=SimpleNamespace(campaign=SimpleNamespace(status=lambda: parent_state)), current=saved['current'], dossier=saved['dossier'],
            findings=saved['findings'], errors=saved['errors'], execution_history=saved['execution_history'],
            final_assessment_history=saved['final_assessment_history'], advisory_scope_history=saved['advisory_scope_history'],
            calls=saved['calls'])
        name = 'snapshot-recovery-' + config['paper_recovery']['sha256'][:24]
        snapshot = runtime.snapshot(problem, recovery_destination=name)
        transition = {'rule': RULE, 'authorization_sha256': config['paper_recovery']['sha256'],
                      'old_snapshot': 'snapshot', 'old_manifest_sha256': item['old_snapshot_sha256'],
                      'new_snapshot': name, 'new_manifest_sha256': delivery.digest(snapshot/'manifest.json'),
                      'proof_pointer_sha256': item['proof_pointer_sha256']}
        transition_path = folder/('recovery-transition-'+config['paper_recovery']['sha256'][:24]+'.json')
        with transition_path.open('xb') as stream:
            stream.write(encoded(transition))
        transition_path.chmod(0o444)
        config.setdefault('paper_recovery_transitions', {})[ident] = {
            'path': str(transition_path.relative_to(root)), 'sha256': delivery.digest(transition_path)}
        ledger['paper_recovery_transition'] = transition
        ledger['snapshot'] = str(snapshot)
        ledger['snapshot_manifest'] = {'path': str(snapshot/'manifest.json'), 'sha256': transition['new_manifest_sha256']}
        (folder/'paper-ledger.json').write_text(json.dumps(ledger, indent=2, sort_keys=True)+'\n')


def active_snapshot(problem, runtime):
    request = load(problem.pilot.root, problem.pilot.config, problem.ident)
    if request is None or problem.ident not in request['problems']:
        return None
    folder = runtime.paper_dir(problem.ident)
    ledger = delivery.read(folder/'paper-ledger.json')
    item = request['problems'][problem.ident]
    transition = ledger.get('paper_recovery_transition', {})
    require(transition == transition_receipt(problem.pilot.root, problem.pilot.config,
                                             runtime.root, problem.ident), 'paper transition receipt differs')
    auth = authorization(problem.pilot.root, problem.pilot.config, problem.ident)
    name = 'snapshot-recovery-' + auth[:24]
    require(transition.get('rule') == RULE and transition.get('new_snapshot') == name
            and transition.get('authorization_sha256') == auth
            and transition.get('old_manifest_sha256') == item['old_snapshot_sha256']
            and delivery.digest(folder/'snapshot/manifest.json') == item['old_snapshot_sha256']
            and delivery.digest(folder/name/'manifest.json') == transition.get('new_manifest_sha256')
            and delivery.digest(folder/name/'evidence/proof-current.json') == item['proof_pointer_sha256']
            and delivery.digest(Path(problem.pilot.root)/'campaign/problems'/problem.ident/'proof-current.json') == item['proof_pointer_sha256']
            and ledger['snapshot_manifest'] == {'path': str(folder/name/'manifest.json'), 'sha256': transition.get('new_manifest_sha256')}
            and ledger['snapshot'] == str((folder/name).resolve()), 'paper evidence transition changed')
    runtime.verify_snapshot(folder/'snapshot', check_budget=lambda: runtime.paper_timeout(1))
    runtime.verify_snapshot(folder/name, check_budget=lambda: runtime.paper_timeout(1))
    return folder/name


def transition_receipt(source, config, exam, ident):
    reference = config.get('paper_recovery_transitions', {}).get(ident, {})
    auth = authorization(source, config, ident)
    expected = 'exam/papers/'+ident+'/recovery-transition-'+auth[:24]+'.json'
    require(reference.get('path') == expected, 'missing pinned paper transition receipt')
    path = delivery.regular(Path(exam)/Path(expected).relative_to('exam'), Path(exam))
    require(delivery.digest(path) == reference.get('sha256'), 'paper transition receipt changed')
    return delivery.read(path)


def snapshot_paths(source, exam):
    """Enumerate only native or authorization-bound versioned snapshot locations."""
    source, exam = Path(source), Path(exam)
    paths = [p.parent for p in exam.glob('papers/*/snapshot/manifest.json')]
    config_path = source/'host-config.json'
    config = delivery.read(config_path) if config_path.is_file() else {}
    for ledger_path in exam.glob('papers/*/paper-ledger.json'):
        transition = delivery.read(ledger_path).get('paper_recovery_transition')
        if transition is None:
            continue
        ident = ledger_path.parent.name
        request = load(source, config, ident)
        require(request is not None and ident in request['problems'], 'unbound versioned snapshot')
        item = request['problems'][ident]
        require(transition == transition_receipt(source, config, exam, ident), 'snapshot transition is not pinned')
        auth = authorization(source, config, ident)
        name = 'snapshot-recovery-' + auth[:24]
        folder = ledger_path.parent
        require(transition.get('rule') == RULE and transition.get('new_snapshot') == name
                and transition.get('authorization_sha256') == auth
                and transition.get('old_manifest_sha256') == item['old_snapshot_sha256']
                and delivery.digest(folder/'snapshot/manifest.json') == item['old_snapshot_sha256']
                and delivery.digest(folder/name/'manifest.json') == transition.get('new_manifest_sha256')
                and delivery.digest(folder/name/'evidence/proof-current.json') == item['proof_pointer_sha256'],
                'versioned snapshot provenance changed')
        paths.append(folder/name)
    return paths


async def resume(engine, request, task, payload):
    item = request['problems'][engine.problem.ident]
    root = engine.problem.pilot.root
    active_snapshot(engine.problem, engine.runtime)
    stage = root/'host/runtime'/item['stage']
    for key, name in [('meta', 'stage.meta.json'), ('raw', 'stage.answer.txt'), ('parsed', 'stage.answer.json'),
                      ('prompt', 'stage.prompt.txt'), ('capability', 'document-capability.json')]:
        require(delivery.digest(stage/name) == item['files'][key], 'preserved rejection changed')
    attempts = engine.ledger.get('paper_recovery_admissions', [])
    auth = authorization(root, engine.problem.pilot.config, engine.problem.ident)
    if attempts:
        require(len(attempts) == 1 and attempts[0]['authorization_sha256'] == auth,
                'paper recovery admission already consumed')
        # Reuse exact admitted capability, not a regenerated input whose public
        # source catalog may have grown during the completed interrupted turn.
        admitted = root/'host/runtime'/attempts[0]['name']
        require((admitted/'document-capability.json').is_file(), 'admitted recovery lacks its exact capability')
        scope = delivery.read(admitted/'document-capability.json')
        require(delivery.scope_binding(scope) == attempts[0]['scope_sha256'], 'admitted recovery scope changed')
        old_store = Path(scope['store_root'])
        for ref in scope['readonly_artifacts'].values():
            path = Path(ref['path'])
            require(path.is_relative_to(old_store), 'admitted recovery source escapes store')
            copied = delivery.regular(engine.root/path.relative_to(old_store), engine.root)
            require(delivery.digest(copied) == ref['sha256'], 'admitted recovery source changed')
            ref['path'] = str(copied)
        identity, answer = delivery.reconcile_completed(engine, {'binding': item}, scope, attempts[0])
        return finish(engine, item, attempts[0], identity, answer)
    _, scope = engine.scoped_payload('reconstruct', payload)
    scope['main_session'] = item['session_id']
    manifest = delivery.read(engine.snapshot/'manifest.json')['files']
    snapshot = delivery.read(engine.snapshot/'snapshot.json')
    current_files = ['snapshot.json', 'evidence/proof-current.json', 'evidence/proof.md',
                     'evidence/current-candidate.json']
    accepted_manifest = snapshot.get('research_status', {}).get('manifest')
    if snapshot.get('research_status', {}).get('successful_complete') is True:
        require(isinstance(accepted_manifest, str), 'accepted snapshot lacks native manifest')
        current_files.append('evidence/' + accepted_manifest)
    for name in current_files:
        require(name in manifest, 'current research source missing: ' + name)
        engine.snapshot_text(name)
        key = 'current:' + name
        scope['readonly_artifacts'][key] = {'path': str(engine.snapshot/name),
            'sha256': manifest[name], 'media_type': 'text/plain'}
        scope['required_artifact_ids'].append(key)
    for key in item['required_artifacts']:
        ref = item['original_artifacts'][key]
        path = delivery.regular(engine.root/ref['path'], engine.root)
        require(delivery.digest(path) == ref['sha256'], 'historical mandatory evidence changed')
        new_key = 'historical:' + key
        scope['readonly_artifacts'][new_key] = {**ref, 'path': str(path)}
        scope['required_artifact_ids'].append(new_key)
    scope['readonly_artifacts']['unaccepted-draft'] = {'path': str(stage/'stage.answer.txt'),
        'sha256': item['files']['raw'], 'media_type': 'application/json'}
    # Scope storage must confine every artifact. Keep an exact unaccepted copy.
    quarantine = engine.root/'unaccepted-reconstruction'
    quarantine.mkdir(exist_ok=True)
    draft = quarantine/'draft.json'
    if not draft.exists():
        draft.write_bytes((stage/'stage.answer.txt').read_bytes())
    require(delivery.digest(draft) == item['files']['raw'], 'unaccepted draft changed')
    scope['readonly_artifacts']['unaccepted-draft']['path'] = str(draft)
    scope['required_artifact_ids'].append('unaccepted-draft')
    adapted = {'binding': item}
    if not attempts:
        require(engine.ledger.get('retrieval_progress') == item['retrieval_progress'], 'old retrieval checkpoint changed')
        engine.reconciled_retrieval_calls = {item['stage']}
        engine.paper_recovery_admission = {**item, 'authorization_sha256': auth}
        instruction = ('EXPLICIT CONTINUATION WITH REVISED RESEARCH EVIDENCE. The earlier draft is UNACCEPTED. '
            'Historical artifacts describe earlier evidence, not current findings or acceptance. '
            'Read EVERY mandatory artifact completely with read_required_evidence before reconstructing against '
            'the CURRENT stage-input and its source dependencies. Preserve current qualifications and deficits. '
            'This consumes one remaining original retrieval turn; no new budget or evidence-request loop. '
            'Return the complete reconstruction JSON, not evidence_requests.\n' + task)
        try:
            identity, answer = await engine._call_once('reconstruct', instruction,
                {'instructions': 'Read all mandatory current and historical evidence before answering.'},
                resume=item['session_id'], writer=True, delivery_scope=scope)
        finally:
            del engine.paper_recovery_admission
        attempts = engine.ledger['paper_recovery_admissions']
        identity, answer = delivery.reconcile_completed(engine, adapted, scope, attempts[0])
    return finish(engine, item, attempts[0], identity, answer)


def finish(engine, item, admission, identity, answer):
    require('evidence_requests' not in answer, 'corrective reconstruction cannot start another retrieval loop')
    progress = engine.ledger.get('retrieval_progress')
    closure = {**item['retrieval_progress'], 'turns': 2, 'closed_by_paper_recovery': admission['name']}
    previous = [entry for entry in engine.ledger.get('retrieval_history', [])
                if entry.get('closed_by_paper_recovery') == admission['name']]
    if progress is not None:
        require(progress == {**item['retrieval_progress'], 'turns': 2}, 'consumed original turn count changed')
        require(not previous, 'duplicate consumed paper turn closure')
        engine.ledger.setdefault('retrieval_history', []).append(closure)
        engine.ledger.pop('retrieval_progress')
    else:
        require(previous == [closure], 'missing or changed consumed paper turn history')
    if identity not in engine.ledger['writer_ids']:
        engine.ledger['writer_ids'].append(identity)
    engine.save()
    return identity, answer
