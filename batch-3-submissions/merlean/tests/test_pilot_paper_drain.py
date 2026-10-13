import asyncio
import copy
import hashlib
import json
import unittest
from unittest.mock import AsyncMock, patch
import test_pilot_paper as fixture
import pilot_paper as paper
from pilot_drain import DrainRequested

class PaperDrainTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixture.PaperTests.setUp
    def legacy(self):
        e=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        e.ledger.update(stage='draft',writer_session='saved-writer',writer_ids=['saved-writer'],
            retrieval_progress={'stage':'repair-draft','session':'saved-writer','turns':0,'writer':True},
            evidence_requests={},errors=[{'stage':'draft','type':'DrainRequested','message':'paper pipeline preserved at cooperative drain'},
                {'stage':'contextual-repair','type':'DrainRequested','message':'host admission closed; preserve completed work and checkpoint before another launch'}])
        for number,stage,session in [(1,'reconstruct','saved-writer'),(2,'raw-audit','reader')]:
            name=f'P1/paper-{number:03d}-{stage}';p=self.problem.pilot.host/'runtime'/name;p.mkdir(parents=True)
            data={'stage.answer.txt':b'{}','stage.prompt.txt':b'Synthetic bounded task','document-capability.json':b'{}'}
            for file,body in data.items():(p/file).write_bytes(body)
            meta={'name':name,'module':'paper-'+stage,'status':'completed','session_id':session,'model_actual':paper.ASTRA,
                'model_verified':True,'turn_completed':True,'fresh_session':True,'resume_session':None,'request_id':name,
                'answer_sha256':hashlib.sha256(data['stage.answer.txt']).hexdigest(),'prompt_sha256':hashlib.sha256(data['stage.prompt.txt']).hexdigest(),
                'document_capability':{'sha256':hashlib.sha256(data['document-capability.json']).hexdigest()},
                'document_audit':{'required_material_delivered':True},'pid':800000+number,'exit_code':0,
                'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:01:00+00:00'}
            (p/'stage.meta.json').write_text(json.dumps(meta));e.ledger['calls'].append(meta)
            e.ledger.setdefault('admissions',[]).append({'name':name,'stage':stage,'resume_session':None})
        e.save();return paper.PaperEngine(self.problem,self.snapshot,self.runtime)

    async def test_saved_zero_marker_resumes_real_draft_admission_same_writer(self):
        e=self.legacy();before=copy.deepcopy(e.ledger['calls'])
        async def boundary(*args,**kwargs):
            self.assertEqual(kwargs.get('resume',args[5] if len(args)>5 else None),'saved-writer')
            self.assertEqual(e.ledger['retrieval_progress']['turns'],1)
            self.assertEqual(e.ledger['calls'][-1]['name'],'P1/paper-003-draft')
            raise RuntimeError('SYNTHETIC_DISPATCH_BOUNDARY')
        with patch.object(paper,'call_stage',side_effect=boundary):
            with self.assertRaisesRegex(RuntimeError,'SYNTHETIC_DISPATCH_BOUNDARY'):
                await e.call('draft','Draft synthetic input',{},resume='saved-writer',writer=True)
        self.assertEqual(e.ledger['calls'][:2],before)
        self.assertEqual(e.ledger['unadmitted_drain_reconciliations'][0]['turns_consumed'],0)
        self.assertEqual(e.ledger['writer_session'],'saved-writer')

    async def test_prior_retrieval_progress_survives_unadmitted_drain(self):
        e=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        original={'stage':'draft','session':'saved-writer','turns':2,'writer':True};e.ledger['retrieval_progress']=copy.deepcopy(original)
        with patch.object(e,'_call_once',side_effect=DrainRequested('closed')):
            with self.assertRaises(DrainRequested):await e.call('draft','task',{},resume='saved-writer',writer=True)
        self.assertEqual(e.ledger['retrieval_progress'],original)
        e.ledger.pop('retrieval_progress')
        with patch.object(e,'_call_once',side_effect=DrainRequested('closed')):
            with self.assertRaises(DrainRequested):await e.call('draft','task',{},resume='saved-writer',writer=True)
        self.assertNotIn('retrieval_progress',e.ledger)

    async def test_drain_after_admission_does_not_erase_consumed_turn(self):
        e=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        async def admitted(*args,**kwargs):
            e.ledger['retrieval_progress']['turns']+=1
            e.ledger['calls'].append({'name':'P1/paper-001-draft','status':'admitted'})
            e.ledger.setdefault('admissions',[]).append({'name':'P1/paper-001-draft'})
            raise DrainRequested('after admission')
        with patch.object(e,'_call_once',side_effect=admitted):
            with self.assertRaises(DrainRequested):await e.call('draft','task',{},resume='saved-writer',writer=True)
        self.assertEqual(e.ledger['retrieval_progress']['turns'],1)
        self.assertEqual(len(e.ledger['admissions']),1)

    async def test_pipeline_drain_never_invokes_contextual_repair(self):
        with patch.object(paper.PaperEngine,'run',side_effect=DrainRequested('closed')),patch.object(paper.PaperEngine,'repair',new_callable=AsyncMock) as repair:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        repair.assert_not_awaited();self.assertEqual(result['status'],'interrupted')

    async def test_ambiguous_admission_and_writer_tamper_fail_closed(self):
        for kind in ('admission','transport','writer','session','turns','requests'):
            with self.subTest(kind=kind):
                # Independent fixture namespaces keep each negative case isolated.
                other=PaperDrainTests('test_pipeline_drain_never_invokes_contextual_repair');other.setUp()
                try:
                    e=other.legacy()
                    if kind=='admission':e.ledger['admissions'].append({'name':'P1/paper-003-repair-draft','stage':'repair-draft'})
                    elif kind=='transport':(other.problem.pilot.host/'runtime/P1/paper-003-repair-draft').mkdir()
                    elif kind=='writer':(other.problem.pilot.host/'runtime/P1/paper-001-reconstruct/stage.answer.txt').write_text('changed')
                    elif kind=='session':e.ledger['writer_session']='different-writer'
                    elif kind=='turns':e.ledger['retrieval_progress']['turns']=1
                    else:e.ledger['evidence_requests']={'draft':['input.txt']}
                    pending=copy.deepcopy(e.ledger['retrieval_progress'])
                    with self.assertRaises(paper.PaperRecoveryRequired):e.restore_retrieval('draft',writer=True)
                    self.assertEqual(e.ledger['retrieval_progress'],pending)
                finally:other.temp.cleanup()

