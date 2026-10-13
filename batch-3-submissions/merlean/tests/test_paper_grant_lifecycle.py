"""Real controller transitions preserve claim history without blocking paper ownership."""
import asyncio
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from campaign import Campaign
from campaign_watchdog import CampaignWatchdog
import test_campaign as campaign_fixtures


class PaperGrantLifecycleTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = self.root / 'input.txt'
        source.write_text('Synthetic lifecycle question.')
        self.c = Campaign.initialize(self.root / 'campaign', {'p': source},
            deadline_utc=None, concurrency=1, owner_key=self.root / 'controller.key')
        self.w = CampaignWatchdog(self.c, self.root / 'host/watchdog.json')

    def finish_partial(self, owner='research-host'):
        token = self.c.claim('p', owner)
        self.c.release('p', token)
        (self.c.root / 'problems/p/partial.txt').write_text('Unresolved synthetic work.')
        self.c.finish('p', partial='partial.txt')
        return token

    def register(self):
        return self.w.register_paper_task('p', asyncio.current_task(), lambda: 'exam-paper-handoff')

    def stage(self, grant):
        return {'name': 'p/host', 'problem': 'p', 'status': 'host_work',
                'ownership_scope': 'exam_paper', 'phase': 'exam-paper-handoff',
                'paper_claim_token': grant}

    def assert_stale(self, stage, **kwargs):
        report = self.w.inspect([stage], **kwargs)
        self.assertIn('stale_ownership', {i['kind'] for i in report['current_incidents']})
        self.assertFalse(report['observations'][0]['ownership_matches'])

    async def test_real_partial_release_finish_grants_and_inspects_without_erasing_history(self):
        token = self.finish_partial()
        before = self.c.status()
        grant = self.register()
        report = self.w.inspect([self.stage(grant)])
        self.assertEqual(report['current_incidents'], [])
        self.assertTrue(report['observations'][0]['ownership_matches'])
        after = self.c.status()
        self.assertEqual(after['events'], before['events'])
        self.assertEqual(after['problems']['p'], before['problems']['p'])
        self.assertEqual(after['problems']['p']['claim_token'], token)
        self.assertEqual(after['problems']['p']['owner'], 'research-host')
        self.assertFalse(after['problems']['p']['successful_complete'])
        self.assertNotEqual(grant, token)
        # The historical research token never authorizes an active research stage.
        research = {'name': 'p/main', 'problem': 'p', 'status': 'host_work', 'claim_token': token}
        self.assert_stale(research)
        self.assert_stale({**self.stage(grant), 'paper_claim_token': token})

    async def test_nonterminal_states_require_release_reconciliation_and_finish(self):
        with self.assertRaisesRegex(ValueError, 'released terminal'):
            self.register()  # pending
        token = self.c.claim('p', 'research-host')
        with self.assertRaisesRegex(ValueError, 'released terminal'):
            self.register()  # running
        self.c.release('p', token, interrupted=True)
        with self.assertRaisesRegex(ValueError, 'released terminal'):
            self.register()  # reconcile_required
        self.c.reconcile('p', token, 'Synthetic host verified all owned work has stopped.')
        with self.assertRaisesRegex(ValueError, 'released terminal'):
            self.register()  # released, not finished
        (self.c.root / 'problems/p/partial.txt').write_text('Unresolved synthetic work.')
        self.c.finish('p', partial='partial.txt')
        self.assertTrue(self.w.inspect([self.stage(self.register())])['observations'][0]['ownership_matches'])

    async def test_reopen_reclaim_and_refinish_invalidates_old_grant(self):
        first = self.finish_partial()
        stage = self.stage(self.register())
        self.c.reopen('p', reason='Synthetic new research generation.')
        self.assert_stale(stage)
        second = self.c.claim('p', 'next-host')
        self.assertNotEqual(first, second)
        self.assert_stale(stage)
        self.c.release('p', second, interrupted=True)
        self.assert_stale(stage)
        self.c.reconcile('p', second, 'Synthetic host verified all owned work has stopped.')
        self.c.finish('p', partial='partial.txt')
        self.assert_stale(stage)  # Same partial artifact cannot revive the old grant.
        self.w.revoke_paper_task('p', stage['paper_claim_token'])
        self.assertTrue(self.w.inspect([self.stage(self.register())])['observations'][0]['ownership_matches'])

    async def test_grant_binding_rejects_owner_token_generation_and_evidence_changes(self):
        self.finish_partial()
        stage = self.stage(self.register())
        for field, value in [('owner', 'different-owner'), ('claim_token', 'different-token'),
                             ('repair_round', 10), ('artifact', {'path': 'other', 'sha256': 'changed'}),
                             ('answer_sha256', 'different-answer')]:
            with self.subTest(field=field):
                # Adversarial controller-state perturbation; no acceptance gate is patched.
                with self.c.transaction() as (_, state):
                    original = json.loads(json.dumps(state['problems']['p']))
                    state['problems']['p'][field] = value
                self.assert_stale(stage)
                with self.c.transaction() as (_, state):
                    state['problems']['p'] = original

    async def test_grants_remain_task_local_revocable_and_nonrestartable(self):
        self.finish_partial()
        other = asyncio.create_task(asyncio.sleep(0))
        with self.assertRaisesRegex(ValueError, 'current retained host task'):
            self.w.register_paper_task('p', other, lambda: 'exam-paper-handoff')
        await other
        grant = self.register()
        stage = self.stage(grant)
        with self.assertRaisesRegex(ValueError, 'already registered'):
            self.register()
        self.assert_stale(stage, restarting=True)
        self.assert_stale({**stage, 'paper_claim_token': 'forged'})
        self.assert_stale({**stage, 'phase': 'research-running'})
        self.assert_stale({**stage, 'name': 'p/main'})
        self.w.revoke_paper_task('p', grant)
        self.assert_stale(stage)
        async def finish_task():
            return self.register()
        completed = asyncio.create_task(finish_task())
        ended_grant = await completed
        self.assertTrue(completed.done())
        self.assert_stale(self.stage(ended_grant))

    async def test_child_identity_and_deadline_checks_still_apply(self):
        self.finish_partial()
        stage = {**self.stage(self.register()), 'name': 'p/paper-001-reconstruct',
                 'status': 'running', 'pid': 1234, 'process_identity': 'synthetic',
                 'deadline_utc': (datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat()}
        with patch('campaign_watchdog.probe_process', return_value={'alive': True, 'identity_match': False}):
            report = self.w.inspect([stage])
        kinds = {i['kind'] for i in report['current_incidents']}
        self.assertIn('stage_deadline', kinds)
        self.assertIn('process_identity_unverified', kinds)
        self.assertNotIn('stale_ownership', kinds)


class CompletePaperGrantLifecycleTests(unittest.IsolatedAsyncioTestCase):
    # Reuse the controller's existing synthetic manifest fixture. Scope review is
    # stubbed exactly as in its controller tests; refresh/finish are real, and no
    # successful_complete flag or grade is manufactured by this lifecycle test.
    setUp = campaign_fixtures.CampaignTests.setUp
    tearDown = campaign_fixtures.CampaignTests.tearDown
    write = campaign_fixtures.CampaignTests.write
    fixture = campaign_fixtures.CampaignTests.fixture

    async def test_real_complete_transition_preserves_historical_claim_for_paper(self):
        self.fixture()
        token = self.c.claim('q1', 'research-host')
        self.c.release('q1', token)
        with patch('campaign.audit_original_scope', return_value=[]):
            self.c.finish('q1', manifest='manifest.json')
            before = self.c.status()
            self.assertEqual(before['problems']['q1']['status'], 'complete')
            self.assertEqual(before['problems']['q1']['claim_token'], token)
            watch = CampaignWatchdog(self.c, self.base / 'host/watchdog.json')
            grant = watch.register_paper_task('q1', asyncio.current_task(), lambda: 'exam-paper-handoff')
            report = watch.inspect([{'name': 'q1/host', 'problem': 'q1', 'status': 'host_work',
                'ownership_scope': 'exam_paper', 'phase': 'exam-paper-handoff', 'paper_claim_token': grant}])
            self.assertTrue(report['observations'][0]['ownership_matches'])
            self.assertNotIn('stale_ownership', {i['kind'] for i in report['current_incidents']})
            self.assertEqual(self.c.status()['problems']['q1'], before['problems']['q1'])
            self.assertEqual(self.c.status()['events'], before['events'])


if __name__ == '__main__':
    unittest.main()
