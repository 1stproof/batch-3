"""Host attribution, exact response deduplication and unknown legacy evidence."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from api_accounting import APIAccountingLedger
from codex_accounting import account_stage

class PurposeAccountingTests(unittest.TestCase):
    def test_exact_groups_mixed_purpose_and_legacy_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=APIAccountingLedger(Path(tmp)/'ledger.sqlite3')
            usage={'input_tokens':100,'cached_input_tokens':40,'cache_write_input_tokens':0,'output_tokens':20,'reasoning_output_tokens':12}
            for rid,model,metadata in [('a','astra',{'phase':'phase2','segment_id':'segment12','problem':'p2','role':'main','purpose':'mixed_main_scientific_reasoning_and_lean_planning','session_id':'s1'}),('b','sol',{})]:
                for _ in range(2):ledger.record(rid,'module',model,usage,'complete',metadata=metadata,event_id=rid,usage_format="codex_flat")
            report=ledger.purpose_summary()
            self.assertEqual(report['total']['call_count'],2)
            self.assertEqual(report['total']['usage']['total_tokens'],240)
            self.assertEqual(report['total'],ledger.summary()['total'])
            self.assertEqual({g['phase'] for g in report['groups']},{'phase2','unknown'})
            self.assertEqual(len(report['responses']),2)
            self.assertIsNone(report['total']['api_equivalent_usd'])
            self.assertIsNone(report['total']['actual_billed_usd'])
            self.assertEqual(next(g for g in report['groups'] if g['model']=='astra')['purpose'],'mixed_main_scientific_reasoning_and_lean_planning')

    def test_no_response_stage_stays_unknown_and_context_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'runtime').mkdir()
            context={'phase':'phase2','segment_id':'segment12','purpose':'route_scout'}
            meta={'name':'p4/scout','module':'route-scout','artifact_directory':'runtime','session_id':None,'model_requested':'astra','status':'running','accounting_context':context}
            receipt=account_stage(root,meta,{})
            report=json.loads((root/'accounting/role-cost-summary.json').read_text())
            self.assertFalse(report['metering_complete'])
            self.assertEqual(receipt['accounting_context'],context)
            self.assertEqual(report['pending_or_unmetered_stages'][0]['stage'],'p4/scout')
            self.assertEqual(report['responses'],[])

    def test_unknown_usage_remains_unknown_in_group(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=APIAccountingLedger(Path(tmp)/'ledger.sqlite3')
            ledger.record('unknown','module','sol',None,'unknown',metadata={'phase':'phase2','purpose':'lean_implementation_compile_fix'})
            group=ledger.purpose_summary()['groups'][0]
            self.assertIsNone(group['totals']['usage']['total_tokens'])
            self.assertIsNone(group['totals']['api_equivalent_usd'])

    def test_frozen_price_cost_matches_existing_ledger_reducer(self):
        with tempfile.TemporaryDirectory() as tmp:
            card=Path(__file__).resolve().parents[1]/'assets/api-prices-2026-09-16.json'
            ledger=APIAccountingLedger(Path(tmp)/'ledger.sqlite3',card)
            ledger.record('priced','main','gpt-6-astra',{'input':1000000,'cached_read':200000,'cache_write':100000,'output':100000,'reasoning_output':80000},'complete',metadata={'phase':'phase-2','purpose':'mixed_main_scientific_reasoning_and_lean_planning'})
            report=ledger.purpose_summary()
            self.assertEqual(report['price_card'],ledger.summary()['price_card'])
            self.assertEqual(report['groups'][0]['totals'],ledger.summary()['total'])
            self.assertEqual(report['groups'][0]['totals']['api_equivalent_usd'],'24.4')
            self.assertIsNone(report['groups'][0]['totals']['actual_billed_usd'])

    def test_bad_dispatch_context_fails_before_provider_preflight(self):
        import asyncio
        from unittest.mock import patch
        import codex_transport
        with tempfile.TemporaryDirectory() as tmp, patch.object(codex_transport,'subscription_preflight') as preflight:
            with self.assertRaises(ValueError):
                asyncio.run(codex_transport.call_stage(Path(tmp),'p/main','text','astra',1,accounting_context={'phase':'phase-2'}))
            preflight.assert_not_called()

    def test_conflicting_stage_alias_preserved_without_double_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'runtime').mkdir()
            base={'name':'p/main1','module':'main','artifact_directory':'runtime','session_id':'session','model_requested':'astra','status':'completed','turn_completed':True,'start_utc':'2026-01-01T00:00:00Z','end_utc':'2026-01-01T00:02:00Z'}
            audit={'status':'verified','response_usage_records':[{'timestamp':'2026-01-01T00:01:00Z','model':'astra','payload':{'thread_id':'session','turn_id':'turn','response_id':'same','usage':{'input_tokens':100,'cached_input_tokens':0,'cache_write_input_tokens':0,'output_tokens':10,'reasoning_output_tokens':5}}}]}
            account_stage(root,base,audit)
            other=dict(base,name='p/main2',accounting_context={'phase':'phase-2','segment_id':'12','purpose':'route_scout'})
            receipt=account_stage(root,other,audit)
            report=json.loads((root/'accounting/role-cost-summary.json').read_text())
            self.assertEqual(report['total']['call_count'],1)
            self.assertEqual(report['response_stage_aliases']['same'],['p/main1','p/main2'])
            self.assertEqual(receipt['metering'],'unknown')
            self.assertTrue(receipt['errors'])
