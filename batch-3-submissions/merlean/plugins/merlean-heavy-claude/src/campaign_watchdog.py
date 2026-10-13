"""Optional deterministic campaign inspection. No model calls, signals or job launches.

The host supplies active stage snapshots and owns any cancellation. Silence is not
proof of a hung model: only an explicit stage/campaign deadline requests cancellation.
Reports preserve recovery requests without changing claims, budgets or feedback.
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
import hashlib
import hmac
import json
import math
import os
from pathlib import Path
import subprocess
import secrets

from campaign import deadline, digest


def capture_process_identity(pid):
    """Return a best-effort portable process birth/command fingerprint, else None.

    This fingerprint is diagnostic, not permission to signal a PID. The host must
    cancel only its retained process/task handle, including after identity checks.
    """
    if type(pid) is not int or pid <= 0:
        return None
    try:
        result = subprocess.run(['ps', '-p', str(pid), '-o', 'lstart=', '-o', 'args='],
                                capture_output=True, text=True, timeout=2)
        value = result.stdout.strip()
        return digest(value.encode()) if result.returncode == 0 and value else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def probe_process(pid, expected_identity):
    if type(pid) is not int or pid <= 0:
        return {'alive': None, 'identity_match': None}
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return {'alive': False, 'identity_match': None}
    except (PermissionError, OSError):
        return {'alive': None, 'identity_match': None}
    actual = capture_process_identity(pid)
    return {'alive': True, 'identity_match': (actual == expected_identity)
            if actual and expected_identity else None}


class CampaignWatchdog:
    """Controller-authorized host report writer; creation alone does not poll."""

    def __init__(self, campaign, report_path, *, interval_seconds=300):
        if (isinstance(interval_seconds, bool) or not isinstance(interval_seconds, (int, float))
                or not math.isfinite(interval_seconds) or interval_seconds <= 0):
            raise ValueError('watchdog interval must be finite and positive')
        self.campaign = campaign
        self.report_path = Path(report_path).resolve()
        if self.report_path.is_relative_to(campaign.root):
            raise ValueError('watchdog report must be outside the agent campaign tree')
        self.interval_seconds = interval_seconds
        self._history = []
        self._paper_grants = {}
        if self.report_path.exists():
            previous = json.loads(self.report_path.read_text())
            self._history = previous.get('incidents', [])

    @staticmethod
    def paper_research_released(cell):
        # The authenticated controller permits finish only from pending/released.
        # release/finish retain owner and claim_token as history; the status, not
        # the presence of that historical token, distinguishes active ownership.
        return cell.get('status') in {'complete', 'partial'}

    @staticmethod
    def paper_binding(cell):
        return {key: cell.get(key) for key in
                ('status', 'successful_complete', 'manifest', 'sha256', 'answer_sha256',
                 'artifact', 'owner', 'claim_token', 'repair_round')}

    def register_paper_task(self, problem, task, phase_reader):
        """Host-only grant; never reconstructed from a stage or restart receipt."""
        if task is not asyncio.current_task() or task.done() or not callable(phase_reader):
            raise ValueError('paper grant requires the current retained host task')
        self.campaign.refresh()
        cell = self.campaign.status()['problems'][problem]
        if not self.paper_research_released(cell):
            raise ValueError('paper grant requires released terminal research state')
        if problem in self._paper_grants:
            raise ValueError('paper task already registered')
        token = secrets.token_hex(32)
        self._paper_grants[problem] = (token, task, self.paper_binding(cell), phase_reader)
        return token

    def revoke_paper_task(self, problem, token):
        grant = self._paper_grants.get(problem)
        if grant and hmac.compare_digest(grant[0], token):
            del self._paper_grants[problem]

    def inspect(self, stages, *, now_utc=None, restarting=False):
        """Snapshot stages without granting their contents controller authority.

        Active stage fields: name, problem, status, pid, process_identity,
        deadline_utc, claim_token. Optional fields: last_progress_utc,
        failure_kind (quota/capacity), consecutive_failures. Terminal snapshots
        may be included for repeated failure diagnostics. On restart no automatic
        adoption, release or retry is possible, even if the process appears dead.
        """
        instant = now_utc or datetime.now(timezone.utc)
        if instant.tzinfo is None:
            raise ValueError('inspection time must include timezone')
        with self.campaign.transaction(write=False) as (registry, state):
            key = self.campaign.owner_key
            if key is None or key.is_relative_to(self.campaign.root) or not hmac.compare_digest(
                    digest(key.read_bytes()), registry.get('owner_key_sha256', '')):
                raise ValueError('valid controller owner key required')
            state = json.loads(json.dumps(state))
            end = deadline(registry['deadline_utc']) if registry['deadline_utc'] is not None else None
        registry_sha256 = state['registry_sha256']
        observations = []
        incidents = []

        def incident(kind, problem, stage=None, action='recovery_needed', **details):
            payload = {'kind': kind, 'problem': problem, 'stage': stage,
                       'action': action, **details}
            payload['id'] = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
            payload['observed_utc'] = instant.isoformat()
            incidents.append(payload)

        active_problems = set()
        for stage in stages:
            name, problem = stage.get('name'), stage.get('problem')
            cell = state['problems'].get(problem)
            if not cell:
                incident('unknown_problem', problem, name)
                continue
            active = stage.get('status') in {'running', 'launching', 'backoff', 'host_work'}
            if stage.get('consecutive_failures', 0) >= 3:
                incident('repeated_infrastructure_failure', problem, name,
                         failure_kind=stage.get('failure_kind', 'unknown'))
            if not active:
                continue
            active_problems.add(problem)
            ownership = (cell.get('status') == 'running' and bool(stage.get('claim_token'))
                         and stage.get('claim_token') == cell.get('claim_token'))
            if stage.get('ownership_scope') == 'exam_paper':
                grant = self._paper_grants.get(problem)
                phase = grant[3]() if grant else None
                paper_phase = isinstance(phase, str) and (phase == 'exam-paper-handoff'
                    or phase.startswith(('running:paper-', 'returned:paper-')))
                ownership = bool(grant and not restarting and not grant[1].done()
                    and paper_phase and stage.get('phase') == phase
                    and stage.get('paper_claim_token') == grant[0]
                    and self.paper_research_released(cell) and self.paper_binding(cell) == grant[2]
                    and (name == problem + '/host' or name.startswith(problem + '/paper-')))
            observation = {'name': name, 'problem': problem, 'ownership_matches': ownership,
                           'last_progress_utc': stage.get('last_progress_utc')}
            if not ownership:
                incident('stale_ownership', problem, name)
                observations.append(observation)
                continue
            if stage.get('mathematical_stagnation') is True:
                incident('mathematical_stagnation', problem, name, action='supervisor_review',
                         evidence=stage.get('progress_evidence'))
            if stage.get('status') == 'host_work':
                observation['health'] = 'host_work'
                if restarting:
                    incident('restart_reconciliation', problem, name)
                elif end is not None and instant >= end:
                    incident('campaign_deadline', problem, name, action='cancel_owned_task')
                if stage.get('deadline_utc') is not None:
                    try:
                        stage_end = deadline(stage['deadline_utc'])
                    except (TypeError, ValueError):
                        incident('stage_deadline_unknown', problem, name)
                    else:
                        if instant >= stage_end and not restarting:
                            incident('stage_deadline', problem, name, action='cancel_owned_task')
                observations.append(observation)
                continue
            if stage.get('status') == 'backoff':
                kind = stage.get('failure_kind', 'unknown')
                observation['health'] = 'quota_wait' if kind == 'quota' else 'provider_backoff'
                if kind != 'capacity':
                    incident('provider_wait', problem, name, action='respect_provider_limits', failure_kind=kind)
                if restarting:
                    incident('restart_reconciliation', problem, name)
                if end is not None and instant >= end:
                    incident('campaign_deadline', problem, name)
                observations.append(observation)
                continue
            expired = False
            stage_end = None
            try:
                stage_end = deadline(stage['deadline_utc'])
            except (KeyError, TypeError, ValueError):
                incident('stage_deadline_unknown', problem, name)
                expired = end is not None and instant >= end
            else:
                expired = instant >= (min(stage_end, end) if end is not None else stage_end)
            if expired and not restarting:
                # Advisory to the host's retained task only. A PID is never
                # sufficient authority, even when its fingerprint matches.
                incident('stage_deadline', problem, name, action='cancel_owned_task')
            probe = probe_process(stage.get('pid'), stage.get('process_identity'))
            observation.update(probe)
            if probe['alive'] is False:
                incident('dead_child', problem, name)
            elif probe['identity_match'] is not True:
                incident('process_identity_unverified', problem, name)
            elif restarting:
                incident('restart_live_job', problem, name, action='preserve_live_job')
            elif not expired and stage_end is not None:
                observation['health'] = 'running_within_deadline'
            observations.append(observation)
        for problem, cell in state['problems'].items():
            if cell['status'] in {'running', 'reconcile_required'} and problem not in active_problems:
                incident('claim_without_active_stage', problem)
            for ticket in cell.get('feedback', []):
                if ticket.get('status') == 'open' and ticket.get('needs_delivery'):
                    incident('undelivered_feedback', problem, action='deliver_feedback',
                             ticket_id=ticket['id'], fingerprint=ticket['fingerprint'],
                             artifacts=ticket.get('artifacts', {}), recipient=ticket.get('recipient'))
        known = {item['id'] for item in self._history}
        self._history.extend(item for item in incidents if item['id'] not in known)
        report = {'schema_version': 1, 'checked_utc': instant.isoformat(),
                  'interval_seconds': self.interval_seconds, 'restarting': restarting,
                  'registry_sha256': registry_sha256, 'deadline_utc': end.isoformat() if end is not None else None,
                  'automatic_restart': False, 'observations': observations,
                  'current_incidents': incidents, 'incidents': self._history}
        self.report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.report_path.with_suffix('.next')
        fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, 'w') as stream:
            json.dump(report, stream, indent=2)
            stream.write('\n')
        temporary.replace(self.report_path)
        return report

    async def monitor(self, snapshot, stop, *, on_incident=None):
        """Host-owned opt-in loop; callback receives advisory incident packets.

        Callback must revalidate and use retained task handles for cancellation,
        never raw PID signaling. It must not interpret delivery as resolution.
        """
        while not stop.is_set():
            report = await asyncio.to_thread(self.inspect, snapshot())
            if on_incident and report['current_incidents']:
                await on_incident(report)
            try:
                await asyncio.wait_for(stop.wait(), timeout=self.interval_seconds)
            except asyncio.TimeoutError:
                pass
