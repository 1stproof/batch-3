"""Host-fed API usage and API-equivalent cost accounting.

The ledger is deliberately passive: callers provide usage reported by a model host.
It does not dispatch requests, discover usage, or infer a subscription invoice.
"""
from __future__ import annotations

from collections.abc import Mapping
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import time
from typing import Any


SCHEMA_VERSION = 1
PRICE_CARD_SCHEMA_VERSION = 1
METRICS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
)
TERMINAL_STATUSES = {"complete", "failed", "cancelled"}
STATUSES = TERMINAL_STATUSES | {"in_flight", "unknown"}
USAGE_MODES = {"cumulative", "delta"}
USAGE_FORMATS = {"normalized", "codex_flat"}
MAX_SQLITE_INTEGER = 2**63 - 1
MILLION = Decimal(1_000_000)

_NORMALIZED_KEYS = {
    "input": "input_tokens",
    "cached_read": "cached_input_tokens",
    "cache_write": "cache_write_input_tokens",
    "output": "output_tokens",
    "reasoning_output": "reasoning_output_tokens",
}
_CODEX_KEYS = {
    "input_tokens": "input_tokens",
    "cached_input_tokens": "cached_input_tokens",
    "cache_write_input_tokens": "cache_write_input_tokens",
    "output_tokens": "output_tokens",
    "reasoning_output_tokens": "reasoning_output_tokens",
}


def _canonical_json(value: object) -> str:
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
    except (TypeError, ValueError) as error:
        raise ValueError(f"value is not canonical JSON: {error}") from error


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value.strip()


def _token(value: object, label: str) -> int:
    if type(value) is not int or value < 0 or value > MAX_SQLITE_INTEGER:
        raise ValueError(f"{label} must be a nonnegative 64-bit integer")
    return value


def _decimal(value: object, label: str) -> Decimal:
    if isinstance(value, bool) or value is None:
        raise ValueError(f"{label} must be a nonnegative decimal")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise ValueError(f"{label} must be a nonnegative decimal") from error
    if not result.is_finite() or result < 0:
        raise ValueError(f"{label} must be a nonnegative decimal")
    return result


def _money(value: Decimal | None) -> str | None:
    if value is None:
        return None
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def normalize_usage(
    usage: Mapping[str, object], *, usage_format: str = "normalized"
) -> dict[str, int | None]:
    """Normalize one cumulative snapshot or delta without inventing missing values.

    ``normalized`` fields are ``input``, ``cached_read``, ``cache_write``,
    ``output``, and ``reasoning_output``. ``codex_flat`` accepts Codex's flat
    ``*_tokens`` fields and optional ``total_tokens``. Missing fields remain
    ``None``; an explicit zero remains known zero.
    """
    if usage_format not in USAGE_FORMATS:
        raise ValueError(f"unsupported usage format: {usage_format}")
    if not isinstance(usage, Mapping):
        raise ValueError("usage must be an object")
    key_map = _NORMALIZED_KEYS if usage_format == "normalized" else _CODEX_KEYS
    allowed = set(key_map)
    if usage_format == "codex_flat":
        allowed.add("total_tokens")
    extras = set(usage) - allowed
    if extras:
        raise ValueError("usage has unknown fields: " + ", ".join(sorted(extras)))

    normalized: dict[str, int | None] = {metric: None for metric in METRICS}
    for source, target in key_map.items():
        if source in usage:
            normalized[target] = _token(usage[source], f"usage.{source}")

    input_tokens = normalized["input_tokens"]
    cached = normalized["cached_input_tokens"]
    cache_write = normalized["cache_write_input_tokens"]
    output = normalized["output_tokens"]
    reasoning = normalized["reasoning_output_tokens"]
    if (cached is not None or cache_write is not None) and input_tokens is None:
        raise ValueError("cached input and cache write are subsets and require input")
    if input_tokens is not None:
        known_subsets = (cached or 0) + (cache_write or 0)
        if known_subsets > input_tokens:
            raise ValueError("cached input plus cache write exceeds inclusive input")
    if reasoning is not None and output is None:
        raise ValueError("reasoning output is a subset and requires output")
    if reasoning is not None and output is not None and reasoning > output:
        raise ValueError("reasoning output exceeds inclusive output")
    if usage_format == "codex_flat" and "total_tokens" in usage:
        total = _token(usage["total_tokens"], "usage.total_tokens")
        if input_tokens is not None and output is not None and total != input_tokens + output:
            raise ValueError("total_tokens must equal input_tokens plus output_tokens")
    return normalized


class PriceCard:
    """Validated immutable price-card snapshot."""

    def __init__(self, source: str | os.PathLike[str] | Mapping[str, object]):
        if isinstance(source, Mapping):
            value = dict(source)
            raw = (_canonical_json(value) + "\n").encode("utf-8")
        else:
            raw = Path(source).read_bytes()
            try:
                value = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                raise ValueError(f"price card is not valid UTF-8 JSON: {error}") from error
        if not isinstance(value, dict):
            raise ValueError("price card must be an object")
        required = {
            "schema_version", "currency", "unit", "retrieved_at_utc", "source_urls",
            "models", "long_context_threshold", "long_context_multipliers",
            "service_multipliers", "basis", "notes",
        }
        missing = required - set(value)
        extras = set(value) - required
        if missing or extras:
            raise ValueError(
                "price card fields mismatch: missing " + ",".join(sorted(missing))
                + "; unknown " + ",".join(sorted(extras))
            )
        if type(value["schema_version"]) is not int or value["schema_version"] != PRICE_CARD_SCHEMA_VERSION:
            raise ValueError("unsupported price-card schema")
        if value["currency"] != "USD" or value["unit"] != "per_million_tokens":
            raise ValueError("price card must use USD per_million_tokens")
        self.retrieved_at_utc = _text(value["retrieved_at_utc"], "retrieved_at_utc")
        urls = value["source_urls"]
        if not isinstance(urls, list) or not urls:
            raise ValueError("source_urls must be a nonempty list")
        self.source_urls = tuple(_text(url, "source URL") for url in urls)
        self.threshold = _token(value["long_context_threshold"], "long_context_threshold")
        self.basis = _text(value["basis"], "basis")
        self.sha256 = hashlib.sha256(raw).hexdigest()
        self.raw_json = raw.decode("utf-8")

        models = value["models"]
        if not isinstance(models, dict) or not models:
            raise ValueError("models must be a nonempty object")
        self.models: dict[str, dict[str, Decimal]] = {}
        rate_keys = {"input", "cached_input", "cache_write", "output"}
        for model, rates in models.items():
            model = _text(model, "model")
            if not isinstance(rates, dict) or set(rates) != rate_keys:
                raise ValueError(f"model {model} must define exactly {sorted(rate_keys)}")
            self.models[model] = {
                key: _decimal(rates[key], f"models.{model}.{key}") for key in rate_keys
            }

        long_rates = value["long_context_multipliers"]
        if not isinstance(long_rates, dict) or set(long_rates) != rate_keys:
            raise ValueError("long_context_multipliers fields mismatch")
        self.long_multipliers = {
            key: _decimal(long_rates[key], f"long_context_multipliers.{key}")
            for key in rate_keys
        }
        services = value["service_multipliers"]
        if not isinstance(services, dict) or not services:
            raise ValueError("service_multipliers must be a nonempty object")
        self.service_multipliers = {
            _text(key, "service tier"): _decimal(multiplier, f"service.{key}")
            for key, multiplier in services.items()
        }

    def provenance(self) -> dict[str, object]:
        return {
            "sha256": self.sha256,
            "retrieved_at_utc": self.retrieved_at_utc,
            "source_urls": list(self.source_urls),
            "basis": self.basis,
            "currency": "USD",
            "unit": "per_million_tokens",
        }


class APIAccountingLedger:
    """Concurrency-safe SQLite ledger for host-supplied per-call usage."""

    def __init__(
        self,
        db: str | os.PathLike[str],
        price_card: str | os.PathLike[str] | Mapping[str, object] | None = None,
    ):
        self.db = Path(db)
        if str(db) == ":memory:":
            raise ValueError("use a file-backed database so accounting survives each connection")
        self.db.parent.mkdir(parents=True, exist_ok=True)
        self.price_card = PriceCard(price_card) if price_card is not None else None
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        deadline = time.monotonic() + 30.0
        connection = sqlite3.connect(self.db, timeout=30)
        try:
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            # Mode promotion may return BUSY without invoking SQLite's busy
            # handler. Bound this idempotent setup operation ourselves; do not
            # multiply the existing 30-second budget by an internal busy wait.
            connection.execute("PRAGMA busy_timeout = 0")
            last_busy = None
            while True:
                if last_busy is not None and time.monotonic() >= deadline:
                    raise last_busy
                cursor = None
                try:
                    cursor = connection.execute("PRAGMA journal_mode = WAL")
                    mode = cursor.fetchone()
                    if not mode or str(mode[0]).lower() != "wal":
                        raise sqlite3.OperationalError("WAL journal mode unavailable")
                    break
                except sqlite3.OperationalError as exc:
                    code = getattr(exc, "sqlite_errorcode", None)
                    if code is None or code & 0xff != sqlite3.SQLITE_BUSY:
                        raise
                    if cursor is not None:
                        cursor.close()
                        cursor = None
                    last_busy = exc
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise
                    time.sleep(min(0.01, remaining))
                finally:
                    if cursor is not None:
                        cursor.close()
            connection.execute("PRAGMA busy_timeout = 30000")
            return connection
        except BaseException:
            connection.close()
            raise

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS accounting_meta (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS calls (
                    call_id TEXT PRIMARY KEY,
                    module TEXT NOT NULL,
                    model TEXT NOT NULL,
                    status TEXT NOT NULL,
                    basis TEXT NOT NULL,
                    service_tier TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    usage_mode TEXT NOT NULL,
                    usage_format TEXT NOT NULL,
                    actual_billed_usd TEXT,
                    input_tokens_observed INTEGER NOT NULL DEFAULT 0,
                    input_tokens_known INTEGER NOT NULL DEFAULT 0,
                    cached_input_tokens_observed INTEGER NOT NULL DEFAULT 0,
                    cached_input_tokens_known INTEGER NOT NULL DEFAULT 0,
                    cache_write_input_tokens_observed INTEGER NOT NULL DEFAULT 0,
                    cache_write_input_tokens_known INTEGER NOT NULL DEFAULT 0,
                    output_tokens_observed INTEGER NOT NULL DEFAULT 0,
                    output_tokens_known INTEGER NOT NULL DEFAULT 0,
                    reasoning_output_tokens_observed INTEGER NOT NULL DEFAULT 0,
                    reasoning_output_tokens_known INTEGER NOT NULL DEFAULT 0,
                    usage_event_count INTEGER NOT NULL DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS usage_events (
                    call_id TEXT NOT NULL REFERENCES calls(call_id),
                    event_id TEXT NOT NULL,
                    payload_sha256 TEXT NOT NULL,
                    PRIMARY KEY (call_id, event_id)
                );
                """
            )
            connection.execute("BEGIN IMMEDIATE")
            expected = {
                "schema_version": str(SCHEMA_VERSION),
                "price_card_sha256": self.price_card.sha256 if self.price_card else "unpriced",
                "price_card_json": self.price_card.raw_json if self.price_card else "null",
            }
            for key, value in expected.items():
                connection.execute(
                    "INSERT OR IGNORE INTO accounting_meta(key, value) VALUES (?, ?)",
                    (key, value),
                )
                row = connection.execute(
                    "SELECT value FROM accounting_meta WHERE key = ?", (key,)
                ).fetchone()
                if row is None or row["value"] != value:
                    raise ValueError(f"accounting database is bound to a different {key}")

    def record(
        self,
        call_id: str,
        module: str,
        model: str,
        usage: Mapping[str, object] | None,
        status: str,
        basis: str = "subscription_api_equivalent",
        service_tier: str = "standard",
        metadata: Mapping[str, object] | None = None,
        *,
        usage_mode: str = "cumulative",
        usage_format: str = "normalized",
        event_id: str | None = None,
        actual_billed_usd: Decimal | str | int | None = None,
    ) -> dict[str, object]:
        """Record one call snapshot or delta and return that call's current state.

        Cumulative snapshots merge monotonically. Delta reports require a stable
        ``event_id`` so retries are idempotent. Reusing an event ID with different
        content is rejected.
        """
        call_id = _text(call_id, "call_id")
        module = _text(module, "module")
        model = _text(model, "model")
        basis = _text(basis, "basis")
        service_tier = _text(service_tier, "service_tier")
        if status not in STATUSES:
            raise ValueError(f"unsupported status: {status}")
        if usage_mode not in USAGE_MODES:
            raise ValueError(f"unsupported usage mode: {usage_mode}")
        if usage_format not in USAGE_FORMATS:
            raise ValueError(f"unsupported usage format: {usage_format}")
        if usage_mode == "delta" and event_id is None:
            raise ValueError("delta usage requires event_id for idempotence")
        if event_id is not None:
            event_id = _text(event_id, "event_id")
        normalized = None if usage is None else normalize_usage(usage, usage_format=usage_format)
        incoming_billed = None if actual_billed_usd is None else _money(
            _decimal(actual_billed_usd, "actual_billed_usd")
        )

        metadata_json: str | None
        if metadata is None:
            metadata_json = None
        elif not isinstance(metadata, Mapping):
            raise ValueError("metadata must be an object")
        else:
            metadata_json = _canonical_json(dict(metadata))

        with self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            row = connection.execute(
                "SELECT * FROM calls WHERE call_id = ?", (call_id,)
            ).fetchone()
            existing_call = row is not None
            if row is None:
                metadata_json = metadata_json if metadata_json is not None else "{}"
                connection.execute(
                    """INSERT INTO calls(
                        call_id, module, model, status, basis, service_tier, metadata_json,
                        usage_mode, usage_format, actual_billed_usd
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        call_id, module, model, status, basis, service_tier, metadata_json,
                        usage_mode, usage_format, incoming_billed,
                    ),
                )
                row = connection.execute(
                    "SELECT * FROM calls WHERE call_id = ?", (call_id,)
                ).fetchone()
            else:
                metadata_json = metadata_json if metadata_json is not None else row["metadata_json"]
                fixed = {
                    "module": module,
                    "model": model,
                    "basis": basis,
                    "service_tier": service_tier,
                    "metadata_json": metadata_json,
                    "usage_mode": usage_mode,
                    "usage_format": usage_format,
                }
                for key, value in fixed.items():
                    if row[key] != value:
                        raise ValueError(f"call_id {call_id} conflicts on {key}")

            event_payload = {
                "call_id": call_id,
                "module": module,
                "model": model,
                "usage": normalized,
                "status": status,
                "basis": basis,
                "service_tier": service_tier,
                "metadata": json.loads(metadata_json),
                "usage_mode": usage_mode,
                "usage_format": usage_format,
                # Hash the incoming event, not values inherited from current call state.
                # This lets an old event replay after a later status/billing transition.
                "actual_billed_usd": incoming_billed,
            }
            payload_hash = hashlib.sha256(
                _canonical_json(event_payload).encode("utf-8")
            ).hexdigest()
            if event_id is not None:
                prior = connection.execute(
                    "SELECT payload_sha256 FROM usage_events WHERE call_id = ? AND event_id = ?",
                    (call_id, event_id),
                ).fetchone()
                if prior is not None:
                    if prior["payload_sha256"] != payload_hash:
                        raise ValueError(f"event_id {event_id} was reused with different content")
                    return self._one_call(connection, call_id)

            if existing_call and row["status"] in TERMINAL_STATUSES and status != row["status"]:
                raise ValueError(f"terminal call {call_id} cannot change status")
            if row["actual_billed_usd"] is not None and incoming_billed not in {
                None, row["actual_billed_usd"]
            }:
                raise ValueError(f"call_id {call_id} conflicts on actual_billed_usd")
            billed = (
                incoming_billed
                if incoming_billed is not None
                else row["actual_billed_usd"]
            )
            if normalized is not None:
                self._merge_usage(
                    connection,
                    row,
                    normalized,
                    usage_mode,
                    terminal_frozen=(
                        existing_call and row["status"] in TERMINAL_STATUSES
                    ),
                )
            connection.execute(
                "UPDATE calls SET status = ?, actual_billed_usd = ? WHERE call_id = ?",
                (status, billed, call_id),
            )
            if event_id is not None:
                connection.execute(
                    "INSERT INTO usage_events(call_id, event_id, payload_sha256) VALUES (?, ?, ?)",
                    (call_id, event_id, payload_hash),
                )
            return self._one_call(connection, call_id)

    def _merge_usage(
        self,
        connection: sqlite3.Connection,
        row: sqlite3.Row,
        usage: dict[str, int | None],
        mode: str,
        *,
        terminal_frozen: bool,
    ) -> None:
        updates: dict[str, int] = {}
        prior_event_count = row["usage_event_count"]
        if terminal_frozen and mode == "delta":
            raise ValueError("terminal call cannot accept new delta usage")
        for metric in METRICS:
            observed_key = metric + "_observed"
            known_key = metric + "_known"
            old_observed = row[observed_key]
            old_known = bool(row[known_key])
            value = usage[metric]
            if mode == "cumulative":
                if value is None:
                    new_observed, new_known = old_observed, old_known
                else:
                    if terminal_frozen and old_known and value != old_observed:
                        raise ValueError(f"terminal {metric} is frozen")
                    if old_known and value < old_observed:
                        raise ValueError(f"cumulative {metric} decreased")
                    new_observed, new_known = value, True
            else:
                if value is None:
                    new_observed, new_known = old_observed, False
                else:
                    if old_observed > MAX_SQLITE_INTEGER - value:
                        raise ValueError(f"delta {metric} exceeds the 64-bit total limit")
                    new_observed = old_observed + value
                    new_known = old_known if prior_event_count else True
            updates[observed_key] = new_observed
            updates[known_key] = int(new_known)

        if (
            updates["cached_input_tokens_observed"]
            + updates["cache_write_input_tokens_observed"]
            > updates["input_tokens_observed"]
        ):
            raise ValueError("aggregate cached input plus cache write exceeds inclusive input")
        if updates["reasoning_output_tokens_observed"] > updates["output_tokens_observed"]:
            raise ValueError("aggregate reasoning output exceeds inclusive output")
        assignments = ", ".join(f"{key} = ?" for key in updates)
        connection.execute(
            f"UPDATE calls SET {assignments}, usage_event_count = usage_event_count + 1 WHERE call_id = ?",
            (*updates.values(), row["call_id"]),
        )

    def _one_call(self, connection: sqlite3.Connection, call_id: str) -> dict[str, object]:
        row = connection.execute(
            "SELECT * FROM calls WHERE call_id = ?", (call_id,)
        ).fetchone()
        assert row is not None
        result: dict[str, object] = {
            "call_id": row["call_id"],
            "module": row["module"],
            "model": row["model"],
            "status": row["status"],
            "basis": row["basis"],
            "service_tier": row["service_tier"],
            "metadata": json.loads(row["metadata_json"]),
            "usage_mode": row["usage_mode"],
            "usage_format": row["usage_format"],
            "actual_billed_usd": row["actual_billed_usd"],
            "usage": {},
        }
        usage_result = result["usage"]
        assert isinstance(usage_result, dict)
        for metric in METRICS:
            usage_result[metric] = (
                row[metric + "_observed"] if row[metric + "_known"] else None
            )
            usage_result[metric + "_observed_lower_bound"] = row[metric + "_observed"]
        return result

    def summary(
        self, *, equivalent_service_tiers: tuple[str, ...] | list[str] = ()
    ) -> dict[str, object]:
        """Return totals by module, by model, and overall.

        Exact totals are ``None`` whenever any included call is unknown or still in
        flight. Observed lower-bound fields remain available and are labelled as such.
        Optional service-tier scenarios reprice the same usage without duplicating calls.
        """
        scenarios: tuple[str, ...] = tuple(equivalent_service_tiers)
        if len(set(scenarios)) != len(scenarios):
            raise ValueError("equivalent service-tier scenarios must be unique")
        for tier in scenarios:
            if self.price_card is None or tier not in self.price_card.service_multipliers:
                raise ValueError(f"unknown equivalent service-tier scenario: {tier}")
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM calls ORDER BY call_id").fetchall()
        modules: dict[str, list[sqlite3.Row]] = {}
        models: dict[str, list[sqlite3.Row]] = {}
        module_models: dict[str, dict[str, list[sqlite3.Row]]] = {}
        for row in rows:
            modules.setdefault(row["module"], []).append(row)
            models.setdefault(row["model"], []).append(row)
            module_models.setdefault(row["module"], {}).setdefault(
                row["model"], []
            ).append(row)
        return {
            "schema_version": SCHEMA_VERSION,
            "price_card": self.price_card.provenance() if self.price_card else None,
            "by_module": {
                key: self._aggregate(value, scenarios) for key, value in sorted(modules.items())
            },
            "by_model": {
                key: self._aggregate(value, scenarios) for key, value in sorted(models.items())
            },
            "by_module_model": {
                module: {
                    model: self._aggregate(group, scenarios)
                    for model, group in sorted(model_groups.items())
                }
                for module, model_groups in sorted(module_models.items())
            },
            "total": self._aggregate(rows, scenarios),
        }

    def purpose_summary(self) -> dict[str, object]:
        """Additive host attribution view; never infer purpose from model output.

        Missing legacy attribution remains unknown. Each response primary key is
        counted once; cached/reasoning usage remains a subset, not extra tokens.
        This view uses the same frozen price card and reducer as summary().
        """
        dimensions = ('phase', 'segment_id', 'problem', 'role', 'purpose', 'session_id')
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM calls ORDER BY call_id").fetchall()
            calls = [self._one_call(connection, row['call_id']) for row in rows]
        groups: dict[tuple[str, ...], list[sqlite3.Row]] = {}
        for row in rows:
            metadata = json.loads(row['metadata_json'])
            key = tuple(metadata.get(field) if isinstance(metadata.get(field), str)
                        and metadata[field] else 'unknown' for field in dimensions) + (row['model'],)
            groups.setdefault(key, []).append(row)
        return {
            'attribution_policy': 'Host dispatch metadata only; mixed calls are not semantically split. Missing legacy fields remain unknown.',
            'token_policy': 'Input includes cached input; output includes reasoning output. Subsets are not added twice.',
            'billing_policy': 'Frozen price-card API-equivalent estimates; actual subscription billing remains unknown.',
            'price_card': self.price_card.provenance() if self.price_card else None,
            'groups': [dict(zip((*dimensions, 'model'), key),
                            response_ids=[row['call_id'] for row in group],
                            totals=self._aggregate(group)) for key, group in sorted(groups.items())],
            'responses': calls,
            'total': self._aggregate(rows),
        }

    def _aggregate(
        self, rows: list[sqlite3.Row], scenarios: tuple[str, ...] = ()
    ) -> dict[str, object]:
        statuses: dict[str, int] = {}
        bases: dict[str, int] = {}
        usage: dict[str, object] = {}
        all_terminal = all(row["status"] in TERMINAL_STATUSES for row in rows)
        for row in rows:
            statuses[row["status"]] = statuses.get(row["status"], 0) + 1
            bases[row["basis"]] = bases.get(row["basis"], 0) + 1
        for metric in METRICS:
            observed = sum(row[metric + "_observed"] for row in rows)
            complete = all_terminal and all(bool(row[metric + "_known"]) for row in rows)
            usage[metric] = observed if complete else None
            usage[metric + "_observed_lower_bound"] = observed
            usage[metric + "_complete"] = complete
        usage["total_tokens"] = (
            usage["input_tokens"] + usage["output_tokens"]
            if usage["input_tokens"] is not None and usage["output_tokens"] is not None
            else None
        )
        usage["total_tokens_observed_lower_bound"] = (
            usage["input_tokens_observed_lower_bound"]
            + usage["output_tokens_observed_lower_bound"]
        )
        usage["total_tokens_complete"] = (
            usage["input_tokens_complete"] and usage["output_tokens_complete"]
        )

        cost_fields = self._aggregate_costs(rows, all_terminal=all_terminal)

        billed_values = [
            Decimal(row["actual_billed_usd"])
            for row in rows
            if row["actual_billed_usd"] is not None
        ]
        billed_exact = (
            sum(billed_values, Decimal(0))
            if len(billed_values) == len(rows) and all_terminal
            else None
        )
        result = {
            "call_count": len(rows),
            "status_counts": dict(sorted(statuses.items())),
            "basis_counts": dict(sorted(bases.items())),
            "in_flight_or_unknown_call_count": sum(
                row["status"] not in TERMINAL_STATUSES for row in rows
            ),
            "missing_usage_call_count": sum(
                not self._has_any_usage(row) for row in rows
            ),
            "usage": usage,
            **cost_fields,
            "actual_billed_usd": _money(billed_exact),
            "actual_billed_usd_observed_lower_bound": _money(
                sum(billed_values, Decimal(0)) if billed_values or not rows else None
            ),
            "actual_billed_usd_is_final": billed_exact is not None,
        }
        if scenarios:
            result["api_equivalent_service_tier_scenarios"] = {
                tier: self._aggregate_costs(
                    rows, all_terminal=all_terminal, service_tier_override=tier
                )
                for tier in scenarios
            }
        return result

    def _aggregate_costs(
        self,
        rows: list[sqlite3.Row],
        *,
        all_terminal: bool,
        service_tier_override: str | None = None,
    ) -> dict[str, object]:
        exact_costs: list[Decimal] = []
        lower_costs: list[Decimal] = []
        unpriced = 0
        for row in rows:
            tier = (
                service_tier_override
                if service_tier_override is not None
                else row["service_tier"]
            )
            if (
                self.price_card is None
                or row["model"] not in self.price_card.models
                or tier not in self.price_card.service_multipliers
            ):
                unpriced += 1
            exact, lower = self._call_cost(row, service_tier_override=service_tier_override)
            if exact is not None:
                exact_costs.append(exact)
            if lower is not None:
                lower_costs.append(lower)
        exact_final = (
            sum(exact_costs, Decimal(0))
            if len(exact_costs) == len(rows) and all_terminal
            else None
        )
        observed_exact = (
            sum(exact_costs, Decimal(0)) if exact_costs else (Decimal(0) if not rows else None)
        )
        return {
            "api_equivalent_usd": _money(exact_final),
            "api_equivalent_usd_observed_exact_subset": _money(observed_exact),
            "api_equivalent_usd_observed_lower_bound": _money(
                sum(lower_costs, Decimal(0)) if lower_costs or not rows else None
            ),
            "api_equivalent_usd_is_final": exact_final is not None,
            "unpriced_call_count": unpriced,
        }

    def _call_cost(
        self, row: sqlite3.Row, *, service_tier_override: str | None = None
    ) -> tuple[Decimal | None, Decimal | None]:
        if self.price_card is None:
            return None, None
        rates = self.price_card.models.get(row["model"])
        tier = service_tier_override if service_tier_override is not None else row["service_tier"]
        service = self.price_card.service_multipliers.get(tier)
        if rates is None or service is None:
            return None, None
        if not self._has_any_usage(row):
            return None, None

        values = {metric: row[metric + "_observed"] for metric in METRICS}
        known = {metric: bool(row[metric + "_known"]) for metric in METRICS}
        input_known = known["input_tokens"]
        guaranteed_long = values["input_tokens"] > self.price_card.threshold
        exact_long: bool | None = guaranteed_long if input_known else (True if guaranteed_long else None)

        def multiplier(bucket: str, *, exact: bool) -> Decimal:
            long_multiplier = self.price_card.long_multipliers[bucket]
            if exact:
                assert exact_long is not None
                return long_multiplier if exact_long else Decimal(1)
            if guaranteed_long:
                return long_multiplier
            return min(Decimal(1), long_multiplier)

        exact: Decimal | None = None
        if (
            input_known
            and known["cached_input_tokens"]
            and known["cache_write_input_tokens"]
            and known["output_tokens"]
        ):
            uncached = (
                values["input_tokens"]
                - values["cached_input_tokens"]
                - values["cache_write_input_tokens"]
            )
            exact = service * (
                Decimal(uncached) * rates["input"] * multiplier("input", exact=True)
                + Decimal(values["cached_input_tokens"])
                * rates["cached_input"]
                * multiplier("cached_input", exact=True)
                + Decimal(values["cache_write_input_tokens"])
                * rates["cache_write"]
                * multiplier("cache_write", exact=True)
                + Decimal(values["output_tokens"])
                * rates["output"]
                * multiplier("output", exact=True)
            ) / MILLION

        if exact is not None and row["status"] in TERMINAL_STATUSES:
            return exact, exact

        input_observed = values["input_tokens"]
        cached_observed = values["cached_input_tokens"]
        write_observed = values["cache_write_input_tokens"]
        other_observed = max(0, input_observed - cached_observed - write_observed)
        cheapest_other = min(
            rates["input"] * multiplier("input", exact=False),
            rates["cached_input"] * multiplier("cached_input", exact=False),
            rates["cache_write"] * multiplier("cache_write", exact=False),
        )
        lower = service * (
            Decimal(cached_observed)
            * rates["cached_input"]
            * multiplier("cached_input", exact=False)
            + Decimal(write_observed)
            * rates["cache_write"]
            * multiplier("cache_write", exact=False)
            + Decimal(other_observed) * cheapest_other
            + Decimal(values["output_tokens"])
            * rates["output"]
            * multiplier("output", exact=False)
        ) / MILLION
        return exact, lower

    @staticmethod
    def _has_any_usage(row: sqlite3.Row) -> bool:
        return any(
            bool(row[metric + "_known"]) or row[metric + "_observed"] > 0
            for metric in METRICS
        )


# Short alias for callers that prefer the domain noun.
UsageLedger = APIAccountingLedger


__all__ = [
    "APIAccountingLedger",
    "UsageLedger",
    "PriceCard",
    "normalize_usage",
]
