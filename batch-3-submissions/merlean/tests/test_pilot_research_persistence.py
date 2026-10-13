"""Scientific checkpoints keep the same main working; paid reviews remain bound."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, Mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
from pilot_drain import DrainRequested
from pilot_candidate_contract import apply_main_response, candidate_hash
import test_pilot_assessment_resume as fixtures

class ResearchPersistenceTests(unittest.TestCase):
    def setUp(self):
        f=fixtures.AssessmentResumeTests();f.setUp();self.addCleanup(f.doCleanups)
        self.f=f;self.x=x=f.x
        x.pilot.root=x.folder;x.pilot.remaining=lambda:1000
        x.pilot.policy=lambda _: 'POLICY';x.pilot.config={'internet_browse':False}
        x.pilot.campaign.status.return_value={'problems':{x.ident:{'status':'running'}}}
        x.restore_checkpoint=Mock(return_value={'preserved':True})
        x.route_obstruction_review=Mock(return_value={'verdict':'INCOMPLETE','gaps':['actual obstruction']})
        x.packet=Mock(return_value={'feedback':[]})
        x.route_scout_history=[];x.final_assessment_history=[];x.research_continuation_state={}
        x.route_scouts=AsyncMock(return_value=None)
        x.execution=AsyncMock(return_value={'workers':[],'main_probe':{'status':'not_requested'}})
        x.active_triage=None
        self.raw=copy.deepcopy(f.raw);self.raw['review_request']='none'
        self.checkpoint={'actionable':False,'raw_checkpoint':self.raw}

    def test_no_action_then_real_progress_reaches_review_same_goal(self):
        purposes=[]
        async def main(instruction,**kwargs):
            purposes.append(kwargs.get('purpose'))
            if len(purposes)==1:
                self.x.last_main_checkpoint=copy.deepcopy(self.checkpoint)
            else:
                self.assertIn('actual obstruction',instruction)
                self.assertIn('Do actual substantive work',instruction)
                self.x.last_main_checkpoint=None
                self.x.current['proof_markdown']+=' Substantive newly developed argument.'
        self.x.main_turn=main
        self.x.review_candidate=AsyncMock(side_effect=DrainRequested('explicit synthetic stop'))
        result=asyncio.run(self.x.run())
        self.assertEqual(purposes,[None,'scientific_strategy_development'])
        self.x.review_candidate.assert_awaited_once_with('focused')
        self.assertEqual(result['status'],'partial')
        self.assertEqual(result['errors'][-1]['type'],'CooperativeDrain')
        self.assertEqual(self.x.research_continuation_state['step'],1)

    def test_repeated_checkpoint_preserves_main_choice_without_review_or_fake_progress(self):
        original=copy.deepcopy(self.x.current);modes=[]
        original_key=p.assessment_key(self.x.current,self.x.execution_history)
        async def main(instruction,**kwargs):
            if len(modes)==6:
                raise p.StageFailure({'name':'q/main','status':'process_failed'},['subscription quota exceeded'])
            modes.append(self.x.research_continuation_state.get('mode'))
            if len(modes)>1:
                self.assertIn('Continue or refine the current approach',instruction)
                self.assertIn('options, not a rotation',instruction)
                self.assertNotIn('genuinely different next step',instruction)
            self.x.last_main_checkpoint=copy.deepcopy(self.checkpoint)
        self.x.main_turn=main;self.x.review_candidate=AsyncMock(side_effect=AssertionError('duplicate review'))
        result=asyncio.run(self.x.run())
        self.assertEqual(result['errors'][-1]['type'],'StageFailure')
        self.assertEqual(set(modes[1:]),{'main_selected'})
        self.assertEqual(self.x.current,original)
        self.assertEqual(p.assessment_key(self.x.current,self.x.execution_history),original_key)
        self.x.execution.assert_not_awaited();self.x.review_candidate.assert_not_awaited()
        self.x.route_scouts.assert_not_awaited()
        self.assertEqual(len(list(self.x.folder.glob('research-continuation-0*.json'))),6)

    def test_legacy_mode_state_continues_without_rewriting_history_or_losing_evidence(self):
        work={k:'Continue the same promising approach using the new local bound.'
              for k in ('objective','approach','work_performed','result','next_step')}
        work['failed_approaches']=['A rejected shortcut retained its original obstruction.']
        self.x.last_main_checkpoint=copy.deepcopy(self.checkpoint)
        self.x.last_main_checkpoint['raw_checkpoint']['research_work']=work
        adverse={'review':{'verdict':'INCOMPLETE','gaps':['exact outstanding use-site hypothesis']}}
        legacy={'step':12,'mode':'alternative_representation','receipt':{'path':'old-receipt.json'},
                'latest_scientific_feedback':adverse}
        self.x.research_continuation_state=legacy
        feedback=self.x.continue_research('no_action',{'research_continuation':legacy})
        current=self.x.research_continuation_state
        self.assertEqual(legacy['mode'],'alternative_representation')
        self.assertEqual(current['step'],13)
        self.assertEqual(current['mode'],'main_selected')
        self.assertEqual(current['last_research_work'],work)
        self.assertEqual(feedback['scientific_context']['latest_scientific_feedback'],adverse)
        event=json.loads((self.x.folder/'research-continuation-00013.json').read_text())
        self.assertEqual(event['previous_receipt'],legacy['receipt'])
        self.assertEqual(event['authority'],'main_research_scheduling_only_no_acceptance_or_dispatch_approval')
        self.x.execution.assert_not_awaited();self.x.route_scouts.assert_not_awaited()

    def test_failed_final_feedback_retained_exact_without_recursive_growth(self):
        adverse={'scopes':[{'verdict':'fail','extra_assumptions':['unjustified premise']}],
                 'silver':{'verdict':'BRONZE','gaps':['missing certificate']},
                 'controller_feedback':[{'finding':'actual adverse disposition'}]}
        feedback=adverse
        for _ in range(8):
            self.x.last_main_checkpoint=copy.deepcopy(self.checkpoint)
            feedback=self.x.continue_research('no_action',{'checkpoint':self.checkpoint,'prior_feedback':feedback})
            self.assertEqual(feedback['scientific_context']['latest_scientific_feedback'],adverse)
            self.assertNotIn('prior_feedback',feedback['latest_blocked_feedback'])
        self.assertEqual(self.x.research_continuation_state['step'],8)
        self.assertLess(len(p.encoded(feedback)),7000)

    def test_research_work_stays_separate_and_grants_no_dispatch_authority(self):
        raw=copy.deepcopy(self.raw)
        raw['research_work']={k:'actual attempted analysis' for k in ('objective','approach','work_performed','result','next_step')}
        raw['research_work']['failed_approaches']=['previous route fails at unresolved inference']
        binding=candidate_hash(self.x.current);raw['selected_candidate_sha256']=binding
        current,checkpoint=apply_main_response(raw,{binding:self.x.current})
        self.assertEqual(current,self.x.current);self.assertFalse(checkpoint['actionable'])
        raw['research_work']['acceptance']='PASS'
        with self.assertRaises(ValueError):apply_main_response(raw,{binding:self.x.current})

    def test_candidate_cannot_smuggle_research_work_to_renew_assessment(self):
        original = copy.deepcopy(self.x.current)
        binding = p.assessment_key(original, self.x.execution_history)
        valid = {k:'actual analysis' for k in ('objective','approach','work_performed','result','next_step')}
        valid['failed_approaches'] = []
        for work in (valid, {'work_performed':'cosmetic scheduling wording'}, None):
            for legacy in (False, True):
                candidate = copy.deepcopy(original)
                if not legacy:
                    candidate['response_type'] = 'candidate_update'
                candidate['research_work'] = work
                with self.assertRaisesRegex(ValueError, 'checkpoint-only'):
                    apply_main_response(candidate, {candidate_hash(original):original}, allow_legacy=legacy)
                self.assertEqual(self.x.current, original)
                self.assertEqual(p.assessment_key(self.x.current,self.x.execution_history), binding)

    def test_carried_completion_skips_every_research_dispatch_and_fails_stale(self):
        cell={'status':'complete','successful_complete':True,'manifest':'manifest.json','sha256':'manifesthash','answer_sha256':'answerhash'}
        record={k:cell[k] for k in ('manifest','sha256','answer_sha256')}
        self.x.pilot.config['carried_complete_problems']={self.x.ident:record}
        self.x.pilot.campaign.status.return_value={'problems':{self.x.ident:cell}}
        self.x.main_turn=AsyncMock(side_effect=AssertionError('completed main rerun'))
        result=asyncio.run(self.x.run())
        self.assertEqual(result['status'],'complete')
        self.x.pilot.campaign.claim.assert_not_called();self.x.main_turn.assert_not_awaited()
        self.x.execution.assert_not_awaited()
        cell['successful_complete']=False
        with self.assertRaisesRegex(ValueError,'carried completion'):
            asyncio.run(self.x.run())
