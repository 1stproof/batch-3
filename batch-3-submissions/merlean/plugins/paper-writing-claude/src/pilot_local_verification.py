"""Lite local verification bookkeeping, not proof or grade authority.

Readable main-owned briefs remain ordinary task context. This module binds a small
operational project to current independent approval and retains every generation.
"""
import copy
import hashlib
import json

class ModuleBoundary(RuntimeError):
    pass

VERSION = 1
OUTCOMES = {'local_evidence', 'mathematical_counterissue', 'encoding_infeasible',
            'scope_expansion', 'no_uncertainty_reduction', 'returned_to_main', 'compile_pending'}
STOPPED = {'returned_to_main', 'awaiting_retriage'}


def digest(value):
    return hashlib.sha256((json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode()).hexdigest()


def claim_basis(candidate, row_id):
    rows = candidate['ledger']['rows']
    matches = [r for r in rows if r.get('id') == row_id]
    if len(matches) != 1:
        raise ValueError('local module requires one exact current ledger claim')
    row = matches[0]
    claim = {k:v for k,v in row.items() if k not in {'id','status','closed','triaged','evidence'}}
    by_id={r['id']:r for r in rows}; closure={}; pending=list(row.get('uses',[]))
    while pending:
        ident=pending.pop()
        if ident in closure: continue
        dependency=by_id.get(ident)
        closure[ident]=({k:v for k,v in dependency.items() if k not in {'status','closed','triaged'}} if dependency else {'external_reference':ident})
        if dependency: pending.extend(dependency.get('uses',[]))
    premises = {'hypotheses':candidate.get('hypotheses'), 'assumptions':candidate.get('assumptions'),
                'assumption_census':candidate.get('assumption_census'),
                'dependency_closure':closure, 'dossier_premises':candidate.get('premises')}
    return digest(claim), digest(premises)


def proposal(task, candidate):
    rows = task.get('row_ids')
    brief = task.get('local_module')
    if (not isinstance(rows,list) or len(rows)!=1 or not isinstance(rows[0],str)
            or not isinstance(brief,dict) or set(brief)!={'brief','max_worker_calls','max_probe_runs'}
            or not isinstance(brief['brief'],str) or not brief['brief'].strip()
            or any(type(brief[k]) is not int or brief[k]<1 for k in ('max_worker_calls','max_probe_runs'))):
        raise ValueError('local Lean task needs one row and a readable local_module brief with positive per-module worker/probe bounds')
    claim, premises = claim_basis(candidate, rows[0])
    return {'row_id':rows[0], 'claim_sha256':claim, 'premises_sha256':premises,
            'brief':brief['brief'], 'limits':{k:brief[k] for k in ('max_worker_calls','max_probe_runs')},
            'owned_scope':task.get('owned_scope'), 'task_sha256':digest(task)}


def latest_modules(modules):
    latest = {}
    for module in modules:
        latest[module['lineage_id']] = module
    return list(latest.values())


def check_review(candidate, review, modules):
    """Validate operational dispositions; existing finding/grade gates stay separate."""
    for decision in review['triage_decisions']:
        if decision['selected'] and (decision.get('verification_uncertainty')!='high'
                or not isinstance(decision.get('local_check_reason'),str)
                or not decision['local_check_reason'].strip()):
            raise ValueError('Lite selection requires high material local verification uncertainty and an independent reason')
        if decision['selected']:
            value = decision.get('local_check')
            if not isinstance(value, dict) or any(not isinstance(value.get(k), str) or not value[k].strip()
                    for k in ('uncertainty', 'intended_objects', 'premise_boundary', 'feasibility', 'expected_value')):
                raise ValueError('selected local check requires exact uncertainty, intended objects, noncircular premise boundary, feasibility/cost and expected value')
    supplied = review.get('local_module_reassessments', [])
    if not isinstance(supplied,list) or any(not isinstance(d,dict) or not isinstance(d.get('module_id'),str) for d in supplied):
        raise ValueError('local module reassessments must be an array')
    by_id = {d.get('module_id'):d for d in supplied}
    current = latest_modules(modules)
    if len(by_id)!=len(supplied) or set(by_id)!={m['module_id'] for m in current}:
        raise ValueError('current independent review must account for each latest local module exactly once')
    decisions={d['row_id']:d for d in review['triage_decisions']}
    for module in current:
        d = by_id[module['module_id']]
        if (d.get('module_evidence_sha256')!=digest(module)
                or not isinstance(d.get('action'),str)
                or d.get('action') not in {'still_required','no_longer_required','replace','continue_local'}
                or not isinstance(d.get('reason'),str) or not d['reason'].strip()
                or not isinstance(d.get('evidence'),str) or not d['evidence'].strip()):
            raise ValueError('module retriage requires exact current evidence and substantive independent disposition')
        if d['action']=='no_longer_required' and (not isinstance(d.get('basis'),str) or d.get('basis') not in {'current_argument','audited_input','replacement_evidence'}):
            raise ValueError('encoding cost alone cannot remove a verification obligation')
        row_id=d.get('current_row_id')
        if row_id is not None and not isinstance(row_id,str):
            raise ValueError('module current row must be string or null')
        if row_id is not None and row_id not in decisions:
            raise ValueError('module reassessment maps to an absent current claim')
        if row_id is None and module['row_id'] in decisions:
            raise ValueError('surviving prior claim needs an explicit current-row disposition')
        if row_id is None and d['action']!='no_longer_required':
            raise ValueError('retired claim requires explicit no-longer-required evidence')
        if row_id is not None:
            selected=decisions[row_id]['selected']
            if (d['action']=='no_longer_required' and selected) or (d['action'] in {'still_required','replace','continue_local'} and not selected):
                raise ValueError('module obligation disposition contradicts current independent selection')
        if d['action'] in {'replace','continue_local'} and (not isinstance(d.get('new_value'),str) or not d['new_value'].strip()):
            raise ValueError('module reentry must explain the new uncertainty-reduction value')
    links=review.get('local_module_task_links',[])
    approved=review.get('approved_lean_tasks',[])
    inline=review.get('approved_inline_lean',False)
    if not isinstance(approved,list) or any(type(i) is not int or i<0 for i in approved) or type(inline) is not bool:
        raise ValueError('local task approvals require integer indices and boolean inline approval')
    indices=approved+(['inline'] if inline else [])
    if (not isinstance(links,list) or any(not isinstance(link,dict)
            or not ((type(link.get('task_index')) is int and link['task_index']>=0)
                    or (type(link.get('task_index')) is str and link['task_index']=='inline')) for link in links)
            or len(links)!=len(indices) or {link.get('task_index') for link in links}!=set(indices)):
        raise ValueError('each approved local task requires an explicit independent lineage link')
    known={m['module_id']:m for m in current}
    for link in links:
        parent=link.get('prior_module_id')
        if parent is not None and (not isinstance(parent,str) or parent not in known):
            raise ValueError('local task prior_module_id must be JSON null for a first registered lineage '
                'or one of the exact current module IDs=' + json.dumps(list(known), ensure_ascii=False)
                + '; historical probe paths and worker/stage labels are provenance, not registered module IDs')
        if not isinstance(link.get('reason'),str) or not link['reason'].strip():
            raise ValueError('local task lineage requires a nonempty independent reason preserving relevant historical evidence')
        if link.get('relation') != ('new_claim' if parent is None else 'same_claim'):
            raise ValueError('local task lineage relation is inconsistent')
        index=link['task_index']
        tasks=candidate.get('sol_tasks',[])
        if index!='inline' and index>=len(tasks):
            raise ValueError('local task lineage index absent from candidate')
        task_rows=candidate.get('lean_probe_rows') if index=='inline' else tasks[index].get('row_ids')
        if not isinstance(task_rows,list) or len(task_rows)!=1:
            raise ValueError('local lineage link requires one exact task row')
        if parent is not None and by_id[parent].get('current_row_id')!=task_rows[0]:
            raise ValueError('module retriage row differs from the approved task row')
        if parent is not None and by_id[parent]['action'] not in {'replace','continue_local'}:
            raise ValueError('prior module must be independently approved for reentry')
    return copy.deepcopy(supplied)


def lineage_counters(modules, prior):
    """Account legacy reset segments and inherited totals without rewriting history."""
    totals = {'worker_calls':0, 'probe_runs':0}
    seen = {}
    for record in modules:
        if record['lineage_id'] != prior['lineage_id']:
            continue
        parent_id = record.get('inherited_counters_from')
        for key in totals:
            value = record.get(key)
            if type(value) is not int or value < 0:
                raise ValueError('local lineage contains invalid consumed counters')
            if record.get('counter_semantics') == 'lineage_total':
                if value < totals[key]:
                    raise ValueError('local cumulative lineage counter regressed')
                totals[key] = value
            elif parent_id is not None:
                parent = seen.get(parent_id)
                if parent is None or value < parent[key]:
                    raise ValueError('legacy inherited local counters cannot be reconciled')
                totals[key] += value - parent[key]
            else:
                # Old replacement generations started counters at zero. Add their
                # consumed work, not their limits; their records stay untouched.
                totals[key] += value
        seen[record['module_id']] = record
        if record['module_id'] == prior['module_id']:
            return totals
    raise ValueError('local lineage prior is absent')


def admit(modules, candidate, task, candidate_binding, approval):
    plan = proposal(task,candidate)
    link=approval.get('local_module_links',{}).get(plan['task_sha256'])
    if link is None:
        return None,'local task has no current independent lineage association'
    matches = [m for m in latest_modules(modules) if m['row_id']==plan['row_id']
               or (m['claim_sha256']==plan['claim_sha256'] and m['premises_sha256']==plan['premises_sha256'])]
    if len(matches)>1:
        return None, 'ambiguous claim lineage requires original-main reconciliation'
    parent=link.get('prior_module_id')
    prior=next((m for m in latest_modules(modules) if m['module_id']==parent),None) if parent else None
    if parent and prior is None: return None,'local task references a missing prior module'
    if matches and prior is None: return None,'known claim cannot be renamed as a new module'
    if matches and prior not in matches: return None,'local claim lineage conflicts with prior matching identity'
    continuing = False
    if prior:
        # Exact already-admitted project keeps counters; never mint a new budget.
        if (prior['task_sha256']==plan['task_sha256'] and prior['candidate_binding']==candidate_binding
                and prior['state']=='working'
                and prior.get('approval_receipt') == approval.get('receipt')
                and lineage_counters(modules, prior) == {k:prior[k] for k in ('worker_calls','probe_runs')}):
            return prior, None
        decision = next((d for d in approval.get('local_module_reassessments',[])
                         if d['module_id']==prior['module_id']),None)
        if (not decision or decision.get('module_evidence_sha256')!=digest(prior)
                or decision.get('action') not in {'replace','continue_local'}):
            return None, 'stopped or changed local module needs exact current independent retriage before reentry'
        old_plan = {k:prior[k] for k in ('claim_sha256','premises_sha256','brief','owned_scope')}
        new_plan = {k:plan[k] for k in old_plan}
        if old_plan==new_plan:
            reports=[r['output'].get('local_module_result') for r in prior['returns'] if isinstance(r.get('output'),dict)]
            progress=any(isinstance(r,dict) and r.get('outcome')=='local_evidence' and r.get('scope_respected') is True
                         and r.get('uncertainty_reduced') is True for r in reports)
            # Inline probes have no worker self-report. Actual retained diagnostics
            # plus this fresh independent evidence/new-value disposition may justify
            # using the remaining original allowance; compilation alone grants nothing.
            inline_evidence=('lean_probe' in task and prior['worker_calls']==0
                             and prior['probe_runs']>0
                             and any('inline_or_worker_probe' in r for r in prior['returns']))
            continuing=(decision['action']=='continue_local' and (progress or inline_evidence) and plan['limits']==prior['limits']
                        and prior['worker_calls']<prior['limits']['max_worker_calls']
                        and prior['probe_runs']<prior['limits']['max_probe_runs'])
            if not continuing:
                return None, 'new label, task hash or budget alone cannot reopen identical local work'
    counters = lineage_counters(modules, prior) if prior else {'worker_calls':0, 'probe_runs':0}
    lineage = prior['lineage_id'] if prior else 'claim-'+digest({'row':plan['row_id'],'claim':plan['claim_sha256']})[:24]
    generation = prior['generation']+1 if prior else 1
    module_id = lineage+'-g'+str(generation)
    record = {**plan,'module_id':module_id,'lineage_id':lineage,'generation':generation,
              'parent_module_id':prior['module_id'] if prior else None,
              'candidate_binding':candidate_binding,'approval_receipt':copy.deepcopy(approval['receipt']),
              'reentry_disposition':copy.deepcopy(decision) if prior else None,
              'state':'working', 'counter_semantics':'lineage_total', **counters,
              'inherited_counters_from':prior['module_id'] if prior else None,'stages':[],'returns':[],
              'submitted_source_sha256':copy.deepcopy(prior.get('submitted_source_sha256', [])) if prior else [],
              'artifact_root':'local-verification/'+module_id,
              'verification_status':'unresolved; independent scientific review required'}
    modules.append(record)
    return record,None


def consume(module, kind):
    counter, limit = ('worker_calls','max_worker_calls') if kind=='worker' else ('probe_runs','max_probe_runs')
    if module['state']!='working' or module[counter]>=module['limits'][limit]:
        module['state']='returned_to_main'
        module['exit_reason']='agreed local resource boundary reached; mathematical obligation unchanged'
        return False
    module[counter]+=1
    return True


def compile_pending_diagnostics(output):
    """Describe shape errors only; never repair output or grant execution authority."""
    report = output.get('local_module_result') if isinstance(output, dict) else None
    if not isinstance(report, dict) or report.get('outcome') != 'compile_pending':
        return []
    errors = []
    for field in ('implementation_complete', 'next_step'):
        path = 'local_module_result.' + field
        if field not in report:
            suffix = '; root-level ' + field + ' does not satisfy this nested field' if field in output else ''
            errors.append(path + ' is required' + suffix)
        elif field == 'implementation_complete' and type(report[field]) is not bool:
            errors.append(path + ' must be a boolean')
        elif field == 'next_step' and (not isinstance(report[field], str) or not report[field].strip()):
            errors.append(path + ' must be a nonempty string')
    if not isinstance(output.get('lean_probe'), str) or not output['lean_probe'].strip():
        errors.append('root lean_probe must be a nonempty source string')
    return errors


def worker_return(module, output, receipt):
    """Retain the complete answer; worker labels never certify a mathematical claim."""
    report = output.get('local_module_result') if isinstance(output,dict) else None
    valid = (isinstance(report,dict) and report.get('module_id')==module['module_id']
             and isinstance(report.get('outcome'),str) and report.get('outcome') in OUTCOMES and type(report.get('scope_respected')) is bool
             and type(report.get('uncertainty_reduced')) is bool
             and isinstance(report.get('evidence'),str) and bool(report['evidence'].strip()))
    returned = {'output':copy.deepcopy(output),'receipt':copy.deepcopy(receipt)}
    diagnostics = compile_pending_diagnostics(output)
    if diagnostics:
        returned['contract_diagnostics'] = diagnostics
    module['returns'].append(returned)
    stage={k:receipt.get(k) for k in ('name','request_id','session_id','status')}
    existing=next((item for item in module['stages'] if item.get('name')==stage['name']),None)
    if existing is None: module['stages'].append(stage)
    else: existing.update(stage)
    stage['usage']='unknown until exact response-ID ledger join'
    pending = (valid and report['outcome']=='compile_pending'
               and report['scope_respected'] is True
               and type(report.get('implementation_complete')) is bool
               and isinstance(report.get('next_step'), str) and bool(report['next_step'].strip())
               and isinstance(output.get('lean_probe'), str) and bool(output['lean_probe'].strip())
               and output.get('lean_probe_rows') == [module['row_id']]
               and not output.get('python_probe'))
    # A compiler diagnostic can precede uncertainty reduction. Historical terminal
    # reports retain their meaning; only this explicit prospective protocol opts in.
    permitted = (module['state']=='working' and valid and report['scope_respected']
                 and ((report['outcome']=='local_evidence' and report['uncertainty_reduced']) or pending))
    if permitted and (output.get('python_probe') or (output.get('lean_probe') and output.get('lean_probe_rows') != [module['row_id']])):
        permitted = False
    if permitted and pending:
        if digest(output['lean_probe']) in module.get('submitted_source_sha256', []):
            permitted = False
    if not permitted:
        module['state']='returned_to_main'
        module['exit_reason']=report.get('outcome') if valid else 'malformed module return; no code executed'
    return bool(permitted)


def execution_binding(module, candidate, task, candidate_binding, approval, *, modules):
    """Immutable operational boundary, not a mathematical equivalence judgment."""
    try:
        plan = proposal(task, candidate)
    except (ValueError, KeyError, TypeError) as error:
        raise ModuleBoundary('local task or candidate boundary is malformed; reassessment required') from error
    if lineage_counters(modules, module) != {k:module[k] for k in ('worker_calls','probe_runs')}:
        raise ModuleBoundary('legacy local counters need independent accounting reassessment')
    if not isinstance(approval, dict):
        raise ModuleBoundary('local independent approval is absent')
    if (any(module.get(k) != plan.get(k) for k in plan)
            or module.get('candidate_binding') != candidate_binding
            or approval.get('candidate_binding') != candidate_binding
            or module['task_sha256'] not in approval.get('approved_lean_task_hashes', [])
            or module['task_sha256'] not in approval.get('local_module_links', {})
            or module['row_id'] not in approval.get('selected_rows', [])
            or module.get('approval_receipt') != approval.get('receipt')):
        raise ModuleBoundary('local task, claim, premises, scope, budget, candidate or approval changed; reassessment required')
    return digest({'plan':plan, 'candidate_binding':candidate_binding,
                   'approval':approval, 'module_id':module['module_id']})


def continue_after_probe(module, output, probe):
    """Continue only a requested unchanged implementation with real diagnostics."""
    report = output.get('local_module_result', {})
    lean = probe.get('lean', {})
    repeat = (module['state']=='working' and report.get('outcome')=='compile_pending'
              and lean.get('status') in {'completed', 'failed'}
              and type(lean.get('exit_code')) is int
              and (lean['exit_code'] != 0 or report.get('implementation_complete') is False))
    if repeat and (module['worker_calls'] >= module['limits']['max_worker_calls']
                   or module['probe_runs'] >= module['limits']['max_probe_runs']):
        repeat = False
        reason = 'agreed local resource boundary reached; mathematical obligation unchanged'
    else:
        reason = 'local implementation returned; independent scientific acceptance or reassessment required'
    if not repeat:
        module['state'] = 'returned_to_main'
        module.setdefault('exit_reason', reason)
    return repeat


COMPILE_PENDING_EXAMPLE = {
    'local_module_result': {'module_id': '<approved module_id>', 'outcome': 'compile_pending',
        'scope_respected': True, 'uncertainty_reduced': False,
        'evidence': '<actual implementation status; no invented compiler result>',
        'implementation_complete': False, 'next_step': '<remaining implementation or diagnostic check>'},
    'lean_probe': '<exact source>', 'lean_probe_rows': ['<exact approved row_id>'], 'python_probe': ''}

WORKER_GUIDANCE = """Return local_module_result {module_id,outcome:compile_pending|local_evidence|mathematical_counterissue|encoding_infeasible|scope_expansion|no_uncertainty_reduction|returned_to_main,scope_respected:boolean,uncertainty_reduced:boolean,evidence:string}. For compile_pending, local_module_result MUST ALSO contain implementation_complete:boolean and next_step:nonempty string. Both fields belong INSIDE local_module_result; root-level fields do not satisfy them. Keep lean_probe (exact source), lean_probe_rows (exactly the approved row), and empty python_probe at the ROOT. This explicitly requests bounded compile/repair within the unchanged approved module, not mathematical acceptance. It does not require claiming uncertainty reduction before any compiler ran. Set nested implementation_complete:true only for source covering the entire requested certificate. A failed compilation may be repaired; a compiled incomplete implementation may be completed within the same scope. The host preserves every attempt and original total budgets. Do not return Python code in this Lean module. Any material mathematical counterissue, scope/premise/goal change, infeasible encoding or no-value diagnosis must use its terminal outcome, not compile_pending. No label grants certification.
Shape example only; replace every placeholder with the actual approved binding and source:
""" + json.dumps(COMPILE_PENDING_EXAMPLE, ensure_ascii=False, indent=2)

MAIN_GUIDANCE = """Lite local verification remains optional. Develop the natural-language argument first. For an exceptionally uncertain existing local inference, keep the normal readable Sol handoff and add local_module:{brief,max_worker_calls,max_probe_runs}, with one row_ids entry. The brief states the local question, accepted explicit premises, narrow scope/non-goals, expected uncertainty reduction and proportionate cost; hints remain advisory. Bounds are main-proposed per-module operational limits, not a global quota. Inline Lean uses lean_probe_module with the same shape and one lean_probe_rows entry. Accepted standard inputs may remain explicit hypotheses with exact applicability; do not build their foundations. Scope expansion, infeasible encoding or repeated work without new value returns full evidence to you. Continue the original research in natural language or propose a justified retarget; operational exit never closes mathematics. Old module obligations remain until existing independent review accounts for them. Zero Lean modules is legitimate when no high-uncertainty local inference needs one; final proof/scope/grade requirements remain unchanged."""

REVIEW_GUIDANCE = """LOCAL MODULE CONTRACT: Every selected current triage_decision additionally needs local_check:{uncertainty,intended_objects,premise_boundary,feasibility,expected_value}, each a substantive string: identify the exact remaining doubt and existing evidence, actual objects and use-site mapping, noncircular accepted premise boundary, bounded encoding feasibility and cost, and what new evidence Lean adds beyond NL review. Novelty or importance alone is insufficient. Zero new Lean checks is valid when individually justified; existing obligations cannot be automatically dropped. Also supply verification_uncertainty:"high" and local_check_reason explaining material local uncertainty and the value/cost of the proposed check. No selection merely to certify an accepted input's foundations. Account every latest supplied module exactly once in local_module_reassessments: {module_id,module_evidence_sha256,action:still_required|no_longer_required|replace|continue_local,current_row_id,reason,evidence}. Copy the exact digest from host_local_module_evidence_sha256; it binds the full supplied module, never mathematical validity. current_row_id maps the prior obligation to the current exact ledger row; null only for a genuinely retired claim. Selection and action must agree. no_longer_required additionally needs basis:current_argument|audited_input|replacement_evidence; cost alone never removes an obligation. Replacement/continuation needs new_value explaining substantively new uncertainty reduction. Retain and disposition all old findings through the existing finding census. For every approved_lean_tasks index (and "inline" when approved_inline_lean:true), supply local_module_task_links:{task_index,prior_module_id,relation:new_claim|same_claim,reason} as an array. Explicitly link renamed/rephrased prior work to its existing lineage; a new claim must be independently justified. Changing labels, budgets or wording is not progress. No bookkeeping label, exit or successful compile grants mathematical authority. Reuse this review; no separate reviewer is required for a bookkeeping event."""


def review_guidance(modules):
    """Expose the validator's exact current namespace without granting task approval."""
    current_ids = [module['module_id'] for module in latest_modules(modules)]
    return (REVIEW_GUIDANCE + '\nCURRENT REGISTERED LOCAL MODULE IDS '
            '(closed allowed non-null prior_module_id census):\n'
            + json.dumps(current_ids, ensure_ascii=False) + '\n'
            'For local_module_task_links, prior_module_id is either JSON null (not the string "null") '
            'or an exact ID in this census. Use relation:"same_claim" only with a listed prior module '
            'and its independently justified replace/continue_local disposition. Use '
            'prior_module_id:null, relation:"new_claim" for the first registered local-module lineage '
            'when independently justified; new_claim denotes registry bookkeeping, not mathematical novelty '
            'or absence of historical work. Historical probe paths, task names, worker/stage labels and '
            'older module generations are not aliases for current registered IDs. Preserve and independently '
            'assess all relevant legacy work in reason/evidence; registration does not authorize repeating it '
            'or reset any known module budget. If this census is empty, local_module_reassessments must be [] '
            'and every approved task link must use JSON null; you may decline approval if the historical '
            'relationship or new value is unresolved. An empty registry does not imply a new scientific claim '
            'or require a Lean task. Field-shape example only, never approval or evidence: '
            '{"task_index":0,"prior_module_id":null,"relation":"new_claim","reason":"<independent reason addressing prior work>"}. '
            'Every existing row-selection, task-approval, proposal, admission and acceptance gate still applies.\n')
