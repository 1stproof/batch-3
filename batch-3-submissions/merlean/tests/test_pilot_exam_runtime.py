"""Executable exam-clock simulations; no live model or benchmark calls."""
import asyncio
from datetime import timedelta
import json
from pathlib import Path
import sys
import tempfile
import shutil
from types import SimpleNamespace
import unittest
import contextlib
import io
from unittest.mock import AsyncMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
from campaign import Campaign
from pilot_exam import ExamRuntime, PaperDeadline, ResearchClosed, new_config


class Clock:
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value


class ExamRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.start = pilot.now()
        self.clock = Clock(self.start)
        self.config = new_config(self.root, start=self.start)
        self.exam = ExamRuntime(self.config, clock=self.clock)

    def problem(self):
        folder = self.root / 'problem'
        folder.mkdir(exist_ok=True)
        (folder / 'current-candidate.json').write_text('{"status":"unknown"}')
        state = {'status': 'partial', 'successful_complete': False}
        return SimpleNamespace(ident='synthetic', original_bytes=b'Prove the exact question.', folder=folder,
            current={'proof_markdown': 'Conditional argument; unresolved lemma.', 'grade': 'SILVER'},
            dossier={}, findings=['open lemma'], errors=[], execution_history=[], final_assessment_history=[],
            advisory_scope_history=[], calls=[],
            pilot=SimpleNamespace(campaign=SimpleNamespace(status=lambda: {'problems': {'synthetic': state}})))

    def test_shared_clock_survives_reconstruction_and_rejects_reset(self):
        self.clock.value += timedelta(hours=23, minutes=10)
        resumed = ExamRuntime(dict(self.config), clock=self.clock)
        self.assertEqual(resumed.remaining(), 50 * 60)
        with self.assertRaises(ResearchClosed):
            resumed.research_timeout(900)
        reset = new_config(self.root, start=self.clock.value)
        with self.assertRaisesRegex(ValueError, 'immutable original'):
            ExamRuntime(reset, clock=self.clock)

    def test_admission_shrinks_long_research_before_handoff(self):
        self.clock.value += timedelta(hours=22.75, seconds=-45)
        self.assertEqual(self.exam.research_timeout(900), 30)
        self.clock.value += timedelta(seconds=31)
        with self.assertRaises(ResearchClosed):
            self.exam.research_timeout(900)
        self.assertGreater(self.exam.remaining(), 3600)

    def test_fresh_default_reserves_seventy_five_minutes_and_explicit_old_clock_survives(self):
        from datetime import datetime
        self.assertEqual(datetime.fromisoformat(self.config['research_close_utc']) - self.start,
                         timedelta(hours=22.75))
        old_root = self.root / 'old'
        old = new_config(old_root, start=self.start, research_hours=22.5)
        ExamRuntime(old, clock=self.clock)
        resumed = ExamRuntime(dict(old), clock=self.clock)
        self.assertEqual(resumed.config['research_close_utc'], old['research_close_utc'])
        self.assertEqual(resumed.config['submission_deadline_utc'], old['submission_deadline_utc'])
        self.clock.value = self.start + timedelta(hours=22.5)
        with self.assertRaises(ResearchClosed):
            resumed.research_timeout(1)
        self.assertGreater(self.exam.research_timeout(1), 0)

    def test_final_deadline_never_renews_on_resume(self):
        self.clock.value += timedelta(hours=24)
        resumed = ExamRuntime(self.config, clock=self.clock)
        with self.assertRaises(PaperDeadline):
            resumed.paper_timeout(900)
        self.assertEqual(resumed.remaining(), 0)

    def test_snapshot_retains_partial_evidence_without_awarding_acceptance(self):
        problem = self.problem()
        path = self.exam.snapshot(problem)
        data = json.loads((path / 'snapshot.json').read_text())
        self.assertFalse(data['research_status']['successful_complete'])
        self.assertEqual(data['current']['grade'], 'SILVER')
        self.assertEqual(data['findings'], ['open lemma'])
        problem.current['grade'] = 'GOLD'
        self.assertEqual(self.exam.snapshot(problem), path)
        self.assertEqual(json.loads((path / 'snapshot.json').read_text())['current']['grade'], 'SILVER')
        tamper = path / 'input.txt'
        tamper.chmod(0o644)
        tamper.write_text('Changed original')
        with self.assertRaisesRegex(ValueError, 'changed'):
            self.exam.snapshot(problem)

    def test_duplicate_writer_blocked_and_terminal_handoff_idempotent(self):
        problem = self.problem()
        async def scenario():
            entered, release = asyncio.Event(), asyncio.Event()
            calls = []
            async def writer(problem, snapshot, runtime):
                calls.append(snapshot)
                entered.set()
                await release.wait()
                return {'status': 'partial_submission', 'paper_verdict': 'INCOMPLETE', 'terminal': True}
            first = asyncio.create_task(self.exam.dispatch(problem, writer))
            await asyncio.wait_for(entered.wait(), 2)
            second = await ExamRuntime(self.config, clock=self.clock).dispatch(problem, writer)
            self.assertEqual(second['status'], 'writer_already_running')
            release.set()
            result = await first
            self.assertEqual(await self.exam.dispatch(problem, writer), result)
            self.assertEqual(len(calls), 1)
        asyncio.run(scenario())

    def test_final_snapshot_check_respects_deadline_and_retains_actual_draft(self):
        problem = self.problem()
        async def writer(problem, snapshot, runtime):
            draft = runtime.paper_dir(problem.ident) / 'reviewed-draft.tex'
            draft.write_text('supported partial result')
            self.clock.value += timedelta(hours=24)
            return {'terminal': True, 'status': 'polished', 'polishing_complete': True,
                    'best_available_tex': str(draft)}
        result = asyncio.run(self.exam.dispatch(problem, writer))
        self.assertEqual(result['status'], 'deadline-partial')
        self.assertFalse(result['polishing_complete'])
        self.assertEqual(result['final_snapshot_verification'], 'INCOMPLETE')
        self.assertEqual(Path(result['best_available_tex']).read_text(), 'supported partial result')
        saved = json.loads((self.exam.paper_dir(problem.ident) / 'result.json').read_text())
        self.assertEqual(saved, result)

    def test_interrupted_writer_resumes_same_immutable_snapshot(self):
        problem = self.problem()
        seen = []
        async def writer(problem, snapshot, runtime):
            seen.append(snapshot)
            if len(seen) == 1:
                (runtime.paper_dir(problem.ident) / 'draft.tex').write_text('preserved draft')
                raise RuntimeError('simulated crash')
            self.assertEqual((runtime.paper_dir(problem.ident) / 'draft.tex').read_text(), 'preserved draft')
            return {'terminal': True, 'status': 'partial_submission'}
        with self.assertRaisesRegex(RuntimeError, 'simulated crash'):
            asyncio.run(self.exam.dispatch(problem, writer))
        problem.current = {}
        result = asyncio.run(ExamRuntime(self.config, clock=self.clock).dispatch(problem, writer))
        self.assertTrue(result['terminal'])
        self.assertEqual(seen[0], seen[1])

    def setup_pilot(self, clock):
        source = self.root / 'input.txt'
        source.write_text('Prove zero equals zero.')
        config = new_config(self.root / 'run', start=clock.value - timedelta(hours=22.75, seconds=-45))
        root = self.root / 'run'
        root.mkdir()
        Campaign.initialize(root / 'campaign', {'synthetic': source}, deadline_utc=config['submission_deadline_utc'],
                            concurrency=1, owner_key=root / 'controller.key', mode='lite', require_paper=False)
        _, policies = pilot.freeze_runtime(root)
        pilot.write(root / 'host-config.json', {'deadline_utc': config['submission_deadline_utc'],
            'exam': config, 'model_concurrency': 1, 'internet_browse': False, 'codex_binary': 'synthetic',
            'source_url': 'https://example.invalid/synthetic', 'problems': ['synthetic'], 'policy_hashes': policies})
        runner = pilot.Pilot(root)
        runner.exam = ExamRuntime(config, clock=clock)
        return runner

    def test_late_admitted_call_finishes_then_real_problem_hands_off_without_proof(self):
        runner = self.setup_pilot(self.clock)
        dispatched, written = [], []
        async def transport(host, name, prompt, model, timeout, resume=None, **kwargs):
            dispatched.append(name)
            self.assertLessEqual(timeout, 30)
            # Even a transport that returns late is checkpointed; handoff does not cancel it.
            self.clock.value += timedelta(seconds=50)
            answer = {'response_type': 'candidate_update', 'proof_markdown': 'Available partial from late call.',
                      'ledger': {'rows': []}, 'remaining_gaps': ['missing proof'], 'sol_tasks': []}
            return {'name': name, 'status': 'completed', 'session_id': 'main-session', 'request_id': name,
                    'model_actual': model, 'model_verified': True}, answer
        async def writer(problem, snapshot, exam):
            written.append(snapshot)
            data = json.loads((snapshot / 'snapshot.json').read_text())
            self.assertIn('Available partial', data['current']['proof_markdown'])
            self.assertFalse(data['research_status']['successful_complete'])
            return {'status': 'partial_submission', 'terminal': True, 'paper_verdict': 'INCOMPLETE'}
        original_dispatch = ExamRuntime.dispatch
        async def dispatch(exam, problem):
            return await original_dispatch(exam, problem, writer)
        with patch.object(pilot, 'subscription_preflight', return_value={}), \
             patch.object(pilot, 'call_stage', side_effect=transport), patch.object(ExamRuntime, 'dispatch', dispatch):
            result = asyncio.run(runner.run())
        self.assertEqual(len(dispatched), 1)
        self.assertEqual(len(written), 1)
        self.assertEqual(result[0]['status'], 'partial')
        self.assertEqual(result[0]['paper']['paper_verdict'], 'INCOMPLETE')
        self.assertFalse(runner.campaign.status()['successful_complete'])

    def test_non_exam_admission_remains_uncapped(self):
        runner = object.__new__(pilot.Pilot)
        runner.exam = None
        runner.deadline = None
        self.assertEqual(runner.remaining(), float('inf'))
        self.assertEqual(runner.research_timeout(900), 900)

    def test_research_queued_on_capacity_cannot_launch_after_handoff(self):
        runner = self.setup_pilot(self.clock)
        async def scenario():
            problem = pilot.Problem(runner, 'synthetic')
            await runner.semaphore.acquire()
            waiting = asyncio.create_task(problem._call_once('main-repair', 'Continue',
                model=pilot.ASTRA, resume=False, timeout=900))
            await asyncio.sleep(0)
            self.clock.value += timedelta(seconds=60)
            runner.semaphore.release()
            with patch.object(pilot, 'call_stage', new=AsyncMock()) as transport:
                with self.assertRaises(ResearchClosed):
                    await waiting
                transport.assert_not_awaited()
        asyncio.run(scenario())

    def test_provider_pause_defers_paper_without_dispatch(self):
        problem = SimpleNamespace(pilot=SimpleNamespace(exam=object(),provider_unavailable=True),
            _run_research=AsyncMock(return_value={'status':'partial'}))
        result = asyncio.run(pilot.Problem.run(problem))
        self.assertEqual(result['paper']['status'],'deferred_provider_unavailable')

    def test_cli_creates_one_clock_for_all_problems(self):
        originals = {}
        for ident in ('one', 'two'):
            (self.root / (ident + '.txt')).write_text('Exact synthetic question ' + ident)
            originals[ident] = ident + '.txt'
        (self.root / 'problems.json').write_text(json.dumps(originals))
        root = self.root / 'new-exam'
        argv = ['pilot', str(root), '--problems', str(self.root / 'problems.json')]
        with patch.object(sys, 'argv', argv), patch.object(pilot, 'subscription_preflight', return_value={}), \
             patch.object(pilot.Pilot, 'run', new=AsyncMock(return_value=[])), contextlib.redirect_stdout(io.StringIO()):
            pilot.main()
        config = json.loads((root / 'host-config.json').read_text())
        self.assertEqual(set(config['problems']), {'one', 'two'})
        self.assertEqual(config['deadline_utc'], config['exam']['submission_deadline_utc'])
        self.assertEqual(config['exam']['clock_scope'], 'whole_campaign_including_continuations')
        self.assertEqual(config['exam']['page_limit'], 16)
        self.assertTrue(config['watchdog_enabled'])
        self.assertTrue(config['paper_export'])

    def test_cli_fresh_explicit_modes_and_hour_overrides(self):
        original = self.root / 'original.txt'; original.write_text('Synthetic question')
        problems = self.root / 'problems.json'; problems.write_text(json.dumps({'one': original.name}))
        cases = [('explicit-exam', ['--exam'], True, 22.75, 24),
                 ('short-exam', ['--exam-research-hours', '1', '--exam-total-hours', '2'], True, 1, 2),
                 ('uncapped', ['--no-exam'], False, None, None),
                 ('limited', ['--no-exam', '--minutes', '30'], False, None, None)]
        for name, options, exam, research, total in cases:
            with self.subTest(name=name):
                root = self.root / name
                with patch.object(sys, 'argv', ['pilot', str(root), '--problems', str(problems), *options]), \
                     patch.object(pilot, 'subscription_preflight', return_value={}), \
                     patch.object(pilot.Pilot, 'run', new=AsyncMock(return_value=[])), contextlib.redirect_stdout(io.StringIO()):
                    pilot.main()
                config = json.loads((root / 'host-config.json').read_text())
                self.assertEqual(bool(config['exam']), exam)
                self.assertEqual(config['paper_export'], exam)
                self.assertEqual(config['watchdog_enabled'], exam)
                if exam:
                    clock = config['exam']
                    start = pilot.datetime.fromisoformat(clock['start_utc'])
                    self.assertEqual(pilot.datetime.fromisoformat(clock['research_close_utc']) - start, timedelta(hours=research))
                    self.assertEqual(pilot.datetime.fromisoformat(clock['submission_deadline_utc']) - start, timedelta(hours=total))
                elif name == 'uncapped': self.assertIsNone(config['deadline_utc'])
                else: self.assertIsNotNone(config['deadline_utc'])

    def test_cli_mode_conflicts_fail_before_auth_or_clock(self):
        for options in [
            ['--problems', 'missing.json', '--minutes', '30'],
            ['--problems', 'missing.json', '--exam', '--minutes', '30'],
            ['--problems', 'missing.json', '--exam', '--no-exam'],
            ['--problems', 'missing.json', '--no-exam', '--exam-total-hours', '2'],
            ['--exam'], ['--no-exam'], ['--minutes', '30'], ['--exam-total-hours', '2'],
            ['--continue-from', 'parent', '--reconciliation', 'receipt', '--no-exam'],
            ['--continue-from', 'parent', '--reconciliation', 'receipt', '--exam'],
            ['--continue-from', 'parent', '--reconciliation', 'receipt', '--exam-total-hours', '2'],
            ['--inspect-watchdog', '--exam'], ['--inspect-watchdog', '--no-exam'],
            ['--inspect-watchdog', '--exam-total-hours', '2'],
            ['--inspect-watchdog', '--problems', 'missing.json']]:
            with self.subTest(options=options), patch.object(sys, 'argv', ['pilot', str(self.root / 'rejected'), *options]), \
                 patch.object(pilot, 'new_exam_config') as clock, patch.object(pilot, 'subscription_preflight') as auth, \
                 contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit): pilot.main()
                clock.assert_not_called(); auth.assert_not_called()
                self.assertFalse((self.root / 'rejected').exists())

    def test_cli_existing_and_continuation_never_construct_clock(self):
        for options in [[], ['--continue-from', 'parent', '--reconciliation', 'receipt']]:
            with self.subTest(options=options), patch.object(sys, 'argv', ['pilot', str(self.root / 'existing'), *options]), \
                 patch.object(pilot, 'new_exam_config') as clock, patch.object(pilot, 'subscription_preflight') as auth, \
                 patch.object(pilot, 'prepare_continuation') as continuation, patch.object(pilot, 'Pilot') as runner, \
                 contextlib.redirect_stdout(io.StringIO()):
                runner.return_value.run = AsyncMock(return_value=[])
                pilot.main()
                clock.assert_not_called(); auth.assert_not_called()
                self.assertEqual(continuation.call_count, int(bool(options)))

    def test_cli_inspection_never_constructs_clock_or_runs_models(self):
        with patch.object(sys, 'argv', ['pilot', str(self.root / 'existing'), '--inspect-watchdog']), \
             patch.object(pilot, 'new_exam_config') as clock, patch.object(pilot, 'subscription_preflight') as auth, \
             patch.object(pilot, 'Campaign'), patch('campaign_watchdog.CampaignWatchdog') as watchdog, \
             patch.object(pilot, 'Pilot') as runner, contextlib.redirect_stdout(io.StringIO()):
            watchdog.return_value.inspect.return_value = {}
            pilot.main()
            clock.assert_not_called(); auth.assert_not_called(); runner.assert_not_called()

    def test_actual_continuation_preserves_original_exam_deadlines(self):
        import test_pilot_continuation_runtime as fixtures
        fixture = fixtures.ContinuationRuntimeTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        source = fixture.fixture.source
        config = json.loads((source / 'host-config.json').read_text())
        config['exam'] = new_config(source, start=pilot.now() - timedelta(hours=23, minutes=10))
        config['deadline_utc'] = config['exam']['submission_deadline_utc']
        ExamRuntime(config['exam'])
        pilot.write(source / 'host-config.json', config)
        registry = json.loads((source / 'campaign/registry.json').read_text())
        registry['deadline_utc'] = config['deadline_utc']
        pilot.write(source / 'campaign/registry.json', registry)
        state = json.loads((source / 'campaign/state.json').read_text())
        state['registry_sha256'] = pilot.sha((source / 'campaign/registry.json').read_bytes())
        pilot.write(source / 'campaign/state.json', state)
        continued = fixture.prepare()
        self.assertEqual(continued['exam'], {**config['exam'],'state_root':str(fixture.root.resolve()/'exam')})
        self.assertEqual(json.loads((source/'exam/clock.json').read_text()),config['exam'])
        self.assertEqual(continued['deadline_utc'], config['deadline_utc'])
        runner = pilot.Pilot(fixture.root)
        with self.assertRaises(ResearchClosed):
            runner.research_timeout(900)
        self.assertLess(runner.exam.remaining(), 50 * 60)

    def test_closed_exam_with_no_main_output_resumes_real_paper_only_path(self):
        import test_pilot_continuation_runtime as fixtures
        fixture = fixtures.ContinuationRuntimeTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        source = fixture.fixture.source
        config = json.loads((source / 'host-config.json').read_text())
        config['exam'] = new_config(source, start=pilot.now() - timedelta(hours=23, minutes=10))
        config['deadline_utc'] = config['exam']['submission_deadline_utc']
        ExamRuntime(config['exam'])
        pilot.write(source / 'host-config.json', config)
        registry = json.loads((source / 'campaign/registry.json').read_text())
        registry['deadline_utc'] = config['deadline_utc']
        pilot.write(source / 'campaign/registry.json', registry)
        state = json.loads((source / 'campaign/state.json').read_text())
        state['registry_sha256'] = pilot.sha((source / 'campaign/registry.json').read_bytes())
        pilot.write(source / 'campaign/state.json', state)
        shutil.rmtree(source / 'host/runtime')
        (source / 'host/runtime').mkdir()
        folder = source / 'campaign/problems/problem'
        (folder / 'current-candidate.json').unlink()
        pilot.write(folder / 'host-progress.json', {'main_session': None, 'calls': [],
                                                  'open_findings': ['No returned proof'], 'errors': []})
        fixture.prepare()
        restored = json.loads((fixture.root / 'continuation-checkpoint.json').read_text())
        self.assertTrue(restored['problems']['problem']['paper_only'])
        runner = pilot.Pilot(fixture.root)
        dispatched = []
        original_dispatch = ExamRuntime.dispatch
        async def writer(problem, snapshot, runtime):
            dispatched.append(snapshot)
            self.assertEqual(json.loads((snapshot / 'snapshot.json').read_text())['current'], {})
            return {'terminal': True, 'status': 'unresolved_submission', 'paper_verdict': 'INCOMPLETE'}
        async def dispatch(runtime, problem):
            return await original_dispatch(runtime, problem, writer)
        with patch.object(pilot, 'subscription_preflight', return_value={}), \
             patch.object(pilot, 'call_stage', new=AsyncMock()) as transport, \
             patch.object(ExamRuntime, 'dispatch', dispatch):
            result = asyncio.run(runner.run())
        transport.assert_not_awaited()
        self.assertEqual(len(dispatched), 1)
        self.assertEqual(result[0]['status'], 'partial')
        self.assertEqual(result[0]['paper']['paper_verdict'], 'INCOMPLETE')
        self.assertFalse(runner.campaign.status()['successful_complete'])


if __name__ == '__main__':
    unittest.main()
