"""The semaphore/drain boundary is real admission; historical attempts are retained."""
import asyncio
import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
from pilot_drain import PilotDrain, DrainRequested
import test_pilot_parallel_routes as fixtures

class AssessmentAdmissionTests(unittest.TestCase):
    def setUp(self):
        f=fixtures.ParallelRouteTests();f.setUp();self.addCleanup(f.doCleanups)
        self.x=f.x;self.f=f
        self.x.final_assessment_history=[]
        self.x.current.pop('route_scout_tasks',None)
        self.x.pilot.config['assessment_protocol_epoch']=p.ASSESSMENT_PROTOCOL_EPOCH
        self.x.review_candidate=AsyncMock(return_value=(f.f.meta('fresh-proof'),{'verdict':'INCOMPLETE'}))

    def test_queued_stage_drained_before_admission_consumes_no_attempt(self):
        async def scenario():
            x=self.x;x.pilot.drain=PilotDrain(x.pilot.host);x.pilot.semaphore=asyncio.Semaphore(1)
            await x.pilot.semaphore.acquire()
            job=asyncio.create_task(x.commission_final_assessment({'mathematically_ready':True}))
            await asyncio.sleep(0)
            self.assertEqual(x.final_assessment_history[0]['attempts'],0)
            p.write(x.pilot.host/'drain-request.json',{'schema_version':1,'action':'drain','request_id':'test','reason':'race'})
            x.pilot.semaphore.release()
            with self.assertRaises(DrainRequested):await job
            self.assertEqual(x.final_assessment_history[0]['attempts'],0)
            self.assertEqual(x.final_assessment_history[0]['status'],'awaiting_admission')
        with patch.object(p,'call_stage',side_effect=AssertionError('must not spawn')):
            asyncio.run(scenario())

    def test_attempt_is_durable_before_transport_and_completed_legacy_never_replays(self):
        async def transport(host,name,prompt,model,timeout,resume,**kwargs):
            record=self.x.final_assessment_history[-1]
            self.assertEqual(record['attempts'],1)
            self.assertEqual(record['status'],'commissioned')
            return self.f.f.meta('fresh-scope'),{'verdict':'unknown'}
        with patch.object(p,'call_stage',side_effect=transport):
            asyncio.run(self.x.commission_final_assessment({'mathematically_ready':True}))
        record=copy.deepcopy(self.x.final_assessment_history[-1]);record.pop('protocol_epoch')
        self.x.final_assessment_history=[record]
        with patch.object(p,'call_stage',side_effect=AssertionError('epoch cannot replay completed assessment')):
            self.assertIsNone(asyncio.run(self.x.commission_final_assessment({'mathematically_ready':True})))

    def test_large_prompt_admission_consumes_attempt_before_actual_transport(self):
        self.x.statement='x'*1_000_001
        with patch.object(p,'call_stage',side_effect=OSError('provider failure')):
            with self.assertRaisesRegex(OSError,'provider failure'):
                asyncio.run(self.x.commission_final_assessment({'mathematically_ready':True}))
        self.assertEqual(self.x.final_assessment_history[0]['attempts'],1)
