"""Portable watchdog checks are deterministic, fail closed, and never relaunch."""
import asyncio
import subprocess
import sys
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from campaign import Campaign
from campaign_watchdog import CampaignWatchdog, capture_process_identity, probe_process


class WatchdogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        source = self.root / 'input.txt'
        source.write_text('Original question')
        self.now = datetime.now(timezone.utc)
        self.c = Campaign.initialize(self.root / 'campaign', {'q': source},
            deadline_utc=(self.now + timedelta(hours=1)).isoformat(), concurrency=1,
            owner_key=self.root / 'controller.key')
        self.token = self.c.claim('q', 'main')
        self.path = self.root / 'host' / 'watchdog.json'
        self.w = CampaignWatchdog(self.c, self.path, interval_seconds=0.01)
        self.stage = {'name': 'q/main', 'problem': 'q', 'status': 'running',
                      'pid': 1234, 'process_identity': 'birth', 'claim_token': self.token,
                      'deadline_utc': (self.now + timedelta(minutes=10)).isoformat(),
                      'last_progress_utc': (self.now - timedelta(hours=2)).isoformat()}

    def inspect(self, alive=True, match=True, **kwargs):
        with patch('campaign_watchdog.probe_process', return_value={
                'alive': alive, 'identity_match': match}):
            return self.w.inspect([self.stage], now_utc=self.now, **kwargs)

    def kinds(self, report):
        return {item['kind'] for item in report['current_incidents']}

    def test_silent_long_reasoning_is_healthy_before_deadline(self):
        report = self.inspect()
        self.assertEqual(report['current_incidents'], [])
        self.assertEqual(report['observations'][0]['health'], 'running_within_deadline')

    def test_dead_child_needs_recovery_without_mutating_claim(self):
        before = (self.c.root / 'state.json').read_bytes()
        self.assertIn('dead_child', self.kinds(self.inspect(False, None)))
        self.assertEqual((self.c.root / 'state.json').read_bytes(), before)

    def test_hung_stage_deadline_requests_only_owned_task_cancellation(self):
        self.stage['deadline_utc'] = (self.now - timedelta(seconds=1)).isoformat()
        incident = self.inspect()['current_incidents'][0]
        self.assertEqual(incident['action'], 'cancel_owned_task')
        self.assertEqual(incident['stage'], 'q/main')
        self.assertIn('process_identity_unverified', self.kinds(self.inspect(True, None)))
        self.assertIn('stage_deadline', self.kinds(self.inspect(True, None)))

    def test_stale_claim_and_identity_fail_closed(self):
        self.stage['claim_token'] = 'old'
        with patch('campaign_watchdog.probe_process') as probe:
            self.assertIn('stale_ownership', self.kinds(self.w.inspect([self.stage], now_utc=self.now)))
            probe.assert_not_called()
        self.stage['claim_token'] = self.token
        self.assertIn('process_identity_unverified', self.kinds(self.inspect(True, False)))
        self.assertIn('process_identity_unverified', self.kinds(self.inspect(None, None)))

    def test_undelivered_feedback_retains_exact_versions_and_open_status(self):
        self.c.release('q', self.token, interrupted=True)
        ticket = self.c.feedback('q')['problems']['q']['feedback'][0]
        report = self.w.inspect([], now_utc=self.now)
        incident = next(i for i in report['current_incidents'] if i['kind'] == 'undelivered_feedback')
        self.assertEqual(incident['ticket_id'], ticket['id'])
        self.assertEqual(incident['fingerprint'], ticket['fingerprint'])
        self.assertTrue(self.c.feedback('q')['problems']['q']['feedback'][0]['needs_delivery'])

    def test_restart_retains_history_and_never_adopts_or_releases(self):
        self.inspect(False, None)
        self.w = CampaignWatchdog(self.c, self.path)
        report = self.inspect(restarting=True)
        self.assertIn('restart_live_job', self.kinds(report))
        self.assertEqual(len(report['incidents']), 2)
        self.assertFalse(report['automatic_restart'])
        self.assertEqual(self.c.status()['problems']['q']['status'], 'running')
        self.assertIn('claim_without_active_stage', self.kinds(self.w.inspect([], restarting=True)))

    def test_quota_is_not_capacity_retry(self):
        self.stage.update(status='backoff', failure_kind='quota')
        self.assertEqual(self.inspect()['current_incidents'][0]['action'], 'respect_provider_limits')
        self.stage['failure_kind'] = 'capacity'
        self.assertEqual(self.inspect()['current_incidents'], [])
        self.stage.update(status='failed', consecutive_failures=3)
        self.assertIn('repeated_infrastructure_failure', self.kinds(self.inspect()))

    def test_host_work_is_covered_and_campaign_deadline_binding(self):
        self.stage['status'] = 'host_work'
        self.assertEqual(self.inspect()['current_incidents'], [])
        report = self.w.inspect([self.stage], now_utc=self.now + timedelta(hours=2))
        self.assertEqual(report['current_incidents'][0]['action'], 'cancel_owned_task')

    def test_report_requires_authority_and_host_location(self):
        with self.assertRaises(ValueError):
            CampaignWatchdog(self.c, self.c.root / 'watchdog.json')
        reader = Campaign(self.c.root)
        with self.assertRaisesRegex(ValueError, 'owner key'):
            CampaignWatchdog(reader, self.path).inspect([])
        self.inspect()
        self.assertEqual(self.path.stat().st_mode & 0o777, 0o600)
        for invalid in (0, -1, True, float('inf'), float('nan')):
            with self.assertRaises(ValueError):
                CampaignWatchdog(self.c, self.path, interval_seconds=invalid)

    def test_probe_distinguishes_missing_from_inaccessible(self):
        with patch('campaign_watchdog.os.kill', side_effect=ProcessLookupError):
            self.assertEqual(probe_process(123, 'birth')['alive'], False)
        with patch('campaign_watchdog.os.kill', side_effect=PermissionError):
            self.assertIsNone(probe_process(123, 'birth')['alive'])
        self.assertIsNone(capture_process_identity(None))


    def test_explicit_stagnation_is_advisory_and_history_deduplicates(self):
        self.stage.update(mathematical_stagnation=True, progress_evidence={'path': 'gap.json', 'sha256': 'abc'})
        report = self.inspect()
        self.assertEqual(report['current_incidents'][0]['action'], 'supervisor_review')
        self.assertEqual(len(self.inspect()['incidents']), 1)
        self.assertEqual(report['registry_sha256'], self.c.status()['registry_sha256'])

    def test_monitor_stops_after_host_callback_without_model_or_restart(self):
        async def run():
            stop = asyncio.Event()
            received = []
            async def callback(report):
                received.append(report)
                stop.set()
            self.stage['deadline_utc'] = (self.now - timedelta(seconds=1)).isoformat()
            with patch('campaign_watchdog.probe_process', return_value={'alive': True, 'identity_match': True}):
                await self.w.monitor(lambda: [self.stage], stop, on_incident=callback)
            return received
        self.assertEqual(len(asyncio.run(run())), 1)

    def test_real_process_identity_and_exit_reconciliation(self):
        child = subprocess.Popen([sys.executable, '-c', 'import time; print("ready", flush=True); time.sleep(0.3)'], stdout=subprocess.PIPE, text=True)
        child.stdout.readline()
        try:
            identity = capture_process_identity(child.pid)
            self.assertIsNotNone(identity)
            self.assertEqual(probe_process(child.pid, identity), {'alive': True, 'identity_match': True})
        finally:
            child.wait(timeout=5)
            child.stdout.close()
        self.assertFalse(probe_process(child.pid, identity)['alive'])
