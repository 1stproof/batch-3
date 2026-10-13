"""Campaign-wide exam clock, cooperative research admission and paper dispatch.

The persisted clock belongs to the original campaign, including all continuations.
Paper completion is deliberately independent of research acceptance.
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone
import uuid


MODEL_TIME_POLICIES = ('formal-clock', 'test-cap', 'legacy-caps')


def model_time_policy(config):
    """Absent saved policy means legacy behavior, never an implicit migration."""
    policy = config.get('exam_model_time_policy', 'legacy-caps')
    cap = config.get('exam_test_call_timeout_seconds')
    if policy not in MODEL_TIME_POLICIES:
        raise ValueError('unsupported exam model time policy')
    if policy != 'legacy-caps' and not config.get('exam'):
        raise ValueError('exam model time policy requires an exam clock')
    if policy == 'test-cap':
        if (isinstance(cap, bool) or not isinstance(cap, (int, float))
                or not math.isfinite(cap) or not 1 <= cap <= 86400):
            raise ValueError('exam test call timeout must be finite and between 1 and 86400')
    elif cap is not None:
        raise ValueError('exam test call timeout requires explicit test-cap policy')
    return policy, cap


def select_model_time_policy(config, *, policy=None, test_cap=None, fresh=False,
                             legacy_override=False):
    """Validate prospective selection before any run creation or reservation."""
    old_policy, old_cap = model_time_policy(config)
    selected = policy if policy is not None else ('formal-clock' if fresh and config.get('exam') else old_policy)
    cap = test_cap if test_cap is not None else (old_cap if selected == old_policy else None)
    result = {'exam_model_time_policy': selected, 'exam_test_call_timeout_seconds': cap}
    model_time_policy({**config, **result})
    if config.get('exam') and selected != 'legacy-caps' and legacy_override:
        raise ValueError('main/paper stage cap overrides require legacy-caps; use explicit exam test-cap policy for testing')
    return result


def model_timeout(runtime, config, phase, legacy_requested):
    """Bound thinking only by the selected policy and the original phase clock.

    Technical operations keep using research_timeout/paper_timeout directly;
    they do not inherit this model-reasoning allowance.
    """
    policy, cap = model_time_policy(config)
    requested = legacy_requested if policy == 'legacy-caps' else cap if policy == 'test-cap' else math.inf
    if phase == 'research':
        return runtime.research_timeout(requested)
    if phase == 'paper':
        return runtime.paper_timeout(requested)
    raise ValueError('unknown model time phase')


class ResearchClosed(RuntimeError):
    """No additional research may be admitted; preserve and write available evidence."""


class PaperDeadline(RuntimeError):
    """The original campaign's submission budget has expired."""


def utc_now():
    return datetime.now(timezone.utc)


def _write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.next')
    with temporary.open('w') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def _time(value):
    result = datetime.fromisoformat(value)
    if result.tzinfo is None:
        raise ValueError('exam timestamps must include timezone')
    return result


def _public(value):
    if isinstance(value, dict):
        return {key: _public(item) for key, item in value.items()
                if key not in {'claim_token', 'owner_key', 'token'}}
    if isinstance(value, list):
        return [_public(item) for item in value]
    return value


def new_config(root, *, start=None, research_hours=22.75, total_hours=24, guard_seconds=15):
    for name, value in [('research_hours', research_hours), ('total_hours', total_hours),
                        ('guard_seconds', guard_seconds)]:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(name + ' must be finite and positive')
    if research_hours >= total_hours or total_hours > 24:
        raise ValueError('exam requires 0 < research hours < total hours <= 24')
    if research_hours * 3600 <= guard_seconds:
        raise ValueError('research allowance must exceed cleanup guard')
    start = start or utc_now()
    return {'schema_version': 1, 'start_utc': start.isoformat(),
        'research_close_utc': (start + timedelta(hours=research_hours)).isoformat(),
        'submission_deadline_utc': (start + timedelta(hours=total_hours)).isoformat(),
        'cleanup_guard_seconds': guard_seconds,
        'state_root': str(Path(root).resolve() / 'exam'),
        'clock_scope': 'whole_campaign_including_continuations',
        'official_rule_source': 'https://1stproof.org/assets/docs/batch3-call-for-submissions.pdf',
        'page_limit': 16}


class ExamRuntime:
    def __init__(self, config, *, clock=utc_now):
        self.config = dict(config)
        self.now = clock
        if config.get('schema_version') != 1 or config.get('clock_scope') != 'whole_campaign_including_continuations':
            raise ValueError('unsupported exam clock')
        self.start = _time(config['start_utc'])
        self.research_close = _time(config['research_close_utc'])
        self.deadline = _time(config['submission_deadline_utc'])
        if not self.start < self.research_close < self.deadline <= self.start + timedelta(hours=24):
            raise ValueError('invalid original exam deadlines')
        self.guard = config['cleanup_guard_seconds']
        if isinstance(self.guard, bool) or not isinstance(self.guard, (float, int)) or not math.isfinite(self.guard) or self.guard <= 0:
            raise ValueError('invalid exam cleanup guard')
        self.root = Path(config['state_root'])
        if not self.root.is_absolute():
            raise ValueError('exam state root must be absolute for continuation identity')
        self.root.mkdir(parents=True, exist_ok=True)
        clock_path = self.root / 'clock.json'
        # Exclusive creation prevents a second host from replacing the origin.
        try:
            with clock_path.open('x') as stream:
                json.dump(config, stream, sort_keys=True)
                stream.flush()
                os.fsync(stream.fileno())
        except FileExistsError:
            if json.loads(clock_path.read_text()) != config:
                raise ValueError('exam clock differs from immutable original campaign clock')

    def remaining(self):
        return max(0, (self.deadline - self.now()).total_seconds())

    def research_timeout(self, requested):
        available = (self.research_close - self.now()).total_seconds() - self.guard
        if available < 1:
            raise ResearchClosed('original campaign research admission closed for reserved paper hour')
        return min(requested, available)

    def paper_timeout(self, requested):
        available = self.remaining() - self.guard
        if available < 1:
            raise PaperDeadline('original campaign submission deadline reached')
        return min(requested, available)

    def paper_dir(self, ident):
        if not ident or Path(ident).name != ident or ident in {'.', '..'}:
            raise ValueError('invalid exam problem identity')
        return self.root / 'papers' / ident

    def snapshot(self, problem, *, recovery_destination=None):
        """Capture once, after all admitted research has returned and been reaped."""
        if recovery_destination is None and getattr(problem.pilot, 'config', {}).get('paper_recovery'):
            from pilot_paper_recovery import active_snapshot
            revised = active_snapshot(problem, self)
            if revised is not None:
                return revised
        if recovery_destination is not None:
            import re
            if not re.fullmatch(r'snapshot-recovery-[0-9a-f]{24}', recovery_destination):
                raise ValueError('invalid versioned paper snapshot destination')
        destination = self.paper_dir(problem.ident) / (recovery_destination or 'snapshot')
        receipt = destination.parent / (destination.name + '-receipt.json')
        if destination.exists():
            expected = json.loads(receipt.read_text())['manifest_sha256']
            if hashlib.sha256((destination / 'manifest.json').read_bytes()).hexdigest() != expected:
                raise ValueError('exam snapshot manifest changed')
            self.verify_snapshot(destination, check_budget=lambda: self.paper_timeout(1))
            return destination
        self.paper_timeout(1)
        destination.parent.mkdir(parents=True, exist_ok=True)
        pending = destination.with_name('snapshot.' + uuid.uuid4().hex + '.next')
        pending.mkdir()
        state = problem.pilot.campaign.status()['problems'][problem.ident]
        payload = {'schema_version': 1, 'problem': problem.ident,
            'original_sha256': hashlib.sha256(problem.original_bytes).hexdigest(),
            'created_utc': self.now().isoformat(), 'exam_clock': self.config,
            'research_status': state, 'current': problem.current,
            'dossier': problem.dossier, 'findings': problem.findings, 'errors': problem.errors,
            'execution_history': problem.execution_history,
            'final_assessment_history': problem.final_assessment_history,
            'advisory_scope_history': problem.advisory_scope_history,
            'calls': problem.calls,
            'authority': 'immutable available evidence; no new research acceptance or grade'}
        _write(pending / 'snapshot.json', _public(payload))
        (pending / 'input.txt').write_bytes(problem.original_bytes)
        for source in sorted(problem.folder.rglob('*')):
            self.paper_timeout(1)
            if source.is_symlink():
                raise ValueError('exam evidence contains a symlink: ' + str(source))
            if source.is_file():
                target = pending / 'evidence' / source.relative_to(problem.folder)
                target.parent.mkdir(parents=True, exist_ok=True)
                with source.open('rb') as incoming, target.open('wb') as outgoing:
                    while True:
                        self.paper_timeout(1)
                        block = incoming.read(1024 * 1024)
                        if not block:
                            break
                        outgoing.write(block)
        files = {}
        for path in sorted(pending.rglob('*')):
            self.paper_timeout(1)
            if path.is_file():
                digest = hashlib.sha256()
                with path.open('rb') as stream:
                    while True:
                        self.paper_timeout(1)
                        block = stream.read(1024 * 1024)
                        if not block:
                            break
                        digest.update(block)
                files[str(path.relative_to(pending))] = digest.hexdigest()
        _write(pending / 'manifest.json', {'schema_version': 1, 'files': files})
        for path in pending.rglob('*'):
            if path.is_file():
                path.chmod(0o444)
        pending.rename(destination)
        _write(receipt, {'manifest_sha256': hashlib.sha256((destination / 'manifest.json').read_bytes()).hexdigest()})
        receipt.chmod(0o444)
        self.verify_snapshot(destination, check_budget=lambda: self.paper_timeout(1))
        return destination

    @staticmethod
    def verify_snapshot(directory, check_budget=lambda: None):
        manifest = json.loads((directory / 'manifest.json').read_text())
        actual = {str(p.relative_to(directory)) for p in directory.rglob('*') if p.is_file()}
        if actual != set(manifest['files']) | {'manifest.json'}:
            raise ValueError('exam snapshot file census changed')
        for name, expected in manifest['files'].items():
            check_budget()
            path = directory / name
            if path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):
                raise ValueError('exam snapshot evidence changed: ' + name)
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                while True:
                    check_budget()
                    block = stream.read(1024 * 1024)
                    if not block:
                        break
                    digest.update(block)
            if digest.hexdigest() != expected:
                raise ValueError('exam snapshot evidence changed: ' + name)

    async def dispatch(self, problem, writer=None):
        """Execute the real writer once; interruption leaves resumable stage receipts."""
        folder = self.paper_dir(problem.ident)
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / 'writer.lock').open('a') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                return {'status': 'writer_already_running', 'terminal': False}
            receipt = folder / 'result.json'
            if receipt.exists():
                result = json.loads(receipt.read_text())
                if result.get('terminal') is True:
                    return result
            from pilot_paper import prepare_exam_fallback
            prepare_exam_fallback(problem, self)
            snapshot = self.snapshot(problem)
            _write(folder / 'handoff.json', {'snapshot': str(snapshot), 'started_utc': self.now().isoformat(),
                'research_acceptance': 'unchanged',
                'handoff_reason': ('reserved_paper_hour' if self.now() >= self.research_close - timedelta(seconds=self.guard)
                                   else 'research_returned_early_complete_or_operational_stop'),
                'submission_deadline_utc': self.config['submission_deadline_utc']})
            if writer is None:
                engine = self.config.get('paper_engine', 'legacy')
                if engine == 'lightweight-v1':
                    from pilot_paper_light import run_exam_paper
                elif engine == 'legacy':
                    from pilot_paper import run_exam_paper
                else:
                    raise ValueError('unsupported saved paper engine')
                writer = run_exam_paper
            result = await writer(problem, snapshot, self)
            if not isinstance(result, dict):
                raise ValueError('paper engine must return an independent result object')
            try:
                self.verify_snapshot(snapshot, check_budget=lambda: self.paper_timeout(1))
            except PaperDeadline:
                # Preserve the writer's actual best artifact, but do not assert a
                # final integrity check that the shared deadline prevented.
                result = {**result, 'status': 'deadline-partial', 'terminal': True,
                          'polishing_complete': False, 'final_snapshot_verification': 'INCOMPLETE'}
            _write(receipt, result)
            return result


def rebase_copied_paper_state(prior_exam, destination):
    """Move only live host storage pointers after an exact stopped-state copy.

    Manuscripts, completed reviews, model identities, snapshot manifests and raw
    evidence remain unchanged. The original tree is never written.
    """
    prior_exam, destination = Path(prior_exam).resolve(), Path(destination).resolve()
    def location(value):
        old = Path(value)
        if not old.is_absolute() or not old.is_relative_to(prior_exam):
            raise ValueError('live paper storage pointer escapes original exam')
        new = destination/old.relative_to(prior_exam)
        if old.is_file() and (not new.is_file() or hashlib.sha256(old.read_bytes()).hexdigest() != hashlib.sha256(new.read_bytes()).hexdigest()):
            raise ValueError('copied paper artifact differs from preserved parent')
        return str(new)
    for ledger_path in (destination/'papers').glob('*/paper-ledger.json'):
        ledger = json.loads(ledger_path.read_text())
        ledger['snapshot'] = location(ledger['snapshot'])
        ref = ledger['snapshot_manifest']
        new_manifest = location(ref['path'])
        if hashlib.sha256(Path(new_manifest).read_bytes()).hexdigest() != ref['sha256']:
            raise ValueError('copied paper snapshot identity changed')
        ledger['snapshot_manifest'] = {**ref,'path':new_manifest}
        for key in ('best_available_tex','best_available_pdf'):
            if ledger.get(key): ledger[key] = location(ledger[key])
        _write(ledger_path, ledger)
        state_path = ledger_path.parent/'work/00-run-state.json'
        if state_path.is_file():
            state = json.loads(state_path.read_text())
            lineage = state.get('raw_lineage')
            if lineage:
                prior_paper = prior_exam/'papers'/ledger_path.parent.name
                def live_file(value):
                    old = Path(value)
                    if (not old.is_relative_to(prior_paper) or old.resolve() != old
                            or not old.is_file() or old.stat().st_nlink != 1):
                        raise ValueError('raw seed path must be a canonical regular owned paper file')
                    new = destination/old.relative_to(prior_exam)
                    if (new.resolve() != new or not new.is_file() or new.stat().st_nlink != 1
                            or old.read_bytes() != new.read_bytes()):
                        raise ValueError('copied raw seed file differs from its canonical parent')
                    return str(new)
                seed_path = Path(lineage['seed_manifest'])
                if (lineage.get('output') != state['output']
                        or lineage.get('manifest_sha256') != state.get('raw_checkpoint', {}).get('manifest_sha256')
                        or seed_path.is_symlink() or not seed_path.is_file()
                        or hashlib.sha256(seed_path.read_bytes()).hexdigest() != lineage['seed_manifest_sha256']):
                    raise ValueError('copied raw lineage lacks exact original seed binding')
                copied_seed = Path(live_file(str(seed_path)))
                seed = json.loads(copied_seed.read_text())
                files = seed.get('files')
                paths = [item.get('path') for item in files if isinstance(item, dict)] if isinstance(files, list) else []
                assets = seed.get('assets', [])
                if (seed.get('schema_version') != 1 or seed.get('output') != state['output']
                        or seed.get('manifest_sha256') != lineage['manifest_sha256']
                        or not paths or len(paths) != len(files) or not all(isinstance(p, str) for p in paths)
                        or len(set(paths)) != len(paths) or paths.count(state['output']) != 1
                        or not isinstance(assets, list) or not all(isinstance(p, str) and p in paths for p in assets)
                        or len(set(assets)) != len(assets)):
                    raise ValueError('copied raw seed has invalid output, files or checkpoint binding')
                seed['output'] = live_file(seed['output'])
                seed['files'] = [{**item, 'path': live_file(item['path'])} for item in files]
                if 'assets' in seed:
                    seed['assets'] = [live_file(path) for path in assets]
                seed['rebased_from'] = {'path': str(seed_path), 'sha256': lineage['seed_manifest_sha256']}
                # Retain the copied historical seed; this separate live seed owns the successor paths.
                live_seed = copied_seed.with_name('00-raw-candidate-seed-rebased-' + lineage['seed_manifest_sha256'][:16] + '.json')
                if live_seed.exists() or live_seed.is_symlink():
                    raise ValueError('rebased raw seed already exists; explicit reconciliation required')
                with live_seed.open('x') as handle:
                    handle.write(json.dumps(seed, sort_keys=True, indent=2) + '\n')
                state['raw_lineage'] = {**lineage, 'output': seed['output'],
                    'seed_manifest': str(live_seed),
                    'seed_manifest_sha256': hashlib.sha256(live_seed.read_bytes()).hexdigest()}
            state['output'], state['work_dir'] = location(state['output']), location(state['work_dir'])
            output = Path(state['output'])
            st = output.stat()
            state['output_reservation'] = {'dev':st.st_dev,'ino':st.st_ino,
                'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
                'claimed_at':datetime.now(timezone.utc).isoformat()}
            _write(state_path,state)
            from paper_writing_codex.workflow import verify_output
            verify_output(state,require_reservation=True,require_content=True)
        result_path = ledger_path.parent/'result.json'
        if result_path.is_file():
            result = json.loads(result_path.read_text())
            for key in ('best_available_tex','best_available_pdf'):
                if result.get(key): result[key] = location(result[key])
            _write(result_path,result)
