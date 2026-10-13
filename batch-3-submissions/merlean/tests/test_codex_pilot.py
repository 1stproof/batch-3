"""Synthetic pilot lifecycle integration; no model, benchmark, or probe execution."""
import asyncio
from datetime import timedelta
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace
from unittest.mock import AsyncMock
import contextlib
import io
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
from campaign import Campaign

class PilotIntegrationTests(unittest.TestCase):
    def test_sol61_transport_keeps_high_reasoning_and_unknown_dated_price(self):
        from codex_transport import _command
        from api_accounting import APIAccountingLedger
        command = _command('gpt-6.1-sol', 'high', None, internet_browse=False)
        self.assertEqual(command[command.index('-m') + 1], 'gpt-6.1-sol')
        self.assertIn('model_reasoning_effort="high"', command)
        self.assertIn('forced_login_method="chatgpt"', command)
        self.assertIn('web_search="disabled"', command)
        self.assertIn('--disable', command)
        with tempfile.TemporaryDirectory() as directory:
            ledger = APIAccountingLedger(Path(directory)/'usage.sqlite3', pilot.REPO/'assets/api-prices-2026-09-16.json')
            ledger.record('worker', 'sol-execution', 'gpt-6.1-sol', None, 'complete')
            total = ledger.summary()['total']
            self.assertEqual(total['unpriced_call_count'], 1)
            self.assertIsNone(total['api_equivalent_usd'])

    def test_fresh_execution_default_and_explicit_model_choices(self):
        for flags, expected in (([], 'gpt-6.1-sol'), (['--execution-model', 'gpt-6-sol'], 'gpt-6-sol'),
                                (['--execution-model', 'gpt-6-astra'], 'gpt-6-astra')):
            with self.subTest(flags=flags), tempfile.TemporaryDirectory() as directory:
                base = Path(directory)
                (base/'problem.txt').write_text('Synthetic question')
                (base/'problems.json').write_text(json.dumps({'problem':'problem.txt'}))
                with patch.object(sys, 'argv', ['pilot', str(base/'run'), '--problems', str(base/'problems.json'), *flags]), \
                     patch.object(pilot, 'subscription_preflight', return_value={}), \
                     patch.object(pilot.Pilot, 'run', new=AsyncMock(return_value=[])), contextlib.redirect_stdout(io.StringIO()):
                    pilot.main()
                config = json.loads((base/'run/host-config.json').read_text())
                self.assertEqual(config['parallel_route_scouts'], {'enabled':True,'width':4,'user_requested':True})
                self.assertEqual(config['model_concurrency'], 30)
                models = config['models']
                self.assertEqual(models, {'main':'gpt-6-astra','reviewers':'gpt-6-astra','execution':expected})

    def test_saved_execution_dispatch_and_legacy_absent_key_are_preserved(self):
        for config, expected in (({}, 'gpt-6-sol'), ({'models':{}}, 'gpt-6-sol'),
                ({'models':{'execution':'gpt-6-sol'}}, 'gpt-6-sol'),
                ({'models':{'execution':'gpt-6.1-sol'}}, 'gpt-6.1-sol'),
                ({'models':{'execution':'gpt-6-astra'}}, 'gpt-6-astra')):
            with self.subTest(config=config), tempfile.TemporaryDirectory() as directory:
                problem = object.__new__(pilot.Problem)
                task = {key:'bounded synthetic task' for key in ('task','context','hypotheses','advisory_hints','owned_scope','acceptance_checks')}
                task['kind'] = 'research'
                problem.current = {'sol_tasks':[task]}
                problem.active_triage = {'candidate_binding':pilot.triage_binding(problem.current),
                    'approved_research_task_hashes':[pilot.sha(pilot.encoded(task))]}
                problem.calls=[]; problem.errors=[]; problem.counter=1
                problem.pilot=SimpleNamespace(config=config,host=Path(directory),policy=lambda _: 'policy')
                before=json.dumps(config,sort_keys=True)
                with patch.object(problem,'call',new=AsyncMock(return_value=({'session_id':'worker'},{}))) as call, \
                     patch.object(problem,'probe',new=AsyncMock(return_value={'status':'not_requested'})):
                    asyncio.run(problem.execution())
                self.assertEqual(call.await_args.kwargs['model'],expected)
                self.assertEqual(json.dumps(config,sort_keys=True),before)

    def test_new_run_browsing_default_and_explicit_off(self):
        for flag, expected in (([], True), (['--internet-browse', 'off'], False)):
            with self.subTest(flag=flag), tempfile.TemporaryDirectory() as directory:
                base = Path(directory)
                (base/'problem.txt').write_text('Prove zero equals zero.')
                (base/'problems.json').write_text(json.dumps({'problem':'problem.txt'}))
                argv = ['pilot', str(base/'run'), '--problems', str(base/'problems.json'), '--codex', 'synthetic', *flag]
                with patch.object(sys, 'argv', argv), patch.object(pilot, 'subscription_preflight', return_value={}), \
                     patch.object(pilot.Pilot, 'run', new=AsyncMock(return_value=[])), contextlib.redirect_stdout(io.StringIO()):
                    pilot.main()
                self.assertIs(json.loads((base/'run/host-config.json').read_text())['internet_browse'], expected)

    def test_unavailable_worker_returns_diagnostics_and_keeps_main_probe(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            problem = object.__new__(pilot.Problem)
            task = {name:'bounded task' for name in ('task','context','hypotheses','advisory_hints','owned_scope','acceptance_checks')}
            task['kind'] = 'research'
            problem.current = {'sol_tasks':[task], 'python_probe':'print(1)'}
            problem.active_triage = {'candidate_binding': pilot.triage_binding(problem.current),
                'approved_research_task_hashes': [pilot.sha(pilot.encoded(task))]}
            problem.calls = []
            problem.errors = []
            problem.counter = 2
            problem.pilot = SimpleNamespace(config={'models':{'execution':pilot.SOL}}, host=root,
                                             policy=lambda name:'policy')
            meta = {'name':'problem/002-sol-execution','module':'sol-execution',
                    'model_requested':pilot.SOL,'status':'process_failed'}
            message = f"The '{pilot.SOL}' model is not supported when using Codex with a ChatGPT account."
            error = pilot.StageFailure(meta, [message])
            async def failed(*args, **kwargs):
                problem.calls.append(meta)
                path = root/'runtime'/meta['name']/'stage.events.jsonl'
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps({'event':{'type':'error','message':message}})+'\n')
                raise error
            with patch.object(problem, 'call', new=AsyncMock(side_effect=failed)) as call, \
                 patch.object(problem, 'probe', new=AsyncMock(return_value={'status':'completed'})) as probe:
                first = asyncio.run(problem.execution())
                second = asyncio.run(problem.execution())
                self.assertEqual(call.await_count, 1)
                self.assertEqual(probe.await_count, 2)
            for result in (first, second):
                self.assertEqual(result['workers'][0]['output']['status'], 'unavailable')
                self.assertNotIn('task_id', result['workers'][0])
                self.assertEqual(result['main_probe']['status'], 'completed')
            self.assertFalse(pilot.StageFailure(meta, [message + ' quota 429']).model_unsupported)
            meta['cli_version'] = 'codex-cli 0.153.0'
            problem.pilot.config['auth'] = {'cli_version': 'codex-cli 0.157.1'}
            self.assertIsNone(problem.execution_unavailability())
            problem.pilot.config['auth'] = {'cli_version': 'codex-cli 0.153.0'}
            self.assertEqual(problem.execution_unavailability()['status'], 'unavailable')

    def run_scenario(self, *, fail_first_scope=False, fail_grade=False, unchanged_after_failure=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'synthetic.txt'
            source.write_text('Show that zero equals zero.')
            deadline = (pilot.now() + timedelta(minutes=3)).isoformat()
            Campaign.initialize(root/'campaign', {'synthetic':source}, deadline_utc=deadline, concurrency=1, owner_key=root/'controller.key', mode='lite', require_paper=False)
            hashes = {}
            for name in pilot.POLICIES:
                content = (pilot.REPO/name).read_bytes()
                path = root/'policy'/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                hashes[name] = pilot.sha(content)
            pilot.write(root/'host-config.json', {'deadline_utc':deadline,'model_concurrency':1,'internet_browse':False,'codex_binary':'synthetic','source_url':'https://example.org/synthetic','problems':['synthetic'],'policy_hashes':hashes})
            prompts = []
            review_ids = []
            delivered_packets = []
            counts = {}
            main_id = '00000000-0000-0000-0000-000000000001'
            async def fake(root, name, prompt, model, timeout, resume_session=None, **kwargs):
                role=kwargs['module']; prompts.append((role,prompt,resume_session))
                counts[role] = counts.get(role,0) + 1
                if role.startswith('main') and unchanged_after_failure and kwargs.get('accounting_context', {}).get('purpose') == 'scientific_strategy_development':
                    runner.deadline = pilot.now()  # Synthetic explicit stop after observed continued main work.
                if role.startswith('main'):
                    tickets = runner.campaign.feedback('synthetic')['problems']['synthetic']['feedback']
                    for ticket in tickets:
                        if ticket['status']=='open' and ticket['needs_delivery']:
                            self.assertIn(ticket['fingerprint'], prompt)
                            self.assertIn(ticket['id'], prompt)
                            delivered_packets.append((ticket['id'],ticket['fingerprint'],main_id))
                sid=main_id if role.startswith('main') else f'00000000-0000-0000-0000-{len(prompts):012d}'
                if not role.startswith('main'):
                    review_ids.append(sid)
                meta={'status':'completed','session_id':sid,'name':name,'prompt_sha256':pilot.sha(prompt),'request_id':name,'model_actual':model,'model_verified':True,'fresh_session':True,'resume_session':None}
                if role.startswith('main'):
                    answer={'response_type':'candidate_update','proof_markdown':'Zero equals zero by reflexivity.','answer_statement':'Zero equals zero by reflexivity.','ledger':{'rows':[{'id':'r1','closed':True,'triaged':False,'status':'debated'}]},'assumption_census':'No additional assumptions.','remaining_gaps':[],'complete_claim':True,'prior_exposure':'none','python_probe':'','sol_tasks':[],'notes':'Synthetic proof.','required_clauses':[{'id':'c1','text':'Show equality.','source_excerpt':'zero equals zero'}]}
                    if fail_first_scope and counts.get('scope-review', 0) and not unchanged_after_failure:
                        answer['assumption_census'] += ' Scope clarification: equality is the single required clause; no omitted cases or extra premises.'
                elif role=='scope-review':
                    answer={'verdict':'PASS_FULL_SCOPE','answer_kind':'proof','coverage':[{'clause_id':'c1','root':'answer','result':'covered','explanation':'Reflexivity proves the requested equality.'}],'extra_assumptions':[],'gaps':[],'findings':{k:'Checked against the synthetic original.' for k in ('source_fidelity','clause_completeness','definitions','premises','answer_direction')}}
                    if fail_first_scope and counts[role] == 1:
                        answer['verdict']='fail'
                        answer['gaps']=['Synthetic scope finding: clause needs independent recheck.']
                elif role=='silver-review':
                    answer={'verdict':'SILVER','review_mode':'comprehensive','triaged_rows':[],'checks':{k:{'pass':True,'rationale':'Synthetic reflexivity needs no L3 certificate.'} for k in ('comprehensive_composition','theorem_face_closure','intended_model','no_open_findings','triage_complete')},'gaps':[]}
                    if fail_grade:
                        answer['verdict']='BRONZE'
                        answer['checks']['triage_complete']={'pass':False,'rationale':'Synthetic certificate is absent.'}
                        answer['gaps']=['Missing required certificate.']
                        runner.deadline=pilot.now()
                else:
                    answer={'verdict':'PASS_COMPLETE_PROOF' if role=='proof-review' else 'INCOMPLETE','gaps':[],'unresolved_findings':[],'resolved_ids':[],'triaged_rows':[],'triage_rationale':'Reflexivity.','review_markdown':'Checked reflexivity.',
                        'triage_decisions':[{'row_id':'r1','selected':False,'trigger':'none',
                            'reason':'Reflexivity is routine.', 'goal_relevance':'Exact requested equality',
                            'inference_ready':True}]}
                meta['answer_sha256'] = pilot.sha(pilot.encoded(answer))
                return meta,answer
            with patch.object(pilot,'subscription_preflight',return_value={}),patch.object(pilot,'call_stage',side_effect=fake):
                runner=pilot.Pilot(root)
                result=asyncio.run(runner.run())
            self.assertEqual(len(review_ids),len(set(review_ids)))
            self.assertNotIn(main_id,review_ids)
            partial = fail_grade or unchanged_after_failure
            self.assertEqual(result[0]['status'],'partial' if partial else 'complete', result)
            state=Campaign(root/'campaign').status()
            self.assertEqual(state['successful_complete'], not partial)
            main_prompts=[p for p in prompts if p[0].startswith('main')]
            self.assertIsNone(main_prompts[0][2])
            self.assertEqual(main_prompts[1][2],main_id)
            self.assertTrue(all(p[2] is None for p in prompts if not p[0].startswith('main')))
            review_modes = [('focused' if 'REVIEW_MODE=focused. ' in p[1] else 'comprehensive')
                            for p in prompts if p[0] == 'proof-review']
            # The completed unchanged assessment stops before another paid focused review.
            self.assertEqual(review_modes, ['focused', 'comprehensive'] * (counts['scope-review'] // 2))
            roles = [p[0] for p in prompts]
            for index, role in enumerate(roles):
                if role == 'scope-review' and roles[index - 1] != 'scope-review':
                    self.assertEqual(roles[index - 1], 'proof-review')
                    self.assertIn('REVIEW_MODE=comprehensive. ', prompts[index - 1][1])
            for role, prompt, _ in prompts:
                if role.endswith('review'):
                    self.assertIn('## Phase L3', prompt)
            all_prompts='\n'.join(p[1] for p in prompts)
            self.assertNotIn((root/'controller.key').read_bytes(), all_prompts.encode())
            self.assertFalse('"claim_token":' in all_prompts, 'Controller claim token key leaked into model prompt')
            if unchanged_after_failure:
                self.assertEqual(counts['scope-review'], 2)
                self.assertEqual(counts['proof-review'], 2)
                self.assertGreaterEqual(runner.problems['synthetic'].research_continuation_state['step'], 1)
                self.assertIn('Do actual substantive work in this turn', all_prompts)
                record = runner.problems['synthetic'].final_assessment_history[0]
                self.assertFalse(record['final_validation']['successful_complete'])
                self.assertTrue(record['final_validation']['manifest']['sha256'])
                self.assertTrue(any('Synthetic scope finding: clause needs independent recheck.' in prompt
                    for _, prompt, _ in main_prompts[1:]))
                self.assertEqual(counts.get('silver-review', 0), 0 if unchanged_after_failure else 1)
            if fail_first_scope and not unchanged_after_failure:
                self.assertEqual(counts['scope-review'],4)
                self.assertEqual(counts['proof-review'],4)
                self.assertEqual(state['problems']['synthetic'].get('repair_round', 0),0)  # Scope rejection occurs before controller grading.
                self.assertTrue(any('Synthetic scope finding: clause needs independent recheck.' in prompt
                    for _, prompt, _ in main_prompts[1:]))
                self.assertEqual(counts.get('silver-review', 0), 0 if unchanged_after_failure else 1)
                tickets=runner.campaign.feedback('synthetic')['problems']['synthetic']['feedback']
                for ident,fingerprint,task in delivered_packets:
                    ticket=next(t for t in tickets if t['id']==ident)
                    self.assertTrue(any(a['fingerprint']==fingerprint and a['task_id']==task for a in ticket['acknowledgments']))

    def test_synthetic_complete_uses_real_controller_and_fresh_reviews(self):
        self.run_scenario()

    def test_failed_scope_delivered_then_repaired_in_same_main(self):
        self.run_scenario(fail_first_scope=True)

    def test_unchanged_scope_failure_checkpoints_instead_of_review_loop(self):
        self.run_scenario(fail_first_scope=True, unchanged_after_failure=True)

    def test_failed_grade_never_successful(self):
        self.run_scenario(fail_grade=True)

    def test_prior_findings_require_explicit_resolution(self):
        gap={'id':'old-gap','severity':'gap','finding':'Missing step.','what_would_resolve':'Prove step.'}
        review=pilot.retain_findings([gap],{'unresolved_findings':[],'resolved_ids':[],'verdict':'PASS_COMPLETE_PROOF','gaps':[]})
        self.assertEqual(review['unresolved_findings'],[gap])
        self.assertFalse(pilot.proof_pass(review))
        resolved=pilot.retain_findings([gap],{'unresolved_findings':[],'resolved_ids':['old-gap'],'verdict':'PASS_COMPLETE_PROOF','gaps':[]})
        self.assertTrue(pilot.proof_pass(resolved))

if __name__=='__main__': unittest.main()
