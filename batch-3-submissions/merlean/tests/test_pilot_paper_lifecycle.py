"""Explicit allowance changes preserve original clocks, evidence and admission limits."""
import asyncio
import contextlib
import io
import json
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import AsyncMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import pilot_paper as paper
import test_pilot_continuation_runtime as continuation
import test_pilot_paper as fixtures


class LifecycleTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperTests.setUp
    transport = fixtures.PaperTests.transport
    retrieval_fixture = fixtures.PaperTests.retrieval_fixture

    def timed_out_chain(self):
        engine = self.retrieval_fixture(interrupted_count=2)
        path = self.problem.pilot.host / 'runtime/P1/paper-004-reconstruct/stage.meta.json'
        meta = json.loads(path.read_text())
        meta.update(start_utc='2026-01-01T00:00:00+00:00',
                    deadline_utc='2026-01-01T00:04:00+00:00',
                    end_utc='2026-01-01T00:04:00.01+00:00', timeout_seconds=240)
        paper._write(path, meta)
        return engine

    async def test_timeout_does_not_trigger_infrastructure_or_content_repair(self):
        with patch.object(paper.PaperEngine, 'run', new=AsyncMock(side_effect=TimeoutError('stage elapsed'))), \
             patch.object(paper.PaperEngine, 'repair', new_callable=AsyncMock) as repair:
            result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertEqual(result['operational_failure'], 'timeout')
        self.assertEqual(result['status'], 'incomplete')
        self.assertFalse(result['terminal'])
        self.assertIn('recovery_required', result)
        repair.assert_not_awaited()

    async def test_unchanged_timeout_recovery_is_attention_not_infrastructure(self):
        self.timed_out_chain()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch, \
             patch.object(paper.PaperEngine,'repair',new_callable=AsyncMock) as repair:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['operational_failure'],'timeout')
        self.assertFalse(result['terminal'])
        dispatch.assert_not_awaited()
        repair.assert_not_awaited()
        self.assertEqual(result['retrieval_progress']['turns'],3)

    async def test_actual_saved_chain_last_turn_with_explicit_larger_allowance(self):
        engine = self.timed_out_chain()
        self.problem.pilot.config.update(paper_stage_timeout_seconds=900,
            explicit_policy_changes={'paper_stage_timeout_seconds': {'old':240, 'new':900}})
        old = {str(p): p.read_bytes() for p in (self.problem.pilot.host/'runtime').rglob('*') if p.is_file()}
        async def dispatch(root, name, prompt, model, timeout, resume=None, **kw):
            self.assertEqual(name, 'P1/paper-005-reconstruct')
            self.assertEqual(resume, 'saved-writer')
            self.assertEqual(timeout, 576)
            self.assertEqual(engine.ledger['retrieval_progress']['turns'], 4)
            return await self.transport(root, name, prompt, model, timeout, resume, **kw)
        with patch.object(paper, 'call_stage', dispatch):
            await engine.call('reconstruct', 'synthetic', {}, writer=True)
        self.assertEqual(old, {str(p): p.read_bytes() for p in (self.problem.pilot.host/'runtime').rglob('*') if p.is_file()})
        allocation = engine.ledger['admissions'][-1]['timeout_allocation']
        self.assertEqual(allocation['recovery_of'], 'P1/paper-004-reconstruct')
        self.assertEqual(allocation['previous_timeout_seconds'], 240)
        self.assertEqual(allocation['retrieval_turn_limit'], 4)
        self.assertEqual(len(self.requests), 1)

    async def test_unchanged_or_silent_or_insufficient_allowance_never_retries(self):
        for cap, change, remaining in [(240,None,3600),(900,None,3600),
                (900,{'old':240,'new':900},1000)]:
            with self.subTest(cap=cap, change=change):
                # Same immutable saved fixture may be reloaded; no calls should be added.
                if not (self.problem.pilot.host/'runtime').exists(): self.timed_out_chain()
                self.problem.pilot.config.update(paper_stage_timeout_seconds=cap,
                    explicit_policy_changes={'paper_stage_timeout_seconds':change} if change else {})
                self.runtime.seconds=remaining
                engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
                with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
                    with self.assertRaisesRegex(paper.PaperRecoveryRequired,'no blind retry'):
                        await engine.call('reconstruct','synthetic',{},writer=True)
                dispatch.assert_not_awaited()
                self.assertEqual(engine.ledger['retrieval_progress']['turns'],3)

    async def test_capacity_wait_refusal_does_not_consume_saved_final_turn(self):
        from contextlib import asynccontextmanager
        engine=self.timed_out_chain()
        self.problem.pilot.config.update(paper_stage_timeout_seconds=900,
            explicit_policy_changes={'paper_stage_timeout_seconds':{'old':240,'new':900}})
        @asynccontextmanager
        async def queued():
            self.runtime.seconds=1000
            yield
        with patch.object(engine,'capacity',queued),patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaisesRegex(paper.PaperRecoveryRequired,'no blind retry'):
                await engine.call('reconstruct','synthetic',{},writer=True)
        dispatch.assert_not_awaited()
        self.assertEqual(engine.ledger['retrieval_progress']['turns'],3)
        self.assertEqual(len(engine.ledger['calls']),4)
        self.assertNotIn('admissions',engine.ledger)

    async def test_fairshare_and_original_deadline_guard_bound_allowance(self):
        from pilot_exam import ExamRuntime, new_config
        self.problem.pilot.config.update(paper_stage_timeout_seconds=900)
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        self.runtime.seconds=7200
        self.assertEqual(engine.stage_timeout(),900)
        self.problem.pilot.config['problems']=['P1','P2','P3']
        self.assertEqual(engine.stage_timeout(),384)
        start=datetime.now(timezone.utc)
        config=new_config(self.root/'real',start=start)
        runtime=ExamRuntime(config,clock=lambda:start+timedelta(hours=24,seconds=-40))
        engine.runtime=runtime
        self.assertLessEqual(engine.stage_timeout(),25)
        self.assertEqual(runtime.config['submission_deadline_utc'],config['submission_deadline_utc'])

    async def test_outer_timeout_requires_attention_without_model_diagnostics(self):
        import pilot_supervisor as outer
        from datetime import datetime, timezone
        root=self.root/'outer';root.mkdir()
        outer.save(root/'host-config.json',{'problems':['P1']})
        outer.save(root/'pilot-result.json',{'end_utc':datetime.now(timezone.utc).isoformat(),
            'results':[{'problem':'P1','status':'complete','paper':{'status':'incomplete',
                'terminal':False,'polishing_complete':False,'operational_failure':'timeout'}}]})
        launch={'pid':123,'process_identity':'owned','operation_started_utc':'2026-01-01T00:00:00+00:00'}
        with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
            report=outer.observation(root,launch,exit_code=0)
        self.assertEqual(report['status'],'paper_incomplete')
        self.assertTrue(report['needs_attention'])
        state=self.root/'outer-state';state.mkdir()
        outer.save(state/'keeper-plan.json',{'diagnose_on_failure':True})
        outer.save(state/'attempt.json',{})
        with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnose') as diagnose:
            outer.keep(state)
        diagnose.assert_not_called()

    async def test_completion_authority_is_separate(self):
        result=paper.completion_status({'status':'complete'}, {'status':'incomplete','terminal':False})
        self.assertTrue(result['research_complete'])
        self.assertFalse(result['paper_complete'])
        self.assertFalse(result['exam_complete'])
        result=paper.completion_status({'status':'partial'}, {'status':'polished','terminal':True,'polishing_complete':True})
        self.assertTrue(result['deliverable_complete'])
        self.assertFalse(result['exam_complete'])


class PaperPolicyTests(unittest.TestCase):
    setUp=continuation.ContinuationRuntimeTests.setUp
    prepare=continuation.ContinuationRuntimeTests.prepare

    def test_legacy_policy_inherited_without_silent_increase(self):
        config=self.prepare()
        self.assertEqual(config['paper_stage_timeout_seconds'],240)
        self.assertNotIn('paper_stage_timeout_seconds',config['explicit_policy_changes'])

    def test_explicit_change_preserves_parent_and_policy(self):
        before={str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()}
        config=self.prepare(paper_stage_timeout_seconds=900)
        self.assertEqual(config['paper_stage_timeout_seconds'],900)
        self.assertEqual(config['explicit_policy_changes']['paper_stage_timeout_seconds'],{'old':240,'new':900})
        reservation=json.loads(Path(config['continuation_reservation']).read_text())
        self.assertEqual(reservation['explicit_policy_changes'],config['explicit_policy_changes'])
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()})

    def test_invalid_policy_rejected_before_destination(self):
        for value in (0,-1,True,float('nan'),float('inf'),3601,'900'):
            with self.subTest(value=value),self.assertRaisesRegex(ValueError,'finite and between'):
                self.prepare(paper_stage_timeout_seconds=value)
            self.assertFalse(self.root.exists())

    def test_native_cli_forwards_policy_and_rejects_live_override(self):
        argv=['pilot',str(self.root),'--continue-from',str(self.fixture.source),'--reconciliation',str(self.fixture.receipt),'--paper-stage-timeout-seconds','900']
        with patch.object(sys,'argv',argv),patch.object(pilot,'prepare_continuation') as prepare, \
             patch.object(pilot,'Pilot') as runner,contextlib.redirect_stdout(io.StringIO()):
            runner.return_value.run=AsyncMock(return_value=[])
            pilot.main()
        self.assertEqual(prepare.call_args.kwargs['paper_stage_timeout_seconds'],900)
        with patch.object(sys,'argv',['pilot',str(self.root),'--paper-stage-timeout-seconds','900']), \
             contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):
            pilot.main()
