"""Opt-in deterministic recovery of proven pre-dispatch local spawn failures.

No signals, account RPC, source edits, session replacement or validator bypass.
A keeper re-entry observes its reserved generation; only a fully validated sealed
parent can authorize one distinct native continuation generation.
"""
from __future__ import annotations

import errno
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pilot_supervisor as outer

RULE = 'local-prespawn-native-continuation-v1'


def binding(value):
    return outer.digest(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def file_map(root):
    paths = sorted(root.rglob('*'))
    if any(p.is_symlink() for p in paths):
        raise ValueError('guardian refuses symlink evidence')
    return {str(p.relative_to(root)): outer.sha(p) for p in paths if p.is_file()}


def route_plan(folder, arguments):
    """Pin executable bytes and the existing selected environment, without RPC."""
    selected = 'codex'
    for index, item in enumerate(arguments):
        if item == '--codex': selected = arguments[index + 1]
        elif item.startswith('--codex='): selected = item.split('=', 1)[1]
    if '--continue-from' in arguments:
        selected = outer.read(Path(arguments[arguments.index('--continue-from') + 1])/'host-config.json')['codex_binary']
    path = Path(shutil.which(selected) or selected).resolve(strict=True)
    return {'rule': RULE, 'codex': {'path': str(path), 'sha256': outer.sha(path)},
            'python': {'path': str(Path(sys.executable).resolve()), 'sha256': outer.sha(Path(sys.executable).resolve())}}


def verify_route(plan):
    from codex_transport import subscription_environment
    if str(Path(sys.executable).resolve(strict=True)) != plan['recovery']['python']['path']:
        raise ValueError('guardian Python executable route changed')
    outer.verify_source(plan['source'])
    if subscription_environment() != plan['environment']:
        raise ValueError('guardian runtime environment changed')
    for route in (plan['recovery']['codex'], plan['recovery']['python']):
        if outer.sha(route['path']) != route['sha256']:
            raise ValueError('guardian executable route changed')


def armed(root, config):
    """A bare host flag is insufficient to defer an exam's paper handoff."""
    try:
        ref = config['guardian_recovery_route']
        path = outer.canonical(ref['path'])
        if outer.sha(path) != ref['sha256']: return False
        plan = outer.read(path)
        if plan.get('recover_on_failure') is not True or plan['recovery']['rule'] != RULE: return False
        state = outer.read(path.parent/'guardian-state.json')
        current = state['generations'][-1]
        return (Path(current['root']) == root.resolve()
                and current['phase'] == 'reserved' and state['plan_sha256'] == ref['sha256'])
    except (OSError, ValueError, KeyError, IndexError, TypeError):
        return False



def startup_guard(root, config):
    """Malformed enrollment is never permission to bypass startup validation."""
    ref = config.get('guardian_recovery_route')
    if ref is None: return
    if not isinstance(ref, dict) or set(ref) != {'path', 'sha256'}:
        raise ValueError('malformed guardian enrollment reference')
    path = outer.canonical(ref['path'])
    if outer.sha(path) != ref['sha256']:
        raise ValueError('guardian enrolled plan changed before host admission')
    plan = outer.read(path); state = outer.read(path.parent/'guardian-state.json')
    if (plan.get('recover_on_failure') is not True or plan['recovery']['rule'] != RULE
            or state.get('plan_sha256') != ref['sha256'] or state.get('rule') != RULE
            or not isinstance(state.get('generations'), list) or not state['generations']):
        raise ValueError('guardian enrollment state is invalid')
    current = state['generations'][-1]
    if Path(current['root']) == root.resolve():
        if current.get('phase') != 'reserved' or current.get('terminal_report'):
            raise ValueError('guardian generation is no longer admitted')
        verify_route(plan)
        unchanged_runtime(root, config, plan)
    elif (not config.get('continuation_parent')
          or any(Path(item['root']) == root.resolve() for item in state['generations'])):
        raise ValueError('host is not the current guardian generation')
    # A separate explicit native manual continuation has already passed
    # validate_start. A valid old enrollment does not claim ownership of it.


def unchanged_runtime(root, config, plan):
    import codex_pilot as pilot
    if config.get('code_hashes') != {str(p.relative_to(pilot.REPO/'src')): outer.sha(p)
                                    for p in (pilot.REPO/'src').rglob('*.py')}:
        raise ValueError('guardian cannot migrate frozen runtime source')
    if config.get('policy_hashes') != {name: outer.sha(pilot.REPO/name) for name in pilot.POLICIES}:
        raise ValueError('guardian cannot migrate frozen policy')
    required = {'proof_document_version': 1, 'lite_local_verification_version': 1,
                'main_response_contract_version': 1, 'original_scope_review_count': 2,
                'assessment_protocol_epoch': pilot.ASSESSMENT_PROTOCOL_EPOCH}
    if any(config.get(key) != value for key, value in required.items()):
        raise ValueError('guardian cannot migrate protocol settings')
    if (config.get('parallel_route_scouts') != pilot.route_config(config.get('parallel_route_scouts'))
            or config.get('campaign_phase') not in ('phase1', 'phase2')
            or config.get('explicit_policy_changes')
            or config.get('codex_binary') != plan['recovery']['codex']['path']):
        raise ValueError('guardian policy or executable route differs')
    if config.get('deadline_utc') and not config.get('exam'):
        raise ValueError('legacy non-exam clock would change during continuation')
    if config.get('exam'):
        from pilot_exam import ExamRuntime
        if ExamRuntime(config['exam']).research_timeout(1) < 1:
            raise ValueError('original research admission is closed')
    if not armed(root, config):
        raise ValueError('guardian recovery route is not armed for this generation')


def census(root, launch, destination):
    """Construct absent-only evidence, then ask the unchanged native validator.

    Use its exact authenticated opaque-file exclusions and PID parser. Reused or
    permission-hidden processes are never accepted by this automatic route.
    """
    import pilot_continuation as native
    before = file_map(root)
    owned = {native._pid(launch['pid'])}
    opaque = native._opaque_review_chunks(root) | native._opaque_public_source_files(root)
    for path in root.rglob('*.json'):
        if path not in opaque:
            owned.update(native._nested_pids(outer.read(path)))
    for pid in owned: native._assert_stopped(pid)
    destination.mkdir(parents=True, exist_ok=False)
    evidence = []
    for name, spec in [('processes.txt', 'pid=,args='), ('lineage.txt', 'pid=,ppid=,pgid=,lstart=,args=')]:
        result = subprocess.run(['ps', '-axo', spec], check=True, capture_output=True, text=True, timeout=10)
        path = destination/name
        path.write_text(result.stdout)
        evidence.append(str(path))
    receipt = {'schema_version': 1, 'source_root': str(root), 'checked_utc': outer.now(),
        'host_pid': launch['pid'], 'owned_pids': sorted(owned), 'reused_pids': [],
        'descendants_checked': True, 'launch_records_checked': True, 'probe_records_checked': True,
        'active_children': [], 'pending_launches': [], 'all_owned_children_stopped': True,
        'evidence': evidence, 'collector': RULE}
    native.validate_process_reconciliation(root, receipt)
    if file_map(root) != before: raise ValueError('parent changed during guardian census')
    path = destination/'reconciliation.json'
    outer.save(path, receipt, exclusive=True)
    from pilot_quota_recheck import reconciled_stack
    ref = {'path': str(path), 'sha256': outer.sha(path)}
    reconciled_stack(root, ref, before, launch)
    return path, before


def recovery_candidate(root, launch, plan, reconciliation):
    """All current failures need exact pre-spawn evidence; no substring inference."""
    import pilot_continuation as native
    config = outer.read(root/'host-config.json')
    unchanged_runtime(root, config, plan)
    result = outer.current_result(root, launch['operation_started_utc'], with_end=True)
    if not result: raise ValueError('no current committed terminal result')
    if result.get('attention_observer_error'): raise ValueError('terminal observer failed')
    rows = result.get('results', [])
    if {row['problem'] for row in rows} != set(config['problems']) or len(rows) != len(config['problems']):
        raise ValueError('terminal problem census incomplete')
    failures = []
    since = launch['operation_started_utc']
    for row in rows:
        ident = row['problem']; folder = root/'campaign/problems'/ident
        if row.get('status') == 'complete':
            if row.get('paper') and not row.get('paper_complete'):
                raise ValueError('completed research has unresolved paper delivery')
            continue
        if row.get('operational_failure') != 'infrastructure':
            raise ValueError('incomplete problem is not a pre-dispatch infrastructure failure')
        if row.get('paper') and row['paper'].get('status') != 'deferred_pre_dispatch_recovery':
            raise ValueError('paper work is outside guardian recovery')
        errors = row.get('errors') or []
        if not errors or 'pre_dispatch_failure' not in errors[-1]:
            raise ValueError('terminal failure lacks exact failed-stage binding')
        ref = errors[-1]['pre_dispatch_failure']
        name = ref['name']
        if len(Path(name).parts) != 2 or Path(name).parts[0] != ident or '..' in Path(name).parts:
            raise ValueError('unsafe failure stage binding')
        path = root/'host/runtime'/name/'stage.meta.json'; meta = outer.read(path)
        expected = {'schema_version': 1, 'errno': ref['local_spawn_failure']['errno'],
                    'boundary': 'await_create_subprocess_exec', 'model_dispatched': False}
        if (type(expected['errno']) is not int or expected['errno'] not in (errno.EAGAIN, errno.ENOMEM)
                or ref.get('local_spawn_failure') != expected or meta.get('local_spawn_failure') != expected
                or meta.get('model_dispatched') is not False or meta.get('status') != 'process_launch_failed'
                or meta.get('pid') is not None or meta.get('session_id') is not None
                or meta.get('name') != name or ref.get('request_id') != meta.get('request_id')
                or ref.get('meta_sha256') != outer.sha(path)
                or not since <= meta.get('start_utc', '') <= meta.get('end_utc', '') <= result['end_utc']):
            raise ValueError('failure is not a verified current pre-dispatch local transient')
        if any(path.with_name(n).exists() for n in ('stage.answer.txt', 'stage.events.jsonl')):
            raise ValueError('failed spawn has answer or event evidence')
        if (folder/(Path(name).name+'.json')).exists():
            raise ValueError('failed spawn published a response')
        progress = outer.read(folder/'host-progress.json')
        if progress.get('errors') != errors: raise ValueError('terminal checkpoint errors differ')
        if (folder/'review-exhaustion.json').exists() and outer.read(folder/'review-exhaustion.json'):
            raise ValueError('exhausted review needs main-owned resolution')
        failures.append({'problem': ident, 'name': name, 'errno': expected['errno'], 'meta_sha256': outer.sha(path)})
    if not failures: raise ValueError('no recoverable failed problem')
    failed_names = {item['name'] for item in failures}
    for path in (root/'host/runtime').glob('*/*/stage.meta.json'):
        meta = outer.read(path)
        if meta.get('start_utc', '') < since: continue
        if meta.get('name') in failed_names: continue
        if meta.get('status') != 'completed': raise ValueError('another current stage is incomplete')
        if any(meta.get('start_utc', '') >= outer.read(root/'host/runtime'/item['name']/'stage.meta.json')['start_utc']
               for item in failures if item['problem'] == path.parent.parent.name):
            raise ValueError('work continued after failed stage')
    checkpoint = native.validate_and_load(root, reconciliation=reconciliation)
    progress_keys = {}
    for ident, saved in checkpoint['problems'].items():
        if (saved.get('paper_only') or saved.get('initial_main_recovery')
                or (saved.get('proof_document') or {}).get('status') == 'draft'):
            raise ValueError('guardian requires an existing submitted main checkpoint')
        if any(item.get('state') == 'working' for item in saved.get('local_verification_modules', [])):
            raise ValueError('unfinished local execution module needs reconciliation')
        if any(item.get('historical_probe') and item.get('result', {}).get('status') in (None, 'unknown', 'running', 'pending')
               for item in saved.get('execution_history', [])):
            raise ValueError('unfinished probe needs reconciliation')
        # Only the main's durable scientific checkpoint renews recovery. New
        # request IDs, duplicate answers, timestamps and whitespace cannot do so.
        from pilot_review_exhaustion import projection
        progress_keys[ident] = {'main_session': saved.get('main_session'),
                               'scientific_checkpoint': projection(saved['current'])}
    return {'progress': binding(progress_keys), 'fault': binding(sorted((f['problem'], f['errno']) for f in failures)),
            'failures': failures, 'parent_manifest_sha256': checkpoint['parent']['manifest_sha256']}


def keep(folder):
    """One durable chain. OS re-entry can only observe an existing reservation."""
    folder = outer.canonical(folder)
    with outer.owner(folder/'guardian-owner'):
        plan_path = folder/'keeper-plan.json'; plan = outer.read(plan_path)
        state_path = folder/'guardian-state.json'
        if not state_path.exists():
            verify_route(plan)
            args = list(plan['pilot_arguments'])
            if '--continue-from' in args:
                raise ValueError('automatic guardian enrollment requires a fresh prospective campaign')
            cleaned = []; skip = False
            for item in args:
                if skip: skip = False; continue
                if item == '--codex': skip = True; continue
                if item.startswith('--codex='): continue
                cleaned.append(item)
            args = cleaned + ['--codex', plan['recovery']['codex']['path'],
                              '--guardian-recovery-route', str(plan_path)]
            state = {'schema_version': 1, 'rule': RULE, 'plan_sha256': outer.sha(plan_path),
                'generations': [{'root': plan['root'], 'operation': str(folder/'generations/000'),
                    'arguments': args, 'phase': 'reserved'}], 'recoveries': []}
            outer.save(state_path, state, exclusive=True)
        else:
            state = outer.read(state_path)
            if state['plan_sha256'] != outer.sha(plan_path): raise ValueError('guardian plan changed')
        while True:
            current = state['generations'][-1]
            if current.get('terminal_report'):
                return current['terminal_report']
            operation = Path(current['operation']); root = Path(current['root'])
            if (operation/'attempt.json').exists():
                report = outer.watch(operation)
            elif current.get('launch_claimed'):
                report = {'status': 'launch_uncertain', 'reason': 'guardian dispatch reservation lacks launch receipt'}
            else:
                verify_route(plan)
                current['launch_claimed'] = True
                outer.save(state_path, state)
                report = outer.run(operation, root, current['arguments'])
            outer.save(folder/'status.json', {**report, 'guardian_generation': len(state['generations'])-1})
            if report.get('status') != 'infrastructure_failed':
                if report.get('status') != 'running':
                    current['terminal_report'] = report
                    outer.save(state_path, state)
                return report
            try:
                if report.get('exit_code') not in (None, 0): raise ValueError('independent host exit failure')
                verify_route(plan)
                launch = outer.read(operation/'launch.json')
                receipt, files = census(root, launch, operation/'guardian-reconciliation')
                # Reuse this exact stopped-stack receipt for optional diagnosis.
                outer.save(operation/'diagnostic-reconciliation.json', {
                    'reconciliation': {'path': str(receipt), 'sha256': outer.sha(receipt)}, 'terminal_files': files}, exclusive=True)
                candidate = recovery_candidate(root, launch, plan, receipt)
                if any(item['progress'] == candidate['progress'] for item in state['recoveries']):
                    raise ValueError('guardian stopped: no new durable progress since prior recovery')
                next_root = root.parent/(Path(plan['root']).name+'-guardian-'+str(len(state['generations'])).zfill(3))
                if next_root.exists(): raise ValueError('successor destination already exists')
                args = ['--continue-from', str(root), '--reconciliation', str(receipt),
                        '--watchdog-interval', str(outer.read(root/'host-config.json').get('watchdog_interval_seconds', 300))]
                if file_map(root) != files: raise ValueError('parent changed before successor reservation')
                state['recoveries'].append(candidate)
                state['generations'].append({'root': str(next_root), 'operation': str(folder/'generations'/str(len(state['generations'])).zfill(3)),
                    'arguments': args, 'phase': 'reserved', 'parent': str(root), 'parent_manifest_sha256': candidate['parent_manifest_sha256']})
                outer.save(state_path, state)
            except (OSError, ValueError, KeyError, TypeError) as error:
                result = {**report, 'recovery': 'blocked', 'recovery_reason': str(error), 'needs_attention': True}
                if (plan.get('diagnose_on_failure') is True
                        and not (operation/'diagnostic-attempt.json').exists()):
                    try:
                        outer.diagnostic_quiescence(operation)
                        route = plan['diagnostic_codex']
                        if outer.sha(route['path']) != route['sha256']: raise ValueError('diagnostic route changed')
                        outer.diagnose(operation, codex=route['path'])
                        result['diagnosis'] = 'attempted_once'
                    except (OSError, ValueError, KeyError) as diagnosis_error:
                        result['diagnosis'] = 'blocked: ' + str(diagnosis_error)
                current['terminal_report'] = result
                outer.save(state_path, state)
                outer.save(folder/'status.json', result)
                return result
