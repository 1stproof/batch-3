"""Durable operational exhaustion, never a mathematical verdict or retry grant."""
import hashlib
from datetime import datetime
import json
import os
from pathlib import Path
import re

from pilot_document_tools import regular_bytes

AUTHORITY = 'operational_exhaustion_only_no_review_or_acceptance_authority'


def save(path, value):
    path = Path(path)
    if path.is_symlink():
        raise ValueError('exhaustion receipt cannot be a symlink')
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def moment(value):
    if not isinstance(value, str):
        raise ValueError('missing exhaustion event timestamp')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('exhaustion event timestamp must include timezone')
    return result


def text(value):
    if not isinstance(value, str):
        raise ValueError('scientific review text must be a string')
    # Whitespace, including paragraph formatting, cannot renew a paid review.
    return re.sub(r'\s+', '', value)


def projection(candidate):
    if not isinstance(candidate, dict) or not isinstance(candidate.get('ledger'), dict):
        raise ValueError('missing scientific review candidate')
    if not all(isinstance(candidate.get(k), str) for k in ('proof_markdown','answer_statement')):
        raise ValueError('missing scientific proof or statement')
    rows = candidate['ledger'].get('rows')
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        raise ValueError('invalid scientific ledger')
    return {'proof': text(candidate['proof_markdown']),
            'answer': text(candidate['answer_statement']),
            'claims': sorted(set(text(row['claim']) for row in rows))}


def mode(instruction):
    values = re.findall(r'REVIEW_MODE=(focused|comprehensive)\.', instruction)
    if len(set(values)) != 1:
        raise ValueError('exhaustion guard requires one explicit review lens')
    return values[0]


def metadata(meta):
    capability = meta.get('document_capability')
    if not isinstance(capability, dict):
        raise ValueError('exhausted review lacks immutable document capability')
    cap = Path(capability['path'])
    stage = cap.parent
    if (cap.name != 'document-capability.json' or stage.parent.parent.name != 'runtime'
            or '/'.join(stage.parts[-2:]) != meta['name']):
        raise ValueError('invalid exhausted stage path')
    raw = regular_bytes(stage/'stage.meta.json')
    if json.loads(raw) != meta:
        raise ValueError('exhausted call metadata changed')
    cap_raw = regular_bytes(cap)
    if hashlib.sha256(cap_raw).hexdigest() != capability['sha256']:
        raise ValueError('exhausted capability changed')
    prompt_raw = regular_bytes(stage/'stage.prompt.txt')
    if hashlib.sha256(prompt_raw).hexdigest() != meta['prompt_sha256']:
        raise ValueError('exhausted prompt changed')
    return stage, json.loads(cap_raw), prompt_raw.decode(), hashlib.sha256(raw).hexdigest()


def derive(calls):
    """Reconstruct only exact two-timeout authenticated document recovery pairs."""
    by_name = {c['name']: c for c in calls}
    if len(by_name) != len(calls):
        raise ValueError('duplicate call identity in exhaustion history')
    records = []
    for second in calls:
        if (second.get('module') != 'proof-review' or second.get('status') != 'timeout_censored'
                or second.get('document_recovery') is None):
            continue
        recovery = second['document_recovery']
        first = by_name.get(recovery.get('source', {}).get('stage'))
        if not first:
            raise ValueError('missing exhausted recovery source')
        for item in (first, second):
            if (item.get('status') != 'timeout_censored' or item.get('turn_completed') is not False
                    or item.get('model_verified') is not True or not item.get('session_id')
                    or item.get('document_audit', {}).get('status') != 'PASS'):
                raise ValueError('invalid exhausted review terminal pair')
        if (first.get('document_recovery') is not None or second.get('resume_session') != first['session_id']
                or second['session_id'] != first['session_id']):
            raise ValueError('exhausted pair is not the one same-reviewer recovery')
        if moment(second['end_utc']) <= moment(first['end_utc']):
            raise ValueError('exhausted calls are not chronologically ordered')
        one, scope, prompt, first_sha = metadata(first)
        two, scope2, prompt2, second_sha = metadata(second)
        if one.parent != two.parent:
            raise ValueError('exhausted pair crossed runtime roots')
        from pilot_document_recovery import verify_recovery
        checked = verify_recovery(one.parent.parent.parent, recovery['source'], name=second['name'],
            module='proof-review', model=second['model_actual'], resume_session=second['session_id'],
            prompt=prompt2, scope=scope2)
        if checked != recovery:
            raise ValueError('exhausted recovery provenance changed')
        from pilot_document_tools import allowed_event, audit_operations
        from pilot_document_recovery import inherit_coverage
        from codex_transport import _tool_event
        events = [json.loads(line)['event'] for line in regular_bytes(two/'stage.events.jsonl').decode().splitlines()]
        if any(_tool_event(event) and not allowed_event(event, scope2) for event in events):
            raise ValueError('exhausted recovery contains forbidden tools')
        document_events = [event for event in events if allowed_event(event, scope2)]
        if digest(document_events) != digest(second.get('document_events')):
            raise ValueError('exhausted recovery events changed')
        saved = second.get('persisted_rollout_audit', {})
        if saved.get('status') != 'verified':
            raise ValueError('exhausted recovery delivery is unverified')
        current_audit = audit_operations(scope2, document_events, saved['tool_events'],
                                        second['session_id'], saved['tool_output_receipts'])
        if inherit_coverage(current_audit, checked, scope=scope2,
                            actual_session=second['session_id']) != second['document_audit']:
            raise ValueError('exhausted recovery delivery audit changed')
        marker = '\nCURRENT CANDIDATE, PREMISES AND COMPLETE REQUIRED FINDINGS\n'
        if prompt.count(marker) != 1:
            raise ValueError('missing exact exhausted scientific input')
        packet, _ = json.JSONDecoder().raw_decode(prompt.split(marker, 1)[1])
        candidate = dict(packet['exact_candidate'])
        proof_ref = scope['readonly_artifacts']['proof']
        proof = regular_bytes(Path(proof_ref['path']))
        if hashlib.sha256(proof).hexdigest() != proof_ref['sha256']:
            raise ValueError('exhausted proof artifact changed')
        candidate['proof_markdown'] = proof.decode()
        required = {}
        for ident in scope['required_artifact_ids']:
            ref = scope['readonly_artifacts'][ident]
            data = regular_bytes(Path(ref['path']))
            if hashlib.sha256(data).hexdigest() != ref['sha256']:
                raise ValueError('exhausted required evidence changed')
            required[ident] = ref['sha256']
        binding = {'lens': mode(prompt), 'model': first['model_actual'],
            'original_sha256': scope['original_sha256'], 'scientific': projection(candidate),
            'required_evidence': required, 'findings_sha256': digest(packet.get('prior_findings', []))}
        record = {'schema_version': 1, 'authority': AUTHORITY, 'binding': binding,
            'reviewer_session': first['session_id'], 'stages': [first['name'], second['name']],
            'stage_meta_sha256': [first_sha, second_sha], 'end_utc': second['end_utc'],
            'limits_consumed': {'bounded_calls': 2, 'same_reviewer_recoveries': 1},
            'required_material_delivered': second['document_audit'].get('required_material_delivered') is True}
        record['id'] = digest(record)
        records.append(record)
    return records


def synchronize(folder, calls):
    records = derive(calls)
    path = Path(folder).resolve()/'review-exhaustion.json'
    if path.is_symlink():
        raise ValueError('exhaustion registry cannot be a symlink')
    if path.exists():
        prior = json.loads(regular_bytes(path))
        if not isinstance(prior, list) or len({r.get('id') for r in prior if isinstance(r, dict)}) != len(prior):
            raise ValueError('malformed exhaustion registry')
        if prior != records[:len(prior)]:
            raise ValueError('exhaustion history missing, reordered or changed')
    if records and (not path.exists() or prior != records):
        # Existing records stay byte-equivalent objects; append only newly proven pairs.
        save(path, records)
    return records


class ExhaustedReview(RuntimeError):
    def __init__(self, records):
        self.feedback = {'status': 'review_exhausted', 'authority': AUTHORITY,
            'exhaustions': [{k:r[k] for k in ('id','stages','limits_consumed','required_material_delivered')} for r in records],
            'instruction': 'Continue the same original main research. Both bounded review calls ended without a completed verdict. '
                'Do not reuse that reviewer or request an unchanged review. Preserve all prior findings and failed calls. '
                'Only changed main-authored scientific proof, statement or claims may be considered for a fresh review; '
                'no review or execution approval was granted. Metadata, formatting and retry requests do not renew admission.'}
        super().__init__('unchanged exhausted independent review requires main-owned scientific work')


def guard(problem, instruction, model, resume_session=None):
    if not getattr(problem, 'calls', []):
        return []
    records = synchronize(problem.folder, problem.calls)
    if not records:
        return []
    if resume_session and any(r['reviewer_session'] == resume_session for r in records):
        raise ExhaustedReview(records)
    lens = mode(instruction)
    # Changing a lens or model is not changed scientific material. No distinct-task
    # exception is inferred by this conservative guard.
    relevant = records
    if not relevant:
        return records
    current = projection(problem.current)
    if any(r['binding']['scientific'] == current for r in relevant):
        raise ExhaustedReview(relevant)
    # A later completed original-main turn is necessary, never sufficient for proof acceptance.
    main = next((c for c in reversed(problem.calls) if c.get('status') == 'completed'
        and c.get('module', '').startswith('main') and c.get('session_id') == problem.session
        and moment(c.get('end_utc')) > max(moment(r['end_utc']) for r in relevant)), None)
    if not main:
        raise ExhaustedReview(relevant)
    authored_path = Path(problem.folder)/'review-material-main.json'
    if not authored_path.is_file():
        raise ExhaustedReview(relevant)
    authored = json.loads(regular_bytes(authored_path))
    if authored != {'main_stage': main['name'], 'main_session': problem.session,
                    'answer_sha256': main['answer_sha256'], 'scientific_sha256': digest(current)}:
        raise ValueError('changed review material lacks exact accepted original-main provenance')
    admission = {'authority': AUTHORITY, 'main_stage': main['name'],
        'main_prompt_sha256': main['prompt_sha256'], 'main_answer_sha256': main['answer_sha256'],
        'exhaustions': [r['id'] for r in relevant], 'current_scientific_sha256': digest(current),
        'changed_fields': {r['id']: [k for k in current if current[k] != r['binding']['scientific'][k]] for r in relevant},
        'rationale': 'Changed main-authored scientific content, not independently established mathematical improvement; all fresh review and acceptance gates still apply.'}
    path = Path(problem.folder)/('review-exhaustion-admission-'+digest(admission)+'.json')
    if path.is_symlink():
        raise ValueError('exhaustion admission cannot be a symlink')
    if path.exists() and json.loads(regular_bytes(path)) != admission:
        raise ValueError('exhaustion admission changed')
    if not path.exists():
        save(path, admission)
    return records
