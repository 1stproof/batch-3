"""Explicit bounded-call changes preserve saved campaigns and other policies."""
import asyncio
import contextlib
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import test_pilot_continuation_runtime as runtime_fixtures


class MainTimeoutTests(unittest.TestCase):
    setUp = runtime_fixtures.ContinuationRuntimeTests.setUp
    prepare = runtime_fixtures.ContinuationRuntimeTests.prepare

    def test_legacy_default_and_main_dispatch(self):
        config = self.prepare()
        self.assertEqual(config['main_call_timeout_seconds'], 900)
        self.assertEqual(config['explicit_policy_changes'], runtime_fixtures.expected_legacy_migration_changes())
        path = self.root/'host-config.json'
        legacy_config = json.loads(path.read_text())
        legacy_config.pop('main_call_timeout_seconds')
        self.fixture.write(path, legacy_config)
        problem = pilot.Problem(pilot.Pilot(self.root), 'problem')
        problem.session = 'main-session'
        answer = {'response_type': 'candidate_update', 'proof_markdown': 'Saved progress', 'ledger': {'rows': []}}
        with patch.object(problem, 'call', new=AsyncMock(return_value=({'name':'problem/005-main-repair','request_id':'mock-request'}, answer))) as call:
            asyncio.run(problem.main_turn('Continue'))
        self.assertEqual(call.call_args.kwargs['timeout'], 900)
        self.assertTrue(call.call_args.kwargs['resume'])

    def test_override_recorded_in_config_reservation_and_actual_dispatch(self):
        before = {str(p): p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()}
        old = json.loads((self.fixture.source/'host-config.json').read_text())
        config = self.prepare(main_call_timeout_seconds=1800)
        change = {**runtime_fixtures.expected_legacy_migration_changes(), 'main_call_timeout_seconds': {'old': 900, 'new': 1800}}
        self.assertEqual(config['explicit_policy_changes'], change)
        self.assertEqual(config['main_call_timeout_seconds'], 1800)
        self.assertIsNone(config['deadline_utc'])
        self.assertFalse(config['internet_browse'])
        self.assertEqual(config.get('models'), old.get('models'))
        reservation = json.loads(Path(config['continuation_reservation']).read_text())
        self.assertEqual(reservation['explicit_policy_changes'], change)
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()})
        problem = pilot.Problem(pilot.Pilot(self.root), 'problem')
        problem.session = 'main-session'
        with patch.object(problem, 'call', new=AsyncMock(return_value=({'name':'problem/005-main-repair','request_id':'mock-request'}, {'response_type': 'candidate_update', 'proof_markdown': 'Saved', 'ledger': {'rows': []}}))) as call:
            asyncio.run(problem.main_turn('Continue'))
        self.assertEqual(call.call_args.kwargs['timeout'], 1800)

    def test_inherits_existing_timeout(self):
        path = self.fixture.source/'host-config.json'
        config = json.loads(path.read_text())
        config['main_call_timeout_seconds'] = 1200
        self.fixture.write(path, config)
        result = self.prepare()
        self.assertEqual(result['main_call_timeout_seconds'], 1200)
        self.assertEqual(result['explicit_policy_changes'], runtime_fixtures.expected_legacy_migration_changes())

    def test_invalid_override_has_no_destination_or_reservation(self):
        for value in (0, -1, True, float('nan'), float('inf'), '1800'):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'finite and positive'):
                self.prepare(main_call_timeout_seconds=value)
            self.assertFalse(self.root.exists())
            self.assertFalse((self.fixture.source.parent/'.continuation-reservations').exists())

    def test_cli_rejects_nonfinite_before_dispatch(self):
        for value in ('0', '-1', 'nan', 'inf'):
            with patch.object(sys, 'argv', ['pilot', str(self.root), '--main-call-timeout-seconds', value]), \
                 patch.object(pilot, 'subscription_preflight') as preflight, \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                pilot.main()
            preflight.assert_not_called()

    def test_cli_forwards_explicit_continuation_override(self):
        argv = ['pilot', str(self.root), '--continue-from', str(self.fixture.source),
                '--reconciliation', str(self.fixture.receipt), '--main-call-timeout-seconds', '1800']
        with patch.object(sys, 'argv', argv), patch.object(pilot, 'prepare_continuation') as prepare, \
             patch.object(pilot, 'Pilot') as runner, contextlib.redirect_stdout(io.StringIO()):
            runner.return_value.run = AsyncMock(return_value=[])
            pilot.main()
        self.assertEqual(prepare.call_args.kwargs['main_call_timeout_seconds'], 1800)
        self.assertIsNone(prepare.call_args.kwargs['internet_browse'])

    def test_existing_run_override_rejected_including_inspection(self):
        for extra in ([], ['--inspect-watchdog']):
            with patch.object(sys, 'argv', ['pilot', str(self.root), '--main-call-timeout-seconds', '1800', *extra]), \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                pilot.main()
