"""Read-only validation and restoration of a stopped pilot segment.

Creating a continuation is an explicit host operation. This module never launches
models, changes the parent run, releases claims, or resets a parent budget.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import shlex
import time
from typing import Any


_NUMBERED = re.compile(r'^(\d+)-')


def _json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError('expected JSON object: ' + path.name)
    return value


def _local_module_registry(folder: Path, progress: dict[str, Any]) -> list[dict[str, Any]]:
    """Read the list-shaped registry without weakening object control-file readers.

    Records are retained verbatim. These are structural/history checks, never
    retroactive scientific approval or permission to resume a stopped module.
    """
    path = folder / 'local-verification-modules.json'
    modules = json.loads(path.read_text(encoding='utf-8')) if path.is_file() else []
    if not isinstance(modules, list) or any(not isinstance(m, dict) for m in modules):
        raise ValueError('local module registry must be a JSON array of objects')
    checkpoint = progress.get('local_verification_modules', [])
    if not isinstance(checkpoint, list) or any(not isinstance(m, dict) for m in checkpoint):
        raise ValueError('checkpoint local module registry must be a JSON array of objects')
    if modules != checkpoint:
        raise ValueError('local module history differs from terminal checkpoint; reconciliation required')
    seen, latest = {}, {}
    for record in modules:
        ident, lineage, generation = (record.get(k) for k in ('module_id', 'lineage_id', 'generation'))
        if (not isinstance(lineage, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', lineage)
                or type(generation) is not int or generation < 1
                or ident != lineage + '-g' + str(generation) or ident in seen):
            raise ValueError('invalid or duplicate local module identity')
        prior = latest.get(lineage)
        if ((prior is None and (generation != 1 or record.get('parent_module_id') is not None))
                or (prior is not None and (generation != prior['generation'] + 1
                    or record.get('parent_module_id') != prior['module_id']))
                or record.get('inherited_counters_from') not in (None, prior['module_id'] if prior else None)):
            raise ValueError('local module lineage or inherited history is inconsistent')
        for key in ('claim_sha256', 'premises_sha256', 'task_sha256', 'candidate_binding'):
            if not isinstance(record.get(key), str) or not re.fullmatch(r'[0-9a-f]{64}', record[key]):
                raise ValueError('local module exact binding is malformed: ' + key)
        limits = record.get('limits')
        if (not isinstance(limits, dict) or set(limits) != {'max_worker_calls', 'max_probe_runs'}
                or any(type(limits[k]) is not int or limits[k] < 1 for k in limits)
                or any(type(record.get(k)) is not int or record[k] < 0 for k in ('worker_calls', 'probe_runs'))
                or record.get('counter_semantics') not in (None, 'lineage_total')
                or record.get('state') not in ('working', 'returned_to_main', 'awaiting_retriage')):
            raise ValueError('local module state or consumed budget is malformed')
        if (not isinstance(record.get('approval_receipt'), dict)
                or any(not isinstance(record.get(k), list) or any(not isinstance(x, dict) for x in record[k])
                       for k in ('stages', 'returns'))):
            raise ValueError('local module approval or retained evidence is malformed')
        if record.get('artifact_root') != 'local-verification/' + ident:
            raise ValueError('local module artifact root is not its canonical confined path')
        artifact = folder / record['artifact_root'] / 'module.json'
        if (artifact.is_symlink() or not artifact.resolve().is_relative_to(folder.resolve())
                or not artifact.is_file() or _json(artifact) != record):
            raise ValueError('local module artifact differs from registry history')
        seen[ident] = record
        latest[lineage] = record
    # Validate legacy reset/inherited accounting without rewriting historical totals.
    from pilot_local_verification import lineage_counters
    for record in latest.values():
        lineage_counters(modules, record)
    return modules


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _pid(value: Any) -> int:
    if type(value) is not int or value <= 1:
        raise ValueError('reconciliation requires positive process IDs greater than one')
    return value


class _ProcessPresent(ValueError):
    pass


def _assert_stopped(pid: int) -> None:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return
    except PermissionError as error:
        raise ValueError('cannot establish that owned process stopped') from error
    raise _ProcessPresent('owned process still exists: ' + str(pid))


def _nested_pids(value: Any) -> set[int]:
    result: set[int] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {'pid', 'host_pid', 'probe_pid', 'child_pid'} and item is not None:
                result.add(_pid(item))
            elif isinstance(item, (dict, list)):
                result.update(_nested_pids(item))
    elif isinstance(value, list):
        for item in value:
            result.update(_nested_pids(item))
    return result


def _aware_time(value: Any) -> datetime:
    try:
        result = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    except ValueError as error:
        raise ValueError('missing or invalid process evidence timestamp') from error
    if result.tzinfo is None:
        raise ValueError('process evidence timestamp requires timezone')
    return result


def _ps_birth(value: str) -> datetime:
    try:
        # ps lstart is local wall time; astimezone applies the local offset at birth.
        return datetime.strptime(value, '%a %b %d %H:%M:%S %Y').astimezone(timezone.utc)
    except ValueError as error:
        raise ValueError('cannot establish current process birth time') from error


def _opaque_review_chunks(source: Path) -> set[Path]:
    """Authenticate raw reviewer chunks without treating their bytes as metadata.

    Historical reviewer input writers used .json for text slices as well as full
    JSON parents. Only typed capability-bound slices are opaque; complete parents
    remain in the ordinary strict JSON/PID census, even if also a whole-size chunk.
    """
    from pilot_document_tools import CHUNK_ID, chunk_bindings, validate_scope
    source = source.resolve(strict=True)
    opaque, parents = set(), set()
    for capability in (source / 'host/runtime').glob('*/*/document-capability.json'):
        if capability.is_symlink():
            raise ValueError('symlink document capability is not allowed')
        scope = _json(capability)
        artifacts = scope.get('readonly_artifacts')
        if not isinstance(artifacts, dict):
            raise ValueError('invalid persisted document artifact capability')
        candidates = [ident for ident, entry in artifacts.items()
                      if isinstance(ident, str) and CHUNK_ID.fullmatch(ident)
                      and isinstance(entry, dict) and Path(entry.get('path', '')).suffix == '.json']
        historical = [ident for ident, entry in artifacts.items()
                      if isinstance(ident, str) and ident.startswith('historical-source:')
                      and isinstance(entry, dict) and Path(entry.get('path', '')).suffix == '.json']
        preserved = [ident for ident in artifacts
                     if ident in ('preserved-author:raw', 'preserved-author:pre-shrink')]
        if not candidates and not historical and not preserved:
            continue
        stage_path = capability.with_name('stage.meta.json')
        stage = _json(stage_path)
        stage_name = str(capability.parent.relative_to(source / 'host/runtime'))
        problem_id = capability.parent.parent.name
        namespace = ('exam', 'papers') if preserved else ('campaign', 'problems')
        folder = source.joinpath(*namespace, problem_id)
        declared_folder = Path(scope.get('store_root', ''))
        if (not declared_folder.is_absolute()
                or declared_folder.parts[-3:] != (*namespace, problem_id)):
            raise ValueError('opaque review chunk has invalid historical store namespace')
        if declared_folder != folder:
            # Continuations copy historical capabilities verbatim. Rebase only
            # exact locally copied bytes proven by the immediate parent manifest;
            # never read a historical absolute path merely because it is declared.
            inherited = _json(source / 'continuation-parent.json')
            files = inherited.get('files')
            if (not isinstance(files, dict) or hashlib.sha256(json.dumps(files, sort_keys=True,
                    separators=(',', ':')).encode()).hexdigest() != inherited.get('manifest_sha256')):
                raise ValueError('inherited opaque chunk lacks exact parent manifest')
            def inherited_file(path):
                if path.resolve() != path or not path.is_relative_to(source):
                    raise ValueError('inherited opaque evidence path is not canonical and local')
                if files.get(str(path.relative_to(source))) != _hash(path):
                    raise ValueError('inherited opaque chunk or capability differs from parent manifest')
            inherited_file(capability); inherited_file(stage_path)
            rebased = {}
            for ident, entry in artifacts.items():
                declared = Path(entry['path'])
                if not declared.is_relative_to(declared_folder):
                    raise ValueError('inherited opaque chunk capability leaves its problem namespace')
                local = folder / declared.relative_to(declared_folder)
                inherited_file(local)
                rebased[ident] = {**entry, 'path': str(local)}
            if 'public_source_store' in scope:
                if scope['public_source_store'] != str(declared_folder / 'public-sources'):
                    raise ValueError('inherited public source store leaves its historical namespace')
                scope = {**scope, 'public_source_store': str(folder / 'public-sources')}
            scope = {**scope, 'store_root': str(folder), 'readonly_artifacts': rebased,
                     'receipt_path': str(capability.with_name('document-operations.jsonl'))}
            artifacts = rebased
        validate_scope(scope)
        if ((candidates and scope['mode'] != 'review') or scope['problem_id'] != problem_id
                or Path(scope['store_root']) != folder
                or scope['producer']['stage'] != stage_name or stage.get('name') != stage_name
                or not scope['producer']['request_id']
                or scope['producer']['request_id'] != stage.get('request_id')
                or (scope['producer']['session_id'] is not None
                    and scope['producer']['session_id'] != stage.get('session_id'))):
            raise ValueError('opaque review chunk lacks exact stage capability binding')
        if preserved:
            # Older author restoration used _artifact's JSON default for TeX.
            # Only these typed, transport-bound author artifacts are opaque.
            role = re.fullmatch(r'paper-\d+-(polish|revise-[12]|repair-.+)', capability.parent.name)
            if (not role or stage.get('module') != 'paper-' + role[1]
                    or scope['mode'] != 'review' or candidates or historical
                    or not scope['producer']['session_id']
                    or stage.get('document_capability', {}).get('sha256') != _hash(capability)):
                raise ValueError('preserved author text lacks authenticated author capability')
            for ident in preserved:
                entry = artifacts[ident]; path = Path(entry['path'])
                if (entry['media_type'] not in ('text/plain', 'application/json')
                        or path.parent != folder / 'input-artifacts'
                        or path.name != entry['sha256'] + '.json'):
                    raise ValueError('preserved author text must be content-addressed local evidence')
                opaque.add(path)
        if historical:
            from pilot_public_sources import verify_public_source, _file
            from pilot_review_history_delivery import AUTHORITY, VERSION
            if stage.get('document_capability', {}).get('sha256') != _hash(capability):
                raise ValueError('historical source capability lacks transport hash binding')
            index_entry = artifacts.get('historical-review-index', {})
            index_path = Path(index_entry.get('path', ''))
            if (index_entry.get('media_type') != 'application/json'
                    or index_path.parent != folder/'historical-review-artifacts'
                    or index_path.name != index_entry.get('sha256', '')+'.json'):
                raise ValueError('historical source lacks exact typed index')
            index = _json(index_path)
            if index.get('schema_version') != VERSION or index.get('authority') != AUTHORITY:
                raise ValueError('historical source index identity differs')
            for ident in historical:
                parts = ident.split(':', 2)
                if len(parts) != 3 or not re.fullmatch(r'[0-9a-f]{64}', parts[1]):
                    raise ValueError('invalid historical source member identity')
                source_id, member_name = parts[1:]
                entry = artifacts[ident]; path = Path(entry['path'])
                if (entry['media_type'] != 'text/plain' or path.parent != folder/'historical-review-artifacts'
                        or path.name != entry['sha256']+'.json'):
                    raise ValueError('historical source member is not content-addressed text')
                sources = [item for item in index.get('public_sources', []) if item.get('source_id') == source_id]
                if len(sources) != 1:
                    raise ValueError('historical source index is ambiguous')
                checked = verify_public_source(folder/'public-sources', source_id)
                members = [m for m in sources[0].get('members', []) if m.get('artifact_id') == ident]
                if (checked.get('status') != 'downloaded' or checked['receipt_sha256'] != sources[0].get('receipt_sha256')
                        or len(members) != 1 or members[0].get('member') != member_name
                        or {k:v for k,v in members[0].items() if k != 'artifact_id'} not in checked['members']
                        or members[0].get('sha256') != entry['sha256']
                        or _file(folder/'public-sources'/source_id, member_name).read_bytes() != path.read_bytes()):
                    raise ValueError('historical source member differs from authenticated source packet')
                opaque.add(path)
        bindings = chunk_bindings(scope)
        for ident in candidates:
            parent_id = bindings[ident][0]
            entry, parent = artifacts[ident], artifacts[parent_id]
            paths = [Path(entry['path']), Path(parent['path'])]
            for path, artifact in zip(paths, (entry, parent)):
                if (path.parent != folder / 'review-evidence'
                        or not re.fullmatch(r'[0-9a-f]{64}\.json', path.name)
                        or path.stem != artifact['sha256']):
                    raise ValueError('opaque review chunk must bind content-addressed local evidence')
            if entry['media_type'] != 'text/plain' or parent['media_type'] != 'application/json':
                raise ValueError('opaque review chunk must bind a complete JSON parent')
            opaque.add(paths[0]); parents.add(paths[1])
    opaque -= parents
    # Exam snapshots copy the exact campaign evidence bytes, including typed
    # text slices historically named .json. Only aliases of already verified
    # opaque chunks qualify; snapshot control JSON and full parents stay strict.
    from pilot_exam import ExamRuntime
    aliases=set()
    for exam_root in (source/'exam',source/'history/prior-exam'):
        from pilot_paper_recovery import snapshot_paths
        for snapshot in snapshot_paths(source, exam_root):
            manifest_path=snapshot/'manifest.json'
            if snapshot.is_symlink() or manifest_path.is_symlink():
                raise ValueError('symlink paper snapshot evidence is not allowed')
            ExamRuntime.verify_snapshot(snapshot)
            manifest=_json(manifest_path)['files']
            problem_id=snapshot.parent.name
            folder=source/'campaign/problems'/problem_id
            for original in opaque:
                if not original.is_relative_to(folder):continue
                relative=Path('evidence')/original.relative_to(folder)
                alias=snapshot/relative
                if not alias.exists():continue
                if manifest.get(relative.as_posix())!=_hash(original) or _hash(alias)!=_hash(original):
                    raise ValueError('paper snapshot opaque alias differs from authenticated original')
                aliases.add(alias)
    return opaque | aliases



def _bound_external(ref: Any) -> Path:
    if not isinstance(ref, dict) or not isinstance(ref.get('path'), str):
        raise ValueError('bound external evidence reference required')
    path = Path(ref['path'])
    if (not path.is_absolute() or not path.is_file() or path.is_symlink()
            or any(parent.is_symlink() for parent in path.parents)
            or _hash(path) != ref.get('sha256')):
        raise ValueError('external evidence hash/path changed')
    return path


def _unambiguous_birth(value: str) -> datetime:
    # ps has local wall time, no UTC offset. Reject DST-fold ambiguity instead
    # of guessing which incarnation a repeated wall-clock value describes.
    parsed = time.strptime(value, '%a %b %d %H:%M:%S %Y')
    candidates = set()
    for dst in (0, 1):
        epoch = time.mktime((*parsed[:8], dst))
        if time.localtime(epoch)[:6] == parsed[:6]:
            candidates.add(epoch)
    if len(candidates) != 1:
        raise ValueError('ambiguous process birth wall time')
    birth = datetime.fromtimestamp(candidates.pop(), timezone.utc)
    if time.strftime('%a', time.localtime(birth.timestamp())) != value.split()[0]:
        raise ValueError('invalid process birth weekday')
    return birth


def _legacy_argv(stage: dict[str, Any]) -> list[str]:
    argv = stage.get('command')
    if (not isinstance(argv, list) or not argv
            or any(not isinstance(arg, str) or not arg or '\x00' in arg for arg in argv)
            or not Path(argv[0]).is_absolute() or not isinstance(stage.get('name'), str)
            or not stage['name'].strip() or not isinstance(stage.get('session_id'), str)
            or not stage['session_id'].strip()
            or stage.get('resume_session') is not None and
            (not isinstance(stage['resume_session'], str) or not stage['resume_session'].strip())):
        raise ValueError('legacy stage requires exact command/name/session evidence')
    if stage.get('resume_session') and stage['resume_session'] not in argv:
        raise ValueError('legacy resume session not bound to original command')
    return argv


def _legacy_absence(source, entry, owned, refs, ends, birth):
    witness_path = _bound_external(entry.get('prior_absence_receipt'))
    audit_path = _bound_external(entry.get('prior_absence_audit'))
    witness, audit = _json(witness_path), _json(audit_path)
    names = ('census', 'raw_census', 'reconciliation', 'terminal', 'sealed_files')
    paths = {name: _bound_external(witness.get(name)) for name in names}
    expected = {str(path): _hash(path) for path in [witness_path, *paths.values()]}
    if (witness.get('schema_version') != 1 or witness.get('source_root') != str(source)
            or audit.get('source_root') != str(source) or audit.get('status') != 'PASS'
            or audit.get('auditor') != 'independent' or audit.get('witness_sha256') != _hash(witness_path)
            or any(audit.get('artifacts', {}).get(name) != digest for name, digest in expected.items())):
        raise ValueError('legacy absence requires independently bound complete evidence')
    checked = _aware_time(witness.get('checked_utc'))
    if not max(ends) < checked < birth or not checked <= _aware_time(audit.get('checked_utc')) <= datetime.now(timezone.utc):
        raise ValueError('legacy absence does not intervene between historical end and current birth')
    census, prior, terminal, seal = (_json(paths[name]) for name in ('census', 'reconciliation', 'terminal', 'sealed_files'))
    if (any(obj.get('source_root') != str(source) for obj in (prior, terminal, seal))
            or witness.get('complete_process_census') is not True
            or witness.get('blockers') != [] or census.get('blockers') != []
            or terminal.get('status') != 'PASS' or terminal.get('live_owned_processes') != []
            or terminal.get('campaign_sealed') is not True or terminal.get('host_absent_both_censuses') is not True
            or census.get('host_absent') is not True
            or prior.get('active_children') != [] or prior.get('pending_launches') != []
            or terminal.get('reconciliation') != witness['reconciliation']
            or terminal.get('sealed_files') != witness['sealed_files']
            or census.get('census_file') != witness['raw_census']
            or _aware_time(census.get('checked_utc')) != checked
            or any(prior.get(key) is not True for key in ('descendants_checked', 'launch_records_checked', 'probe_records_checked',
                'all_owned_children_stopped', 'owned_process_groups_checked', 'document_mcp_segment_path_census_checked'))):
        raise ValueError('legacy absence census/terminal binding incomplete')
    prior_owned = {_pid(pid) for pid in prior.get('owned_pids', [])}
    if (not owned <= prior_owned or witness.get('owned_pids') != prior.get('owned_pids')
            or census.get('owned_pid_count') != len(prior_owned)):
        raise ValueError('legacy absence omits persisted ownership')
    present = set()
    for line in paths['raw_census'].read_text().splitlines():
        fields = line.split(None, 8)
        if len(fields) != 9:
            raise ValueError('incomplete prior process census')
        pid, parent, group = map(int, fields[:3])
        if pid <= 0 or parent < 0 or group <= 0 or pid in present or not fields[8].strip():
            raise ValueError('invalid prior process census')
        _unambiguous_birth(' '.join(fields[3:8]))
        present.add(pid)
    recorded = sorted(present & prior_owned)
    if (not present or entry['pid'] in present or census.get('process_count') != len(present)
            or census.get('recorded_present_pids') != recorded
            or witness.get('recorded_present_pids') != recorded):
        raise ValueError('prior census does not establish legacy PID absence')
    files = seal.get('files')
    if not isinstance(files, list) or any(not isinstance(item, dict) for item in files):
        raise ValueError('invalid prior seal file census')
    sealed = {item.get('path'): item.get('sha256') for item in files}
    if len(sealed) != len(files):
        raise ValueError('duplicate prior seal file')
    for ref in refs:
        if sealed.get(ref['path']) != ref['sha256']:
            raise ValueError('historical stage not bound by prior seal')
    return prior

def _opaque_public_source_files(source: Path) -> set[Path]:
    """Classify external bytes, without granting source or research authority.

    Only native stores qualify. Completed/failed receipts bind an exact payload
    census; an interrupted helper's confined bytes remain quarantined. Host
    admissions and helper lifetimes always pass through the ordinary PID census.
    """
    from pilot_public_sources import HEX, digest, source_content_files, verify_public_source
    from pilot_exam import ExamRuntime
    stores = list(source.glob('campaign/problems/*/public-sources'))
    for exam in (source/'exam', source/'history/prior-exam'):
        stores.extend(exam.glob('papers/*/public-sources'))
        from pilot_paper_recovery import snapshot_paths
        for snapshot in snapshot_paths(source, exam):
            store = snapshot/'evidence/public-sources'
            if not store.exists():
                continue
            receipt = snapshot.parent/(snapshot.name+'-receipt.json')
            if (receipt.is_symlink() or not receipt.is_file()
                    or _json(receipt).get('manifest_sha256') != _hash(snapshot/'manifest.json')):
                raise ValueError('public source snapshot manifest lacks native receipt binding')
            ExamRuntime.verify_snapshot(snapshot)
            stores.append(store)
    opaque = set()
    controls = {'admission.json', 'receipt.json', 'helper-lifetime.json',
                'converter-lifetime.json', 'partial-content.json'}
    for store in stores:
        if store.resolve() != store or not store.is_dir():
            raise ValueError('public source store must be a confined native directory')
        for folder in store.iterdir():
            if folder.name == '.admission-lock' and folder.is_file() and not folder.is_symlink():
                continue
            if folder.is_symlink() or not folder.is_dir() or HEX.fullmatch(folder.name) is None:
                raise ValueError('unrecognized public source store entry')
            admission = _json(folder/'admission.json')
            url = admission.get('requested_url')
            if (type(url) is not str or admission.get('source_id') != folder.name
                    or digest(url.encode()) != folder.name or admission.get('attempt') != 1):
                raise ValueError('public source admission identity mismatch')
            actual = source_content_files(folder)  # Also rejects symlinks anywhere.
            for entry in actual:
                name = entry['path']
                if name not in {'raw', 'source.gz', 'source.txt'} and not name.startswith('extracted/'):
                    raise ValueError('unrecognized public source payload path')
            if (folder/'receipt.json').exists():
                evidence = verify_public_source(store, folder.name)
                listed = evidence.get('content_files')
                if (evidence.get('status') not in {'downloaded', 'unavailable'}
                        or evidence.get('requested_url') != url
                        or evidence.get('retryable') is not False
                        or not isinstance(listed, list)
                        or any(not isinstance(item, dict) or set(item) != {'path', 'sha256'} for item in listed)
                        or sorted(listed, key=lambda item: item['path']) != actual):
                    raise ValueError('public source receipt payload census mismatch')
            elif actual:
                # SIGKILL cannot write a final payload manifest. These bytes are
                # preserved as unavailable, never exposed as a completed source.
                helper = _json(folder/'helper-lifetime.json')
                if (helper.get('admission_sha256') != _hash(folder/'admission.json')
                        or type(helper.get('pid')) is not int or helper['pid'] <= 0):
                    raise ValueError('interrupted public source lacks bound helper lifetime')
            opaque.update(folder/item['path'] for item in actual if Path(item['path']).suffix == '.json')
            # No control file is ever excluded, including unexpected process fields.
            if any(path.name in controls and path.parent == folder for path in opaque):
                raise ValueError('public source payload overlaps host metadata')
    return opaque


def validate_process_reconciliation(source: Path, receipt: dict[str, Any]) -> list[dict[str, Any]]:
    """Recheck stopped ownership; a recycled number requires bound terminal evidence.

    Optional reused_pids entries contain pid, current_process_identity, observed_utc,
    and stage_receipts [{path, sha256}] covering ALL matching stage.meta.json files.
    A new process must be born strictly after every historical stage ended. The
    helper never signals processes, writes receipts, or treats reuse as completion.
    """
    source = source.resolve(strict=True)
    if receipt.get('schema_version') != 1 or Path(receipt.get('source_root', '')).resolve() != source:
        raise ValueError('process reconciliation does not bind parent segment')
    checked = _aware_time(receipt.get('checked_utc'))
    if checked > datetime.now(timezone.utc):
        raise ValueError('process reconciliation timestamp is in the future')
    if any(receipt.get(key) is not True for key in
           ('descendants_checked', 'launch_records_checked', 'probe_records_checked')):
        raise ValueError('process reconciliation requires complete descendant/launch/probe census')
    owned = {_pid(value) for value in receipt.get('owned_pids', [])}
    if _pid(receipt.get('host_pid')) not in owned:
        raise ValueError('host PID missing from reconciliation census')
    persisted = set()
    process_records = []
    def records(value, path):
        if isinstance(value, dict):
            if any(value.get(key) is not None for key in ('pid', 'host_pid', 'probe_pid', 'child_pid')):
                process_records.append((path, value))
            for child in value.values():
                records(child, path)
        elif isinstance(value, list):
            for child in value:
                records(child, path)
    opaque_chunks = _opaque_review_chunks(source) | _opaque_public_source_files(source)
    # Snapshot control records are immutable copies, not new process owners.
    # Recognize only native snapshot locations with their complete manifest and
    # receipt; the individual embedded record must still equal a bound stage.
    from pilot_exam import ExamRuntime
    snapshot_controls = {}
    for exam_root in (source/'exam', source/'history/prior-exam'):
        from pilot_paper_recovery import snapshot_paths
        for snapshot in snapshot_paths(source, exam_root):
            snapshot_controls[snapshot/'snapshot.json'] = snapshot.parent.name
    verified_snapshot_controls = set()
    for path in source.rglob('*.json'):
        if path.is_symlink():
            raise ValueError('symlink process evidence is not allowed')
        if path in opaque_chunks:
            continue
        value = json.loads(path.read_text(encoding='utf-8'))
        persisted.update(_nested_pids(value))
        records(value, path)
    if not persisted <= owned:
        raise ValueError('persisted process missing from reconciliation census')
    entries = receipt.get('reused_pids', [])
    if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
        raise ValueError('reused_pids must be an array of evidence objects')
    by_pid = {}
    for entry in entries:
        pid = _pid(entry.get('pid'))
        if pid not in owned or pid == receipt['host_pid'] or pid in by_pid:
            raise ValueError('invalid or duplicate reused PID census entry')
        by_pid[pid] = entry
    observations = []
    legacy_markers, legacy_groups = set(), set()
    terminal = {'completed', 'process_failed', 'timeout_censored', 'cancelled', 'host_cancelled'}
    for pid in sorted(owned):
        try:
            _assert_stopped(pid)
            continue
        except ValueError as error:
            # EPERM on an unrelated root-owned recycled PID is not identity
            # evidence, but an explicit receipt may still be fully checked via ps.
            if (pid not in by_pid or not (isinstance(error, _ProcessPresent)
                    or isinstance(error.__cause__, PermissionError))):
                raise
        entry = by_pid[pid]
        legacy = entry.get('evidence_kind') == 'legacy_terminal_receipt'
        if entry.get('evidence_kind') not in (None, 'fingerprint', 'legacy_terminal_receipt'):
            raise ValueError('unsupported PID reuse evidence kind')
        observed = _aware_time(entry.get('observed_utc'))
        if observed > checked:
            raise ValueError('reused PID observation is newer than reconciliation')
        expected_current = entry.get('current_process_identity')
        if not isinstance(expected_current, str) or not re.fullmatch(r'[0-9a-f]{64}', expected_current):
            raise ValueError('reused PID requires complete current process identity')
        stages = {}
        for path in (source / 'host/runtime').glob('*/*/stage.meta.json'):
            stage = _json(path)
            if stage.get('pid') == pid:
                stages[str(path.relative_to(source))] = (path, stage)
        refs = entry.get('stage_receipts')
        if (not stages or not isinstance(refs, list) or any(not isinstance(ref, dict) for ref in refs)
                or len(refs) != len(stages) or {ref.get('path') for ref in refs} != set(stages)):
            raise ValueError('reused PID requires every historical stage receipt')
        for record_path, record in process_records:
            if pid not in [record.get(key) for key in ('pid', 'host_pid', 'probe_pid', 'child_pid')]:
                continue
            stage_entry = stages.get(str(record_path.relative_to(source)))
            is_stage = stage_entry is not None and record == stage_entry[1]
            is_copy = (record_path.name in {'host-progress.json', 'continuation-checkpoint.json'}
                       and not any(record.get(key) == pid for key in ('host_pid', 'probe_pid', 'child_pid'))
                       and any((record == stage if legacy else record.get('name') == stage.get('name'))
                               and record.get('process_identity') == stage.get('process_identity')
                               for _, stage in stages.values()))
            if record_path in snapshot_controls and record_path not in verified_snapshot_controls:
                snapshot = record_path.parent
                receipt_path = snapshot.parent/(snapshot.name+'-receipt.json')
                if (record_path.is_symlink() or snapshot.is_symlink() or receipt_path.is_symlink()
                        or not receipt_path.is_file()
                        or _json(receipt_path).get('manifest_sha256') != _hash(snapshot/'manifest.json')):
                    raise ValueError('paper snapshot process alias lacks bound manifest')
                ExamRuntime.verify_snapshot(snapshot)
                verified_snapshot_controls.add(record_path)
            is_snapshot_copy = (record_path in snapshot_controls
                and not any(record.get(key) == pid for key in ('host_pid', 'probe_pid', 'child_pid'))
                and any(record == stage
                        and stage.get('name', '').split('/')[0] == snapshot_controls[record_path]
                        for _, stage in stages.values()))
            if not is_stage and not is_copy and not is_snapshot_copy:
                raise ValueError('reused PID has unsupported non-stage ownership evidence')
        identities, ends = set(), []
        for ref in refs:
            path, stage = stages[ref['path']]
            if path.is_symlink() or not path.resolve().is_relative_to(source) or _hash(path) != ref.get('sha256'):
                raise ValueError('reused PID stage receipt hash/path changed')
            identity = stage.get('process_identity')
            if legacy:
                if identity is not None:
                    raise ValueError('legacy route requires absent historical identity')
                _legacy_argv(stage)
            elif not isinstance(identity, str) or not re.fullmatch(r'[0-9a-f]{64}', identity):
                raise ValueError('historical process identity missing or incomplete')
            if stage.get('status') not in terminal or type(stage.get('exit_code')) is not int:
                raise ValueError('historical reused PID stage is not terminal')
            start, end = _aware_time(stage.get('start_utc')), _aware_time(stage.get('end_utc'))
            if not start <= end <= observed:
                raise ValueError('historical stage timing does not precede reused PID observation')
            identities.add(identity); ends.append(end)
        probe = subprocess.run(['ps', '-p', str(pid), '-o', 'lstart=', '-o', 'args='],
                               capture_output=True, text=True, timeout=2)
        value = probe.stdout.strip()
        if probe.returncode != 0 or not value:
            # It may have exited between checks, but unavailable ps is not absence.
            _assert_stopped(pid)
            continue
        fingerprint = hashlib.sha256(value.encode()).hexdigest()
        fields = value.split(None, 5)
        if len(fields) != 6:
            raise ValueError('current process birth/command evidence incomplete')
        birth = (_unambiguous_birth if legacy else _ps_birth)(' '.join(fields[:5]))
        if (fingerprint != expected_current or fingerprint in identities or birth <= max(ends)
                or birth > observed or str(source) in fields[5]):
            raise ValueError('current PID is not the verified later unrelated incarnation')
        if legacy:
            prior = _legacy_absence(source, entry, owned, refs, ends, birth)
            current_argv = shlex.split(fields[5])
            if not current_argv or not Path(current_argv[0]).is_absolute():
                raise ValueError('ambiguous current executable')
            executable = subprocess.run(['ps', '-p', str(pid), '-o', 'comm='],
                                        check=True, capture_output=True, text=True, timeout=2).stdout.strip()
            if (not executable or '\n' in executable or not Path(executable).is_absolute()
                    or executable != entry.get('current_executable') or current_argv[0] != executable):
                raise ValueError('ambiguous current executable evidence')
            original = [stage for _, stage in stages.values()]
            executables = {str(Path(_legacy_argv(stage)[0]).resolve()) for stage in original}
            markers = {str(source), 'pilot_document_tools'}
            markers.update(prior.get('mcp_source_paths', []))
            markers.update(stage[key] for stage in original for key in ('session_id', 'resume_session') if stage.get(key))
            legacy_markers.update(markers)
            legacy_groups.update(_pid(group) for group in prior.get('recorded_group_ids', []))
            if str(Path(executable).resolve()) in executables or 'mcp' in fields[5].lower() or any(marker in fields[5] for marker in markers):
                raise ValueError('legacy current command retains historical ownership')
        observations.append({'pid': pid, 'current_process_identity': fingerprint,
                             'current_birth_utc': birth.isoformat(),
                             'current_command_sha256': hashlib.sha256(fields[5].encode()).hexdigest(),
                             'historical_end_utc': max(ends).isoformat()})
    census = subprocess.run(['ps', '-axo', 'pid=,args='], check=True, capture_output=True, text=True, timeout=10)
    for line in census.stdout.splitlines():
        fields = line.strip().split(None, 1)
        if len(fields) == 2 and int(fields[0]) != os.getpid() and str(source) in fields[1]:
            raise ValueError('live process still references parent segment')
    reused = {item['pid']: item for item in observations}
    table = subprocess.run(['ps', '-axo', 'pid=,ppid=,pgid=,lstart=,args='],
                           check=True, capture_output=True, text=True, timeout=10)
    seen = set()
    for line in table.stdout.splitlines():
        fields = line.split(None, 8)
        if len(fields) != 9:
            raise ValueError('incomplete process lineage census')
        pid, parent, group = map(int, fields[:3])
        seen.add(pid)
        birth = _ps_birth(' '.join(fields[3:8]))
        if pid in reused and (birth != _aware_time(reused[pid]['current_birth_utc'])
                or hashlib.sha256(fields[8].encode()).hexdigest() != reused[pid]['current_command_sha256']):
            raise ValueError('reused process changed during lineage census')
        if parent in owned - set(reused):
            raise ValueError('owned descendant remains in process census')
        if group in owned:
            if group not in reused or birth <= _aware_time(reused[group]['historical_end_utc']):
                raise ValueError('historical owned process group remains')
        if group in legacy_groups:
            raise ValueError('historical recorded process group remains')
        if pid != os.getpid() and (str(source) in fields[8] or any(marker in fields[8] for marker in legacy_markers)):
            raise ValueError('live process still references parent segment')
    # Recheck after the group census to reject a second reuse or argv change.
    from campaign_watchdog import capture_process_identity
    for pid in owned - set(reused):
        _assert_stopped(pid)
    for item in observations:
        if item['pid'] not in seen:
            _assert_stopped(item['pid'])
        actual = capture_process_identity(item['pid'])
        if actual != item['current_process_identity']:
            _assert_stopped(item['pid'])
    return observations


def validate_and_load(source: Path, *, reconciliation: Path, operational_handoff_resolution=None, target_root=None, initial_main_recovery=None, assessment_delivery_resolution=None) -> dict[str, Any]:
    """Return restoration payloads after fail-closed process/evidence validation.

    The reconciliation receipt must enumerate host, stage, probe and launch PIDs,
    attest a descendant census, and link existing evidence. Every PID is checked
    again. A live command referencing the parent directory also blocks reuse.
    No receipt is inferred from a terminal campaign status alone.
    """
    source = source.resolve(strict=True)
    import pilot_handoff_resolution as resolution
    import pilot_assessment_delivery_resolution as delivery_resolution
    if assessment_delivery_resolution is not None and target_root is None:
        raise ValueError('delivery resolution requires fixed successor')
    pending_delivery = delivery_resolution.request(assessment_delivery_resolution,source,target_root) if assessment_delivery_resolution is not None else None
    if operational_handoff_resolution is not None and target_root is None:
        raise ValueError('explicit handoff resolution requires fixed target_root')
    pending_resolution = resolution.request(operational_handoff_resolution, source, target_root) if operational_handoff_resolution is not None else None
    receipt = _json(reconciliation)
    if receipt.get('schema_version') != 1 or Path(receipt.get('source_root', '')).resolve() != source:
        raise ValueError('reconciliation receipt does not bind this parent segment')
    checked = datetime.fromisoformat(str(receipt.get('checked_utc', '')).replace('Z', '+00:00'))
    if checked.tzinfo is None or checked > datetime.now(timezone.utc):
        raise ValueError('invalid reconciliation timestamp')
    for field in ('descendants_checked', 'launch_records_checked', 'probe_records_checked'):
        if receipt.get(field) is not True:
            raise ValueError('missing reconciliation evidence: ' + field)
    evidence = receipt.get('evidence')
    if not isinstance(evidence, list) or not evidence:
        raise ValueError('reconciliation evidence files required')
    evidence_hashes = {}
    for name in evidence:
        path = Path(name)
        if not path.is_absolute():
            path = reconciliation.resolve().parent / path
        if not path.is_file():
            raise ValueError('missing reconciliation evidence file')
        evidence_hashes[str(path.resolve())] = _hash(path)
    owned = {_pid(value) for value in receipt.get('owned_pids', [])}
    if _pid(receipt.get('host_pid')) not in owned:
        raise ValueError('host PID missing from reconciliation census')
    config = _json(source / 'host-config.json')
    resolved_handoffs = resolution.records(source, config)
    resolved_deliveries = delivery_resolution.records(source,config)
    if config.get('main_response_contract_version') not in (None, 1):
        raise ValueError('unsupported main response contract version')
    for group, directory in (('policy_hashes', 'policy'), ('code_hashes', 'code')):
        for name, expected in config.get(group, {}).items():
            relative = Path(name)
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError('unsafe frozen artifact path')
            if _hash(source / directory / relative) != expected:
                raise ValueError('frozen artifact hash mismatch: ' + name)
    from pilot_infrastructure_notice import load_notice
    load_notice(source, config)
    result = _json(source / 'pilot-result.json')
    if not result.get('end_utc'):
        raise ValueError('parent segment has no terminal result receipt')
    registry = _json(source / 'campaign/registry.json')
    state = _json(source / 'campaign/state.json')
    if state.get('registry_sha256') != _hash(source / 'campaign/registry.json') or state.get('sealed') is not True:
        raise ValueError('parent campaign is not sealed against its registry')
    if registry.get('deadline_utc') != config.get('deadline_utc') or registry.get('mode') != config.get('mode'):
        raise ValueError('parent scope or deadline differs from frozen configuration')
    if set(config['problems']) != set(registry['problems']):
        raise ValueError('parent problem registry mismatch')
    paths = sorted(source.rglob('*'))
    if any(path.is_symlink() for path in paths):
        raise ValueError('parent segment contains symlinks; explicit reconciliation required')
    files = {str(path.relative_to(source)): _hash(path) for path in paths if path.is_file()}
    validate_process_reconciliation(source, receipt)
    exam_closed = False
    if config.get('exam'):
        from pilot_exam import ExamRuntime
        exam_config = config['exam']
        if not (Path(exam_config['state_root']) / 'clock.json').is_file():
            raise ValueError('exam continuation lacks original persisted clock')
        exam = ExamRuntime(exam_config)
        if config['deadline_utc'] != exam_config['submission_deadline_utc']:
            raise ValueError('exam continuation deadline differs from original clock')
        exam_closed = datetime.now(timezone.utc) >= exam.research_close
    restored = {}
    for ident in config['problems']:
        if not isinstance(ident, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', ident):
            raise ValueError('unsafe problem identifier')
        folder = source / 'campaign/problems' / ident
        if _hash(folder / 'input.txt') != registry['problems'][ident]['sha256']:
            raise ValueError('original question hash mismatch')
        for path in delivery_resolution.paths(folder):
            if path.exists() or path.is_symlink():
                if not delivery_resolution.covers(resolved_deliveries,ident,receipt=_json(path)) and not (
                        pending_delivery and pending_delivery['request']['problem_id']==ident
                        and pending_delivery['request']['handoff_sha256']==_hash(path)):
                    raise ValueError('pending completed-assessment handoff requires supervisor diagnosis; automatic continuation is not authorized')
        handoff_paths = [folder / 'operational-handoff.json', *folder.glob('operational-handoff-*.json')]
        for handoff_path in handoff_paths:
            if handoff_path.exists() or handoff_path.is_symlink():
                handoff = _json(handoff_path)
                if not resolution.covers(resolved_handoffs, ident, receipt=handoff) and not (pending_resolution and
                        pending_resolution['request']['problem_id'] == ident and
                        pending_resolution['request']['handoff_sha256'] == _hash(handoff_path)):
                    raise ValueError('pending operational handoff requires explicit supervised resolution; automatic continuation is not authorized')
        progress = _json(folder / 'host-progress.json')
        stage_paths = sorted((source / 'host/runtime' / ident).glob('*/stage.meta.json'),
                             key=lambda path: int(match.group(1)) if (match := _NUMBERED.match(path.parent.name)) else -1)
        calls = [_json(path) for path in stage_paths]
        if (not calls and not exam_closed) or any(call['name'] != ident + '/' + path.parent.name for call, path in zip(calls, stage_paths)):
            raise ValueError('missing or mismatched parent stage evidence')
        for call, stage_path in zip(calls, stage_paths):
            if call.get('status') == 'completed':
                if not call.get('answer_sha256'):
                    raise ValueError('completed response has no answer hash')
                raw_answer = stage_path.with_name('stage.answer.txt')
                if not raw_answer.is_file() or _hash(raw_answer) != call['answer_sha256']:
                    raise ValueError('completed response answer hash mismatch')
                from codex_transport import extract_answer
                raw_text = raw_answer.read_text(encoding='utf-8')
                parsed, _, parse_error = extract_answer(raw_text)
                if parsed is None:
                    parsed = {'raw_answer': raw_text, 'parse_error': parse_error}
                if (call.get('module', '').startswith('main') and isinstance(parsed, dict)
                        and parsed.get('response_type') in {'operational_handoff','assessment_handoff'}):
                    number = int(call['name'].split('/')[-1].split('-')[0])
                    rejected = folder / ('main-' + str(number) + '-invalid-contract.json')
                    if not rejected.is_file() or _json(rejected).get('raw_response') != parsed:
                        if parsed['response_type']=='assessment_handoff':
                            if not delivery_resolution.covers(resolved_deliveries,ident,stage=call['name']) and not (
                                    pending_delivery and pending_delivery['request']['problem_id']==ident
                                    and pending_delivery['request']['source_stage']==call['name']):
                                raise ValueError('completed assessment handoff response requires supervisor diagnosis before continuation')
                        elif not resolution.covers(resolved_handoffs, ident, stage=call['name']) and not (pending_resolution and
                                pending_resolution['request']['problem_id'] == ident and pending_resolution['request']['source_stage'] == call['name']):
                            raise ValueError('completed operational handoff response requires supervised resolution before continuation')
                saved_path = folder / (call['name'].split('/')[-1] + '.json')
                saved = (json.loads(saved_path.read_text(encoding='utf-8'))
                         if call['module'] in ('proof-review', 'scope-review') or call['module'].startswith(('main', 'route-scout')) else _json(saved_path))
                if parsed != saved:
                    raise ValueError('saved response differs from verified transport answer')
        saved_names = {call['name'] for call in progress.get('calls', [])}
        if not saved_names <= {call['name'] for call in calls}:
            raise ValueError('checkpoint references missing stage receipts')
        # Paper transport is reconciled and hash-checked above, but is never
        # research review, implementation, main identity, or grade evidence.
        calls = [call for call in calls if not call.get('module', '').startswith('paper-')]
        stage_paths = [path for path in stage_paths
                       if not _json(path).get('module', '').startswith('paper-')]
        if exam_closed and state['problems'][ident].get('successful_complete') is not True:
            # A stopped exam may have zero valid main outputs. After the original
            # research close, preserve available unaccepted work solely for the
            # existing paper writer; never invent main/proof provenance.
            current_path = folder / 'current-candidate.json'
            current = _json(current_path) if current_path.is_file() else {}
            restored[ident] = {'paper_only': True, 'proof_document': None,
                'main_session': progress.get('main_session'), 'implementers': [], 'calls': calls,
                'current': current, 'dossier': {}, 'counter': 0,
                'findings': progress.get('open_findings', []), 'errors': progress.get('errors', []),
                'execution_history': [], 'reviewer_history': [], 'triage_history': [],
                'local_verification_modules': [], 'advisory_scope_history': [],
                'final_assessment_history': [], 'finding_history': [],
                'original_sha256': registry['problems'][ident]['sha256']}
            continue
        if initial_main_recovery is not None:
            from pilot_initial_recovery import validate_initial_recovery
            restored[ident] = validate_initial_recovery(source, config, progress, calls,
                authorization=initial_main_recovery, problem_id=ident, target_root=target_root)
            continue
        session = progress.get('main_session')
        mains = [call for call in calls if call['module'].startswith('main') and call.get('status') == 'completed']
        if not session or not mains or any(call.get('session_id') != session for call in mains):
            raise ValueError('persistent main identity is missing or inconsistent')
        implementers = sorted({session} | {call['session_id'] for call in calls if call['module'].startswith(('sol', 'route-scout')) and call.get('session_id')})
        reviewers = [call for call in calls if not call['module'].startswith(('main', 'sol', 'route-scout'))]
        if any(call.get('session_id') in implementers for call in reviewers):
            raise ValueError('reviewer identity collides with an implementer')
        dossiers = [call for call in mains if call['module'] == 'main-dossier']
        if not dossiers:
            raise ValueError('missing original dossier')
        dossier_path = folder / 'accepted-dossier.json'
        if dossier_path.is_file():
            receipt = _json(dossier_path)
            source_stage = next((call for call in mains if call['name'] == receipt.get('source_stage')), None)
            if not source_stage or source_stage['answer_sha256'] != receipt.get('raw_response_sha256'):
                raise ValueError('accepted dossier lacks verified original main source')
            from pilot_candidate_contract import apply_main_response
            raw_dossier = json.loads((folder / (source_stage['name'].split('/')[-1] + '.json')).read_text())
            rejected_path = folder / ('main-' + str(int(source_stage['name'].split('/')[-1].split('-')[0])) + '-invalid-contract.json')
            if rejected_path.is_file() and _json(rejected_path).get('raw_response') == raw_dossier:
                raise ValueError('accepted dossier source was rejected by the main contract')
            dossier, _ = apply_main_response(raw_dossier, {})
            if dossier != receipt.get('effective_candidate'):
                raise ValueError('accepted dossier differs from source response')
        else:
            dossier = _json(folder / (dossiers[0]['name'].split('/')[-1] + '.json'))
            rejected_path = folder / ('main-' + str(int(dossiers[0]['name'].split('/')[-1].split('-')[0])) + '-invalid-contract.json')
            if rejected_path.is_file() and _json(rejected_path).get('raw_response') == dossier:
                raise ValueError('original dossier source was rejected by the main contract')
        proof_state = None
        if (config.get('proof_document_version') == 1
                and not (folder/'proof-current.json').is_file()
                and not (state['problems'][ident].get('status') == 'complete'
                         and state['problems'][ident].get('successful_complete') is True
                         and ident in config.get('carried_complete_problems', {}))):
            raise ValueError('unfinished document campaign is missing canonical proof pointer; preserve for reconciliation')
        if config.get('proof_document_version') == 1 and (folder/'proof-current.json').is_file():
            import pilot_proof_document as documents
            identity = dict(problem_id=ident, original_sha256=registry['problems'][ident]['sha256'], main_session=session)
            proof_state = documents.read_current(folder, **identity)
            current = documents.read_submission(folder, **identity)['candidate']
            if proof_state['status'] == 'draft':
                draft_producer = proof_state['manifest']['producer']
                draft_call = next((c for c in calls if c['name'] == draft_producer['stage']), None)
                if (draft_call is None or not draft_call['module'].startswith('main')
                        or draft_call.get('request_id') != draft_producer['request_id']
                        or draft_call.get('session_id') != session):
                    raise ValueError('saved draft lacks exact original-main stage provenance; preserve for reconciliation')
                operations = source/'host/runtime'/draft_call['name']/'document-operations.jsonl'
                acknowledgments = [json.loads(line) for line in operations.read_text().splitlines()] if operations.is_file() else []
                ref = {k: proof_state[k] for k in ('revision','manifest_sha256','proof_sha256','status')}
                if not any(item.get('tool') == 'save_proof_revision' and item.get('is_error') is False
                        and item.get('producer') == draft_producer and item.get('session_id') == session
                        and item.get('saved_revision') == ref for item in acknowledgments):
                    raise ValueError('saved draft publication lacks durable save acknowledgment; preserve for reconciliation')
        else:
            current = _json(folder / 'current-candidate.json')
        replay_mains = []
        valid_main_answers = []
        for call in mains:
            raw = json.loads((folder / (call['name'].split('/')[-1] + '.json')).read_text())
            rejected_path = folder / ('main-' + str(int(call['name'].split('/')[-1].split('-')[0])) + '-invalid-contract.json')
            if rejected_path.is_file() and _json(rejected_path).get('raw_response') == raw:
                continue
            if isinstance(raw, dict) and raw.get('response_type') in {'operational_handoff','assessment_handoff'}:
                continue  # Validated operational history never becomes a scientific candidate.
            replay_mains.append(call)
            valid_main_answers.append(raw)
        from pilot_candidate_contract import replay_main_responses
        replayed, replay_known = replay_main_responses(valid_main_answers, legacy_indices=[i for i, call in enumerate(replay_mains)
            if config.get('main_response_contract_version') != 1 or call['name'] in config.get('legacy_main_stages', [])])
        if proof_state is not None:
            from pilot_candidate_contract import candidate_hash
            submitted = documents.read_submission(folder, **identity)
            producer = submitted['manifest']['producer']
            bound_call = next((c for c in replay_mains if c['name'] == producer['stage']), None)
            producer_candidate = None
            if bound_call is not None:
                bound_index = replay_mains.index(bound_call)
                producer_candidate, _ = replay_main_responses(valid_main_answers[:bound_index+1],
                    legacy_indices=[i for i,c in enumerate(replay_mains[:bound_index+1])
                        if config.get('main_response_contract_version') != 1 or c['name'] in config.get('legacy_main_stages', [])])
            if (bound_call is None or documents.encoded(producer_candidate) != documents.encoded(current)
                    or bound_call.get('request_id') != producer['request_id']
                    or bound_call.get('session_id') != session
                    or candidate_hash(current) not in replay_known
                    or documents.encoded(replay_known[candidate_hash(current)]) != documents.encoded(current)):
                raise ValueError('submitted proof lacks exact verified original-main candidate provenance')
        elif replayed is None or current != replayed:
            raise ValueError('current candidate does not match latest valid completed main response')
        reviewer_history = []
        for call in reviewers:
            answer_path = folder / (call['name'].split('/')[-1] + '.json')
            reviewer_history.append({'stage': call['name'], 'session_id': call.get('session_id'),
                                     'status': call['status'], 'answer_sha256': call.get('answer_sha256'),
                                     'output': (json.loads(answer_path.read_text(encoding='utf-8'))
                                                if call['module'] in ('proof-review', 'scope-review') else _json(answer_path))
                                               if answer_path.is_file() else None})
        # Transport completion is not protocol acceptance. Bind preserved rejection
        # receipts to their exact raw response before returning them to the same main.
        by_stage = {item['stage']: item for item in reviewer_history}
        by_call = {call['name']: call for call in reviewers}
        for item in reviewer_history:
            item['protocol_status'] = 'not_revalidated'
        for diagnostic_path in sorted(folder.glob('review-*-invalid-*.json')):
            diagnostic = json.loads(diagnostic_path.read_text(encoding='utf-8'))
            if not isinstance(diagnostic, dict) or not isinstance(diagnostic.get('receipt'), dict):
                raise ValueError('invalid historical review diagnostic binding')
            receipt = diagnostic['receipt']
            stage = receipt.get('name')
            if not isinstance(stage, str):
                raise ValueError('invalid historical review diagnostic binding')
            item, call = by_stage.get(stage), by_call.get(stage)
            if (diagnostic.get('status') != 'invalid_not_authority' or item is None
                    or not isinstance(diagnostic.get('error'), str) or not diagnostic['error'].strip()
                    or any(not isinstance(receipt.get(key), str) or not receipt[key] for key in
                           ('name', 'session_id', 'answer_sha256', 'prompt_sha256', 'request_id'))
                    or not isinstance(diagnostic.get('candidate_sha256'), str)
                    or not re.fullmatch(r'[0-9a-f]{64}', diagnostic['candidate_sha256'])
                    or any(receipt.get(key) != call.get(key) for key in
                           ('name', 'session_id', 'answer_sha256', 'prompt_sha256', 'request_id'))
                    or diagnostic['candidate_sha256'] not in replay_known
                    or diagnostic['candidate_sha256'] != receipt.get('reviewed_candidate_sha256')
                    or json.dumps(diagnostic.get('invalid_review'), sort_keys=True) != json.dumps(item['output'], sort_keys=True)):
                raise ValueError('invalid historical review diagnostic binding')
            item['protocol_status'] = 'invalid_not_authority'
            item.setdefault('invalid_protocol_diagnostics', []).append({
                'path': str(diagnostic_path.relative_to(source)),
                'sha256': _hash(diagnostic_path), 'diagnostic': diagnostic})
        triage_history = progress.get('triage_history', [])
        if not triage_history:
            # Pre-triage pilots kept independent selections only in reviewer answers.
            # Preserve those verified records even if the main cleared its row flags.
            # This is historical evidence, never execution authorization.
            selections = {}
            sources = []
            for review in reviewer_history:
                output = review.get('output')
                if (review['status'] != 'completed' or review.get('protocol_status') == 'invalid_not_authority'
                        or not isinstance(output, dict)):
                    continue
                selected = output.get('triaged_rows', [])
                if not isinstance(selected, list) or any(not isinstance(row, str) for row in selected):
                    raise ValueError('invalid historical reviewer triage selection')
                if selected:
                    sources.append({key: review[key] for key in ('stage', 'session_id', 'answer_sha256')})
                for row in selected:
                    selections[row] = {'row_id': row, 'selected': True,
                                       'reason': 'Historical independent selection: ' + review['stage']}
            if selections:
                triage_history = [{'legacy': True, 'authorization': False,
                                   'decisions': list(selections.values()),
                                   'selected_rows': sorted(selections), 'sources': sources}]
        counter = max([int(match.group(1)) for path in list(folder.iterdir()) + [p.parent for p in stage_paths]
                       if (match := _NUMBERED.match(path.name))], default=0)
        execution = []
        for call in calls:
            if call['module'].startswith('sol'):
                answer = folder / (call['name'].split('/')[-1] + '.json')
                execution.append({'historical_stage': call['name'], 'session_id': call.get('session_id'),
                                  'execution_receipt':{k:call.get(k) for k in ('name','request_id','answer_sha256')},
                                  'status': call['status'], 'output': _json(answer) if answer.is_file() else None})
        for directory in sorted([*(folder / 'probes').glob('*'), *(folder / 'local-verification').glob('*/probes/*')]):
            if not directory.is_dir():
                continue
            artifacts = {str(path.relative_to(folder)): {'sha256': _hash(path), 'text': path.read_text(encoding='utf-8')}
                         for path in sorted(directory.rglob('*')) if path.is_file()}
            result_path = directory / 'result.json'
            execution.append({'historical_probe': str(directory.relative_to(folder)),
                              'result': _json(result_path) if result_path.is_file() else {'status': 'unknown'},
                              'artifacts': artifacts})
        modules = _local_module_registry(folder, progress)
        restored_findings = list(progress.get('open_findings', []))
        restored_finding_history = list(progress.get('finding_history', []))
        if proof_state is not None:
            # Publication is authoritative before the derived host-progress write.
            # Recover newly published checkpoint obligations from its verified raw
            # producer, but do not reopen versions already archived by a review.
            published_answer = valid_main_answers[bound_index]
            if published_answer.get('response_type') == 'blocked_checkpoint':
                for finding in published_answer['unreviewed_findings']:
                    fingerprint = hashlib.sha256(documents.encoded(finding).encode()).hexdigest()
                    archived = any(item.get('sha256') == fingerprint and item.get('finding') == finding
                                   for item in restored_finding_history)
                    if not archived:
                        if finding not in restored_findings:
                            restored_findings.append(finding)
                        restored_finding_history.append({'sha256': fingerprint, 'finding': finding})
        restored[ident] = {'proof_document': ({k: proof_state[k] for k in ('revision', 'manifest_sha256', 'status', 'proof_sha256')} if proof_state else None),
                           'main_session': session, 'implementers': implementers, 'calls': calls,
                           'findings': restored_findings, 'errors': progress.get('errors', []),
                           'dossier': dossier, 'current': current, 'counter': counter,
                           'execution_history': execution, 'reviewer_history': reviewer_history,
                           'triage_history': triage_history,
                           'local_verification_modules': modules,
                           'advisory_scope_history': progress.get('advisory_scope_history', []),
                           'final_assessment_history': progress.get('final_assessment_history', []),
                           'finding_history': restored_finding_history,
                           'original_sha256': registry['problems'][ident]['sha256']}
    manifest_hash = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    new_resolution = resolution.validate_new(pending_resolution, source, manifest_hash, restored)
    new_delivery = delivery_resolution.validate_new(pending_delivery,source,manifest_hash,restored)
    return {'schema_version': 1, 'config': config, 'problems': restored,
            'operational_handoff_resolutions': resolved_handoffs, 'new_handoff_resolution': new_resolution,
            'assessment_delivery_resolutions':resolved_deliveries,'new_assessment_delivery_resolution':new_delivery,
            'parent': {'source_root': str(source), 'manifest_sha256': manifest_hash, 'files': files,
                       'reconciliation_sha256': _hash(reconciliation), 'reconciliation_evidence': evidence_hashes,
                       'prior_deadline_utc': config.get('deadline_utc'), 'result': result,
                       'historical_usage': 'Parent stage usage and raw events remain linked by this manifest; missing response metering remains unknown.'}}
