import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from original_scope import audit_original_scope, scope_checked_view
from research_grade import audit_manifest
from plan_store.offline_store import OfflinePlanGraph


class OriginalScopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.signature = 'theorem answer : ¬ (∀ n : ℕ, n = 0)'
        self.root = {'name': 'answer', 'signature': self.signature,
                     'signature_sha256': self.digest(self.signature),
                     'lean_file': self.write('Proof.lean', self.signature + ' := by\n  intro h\n  have := h 1\n  omega\n'),
                     'definitions': []}
        self.original = {'input_kind': 'natural_language', 'source_kind': 'user_request',
                         'origin': 'user-request:initial-question',
                         'source': self.write('request.txt', 'Decide whether every natural number equals zero.'),
                         'statement': 'Decide whether every natural number equals zero.',
                         'required_clauses': [{'id': 'all-n', 'text': 'Decide the universal assertion for all naturals.',
                                              'source_excerpt': 'every natural number equals zero'}],
                         'unresolved_conflicts': []}
        self.target = {'target_signature': self.signature, 'plan_statement_id': 'answer'}
        self.manifest = {'grade': 'SILVER', 'manifest_author': 'submitter',
                         'implementers': ['proof-worker'], 'provider': 'codex', 'question_status': 'settled',
                         'original_problem': self.write('original.json', self.original),
                         'target_contract': self.write('target.json', self.target)}
        self.report = {'verdict': 'PASS_FULL_SCOPE', 'reviewer': 'independent-reviewer',
                       'implementer': 'proof-worker', 'implementers': ['proof-worker'],
                       'original_problem_sha256': self.manifest['original_problem']['sha256'],
                       'target_contract_sha256': self.manifest['target_contract']['sha256'],
                       'roots': [self.root], 'extra_assumptions': [], 'gaps': [],
                       'answer_kind': 'counterexample',
                       'coverage': [{'clause_id': 'all-n', 'root': 'answer', 'result': 'covered',
                                     'explanation': 'The witness one refutes the entire universal statement.'}],
                       'findings': {key: 'Independently checked this required semantic comparison.' for key in
                                    ['source_fidelity', 'clause_completeness', 'definitions', 'premises', 'answer_direction']}}
        self.provenance = {'provider': 'codex', 'model_family': 'astra', 'model': 'gpt-6-astra',
                           'reviewer': 'independent-reviewer', 'task_id': 'review-task', 'role': 'original_scope_review'}
        self.report['review_input_sha256'] = self.digest('synthetic immutable scope inputs')
        self.provenance.update(review_input_sha256=self.report['review_input_sha256'],
                               prompt_sha256=self.digest('synthetic identical scope prompt'))
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.refresh()

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def digest(text):
        return hashlib.sha256(text.encode()).hexdigest()

    def write(self, name, value):
        text = json.dumps(value, ensure_ascii=False, indent=2) if isinstance(value, (list, dict)) else value
        (self.base / name).parent.mkdir(parents=True, exist_ok=True)
        (self.base / name).write_text(text)
        return {'path': name, 'sha256': self.digest(text)}

    def refresh(self):
        self.report['proof_snapshot_sha256'] = self.digest(json.dumps(self.report['roots'], sort_keys=True, separators=(',', ':')))
        self.manifest['original_scope_audit'] = self.write('review.json', self.report)
        # Two independent synthetic actors review the same test interface. Test
        # mutations are intentionally applied to both fixture reports, never to
        # production evidence or persisted historical reviews.
        second = copy.deepcopy(self.report)
        second['reviewer'] = 'second-independent-reviewer'
        receipt = dict(self.provenance, reviewer=second['reviewer'], task_id='second-review-task')
        second['reviewer_provenance'] = self.write('second-dispatch.json', receipt)
        self.manifest['original_scope_audits'] = [self.manifest['original_scope_audit'], self.write('second-review.json', second)]

        self.manifest_ref = self.write('manifest.json', self.manifest)

    def errors(self):
        self.refresh()
        return audit_manifest(self.manifest, self.base)

    def test_full_finite_counterexample_can_pass_lite_scope_without_git_commit(self):
        self.assertEqual(self.errors(), [])

    def test_missing_audit_blocks_lite_and_heavy(self):
        for grade in ['BRONZE', 'SILVER', 'GOLD']:
            self.manifest['grade'] = grade
            self.manifest.pop('original_scope_audit', None)
            self.manifest.pop('original_scope_audits', None)
            self.assertTrue(any('ORIGINAL_SCOPE' in e for e in audit_manifest(self.manifest, self.base)))

    def test_author_or_any_implementation_worker_cannot_review(self):
        for reviewer in [' SUBMITTER ', 'PROOF-WORKER']:
            self.report['reviewer'] = reviewer
            self.assertTrue(any('INDEPENDENCE' in e for e in self.errors()))

    def test_failed_uncertain_empty_and_partial_clause_audits_fail(self):
        for verdict in ['FAIL_SCOPE', 'NEEDS_CLARIFICATION', 'passed', None]:
            self.report['verdict'] = verdict
            self.assertTrue(self.errors())
        self.report['verdict'] = 'PASS_FULL_SCOPE'
        self.report['coverage'] = []
        self.assertTrue(any('COVERAGE' in e for e in self.errors()))
        self.original['required_clauses'] = []
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.assertTrue(any('CENSUS' in e for e in self.errors()))

    def test_stale_original_target_main_source_and_report_fail(self):
        for name in ['request.txt', 'original.json', 'target.json', 'Proof.lean', 'review.json']:
            path = self.base / name
            before = path.read_bytes()
            path.write_bytes(before + b'\nchanged')
            self.assertTrue(audit_manifest(self.manifest, self.base), name)
            path.write_bytes(before)

    def test_narrowed_selected_theorem_cannot_replay_full_review(self):
        target = dict(self.target, target_signature='theorem only_zero : (0 : ℕ) = 0')
        self.manifest['target_contract'] = self.write('target.json', target)
        self.assertTrue(any('STALE' in e or 'TARGET' in e for e in self.errors()))
        self.report['target_contract_sha256'] = self.manifest['target_contract']['sha256']
        self.assertTrue(any('TARGET' in e for e in self.errors()))

    def test_extra_premises_and_unresolved_mixed_conflicts_block(self):
        self.report['extra_assumptions'] = ['Assume the omitted original conclusion.']
        self.assertTrue(any('INCOMPLETE' in e for e in self.errors()))
        self.report['extra_assumptions'] = []
        self.original['unresolved_conflicts'] = ['Natural language and Lean domains disagree.']
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.assertTrue(any('CONFLICT' in e for e in self.errors()))

    def test_local_lemma_grade_is_allowed_but_cli_reports_original_not_certified(self):
        self.manifest = {'grade': 'SILVER', 'question_status': 'interface_lemma'}
        self.assertEqual(audit_manifest(self.manifest, self.base), [])
        self.write('manifest.json', self.manifest)
        run = subprocess.run([sys.executable, str(ROOT / 'scripts/audit_research_grade.py'), str(self.base / 'manifest.json')], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn('NOT CERTIFIED', run.stdout)

    def test_real_cli_rejects_missing_scope_and_accepts_reviewed_counterexample(self):
        command = [sys.executable, str(ROOT / 'scripts/audit_research_grade.py'), str(self.base / 'manifest.json')]
        good = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        self.manifest.pop('original_scope_audit')
        self.manifest.pop('original_scope_audits')
        self.write('manifest.json', self.manifest)
        bad = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn('ORIGINAL_SCOPE', bad.stdout)

    def test_plan_crud_cannot_claim_settled_without_audit_and_masks_stale_claim(self):
        graph = OfflinePlanGraph(self.base / 'plan')
        node = {'id': 'answer', 'type': 'Theorem', 'name': 'answer', 'content': 'Original answer',
                'dependencies': [], 'hierarchy_level': 0, 'anchor': self.signature, 'question_status': 'settled'}
        with self.assertRaisesRegex(ValueError, 'ORIGINAL_SCOPE'):
            graph.add(node)
        node['original_scope_manifest'] = dict(self.manifest_ref, path=str(self.base / 'manifest.json'))
        graph.add(node)
        self.assertEqual(graph.get('answer')['original_scope_status'], 'passed')
        (self.base / 'Proof.lean').write_text('changed proof bytes')
        self.assertEqual(graph.get('answer')['question_status'], 'scope_review_required')
        self.assertEqual(graph.topo_sorted()[0]['question_status'], 'scope_review_required')
        exported, _ = graph.export()
        self.assertFalse(exported['statements'][0]['submission_eligible'])
        with self.assertRaisesRegex(ValueError, 'ORIGINAL_SCOPE'):
            graph.update('answer', content='Try to keep stale completion')

    def test_scope_view_preserves_live_node_mutation_for_receipt_reconciliation(self):
        graph = OfflinePlanGraph(self.base / 'live-plan')
        node = {'id': 'answer', 'type': 'Theorem', 'anchor': self.signature, 'question_status': 'settled',
                'original_scope_manifest': dict(self.manifest_ref, path=str(self.base / 'manifest.json'))}
        graph.add(node)
        graph.get('answer')['anchor'] += ' '
        self.assertEqual(graph._nodes['answer']['anchor'], self.signature + ' ')
        self.assertEqual(graph.get('answer')['original_scope_status'], 'blocked')
        # The blocked projection must not erase the originally stored historical claim.
        self.assertEqual(graph._nodes['answer']['question_status'], 'settled')

    def test_online_plan_store_uses_same_completion_and_stale_view_gate(self):
        import types
        import importlib.util
        import plan_store
        memory = Mock()
        memory.get_all.return_value = {'results': []}
        memory.add.return_value = {'results': [{'id': 'memory-answer'}]}
        fake_config = types.SimpleNamespace(SCOPE='scope-test', get_plan_memory=lambda _: memory)
        spec = importlib.util.spec_from_file_location('plan_store._scope_test_store', ROOT / 'src/plan_store/store.py')
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'plan_store.config': fake_config}), patch.object(plan_store, 'config', fake_config, create=True):
            spec.loader.exec_module(module)
        graph = module.PlanGraph(self.base / 'online-plan')
        node = {'id': 'answer', 'type': 'Theorem', 'name': 'answer', 'content': 'Original answer',
                'dependencies': [], 'hierarchy_level': 0, 'anchor': self.signature,
                'question_status': 'settled', 'claim_scope': 'full_original'}
        with self.assertRaisesRegex(ValueError, 'ORIGINAL_SCOPE'):
            graph.add(node)
        node['original_scope_manifest'] = dict(self.manifest_ref, path=str(self.base / 'manifest.json'))
        graph.add(node)
        (self.base / 'Proof.lean').write_text('stale root source')
        for result in [graph.get('answer'), graph.all()[0], graph.topo_sorted()[0]]:
            self.assertEqual(result['question_status'], 'scope_review_required')
            self.assertNotEqual(result['claim_scope'], 'full_original')
        with self.assertRaisesRegex(ValueError, 'ORIGINAL_SCOPE'):
            graph.update('answer', submission_eligible=True)

    def test_namespaced_roots_and_originals_bind_correct_namespace(self):
        self.root['name'] = 'Actual.answer'
        self.root['lean_file'] = self.write('Proof.lean', 'namespace Actual\n' + self.signature + ' := by sorry\nend Actual\n')
        self.report['coverage'][0]['root'] = 'Actual.answer'
        self.assertEqual(self.errors(), [])
        self.root['name'] = 'Wrong.answer'
        self.report['coverage'][0]['root'] = 'Wrong.answer'
        self.assertTrue(any('INTERFACE' in e for e in self.errors()))

    def test_whitespace_inside_string_literals_is_never_type_normalized_away(self):
        self.attach_lean('lean')
        original_signature = 'theorem requested : "a b" = "ab"'
        source = self.write('original.lean', original_signature + ' := by sorry\n')
        self.original.update(source=source, statement=original_signature)
        self.original['required_clauses'][0]['source_excerpt'] = original_signature
        self.original['lean_target'].update(signature=original_signature, source=source)
        self.signature = 'theorem answer : "ab" = "ab"'
        self.root.update(signature=self.signature, signature_sha256=self.digest(self.signature),
                         lean_file=self.write('Proof.lean', self.signature + ' := by rfl\n'))
        self.target['target_signature'] = self.signature
        self.manifest['target_contract'] = self.write('target.json', self.target)
        self.report['target_contract_sha256'] = self.manifest['target_contract']['sha256']
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.report['lean_comparison'].update(original_signature_sha256=self.digest(original_signature),
                                               target_signature_sha256=self.digest(self.signature))
        self.assertTrue(any('exact type' in e for e in self.errors()))

    def test_provider_specific_review_model_is_required(self):
        for wrong in ['gpt-5.6-sol', 'gpt-5.5']:
            self.provenance['model'] = wrong
            self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
            self.assertTrue(any('REVIEWER_MODEL' in e for e in self.errors()))
        self.manifest['provider'] = 'claude'
        self.provenance.update(provider='claude', model_family='fable', model='host-resolved-fable')
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.assertEqual(self.errors(), [])
        self.provenance['model'] = 'claude-opus'
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.assertTrue(any('REVIEWER_MODEL' in e for e in self.errors()))

    def test_gold_cannot_hide_coverage_or_bridge_roots_outside_live_kernel_census(self):
        self.manifest['grade'] = 'GOLD'
        self.manifest['kernel_evidence'] = self.write('kernel.json', {'root_declarations': []})
        self.manifest['theorem_faces'] = []
        self.assertTrue(any('KERNEL_BINDING' in e for e in self.errors()))
        root = dict(self.root, signature_hash=self.root['signature_sha256'])
        self.manifest['kernel_evidence'] = self.write('nested/kernel.json', {'root_declarations': [root]})
        self.manifest['theorem_faces'] = [{'lean_decl': 'answer', 'covered': True}]
        self.assertFalse(any('ORIGINAL_SCOPE_KERNEL_BINDING' in e for e in self.errors()))
        root['signature_hash'] = 'a' * 64
        self.manifest['kernel_evidence'] = self.write('nested/kernel.json', {'root_declarations': [root]})
        self.assertTrue(any('KERNEL_BINDING' in e for e in self.errors()))

    def test_self_authored_challenge_and_string_or_comment_declarations_block(self):
        self.original['source_kind'] = 'self_authored_comparator'
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.assertTrue(any('SOURCE' in e for e in self.errors()))
        self.original['source_kind'] = 'user_request'
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        for fake in ['def spoof : String := "' + self.signature + ' := by trivial"', '/- ' + self.signature + ' := by trivial -/']:
            self.root['lean_file'] = self.write('Proof.lean', fake)
            self.assertTrue(any('INTERFACE' in e for e in self.errors()))

    def test_short_original_statement_and_toolchain_are_valid(self):
        self.original['statement'] = '证明 1+1=2'
        self.original['source'] = self.write('request.txt', '证明 1+1=2')
        self.original['required_clauses'] = [{'id': 'all-n', 'text': '1+1=2', 'source_excerpt': '1+1=2'}]
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.signature = 'theorem answer : (1 : ℕ) + 1 = 2'
        self.root.update(signature=self.signature, signature_sha256=self.digest(self.signature),
                         lean_file=self.write('Proof.lean', self.signature + ' := by decide\n'))
        self.target['target_signature'] = self.signature
        self.manifest['target_contract'] = self.write('target.json', self.target)
        self.report['target_contract_sha256'] = self.manifest['target_contract']['sha256']
        self.report['answer_kind'] = 'proof'
        self.report['coverage'][0]['explanation'] = 'The theorem directly establishes the original arithmetic equality.'
        self.assertEqual(self.errors(), [])
        # Restore the counterexample interface for the independent Lean-input version check.
        self.signature = 'theorem answer : ¬ (∀ n : ℕ, n = 0)'
        self.root.update(signature=self.signature, signature_sha256=self.digest(self.signature),
                         lean_file=self.write('Proof.lean', self.signature + ' := by sorry\n'))
        self.target['target_signature'] = self.signature
        self.manifest['target_contract'] = self.write('target.json', self.target)
        self.report['target_contract_sha256'] = self.manifest['target_contract']['sha256']
        self.attach_lean('lean')
        self.original['lean_target']['toolchain'] = 'v4.34.0'
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.assertEqual(self.errors(), [])

    def attach_lean(self, kind):
        signature = 'theorem requested : ¬ (∀ n : ℕ, n = 0)'
        # Original frozen pasted Lean is an independent snapshot, not our selected root.
        source = self.write('original.lean', signature + ' := by sorry\n')
        self.original.update(input_kind=kind, source=source, statement=signature,
                             required_clauses=[{'id': 'all-n', 'text': 'Decide the full original universal proposition.', 'source_excerpt': signature}])
        if kind == 'mixed':
            self.original['natural_language'] = {'source': self.write('mixed-request.txt', 'Refute the assertion that all natural numbers equal zero.'),
                                                  'statement': 'Refute the assertion that all natural numbers equal zero.'}
            self.report['findings']['mixed_consistency'] = 'The natural-language refutation request and the Lean negation have identical domains and quantifiers.'
        self.original['lean_target'] = {'declaration': 'requested', 'signature': signature, 'source': source,
                                        'definitions': [], 'toolchain': 'leanprover/lean4:v4.34.0-rc1',
                                        'imports': [{'module': 'Mathlib', 'revision': 'a' * 40}]}
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.report['lean_comparison'] = {'mode': 'exact_type', 'original_signature_sha256': self.digest(signature), 'target_signature_sha256': self.digest(self.signature)}

    def test_user_lean_and_mixed_originals_use_exact_type_not_natural_language_only(self):
        for kind in ['lean', 'mixed']:
            self.attach_lean(kind)
            self.assertEqual(self.errors(), [], kind)
        self.report['lean_comparison']['original_signature_sha256'] = 'b' * 64
        self.assertTrue(any('LEAN' in e for e in self.errors()))

    def test_mixed_original_cannot_drop_or_modify_the_natural_language_request(self):
        self.attach_lean('mixed')
        self.assertEqual(self.errors(), [])
        (self.base / 'mixed-request.txt').write_text('A different and strictly stronger original task.')
        self.assertTrue(self.errors())
        self.original.pop('natural_language')
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.assertTrue(any('MIXED' in e for e in self.errors()))

    def test_lean_original_narrowing_and_unverified_bridge_fail(self):
        self.attach_lean('lean')
        self.original['lean_target']['signature'] = 'theorem requested : True'
        source = self.write('original.lean', 'theorem requested : True := by trivial\n')
        self.original.update(source=source, statement='theorem requested : True')
        self.original['lean_target']['source'] = source
        self.original['required_clauses'][0]['source_excerpt'] = 'theorem requested : True'
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
        self.report['lean_comparison']['original_signature_sha256'] = self.digest('theorem requested : True')
        self.assertTrue(any('exact type' in e for e in self.errors()))
        self.report['lean_comparison']['mode'] = 'checked_bridge'
        self.report['lean_comparison']['bridge_root'] = 'answer'
        self.assertTrue(any('bridge' in e for e in self.errors()))

if __name__ == '__main__':
    unittest.main()
