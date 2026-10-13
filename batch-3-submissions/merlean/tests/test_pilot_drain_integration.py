"""Host drain integration: durable main output, closed queues, reconciled children."""
import asyncio
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
from pilot_drain import DrainRequested
import test_pilot_continuation_runtime as fixtures
from test_pilot_main_inputs import deliver_main_scope


class DrainIntegrationTests(unittest.TestCase):
    setUp = fixtures.ContinuationRuntimeTests.setUp
    prepare = fixtures.ContinuationRuntimeTests.prepare

    def request(self, runner):
        pilot.write(runner.drain.request_path, {'schema_version': 1, 'action': 'drain',
            'request_id': 'test-drain', 'reason': 'checkpoint without interruption'})

    def test_active_main_commits_before_closed_queued_stage_probe_and_final_ack(self):
        self.prepare()
        async def scenario():
            runner = pilot.Pilot(self.root)
            runner.semaphore = asyncio.Semaphore(1)
            entered, finish = asyncio.Event(), asyncio.Event()
            processes, dispatched = [], []
            async def transport(host, name, prompt, model, timeout, resume, **kwargs):
                dispatched.append(name)
                process = await asyncio.create_subprocess_exec(sys.executable, '-c',
                    "import sys; sys.stdout.write('owned diagnostic\\n' * 12000)",
                    stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, start_new_session=True)
                processes.append(process)
                entered.set()
                await finish.wait()
                stdout, stderr = await process.communicate()
                self.assertEqual(len(stdout), len(b'owned diagnostic\n') * 12000)
                self.assertEqual(stderr, b'')
                meta = {'name': name, 'request_id': 'synthetic-request', 'status': 'completed', 'session_id': 'main-session',
                    'pid': process.pid, 'exit_code': process.returncode, 'end_utc': pilot.now().isoformat(),
                    'model_actual': pilot.ASTRA, 'model_verified': True, 'prompt_sha256': pilot.sha(prompt)}
                meta['document_audit'] = deliver_main_scope(kwargs['document_scope'],
                    host/'runtime'/name, name, 'main-session')
                pilot.write(host/'runtime'/name/'stage.meta.json', meta)
                pilot.write(host/'accounting'/'test-receipt.json', {'recorded': name})
                return meta, {'response_type': 'candidate_update', 'proof_markdown': 'EXACT NEWLY RETURNED MAIN ANSWER', 'ledger': {'rows': []}}
            with patch.object(pilot, 'subscription_preflight', return_value={}), patch.object(pilot, 'call_stage', side_effect=transport):
                running = asyncio.create_task(runner.run())
                await entered.wait()
                queued_problem = pilot.Problem(runner, 'problem')
                queued = asyncio.create_task(queued_problem._call_once('scope-review', 'queued', model=pilot.ASTRA, resume=False, timeout=300))
                await asyncio.sleep(0)
                self.request(runner)
                self.assertFalse(runner.drain.ack_path.exists())
                runner.drain.poll()
                self.assertFalse(running.done())
                finish.set()
                result = await running
                with self.assertRaises(DrainRequested):
                    await queued
                with patch.object(asyncio, 'create_subprocess_exec', new=AsyncMock()) as spawn:
                    with self.assertRaises(DrainRequested):
                        await queued_problem.probe({'python_probe': 'print(1)'}, 'blocked')
                    spawn.assert_not_called()
            self.assertEqual(len(dispatched), 1)
            self.assertEqual(processes[0].returncode, 0)
            self.assertEqual(result[0]['status'], 'partial')
            folder = runner.root/'campaign/problems/problem'
            current = json.loads((folder/'current-candidate.json').read_text())
            self.assertEqual(current['proof_markdown'], 'EXACT NEWLY RETURNED MAIN ANSWER')
            self.assertIn('EXACT NEWLY RETURNED MAIN ANSWER', (folder/'partial.md').read_text())
            self.assertTrue((runner.host/'accounting/test-receipt.json').exists())
            self.assertEqual(json.loads(runner.drain.ack_path.read_text())['status'], 'drained')
            self.assertTrue(json.loads((runner.host/'drain-owned-children.json').read_text())['all_owned_children_stopped'])
        asyncio.run(scenario())

    def test_capacity_retry_blocked_after_admitted_failure(self):
        self.prepare()
        async def scenario():
            runner = pilot.Pilot(self.root)
            problem = pilot.Problem(runner, 'problem')
            async def fail(*args, **kwargs):
                self.request(runner)
                raise pilot.StageFailure({'name': 'problem/next', 'status': 'process_failed'}, ['model at capacity'])
            with patch.object(problem, '_call_once', side_effect=fail) as stage, patch.object(asyncio, 'sleep', new=AsyncMock()) as sleep:
                with self.assertRaises(DrainRequested):
                    await problem.call('main-repair', 'Continue')
                self.assertEqual(stage.call_count, 1)
                sleep.assert_not_called()
        asyncio.run(scenario())

    def test_unreconciled_new_process_group_blocks_ack_inherited_pid_ignored(self):
        self.prepare()
        async def scenario():
            runner = pilot.Pilot(self.root)
            self.request(runner)
            runner.drain.poll()
            # Only this host's admitted names are considered. Copied parent
            # runtime files contain old PIDs and cannot authorize or block drain.
            with patch.object(pilot.os, 'killpg', side_effect=AssertionError('inherited PID probed')):
                self.assertTrue(runner.reconcile_drain_children()['all_owned_children_stopped'])
            runner.drain_stage_names.add('problem/new-owned')
            pilot.write(runner.host/'runtime/problem/new-owned/stage.meta.json',
                        {'status': 'running', 'pid': 12345})
            receipt = runner.reconcile_drain_children()
            self.assertFalse(receipt['all_owned_children_stopped'])
            self.assertTrue(receipt['pending_launches'])
            self.assertFalse(runner.drain.ack_path.exists())
        asyncio.run(scenario())
