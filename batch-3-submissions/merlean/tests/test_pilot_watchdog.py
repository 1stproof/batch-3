"""Host lifecycle tests: synthetic work only, no model or benchmark calls."""
import asyncio
from datetime import timedelta
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
from campaign import Campaign


class PilotWatchdogTests(unittest.TestCase):
    def prepare(self, root, enabled=True, minutes=2):
        source = root/'question.txt'
        source.write_text('Prove 0 = 0.')
        end = (pilot.now()+timedelta(minutes=minutes)).isoformat()
        Campaign.initialize(root/'campaign', {'p': source}, deadline_utc=end,
                            concurrency=1, owner_key=root/'controller.key', require_paper=False)
        data = Path(pilot.__file__).read_bytes()
        (root/'code').mkdir()
        (root/'code/codex_pilot.py').write_bytes(data)
        pilot.write(root/'host-config.json', {'deadline_utc':end, 'problems':['p'],
            'model_concurrency':1, 'codex_binary':'synthetic', 'internet_browse':False,
            'watchdog_enabled':enabled, 'watchdog_interval_seconds':0.01,
            'code_hashes':{'codex_pilot.py':pilot.sha(data)}})
        return pilot.Pilot(root)

    def test_deadline_config_cannot_extend_frozen_campaign(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); self.prepare(root)
            config=json.loads((root/'host-config.json').read_text())
            config['deadline_utc']=(pilot.now()+timedelta(days=1)).isoformat()
            pilot.write(root/'host-config.json', config)
            with self.assertRaisesRegex(ValueError,'deadline'):
                pilot.Pilot(root)

    def test_changed_code_snapshot_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); self.prepare(root)
            (root/'code/codex_pilot.py').write_text('changed')
            with self.assertRaisesRegex(ValueError,'source changed'):
                pilot.Pilot(root)

    def test_watchdog_cancel_drains_once_then_banks_partial(self):
        async def scenario(root):
            runner=self.prepare(root)
            stopped=asyncio.Event(); counts={'cancels':0}
            async def main_turn(problem, instruction, dossier=False):
                try:
                    await asyncio.Event().wait()
                except asyncio.CancelledError:
                    counts['cancels']+=1
                    await asyncio.sleep(.05)
                    stopped.set()
                    raise
            def inspect(watchdog, stages, **kwargs):
                return {'current_incidents':[{'kind':'stage_deadline','problem':'p',
                        'stage':'p/host','action':'cancel_owned_task'}]}
            with patch.object(pilot, 'subscription_preflight', return_value={}), \
                 patch.object(pilot.Pilot, 'policy', return_value='Synthetic policy'), \
                 patch.object(pilot.Problem, 'main_turn', main_turn), \
                 patch('campaign_watchdog.CampaignWatchdog.inspect', inspect):
                results=await asyncio.wait_for(runner.run(), 2)
            self.assertTrue(stopped.is_set())
            self.assertEqual(counts['cancels'],1)
            self.assertEqual(results[0]['status'],'partial')
            self.assertEqual(runner.campaign.status()['problems']['p']['status'],'partial')
            self.assertTrue((root/'campaign/problems/p/partial.md').is_file())
            self.assertIn('HostCancellation',(root/'campaign/problems/p/partial.md').read_text())
        with tempfile.TemporaryDirectory() as directory:
            asyncio.run(scenario(Path(directory)))

    def test_normal_run_does_not_create_watchdog(self):
        async def scenario(root):
            runner=self.prepare(root, enabled=False)
            with patch.object(pilot, 'subscription_preflight', return_value={}), \
                 patch.object(pilot.Pilot, 'policy', side_effect=RuntimeError('synthetic stop')), \
                 patch('campaign_watchdog.CampaignWatchdog') as watchdog:
                result=await runner.run()
            watchdog.assert_not_called()
            self.assertEqual(result[0]['status'],'partial')
        with tempfile.TemporaryDirectory() as directory:
            asyncio.run(scenario(Path(directory)))

    def test_capacity_wait_is_classified_without_resetting_deadline(self):
        async def scenario(root):
            runner=self.prepare(root)
            problem=pilot.Problem(runner,'p')
            problem.token=runner.campaign.claim('p','host')
            problem.phase='capacity-wait:main-repair'
            problem.failure_kind='capacity'; problem.consecutive_failures=3
            runner.problems={'p':problem}; runner.tasks={'p':asyncio.current_task()}
            stage=runner.watchdog_snapshot()[0]
            self.assertEqual(stage['status'],'backoff')
            self.assertEqual(stage['failure_kind'],'capacity')
            self.assertEqual(stage['consecutive_failures'],3)
            self.assertEqual(stage['deadline_utc'],runner.config['deadline_utc'])
        with tempfile.TemporaryDirectory() as directory:
            asyncio.run(scenario(Path(directory)))

    def test_native_carried_complete_paper_survives_multiple_watchdog_intervals(self):
        import types
        import campaign_watchdog as watchdog
        import threading
        async def scenario(root):
            runner=self.prepare(root)
            cell={'status':'complete','successful_complete':True,'manifest':'synthetic.json',
                  'sha256':'synthetic-manifest','answer_sha256':'synthetic-answer','claim_token':None}
            with runner.campaign.transaction() as (_,state):
                state['problems']['p'].update(cell)
            runner.config['carried_complete_problems']={'p':{k:cell[k] for k in ('manifest','sha256','answer_sha256')}}
            reports=[]
            owner_thread=threading.get_ident()
            async def dispatch(problem):
                # The initial host handoff is observed before any child metadata.
                await asyncio.sleep(.025)
                name='p/paper-004-reconstruct';problem.active_stage=name
                pilot.write(runner.host/'runtime'/name/'stage.meta.json',{
                    'name':name,'status':'running','pid':12345,'process_identity':'synthetic',
                    'start_utc':pilot.now().isoformat(),'timeout_seconds':60})
                await asyncio.sleep(.055)  # More than five configured watchdog intervals.
                problem.active_stage=None
                return {'status':'polished','terminal':True,'polishing_complete':True}
            runner.exam=types.SimpleNamespace(dispatch=dispatch)
            original=watchdog.CampaignWatchdog.inspect
            def inspect(instance, stages, **kwargs):
                self.assertEqual(threading.get_ident(),owner_thread,
                    'grant/phase ownership must be inspected atomically on the host event loop')
                report=original(instance,stages,**kwargs);reports.append(report);return report
            with patch.object(Campaign,'_refresh'), patch.object(runner.campaign,'seal'), \
                 patch.object(pilot,'subscription_preflight',return_value={}), \
                 patch('pilot_paper.prepare_exam_fallback'), \
                 patch.object(pilot.Problem,'restore_checkpoint',return_value={'preserved':True}), \
                 patch.object(pilot.Problem,'main_turn',side_effect=AssertionError('research replay')), \
                 patch.object(runner.campaign,'claim',side_effect=AssertionError('research reclaim')), \
                 patch.object(watchdog,'probe_process',return_value={'alive':True,'identity_match':True}), \
                 patch.object(watchdog.CampaignWatchdog,'inspect',inspect):
                result=await runner.run()
            self.assertGreaterEqual(len(reports),4)
            self.assertFalse(any(r['current_incidents'] for r in reports))
            self.assertTrue(any(o['health']=='host_work' for r in reports for o in r['observations']))
            self.assertTrue(any(o['health']=='running_within_deadline' for r in reports for o in r['observations']))
            self.assertEqual(result[0]['paper']['status'],'polished')
            self.assertEqual(runner.watchdog._paper_grants,{})
            self.assertIsNone(runner.problems['p'].paper_claim_token)
        with tempfile.TemporaryDirectory() as directory:
            asyncio.run(scenario(Path(directory)))

    def test_paper_grant_missing_forged_changed_revoked_and_deadline(self):
        from campaign_watchdog import CampaignWatchdog
        async def scenario(root):
            runner=self.prepare(root, minutes=60)
            cell={'status':'partial','claim_token':None,'manifest':None,'sha256':None,'answer_sha256':None}
            with runner.campaign.transaction() as (_,state): state['problems']['p'].update(cell)
            watch=CampaignWatchdog(runner.campaign,runner.host/'test-watchdog.json')
            stage={'name':'p/paper-004-reconstruct','problem':'p','status':'running',
                   'phase':'exam-paper-handoff','ownership_scope':'exam_paper','paper_claim_token':'forged','pid':123,
                   'process_identity':'synthetic','deadline_utc':(pilot.now()+timedelta(seconds=900)).isoformat()}
            def kinds(**kwargs):return {i['kind'] for i in watch.inspect([stage],**kwargs)['current_incidents']}
            with patch.object(Campaign,'_refresh'), patch('campaign_watchdog.probe_process',return_value={'alive':True,'identity_match':True}):
                self.assertIn('stale_ownership',kinds())
                phase=['exam-paper-handoff']
                token=watch.register_paper_task('p',asyncio.current_task(),lambda:phase[0]);stage['paper_claim_token']=token
                self.assertEqual(kinds(now_utc=pilot.now()+timedelta(seconds=301)),set())
                self.assertIn('stage_deadline',kinds(now_utc=pilot.now()+timedelta(seconds=901)))
                self.assertIn('stale_ownership',kinds(restarting=True))
                phase[0]='running:main-repair'
                self.assertIn('stale_ownership',kinds())  # Snapshot still claims a paper phase.
                phase[0]='exam-paper-handoff'
                stage['problem']='other';self.assertIn('unknown_problem',kinds());stage['problem']='p'
                stage['name']='p/main';self.assertIn('stale_ownership',kinds());stage['name']='p/paper-004-reconstruct'
                with runner.campaign.transaction() as (_,state):state['problems']['p']['answer_sha256']='changed'
                self.assertIn('stale_ownership',kinds())
                watch.revoke_paper_task('p',token);self.assertIn('stale_ownership',kinds())
                with runner.campaign.transaction() as (_,state):state['problems']['p']['answer_sha256']=None
                async def short_task():
                    return watch.register_paper_task('p',asyncio.current_task(),lambda:'exam-paper-handoff')
                task=asyncio.create_task(short_task());stage['paper_claim_token']=await task
                self.assertTrue(task.done());self.assertIn('stale_ownership',kinds())
        with tempfile.TemporaryDirectory() as directory:asyncio.run(scenario(Path(directory)))

if __name__ == '__main__':
    unittest.main()
