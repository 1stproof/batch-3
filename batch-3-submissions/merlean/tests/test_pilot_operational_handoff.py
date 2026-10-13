import asyncio
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch, AsyncMock
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_operational_handoff as h
import pilot_review_exhaustion as e
import codex_pilot as pilot
from pilot_candidate_contract import candidate_hash


class OperationalHandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.folder=self.root/'problem';self.folder.mkdir()
        self.stage=self.root/'host/runtime/example/003-main-repair';self.stage.mkdir(parents=True)
        self.candidate={'proof_markdown':'A retained proof.', 'answer_statement':'Claim', 'ledger':{'rows':[{'id':'x','claim':'Claim'}]},'sol_tasks':[{'retained':'not silently withdrawn'}]}
        self.document={'revision':'r1','manifest_sha256':'a'*64,'proof_sha256':hashlib.sha256(self.candidate['proof_markdown'].encode()).hexdigest(),'status':'submitted','proof_markdown':self.candidate['proof_markdown']}
        self.record={'id':'b'*64,'binding':{'scientific':e.projection(self.candidate)},'required_material_delivered':True,'end_utc':'2026-01-01T00:20:00+00:00'}
        self.raw={'response_type':h.KIND,'selected_candidate_sha256':candidate_hash(self.candidate),'exhaustion_ids':['b'*64],'reason':'Required independent review is unavailable; no new work proposed.','no_new_scientific_work':True}
        self.problem=SimpleNamespace(folder=self.folder,current=copy.deepcopy(self.candidate),session='original',calls=[],findings=[{'retained':'gap'}],execution_history=[{'retained':'failed'}],route_scout_history=[],local_verification_modules=[],active_stages=set(),counter=3,review_exhaustions=[self.record],documents_enabled=lambda:True,document_current=lambda:copy.deepcopy(self.document))
        self.write_stage(self.raw)
        self.sync=patch.object(e,'synchronize',return_value=[self.record]);self.sync.start();self.addCleanup(self.sync.stop)

    def write_stage(self, raw, **changes):
        cap=b'{}';prompt=b'Generic main task';text=json.dumps(raw).encode()
        (self.stage/'document-capability.json').write_bytes(cap);(self.stage/'stage.prompt.txt').write_bytes(prompt)
        (self.stage/'stage.answer.txt').write_bytes(text);(self.stage/'stage.answer.json').write_text(json.dumps(raw))
        self.meta={'name':'example/003-main-repair','module':'main-repair','status':'completed','session_id':'original','model_verified':True,'turn_completed':True,'document_audit':{'required_material_delivered':True},'start_utc':'2026-01-01T00:21:00+00:00','end_utc':'2026-01-01T00:22:00+00:00','document_capability':{'path':str(self.stage/'document-capability.json'),'sha256':hashlib.sha256(cap).hexdigest()},'prompt_sha256':hashlib.sha256(prompt).hexdigest(),'answer_sha256':hashlib.sha256(text).hexdigest(),**changes}
        (self.stage/'stage.meta.json').write_text(json.dumps(self.meta));self.problem.calls=[self.meta]
        (self.folder/'003-main-repair.json').write_text(json.dumps(raw))

    def test_valid_request_preserves_science_and_is_idempotent(self):
        before=copy.deepcopy({k:getattr(self.problem,k) for k in ['current','findings','execution_history','route_scout_history','local_verification_modules','calls','counter']})
        with self.assertRaises(h.OperationalHandoff):h.commit(self.problem,self.raw,self.meta)
        data=(self.folder/h.FILE).read_bytes()
        for action in [lambda:h.commit(self.problem,self.raw,self.meta),lambda:h.guard(self.problem)]:
            with self.assertRaises(h.OperationalHandoff):action()
            self.assertEqual((self.folder/h.FILE).read_bytes(),data)
        self.assertEqual(before,{k:getattr(self.problem,k) for k in before})
        self.assertFalse(json.loads(data)['automatic_resume_authorized'])

    def test_extra_science_stale_duplicate_boolean_and_draft_reject(self):
        invalid=[{**self.raw,'proof_markdown':'Changed'}, {**self.raw,'no_new_scientific_work':1}, {**self.raw,'reason':[]}, {**self.raw,'exhaustion_ids':['b'*64,'b'*64]}, {**self.raw,'exhaustion_ids':['c'*64]}, {**self.raw,'selected_candidate_sha256':'c'*64}]
        for raw in invalid:
            with self.subTest(raw=raw),self.assertRaises(ValueError):h.validate_request(self.problem,raw,[self.record])
        self.document['status']='draft'
        with self.assertRaisesRegex(ValueError,'pending'):h.validate_request(self.problem,self.raw,[self.record])
        self.assertFalse((self.folder/h.FILE).exists())

    def test_authentication_chronology_and_incomplete_call_reject(self):
        for changes in [{'session_id':'other'},{'status':'timeout_censored'},{'model_verified':False},{'start_utc':'2026-01-01T00:19:00+00:00'},{'document_audit':{'required_material_delivered':False}}]:
            self.write_stage(self.raw,**changes)
            with self.subTest(changes=changes),self.assertRaises(ValueError):h.commit(self.problem,self.raw,self.meta)
        self.write_stage(self.raw);(self.stage/'stage.answer.txt').write_text('tampered')
        with self.assertRaisesRegex(ValueError,'hash'):h.commit(self.problem,self.raw,self.meta)

    def test_crash_gap_recovers_only_latest_valid_completed_answer(self):
        (self.folder/'003-main-repair.json').unlink()  # Crash before campaign copy/checkpoint.
        with self.assertRaises(h.OperationalHandoff):h.guard(self.problem)
        self.assertTrue((self.folder/h.FILE).exists())
        (self.folder/h.FILE).unlink();self.problem.calls.append({'name':'example/004-main-repair','status':'running','module':'main-repair'})
        h.guard(self.problem);self.assertFalse((self.folder/h.FILE).exists())

    def test_write_interruption_and_malformed_receipt_fail_closed(self):
        with patch.object(h.os,'fsync',side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):h.commit(self.problem,self.raw,self.meta)
        with self.assertRaises(h.OperationalHandoff):h.guard(self.problem)
        (self.folder/h.FILE).write_text('{')
        self.problem.operational_handoff_pending=False
        with self.assertRaises(ValueError):h.guard(self.problem)
        self.assertTrue(self.problem.operational_handoff_pending)

    def test_state_changes_symlinks_and_later_history_reject(self):
        with self.assertRaises(h.OperationalHandoff):h.commit(self.problem,self.raw,self.meta)
        self.problem.findings.append({'new':'must not disappear'})
        with self.assertRaises(ValueError):h.guard(self.problem)
        self.problem.findings.pop();self.problem.calls.append({'name':'example/004-main-repair'})
        with self.assertRaises(ValueError):h.guard(self.problem)
        p=self.folder/h.FILE;p.unlink();p.symlink_to(self.root/'missing')
        with self.assertRaises(ValueError):h.guard(self.problem)

    def test_invalid_recorded_attempt_keeps_existing_correction_route(self):
        bad={**self.raw,'extra':'not accepted'};self.write_stage(bad)
        (self.folder/'main-3-invalid-contract.json').write_text(json.dumps({'raw_response':bad}))
        h.guard(self.problem);self.assertFalse((self.folder/h.FILE).exists())
        ordinary={'response_type':'blocked_checkpoint'};self.write_stage(ordinary);h.guard(self.problem)
        self.assertFalse((self.folder/h.FILE).exists())

    def test_direct_calls_block_before_dispatch_counter_and_paper(self):
        with self.assertRaises(h.OperationalHandoff):h.commit(self.problem,self.raw,self.meta)
        self.problem.execution_capability=lambda *a: self.fail('capability/dispatch reached')
        for call in [lambda:pilot.Problem.call(self.problem,'main-repair','task'),lambda:pilot.Problem._call_once(self.problem,'proof-review','task',model='gpt-6-astra',resume=False,timeout=600)]:
            with self.assertRaises(h.OperationalHandoff):asyncio.run(call())
        self.assertEqual(self.problem.counter,3)
        self.problem._run_research=AsyncMock(return_value={'status':'partial'})
        dispatch=AsyncMock();self.problem.pilot=SimpleNamespace(exam=SimpleNamespace(dispatch=dispatch),drain=SimpleNamespace(poll=lambda:False))
        result=asyncio.run(pilot.Problem.run(self.problem));dispatch.assert_not_awaited();self.assertEqual(result['status'],'partial')

    def test_real_continuation_loader_refuses_persisted_and_crash_gap_handoff(self):
        import test_pilot_continuation as fixture_module
        fixture=fixture_module.ContinuationTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        receipt=fixture.folder/h.FILE;receipt.write_text('{}')
        with self.assertRaisesRegex(ValueError,'pending operational handoff'):fixture.load()
        receipt.unlink()
        stage=fixture.source/'host/runtime/problem/001-main-dossier'
        raw=json.dumps(self.raw).encode()
        (stage/'stage.answer.txt').write_bytes(raw)
        meta=json.loads((stage/'stage.meta.json').read_text());meta['answer_sha256']=hashlib.sha256(raw).hexdigest()
        (stage/'stage.meta.json').write_text(json.dumps(meta))
        (fixture.folder/'001-main-dossier.json').unlink() # No campaign response copy yet.
        with self.assertRaisesRegex(ValueError,'completed operational handoff'):fixture.load()
        self.assertFalse((fixture.base/'successor').exists())

    def test_real_outer_loop_main_and_postexecution_handoff_stop_before_review_or_paper(self):
        for postexecution in (False, True):
            with self.subTest(postexecution=postexecution):
                path=self.folder/h.FILE
                if path.exists():path.unlink()
                x=pilot.Problem.__new__(pilot.Problem)
                x.__dict__.update(self.problem.__dict__)
                x.operational_handoff_pending=False;x.calls=[];x.counter=2;x.ident='example';x.errors=[];x.token=None
                x.execution_history=[];x.final_assessment_history=[]
                record={**self.record,'stages':['example/001-proof-review','example/002-proof-review'],'limits_consumed':{'bounded_calls':2,'same_reviewer_recoveries':1}}
                x.review_exhaustions=[record]
                states={'example':{'status':'pending'}};released=[];paper=AsyncMock()
                campaign=SimpleNamespace(claim=lambda *a:'claim',release=lambda *a:(released.append(a),states['example'].update(status='released')),status=lambda:{'problems':states},finish=lambda *a,**k:states['example'].update(status='partial'))
                x.pilot=SimpleNamespace(config={'internet_browse':False},root=self.root,campaign=campaign,exam=SimpleNamespace(research_timeout=lambda n:n,dispatch=paper),drain=SimpleNamespace(poll=lambda:False),remaining=lambda:100,policy=lambda n:'Generic policy')
                x.carried_completion=lambda:None;x.restore_checkpoint=lambda:{'restored':True};x.status=lambda phase:None
                x.packet=lambda:{'feedback':[]};x.local_modules_enabled=lambda:False
                x.publish_document=lambda *a:self.fail('handoff published candidate')
                x.continue_research=lambda *a:self.fail('handoff scheduled another main')
                x.review_candidate=AsyncMock(side_effect=AssertionError('handoff dispatched review'))
                x.route_scouts=AsyncMock(return_value=None)
                x.execution=AsyncMock(return_value={'workers':[{'output':{'status':'done'}}],'main_probe':{}})
                async def call(*a,**kw):
                    x.counter+=1;x.calls.append(self.meta)
                    return self.meta,copy.deepcopy(self.raw)
                x.call=AsyncMock(side_effect=call)
                count=0
                async def main(*a,**kw):
                    nonlocal count
                    count+=1
                    if postexecution and count==1:return x.current
                    return await pilot.Problem.main_turn(x,*a,**kw)
                x.main_turn=main
                before=copy.deepcopy(x.current)
                with patch.object(pilot,'feedback_notice',return_value={}),patch.object(e,'synchronize',return_value=[record]):
                    result=asyncio.run(pilot.Problem.run(x))
                self.assertEqual(result['status'],'partial');self.assertEqual(x.current,before)
                self.assertEqual(x.counter,3);self.assertEqual(x.call.await_count,1)
                self.assertEqual(x.errors[-1]['reason'],'explicit_operational_handoff')
                self.assertEqual(len(released),1);self.assertTrue((self.folder/'partial.md').is_file())
                x.review_candidate.assert_not_awaited();paper.assert_not_awaited()
                self.assertEqual(x.execution.await_count,1 if postexecution else 0)

    def test_transport_handoff_cannot_be_hidden_by_altered_campaign_copy(self):
        (self.folder/'003-main-repair.json').write_text(json.dumps({'response_type':'blocked_checkpoint'}))
        with self.assertRaisesRegex(ValueError,'copy differs'):h.guard(self.problem)
        self.assertTrue(self.problem.operational_handoff_pending)
        self.assertFalse((self.folder/h.FILE).exists())
        (self.folder/'main-3-invalid-contract.json').write_text(json.dumps({'raw_response':{'response_type':'blocked_checkpoint'}}))
        with self.assertRaisesRegex(ValueError,'copy differs'):h.guard(self.problem)

    def test_ordinary_legacy_calls_gain_no_new_model_or_delivery_requirements(self):
        self.write_stage({'response_type':'blocked_checkpoint'},model_verified=False,document_audit={})
        h.guard(self.problem)
        self.assertFalse((self.folder/h.FILE).exists())
        self.problem.review_exhaustions=[];self.problem.current={'legacy':'not a current review candidate'}
        self.assertFalse(h.capability(self.problem)['eligible'])

    def test_generic_guidance_has_no_count_trigger_or_mathematical_verdict(self):
        self.assertIn(h.GUIDANCE,pilot.MAIN_FIELDS)
        cap=h.capability(self.problem);self.assertTrue(cap['eligible'])
        self.assertIn('self-report',h.GUIDANCE);self.assertIn('Never conceal',h.GUIDANCE)
        self.problem.research_continuation_state={'unchanged_binding_steps':100000}
        self.problem.review_exhaustions=[]
        self.assertFalse(h.capability(self.problem)['eligible'])


if __name__=='__main__':unittest.main()
