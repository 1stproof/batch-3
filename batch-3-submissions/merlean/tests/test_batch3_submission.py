import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import batch3_submission as entry


class SubmissionTests(unittest.TestCase):
    def test_input_rejects_traversal_duplicates_and_empty_text(self):
        for problems in ([{'id': '../a', 'latex': 'x'}],
                         [{'id': 'a', 'latex': 'x'}, {'id': 'a', 'latex': 'y'}],
                         [{'id': 'a', 'latex': ''}]):
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'input.json'
                path.write_text(json.dumps({'problems': problems}))
                with self.assertRaises(ValueError):
                    entry.read_problems(path)

    def test_valid_input_preserves_latex(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.json'
            path.write_text(json.dumps({'problems': [{'id': 'prob-001', 'latex': r'\forall x'}]}))
            self.assertEqual(entry.read_problems(path), {'prob-001': r'\forall x'})

    def test_login_key_is_stdin_only_and_removed_from_environment(self):
        import os
        import subprocess
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENAI_API_KEY': 'test-credential'}, clear=True):
            with patch.object(entry.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)) as call:
                entry.authenticate('/bin/codex', Path(tmp) / 'private')
            self.assertNotIn('OPENAI_API_KEY', os.environ)
            self.assertEqual(os.environ['MERLEAN_CODEX_AUTH'], 'api')
            self.assertNotIn('test-credential', str(call.call_args.args))
            self.assertEqual(call.call_args.kwargs['input'], 'test-credential\n')

    def test_pdf_existence_does_not_imply_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'run-01'
            folder = root / 'exam/papers/p1'
            folder.mkdir(parents=True)
            (folder / 'final.pdf').write_bytes(b'%PDF-draft')
            (folder / 'paper-ledger.json').write_text(json.dumps({'status': 'incomplete', 'stage': 'review'}))
            result = entry.publish(root, Path(tmp), ['p1'])
            self.assertEqual(result['p1']['paper_status'], 'incomplete')
            self.assertEqual(result['p1']['artifacts'], ['solutions/p1/final.pdf'])

    def test_usage_index_includes_operator_evidence_without_fabricating_totals(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            turn = root / 'operations/state/incidents/incident/turn-001'
            turn.mkdir(parents=True)
            for name in ('events.jsonl', 'stage.response-usage.json', 'accounting-receipt.json'):
                (turn / name).write_text('{}')
            entry.usage_index(root)
            value = json.loads((root / 'token-usage-index.json').read_text())
            self.assertEqual(len(value['operations_usage_evidence']), 1)
            self.assertEqual(len(value['operations_accounting_receipts']), 1)
            self.assertIsNone(value['actual_billed_usd'])
            self.assertEqual(value['missing_usage'], 'UNKNOWN')

    def test_light_completion_requires_native_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'run-01'
            folder = root / 'exam/papers/p1'
            folder.mkdir(parents=True)
            (folder / 'light-paper-ledger.json').write_text('{"stage": "complete"}')
            with patch('pilot_paper_light.verify_completed', side_effect=ValueError('incomplete evidence')):
                result = entry.publish(root, Path(tmp), ['p1'])
            self.assertEqual(result['p1']['paper_status'], 'verification_failed')

    def test_clock_is_explicit_and_network_enabled(self):
        start = entry.now()
        with patch.object(entry, 'load', return_value=[]):
            args = entry.command(Path('/tmp/run'), Path('/tmp/problems.json'), '/bin/codex', start)
        self.assertEqual(args[args.index('--exam-research-hours') + 1], '22.75')
        self.assertEqual(args[args.index('--exam-total-hours') + 1], '24')
        self.assertEqual(args[args.index('--exam-start-utc') + 1], start.isoformat())
        self.assertEqual(args[args.index('--internet-browse') + 1], 'on')

    def test_empty_input_no_api_login_and_no_second_attempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.json'
            path.write_text('{"problems": []}')
            output = Path(tmp) / 'output'
            with patch.object(entry, 'authenticate') as login:
                self.assertEqual(entry.run(path, output, '/bin/codex', entry.now()), 0)
                login.assert_not_called()
                with self.assertRaises(FileExistsError):
                    entry.run(path, output, '/bin/codex', entry.now())


if __name__ == '__main__':
    unittest.main()
