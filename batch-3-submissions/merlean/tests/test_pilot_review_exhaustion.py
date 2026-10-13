import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_review_exhaustion as guard
import codex_pilot as pilot

class ReviewExhaustionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name).resolve()
        self.candidate={'proof_markdown':'A proof with steps','answer_statement':'A statement',
                        'ledger':{'rows':[{'claim':'First claim'},{'claim':'Second claim'}]}}
        self.record={'schema_version':1,'authority':guard.AUTHORITY,'binding':{'lens':'focused','model':pilot.ASTRA,
                     'scientific':guard.projection(self.candidate)},'reviewer_session':'reviewer','stages':['p/1','p/2'],
                     'end_utc':'2026-01-01T00:00:00Z','limits_consumed':{'bounded_calls':2,'same_reviewer_recoveries':1},
                     'required_material_delivered':True,'id':'exhausted'}
        self.main={'name':'p/3-main','module':'main-repair','status':'completed','session_id':'main',
                   'end_utc':'2026-01-02T00:00:00Z','prompt_sha256':'prompt','answer_sha256':'answer'}
        self.problem=SimpleNamespace(folder=self.folder,calls=[self.main],current=copy.deepcopy(self.candidate),session='main')
    def check(self,resume=None):
        with patch.object(guard,'derive',return_value=[self.record]):
            return guard.guard(self.problem,'REVIEW_MODE=focused.',pilot.ASTRA,resume)
    def test_same_science_metadata_order_whitespace_nonce_and_retry_prose_blocked(self):
        for mutation in ('none','notes','nonce','whitespace','order','rowstatus'):
            self.problem.current=copy.deepcopy(self.candidate)
            c=self.problem.current
            if mutation=='notes':c.update(notes='please retry after migration',review_request='different prose',revision=100)
            if mutation=='nonce':c['nonce']='unique'
            if mutation=='whitespace':c['proof_markdown']=' A\n proof   with\tsteps '
            if mutation=='order':c['ledger']['rows'].reverse()
            if mutation=='rowstatus':c['ledger']['rows'][0].update(status='proved',triaged=False,evidence='new self-report')
            with self.subTest(mutation=mutation),self.assertRaises(guard.ExhaustedReview):self.check()
    def test_changed_content_requires_accepted_same_main_provenance_and_fresh_reviewer(self):
        self.problem.current['proof_markdown']='A proof with a different argument'
        with self.assertRaises(guard.ExhaustedReview):self.check()
        record={'main_stage':self.main['name'],'main_session':'main','answer_sha256':'answer',
                'scientific_sha256':guard.digest(guard.projection(self.problem.current))}
        (self.folder/'review-material-main.json').write_text(json.dumps(record))
        self.check()
        with self.assertRaises(guard.ExhaustedReview):self.check('reviewer')
        self.problem.calls[0]['session_id']='other-main'
        with self.assertRaises(guard.ExhaustedReview):self.check()
    def test_admission_symlink_is_rejected_without_target_write(self):
        self.problem.current['proof_markdown']='A changed main-authored proof'
        (self.folder/'review-material-main.json').write_text(json.dumps({'main_stage':self.main['name'],
            'main_session':'main','answer_sha256':'answer','scientific_sha256':guard.digest(guard.projection(self.problem.current))}))
        self.check()
        receipt=next(self.folder.glob('review-exhaustion-admission-*.json'));receipt.unlink()
        target=self.folder/'never-write';receipt.symlink_to(target)
        with self.assertRaises(ValueError):self.check()
        self.assertFalse(target.exists())

    def test_model_or_lens_switch_does_not_reset_exhausted_material(self):
        with patch.object(guard,'derive',return_value=[self.record]):
            for instruction,model in [('REVIEW_MODE=comprehensive.',pilot.ASTRA),('REVIEW_MODE=focused.','different-model')]:
                with self.assertRaises(guard.ExhaustedReview):guard.guard(self.problem,instruction,model)

    def test_registry_survives_repeated_restoration_and_rejects_loss_or_mutation(self):
        with patch.object(guard,'derive',return_value=[self.record]):
            for _ in range(3):self.assertEqual(guard.synchronize(self.folder,[]),[self.record])
        before=(self.folder/'review-exhaustion.json').read_bytes()
        with patch.object(guard,'derive',return_value=[]),self.assertRaises(ValueError):guard.synchronize(self.folder,[])
        self.assertEqual(before,(self.folder/'review-exhaustion.json').read_bytes())
        (self.folder/'review-exhaustion.json').write_text('{}')
        with patch.object(guard,'derive',return_value=[self.record]),self.assertRaises(ValueError):guard.synchronize(self.folder,[])
    def test_direct_and_public_dispatch_stop_before_counter_budget_or_process(self):
        p=pilot.Problem.__new__(pilot.Problem);p.execution_capability=Mock();p.counter=451
        p.pilot=SimpleNamespace()
        with patch.object(guard,'guard',side_effect=guard.ExhaustedReview([self.record])) as check:
            for direct in (False,True):
                with self.assertRaises(guard.ExhaustedReview):
                    if direct:asyncio.run(p._call_once('proof-review','REVIEW_MODE=focused.',model=pilot.ASTRA,resume=False,timeout=600))
                    else:asyncio.run(p.call('proof-review','REVIEW_MODE=focused.',timeout=600))
                self.assertEqual(p.counter,451)
            self.assertEqual(check.call_count,2)
    def test_feedback_has_no_verdict_findings_task_approval_or_commentary(self):
        error=guard.ExhaustedReview([self.record]);f=error.feedback
        self.assertEqual(f['authority'],guard.AUTHORITY)
        self.assertFalse(set(f)&{'verdict','unresolved_findings','approved_lean_tasks','approved_research_tasks','mathematically_ready'})
    def test_invalid_candidate_and_stale_main_binding_rejected(self):
        with self.assertRaises(ValueError):guard.projection({'ledger':{'rows':[]}})
        self.problem.current['answer_statement']='Changed statement'
        (self.folder/'review-material-main.json').write_text('{}')
        with self.assertRaises(ValueError):self.check()

class AuthenticatedPairTests(unittest.TestCase):
    def pair(self):
        import test_pilot_document_recovery as fixtures
        import pilot_document_tools as tools
        import pilot_document_recovery as recovery
        fixture=fixtures.DocumentRecoveryTests();fixture.setUp();self.addCleanup(fixture.tearDown)
        root,first,meta,kwargs=fixture.build()
        proof=root/'proof.md';proof.write_text('A complete candidate narrative')
        candidate={'answer_statement':'A statement','ledger':{'rows':[{'claim':'A claim'}]}}
        scopes=[]
        for stage in (first,first.parent/'002-proof-review'):
            path=stage/'document-capability.json';scope=json.loads(path.read_text())
            scope['readonly_artifacts']['proof']={'path':str(proof),'sha256':tools.digest(proof.read_bytes()),'media_type':'text/markdown'}
            scope['inline_artifact_ids']=['proof'];path.write_text(json.dumps(scope));scopes.append(scope)
        meta['document_capability']['sha256']=tools.digest((first/'document-capability.json').read_bytes())
        meta['document_audit']=tools.audit_operations(scopes[0],meta['document_events'],meta['persisted_rollout_audit']['tool_events'],meta['session_id'],meta['persisted_rollout_audit']['tool_output_receipts'])
        base='REVIEW_MODE=focused.\nCURRENT CANDIDATE, PREMISES AND COMPLETE REQUIRED FINDINGS\n'+json.dumps({'exact_candidate':candidate,'prior_findings':[]})
        prompt=base+'\n'+tools.invocation_guidance('review')
        meta.update(turn_completed=False,end_utc='2026-01-01T00:00:00Z',prompt_sha256=tools.digest(prompt.encode()),prompt_bytes=len(prompt.encode()))
        (first/'stage.prompt.txt').write_text(prompt);(first/'stage.meta.json').write_text(json.dumps(meta))
        second=first.parent/'002-proof-review';prompt2=base+recovery.TIMEOUT_RECOVERY_GUIDANCE+'\n'+tools.invocation_guidance('review')
        checked=recovery.verify_recovery(root,recovery.recovery_reference(root,meta),name='p/002-proof-review',module='proof-review',model=pilot.ASTRA,resume_session=meta['session_id'],prompt=prompt2,scope=scopes[1])
        (second/'stage.prompt.txt').write_text(prompt2);(second/'stage.events.jsonl').write_text('')
        second_meta={**meta,'name':'p/002-proof-review','resume_session':meta['session_id'],
                     'end_utc':'2026-01-01T00:10:00Z','document_recovery':checked,
                     'document_capability':{'path':str(second/'document-capability.json'),'sha256':tools.digest((second/'document-capability.json').read_bytes())},
                     'prompt_sha256':tools.digest(prompt2.encode()),'prompt_bytes':len(prompt2.encode()),'document_events':[],
                     'persisted_rollout_audit':{'status':'verified','tool_events':[],'tool_output_receipts':[]}}
        a=tools.audit_operations(scopes[1],[],[],meta['session_id'],[])
        second_meta['document_audit']=recovery.inherit_coverage(a,checked,scope=scopes[1],actual_session=meta['session_id'])
        (second/'stage.meta.json').write_text(json.dumps(second_meta))
        return root,[meta,second_meta]
    def test_authenticated_pair_and_missing_or_changed_history_fail_closed(self):
        root,calls=self.pair();records=guard.derive(calls)
        self.assertEqual(len(records),1);self.assertEqual(records[0]['limits_consumed']['same_reviewer_recoveries'],1)
        self.assertEqual(guard.synchronize(root,calls),records)
        self.assertEqual(guard.synchronize(root,calls),records)
        for change in ('missing','session','scope','metadata'):
            bad=copy.deepcopy(calls)
            if change=='missing':bad=bad[1:]
            elif change=='session':bad[1]['resume_session']='wrong'
            elif change=='scope':bad[1]['document_recovery']['immutable_scope_sha256']='wrong'
            else:bad[0]['end_utc']='changed'
            with self.subTest(change=change),self.assertRaises(ValueError):guard.derive(bad)
    def test_registry_and_material_symlinks_fail_closed(self):
        root,calls=self.pair();path=root/'review-exhaustion.json';path.symlink_to(root/'absent')
        with self.assertRaises(ValueError):guard.synchronize(root,calls)
        with self.assertRaises(ValueError):guard.save(path,{})
        self.assertFalse((root/'absent').exists())

if __name__=='__main__':unittest.main()
