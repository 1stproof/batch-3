"""Explicit recovery of a terminal first-main provider failure without research output.

This reader never launches, changes the parent, renews budgets, or authenticates an
account. Call only after ordinary terminal/process/source reconciliation. The
caller binds the selected account route and reserves the successor exactly once.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid


def _hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _require(condition, message):
    if not condition:
        raise ValueError('initial main recovery: ' + message)


def _time(value):
    result = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    _require(result.tzinfo is not None, 'timezone required')
    return result


def _events(stage, *, allow_empty=False):
    values = [json.loads(line) for line in (stage / 'stage.events.jsonl').read_text().splitlines() if line.strip()]
    _require((values or allow_empty) and all(isinstance(v, dict) and isinstance(v.get('event'), dict) for v in values), 'malformed event evidence')
    return [v['event'] for v in values]


def _empty_stage(stage, call, *, paper=False):
    answer = stage / 'stage.answer.txt'
    _require(answer.is_file() and answer.read_bytes() == b'' and call.get('answer_bytes') == 0
             and call.get('answer_sha256') == _hash(answer), 'nonempty or unbound answer')
    _require(call.get('status') in ({'process_failed', 'unverifiable_rollout_audit'} if paper else {'process_failed'}) and call.get('turn_completed') is False
             and type(call.get('exit_code')) is int and call['exit_code'] != 0, 'stage is not failed before completion')
    _require(call.get('tool_event_count') == 0 and call.get('persisted_tool_event_count') == 0
             and call.get('tool_events') == [] and call.get('persisted_tool_events') == []
             and not call.get('document_events'), 'tool activity cannot be recovered by this route')
    _require(call.get('usage') is None and not call.get('accounting', {}).get('response_ids')
             and not call.get('accounting', {}).get('encountered_response_ids'), 'response evidence requires ordinary continuation')
    _require(not call.get('answer_json_extracted') and not call.get('answer_markdown_extracted'), 'answer extraction is present')
    for filename in ('stage.response-usage.json', 'stage.messages.json'):
        _require(json.loads((stage / filename).read_text()) == [], 'raw response or message evidence exists')
    events = _events(stage, allow_empty=paper)
    for event in events:
        kind = event.get('type')
        _require(kind in {'thread.started', 'turn.started', 'turn.failed', 'error', 'item.completed'}, 'unexpected event before recovery')
        if kind == 'item.completed':
            _require(isinstance(event.get('item'), dict) and event['item'].get('type') == 'error', 'scientific or tool item exists')
    return events


def validate_initial_recovery(source, config, progress, calls, *, authorization,
                              problem_id, target_root):
    """Return a restoration payload for one explicitly authorized empty first turn.

    ``authorization`` is an external JSON object, passed only by an explicit CLI
    option. Its binary binding authorizes that exact route; account identity and
    isolated-home verification are separate prelaunch requirements. Fresh-session
    recovery explicitly preserves failed identity without claiming continuity.
    """
    source, target = Path(source).resolve(strict=True), Path(target_root).resolve()
    a = authorization
    _require(isinstance(a, dict) and a.get('schema_version') == 1
             and a.get('kind') == 'initial_main_provider_failure'
             and a.get('authorization') == 'explicit_user'
             and type(a.get('max_recovery_attempts')) is int and a['max_recovery_attempts'] == 1,
             'explicit bounded authorization required')
    _require(a.get('parent_root') == str(source) and a.get('target_root') == str(target)
             and target != source and not target.is_relative_to(source) and not source.is_relative_to(target), 'parent/target mismatch')
    _require(a.get('problem_id') == problem_id and config.get('problems') == [problem_id], 'single original problem required')
    _require(not config.get('initial_main_recovery') and not config.get('continuation_parent'), 'recovery already consumed or parent is a continuation')
    _require(a.get('parent_config_sha256') == _hash(source / 'host-config.json'), 'parent configuration changed')
    _require(json.loads((source / 'host-config.json').read_text()) == config, 'configuration differs from parent')
    mode = a.get('recovery_session_mode')
    _require(mode in {'same_session', 'fresh_session'}, 'explicit conversation mode required')
    binary = Path(a.get('codex_binary', ''))
    _require(binary.is_absolute() and binary.is_file() and a.get('codex_binary_sha256') == _hash(binary), 'selected binary route changed')
    binding = a.get('account_route')
    _require(isinstance(binding, dict) and binding.get('user_authorized') is True
             and isinstance(binding.get('account_id'), str) and bool(binding['account_id'])
             and isinstance(binding.get('auth_source'), str) and Path(binding['auth_source']).is_absolute(), 'explicit account route required')
    exam = config.get('exam')
    _require(isinstance(exam, dict), 'this recovery requires an existing exam clock')
    clock = source / 'exam/clock.json'
    _require(a.get('clock_sha256') == _hash(clock) and json.loads(clock.read_text()) == exam, 'original clock changed')
    _require(config.get('deadline_utc') == exam.get('submission_deadline_utc')
             and _time(exam['start_utc']) < _time(exam['research_close_utc']) < _time(exam['submission_deadline_utc'])
             and datetime.now(timezone.utc) < _time(exam['research_close_utc']), 'original research clock closed or inconsistent')
    folder = source / 'campaign/problems' / problem_id
    original = _hash(folder / 'input.txt')
    _require(a.get('original_sha256') == original, 'original input changed')
    allowed = {'input.txt', 'host-progress.json', '001-main-dossier.json', 'paper-001-reconstruct.json', 'partial.md', 'working-log.md'}
    _require(all(p.is_file() and not p.is_symlink() and p.name in allowed for p in folder.iterdir()), 'unexpected scientific or orphan artifact exists')
    for filename in ('001-main-dossier.json', 'paper-001-reconstruct.json'):
        failed_answer = folder / filename
        if failed_answer.exists():
            raw = json.loads(failed_answer.read_text())
            _require(isinstance(raw, dict) and raw.get('raw_answer') == ''
                     and set(raw) <= {'raw_answer', 'parse_error'}, 'saved response has material content')
    _require(not any((folder / name).exists() for name in ('accepted-dossier.json', 'current-candidate.json', 'proof-current.json', 'proof-revisions', 'probes', 'local-verification')), 'scientific artifact exists')
    for key in ('open_findings', 'triage_history', 'advisory_scope_history', 'final_assessment_history', 'finding_history', 'route_scout_history', 'local_verification_modules', 'research_continuation_state', 'execution_history'):
        _require(not progress.get(key), 'scientific history exists: ' + key)
    _require(progress == json.loads((folder / 'host-progress.json').read_text()), 'progress differs from parent')
    research = [c for c in calls if not c.get('module', '').startswith('paper-')]
    _require(len(research) == 1, 'exactly one failed first research stage required')
    call = research[0]
    _require(call.get('name') == problem_id + '/001-main-dossier' and call.get('module') == 'main-dossier', 'not the first dossier')
    stage = source / 'host/runtime' / call['name']
    _require(json.loads((stage / 'stage.meta.json').read_text()) == call
             and a.get('stage_meta_sha256') == _hash(stage / 'stage.meta.json')
             and a.get('events_sha256') == _hash(stage / 'stage.events.jsonl')
             and a.get('prompt_sha256') == call.get('prompt_sha256') == _hash(stage / 'stage.prompt.txt'), 'stage evidence changed')
    session = call.get('session_id')
    _require(isinstance(session, str), 'verified failed session is required')
    try:
        uuid.UUID(session)
    except (ValueError, TypeError, AttributeError) as error:
        raise ValueError('initial main recovery: invalid failed session') from error
    _require(a.get('session_id') == session and progress.get('main_session') in (None, session)
             and call.get('resume_session') is None and call.get('fresh_session') is True,
             'failed session identity mismatch')
    _require(call.get('model_verified') is True and call.get('model_actual') == call.get('model_requested')
             and call.get('model_requested') == config.get('models', {}).get('main'), 'unverified model')
    audit = call.get('persisted_rollout_audit', {})
    _require(audit.get('status') == 'verified' and audit.get('tool_events') == []
             and not audit.get('response_usage_records'), 'persisted rollout is not empty and verified')
    events = _empty_stage(stage, call)
    _require([e.get('thread_id') for e in events if e.get('type') == 'thread.started'] == [session], 'raw thread identity mismatch')
    failed = [e for e in events if e.get('type') == 'turn.failed']
    _require(len(failed) == 1 and isinstance(failed[0].get('error'), dict)
             and isinstance(failed[0]['error'].get('message'), str) and failed[0]['error']['message'].strip(), 'explicit provider failure missing')
    _require(call.get('protocol_errors') == ['turn.failed'], 'other protocol failure requires supervision')
    all_calls = progress.get('calls')
    _require(isinstance(all_calls, list) and call in all_calls, 'missing saved call history')
    disk_stages = sorted((source / 'host/runtime' / problem_id).glob('*/stage.meta.json'))
    disk_calls = [json.loads(p.read_text()) for p in disk_stages]
    _require(len({c.get('name') for c in all_calls}) == len(all_calls)
             and len(all_calls) == len(disk_calls) and all(c in disk_calls for c in all_calls), 'unrepresented stage history')
    for paper in all_calls:
        if paper == call:
            continue
        _require(paper.get('module', '').startswith('paper-') and paper.get('session_id') is None
                 and paper.get('model_verified') is False, 'later scientific or verified paper stage exists')
        _require(not _empty_stage(source / 'host/runtime' / paper['name'], paper, paper=True), 'paper emitted events')
    paper_result = source / 'exam/papers' / problem_id / 'result.json'
    if paper_result.exists():
        paper = json.loads(paper_result.read_text())
        _require(paper.get('status') == 'incomplete' and paper.get('polishing_complete') is False
                 and not paper.get('completed') and not paper.get('writer_ids') and not paper.get('reader_ids'), 'paper progress exists')
    marker = {'schema_version': 1, 'kind': a['kind'], 'recovery_session_mode': mode,
              'failed_session_id': session, 'failed_stage': call['name'], 'recovery_attempts': 1,
              'authorization_sha256': hashlib.sha256(json.dumps(a, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
              'parent_config_sha256': a['parent_config_sha256'], 'clock_sha256': a['clock_sha256'],
              'account_route': binding, 'codex_binary': str(binary), 'codex_binary_sha256': a['codex_binary_sha256']}
    return {'initial_main_recovery': marker, 'main_session': session if mode == 'same_session' else None,
            'implementers': [session] if mode == 'same_session' else [], 'calls': all_calls,
            'findings': [], 'errors': progress.get('errors', []), 'current': {}, 'dossier': {},
            'counter': 1, 'execution_history': [], 'reviewer_history': [], 'triage_history': [],
            'local_verification_modules': [], 'advisory_scope_history': [], 'final_assessment_history': [],
            'finding_history': [], 'original_sha256': original, 'proof_document': None}
