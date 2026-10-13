"""Dynamic host dispatches, advisory-only and bounded by scientific census."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
from pilot_candidate_contract import apply_main_response,candidate_hash
from pilot_route_scouts import eligible_obstructions,validate_tasks,validate_config,fresh_config
import test_pilot_review_handoff as fixture

class ParallelRouteTests(unittest.TestCase):
    def setUp(self):
        f=fixture.ReviewHandoffTests();f.setUp();self.addCleanup(f.doCleanups)
        self.f,self.x=f,f.problem;x=self.x
        x.statement='Exact original';x.dossier={};x.findings=[];x.triage_history=[];x.route_scout_history=[]
        x.status=lambda phase: None
        x.current['ledger']['rows']=[{'id':'r','claim':'A scientifically difficult existing inference','closed':False}]
        x.pilot.config={'parallel_route_scouts':{'enabled':True,'width':2,'user_requested':True},
            'internet_browse':False,'codex_binary':'synthetic','campaign_phase':'phase2','accounting_segment_id':'segment'}
        x.pilot.root=x.folder;x.pilot.host=x.folder/'host';x.pilot.semaphore=asyncio.Semaphore(2)
        x.pilot.remaining=lambda:1000
        x.tasks=[{'angle':angle,'task':'Explore '+angle,'context':'Complete bounded context for exact row r',
                  'purpose':'certificate_strategy','target_row_ids':['r'],'obstruction_ids':[]}
                 for angle in ('representation','existing-certificate-cost')]
        review={'triaged_rows':['r'],'unresolved_findings':[]}
        meta=f.meta('independent-proof');meta['name']='q/004-proof-review'
        p.write(x.folder/'review-004-effective.json',review)
        x.triage_history=[{'candidate_binding':p.triage_binding(x.current),'selected_rows':['r'],
                          'receipt':x.review_receipt(meta)}]
        x.calls=[meta];x.consecutive_failures=0;x.errors=[]
        # Exercise typed checkpoint overlay, not a directly injected task/current review.
        raw={'response_type':'blocked_checkpoint','selected_candidate_sha256':candidate_hash(x.current),
            'checkpoint_metadata':{'reason':'Request independently chosen scientific alternatives'},
            'proposed_work':{'sol_tasks':[],'python_probe':'','lean_probe':'','lean_probe_rows':[],
                             'route_scout_tasks':x.tasks},'unreviewed_findings':[],'review_request':'route_exploration'}
        # Existing complete candidates have explicit empty execution fields.
        x.current.update(sol_tasks=[],python_probe='',lean_probe='',lean_probe_rows=[])
        raw['selected_candidate_sha256']=candidate_hash(x.current)
        x.triage_history[0]['candidate_binding']=p.triage_binding(x.current)
        x.current,checkpoint=apply_main_response(raw,{candidate_hash(x.current):x.current})
        self.assertTrue(checkpoint['actionable'])

    def portfolio(self, count):
        tasks = []
        for i in range(count):
            tasks.append({**copy.deepcopy(self.x.tasks[i % 2]),
                          'angle': 'distinct-angle-' + str(i), 'task': 'Distinct task ' + str(i)})
        return tasks

    def test_config_legacy_and_dynamic_bounds_and_all_pair_distinctness(self):
        self.assertEqual(validate_config(), {'enabled':False,'width':2,'user_requested':False})
        self.assertEqual(validate_config(fresh_config()), {'enabled':True,'width':4,'user_requested':True})
        for width in (2,3,4):
            self.assertEqual(validate_config({**fresh_config(),'width':width})['width'],width)
        for width in (True,1,5,4.0):
            with self.assertRaises(ValueError):validate_config({**fresh_config(),'width':width})
        for count in (0,2,3,4):validate_tasks(self.portfolio(count))
        for count in (1,5):
            with self.assertRaises(ValueError):validate_tasks(self.portfolio(count))
        for field in ('angle','task'):
            tasks=self.portfolio(4);tasks[3][field]=tasks[2][field]
            with self.assertRaises(ValueError):validate_tasks(tasks)

    def test_three_and_four_real_concurrent_advisory_calls_no_peer_leak_or_topup(self):
        for count in (3,4):
            with self.subTest(count=count):
                self.setUp();x=self.x
                x.pilot.config['parallel_route_scouts']=fresh_config()
                x.current['route_scout_tasks']=self.portfolio(count)
                x.pilot.semaphore=asyncio.Semaphore(4)
                async def scenario():
                    entered=[];barrier=asyncio.Event()
                    async def transport(host,name,prompt,model,timeout,resume,**kwargs):
                        entered.append((name,prompt,model,resume))
                        if len(entered)==count:barrier.set()
                        await asyncio.wait_for(barrier.wait(),1)
                        meta=self.f.meta('actor-'+name);meta.update(name=name,prompt_sha256=p.sha(prompt))
                        return meta,{'skeleton':'PRIVATE-PEER-'+name}
                    with patch.object(p,'call_stage',side_effect=transport):
                        result=await x.route_scouts()
                        self.assertEqual(result['status'],'returned_advisory')
                        self.assertEqual(len(result['slots']),count)
                        self.assertEqual(len(entered),count)
                        self.assertTrue(all(call[2:]==(p.ASTRA,None) for call in entered))
                        self.assertTrue(all('PRIVATE-PEER-' not in call[1] for call in entered))
                        self.assertEqual(len({s['receipt']['session_id'] for s in result['slots']}),count)
                        x.current['route_scout_tasks']=self.portfolio(4)
                        self.assertEqual((await x.route_scouts())['status'],'already_assessed')
                        self.assertEqual(len(entered),count)
                asyncio.run(scenario())

    def test_saved_width_and_disabled_modes_never_admit_extra_calls(self):
        self.x.current['route_scout_tasks']=self.portfolio(4)
        with patch.object(p,'call_stage',side_effect=AssertionError('must not dispatch')):
            result=asyncio.run(self.x.route_scouts())
            self.assertEqual(result['max_scouts'],2)
            self.assertFalse(self.x.route_scout_history)
            self.x.pilot.config['parallel_route_scouts']=None
            self.assertEqual(asyncio.run(self.x.route_scouts())['reason'],'parallel routes disabled')
            self.x.pilot.config['parallel_route_scouts']=fresh_config()
            self.x.current['route_scout_tasks']=[]
            self.assertIsNone(asyncio.run(self.x.route_scouts()))

    def test_global_thirty_model_slots_admit_thirty_and_queue_thirty_first(self):
        async def scenario():
            x=self.x;x.pilot.semaphore=asyncio.Semaphore(30)
            entered=[];active=0;peak=0
            thirty=asyncio.Event();release=asyncio.Event()
            async def transport(host,name,prompt,model,timeout,resume,**kwargs):
                nonlocal active,peak
                entered.append(name);active+=1;peak=max(peak,active)
                if len(entered)==30:thirty.set()
                await release.wait()
                active-=1
                meta=self.f.meta('actor-'+name);meta.update(name=name)
                return meta,{'advisory':'synthetic'}
            with patch.object(p,'call_stage',side_effect=transport):
                jobs=[asyncio.create_task(x.call('route-scout-'+str(i),'Synthetic',
                       model=p.ASTRA,timeout=300)) for i in range(31)]
                try:
                    await asyncio.wait_for(thirty.wait(),2)
                    await asyncio.sleep(0)
                    self.assertEqual(len(entered),30)
                    self.assertEqual(peak,30)
                    release.set()
                    await asyncio.wait_for(asyncio.gather(*jobs),2)
                    self.assertEqual(len(entered),31)
                    self.assertEqual(peak,30)
                finally:
                    release.set()
                    for job in jobs:
                        if not job.done():job.cancel()
                    await asyncio.gather(*jobs,return_exceptions=True)
        asyncio.run(scenario())

    def test_four_slots_duplicate_late_identity_is_not_success(self):
        self.x.pilot.config['parallel_route_scouts']=fresh_config()
        self.x.current['route_scout_tasks']=self.portfolio(4)
        async def transport(host,name,prompt,model,timeout,resume,**kwargs):
            sid='collision' if name.endswith(('3','4')) else 'actor-'+name
            meta=self.f.meta(sid);meta.update(name=name)
            return meta,{'partial':'preserve'}
        with patch.object(p,'call_stage',side_effect=transport):
            result=asyncio.run(self.x.route_scouts())
        self.assertEqual(result['status'],'incomplete_advisory')
        self.assertEqual(len(result['slots']),4)

    def test_failure_in_fourth_slot_preserves_all_siblings_and_no_replay(self):
        self.x.pilot.config['parallel_route_scouts']=fresh_config()
        self.x.current['route_scout_tasks']=self.portfolio(4)
        finished=[]
        async def transport(host,name,prompt,model,timeout,resume,**kwargs):
            await asyncio.sleep(0)
            meta=self.f.meta('actor-'+name);meta.update(name=name,status='process_failed' if name.endswith('4') else 'completed')
            finished.append(name)
            return meta,{'partial':'preserved-'+name}
        with patch.object(p,'call_stage',side_effect=transport):
            with self.assertRaises(p.StageFailure):asyncio.run(self.x.route_scouts())
        self.assertEqual(len(finished),4)
        result=json.loads((self.x.folder/'route-scout-history.json').read_text())[-1]
        self.assertEqual(result['status'],'incomplete_advisory')
        self.assertEqual(len(result['slots']),4)
        with patch.object(p,'call_stage',side_effect=AssertionError('duplicate')):
            self.assertEqual(asyncio.run(self.x.route_scouts())['status'],'already_assessed')

    def test_general_permission_does_not_bypass_promising_candidate_convergence(self):
        self.x.pilot.config['parallel_route_scouts']=fresh_config()
        self.x.current['route_scout_tasks']=self.portfolio(4)
        for task in self.x.current['route_scout_tasks']:task['purpose']='scientific_alternative'
        self.x.convergence_state={'phase':{'name':'converging','consumer_ids':['necessary-gap']},
                                  'candidates':{},'observations':{},'research_archive':{},'auxiliary_archive':{}}
        with patch.object(p,'call_stage',side_effect=AssertionError('unrelated exploration')):
            result=asyncio.run(self.x.route_scouts())
        self.assertFalse(result['convergence_admission']['allowed'])
        self.assertEqual(result['status'],'not_dispatched')

    def test_parallel_blind_distinct_actual_stages_and_implementer_census(self):
        async def scenario():
            entered=[];barrier=asyncio.Event();contexts=[]
            async def transport(host,name,prompt,model,timeout,resume,**kwargs):
                entered.append((name,prompt,model,resume));contexts.append(kwargs['accounting_context'])
                if len(entered)==2:barrier.set()
                await asyncio.wait_for(barrier.wait(),1)
                sid='scout-'+name.split('-')[-1]
                meta=self.f.meta(sid);meta.update(name=name,prompt_sha256=p.sha(prompt))
                return meta,{'representation':'PRIVATE-'+sid,'skeleton':[],'weakest_step':'unknown',
                    'kill_test':'proposed, not executed','viability':'unknown','remaining_obligations':['all']}
            with patch.object(p,'call_stage',side_effect=transport):
                result=await self.x.route_scouts()
                self.assertEqual(result['status'],'returned_advisory')
                self.assertEqual(len(entered),2)
                self.assertNotEqual(entered[0][0],entered[1][0])
                self.assertTrue(all(x[2:]==(p.ASTRA,None) for x in entered))
                self.assertTrue(all('PRIVATE-' not in x[1] for x in entered))
                self.assertEqual({c['purpose'] for c in contexts},{'route_scout'})
                self.assertEqual({c['phase'] for c in contexts},{'phase2'})
                for slot in result['slots']:
                    self.assertIn(slot['receipt']['session_id'],self.x.implementers)
                again=await self.x.route_scouts()
                self.assertEqual(again['status'],'already_assessed');self.assertEqual(len(entered),2)
                self.x.current['route_scout_tasks'][0]['task']='Cosmetic rewording'
                self.assertEqual((await self.x.route_scouts())['status'],'already_assessed')
                self.assertEqual(len(entered),2)
        asyncio.run(scenario())

    def test_user_request_cannot_make_admin_only_or_stale_selection_eligible(self):
        self.x.triage_history[0]['candidate_binding']='stale'
        # This synthetic stale receipt has no transport evidence: fail closed.
        with self.assertRaisesRegex(ValueError,'transport evidence'):
            asyncio.run(self.x.route_scouts())
        self.x.triage_history=[]
        self.x.current['ledger']['rows'][0]['triaged']=True
        self.assertEqual(asyncio.run(self.x.route_scouts())['status'],'not_dispatched')
        validate_tasks([])
        with self.assertRaises(ValueError):validate_tasks(self.x.tasks[:1])
        with self.assertRaises(ValueError):validate_tasks([self.x.tasks[0],self.x.tasks[0]])

    def test_failed_scout_actor_and_success_are_preserved_without_redispatch(self):
        async def transport(host,name,prompt,model,timeout,resume,**kwargs):
            meta=self.f.meta('actor-'+name)
            meta.update(name=name,status='process_failed' if name.endswith('1') else 'completed')
            return meta,{'partial':'all returned content'}
        with patch.object(p,'call_stage',side_effect=transport):
            with self.assertRaises(p.StageFailure):
                asyncio.run(self.x.route_scouts())
        result=json.loads((self.x.folder/'route-scout-history.json').read_text())[-1]
        self.assertEqual(result['status'],'incomplete_advisory')
        self.assertEqual(len([a for a in self.x.implementers if a.startswith('actor-')]),2)
        saved=json.loads((self.x.folder/'route-scout-history.json').read_text())
        self.assertEqual(saved[-1],result)
        with patch.object(p,'call_stage',side_effect=AssertionError('duplicate scout')):
            self.assertEqual(asyncio.run(self.x.route_scouts())['status'],'already_assessed')
