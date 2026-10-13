"""Typed main updates and exact host-owned candidate selection; no prose authority."""
import copy
import hashlib
import json
from pilot_route_scouts import validate_tasks
from pilot_research_continuation import validate_research_work



DRAFT_CHECKPOINT_FIELDS = frozenset({'response_type', 'proof_revision', 'reason'})
DRAFT_CHECKPOINT_GUIDANCE = (
    'When the host enables proof documents, a save-only draft turn has EXACTLY this JSON shape: '
    '{"response_type":"draft_checkpoint","proof_revision":"<exact current revision from read_current_proof>",'
    '"reason":"<nonempty operational reason>"}. '
    'Those are the only three fields. Do not include proof_sha256, manifest_sha256, proof_markdown, '
    'selected_candidate_sha256, research_work, findings, proposed_work, review_request or any other field. '
    'Document-tool hashes are read/save receipts, not additional draft_checkpoint fields. '
    'Read the current revision; a stale revision is rejected. This response only preserves an unsubmitted '
    'draft and grants no scientific candidate change, execution, review, certificate, grade or acceptance authority. '
    'To submit changed scientific work, return the complete candidate_update with the exact current proof_revision, '
    'complete saved proof body and consistent scientific sidecars. A pending draft cannot be bypassed with '
    'blocked_checkpoint. Never remove scientific content from a required submission merely to fit a save-only shape.'
)


def draft_checkpoint_diagnostics(raw):
    """Literal shape diagnostics only; do not rewrite or accept the response."""
    if not isinstance(raw, dict):
        return {'expected_fields': sorted(DRAFT_CHECKPOINT_FIELDS), 'error': 'response must be an object'}
    result = {'expected_fields': sorted(DRAFT_CHECKPOINT_FIELDS),
              'missing_fields': sorted(DRAFT_CHECKPOINT_FIELDS - set(raw)),
              'unexpected_fields': sorted(set(raw) - DRAFT_CHECKPOINT_FIELDS)}
    result['reason_nonempty_string'] = isinstance(raw.get('reason'), str) and bool(raw['reason'].strip())
    result['proof_revision_nonempty_string'] = isinstance(raw.get('proof_revision'), str) and bool(raw['proof_revision'].strip())
    return result


CHECKPOINT_FINDING_SEVERITIES = ('fatal', 'gap', 'nitpick')
CHECKPOINT_FINDING_KINDS = ('mathematical', 'certificate')
CHECKPOINT_FINDING_SCHEMA = {
    'id': 'nonempty stable string',
    'severity': list(CHECKPOINT_FINDING_SEVERITIES),
    'kind': list(CHECKPOINT_FINDING_KINDS),
    'finding': 'nonempty substantive string; exact key finding, not text',
}
CHECKPOINT_FINDING_GUIDANCE = (
    'Each unreviewed_findings entry requires these named fields (additional fields remain preserved): '
    + json.dumps(CHECKPOINT_FINDING_SCHEMA, ensure_ascii=False) + '. '
    'This array introduces scientific findings only. kind=host_gate is not permitted here. '
    'Inherited host-gate and workflow records remain preserved by the host; refer to their '
    'unchanged IDs and full administrative notes in checkpoint_metadata.reason instead of '
    'copying them into this scientific array or relabeling them mathematical/certificate. '
    'Do not erase substantive scientific findings to satisfy formatting. Preserve every '
    'scientific claim and its correct classification; if the checkpoint cannot represent '
    'substantive new work, return a complete candidate_update. No schema correction grants '
    'review, worker, certificate or acceptance authority.'
)


def checkpoint_finding_diagnostics(findings):
    """Report literal protocol defects only; never classify or rewrite a finding."""
    errors = []
    if not isinstance(findings, list):
        return [{'path':'unreviewed_findings','expected':'array','actual':copy.deepcopy(findings)}]
    for index, finding in enumerate(findings):
        path = f'unreviewed_findings[{index}]'
        if not isinstance(finding, dict):
            errors.append({'path':path,'expected':'object','actual':copy.deepcopy(finding)})
            continue
        for field in ('id', 'severity', 'kind', 'finding'):
            value = finding.get(field)
            allowed = CHECKPOINT_FINDING_SEVERITIES if field=='severity' else CHECKPOINT_FINDING_KINDS if field=='kind' else None
            valid = isinstance(value,str) and (value in allowed if allowed else bool(value))
            if not valid:
                error={'path':path+'.'+field,'expected':CHECKPOINT_FINDING_SCHEMA[field],
                       'present':field in finding,'actual':copy.deepcopy(value)}
                if field=='finding' and 'text' in finding:
                    error['unsupported_alias_present']='text; no automatic alias conversion'
                errors.append(error)
    return errors


def candidate_hash(value):
    return hashlib.sha256((json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest()


def full_candidate(value):
    return (isinstance(value, dict) and isinstance(value.get('proof_markdown'), str)
            and bool(value['proof_markdown'].strip()) and isinstance(value.get('ledger'), dict)
            and isinstance(value['ledger'].get('rows'), list))


def apply_main_response(answer, known, *, allow_legacy=False):
    if not isinstance(answer, dict):
        raise ValueError('typed main response must be an object')
    kind = answer.get('response_type')
    if kind == 'candidate_update' or (kind is None and allow_legacy):
        if 'research_work' in answer:
            raise ValueError('research_work is checkpoint-only scheduling evidence, never a candidate field')
        candidate = copy.deepcopy(answer)
        candidate.pop('response_type', None)
        candidate.pop('proof_revision', None)  # Operational save binding; never scientific hash churn.
        validate_tasks(candidate.get('route_scout_tasks', []))
        if not full_candidate(candidate):
            raise ValueError('candidate_update requires complete proof_markdown and structured ledger')
        return candidate, None
    if kind != 'blocked_checkpoint':
        raise ValueError('response_type must be candidate_update or blocked_checkpoint')
    keys = {'response_type', 'selected_candidate_sha256', 'checkpoint_metadata', 'proposed_work',
            'unreviewed_findings', 'review_request'}
    if set(answer) not in (keys, keys | {'research_work'}):
        raise ValueError('blocked_checkpoint requires exactly the documented root keys')
    validate_research_work(answer.get('research_work'))
    binding = answer['selected_candidate_sha256']
    if not isinstance(binding, str) or binding not in known or candidate_hash(known[binding]) != binding:
        raise ValueError('checkpoint selected candidate is not a known immutable host artifact')
    metadata = answer['checkpoint_metadata']
    if (not isinstance(metadata, dict) or set(metadata) != {'reason'}
            or not isinstance(metadata['reason'], str) or not metadata['reason'].strip()):
        raise ValueError('checkpoint_metadata requires only a nonempty reason; substantive fields belong in candidate_update')
    work = answer['proposed_work']
    if (not isinstance(work, dict) or set(work) not in ({'sol_tasks', 'python_probe', 'lean_probe', 'lean_probe_rows'},
                                 {'sol_tasks', 'python_probe', 'lean_probe', 'lean_probe_rows', 'route_scout_tasks'})
            or not isinstance(work['sol_tasks'], list) or len(work['sol_tasks']) > 2
            or any(not isinstance(work[k], str) for k in ('python_probe', 'lean_probe'))
            or not isinstance(work['lean_probe_rows'], list)):
        raise ValueError('checkpoint proposed_work must explicitly enumerate every task and probe')
    if (answer['review_request'] not in ('none', 'task_review', 'substantive_reassessment', 'route_exploration')
            or not isinstance(answer['unreviewed_findings'], list)):
        raise ValueError('invalid checkpoint review request or findings')
    defects = checkpoint_finding_diagnostics(answer['unreviewed_findings'])
    if defects:
        raise ValueError('checkpoint finding schema errors: ' + json.dumps(defects, ensure_ascii=False))
    if work['python_probe'] or work['lean_probe']:
        raise ValueError('checkpoint probes must be proposed as exact sol_tasks for independent task approval')
    validate_tasks(work.get('route_scout_tasks', []))
    candidate = copy.deepcopy(known[binding])
    if 'route_scout_tasks' in candidate or 'route_scout_tasks' in work:
        candidate['route_scout_tasks'] = copy.deepcopy(work.get('route_scout_tasks', []))
    candidate.update(copy.deepcopy(work))  # Exact proposals replace old tasks; never inherit authorization.
    if answer['unreviewed_findings']:
        candidate['unreviewed_checkpoint_findings'] = copy.deepcopy(answer['unreviewed_findings'])
    actionable = (any(work[k] for k in ('sol_tasks', 'python_probe', 'lean_probe'))
                  or bool(work.get('route_scout_tasks')) or answer['review_request'] != 'none' or bool(answer['unreviewed_findings']))
    return candidate, {'raw_checkpoint': copy.deepcopy(answer), 'selected_candidate_sha256': binding,
                       'effective_candidate_sha256': candidate_hash(candidate), 'actionable': bool(actionable)}


def replay_main_responses(answers, *, legacy_indices=()):
    """Replay preserved legacy full artifacts plus explicit typed updates in chronology."""
    known, current = {}, None
    for index, answer in enumerate(answers):
        if isinstance(answer, dict) and answer.get('response_type') == 'draft_checkpoint':
            continue  # Operational saved-document pause never replaces scientific candidate.
        try:
            candidate, _ = apply_main_response(answer, known, allow_legacy=index in legacy_indices)
        except ValueError:
            continue  # Invalid completed replies remain evidence, never current-candidate authority.
        known[candidate_hash(candidate)] = candidate
        current = candidate
    return current, known
