"""Offline, bounded analysis of existing transport records; no runtime imports or writes."""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import math
import os
import re
from pathlib import Path
import stat
import sys
import time

SCHEMA = 1
MAX_BYTES = 128 * 1024 * 1024
MAX_LINES = 100000
MAX_STAGES = 128
MAX_INTERVAL_DETAILS = 256
MAX_ELAPSED_SECONDS = 1_000_000_000_000
MAX_LINE_BYTES = 8 * 1024 * 1024
DOCUMENT_TOOLS = {'read_artifact', 'read_required_evidence', 'read_current_proof', 'save_proof_revision'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(path, limit=MAX_BYTES):
    """Bind a twice-identical bounded prefix. Appends allowed; replacement/rewrite rejected."""
    path = Path(path)
    if type(limit) is not int or not 1 <= limit <= MAX_BYTES:
        raise ValueError('snapshot limit must be positive')
    if path.is_symlink():
        raise ValueError('symlink input refused')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode):
            raise ValueError('regular input file required')
        length = min(before.st_size, limit)
        def read_prefix():
            os.lseek(fd, 0, os.SEEK_SET)
            chunks, remaining = [], length
            while remaining:
                block = os.read(fd, min(1024 * 1024, remaining))
                if not block:
                    raise ValueError('input shrank during snapshot')
                chunks.append(block); remaining -= len(block)
            return b''.join(chunks)
        data = read_prefix()
        if read_prefix() != data:
            raise ValueError('input prefix changed during snapshot')
        after = os.fstat(fd)
        named = path.stat(follow_symlinks=False)
        if (named.st_dev, named.st_ino) != (before.st_dev, before.st_ino) or not stat.S_ISREG(named.st_mode):
            raise ValueError('input path replaced during snapshot')
        if after.st_size < before.st_size:
            raise ValueError('input shrank during snapshot')
        receipt = {'path': str(path.absolute()), 'prefix_sha256': digest(data), 'prefix_bytes': len(data),
                   'size_before': before.st_size, 'size_after': after.st_size,
                   'stable_prefix_twice_read': True, 'grew': after.st_size > before.st_size,
                   'byte_cap_reached': length < before.st_size,
                   'whole_file_at_snapshot': len(data) == after.st_size}
        return data, receipt
    finally:
        os.close(fd)


def finite(value):
    try:
        return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= MAX_ELAPSED_SECONDS
    except (OverflowError, ValueError):
        return False


def union_seconds(intervals):
    total = 0.0; right = None
    for left, end in sorted(intervals):
        if right is None or left > right:
            total += end - left
        else:
            total += max(0, end - right)
        right = end if right is None else max(right, end)
    return total


def analyze_events(data, duration=None, *, max_lines=MAX_LINES, max_line_bytes=MAX_LINE_BYTES):
    if type(max_lines) is not int or not 1 <= max_lines <= MAX_LINES or type(max_line_bytes) is not int or not 1 <= max_line_bytes <= MAX_LINE_BYTES:
        raise ValueError('event limits must be positive')
    records = {}; issues = {}; parsed = 0; last = 0.0; previous = None; first = None; required_last = None
    def issue(name): issues[name] = issues.get(name, 0) + 1
    # Only complete newline-terminated records are considered. Never decode a truncated tail.
    last_newline = data.rfind(b'\n')
    complete = data[:last_newline + 1] if last_newline >= 0 else b''
    tail_bytes = len(data) - len(complete)
    lines = complete.splitlines(keepends=True)
    dropped = max(0, len(lines) - max_lines)
    for line in lines[:max_lines]:
        if len(line) > max_line_bytes:
            issue('oversized_line'); continue
        try:
            envelope = json.loads(line)
        except (ValueError, UnicodeError):
            issue('malformed_line'); continue
        if not isinstance(envelope, dict) or not finite(envelope.get('elapsed_s')) or not isinstance(envelope.get('event'), dict):
            issue('invalid_envelope'); continue
        elapsed = float(envelope['elapsed_s']); parsed += 1
        if previous is not None and elapsed < previous: issue('nonmonotonic_event_time')
        previous = elapsed; last = max(last, elapsed)
        if first is None: first = elapsed
        event = envelope['event']; item = event.get('item')
        if not isinstance(item, dict) or item.get('type') != 'mcp_tool_call' or item.get('server') != 'merlean_documents': continue
        ident, tool = item.get('id'), item.get('tool')
        if not isinstance(ident, str) or not ident or len(ident) > 256 or not isinstance(tool,str) or tool not in DOCUMENT_TOOLS:
            issue('unrecognized_document_item'); continue
        kind = event.get('type')
        if kind not in ('item.started', 'item.completed'): continue
        record = records.setdefault(ident, {'tool': tool, 'invalid': False})
        key = 'start' if kind == 'item.started' else 'end'
        if key in record or record['tool'] != tool:
            record['invalid'] = True; issue('duplicate_or_changed_document_item')
        else:
            if key == 'end' and 'start' not in record:
                record['invalid'] = True; issue('completion_before_start')
            record[key] = elapsed
            if key == 'end':
                record['completion_status'] = item.get('status') if item.get('status') in ('completed','failed','in_progress') else 'unknown'
        if key == 'end' and tool == 'read_required_evidence': required_last = elapsed
    intervals = []; details = []; totals = {}; unmatched = 0
    bound = float(duration) if finite(duration) else last if parsed else None
    if duration is not None and not finite(duration): issue('invalid_recorded_elapsed')
    if finite(duration) and parsed and last > duration: issue('event_after_recorded_elapsed')
    for record in records.values():
        if record['invalid']: continue
        if 'start' not in record or 'end' not in record:
            unmatched += 1; continue
        left, right = record['start'], record['end']
        if right < left or bound is None or right > bound or left > bound:
            issue('reversed_or_out_of_bounds_interval'); continue
        intervals.append((left, right))
        if len(details) < MAX_INTERVAL_DETAILS:
            details.append({'tool':record['tool'],'start_elapsed_s':left,'end_elapsed_s':right,'duration_s':right-left,'completion_status':record['completion_status']})
        value = totals.setdefault(record['tool'], {'paired_calls': 0, 'interval_sum_s': 0.0, 'completion_status_counts': {}})
        value['paired_calls'] += 1; value['interval_sum_s'] += right - left
        status = record['completion_status']; value['completion_status_counts'][status] = value['completion_status_counts'].get(status,0)+1
    invalid_clock = any(k in issues for k in ('invalid_recorded_elapsed','nonmonotonic_event_time','event_after_recorded_elapsed','reversed_or_out_of_bounds_interval','invalid_envelope'))
    union = union_seconds(intervals); summed = sum(b-a for a,b in intervals)
    if invalid_clock:
        totals = {}; union = summed = None
    gaps = []; rightmost = None
    for left,right in sorted(intervals):
        if rightmost is not None and left > rightmost: gaps.append(left-rightmost)
        rightmost = right if rightmost is None else max(rightmost,right)
    observed_valid = parsed > 0 and not issues and not dropped and not tail_bytes and unmatched == 0
    return {'clock_domain': 'stage-local transport elapsed_s; not comparable across stages',
            'observed_elapsed_horizon_s': bound, 'horizon_basis': 'recorded_transport_elapsed_s' if finite(duration) else 'latest_observed_event_lower_bound' if parsed else 'UNAVAILABLE',
            'parsed_event_count': parsed, 'first_observed_event_elapsed_s': first,
            'last_observed_event_elapsed_s': last if parsed else None,
            'document_tools': totals,
            'document_interval_details': details if not invalid_clock else [],
            'interval_details_cap':MAX_INTERVAL_DETAILS,
            'interval_details_omitted':max(0,len(intervals)-len(details)),
            'between_paired_document_intervals_unclassified':({'count':len(gaps),'sum_s':sum(gaps),'max_s':max(gaps) if gaps else None} if not invalid_clock and intervals else None), 'document_paired_interval_sum_s': summed,
            'document_paired_interval_union_s': union, 'document_overlap_s': max(0.0, summed-union) if union is not None else None,
            'outside_paired_document_intervals_unclassified_s': max(0.0, bound-union) if bound is not None and union is not None else None,
            'last_required_read_completion_elapsed_s': required_last if observed_valid and not invalid_clock else None,
            'coverage_completion_time': None,
            'unmatched_document_items': unmatched, 'issues': issues,
            'partial_trailing_bytes': tail_bytes, 'line_cap_dropped_records': dropped,
            'observed_prefix_pairs_complete': observed_valid,
            'interpretation': 'Client-observed native event-envelope intervals, not server service or model/network time. Outside their union is unclassified; partial/invalid pairs may be included in that residual. Last read completion is not an authenticated coverage milestone.'}


def metadata_fields(meta):
    """Bounded typed labels only; malformed values never enter the report verbatim."""
    clean = {}; issues = []
    patterns = {'name':r'[A-Za-z0-9][A-Za-z0-9_/-]{0,159}',
                'request_id':r'b2l-[0-9a-f]{64}',
                'session_id':r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',
                'resume_session':r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}'}
    for key in ('name','request_id','status'):
        if meta.get(key) is None: issues.append('missing_'+key)
    for key, pattern in patterns.items():
        value=meta.get(key)
        clean[key]=value if isinstance(value,str) and re.fullmatch(pattern,value) else None
        if value is not None and clean[key] is None: issues.append('invalid_'+key)
    statuses={'launching','running','completed','process_launch_failed','process_failed','timeout_censored','cancelled','transport_io_failed','invalid_document_tool_audit','unverifiable_rollout_audit','invalid_tool_attempt','invalid_transport_completion','model_identity_unverified','invalid_paper_image_inputs','resume_identity_mismatch'}
    value=meta.get('status');clean['status']=value if isinstance(value,str) and value in statuses else None
    if value is not None and clean['status'] is None:issues.append('invalid_status')
    for key in ('fresh_session','turn_completed'):
        value=meta.get(key);clean[key]=value if type(value) is bool else None
        if value is not None and clean[key] is None:issues.append('invalid_'+key)
    for key in ('start_utc','end_utc'):
        value=meta.get(key);clean[key]=value if isinstance(value,str) and len(value)<=40 and utc(value) is not None else None
        if value is not None and clean[key] is None:issues.append('invalid_'+key)
    audit=meta.get('document_audit',{});audit=audit if isinstance(audit,dict) else {}
    clean['document_audit']={'status':audit.get('status') if isinstance(audit.get('status'),str) and audit['status'] in ('PASS','FAIL') else None,
        'required_material_delivered':audit.get('required_material_delivered') if type(audit.get('required_material_delivered')) is bool else None,
        'receipt_count':audit.get('receipt_count') if type(audit.get('receipt_count')) is int and 0<=audit['receipt_count']<=MAX_LINES else None}
    for key,value in clean['document_audit'].items():
        if audit.get(key) is not None and value is None:issues.append('invalid_document_audit_'+key)
    return clean,issues


def analyze_stage(stage, *, max_bytes=MAX_BYTES, max_lines=MAX_LINES, max_line_bytes=MAX_LINE_BYTES):
    stage = Path(stage)
    if stage.is_symlink() or not stage.is_dir(): raise ValueError('regular stage directory required')
    meta_path = stage/'stage.meta.json'
    if meta_path.exists() or meta_path.is_symlink():
        meta_data, meta_receipt = snapshot(meta_path, max_bytes)
        if not meta_receipt['whole_file_at_snapshot']: raise ValueError('metadata exceeds snapshot cap or changed')
        meta = json.loads(meta_data)
    else:
        meta_data = None; meta = {}
        meta_receipt = {'path':str(meta_path.absolute()),'status':'UNAVAILABLE','reason':'metadata absent'}
    if not isinstance(meta, dict): raise ValueError('metadata must be object')
    event_path = stage/'stage.events.jsonl'
    if event_path.exists() or event_path.is_symlink():
        data, event_receipt = snapshot(event_path, max_bytes)
    else:
        data, event_receipt = b'', {'path':str(event_path.absolute()),'status':'UNAVAILABLE','reason':'event file absent'}
    if meta_data is not None:
        meta_after, _ = snapshot(meta_path, max_bytes)
        if meta_after != meta_data: raise ValueError('metadata changed across event snapshot; retry later')
    elif meta_path.exists() or meta_path.is_symlink():
        raise ValueError('metadata appeared across event snapshot; retry later')
    metrics = analyze_events(data, meta.get('elapsed_s'), max_lines=max_lines, max_line_bytes=max_line_bytes)
    clean, metadata_issues = metadata_fields(meta)
    audit = clean['document_audit']
    result = {'schema_version': SCHEMA, 'stage': clean.get('name'), 'request_id': clean.get('request_id'),
              'session_id': clean.get('session_id'), 'resume_session': clean.get('resume_session'),
              'fresh_session': clean.get('fresh_session'), 'document_recovery_record_present': isinstance(meta.get('document_recovery'),dict),
              'session_matches_resume': clean['session_id']==clean['resume_session'] if clean['session_id'] and clean['resume_session'] else None,
              'recorded_status': clean.get('status'), 'recorded_turn_completed': clean.get('turn_completed'),
              'censored_or_unfinished': (clean['status'] != 'completed' or clean.get('turn_completed') is False) if isinstance(clean.get('status'),str) else None,
              'recorded_start_utc': clean.get('start_utc'), 'recorded_end_utc': clean.get('end_utc'),
              'recorded_transport_elapsed_s': meta.get('elapsed_s') if finite(meta.get('elapsed_s')) else None,
              'recorded_document_audit': {k:audit.get(k) for k in ('status','required_material_delivered','receipt_count')},
              'sources': {'meta':meta_receipt,'events':event_receipt}, 'metrics': metrics,
              'unavailable_attribution': ['model inference','model reading','provider queue','server-exclusive document service','network transport','host preparation before transport clock','host audit/persistence after recorded elapsed_s'],
              'authority': 'observational_only_no_delivery_acceptance_or_accounting_authority'}
    result['metadata_issues'] = metadata_issues
    result['limits'] = {'max_bytes':max_bytes,'max_lines':max_lines,'max_line_bytes':max_line_bytes,'max_elapsed_seconds':MAX_ELAPSED_SECONDS}
    result['measurement_status'] = ('PARTIAL_OR_UNAVAILABLE' if metadata_issues or not metrics['observed_prefix_pairs_complete'] or not event_receipt.get('whole_file_at_snapshot') or meta_data is None else 'RECORDED_PREFIX_ANALYZED')
    result['dedup_key'] = digest(json.dumps([result['stage'],result['request_id'],meta_receipt.get('prefix_sha256'),event_receipt.get('prefix_sha256'),result['limits'],digest(Path(__file__).read_bytes())],sort_keys=True,separators=(',',':')).encode())
    return result


def utc(value):
    if not isinstance(value,str): return None
    try:
        parsed = datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
        return parsed.timestamp() if parsed.tzinfo is not None else None
    except (ValueError, OverflowError, OSError): return None


def report(stages, **limits):
    if not 1 <= len(stages) <= MAX_STAGES: raise ValueError('one to128 explicit stage paths required')
    results = []; seen = {}; duplicates = 0
    for stage in stages:
        item = analyze_stage(stage, **limits)
        identity = (item['stage'],item['request_id'],item['session_id']) if item['request_id'] else ('unbound',str(Path(stage).absolute()))
        binding = [item['sources'][k].get('prefix_sha256') for k in ('meta','events')]
        if identity in seen:
            if seen[identity] != binding: raise ValueError('conflicting snapshots for duplicated stage identity')
            duplicates += 1; continue
        seen[identity] = binding; results.append(item)
    intervals = []; unavailable = 0
    for item in results:
        a,b = utc(item['recorded_start_utc']),utc(item['recorded_end_utc'])
        if a is None or b is None or b < a: unavailable += 1
        else: intervals.append((a,b))
    summed=sum(b-a for a,b in intervals); union=union_seconds(intervals)
    return {'schema_version':SCHEMA,'status':'OBSERVATIONAL_PARTIAL' if any(x['measurement_status']=='PARTIAL_OR_UNAVAILABLE' for x in results) else 'OBSERVATIONAL_REPORT','analyzer_sha256':digest(Path(__file__).read_bytes()),
            'stages':results,'duplicate_stage_copies_excluded':duplicates,
            'recorded_utc_stage_intervals':{'count':len(intervals),'unavailable':unavailable,'sum_s':summed,'union_s':union,'overlap_s':max(0.0,summed-union),'clock_domain':'recorded UTC boundaries; not a sum of cross-stage monotonic clocks'},
            'model_calls':0,'added_prompt_tokens':0,'source_mutations':0,
            'limitations':['No inference, reading, queue or network decomposition is inferred.','Durations are wall time, not CPU time. Nested/overlapping intervals must not be summed as independent cost.','Coverage is the existing recorded audit result, not newly authenticated by this analyzer.','A twice-identical prefix is not an atomic multi-file snapshot; growing/partial/capped records remain explicit.','No causal, performance-equivalence, billing or mathematical conclusion.']}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stages',nargs='+',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--max-bytes',type=int,default=MAX_BYTES)
    parser.add_argument('--max-lines',type=int,default=MAX_LINES)
    parser.add_argument('--max-line-bytes',type=int,default=MAX_LINE_BYTES)
    args=parser.parse_args(argv)
    output=args.output.absolute()
    for stage in args.stages:
        resolved=stage.resolve()
        # A canonical pilot stage lives under run/host/runtime/problem/stage.
        forbidden=resolved.parents[3] if len(resolved.parents)>3 and resolved.parents[1].name=='runtime' and resolved.parents[2].name=='host' else resolved
        if output.resolve().is_relative_to(forbidden): parser.error('output must be outside input run/stage')
    analysis_started=time.perf_counter()
    value=report(args.stages,max_bytes=args.max_bytes,max_lines=args.max_lines,max_line_bytes=args.max_line_bytes)
    data=(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    fd=os.open(output,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    try:
        with os.fdopen(fd,'wb') as handle: handle.write(data)
    except BaseException: raise
    print(json.dumps({'status':value['status'],'output':str(output),'report_bytes':len(data),'report_sha256':digest(data),'stages':len(value['stages']),'analysis_and_report_write_wall_s':time.perf_counter()-analysis_started,'cost_scope':'Offline snapshots, parsing, aggregation and report serialization/write; excludes interpreter startup and this receipt output.'}))

if __name__=='__main__': main()
