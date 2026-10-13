"""Prospective shape disclosure, with strict unchanged execution authority."""
import copy
import json
import tempfile
import unittest
import test_pilot_local_compile_cycle as cycle
import pilot_local_verification as m

class ContractTests(unittest.TestCase):
    def module(self):
        return {'module_id':'m','row_id':'r','state':'working','returns':[],'stages':[]}
    def pending(self):
        data=cycle.CompileCycle().pending();data['local_module_result']['module_id']='m';return data
    def test_example_is_parseable_and_nested(self):
        example=json.loads(m.WORKER_GUIDANCE.split('Shape example only; replace every placeholder with the actual approved binding and source:\n')[1])
        self.assertEqual(example,m.COMPILE_PENDING_EXAMPLE)
        self.assertIn('implementation_complete',example['local_module_result'])
        self.assertNotIn('implementation_complete',example)
        self.assertIn('lean_probe',example)
    def test_root_only_is_retained_rejected_with_precise_diagnostics(self):
        data=self.pending()
        for key in ('implementation_complete','next_step'):data[key]=data['local_module_result'].pop(key)
        before=copy.deepcopy(data);module=self.module()
        self.assertFalse(m.worker_return(module,data,{'name':'worker'}))
        self.assertEqual(data,before);self.assertEqual(module['returns'][0]['output'],before)
        self.assertEqual(module['state'],'returned_to_main')
        self.assertEqual(module['returns'][0]['contract_diagnostics'],[
            'local_module_result.implementation_complete is required; root-level implementation_complete does not satisfy this nested field',
            'local_module_result.next_step is required; root-level next_step does not satisfy this nested field'])
    def test_type_missing_and_empty_diagnostics_do_not_admit(self):
        for field,value in [('implementation_complete',0),('implementation_complete','false'),('next_step',[]),('next_step',' ')]:
            data=self.pending();data['local_module_result'][field]=value;module=self.module()
            self.assertFalse(m.worker_return(module,data,{}));self.assertTrue(module['returns'][0]['contract_diagnostics'])
        data=self.pending();data['lean_probe']='';module=self.module()
        self.assertFalse(m.worker_return(module,data,{}))
        self.assertIn('root lean_probe must be a nonempty source string',module['returns'][0]['contract_diagnostics'])
    def test_valid_nested_extra_root_fields_do_not_change_predicate(self):
        data=self.pending();data.update(implementation_complete='ignored root value',next_step=[])
        module=self.module();self.assertTrue(m.worker_return(module,data,{}))
        self.assertNotIn('contract_diagnostics',module['returns'][0])
    def test_wrong_level_never_compiles_corrected_prospective_shape_runs_once(self):
        fixture=cycle.CompileCycle();bad=fixture.pending()
        for field in ('implementation_complete','next_step'):bad[field]=bad['local_module_result'].pop(field)
        with tempfile.TemporaryDirectory() as tmp:
            p,_,_,_,launch=fixture.run_cycle(tmp,[bad],[])
            launch.assert_not_called();module=p.local_verification_modules[0]
            self.assertEqual((module['worker_calls'],module['probe_runs']),(1,0))
            self.assertEqual(len(module['returns'][0]['contract_diagnostics']),2)
        with tempfile.TemporaryDirectory() as tmp:
            p,_,_,_,launch=fixture.run_cycle(tmp,[fixture.pending()], [{'status':'completed','exit_code':0,'stdout':'synthetic diagnostic'}])
            self.assertEqual(launch.await_count,1)
            self.assertEqual((p.local_verification_modules[0]['worker_calls'],p.local_verification_modules[0]['probe_runs']),(1,1))
            self.assertNotIn('grade',p.local_verification_modules[0])

    def test_additive_diagnostics_survive_strict_registry_restore(self):
        from pilot_continuation import _local_module_registry
        fixture=cycle.CompileCycle();bad=fixture.pending()
        for key in ('implementation_complete','next_step'):bad[key]=bad['local_module_result'].pop(key)
        with tempfile.TemporaryDirectory() as tmp:
            p,_,_,_,launch=fixture.run_cycle(tmp,[bad],[])
            before=copy.deepcopy(p.local_verification_modules)
            restored=_local_module_registry(p.folder,{'local_verification_modules':before})
            self.assertEqual(restored,before)
            self.assertEqual(restored[0]['returns'][0]['output']['implementation_complete'],True)
            self.assertEqual(len(restored[0]['returns'][0]['contract_diagnostics']),2)
            self.assertEqual((restored[0]['worker_calls'],restored[0]['probe_runs']),(1,0))
            launch.assert_not_called()

if __name__=='__main__':unittest.main()
