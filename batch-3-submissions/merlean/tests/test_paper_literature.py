"""Guard exam-mode completion without pretending novelty or hiding dependencies."""
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from paper_writing_codex.cli import _compose_artifact_errors
from paper_writing_codex.literature import novelty_errors
from paper_writing_codex.tex_inventory import inventory_tex
from paper_writing_codex.workflow import init_compose, configure_profile, init_refine


class ExamLiteratureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.state = init_compose(self.root / 'paper-v1.tex', profile='exam')
        self.work = Path(self.state['work_dir'])
        self.output = Path(self.state['output'])
        self.output.write_text(r'\documentclass{article}\newtheorem{theorem}{Theorem}\begin{document}'
                               r'\begin{theorem}\label{t:answer}The answer follows under the stated hypotheses.\end{theorem}'
                               r'\end{document}')
        self.inventory = inventory_tex(self.output)
        statement = next(u for u in self.inventory['units'] if u['kind'] == 'statement')
        self.result = {'result_id': 'answer', 'candidate_label': 't:answer',
                       'normalized_sha256': statement['normalized_sha256'],
                       'hypothesis_surface': 'The stated hypotheses.',
                       'novelty_status': 'NOT_REQUESTED', 'priority_claim': False,
                       'novelty_evidence': 'Novelty is not requested for this exam answer.',
                       'novelty_limitations': 'Novelty was deliberately not assessed; no priority claim.'}
        (self.work / '03-literature-retrieval.md').write_text('No novelty search requested; no external result used. Full proof is supplied.')
        self.audit = {'verdict': 'PASS', 'reviewer_id': 'reader', 'writer_ids': ['writer'],
                      'candidate_source_tree_sha256': self.inventory['source_tree_sha256'],
                      'novelty_status': 'NOT_REQUESTED', 'result_ids': ['answer'],
                      'policy_record': self.ref('literature-policy.json'),
                      'retrieval_record': self.ref('03-literature-retrieval.md'),
                      'priority_claims_absent': True, 'unresolved_proof_dependencies': [],
                      'unresolved_attribution_issues': [],
                      'overlap_disposition': 'A known prior result is acknowledged without claiming originality.',
                      'findings': 'Independent reader checked all claims and all proof dependencies; none omitted.'}
        self.save_audit()

    def ref(self, name):
        return {'path': name, 'sha256': hashlib.sha256((self.work / name).read_bytes()).hexdigest()}

    def save_audit(self):
        (self.work / 'literature-audit.json').write_text(json.dumps(self.audit))
        self.result['literature_audit'] = self.ref('literature-audit.json')
        (self.work / '03-main-results.json').write_text(json.dumps({'main_results': [self.result]}))

    def errors(self):
        return novelty_errors(self.state, self.result, inventory_tex(self.output))

    def test_exam_self_contained_answer_can_finish_novelty_gate_without_search(self):
        self.assertEqual(self.errors(), [])
        issues = _compose_artifact_errors(self.state)
        self.assertFalse([e for e in issues if 'compose main' in e])
        profile = json.loads((self.work / 'writing-profile.json').read_text())
        self.assertTrue(profile['compression_required'])
        self.assertEqual(profile['polishing'], 'full')
        self.assertTrue(profile['readability_required'])
        self.assertTrue(all(g['status'] == 'pending' for n,g in self.state['gates'].items() if n != 'preflight'))

    def test_disabled_policy_cannot_be_bypassed_with_verified_novelty_label(self):
        for status in ('CLEAR', 'ADJACENT', 'COLLISION', 'UNKNOWN'):
            with self.subTest(status=status):
                self.result['novelty_status'] = status
                self.result.pop('literature_audit', None)
                self.assertTrue(self.errors())

    def test_invalid_evidence_and_real_dependencies_still_block(self):
        original = copy.deepcopy(self.audit)
        for key, value in [('priority_claims_absent', False), ('verdict', 'FAIL'),
                           ('unresolved_proof_dependencies', ['unproved imported axiom']),
                           ('unresolved_attribution_issues', ['missing known attribution']),
                           ('result_ids', ['different-result']), ('reviewer_id', ' WRITER '),
                           ('overlap_disposition', '')]:
            with self.subTest(key=key):
                self.audit = {**original, key: value}
                self.save_audit()
                self.assertTrue(self.errors())
        self.audit = original
        self.save_audit()
        self.result['priority_claim'] = True
        self.assertTrue(self.errors())

    def test_changed_manuscript_policy_and_evidence_invalidate_audit(self):
        for filename in ['paper', 'literature-policy.json', '03-literature-retrieval.md', 'literature-audit.json']:
            with self.subTest(file=filename):
                p = self.output if filename == 'paper' else self.work / filename
                before = p.read_bytes()
                p.write_bytes(before + b'\n ')
                self.assertTrue(self.errors())
                p.write_bytes(before)

    def test_disabled_not_requested_distinct_from_failed_enabled_assessment(self):
        self.result['novelty_status'] = 'NOT_ASSESSED'
        self.audit['novelty_status'] = 'NOT_ASSESSED'
        self.save_audit()
        self.assertTrue(self.errors())
        p = self.work / 'literature-policy.json'
        policy = json.loads(p.read_text()); policy['assess_novelty'] = True
        p.write_text(json.dumps(policy)); self.audit['policy_record'] = self.ref(p.name)
        self.save_audit()
        self.assertEqual(self.errors(), [])
        self.result['novelty_status'] = 'COLLISION'
        self.assertTrue(self.errors())

    def test_writer_cannot_hide_identity_recorded_in_raw_checkpoint(self):
        raw = self.work / 'raw.json'
        raw.write_text(json.dumps({'evidence': {'writer_ids': ['reader']}}))
        self.state['raw_checkpoint'] = {'manifest': str(raw), 'manifest_sha256': self.ref(raw.name)['sha256']}
        self.assertTrue(self.errors())

    def test_profile_switch_preserves_state_history_and_reopens_gates_only(self):
        p = self.work / '00-run-state.json'
        state = json.loads(p.read_text())
        for item in state['gates'].values(): item['status'] = 'pass'
        p.write_text(json.dumps(state)); before = p.read_text(); tex = self.output.read_bytes()
        change = configure_profile(p, 'standard')
        receipt = json.loads(Path(change['history']).read_text())
        self.assertEqual(receipt['previous'][p.name], before)
        updated = json.loads(p.read_text())
        self.assertEqual(updated['gates']['main-results']['status'], 'pending')
        self.assertEqual(updated['gates']['framework']['status'], 'pass')
        self.assertFalse(change['literature']['assess_novelty'])
        self.assertEqual(self.output.read_bytes(), tex)
        self.assertFalse(configure_profile(p, 'standard')['changed'])

    def test_invalid_profile_no_side_effects_and_refine_support(self):
        p = self.root / 'untouched.tex'
        with self.assertRaises(ValueError): init_compose(p, profile='invalid')
        self.assertFalse(p.exists())
        source = self.root / 'source.tex'; source.write_text(self.output.read_text())
        refined = init_refine(source, profile='exam')
        self.assertTrue(json.loads((Path(refined['work_dir'])/'writing-profile.json').read_text())['readability_required'])


if __name__ == '__main__': unittest.main()
