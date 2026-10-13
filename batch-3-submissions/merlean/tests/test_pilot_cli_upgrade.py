"""Explicit executable selection never resets continuation history."""
import json
import os
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch
import test_pilot_continuation_runtime as fixtures

pilot = fixtures.pilot
continuation = fixtures.continuation

class CliUpgradeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ContinuationRuntimeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.binary = (self.fixture.fixture.base/'new-codex').resolve()
        self.binary.write_text('#!/bin/sh\nexit 0\n')
        self.binary.chmod(0o755)

    def prepare(self, preflight=None, **kwargs):
        with patch.object(continuation.os, 'kill', side_effect=ProcessLookupError), \
             patch.object(continuation.subprocess, 'run', return_value=subprocess.CompletedProcess([],0,'','')), \
             patch.object(pilot, 'subscription_preflight', side_effect=preflight or (lambda _: {'cli_version':'codex-cli 0.159.2'})):
            return pilot.prepare_continuation(self.fixture.fixture.source, self.fixture.root,
                self.fixture.fixture.receipt, codex_binary=self.binary, **kwargs)

    def test_explicit_binary_preserves_history(self):
        source=self.fixture.fixture.source
        before={str(p.relative_to(source)):p.read_bytes() for p in source.rglob('*') if p.is_file()}
        config=self.prepare()
        self.assertEqual(config['codex_binary'],str(self.binary))
        change=config['explicit_policy_changes']['codex_binary']
        self.assertEqual(change['old'],'synthetic')
        self.assertEqual(change['new_sha256'],pilot.sha(self.binary.read_bytes()))
        self.assertEqual(change['new_cli_version'],'codex-cli 0.159.2')
        self.assertEqual(before,{str(p.relative_to(source)):p.read_bytes() for p in source.rglob('*') if p.is_file()})
        self.assertTrue((self.fixture.root/'host/runtime/problem/004-main-repair/stage.meta.json').is_file())

    def test_changed_binary_fails_before_reservation(self):
        def preflight(_):
            self.binary.write_text('changed')
            return {'cli_version':'codex-cli 0.159.2'}
        with self.assertRaisesRegex(ValueError,'changed during preflight'):
            self.prepare(preflight)
        self.assertFalse(self.fixture.root.exists())
        self.assertFalse((self.fixture.fixture.source.parent/'.continuation-reservations').exists())

    def test_symlink_rejected_before_preflight(self):
        link=self.binary.with_name('alias');link.symlink_to(self.binary);self.binary=link
        with self.assertRaisesRegex(ValueError,'canonical absolute'):
            self.prepare(lambda _: self.fail('preflight called'))
        self.assertFalse(self.fixture.root.exists())

    def test_unavailability_is_version_scoped_and_history_unchanged(self):
        from types import SimpleNamespace
        problem=object.__new__(pilot.Problem)
        host=self.fixture.fixture.base/'synthetic-host'
        call={'status':'process_failed','module':'sol-execution','model_requested':pilot.SOL,'name':'problem/001-sol-execution','cli_version':'codex-cli 0.157.1'}
        problem.calls=[call]
        problem.pilot=SimpleNamespace(host=host,config={'models':{'execution':pilot.SOL},'auth':{'cli_version':'codex-cli 0.157.1'}})
        path=host/'runtime'/call['name']/'stage.events.jsonl';path.parent.mkdir(parents=True)
        path.write_text(json.dumps({'event':{'type':'error','message':f"The '{pilot.SOL}' model is not supported when using Codex with a ChatGPT account."}})+'\n')
        history=path.read_bytes();calls=json.dumps(problem.calls)
        self.assertEqual(problem.execution_unavailability()['status'],'unavailable')
        problem.pilot.config['auth']['cli_version']='codex-cli 0.159.2'
        self.assertIsNone(problem.execution_unavailability())
        self.assertEqual(json.dumps(problem.calls),calls)
        self.assertEqual(path.read_bytes(),history)
        del call['cli_version']
        self.assertEqual(problem.execution_unavailability()['status'],'unavailable')
        problem.pilot.config['auth']={}
        self.assertEqual(problem.execution_unavailability()['status'],'unavailable')

    def test_subscription_version_allowlist_remains_exact(self):
        import codex_transport as transport
        for version,allowed in [('0.153.0',True),('0.157.1',True),('0.159.2',True),('0.159.3',False)]:
            with self.subTest(version=version), patch('subprocess.run',side_effect=[
                subprocess.CompletedProcess([],0,'Logged in using ChatGPT',''),
                subprocess.CompletedProcess([],0,'codex-cli '+version+'\n','')]):
                if allowed:
                    self.assertEqual(transport.subscription_preflight('/synthetic/codex')['cli_version'],'codex-cli '+version)
                else:
                    with self.assertRaisesRegex(RuntimeError,'new boundary audit'):
                        transport.subscription_preflight('/synthetic/codex')
