"""The shared editorial contract reaches real dispatches without filtering evidence."""
import json
import hashlib
from pathlib import Path
import shutil
import subprocess
import unittest
from unittest.mock import patch

import test_pilot_paper as fixtures
import pilot_paper as paper


class EditorialContractTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperTests.setUp
    transport = fixtures.PaperTests.transport

    def assert_editorial_contract(self, prompt):
        instruction = prompt.split('\nTASK:\n', 1)[0]
        contract = (paper.REPO / paper.READER_FACING_POLICY).read_text()
        self.assertEqual(instruction.count(contract), 1)
        for required in (
            'final TeX/PDF for an external mathematical reader',
            'unresolved proof gaps, counterexamples, dependencies and known credit',
            'compares mathematical content and qualifications, not verbatim',
            'not a keyword ban or an automatic text filter',
            'change of representation or quotient',
            'never invent a missing justification',
            'Every newly authored figure must use LaTeX `tikzpicture`',
            'no figure\nis required in every paper',
            'never replaces\nits proof',
            'BibTeX metadata is not content validation',
            'compare the final typeset bibliography entry',
            'No arbitrary shortening target',
            'Use tools only to resolve a concrete need',
            'metadata or hashes alone do not validate a cited claim',
        ):
            self.assertIn(required, instruction)

    async def test_actual_reconstruction_fidelity_and_draft_dispatch_preserve_raw(self):
        before = {p.name: p.read_bytes() for p in self.snapshot.iterdir()}
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        with patch.object(paper, 'call_stage', side_effect=self.transport), patch.object(
                engine, 'compile', side_effect=RuntimeError('stop before compiler')):
            with self.assertRaisesRegex(RuntimeError, 'stop before compiler'):
                await engine.run()
        self.assertEqual([r[0] for r in self.requests], ['reconstruct', 'raw-audit', 'draft'])
        for stage, prompt, _, kw in self.requests:
            self.assert_editorial_contract(prompt)
            self.assertTrue(kw['internet_browse'])
            self.assertIn('fetch_public_source', prompt)
            self.assertIn('document_scope', kw)
            if stage == 'raw-audit':
                self.assertIn('workflow status in the evidence records', prompt)
                self.assertIn('Do not require final publication prose', prompt)
        self.assertEqual((engine.root / 'raw-source.tex').read_text(), self.tex)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.snapshot.iterdir()})
        self.assertFalse(engine.ledger['research_acceptance_changed'])

    async def test_fresh_readers_receive_neutral_rubric_and_revision_receives_author_policy(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.output.write_text(self.tex)
        engine.ledger.update(stage='reader-1', writer_session='writer', writer_ids=['writer'])
        with patch.object(paper, 'call_stage', side_effect=self.transport), patch.object(
                engine, 'compile', side_effect=RuntimeError('stop after readers')):
            with self.assertRaisesRegex(RuntimeError, 'stop after readers'):
                await engine.run()
        self.assertEqual([r[0] for r in self.requests],
                         ['reader-1', 'revise-1', 'reader-2', 'revise-2', 'verify-2'])
        for stage, prompt, resume, kw in self.requests:
            if stage.startswith('revise-'):
                self.assert_editorial_contract(prompt)
            else:
                instruction = prompt.split('\nTASK:\n', 1)[0]
                self.assertIn(paper.READER_RUBRIC, instruction)
                self.assertNotIn((paper.REPO / paper.READER_FACING_POLICY).read_text(), instruction)
                self.assertNotIn('The exam is ten problems', instruction)
            self.assertEqual(kw['internet_browse'], stage.startswith('revise-'))
            if stage.startswith('reader-'):
                payload = json.loads(prompt.split('\nINPUT:\n', 1)[1])
                self.assertEqual(set(payload), {'manuscript', 'guideline'})
                self.assertNotIn('ESSENTIAL_RESEARCH_GAP', prompt)
                self.assertIsNone(resume)

    async def test_polish_proof_audit_and_repair_use_same_contract(self):
        # Exercise assembly at the transport boundary for stages with differing
        # payload delivery, including repairs and an existing saved guideline.
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        old_guideline = engine.guideline.read_bytes()
        for stage in ('polish', 'proof-audit', 'repair-polish'):
            with self.subTest(stage=stage), patch.object(paper, 'call_stage', side_effect=self.transport):
                await engine.call(stage, 'Review the supplied material.', {'manuscript': self.tex},
                                  writer=stage != 'proof-audit')
            self.assert_editorial_contract(self.requests[-1][1])
        self.assertEqual(engine.guideline.read_bytes(), old_guideline)

    async def test_explicit_offline_config_never_grants_public_retrieval(self):
        self.problem.pilot.config['internet_browse'] = False
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        with patch.object(paper, 'call_stage', side_effect=self.transport):
            await engine.call('draft', 'Prepare the mathematical draft.', {'manuscript': self.tex}, writer=True)
        _, prompt, _, kw = self.requests[-1]
        self.assertFalse(kw['internet_browse'])
        self.assertIn('Public retrieval is disabled for this stage', prompt)
        self.assertNotIn('Public search and source downloads are available', prompt)

    def source_snapshot(self, *, binary):
        import pilot_public_sources as sources
        body = b'\x1f\x8bsynthetic source archive' if binary else b'Exact exported BibTeX or TeX source.'
        content = b'For every finite set, under the stated hypothesis, the claim follows.'
        def worker(url, folder):
            (folder/'raw').write_bytes(body)
            member = 'source.txt' if binary else 'raw'
            if binary: (folder/member).write_bytes(content)
            text = content if binary else body
            return {'final_url': url, 'content_type': 'application/octet-stream',
                    'raw_sha256': sources.digest(body), 'members': [
                {'member': member, 'sha256': sources.digest(text), 'characters': len(text), 'bytes': len(text)}]}
        with patch.object(sources, '_run_worker', side_effect=worker):
            receipt = sources.fetch_public_source(self.snapshot/'evidence/public-sources', 'https://example.org/source')
        manifest = {p.relative_to(self.snapshot).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in self.snapshot.rglob('*') if p.is_file() and p.name != 'manifest.json'}
        (self.snapshot/'manifest.json').write_text(json.dumps({'schema_version': 1, 'files': manifest}))
        return receipt

    def test_public_source_handoff_preserves_bytes_and_requires_actual_extracted_text(self):
        receipt = self.source_snapshot(binary=True)
        original = {p.relative_to(self.snapshot).as_posix(): p.read_bytes()
                    for p in self.snapshot.rglob('*') if p.is_file()}
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        _, scope = engine.scoped_payload('proof-audit', {'source': {
            'path': receipt['source_path'], 'sha256': receipt['raw_sha256']}})
        prefix = 'archive:evidence/public-sources/' + receipt['source_id'] + '/'
        self.assertIn(prefix+'source.txt', scope['required_artifact_ids'])
        provenance = json.loads(Path(scope['readonly_artifacts'][prefix+'raw']['path']).read_text())
        self.assertEqual(provenance['sha256'], receipt['raw_sha256'])
        self.assertEqual(provenance['required_source_text_ids'], [prefix+'source.txt'])
        self.assertEqual(engine.context()['public_sources'][0]['source_id'], receipt['source_id'])
        self.assertEqual(original, {p.relative_to(self.snapshot).as_posix(): p.read_bytes()
                                   for p in self.snapshot.rglob('*') if p.is_file()})

    def test_plain_source_raw_is_exact_text_not_provenance_substitution(self):
        receipt = self.source_snapshot(binary=False)
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        _, scope = engine.scoped_payload('proof-audit', {'source': {
            'path': receipt['source_path'], 'sha256': receipt['raw_sha256']}})
        ident = 'archive:evidence/public-sources/' + receipt['source_id'] + '/raw'
        artifact = scope['readonly_artifacts'][ident]
        self.assertEqual(artifact['sha256'], receipt['raw_sha256'])
        self.assertEqual(Path(artifact['path']).read_bytes(), Path(receipt['source_path']).read_bytes())

    def test_mutated_source_snapshot_cannot_seed_public_cache(self):
        receipt = self.source_snapshot(binary=True)
        Path(receipt['source_path']).write_bytes(b'changed source after snapshot')
        with self.assertRaisesRegex(ValueError, 'immutable research snapshot contents changed'):
            paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        self.assertFalse((self.runtime.paper_dir('P1')/'public-sources').exists())

    def test_no_keyword_filter_or_mathematical_rewrite(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        tex = r'''\documentclass{article}
\usepackage{tikz}
\begin{document}
For every finite set $X$, assume the controller is injective. Its hash function
has acceptance probability $p$. The gold standard comparison uses this hypothesis.
Without injectivity the claimed bound is unproved; the two-point constant map
is a counterexample. The conclusion depends on Lemma 2 and credits its author.
\begin{tikzpicture}\node (x) {$X$};\node[right of=x] (y) {$Y$};
\draw[->] (x) -- node[above] {$f$} (y);\end{tikzpicture}
\end{document}'''
        raw = engine.root / 'raw-source.tex'
        raw.write_text('Historical SILVER/GOLD controller ticket audit session hash.\n' + tex)
        before = raw.read_bytes()
        engine.writer_result({'tex': tex, 'artifacts': {
            '01-critical-path.md': 'Historical SILVER/GOLD controller ticket audit session hash.'}})
        self.assertEqual(engine.output.read_text(), tex)
        self.assertEqual(raw.read_bytes(), before)
        self.assertIn('SILVER/GOLD', (engine.work / '01-critical-path.md').read_text())
        self.assertFalse(engine.ledger['research_acceptance_changed'])

    def test_shared_entrypoints_resolve_contract_and_keep_source_standard(self):
        for name in ('paper-writing.md', 'paper-compose.md', 'paper-claude-protocol.md',
                     'paper-audit.md', 'paper/protocol.md', 'paper/mathematical-writing.md',
                     'paper/raw-checkpoint.md', 'paper/refinement.md',
                     'paper/audit-checklist.md', 'paper/reader-proof-quality.md'):
            self.assertIn('reader-facing-paper.md', (paper.REPO / 'workflows' / name).read_text())
        references = (paper.REPO / 'workflows/paper/references.md').read_text()
        for required in ('Download the complete source archive', 'inspect the actual TeX',
                         'Save that block verbatim', 'does not grant network',
                         'Preserve established credit'):
            self.assertIn(required, references)

    def test_unresolved_fallback_states_mathematical_limitation(self):
        tex = paper.baseline_tex('P1')
        self.assertIn('Unresolved answer', tex)
        self.assertIn('supplies no proof', tex)
        for process_claim in ('grade', 'audit', 'SILVER', 'GOLD', 'accepted'):
            self.assertNotIn(process_claim, tex)

    @unittest.skipUnless(shutil.which('pdflatex') and shutil.which('kpsewhich'), 'LaTeX unavailable')
    def test_literal_tikz_figure_compiles_through_existing_pipeline(self):
        if subprocess.run(['kpsewhich', 'tikz.sty'], capture_output=True).returncode:
            self.skipTest('TikZ unavailable')
        from paper_writing_codex.cli import _compile_tex
        tex = r'''\documentclass[11pt]{article}
\usepackage{tikz}
\begin{document}
Let $f:X\to Y$ be a map. The arrow records its domain and codomain.
\begin{figure}[h]\centering
\begin{tikzpicture}\node (x) at (0,0) {$X$};\node (y) at (2,0) {$Y$};
\draw[->] (x) -- node[above] {$f$} (y);\end{tikzpicture}
\caption{Domain and codomain of the stated map.}\end{figure}
\end{document}'''
        source = self.root/'figure.tex'; source.write_text(paper._validate_tex(tex))
        report = _compile_tex(source, 60)
        self.assertTrue(report['pass'], report)
        self.assertEqual(report['pdf_pages'], 1)
