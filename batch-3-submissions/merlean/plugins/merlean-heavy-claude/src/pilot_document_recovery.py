"""Verified delivery continuity for one existing same-reviewer timeout recovery.

This module carries historical delivery facts, never a review verdict or proof
acceptance. It neither dispatches work nor combines partial artifact reads.
"""
import json
from pathlib import Path
import re

from pilot_document_tools import (NAMESPACE, allowed_event, audit_operations,
                                  digest, encoded, invocation_guidance,
                                  regular_bytes, validate_scope)
from pilot_document_tools import expand_chunk_coverage, required_read_progress

TIMEOUT_RECOVERY_GUIDANCE = (
    '\nHOST RECOVERY: The previous bounded call was interrupted at its call deadline. '
    'Continue the same assigned task from the preserved context; no partial response was accepted. '
    'Return a substantive checkpoint promptly.\n')


def recovery_delivery_guidance(scope, audit):
    return ('\nVERIFIED SAME-REVIEWER REQUIRED DELIVERY PROGRESS\n' +
            encoded(required_read_progress(scope, audit['artifact_coverage'])) +
            '\nRead the missing pages directly; do not re-read completed pages merely to navigate. '
            'This progress applies only to this authenticated same-session recovery.\n')


def _stage_path(root, stage):
    if not isinstance(stage, str) or re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', stage) is None:
        raise ValueError('invalid document recovery stage')
    if any(part in ('.', '..') for part in stage.split('/')):
        raise ValueError('invalid document recovery stage')
    return Path(root).resolve() / 'runtime' / stage


def recovery_reference(root, meta):
    """Bind the exact terminal timeout metadata selected by the existing loop."""
    data = regular_bytes(_stage_path(root, meta['name']) / 'stage.meta.json')
    if json.loads(data) != meta:
        raise ValueError('document recovery metadata differs from returned stage')
    return {'stage': meta['name'], 'meta_sha256': digest(data)}


def _immutable_scope(scope):
    return {key: value for key, value in scope.items() if key not in ('producer', 'receipt_path')}


def verify_recovery(root, reference, *, name, module, model, resume_session, prompt, scope):
    """Re-audit the immediate prior delivery before admitting a recovery call."""
    if (type(reference) is not dict or set(reference) != {'stage', 'meta_sha256'}
            or not isinstance(reference['meta_sha256'], str)
            or re.fullmatch('[0-9a-f]{64}', reference['meta_sha256']) is None):
        raise ValueError('invalid document recovery reference')
    previous = _stage_path(root, reference['stage'])
    current = _stage_path(root, name)
    if previous == current or previous.parent != current.parent:
        raise ValueError('document recovery must remain in the same problem')
    data = regular_bytes(previous / 'stage.meta.json')
    if digest(data) != reference['meta_sha256']:
        raise ValueError('document recovery metadata changed')
    meta = json.loads(data)
    if (type(meta) is not dict or meta.get('name') != reference['stage']
            or meta.get('status') != 'timeout_censored' or meta.get('module') != module
            or not resume_session or meta.get('session_id') != resume_session
            or meta.get('model_requested') != model or meta.get('model_actual') != model
            or meta.get('model_verified') is not True or meta.get('internet_browse') is not False
            or meta.get('document_recovery') is not None
            or meta.get('tool_event_count') != 0 or meta.get('tool_events') != []
            or meta.get('persisted_tool_event_count') != 0 or meta.get('persisted_tool_events') != []):
        raise ValueError('prior stage is not an eligible exact reviewer timeout')
    capability = meta.get('document_capability', {})
    capability_path = previous / 'document-capability.json'
    if capability.get('path') != str(capability_path):
        raise ValueError('prior recovery capability is outside its stage')
    cap_bytes = regular_bytes(capability_path)
    if digest(cap_bytes) != capability.get('sha256'):
        raise ValueError('prior recovery capability changed')
    prior_scope = validate_scope(json.loads(cap_bytes))
    if (scope.get('mode') != 'review' or prior_scope['mode'] != 'review'
            or encoded(_immutable_scope(prior_scope)) != encoded(_immutable_scope(scope))
            or scope['problem_id'] != name.split('/')[0]
            or prior_scope['producer'] != {'stage': meta['name'], 'request_id': meta.get('request_id'),
                                          'session_id': meta.get('resume_session')}
            or prior_scope['receipt_path'] != str(previous / 'document-operations.jsonl')):
        raise ValueError('document recovery immutable scope or producing identity differs')
    old_prompt = regular_bytes(previous / 'stage.prompt.txt')
    suffix = '\n' + invocation_guidance('review')
    old_text = old_prompt.decode('utf-8')
    if (digest(old_prompt) != meta.get('prompt_sha256') or len(old_prompt) != meta.get('prompt_bytes')
            or not old_text.endswith(suffix)):
        raise ValueError('document recovery is not the exact same logical prompt')
    saved = meta.get('persisted_rollout_audit', {})
    # stage.meta.json sorts object keys; native argument/result hashes retain
    # their original order. Re-audit the preserved raw event stream instead.
    from codex_transport import _tool_event
    event_bytes = regular_bytes(previous / 'stage.events.jsonl')
    raw_events = [json.loads(line)['event'] for line in event_bytes.decode().splitlines()]
    if any(_tool_event(event) and not allowed_event(event, prior_scope) for event in raw_events):
        raise ValueError('prior timeout raw events contain a forbidden tool')
    events = [event for event in raw_events if allowed_event(event, prior_scope)]
    if json.dumps(events, sort_keys=True) != json.dumps(meta.get('document_events'), sort_keys=True):
        raise ValueError('prior timeout raw document events differ from stage metadata')
    if (saved.get('status') != 'verified' or 'tool_output_receipts' not in saved
            or any(not allowed_event(event, prior_scope) for event in events)
            or any(event.get('namespace') != NAMESPACE or event.get('name') not in ('read_artifact', 'read_required_evidence')
                   for event in saved.get('tool_events', []))):
        raise ValueError('prior timeout contains unverified or forbidden tool evidence')
    verified = audit_operations(prior_scope, events, saved['tool_events'], resume_session,
                                saved['tool_output_receipts'])
    if verified.get('status') != 'PASS' or json.dumps(verified, sort_keys=True) != json.dumps(meta.get('document_audit'), sort_keys=True):
        raise ValueError('prior document delivery audit cannot be independently reproduced')
    expected = old_text[:-len(suffix)] + TIMEOUT_RECOVERY_GUIDANCE
    # Old fixtures/callers without the progress suffix remain exact legacy prompts.
    if prompt not in (expected + suffix, expected + recovery_delivery_guidance(scope, verified) + suffix):
        raise ValueError('document recovery is not the exact same logical prompt')
    return {'schema_version': 1, 'source': dict(reference), 'source_request_id': meta['request_id'],
            'source_prompt_sha256': meta['prompt_sha256'], 'current_prompt_sha256': digest(prompt.encode()),
            'source_capability_sha256': capability['sha256'], 'source_receipt_sha256': verified['receipt_sha256'],
            'source_events_sha256': digest(event_bytes),
            'session_id': resume_session, 'model': model, 'problem_id': scope['problem_id'],
            'original_sha256': scope['original_sha256'],
            'immutable_scope_sha256': digest(encoded(_immutable_scope(scope)).encode()),
            'full_artifact_ids': [key for key, complete in verified['artifact_coverage'].items() if complete is True],
            'authority': 'same-reviewer prior complete delivery only; no comprehension or acceptance'}


def inherit_coverage(audit, recovery, *, scope, actual_session):
    """Carry only complete prior reads; retain the current stage audit separately."""
    if actual_session != recovery['session_id']:
        raise ValueError('document recovery actual reviewer session differs')
    if audit.get('status') != 'PASS':
        return audit
    coverage = dict(audit['artifact_coverage'])
    for ident in recovery['full_artifact_ids']:
        if ident not in coverage:
            raise ValueError('recovered artifact is absent from current scope')
        coverage[ident] = True
    coverage = expand_chunk_coverage(scope, coverage)
    required = {ident: coverage[ident] for ident in scope['required_artifact_ids']}
    return {**audit, 'current_attempt_artifact_coverage': dict(audit['artifact_coverage']),
            'artifact_coverage': coverage, 'required_artifact_coverage': required,
            'required_material_delivered': all(required.values()),
            'recovery_inheritance': recovery}
