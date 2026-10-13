"""Synthetic response accounting; no provider calls or private rollout fixtures."""
import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from codex_accounting import account_stage
from api_accounting import APIAccountingLedger
import codex_transport as transport


class AccountingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'runtime/p/main').mkdir(parents=True)
        self.meta = dict(name='p/main', module='main', model_requested='test-astra',
                         artifact_directory='runtime/p/main', session_id='session',
                         start_utc='2026-01-01T00:01:00Z', end_utc='2026-01-01T00:02:00Z',
                         status='completed', turn_completed=True)
        self.record = dict(timestamp='2026-01-01T00:01:30Z', model='test-astra',
                           payload=dict(thread_id='session', turn_id='turn', response_id='response',
                                        usage=dict(input_tokens=100, cached_input_tokens=40,
                                                   output_tokens=20, reasoning_output_tokens=12)))

    def collect(self, records=None, status='verified'):
        receipt = account_stage(self.root, self.meta, dict(status=status, response_usage_records=[self.record] if records is None else records))
        summary = json.loads((self.root / 'accounting/summary.json').read_text())
        return receipt, summary

    def test_api_usage_is_not_subscription_charge_or_guessed_reasoning(self):
        self.meta['authentication']='api'
        receipt,summary=self.collect()
        self.assertEqual(receipt['authentication'],'api')
        self.assertIsNone(receipt['actual_billed_usd'])
        self.assertEqual(summary['ledger']['total']['usage']['reasoning_output_tokens'],12)
        self.record['payload']['usage'].pop('reasoning_output_tokens')
        self.record['payload']['response_id']='second'
        receipt,_=self.collect()
        self.assertEqual(receipt['metering'],'unknown')

    def test_historical_usage_and_recursive_lineage_stay_separate(self):
        self.root = self.root / 'continuation/host'
        (self.root / 'runtime/p/main').mkdir(parents=True)
        directory = self.root.parent / 'history/accounting'
        directory.mkdir(parents=True)
        history = {'metering_complete': False, 'ledger': {'total': {'usage': {'input_tokens': 700}}},
                   'historical_accounting': {'summary': {'ledger': {'total': {'usage': {'input_tokens': 300}}}}}}
        raw = json.dumps(history).encode()
        (directory / 'summary.json').write_bytes(raw)
        self.record['payload']['usage']['cache_write_input_tokens'] = 0
        _, summary = self.collect()
        self.assertTrue(summary['segment_metering_complete'])
        self.assertFalse(summary['metering_complete'])
        self.assertEqual(summary['ledger']['total']['usage']['input_tokens'], 100)
        self.assertEqual(summary['historical_accounting']['summary'], history)
        import hashlib
        self.assertEqual(summary['historical_accounting']['sha256'], hashlib.sha256(raw).hexdigest())
        self.assertEqual((directory / 'summary.json').read_bytes(), raw)

    def test_legacy_or_missing_historical_metering_stays_unknown(self):
        self.root = self.root / 'continuation/host'
        (self.root / 'runtime/p/main').mkdir(parents=True)
        directory = self.root.parent / 'history/accounting'
        directory.mkdir(parents=True)
        self.record['payload']['usage']['cache_write_input_tokens'] = 0
        for history in ({'is_final': True, 'pending_or_unmetered_stages': [], 'ledger': {}}, {'metering_complete': True}):
            (directory / 'summary.json').write_text(json.dumps(history))
            _, summary = self.collect()
            self.assertEqual(summary['metering_complete'], history.get('metering_complete') is True)
        (directory / 'summary.json').unlink()
        _, summary = self.collect()
        self.assertFalse(summary['metering_complete'])
        self.assertIn('missing', summary['historical_accounting']['error'])

    def test_idempotent_inclusive_usage_and_unknown_price(self):
        self.collect()
        _, summary = self.collect()
        total = summary['ledger']['total']
        self.assertEqual(total['call_count'], 1)
        self.assertEqual(total['usage']['total_tokens'], 120)
        self.assertEqual(total['usage']['reasoning_output_tokens'], 12)
        self.assertIsNone(total['usage']['cache_write_input_tokens'])
        self.assertIsNone(total['api_equivalent_usd'])
        self.assertIsNone(total['actual_billed_usd'])

    def test_missing_usage_is_unknown(self):
        self.record['payload'].pop('usage')
        receipt, summary = self.collect()
        self.assertEqual(receipt['metering'], 'unknown')
        self.assertIsNone(summary['ledger']['total']['usage']['total_tokens'])
        self.assertFalse(summary['metering_complete'])

    def test_failed_and_censored_usage_is_only_subtotal(self):
        for status in ('cancelled', 'timeout_censored', 'process_failed'):
            self.meta['status'] = status
            receipt, summary = self.collect(status='unavailable')
            self.assertEqual(receipt['metering'], 'unknown')
            self.assertEqual(summary['ledger']['total']['usage']['total_tokens_observed_lower_bound'], 120)

    def test_actual_model_never_falls_back_to_requested(self):
        self.record['model'] = 'test-sol'
        receipt, summary = self.collect()
        self.assertEqual(list(summary['ledger']['by_model']), ['test-sol'])
        self.assertEqual(receipt['metering'], 'unknown')

    def test_conflicting_duplicate_is_reported(self):
        self.collect()
        self.record['payload']['usage']['input_tokens'] = 101
        receipt, summary = self.collect()
        self.assertTrue(receipt['errors'])
        self.assertEqual(summary['ledger']['total']['usage']['input_tokens'], 100)

    def test_time_window_and_identity_reject_history(self):
        self.record['timestamp'] = '2026-01-01T00:00:30Z'
        receipt, summary = self.collect()
        self.assertTrue(receipt['errors'])
        self.assertEqual(summary['ledger']['total']['call_count'], 0)
        self.record['timestamp'] = '2026-01-01T00:01:30Z'
        self.record['payload']['thread_id'] = 'other-session'
        receipt, summary = self.collect()
        self.assertTrue(receipt['errors'])
        self.assertEqual(summary['ledger']['total']['call_count'], 0)

    def test_resumed_rollout_and_truncated_cancel_preserve_exact_records(self):
        folder = self.root / 'sessions/2026/01/01'
        folder.mkdir(parents=True)
        events = [dict(timestamp='2026-01-01T00:00:00Z', type='turn_context', payload=dict(turn_id='old', model='test-sol')),
                  dict(timestamp='2026-01-01T00:00:30Z', type='token_usage_record', payload=dict(response_id='old-response', usage={'input_tokens':999})),
                  dict(timestamp='2026-01-01T00:01:01Z', type='turn_context', payload=dict(turn_id='turn', model='test-astra')),
                  dict(timestamp=self.record['timestamp'], type='token_usage_record', payload=self.record['payload']),
                  dict(timestamp='2026-01-01T00:01:31Z', type='event_msg', payload=dict(type='token_count', info={'total_token_usage':{'input_tokens':9999}}))]
        (folder / 'rollout-session.jsonl').write_text('\n'.join(map(json.dumps, events)) + '\n{"truncated":')
        with patch.dict(os.environ, {'CODEX_HOME': str(self.root)}):
            audit = transport._persisted_tool_audit('session', self.meta['start_utc'])
        self.assertEqual(audit['status'], 'unavailable')
        self.assertEqual(audit['response_usage_records'], [self.record])
        self.meta['status'] = 'cancelled'
        receipt = account_stage(self.root, self.meta, audit)
        self.assertEqual(receipt['response_ids'], ['response'])
        self.assertEqual(receipt['metering'], 'unknown')

    def test_timeout_and_cancellation_automatically_preserve_accounting(self):
        for cancel in (False, True):
            program = self.root / 'slow.py'
            program.write_text('import sys, time\nsys.stdin.read()\nprint(\'{"type":"thread.started","thread_id":"session"}\', flush=True)\ntime.sleep(10)\n')
            def audit(session, start):
                record = dict(self.record, timestamp=start)
                record['payload'] = dict(record['payload'], response_id='cancel' if cancel else 'timeout')
                return dict(status='verified', tool_events=[], turn_contexts=[dict(model='test-astra')], response_usage_records=[record])
            async def run():
                task = asyncio.create_task(transport.call_stage(self.root, 'p/cancel' if cancel else 'p/timeout', 'synthetic', 'test-astra', 5 if cancel else 0.1, module='main'))
                if cancel:
                    await asyncio.sleep(0.1)
                    task.cancel()
                    with self.assertRaises(asyncio.CancelledError):
                        await task
                else:
                    await task
            with patch.object(transport, 'subscription_preflight', return_value=dict(authentication='chatgpt', cli_version='test')), patch.object(transport, '_command', return_value=[sys.executable, str(program)]), patch.object(transport, '_persisted_tool_audit', side_effect=audit):
                asyncio.run(run())
            meta = json.loads((self.root / ('runtime/p/cancel/stage.meta.json' if cancel else 'runtime/p/timeout/stage.meta.json')).read_text())
            self.assertEqual(meta['status'], 'cancelled' if cancel else 'timeout_censored')
            self.assertEqual(meta['accounting']['metering'], 'unknown')
            self.assertEqual(meta['accounting']['response_ids'], ['cancel' if cancel else 'timeout'])

    def test_cancellation_during_spawn_reaps_owned_child(self):
        original = asyncio.create_subprocess_exec
        processes = []
        async def scenario():
            spawned = asyncio.Event()
            release = asyncio.Event()
            async def delayed(*args, **kwargs):
                process = await original(*args, **kwargs)
                processes.append(process)
                spawned.set()
                await release.wait()
                return process
            with patch.object(transport.asyncio, 'create_subprocess_exec', side_effect=delayed):
                task = asyncio.create_task(transport.call_stage(self.root, 'p/spawn-cancel', 'synthetic', 'test-astra', 5, module='main'))
                await spawned.wait()
                task.cancel()
                release.set()
                with self.assertRaises(asyncio.CancelledError):
                    await task
            self.assertIsNotNone(processes[0].returncode)
        with patch.object(transport, 'subscription_preflight', return_value=dict(authentication='chatgpt', cli_version='test')), patch.object(transport, '_command', return_value=[sys.executable, '-c', 'import time; time.sleep(10)']):
            asyncio.run(scenario())
        meta = json.loads((self.root / 'runtime/p/spawn-cancel/stage.meta.json').read_text())
        self.assertEqual(meta['status'], 'cancelled')
        self.assertEqual(meta['accounting']['metering'], 'unknown')

    def test_usage_before_context_uses_unique_exact_turn_model(self):
        folder = self.root / 'sessions/2026/01/01'
        folder.mkdir(parents=True)
        usage = dict(timestamp=self.record['timestamp'], type='token_usage_record', payload=self.record['payload'])
        context = dict(timestamp='2026-01-01T00:01:31Z', type='turn_context', payload=dict(turn_id='turn', model='test-astra'))
        compacted = dict(timestamp='2026-01-01T00:01:30Z', type='compacted', payload=dict(compaction_response_id='response'))
        path = folder / 'rollout-session.jsonl'
        for contexts, expected in (([context], 'test-astra'),
                                   ([context, context], 'test-astra'),
                                   ([context, dict(context, payload=dict(turn_id='turn', model='test-sol'))], None),
                                   ([dict(context, payload=dict(turn_id='other-turn', model='test-astra'))], None),
                                   ([context, dict(context, payload=dict(turn_id='turn'))], None)):
            path.write_text('\n'.join(map(json.dumps, [usage, compacted] + contexts)))
            with patch.dict(os.environ, {'CODEX_HOME': str(self.root)}):
                audit = transport._persisted_tool_audit('session', self.meta['start_utc'])
            self.assertEqual(audit['response_usage_records'][0]['model'], expected)
            self.assertEqual(audit['response_usage_records'][0]['payload']['usage'], self.record['payload']['usage'])
            self.assertIn('backend response model not independently verified', audit['usage_model_attribution'])

    def test_normal_transport_automatically_ingests(self):
        program = self.root / 'fake.py'
        events = [dict(type='thread.started', thread_id='session'), dict(type='item.completed', item=dict(type='agent_message', text='done')), dict(type='turn.completed', usage={'input_tokens':9999})]
        program.write_text('import sys\nsys.stdin.read()\n' + '\n'.join('print(' + repr(json.dumps(event)) + ', flush=True)' for event in events))
        def audit(session, start):
            record = dict(self.record, timestamp=start)
            return dict(status='verified', tool_events=[], turn_contexts=[dict(model='test-astra')], response_usage_records=[record])
        with patch.object(transport, 'subscription_preflight', return_value=dict(authentication='chatgpt', cli_version='test')), patch.object(transport, '_command', return_value=[sys.executable, str(program)]), patch.object(transport, '_persisted_tool_audit', side_effect=audit):
            meta, _ = asyncio.run(transport.call_stage(self.root, 'p/other', 'synthetic', 'test-astra', 5, module='main'))
        self.assertEqual(meta['accounting']['response_ids'], ['response'])
        summary = json.loads((self.root / 'accounting/summary.json').read_text())
        self.assertEqual(summary['ledger']['total']['usage']['input_tokens'], 100)


if __name__ == '__main__':
    unittest.main()
