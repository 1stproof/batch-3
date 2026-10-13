import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
import pilot_assessment_handoff as h
import pilot_operational_handoff as old
import test_pilot_operational_handoff as fixture
import test_pilot_continuation as native

class AssessmentHandoffTests(unittest.TestCase):
    def setUp(self):
        self.f=fixture.OperationalHandoffTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.x=self.f.problem;self.x.current['sol_tasks']=[];self.x.execution_history=[];self.x.implementers=['original']
        self.candidate=p.sha(p.encoded(self.x.current))
        stage=self.f.root/'host/runtime/example/002-proof-review';stage.mkdir()
        raw={'verdict':'INCOMPLETE','candidate_sha256':self.candidate,'mathematically_ready':True,
            'gaps':[],'unresolved_findings':[{'id':'pending','severity':'gap','kind':'host_gate'}]}
        payload=json.dumps(raw).encode();prompt=b'Exact independent review';cap=b'{}'
        for name,data in [('stage.answer.txt',payload),('stage.prompt.txt',prompt),('document-capability.json',cap)]:
            (stage/name).write_bytes(data)
        self.review={'name':'example/002-proof-review','module':'proof-review','request_id':'review-request',
            'status':'completed','session_id':'reviewer','model_actual':'gpt-6-astra','model_verified':True,
            'fresh_session':True,'resume_session':None,'prompt_sha256':p.sha(prompt),'answer_sha256':p.sha(payload),
            'end_utc':'2026-01-01T00:20:00+00:00','document_audit':{'required_material_delivered':True},
            'document_capability':{'path':str(stage/'document-capability.json'),'sha256':p.sha(cap)}}
        (stage/'stage.meta.json').write_text(json.dumps(self.review))
        self.x.calls=[self.review]
        receipt={k:self.review.get(k) for k in ('name','status','session_id','model_actual','model_verified',
            'fresh_session','resume_session','prompt_sha256','answer_sha256','request_id')}
        receipt['reviewed_candidate_sha256']=self.candidate
        self.x.final_assessment_history=[{'binding_key':p.assessment_key(self.x.current,[]),
            'execution_identity_version':2,'candidate_sha256':self.candidate,'status':'reviewed','attempts':1,
            'proof_receipt':receipt}]
        self.raw={'response_type':h.KIND,'selected_candidate_sha256':self.candidate,
            'assessment_ids':h.capability(self.x)['assessment_ids'],'reason':'Need operational diagnosis; all findings remain.',
            'no_new_scientific_work':True}
        self.write_main(self.raw)
    def write_main(self,raw,**changes):
        self.f.write_stage(raw,**changes);self.x.calls=[self.review,self.f.meta]
    def test_explicit_handoff_preserves_negative_verdict_and_no_renewal(self):
        before=copy.deepcopy((self.x.current,self.x.findings,self.x.final_assessment_history))
        with self.assertRaises(old.OperationalHandoff):p.Problem.apply_authored_response(self.x,self.raw,{})
        receipt=json.loads((self.x.folder/h.FILE).read_text())
        self.assertFalse(receipt['automatic_resume_authorized']);self.assertFalse(receipt['acceptance_authority'])
        self.assertEqual(before,(self.x.current,self.x.findings,self.x.final_assessment_history))
        self.assertFalse(p.proof_pass({'verdict':'INCOMPLETE','mathematically_ready':True,'gaps':[]}))
        with self.assertRaises(old.OperationalHandoff):h.guard(self.x)
    def test_crash_after_answer_before_receipt_is_reconciled(self):
        self.assertFalse((self.x.folder/h.FILE).exists())
        with self.assertRaises(old.OperationalHandoff):h.guard(self.x)
        self.assertTrue((self.x.folder/h.FILE).is_file())
    def test_forged_ids_boolean_or_changed_candidate_cannot_handoff(self):
        for change in [{'assessment_ids':['a'*64]},{'no_new_scientific_work':1},{'selected_candidate_sha256':'b'*64}]:
            raw={**self.raw,**change};self.write_main(raw)
            with self.subTest(change=change),self.assertRaises(ValueError):h.commit(self.x,raw,self.f.meta)
        self.write_main(self.raw);self.x.current['proof_markdown']='new substantive proof'
        self.assertFalse(h.capability(self.x)['eligible'])
    def test_changed_execution_and_incomplete_delivery_remove_capability(self):
        self.x.execution_history=[{'main_probe':{'python':{'status':'failed','source':'x',
            'source_ref':{'path':'probes/new-python/source.py','sha256':p.sha('x')}}}}]
        self.assertFalse(h.capability(self.x)['eligible'])
        self.x.execution_history=[];self.review['document_audit']['required_material_delivered']=False
        self.assertFalse(h.capability(self.x)['eligible'])
    def test_tampered_review_or_later_calls_fail_closed(self):
        stage=Path(self.review['document_capability']['path']).parent
        (stage/'stage.answer.txt').write_text('{}')
        with self.assertRaisesRegex(ValueError,'answer changed'):h.capability(self.x)
    def test_no_automatic_handoff_from_ordinary_checkpoint(self):
        self.write_main({'response_type':'blocked_checkpoint'})
        h.guard(self.x)
        self.assertFalse((self.x.folder/h.FILE).exists())
    def test_main_turn_invalid_handoff_uses_existing_single_structural_correction(self):
        import asyncio
        import test_pilot_checkpoint_scope_contract as checkpoints
        f=checkpoints.MainCheckpointRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        x=f.x;x.folder=self.x.folder;x.session='original';x.calls=[];x.counter=2
        self.f.problem=x
        responses=iter([{'response_type':h.KIND},copy.deepcopy(f.raw)]);instructions=[]
        async def call(role,instruction,**kwargs):
            h.guard(x)  # Real pre-dispatch crash-gap guard, including correction.
            x.counter+=1;instructions.append(instruction)
            raw=next(responses);self.f.write_stage(raw)
            return self.f.meta,raw
        x.call=call
        asyncio.run(x.main_turn('Continue the exact original task'))
        self.assertEqual(len(instructions),2)
        rejected=json.loads((x.folder/'main-3-invalid-contract.json').read_text())
        self.assertEqual(rejected['raw_response'],{'response_type':h.KIND})
        self.assertFalse((x.folder/h.FILE).exists())

    def test_native_restore_retains_rejected_handoff_then_valid_correction(self):
        f=native.ContinuationTests();f.setUp();self.addCleanup(f.doCleanups)
        invalid={'response_type':h.KIND}
        first=f.calls[3];first['status']='completed'
        data=json.dumps(invalid).encode();first['answer_sha256']=p.sha(data)
        stage=f.source/'host/runtime'/first['name'];(stage/'stage.answer.txt').write_bytes(data)
        f.write(stage/'stage.meta.json',first);f.write(f.folder/'004-main-repair.json',invalid)
        f.write(f.folder/'main-4-invalid-contract.json',{'raw_response':invalid,'error':'invalid fields'})
        corrected=json.loads((f.folder/'current-candidate.json').read_text());data=json.dumps(corrected).encode()
        second={**first,'name':'problem/005-main-repair','request_id':'corrected','answer_sha256':p.sha(data),'pid':900005}
        stage=f.source/'host/runtime'/second['name'];stage.mkdir(parents=True)
        (stage/'stage.answer.txt').write_bytes(data);f.write(stage/'stage.meta.json',second)
        f.write(f.folder/'005-main-repair.json',corrected)
        rec=json.loads(f.receipt.read_text());rec['owned_pids'].append(900005);f.write(f.receipt,rec)
        result=f.load()['problems']['problem']
        self.assertEqual(result['current'],corrected)
        self.assertEqual(result['calls'][-1]['name'],second['name'])
        self.assertEqual(json.loads((f.folder/'004-main-repair.json').read_text()),invalid)

    def test_native_continuation_rejects_crash_gap_handoff(self):
        f=native.ContinuationTests();f.setUp();self.addCleanup(f.doCleanups)
        stage=f.source/'host/runtime'/f.calls[0]['name'];data=json.dumps({'response_type':h.KIND}).encode()
        (stage/'stage.answer.txt').write_bytes(data);f.calls[0]['answer_sha256']=p.sha(data)
        f.write(stage/'stage.meta.json',f.calls[0])
        with self.assertRaisesRegex(ValueError,'assessment handoff response'):f.load()

if __name__=='__main__':unittest.main()
