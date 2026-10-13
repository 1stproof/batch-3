"""Stable dispatch evidence identities; never execution or acceptance authority.

Inputs come from host execution results or native authenticated reconstruction.
Presentation wrappers, grouping and filesystem roots do not identify evidence.
"""
import hashlib
import json
from pathlib import PurePosixPath

VERSION = 2
IGNORED = {None, 'not_requested', 'deferred'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def worker(session, output, receipt):
    if not isinstance(session, str) or not session:
        raise ValueError('execution evidence lacks worker producer identity')
    if not isinstance(receipt, dict) or any(not receipt.get(k) for k in ('name','request_id','answer_sha256')):
        raise ValueError('execution evidence lacks worker dispatch provenance')
    return {'kind': 'worker', 'session_id': session, 'receipt': receipt, 'output_sha256': digest(output)}


def probe(path, result, source):
    path = str(PurePosixPath(path))
    if (not (path.startswith('probes/') or (path.startswith('local-verification/') and '/probes/' in path))
            or '..' in PurePosixPath(path).parts or PurePosixPath(path).is_absolute()):
        raise ValueError('execution evidence probe path is not confined')
    return {'kind': 'probe', 'path': path, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'result_sha256': digest(result)}


def atoms(execution):
    values = []
    def probes(group):
        for value in group.values():
            if not isinstance(value, dict) or value.get('status') in IGNORED:
                continue
            if 'source_ref' not in value and value.get('status') in {'unavailable','disabled'}:
                continue  # Host policy/config denial, no admitted probe.
            if 'source_ref' not in value:
                raise ValueError('execution evidence lacks canonical probe producer')
            ref = value['source_ref']; source = value.get('source')
            if not isinstance(source, str) or hashlib.sha256(source.encode()).hexdigest() != ref.get('sha256'):
                raise ValueError('execution evidence probe source changed')
            result = {k: v for k, v in value.items() if k not in {'source','source_ref','stdout_ref'}}
            values.append(probe(str(PurePosixPath(ref['path']).parent), result, source))
    for item in execution:
        if 'historical_stage' in item:
            if item.get('status') == 'completed' and (item.get('output') or {}).get('status') not in {'deferred','unavailable','not_requested'}:
                values.append(worker(item.get('session_id'), item.get('output'), item.get('execution_receipt')))
        elif 'historical_probe' in item:
            result = item['result']
            if result.get('status') in IGNORED:
                continue
            path = item['historical_probe']; artifacts = item.get('artifacts', {})
            sources = [v for k,v in artifacts.items() if k in {path+'/source.py',path+'/source.lean'}]
            if len(sources) != 1:
                raise ValueError('execution evidence probe lacks exact source')
            source = sources[0]
            if hashlib.sha256(source['text'].encode()).hexdigest() != source['sha256']:
                raise ValueError('execution evidence restored source changed')
            values.append(probe(path, result, source['text']))
        else:
            for value in item.get('workers', []):
                output = value.get('output', {})
                if output.get('status') in {'deferred','unavailable','not_requested'}:
                    continue
                values.append(worker(value.get('task_id'), output, value.get('execution_receipt')))
                probes(value.get('probe', {}))
            probes(item.get('main_probe', {}))
    # Repeated presentation of one producer is not new work. Separate runs have
    # distinct worker sessions or probe paths even when their output is identical.
    producers = {}
    for value in values:
        producer = (value['kind'], value['path']) if value['kind']=='probe' else (value['kind'], value['receipt']['name'], value['receipt']['request_id'])
        if producer in producers and producers[producer] != value:
            raise ValueError('conflicting execution content for one authenticated producer')
        producers[producer] = value
    unique = {digest(value): value for value in values}
    return {key: unique[key] for key in sorted(unique)}
