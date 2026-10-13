"""The empty-first-turn route never grants ordinary candidate recovery authority."""
import asyncio
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from pilot_initial_recovery import validate_initial_recovery


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value))


class InitialRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name).resolve()
        self.source, self.target = base / 'parent', base / 'successor'
        self.folder = self.source / 'campaign/problems/example'
        self.stage = self.source / 'host/runtime/example/001-main-dossier'
        self.folder.mkdir(parents=True); self.stage.mkdir(parents=True)
        self.binary = base / 'isolated-codex'; self.binary.write_text('synthetic route')
        self.session = '11111111-1111-4111-8111-111111111111'
        now = datetime.now(timezone.utc)
        self.clock = dict(start_utc=now.isoformat(), research_close_utc=(now + timedelta(hours=23)).isoformat(), submission_deadline_utc=(now + timedelta(hours=24)).isoformat())
        self.config = dict(problems=['example'], exam=self.clock, deadline_utc=self.clock['submission_deadline_utc'], models={'main': 'gpt-6-astra'})
        (self.folder / 'input.txt').write_text('Synthetic original problem')
        (self.stage / 'stage.prompt.txt').write_text('Synthetic first dossier prompt')
        (self.stage / 'stage.answer.txt').write_bytes(b'')
        write(self.stage / 'stage.response-usage.json', [])
        write(self.stage / 'stage.messages.json', [])
        self.call = dict(name='example/001-main-dossier', module='main-dossier', status='process_failed', exit_code=1, session_id=self.session,
            resume_session=None, fresh_session=True, model_verified=True, model_actual='gpt-6-astra', model_requested='gpt-6-astra',
            answer_bytes=0, answer_sha256=digest(self.stage / 'stage.answer.txt'), prompt_sha256=digest(self.stage / 'stage.prompt.txt'),
            turn_completed=False, tool_event_count=0, persisted_tool_event_count=0, tool_events=[], persisted_tool_events=[], usage=None,
            accounting={'response_ids': [], 'encountered_response_ids': []}, protocol_errors=['turn.failed'],
            persisted_rollout_audit={'status':'verified', 'tool_events':[], 'response_usage_records': []})
        self.events = [{'type':'thread.started', 'thread_id': self.session}, {'type':'turn.started'}, {'type':'turn.failed','error':{'message':'Provider quota unavailable'}}]
        self.progress = dict(main_session=None, calls=[self.call], errors=[{'type':'StageFailure'}])
        self.auth = dict(schema_version=1,kind='initial_main_provider_failure',authorization='explicit_user',max_recovery_attempts=1,
            parent_root=str(self.source),target_root=str(self.target),problem_id='example', recovery_session_mode='fresh_session',
            session_id=self.session,codex_binary=str(self.binary),codex_binary_sha256=digest(self.binary),
            account_route={'user_authorized':True,'account_id':'synthetic-account','auth_source':str(base / '.codex/auth.json')})
        self.sync()

    def sync(self):
        write(self.source / 'host-config.json', self.config)
        write(self.source / 'exam/clock.json', self.clock)
        write(self.stage / 'stage.meta.json', self.call)
        write(self.folder / 'host-progress.json', self.progress)
        (self.stage / 'stage.events.jsonl').write_text(''.join(json.dumps({'event':e})+'\n' for e in self.events))
        for key,p in [('parent_config_sha256',self.source/'host-config.json'),('stage_meta_sha256',self.stage/'stage.meta.json'),('events_sha256',self.stage/'stage.events.jsonl'),('prompt_sha256',self.stage/'stage.prompt.txt'),('original_sha256',self.folder/'input.txt'),('clock_sha256',self.source/'exam/clock.json')]:
            self.auth[key] = digest(p)

    def load(self):
        return validate_initial_recovery(self.source,self.config,self.progress,[self.call],authorization=self.auth,problem_id='example',target_root=self.target)

    def test_explicit_fresh_conversation_retains_failure_and_clock(self):
        before = {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        result = self.load()
        self.assertIsNone(result['main_session'])
        self.assertEqual(result['initial_main_recovery']['failed_session_id'],self.session)
        self.assertEqual(result['calls'],self.progress['calls'])
        self.assertEqual(result['errors'],self.progress['errors'])
        self.assertEqual(result['initial_main_recovery']['clock_sha256'],digest(self.source/'exam/clock.json'))
        self.assertEqual(before,{str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})
        self.assertFalse(self.target.exists())

    def test_explicit_same_session_preserves_identity(self):
        self.auth['recovery_session_mode']='same_session'
        self.assertEqual(self.load()['main_session'],self.session)

    def test_missing_session_blocks_both_modes(self):
        self.call['session_id']=None; self.sync()
        for mode in ('same_session','fresh_session'):
            self.auth['recovery_session_mode']=mode
            with self.assertRaises(ValueError): self.load()

    def test_existing_candidate_never_gets_fresh_authority(self):
        for name in ('current-candidate.json','accepted-dossier.json','proof-current.json','proof.md','plan.json'):
            write(self.folder/name,{})
            with self.subTest(name=name), self.assertRaises(ValueError): self.load()
            (self.folder/name).unlink()

    def test_later_research_stage_blocks(self):
        later={**self.call,'name':'example/002-main-dossier'}
        self.progress['calls'].append(later)
        write(self.source/'host/runtime'/later['name']/'stage.meta.json',later)
        self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_completed_first_response_cannot_use_fresh_exception(self):
        self.call['status']='completed'; self.call['turn_completed']=True; self.call['exit_code']=0
        self.events[-1]={'type':'turn.completed'}; self.sync()
        with self.assertRaises(ValueError):self.load()

    def test_provider_failure_requires_raw_failure(self):
        self.events.pop(); self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_positive_answer_and_completed_event_block(self):
        (self.stage/'stage.answer.txt').write_text('Positive work')
        self.call['answer_bytes']=13; self.call['answer_sha256']=digest(self.stage/'stage.answer.txt'); self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_unexpected_tool_and_scientific_event_block(self):
        for event in ({'type':'turn.completed'},{'type':'item.completed','item':{'type':'agent_message','text':'work'}},{'type':'item.completed','item':{'type':'mcp_tool_call'}}):
            with self.subTest(event=event):
                self.events.append(event); self.sync()
                with self.assertRaises(ValueError): self.load()
                self.events.pop()

    def test_preexisting_recovery_or_continuation_cannot_renew_bound(self):
        for key in ('initial_main_recovery','continuation_parent'):
            self.config[key]='present'; self.sync()
            with self.assertRaises(ValueError): self.load()
            del self.config[key]

    def test_expired_research_clock_blocks(self):
        self.clock['start_utc']='2000-01-01T00:00:00Z'; self.clock['research_close_utc']='2000-01-01T23:00:00Z'
        self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_hash_tamper_and_binary_route_tamper_block(self):
        for key in ('parent_config_sha256','stage_meta_sha256','events_sha256','prompt_sha256','original_sha256','clock_sha256','codex_binary_sha256'):
            old=self.auth[key]; self.auth[key]='0'*64
            with self.subTest(key=key), self.assertRaises(ValueError): self.load()
            self.auth[key]=old

    def test_account_route_and_mode_require_explicit_authority(self):
        for key in ('account_route','recovery_session_mode','authorization'):
            old=self.auth.pop(key)
            with self.subTest(key=key), self.assertRaises(ValueError): self.load()
            self.auth[key]=old

    def test_empty_failed_paper_preserved_but_verified_paper_blocks(self):
        paper={**deepcopy(self.call),'name':'example/paper-001-reconstruct','module':'paper-reconstruct','status':'unverifiable_rollout_audit','session_id':None,'model_verified':False,'model_actual':None}
        stage=self.source/'host/runtime'/paper['name']; stage.mkdir()
        (stage/'stage.answer.txt').write_bytes(b''); (stage/'stage.events.jsonl').write_text('')
        write(stage/'stage.response-usage.json',[]); write(stage/'stage.messages.json',[])
        write(stage/'stage.meta.json',paper); self.progress['calls'].append(paper); self.sync()
        self.assertEqual(len(self.load()['calls']),2)
        paper['model_verified']=True; write(stage/'stage.meta.json',paper); self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_orphan_science_and_raw_message_or_usage_block(self):
        for filename in ('proof.md', 'current-candidate.md', 'plan.json'):
            path=self.folder/filename; path.write_text('orphan work')
            with self.subTest(filename=filename), self.assertRaises(ValueError): self.load()
            path.unlink()
        for filename in ('stage.messages.json', 'stage.response-usage.json'):
            path=self.stage/filename; write(path,[{'text':'science or usage'}])
            with self.subTest(filename=filename), self.assertRaises(ValueError): self.load()
            write(path,[])

    def test_duplicate_saved_call_cannot_hide_disk_stage(self):
        later={**self.call,'name':'example/002-main-dossier'}
        write(self.source/'host/runtime'/later['name']/'stage.meta.json',later)
        self.progress['calls'].append(self.call); self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_positive_history_blocks(self):
        self.progress['triage_history']=[{'completed':True}]; self.sync()
        with self.assertRaises(ValueError): self.load()

    def test_native_successor_and_first_dossier_preserve_clock_and_parent(self):
        import codex_pilot as pilot
        import pilot_continuation as continuation
        self.clock.update(schema_version=1, clock_scope='whole_campaign_including_continuations',
                          cleanup_guard_seconds=15, state_root=str(self.source/'exam'), page_limit=16)
        self.config.update(internet_browse=False, codex_binary='old-route', mode='lite')
        self.sync()
        saved=self.load()
        write(self.source/'campaign/state.json',{'problems':{'example':{'status':'partial','successful_complete':False}}})
        before={str(p.relative_to(self.source)):digest(p) for p in self.source.rglob('*') if p.is_file()}
        checkpoint={'config':self.config,'problems':{'example':saved},'parent':{'source_root':str(self.source),
            'files':before,'manifest_sha256':hashlib.sha256(json.dumps(before,sort_keys=True,separators=(',',':')).encode()).hexdigest()}}
        auth_path=self.source.parent/'authorization.json';write(auth_path,self.auth)
        with patch.object(continuation,'validate_and_load',return_value=checkpoint), patch.object(pilot,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'codex-cli 0.157.1'}) as auth, patch.object(pilot,'freeze_runtime',return_value=({},{})):
            config=pilot.prepare_continuation(self.source,self.target,self.source.parent/'reconciliation.json',initial_main_recovery=auth_path)
        auth.assert_called_once_with(str(self.binary))
        self.assertEqual(config['codex_binary'],str(self.binary))
        self.assertEqual(config['exam']['state_root'],str(self.target/'exam'))
        for key in ('start_utc','research_close_utc','submission_deadline_utc'):
            self.assertEqual(config['exam'][key],self.clock[key])
        self.assertEqual(json.loads((self.target/'exam/clock.json').read_text()),config['exam'])
        self.assertEqual(before,{str(p.relative_to(self.source)):digest(p) for p in self.source.rglob('*') if p.is_file()})
        self.assertFalse((self.target/'campaign/problems/example/proof-current.json').exists())
        fake=SimpleNamespace(root=self.target,config=config,exam=SimpleNamespace(research_timeout=lambda x:x),
                             campaign=SimpleNamespace(claim=lambda *args:'synthetic-claim',release=lambda *args:None),policy=lambda _: 'synthetic generic policy')
        problem=pilot.Problem(fake,'example')
        class ReachedDossier(BaseException):pass
        observed={}
        async def first(instruction,dossier=False,purpose=None):
            observed.update(dossier=dossier,session=problem.session,calls=list(problem.calls),instruction=instruction)
            raise ReachedDossier()
        with patch.object(problem,'status'),patch.object(problem,'main_turn',side_effect=first):
            with self.assertRaises(ReachedDossier):asyncio.run(problem._run_research())
        self.assertTrue(observed['dossier']);self.assertIsNone(observed['session'])
        self.assertEqual(observed['calls'],saved['calls'])
        self.assertNotIn('main-repair',observed['instruction'])


if __name__ == '__main__':
    unittest.main()
