"""Durable evidence-based research scheduling; never proof or grade authority.

Only the host calls observation after its existing provenance/independence and
substantive validators. Candidate fields are never interpreted as review receipts.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path

from pilot_candidate_contract import candidate_hash, full_candidate
from pilot_research_continuation import validate_research_work

DOMAINS = ('original_scope', 'mathematical', 'certification', 'delivery')
GUIDANCE = (
    'When a coherent high-level proof skeleton looks promising, include convergence_outline '
    '{skeleton:string,why_promising:string,open_gap_ids:string[]} in the candidate. This starts '
    'convergence before proof completion: prioritize its necessary gaps, scope, validation and write-up; '
    'nonessential alternative route work is paused. The outline is a scheduling proposal, never proof. '
    'During convergence each research Sol task must name current consumer_ids from open_gap_ids or '
    'independent current mathematical finding IDs and explain necessity in its context; independent task approval remains required. '
    'Preserve the best independently reviewed original-scope candidate while exploring alternatives. '
    'Track original-scope, mathematical, certification and delivery deficits separately. '
    'A broader or conditional result does not replace the original answer. Reopen a settled scope '
    'decision only for changed exact evidence or a newly evidenced objection, retaining the old decision. '
    'Before repeating auxiliary work, identify its exact consumers and the uncertainty it can reduce; '
    'if the original crux is unchanged, explain new value or reconsider the route. '
    'Faithful encoding cost can trigger independent certificate retriage, never a waiver. '
    'Preserve failures and useful negative research. These records grant no acceptance, execution '
    'approval or paid review eligibility and impose no lifetime cap or strategy rotation.'
)


def digest(value):
    return candidate_hash(value)


def _hash(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def observation(candidate, evidence, *, original_sha256, receipts=(), validated=False):
    """Bind a host-validated observation. No caller-supplied candidate receipt is read.

    ``validated`` records completion of the pre-existing domain validator, not a
    model claim. Review/scope additionally require real independent host receipts.
    Certification/delivery can be host deterministic validations without reviewers.
    """
    if validated is not True or not _hash(original_sha256):
        raise ValueError('convergence observations require host validation and frozen original binding')
    return {'candidate_sha256': digest(candidate), 'original_sha256': original_sha256,
            'evidence_sha256': digest(evidence), 'evidence': copy.deepcopy(evidence),
            'receipts': copy.deepcopy(list(receipts)), 'host_validated': True}


def _validate_observation(value, binding, original, domain):
    if (not isinstance(value, dict) or value.get('candidate_sha256') != binding
            or value.get('original_sha256') != original or value.get('host_validated') is not True
            or value.get('evidence_sha256') != digest(value.get('evidence'))
            or not isinstance(value.get('evidence'), dict)):
        raise ValueError('stale, unvalidated or altered convergence ' + domain + ' evidence')
    receipts = value.get('receipts', [])
    if domain in ('review', 'scope', 'advisory_scope'):
        required = 2 if domain == 'scope' else 1
        if not isinstance(receipts, list) or len(receipts) != required:
            raise ValueError('convergence needs the independent host review receipt census')
        sessions = []
        for receipt in receipts:
            origin = receipt.get('independent_recovery_origin', {}) if isinstance(receipt, dict) else {}
            recovered = (domain != 'scope' and isinstance(origin, dict) and bool(origin)
                and origin.get('status') == 'timeout_censored' and origin.get('fresh_session') is True
                and not origin.get('resume_session') and origin.get('model_actual') == 'gpt-6-astra'
                and origin.get('model_verified') is True and _hash(origin.get('prompt_sha256'))
                and origin.get('reviewed_candidate_sha256') == binding
                and origin.get('session_id') == receipt.get('session_id') == receipt.get('resume_session')
                and origin.get('name') != receipt.get('name'))
            fresh = isinstance(receipt, dict) and receipt.get('fresh_session') is True and not receipt.get('resume_session')
            if (not isinstance(receipt, dict) or receipt.get('status') != 'completed'
                    or receipt.get('model_verified') is not True or not (fresh or recovered)
                    or not receipt.get('session_id')
                    or receipt.get('reviewed_candidate_sha256') != binding
                    or not _hash(receipt.get('prompt_sha256')) or not _hash(receipt.get('answer_sha256'))):
                raise ValueError('convergence review receipt is incomplete or stale')
            sessions.append(receipt['session_id'])
        if len(set(sessions)) != required:
            raise ValueError('scope panel must contain distinct reviewers')


def _deficit(status='unknown', items=(), evidence=None):
    return {'status': status, 'items': copy.deepcopy(list(items)), 'evidence_sha256': evidence}


def _core(record):
    return digest({k: {field: value for field, value in record['deficits'][k].items()
                       if field != 'evidence_sha256'} for k in DOMAINS[:2]})


def _findings(review, kind):
    return [f for f in review.get('unresolved_findings', [])
            if f.get('severity') in ('fatal', 'gap') and
            (f.get('kind', 'mathematical') == 'certificate') == (kind == 'certification')
            and f.get('kind') != 'host_gate']


def _review_deficits(evidence, ref):
    math = _findings(evidence, 'mathematical')
    math += [{'id': 'review-gap-' + digest(gap), 'finding': gap} for gap in evidence.get('gaps', [])]
    for decision in evidence.get('triage_decisions', []):
        if decision.get('trigger') == 'research_gap':
            math.append({'id': 'row-' + decision['row_id'], 'finding': decision.get('reason'),
                         'row_id': decision['row_id']})
    # Focused first-gap review is useful evidence, never comprehensive closure.
    complete = (evidence.get('positive_authority') is not False and evidence.get('review_mode') == 'comprehensive' and not math
                and (evidence.get('verdict') == 'PASS_COMPLETE_PROOF'
                     or evidence.get('mathematically_ready') is True))
    cert = _findings(evidence, 'certification')
    cert += [{'id': 'row-' + d['row_id'], 'row_id': d['row_id'], 'finding': d.get('reason')}
             for d in evidence.get('triage_decisions', []) if d.get('selected') is True]
    return (_deficit('closed' if complete else 'open' if math else 'unknown', math, ref),
            _deficit('open' if cert else 'unknown', cert, ref))


def update_convergence(previous, *, original_sha256, candidate, review=None, scope=None, advisory_scope=None,
                       certification=None, delivery=None, research_work=None, auxiliary_work=None):
    """Pure JSON reducer. Exact host observations, not claimed progress, change status.

    Scope evidence is {passed: bool, reports: [two reports], errors: [...]}; the
    host must run audit_original_scope first. Certification/delivery use
    {passed: bool, deficits: [...], ...} after their existing deterministic gates.
    Scope updates are deduplicated by exact evidence, not round counters.
    """
    if not _hash(original_sha256) or not full_candidate(candidate):
        raise ValueError('convergence needs frozen original and complete candidate')
    state = ({**previous, **{key: dict(previous[key]) for key in
        ('candidates', 'observations', 'research_archive', 'auxiliary_archive')},
        'scope_decisions': list(previous['scope_decisions'])} if previous else {
        'schema_version': 1, 'original_sha256': original_sha256, 'candidates': {},
        'observations': {}, 'scope_decisions': [], 'research_archive': {},
        'auxiliary_archive': {}, 'best_reviewed_original_candidate': None,
        'best_reviewed_mathematical_candidate': None})
    if state.get('schema_version') != 1 or state.get('original_sha256') != original_sha256:
        raise ValueError('convergence original binding or schema changed')
    binding = digest(candidate)
    prior_current = state.get('current_candidate_sha256')
    old_record = state['candidates'].get(binding)
    record = ({**old_record, 'deficits': copy.deepcopy(old_record['deficits']),
               'observation_refs': dict(old_record['observation_refs'])} if old_record else {
        'candidate_sha256': binding, 'candidate': copy.deepcopy(candidate),
        'scope_qualification': 'unreviewed_original_scope',
        'deficits': {kind: _deficit() for kind in DOMAINS}, 'observation_refs': {}})
    if record['candidate'] != candidate:
        raise ValueError('immutable convergence candidate changed')
    old_core = _core(record)
    changes = []
    for domain, value in [('review', review), ('advisory_scope', advisory_scope), ('scope', scope), ('certification', certification), ('delivery', delivery)]:
        if value is None:
            continue
        _validate_observation(value, binding, original_sha256, domain)
        ref = digest(value)
        state['observations'].setdefault(ref, copy.deepcopy(value))
        if record['observation_refs'].get(domain) == ref:
            continue
        prior_ref = record['observation_refs'].get(domain)
        if (prior_ref and state['observations'][prior_ref]['evidence_sha256'] == value['evidence_sha256']):
            continue  # New transport or scheduling metadata alone does not reopen a decision.
        record['observation_refs'][domain] = ref
        evidence = value['evidence']
        if domain == 'review':
            mathematical, cert = _review_deficits(evidence, ref)
            if evidence.get('review_mode') == 'comprehensive' and evidence.get('positive_authority') is not False:
                record['observation_refs']['comprehensive_review'] = ref
            # A focused check cannot erase the exact candidate's previously
            # complete review merely by omitting a whole-proof verdict. A new
            # adverse mathematical finding still invalidates the banked answer.
            previous_math = record['deficits']['mathematical']
            if not ((evidence.get('review_mode') != 'comprehensive' or evidence.get('positive_authority') is False)
                    and mathematical['status'] == 'unknown' and previous_math['status'] == 'closed'):
                record['deficits']['mathematical'] = mathematical
            # A review does not overturn independently validated certification with
            # identical obligations; changed selection/findings requires revalidation.
            previous_cert = record['deficits']['certification']
            if evidence.get('positive_authority') is False:
                # Partial delivery cannot erase an existing selected-certificate deficit.
                prior_items = previous_cert['items']
                additional = [item for item in cert['items'] if item not in prior_items]
                cert = (_deficit('open', prior_items + additional, ref) if additional else previous_cert)
            if previous_cert['status'] != 'closed' or cert['items'] != previous_cert['items']:
                record['deficits']['certification'] = cert
        elif domain == 'advisory_scope':
            if evidence.get('verdict') not in ('adequate', 'inadequate', 'unknown'):
                raise ValueError('advisory scope requires actual independent scope verdict')
            # Advice fixes the working interpretation, never the final scope gate.
            record['scope_qualification'] = 'advisory_' + evidence['verdict'] + '_not_final'
            if record['deficits']['original_scope']['status'] != 'closed' or evidence['verdict'] == 'inadequate':
                record['deficits']['original_scope'] = _deficit(
                    'open' if evidence['verdict'] == 'inadequate' else 'unknown',
                    evidence.get('missing_evidence', []) or evidence.get('findings', []), ref)
            state['scope_decisions'].append({'candidate_sha256': binding, 'observation_sha256': ref,
                'previous_observation_sha256': prior_ref, 'status': evidence['verdict'],
                'authority': 'advisory_only',
                'reopening_basis': 'changed_exact_independent_evidence' if prior_ref else 'initial_independent_evidence'})
        elif domain == 'scope':
            reports = evidence.get('reports')
            if (type(evidence.get('passed')) is not bool or not isinstance(reports, list) or len(reports) != 2
                    or not isinstance(evidence.get('errors'), list)):
                raise ValueError('scope evidence requires audited panel and errors')
            if evidence['passed'] and (evidence['errors'] or any(
                    r.get('verdict') != 'PASS_FULL_SCOPE' or r.get('gaps') or r.get('extra_assumptions')
                    or not r.get('coverage') or any(c.get('result') != 'covered' for c in r['coverage'])
                    for r in reports)):
                raise ValueError('scope pass contradicts panel evidence')
            items = evidence['errors'] or [g for r in reports for g in r.get('gaps', [])]
            record['deficits']['original_scope'] = _deficit('closed' if evidence['passed'] else 'open', items, ref)
            record['scope_qualification'] = 'audited_original_scope' if evidence['passed'] else 'original_scope_rejected'
            state['scope_decisions'].append({'candidate_sha256': binding, 'observation_sha256': ref,
                'previous_observation_sha256': prior_ref, 'status': record['deficits']['original_scope']['status'],
                'reopening_basis': 'changed_exact_independent_evidence' if prior_ref else 'initial_independent_evidence'})
        else:
            if type(evidence.get('passed')) is not bool or not isinstance(evidence.get('deficits'), list):
                raise ValueError(domain + ' requires explicit host result and deficits')
            if evidence['passed'] and evidence['deficits']:
                raise ValueError('passing result cannot retain deficits')
            record['deficits'][domain] = _deficit('closed' if evidence['passed'] else 'open', evidence['deficits'], ref)
        changes.append(domain)
    state['candidates'][binding] = record
    state['current_candidate_sha256'] = binding
    outline = candidate.get('convergence_outline')
    if outline is not None and (not isinstance(outline, dict)
            or any(not isinstance(outline.get(k), str) or not outline[k].strip() for k in ('skeleton', 'why_promising'))
            or not isinstance(outline.get('open_gap_ids'), list)
            or any(not isinstance(i, str) or not i for i in outline['open_gap_ids'])):
        raise ValueError('convergence outline needs substantive skeleton, promise and stable open gap IDs')
    phase = copy.deepcopy(state.get('phase', {'name': 'exploring', 'consumer_ids': [], 'evidence_refs': []}))
    ready = outline is not None or record['deficits']['mathematical']['status'] == 'closed'
    if phase['name'] == 'reconsidering':
        ready = ((outline is not None and digest(outline) != phase.get('rejected_outline_sha256'))
                 or (review is not None and record['deficits']['mathematical']['status'] == 'closed'
                     and digest(review) not in phase.get('evidence_refs', [])))
    if ready:
        if phase['name'] != 'converging':
            phase = {'name': 'converging', 'anchor_candidate_sha256': binding,
                     'consumer_ids': [], 'evidence_refs': [], 'basis': 'promising_skeleton' if outline else 'reviewed_mathematics'}
        phase['consumer_ids'] = sorted(set(phase['consumer_ids']) | set((outline or {}).get('open_gap_ids', [])))
    if review is not None:
        findings = review['evidence'].get('unresolved_findings', [])
        phase['consumer_ids'] = sorted(set(phase['consumer_ids']) | {
            f['id'] for f in findings if f.get('kind', 'mathematical') == 'mathematical' and f.get('severity') in ('gap', 'fatal')})
        reopening = review['evidence'].get('convergence_reopening', {})
        if (any(f.get('severity') == 'fatal' and f.get('kind', 'mathematical') == 'mathematical' for f in findings)
                or (reopening.get('reason') in ('counterexample', 'key_bridge_failed', 'original_scope_uncovered')
                    and reopening.get('finding_ids') and set(reopening['finding_ids']).issubset({f['id'] for f in findings}))):
            phase.update(name='reconsidering', basis='independently_evidenced_obstruction', evidence_refs=[digest(review)])
            phase['rejected_outline_sha256'] = digest(outline)
    if ((scope is not None and scope['evidence']['passed'] is False)
            or (advisory_scope is not None and advisory_scope['evidence']['verdict'] == 'inadequate')):
        phase.update(name='reconsidering', basis='independent_original_scope_objection',
                     evidence_refs=[digest(scope or advisory_scope)])
        phase['rejected_outline_sha256'] = digest(outline)
    state['phase'] = phase
    best = state.get('best_reviewed_original_candidate')
    eligible = [key for key, item in state['candidates'].items()
                if item['deficits']['original_scope']['status'] == 'closed'
                and item['deficits']['mathematical']['status'] == 'closed']
    # Preserve a complete reviewed original answer across experiments. Never rank
    # proofs by length, newer timestamps, fewer reported findings or self grading.
    state['best_reviewed_original_candidate'] = best if best in eligible else next(iter(eligible), None)
    mathematical = [key for key, item in state['candidates'].items()
                    if item['deficits']['mathematical']['status'] == 'closed']
    previous_math = state.get('best_reviewed_mathematical_candidate')
    scope_rank = {'audited_original_scope': 3, 'advisory_adequate_not_final': 2,
                  'unreviewed_original_scope': 1, 'advisory_unknown_not_final': 1}
    # A reviewed NL answer is banked before certification. Scope remains explicit;
    # equal qualification preserves the incumbent instead of preferring newer prose.
    preference = ([previous_math] if previous_math in mathematical else []) + mathematical
    state['best_reviewed_mathematical_candidate'] = (max(preference,
        key=lambda key: scope_rank.get(state['candidates'][key]['scope_qualification'], 0)) if preference else None)
    if research_work is not None:
        work = validate_research_work(research_work)
        state['research_archive'].setdefault(digest(work), {'candidate_sha256': binding, 'work': work})
    new_core = _core(record)
    triggers = []
    if changes:
        triggers.append('independent_evidence_changed')
    if prior_current and prior_current != binding and state['best_reviewed_original_candidate'] != binding:
        triggers.append('preserve_best_original_answer_during_alternative_research')
    if research_work is not None and old_core == new_core:
        triggers.append('research_recorded_without_claiming_gap_closure')
    if auxiliary_work is not None:
        items = auxiliary_work if isinstance(auxiliary_work, list) else [auxiliary_work]
        for item in items:
            checked = check_auxiliary_work(state, item)
            archived = {**checked, 'candidate_sha256': binding, 'core_evidence_sha256': new_core}
            if any(a['core_evidence_sha256'] == new_core and a['consumers'] == checked['consumers']
                   for a in state['auxiliary_archive'].values()) and not checked.get('new_value'):
                triggers.append('auxiliary_crux_unchanged_reconsider_value')
            state['auxiliary_archive'].setdefault(digest(archived), archived)
    state['triggers'] = sorted(set(triggers))
    return state


def check_auxiliary_work(state, work):
    """Validate an explicit consumer map; it does not authorize a worker or Lean."""
    if (not isinstance(work, dict) or not isinstance(work.get('work_id'), str) or not work['work_id']
            or not isinstance(work.get('consumers'), list) or not work['consumers']
            or not isinstance(work.get('expected_contribution'), str) or not work['expected_contribution'].strip()):
        raise ValueError('auxiliary work requires identity, exact consumers and expected contribution')
    for consumer in work['consumers']:
        if (not isinstance(consumer, dict) or consumer.get('domain') not in DOMAINS
                or not isinstance(consumer.get('id'), str) or not consumer['id']):
            raise ValueError('auxiliary consumer needs deficit domain and stable finding/row/clause ID')
    if 'new_value' in work and (not isinstance(work['new_value'], str) or not work['new_value'].strip()):
        raise ValueError('auxiliary new value must explain actual uncertainty reduction')
    return copy.deepcopy(work)


def certification_retriage(modules):
    """Exact module failures trigger reassessment; cost never deletes an obligation."""
    latest = {}
    for module in modules:
        latest[module['lineage_id']] = module
    reasons = {'encoding_infeasible', 'scope_expansion', 'no_uncertainty_reduction', 'returned_to_main'}
    return [{'module_id': m['module_id'], 'module_evidence_sha256': digest(m),
             'row_id': m.get('row_id'), 'reason': m.get('exit_reason', m.get('outcome', m.get('state'))),
             'required_action': 'independent_cost_feasibility_retriage', 'obligation_waived': False}
            for m in latest.values() if m.get('state') in ('returned_to_main', 'awaiting_retriage')
            or m.get('outcome') in reasons]


def module_consumers(candidate, modules):
    """Derive exact ledger consumers, preserving missing/retired claim diagnostics."""
    rows = candidate['ledger']['rows']
    result = []
    for module in modules:
        row_id = module.get('row_id')
        consumers = [row['id'] for row in rows if row_id in row.get('uses', [])]
        result.append({'work_id': module['module_id'], 'module_evidence_sha256': digest(module),
            'consumers': [{'domain': 'certification', 'id': row_id or module['module_id']}],
            'ledger_consumers': consumers, 'claim_present': any(r.get('id') == row_id for r in rows),
            'expected_contribution': module.get('brief') or 'Independently selected local claim verification',
            **({'new_value': module['reentry_disposition']['new_value']}
               if (module.get('reentry_disposition') or {}).get('new_value') else {})})
    return result


def compact_context(state, *, modules=()):
    """No recursive evidence packages; immutable artifacts remain in the store."""
    if not state:
        return {'instruction': GUIDANCE}
    current = state['candidates'][state['current_candidate_sha256']]
    return {'instruction': GUIDANCE, 'original_sha256': state['original_sha256'],
        'current_candidate_sha256': state['current_candidate_sha256'],
        'best_reviewed_original_candidate': state['best_reviewed_original_candidate'],
        'best_reviewed_mathematical_candidate': state.get('best_reviewed_mathematical_candidate'),
        'best_mathematical_scope_qualification': state['candidates'][state['best_reviewed_mathematical_candidate']]['scope_qualification']
            if state.get('best_reviewed_mathematical_candidate') else None,
        'current_scope_qualification': current['scope_qualification'],
        'phase': state.get('phase'),
        'deficits': {k: {'status': v['status'], 'count': len(v['items']),
                         'evidence_sha256': v['evidence_sha256']} for k, v in current['deficits'].items()},
        'next_eligible_action': ('complete_required_evidence_delivery' if current['deficits']['delivery']['status'] == 'open' else
            'address_mathematical_findings' if current['deficits']['mathematical']['status'] == 'open' else
            'resolve_selected_certification_obligations' if current['deficits']['certification']['status'] == 'open' else
            'obtain_required_independent_scope_and_final_verification'),
        'triggers': state.get('triggers', []), 'certificate_retriage': certification_retriage(modules),
        'archive': {'candidate_count': len(state['candidates']), 'research_count': len(state['research_archive']),
                    'auxiliary_count': len(state['auxiliary_archive'])},
        'authority': 'scheduling_only_no_grade_acceptance_or_dispatch'}


def work_admission(state, *, kind, consumer_ids=(), reason=''):
    """Default generic scheduling gate, independent of provider, mode and deadlines.

    Existing mathematical/task authorizations still apply after this gate permits
    a task. IDs and reason establish necessity, not mathematical correctness.
    """
    phase = state.get('phase', {'name': 'exploring', 'consumer_ids': []})
    consumers = set(consumer_ids)
    necessary = kind in ('gap_closure', 'scope', 'validation', 'writeup')
    mapped = bool(consumers) and consumers.issubset(set(phase.get('consumer_ids', []))) and bool(reason.strip())
    allowed = phase['name'] != 'converging' or necessary or mapped
    return {'allowed': allowed, 'phase': phase['name'], 'kind': kind,
        'consumer_ids': sorted(consumers), 'reason': reason,
        'basis': 'necessary_candidate_work' if necessary else 'mapped_current_obstruction' if mapped
                 else 'exploration_open' if allowed else 'nonessential_parallel_exploration_paused',
        'authority': 'scheduling_only_existing_approvals_still_required'}


def scout_admission(state, tasks, *, user_requested=False):
    decisions = [({'allowed': True, 'phase': state.get('phase', {}).get('name', 'exploring'),
        'kind': 'route_exploration', 'consumer_ids': t.get('obstruction_ids', []),
        'reason': t.get('context', ''), 'basis': 'user_requested_advisory_exploration',
        'authority': 'scheduling_only_existing_approvals_still_required'}
        if user_requested is True and t.get('purpose') == 'scientific_alternative' else work_admission(state, kind='route_exploration',
        consumer_ids=t.get('obstruction_ids', []), reason=t.get('context', ''))) for t in tasks]
    return {'allowed': all(d['allowed'] for d in decisions), 'decisions': decisions,
            'phase': state.get('phase', {}).get('name', 'exploring')}


class ConvergenceStore:
    """Atomic current index and content-addressed immutable full state snapshots.

    Store is main-owned, like the plan. Never follow model-supplied paths.
    """
    def __init__(self, folder):
        self.folder = Path(folder)
        self.path = self.folder / 'research-convergence.json'
        self.archive = self.folder / 'convergence-archive'

    def load(self):
        if not self.path.exists():
            return {}
        pointer = json.loads(self.path.read_text())
        ref = pointer.get('state_sha256')
        if not _hash(ref):
            raise ValueError('invalid convergence archive reference')
        value = json.loads((self.archive / (ref + '.json')).read_text())
        if value.get('storage_format') == 'individual_records_v1':
            value = value['state']
            for table in ('candidates', 'observations', 'research_archive', 'auxiliary_archive'):
                value[table] = {key: self._load_record(item['record_sha256']) for key, item in value[table].items()}
            for candidate in value['candidates'].values():
                body = candidate['candidate']
                if isinstance(body, dict) and set(body) == {'body_record_sha256'}:
                    candidate['candidate'] = self._load_record(body['body_record_sha256'])
        if digest(value) != ref:
            raise ValueError('convergence archive changed')
        return value

    def _load_record(self, ref):
        if not _hash(ref):
            raise ValueError('invalid convergence record reference')
        value = json.loads((self.archive / 'records' / (ref + '.json')).read_text())
        if digest(value) != ref:
            raise ValueError('convergence record changed')
        return value

    @staticmethod
    def _immutable(path, value):
        data = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
        try:
            with path.open('x', encoding='utf-8') as stream:
                stream.write(data)
        except FileExistsError:
            if path.read_text() != data:
                raise ValueError('immutable convergence archive collision')

    def save(self, state):
        self.archive.mkdir(parents=True, exist_ok=True)
        (self.archive / 'records').mkdir(exist_ok=True)
        ref = digest(state)
        path = self.archive / (ref + '.json')
        manifest = dict(state)
        for table in ('candidates', 'observations', 'research_archive', 'auxiliary_archive'):
            manifest[table] = {}
            for key, value in state[table].items():
                if table == 'candidates':
                    body_ref = digest(value['candidate'])
                    self._immutable(self.archive / 'records' / (body_ref + '.json'), value['candidate'])
                    value = {**value, 'candidate': {'body_record_sha256': body_ref}}
                item_ref = digest(value)
                self._immutable(self.archive / 'records' / (item_ref + '.json'), value)
                manifest[table][key] = {'record_sha256': item_ref}
        self._immutable(path, {'storage_format': 'individual_records_v1', 'state': manifest})
        temporary = self.path.with_suffix('.tmp')
        temporary.write_text(json.dumps({'schema_version': 1, 'state_sha256': ref}) + '\n')
        os.replace(temporary, self.path)
        return {'path': str(path.relative_to(self.folder)), 'sha256': ref}
