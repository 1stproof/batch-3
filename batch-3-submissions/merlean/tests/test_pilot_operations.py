"""Operations observer integration: real local CLI children, no provider calls."""
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_operations as ops
from campaign_watchdog import capture_process_identity

SESSION = '11111111-2222-4333-8444-555555555555'


class OperationsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / 'run'
        self.operation = self.base / 'supervisor'
        self.state = self.base / 'operations'
        self.workspace = self.base / 'operator-work'
        self.codex = self.base / 'fake-codex'
        self.codex.write_text('#!' + sys.executable + '\n' + '''import json, pathlib, sys, time
p=pathlib.Path.cwd()
with (p/'calls.jsonl').open('a') as f: f.write(json.dumps(sys.argv[1:])+'\\n')
sys.stdin.read()
mode=(p/'mode').read_text() if (p/'mode').exists() else 'success'
if mode!='missing': print(json.dumps({'type':'thread.started','thread_id':'11111111-2222-4333-8444-555555555555'}),flush=True)
time.sleep(.35)
print(json.dumps({'type':'error','message':'insufficient_quota'}) if mode=='quota' else json.dumps({'type':'turn.completed'}),flush=True)
''')
        self.codex.chmod(0o755)
        self.config = {'models': {'main': 'gpt-6-astra', 'execution': 'gpt-6.1-sol'},
                       'codex_binary': str(self.codex), 'problems': ['P1'],
                       'exam': {'submission_deadline_utc': (datetime.now(timezone.utc)+timedelta(hours=24)).isoformat()}}
        self.write(self.root/'host-config.json', self.config)
        self.launch = {'pid': 99999999, 'process_identity': 'absent',
                       'operation_started_utc': '2020-01-01T00:00:00+00:00'}
        self.bind_operation()
        ops.initialize(self.state, self.operation, self.codex, self.workspace, cooldown=60)
        self.addCleanup(self.reap)

    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def bind_operation(self):
        self.write(self.operation/'attempt.json', {'root': str(self.root)})
        self.launch['attempt_sha256'] = ops.supervisor.sha(self.operation/'attempt.json')
        self.write(self.operation/'launch.json', self.launch)

    def saved(self):
        return json.loads((self.state/'ops-state.json').read_text())

    def calls(self):
        p = self.workspace/'calls.jsonl'
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []

    def reap(self):
        if not (self.state/'ops-state.json').exists(): return
        active = self.saved().get('active')
        if active and active.get('pid'):
            try: os.waitpid(active['pid'], 0)
            except ChildProcessError: pass

    def finish(self):
        until = time.monotonic() + 5
        while time.monotonic() < until:
            result = ops.tick(self.state)
            if result['status'] not in ('operator_running', 'operator_ownership_uncertain'):
                return result
            time.sleep(.05)
        self.fail('fake CLI did not finish within five seconds')

    def change_incident(self):
        self.write(self.root/'host/runtime/P1/001/stage.meta.json', {'status': 'failed', 'new': True})
        saved = self.saved()
        for value in saved['incidents'].values(): value['started_epoch'] = value['finished_epoch'] = 0
        self.write(self.state/'ops-state.json', saved)

    def test_mandate_distinguishes_protocol_repair_from_content_authority(self):
        mandate = ops.PROMPT.read_text()
        for requirement in (
            'original writer can correct its own response',
            'Use only the remaining existing allowance',
            'Never accept the rejected response',
            'original writer alone supplies corrected content',
            'even a protocol-valid correction may still fail release gates',
            'Never reset this record or the watcher budget',
        ):
            self.assertIn(requirement, mandate)

    def test_native_healthy_observation_never_launches_operator(self):
        self.launch.update(pid=os.getpid(), process_identity=capture_process_identity(os.getpid()))
        self.bind_operation()
        self.write(self.state/'route.json', ops.route_info(self.operation))
        self.assertEqual(ops.tick(self.state)['status'], 'running')
        self.assertEqual(self.calls(), [])

    def test_fault_actual_child_dedup_and_same_session_resume(self):
        self.assertEqual(ops.tick(self.state)['status'], 'operator_started')
        self.assertEqual(ops.tick(self.state)['status'], 'operator_running')
        self.assertEqual(self.finish()['status'], 'incident_cooldown')
        self.assertEqual(self.saved()['session_id'], SESSION)
        self.assertEqual(len(self.calls()), 1)
        self.change_incident()
        self.assertEqual(ops.tick(self.state)['status'], 'operator_started')
        self.finish()
        argv = self.calls()[1]
        self.assertEqual(argv[argv.index('exec'):argv.index('exec')+2], ['exec', 'resume'])
        self.assertIn(SESSION, argv)
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', argv)
        self.assertIn('workspace-write', argv)
        self.assertIn('forced_login_method="chatgpt"', argv)

    def test_uncertain_reserved_or_mismatched_operator_never_duplicates(self):
        for active in ({'pid': None}, {'pid': os.getpid(), 'process_identity': 'wrong'},
                       {'pid': os.getpid(), 'process_identity': None}):
            saved = self.saved(); saved['active'] = active
            self.write(self.state/'ops-state.json', saved)
            self.assertFalse(ops.tick(self.state)['model_call'])
        self.assertEqual(self.calls(), [])
        saved['active'] = None; self.write(self.state/'ops-state.json', saved)

    def test_quota_pauses_without_new_session_or_retry(self):
        (self.workspace/'mode').write_text('quota')
        ops.tick(self.state)
        self.assertEqual(self.finish()['status'], 'operator_quota_paused')
        self.change_incident()
        self.assertFalse(ops.tick(self.state)['model_call'])
        self.assertEqual(len(self.calls()), 1)

    def test_new_incident_cooldown(self):
        ops.tick(self.state); self.finish()
        self.write(self.root/'host/runtime/P1/002/stage.meta.json', {'status': 'failed'})
        self.assertEqual(ops.tick(self.state)['status'], 'incident_cooldown')
        self.assertEqual(len(self.calls()), 1)

    def test_original_deadline_prevents_dispatch(self):
        route = json.loads((self.state/'route.json').read_text())
        route['deadline_utc'] = '2000-01-01T00:00:00+00:00'
        self.write(self.state/'route.json', route)
        self.assertEqual(ops.tick(self.state)['status'], 'original_deadline_reached')
        self.assertEqual(self.calls(), [])

    def test_native_incomplete_paper_is_actionable(self):
        self.write(self.root/'pilot-result.json', {'end_utc': datetime.now(timezone.utc).isoformat(),
            'results': [{'problem': 'P1', 'status': 'complete', 'paper': {'status': 'draft'}}]})
        result = ops.tick(self.state)
        self.assertTrue(result['model_call'])
        self.assertEqual(json.loads((self.state/'observation.json').read_text())['status'], 'paper_incomplete')
        self.finish()

    def test_route_rejects_deadline_or_model_change(self):
        other = self.base/'other'; operation = self.base/'other-supervisor'
        for key in ('deadline', 'models'):
            config = json.loads(json.dumps(self.config))
            if key == 'deadline': config['exam']['submission_deadline_utc'] = '2099-01-01T00:00:00+00:00'
            else: config['models']['execution'] = 'different'
            self.write(other/'host-config.json', config)
            self.write(operation/'attempt.json', {'root': str(other)})
            self.write(operation/'launch.json', {**self.launch, 'attempt_sha256': ops.supervisor.sha(operation/'attempt.json')})
            with self.assertRaises(ValueError): ops.set_route(self.state, operation)
        self.assertEqual(self.calls(), [])

    def test_missing_session_blocks_new_incident_dispatch(self):
        (self.workspace/'mode').write_text('missing')
        ops.tick(self.state)
        self.assertEqual(self.finish()['status'], 'operator_identity_attention')
        self.change_incident()
        self.assertEqual(ops.tick(self.state)['status'], 'operator_identity_attention')
        self.assertEqual(len(self.calls()), 1)

    def test_bounded_same_incident_followup_and_disposition(self):
        ops.tick(self.state); self.finish()
        for expected in (2, 3):
            saved = self.saved()
            for item in saved['incidents'].values(): item['started_epoch'] = item['finished_epoch'] = 0
            self.write(self.state/'ops-state.json', saved)
            self.assertEqual(ops.tick(self.state)['status'], 'operator_started')
            self.finish()
            self.assertEqual(len(self.calls()), expected)
        self.assertEqual(ops.tick(self.state)['status'], 'incident_followup_limit_attention')
        fingerprint = next(iter(self.saved()['incidents']))
        self.write(self.state/'incidents'/fingerprint/'disposition.json', {'status': 'blocked', 'reason': 'synthetic external dependency'})
        self.assertEqual(ops.tick(self.state)['status'], 'incident_disposition_recorded')

    def test_false_resolved_does_not_hide_native_failure(self):
        result = ops.tick(self.state); self.finish()
        self.write(self.state/'incidents'/result['incident']/'disposition.json', {'status': 'resolved'})
        saved = self.saved()
        for item in saved['incidents'].values(): item['started_epoch'] = item['finished_epoch'] = 0
        self.write(self.state/'ops-state.json', saved)
        self.assertEqual(ops.tick(self.state)['status'], 'operator_started')
        self.finish()

    def test_healthy_sibling_progress_does_not_renew_fault_identity(self):
        route = ops.route_info(self.operation)
        report = {'status': 'paper_incomplete', 'issues': [{'problem': 'P1', 'kind': 'paper_incomplete'}]}
        before = ops.digest(ops.compact(report, route))
        self.write(self.root/'host/runtime/P9/009/stage.meta.json', {'status': 'completed'})
        self.assertEqual(ops.digest(ops.compact(report, route)), before)
        self.write(self.root/'host/runtime/P1/003/stage.meta.json', {'status': 'failed'})
        self.assertNotEqual(ops.digest(ops.compact(report, route)), before)

    def test_authenticated_live_descendant_route(self):
        other = self.base/'next-run'; operation = self.base/'next-supervisor'
        self.write(other/'continuation-checkpoint.json', {'synthetic': 'checkpoint'})
        config = {**self.config, 'continuation_parent': str(self.root),
                  'continuation_checkpoint': {'sha256': ops.supervisor.sha(other/'continuation-checkpoint.json')}}
        self.write(other/'host-config.json', config)
        files = {'host-config.json': ops.supervisor.sha(self.root/'host-config.json')}
        self.write(other/'continuation-parent.json', {'source_root': str(self.root), 'files': files,
                                                    'manifest_sha256': ops.digest(files)})
        self.write(operation/'attempt.json', {'root': str(other)})
        self.write(operation/'launch.json', {**self.launch, 'pid': os.getpid(),
            'process_identity': capture_process_identity(os.getpid()),
            'attempt_sha256': ops.supervisor.sha(operation/'attempt.json')})
        self.assertEqual(ops.set_route(self.state, operation)['status'], 'active_route_updated')
        self.assertEqual(ops.tick(self.state)['status'], 'running')
        self.assertEqual(self.calls(), [])

    def test_completed_descendant_requires_native_paper_artifacts(self):
        self.test_authenticated_live_descendant_route()
        self.write(self.state/'route.json', ops.route_info(self.operation))
        other = self.base/'next-run'; operation = self.base/'next-supervisor'
        launch = json.loads((operation/'launch.json').read_text())
        launch.update(pid=99999999, process_identity='absent')
        self.write(operation/'launch.json', launch)
        folder = other/'exam/papers/P1'; folder.mkdir(parents=True)
        (folder/'paper.tex').write_text('synthetic artifact, no scientific content')
        (folder/'final.pdf').write_bytes(b'%PDF-synthetic-fixture')
        self.write(other/'campaign/state.json', {'problems': {'P1': {'successful_complete': True}}})
        self.write(other/'pilot-result.json', {'end_utc': datetime.now(timezone.utc).isoformat(),
            'results': [{'problem': 'P1', 'status': 'complete', 'paper': {
                'status': 'polished', 'terminal': True, 'polishing_complete': True,
                'best_available_tex': str(folder/'paper.tex'), 'best_available_pdf': str(folder/'final.pdf')}}]})
        self.assertEqual(ops.set_route(self.state, operation)['status'], 'active_route_updated')
        self.write(self.state/'route.json', ops.route_info(self.operation))
        self.write(other/'campaign/state.json', {'problems': {'OTHER': {'successful_complete': True}}})
        with self.assertRaises(ValueError): ops.set_route(self.state, operation)
        self.write(other/'campaign/state.json', {'problems': {'P1': {'successful_complete': True}}})
        (folder/'final.pdf').unlink()
        with self.assertRaises(ValueError): ops.set_route(self.state, operation)
        self.assertEqual(self.calls(), [])

    def test_deadline_signals_only_exact_owned_operator_once(self):
        import signal
        ops.tick(self.state)
        active = self.saved()['active']
        route = json.loads((self.state/'route.json').read_text())
        route['deadline_utc'] = '2000-01-01T00:00:00+00:00'
        self.write(self.state/'route.json', route)
        with patch.object(ops.os, 'kill') as kill, patch.object(ops, 'probe_process', return_value={'alive': True, 'identity_match': True}):
            ops.tick(self.state); ops.tick(self.state)
        kill.assert_called_once_with(active['pid'], signal.SIGTERM)

    def test_environment_drift_rejects_before_spawn(self):
        with patch('codex_transport.subscription_environment', return_value={'PATH': '/changed'}):
            with self.assertRaises(ValueError): ops.tick(self.state)
        self.assertEqual(self.calls(), [])

    def test_live_sibling_attention_wakes_once(self):
        report = {'status': 'running', 'process': {'alive': True, 'identity_match': True},
                  'health': [{'kind': 'problem_ended_with_attention', 'problem': 'P1'}], 'issues': []}
        with patch.object(ops.supervisor, 'observation', return_value=report):
            self.assertEqual(ops.tick(self.state)['status'], 'operator_started')
            self.assertEqual(ops.tick(self.state)['status'], 'operator_running')
            self.finish()
        self.assertEqual(len(self.calls()), 1)

    def test_watch_errors_are_durable_and_do_not_dispatch(self):
        with patch.object(ops, 'tick', side_effect=ValueError('invalid binding')), \
             patch.object(ops.time, 'sleep', side_effect=InterruptedError):
            with self.assertRaises(InterruptedError): ops.run(self.state)
        report = json.loads((self.state/'watcher-status.json').read_text())
        self.assertEqual(report['status'], 'operations_attention')
        self.assertFalse(report['model_call'])
        self.assertEqual(self.calls(), [])


if __name__ == '__main__': unittest.main()
