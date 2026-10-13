"""Deterministic offline summaries of recorded activity and evidence; no control authority."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from pilot_timing_analysis import snapshot

MAX_BYTES = 32 * 1024 * 1024
MAX_ITEMS = 100000
FILES = {'activity': 'host-progress.json', 'convergence': 'research-convergence.json',
         'continuation': 'research-continuation-state.json', 'exhaustion': 'review-exhaustion.json'}
SEMANTICS = {
    'process_activity': 'Completed calls are recorded process outcomes, not accepted scientific results.',
    'retained_work': 'Distinct retained records are not independently established novelty or progress.',
    'artifact_state': 'Distinct bindings or changed bytes are not mathematical improvement.',
    'independent_evidence': 'References and deficit statuses are recorded host state, not revalidated receipts or new acceptance.',
    'delivery': 'Required-material delivery receipts do not establish comprehension, attention, or complete retained model context.',
    'exhaustion': 'Bounded review exhaustion without a verdict is not mathematical rejection.',
    'deduplication': 'Dispatch request deduplication does not establish identical reasoning or absence of useful work.',
    'persistence': 'Unchanged-step counts are observations, not stopping thresholds or scientific judgments.',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def object_value(value):
    if not isinstance(value, dict):
        raise ValueError('object_required')
    return value


def collection(value, kind):
    if not isinstance(value, kind) or len(value) > MAX_ITEMS:
        raise ValueError('bounded_collection_required')
    return value


def hash_value(value):
    if not isinstance(value, str) or not re.fullmatch('[0-9a-f]{64}', value):
        raise ValueError('hash_required')
    return value


def count_value(value):
    if type(value) is not int or not 0 <= value <= MAX_ITEMS:
        raise ValueError('bounded_count_required')
    return value


def no_symlink_ancestors(path):
    for part in (Path(path).absolute(), *Path(path).absolute().parents):
        if part.is_symlink():
            raise ValueError('symlink_path_refused')


def activity(value):
    calls = collection(object_value(value).get('calls'), list)
    statuses = {key: 0 for key in ('completed', 'running', 'timeout', 'failed', 'cancelled', 'unknown')}
    delivery = {'recorded_true': 0, 'recorded_false': 0, 'unknown': 0}
    identities = set()
    for call in calls:
        call = object_value(call)
        # Identity is used only to reject duplicated records; never emitted.
        name = call.get('name')
        if not isinstance(name, str) or not 1 <= len(name) <= 200 or name in identities:
            raise ValueError('invalid_or_duplicate_call_identity')
        identities.add(name)
        status = call.get('status')
        status = {'timeout_censored': 'timeout', 'process_failed': 'failed', 'process_launch_failed': 'failed', 'transport_io_failed': 'failed', 'host_cancelled': 'cancelled'}.get(status, status) if isinstance(status, str) else None
        statuses[status if isinstance(status, str) and status in statuses else 'unknown'] += 1
        audit = call.get('document_audit')
        delivered = audit.get('required_material_delivered') if isinstance(audit, dict) else None
        delivery['recorded_true' if delivered is True else 'recorded_false' if delivered is False else 'unknown'] += 1
    return {'recorded_calls': len(calls), 'recorded_status_counts': statuses,
            'required_material_delivery_receipts': delivery, 'accepted_results_inferred': False}


def convergence(value, *, indexed=False):
    value = object_value(value)
    candidates = collection(value.get('candidates'), dict)
    current = hash_value(value.get('current_candidate_sha256'))
    for key in candidates:
        hash_value(key)
    record = object_value(candidates.get(current))
    if record.get('candidate_sha256') != current:
        raise ValueError('current_candidate_binding_mismatch')
    observations = collection(value.get('observations'), dict)
    for table in ('candidates', 'observations', 'research_archive', 'auxiliary_archive'):
        for key, entry in collection(value.get(table), dict).items():
            hash_value(key)
            entry = object_value(entry)
            if indexed and not (table == 'candidates' and key == current):
                if set(entry) != {'record_sha256'}:
                    raise ValueError('malformed_index_entry')
                hash_value(entry['record_sha256'])
            else:
                hash_value(entry.get('candidate_sha256'))
                if table == 'research_archive':
                    object_value(entry.get('work'))
    refs = object_value(record.get('observation_refs'))
    selected = {}
    for domain in ('review', 'comprehensive_review', 'scope', 'advisory_scope', 'certification', 'delivery'):
        if domain in refs:
            ref = hash_value(refs[domain])
            obs = object_value(observations.get(ref))
            if indexed:
                hash_value(obs.get('record_sha256'))
            elif obs.get('candidate_sha256') != current:
                raise ValueError('stale_observation_binding')
            selected[domain] = ref
    deficits = object_value(record.get('deficits'))
    states = {}
    for domain in ('original_scope', 'mathematical', 'certification', 'delivery'):
        status = object_value(deficits.get(domain)).get('status')
        if status not in ('open', 'closed', 'unknown'):
            raise ValueError('invalid_deficit_status')
        states[domain] = status
    return {'current_candidate_sha256': current,
            'distinct_archived_candidate_bindings': len(candidates),
            'retained_research_records': len(collection(value.get('research_archive'), dict)),
            'retained_auxiliary_records': len(collection(value.get('auxiliary_archive'), dict)),
            'recorded_observations': len(observations), 'current_recorded_observation_refs': selected,
            'current_recorded_deficit_statuses': states,
            'independence_revalidated': False, 'acceptance_inferred': False}


def continuation(value):
    value = object_value(value)
    return {'recorded_step': count_value(value.get('step')),
            'recorded_unchanged_binding_steps': count_value(value.get('unchanged_binding_steps')),
            'current_candidate_sha256': hash_value(object_value(value.get('bindings')).get('candidate_sha256')),
            'stop_or_dispatch_authority': False}


def exhaustion(value):
    values = collection(value, list)
    ids = set()
    delivered = {'recorded_true': 0, 'recorded_false': 0, 'unknown': 0}
    for item in values:
        item = object_value(item)
        ident = hash_value(item.get('id'))
        if ident in ids:
            raise ValueError('duplicate_exhaustion_record')
        ids.add(ident)
        delivery = item.get('required_material_delivered')
        delivered['recorded_true' if delivery is True else 'recorded_false' if delivery is False else 'unknown'] += 1
    return {'recorded_exhaustion_records': len(values), 'required_material_delivery_receipts': delivered,
            'exhaustion_reauthenticated': False, 'mathematical_rejection_inferred': False}


def report(problem):
    """Only whole, twice-identical bounded file snapshots are parsed; no raw prose output."""
    problem = Path(problem)
    no_symlink_ancestors(problem)
    results, sources, issues = {}, {}, {}
    for kind, filename in FILES.items():
        try:
            raw, receipt = snapshot(problem / filename, MAX_BYTES)
            # Do not emit file paths, timestamps, arbitrary errors or any source payload.
            sources[kind] = {key: receipt[key] for key in ('prefix_sha256', 'prefix_bytes', 'size_before', 'size_after', 'whole_file_at_snapshot')}
            if not receipt['whole_file_at_snapshot'] or receipt['grew']:
                raise ValueError('incomplete_snapshot')
            value = json.loads(raw)
            if kind == 'convergence' and isinstance(value, dict) and 'state_sha256' in value:
                ref = hash_value(value['state_sha256'])
                archive = problem / 'convergence-archive'
                if archive.is_symlink() or (archive / 'records').is_symlink():
                    raise ValueError('archive_symlink')
                manifest_raw, manifest_receipt = snapshot(archive / (ref + '.json'), MAX_BYTES)
                if not manifest_receipt['whole_file_at_snapshot'] or manifest_receipt['grew']:
                    raise ValueError('incomplete_manifest')
                manifest = object_value(json.loads(manifest_raw))
                sources['convergence_manifest'] = {'sha256': sha(manifest_raw), 'bytes': len(manifest_raw)}
                if manifest.get('storage_format') != 'individual_records_v1':
                    raise ValueError('unsupported_archive_format')
                state = object_value(manifest.get('state'))
                current = hash_value(state.get('current_candidate_sha256'))
                candidates = collection(state.get('candidates'), dict)
                record_ref = hash_value(object_value(candidates.get(current)).get('record_sha256'))
                record_raw, record_receipt = snapshot(archive / 'records' / (record_ref + '.json'), MAX_BYTES)
                if not record_receipt['whole_file_at_snapshot'] or record_receipt['grew']:
                    raise ValueError('incomplete_current_record')
                record = object_value(json.loads(record_raw))
                # Record hashes use the maintained canonical JSON representation.
                if sha((json.dumps(record, ensure_ascii=False, indent=2) + '\n').encode()) != record_ref:
                    raise ValueError('current_record_hash_mismatch')
                sources['convergence_current_record'] = {'sha256': sha(record_raw), 'bytes': len(record_raw)}
                state['candidates'] = {**candidates, current: record}
                results[kind] = convergence(state, indexed=True)
                results[kind]['archive_scope'] = 'manifest_and_current_record_only_full_state_not_reauthenticated'
            else:
                results[kind] = globals()[kind](value)
        except FileNotFoundError:
            results[kind] = None; issues[kind] = 'missing_record'
        except (OSError, ValueError, TypeError, KeyError, RecursionError):
            results[kind] = None; issues[kind] = 'invalid_unstable_or_bounded_record'
    left, right = results.get('convergence'), results.get('continuation')
    coherent = None
    if left is not None and right is not None:
        coherent = left['current_candidate_sha256'] == right['current_candidate_sha256']
        if not coherent:
            issues['cross_file_candidate'] = 'different_recorded_bindings_no_atomic_snapshot_claim'
    return {'schema_version': 1, 'status': 'PARTIAL_OR_INCONSISTENT' if issues else 'RECORDED_STATE_SUMMARIZED',
            'authority': 'observation_only_no_acceptance_dispatch_or_stop',
            'analyzer_sha256': sha(Path(__file__).read_bytes()),
            'snapshot_reader_sha256': sha(Path(__file__).with_name('pilot_timing_analysis.py').read_bytes()),
            'limits': {'max_file_bytes': MAX_BYTES, 'max_collection_items': MAX_ITEMS},
            'sources': sources, 'issues': issues, 'recorded_candidate_bindings_agree': coherent,
            'atomic_campaign_snapshot': False, 'history_scope': 'Cumulative saved records may include inherited history; not a current-run or time-window census.', 'semantics': SEMANTICS, 'dimensions': results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--problem', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(argv)
    no_symlink_ancestors(args.problem)
    no_symlink_ancestors(args.output)
    root = args.problem.resolve()
    # Standard campaign/problems/problem layout: forbid the entire run.
    forbidden = root.parents[2] if len(root.parents) > 2 and root.parent.name == 'problems' and root.parents[1].name == 'campaign' else root
    if args.output.resolve().is_relative_to(forbidden):
        parser.error('output must be outside the input run/problem')
    result = report(args.problem)
    data = (json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + '\n').encode()
    fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data)
    print(json.dumps({'status': result['status'], 'report_sha256': sha(data), 'report_bytes': len(data)}))


if __name__ == '__main__':
    main()
