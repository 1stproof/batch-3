"""Deterministic campaign bookkeeping; never launches model jobs. Evidence audits may run Lean/TeX."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import secrets
import hmac
import os
from pathlib import Path
import re
import uuid

from original_scope import audit_original_scope


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def now():
    return datetime.now(timezone.utc)


def deadline(value):
    if not isinstance(value, str):
        raise ValueError('finite deadline must be a timezone-qualified string')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('deadline must include a timezone')
    return result


def read_json(path):
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ValueError('expected JSON object: ' + str(path))
    return value


def atomic(path, data):
    temporary = path.with_suffix('.next')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def pinned(ref, base):
    if not isinstance(ref, dict):
        raise ValueError('missing pinned evidence')
    path = (base / ref['path']).resolve()
    path.relative_to(base.resolve())
    payload = path.read_bytes()
    if digest(payload) != ref['sha256']:
        raise ValueError('stale evidence: ' + str(path))
    return path, payload


def identity(value):
    return ' '.join(value.casefold().split()) if isinstance(value, str) else ''


class Campaign:
    def __init__(self, root, *, owner_key=None):
        self.root = Path(root).resolve()
        self.owner_key = Path(owner_key).resolve() if owner_key is not None else None

    @classmethod
    def initialize(cls, root, problems, *, deadline_utc, concurrency, owner_key,
                   mode="lite", require_paper=False, max_pages=None):
        """Copy input once; deadline_utc=None explicitly selects no campaign time cap.

        Existing campaign roots cannot be reinitialized. Finite per-stage host
        timeouts remain required independently of this overall campaign policy.
        """
        if type(concurrency) is not int or concurrency < 1:
            raise ValueError('concurrency must be a positive integer')
        if deadline_utc is not None and deadline(deadline_utc) <= now():
            raise ValueError('deadline has already passed')
        if not isinstance(problems, dict) or not problems:
            raise ValueError('nonempty problem id to source path map required')
        inputs = {}
        for ident, source in problems.items():
            if not isinstance(ident, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', ident):
                raise ValueError('invalid problem id')
            inputs[ident] = Path(source).read_bytes()
        if mode not in {'lite', 'heavy'} or type(require_paper) is not bool:
            raise ValueError('mode must be lite/heavy and require_paper must be boolean')
        if max_pages is not None and (type(max_pages) is not int or max_pages < 1):
            raise ValueError('max_pages must be a positive integer')
        if owner_key is None:
            raise ValueError('controller owner key path required')
        campaign = cls(root, owner_key=owner_key)
        if campaign.owner_key.is_relative_to(campaign.root):
            raise ValueError('owner key must be outside the campaign tree')
        if campaign.root.exists():
            raise ValueError('campaign root already exists')
        secret = secrets.token_bytes(32)
        fd = os.open(campaign.owner_key, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'wb') as key_file:
            key_file.write(secret)
        campaign.root.mkdir(parents=True, exist_ok=False)
        registry = {'version': 2, 'owner_key_sha256': digest(secret), 'mode': mode,
                    'require_paper': require_paper, 'max_pages': max_pages, 'deadline_utc': deadline_utc, 'concurrency': concurrency, 'problems': {}}
        states = {}
        for ident, payload in inputs.items():
            folder = campaign.root / 'problems' / ident
            folder.mkdir(parents=True)
            (folder / 'input.txt').write_bytes(payload)
            registry['problems'][ident] = {'path': f'problems/{ident}/input.txt', 'sha256': digest(payload)}
            states[ident] = {'status': 'pending', 'observations': {}}
        atomic(campaign.root / 'registry.json', registry)
        atomic(campaign.root / 'state.json', {'registry_sha256': digest((campaign.root / 'registry.json').read_bytes()), 'sealed': False, 'problems': states, 'events': []})
        with campaign.transaction() as (registry, state):
            campaign._refresh(registry, state)
        return campaign

    @contextmanager
    def transaction(self, *, write=True):
        with (self.root / 'coordinator.lock').open('a' if write else 'r') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            state = read_json(self.root / 'state.json')
            registry_payload = (self.root / 'registry.json').read_bytes()
            if digest(registry_payload) != state['registry_sha256']:
                raise ValueError('frozen registry changed')
            registry = json.loads(registry_payload)
            if write:
                if self.owner_key is None or self.owner_key.is_relative_to(self.root):
                    raise ValueError('controller owner key outside campaign tree required')
                if not hmac.compare_digest(digest(self.owner_key.read_bytes()), registry.get('owner_key_sha256', '')):
                    raise ValueError('invalid controller owner key')
            for ref in registry['problems'].values():
                pinned(ref, self.root)
            yield registry, state
            if write:
                atomic(self.root / 'state.json', state)
                self._write_table(registry, state)

    def _write_table(self, registry, state):
        lines = ['# Campaign project table', '',
                 f"Problems: {len(registry['problems'])}",
                 f"Mode: {registry['mode']}",
                 f"Validated at: {state.get('validated_at', 'pending')}",
                 f"Successful completion: {state.get('successful_complete', False)}", '',
                 '| Problem | Lifecycle | Original solved | Silver review | Gold | Paper | Open feedback | Needs delivery |',
                 '| --- | --- | --- | --- | --- | --- | --- | --- |']
        for ident, cell in state['problems'].items():
            observations = cell.get('observations', {})
            columns = [observations.get(k, {}).get('status', 'pending')
                       for k in ('original', 'silver', 'gold', 'paper')]
            lines.append('| ' + ' | '.join([ident, cell['status'], *columns, str(sum(t['status'] == 'open' for t in cell.get('feedback', []))), str(sum(t.get('needs_delivery', False) for t in cell.get('feedback', [])))]) + ' |')
        lines += ['', 'Generated by the controller. Evidence details are in state.json.',
                  'Silver review_recorded records an independent review; it is not a kernel grade certificate.',
                  'This is a snapshot. Run refresh to revalidate current evidence.', '']
        temporary = self.root / 'project-table.next'
        temporary.write_text('\n'.join(lines))
        temporary.replace(self.root / 'project-table.md')

    def _ref(self, ident, path):
        folder = self.root / 'problems' / ident
        resolved = (folder / path).resolve()
        resolved.relative_to(folder)
        return {'path': str(resolved.relative_to(folder)), 'sha256': digest(resolved.read_bytes())}

    def observe(self, ident, *, manifest, paper_state=None):
        """Register evidence paths; callers cannot assign a completion or grade flag."""
        with self.transaction() as (registry, state):
            if state['sealed']:
                raise ValueError('campaign sealed')
            cell = state['problems'][ident]
            cell['research_manifest'] = self._ref(ident, manifest)
            if paper_state is not None:
                cell['paper_state'] = self._ref(ident, paper_state)
            self._refresh(registry, state)
            self.event(state, 'observe', ident)

    def _refresh(self, registry, state, *, record_feedback=True):
        from campaign_evidence import assess_evidence
        state['problem_count'] = len(registry['problems'])
        successful = True
        for ident, cell in state['problems'].items():
            previous = cell.get('observations', {})
            original = {'status': 'pending', 'details': []}
            if cell.get('manifest'):
                try:
                    result = self.validate_complete(ident, registry, cell['manifest'])
                    if result['sha256'] != cell['sha256']:
                        raise ValueError('completed manifest changed')
                    original = {'status': 'verified', 'details': [], 'evidence': result}
                except (ValueError, KeyError, TypeError, OSError, AttributeError, RecursionError) as error:
                    original = {'status': 'stale', 'details': [str(error)]}
            observations = {
                'silver': {'status': 'pending', 'details': []},
                'gold': {'status': 'pending' if registry['mode'] == 'heavy' else 'not_applicable', 'details': []},
                'paper': {'status': 'pending' if registry['require_paper'] else 'not_requested', 'details': []},
            }
            answer_bound = False
            if cell.get('research_manifest'):
                try:
                    folder = self.root / 'problems' / ident
                    manifest_path, _ = pinned(cell['research_manifest'], folder)
                    paper_path = pinned(cell['paper_state'], folder)[0] if cell.get('paper_state') else None
                    result = assess_evidence(manifest_path, mode=registry['mode'],
                                             paper_state=paper_path, max_pages=registry['max_pages'])
                    answer = result.get('answer') or {}
                    if original['status'] == 'verified':
                        original_manifest = read_json(folder / cell['manifest'])
                        expected_answer, _ = pinned(original_manifest['final_answer'], (folder / cell['manifest']).parent)
                        observed_answer = Path(answer.get('path', ''))
                        if not observed_answer.is_absolute():
                            observed_answer = manifest_path.parent / observed_answer
                        answer_bound = (answer.get('sha256') == cell['answer_sha256']
                                        and observed_answer.resolve() == expected_answer)
                    observations.update({k: result[k] for k in ('silver', 'gold', 'paper')})
                    for kind in observations:
                        if observations[kind]['status'] == 'failed' and previous.get(kind, {}).get('status') in {'verified', 'review_recorded', 'complete', 'stale'}:
                            observations[kind]['status'] = 'stale'
                except (ValueError, KeyError, TypeError, OSError, AttributeError, RecursionError) as error:
                    for kind in observations:
                        if observations[kind]['status'] not in {'not_applicable', 'not_requested'}:
                            observations[kind] = {'status': 'stale', 'details': [str(error)]}
            observations['original'] = original
            cell['observations'] = observations
            grade_ok = (observations['gold']['status'] == 'verified' if registry['mode'] == 'heavy'
                        else observations['silver']['status'] == 'review_recorded')
            cell['evidence_matches_original_answer'] = answer_bound
            goals = [original['status'] == 'verified', answer_bound, grade_ok]
            if registry['require_paper']:
                goals.append(observations['paper']['status'] == 'complete')
            cell['successful_complete'] = all(goals)
            if record_feedback:
                self._sync_feedback(state, ident, registry, previous)
            successful = successful and cell['successful_complete']
        state['successful_complete'] = successful
        state['validated_at'] = now().isoformat()

    def refresh(self):
        with self.transaction() as (registry, state):
            self._refresh(registry, state)
            return state

    def event(self, state, action, ident=None, **details):
        state['events'].append({'at': now().isoformat(), 'action': action, 'problem': ident, **details})

    def _ticket(self, state, ident, gate, errors, *, recipient="problem_main"):
        cell = state['problems'][ident]
        artifacts = {k: cell[k] for k in ('candidate', 'research_manifest', 'paper_state',
                     'manifest', 'sha256', 'answer_sha256', 'claim_token') if k in cell}
        fingerprint = digest(json.dumps([gate, errors, artifacts], sort_keys=True).encode())
        tickets = cell.setdefault('feedback', [])
        for ticket in tickets:
            if ticket['gate'] == gate and ticket['status'] == 'open':
                if ticket['fingerprint'] != fingerprint:
                    ticket.setdefault('history', []).append({k: ticket[k] for k in
                        ('fingerprint', 'errors', 'artifacts', 'updated_at', 'repair_round')})
                    ticket.update(fingerprint=fingerprint, errors=list(errors), artifacts=artifacts,
                                  updated_at=now().isoformat(), repair_round=cell.get('repair_round', 0), needs_delivery=True)
                return ticket
        ticket = {'id': uuid.uuid4().hex, 'gate': gate, 'recipient': recipient,
                  'status': 'open', 'needs_delivery': True, 'errors': list(errors), 'artifacts': artifacts,
                  'fingerprint': fingerprint, 'repair_round': cell.get('repair_round', 0),
                  'created_at': now().isoformat(), 'updated_at': now().isoformat(),
                  'action': ('Confirm the prior job stopped and reconcile its claim before resuming.'
                             if recipient == 'host' else
                             'Return these exact findings and artifacts to the persistent problem main; '
                             'repair within the frozen goal and obtain current independent review before resubmission.'),
                  'acknowledgments': [], 'history': []}
        tickets.append(ticket)
        return ticket

    def _resolve_feedback(self, cell, gate, evidence):
        for ticket in cell.get('feedback', []):
            if ticket['gate'] == gate and ticket['status'] == 'open':
                ticket.update(status='resolved', needs_delivery=False, resolved_at=now().isoformat(), resolution=evidence)

    def _sync_feedback(self, state, ident, registry, previous):
        cell = state['problems'][ident]
        observations = cell['observations']
        required = {'original': 'verified',
                    'gold' if registry['mode'] == 'heavy' else 'silver':
                    'verified' if registry['mode'] == 'heavy' else 'review_recorded'}
        if registry['require_paper']:
            required['paper'] = 'complete'
        for gate, passing in required.items():
            observation = observations[gate]
            if observation['status'] == passing:
                if gate != 'original' and not cell['evidence_matches_original_answer']:
                    continue
                self._resolve_feedback(cell, gate, {'validated_at': now().isoformat(),
                    'observation': observation, 'manifest': cell.get('research_manifest')})
            elif (observation['status'] in {'failed', 'stale'} or cell['status'] == 'complete'
                  or previous.get(gate, {}).get('status') == passing):
                self._ticket(state, ident, gate, observation.get('details') or
                             [f"Required {gate} evidence is {observation['status']}."])
        if cell['evidence_matches_original_answer']:
            self._resolve_feedback(cell, 'answer_binding', {'manifest': cell.get('research_manifest'),
                                   'answer_sha256': cell.get('answer_sha256')})
        elif cell['status'] == 'complete':
            self._ticket(state, ident, 'answer_binding',
                         ['Research evidence must bind the completed original answer path and hash.'])

    def feedback(self, ident=None):
        """Read the durable host-delivery packet; does not dispatch or mark delivery."""
        with self.transaction(write=False) as (registry, state):
            problems = state['problems']
            if ident is not None:
                problems = {ident: problems[ident]}
            return {'delivery_automatic': False, 'mode': registry['mode'],
                    'deadline_utc': registry['deadline_utc'], 'sealed': state['sealed'],
                    'registry_sha256': state['registry_sha256'], 'problems': {
                key: {'repair_round': cell.get('repair_round', 0), 'lifecycle': cell['status'],
                      'frozen_source': registry['problems'][key], 'owner': cell.get('owner'),
                      'claim_token': cell.get('claim_token'), 'revisions': cell.get('revisions', []),
                      'feedback': cell.get('feedback', [])} for key, cell in problems.items()}}

    def acknowledge(self, ident, ticket_id, *, task_id, receipt, fingerprint):
        if not identity(task_id) or not identity(receipt):
            raise ValueError('actual delivery task id and receipt required')
        with self.transaction() as (_, state):
            ticket = next((t for t in state['problems'][ident].get('feedback', [])
                           if t['id'] == ticket_id), None)
            if ticket is None:
                raise ValueError('unknown feedback ticket')
            if fingerprint != ticket['fingerprint']:
                raise ValueError('feedback changed; deliver the current fingerprint before acknowledging')
            ticket['acknowledgments'].append({'at': now().isoformat(),
                                             'task_id': task_id, 'receipt': receipt, 'fingerprint': ticket['fingerprint']})
            ticket['needs_delivery'] = False
            self.event(state, 'feedback_acknowledged', ident, ticket_id=ticket_id, task_id=task_id)

    def reopen(self, ident, *, reason):
        if not identity(reason):
            raise ValueError('repair reason required')
        with self.transaction() as (registry, state):
            cell = state['problems'][ident]
            if state['sealed'] or (registry['deadline_utc'] is not None
                                   and now() >= deadline(registry['deadline_utc'])):
                raise ValueError('campaign sealed or deadline reached')
            if cell['status'] not in {'complete', 'partial', 'pending', 'released'}:
                raise ValueError('stop and reconcile active or unresolved jobs before repair')
            if cell['status'] in {'pending', 'released'} and not cell.get('candidate'):
                raise ValueError('reopen requires a terminal result or rejected submission')
            archived = {k: cell.pop(k) for k in ('manifest', 'sha256', 'answer_sha256',
                        'artifact', 'candidate', 'research_manifest', 'paper_state') if k in cell}
            cell.setdefault('revisions', []).append({'at': now().isoformat(), 'reason': reason,
                'repair_round': cell.get('repair_round', 0), 'previous_status': cell['status'],
                'artifacts': archived})
            cell.update(status='released', repair_round=cell.get('repair_round', 0) + 1)
            self._refresh(registry, state)
            self.event(state, 'reopen', ident, reason=reason, repair_round=cell['repair_round'])

    def claim(self, ident, owner):
        if not identity(owner):
            raise ValueError('owner required')
        with self.transaction() as (registry, state):
            if state['sealed'] or (registry['deadline_utc'] is not None
                                   and now() >= deadline(registry['deadline_utc'])):
                raise ValueError('campaign sealed or deadline reached')
            cell = state['problems'][ident]
            if cell['status'] not in {'pending', 'released'}:
                raise ValueError('problem is already claimed, unresolved, or terminal')
            occupied = sum(c['status'] in {'running', 'reconcile_required'} for c in state['problems'].values())
            if occupied >= registry['concurrency']:
                raise ValueError('concurrency limit reached')
            token = uuid.uuid4().hex
            cell.pop('reconciliation', None)
            cell.update(status='running', owner=owner, claim_token=token)
            self.event(state, 'claim', ident, owner=owner, claim_token=token)
            return token

    def release(self, ident, token, *, interrupted=False):
        with self.transaction() as (_, state):
            cell = state['problems'][ident]
            if state['sealed'] or cell['status'] != 'running' or cell.get('claim_token') != token:
                raise ValueError('current claim token required')
            cell['status'] = 'reconcile_required' if interrupted else 'released'
            if interrupted:
                self._ticket(state, ident, 'infrastructure', ['Prior job may still be running.'], recipient='host')
            self.event(state, 'interrupted' if interrupted else 'release', ident,
                       owner=cell['owner'], claim_token=token)

    def reconcile(self, ident, token, evidence):
        """Host attests the prior job has stopped; this never kills or relaunches it."""
        if not isinstance(evidence, str) or len(evidence.strip()) < 12:
            raise ValueError('host reconciliation evidence required')
        with self.transaction() as (_, state):
            cell = state['problems'][ident]
            if state['sealed'] or cell['status'] not in {'running', 'reconcile_required'} or cell.get('claim_token') != token:
                raise ValueError('existing unresolved claim required')
            cell.update(status='released', reconciliation=evidence)
            self._resolve_feedback(cell, 'infrastructure', {'claim_token': token, 'host_reconciliation': evidence})
            self.event(state, 'reconcile_stopped', ident, owner=cell['owner'],
                       claim_token=token, evidence=evidence)

    def validate_complete(self, ident, registry, manifest_path):
        folder = (self.root / 'problems' / ident).resolve()
        manifest_path = (folder / manifest_path).resolve()
        manifest_path.relative_to(folder)
        manifest = read_json(manifest_path)
        errors = audit_original_scope(manifest, manifest_path.parent, required=True, require_final_answer=True)
        if errors:
            raise ValueError('; '.join(errors))
        original_path, original_bytes = pinned(manifest['original_problem'], manifest_path.parent)
        original = json.loads(original_bytes)
        _, source = pinned(original['source'], original_path.parent)
        if digest(source) != registry['problems'][ident]['sha256']:
            raise ValueError('scope review is for a different registered original problem')
        answer_path, answer = pinned(manifest['final_answer'], manifest_path.parent)
        answer_path.relative_to(folder)
        report_path, report_bytes = pinned(manifest.get('final_proof_review'), manifest_path.parent)
        review = json.loads(report_bytes)
        implementers = manifest.get('implementers')
        if not isinstance(implementers, list) or not implementers or any(not identity(x) for x in implementers):
            raise ValueError('full implementer census required')
        reviewer = identity(review.get('reviewer'))
        census = {identity(x) for x in implementers}
        author = identity(manifest.get('manifest_author'))
        if not author or not reviewer or reviewer in census | {author}:
            raise ValueError('independent proof reviewer required')
        if review.get('implementers') != implementers:
            raise ValueError('proof review implementer census mismatch')
        if (review.get('verdict') != 'PASS_COMPLETE_PROOF' or review.get('gaps') != []
                or review.get('final_answer_sha256') != digest(answer)):
            raise ValueError('passing proof review for current answer required')
        _, provenance_bytes = pinned(review.get('reviewer_provenance'), report_path.parent)
        provenance = json.loads(provenance_bytes)
        if (identity(provenance.get('reviewer')) != reviewer
                or provenance.get('role') != 'final_proof_review'
                or any(not identity(provenance.get(k)) for k in ('task_id', 'model', 'provider'))
                or provenance.get('final_answer_sha256') != digest(answer)):
            raise ValueError('hash-bound proof review dispatch provenance required')
        provider = manifest.get('provider')
        if provider not in {'codex', 'claude'} or provenance.get('provider') != provider:
            raise ValueError('proof review requires matching provider provenance')
        if provider == 'codex' and provenance.get('model') != 'gpt-6-astra':
            raise ValueError('independent substantive proof review requires Astra')
        return {'manifest': str(manifest_path.relative_to(folder)), 'sha256': digest(manifest_path.read_bytes()), 'answer_sha256': digest(answer)}

    def finish(self, ident, *, manifest=None, partial=None):
        if (manifest is None) == (partial is None):
            raise ValueError('choose complete manifest or partial artifact')
        failure = None
        with self.transaction() as (registry, state):
            cell = state['problems'][ident]
            if state['sealed'] or cell['status'] not in {'pending', 'released'}:
                raise ValueError('release or reconcile the job before finishing')
            if manifest is not None:
                cell['candidate'] = {'path': str(manifest), 'sha256': None}
                try:
                    cell['candidate'] = self._ref(ident, manifest)
                    cell.update(self.validate_complete(ident, registry, manifest), status='complete')
                    cell['research_manifest'] = cell['candidate']
                    self._resolve_feedback(cell, 'submission', {'manifest': cell['candidate'],
                                           'answer_sha256': cell['answer_sha256']})
                except (ValueError, KeyError, TypeError, OSError, AttributeError, RecursionError) as error:
                    failure = str(error)
                    self._ticket(state, ident, 'submission', [failure])
                    self.event(state, 'finish_rejected', ident, error=failure,
                               candidate=cell.get('candidate'))
            else:
                folder = self.root / 'problems' / ident
                path = (folder / partial).resolve()
                path.relative_to(folder)
                cell.update(status='partial', artifact={'path': str(path.relative_to(folder)), 'sha256': digest(path.read_bytes())})
                self._resolve_feedback(cell, 'partial_artifact', {'artifact': cell['artifact']})
            self._refresh(registry, state)
            if failure is None:
                self.event(state, 'finish_' + cell['status'], ident)
        if failure is not None:
            raise ValueError(failure)

    def seal(self):
        failure = None
        with self.transaction() as (registry, state):
            self._refresh(registry, state)
            errors = []
            for ident, cell in state['problems'].items():
                if cell['status'] == 'complete':
                    if not cell['successful_complete']:
                        details = [str(detail) for observation in cell['observations'].values()
                                   for detail in observation.get('details', [])]
                        errors.append(f'{ident}: all configured completion gates must pass'
                                      + (': ' + '; '.join(details) if details else ''))
                elif cell['status'] == 'partial':
                    try:
                        pinned(cell['artifact'], self.root / 'problems' / ident)
                        self._resolve_feedback(cell, 'partial_artifact', {'artifact': cell['artifact']})
                    except (ValueError, KeyError, TypeError, OSError, AttributeError, RecursionError) as error:
                        self._ticket(state, ident, 'partial_artifact', [str(error)])
                        errors.append(f'{ident}: {error}')
                else:
                    errors.append(f'{ident}: all problems must be complete or explicitly partial')
            if errors:
                failure = '; '.join(errors)
                self.event(state, 'seal_rejected', errors=errors)
            else:
                state['sealed'] = True
                self.event(state, 'seal')
        if failure is not None:
            raise ValueError(failure)

    def status(self):
        with self.transaction(write=False) as (registry, state):
            self._refresh(registry, state, record_feedback=False)
            return {'deadline_utc': registry['deadline_utc'], 'concurrency': registry['concurrency'], 'mode': registry['mode'], **state}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--owner-key', type=Path, help='private controller key outside the campaign tree')
    commands = parser.add_subparsers(dest='command', required=True)
    init = commands.add_parser('init')
    init.add_argument('--problems', type=Path, required=True, help='JSON id to source path map; paths relative to this file')
    init.add_argument('--deadline', required=True)
    init.add_argument('--concurrency', required=True, type=int)
    init.add_argument('--mode', choices=('lite', 'heavy'), default='lite')
    init.add_argument('--require-paper', action='store_true')
    init.add_argument('--max-pages', type=int)
    claim = commands.add_parser('claim'); claim.add_argument('problem'); claim.add_argument('--owner', required=True)
    release = commands.add_parser('release'); release.add_argument('problem'); release.add_argument('--token', required=True); release.add_argument('--interrupted', action='store_true')
    reconcile = commands.add_parser('reconcile'); reconcile.add_argument('problem'); reconcile.add_argument('--token', required=True); reconcile.add_argument('--evidence', required=True)
    finish = commands.add_parser('finish'); finish.add_argument('problem')
    choice = finish.add_mutually_exclusive_group(required=True); choice.add_argument('--manifest'); choice.add_argument('--partial')
    observe = commands.add_parser('observe'); observe.add_argument('problem')
    observe.add_argument('--manifest', required=True); observe.add_argument('--paper-state')
    feedback = commands.add_parser('feedback'); feedback.add_argument('problem', nargs='?')
    ack = commands.add_parser('acknowledge'); ack.add_argument('problem'); ack.add_argument('--ticket', required=True)
    ack.add_argument('--task-id', required=True); ack.add_argument('--receipt', required=True)
    ack.add_argument('--fingerprint', required=True)
    reopen = commands.add_parser('reopen'); reopen.add_argument('problem'); reopen.add_argument('--reason', required=True)
    commands.add_parser('refresh')
    commands.add_parser('seal'); commands.add_parser('status')
    args = parser.parse_args()
    try:
        campaign = Campaign(args.root, owner_key=args.owner_key)
        if args.command == 'init':
            Campaign.initialize(args.root, {k: args.problems.parent / v for k, v in read_json(args.problems).items()}, deadline_utc=args.deadline, concurrency=args.concurrency, owner_key=args.owner_key, mode=args.mode, require_paper=args.require_paper, max_pages=args.max_pages)
        elif args.command == 'claim':
            print(campaign.claim(args.problem, args.owner))
        elif args.command == 'release':
            campaign.release(args.problem, args.token, interrupted=args.interrupted)
        elif args.command == 'reconcile':
            campaign.reconcile(args.problem, args.token, args.evidence)
        elif args.command == 'finish':
            campaign.finish(args.problem, manifest=args.manifest, partial=args.partial)
        elif args.command == 'observe':
            campaign.observe(args.problem, manifest=args.manifest, paper_state=args.paper_state)
        elif args.command == 'feedback':
            print(json.dumps(campaign.feedback(args.problem), indent=2))
        elif args.command == 'acknowledge':
            campaign.acknowledge(args.problem, args.ticket, task_id=args.task_id, receipt=args.receipt, fingerprint=args.fingerprint)
        elif args.command == 'reopen':
            campaign.reopen(args.problem, reason=args.reason)
        elif args.command == 'refresh':
            print(json.dumps(campaign.refresh(), indent=2))
        elif args.command == 'seal':
            campaign.seal()
        else:
            print(json.dumps(campaign.status(), indent=2))
    except (ValueError, KeyError, TypeError, OSError, AttributeError, RecursionError) as error:
        parser.exit(2, str(error) + '\n')


if __name__ == '__main__':
    main()
