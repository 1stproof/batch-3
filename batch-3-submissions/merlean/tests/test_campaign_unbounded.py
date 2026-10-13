"""Explicit unbounded campaigns preserve bounded calls and authority gates."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from campaign import Campaign
from campaign_watchdog import CampaignWatchdog


class UnboundedCampaignTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        source = self.root / 'input.txt'
        source.write_text('Exact original')
        self.now = datetime.now(timezone.utc)
        self.c = Campaign.initialize(self.root / 'campaign', {'q': source},
            deadline_utc=None, concurrency=1, owner_key=self.root / 'key')
        self.w = CampaignWatchdog(self.c, self.root / 'watchdog.json')

    def test_unbounded_claim_reopen_keeps_history_and_seal_gate(self):
        with patch('campaign.now', return_value=self.now + timedelta(days=900)):
            token = self.c.claim('q', 'main')
            self.c.release('q', token)
            (self.c.root / 'problems/q/partial.md').write_text('Honest partial')
            self.c.finish('q', partial='partial.md')
            self.c.reopen('q', reason='Authorized continuation of saved work')
            self.assertEqual(self.c.status()['problems']['q']['repair_round'], 1)
            self.assertIsNone(self.c.status()['deadline_utc'])
            self.assertIsNone(self.c.feedback()['deadline_utc'])
            self.c.finish('q', partial='partial.md')
            self.c.seal()
            with self.assertRaisesRegex(ValueError, 'sealed'):
                self.c.reopen('q', reason='Sealed still blocks mutation')

    def test_stage_deadline_survives_no_campaign_cap(self):
        token = self.c.claim('q', 'main')
        stage = {'name': 'q/main', 'problem': 'q', 'status': 'running',
                 'claim_token': token, 'pid': 42, 'process_identity': 'owned',
                 'deadline_utc': (self.now + timedelta(minutes=10)).isoformat()}
        with patch('campaign_watchdog.probe_process', return_value={'alive': True, 'identity_match': True}):
            report = self.w.inspect([stage], now_utc=self.now)
            self.assertEqual(report['current_incidents'], [])
            self.assertIsNone(report['deadline_utc'])
            report = self.w.inspect([stage], now_utc=self.now + timedelta(minutes=11))
            self.assertEqual(report['current_incidents'][0]['action'], 'cancel_owned_task')
            stage['deadline_utc'] = None
            report = self.w.inspect([stage], now_utc=self.now)
            self.assertIn('stage_deadline_unknown', {i['kind'] for i in report['current_incidents']})

    def test_host_work_uncapped_but_optional_probe_deadline_enforced(self):
        stage = {'name': 'q/host', 'problem': 'q', 'status': 'host_work',
                 'claim_token': self.c.claim('q', 'main')}
        future = self.now + timedelta(days=900)
        self.assertEqual(self.w.inspect([stage], now_utc=future)['current_incidents'], [])
        stage['deadline_utc'] = (self.now + timedelta(seconds=30)).isoformat()
        self.assertEqual(self.w.inspect([stage], now_utc=future)['current_incidents'][0]['kind'], 'stage_deadline')
        stage.update(status='backoff', failure_kind='quota')
        report = self.w.inspect([stage], now_utc=future)
        self.assertEqual(report['current_incidents'][0]['action'], 'respect_provider_limits')

    def test_unbounded_keeps_duplicate_claim_and_restart_safety(self):
        token = self.c.claim('q', 'main')
        with self.assertRaisesRegex(ValueError, 'already claimed'):
            self.c.claim('q', 'duplicate')
        stage = {'name': 'q/host', 'problem': 'q', 'status': 'host_work', 'claim_token': token}
        report = self.w.inspect([stage], restarting=True)
        self.assertFalse(report['automatic_restart'])
        self.assertEqual(report['current_incidents'][0]['kind'], 'restart_reconciliation')
        self.assertEqual(self.c.status()['problems']['q']['claim_token'], token)
