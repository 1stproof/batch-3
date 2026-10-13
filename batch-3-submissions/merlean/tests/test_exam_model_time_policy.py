"""Formal model thinking follows original phase clocks; test caps require opt-in."""
import asyncio
import contextlib
from datetime import timedelta
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as pilot
import pilot_paper as paper
from pilot_exam import (ExamRuntime, ResearchClosed, new_config, model_time_policy,
                        select_model_time_policy, model_timeout)
import test_pilot_exam_runtime as clock_fixtures
import test_pilot_continuation_runtime as continuation_fixtures
import test_pilot_paper as paper_fixtures


class ModelDispatchTests(unittest.TestCase):
    setUp=clock_fixtures.ExamRuntimeTests.setUp
    setup_pilot=clock_fixtures.ExamRuntimeTests.setup_pilot

    def runner(self,policy='formal-clock',cap=None):
        runner=self.setup_pilot(self.clock)
        self.clock.value-=timedelta(hours=2)
        runner.config.update(exam_model_time_policy=policy,exam_test_call_timeout_seconds=cap)
        runner.remaining=runner.exam.remaining
        return runner

    def test_every_research_model_role_uses_formal_phase_not_internal_caps(self):
        runner=self.runner()
        async def scenario():
            problem=pilot.Problem(runner,'synthetic')
            observed=[]
            async def transport(host,name,prompt,model,timeout,resume=None,**kwargs):
                observed.append((kwargs['module'],timeout))
                return {'name':name,'status':'completed','session_id':'main-session' if kwargs['module'].startswith('main') else name,'model_actual':model,'model_verified':True},{}
            roles=[('main-dossier',900),('main-repair',900),('route-scout-1',300),
                   ('sol-execution',300),('proof-review',600),('scope-review',300),
                   ('silver-review',300),('assumption-review',300),
                   ('advisory-scope-review',300),('preacceptance-scope-review',300)]
            with patch.object(pilot,'call_stage',transport):
                for role,cap in roles:
                    await problem.call(role,'Synthetic bounded task',timeout=cap)
            self.assertEqual([role for role,_ in observed],[role for role,_ in roles])
            self.assertTrue(all(timeout==7230 for _,timeout in observed),observed)
        asyncio.run(scenario())

    def test_testcap_applies_to_main_review_and_execution(self):
        runner=self.runner('test-cap',1500)
        async def scenario():
            problem=pilot.Problem(runner,'synthetic')
            async def transport(host,name,prompt,model,timeout,resume=None,**kwargs):
                self.assertEqual(timeout,1500)
                return {'name':name,'status':'completed','session_id':'main-session' if kwargs['module'].startswith('main') else name,'model_actual':model,'model_verified':True},{}
            with patch.object(pilot,'call_stage',transport):
                for role,cap in [('main-repair',900),('proof-review',600),('sol-execution',300)]:
                    await problem.call(role,'Synthetic',timeout=cap)
        asyncio.run(scenario())

    def test_waiting_capacity_recomputes_original_phase_allowance(self):
        runner=self.runner()
        async def scenario():
            problem=pilot.Problem(runner,'synthetic')
            await runner.semaphore.acquire()
            waiting=asyncio.create_task(problem.call('main-repair','Synthetic',timeout=900))
            await asyncio.sleep(0)
            self.clock.value+=timedelta(seconds=7200)
            async def transport(host,name,prompt,model,timeout,resume=None,**kwargs):
                self.assertEqual(timeout,30)
                return {'name':name,'status':'completed','session_id':'main-session' if kwargs['module'].startswith('main') else name,'model_actual':model,'model_verified':True},{}
            with patch.object(pilot,'call_stage',transport):
                runner.semaphore.release()
                await waiting
        asyncio.run(scenario())

    def test_formal_deadline_never_admits_retry(self):
        runner=self.runner()
        async def scenario():
            problem=pilot.Problem(runner,'synthetic')
            async def transport(host,name,prompt,model,timeout,resume=None,**kwargs):
                self.clock.value+=timedelta(seconds=timeout)
                return {'name':name,'status':'timeout_censored','session_id':name,'model_actual':model,'model_verified':True},{}
            with patch.object(pilot,'call_stage',side_effect=transport) as dispatch:
                with self.assertRaises(ResearchClosed):
                    await problem.call('main-repair','Synthetic',timeout=900)
            self.assertEqual(dispatch.await_count,1)
        asyncio.run(scenario())

    def test_technical_operations_still_use_their_own_caps(self):
        runner=self.runner()
        self.assertEqual(runner.research_timeout(70),70)
        self.assertEqual(runner.exam.paper_timeout(120),120)
        self.assertEqual(model_timeout(runner.exam,runner.config,'research',70),7230)

    def test_formal_paper_preserves_original_cleanup_guard_at_submission(self):
        self.clock.value=self.exam.deadline-timedelta(seconds=40)
        config={'exam':self.config,'exam_model_time_policy':'formal-clock'}
        self.assertEqual(model_timeout(self.exam,config,'paper',900),25)
        self.clock.value+=timedelta(seconds=26)
        from pilot_exam import PaperDeadline
        with self.assertRaises(PaperDeadline):model_timeout(self.exam,config,'paper',900)

    def test_fresh_cli_formal_and_explicit_test_modes(self):
        original=self.root/'original.txt';original.write_text('Synthetic')
        problem_map=self.root/'map.json';problem_map.write_text(json.dumps({'p':original.name}))
        for name,options,expected,cap in [('formal',[],'formal-clock',None),
            ('test',['--exam-model-time-policy','test-cap','--exam-test-call-timeout-seconds','75'],'test-cap',75),
            ('nonexam',['--no-exam','--main-call-timeout-seconds','1800'],'legacy-caps',None)]:
            root=self.root/name
            with patch.object(sys,'argv',['pilot',str(root),'--problems',str(problem_map),*options]), \
                 patch.object(pilot,'subscription_preflight',return_value={}), \
                 patch.object(pilot.Pilot,'run',new=AsyncMock(return_value=[])),contextlib.redirect_stdout(io.StringIO()):
                pilot.main()
            config=json.loads((root/'host-config.json').read_text())
            self.assertEqual(model_time_policy(config),(expected,cap))

    def test_bad_cli_combinations_fail_before_auth_and_creation(self):
        for options in [ ['--main-call-timeout-seconds','900'],['--paper-stage-timeout-seconds','900'],
            ['--exam-test-call-timeout-seconds','75'],['--exam-model-time-policy','test-cap'],
            ['--exam-model-time-policy','test-cap','--exam-test-call-timeout-seconds','nan'],
            ['--no-exam','--exam-model-time-policy','formal-clock']]:
            with patch.object(sys,'argv',['pilot',str(self.root/'bad'),'--problems','absent',*options]), \
                 patch.object(pilot,'subscription_preflight') as auth,contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):
                pilot.main()
            auth.assert_not_called()
            self.assertFalse((self.root/'bad').exists())


class PaperModelTests(unittest.IsolatedAsyncioTestCase):
    setUp=paper_fixtures.PaperTests.setUp
    transport=paper_fixtures.PaperTests.transport
    retrieval_fixture=paper_fixtures.PaperTests.retrieval_fixture

    async def test_formal_paper_outer_timer_uses_global_allowance_without_fairshare(self):
        self.problem.pilot.config.update(exam=True,exam_model_time_policy='formal-clock',
            problems=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10'],model_concurrency=1)
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        self.assertEqual(engine.stage_timeout(),3600)
        self.assertFalse(engine.timeout_allocation['fair_share_is_deadline'])
        with patch.object(paper,'call_stage',side_effect=self.transport) as dispatch, \
             patch.object(paper.asyncio,'wait_for',wraps=asyncio.wait_for) as timers:
            for stage in ('reconstruct','raw-audit','draft','polish','reader-1','revise-1',
                          'reader-2','revise-2','verify-2','visual-review','proof-audit',
                          'finalize-ledgers','repair-proof-audit'):
                payload = {}
                if stage in ('reader-1','reader-2','verify-2'):
                    extra = {'reports': [], 'dispositions': []} if stage == 'verify-2' else {}
                    payload = engine.reader_payload(stage, self.tex, **extra)
                await engine.call(stage,'Synthetic',payload,writer=stage in ('reconstruct','draft','polish'))
        self.assertTrue(all(call.args[4]==3600 for call in dispatch.call_args_list))
        self.assertEqual(len(dispatch.call_args_list),13)
        self.assertTrue(all(call.kwargs.get('timeout',call.args[1] if len(call.args)>1 else None)==3600
                            for call in timers.call_args_list))
        self.assertEqual(engine.ledger['admissions'][-1]['timeout_allocation']['policy'],'formal-clock')

    async def test_paper_test_cap_is_explicit_and_applies_to_readers(self):
        self.problem.pilot.config.update(exam=True,exam_model_time_policy='test-cap',exam_test_call_timeout_seconds=1234)
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',side_effect=self.transport) as dispatch:
            await engine.call('reader-1','Synthetic',engine.reader_payload('reader-1',self.tex))
        self.assertEqual(dispatch.call_args.args[4],1234)
        self.runtime.seconds=20
        self.assertEqual(engine.stage_timeout(),20)

    async def test_saved_retrieval_explicit_formal_migration_preserves_turns_and_session(self):
        engine=self.retrieval_fixture(interrupted_count=2)
        meta_path=self.problem.pilot.host/'runtime/P1/paper-004-reconstruct/stage.meta.json'
        meta=json.loads(meta_path.read_text());meta.update(timeout_seconds=900,
            deadline_utc=meta['end_utc']);paper._write(meta_path,meta)
        self.problem.pilot.config.update(exam=True,exam_model_time_policy='formal-clock',
            explicit_policy_changes={'exam_model_time_policy':{'old':'legacy-caps','new':'formal-clock'}})
        with patch.object(paper,'call_stage',side_effect=self.transport) as dispatch:
            identity,_=await engine.call('reconstruct','Synthetic',{},writer=True)
        self.assertEqual(identity,'saved-writer')
        self.assertEqual(dispatch.call_args.args[1],'P1/paper-005-reconstruct')
        self.assertEqual(dispatch.call_args.args[4],3600)
        self.assertEqual(engine.ledger['admissions'][-1]['timeout_allocation']['retrieval_turn_limit'],4)


class MigrationTests(unittest.TestCase):
    prepare=continuation_fixtures.ContinuationRuntimeTests.prepare
    def setUp(self):
        continuation_fixtures.ContinuationRuntimeTests.setUp(self)
        source=self.fixture.source
        config=json.loads((source/'host-config.json').read_text())
        config['exam']=new_config(source,start=pilot.now()-timedelta(hours=23,minutes=10))
        config['deadline_utc']=config['exam']['submission_deadline_utc'];ExamRuntime(config['exam'])
        pilot.write(source/'host-config.json',config)
        registry=json.loads((source/'campaign/registry.json').read_text());registry['deadline_utc']=config['deadline_utc']
        pilot.write(source/'campaign/registry.json',registry)
        state=json.loads((source/'campaign/state.json').read_text());state['registry_sha256']=pilot.sha((source/'campaign/registry.json').read_bytes())
        pilot.write(source/'campaign/state.json',state)
        self.old=config

    def test_legacy_saved_policy_does_not_silently_change(self):
        config=self.prepare()
        self.assertEqual(model_time_policy(config),('legacy-caps',None))
        self.assertNotIn('exam_model_time_policy',config['explicit_policy_changes'])

    def test_explicit_native_migration_preserves_clock_parent_and_models(self):
        before={str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()}
        config=self.prepare(exam_model_time_policy='formal-clock')
        self.assertEqual(config['explicit_policy_changes']['exam_model_time_policy'],{'old':'legacy-caps','new':'formal-clock'})
        self.assertEqual(config['exam'],{**self.old['exam'],'state_root':str(self.root.resolve()/'exam')})
        self.assertEqual(config.get('models'),self.old.get('models'))
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()})
        self.assertEqual(json.loads(Path(config['continuation_reservation']).read_text())['explicit_policy_changes'],config['explicit_policy_changes'])

    def test_invalid_api_policy_rejected_before_reservation(self):
        for kwargs in [{'exam_model_time_policy':'formal-clock','paper_stage_timeout_seconds':900},
            {'exam_model_time_policy':'formal-clock','main_call_timeout_seconds':900},
            {'exam_model_time_policy':'test-cap'}, {'exam_test_call_timeout_seconds':900},
            {'exam_model_time_policy':'test-cap','exam_test_call_timeout_seconds':float('inf')}]:
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):self.prepare(**kwargs)
            self.assertFalse(self.root.exists())
            self.assertFalse((self.fixture.source.parent/'.continuation-reservations').exists())

    def test_native_continuation_cli_forwards_explicit_policy(self):
        argv=['pilot',str(self.root),'--continue-from',str(self.fixture.source),
              '--reconciliation',str(self.fixture.receipt),'--exam-model-time-policy','formal-clock']
        with patch.object(sys,'argv',argv),patch.object(pilot,'prepare_continuation') as prepare, \
             patch.object(pilot,'Pilot') as runner,contextlib.redirect_stdout(io.StringIO()):
            runner.return_value.run=AsyncMock(return_value=[])
            pilot.main()
        self.assertEqual(prepare.call_args.kwargs['exam_model_time_policy'],'formal-clock')
        self.assertIsNone(prepare.call_args.kwargs['exam_test_call_timeout_seconds'])

    def test_config_load_rejects_invalid_combinations(self):
        config=self.prepare(exam_model_time_policy='formal-clock')
        path=self.root/'host-config.json'
        for changes in [{'exam_test_call_timeout_seconds':900}, {'exam_model_time_policy':'test-cap'},
                {'exam_model_time_policy':'invalid'}]:
            pilot.write(path,{**config,**changes})
            with self.assertRaises(ValueError):pilot.Pilot(self.root)
