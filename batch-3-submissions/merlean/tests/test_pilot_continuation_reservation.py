"""Canceled preparations can be superseded once with exact external evidence."""
import asyncio
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import pilot_continuation_reservation as reservation
import test_pilot_continuation_runtime as fixtures


class ReservationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ContinuationRuntimeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.cancelled = self.fixture.root.resolve()
        self.config = self.fixture.prepare()
        self.source = self.fixture.fixture.source.resolve()
        self.root = self.fixture.fixture.base.resolve() / 'replacement'
        self.parent = json.loads((self.cancelled / 'continuation-parent.json').read_text())
        self.predecessor = Path(self.config['continuation_reservation'])
        self.inventory = self.fixture.fixture.base.resolve() / 'cancelled-inventory.json'
        self.launch = self.cancelled.with_name(self.cancelled.name + '.launch.json')
        self.path = self.fixture.fixture.base.resolve() / 'supersession.json'
        self.write(self.launch, {'status': 'cancelled_before_launch', 'run_root': str(self.cancelled), 'model_dispatched': False})
        self.refresh_inventory()
        self.receipt = {'schema_version': 1, 'kind': 'cancelled_unstarted_continuation_supersession',
            'parent': str(self.source), 'parent_manifest_sha256': self.parent['manifest_sha256'],
            'destination': str(self.root), 'cancelled_root': str(self.cancelled),
            'cancelled_config_sha256': reservation.digest((self.cancelled / 'host-config.json').read_bytes()),
            'predecessor_reservation': self.ref(self.predecessor), 'cancelled_inventory': self.ref(self.inventory),
            'cancelled_launch': self.ref(self.launch), 'checked_utc': datetime.now(timezone.utc).isoformat(),
            'model_dispatched': False}
        self.save()

    @staticmethod
    def write(path, value):
        path.write_text(json.dumps(value))

    @staticmethod
    def ref(path):
        return {'path': str(path), 'sha256': reservation.digest(path.read_bytes())}

    def save(self):
        self.write(self.path, self.receipt)

    def refresh_inventory(self):
        self.write(self.inventory, {'status': 'cancelled_before_launch', 'run_root': str(self.cancelled),
                   'model_dispatched': False, 'files': reservation._files(self.cancelled)})
        if hasattr(self, 'receipt'):
            self.receipt['cancelled_inventory'] = self.ref(self.inventory)
            self.save()

    def validate(self, output=''):
        with patch.object(reservation.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, output, '')):
            return reservation.validate_supersession(self.source, self.root, self.parent, self.path)

    def test_exact_cancellation_supersedes_once_preserving_every_old_byte(self):
        before = reservation._files(self.cancelled)
        old = self.predecessor.read_bytes()
        barrier = self.launch.read_bytes()
        config = self.fixture.prepare(self.root, reservation_supersession=self.path)
        claim = reservation.successor_path(self.predecessor)
        self.assertEqual(config['continuation_reservation'], str(claim))
        self.assertEqual(self.predecessor.read_bytes(), old)
        self.assertEqual(self.launch.read_bytes(), barrier)
        self.assertEqual(reservation._files(self.cancelled), before)
        with patch.object(reservation.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')):
            reservation.validate_start(self.root, config)
        other = self.root.with_name('competitor')
        self.receipt['destination'] = str(other); self.save()
        with self.assertRaises(FileExistsError):
            self.fixture.prepare(other, reservation_supersession=self.path)
        self.assertFalse(other.exists())
        with self.assertRaises(FileExistsError):
            self.fixture.prepare(self.root.with_name('without-explicit-receipt'))

    def test_failed_preparation_retains_exclusive_successor(self):
        with patch.object(pilot, 'freeze_runtime', side_effect=RuntimeError('synthetic preparation stop')):
            with self.assertRaisesRegex(RuntimeError, 'synthetic preparation stop'):
                self.fixture.prepare(self.root, reservation_supersession=self.path)
        self.assertTrue(reservation.successor_path(self.predecessor).is_file())
        self.assertTrue(self.predecessor.is_file())

    def test_missing_stale_and_mismatched_receipts_fail_before_claim(self):
        original = copy.deepcopy(self.receipt)
        for key in ('parent', 'parent_manifest_sha256', 'destination', 'cancelled_config_sha256'):
            with self.subTest(key=key):
                self.receipt = copy.deepcopy(original); self.receipt[key] = 'stale'; self.save()
                with self.assertRaises(ValueError): self.validate()
        for key in ('predecessor_reservation', 'cancelled_inventory', 'cancelled_launch'):
            with self.subTest(key=key):
                self.receipt = copy.deepcopy(original); self.receipt[key]['sha256'] = '0' * 64; self.save()
                with self.assertRaisesRegex(ValueError, 'hash mismatch'): self.validate()
        self.receipt = copy.deepcopy(original); del self.receipt['cancelled_launch']; self.save()
        with self.assertRaises(ValueError): self.validate()
        self.path.unlink()
        with self.assertRaises(FileNotFoundError): self.validate()
        self.assertFalse(reservation.successor_path(self.predecessor).exists())

    def test_started_or_launch_reserved_predecessor_fails(self):
        for status in ('launch_reserved', 'launched'):
            self.write(self.launch, {'status': status, 'run_root': str(self.cancelled), 'model_dispatched': False})
            self.receipt['cancelled_launch'] = self.ref(self.launch); self.save()
            with self.assertRaisesRegex(ValueError, 'before launch'): self.validate()
        self.write(self.launch, {'status': 'cancelled_before_launch', 'run_root': str(self.cancelled), 'model_dispatched': False, 'pid': None})
        self.receipt['cancelled_launch'] = self.ref(self.launch); self.save()
        with self.assertRaisesRegex(ValueError, 'before launch'): self.validate()
        self.write(self.launch, {'status': 'cancelled_before_launch', 'run_root': str(self.cancelled), 'model_dispatched': False})
        self.receipt['cancelled_launch'] = self.ref(self.launch); self.save()
        for marker in (self.cancelled / 'HOST-STARTED', self.cancelled / 'pilot-result.json', self.cancelled.with_name(self.cancelled.name + '.host.log')):
            marker.write_text('started')
            with self.assertRaisesRegex(ValueError, 'execution evidence'): self.validate()
            marker.unlink()

    def test_inventory_transport_and_symlink_changes_fail(self):
        extra = self.cancelled / 'extra.txt'; extra.write_text('unrecorded')
        with self.assertRaisesRegex(ValueError, 'file census changed'): self.validate()
        extra.unlink()
        stage = self.cancelled / 'host/runtime/new-stage'; stage.write_text('new transport')
        self.refresh_inventory()
        with self.assertRaisesRegex(ValueError, 'new transport'): self.validate()
        stage.unlink(); self.refresh_inventory()
        extra.symlink_to(self.cancelled / 'host-config.json')
        with self.assertRaisesRegex(ValueError, 'symlinks'): self.validate()

    def test_live_or_unavailable_process_census_fails(self):
        with self.assertRaisesRegex(ValueError, 'live process'):
            self.validate('999999 1 999999 python ' + str(self.cancelled) + '/code/codex_pilot.py\n')
        with self.assertRaisesRegex(ValueError, 'incomplete cancellation process census'):
            self.validate('malformed process census\n')
        with patch.object(reservation.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'ps')):
            with self.assertRaises(subprocess.CalledProcessError):
                reservation.validate_supersession(self.source, self.root, self.parent, self.path)

    def test_empty_accounting_allowed_but_wal_activity_rejected_without_writes(self):
        folder = self.cancelled / 'host/accounting'; folder.mkdir()
        database = folder / 'usage.sqlite3'
        connection = sqlite3.connect(database)
        connection.executescript('PRAGMA journal_mode=WAL; CREATE TABLE calls (id TEXT); CREATE TABLE usage_events (id TEXT);')
        connection.commit()
        self.refresh_inventory(); before = reservation._files(self.cancelled)
        self.validate()
        self.assertEqual(reservation._files(self.cancelled), before)
        connection.execute("INSERT INTO calls VALUES ('new-response')"); connection.commit()
        self.refresh_inventory(); before = reservation._files(self.cancelled)
        try:
            with self.assertRaisesRegex(ValueError, 'accounting activity'): self.validate()
            self.assertEqual(reservation._files(self.cancelled), before)
        finally:
            connection.close()

    def test_cancelled_or_superseded_run_cannot_reach_start(self):
        runner = pilot.Pilot(self.cancelled)
        with patch.object(pilot, 'subscription_preflight') as dispatch:
            with self.assertRaisesRegex(ValueError, 'cancelled preparation cannot start'):
                asyncio.run(runner.run())
            dispatch.assert_not_called()
        self.launch.unlink()
        reservation.successor_path(self.predecessor).write_text('{}')
        with self.assertRaisesRegex(ValueError, 'superseded'):
            reservation.validate_start(self.cancelled, self.config)

    def test_successor_start_rechecks_cancellation_hash_and_processes(self):
        config = self.fixture.prepare(self.root, reservation_supersession=self.path)
        before = self.launch.read_bytes(); self.launch.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            reservation.validate_start(self.root, config)
        self.launch.write_bytes(before)
        with patch.object(reservation.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '999999 1 999999 python '+str(self.cancelled)+'\n', '')):
            with self.assertRaisesRegex(ValueError, 'live process'):
                reservation.validate_start(self.root, config)


if __name__ == '__main__':
    unittest.main()
