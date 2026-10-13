"""Bounded main-selected advisory route portfolios; never acceptance authority."""
import hashlib
import json

DEFAULT = {'enabled': False, 'width': 2, 'user_requested': False}

def fresh_config():
    """New campaigns allow main-selected portfolios; saved/missing configs stay legacy."""
    return {'enabled': True, 'width': 4, 'user_requested': True}

def validate_config(value=None):
    value = dict(DEFAULT) if value is None else value
    if (not isinstance(value, dict) or set(value) != set(DEFAULT)
            or type(value['enabled']) is not bool or type(value['user_requested']) is not bool
            or type(value['width']) is not int or value['width'] not in (2, 3, 4)):
        raise ValueError('parallel_route_scouts requires enabled:boolean,width:2..4,user_requested:boolean')
    return dict(value)

def validate_tasks(tasks):
    if not isinstance(tasks, list) or len(tasks) not in (0, 2, 3, 4):
        raise ValueError('route portfolio requires zero or two to four distinct main-owned tasks')
    keys = {'angle', 'task', 'context', 'purpose', 'target_row_ids', 'obstruction_ids'}
    for task in tasks:
        if (not isinstance(task, dict) or set(task) != keys
                or any(not isinstance(task[k], str) or not task[k].strip() for k in ('angle','task','context'))
                or task['purpose'] not in ('scientific_alternative','certificate_strategy')
                or any(not isinstance(task[k], list) or any(not isinstance(v,str) or not v for v in task[k])
                       for k in ('target_row_ids','obstruction_ids'))
                or not task['target_row_ids']):
            raise ValueError('route tasks need exact scientific purpose, complete context, target rows and obstruction IDs')
    if (len({t['angle'].strip().casefold() for t in tasks}) != len(tasks)
            or len({t['task'].strip() for t in tasks}) != len(tasks)):
        raise ValueError('parallel route tasks must explore distinct main-selected angles')
    return tasks

def eligible_obstructions(tasks, candidate, current_review, *, user_requested=False):
    """Independent findings/selection, or explicitly requested advisory scientific alternatives."""
    rows = {r['id']: r for r in candidate['ledger']['rows'] if isinstance(r,dict) and isinstance(r.get('id'),str)}
    findings = {f['id']: f for f in current_review.get('unresolved_findings', [])
                if isinstance(f,dict) and isinstance(f.get('id'),str) and f.get('severity') in ('fatal','gap')
                and f.get('kind') == 'mathematical'
                and ('host_advisory_only_finding_ids' not in current_review
                     or f['id'] in current_review['host_advisory_only_finding_ids'])}
    selected = set(current_review.get('triaged_rows', []))
    chosen = {}
    for task in tasks:
        if any(row not in rows for row in task['target_row_ids']):
            raise ValueError('route proposal targets an absent current ledger row')
        matched = [findings[i] for i in task['obstruction_ids'] if i in findings]
        cert_rows = [r for r in task['target_row_ids'] if r in selected]
        requested = user_requested is True and task['purpose'] == 'scientific_alternative'
        if not matched and not cert_rows and not requested:
            raise ValueError('route proposal lacks current independent scientific obstruction; administrative failures do not qualify')
        if task['obstruction_ids'] and len(matched) != len(task['obstruction_ids']):
            # Certificate trigger comes from independent selected rows, not arbitrary legacy gate findings.
            raise ValueError('route obstruction IDs must identify current mathematical findings')
        if requested and not matched and not cert_rows:
            chosen['user_requested_advisory_exploration'] = True
            # Task selectors and rewording cannot purchase another user-only portfolio.
            for row_id, row_value in rows.items():
                chosen['row:' + row_id] = row_value
        for row in task['target_row_ids']:
            chosen['row:' + row] = rows[row]
        for finding in matched:
            chosen['finding:' + finding['id']] = finding
    return chosen

def census_key(candidate_key, obstructions):
    return hashlib.sha256(json.dumps({'candidate_and_execution':candidate_key,'obstructions':obstructions},
        ensure_ascii=False, sort_keys=True, separators=(',',':')).encode()).hexdigest()
