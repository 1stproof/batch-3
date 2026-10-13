"""Malformed procedural gate syntax uses bounded protocol recovery, never acceptance."""
import asyncio
import copy
import unittest
from unittest.mock import AsyncMock
import test_pilot_final_progression as fixtures
from test_pilot_review_recovery import restore_packet
import codex_pilot as p
import json

class GateSchemaTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.FinalProgressionTests(); self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.x = self.f.x
        self.x.findings = [self.f.finding('scope', kind='certificate', row_id='composition')]

    def disposition(self, **fields):
        return self.f.disposition('scope', 'downstream_obligation',
            no_mathematical_or_certificate_claim=True,
            row_association_explanation='Final scope audit is a workflow requirement', **fields)

    def test_missing_nonstring_unknown_wrong_enum_and_conflicting_gate_rejected(self):
        fields = ({'obligation': 'final_scope_acceptance'}, {}, {'gate': None}, {'gate': []},
                  {'gate': {}}, {'gate': 1}, {'gate': 'unknown'}, {'gate': 'proof_review_dispatch'},
                  {'gate': 'final_scope_acceptance', 'obligation': 'silver_acceptance'})
        for f in fields:
            with self.subTest(fields=f), self.assertRaisesRegex(ValueError, 'canonical gate:string'):
                p.finding_projection(self.x.findings,
                    self.f.review(finding_dispositions=[self.disposition(**f)]), self.x.current, {})

    def test_actual_shape_retries_fresh_without_publishing_invalid_authority(self):
        invalid = self.f.review(finding_dispositions=[self.disposition(obligation='final_scope_acceptance')])
        valid = self.f.review(finding_dispositions=[self.disposition(gate='final_scope_acceptance')])
        before = copy.deepcopy(invalid); calls=[]
        async def call(role, instruction, **kwargs):
            calls.append(instruction)
            if len(calls) == 1: return self.f.meta('invalid'), invalid
            self.assertIsNone(self.x.active_triage)
            self.assertEqual(self.x.findings[0]['severity'], 'gap')
            return self.f.meta('fresh'), valid
        self.x.call = call
        _, effective = asyncio.run(self.x.review_candidate('comprehensive'))
        self.assertEqual(len(calls), 2)
        self.assertEqual(invalid, before)
        packet = restore_packet(json.loads(calls[1].split('EXACT REVIEW INPUTS (lossless supplied-text bindings):\n')[1]))
        diagnostic = packet['invalid_prior_response_not_authority']
        self.assertEqual(diagnostic['invalid_review'], invalid)
        self.assertIn('canonical gate:string', diagnostic['error'])
        self.assertEqual(effective['resolved_ids'], [])
        self.assertIn('still_required', effective['finding_accountability']['dispositions'][0]['authority'])
        self.assertEqual(self.x.active_triage['receipt']['session_id'], 'fresh')
        self.assertIn('"gate":"final_scope_acceptance"', calls[0])

    def test_second_malformed_response_stops_without_authorization(self):
        invalid = self.f.review(finding_dispositions=[self.disposition(obligation='final_scope_acceptance')])
        self.x.call = AsyncMock(side_effect=[(self.f.meta('one'), invalid), (self.f.meta('two'), invalid)])
        with self.assertRaisesRegex(ValueError, 'canonical gate:string'):
            asyncio.run(self.x.review_candidate('comprehensive'))
        self.assertEqual(self.x.call.await_count, 2)
        self.assertIsNone(self.x.active_triage)
        self.assertEqual(self.x.triage_history, [])
        self.assertEqual(len(list(self.x.folder.glob('*invalid-*.json'))), 2)

    def test_valid_syntax_never_overrides_substantive_or_receipt_requirements(self):
        for mutation in ({'candidate_sha256': 'stale'}, {'no_mathematical_or_certificate_claim': False},
                         {'direct_consumers': ['composition']}, {'evidence': ''}):
            disposition = self.disposition(gate='final_scope_acceptance') | mutation
            effective = p.finding_projection(self.x.findings,
                self.f.review(finding_dispositions=[disposition]), self.x.current, {})
            self.assertFalse(effective['finding_accountability']['complete'])
            self.assertFalse(p.proof_pass(effective))
        disposition = self.disposition(gate='proof_review_dispatch') | {'status': 'pending_host_gate'}
        effective = p.finding_projection(self.x.findings,
            self.f.review(finding_dispositions=[disposition]), self.x.current, {})
        self.assertFalse(p.proof_pass(effective))

if __name__ == '__main__': unittest.main()
