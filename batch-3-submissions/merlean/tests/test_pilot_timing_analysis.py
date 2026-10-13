"""Deterministic offline observation, never model dispatch or timing authority."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_timing_analysis as t


def event(at,kind='thread.started',ident=None,tool='read_artifact',status='completed'):
    e={'type':kind}
    if ident is not None:e['item']={'type':'mcp_tool_call','server':'merlean_documents','id':ident,'tool':tool,'status':status,'arguments':{'PRIVATE':'NEVER_OUTPUT_PAYLOAD'},'result':{'text':'NEVER_OUTPUT_PAYLOAD'}}
    return (json.dumps({'elapsed_s':at,'utc':'2026-09-30T00:00:00Z','event':e})+'\n').encode()

class TimingTests(unittest.TestCase):
    def test_overlap_union_and_unknown_residual(self):
        data=event(1,'item.started','a')+event(2,'item.started','b')+event(4,'item.completed','a')+event(5,'item.completed','b')
        r=t.analyze_events(data,10)
        self.assertEqual(r['document_paired_interval_sum_s'],6)
        self.assertEqual(r['document_paired_interval_union_s'],4)
        self.assertEqual(r['document_overlap_s'],2)
        self.assertEqual(r['outside_paired_document_intervals_unclassified_s'],6)
        self.assertIsNone(r['coverage_completion_time'])
        self.assertEqual(len(r['document_interval_details']),2)
        self.assertEqual(r['between_paired_document_intervals_unclassified']['count'],0)
        self.assertNotIn('NEVER_OUTPUT_PAYLOAD',json.dumps(r))
    def test_unmatched_duplicate_and_reversed_arrival_are_not_valid_pairs(self):
        for data in [event(1,'item.started','a'),event(1,'item.started','a')+event(2,'item.started','a')+event(3,'item.completed','a'),event(1,'item.completed','a')+event(1,'item.started','a')]:
            r=t.analyze_events(data,10);self.assertFalse(r['observed_prefix_pairs_complete']);self.assertEqual(r['document_paired_interval_union_s'],0)
    def test_invalid_clocks_make_duration_attribution_unknown(self):
        for data in [event(3)+event(2),event(11),event(float('nan')),event(float('inf')),event(10**400)]:
            r=t.analyze_events(data,10)
            self.assertFalse(r['observed_prefix_pairs_complete']);self.assertIsNone(r['document_paired_interval_union_s']);self.assertIsNone(r['outside_paired_document_intervals_unclassified_s'])
    def test_numeric_interval_details_capped_and_gaps_exact(self):
        data=b''.join(event(i*3,'item.started',str(i))+event(i*3+1,'item.completed',str(i)) for i in range(300))
        r=t.analyze_events(data,900)
        self.assertEqual(len(r['document_interval_details']),256)
        self.assertEqual(r['interval_details_omitted'],44)
        self.assertEqual(r['between_paired_document_intervals_unclassified'],{'count':299,'sum_s':598.0,'max_s':2.0})
    def test_invalid_supplied_horizon_and_large_finite_aggregate_are_unknown(self):
        data=event(1,'item.started','a')+event(2,'item.completed','a')
        for duration in (float('nan'),-1,'bad',True,1e308):
            r=t.analyze_events(data,duration)
            self.assertIn('invalid_recorded_elapsed',r['issues'])
            self.assertIsNone(r['document_paired_interval_sum_s'])
            json.dumps(r,allow_nan=False)
        data=event(0,'item.started','a')+event(0,'item.started','b')+event(1e308,'item.completed','a')+event(1e308,'item.completed','b')
        r=t.analyze_events(data,1e308);self.assertFalse(r['observed_prefix_pairs_complete']);json.dumps(r,allow_nan=False)
    def test_missing_clock_not_zero(self):
        r=t.analyze_events(b'')
        self.assertIsNone(r['observed_elapsed_horizon_s']);self.assertIsNone(r['outside_paired_document_intervals_unclassified_s']);self.assertFalse(r['observed_prefix_pairs_complete'])
    def test_partial_tail_bad_line_and_caps_explicit(self):
        for data,kwargs in [(event(1)+b'{unfinished',{}),(event(1)+b'not json\n',{}),(event(1)+event(2),{'max_lines':1}),(event(1),{'max_line_bytes':2})]:
            r=t.analyze_events(data,10,**kwargs);self.assertFalse(r['observed_prefix_pairs_complete'])
        self.assertGreater(t.analyze_events(event(1)+b'bad')['partial_trailing_bytes'],0)
    def test_completion_status_not_successful_delivery(self):
        r=t.analyze_events(event(1,'item.started','a')+event(2,'item.completed','a',status='failed'),3)
        self.assertEqual(r['document_tools']['read_artifact']['completion_status_counts'],{'failed':1});self.assertIsNone(r['coverage_completion_time'])
    def stage(self,root,name='001-proof-review'):
        p=root/'run/host/runtime/p'/name;p.mkdir(parents=True)
        meta={'name':'p/'+name,'request_id':'b2l-'+'a'*64,'session_id':'11111111-1111-1111-1111-111111111111','status':'completed','fresh_session':True,'turn_completed':True,'elapsed_s':10,'start_utc':'2026-09-30T00:00:00Z','end_utc':'2026-09-30T00:00:10Z','document_audit':{'status':'PASS','required_material_delivered':True,'receipt_count':1}}
        (p/'stage.meta.json').write_text(json.dumps(meta));(p/'stage.events.jsonl').write_bytes(event(1,'item.started','a')+event(2,'item.completed','a'));return p,meta
    def test_deterministic_core_and_options_bound_dedup(self):
        with tempfile.TemporaryDirectory() as tmp:
            p,_=self.stage(Path(tmp));a=t.report([p]);os.utime(p/'stage.events.jsonl',None);b=t.report([p]);self.assertEqual(a,b)
            self.assertEqual(t.report([p,p])['duplicate_stage_copies_excluded'],1)
            self.assertNotEqual(a['stages'][0]['dedup_key'],t.report([p],max_lines=1)['stages'][0]['dedup_key'])
    def test_metadata_payload_types_not_echoed(self):
        with tempfile.TemporaryDirectory() as tmp:
            p,meta=self.stage(Path(tmp))
            for key in ('name','request_id','session_id','status','start_utc'):meta[key]={'PRIVATE':'NEVER_OUTPUT_PAYLOAD'}
            meta['document_audit']={'status':['NEVER_OUTPUT_PAYLOAD'],'receipt_count':'NEVER_OUTPUT_PAYLOAD'}
            (p/'stage.meta.json').write_text(json.dumps(meta));r=t.report([p]);self.assertNotIn('NEVER_OUTPUT_PAYLOAD',json.dumps(r));self.assertEqual(r['status'],'OBSERVATIONAL_PARTIAL')
    def test_missing_files_and_terminal_censoring(self):
        with tempfile.TemporaryDirectory() as tmp:
            p,meta=self.stage(Path(tmp));(p/'stage.meta.json').unlink();(p/'stage.events.jsonl').unlink()
            r=t.analyze_stage(p);self.assertIsNone(r['metrics']['observed_elapsed_horizon_s']);self.assertEqual(r['measurement_status'],'PARTIAL_OR_UNAVAILABLE')
            for state in ('timeout_censored','cancelled'):
                meta['status']=state;meta['turn_completed']=False;(p/'stage.meta.json').write_text(json.dumps(meta));self.assertTrue(t.analyze_stage(p)['censored_or_unfinished'])
    def test_snapshot_rewrite_symlink_and_byte_cap(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'input';p.write_bytes(b'abc');link=Path(tmp)/'link';link.symlink_to(p)
            with self.assertRaises(ValueError):t.snapshot(link)
            with patch.object(t.os,'read',side_effect=[b'abc',b'xyz']):
                with self.assertRaises(ValueError):t.snapshot(p)
            data,receipt=t.snapshot(p,2);self.assertEqual(data,b'ab');self.assertTrue(receipt['byte_cap_reached'])
    def test_fifo_input_is_refused_without_blocking_open(self):
        with tempfile.TemporaryDirectory() as tmp:
            fifo=Path(tmp)/'fifo';os.mkfifo(fifo)
            with self.assertRaisesRegex(ValueError,'regular input file required'):t.snapshot(fifo)
    def test_cli_external_only_exclusive_and_no_input_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p,_=self.stage(root);before={x.name:x.read_bytes() for x in p.iterdir()}
            for output in [p/'report.json',root/'run/report.json']:
                with contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):t.main([str(p),'--output',str(output)])
            alias=root/'alias';alias.symlink_to(root/'run',target_is_directory=True)
            with contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):t.main([str(p),'--output',str(alias/'report.json')])
            output=root/'report.json'
            with contextlib.redirect_stdout(io.StringIO()):t.main([str(p),'--output',str(output)])
            with self.assertRaises(FileExistsError):t.main([str(p),'--output',str(output)])
            self.assertEqual(before,{x.name:x.read_bytes() for x in p.iterdir()})
            self.assertNotIn('analysis_wall_s',output.read_text());self.assertNotIn('NEVER_OUTPUT_PAYLOAD',output.read_text())

if __name__=='__main__':unittest.main()
