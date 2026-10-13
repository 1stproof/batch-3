import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_evidence_status as e
import pilot_convergence as c


class EvidenceStatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.problem = self.root / 'run/campaign/problems/example'
        self.problem.mkdir(parents=True)
        self.candidate = {'proof_markdown': 'PRIVATE SCIENTIFIC BODY', 'answer_statement': 'Statement', 'ledger': {'rows': []}}
        self.state = c.update_convergence(None, original_sha256='a'*64, candidate=self.candidate)
        self.store = c.ConvergenceStore(self.problem)
        self.store.save(self.state)
        self.write('host-progress.json', {'calls': [{'name': '1-main', 'status': 'completed', 'document_audit': {'required_material_delivered': True}, 'private': 'SECRET'}]})
        self.write('review-exhaustion.json', [])
        self.write('research-continuation-state.json', {'step': 1, 'unchanged_binding_steps': 1, 'bindings': {'candidate_sha256': c.digest(self.candidate)}})

    def write(self, name, value):
        (self.problem / name).write_text(json.dumps(value))

    def test_real_store_compact_report_deterministic_no_payload_or_authority(self):
        before = {str(p): p.read_bytes() for p in self.problem.rglob('*') if p.is_file()}
        a = e.report(self.problem); self.assertEqual(a, e.report(self.problem))
        self.assertEqual(a['status'], 'RECORDED_STATE_SUMMARIZED')
        self.assertEqual(a['dimensions']['convergence']['distinct_archived_candidate_bindings'], 1)
        self.assertFalse(a['dimensions']['convergence']['acceptance_inferred'])
        self.assertNotIn('PRIVATE', json.dumps(a)); self.assertNotIn('SECRET', json.dumps(a))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.problem.rglob('*') if p.is_file()})

    def test_useful_unchanged_plateau_does_not_close_gaps_or_prevent_later_change(self):
        state = self.state
        for i in range(30):
            work = dict(objective='Investigate', approach='Check', work_performed=str(i), result='Retained work', next_step='Continue', failed_approaches=[])
            state = c.update_convergence(state, original_sha256='a'*64, candidate=self.candidate, research_work=work)
        self.store.save(state)
        report = e.report(self.problem)['dimensions']['convergence']
        self.assertEqual(report['retained_research_records'], 30)
        self.assertEqual(report['distinct_archived_candidate_bindings'], 1)
        self.assertEqual(report['current_recorded_deficit_statuses']['mathematical'], 'unknown')
        changed = {**self.candidate, 'proof_markdown': 'Genuine additional argument'}
        state = c.update_convergence(state, original_sha256='a'*64, candidate=changed)
        self.store.save(state)
        self.assertEqual(e.report(self.problem)['dimensions']['convergence']['distinct_archived_candidate_bindings'], 2)
        self.assertFalse(e.report(self.problem)['recorded_candidate_bindings_agree'])

    def test_transport_delivery_and_exhaustion_do_not_establish_review_or_comprehension(self):
        self.write('host-progress.json', {'calls': [
            {'name': 'a', 'status': 'timeout_censored', 'document_audit': {'required_material_delivered': True}, 'model_context_claim': 'truncated'},
            {'name': 'b', 'status': 'process_failed'}, {'name': 'c', 'status': 'cancelled'}]})
        self.write('review-exhaustion.json', [{'id': 'b'*64, 'required_material_delivered': True}])
        a = e.report(self.problem)
        self.assertEqual(a['dimensions']['activity']['recorded_status_counts']['timeout'], 1)
        self.assertEqual(a['dimensions']['activity']['required_material_delivery_receipts']['recorded_true'], 1)
        self.assertEqual(a['dimensions']['convergence']['current_recorded_observation_refs'], {})
        self.assertFalse(a['dimensions']['exhaustion']['mathematical_rejection_inferred'])
        self.assertIn('comprehension', a['semantics']['delivery'])

    def test_missing_invalid_capped_and_duplicate_records_are_unknown_not_zero(self):
        (self.problem / 'host-progress.json').unlink()
        self.assertIsNone(e.report(self.problem)['dimensions']['activity'])
        for calls in [False, {}, [{'name': 'a'}, {'name': 'a'}], [{'name': {'SECRET': 'data'}}]]:
            self.write('host-progress.json', {'calls': calls})
            self.assertIsNone(e.report(self.problem)['dimensions']['activity'])
        self.write('research-continuation-state.json', {'step': True})
        self.assertIsNone(e.report(self.problem)['dimensions']['continuation'])
        with patch.object(e, 'MAX_BYTES', 8):
            self.assertEqual(e.report(self.problem)['status'], 'PARTIAL_OR_INCONSISTENT')

    def test_malformed_status_never_leaks_payload(self):
        self.write('host-progress.json', {'calls': [{'name': 'a', 'status': {'SECRET': 'text'}, 'document_audit': {'required_material_delivered': 'SECRET'}}]})
        a = e.report(self.problem)
        self.assertEqual(a['dimensions']['activity']['recorded_status_counts']['unknown'], 1)
        self.assertNotIn('SECRET', json.dumps(a))

    def test_record_tamper_and_unsafe_manifest_references_fail_closed(self):
        pointer = json.loads((self.problem/'research-convergence.json').read_text())
        manifest = json.loads((self.problem/'convergence-archive'/f"{pointer['state_sha256']}.json").read_text())
        ref = manifest['state']['candidates'][c.digest(self.candidate)]['record_sha256']
        path = self.problem/'convergence-archive/records'/f'{ref}.json'
        path.write_text('{}')
        self.assertIsNone(e.report(self.problem)['dimensions']['convergence'])
        self.write('research-convergence.json', {'state_sha256': '../SECRET'})
        self.assertIsNone(e.report(self.problem)['dimensions']['convergence'])

    def test_symlink_fifo_and_parent_alias_refused(self):
        target = self.problem/'host-progress.json'; target.unlink(); os.mkfifo(target)
        self.assertIsNone(e.report(self.problem)['dimensions']['activity'])
        target.unlink(); target.symlink_to(self.root/'absent')
        self.assertIsNone(e.report(self.problem)['dimensions']['activity'])
        alias = self.root/'alias'; alias.symlink_to(self.problem, target_is_directory=True)
        with self.assertRaises(ValueError): e.report(alias)
        with self.assertRaises(ValueError): e.main(['--problem', str(self.problem), '--output', str(alias/'report.json')])

    def test_cli_exclusive_external_output_and_run_containment(self):
        for output in [self.problem/'report.json', self.root/'run/report.json']:
            with self.assertRaises(SystemExit): e.main(['--problem', str(self.problem), '--output', str(output)])
        output = self.root/'report.json'
        e.main(['--problem', str(self.problem), '--output', str(output)])
        self.assertTrue(output.is_file())
        with self.assertRaises(FileExistsError): e.main(['--problem', str(self.problem), '--output', str(output)])

    def test_malformed_archive_entries_are_unknown_not_retained_work(self):
        for table in ('candidates', 'observations', 'research_archive', 'auxiliary_archive'):
            for invalid in ({'bad': False}, {'e'*64: False}, {'e'*64: {'record_sha256': '../bad'}}):
                state = copy.deepcopy(self.state)
                state[table].update(invalid)
                self.write('research-convergence.json', state)
                self.assertIsNone(e.report(self.problem)['dimensions']['convergence'])
        self.store.save(self.state)
        pointer = json.loads((self.problem/'research-convergence.json').read_text())
        path = self.problem/'convergence-archive'/f"{pointer['state_sha256']}.json"
        manifest = json.loads(path.read_text())
        manifest['state']['research_archive'] = {'f'*64: False}
        path.write_text(json.dumps(manifest))
        self.assertIsNone(e.report(self.problem)['dimensions']['convergence'])

    def test_snapshot_growth_is_partial_not_silent_success(self):
        original = e.snapshot
        def changed(path, limit):
            raw, receipt = original(path, limit)
            if path.name == 'host-progress.json': receipt['grew'] = True
            return raw, receipt
        with patch.object(e, 'snapshot', changed):
            self.assertIsNone(e.report(self.problem)['dimensions']['activity'])


if __name__ == '__main__': unittest.main()
