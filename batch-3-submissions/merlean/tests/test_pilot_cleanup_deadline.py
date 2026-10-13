"""Expected paper cleanup expiry is not a new paid diagnostic opportunity."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import unittest
from unittest.mock import patch

import test_pilot_terminal_attention as fixtures
import pilot_supervisor as outer


class CleanupDeadlineTests(unittest.TestCase):
    setUp = fixtures.AttentionTests.setUp
    observe = fixtures.AttentionTests.observe

    def fixture(self, seconds_before=14):
        deadline = datetime.now(timezone.utc) - timedelta(seconds=1)
        self.config['exam'].update(submission_deadline_utc=deadline.isoformat(), cleanup_guard_seconds=15)
        outer.save(self.root/'host-config.json', self.config)
        folder = self.root/'exam/papers/p'; folder.mkdir(parents=True, exist_ok=True)
        paper = {'status': 'deadline-partial', 'terminal': True, 'polishing_complete': False,
                 'operational_failure': 'timeout'}
        self.rows = [{'problem': 'p', 'status': 'partial', 'paper': paper}]
        self.ended = (deadline-timedelta(seconds=seconds_before)).isoformat()
        outer.save(folder/'result.json', paper)
        outer.save(folder/'handoff.json', {'submission_deadline_utc': deadline.isoformat()})
        self.write_result()
        return folder

    def write_result(self):
        outer.save(self.root/'pilot-result.json', {'end_utc': self.ended, 'results': self.rows})

    def test_cleanup_expiry_preserves_incomplete_issues_without_diagnosis_even_if_quiescent(self):
        self.fixture()
        report = self.observe()
        self.assertEqual(report['status'], 'deadline_reached')
        self.assertEqual({i['kind'] for i in report['issues']}, {'research_incomplete', 'paper_incomplete'})
        self.assertTrue(report['needs_attention'])
        outer.save(self.state/'keeper-plan.json', {'diagnose_on_failure': True})
        with patch.object(outer, 'watch', return_value=report), patch.object(
                outer, 'diagnostic_quiescence', return_value=None) as guard, patch.object(outer, 'diagnose') as diagnose:
            self.assertEqual(outer.keep(self.state)['status'], 'deadline_reached')
        guard.assert_not_called(); diagnose.assert_not_called()

    def test_boundary_is_strict_and_early_stop_stays_actionable(self):
        for before, expected in [(16, 'paper_incomplete'), (16.001, 'paper_incomplete'),
                                 (15.999, 'deadline_reached'), (1, 'deadline_reached')]:
            with self.subTest(before=before):
                self.fixture(before)
                self.assertEqual(self.observe()['status'], expected)

    def test_receipt_handoff_and_terminal_state_must_match(self):
        for defect in ('missing', 'different', 'handoff', 'symlink', 'nonterminal', 'not_deadline'):
            with self.subTest(defect=defect):
                folder = self.fixture()
                receipt = folder/'result.json'
                if defect == 'missing': receipt.unlink()
                if defect == 'different': outer.save(receipt, {**self.rows[0]['paper'], 'extra': 'unbound'})
                if defect == 'handoff': outer.save(folder/'handoff.json', {'submission_deadline_utc': self.since})
                if defect == 'symlink':
                    target = self.base/'receipt.json'; target.write_bytes(receipt.read_bytes())
                    receipt.unlink(); receipt.symlink_to(target)
                if defect in ('nonterminal', 'not_deadline'):
                    self.rows[0]['paper'].update({'terminal': False} if defect == 'nonterminal' else {'status': 'incomplete'})
                    outer.save(receipt, self.rows[0]['paper']); self.write_result()
                self.assertEqual(self.observe()['status'], 'paper_incomplete')
                if receipt.is_symlink(): receipt.unlink()

    def test_invalid_guards_and_real_failures_cannot_be_masked(self):
        for guard in (False, 0, -1, '15', float('inf'), float('nan'), 1e300):
            self.fixture(); self.config['exam']['cleanup_guard_seconds'] = guard
            outer.save(self.root/'host-config.json', self.config)
            self.assertEqual(self.observe()['status'], 'paper_incomplete')
        for where, failure, expected in [('paper', 'infrastructure', 'infrastructure_failed'),
                                         ('paper', 'delivery', 'paper_incomplete'),
                                         ('row', 'infrastructure', 'infrastructure_failed')]:
            folder = self.fixture()
            (self.rows[0]['paper'] if where == 'paper' else self.rows[0])['operational_failure'] = failure
            outer.save(folder/'result.json', self.rows[0]['paper']); self.write_result()
            self.assertEqual(self.observe()['status'], expected)

    def test_running_owner_remains_running_at_cleanup_boundary(self):
        self.fixture()
        self.assertEqual(self.observe(alive=True, code=None)['status'], 'running')

    def test_nonzero_host_exit_before_hard_deadline_still_signals_infrastructure_failure(self):
        self.fixture()
        self.assertEqual(self.observe(code=0)['status'], 'deadline_reached')
        self.assertEqual(self.observe(code=1)['status'], 'infrastructure_failed')
        self.ended = self.config['exam']['submission_deadline_utc']; self.write_result()
        self.assertEqual(self.observe(code=1)['status'], 'deadline_reached')

    def test_polished_sibling_requires_its_real_deliverables(self):
        self.fixture()
        self.config['problems'].append('q'); outer.save(self.root/'host-config.json', self.config)
        folder = self.root/'exam/papers/q'; folder.mkdir(parents=True)
        (folder/'paper.tex').write_text('synthetic paper')
        (folder/'final.pdf').write_bytes(b'%PDF-synthetic')
        self.rows.append({'problem': 'q', 'status': 'complete', 'paper': {
            'status': 'polished', 'terminal': True, 'polishing_complete': True,
            'best_available_tex': str(folder/'paper.tex'), 'best_available_pdf': str(folder/'final.pdf')}})
        self.write_result()
        self.assertEqual(self.observe()['status'], 'deadline_reached')
        (folder/'final.pdf').unlink()
        report = self.observe()
        self.assertEqual(report['status'], 'paper_incomplete')
        self.assertIn('missing_or_invalid_paper_artifact', {i['kind'] for i in report['issues']})
