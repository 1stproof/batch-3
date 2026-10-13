"""Synthetic host boundary tests; no model, compiler, or research dispatch."""
import asyncio
import copy
import json
import sys
import tempfile
import unittest
from contextlib import nullcontext
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p
import pilot_local_verification as m
import test_pilot_handoff_routing as routing_fixture
import test_pilot_local_verification as module_fixture


class CompileCycle(unittest.TestCase):
    def fixture(self, root, reports, diagnostics, mutate=None, workers=3, probes=3):
        f = routing_fixture.RoutingTests(); x = f.problem(root); x.ident = 'synthetic'
        task, _ = f.authorized(x)
        task['local_module'] = {'brief':'One unchanged synthetic interface',
            'max_worker_calls':workers, 'max_probe_runs':probes}
        x.pilot.config.update(lite_local_verification_version=1,
                             lean_executable='synthetic-lean', lean_library_paths=[])
        x.pilot.root = Path(root); x.pilot.drain_probes = {}
        x.pilot.remaining = lambda: 1000
        x.pilot.drain = SimpleNamespace(check=lambda:None, admission=lambda *args:nullcontext())
        digest = m.digest(task)
        x.active_triage.update(approved_lean_task_hashes=[digest],local_module_reassessments=[],
            local_module_links={digest:{'prior_module_id':None,'relation':'new_claim'}})
        x.probe = p.Problem.probe.__get__(x)
        seen = []
        async def call(role, prompt, **kwargs):
            kwargs['on_admitted'](); x.counter += 1
            module = x.local_verification_modules[-1]
            data = copy.deepcopy(reports[len(seen)])
            report = data.setdefault('local_module_result', {})
            report.setdefault('module_id', module['module_id'])
            seen.append(prompt)
            if mutate: mutate(x, task, len(seen))
            return {'name':f'synthetic/{x.counter}-sol-execution', 'session_id':f'worker-{x.counter}',
                    'status':'completed'}, data
        x.call = AsyncMock(side_effect=call)
        process = SimpleNamespace(returncode=0)
        process.communicate = AsyncMock(side_effect=[(json.dumps(d).encode(),b'') for d in diagnostics])
        return x, task, seen, process

    def pending(self, source='source one', complete=True, **overrides):
        result = {'lean_probe':source, 'lean_probe_rows':['r'], 'python_probe':'',
            'local_module_result':{'outcome':'compile_pending','scope_respected':True,
                'uncertainty_reduced':False, 'evidence':'Source needs a real diagnostic',
                'implementation_complete':complete,'next_step':'Check source then repair exact diagnostics'}}
        result['local_module_result'].update(overrides)
        return result

    def run_cycle(self, root, reports, diagnostics, **kwargs):
        x, task, seen, process = self.fixture(root,reports,diagnostics,**kwargs)
        with patch('asyncio.create_subprocess_exec', AsyncMock(return_value=process)) as launch:
            result=asyncio.run(x.execution())
        return x, result, seen, process, launch

    def test_first_diagnostic_then_repair_same_module_original_counters(self):
        with tempfile.TemporaryDirectory() as root:
            reports=[self.pending(),self.pending('source two')]
            diagnostics=[{'status':'failed','exit_code':1,'stdout':'exact type error'},
                         {'status':'completed','exit_code':0,'stdout':'clean axiom report'}]
            x,result,seen,process,launch=self.run_cycle(root,reports,diagnostics)
            module=x.local_verification_modules[0]
            self.assertEqual(len(x.local_verification_modules),1)
            self.assertEqual((module['worker_calls'],module['probe_runs']),(2,2))
            self.assertEqual(module['state'],'returned_to_main')
            self.assertIn('exact type error', seen[1])
            self.assertIn('source one', seen[1])
            self.assertIn('no session continuity is claimed', seen[1])
            self.assertEqual(launch.await_count,2)
            self.assertEqual(len(list((Path(root)/module['artifact_root']/'probes').glob('*/result.json'))),2)
            self.assertEqual(len(result['workers']),2)
            self.assertIn('unresolved',module['verification_status'])
            self.assertNotIn('grade',module)

    def test_compiled_partial_can_finish_but_full_clean_stops(self):
        with tempfile.TemporaryDirectory() as root:
            x,_,seen,_,launch=self.run_cycle(root,[self.pending(complete=False),self.pending('complete source')],
                [{'status':'completed','exit_code':0,'stdout':'partial'},
                 {'status':'completed','exit_code':0,'stdout':'complete'}])
            self.assertEqual(len(seen),2);self.assertEqual(launch.await_count,2)
            self.assertEqual(x.local_verification_modules[0]['worker_calls'],2)

    def test_terminal_historical_or_adverse_report_never_runs_source(self):
        for outcome in ('returned_to_main','scope_expansion','encoding_infeasible',
                        'mathematical_counterissue','no_uncertainty_reduction'):
            with self.subTest(outcome=outcome), tempfile.TemporaryDirectory() as root:
                x,result,_,_,launch=self.run_cycle(root,[self.pending(outcome=outcome)],[])
                launch.assert_not_called()
                self.assertEqual(x.local_verification_modules[0]['probe_runs'],0)
                self.assertEqual(result['workers'][0]['probe']['status'],'not_requested')
                self.assertEqual(x.local_verification_modules[0]['returns'][0]['output']['lean_probe'],'source one')

    def test_malformed_pending_and_hidden_extra_work_never_probe(self):
        variants=[]
        for field in ('implementation_complete','next_step','scope_respected'):
            data=self.pending();data['local_module_result'].pop(field);variants.append(data)
        data=self.pending();data['lean_probe_rows']=['r','extra'];variants.append(data)
        data=self.pending();data['python_probe']='unauthorized python';variants.append(data)
        data=self.pending();data['lean_probe']='';variants.append(data)
        data=self.pending();data['local_module_result']=[];variants.append(data)
        for data in variants:
            with self.subTest(data=data), tempfile.TemporaryDirectory() as root:
                # malformed report stays malformed in this fixture
                if isinstance(data['local_module_result'],list):
                    module={'module_id':'m','row_id':'r','state':'working','returns':[],'stages':[]}
                    self.assertFalse(m.worker_return(module,data,{}));continue
                x,_,_,_,launch=self.run_cycle(root,[data],[])
                launch.assert_not_called();self.assertEqual(x.local_verification_modules[0]['probe_runs'],0)

    def test_changed_binding_after_worker_prevents_compilation(self):
        def mutate(which):
            def change(x,task,count):
                if which=='candidate':x.current['proof_markdown']+=' altered'
                elif which=='task':task['task']+=' altered'
                elif which=='premise':x.current['assumptions']=['new premise']
                elif which=='scope':task['owned_scope']='expanded'
                elif which=='budget':task['local_module']['max_probe_runs']+=1
                elif which=='approval':x.active_triage['receipt']['answer_sha256']='different approval'
                elif which=='object':x.current['ledger']['rows'][0]['intended_objects']='different object'
            return change
        for which in ('candidate','task','premise','scope','budget','approval','object'):
            with self.subTest(which=which), tempfile.TemporaryDirectory() as root:
                x,_,_,_,launch=self.run_cycle(root,[self.pending()],[],mutate=mutate(which))
                launch.assert_not_called();self.assertEqual(x.local_verification_modules[0]['probe_runs'],0)
                self.assertEqual(x.local_verification_modules[0]['state'],'returned_to_main')
                self.assertEqual(x.local_verification_modules[0]['submitted_source_sha256'],[])

    def test_budget_exhaustion_never_dispatches_an_extra_worker(self):
        for workers,probes in ((1,3),(3,1)):
            with self.subTest(workers=workers,probes=probes), tempfile.TemporaryDirectory() as root:
                x,_,seen,_,launch=self.run_cycle(root,[self.pending()],
                    [{'status':'failed','exit_code':1,'stdout':'real failure'}],workers=workers,probes=probes)
                self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)
                self.assertEqual((x.local_verification_modules[0]['worker_calls'],x.local_verification_modules[0]['probe_runs']),(1,1))

    def test_identical_source_no_new_probe_and_unavailable_no_retry(self):
        with tempfile.TemporaryDirectory() as root:
            x,_,seen,_,launch=self.run_cycle(root,[self.pending(),self.pending()],
                [{'status':'failed','exit_code':1,'stdout':'failure'}])
            self.assertEqual(len(seen),2);self.assertEqual(launch.await_count,1)
            self.assertEqual(x.local_verification_modules[0]['probe_runs'],1)
        with tempfile.TemporaryDirectory() as root:
            x,_,seen,_,launch=self.run_cycle(root,[self.pending()],
                [{'status':'unavailable','error':'missing compiler'}])
            self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)

    def test_no_actual_diagnostic_does_not_continue(self):
        for diagnostic in ({'status':'not_requested'}, {'status':'completed','stdout':'no exit evidence'}):
            with self.subTest(diagnostic=diagnostic), tempfile.TemporaryDirectory() as root:
                x,_,seen,_,launch=self.run_cycle(root,[self.pending(complete=False)],[diagnostic])
                self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)
                self.assertEqual(x.local_verification_modules[0]['state'],'returned_to_main')

    def test_changed_approval_after_probe_blocks_next_worker(self):
        with tempfile.TemporaryDirectory() as root:
            x,task,seen,process=self.fixture(root,[self.pending(complete=False)],[])
            async def communicate(request):
                x.active_triage['receipt']['answer_sha256']='changed-after-compiler'
                return json.dumps({'status':'failed','exit_code':1,'stdout':'diagnostic'}).encode(), b''
            process.communicate=AsyncMock(side_effect=communicate)
            with patch('asyncio.create_subprocess_exec',AsyncMock(return_value=process)) as launch:
                result=asyncio.run(x.execution())
            self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)
            self.assertEqual(x.local_verification_modules[0]['worker_calls'],1)
            self.assertEqual(result['workers'][-1]['output']['status'],'deferred')

    def test_drain_between_repairs_preserves_evidence_without_consuming_new_budget(self):
        with tempfile.TemporaryDirectory() as root:
            x,task,seen,process=self.fixture(root,[self.pending(complete=False)],
                [{'status':'failed','exit_code':1,'stdout':'failure retained before drain'}])
            checks=[]
            def check():
                checks.append(True)
                if len(checks)>1:raise RuntimeError('synthetic cooperative drain')
            x.pilot.drain.check=check
            with patch('asyncio.create_subprocess_exec',AsyncMock(return_value=process)) as launch:
                with self.assertRaisesRegex(RuntimeError,'cooperative drain'):asyncio.run(x.execution())
            module=x.local_verification_modules[0]
            self.assertEqual((module['worker_calls'],module['probe_runs']),(1,1))
            self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)
            saved=json.loads((Path(root)/module['artifact_root']/'module.json').read_text())
            self.assertIn('failure retained before drain',json.dumps(saved))
            self.assertIn('source one',json.dumps(saved))

    def test_generic_local_evidence_does_not_authorize_another_attempt(self):
        with tempfile.TemporaryDirectory() as root:
            x,_,seen,_,launch=self.run_cycle(root,[self.pending(outcome='local_evidence',uncertainty_reduced=True)],
                [{'status':'failed','exit_code':1,'stdout':'failure'}])
            self.assertEqual(len(seen),1);self.assertEqual(launch.await_count,1)


class SelectionAndHistory(unittest.TestCase):
    def test_each_selection_value_field_required_but_zero_is_valid(self):
        for key in ('uncertainty','intended_objects','premise_boundary','feasibility','expected_value'):
            f=module_fixture.LocalModules();f.setUp();f.r['triage_decisions'][0]['local_check'].pop(key)
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'selected local check'):f.start()
        f=module_fixture.LocalModules();f.setUp()
        self.assertEqual(m.check_review(f.c,{'triage_decisions':[{'row_id':'r','selected':False}]},[]),[])

    def test_replacement_inherits_consumed_totals_without_history_mutation(self):
        f=module_fixture.LocalModules();f.setUp();old=f.start();m.consume(old,'worker');m.consume(old,'probe')
        old['state']='returned_to_main';before=copy.deepcopy(old)
        f.r['local_module_reassessments']=[f.disposition(old,'replace')]
        f.r['local_module_task_links'][0].update(prior_module_id=old['module_id'],relation='same_claim')
        f.task['local_module']['brief']='Independently reviewed changed representation'
        new,error=m.admit(f.modules,f.c,f.task,'new-binding',f.approval())
        self.assertIsNone(error);self.assertEqual(old,before)
        self.assertEqual((new['worker_calls'],new['probe_runs']),(1,1))
        self.assertEqual(new['inherited_counters_from'],old['module_id'])
        self.assertEqual(new['limits'],old['limits'])

    def test_three_generations_and_legacy_reset_segments_are_not_double_counted(self):
        records = [
            {'module_id':'a-g1','lineage_id':'a','worker_calls':2,'probe_runs':3,'inherited_counters_from':None},
            {'module_id':'a-g2','lineage_id':'a','worker_calls':1,'probe_runs':1,'inherited_counters_from':None},
            {'module_id':'a-g3','lineage_id':'a','worker_calls':2,'probe_runs':2,'inherited_counters_from':'a-g2'},
        ]
        before=copy.deepcopy(records)
        self.assertEqual(m.lineage_counters(records,records[-1]),{'worker_calls':4,'probe_runs':5})
        records.append({'module_id':'a-g4','lineage_id':'a','worker_calls':5,'probe_runs':6,
                        'inherited_counters_from':'a-g3','counter_semantics':'lineage_total'})
        records.append({'module_id':'a-g5','lineage_id':'a','worker_calls':6,'probe_runs':7,
                        'inherited_counters_from':'a-g4','counter_semantics':'lineage_total'})
        self.assertEqual(m.lineage_counters(records,records[-1]),{'worker_calls':6,'probe_runs':7})
        self.assertEqual(records[:3],before)
        records[-1]['worker_calls']=1
        with self.assertRaisesRegex(ValueError,'regressed'):m.lineage_counters(records,records[-1])

    def test_legacy_reset_history_is_charged_on_reassessment_not_erased(self):
        f=module_fixture.LocalModules();f.setUp();first=f.start()
        first.pop('counter_semantics');first['worker_calls']=1;first['probe_runs']=1
        first['state']='returned_to_main'
        second=copy.deepcopy(first);second.update(module_id=first['lineage_id']+'-g2',generation=2,
            parent_module_id=first['module_id'],inherited_counters_from=None)
        f.modules.append(second);before=copy.deepcopy(f.modules)
        f.r['local_module_reassessments']=[f.disposition(second,'replace')]
        f.r['local_module_task_links'][0].update(prior_module_id=second['module_id'],relation='same_claim')
        f.task['local_module']['brief']='Independent changed representation'
        new,error=m.admit(f.modules,f.c,f.task,'new-binding',f.approval())
        self.assertIsNone(error);self.assertEqual(f.modules[:2],before)
        self.assertEqual((new['worker_calls'],new['probe_runs']),(2,2))
        self.assertFalse(m.consume(new,'worker'))
        self.assertFalse(m.consume(new,'probe'))

    def test_working_legacy_reset_cannot_bypass_accounting_reassessment(self):
        f=module_fixture.LocalModules();f.setUp();first=f.start()
        first.pop('counter_semantics');first['worker_calls']=1;first['probe_runs']=1
        first['state']='returned_to_main'
        second=copy.deepcopy(first);second.update(module_id=first['lineage_id']+'-g2',generation=2,
            parent_module_id=first['module_id'],inherited_counters_from=None,state='working')
        f.modules.append(second);before=copy.deepcopy(f.modules)
        approval={'receipt':copy.deepcopy(second['approval_receipt']),
                  'local_module_links':{m.digest(f.task):{'prior_module_id':second['module_id'],'relation':'same_claim'}},
                  'local_module_reassessments':[]}
        module,error=m.admit(f.modules,f.c,f.task,'binding',approval)
        self.assertIsNone(module);self.assertIn('retriage',error);self.assertEqual(f.modules,before)
        with self.assertRaisesRegex(m.ModuleBoundary,'accounting reassessment'):
            m.execution_binding(second,f.c,f.task,'binding',approval,modules=f.modules)

if __name__=='__main__':unittest.main()
