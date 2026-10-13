"""A drained host reservation may finish once; repeated completed requests still stop."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p

class AdmittedMock(AsyncMock):
    """Simulate the real transport's concrete admission callback before dispatch."""
    async def _execute_mock_call(self, *args, **kwargs):
        callback = kwargs.get('on_admitted')
        if callback:
            callback()
        return await super()._execute_mock_call(*args, **kwargs)

import test_pilot_checkpoint_scope_contract as fixtures
from pilot_candidate_contract import apply_main_response

class AssessmentResumeTests(unittest.TestCase):
    def setUp(self):
        f = fixtures.MainCheckpointRuntimeTests(); f.setUp(); self.addCleanup(f.doCleanups)
        self.f, self.x, self.raw = f, f.x, f.raw
        self.raw['review_request'] = 'substantive_reassessment'
        x = self.x
        x.status = lambda _: None
        cap_patch=patch.object(p.assessment_handoff,'capability',return_value={'eligible':False,'assessment_ids':[]})
        cap_patch.start();self.addCleanup(cap_patch.stop)
        x.pilot.root = x.folder; x.original_bytes = b'original'; x.statement = 'original'
        self.pending = {'execution_identity_version':2, 'binding_key': p.assessment_key(x.current, []),
            'candidate_sha256': p.sha(p.encoded(x.current)), 'status': 'commissioned', 'attempts': 1,
            'retry_after_reconciliation': True, 'authority': 'assessment_only'}
        self.saved = {'current':copy.deepcopy(x.current),'findings':copy.deepcopy(x.findings),
            'main_session':'actual-main','original_sha256':p.sha(b'original'),'implementers':['actual-main'],
            'calls':[],'errors':[{'type':'CooperativeDrain'}],'dossier':{},'counter':7,
            'execution_history':[], 'final_assessment_history':[self.pending]}
        _, checkpoint = apply_main_response(self.raw, {p.sha(p.encoded(x.current)):x.current})
        checkpoint['execution_identity_version']=2
        checkpoint['request_key'] = p.checkpoint_request_key(checkpoint, [])
        p.write(x.folder/'main-6-checkpoint.json',checkpoint)

    def restore(self):
        ref = p.write(self.x.folder/'continuation-checkpoint.json', {'problems':{self.x.ident:self.saved}})
        self.x.pilot.config={'continuation_checkpoint':ref,'internet_browse':False}
        self.x.restore_checkpoint()

    def main(self):
        self.x.call=AdmittedMock(return_value=(self.f.f.meta('actual-main'),copy.deepcopy(self.raw)))
        asyncio.run(self.x.main_turn('Continue'))
        return self.x.last_main_checkpoint

    def test_epoch_migration_preserves_exact_legacy_attempts_and_mints_new_eligibility(self):
        previous = dict(self.pending, attempts=2, retry_after_reconciliation=False)
        self.saved['final_assessment_history'] = [copy.deepcopy(previous)]
        ref = p.write(self.x.folder/'continuation-checkpoint.json', {'problems':{self.x.ident:self.saved}})
        self.x.pilot.config = {'continuation_checkpoint':ref, 'internet_browse':False,
                              'assessment_protocol_epoch':p.ASSESSMENT_PROTOCOL_EPOCH}
        self.x.restore_checkpoint()
        self.assertEqual(self.x.final_assessment_history[0], previous)
        self.assertEqual(len(self.x.final_assessment_history), 2)
        migrated = self.x.final_assessment_history[1]
        self.assertEqual(migrated['attempts'], 2)
        self.assertEqual(migrated['infrastructure_resume_of'], p.sha(p.encoded(previous)))
        self.assertTrue(migrated['retry_after_reconciliation'])
        checkpoint = self.main()
        self.assertTrue(checkpoint['actionable'])
        self.assertEqual(checkpoint['assessment_recovery']['attempts_before_resume'], 2)
        self.assertEqual(self.x.final_assessment_history[0], previous)

    def test_actual_commissioned_shape_survives_duplicate_and_records_new_attempt(self):
        self.restore(); checkpoint=self.main()
        self.assertTrue(checkpoint['actionable'])
        recovery=checkpoint['assessment_recovery']
        self.assertEqual(checkpoint['request_key'],json.loads((self.x.folder/'main-6-checkpoint.json').read_text())['request_key'])
        self.x.call=AdmittedMock(return_value=(self.f.f.meta('fresh-advice'),{'verdict':'unknown'}))
        self.x.review_candidate=AsyncMock(return_value=(self.f.f.meta('fresh-proof'),{'verdict':'INCOMPLETE'}))
        asyncio.run(self.x.commission_final_assessment(None,resume_reservation=recovery))
        self.assertEqual(self.x.final_assessment_history[0]['attempts'],2)
        self.assertFalse(self.x.final_assessment_history[0]['retry_after_reconciliation'])
        self.assertEqual(self.x.final_assessment_history[0]['prior_attempts'][0]['status'],'commissioned')
        self.x.review_candidate.assert_awaited_once_with('comprehensive')
        self.assertEqual(self.x.call.call_args.args[0],'preacceptance-scope-review')
        with self.assertRaisesRegex(ValueError,'reconciled host admission'):
            asyncio.run(self.x.commission_final_assessment(None,resume_reservation=recovery))
        self.assertFalse(self.main()['actionable'])

    def test_completed_rejected_absent_or_changed_binding_cannot_bypass_dedup(self):
        cases=[[],[dict(self.pending,status='reviewed')],
            [dict(self.pending,final_validation={'successful_complete':False})],
            [dict(self.pending,candidate_sha256='0'*64)],
            [dict(self.pending,binding_key='0'*64)]]
        for records in cases:
            with self.subTest(records=records):
                self.saved['final_assessment_history']=records
                self.restore()
                self.assertFalse(self.main()['actionable'])

    def test_live_object_cannot_mint_admission_and_new_work_is_not_resumed(self):
        self.x.final_assessment_history=[copy.deepcopy(self.pending)]
        self.assertFalse(self.main()['actionable'])
        self.restore()
        _, checkpoint=apply_main_response(self.raw,{p.sha(p.encoded(self.x.current)):self.x.current})
        checkpoint['raw_checkpoint']['proposed_work']['sol_tasks']=[{'task':'new work'}]
        self.assertIsNone(self.x.admit_interrupted_assessment(checkpoint,self.x.current))

    def test_changed_execution_blocks_recovery_but_historical_attempts_are_not_a_cap(self):
        self.restore()
        self.x.execution_history=[{'workers':[{'task_id':'new-worker','execution_receipt':{'name':'q/009-sol-execution','request_id':'new','answer_sha256':'a'*64},'output':{'status':'completed','result':'new'}}],
                                  'main_probe':{'status':'not_requested'}}]
        _, checkpoint=apply_main_response(self.raw,{p.sha(p.encoded(self.x.current)):self.x.current})
        self.assertIsNone(self.x.admit_interrupted_assessment(checkpoint,self.x.current))
        self.saved['final_assessment_history']=[dict(self.pending,attempts=2)]
        self.restore(); self.assertTrue(self.main()['actionable'])

    def test_interruption_during_resumed_dispatch_persists_consumed_bound(self):
        self.restore(); checkpoint=self.main()
        self.x.call=AdmittedMock(side_effect=RuntimeError('captured dispatch boundary'))
        with self.assertRaisesRegex(RuntimeError,'captured dispatch'):
            asyncio.run(self.x.commission_final_assessment(None,resume_reservation=checkpoint['assessment_recovery']))
        self.assertEqual(self.x.final_assessment_history[0]['attempts'],2)
        self.assertEqual(self.x.final_assessment_history[0]['status'],'commissioned')
        self.assertFalse(self.x.final_assessment_history[0]['retry_after_reconciliation'])

    def test_run_resumes_pending_stage_without_focused_review_or_execution(self):
        self.restore()
        self.x.pilot.remaining=lambda:100
        self.x.pilot.campaign.status.return_value={'problems':{self.x.ident:{'status':'running'}}}
        roles=[]
        async def call(role,instruction,**kwargs):
            roles.append(role)
            if kwargs.get('on_admitted'):
                kwargs['on_admitted']()
            if role.startswith('main'):
                return self.f.f.meta('actual-main'),copy.deepcopy(self.raw)
            raise RuntimeError('captured pending assessment boundary')
        self.x.call=call
        self.x.execution=AsyncMock(side_effect=AssertionError('must not dispatch execution'))
        self.x.review_candidate=AsyncMock(side_effect=AssertionError('must not dispatch focused review'))
        result=asyncio.run(self.x.run())
        self.assertEqual(roles,['main-repair','preacceptance-scope-review'])
        self.assertEqual(result['status'],'partial')
        self.assertEqual(self.x.final_assessment_history[0]['attempts'],2)
        self.x.execution.assert_not_awaited()
        self.x.review_candidate.assert_not_awaited()
