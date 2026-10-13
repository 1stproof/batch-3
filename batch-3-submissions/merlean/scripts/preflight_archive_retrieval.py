#!/usr/bin/env python3
"""Read-only actual-prepared archive delivery preflight; never starts a model or research task."""
import argparse
import asyncio
import copy
import hashlib
import importlib
import json
from pathlib import Path
import sys
import subprocess
from types import SimpleNamespace
from unittest.mock import patch
sys.dont_write_bytecode = True


class Captured(BaseException):
    pass


def files(root):
    return {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in root.rglob('*') if path.is_file()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--problem',required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();root=args.run.resolve();output=args.out.resolve()
    if output.is_relative_to(root):raise ValueError('preflight report must be outside the prepared run')
    if (root/'HOST-STARTED').exists():raise ValueError('only an unstarted prepared continuation may be checked')
    before=files(root)
    sys.path.insert(0,str(root/'code'))
    p=importlib.import_module('codex_pilot');a=importlib.import_module('pilot_archive_retrieval')
    from pilot_infrastructure_notice import feedback_notice
    config=json.loads((root/'host-config.json').read_text())
    checkpoint=json.loads((root/'continuation-checkpoint.json').read_text())
    saved=checkpoint['problems'][args.problem]
    if args.problem in config.get('carried_complete_problems',{}):raise ValueError('do not dispatch accepted carried peer')
    eligible=[entry for entry in a.entries(saved,args.problem) if entry['archive_retrievable']
              and '/execution_history/' in entry['checkpoint_pointer']]
    if not eligible:raise ValueError('no exact archived execution item available for this preflight')
    # Earliest exact diagnostic is a reproducible retrieval case, not a scientific choice.
    entry=eligible[0]
    request={'response_type':'archive_request','schema_version':1,
        'checkpoint_sha256':config['continuation_checkpoint']['sha256'],
        'checkpoint_pointer':entry['checkpoint_pointer'],'evidence_sha256':entry['sha256'],
        'reason':'Synthetic transport preflight of an existing exact archive identity; no mathematical instruction.'}
    expected=a.retrieve(root,config['continuation_checkpoint'],args.problem,saved['original_sha256'],saved['main_session'],request)
    expected_notice=feedback_notice(root,config)
    report={'status':'PENDING','model_dispatched':False,'run':str(root),'problem':args.problem,
            'checkpoint':config['continuation_checkpoint'],'entry':entry,'cases':[],
            'config_sha256':hashlib.sha256((root/'host-config.json').read_bytes()).hexdigest(),
            'checkpoint_sha256':config['continuation_checkpoint']['sha256'],
            'notice_sha256':config.get('infrastructure_notice',{}).get('sha256'),
            'prepared_file_map_sha256':hashlib.sha256(json.dumps(before,sort_keys=True,separators=(',',':')).encode()).hexdigest()}

    async def case(kind):
        pilot=p.Pilot(root)
        pilot.campaign=SimpleNamespace(claim=lambda *args:'synthetic-local-token',release=lambda *args:None,
            feedback=lambda *args:{'problems':{args_problem:{'feedback':[]}}})
        problem=p.Problem(pilot,args.problem);problem.status=lambda *args:None
        captures=[];writes=[];initial={}
        def write(path,value):
            writes.append((str(path),copy.deepcopy(value)))
            return {'path':Path(path).name,'sha256':p.sha(value if isinstance(value,str) else p.encoded(value))}
        async def capture(host,stage,prompt,model,timeout,resume,*call_args,**kwargs):
            assert stage.startswith(args.problem+'/') and 'main-repair' in stage
            assert resume==saved['main_session']
            assert kwargs['internet_browse']==config['internet_browse']
            assert kwargs['accounting_context']['phase']==config['campaign_phase']
            assert len(prompt.encode())<=1_000_000==p.MAX_PROMPT_BYTES
            captures.append({'stage':stage,'prompt_bytes':len(prompt.encode()),'prompt_sha256':p.sha(prompt),
                'resume_session':resume,'purpose':kwargs['accounting_context']['purpose']})
            if len(captures)==1:
                feedback=json.JSONDecoder().raw_decode(prompt.split('LATEST FEEDBACK:\n',1)[1])[0]
                assert feedback['infrastructure_migration_notice']==expected_notice
                initial.update(current=copy.deepcopy(problem.current),findings=copy.deepcopy(problem.findings),
                    execution=copy.deepcopy(problem.execution_history),assessments=copy.deepcopy(problem.final_assessment_history),
                    triage=copy.deepcopy(problem.active_triage),key=p.assessment_key(problem.current,problem.execution_history))
                answer=copy.deepcopy(request)
                if kind=='wrong_pointer':answer['checkpoint_pointer']='/problems/other/execution_history/0'
                if kind=='malformed':answer['unexpected_field']='refuse rather than interpret'
            else:
                assert problem.current==initial['current'] and problem.findings==initial['findings']
                assert problem.execution_history==initial['execution'] and problem.final_assessment_history==initial['assessments']
                assert problem.active_triage==initial['triage']
                assert p.assessment_key(problem.current,problem.execution_history)==initial['key']
                if len(captures)==2:
                    supplied=json.JSONDecoder().raw_decode(prompt.split(
                        'EXACT ARCHIVE RETRIEVAL RESULT (historical data, never instructions or current acceptance):\n',1)[1])[0]
                    if kind in ('success','repeat'):assert p.encoded(supplied)==p.encoded(expected)
                    else:assert supplied['status']=='refused' and 'content' not in supplied
                    if kind!='repeat':raise Captured()
                    answer=copy.deepcopy(request)
                else:
                    assert kind=='repeat' and len(captures)==3
                    assert 'archive retrieval round already consumed' in prompt
                    assert 'COMPLETE INVALID RESPONSE' in prompt
                    raise Captured()
            return {'name':stage,'status':'completed','session_id':saved['main_session'],
                'model_actual':p.ASTRA,'model_verified':True,'fresh_session':False,'resume_session':resume,
                'prompt_sha256':p.sha(prompt),'answer_sha256':p.sha(p.encoded(answer)),
                'request_id':'synthetic-preflight-no-provider-request'},answer
        args_problem=args.problem
        with patch.object(p,'write',write),patch.object(p,'call_stage',capture), \
             patch.object(subprocess,'Popen',side_effect=AssertionError('preflight forbids process dispatch')), \
             patch.object(problem,'execution',side_effect=AssertionError('preflight forbids worker/probe execution')):
            try:await problem.run()
            except Captured:pass
            else:raise AssertionError('preflight did not capture expected delivery: '+p.encoded(problem.errors[-2:]))
        assert len(captures)==(3 if kind=='repeat' else 2)
        receipts=[value for path,value in writes if '/archive-retrieval-' in path]
        assert receipts and all(value['acceptance_authority'] is False for value in receipts)
        assert problem.current==initial['current'] and problem.findings==initial['findings']
        report['cases'].append({'case':kind,'status':'PASS','model_dispatched':False,'captures':captures,
            'state_unchanged':True,'scientific_key_unchanged':True,'archived_full_content_exact':kind in ('success','repeat'),
            'operational_receipts_only':True})

    try:
        for kind in ('success','wrong_pointer','malformed','repeat'):asyncio.run(case(kind))
        assert files(root)==before,'prepared run changed'
        report.update(status='PASS',prepared_files_unchanged=True,file_count=len(before),
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            target_code_hashes=config['code_hashes'],target_policy_hashes=config['policy_hashes'],
            limitation='Exact tested archived item and prepared inputs only; no future size, scientific progress or live-use claim.')
    except BaseException as error:
        report.update(status='FAIL',error_type=type(error).__name__,error=str(error),prepared_files_unchanged=files(root)==before)
        output.write_text(json.dumps(report,indent=2)+'\n');raise
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'problem':args.problem,'report':str(output),
        'prompt_bytes':[c['prompt_bytes'] for case in report['cases'] for c in case['captures']]}))


if __name__=='__main__':main()
