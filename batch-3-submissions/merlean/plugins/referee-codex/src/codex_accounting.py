"""Automatic host-only accounting for isolated Codex stages.

Only exact response usage is ingested. CLI turn aggregates are never deltas.
The stage register tracks incomplete metering separately from response calls.
"""
from __future__ import annotations

from contextlib import closing
import datetime
import fcntl
import hashlib
import json
from pathlib import Path
import sqlite3
from typing import Any, Mapping

from api_accounting import APIAccountingLedger, METRICS


def _write(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + '.next')
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    temporary.replace(path)


def _instant(value: str) -> datetime.datetime:
    result = datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('timestamp lacks timezone')
    return result


def account_stage(root: Path, meta: Mapping[str, Any], audit: Mapping[str, Any],
                  *, price_card: Path | None = None) -> dict[str, Any]:
    """Persist evidence and idempotently collect responses, including failed stages.

    Calls with missing usage, identity, or a truncated audit remain explicitly
    unmetered. Accounting failures are durable metadata, never guessed zeroes.
    """
    directory = root / 'accounting'
    directory.mkdir(parents=True, exist_ok=True)
    records = audit.get('response_usage_records', [])
    evidence = root / meta['artifact_directory'] / 'stage.response-usage.json'
    _write(evidence, records)
    with (directory / 'collector.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        errors: list[str] = []
        response_ids: set[str] = set()
        encountered_response_ids: set[str] = set()
        ledger = APIAccountingLedger(directory / 'usage.sqlite3', price_card)
        for record in records:
            try:
                payload = record['payload']
                response_id = payload.get('response_id')
                if not isinstance(response_id, str) or not response_id.strip():
                    raise ValueError('missing response identity')
                if not meta.get('session_id') or payload.get('thread_id') != meta['session_id']:
                    raise ValueError('response session identity mismatch')
                when = _instant(record['timestamp'])
                if when < _instant(meta['start_utc']) or (meta.get('end_utc') and when > _instant(meta['end_utc'])):
                    raise ValueError('response outside stage time window')
                model = record.get('model')
                if not isinstance(model, str) or not model.strip():
                    raise ValueError('missing actual response model')
                problem = meta['name'].split('/')[0]
                role = meta['module']
                identity = {'problem': problem, 'role': role, 'stage': meta['name'],
                            'session_id': meta['session_id'], 'turn_id': payload.get('turn_id'),
                            'timestamp': record['timestamp'], 'model_requested': meta['model_requested']}
                context = meta.get('accounting_context')
                if context is not None:
                    if (not isinstance(context, dict) or set(context) != {'phase', 'segment_id', 'purpose'}
                            or any(not isinstance(value, str) or not value.strip() for value in context.values())):
                        raise ValueError('invalid host accounting context')
                    identity.update(context)
                if not identity['turn_id']:
                    raise ValueError('missing turn identity')
                encountered_response_ids.add(response_id)
                ledger.record(call_id=response_id,
                              module='/'.join((problem, role, meta['session_id'])),
                              model=model, usage=payload.get('usage'), status='complete',
                              basis=('api_token_usage' if meta.get('authentication') == 'api' else 'subscription_api_equivalent'), service_tier='standard',
                              metadata=identity, usage_format='codex_flat', event_id=response_id)
                response_ids.add(response_id)
                if not isinstance(payload.get('usage'), dict) or not all(key in payload['usage'] for key in METRICS):
                    errors.append('missing or partial response usage: ' + response_id)
                if model != meta['model_requested']:
                    errors.append('actual model differs from requested model: ' + response_id)
            except (KeyError, TypeError, ValueError) as error:
                errors.append(str(error))
        complete = bool(response_ids) and not errors and audit.get('status') == 'verified' and meta.get('turn_completed') is True and meta.get('status') == 'completed'
        receipt = {'stage': meta['name'], 'status': meta['status'],
                   'session_id': meta.get('session_id'), 'model_requested': meta['model_requested'],
                   'response_ids': sorted(response_ids), 'encountered_response_ids': sorted(encountered_response_ids), 'metering': 'observed' if complete else 'unknown',
                   'errors': errors, 'authentication': meta.get('authentication', 'chatgpt'),
                   'actual_billed_usd': None, 'actual_subscription_billed_usd': None,
                   'accounting_context': meta.get('accounting_context'),
                   'problem': meta['name'].split('/')[0], 'role': meta['module']}
        with closing(sqlite3.connect(directory / 'usage.sqlite3')) as connection:
            connection.execute('CREATE TABLE IF NOT EXISTS codex_stages (stage TEXT PRIMARY KEY, receipt TEXT NOT NULL)')
            connection.execute('INSERT OR REPLACE INTO codex_stages VALUES (?, ?)', (meta['name'], json.dumps(receipt)))
            connection.commit()
            stages = [json.loads(row[0]) for row in connection.execute('SELECT receipt FROM codex_stages ORDER BY stage')]
        summary = {'scope': 'Transport-owned stages only; excludes orchestration, setup, external monitors and other sessions.',
                   'usage_source': 'Exact token_usage_record.payload.usage; response_id deduplication.',
                   'billing': 'Token usage evidence and optional price-card estimates only; actual billed USD unknown.',
                   'pending_or_unmetered_stages': [stage for stage in stages if stage['metering'] == 'unknown'],
                   'ledger': ledger.summary()}
        attribution = ledger.purpose_summary()
        attribution['stage_receipts'] = stages
        attribution['response_stage_aliases'] = {
            response_id: [stage['stage'] for stage in stages if response_id in stage.get('encountered_response_ids', stage['response_ids'])]
            for response_id in sorted({response_id for stage in stages for response_id in stage.get('encountered_response_ids', stage['response_ids'])})}
        attribution['pending_or_unmetered_stages'] = summary['pending_or_unmetered_stages']
        attribution['metering_complete'] = not summary['pending_or_unmetered_stages']
        _write(directory / 'role-cost-summary.json', attribution)
        summary['role_cost_summary'] = 'role-cost-summary.json'
        summary['segment_metering_complete'] = not summary['pending_or_unmetered_stages']
        summary['metering_complete'] = summary['segment_metering_complete']
        summary['ledger_scope'] = 'Current segment only; historical segment totals are preserved separately and are not added without response-ID reconciliation.'
        history_path = root.parent / 'history/accounting/summary.json'
        if history_path.is_file():
            raw_history = history_path.read_bytes()
            try:
                history = json.loads(raw_history)
                if not isinstance(history, dict):
                    raise ValueError('historical accounting summary must be an object')
            except (UnicodeDecodeError, ValueError):
                history = {'metering_complete': False, 'error': 'historical accounting summary is unreadable'}
            summary['historical_accounting'] = {
                'path': '../history/accounting/summary.json',
                'sha256': hashlib.sha256(raw_history).hexdigest(),
                'summary': history,
                'totals_policy': 'Preserved parent report, including earlier lineage. No cross-segment summation or deduplication is claimed.',
            }
            # Older passive reports lack a complete-metering proof, even when
            # their observed response subset has an exact sum or is_final=true.
            summary['metering_complete'] = summary['segment_metering_complete'] and history.get('metering_complete') is True
        elif (root.parent / 'history/accounting').exists():
            summary['historical_accounting'] = {'path': '../history/accounting/summary.json',
                                                'metering_complete': False,
                                                'error': 'historical accounting summary missing'}
            summary['metering_complete'] = False
        _write(directory / 'summary.json', summary)
        return receipt
