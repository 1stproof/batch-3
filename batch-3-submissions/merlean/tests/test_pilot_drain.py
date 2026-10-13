"""Future cooperative drain closes admission while active work finishes normally."""
import asyncio
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from pilot_drain import DrainRequested, PilotDrain


class PilotDrainTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.drain = PilotDrain(self.root / 'host')
        self.drain.directory.mkdir()

    def request(self):
        self.drain.request_path.write_text(json.dumps({'schema_version': 1, 'action': 'drain',
            'request_id': 'requested-once', 'reason': 'Save a stable successor checkpoint'}))

    def committed(self):
        checkpoint = self.root / 'problem-checkpoint.json'
        checkpoint.write_text(json.dumps({'current': 'exact saved answer', 'status': 'partial'}))
        result = self.root / 'pilot-result.json'
        result.write_text(json.dumps({'end_utc': datetime.now(timezone.utc).isoformat(),
                                     'results': [{'problem': 'q', 'status': 'partial'}]}))
        reconcile = self.root / 'owned-children-reconciled.json'
        reconcile.write_text(json.dumps({'schema_version': 1, 'host_session_id': self.drain.host_session_id,
            'checked_utc': datetime.now(timezone.utc).isoformat(), 'all_owned_children_stopped': True,
            'active_children': [], 'pending_launches': []}))
        return dict(checkpoint_paths=[checkpoint], result_path=result, reconciliation_path=reconcile)

    async def test_queued_dispatch_rejected_active_result_and_accounting_committed(self):
        semaphore = asyncio.Semaphore(1)
        active = asyncio.Event()
        finish = asyncio.Event()
        events = []
        async def running():
            async with semaphore:
                with self.drain.admission('stage', 'q/main'):
                    active.set()
                    await finish.wait()
                    events.extend(['answer_saved', 'accounting_saved'])
        async def queued():
            async with semaphore:
                with self.drain.admission('stage', 'q/queued'):
                    events.append('UNSAFE_LAUNCH')
        first = asyncio.create_task(running())
        await active.wait()
        second = asyncio.create_task(queued())
        self.request()
        self.assertFalse(self.drain.closed_path.exists())
        self.assertFalse(self.drain.ack_path.exists())
        self.drain.poll()
        self.assertTrue(self.drain.closed_path.exists())
        self.assertFalse(first.done())
        self.assertFalse(first.cancelled())
        with self.assertRaisesRegex(ValueError, 'still active'):
            self.drain.acknowledge(**self.committed())
        finish.set()
        await first
        with self.assertRaises(DrainRequested):
            await second
        self.assertEqual(events, ['answer_saved', 'accounting_saved'])
        self.assertFalse(self.drain.ack_path.exists())
        receipt = self.drain.acknowledge(**self.committed())
        self.assertEqual(receipt['status'], 'drained')
        self.assertEqual(receipt['active_operations'], 0)
        self.assertEqual(self.drain.ack_path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(receipt['terminal_result']['sha256'], hashlib.sha256((self.root/'pilot-result.json').read_bytes()).hexdigest())

    async def test_request_creation_not_ack_and_removal_never_reopens(self):
        self.request()
        self.assertFalse(self.drain.closed)
        with self.assertRaises(DrainRequested):
            with self.drain.admission('probe', 'q/python'):
                self.fail('probe admitted after observed drain')
        self.drain.request_path.unlink()
        with self.assertRaises(DrainRequested):
            self.drain.check()
        replacement = PilotDrain(self.drain.directory)
        with self.assertRaises(DrainRequested):
            replacement.check()
        with self.assertRaisesRegex(ValueError, 'current host admission closure'):
            replacement.acknowledge(**self.committed())

    async def test_malformed_request_closes_without_cancel_or_signal(self):
        for payload in ('{', '[]', '{"schema_version":1,"action":"stop-now"}'):
            directory = self.root / str(len(list(self.root.iterdir())))
            directory.mkdir()
            gate = PilotDrain(directory)
            gate.request_path.write_text(payload)
            with patch('os.kill', side_effect=AssertionError('must never signal')):
                with self.assertRaises(DrainRequested):
                    gate.check()
            closure = json.loads(gate.closed_path.read_text())
            self.assertIsNotNone(closure['request_error'])
            self.assertFalse(closure['drained'])
            self.assertFalse(gate.ack_path.exists())

    async def test_unreadable_request_fails_closed(self):
        with patch.object(Path, 'read_bytes', side_effect=PermissionError):
            with self.assertRaises(DrainRequested):
                self.drain.check()
        self.assertTrue(self.drain.closed)

    async def test_uncertain_launch_or_stale_reconciliation_blocks_final_ack(self):
        self.request()
        self.drain.poll()
        inputs = self.committed()
        path = inputs['reconciliation_path']
        original = json.loads(path.read_text())
        for changes in ({'pending_launches': ['unknown-launch']}, {'active_children': [123]},
                        {'all_owned_children_stopped': False}, {'host_session_id': 'prior-host'},
                        {'checked_utc': '2000-01-01T00:00:00Z'}):
            path.write_text(json.dumps(original | changes))
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.drain.acknowledge(**inputs)
            self.assertFalse(self.drain.ack_path.exists())
        path.write_text(json.dumps(original))
        inputs['checkpoint_paths'][0].unlink()
        with self.assertRaises(FileNotFoundError):
            self.drain.acknowledge(**inputs)
        self.assertFalse(self.drain.ack_path.exists())

    async def test_retry_boundary_and_probe_admission_share_gate(self):
        with self.drain.admission('stage', 'q/failed-capacity-attempt'):
            await asyncio.sleep(0)
        self.request()
        with self.assertRaises(DrainRequested):
            self.drain.check()
        with self.assertRaises(DrainRequested):
            with self.drain.admission('probe', 'q/next-probe'):
                self.fail('probe started')
        self.assertEqual(self.drain.active_count, 0)

    async def test_healthy_admission_does_not_create_drain_receipts(self):
        with self.drain.admission('stage', 'q/healthy'):
            self.assertEqual(self.drain.active_count, 1)
        self.assertEqual(self.drain.active_count, 0)
        self.assertFalse(self.drain.closed_path.exists())
        self.assertFalse(self.drain.ack_path.exists())


if __name__ == '__main__':
    unittest.main()
