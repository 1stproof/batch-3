"""Prospective guardian recovery with real native checkpoints and no model calls."""
import asyncio
from datetime import datetime, timedelta, timezone
import errno
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as pilot
import codex_transport as transport
import pilot_continuation as native
import pilot_guardian as guardian
import pilot_supervisor as outer
import pilot_proof_document as documents
from pilot_exam import new_config
import test_pilot_continuation as fixtures


class GuardianTests(unittest.TestCase):
    def setUp(self):
        f = self.fixture = fixtures.ContinuationTests(); f.setUp(); self.addCleanup(f.doCleanups)
        f.base=f.base.resolve();f.source=f.source.resolve();f.folder=f.folder.resolve();f.receipt=f.receipt.resolve()
        self.root = f.source; self.folder = f.base/'guardian'; self.folder.mkdir()
        self.operation = self.folder/'generations/000'; self.operation.mkdir(parents=True)
        self.since = (datetime.now(timezone.utc)-timedelta(minutes=2)).isoformat()
        self.start = (datetime.now(timezone.utc)-timedelta(minutes=1)).isoformat()
        self.end = (datetime.now(timezone.utc)-timedelta(seconds=5)).isoformat()
        self.launch = {'pid': 900000, 'root': str(f.source), 'operation_started_utc': self.since}
        self.plan = {'root':str(f.source), 'pilot_arguments':['--problems','synthetic.json'],
            'recover_on_failure':True, 'source':outer.source_binding(), 'environment':transport.subscription_environment(),
            'recovery':guardian.route_plan(self.folder,['--codex',sys.executable]), 'diagnose_on_failure':False}
        outer.save(self.folder/'keeper-plan.json',self.plan)
        self.state = {'schema_version':1,'rule':guardian.RULE,'plan_sha256':outer.sha(self.folder/'keeper-plan.json'),
            'generations':[{'root':str(f.source),'operation':str(self.operation),'arguments':[], 'phase':'reserved','launch_claimed':True}], 'recoveries':[]}
        outer.save(self.folder/'guardian-state.json',self.state)
        outer.save(self.operation/'attempt.json', {'root':str(f.source)})
        self.launch['attempt_sha256']=outer.sha(self.operation/'attempt.json')
        outer.save(self.operation/'launch.json',self.launch)
        config=outer.read(f.source/'host-config.json')
        code,policy=pilot.freeze_runtime(f.source)
        config.update(code_hashes=code,policy_hashes=policy, proof_document_version=1,lite_local_verification_version=1,
            main_response_contract_version=1,original_scope_review_count=2,assessment_protocol_epoch=pilot.ASSESSMENT_PROTOCOL_EPOCH,
            parallel_route_scouts=pilot.route_config(), campaign_phase='phase1', codex_binary=str(Path(sys.executable).resolve()),
            model_concurrency=1,internet_browse=False,legacy_main_stages=[],source_url='https://example.invalid/original',
            watchdog_enabled=False,watchdog_interval_seconds=300,
            guardian_recovery_route={'path':str(self.folder/'keeper-plan.json'),'sha256':outer.sha(self.folder/'keeper-plan.json')})
        exam=new_config(f.source,start=datetime.now(timezone.utc)-timedelta(minutes=5))
        config.update(exam=exam,deadline_utc=exam['submission_deadline_utc'])
        outer.save(f.source/'host-config.json',config); (f.source/'exam').mkdir()
        outer.save(f.source/'exam/clock.json',exam)
        registry=outer.read(f.source/'campaign/registry.json');registry['deadline_utc']=config['deadline_utc']
        outer.save(f.source/'campaign/registry.json',registry)
        state=outer.read(f.source/'campaign/state.json');state['registry_sha256']=outer.sha(f.source/'campaign/registry.json')
        outer.save(f.source/'campaign/state.json',state)
        candidate={'proof_markdown':'latest valid candidate','answer_statement':'synthetic answer','ledger':{'rows':[]}}
        candidate=json.loads(json.dumps(candidate,sort_keys=True))
        raw={**candidate,'response_type':'candidate_update'}
        main=f.calls[0]; main['answer_sha256']=guardian.binding(raw) # overwritten with exact serialized bytes below
        outer.save(f.folder/'001-main-dossier.json',raw)
        answer=(f.folder/'001-main-dossier.json').read_bytes()
        (f.source/'host/runtime'/main['name']/'stage.answer.txt').write_bytes(answer)
        main['answer_sha256']=outer.digest(answer)
        outer.save(f.source/'host/runtime'/main['name']/'stage.meta.json',main)
        outer.save(f.folder/'accepted-dossier.json',{'source_stage':main['name'],'raw_response_sha256':main['answer_sha256'],'effective_candidate':candidate})
        outer.save(f.folder/'current-candidate.json',candidate)
        documents.submit(f.folder,problem_id='problem',original_sha256=registry['problems']['problem']['sha256'],main_session='main-session',expected_revision=None,candidate=candidate,
            producer={'stage':main['name'],'request_id':main['request_id'],'session_id':'main-session'})
        failed=f.calls[-1]; failed.pop('pid'); failed.pop('session_id')
        failed.update(status='process_launch_failed',start_utc=self.start,end_utc=self.end,resume_session='main-session',model_dispatched=False,
            local_spawn_failure={'schema_version':1,'errno':errno.EAGAIN,'boundary':'await_create_subprocess_exec','model_dispatched':False})
        self.meta_path=f.source/'host/runtime'/failed['name']/'stage.meta.json';outer.save(self.meta_path,failed)
        (f.folder/'004-main-repair.json').unlink()
        self.refresh_failure()
        self.report={'status':'infrastructure_failed','exit_code':0,'process':{'alive':False,'identity_match':False}}

    def refresh_failure(self):
        f=self.fixture; meta=outer.read(self.meta_path)
        self.failure={'name':meta['name'],'request_id':meta['request_id'],'meta_sha256':outer.sha(self.meta_path),'local_spawn_failure':meta['local_spawn_failure']}
        errors=[{'type':'BlockingIOError','pre_dispatch_failure':self.failure,'utc':self.end}]
        progress=outer.read(f.folder/'host-progress.json');progress.update(calls=f.calls[:-1],errors=errors)
        outer.save(f.folder/'host-progress.json',progress)
        outer.save(f.source/'pilot-result.json',{'end_utc':self.end,'results':[{'problem':'problem','status':'partial','operational_failure':'infrastructure','errors':errors,
            'paper':{'status':'deferred_pre_dispatch_recovery','terminal':False,'polishing_complete':False}}]})

    def census(self, suffix='census'):
        with patch.object(native.os,'kill',side_effect=ProcessLookupError), patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')):
            return guardian.census(self.root,self.launch,self.fixture.base/suffix)

    def candidate(self, receipt):
        with patch.object(native.os,'kill',side_effect=ProcessLookupError), patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')):
            return guardian.recovery_candidate(self.root,self.launch,self.plan,receipt)

    def test_real_native_prepare_preserves_session_clock_history_and_resumes_main(self):
        receipt,files=self.census()
        self.candidate(receipt)
        target=self.fixture.base/'successor'
        before=guardian.file_map(self.root)
        with patch.object(native.os,'kill',side_effect=ProcessLookupError), patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), patch.object(pilot,'subscription_preflight',return_value={}):
            config=pilot.prepare_continuation(self.root,target,receipt)
        self.assertEqual(config['explicit_policy_changes'],{})
        self.assertEqual(config['exam']['start_utc'],outer.read(self.root/'host-config.json')['exam']['start_utc'])
        self.assertEqual(config['exam']['submission_deadline_utc'],outer.read(self.root/'host-config.json')['exam']['submission_deadline_utc'])
        saved=outer.read(target/'continuation-checkpoint.json')['problems']['problem']
        self.assertEqual(saved['main_session'],'main-session');self.assertEqual(saved['counter'],4)
        self.assertEqual(saved['findings'],[{'id':'open-finding'}]);self.assertEqual(guardian.file_map(self.root),before)
        seen=[]
        async def main(problem,instruction,dossier=False,purpose=None):
            seen.append((problem.session,problem.counter,dossier))
            raise RuntimeError('local fixture ends at resumed main boundary')
        runner=pilot.Pilot(target)
        with patch.object(pilot.Problem,'main_turn',main), patch.object(pilot.Problem,'execution',side_effect=AssertionError('completed work replayed')), patch.object(pilot,'call_stage',side_effect=AssertionError('paid call')):
            result=asyncio.run(pilot.Problem(runner,'problem')._run_research())
        self.assertEqual(seen,[('main-session',4,False)]);self.assertEqual(result['status'],'partial')

    def test_guardian_launches_one_real_local_successor_with_native_prepare(self):
        fake_source=self.fixture.base/'fake-launcher';fake_source.mkdir()
        program="""import sys,asyncio,json
from pathlib import Path
sys.path.insert(0, SOURCE)
from unittest.mock import patch
import codex_pilot as pilot
import pilot_continuation as native
import subprocess
real_run=subprocess.run
def isolated_run(args,**kwargs):
    if args[:2]==['ps','-axo']:return subprocess.CompletedProcess(args,0,'','')
    return real_run(args,**kwargs)
root=Path(sys.argv[1]);args=sys.argv[2:]
parent=Path(args[args.index('--continue-from')+1]);receipt=Path(args[args.index('--reconciliation')+1])
with patch.object(pilot,'subscription_preflight',return_value={}),patch.object(native,'_assert_stopped',return_value=None),patch.object(native.subprocess,'run',side_effect=isolated_run):
    config=pilot.prepare_continuation(parent,root,receipt)
runner=pilot.Pilot(root)
async def resumed(problem,instruction,dossier=False,purpose=None):
    (root/'local-progress.json').write_text(json.dumps({'session':problem.session,'counter':problem.counter,'dossier':dossier,'original_clock':config['exam']['start_utc']}))
    raise RuntimeError('local fixture stopped after actual restored-main entry')
with patch.object(pilot.Problem,'main_turn',resumed),patch.object(pilot,'call_stage',side_effect=AssertionError('unexpected paid call')):
    asyncio.run(pilot.Problem(runner,'problem')._run_research())
""".replace('SOURCE',repr(str(pilot.REPO/'src')))
        (fake_source/'codex_pilot.py').write_text(program)
        original_watch=outer.watch;original_run=outer.run;original_popen=subprocess.Popen
        seen=[];children=[];real_run=subprocess.run
        def isolated_run(args,**kwargs):
            if args[:2]==['ps','-axo']:return subprocess.CompletedProcess(args,0,'','')
            return real_run(args,**kwargs)
        def popen(*args,**kwargs):
            child=original_popen(*args,**kwargs)
            if str(fake_source/'codex_pilot.py') in args[0]:children.append(child)
            return child
        def watch(operation,**kwargs):
            if operation==self.operation:return self.report
            return original_watch(operation,**kwargs)
        def run(operation,root,args,**kwargs):
            seen.append(str(root));return original_run(operation,root,args,interval=.01)
        with patch.object(outer,'watch',side_effect=watch),patch.object(outer,'run',side_effect=run),patch.object(outer,'SOURCE',fake_source),patch.object(outer,'source_binding',return_value=self.plan['source']),patch.object(subprocess,'Popen',side_effect=popen),patch.object(subprocess,'run',side_effect=isolated_run),patch.object(native,'_assert_stopped',return_value=None),patch.object(transport,'call_stage',side_effect=AssertionError('guardian model call')):
            result=guardian.keep(self.folder)
            for child in children:child.wait(timeout=10)
            repeated=guardian.keep(self.folder)
        self.assertEqual(len(seen),1);self.assertEqual(result,repeated)
        target=Path(seen[0]);saved=outer.read(target/'local-progress.json')
        self.assertEqual(saved['session'],'main-session');self.assertEqual(saved['counter'],4);self.assertFalse(saved['dossier'])
        self.assertEqual(saved['original_clock'],outer.read(self.root/'host-config.json')['exam']['start_utc'])
        self.assertEqual(outer.read(target/'host-config.json')['explicit_policy_changes'],{})
        ledger=outer.read(self.folder/'guardian-state.json')
        self.assertEqual(len(ledger['generations']),2);self.assertEqual(len(ledger['recoveries']),1)
        self.assertTrue((Path(ledger['generations'][1]['operation'])/'launch.json').exists())

    def test_reserved_generation_without_attempt_never_replays(self):
        (self.operation/'attempt.json').unlink()
        with patch.object(outer,'run',side_effect=AssertionError('uncertain replay')),patch.object(transport,'call_stage',side_effect=AssertionError('guardian model')):
            self.assertEqual(guardian.keep(self.folder)['status'],'launch_uncertain')

    def test_armed_startup_rechecks_before_auth_or_paid_admission(self):
        from types import SimpleNamespace
        runner=SimpleNamespace(root=self.root,config=outer.read(self.root/'host-config.json'))
        with patch.object(guardian,'verify_route',side_effect=ValueError('source changed after parent check')),patch.object(pilot,'subscription_preflight',side_effect=AssertionError('early auth')),patch.object(pilot,'call_stage',side_effect=AssertionError('early model')):
            with self.assertRaisesRegex(ValueError,'source changed'):asyncio.run(pilot.Pilot.run(runner))
        runner.config['assessment_protocol_epoch']='old'
        with patch.object(pilot,'subscription_preflight',side_effect=AssertionError('early auth')),patch.object(pilot,'call_stage',side_effect=AssertionError('early model')):
            with self.assertRaisesRegex(ValueError,'protocol settings'):asyncio.run(pilot.Pilot.run(runner))

    def test_malformed_enrollment_cannot_bypass_startup_guard(self):
        from types import SimpleNamespace
        runner=SimpleNamespace(root=self.root,config=outer.read(self.root/'host-config.json'))
        for path,mutation in [(self.folder/'keeper-plan.json',lambda value:{**value,'extra':'tampered'}),
                              (self.folder/'guardian-state.json',lambda value:{**value,'plan_sha256':'wrong'}),
                              (self.folder/'guardian-state.json',lambda value:{**value,'generations':[]})]:
            before=path.read_bytes();outer.save(path,mutation(outer.read(path)))
            with patch.object(pilot,'subscription_preflight',side_effect=AssertionError('auth bypass')),patch.object(pilot,'call_stage',side_effect=AssertionError('paid bypass')):
                with self.assertRaises(ValueError):asyncio.run(pilot.Pilot.run(runner))
            path.write_bytes(before)
        for malformed in ({}, [], '', False):
            with patch.object(pilot,'subscription_preflight',side_effect=AssertionError('malformed bypass')):
                with self.assertRaises(ValueError):asyncio.run(pilot.Pilot.run(SimpleNamespace(root=self.root,config={**runner.config,'guardian_recovery_route':malformed})))
        target=self.fixture.base/'manual-successor'
        manual={**runner.config,'continuation_parent':str(self.root)}
        with patch.object(guardian,'verify_route',side_effect=AssertionError('manual source migration intercepted')):
            guardian.startup_guard(target,manual)

    def test_python_symlink_retarget_cannot_bypass_pinned_route(self):
        first=self.fixture.base/'python-a';second=self.fixture.base/'python-b';link=self.fixture.base/'python-link'
        first.write_bytes(b'first pinned interpreter');second.write_bytes(b'different interpreter');link.symlink_to(first)
        plan={**self.plan,'recovery':{**self.plan['recovery'],'python':{'path':str(first),'sha256':outer.sha(first)}}}
        with patch.object(guardian.sys,'executable',str(link)),patch.object(transport,'call_stage',side_effect=AssertionError('route model')):
            guardian.verify_route(plan)
            link.unlink();link.symlink_to(second)
            with self.assertRaisesRegex(ValueError,'Python executable route changed'):guardian.verify_route(plan)
        self.assertEqual(outer.sha(first),plan['recovery']['python']['sha256'])

    def test_recipe_is_prospective_scheduled_and_zero_model(self):
        import plistlib
        folder=self.fixture.base/'new-recipe';target=self.fixture.base/'fresh'
        with patch.object(transport,'call_stage',side_effect=AssertionError('recipe model')),patch.object(transport,'subscription_preflight',side_effect=AssertionError('recipe account')):
            result=outer.recipe(folder,target,['--problems','inputs.json','--exam','--internet-browse','on','--codex',sys.executable],recover_on_failure=True)
        self.assertEqual(result['status'],'recipe_created_not_installed')
        recipe=plistlib.loads((folder/'keeper.plist').read_bytes())
        self.assertEqual(recipe['StartInterval'],600);self.assertEqual(recipe['KeepAlive'],{'SuccessfulExit':False})
        self.assertFalse(target.exists())

    def test_unknown_live_or_reused_pid_blocks_census(self):
        with patch.object(native.os,'kill',return_value=None):
            with self.assertRaisesRegex(ValueError,'still exists'):guardian.census(self.root,self.launch,self.fixture.base/'census')

    def test_no_current_receipt_or_nontransient_or_published_answer_is_eligible(self):
        receipt,_=self.census()
        for field,value in [('model_dispatched',True),('pid',900005),('status','process_failed')]:
            original=self.meta_path.read_bytes();meta=outer.read(self.meta_path);meta[field]=value;outer.save(self.meta_path,meta);self.refresh_failure()
            with self.assertRaises(ValueError):self.candidate(receipt)
            self.meta_path.write_bytes(original);self.refresh_failure()
        self.meta_path.with_name('stage.answer.txt').write_text('late answer')
        with self.assertRaisesRegex(ValueError,'answer or event'):self.candidate(receipt)

    def test_exact_source_protocol_and_route_required(self):
        receipt,_=self.census();path=self.root/'host-config.json';before=path.read_bytes()
        for key,value in [('code_hashes',{}),('assessment_protocol_epoch','old'),('explicit_policy_changes',{'x':1}),('codex_binary','other')]:
            config=outer.read(path);config[key]=value;outer.save(path,config)
            with self.assertRaises(ValueError):self.candidate(receipt)
            path.write_bytes(before)

    def test_content_fingerprint_ignores_attempts_and_whitespace(self):
        receipt,_=self.census();original=self.candidate(receipt)
        self.assertEqual(original['progress'],self.candidate(receipt)['progress'])
        from pilot_review_exhaustion import projection
        base={'proof_markdown':'A proof','answer_statement':'An answer','ledger':{'rows':[{'claim':'A claim'}]}}
        variant={'proof_markdown':' A  proof\n','answer_statement':'An\tanswer','ledger':{'rows':[{'claim':' A claim '}]},
            'request_id':'new','utc':'later','artifact_path':'new-segment/artifact','duplicate_answers':['same','same']}
        self.assertEqual(guardian.binding(projection(base)),guardian.binding(projection(variant)))
        variant['proof_markdown']='A substantively changed proof'
        self.assertNotEqual(guardian.binding(projection(base)),guardian.binding(projection(variant)))
        # The same scientific checkpoint blocks even a different local errno.
        meta=outer.read(self.meta_path);meta['local_spawn_failure']['errno']=errno.ENOMEM;outer.save(self.meta_path,meta);self.refresh_failure()
        self.assertEqual(original['progress'],self.candidate(receipt)['progress'])

    def test_existing_healthy_and_blocked_reentry_use_no_models_or_route_refresh(self):
        with patch.object(outer,'watch',return_value={'status':'running'}) as watch, patch.object(guardian,'verify_route',side_effect=AssertionError('healthy route refresh')), patch.object(guardian,'census',side_effect=AssertionError('healthy census')), patch.object(pilot,'call_stage',side_effect=AssertionError('paid guardian')):
            self.assertEqual(guardian.keep(self.folder)['status'],'running');watch.assert_called_once()
        state=outer.read(self.folder/'guardian-state.json');state['generations'][-1]['terminal_report']={'status':'infrastructure_failed','recovery':'blocked'};outer.save(self.folder/'guardian-state.json',state)
        with patch.object(outer,'watch',side_effect=AssertionError('blocked re-observation')), patch.object(guardian,'verify_route',side_effect=AssertionError('blocked route refresh')):
            self.assertEqual(guardian.keep(self.folder)['recovery'],'blocked')

    def test_repeat_checkpoint_blocks_successor_and_cached_reentry(self):
        receipt,_=self.census();candidate=self.candidate(receipt)
        state=outer.read(self.folder/'guardian-state.json');state['recoveries']=[candidate];outer.save(self.folder/'guardian-state.json',state)
        with patch.object(outer,'watch',return_value=self.report), patch.object(native.os,'kill',side_effect=ProcessLookupError), patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), patch.object(outer,'run',side_effect=AssertionError('repeat launch')):
            result=guardian.keep(self.folder)
        self.assertIn('no new durable progress',result['recovery_reason'])
        with patch.object(guardian,'census',side_effect=AssertionError('repeat census')):
            self.assertEqual(guardian.keep(self.folder),result)

    def test_transport_receipt_only_for_confirmed_os_spawn_error(self):
        for number in (errno.EAGAIN,errno.ENOMEM,errno.EACCES):
            target=self.fixture.base/('transport-'+str(number))
            with patch.object(transport,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'test'}), patch.object(transport.asyncio,'create_subprocess_exec',side_effect=OSError(number,'synthetic local spawn failure')):
                with self.assertRaises(OSError) as raised:
                    asyncio.run(transport.call_stage(target,'problem/001-main','synthetic','gpt-6-astra',5,internet_browse=False))
            meta=outer.read(target/'runtime/problem/001-main/stage.meta.json')
            self.assertEqual(meta['status'],'process_launch_failed')
            self.assertEqual('local_spawn_failure' in meta,number in (errno.EAGAIN,errno.ENOMEM))
            if number in (errno.EAGAIN,errno.ENOMEM):
                self.assertFalse(meta['model_dispatched']);self.assertEqual(raised.exception.pilot_stage_failure['meta_sha256'],outer.sha(target/'runtime/problem/001-main/stage.meta.json'))

    def test_exam_defers_only_armed_route_without_snapshot_or_pdf_claim(self):
        from types import SimpleNamespace
        research=outer.read(self.root/'pilot-result.json')['results'][0]
        class Exam:
            async def dispatch(self,problem):return {'status':'ordinary-paper-path'}
            def paper_dir(self,ident):return self_root/'exam/papers'/ident
        self_root=self.root
        class Drain:
            def poll(self):return False
        problem=SimpleNamespace(pilot=SimpleNamespace(root=self.root,config=outer.read(self.root/'host-config.json'),exam=Exam(),drain=Drain()), ident='problem',status=lambda x:None)
        async def research_call():return research
        problem._run_research=research_call
        from pilot_paper import prepare_exam_fallback
        fallback=prepare_exam_fallback(problem,problem.pilot.exam)
        fallback_before=Path(fallback['tex']).read_bytes()
        result=asyncio.run(pilot.Problem.run(problem));self.assertEqual(result['paper']['status'],'deferred_pre_dispatch_recovery');self.assertIsNone(result['paper']['best_available_pdf'])
        self.assertFalse((self.root/'exam/papers/problem/snapshot').exists())
        self.assertEqual(Path(result['paper']['best_available_tex']).read_bytes(),fallback_before)
        problem.pilot.config['guardian_recovery_route']['sha256']='wrong'
        result=asyncio.run(pilot.Problem.run(problem));self.assertEqual(result['paper']['status'],'ordinary-paper-path')
        problem.pilot.config.pop('guardian_recovery_route')
        result=asyncio.run(pilot.Problem.run(problem));self.assertEqual(result['paper']['status'],'ordinary-paper-path')

if __name__=='__main__':unittest.main()
