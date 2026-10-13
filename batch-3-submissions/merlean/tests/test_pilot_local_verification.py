import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_local_verification as m

class LocalModules(unittest.TestCase):
    def setUp(self):
        self.task={'kind':'lean','row_ids':['r'],'owned_scope':'local source','local_module':{'brief':'Check local uncertainty assuming H, no foundations','max_worker_calls':2,'max_probe_runs':2}}
        self.c={'hypotheses':['accepted H'],'ledger':{'rows':[{'id':'r','statement':'claim','uses':['h']},{'id':'h','statement':'H','uses':[]}]},'sol_tasks':[self.task]}
        self.r={'triage_decisions':[{'row_id':'r','selected':True,'verification_uncertainty':'high','local_check_reason':'material uncertainty','local_check':{k:'Independent substantive '+k for k in ('uncertainty','intended_objects','premise_boundary','feasibility','expected_value')}},{'row_id':'h','selected':False}],'approved_lean_tasks':[0],'local_module_task_links':[{'task_index':0,'prior_module_id':None,'relation':'new_claim','reason':'first claim'}]}
        self.modules=[]
    def approval(self):
        ds=m.check_review(self.c,self.r,self.modules)
        return {'receipt':{'name':'fresh-review'},'local_module_reassessments':ds,'local_module_links':{m.digest(self.task):copy.deepcopy(self.r['local_module_task_links'][0])}}
    def start(self):
        module,error=m.admit(self.modules,self.c,self.task,'binding',self.approval());self.assertIsNone(error);return module
    def disposition(self,module,action='still_required',row='r'):
        return {'module_id':module['module_id'],'module_evidence_sha256':m.digest(module),'action':action,'current_row_id':row,'reason':'independent analysis','evidence':'full evidence','basis':'current_argument','new_value':'different local interface'}
    def test_premise_content_not_only_id_bound(self):
        a=m.claim_basis(self.c,'r');self.c['ledger']['rows'][1]['statement']='changed H';b=m.claim_basis(self.c,'r')
        self.assertEqual(a[0],b[0]);self.assertNotEqual(a[1],b[1])
    def test_zero_local_checks_and_low_uncertainty(self):
        self.assertEqual(m.check_review(self.c,{'triage_decisions':[{'row_id':'r','selected':False}]},[]),[])
        self.r['triage_decisions'][0]['verification_uncertainty']='low'
        with self.assertRaises(ValueError):self.start()
    def test_exit_retains_complete_failed_code_without_permission(self):
        module=self.start();m.consume(module,'worker')
        output={'lean_probe':'untrusted code','local_module_result':{'module_id':module['module_id'],'outcome':'scope_expansion','scope_respected':False,'uncertainty_reduced':False,'evidence':'foundations would expand'}}
        self.assertFalse(m.worker_return(module,output,{'name':'p/sol','session_id':'sol'}))
        self.assertEqual(module['returns'][0]['output'],output);self.assertFalse(m.consume(module,'probe'))
        self.assertIn('unresolved',module['verification_status'])
    def test_disposition_coherence_retirement_and_cost_only(self):
        module=self.start();self.r['approved_lean_tasks']=[];self.r['local_module_task_links']=[]
        self.r['local_module_reassessments']=[self.disposition(module)]
        self.r['triage_decisions'][0]['selected']=False
        with self.assertRaises(ValueError):m.check_review(self.c,self.r,self.modules)
        d=self.disposition(module,'no_longer_required',None);self.r['local_module_reassessments']=[d]
        with self.assertRaises(ValueError):m.check_review(self.c,self.r,self.modules)
        d['current_row_id']='r';m.check_review(self.c,self.r,self.modules)
        d['basis']='cost_only'
        with self.assertRaises(ValueError):m.check_review(self.c,self.r,self.modules)
    def test_reentry_retains_history_no_budget_only_reset(self):
        module=self.start();m.consume(module,'worker');module['state']='returned_to_main'
        self.r['local_module_reassessments']=[self.disposition(module,'continue_local')]
        self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'],relation='same_claim')
        self.task['local_module']['max_worker_calls']=100
        _,error=m.admit(self.modules,self.c,self.task,'new-binding',self.approval());self.assertIn('budget',error)
        self.task['local_module']['brief']='New independently justified local interface'
        new,error=m.admit(self.modules,self.c,self.task,'new-binding',self.approval());self.assertIsNone(error)
        self.assertEqual(new['lineage_id'],module['lineage_id']);self.assertEqual(module['worker_calls'],1)
    def test_inline_plan_churn_does_not_renew_scientific_assessment(self):
        import codex_pilot as pilot
        before=pilot.assessment_key(self.c,[])
        binding=pilot.triage_binding(self.c)
        self.c['lean_probe_module']={'brief':'new label','max_worker_calls':99,'max_probe_runs':99}
        self.assertEqual(before,pilot.assessment_key(self.c,[]))
        self.assertEqual(binding,pilot.triage_binding(self.c))
    def test_progress_continues_with_remaining_counters_not_new_budget(self):
        module=self.start();m.consume(module,'worker');m.consume(module,'probe')
        output={'local_module_result':{'module_id':module['module_id'],'outcome':'local_evidence','scope_respected':True,'uncertainty_reduced':True,'evidence':'partial checked interface'}}
        self.assertTrue(m.worker_return(module,output,{'name':'first-sol'}));module['state']='returned_to_main'
        self.r['local_module_reassessments']=[self.disposition(module,'continue_local')]
        self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'],relation='same_claim')
        new,error=m.admit(self.modules,self.c,self.task,'binding',self.approval());self.assertIsNone(error)
        self.assertEqual((new['worker_calls'],new['probe_runs']),(1,1))
        self.assertTrue(m.consume(new,'worker'));self.assertFalse(m.consume(new,'worker'))
        self.assertEqual(module['worker_calls'],1)
    def test_unhashable_and_boolean_reviewer_tags_recover_as_valueerror(self):
        module=self.start()
        self.r['local_module_reassessments']=[self.disposition(module,'continue_local')]
        self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'],relation='same_claim')
        for section,key,value in [('local_module_reassessments','module_id',[]),('local_module_reassessments','current_row_id',{}),('local_module_reassessments','action',[]),('local_module_task_links','task_index',{}),('local_module_task_links','task_index',True),('local_module_task_links','prior_module_id',[])]:
            r=copy.deepcopy(self.r);r[section][0][key]=value
            with self.assertRaises(ValueError):m.check_review(self.c,r,self.modules)
    def test_malformed_worker_return_cannot_reopen_or_crash(self):
        for malformed in ([],None,'bad'):
            self.setUp();module=self.start()
            self.assertFalse(m.worker_return(module,{'local_module_result':malformed},{'name':'p/sol'}))
            self.r['local_module_reassessments']=[self.disposition(module,'continue_local')]
            self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'],relation='same_claim')
            new,error=m.admit(self.modules,self.c,self.task,'binding',self.approval())
            self.assertIsNone(new);self.assertIn('cannot reopen',error)
    def test_inline_remaining_allowance_requires_current_review_and_preserves_counters(self):
        self.task['lean_probe']='exact inline code'
        module=self.start();m.consume(module,'probe')
        module['returns'].append({'inline_or_worker_probe':{'status':'failed','stdout':'full compiler diagnostic'}})
        module['state']='returned_to_main'
        self.r['local_module_reassessments']=[self.disposition(module,'continue_local')]
        self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'],relation='same_claim')
        approval=self.approval()
        saved=copy.deepcopy(module['returns']);module['returns']=[]
        approval['local_module_reassessments'][0]['module_evidence_sha256']=m.digest(module)
        refused,error=m.admit(self.modules,self.c,self.task,'binding',approval);self.assertIsNone(refused)
        module['returns']=saved
        refused,error=m.admit(self.modules,self.c,self.task,'binding',approval);self.assertIsNone(refused) # stale exact evidence
        new,error=m.admit(self.modules,self.c,self.task,'binding',self.approval());self.assertIsNone(error)
        self.assertEqual(new['probe_runs'],1);self.assertEqual(new['worker_calls'],0)
        self.assertIn('unresolved',new['verification_status'])
    def test_closed_lineage_census_uses_latest_ids_and_explains_legacy_provenance(self):
        modules = [{'lineage_id':'claim-a', 'module_id':'claim-a-g1'},
                   {'lineage_id':'claim-a', 'module_id':'claim-a-g2'}]
        guidance = m.review_guidance(modules)
        census = guidance.split('(closed allowed non-null prior_module_id census):\n',1)[1].split('\n',1)[0]
        self.assertEqual(__import__('json').loads(census), ['claim-a-g2'])
        empty = m.review_guidance([])
        self.assertIn('census):\n[]\n', empty)
        self.assertIn('JSON null (not the string "null")', empty)
        self.assertIn('not mathematical novelty', empty)
        self.assertIn('Historical probe paths', empty)
        self.assertIn('may decline approval', empty)

    def test_unknown_and_stale_lineage_ids_stay_invalid_without_mutation(self):
        for parent in ('probes/legacy-worker-lean', 'null', [], False):
            review = copy.deepcopy(self.r)
            review['local_module_task_links'][0].update(prior_module_id=parent, relation='same_claim')
            before = copy.deepcopy(review)
            with self.subTest(parent=parent), self.assertRaisesRegex(ValueError, r'exact current module IDs=\[\]'):
                m.check_review(self.c, review, [])
            self.assertEqual(review, before)
        module = self.start()
        latest = copy.deepcopy(module); latest.update(module_id=module['lineage_id']+'-g2', generation=2)
        self.modules.append(latest)
        self.r['local_module_reassessments'] = [self.disposition(latest, 'continue_local')]
        self.r['local_module_task_links'][0].update(prior_module_id=module['module_id'], relation='same_claim')
        with self.assertRaisesRegex(ValueError, 'exact current module IDs=') as error:
            m.check_review(self.c, self.r, self.modules)
        self.assertIn(latest['module_id'], str(error.exception))

    def test_null_parent_cannot_reset_known_module_or_replace_independent_reason(self):
        self.r['local_module_task_links'][0]['reason'] = ''
        with self.assertRaisesRegex(ValueError, 'nonempty independent reason'):
            m.check_review(self.c, self.r, [])
        self.r['local_module_task_links'][0]['reason'] = 'First structured lineage; historical evidence assessed'
        module = self.start()
        self.r['local_module_reassessments'] = [self.disposition(module)]
        admitted, error = m.admit(self.modules, self.c, self.task, 'another-binding', self.approval())
        self.assertIsNone(admitted)
        self.assertIn('known claim cannot be renamed', error)
        self.assertEqual(len(self.modules), 1)

    def test_bad_approval_is_valueerror(self):
        for field,value in [('approved_lean_tasks',None),('approved_inline_lean','yes')]:
            r=copy.deepcopy(self.r);r[field]=value
            with self.assertRaises(ValueError):m.check_review(self.c,r,[])

class ModuleRuntimeTests(unittest.TestCase):
    def test_worker_scope_exit_retains_code_and_never_probes_it(self):
        import asyncio, tempfile
        from unittest.mock import AsyncMock
        from test_pilot_handoff_routing import RoutingTests
        import codex_pilot as p
        with tempfile.TemporaryDirectory() as root:
            fixture=RoutingTests();x=fixture.problem(root);x.ident='problem'
            task,_=fixture.authorized(x)
            task['local_module']={'brief':'Local claim only; accept H','max_worker_calls':2,'max_probe_runs':2}
            x.pilot.config['lite_local_verification_version']=1
            digest=p.sha(p.encoded(task))
            x.active_triage.update(approved_lean_task_hashes=[digest],local_module_reassessments=[],local_module_links={digest:{'prior_module_id':None,'relation':'new_claim'}})
            async def call(role,prompt,**kwargs):
                kwargs['on_admitted']()
                module=x.local_verification_modules[-1]
                return {'name':'problem/001-sol-execution','session_id':'sol','status':'completed'}, {'lean_probe':'must not run','local_module_result':{'module_id':module['module_id'],'outcome':'scope_expansion','scope_respected':False,'uncertainty_reduced':False,'evidence':'would widen accepted foundations'}}
            x.call=AsyncMock(side_effect=call)
            result=asyncio.run(x.execution())
            self.assertEqual(result['workers'][0]['probe']['status'],'not_requested')
            self.assertEqual(x.local_verification_modules[0]['worker_calls'],1)
            self.assertEqual(x.local_verification_modules[0]['returns'][0]['output']['lean_probe'],'must not run')
            self.assertEqual(x.probe.call_count,1) # only ordinary empty main probe path
            self.assertNotEqual(x.probe.call_args.args[0].get('lean_probe'),'must not run')
    def test_no_dispatch_module_rejection_does_not_renew_assessment(self):
        import asyncio,tempfile
        from unittest.mock import AsyncMock
        from test_pilot_handoff_routing import RoutingTests
        import codex_pilot as p
        with tempfile.TemporaryDirectory() as root:
            fixture=RoutingTests();x=fixture.problem(root);task,_=fixture.authorized(x)
            task['local_module']={'brief':'local only','max_worker_calls':1,'max_probe_runs':1}
            x.pilot.config['lite_local_verification_version']=1
            x.active_triage['approved_lean_task_hashes']=[p.sha(p.encoded(task))]
            x.active_triage['local_module_links']={} # no current independent lineage association
            x.call=AsyncMock()
            x.probe=AsyncMock(return_value={'status':'not_requested'})
            before=p.assessment_key(x.current,[])
            result=asyncio.run(x.execution())
            self.assertEqual(result['workers'][0]['output']['status'],'deferred')
            self.assertEqual(result['workers'][0]['output']['operational_status'],'returned_to_main')
            x.call.assert_not_called()
            self.assertEqual(before,p.assessment_key(x.current,[result]))
    def test_inline_code_cannot_use_worker_selection_without_module(self):
        import asyncio,tempfile
        from types import SimpleNamespace
        from test_pilot_handoff_routing import RoutingTests
        import codex_pilot as p
        with tempfile.TemporaryDirectory() as root:
            fixture=RoutingTests();x=fixture.problem(root);fixture.authorized(x)
            x.pilot.config['lite_local_verification_version']=1
            x.pilot.drain=SimpleNamespace(check=lambda:None)
            result=asyncio.run(p.Problem.probe(x,{'lean_probe':'unauthorized','lean_probe_rows':['r']},'inline'))
            self.assertEqual(result['lean']['status'],'deferred')
            self.assertEqual(result['status'],'not_requested')
            self.assertEqual(p.assessment_key(x.current,[]),p.assessment_key(x.current,[{'workers':[],'main_probe':result}]))
            actual={'workers':[],'main_probe':{'python':{'status':'passed','stdout':'actual result','source':'x','source_ref':{'path':'probes/one-python/source.py','sha256':p.sha('x')}},'lean':result['lean']}}
            self.assertNotEqual(p.assessment_key(x.current,[]),p.assessment_key(x.current,[actual]))
            self.assertFalse((Path(root)/'local-verification').exists())

if __name__=='__main__':unittest.main()
