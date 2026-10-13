"""Exact evidence packaging stays bounded without relying on omitted reviewer inputs."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import test_pilot_review_handoff as handoff_fixtures


class ContextPackagingTests(unittest.TestCase):
    def saved(self):
        return {'current': {'proof_markdown': 'Full exact current proof', 'ledger': {'rows': []}},
                'findings': [{'id': 'current-gap', 'finding': 'Exact required current feedback'}],
                'errors': [], 'calls': [], 'dossier': {}, 'main_session': 'same-main',
                'reviewer_history': [{'stage': 'q/008-proof-review', 'status': 'completed',
                    'output': {'verdict': 'INCOMPLETE', 'gaps': ['Exact reviewer gap']}}],
                'execution_history': []}

    def test_large_history_latest_numeric_failures_and_source_preserved(self):
        saved = self.saved()
        for n in range(20):
            saved['execution_history'].append({'historical_stage': f'q/{n:03}-sol-execution',
                'status': 'completed', 'output': {'history': str(n) + 'old distinct text ' * 10000}})
        saved['execution_history'] += [
            {'historical_probe': 'probes/main-10-lean', 'result': {'status': 'completed', 'stdout': 'latest successful result'},
             'artifacts': {'source.lean': {'text': 'exact latest source', 'sha256': pilot.sha('exact latest source')},
                           'result.json': {'text': json.dumps({'status': 'completed', 'stdout': 'latest successful result'}), 'sha256': 'original-result-hash'},
                           'unique-log.txt': {'text': 'UNIQUE INTERRUPTED DIAGNOSTIC', 'sha256': 'loghash'}}},
            {'historical_probe': 'probes/main-9-lean', 'result': {'status': 'failed', 'stderr': 'exact prior failed diagnostic'},
             'artifacts': {'source.lean': {'text': 'exact failed source', 'sha256': pilot.sha('exact failed source')}}}]
        before = copy.deepcopy(saved)
        packet = pilot.continuation_context(saved, {'path': 'checkpoint.json', 'sha256': 'immutable'}, 'q')
        self.assertEqual(saved, before)
        self.assertEqual(packet['saved_current'], saved['current'])
        self.assertEqual(packet['open_findings'], saved['findings'])
        self.assertEqual(packet['latest_historical_reviewers'][0]['evidence'], saved['reviewer_history'][0])
        body = pilot.encoded(packet)
        for exact in ('latest successful result', 'exact prior failed diagnostic', 'exact latest source', 'exact failed source'):
            self.assertIn(exact, body)
        self.assertIn('same_supplied_content_as', body)
        self.assertIn('UNIQUE INTERRUPTED DIAGNOSTIC', body)
        self.assertIn('original-main archive_request v1 channel', body)
        self.assertIn('other entries are unavailable', body)
        self.assertIn('do not certify the current candidate', body)
        self.assertGreater(len(pilot.encoded(saved).encode()), 1_048_576)
        self.assertGreater(len(body.encode()), 0)
        index = packet['history_manifest']['entries']
        entry = next(e for e in index if e['checkpoint_pointer'] == '/problems/q/execution_history/0')
        self.assertEqual(entry['sha256'], pilot.sha(pilot.encoded(saved['execution_history'][0])))
        self.assertEqual(entry['encoded_bytes'], len(pilot.encoded(saved['execution_history'][0]).encode()))

    def test_latest_rejection_remains_visible_after_newer_completed_review(self):
        saved = self.saved()
        saved['reviewer_history'][0].update(protocol_status='invalid_not_authority',
            invalid_protocol_diagnostics=[{'diagnostic': {'error': 'exact rejected-review reason'}}])
        saved['reviewer_history'].append({'stage': 'q/009-proof-review', 'status': 'completed',
            'protocol_status': 'not_revalidated', 'output': {'verdict': 'PASS_COMPLETE_PROOF'}})
        before = copy.deepcopy(saved)
        packet = pilot.continuation_context(saved, {'path': 'checkpoint.json', 'sha256': 'immutable'}, 'q')
        self.assertEqual([x['checkpoint_index'] for x in packet['latest_historical_reviewers']], [0, 1])
        self.assertEqual(packet['latest_historical_reviewers'][0]['evidence'], saved['reviewer_history'][0])
        self.assertIn('not_revalidated', packet['review_authority_instruction'])
        self.assertIn('NO finding resolution', packet['review_authority_instruction'])
        self.assertEqual(saved, before)

    def test_protocol_rejection_and_transport_failure_have_separate_latest_evidence(self):
        saved = self.saved()
        rejected = {'stage': 'q/253-proof-review', 'status': 'completed',
            'protocol_status': 'invalid_not_authority',
            'output': {'verdict': 'PASS_COMPLETE_PROOF'},
            'invalid_protocol_diagnostics': [{'diagnostic': {'error': 'exact rejection253'}}]}
        completed = {'stage': 'q/286-proof-review', 'status': 'completed',
            'protocol_status': 'not_revalidated', 'output': {'verdict': 'INCOMPLETE'}}
        failed = {'stage': 'q/287-proof-review', 'status': 'timeout_censored',
            'protocol_status': 'not_revalidated', 'output': None}
        for history, expected in (([rejected, completed, failed], [253, 287]),
                                  ([rejected, failed, dict(completed, stage='q/288-proof-review')], [253, 287, 288])):
            with self.subTest(expected=expected):
                saved['reviewer_history'] = history
                before = copy.deepcopy(saved)
                packet = pilot.continuation_context(saved, {'path': 'checkpoint.json', 'sha256': 'immutable'}, 'q')
                supplied = [x['evidence'] for x in packet['latest_historical_reviewers']]
                self.assertEqual([int(x['stage'].split('/')[1].split('-')[0]) for x in supplied], expected)
                self.assertEqual(supplied[0], rejected)
                self.assertIn('NO finding resolution', packet['review_authority_instruction'])
                self.assertEqual(saved, before)

    def test_prompt_compaction_preserves_values_and_durable_hash_serialization(self):
        value = {'text': ' spaces  and\nnewlines\tUnicode α ', 'nested': [{'n': 1, 'v': None}],
                 'literal': '[Exact supplied text: text-0]'}
        durable = pilot.encoded(value)
        compact = pilot.prompt_encoded(value)
        self.assertEqual(json.loads(compact), value)
        self.assertLess(len(compact.encode()), len(durable.encode()))
        self.assertEqual(pilot.encoded(value), durable)
        self.assertEqual(durable, json.dumps(value, ensure_ascii=False, indent=2) + '\n')

    def test_actual_review_packet_roundtrip_across_all_sections(self):
        fixture = handoff_fixtures.ReviewHandoffTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        problem = fixture.problem
        shared = 'Exact shared source and diagnostics\n' * 50
        problem.dossier = {'claim': shared}
        problem.current = {'proof_markdown': shared, 'ledger': {'rows': []}}
        problem.findings = [{'id': 'f', 'severity': 'gap', 'finding': shared,
                             'what_would_resolve': 'Supply missing inference'}]
        problem.triage_history = [{'authorization': False, 'reason': shared, 'decisions': []}]
        problem.execution_history = [{'stdout': shared, 'other': 'distinct source'}]
        expected = {'host_local_module_evidence_sha256': {}, 'local_verification_modules': [], 'exact_dossier': problem.dossier, 'exact_candidate': problem.current,
                    'prior_findings': problem.findings, 'advisory_route_portfolios': [],
                    'host_candidate_sha256': pilot.sha(pilot.encoded(problem.current)),
                    'finding_history': [{'sha256': pilot.sha(pilot.encoded(problem.findings[0])),
                                         'finding': problem.findings[0]}],
                    'preacceptance_scope_assessments': [],
                    'prior_triage_reassess_independently': problem.triage_history,
                    'actual_execution_evidence': problem.execution_history, 'advisory_scope_history': []}
        before = copy.deepcopy(expected)
        problem.call = AsyncMock(side_effect=RuntimeError('capture before dispatch'))
        with self.assertRaisesRegex(RuntimeError, 'capture before dispatch'):
            asyncio.run(problem.review_candidate('focused'))
        prompt = problem.call.call_args.args[1]
        packed = json.loads(prompt.split('EXACT REVIEW INPUTS (lossless supplied-text bindings):\n', 1)[1])
        from test_pilot_review_recovery import restore_packet
        restored = restore_packet(packed)
        self.assertEqual(restored, before)
        self.assertEqual(expected, before)
        self.assertIn('CURRENT LEDGER ROW IDS', prompt)

    def test_final_scope_and_silver_packets_roundtrip_every_field(self):
        fixture = handoff_fixtures.ReviewHandoffTests()
        fixture.setUp(); self.addCleanup(fixture.doCleanups)
        x = fixture.problem
        shared = 'Exact repeated proof/source α with whitespace  \n' * 100
        x.current['proof_markdown'] = x.current['answer_statement'] + shared
        x.current['ledger']['rows'] = [{'id': 'r', 'evidence': shared,
            'premise_manifest_data': {'premises': [], 'source': shared}}]
        serialized = pilot.encoded({'source': shared, 'nested': {'unknown': None, 'number': 3}})
        x.execution_history = [{'source': shared, 'diagnostics': serialized,
                                'distinct': 'Unique retained diagnostic'}]
        raw_proof = {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [],
                     'review_mode': 'comprehensive', 'review_markdown': shared,
                     'exact_serialized_artifact': serialized}
        x.active_triage = {'candidate_binding': pilot.triage_binding(x.current),
            'review_mode': 'comprehensive', 'selected_rows': [], 'receipt': {'session_id': 'proof'}}
        captured = {}; packed_inputs = []
        real_pack = pilot.review_inputs
        def packing(value):
            packed_inputs.append(copy.deepcopy(value))
            return real_pack(value)
        scope_calls = []
        async def call(role, instruction, **kwargs):
            captured[role] = instruction
            if role == 'scope-review':
                scope_calls.append(instruction)
            return fixture.meta(role + str(len(scope_calls)) if role == 'scope-review' else role), (
                dict(handoff_fixtures.scope_report(), findings={k: shared + serialized for k in pilot.SCOPE_FINDING_KEYS})
                if role == 'scope-review' else {'verdict': 'INCOMPLETE', 'gaps': [shared]})
        def replace_pointer(target, pointer, value):
            keys = [k.replace('~1', '/').replace('~0', '~') for k in pointer.split('/')[1:]]
            for key in keys[:-1]:
                target = target[int(key)] if isinstance(target, list) else target[key]
            target[int(keys[-1]) if isinstance(target, list) else keys[-1]] = value
        def restore(packet):
            from pilot_review_inputs import restore_review_packet
            if isinstance(packet, dict) and 'review_packet_codec' in packet:
                packet = restore_review_packet(packet)
            from review_packet_codec import restore_schema_inputs
            if isinstance(packet, dict) and 'schema_codec' in packet:
                packet = restore_schema_inputs(packet)
            if 'supplied_texts' in packet:
                evidence = copy.deepcopy(packet['evidence'])
                for binding in packet['bindings']:
                    replace_pointer(evidence, binding['pointer'], packet['supplied_texts'][binding['supplied_text']])
                packet = evidence
            if 'serialization_bindings' in packet:
                evidence = packet['review_inputs']
                for binding in packet['serialization_bindings']:
                    spec = packet['serializations'][binding['serialization_index']]
                    value = json.dumps(spec['json_value'], ensure_ascii=spec['ensure_ascii'],
                                       indent=spec['indent']) + spec['trailing_text']
                    replace_pointer(evidence, binding['pointer'], value)
                packet = evidence
            return packet
        x.call = call
        before = copy.deepcopy(x.current)
        with patch.object(pilot, 'review_inputs', side_effect=packing), patch('original_scope.audit_original_scope', return_value=[]):
            asyncio.run(x.validate_candidate(fixture.meta('proof'), raw_proof))
        expected_keys = [
            {'host_metadata', 'prior_proof_review', 'original_descriptor', 'root_interface', 'final_artifact'},
            {'host_metadata', 'candidate_and_ledger', 'execution_evidence', 'local_verification_modules', 'local_module_reassessments', 'prior_proof_review', 'scope_reviews'}]
        for index, role in enumerate(('scope-review', 'silver-review')):
            packed = captured[role].split('EXACT FINAL REVIEW INPUTS (lossless supplied-text bindings):\n')[1]
            restored = restore(json.loads(packed))
            self.assertEqual(restored, packed_inputs[index])
            self.assertEqual(set(restored), expected_keys[index])
            for ref in restored['host_metadata']['artifact_references'].values():
                if isinstance(ref, dict) and 'path' in ref:
                    self.assertEqual(pilot.sha((x.folder / ref['path']).read_bytes()), ref['sha256'])
            self.assertEqual(restored['prior_proof_review']['substantive_review'], raw_proof)
            self.assertLess(len(packed.encode()), len(pilot.encoded(restored).encode()))
        self.assertEqual(x.current, before)
        self.assertEqual(packed_inputs[1]['execution_evidence'], x.execution_history)
        self.assertEqual(packed_inputs[0]['final_artifact'], x.current['proof_markdown'])
        self.assertEqual(packed_inputs[1]['scope_reviews'][0]['verdict'], 'PASS_FULL_SCOPE')

    def test_required_current_input_is_never_truncated(self):
        saved = self.saved()
        saved['current']['proof_markdown'] = 'Required exact proof ' * 50000
        packet = pilot.continuation_context(saved, {'path': 'checkpoint.json', 'sha256': 'immutable'}, 'q')
        self.assertIn(saved['current']['proof_markdown'], pilot.encoded(packet))

    def test_lossless_reviewer_encoding_roundtrips_every_distinct_byte_string(self):
        source = 'theorem exact : True := by trivial\n' * 3000
        diagnostics = 'failed: exact original diagnostic\n' * 1000
        value = [{'source': source, 'result': {'stdout': diagnostics, 'source': source},
                  'artifacts': {'source.lean': {'text': source}, 'stdout.txt': {'text': diagnostics}},
                  'distinct': 'KEEP THIS DIFFERENT SOURCE\n' * 500}]
        packed = pilot.lossless_evidence(value)
        restored = copy.deepcopy(packed['evidence'])
        for binding in packed['bindings']:
            tokens = [part.replace('~1', '/').replace('~0', '~') for part in binding['pointer'].split('/')[1:]]
            current = restored
            for token in tokens[:-1]:
                current = current[int(token)] if isinstance(current, list) else current[token]
            key = int(tokens[-1]) if isinstance(current, list) else tokens[-1]
            current[key] = packed['supplied_texts'][binding['supplied_text']]
        self.assertEqual(restored, value)
        self.assertLess(len(pilot.encoded(packed)), len(pilot.encoded(value)) / 2)
        self.assertIn('no external access', packed['encoding'])

    def test_serialized_artifact_packing_is_exact_and_keeps_noncanonical_text(self):
        source = 'theorem exact : True := by trivial\n' * 200
        artifact = {'source': source, 'stdout': 'α diagnostics\n' * 100}
        value = {'a/b~c': [json.dumps(artifact, ensure_ascii=False, indent=2) + '\n'],
                 'actual': artifact, 'noncanonical': json.dumps(artifact, indent=3),
                 'marker': '[Exact serialized JSON artifact 0]'}
        before = copy.deepcopy(value)
        packed = pilot.review_inputs(value)
        restored = copy.deepcopy(packed.get('evidence', packed))
        def put(target, pointer, value):
            keys = [k.replace('~1', '/').replace('~0', '~') for k in pointer.split('/')[1:]]
            for key in keys[:-1]:
                target = target[int(key)] if isinstance(target, list) else target[key]
            target[int(keys[-1]) if isinstance(target, list) else keys[-1]] = value
        for binding in packed.get('bindings', []):
            put(restored, binding['pointer'], packed['supplied_texts'][binding['supplied_text']])
        self.assertIn('serialization_bindings', restored)
        for binding in restored['serialization_bindings']:
            spec = restored['serializations'][binding['serialization_index']]
            original = json.dumps(spec['json_value'], ensure_ascii=spec['ensure_ascii'], indent=spec['indent']) + spec['trailing_text']
            put(restored['review_inputs'], binding['pointer'], original)
        self.assertEqual(restored['review_inputs'], before)
        self.assertEqual(value, before)
        self.assertLess(len(pilot.prompt_encoded(packed)), len(pilot.prompt_encoded(value)))

    def test_string_review_answer_persistence_stays_json(self):
        fixture = handoff_fixtures.ReviewHandoffTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        problem = fixture.problem
        problem.pilot.semaphore = asyncio.Semaphore(1)
        problem.pilot.remaining = lambda: 1800
        problem.pilot.config = {'internet_browse': False, 'codex_binary': 'unused'}
        problem.pilot.host = fixture.folder / 'host'
        problem.statement = 'Exact original'
        problem.status = Mock()
        problem.calls = []
        answer = 'invalid review: exact string'
        async def run():
            with patch.object(pilot, 'call_stage', new=AsyncMock(return_value=(fixture.meta('fresh-review'), answer))):
                await problem._call_once('proof-review', 'review', model=pilot.ASTRA, resume=False, timeout=600)
        asyncio.run(run())
        self.assertEqual(json.loads((problem.folder / '008-proof-review.json').read_text()), answer)

    def test_large_prompt_reaches_transport_with_complete_required_input(self):
        fixture = handoff_fixtures.ReviewHandoffTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        problem = fixture.problem
        problem.pilot.semaphore = asyncio.Semaphore(1)
        problem.pilot.remaining = lambda: 1800
        problem.pilot.config = {'internet_browse': False, 'codex_binary': 'unused'}
        problem.pilot.host = fixture.folder/'host'
        problem.statement = 'Exact original'
        problem.status = Mock()
        problem.calls = []
        instruction = 'Exact required input ' * 60000
        async def run():
            with patch.object(pilot, 'call_stage', new=AsyncMock(return_value=(fixture.meta('fresh-review'), {}))) as dispatch:
                await problem._call_once('proof-review', instruction, model=pilot.ASTRA, resume=False, timeout=600)
                dispatch.assert_awaited_once()
                self.assertIn(instruction, dispatch.call_args.args[2])
                self.assertGreater(len(dispatch.call_args.args[2].encode()), 1_000_000)
        asyncio.run(run())
        self.assertEqual(instruction, 'Exact required input ' * 60000)

    def test_complete_main_prompt_with_real_policies_preserves_current_inputs(self):
        fixture = handoff_fixtures.ReviewHandoffTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        problem = fixture.problem
        saved = self.saved()
        saved['execution_history'] = [{'historical_stage': f'q/{n:03}-sol-execution',
            'status': 'completed', 'output': {'exact': str(n) + 'old evidence ' * 12000}} for n in range(20)]
        packet = pilot.continuation_context(saved, {'path': 'checkpoint.json', 'sha256': 'immutable'}, 'q')
        problem.pilot.semaphore = asyncio.Semaphore(1)
        problem.pilot.remaining = lambda: 1800
        problem.pilot.config = {'internet_browse': False, 'codex_binary': 'unused'}
        problem.pilot.host = fixture.folder/'host'
        problem.pilot.policy = lambda path: (pilot.REPO/path).read_text()
        problem.statement = 'Exact original question'
        problem.status = Mock()
        problem.calls = []
        async def run():
            with patch.object(pilot, 'call_stage', new=AsyncMock(return_value=(fixture.meta('actual-main'), {}))) as dispatch:
                await problem._call_once('main-repair', pilot.encoded(packet), model=pilot.ASTRA, resume=True, timeout=1800)
                prompt = dispatch.call_args.args[2]
                self.assertGreater(len(prompt.encode('utf-8')), 0)
                self.assertIn('Full exact current proof', prompt)
                self.assertIn('Exact required current feedback', prompt)
                self.assertIn('Exact reviewer gap', prompt)
                self.assertIn('Exact original question', prompt)
                self.assertEqual(dispatch.call_args.args[5], 'actual-main')
        asyncio.run(run())
