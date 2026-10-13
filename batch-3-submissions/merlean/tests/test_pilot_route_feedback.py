"""Supplemental objections do not hide authenticated adverse scientific feedback."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
import test_pilot_parallel_routes as fixtures
import test_pilot_research_persistence as persistence

class RouteFeedbackTests(unittest.TestCase):
    def setUp(self):
        f=fixtures.ParallelRouteTests();f.setUp();self.addCleanup(f.doCleanups)
        self.x=x=f.x
        x.pilot.host=x.folder/'host';x.pilot.config['legacy_main_stages']=['q/001-main-dossier']
        original=copy.deepcopy(x.current);original.pop('route_scout_tasks',None)
        original['unreviewed_checkpoint_findings']=[{'id':'prior','finding':'old supplemental observation'}]
        self.original=original
        mainpath=x.pilot.host/'runtime/q/001-main-dossier';mainpath.mkdir(parents=True)
        mainraw='```json\n'+p.encoded(original)+'```\n';(mainpath/'stage.answer.txt').write_text(mainraw)
        p.write(x.folder/'001-main-dossier.json',original)
        main={'name':'q/001-main-dossier','module':'main-dossier','status':'completed','answer_sha256':p.sha(mainraw),'session_id':x.session}
        self.review={'triaged_rows':[],'unresolved_findings':[{'id':'scientific-gap','severity':'gap','kind':'mathematical','finding':'Independent unresolved inference'}]}
        reviewpath=x.pilot.host/'runtime/q/004-proof-review';reviewpath.mkdir(parents=True)
        reviewraw='```json\n'+p.encoded(self.review)+'```\n';(reviewpath/'stage.answer.txt').write_text(reviewraw);(reviewpath/'stage.prompt.txt').write_text('exact review prompt')
        meta=f.f.meta('independent-proof');meta.update(name='q/004-proof-review',module='proof-review',answer_sha256=p.sha(reviewraw),prompt_sha256=p.sha('exact review prompt'))
        receipt=x.review_receipt(meta);receipt.update(reviewed_candidate_sha256=p.sha(p.encoded(original)),reviewed_proof_sha256=p.sha(original['proof_markdown']))
        x.calls=[main,meta];x.triage_history=[{'candidate_binding':p.triage_binding(original),'selected_rows':[],'receipt':receipt}]
        p.write(x.folder/'review-004-effective.json',self.review)
        x.current=copy.deepcopy(original);x.current['unreviewed_checkpoint_findings']=[{'id':'new','finding':'New adverse worker observation'}]
        x.current['route_scout_tasks']=copy.deepcopy(x.tasks)
        for task in x.current['route_scout_tasks']:
            task['obstruction_ids']=['scientific-gap'];task['purpose']='scientific_alternative'
        x.active_triage=None

    def test_supplemental_findings_preserve_adverse_trigger_not_execution_authority(self):
        self.assertNotEqual(p.triage_binding(self.original),p.triage_binding(self.x.current))
        review=self.x.route_obstruction_review()
        self.assertEqual(review['host_advisory_only_finding_ids'],['scientific-gap'])
        self.assertTrue(p.eligible_obstructions(self.x.current['route_scout_tasks'],self.x.current,review))
        self.assertEqual(self.x.current['unreviewed_checkpoint_findings'][0]['id'],'new')
        self.assertIsNone(self.x.active_triage)

    def test_changed_scientific_fields_and_fake_receipt_cannot_reuse_trigger(self):
        baseline=copy.deepcopy(self.x.current)
        for mutate in (lambda c:c.update(proof_markdown='changed proof'),lambda c:c['ledger']['rows'][0].update(claim='changed claim'),lambda c:c.update(assumptions=['new premise'])):
            self.x.current=copy.deepcopy(baseline);mutate(self.x.current)
            self.assertEqual(self.x.route_obstruction_review(),{})
        self.x.current=baseline
        self.x.triage_history[0]['receipt']['answer_sha256']='forged'
        with self.assertRaisesRegex(ValueError,'host dispatch record'):
            self.x.route_obstruction_review()

    def test_tampered_effective_objection_is_not_raw_report_authority(self):
        corrupt=copy.deepcopy(self.review);corrupt['unresolved_findings'][0]['finding']='forged motivation'
        p.write(self.x.folder/'review-004-effective.json',corrupt)
        with self.assertRaisesRegex(ValueError,'authenticated independent report'):
            self.x.route_obstruction_review()

    def test_missing_report_or_admin_only_request_returns_rejection_without_dispatch(self):
        self.x.call=AsyncMock(side_effect=AssertionError('ineligible scout dispatch'))
        self.x.current['route_scout_tasks'][0]['obstruction_ids']=['administrative-only']
        result=asyncio.run(self.x.route_scouts())
        self.assertEqual(result['status'],'not_dispatched');self.assertEqual(result['tasks'],self.x.current['route_scout_tasks'])
        self.x.call.assert_not_awaited();self.assertEqual(self.x.route_scout_history,[])
        (self.x.folder/'review-004-effective.json').unlink()
        self.assertEqual(self.x.route_obstruction_review(),{})

    def test_rejected_route_keeps_same_main_working_with_complete_failed_feedback(self):
        f=persistence.ResearchPersistenceTests();f.setUp();self.addCleanup(f.doCleanups)
        x=f.x;calls=[]
        async def main(instruction,**kwargs):
            calls.append(instruction)
            x.last_main_checkpoint={'actionable':True}
            if len(calls)==3:
                self.assertIn('route rejected exact reason',instruction)
                self.assertIn('Complete adverse proof finding retained',instruction)
                raise p.DrainRequested('explicit stop')
        x.main_turn=main
        x.route_scouts=AsyncMock(side_effect=[None,{'status':'not_dispatched','reason':'route rejected exact reason','tasks':[{'exact':'proposal'}]}])
        x.review_candidate=AsyncMock(return_value=({}, {'verdict':'INCOMPLETE','gaps':['Complete adverse proof finding retained']}))
        result=asyncio.run(x.run())
        self.assertEqual(len(calls),3);self.assertEqual(result['errors'][-1]['type'],'CooperativeDrain')
        x.execution.assert_awaited_once()
        x.review_candidate.assert_awaited_once_with('focused')

    def test_supplemental_churn_cannot_renew_identical_portfolio(self):
        x=self.x
        review=x.route_obstruction_review()
        obs=p.eligible_obstructions(x.current['route_scout_tasks'],x.current,review)
        basis=copy.deepcopy(x.current);basis.pop('unreviewed_checkpoint_findings')
        key=p.census_key(p.assessment_key(basis,x.execution_history),obs)
        x.route_scout_history=[{'census_key':key,'status':'completed'}]
        x.current['unreviewed_checkpoint_findings'].append({'id':'churn','finding':'another main observation'})
        x.current['route_scout_tasks'][0]['task']+=' cosmetic wording'
        x.call=AsyncMock(side_effect=AssertionError('duplicate scout'))
        result=asyncio.run(x.route_scouts())
        self.assertEqual(result['status'],'already_assessed');x.call.assert_not_awaited()
        changed=copy.deepcopy(basis);changed['proof_markdown']+=' new scientific argument'
        self.assertNotEqual(key,p.census_key(p.assessment_key(changed,x.execution_history),obs))

    def test_newest_applicable_report_does_not_select_old_favorable_obstruction(self):
        x=self.x
        latest=copy.deepcopy(x.triage_history[-1]);meta=copy.deepcopy(x.calls[-1])
        meta['name']='q/005-proof-review';meta['session_id']='new-independent'
        raw=p.encoded({'triaged_rows':[],'unresolved_findings':[]})
        meta['answer_sha256']=p.sha(raw)
        folder=x.pilot.host/'runtime'/meta['name'];folder.mkdir(parents=True)
        (folder/'stage.answer.txt').write_text(raw);(folder/'stage.prompt.txt').write_text('exact review prompt')
        latest['receipt'].update(meta);x.calls.append(meta);x.triage_history.append(latest)
        p.write(x.folder/'review-005-effective.json',{'triaged_rows':[],'unresolved_findings':[]})
        result=asyncio.run(x.route_scouts());self.assertEqual(result['status'],'not_dispatched')
        (x.folder/'review-005-effective.json').unlink()
        self.assertEqual(x.route_obstruction_review(),{})

    def test_legacy_paid_portfolio_remains_deduplicated_after_upgrade(self):
        x=self.x;obs=p.eligible_obstructions(x.current['route_scout_tasks'],x.current,x.route_obstruction_review())
        old={'candidate_sha256':p.sha(p.encoded(self.original)),
             'census_key':p.census_key(p.assessment_key(self.original,x.execution_history),obs),
             'obstructions':obs,'status':'completed'}
        x.route_scout_history=[copy.deepcopy(old)]
        x.call=AsyncMock(side_effect=AssertionError('legacy duplicate scout'))
        self.assertEqual(asyncio.run(x.route_scouts())['status'],'already_assessed')
        self.assertEqual(x.route_scout_history,[old]);x.call.assert_not_awaited()
