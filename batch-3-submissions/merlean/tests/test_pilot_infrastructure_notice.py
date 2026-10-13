"""Infrastructure notices bind frozen host evidence, never grant acceptance."""
import asyncio
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p
import pilot_infrastructure_notice as n
import test_pilot_continuation_runtime as fixtures
from test_pilot_main_inputs import deliver_main_scope

class NoticeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = self.root / 'infrastructure-notice'; self.base.mkdir()
        files = {'saved-proof': 'a' * 64}
        self.parent = {'source_root': '/immutable-parent', 'files': files,
            'manifest_sha256': n.digest(json.dumps(files, sort_keys=True, separators=(',', ':')).encode())}
        self.config = {'continuation_parent': '/immutable-parent', 'code_hashes': {'codex_pilot.py': 'b' * 64},
            'policy_hashes': {'roles/original-problem-reviewer.md': 'c' * 64},
            'main_response_contract_version': 1, 'original_scope_review_count': 2,
            'internet_browse': False, 'models': {'main': p.ASTRA}}
        self.audit = {'status': 'PASS', 'target_code_hashes': self.config['code_hashes'],
                      'target_policy_hashes': self.config['policy_hashes']}
        self.audit_bytes = json.dumps(self.audit).encode(); (self.base/'audit.json').write_bytes(self.audit_bytes)
        self.notice = {'schema_version': 1, 'kind': 'infrastructure_migration_notice',
            'parent_source_root': self.parent['source_root'], 'parent_manifest_sha256': self.parent['manifest_sha256'],
            'target_code_hashes': self.config['code_hashes'], 'target_policy_hashes': self.config['policy_hashes'],
            'target_runtime_policy': n.policy_binding(self.config), 'changes': list(n.CHANGES),
            'evidence': [{'kind': 'current_infrastructure_audit', 'path': 'audit.json', 'sha256': n.digest(self.audit_bytes)}],
            'authority': n.AUTHORITY, 'availability': n.AVAILABILITY}
        self.freeze()

    def freeze(self):
        data = json.dumps(self.notice).encode(); (self.base/'notice.json').write_bytes(data)
        self.config['infrastructure_notice'] = {'path': 'infrastructure-notice/notice.json', 'sha256': n.digest(data)}
        (self.root/'continuation-parent.json').write_text(json.dumps(self.parent))

    def test_complete_prospective_predicate_and_no_authority(self):
        feedback = n.feedback_notice(self.root, self.config)
        self.assertEqual(feedback['receipt'], self.notice)
        self.assertEqual(feedback['host_verified_receipt'], self.config['infrastructure_notice'])
        text = feedback['prospective_changes']['scope_schema_precheck']
        for key in p.SCOPE_FINDING_KEYS | {'coverage', 'extra_assumptions', 'verification_language'}:
            self.assertIn(key, text)
        self.assertIn('No report is retroactively repaired', feedback['authority_boundary'])
        self.assertEqual(n.load_notice(self.root, {}), None)

    def test_historical_rejected_review_feedback_notice_remains_non_authoritative(self):
        self.notice['changes'] = ['rejected_review_authority_feedback']
        self.freeze()
        feedback = n.feedback_notice(self.root, self.config)
        self.assertEqual(feedback['receipt'], self.notice)
        self.assertIn('rejected, non-authoritative', feedback['prospective_changes']['rejected_review_authority_feedback'])
        self.assertIn('No report is retroactively repaired', feedback['authority_boundary'])

    def test_lossless_main_delivery_notice_is_bound_and_non_authoritative(self):
        self.notice['changes'] = ['lossless_main_task_document_delivery']
        self.freeze()
        feedback = n.feedback_notice(self.root, self.config)
        self.assertEqual(feedback['receipt'], self.notice)
        text = feedback['prospective_changes']['lossless_main_task_document_delivery']
        for required in ('Every original byte', 'current stage', 'Hash', 'original session', 'retry bound'):
            self.assertIn(required, text)
        self.assertIn('No report is retroactively repaired', feedback['authority_boundary'])

    def test_lineage_notice_does_not_grant_or_repair_historical_authority(self):
        self.notice['changes'] = ['local_module_lineage_census']
        self.freeze()
        feedback = n.feedback_notice(self.root, self.config)
        text = feedback['prospective_changes']['local_module_lineage_census']
        self.assertIn('Unknown and stale IDs still fail validation', text)
        self.assertIn('not a new mathematical claim', text)
        self.assertIn('not repaired retrospectively', text)
        self.assertEqual(feedback['receipt'], self.notice)

    def test_exact_sharing_notice_preserves_required_history_and_authority(self):
        self.notice['changes'] = ['exact_shared_main_feedback']
        self.freeze()
        feedback = n.feedback_notice(self.root, self.config)
        text = feedback['prospective_changes']['exact_shared_main_feedback']
        self.assertIn('exact inverse reconstruction', text)
        self.assertIn('does not select, summarize or make history optional', text)
        self.assertIn('all unique contents and bindings', text)
        self.assertEqual(feedback['receipt'], self.notice)

    def test_convergence_migration_notice_discloses_scheduling_and_absent_exam(self):
        self.notice['changes'] = ['candidate_focused_convergence']
        self.freeze()
        feedback = n.feedback_notice(self.root, self.config)
        self.assertEqual(feedback['receipt'], self.notice)
        text = feedback['prospective_changes']['candidate_focused_convergence']
        self.assertIn('scheduling state, not proof completeness', text)
        self.assertIn('no exam profile, competition clock or automatic deadline', text)
        self.assertIn('Concrete contrary evidence can reopen targeted exploration', text)

    def test_tampered_notice_evidence_maps_parent_and_authority_fail_closed(self):
        for change in ('notice', 'evidence', 'code', 'policy', 'runtime', 'parent', 'authority', 'extra'):
            with self.subTest(change=change):
                notice, config, parent = copy.deepcopy(self.notice), copy.deepcopy(self.config), copy.deepcopy(self.parent)
                if change == 'notice':
                    (self.base/'notice.json').write_text('{}')
                    with self.assertRaises(ValueError): n.load_notice(self.root, config)
                    self.freeze(); continue
                if change == 'evidence': notice['evidence'][0]['sha256'] = '0' * 64
                if change == 'code': config['code_hashes']['codex_pilot.py'] = '0' * 64
                if change == 'policy': config['policy_hashes']['roles/original-problem-reviewer.md'] = '0' * 64
                if change == 'runtime': config['original_scope_review_count'] = 1
                if change == 'parent': parent['files']['new'] = '0' * 64
                if change == 'authority': notice['authority'] = 'proof_pass'
                if change == 'extra': notice['accept_old_review'] = True
                with self.assertRaises(ValueError): n.validate_notice(notice, self.base, config, parent)

    def test_traversal_duplicate_reserved_and_unbound_audit_rejected(self):
        for name in ('../audit.json', '/audit.json', 'notice.json', './notice.json', './audit.json'):
            value = copy.deepcopy(self.notice); value['evidence'][0]['path'] = name
            with self.assertRaises(ValueError): n.validate_notice(value, self.base, self.config, self.parent)
        value = copy.deepcopy(self.notice); value['evidence'] *= 2
        with self.assertRaises(ValueError): n.validate_notice(value, self.base, self.config, self.parent)
        report = dict(self.audit, target_code_hashes={})
        data = json.dumps(report).encode(); (self.base/'audit.json').write_bytes(data)
        value = copy.deepcopy(self.notice); value['evidence'][0]['sha256'] = n.digest(data)
        with self.assertRaisesRegex(ValueError, 'exact target'): n.validate_notice(value, self.base, self.config, self.parent)

class NoticePreparationTests(unittest.TestCase):
    setUp = fixtures.ContinuationRuntimeTests.setUp

    def test_prepare_copies_validated_evidence_and_optional_omission(self):
        from pilot_continuation import validate_and_load
        checkpoint = self.fixture.load()
        evidence = self.root.parent / 'notice-source'; evidence.mkdir()
        code = {str(path.relative_to(p.REPO/'src')): p.sha(path.read_bytes()) for path in (p.REPO/'src').rglob('*.py')}
        policies = {name: p.sha((p.REPO/name).read_bytes()) for name in p.POLICIES}
        config = {**checkpoint['config'], 'proof_document_version':1, 'lite_local_verification_version':1, 'main_response_contract_version':1,'original_scope_review_count':2,
                  'parallel_route_scouts': {'enabled':False,'width':2,'user_requested':False},
                  'assessment_protocol_epoch':'progress-aware-admission-v1','campaign_phase':'phase1',
                  'code_hashes':code,'policy_hashes':policies,'continuation_parent':str(self.fixture.source.resolve())}
        audit = {'status':'PASS','target_code_hashes':code,'target_policy_hashes':policies}
        raw = json.dumps(audit).encode(); (evidence/'audit.json').write_bytes(raw)
        notice = {'schema_version':1,'kind':'infrastructure_migration_notice',
            'parent_source_root':str(self.fixture.source.resolve()), 'parent_manifest_sha256':checkpoint['parent']['manifest_sha256'],
            'target_code_hashes':code,'target_policy_hashes':policies,'target_runtime_policy':n.policy_binding(config),
            'changes':['scope_schema_precheck','explicit_migration_notice'],
            'evidence':[{'kind':'current_infrastructure_audit','path':'audit.json','sha256':n.digest(raw)}],
            'authority':n.AUTHORITY,'availability':n.AVAILABILITY}
        path=evidence/'source-notice.json'; path.write_text(json.dumps(notice))
        with patch('pilot_continuation.validate_and_load', return_value=checkpoint), patch.object(p,'subscription_preflight',return_value={}):
            result=p.prepare_continuation(self.fixture.source,self.root,self.fixture.receipt,infrastructure_notice=path)
        self.assertEqual(n.load_notice(self.root,result),notice)
        (evidence/'audit.json').write_text('external later changed')
        self.assertEqual(n.load_notice(self.root,result),notice)
        self.assertIn('infrastructure_notice',result['explicit_policy_changes'])
        runner = p.Pilot(self.root)
        captured = []
        async def dispatch(host, name, prompt, model, timeout, resume, **kwargs):
            spec = kwargs['document_scope']
            task = Path(spec['readonly_artifacts']['main-task']['path']).read_text()
            captured.append((task, resume))
            self.assertNotIn('LATEST FEEDBACK:\n', prompt)
            document_audit = deliver_main_scope(spec, host/'runtime'/name, name, resume)
            runner.deadline = p.now()  # Explicit synthetic stop; no-action itself no longer ends research.
            selected = checkpoint['problems']['problem']['current']
            response = {'response_type':'blocked_checkpoint', 'selected_candidate_sha256':p.sha(p.encoded(selected)),
                'checkpoint_metadata':{'reason':'No useful fresh review requested by this synthetic main'},
                'proposed_work':{'sol_tasks':[],'python_probe':'','lean_probe':'','lean_probe_rows':[]},
                'unreviewed_findings':[], 'review_request':'none'}
            return {'name':name,'module':'main-repair','status':'completed','session_id':'main-session',
                'model_actual':p.ASTRA,'model_verified':True,'prompt_sha256':p.sha(prompt),
                'request_id':'synthetic-request', 'document_audit':document_audit,
                'answer_sha256':p.sha(p.encoded(response))}, response
        with patch.object(p, 'call_stage', side_effect=dispatch), patch.object(p, 'subscription_preflight', return_value={}):
            outcomes = asyncio.run(runner.run())
        self.assertEqual(len(captured), 1)
        self.assertEqual(captured[0][1], 'main-session')
        feedback, _ = json.JSONDecoder().raw_decode(captured[0][0].split('LATEST FEEDBACK:\n', 1)[1])
        supplied = feedback['infrastructure_migration_notice']
        self.assertEqual(supplied['receipt'], notice)
        self.assertEqual(supplied['host_verified_receipt'], result['infrastructure_notice'])
        self.assertEqual(p.sha(p.encoded(supplied['receipt'])), p.sha(p.encoded(notice)))
        self.assertIn('verification_language', captured[0][0])
        self.assertIn('No report is retroactively repaired', captured[0][0])
        self.assertEqual(outcomes[0]['status'], 'partial')
        self.assertNotIn('scope-review', [c.get('module') for c in runner.problems['problem'].calls
                                        if c.get('name') not in {v['name'] for v in checkpoint['problems']['problem']['calls']}])
