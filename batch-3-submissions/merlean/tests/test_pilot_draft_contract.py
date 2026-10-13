import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as pilot
import pilot_candidate_contract as contract
import pilot_document_tools as tools
import pilot_proof_document as documents
import test_pilot_proof_document as fixtures

class DraftContractTests(unittest.TestCase):
    def setUp(self):
        self.fixture=fixtures.ProofPilotIntegrationTests();self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups);self.x=self.fixture.x
        self.saved=documents.save_draft(self.x.folder,**self.x.document_identity(),
            expected_revision=self.x.document_current()['revision'],proof_markdown='Unsubmitted draft with an explicit gap',
            producer={'stage':'q/002-main','request_id':'save','session_id':'main'})
        self.raw={'response_type':'draft_checkpoint','proof_revision':self.saved['revision'],'reason':'Preserve the unsubmitted draft.'}
    def test_exact_schema_shared_by_main_and_main_document_instructions(self):
        self.assertIn(contract.DRAFT_CHECKPOINT_GUIDANCE,pilot.MAIN_FIELDS)
        self.assertIn(contract.DRAFT_CHECKPOINT_GUIDANCE,tools.invocation_guidance('main'))
        self.assertNotIn(contract.DRAFT_CHECKPOINT_GUIDANCE,tools.invocation_guidance('review'))
        self.assertEqual(contract.DRAFT_CHECKPOINT_FIELDS,{'response_type','proof_revision','reason'})
    def test_valid_save_only_does_not_publish_or_change_scientific_candidate(self):
        before=copy.deepcopy(self.x.current);pointer=self.x.document_current()
        effective,checkpoint=self.x.apply_authored_response(self.raw,{})
        self.assertEqual(effective,before);self.assertEqual(self.x.current,before)
        self.assertFalse(checkpoint['actionable']);self.assertTrue(checkpoint['operational_draft_checkpoint'])
        self.assertEqual(self.x.document_current(),pointer);self.assertEqual(pointer['status'],'draft')
        self.assertEqual(self.x.document_submission()['candidate'],before)
        with self.assertRaisesRegex(ValueError,'submitted'):self.x.review_context({'exact_candidate':before})
    def test_extra_hash_scientific_fields_missing_stale_and_empty_reason_rejected(self):
        invalid=[dict(self.raw,proof_sha256=self.saved['proof_sha256']),dict(self.raw,research_work={'result':'a claim'}),
                 dict(self.raw,unreviewed_findings=[]),dict(self.raw,review_request='none'),dict(self.raw,reason=' '),
                 dict(self.raw,reason=[]),dict(self.raw,proof_revision=17),dict(self.raw,proof_revision='stale')]
        missing=dict(self.raw);missing.pop('reason');invalid.append(missing)
        before=copy.deepcopy(self.x.current)
        for raw in invalid:
            with self.subTest(keys=list(raw)),self.assertRaises(ValueError):self.x.apply_authored_response(raw,{})
            self.assertEqual(self.x.current,before);self.assertEqual(self.x.document_current()['status'],'draft')
        diag=contract.draft_checkpoint_diagnostics(invalid[0]);self.assertEqual(diag['unexpected_fields'],['proof_sha256'])
        self.assertEqual(diag['missing_fields'],[])
        self.assertEqual(contract.draft_checkpoint_diagnostics(missing)['missing_fields'],['reason'])
    def run_correction(self, second_valid):
        before=copy.deepcopy(self.x.current);prompts=[]
        bad=dict(self.raw,proof_sha256=self.saved['proof_sha256'])
        async def call(role,instruction,**kwargs):
            prompts.append(instruction);self.x.counter+=1
            response=self.raw if second_valid and len(prompts)==2 else bad
            return self.fixture.f.meta(str(self.x.counter)+'-main'),copy.deepcopy(response)
        self.x.call=call
        if second_valid:asyncio.run(self.x.main_turn('Continue same main'))
        else:
            with self.assertRaisesRegex(ValueError,'proof_sha256'):asyncio.run(self.x.main_turn('Continue same main'))
        self.assertEqual(len(prompts),2)
        self.assertIn(contract.DRAFT_CHECKPOINT_GUIDANCE,prompts[0]);self.assertIn(contract.DRAFT_CHECKPOINT_GUIDANCE,prompts[1])
        self.assertIn('proof_sha256',prompts[1]);self.assertIn(pilot.encoded(bad),prompts[1])
        self.assertEqual(self.x.current,before);self.assertEqual(self.x.document_current()['status'],'draft')
        failures=[json.loads(p.read_text()) for p in self.x.folder.glob('*invalid-contract.json')]
        self.assertEqual(len(failures),1 if second_valid else 2)
        self.assertTrue(all(x['acceptance_authority'] is False for x in failures))
        self.assertTrue(all(x['draft_schema_diagnostics']['unexpected_fields']==['proof_sha256'] for x in failures))
        if not second_valid:self.assertTrue(failures[-1].get('recovery_exhausted') or failures[0].get('recovery_exhausted'))
    def test_existing_single_correction_gets_exact_shape_and_can_save_only(self):self.run_correction(True)
    def test_repeated_extra_hash_still_exhausts_existing_single_correction(self):self.run_correction(False)

if __name__=='__main__':unittest.main()
