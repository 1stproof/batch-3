"""Tests for host-fed token and API-equivalent accounting."""
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
import json
from pathlib import Path
import sys
import tempfile
import sqlite3
import threading
from unittest.mock import MagicMock, patch
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from api_accounting import APIAccountingLedger, normalize_usage


PRICE_CARD = ROOT / "assets/api-prices-2026-09-16.json"


class APIAccountingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = Path(self.temp.name) / "usage.sqlite3"
        self.ledger = APIAccountingLedger(self.db, PRICE_CARD)

    def tearDown(self):
        self.temp.cleanup()

    def test_normalization_preserves_subsets_and_reasoning(self):
        usage = normalize_usage(
            {
                "input_tokens": 100,
                "cached_input_tokens": 20,
                "cache_write_input_tokens": 10,
                "output_tokens": 40,
                "reasoning_output_tokens": 30,
                "total_tokens": 140,
            },
            usage_format="codex_flat",
        )
        self.assertEqual(usage["input_tokens"], 100)
        self.assertEqual(usage["reasoning_output_tokens"], 30)
        with self.assertRaisesRegex(ValueError, "exceeds inclusive input"):
            normalize_usage(
                {"input": 10, "cached_read": 8, "cache_write": 3},
                usage_format="normalized",
            )
        with self.assertRaisesRegex(ValueError, "requires output"):
            normalize_usage({"reasoning_output": 1})

    def test_exact_price_cache_reasoning_and_mixed_groups(self):
        self.ledger.record(
            "a1", "actor", "gpt-6-astra",
            {"input": 1_000_000, "cached_read": 200_000, "cache_write": 100_000,
             "output": 100_000, "reasoning_output": 80_000},
            "complete",
        )
        self.ledger.record(
            "s1", "review", "gpt-5.6-sol",
            {"input": 100_000, "cached_read": 0, "cache_write": 0,
             "output": 10_000, "reasoning_output": 9_000},
            "complete",
        )
        summary = self.ledger.summary()
        # Astra is long-context: (700k*10*2 + 200k*1*2 + 100k*12.5*2
        # + 100k*50*1.5) / 1m = 24.4. Sol = .6. Reasoning is not added.
        self.assertEqual(summary["by_module"]["actor"]["api_equivalent_usd"], "24.4")
        self.assertEqual(summary["by_module"]["review"]["api_equivalent_usd"], "0.6")
        self.assertEqual(summary["total"]["api_equivalent_usd"], "25")
        self.assertEqual(summary["total"]["api_equivalent_usd_observed_lower_bound"], "25")
        self.assertEqual(
            summary["by_module"]["actor"]["api_equivalent_usd_observed_lower_bound"],
            "24.4",
        )
        self.assertEqual(summary["total"]["usage"]["total_tokens"], 1_210_000)
        self.assertEqual(summary["total"]["usage"]["reasoning_output_tokens"], 89_000)
        self.assertIsNone(summary["total"]["actual_billed_usd"])

    def test_long_context_is_per_request_and_service_multiplier(self):
        for index in range(2):
            self.ledger.record(
                f"short-{index}", "actor", "gpt-6-astra",
                {"input": 200_000, "cached_read": 0, "cache_write": 0, "output": 0},
                "complete", service_tier="standard",
            )
        self.ledger.record(
            "threshold", "actor", "gpt-6-astra",
            {"input": 272_000, "cached_read": 0, "cache_write": 0, "output": 0},
            "complete", service_tier="standard",
        )
        self.ledger.record(
            "long", "actor", "gpt-6-astra",
            {"input": 272_001, "cached_read": 0, "cache_write": 0, "output": 0},
            "complete", service_tier="fast",
        )
        summary = self.ledger.summary()["total"]
        # Two short requests cost $2 each. Long: 272001 * $10 * 2 long * 2 fast.
        expected = (
            Decimal("4")
            + Decimal(272_000) * Decimal(10) / Decimal(1_000_000)
            + Decimal(272_001) * Decimal(40) / Decimal(1_000_000)
        )
        self.assertEqual(summary["api_equivalent_usd"], format(expected, "f"))

    def test_cumulative_retry_is_idempotent_and_conflicts_are_rejected(self):
        kwargs = dict(
            call_id="call", module="actor", model="gpt-6-astra",
            usage={"input": 100, "cached_read": 0, "cache_write": 0, "output": 20},
            status="in_flight", event_id="response-1",
        )
        self.ledger.record(**kwargs)
        self.ledger.record(**kwargs)
        usage = self.ledger.summary()["total"]["usage"]
        self.assertIsNone(usage["input_tokens"])
        self.assertFalse(usage["input_tokens_complete"])
        self.assertEqual(usage["input_tokens_observed_lower_bound"], 100)
        with self.assertRaisesRegex(ValueError, "reused with different content"):
            self.ledger.record(**{**kwargs, "status": "complete"})
        with self.assertRaisesRegex(ValueError, "conflicts on model"):
            self.ledger.record(
                "call", "actor", "gpt-5.6-sol", None, "in_flight"
            )

    def test_delta_retry_and_partial_unknown_are_not_zero(self):
        self.ledger.record(
            "delta", "actor", "gpt-6-astra",
            {"input": 100, "output": 10}, "in_flight",
            usage_mode="delta", event_id="e1",
        )
        self.ledger.record(
            "delta", "actor", "gpt-6-astra",
            {"input": 50, "output": 5}, "in_flight",
            usage_mode="delta", event_id="e2",
        )
        self.ledger.record(
            "delta", "actor", "gpt-6-astra",
            {"input": 50, "output": 5}, "in_flight",
            usage_mode="delta", event_id="e2",
        )
        total = self.ledger.summary()["total"]
        self.assertIsNone(total["usage"]["input_tokens"])
        self.assertEqual(total["usage"]["input_tokens_observed_lower_bound"], 150)
        self.assertIsNone(total["usage"]["cached_input_tokens"])
        self.assertIsNone(total["api_equivalent_usd"])
        self.assertFalse(total["api_equivalent_usd_is_final"])
        self.assertEqual(total["in_flight_or_unknown_call_count"], 1)

    def test_unknown_model_and_missing_usage_remain_unknown(self):
        self.ledger.record("u1", "actor", "unknown-model", None, "complete")
        total = self.ledger.summary()["total"]
        self.assertIsNone(total["usage"]["input_tokens"])
        self.assertIsNone(total["api_equivalent_usd"])
        self.assertIsNone(total["api_equivalent_usd_observed_lower_bound"])
        self.assertEqual(total["unpriced_call_count"], 1)
        self.assertEqual(total["missing_usage_call_count"], 1)

    def test_absent_usage_is_unknown_even_for_priced_model(self):
        self.ledger.record("missing", "actor", "gpt-6-astra", None, "failed")
        total = self.ledger.summary()["total"]
        self.assertIsNone(total["api_equivalent_usd"])
        self.assertIsNone(total["api_equivalent_usd_observed_lower_bound"])
        self.assertEqual(total["missing_usage_call_count"], 1)
        self.assertEqual(total["unpriced_call_count"], 0)

    def test_in_flight_known_usage_is_only_an_observed_lower_bound(self):
        self.ledger.record(
            "live", "actor", "gpt-6-astra",
            {"input": 100, "cached_read": 0, "cache_write": 0, "output": 20},
            "in_flight",
        )
        total = self.ledger.summary()["total"]
        self.assertIsNone(total["usage"]["input_tokens"])
        self.assertIsNone(total["usage"]["total_tokens"])
        self.assertFalse(total["usage"]["input_tokens_complete"])
        self.assertFalse(total["usage"]["total_tokens_complete"])
        self.assertEqual(total["usage"]["total_tokens_observed_lower_bound"], 120)
        self.assertIsNone(total["api_equivalent_usd"])
        self.assertFalse(total["api_equivalent_usd_is_final"])

    def test_terminal_usage_is_frozen_but_unknown_fields_may_be_filled(self):
        self.ledger.record(
            "late", "actor", "gpt-6-astra",
            {"input": 100, "output": 20}, "complete", event_id="terminal",
        )
        self.assertIsNone(self.ledger.summary()["total"]["api_equivalent_usd"])
        self.ledger.record(
            "late", "actor", "gpt-6-astra",
            {"input": 100, "cached_read": 0, "cache_write": 0, "output": 20},
            "complete", event_id="late-breakdown",
        )
        total = self.ledger.summary()["total"]
        self.assertEqual(total["usage"]["total_tokens"], 120)
        self.assertEqual(total["api_equivalent_usd"], "0.002")
        self.assertEqual(
            total["api_equivalent_usd_observed_lower_bound"],
            total["api_equivalent_usd"],
        )
        with self.assertRaisesRegex(ValueError, "terminal input_tokens is frozen"):
            self.ledger.record(
                "late", "actor", "gpt-6-astra",
                {"input": 101, "cached_read": 0, "cache_write": 0, "output": 20},
                "complete", event_id="mutate-final",
            )

        self.ledger.record(
            "delta-final", "actor", "gpt-6-astra",
            {"input": 10, "cached_read": 0, "cache_write": 0, "output": 1},
            "complete", usage_mode="delta", event_id="d1",
        )
        with self.assertRaisesRegex(ValueError, "cannot accept new delta"):
            self.ledger.record(
                "delta-final", "actor", "gpt-6-astra",
                {"input": 1, "cached_read": 0, "cache_write": 0, "output": 0},
                "complete", usage_mode="delta", event_id="d2",
            )

    def test_old_event_replay_after_terminal_transition_is_idempotent(self):
        first = dict(
            call_id="replay", module="actor", model="gpt-6-astra",
            usage={"input": 100, "cached_read": 0, "cache_write": 0, "output": 10},
            status="in_flight", event_id="response-1",
        )
        self.ledger.record(**first)
        self.ledger.record(
            "replay", "actor", "gpt-6-astra",
            {"input": 120, "cached_read": 0, "cache_write": 0, "output": 12},
            "complete", event_id="response-final",
        )
        replayed = self.ledger.record(**first)
        self.assertEqual(replayed["status"], "complete")
        self.assertEqual(replayed["usage"]["input_tokens"], 120)
        with self.assertRaisesRegex(ValueError, "reused with different content"):
            self.ledger.record(**{**first, "usage": {
                "input": 101, "cached_read": 0, "cache_write": 0, "output": 10,
            }})

    def test_actual_billed_is_separate_and_only_final_when_complete(self):
        self.ledger.record(
            "paid", "external", "gpt-5.6-sol",
            {"input": 0, "cached_read": 0, "cache_write": 0, "output": 0},
            "complete", basis="api_actual", actual_billed_usd="1.23",
        )
        total = self.ledger.summary()["total"]
        self.assertEqual(total["api_equivalent_usd"], "0")
        self.assertEqual(total["actual_billed_usd"], "1.23")

    def test_alternate_service_scenario_does_not_duplicate_tokens(self):
        self.ledger.record(
            "scenario", "actor", "gpt-6-astra",
            {"input": 100_000, "cached_read": 0, "cache_write": 0, "output": 10_000},
            "complete", service_tier="standard",
            metadata={"actual_service_tier": None},
        )
        total = self.ledger.summary(equivalent_service_tiers=["fast"])["total"]
        self.assertEqual(total["usage"]["total_tokens"], 110_000)
        self.assertEqual(total["api_equivalent_usd"], "1.5")
        scenario = total["api_equivalent_service_tier_scenarios"]["fast"]
        self.assertEqual(scenario["api_equivalent_usd"], "3")
        self.assertEqual(total["call_count"], 1)

    def test_concurrent_distinct_calls_are_atomic(self):
        def add(index: int) -> None:
            ledger = APIAccountingLedger(self.db, PRICE_CARD)
            ledger.record(
                f"c-{index}", "review", "gpt-5.6-sol",
                {"input": 1000, "cached_read": 0, "cache_write": 0, "output": 100},
                "complete", event_id="final",
            )

        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(add, range(24)))
        total = self.ledger.summary()["total"]
        self.assertEqual(total["call_count"], 24)
        self.assertEqual(total["usage"]["input_tokens"], 24_000)
        self.assertEqual(total["api_equivalent_usd"], "0.144")

    def test_concurrent_distinct_deltas_for_same_call_are_atomic(self):
        self.ledger.record(
            "shared", "review", "gpt-5.6-sol", None, "in_flight",
            usage_mode="delta", event_id="registered",
        )

        def add(index: int) -> None:
            ledger = APIAccountingLedger(self.db, PRICE_CARD)
            ledger.record(
                "shared", "review", "gpt-5.6-sol",
                {"input": 1000, "cached_read": 100, "cache_write": 50, "output": 100},
                "in_flight", usage_mode="delta", event_id=f"delta-{index}",
            )

        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(add, range(24)))
        self.ledger.record(
            "shared", "review", "gpt-5.6-sol", None, "complete",
            usage_mode="delta", event_id="final-status",
        )
        total = self.ledger.summary()["total"]
        self.assertEqual(total["call_count"], 1)
        self.assertEqual(total["usage"]["input_tokens"], 24_000)
        self.assertEqual(total["usage"]["cached_input_tokens"], 2_400)
        self.assertEqual(total["usage"]["cache_write_input_tokens"], 1_200)
        self.assertEqual(total["usage"]["output_tokens"], 2_400)

    def test_nested_module_model_aggregates_use_the_same_calls_once(self):
        self.ledger.record(
            "a", "research", "gpt-6-astra",
            {"input": 10, "cached_read": 0, "cache_write": 0, "output": 1},
            "complete",
        )
        self.ledger.record(
            "s", "research", "gpt-5.6-sol",
            {"input": 20, "cached_read": 0, "cache_write": 0, "output": 2},
            "complete",
        )
        summary = self.ledger.summary()
        nested = summary["by_module_model"]["research"]
        self.assertEqual(nested["gpt-6-astra"]["call_count"], 1)
        self.assertEqual(nested["gpt-5.6-sol"]["call_count"], 1)
        self.assertEqual(summary["by_module"]["research"]["call_count"], 2)
        self.assertEqual(summary["total"]["call_count"], 2)

    def test_concurrent_initialization_is_atomic(self):
        fresh_db = Path(self.temp.name) / "fresh.sqlite3"
        start = threading.Barrier(8)

        def initialize(_: int) -> str:
            start.wait(timeout=10)
            return APIAccountingLedger(fresh_db, PRICE_CARD).summary()["price_card"]["sha256"]

        with ThreadPoolExecutor(max_workers=8) as pool:
            hashes = list(pool.map(initialize, range(16)))
        self.assertEqual(len(set(hashes)), 1)

    def test_price_card_provenance_and_database_binding(self):
        summary = self.ledger.summary()
        raw = PRICE_CARD.read_bytes()
        import hashlib
        self.assertEqual(summary["price_card"]["sha256"], hashlib.sha256(raw).hexdigest())
        changed = json.loads(raw)
        changed["models"]["gpt-6-astra"]["input"] = "11"
        with self.assertRaisesRegex(ValueError, "different price_card"):
            APIAccountingLedger(self.db, changed)




class WALConnectionSetupTests(unittest.TestCase):
    def setup_connection(self, outcomes):
        connection = MagicMock()
        wal_cursor = MagicMock()
        wal_cursor.fetchone.return_value = ('wal',)
        states = iter(outcomes)
        def execute(statement):
            if statement == 'PRAGMA journal_mode = WAL':
                value = next(states)
                if isinstance(value, BaseException):
                    raise value
                return wal_cursor if value == 'wal' else value
            return MagicMock()
        connection.execute.side_effect = execute
        ledger = APIAccountingLedger.__new__(APIAccountingLedger)
        ledger.db = Path('unused-synthetic.sqlite3')
        return ledger, connection, wal_cursor

    @staticmethod
    def busy(code=sqlite3.SQLITE_BUSY):
        error = sqlite3.OperationalError('synthetic busy')
        error.sqlite_errorcode = code
        return error

    def test_busy_then_success_restores_timeout_and_closes_cursor(self):
        ledger, connection, cursor = self.setup_connection([self.busy(5 | 256), 'wal'])
        with patch('api_accounting.sqlite3.connect', return_value=connection), \
             patch('api_accounting.time.monotonic', side_effect=[0, 0.001, 0.011]), \
             patch('api_accounting.time.sleep') as sleep:
            self.assertIs(ledger._connect(), connection)
        sleep.assert_called_once_with(0.01)
        self.assertEqual(connection.execute.call_args_list[-1].args[0], 'PRAGMA busy_timeout = 30000')
        cursor.close.assert_called_once()
        connection.close.assert_not_called()

    def test_busy_fetch_releases_cursor_before_waiting(self):
        blocked = MagicMock()
        blocked.fetchone.side_effect = self.busy()
        ledger, connection, _ = self.setup_connection([blocked, 'wal'])
        def sleep(_):
            blocked.close.assert_called_once()
        with patch('api_accounting.sqlite3.connect', return_value=connection), \
             patch('api_accounting.time.monotonic', side_effect=[0, 0.001, 0.011]), \
             patch('api_accounting.time.sleep', side_effect=sleep):
            self.assertIs(ledger._connect(), connection)
        blocked.close.assert_called_once()

        error = self.busy()
        ledger, connection, _ = self.setup_connection([error])
        with patch('api_accounting.sqlite3.connect', return_value=connection), \
             patch('api_accounting.time.monotonic', side_effect=[0, 29.995, 30]), \
             patch('api_accounting.time.sleep') as sleep:
            with self.assertRaises(sqlite3.OperationalError) as caught:
                ledger._connect()
        self.assertIs(caught.exception, error)
        self.assertAlmostEqual(sleep.call_args.args[0], 0.005)
        self.assertEqual(sum(c.args[0] == 'PRAGMA journal_mode = WAL' for c in connection.execute.call_args_list), 1)
        connection.close.assert_called_once()

    def test_non_busy_error_propagates_immediately_and_closes(self):
        error = self.busy(sqlite3.SQLITE_LOCKED)
        ledger, connection, _ = self.setup_connection([error])
        with patch('api_accounting.sqlite3.connect', return_value=connection), \
             patch('api_accounting.time.sleep') as sleep:
            with self.assertRaises(sqlite3.OperationalError) as caught:
                ledger._connect()
        self.assertIs(caught.exception, error)
        sleep.assert_not_called()
        connection.close.assert_called_once()

    def test_non_wal_result_refused_and_closed(self):
        cursor = MagicMock()
        cursor.fetchone.return_value = ('delete',)
        ledger, connection, _ = self.setup_connection([cursor])
        with patch('api_accounting.sqlite3.connect', return_value=connection), \
             patch('api_accounting.time.sleep') as sleep:
            with self.assertRaisesRegex(sqlite3.OperationalError, 'WAL journal mode unavailable'):
                ledger._connect()
        sleep.assert_not_called()
        cursor.close.assert_called_once()
        connection.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
