"""Small event-driven launcher for a persistent, tool-capable Astra operator.

This is operational delegation, not a patch approval engine or scientific judge.
Healthy observations never call a model. The operator owns ad hoc diagnosis,
independent review and lawful native continuation under the accompanying prompt.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import signal
import time
import uuid

import pilot_supervisor as supervisor
from campaign_watchdog import probe_process

MODEL='gpt-6-astra'
_CHILDREN={}
PROMPT=Path(__file__).resolve().parent.parent/'docs/pilot-operations-prompt.md'
ACTIONABLE={'infrastructure_failed','unexpected_stop','paper_incomplete','handoff'}


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def route_info(operation):
    operation=supervisor.canonical(operation)
    attempt=supervisor.read(operation/'attempt.json');launch=supervisor.read(operation/'launch.json')
    if launch.get('attempt_sha256')!=supervisor.sha(operation/'attempt.json'):
        raise ValueError('operation launch does not bind its reservation')
    root=supervisor.canonical(attempt['root']);config=supervisor.read(root/'host-config.json')
    deadline=config.get('exam',{}).get('submission_deadline_utc')
    if not deadline: raise ValueError('operations watcher requires the original exam deadline')
    return {'operation':str(operation),'root':str(root),'deadline_utc':deadline,
            'exam_clock':{k:v for k,v in config['exam'].items() if k!='state_root'},
            'models':config['models'],'codex_binary':config['codex_binary'],'launch':launch}


def initialize(state,operation,codex,workspace,cooldown=900,container_tools=False):
    state=supervisor.canonical(state);workspace=supervisor.canonical(workspace);codex=supervisor.canonical(codex)
    if not codex.is_file() or not os.access(codex,os.X_OK): raise ValueError('ordinary Codex executable unavailable')
    if type(cooldown)!=int or cooldown<60: raise ValueError('cooldown must be at least 60 seconds')
    if container_tools and not Path('/.dockerenv').is_file(): raise ValueError('full tool access requires explicit container deployment')
    route=route_info(operation)
    for path in (state,workspace):
        if path.is_relative_to(Path(route['root'])) or Path(route['root']).is_relative_to(path):
            raise ValueError('operations storage must be separate from exam roots')
    from codex_transport import subscription_environment
    with supervisor.owner(state):
        workspace.mkdir(parents=True,exist_ok=True)
        supervisor.save(state/'config.json',{'schema_version':1,'codex':str(codex),'codex_sha256':supervisor.sha(codex),
            'workspace':str(workspace),'container_tools':container_tools,'task_root':str(Path(route['root']).parent),'cooldown_seconds':cooldown,'initial_route':route,
            'prompt_sha256':supervisor.sha(PROMPT),'environment':subscription_environment()},exclusive=True)
        supervisor.save(state/'route.json',route,exclusive=True)
        supervisor.save(state/'ops-state.json',{'session_id':None,'active':None,'incidents':{},'quota_paused':False},exclusive=True)
    return {'status':'initialized_no_model_call','state':str(state)}


def set_route(state,operation):
    """Publish only an actually launched descendant retaining clock/models."""
    state=supervisor.canonical(state)
    with supervisor.owner(state):
        config=supervisor.read(state/'config.json');old=supervisor.read(state/'route.json');new=route_info(operation)
        initial=config['initial_route']
        for key in ('deadline_utc','exam_clock','models','codex_binary'):
            if new[key]!=initial[key]: raise ValueError('operator route cannot change original '+key)
        current=Path(new['root']);seen=set()
        while str(current)!=old['root']:
            if current in seen: raise ValueError('cyclic continuation lineage')
            seen.add(current)
            child_config=supervisor.read(current/'host-config.json')
            parent=child_config.get('continuation_parent')
            if not parent or len(seen)>64: raise ValueError('new route is not an authenticated native descendant')
            receipt=supervisor.read(current/'continuation-parent.json')
            if receipt.get('source_root')!=parent or not receipt.get('files') or digest(receipt['files'])!=receipt.get('manifest_sha256'):
                raise ValueError('continuation parent manifest mismatch')
            parent_root=supervisor.canonical(parent)
            for relative,expected in receipt['files'].items():
                member=supervisor.canonical(parent_root/relative)
                if not member.is_relative_to(parent_root) or supervisor.sha(member)!=expected:
                    raise ValueError('preserved native parent changed')
            ref=child_config.get('continuation_checkpoint',{})
            if ref.get('sha256')!=supervisor.sha(current/'continuation-checkpoint.json'):
                raise ValueError('continuation checkpoint binding changed')
            current=supervisor.canonical(parent)
        process=probe_process(new['launch']['pid'],new['launch'].get('process_identity'))
        if process!={'alive':True,'identity_match':True}:
            report=supervisor.observation(Path(new['root']),new['launch'])
            cells=supervisor.read(Path(new['root'])/'campaign/state.json').get('problems',{})
            complete=(process.get('alive') is False and report.get('status')=='exited' and not report.get('issues')
                      and bool(cells) and set(cells)==set(supervisor.read(Path(new['root'])/'host-config.json')['problems'])
                      and all(c.get('successful_complete') is True for c in cells.values()))
            if not complete: raise ValueError('successor must be owned-running or natively fully complete before routing')
        supervisor.save(state/'route.json',new)
        return {'status':'active_route_updated','root':new['root']}


def command(codex,session,*,task_root=None,container_tools=False):
    from codex_transport import authentication_mode
    argv=[codex]
    if not container_tools:
        argv+=['-a','never','-s','workspace-write']
        if task_root: argv+=['--add-dir',task_root]
    argv+=['exec']+(['resume'] if session else [])
    argv+=['--ignore-user-config','--ignore-rules','--json','--skip-git-repo-check',
           '-m',MODEL,'-c','forced_login_method='+json.dumps(authentication_mode()),'-c','model_reasoning_effort="high"']
    if container_tools: argv.append('--dangerously-bypass-approvals-and-sandbox')
    if session: argv.append(session)
    return argv+['-']


def events(path):
    result=[]
    if path.exists():
        with path.open() as stream:
            for line in stream:
                try: item=json.loads(line)
                except (ValueError,UnicodeError): continue
                if isinstance(item,dict) and item.get('type') in {'thread.started','turn.completed','turn.failed','error'}: result.append(item)
    return result


def finish_active(state,saved):
    active=saved['active']
    if active.get('pid') is None: return 'uncertain_reserved_operator'
    child=_CHILDREN.get(active['pid'])
    if child is not None:
        if child.poll() is not None: _CHILDREN.pop(active['pid'],None)
    else:
        try: os.waitpid(active['pid'],os.WNOHANG)
        except ChildProcessError: pass
    status=probe_process(active['pid'],active.get('process_identity'))
    if status.get('alive') is not False: return 'operator_running' if status.get('identity_match') else 'operator_ownership_uncertain'
    rows=events(Path(active['events']))
    sessions={r.get('thread_id') for r in rows if r.get('type')=='thread.started'}
    error_text=' '.join(json.dumps(r).lower() for r in rows if r.get('type') in ('error','turn.failed'))
    if any(code in error_text for code in ('quota','usage_limit','rate_limit','insufficient_quota')): saved['quota_paused']=True
    if len(sessions)!=1:
        saved['attention']='operator exited without one authenticated session identity'
        saved['active']=None;supervisor.save(state/'ops-state.json',saved)
        return 'operator_identity_attention'
    if len(sessions)==1:
        session=sessions.pop()
        try: uuid.UUID(session)
        except (ValueError,TypeError,AttributeError):
            saved['attention']='operator returned malformed session identity'
            saved['active']=None;supervisor.save(state/'ops-state.json',saved)
            return 'operator_identity_attention'
        if saved['session_id'] and session!=saved['session_id']:
            saved['attention']='operations session identity changed'
            saved['active']=None;supervisor.save(state/'ops-state.json',saved)
            return 'operator_identity_attention'
        saved['session_id']=session
    # Terminal-only metering in the operations namespace. Never poll a live
    # response or merge operator usage into research stage accounting.
    from codex_transport import _persisted_tool_audit, authentication_mode
    from codex_accounting import account_stage
    started = saved['incidents'][active['fingerprint']]['started_utc']
    ended = supervisor.now()
    try:
        audit = _persisted_tool_audit(session, started)
        completed = any(r.get('type') == 'turn.completed' for r in rows)
        metadata = {'name': 'operations/' + active['fingerprint'] + '/' + Path(active['events']).parent.name,
                    'module': 'operations', 'artifact_directory': str(Path(active['events']).parent.relative_to(state)),
                    'session_id': session, 'start_utc': started, 'end_utc': ended,
                    'model_requested': MODEL, 'turn_completed': completed,
                    'status': 'completed' if completed else 'incomplete',
                    'authentication': authentication_mode()}
        receipt = account_stage(state, metadata, audit)
    except (ValueError, OSError, KeyError, TypeError) as error:
        receipt = {'metering': 'unknown', 'error_type': type(error).__name__}
    supervisor.save(Path(active['events']).parent/'accounting-receipt.json', receipt)
    saved['incidents'][active['fingerprint']].update(finished_utc=supervisor.now(),finished_epoch=time.time(),
        outcome='completed' if any(r.get('type')=='turn.completed' for r in rows) else 'incomplete_no_retry')
    saved['active']=None;supervisor.save(state/'ops-state.json',saved)
    return 'operator_finished'


def compact(report,route):
    # Only affected tasks contribute identity: healthy sibling progress must not
    # renew the same failed task's operations allowance.
    root=Path(route['root']);issues=report.get('issues',[]);health=report.get('health',[])
    affected={x.get('problem') for x in issues+health if x.get('problem')}
    paths={x.get('path') for x in health if x.get('path')}
    for name in paths:
        parts=Path(name).parts
        if len(parts)>2 and parts[:2]==('host','runtime'): affected.add(parts[2])
    metadata={}
    for p in (root/'host/runtime').glob('*/*/stage.meta.json'):
        if affected and p.parent.parent.name not in affected: continue
        if not affected and report['status']=='running': continue
        metadata[str(p.relative_to(root))]=supervisor.sha(p)
    return {'root':route['root'],'status':report['status'],'issues':issues,
            'health':health,'transport_metadata':metadata,'deadline_utc':route['deadline_utc']}


def tick(state):
    state=supervisor.canonical(state)
    with supervisor.owner(state):
        config=supervisor.read(state/'config.json');saved=supervisor.read(state/'ops-state.json');route=supervisor.read(state/'route.json')
        if datetime.now(timezone.utc)>=datetime.fromisoformat(route['deadline_utc']):
            active=saved.get('active')
            if active and active.get('pid') and not active.get('deadline_stop_requested'):
                if probe_process(active['pid'],active.get('process_identity'))=={'alive':True,'identity_match':True}:
                    os.kill(active['pid'],signal.SIGTERM)  # Only the owned operator, never a group or research child.
                    active['deadline_stop_requested']=supervisor.now();supervisor.save(state/'ops-state.json',saved)
            return {'status':'original_deadline_reached','model_call':False}
        if saved['active']:
            status=finish_active(state,saved)
            if status!='operator_finished': return {'status':status,'model_call':False}
        if saved.get('attention'): return {'status':'operator_identity_attention','model_call':False}
        if saved.get('quota_paused'): return {'status':'operator_quota_paused','model_call':False}
        if datetime.now(timezone.utc)>=datetime.fromisoformat(route['deadline_utc']):
            return {'status':'original_deadline_reached','model_call':False}
        info=route_info(route['operation'])
        if info!=route: raise ValueError('active operation binding changed')
        report=supervisor.observation(Path(route['root']),route['launch'])
        supervisor.save(state/'observation.json',report)
        health={x.get('kind') for x in report.get('health',[])}
        stalled=report['status']=='running' and (bool(health & {'pending_obligation_without_task','problem_ended_with_attention','dead_child','stale_ownership'}) or {'stage_deadline_overdue','watchdog_stale_or_missing'}<=health)
        if report['status'] not in ACTIONABLE and not stalled: return {'status':report['status'],'model_call':False}
        if supervisor.unresolved_quota(report.get('evidence',[])): return {'status':'quota_paused','model_call':False}
        if not stalled and report.get('process',{}).get('alive') is not False:
            return {'status':'ownership_requires_attention','model_call':False}
        packet=compact(report,route);fingerprint=digest(packet)
        previous=saved['incidents'].get(fingerprint,{})
        disposition=state/'incidents'/fingerprint/'disposition.json'
        if disposition.is_file():
            outcome=supervisor.read(disposition)
            if outcome.get('status') in {'blocked','quota_paused'} and outcome.get('reason'):
                return {'status':'incident_disposition_recorded','model_call':False}
            # A self-reported resolved outcome cannot hide native unfinished work.
        if previous and (previous.get('attempts',1)>=3 or not saved.get('session_id')):
            return {'status':'incident_followup_limit_attention','model_call':False}
        last=max((max(i.get('started_epoch',0),i.get('finished_epoch',0)) for i in saved['incidents'].values()),default=0)
        if time.time()-last<config['cooldown_seconds']: return {'status':'incident_cooldown','model_call':False}
        if supervisor.sha(config['codex'])!=config['codex_sha256'] or supervisor.sha(PROMPT)!=config['prompt_sha256']:
            raise ValueError('operator binary or mandate changed')
        from codex_transport import subscription_environment
        if subscription_environment()!=config['environment']: raise ValueError('operations authentication/runtime environment changed')
        incident=state/'incidents'/fingerprint/str(previous.get('attempts',0)+1);incident.mkdir(parents=True,exist_ok=False)
        supervisor.save(incident/'incident.json',packet,exclusive=True)
        prompt=PROMPT.read_text()+'\n\nOPERATIONS STATE: '+str(state)+'\nINCIDENT DIRECTORY: '+str(incident)+'\nDISPOSITION FILE: '+str(disposition)+'\nACTIVE ROUTE: '+str(state/'route.json')+'\nINCIDENT:\n'+json.dumps(packet)
        (incident/'prompt.txt').write_text(prompt)
        active={'fingerprint':fingerprint,'pid':None,'process_identity':None,'events':str(incident/'events.jsonl')}
        saved['active']=active;saved['incidents'][fingerprint]={'attempts':previous.get('attempts',0)+1,'started_epoch':time.time(),'started_utc':supervisor.now()}
        supervisor.save(state/'ops-state.json',saved) # Durable reservation precedes spawn; no crash replay.
        from codex_transport import subscription_environment
        env=subscription_environment()
        if env!=config['environment']: raise ValueError('operations authentication/runtime environment changed')
        with (incident/'prompt.txt').open('rb') as stdin,(incident/'events.jsonl').open('xb') as stdout,(incident/'stderr.log').open('xb') as stderr:
            child=subprocess.Popen(command(config['codex'],saved['session_id'],task_root=config['task_root'],container_tools=config.get('container_tools',False)),cwd=config['workspace'],env=env,
                                   stdin=stdin,stdout=stdout,stderr=stderr,start_new_session=True)
        _CHILDREN[child.pid]=child
        active.update(pid=child.pid,process_identity=supervisor.settled_identity(child))
        supervisor.save(state/'ops-state.json',saved)
        return {'status':'operator_started','model_call':True,'pid':child.pid,'incident':fingerprint}


def run(state,interval=30):
    while True:
        try: result=tick(state)
        except Exception as error:
            result={'status':'operations_attention','model_call':False,'error_type':type(error).__name__,'error':str(error)}
        supervisor.save(Path(state)/'watcher-status.json',{**result,'checked_utc':supervisor.now()})
        if result['status'] in ('original_deadline_reached','exited'): return result
        time.sleep(interval)


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    init=sub.add_parser('init');init.add_argument('state',type=Path);init.add_argument('--operation',type=Path,required=True)
    init.add_argument('--codex',type=Path,required=True);init.add_argument('--workspace',type=Path,required=True);init.add_argument('--cooldown',type=int,default=900);init.add_argument('--container-tools',action='store_true',help='explicitly allow unsandboxed shell inside an externally confined task container')
    watch=sub.add_parser('watch');watch.add_argument('state',type=Path);watch.add_argument('--once',action='store_true');watch.add_argument('--interval',type=int,default=30)
    route=sub.add_parser('route');route.add_argument('state',type=Path);route.add_argument('--operation',type=Path,required=True)
    args=parser.parse_args()
    if args.action=='init':result=initialize(args.state,args.operation,args.codex,args.workspace,args.cooldown,args.container_tools)
    elif args.action=='route':result=set_route(args.state,args.operation)
    else:result=tick(args.state) if args.once else run(args.state,max(5,args.interval))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
