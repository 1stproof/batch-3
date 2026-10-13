"""Terminal operational obligations never turn healthy work into model polling."""
import asyncio
import json
from pathlib import Path
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_supervisor as outer
import codex_pilot as pilot

class AttentionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve(); self.root = self.base/'run'; self.root.mkdir(); (self.root/'host').mkdir()
        self.state = self.base/'keeper'; self.state.mkdir()
        self.since = (datetime.now(timezone.utc)-timedelta(minutes=10)).isoformat()
        self.config = {'problems':['p'], 'exam':{'submission_deadline_utc':
                       (datetime.now(timezone.utc)+timedelta(hours=10)).isoformat()}}
        outer.save(self.root/'host-config.json', self.config)
        outer.save(self.state/'attempt.json', {'root':str(self.root)})
        self.launch = {'pid':123, 'process_identity':'owned', 'operation_started_utc':self.since,
                       'attempt_sha256':outer.sha(self.state/'attempt.json')}
        outer.save(self.state/'launch.json', self.launch)

    def observe(self, *, alive=False, code=0):
        with patch.object(outer,'probe_process',return_value={'alive':alive, 'identity_match':True if alive else None}):
            return outer.observation(self.root,self.launch,exit_code=code)

    def result(self, paper=None):
        row={'problem':'p','status':'complete'}
        if paper is not None: row['paper']=paper
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[row]})

    def polished(self):
        folder=self.root/'exam/papers/p';folder.mkdir(parents=True,exist_ok=True)
        (folder/'paper.tex').write_text('synthetic');(folder/'final.pdf').write_bytes(b'%PDF-synthetic')
        return {'status':'polished','terminal':True,'polishing_complete':True,
                'best_available_tex':str(folder/'paper.tex'),'best_available_pdf':str(folder/'final.pdf')}

    def test_missing_malformed_stale_and_wrong_result_are_unexpected_exit(self):
        for value in (None, '{', json.dumps({'end_utc':'2000-01-01T00:00:00+00:00','results':[]}),
                      json.dumps({'end_utc':outer.now(),'results':[{'problem':'wrong','status':'complete'}]})):
            path=self.root/'pilot-result.json'
            if value is None:path.unlink(missing_ok=True)
            else:path.write_text(value)
            report=self.observe();self.assertEqual(report['status'],'unexpected_stop');self.assertTrue(report['needs_attention'])

    def test_actual_regular_confined_nonempty_artifacts_required(self):
        paper=self.polished();self.result(paper);self.assertEqual(self.observe()['status'],'exited')
        pdf=Path(paper['best_available_pdf'])
        for mode in ('absent','empty','symlink','external'):
            with self.subTest(mode=mode):
                pdf.unlink(missing_ok=True)
                outside=self.base/'outside.pdf';outside.write_bytes(b'%PDF-ok')
                if mode=='empty':pdf.write_bytes(b'')
                if mode=='symlink':pdf.symlink_to(outside)
                if mode=='external':paper['best_available_pdf']=str(outside)
                self.result(paper);self.assertEqual(self.observe()['status'],'paper_incomplete')
                paper['best_available_pdf']=str(pdf)

    def test_nonexam_partial_does_not_promise_paper(self):
        self.config.pop('exam');outer.save(self.root/'host-config.json',self.config)
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[{'problem':'p','status':'partial'}]})
        self.assertEqual(self.observe()['status'],'exited')

    def test_active_owned_writer_dominates_quota_and_missing_pdf(self):
        self.result({'status':'incomplete','terminal':False})
        with patch.object(outer,'failure_evidence',return_value=[{'failure_codes':['provider_quota']}]),patch.object(outer,'diagnose') as diagnose:
            report=self.observe(alive=True,code=None)
        self.assertEqual(report['status'],'running');self.assertFalse(report['needs_attention']);self.assertEqual(report['issues'],[])
        diagnose.assert_not_called()

    def test_deadline_and_authenticated_manual_stop_are_distinct(self):
        self.result({'status':'incomplete','terminal':False})
        self.assertEqual(self.observe()['status'],'paper_incomplete')
        self.config['exam']['submission_deadline_utc']=self.since
        outer.save(self.root/'host-config.json',self.config)
        self.assertEqual(self.observe()['status'],'deadline_reached')
        outer.save(self.root/'host/drain-request.json',{'schema_version':1,'action':'drain','request_id':'r','reason':'requested'})
        closed={'status':'admission_closed','closed_utc':outer.now(),'host_pid':123,'request_id':'r',
                'request_sha256':outer.sha(self.root/'host/drain-request.json'),'request_error':None}
        outer.save(self.root/'host/drain-admission-closed.json',closed)
        self.assertEqual(self.observe()['status'],'manual_stop')
        closed['host_pid']=999;outer.save(self.root/'host/drain-admission-closed.json',closed)
        self.assertEqual(self.observe()['status'],'deadline_reached')

    def test_current_handoff_distinct_from_historical_error(self):
        row={'problem':'p','status':'partial','errors':[{'reason':'explicit_operational_handoff','utc':outer.now(),'handoff':{'status':'supervisor_needed','authority':'supervisor_needed_no_dispatch_review_or_acceptance_authority'}}]}
        folder=self.root/'campaign/problems/p';folder.mkdir(parents=True)
        outer.save(folder/'operational-handoff.json',row['errors'][0]['handoff'])
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[row]})
        self.assertEqual(self.observe()['status'],'handoff')
        row['errors'][0]['utc']='2000-01-01T00:00:00+00:00'
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[row]})
        self.assertEqual(self.observe()['status'],'paper_incomplete')

    def test_saved_exit_revalidates_and_deduplicates_event(self):
        outer.save(self.state/'status.json',{'status':'exited','exit_code':0})
        with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
            first=outer.watch(self.state,once=True);second=outer.watch(self.state,once=True)
        self.assertEqual(first['status'],'unexpected_stop');self.assertEqual(first['attention_event'],second['attention_event'])
        self.assertEqual(len(list((self.state/'attention-events').glob('*.json'))),1)

    def test_task_snapshot_is_observational_owner_bound_and_transition_safe(self):
        state={'host_pid':123,'process_identity':'owned','started_utc':outer.now(), 'phase':'running',
               'tasks':[{'problem':'p','state':'unscheduled','obligation_pending':True}]}
        for phase in ('starting','finalizing','finished','running'):
            state['phase']=phase;outer.save(self.root/'host/task-state.json',state)
            report=self.observe(alive=True,code=None)
            self.assertEqual(bool(report['health']),phase=='running')
            self.assertEqual(report['status'],'running')
        state['process_identity']='other';outer.save(self.root/'host/task-state.json',state)
        self.assertFalse(self.observe(alive=True,code=None)['health'])
        state['process_identity']='owned';state['tasks'][0]['state']='done';outer.save(self.root/'host/task-state.json',state)
        self.assertFalse(self.observe(alive=True,code=None)['health'])

    def test_blocked_diagnosis_is_durable_and_never_invoked(self):
        outer.save(self.state/'keeper-plan.json',{'diagnose_on_failure':True})
        report=self.observe()
        with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnostic_quiescence',side_effect=ValueError('active child')),patch.object(outer,'diagnose') as diagnose:
            result=outer.keep(self.state)
        diagnose.assert_not_called();self.assertEqual(outer.read(self.state/'status.json'),result)
        self.assertEqual(result['diagnosis'],'blocked_pending_whole_stack_reconciliation')

    def test_actual_quiescence_keeps_reconciliation_barrier(self):
        with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
            with self.assertRaises(FileNotFoundError):outer.diagnostic_quiescence(self.state)
        with patch.object(outer,'probe_process',return_value={'alive':True,'identity_match':True}):
            with self.assertRaisesRegex(ValueError,'live or uncertain'):outer.diagnostic_quiescence(self.state)

    def test_native_run_emits_attention_without_outer_keeper(self):
        host=pilot.Pilot.__new__(pilot.Pilot);host.root=self.root;host.host=self.root/'host';host.host.mkdir(exist_ok=True)
        host.config={**self.config,'codex_binary':'codex','internet_browse':False,'watchdog_enabled':False}
        host.exam=Mock();host.campaign=Mock();host.drain=Mock();host.drain.poll.return_value=False
        host.watchdog_stop=asyncio.Event();host.tasks={};host.problems={}
        problem=Mock();problem.active_stage=None;problem.run=AsyncMock(return_value={'problem':'p','status':'partial'})
        with patch('pilot_continuation_reservation.validate_start'),patch.object(pilot,'subscription_preflight'),patch.object(pilot,'Problem',return_value=problem),patch('pilot_paper.prepare_exam_fallback'),patch('campaign_watchdog.capture_process_identity',return_value='owned'):
            asyncio.run(host.run())
        result=outer.read(self.root/'pilot-result.json')
        self.assertEqual(result['operational_attention']['status'],'paper_incomplete')
        self.assertTrue(result['operational_attention']['needs_attention'])
        self.assertEqual(outer.read(host.host/'task-state.json')['phase'],'finished')

    def test_malformed_nested_result_never_crashes(self):
        for row in ({'problem':[],'status':'complete'}, {'problem':'p','status':'complete','paper':[]},
                    {'problem':'p','status':'complete','errors':42}, {'problem':'p','status':'complete','paper':{'status':[]}}):
            outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[row]})
            self.assertEqual(self.observe()['status'],'unexpected_stop')

    def test_delayed_observation_cannot_relabel_early_stop_as_deadline(self):
        instant=datetime.now(timezone.utc)
        self.config['exam']['submission_deadline_utc']=(instant-timedelta(minutes=1)).isoformat()
        outer.save(self.root/'host-config.json',self.config)
        outer.save(self.root/'pilot-result.json',{'end_utc':(instant-timedelta(minutes=2)).isoformat(),
                   'results':[{'problem':'p','status':'partial','operational_failure':'infrastructure'}]})
        self.assertEqual(self.observe()['status'],'infrastructure_failed')
        (self.root/'pilot-result.json').unlink()
        self.assertEqual(self.observe()['status'],'unexpected_stop')

    def test_exam_early_partial_with_paper_still_needs_attention(self):
        paper=self.polished()
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),
                   'results':[{'problem':'p','status':'partial','paper':paper}]})
        self.assertEqual(self.observe()['status'],'unexpected_stop')

    def test_keep_healthy_owner_cannot_diagnose_or_reconcile(self):
        outer.save(self.state/'keeper-plan.json',{'diagnose_on_failure':True})
        with patch.object(outer,'watch',return_value=self.observe(alive=True,code=None)),patch.object(outer,'diagnostic_quiescence') as guard,patch.object(outer,'diagnose') as diagnose:
            self.assertEqual(outer.keep(self.state)['status'],'running')
        guard.assert_not_called();diagnose.assert_not_called()

    def test_two_problem_completion_notice_and_observer_failure_do_not_cancel_sibling(self):
        async def scenario(fail_write):
            host=pilot.Pilot.__new__(pilot.Pilot);host.root=self.root;host.host=self.root/'host'
            host.config={**self.config,'problems':['p','q'],'codex_binary':'codex','internet_browse':False,'watchdog_enabled':False}
            host.exam=Mock();host.campaign=Mock();host.drain=Mock();host.drain.poll.return_value=False
            host.watchdog_stop=asyncio.Event();host.tasks={};host.problems={}
            gate=asyncio.Event()
            async def qrun():
                await gate.wait();return {'problem':'q','status':'partial'}
            p=Mock(active_stage=None);p.run=AsyncMock(return_value={'problem':'p','status':'partial'})
            q=Mock(active_stage='q/current');q.run=qrun
            real_write=pilot.write
            def write(path,value):
                if fail_write and path.name in {'task-state.json','attention-observer-error.json'}:
                    raise OSError('synthetic observer disk failure')
                real_write(path,value)
            with patch('pilot_continuation_reservation.validate_start'),patch.object(pilot,'subscription_preflight'),patch.object(pilot,'Problem',side_effect=[p,q]),patch('pilot_paper.prepare_exam_fallback'),patch('campaign_watchdog.capture_process_identity',return_value='owned'),patch.object(pilot,'write',side_effect=write):
                running=asyncio.create_task(host.run())
                for _ in range(6):await asyncio.sleep(0)
                self.assertFalse(running.done());self.assertFalse(host.tasks['q'].done())
                self.assertTrue(host.problem_attention['p']['needs_attention'])
                if not fail_write:
                    report=outer.task_observations(self.root,{**self.launch,'pid':__import__('os').getpid()})
                    self.assertEqual(report[0]['kind'],'problem_ended_with_attention')
                gate.set();await running
                self.assertFalse(host.tasks['q'].cancelled())
            (self.root/'HOST-STARTED').unlink()
        asyncio.run(scenario(False));asyncio.run(scenario(True))

    def test_invalid_config_ids_and_nested_types_are_attention(self):
        self.result()
        for config in ([], None, {'problems':['../other']}, {'problems':['p','p']}, {'problems':[[]]}):
            outer.save(self.root/'host-config.json',config)
            self.assertEqual(self.observe()['status'],'unexpected_stop')

    def test_only_current_owner_watchdog_incidents_surface(self):
        state={'host_pid':123,'process_identity':'owned','started_utc':outer.now(),'observed_utc':outer.now(),
               'phase':'running','tasks':[{'problem':'p','state':'running','active_stage':'p/current'}]}
        outer.save(self.root/'host/task-state.json',state)
        incident={'kind':'stale_ownership','stage':'p/current'}
        report={'checked_utc':outer.now(),'current_incidents':[],'incidents':[incident]}
        outer.save(self.root/'host/watchdog.json',report)
        self.assertFalse(self.observe(alive=True,code=None)['health'])
        report['current_incidents']=[incident];outer.save(self.root/'host/watchdog.json',report)
        self.assertEqual(self.observe(alive=True,code=None)['health'][0]['kind'],'stale_ownership')
        report['checked_utc']='2000-01-01T00:00:00+00:00';outer.save(self.root/'host/watchdog.json',report)
        self.assertFalse(self.observe(alive=True,code=None)['health'])

    def test_intentional_stop_with_failure_remains_ineligible_for_diagnosis(self):
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),
                   'results':[{'problem':'p','status':'partial','operational_failure':'infrastructure'}]})
        self.config['exam']['submission_deadline_utc']=self.since
        outer.save(self.root/'host-config.json',self.config)
        report=self.observe();self.assertEqual(report['status'],'deadline_reached');self.assertTrue(report['needs_attention'])
        outer.save(self.state/'keeper-plan.json',{'diagnose_on_failure':True})
        with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnostic_quiescence') as guard,patch.object(outer,'diagnose') as diagnose:
            outer.keep(self.state)
        guard.assert_not_called();diagnose.assert_not_called()

    def test_reconciled_terminal_event_routes_one_bounded_diagnosis(self):
        binary=self.base/'codex';binary.write_text('synthetic binary')
        outer.save(self.state/'keeper-plan.json',{'diagnose_on_failure':True,
                   'diagnostic_codex':{'path':str(binary),'sha256':outer.sha(binary)}})
        report=self.observe()
        def diagnosed(*args,**kwargs):
            outer.save(self.state/'diagnostic-attempt.json',{'reserved_once':True},exclusive=True)
        with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnostic_quiescence'),patch.object(outer,'diagnose',side_effect=diagnosed) as diagnose:
            self.assertEqual(outer.keep(self.state)['diagnosis'],'attempted_once')
            outer.keep(self.state)
        self.assertEqual(diagnose.call_count,1)

    def test_malformed_drain_receipt_does_not_break_healthy_observation(self):
        for malformed in (None, [], 'bad'):
            outer.save(self.root/'host/drain-admission-closed.json',malformed)
            outer.save(self.root/'host/drain-request.json',malformed)
            self.assertEqual(self.observe(alive=True,code=None)['status'],'running')

    def test_recovered_quota_is_scoped_to_same_problem(self):
        evidence=[{'path':'host/runtime/p/001/stage.meta.json','problem':'p','start_utc':self.since,
                   'failure_codes':['provider_quota'],'status':'process_failed'}]
        later={'path':'host/runtime/p/002/stage.meta.json','problem':'p','start_utc':outer.now(),
               'failure_codes':[],'status':'completed'}
        with patch.object(outer,'failure_evidence',return_value=evidence+[later]):
            self.assertEqual(self.observe()['status'],'unexpected_stop')
        later['status']='process_failed'
        with patch.object(outer,'failure_evidence',return_value=evidence+[later]):
            self.assertEqual(self.observe()['status'],'quota_paused')
        later['status']='completed'
        later['problem']='q';later['path']='host/runtime/q/002/stage.meta.json'
        with patch.object(outer,'failure_evidence',return_value=evidence+[later]):
            self.assertEqual(self.observe()['status'],'quota_paused')
