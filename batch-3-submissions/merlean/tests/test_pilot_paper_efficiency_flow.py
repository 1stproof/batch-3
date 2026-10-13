"""Native paper control-flow tests; model answers are synthetic, never approval evidence."""
import copy
import hashlib
import json
import unittest
from unittest.mock import patch
import test_pilot_paper as fixtures
import pilot_paper as paper


class BoundaryReached(BaseException):
    pass


class EfficiencyFlowTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperTests.setUp
    transport = fixtures.PaperTests.transport

    def engine_at(self, stage):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.ledger.update(stage=stage, writer_session='original-writer', writer_ids=['original-writer'])
        engine.ledger.pop('literature_contract', None)
        engine.ledger.pop('reference_cache', None)
        engine.output.write_text(self.tex)
        (engine.root/'raw-source.tex').write_text(self.tex)
        engine.save()
        return engine

    async def exercise_failure(self, persistent):
        engine = self.engine_at('proof-audit')
        calls = []
        audits = []
        async def transport(*args, **kwargs):
            stage = kwargs['module'].removeprefix('paper-')
            calls.append((stage, args[5]))
            if stage == 'finalize-ledgers':
                raise BoundaryReached()
            meta, answer = await self.transport(*args, **kwargs)
            if stage == 'proof-audit':
                verdict = 'FAIL' if persistent or not audits else 'PASS'
                answer = {'reader_sidecar': {'verdict': verdict, 'findings': 'Synthetic undefined term requires an author explanation.'}}
            elif stage == 'repair-proof-audit':
                answer = {'artifacts': {'07-terminology.md': 'Synthetic author definition correction number '+str(len(calls))},
                          'revision_summary': 'The author clarified the specific term identified by the independent reviewer.'}
            return meta, answer
        # Review semantics are fixture inputs. The native loop, calls, admissions,
        # repair cap, stage transitions and independent-session choices are real.
        def store(current, identity, answer):
            audits.append(identity)
            paper._write(current.work/'07-reader-audit.json', answer['reader_sidecar'])
        with patch.object(paper, 'call_stage', side_effect=transport), patch.object(paper.PaperEngine, 'store_audits', store), patch.object(paper, 'candidate_raw_inventory', return_value={}):
            if persistent:
                result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
            else:
                with self.assertRaises(BoundaryReached):
                    await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
                result = paper._json(engine.ledger_path)
        return result, calls, audits

    async def test_independent_fail_repairs_before_fresh_full_audit_and_finalization(self):
        result, calls, audits = await self.exercise_failure(False)
        self.assertEqual([s for s, _ in calls], ['proof-audit', 'repair-proof-audit', 'proof-audit', 'finalize-ledgers'])
        self.assertEqual(calls[1][1], 'original-writer')
        self.assertIsNone(calls[0][1]); self.assertIsNone(calls[2][1])
        self.assertEqual(len(set(audits)), 2)
        self.assertEqual(len(result['repairs']), 1)
        self.assertTrue(any('reader-sidecar' in e['message'] for e in result['errors']))
        self.assertFalse(result['polishing_complete'])

    async def test_repeated_fail_keeps_existing_four_repair_cap(self):
        result, calls, audits = await self.exercise_failure(True)
        self.assertEqual(sum(s == 'repair-proof-audit' for s, _ in calls), 4)
        self.assertEqual(len(audits), 5)
        self.assertEqual(len(set(audits)), 5)
        self.assertNotIn('finalize-ledgers', [s for s, _ in calls])
        self.assertEqual(len(result['repairs']), 4)
        self.assertEqual(result['stage'], 'proof-audit')
        self.assertFalse(result['polishing_complete'])

    async def test_two_noop_rounds_keep_exact_file_and_real_verification(self):
        engine = self.engine_at('reader-1')
        before = engine.output.read_bytes(); inode = engine.output.stat().st_ino
        calls = []
        async def transport(*args, **kwargs):
            stage = kwargs['module'].removeprefix('paper-')
            calls.append((stage, args[5]))
            meta, answer = await self.transport(*args, **kwargs)
            if stage.startswith('revise-'):
                answer.pop('tex')
                answer['unchanged_manuscript_sha256'] = hashlib.sha256(before).hexdigest()
            return meta, answer
        async def stop_compile(*args, **kwargs):
            raise BoundaryReached()
        with patch.object(paper, 'call_stage', side_effect=transport), patch.object(paper.PaperEngine, 'compile', stop_compile):
            with self.assertRaises(BoundaryReached):
                await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertEqual([s for s, _ in calls], ['reader-1','revise-1','reader-2','revise-2','verify-2'])
        self.assertEqual(engine.output.read_bytes(), before)
        self.assertEqual(engine.output.stat().st_ino, inode)
        rounds = paper._json(engine.work/'08-reader-rounds.json')
        self.assertEqual(len(rounds['rounds']), 2)
        self.assertNotEqual(rounds['rounds'][0]['reader_id'], rounds['rounds'][1]['reader_id'])
        self.assertEqual(calls[-1][1], rounds['rounds'][1]['reader_id'])
        self.assertEqual(paper.reader_round_errors(paper._json(engine.state_path), required=True), [])
        self.assertEqual(paper._json(engine.ledger_path)['stage'], 'final-compile')

    async def test_completed_correction_without_checkpoint_is_not_redispatched(self):
        engine = self.engine_at('proof-audit')
        name = 'P1/paper-001-repair-proof-audit'
        directory = self.problem.pilot.host/'runtime'/name
        directory.mkdir(parents=True)
        meta = {'name':name,'module':'paper-repair-proof-audit','status':'completed','pid':800001,'exit_code':0,
                'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00',
                'session_id':'original-writer','answer_sha256':'1'*64}
        paper._write(directory/'stage.meta.json',meta)
        engine.ledger['calls']=[{'name':name,'status':'admitted','stage':'repair-proof-audit'}]
        engine.ledger['retrieval_progress']={'stage':'repair-proof-audit','session':'original-writer','turns':1,'writer':True}
        engine.ledger['errors']=[{'stage':'proof-audit','type':'ValueError','message':'Synthetic independent reader finding retained.'}]
        engine.save(); before=copy.deepcopy(engine.ledger['calls'])
        with patch.object(paper, 'call_stage', side_effect=AssertionError('must not redispatch')) as dispatch:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        dispatch.assert_not_called()
        self.assertEqual(result['calls'],before)
        self.assertEqual(result['retrieval_progress']['turns'],1)
        self.assertFalse(result['polishing_complete'])
        self.assertTrue(any(e['type']=='PaperRecoveryRequired' for e in result['errors']))

    async def test_interrupted_unreconciled_repair_admission_never_redispatches(self):
        engine = self.engine_at('proof-audit')
        engine.ledger['calls']=[{'name':'P1/paper-001-repair-proof-audit','status':'admitted','stage':'repair-proof-audit'}]
        engine.ledger['retrieval_progress']={'stage':'repair-proof-audit','session':'original-writer','turns':1,'writer':True}
        engine.ledger['errors']=[{'stage':'proof-audit','type':'ValueError','message':'Synthetic independent finding must remain unresolved.'}]
        engine.save()
        with patch.object(paper,'call_stage',side_effect=AssertionError('unreconciled admission cannot dispatch')) as dispatch:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        dispatch.assert_not_called()
        self.assertEqual(result['retrieval_progress']['turns'],1)
        self.assertEqual(result['calls'],engine.ledger['calls'])
        self.assertFalse(result['polishing_complete'])
        self.assertTrue(any(e['type']=='PaperRecoveryRequired' for e in result['errors']))
