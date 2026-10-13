"""Readable history is reconstructible evidence, never research authority."""
import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_working_log as log
import codex_pilot as pilot


class WorkingLogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'parent'
        self.root.mkdir()
        self.work = {'objective': 'Resolve the remaining implication', 'approach': 'Try the finite case',
            'work_performed': 'Derived the finite reduction', 'result': 'Infinite case remains a hypothesis',
            'failed_approaches': ['Direct compactness did not close the gap'], 'next_step': 'Test the extension step'}

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
        return path

    def evidence(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in self.root.rglob('*') if path.is_file() and path.name != 'working-log.md'}

    def test_resume_reconstructs_sequence_and_lessons_without_modifying_sources(self):
        self.write('host-progress.json', {'phase': 'partial-checkpoint', 'calls': [],
            'open_findings': [{'id': 'gap-1', 'description': 'Infinite case unresolved'}]})
        for step in (10, 2):
            self.write(f'research-continuation-{step:05d}.json', {'step': step,
                'reason': 'no_action_checkpoint', 'mode': 'obstruction_analysis',
                'last_research_work': self.work, 'bindings': {'candidate_sha256': 'a' * 64},
                'previous_receipt': {'path': 'earlier.json', 'sha256': 'b' * 64}})
        for name in ('proof.md', 'notes.md', 'ledger.md', 'failure-log.md'):
            (self.root / name).write_text('Original authored ' + name + '\n')
        self.write('current-candidate.json', {'proof_markdown': 'authored proof', 'ledger': {'rows': []}})
        original = self.evidence()
        self.assertEqual(log.refresh(self.root)['status'], 'updated')
        first = (self.root / 'working-log.md').read_bytes()
        text = first.decode()
        self.assertLess(text.index('### research-continuation-00002'), text.index('### research-continuation-00010'))
        self.assertIn(self.work['failed_approaches'][0], text)
        self.assertIn(self.work['next_step'], text)
        self.assertIn('not supplied by this record', text)
        self.assertIn('Reconstructed from durable records', text)
        self.assertIn('[failure-log.md](failure-log.md)', text)
        self.assertEqual(self.evidence(), original)
        self.assertEqual(log.refresh(self.root)['status'], 'unchanged')
        child = Path(self.tmp.name) / 'continued'
        shutil.copytree(self.root, child)
        (child / 'working-log.md').unlink()
        self.assertEqual(log.refresh(child)['status'], 'updated')
        self.assertEqual((child / 'working-log.md').read_bytes(), first)
        child_record = json.loads((child / 'host-progress.json').read_text())
        child_record['phase'] = 'restored-existing-main'
        (child / 'host-progress.json').write_text(json.dumps(child_record))
        self.assertEqual(log.refresh(child)['status'], 'updated')
        self.assertIn('restored-existing-main', (child / 'working-log.md').read_text())
        self.assertEqual(self.evidence(), original)

    def test_incomplete_failed_and_successful_outcomes_keep_their_distinctions(self):
        calls = [{'name': f'p/{n:03d}-main-repair', 'status': status, 'module': 'main-repair',
                  'end_utc': f'2026-01-01T00:0{n}:00Z', 'answer_sha256': str(n) * 64}
                 for n, status in ((1, 'timeout_censored'), (2, 'process_failed'), (3, 'completed'))]
        progress = {'phase': 'complete-with-current-scope-proof-silver-evidence', 'calls': calls,
            'errors': [{'type': 'StageFailure', 'error': 'connection lost', 'stage': calls[1]['name']}],
            'open_findings': [], 'final_assessment_history': [
                {'status': 'commissioned', 'candidate_sha256': 'c' * 64, 'attempts': 1},
                {'status': 'completed', 'candidate_sha256': 'c' * 64,
                 'final_validation': {'successful_complete': True, 'manifest': {'path': 'final-manifest.json', 'sha256': 'd' * 64}}}]}
        path = self.write('host-progress.json', progress)
        self.write('003-main-repair.json', {'response_type': 'candidate_update', 'proof_markdown': 'PRIVATE_PROOF_BODY'})
        self.write('probes/main-2-lean/result.json', {'status': 'failed', 'stderr': 'FULL_DIAGNOSTICS'})
        self.write('main-2-invalid-contract.json', {'error': 'malformed response', 'acceptance_authority': False})
        self.write('proof-current.json', {'revision': 'r00000001-test', 'manifest_sha256': 'e' * 64})
        self.write('proof-revisions/r00000001-test/manifest.json', {'revision': 'r00000001-test',
            'created_utc': '2026-01-01T00:03:00Z', 'status': 'submitted', 'files': {'proof.md': 'f' * 64}})
        original = self.evidence()
        self.assertEqual(log.refresh(self.root)['status'], 'updated')
        output = (self.root / 'working-log.md').read_text()
        for phrase in ('timeout_censored', 'process_failed', 'connection lost', 'commissioned',
                       'successful_complete', 'final-manifest.json', 'r00000001-test', 'malformed response'):
            self.assertIn(phrase, output)
        self.assertIn(hashlib.sha256(path.read_bytes()).hexdigest(), output)
        self.assertIn('/calls/0', output)
        self.assertIn('Transport completion is not mathematical success', output)
        self.assertIn('host reports, not revalidation', output)
        self.assertNotIn('PRIVATE_PROOF_BODY', output)
        self.assertNotIn('FULL_DIAGNOSTICS', output)
        self.assertEqual(self.evidence(), original)
        self.assertEqual(json.loads(path.read_text()), progress)

    def test_nested_histories_do_not_expand_projection(self):
        record = {'step': 1, 'last_research_work': self.work,
                  'feedback': {'prior_feedback': 'NESTED_PRIVATE_HISTORY' * 1000}}
        self.write('research-continuation-00001.json', record)
        before = log.render(self.root)
        for _ in range(10):
            record['feedback'] = {'prior_feedback': copy.deepcopy(record['feedback'])}
        self.write('research-continuation-00001.json', record)
        after = log.render(self.root)
        self.assertEqual(len(before), len(after))
        self.assertNotIn('NESTED_PRIVATE_HISTORY', after)

    def test_malformed_legacy_and_missing_records_are_observable_nonfatal(self):
        self.write('host-progress.json', {'phase': 'legacy', 'calls': None, 'open_findings': [None], 'errors': 'bad'})
        self.write('main-1-checkpoint.json', ['legacy'])
        self.write('research-continuation-00001.json', {'last_research_work': None})
        (self.root / 'research-continuation-00002.json').write_bytes(b'\xffinvalid')
        self.assertEqual(log.refresh(self.root)['status'], 'updated')
        text = (self.root / 'working-log.md').read_text()
        self.assertIn('malformed JSON', text)
        self.assertIn('Malformed `calls`', text)
        self.assertIn('Legacy or malformed non-object', text)
        self.assertIn('no regular authored file present', text)
        with patch.object(log.os, 'replace', side_effect=OSError('test disk failure')):
            self.write('host-progress.json', {'phase': 'changed'})
            outcome = log.refresh(self.root)
        self.assertEqual(outcome['status'], 'failed')
        self.assertIn('test disk failure', outcome['reason'])
        self.assertEqual((self.root / 'working-log.md').read_text(), text)
        self.assertEqual(list(self.root.glob('.working-log-*')), [])

    def test_preserves_authored_log_and_refuses_symlink_reads_and_writes(self):
        target = self.root / 'working-log.md'
        target.write_text('Human history')
        self.assertEqual(log.refresh(self.root)['status'], 'skipped')
        self.assertEqual(target.read_text(), 'Human history')
        target.unlink()
        outside = Path(self.tmp.name) / 'outside'
        outside.write_text('private untouched evidence')
        target.symlink_to(outside)
        self.assertEqual(log.refresh(self.root)['status'], 'skipped')
        target.unlink()
        (self.root / 'main-1-checkpoint.json').symlink_to(outside)
        self.assertEqual(log.refresh(self.root)['status'], 'updated')
        text = target.read_text()
        self.assertIn('Source skipped: symbolic link', text)
        self.assertNotIn('private untouched evidence', text)
        self.assertEqual(outside.read_text(), 'private untouched evidence')

    def test_real_host_status_creates_updates_and_reports_failure_without_scientific_mutation(self):
        folder = self.root / 'campaign' / 'problems' / 'synthetic'
        folder.mkdir(parents=True)
        (folder / 'input.txt').write_text('Synthetic test statement\n')
        host = SimpleNamespace(root=self.root, deadline=None)
        problem = pilot.Problem(host, 'synthetic')
        problem.current = {'proof_markdown': 'Preserved authored proof', 'ledger': {'rows': []}}
        problem.findings = [{'id': 'open', 'description': 'Extension step unresolved'}]
        problem.errors = [{'type': 'StageFailure', 'error': 'earlier timeout'}]
        problem.calls = [{'name': 'synthetic/001-main-repair', 'status': 'timeout_censored'}]
        pilot.write(folder / 'proof.md', problem.current['proof_markdown'])
        pilot.write(folder / 'current-candidate.json', problem.current)
        pilot.write(self.root / 'campaign/state.json', {'problems': {'synthetic': {'status': 'partial'}}})
        saved = {path: path.read_bytes() for path in (folder / 'proof.md', folder / 'current-candidate.json',
                                                     self.root / 'campaign/state.json')}
        scientific = copy.deepcopy((problem.current, problem.findings, problem.errors))
        with redirect_stdout(io.StringIO()), patch.object(pilot, 'call_stage', side_effect=AssertionError('no dispatch permitted')):
            problem.status('partial-checkpoint')
            self.assertEqual(problem.working_log_status['status'], 'updated')
            self.assertIn('earlier timeout', (folder / 'working-log.md').read_text())
            pilot.write(folder / 'research-continuation-00001.json', {'step': 1,
                'reason': 'no_action_checkpoint', 'last_research_work': self.work})
            problem.status('restored-existing-main')
            resumed = (folder / 'working-log.md').read_text()
            self.assertIn('restored-existing-main', resumed)
            self.assertIn(self.work['next_step'], resumed)
            self.assertEqual((problem.current, problem.findings, problem.errors), scientific)
            self.assertEqual({path: path.read_bytes() for path in saved}, saved)
            output = io.StringIO()
            with redirect_stdout(output), patch.object(log, 'render', side_effect=OSError('synthetic view failure')):
                problem.status('continuing-main-research')
            self.assertEqual(problem.working_log_status['status'], 'failed')
            self.assertIn('synthetic view failure', output.getvalue())
            self.assertIn('working_log', output.getvalue())
            self.assertEqual((folder / 'working-log.md').read_text(), resumed)
            self.assertEqual(json.loads((folder / 'host-progress.json').read_text())['phase'], 'continuing-main-research')
            self.assertEqual((problem.current, problem.findings, problem.errors), scientific)
            self.assertEqual({path: path.read_bytes() for path in saved}, saved)


if __name__ == '__main__':
    unittest.main()
