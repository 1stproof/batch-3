"""Independent synthetic audit of portable host safety and metering boundaries."""
from datetime import datetime, timedelta, timezone
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from campaign import Campaign
from campaign_watchdog import CampaignWatchdog
from codex_accounting import account_stage
import codex_pilot


class HostBoundaryAuditTests(unittest.TestCase):
    def test_forensic_inspection_does_not_invent_historical_claim_binding(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'source.txt'
            source.write_text('Synthetic equality.')
            instant = datetime.now(timezone.utc)
            campaign = Campaign.initialize(root / 'campaign', {'p':source},
                deadline_utc=(instant + timedelta(minutes=10)).isoformat(), concurrency=1,
                owner_key=root / 'controller.key')
            campaign.claim('p', 'current-owner')
            path = root / 'host/runtime/p/old-stage/stage.meta.json'
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'name':'p/old-stage','status':'running',
                'pid':1234567,'start_utc':instant.isoformat(),'timeout_seconds':60}))
            with patch.object(sys, 'argv', ['pilot', str(root), '--inspect-watchdog']), \
                 patch.object(CampaignWatchdog, 'inspect', return_value={}) as inspect, \
                 patch.object(codex_pilot, 'subscription_preflight') as preflight, \
                 contextlib.redirect_stdout(io.StringIO()):
                codex_pilot.main()
            self.assertIsNone(inspect.call_args.args[0][0].get('claim_token'))
            self.assertTrue(inspect.call_args.kwargs['restarting'])
            preflight.assert_not_called()

    def test_incomplete_counters_never_claim_complete_metering(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'runtime' / 'p' / 'stage').mkdir(parents=True)
            meta = self.meta()
            audit = self.audit({'input_tokens': 100})
            receipt = account_stage(root, meta, audit)
            self.assertEqual(receipt['metering'], 'unknown')
            summary = json.loads((root / 'accounting' / 'summary.json').read_text())
            self.assertFalse(summary['metering_complete'])
            self.assertIsNone(summary['ledger']['total']['usage']['output_tokens'])

    def test_censored_stage_retains_observed_subtotal_and_unknown_remainder(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'runtime' / 'p' / 'stage').mkdir(parents=True)
            meta = self.meta()
            meta['status'] = 'timeout_censored'
            usage = {'input_tokens':100,'cached_input_tokens':20,'cache_write_input_tokens':0,
                     'output_tokens':30,'reasoning_output_tokens':10,'total_tokens':130}
            first = account_stage(root, meta, self.audit(usage))
            second = account_stage(root, meta, self.audit(usage))
            self.assertEqual(first, second)
            self.assertEqual(second['metering'], 'unknown')
            summary = json.loads((root / 'accounting' / 'summary.json').read_text())
            self.assertFalse(summary['metering_complete'])
            self.assertEqual(summary['ledger']['total']['call_count'], 1)
            self.assertEqual(summary['ledger']['total']['usage']['total_tokens_observed_lower_bound'], 130)

    def test_old_resumed_response_not_charged_to_current_stage(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'runtime' / 'p' / 'stage').mkdir(parents=True)
            audit = self.audit({'input_tokens':100,'output_tokens':30})
            audit['response_usage_records'][0]['timestamp'] = '2026-01-01T00:00:00Z'
            receipt = account_stage(root, self.meta(), audit)
            self.assertEqual(receipt['metering'], 'unknown')
            self.assertEqual(receipt['response_ids'], [])

    def test_watchdog_cannot_signal_or_release_from_supplied_pid(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'source.txt'
            source.write_text('Synthetic equality.')
            instant = datetime.now(timezone.utc)
            campaign = Campaign.initialize(root / 'campaign', {'p':source},
                deadline_utc=(instant + timedelta(minutes=10)).isoformat(), concurrency=1,
                owner_key=root / 'controller.key')
            token = campaign.claim('p', 'host')
            before = (root / 'campaign' / 'state.json').read_bytes()
            watchdog = CampaignWatchdog(campaign, root / 'host' / 'watchdog.json')
            with patch('campaign_watchdog.os.kill') as signal, patch(
                'campaign_watchdog.capture_process_identity', return_value='unrelated-process'):
                report = watchdog.inspect([{'name':'p/stage','problem':'p','status':'running',
                    'pid':1234567,'process_identity':'expected','claim_token':token,
                    'deadline_utc':(instant - timedelta(seconds=1)).isoformat()}],
                    now_utc=instant, restarting=True)
            self.assertTrue(all(call.args[1] == 0 for call in signal.call_args_list))
            self.assertFalse(report['automatic_restart'])
            self.assertEqual(before, (root / 'campaign' / 'state.json').read_bytes())
            self.assertIn('process_identity_unverified', {i['kind'] for i in report['current_incidents']})

    @staticmethod
    def meta():
        return {'artifact_directory':'runtime/p/stage','session_id':'session-1',
                'start_utc':'2026-01-01T00:01:00Z','end_utc':'2026-01-01T00:02:00Z',
                'name':'p/stage','module':'main','model_requested':'gpt-6-astra',
                'turn_completed':True,'status':'completed'}

    @staticmethod
    def audit(usage):
        return {'status':'verified','response_usage_records':[{
            'timestamp':'2026-01-01T00:01:30Z','model':'gpt-6-astra',
            'payload':{'response_id':'response-1','thread_id':'session-1',
                       'turn_id':'turn-1','usage':usage}}]}


if __name__ == '__main__':
    unittest.main()
