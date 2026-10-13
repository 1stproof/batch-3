"""Native copied-paper handoff preserves frozen evidence and avoids repeated reviews."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import types
import unittest
from unittest.mock import AsyncMock, patch

import test_pilot_paper as fixtures
import pilot_paper as paper
from pilot_exam import rebase_copied_paper_state
from pilot_document_tools import invocation_guidance
from codex_transport import _literal_web_bridge
from paper_writing_codex.raw import raw_errors, candidate_raw_inventory


class Boundary(Exception):
    pass


class RawHandoffTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperTests.setUp
    transport = fixtures.PaperTests.transport

    def stop_after(self, engine, wanted):
        original = engine.advance
        def advance(stage):
            original(stage)
            if stage == wanted:
                raise Boundary(stage)
        return patch.object(engine, 'advance', advance)

    async def pending(self):
        self.problem.pilot.config['internet_browse'] = False
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        with patch.object(paper, 'call_stage', self.transport), self.stop_after(engine, 'raw-audit'):
            with self.assertRaises(Boundary):
                await engine.run()
        return engine

    async def frozen(self, started=False):
        engine = await self.pending()
        if started:
            with patch.object(paper, 'call_stage', self.transport), patch.object(engine, 'advance', side_effect=Boundary('before advance')):
                with self.assertRaises(Boundary):
                    await engine.run()
        else:
            with patch.object(paper, 'call_stage', self.transport), patch.object(paper, 'start_from_raw', side_effect=Boundary('before start')):
                with self.assertRaises(Boundary):
                    await engine.run()
        return engine

    def copied(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        target = Path(temp.name).resolve()/'successor'
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        shutil.copytree(self.root, target)
        rebase_copied_paper_state(self.root, target)
        problem = types.SimpleNamespace(ident='P1', pilot=types.SimpleNamespace(
            root=target, host=target/'host', config=dict(self.problem.pilot.config),
            semaphore=self.problem.pilot.semaphore))
        engine = paper.PaperEngine(problem, target/'snapshot', fixtures.Runtime(target))
        self.assertEqual(before, {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        return engine, before

    async def test_pending_raw_audit_native_copy_finishes_without_reservation_failure(self):
        await self.pending()
        engine, before = self.copied()
        raw = (engine.root/'raw-source.tex').read_bytes()
        with patch.object(paper, 'call_stage', self.transport), self.stop_after(engine, 'draft'):
            with self.assertRaises(Boundary):
                await engine.run()
        self.assertEqual([r[0] for r in self.requests], ['reconstruct','raw-audit'])
        self.assertEqual(engine.output.read_bytes(), raw)
        self.assertEqual(raw_errors(json.loads(engine.state_path.read_text()), required=True,lineage=True), [])
        self.assertEqual(before, {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    async def test_frozen_checkpoint_copy_reuses_audit_without_model_or_refreeze(self):
        await self.frozen()
        engine, before = self.copied()
        state = json.loads(engine.state_path.read_text())
        checkpoint = dict(state['raw_checkpoint'])
        calls = list(engine.ledger['calls'])
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch, patch.object(paper,'freeze_raw') as freeze, self.stop_after(engine,'draft'):
            with self.assertRaises(Boundary):
                await engine.run()
        dispatch.assert_not_awaited();freeze.assert_not_called()
        self.assertEqual(engine.ledger['calls'],calls)
        self.assertEqual(json.loads(engine.state_path.read_text())['raw_checkpoint'],checkpoint)
        self.assertEqual(before,{str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    async def test_started_checkpoint_copy_rebases_seed_and_advances_without_replay(self):
        await self.frozen(started=True)
        engine,before=self.copied()
        state=json.loads(engine.state_path.read_text())
        self.assertEqual(raw_errors(state,required=True,lineage=True),[])
        self.assertTrue(Path(state['raw_lineage']['seed_manifest']).is_relative_to(engine.root))
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch, patch.object(paper,'start_from_raw') as start, self.stop_after(engine,'draft'):
            with self.assertRaises(Boundary):await engine.run()
        dispatch.assert_not_awaited();start.assert_not_called()
        first=candidate_raw_inventory(state)
        engine.output.write_text(engine.output.read_text()+'\n% destination-only edit\n')
        self.assertNotEqual(candidate_raw_inventory(state)['source_sha256'],first['source_sha256'])
        self.assertEqual(before,{str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    async def test_edited_draft_copy_preserves_seed_hashes_and_uses_successor_inventory(self):
        parent = await self.frozen(started=True)
        parent.advance('draft')
        parent.output.write_text(parent.output.read_text() + '\n% saved editorial progress\n')
        old_state = json.loads(parent.state_path.read_text())
        old_seed = json.loads(Path(old_state['raw_lineage']['seed_manifest']).read_text())
        engine, before = self.copied()
        state = json.loads(engine.state_path.read_text())
        seed = json.loads(Path(state['raw_lineage']['seed_manifest']).read_text())
        self.assertEqual(engine.ledger['stage'], 'draft')
        self.assertEqual([item['sha256'] for item in seed['files']], [item['sha256'] for item in old_seed['files']])
        self.assertEqual(engine.output.read_bytes(), parent.output.read_bytes())
        self.assertEqual(raw_errors(state, required=True, lineage=True), [])
        engine.output.write_text(engine.output.read_text() + '\n% new successor edit\n')
        self.assertEqual(candidate_raw_inventory(state)['source_sha256'], hashlib.sha256(engine.output.read_bytes()).hexdigest())
        self.assertEqual(before, {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    async def test_native_rebase_tracks_copied_unreferenced_support_asset(self):
        from test_paper_raw import evidence_fixture
        engine = await self.pending()
        raw = engine.root/'raw-source.tex'
        asset = engine.root/'source-note.txt'
        asset.write_text('Synthetic retained support asset')
        evidence = evidence_fixture(engine.state_path, raw, [asset])
        paper.mark_gate(engine.state_path, 'critical-path', 'pass', [str(evidence)])
        paper.freeze_raw(engine.state_path, raw, 'pre-editorial', evidence, assets=[asset])
        engine.finish_raw_handoff()
        successor, before = self.copied()
        state = json.loads(successor.state_path.read_text())
        seed = json.loads(Path(state['raw_lineage']['seed_manifest']).read_text())
        self.assertEqual(len(seed['assets']), 1)
        copied_asset = Path(seed['assets'][0])
        self.assertTrue(copied_asset.is_relative_to(successor.root))
        initial = candidate_raw_inventory(state)
        copied_asset.write_text('Changed successor support asset')
        self.assertNotEqual(candidate_raw_inventory(state)['source_tree_sha256'], initial['source_tree_sha256'])
        self.assertEqual(before, {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    async def test_rehashed_empty_or_escaping_seed_is_rejected(self):
        engine = await self.frozen(started=True)
        state = json.loads(engine.state_path.read_text())
        seed_path = Path(state['raw_lineage']['seed_manifest'])
        original = json.loads(seed_path.read_text())
        for files in ([], original['files']*2,
                      [*original['files'], {'path':str(self.root/'snapshot/input.txt'), 'sha256':'0'*64}],
                      [*original['files'], {'path':str(engine.root/'../P1/paper.tex'), 'sha256':'0'*64}]):
            with self.subTest(files=files):
                seed_path.write_text(json.dumps({**original,'files':files}))
                state['raw_lineage']['seed_manifest_sha256'] = hashlib.sha256(seed_path.read_bytes()).hexdigest()
                engine.state_path.write_text(json.dumps(state))
                with self.assertRaises(ValueError): self.copied()
        seed_path.write_text(json.dumps({**original,'files':[]}))
        state['raw_lineage']['seed_manifest_sha256'] = hashlib.sha256(seed_path.read_bytes()).hexdigest()
        engine.state_path.write_text(json.dumps(state))
        with self.assertRaisesRegex(paper.PaperRecoveryRequired,'explicit reconciliation'):
            engine.finish_raw_handoff()

    async def test_corrupt_seed_blocks_native_rebase(self):
        engine = await self.frozen(started=True)
        state = json.loads(engine.state_path.read_text())
        Path(state['raw_lineage']['seed_manifest']).write_text('{}')
        with self.assertRaisesRegex(ValueError, 'exact original seed binding'):
            self.copied()

    async def test_changed_candidate_blocks_frozen_handoff_without_overwrite(self):
        engine=await self.frozen()
        engine.output.write_text('unreviewed saved candidate')
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaisesRegex(paper.PaperRecoveryRequired,'unreviewed candidate'):
                await engine.run()
        dispatch.assert_not_awaited()
        self.assertEqual(engine.output.read_text(),'unreviewed saved candidate')

    async def test_changed_raw_checkpoint_blocks_without_model(self):
        engine=await self.frozen()
        state=json.loads(engine.state_path.read_text())
        Path(state['raw_checkpoint']['manifest']).write_text('{}')
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaisesRegex(paper.PaperRecoveryRequired,'manifest hash changed'):
                await engine.run()
        dispatch.assert_not_awaited()

    def test_advertised_bridge_example_matches_actual_strict_validator(self):
        guidance=invocation_guidance('review',public_sources=True)
        example=re.search(r'For example: (text\(await tools\.web__run\(.*?\)\);)',guidance).group(1)
        payload={'type':'custom_tool_call','name':'exec','input':example}
        self.assertTrue(_literal_web_bridge(payload))
        self.assertFalse(_literal_web_bridge({**payload,'input':example.replace('"search_query"','search_query')}))
        self.assertFalse(_literal_web_bridge({**payload,'input':'const r = '+example}))
        self.assertIn('functions.wait',guidance)
        self.assertNotIn('For example: text(await tools.web__run',invocation_guidance('review',public_sources=False))
