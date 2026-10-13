import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
import pilot_execution_identity as identity
import test_pilot_continuation as native

class ExecutionIdentityTests(unittest.TestCase):
    def setUp(self):
        self.f=native.ContinuationTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.candidate={'proof_markdown':'Retained synthetic proof','ledger':{'rows':[]}}
        self.checkpoint={'effective_candidate_sha256':p.sha(p.encoded(self.candidate)),
            'raw_checkpoint':{'review_request':'substantive_reassessment'}}
        call=self.f.calls[1]
        source=(self.f.folder/'probes/main-3-lean/source.lean').read_text()
        result=json.loads((self.f.folder/'probes/main-3-lean/result.json').read_text())
        self.live=[{'workers':[{'task_id':call['session_id'],
            'execution_receipt':{k:call[k] for k in ('name','request_id','answer_sha256')},
            'output':{'status':'completed'},'probe':{'status':'not_requested'}}],
            'main_probe':{'lean':{**result,'source':source,
                'source_ref':{'path':'probes/main-3-lean/source.lean','sha256':p.sha(source)},
                'stdout_ref':{'path':'probes/main-3-lean/stdout.txt','sha256':p.sha('')}}}}]
    def keys(self,values):
        return p.assessment_key(self.candidate,values),p.checkpoint_request_key(self.checkpoint,values)
    def test_native_restore_preserves_worker_and_failed_probe_keys_twice(self):
        first=self.f.load()['problems']['problem']['execution_history']
        self.assertEqual(self.keys(self.live),self.keys(first))
        # A second native reconstruction of preserved evidence cannot renew keys.
        second=self.f.load()['problems']['problem']['execution_history']
        self.assertEqual(first,second);self.assertEqual(self.keys(first),self.keys(second))
        self.assertEqual(len(identity.atoms(first)),2)
    def test_two_native_successors_preserve_dispatch_keys_and_history(self):
        self.native_successors(self.live)

    def native_successors(self, live):
        import subprocess
        from unittest.mock import patch
        import pilot_continuation as loader
        config=json.loads((self.f.source/'host-config.json').read_text())
        config.update(codex_binary='synthetic',model_concurrency=1,internet_browse=False,
            original_scope_review_count=2,source_url='https://example.invalid/original')
        self.f.write(self.f.source/'host-config.json',config)
        current=self.f.source;receipt=self.f.receipt; expected=self.keys(live)
        for generation in range(2):
            target=self.f.base/('successor-'+str(generation))
            with patch.object(loader.os,'kill',side_effect=ProcessLookupError), \
                    patch.object(loader.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), \
                    patch.object(p,'subscription_preflight',return_value={}):
                p.prepare_continuation(current,target,receipt)
                restored=p.Problem(p.Pilot(target),'problem');restored.restore_checkpoint()
            self.assertEqual(expected,self.keys(restored.execution_history))
            self.assertEqual(restored.session,'main-session')
            state=json.loads((target/'campaign/state.json').read_text());state['sealed']=True
            self.f.write(target/'campaign/state.json',state)
            self.f.write(target/'pilot-result.json',{'end_utc':'2026-01-01T00:45:01Z','results':[{'problem':'problem','status':'partial'}]})
            rec=json.loads(receipt.read_text());rec['source_root']=str(target);rec['evidence']=[str(target/'pilot-result.json')]
            receipt=self.f.base/('reconciliation-'+str(generation)+'.json');self.f.write(receipt,rec)
            current=target

    def test_native_route_history_does_not_become_execution_or_renew_keys(self):
        output={'viability':'incomplete','remaining_obligations':['retained generic gap']}
        raw=json.dumps(output).encode()
        call={'name':'problem/005-route-scout-1','module':'route-scout-1','status':'completed',
            'session_id':'scout','request_id':'route-request','answer_sha256':p.sha(raw),'pid':900005}
        stage=self.f.source/'host/runtime'/call['name'];stage.mkdir(parents=True)
        (stage/'stage.answer.txt').write_bytes(raw);self.f.write(stage/'stage.meta.json',call)
        self.f.write(self.f.folder/'005-route-scout-1.json',output)
        rec=json.loads(self.f.receipt.read_text());rec['owned_pids'].append(900005);self.f.write(self.f.receipt,rec)
        live=self.live+[{'status':'returned_advisory','slots':[{'status':'returned','receipt':call,'output':output}]}]
        restored=self.f.load()['problems']['problem']['execution_history']
        self.assertEqual(self.keys(live),self.keys(restored))
        self.assertEqual(self.keys(self.live),self.keys(live))
        failed={'status':'incomplete_advisory','slots':[{'status':'interrupted_or_failed','receipt':{**call,'status':'process_failed'}}]}
        self.assertEqual(self.keys(live),self.keys(live+[failed]))
        self.native_successors(live)

    def test_group_order_duplicates_and_deferred_unavailability_do_not_renew(self):
        values=copy.deepcopy(self.live)
        values.append({'workers':[{'output':{'status':'deferred'}},{'output':{'status':'unavailable','stage':'failed'}}],
            'main_probe':{'lean':{'status':'deferred'},'status':'not_requested'}})
        self.assertEqual(self.keys(self.live),self.keys(values+self.live))
    def test_new_producer_same_output_and_changed_result_are_new_evidence(self):
        original=self.keys(self.live)
        changed=copy.deepcopy(self.live);changed[0]['workers'][0]['execution_receipt']['request_id']='different'
        self.assertNotEqual(original,self.keys(changed))
        changed=copy.deepcopy(self.live);changed[0]['main_probe']['lean']['stderr']='new actual failure'
        self.assertNotEqual(original,self.keys(changed))
        changed=copy.deepcopy(self.live);changed[0]['main_probe']['lean']['source_ref']['path']='probes/main-4-lean/source.lean'
        self.assertNotEqual(original,self.keys(changed))
    def test_conflicting_content_for_same_producer_is_not_new_evidence(self):
        changed=copy.deepcopy(self.live)
        changed[0]['workers'][0]['output']={'status':'completed','different':'forged'}
        with self.assertRaisesRegex(ValueError,'conflicting'):self.keys(self.live+changed)
        changed=copy.deepcopy(self.live);changed[0]['main_probe']['lean']['stderr']='conflicting'
        with self.assertRaisesRegex(ValueError,'conflicting'):self.keys(self.live+changed)

    def test_missing_producer_or_tampered_source_fails_closed(self):
        for kind in ['worker','source','path']:
            changed=copy.deepcopy(self.live)
            if kind=='worker':changed[0]['workers'][0].pop('execution_receipt')
            if kind=='source':changed[0]['main_probe']['lean']['source']='changed'
            if kind=='path':changed[0]['main_probe']['lean']['source_ref']['path']='../escape/source.lean'
            with self.subTest(kind=kind),self.assertRaises(ValueError):self.keys(changed)
    def test_native_changed_result_changes_key_and_source_tamper_detected(self):
        before=self.keys(self.f.load()['problems']['problem']['execution_history'])
        self.f.write(self.f.folder/'probes/main-3-lean/result.json',{'status':'failed','stderr':'different'})
        restored=self.f.load()['problems']['problem']['execution_history']
        self.assertNotEqual(before,self.keys(restored))
        restored[-1]['artifacts']['probes/main-3-lean/source.lean']['text']='tampered'
        with self.assertRaisesRegex(ValueError,'source changed'):self.keys(restored)
    def test_legacy_checkpoint_without_assessment_cannot_renew_request(self):
        import asyncio
        import test_pilot_checkpoint_scope_contract as fixtures
        f=fixtures.MainCheckpointRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        f.raw['review_request']='substantive_reassessment'
        old={'raw_checkpoint':copy.deepcopy(f.raw),'effective_candidate_sha256':p.sha(p.encoded(f.x.current)),
            'request_key':'historical-key','actionable':True}
        path=f.x.folder/'main-1-checkpoint.json';p.write(path,old)
        async def call(*args,**kwargs):return f.f.meta('main'),copy.deepcopy(f.raw)
        f.x.call=call
        with self.assertRaisesRegex(ValueError,'legacy checkpoint'):asyncio.run(f.x.main_turn('Continue'))
        self.assertEqual(json.loads(path.read_text()),old)

    def test_legacy_same_candidate_admission_fails_closed(self):
        from types import SimpleNamespace
        x=object.__new__(p.Problem);x.pilot=SimpleNamespace(config={'continuation_checkpoint':{}},host=self.f.source/'host')
        x.pilot.config['continuation_checkpoint']={'path':'bound'}
        x.current=self.candidate;x.calls=[];x.folder=self.f.folder
        record={'candidate_sha256':p.sha(p.encoded(self.candidate)),'binding_key':'legacy','attempts':3}
        x.final_assessment_history=[record]
        with self.assertRaisesRegex(ValueError,'legacy assessment'):x.guard_legacy_execution_identity()
        self.assertEqual(record['binding_key'],'legacy');self.assertEqual(record['attempts'],3)
        record['execution_identity_version']=2;x.guard_legacy_execution_identity()

if __name__=='__main__':unittest.main()
