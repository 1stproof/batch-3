"""Read-only account metadata after a quota pause; never research admission."""
from __future__ import annotations
import asyncio
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import signal
import sys
import uuid

INTERVAL_SECONDS = 600
RPC_TIMEOUT_SECONDS = 20
FRAME_LIMIT = 1024 * 1024
ENV_KEYS = {'HOME','PATH','USER','LOGNAME','TMPDIR','LANG','LC_ALL','CODEX_HOME'}


def sanitize_limit(value):
    if value is None: return None
    if not isinstance(value,dict): raise ValueError('malformed quota bucket')
    result = {k:value[k] for k in ('limitId','limitName','normalModelSlug','planType','rateLimitReachedType','spendControlReached') if k in value}
    for key in ('primary','secondary'):
        window = value.get(key)
        if window is not None and not isinstance(window,dict): raise ValueError('malformed quota window')
        result[key] = None if window is None else {k:window[k] for k in ('usedPercent','windowDurationMins','resetsAt') if k in window}
    # Individual caps are intentionally not interpreted as global model access.
    cap = value.get('individualLimit')
    result['individualLimitPresent'] = cap is not None
    return result


def classify(snapshot, expected_account):
    if snapshot.get('account_id') != expected_account or snapshot.get('limits_account_id') != expected_account:
        return 'unknown_account_mismatch'
    if snapshot.get('account_type') != 'chatgpt' or snapshot.get('auth_unchanged') is not True:
        return 'unknown_authentication'
    buckets = snapshot.get('buckets')
    if not isinstance(buckets,dict) or not buckets: return 'unknown_missing_limits'
    unknown = False
    for bucket in buckets.values():
        if not isinstance(bucket,dict): unknown=True; continue
        if bucket.get('rateLimitReachedType') is not None or bucket.get('spendControlReached') is True:
            return 'limit_reported'
        if 'rateLimitReachedType' not in bucket or bucket.get('spendControlReached') is not False or bucket.get('individualLimitPresent') is not False:
            unknown=True
        windows = [bucket[k] for k in ('primary','secondary') if isinstance(bucket.get(k),dict)]
        if not windows: unknown=True
        for window in windows:
            used = window.get('usedPercent')
            for field in ('windowDurationMins','resetsAt'):
                value=window.get(field)
                if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<=0:unknown=True
            if isinstance(used,bool) or not isinstance(used,(int,float)) or not math.isfinite(used) or used<0:
                unknown=True
            elif used>=100: return 'limit_reported'
    return 'unknown_incomplete_limits' if unknown else 'metadata_no_limit_observed'


def validate_route(folder, path):
    import pilot_supervisor as outer
    route = outer.read(path); attempt = outer.read(folder/'attempt.json')
    root = outer.canonical(attempt['root']); config_path = root/'host-config.json'; config = outer.read(config_path)
    if route.get('schema_version') != 1 or route.get('authority') != 'explicit_operator_verified_selected_route':
        raise ValueError('explicit reviewed account route required')
    for key, expected in {'root':str(root),'attempt_sha256':outer.sha(folder/'attempt.json'),
                          'host_config_sha256':outer.sha(config_path),'codex_binary':config['codex_binary']}.items():
        if route.get(key) != expected: raise ValueError('selected route binding mismatch: '+key)
    binary = outer.canonical(route['codex_binary'])
    if outer.sha(binary) != route.get('codex_binary_sha256'): raise ValueError('selected binary changed')
    home = outer.canonical(route['codex_home']); auth = home/'auth.json'
    if str(auth.resolve()) != route.get('auth_source'): raise ValueError('selected authentication source changed')
    if outer.read(auth).get('tokens',{}).get('account_id') != route.get('account_id') or not route.get('account_id'):
        raise ValueError('selected account changed')
    env = route.get('environment')
    if (not isinstance(env,dict) or set(env)-ENV_KEYS or not all(isinstance(v,str) for v in env.values())
            or env.get('CODEX_HOME') != str(home)):
        raise ValueError('explicit sanitized selected-route environment required')
    if env.get('HOME') != os.environ.get('HOME'): raise ValueError('selected login home differs from operator')
    return route, root, config


def reconciled_stack(root, witness, expected_files, launch):
    """Require an independently bound terminal census, then recheck it live."""
    import pilot_supervisor as outer
    from pilot_continuation import validate_process_reconciliation
    from pilot_continuation_reservation import base_reservation
    if os.path.lexists(base_reservation(root)):
        raise ValueError('successor reservation exists; historical-parent intervention disabled')
    path=outer.canonical(witness['path'])
    if outer.sha(path)!=witness.get('sha256'):raise ValueError('terminal reconciliation changed')
    receipt=outer.read(path)
    if (receipt.get('host_pid')!=launch['pid'] or receipt.get('active_children')!=[]
            or receipt.get('pending_launches')!=[] or receipt.get('all_owned_children_stopped') is not True):
        raise ValueError('whole lower stack has not been reconciled stopped')
    actual={str(p.relative_to(root)):outer.sha(p) for p in root.rglob('*') if p.is_file()}
    if not expected_files or actual!=expected_files:raise ValueError('terminal lower-stack state changed')
    for path in (root/'host/runtime').glob('*/*/stage.meta.json'):
        if outer.read(path).get('status') in {'running','admitted','launching','pending'}:
            raise ValueError('lower stage is active or awaiting reconciliation')
    validate_process_reconciliation(root,receipt)
    return actual


def stopped_stack(folder, root, route, config, launch):
    import pilot_supervisor as outer
    since=launch['operation_started_utc']
    if (outer.terminal_outcome(root,config,since) != 'quota_paused'
            or not any('provider_quota' in item.get('failure_codes',[]) for item in outer.failure_evidence(root,since=since))):
        raise ValueError('current operation lacks a terminal provider-quota failure')
    return reconciled_stack(root,route.get('reconciliation') or {},route.get('terminal_files'),launch)


async def query(route, cwd):
    from pilot_document_startup import helper_identity
    from codex_transport import DISABLED_FEATURES, authentication_mode
    import pilot_supervisor as outer
    auth = Path(route['codex_home'])/'auth.json'; before = outer.sha(auth)
    command = [route['codex_binary'],'app-server','--stdio','-c','forced_login_method='+json.dumps(authentication_mode()),'-c','model_provider="openai"',
               '-c','mcp_servers={}','-c','apps={}','-c','plugins={}']
    for feature in DISABLED_FEATURES: command += ['--disable',feature]
    result = {'model_calls':0,'thread_requests':0,'turn_requests':0,'tool_calls':0,'rpc_methods':[],
              'originator_environment_override':None,'scope':'Account metadata only; not model-specific or resumed-turn admission.'}
    process=None; launch=None; birth=None
    try:
        async with asyncio.timeout(RPC_TIMEOUT_SECONDS):
            launch=asyncio.create_task(asyncio.create_subprocess_exec(*command,cwd=cwd,env=route['environment'],
                stdin=-1,stdout=-1,stderr=-3,start_new_session=True,limit=FRAME_LIMIT))
            process=await asyncio.shield(launch); birth=helper_identity(process.pid)
            async def rpc(ident, method, params):
                result['rpc_methods'].append(method)
                process.stdin.write((json.dumps({'id':ident,'method':method,'params':params})+'\n').encode()); await process.stdin.drain()
                while True:
                    line=await process.stdout.readline()
                    if not line or len(line)>FRAME_LIMIT: raise RuntimeError('bounded account RPC frame failure')
                    message=json.loads(line)
                    if message.get('id')==ident:
                        if 'error' in message: raise RuntimeError('account RPC rejected')
                        return message['result']
            await rpc(1,'initialize',{'clientInfo':{'name':'codex_exec','version':'1'}})
            process.stdin.write(b'{"method":"initialized"}\n'); await process.stdin.drain()
            account=await rpc(2,'account/read',{'refreshToken':False})
            limits=await rpc(3,'account/rateLimits/read',{})
            buckets=limits.get('rateLimitsByLimitId')
            if not buckets: buckets={'legacy':limits.get('rateLimits')}
            if not isinstance(buckets,dict): raise ValueError('malformed quota map')
            result.update(account_id=(account.get('workspaceRouting') or {}).get('chatgptAccountId'),
                account_type=(account.get('account') or {}).get('type'),plan_type=(account.get('account') or {}).get('planType'),
                limits_account_id=limits.get('accountId'),buckets={k:sanitize_limit(v) for k,v in buckets.items()})
    except Exception as error: result['error_type']=type(error).__name__
    finally:
        if process is None and launch is not None:
            try: process=await launch; birth=helper_identity(process.pid)
            except Exception: pass
        if process is not None:
            process.stdin.close()
            try:
                await asyncio.wait_for(process.wait(),2); result['cleanup']='exited_after_stdin_close'
            except asyncio.TimeoutError:
                if birth and helper_identity(process.pid)==birth:
                    try: os.killpg(process.pid,signal.SIGKILL)
                    except ProcessLookupError: pass
                    try: await asyncio.wait_for(process.wait(),2); result['cleanup']='owned_group_killed_and_reaped'
                    except asyncio.TimeoutError: result['cleanup']='unknown_reap_timeout'
                else: result['cleanup']='unknown_ownership_no_signal'
            result['helper_pid']=process.pid; result['helper_identity']=birth
        result['auth_unchanged']=outer.sha(auth)==before
    return result


def recheck(folder, route_path):
    import pilot_supervisor as outer
    folder=outer.canonical(folder); route_path=outer.canonical(route_path)
    with outer.owner(folder):
        report=outer.read(folder/'status.json')
        if report.get('status')!='quota_paused': raise ValueError('quota recheck requires a saved quota pause')
        launch=outer.read(folder/'launch.json')
        if launch.get('attempt_sha256') != outer.sha(folder/'attempt.json'): raise ValueError('launch binding changed')
        process=outer.probe_process(launch['pid'],launch.get('process_identity'))
        if process.get('alive') is not False: raise ValueError('host ownership must be reconciled before quota recheck')
        route, root, config=validate_route(folder,route_path)
        stopped_stack(folder,root,route,config,launch)
        deadline=(config.get('exam') or {}).get('submission_deadline_utc')
        if deadline and datetime.fromisoformat(deadline)<=datetime.now(timezone.utc):
            return {'status':'exam_deadline_passed','historical_status':'quota_paused','needs_attention':True,'model_calls':0,'automatic_restart':False}
        corrected=outer.attention(report)
        if corrected != report: outer.save(folder/'status.json',corrected)
        latest=folder/'quota-recheck-last-attempt.json'
        if latest.exists():
            prior=outer.read(latest)
            if prior.get('cleanup_unknown'): raise ValueError('reconcile prior account helper before another recheck')
            age=(datetime.now(timezone.utc)-datetime.fromisoformat(prior['started_utc'])).total_seconds()
            if age<INTERVAL_SECONDS: return {'status':'throttled','needs_attention':True,'model_calls':0,'minimum_interval_seconds':INTERVAL_SECONDS}
        ident=uuid.uuid4().hex; started=outer.now()
        reservation={'id':ident,'started_utc':started,'route_sha256':outer.sha(route_path),'cleanup_unknown':True}
        # A keeper crash during this query blocks automatic repetition until the
        # operator reconciles the exact query attempt; elapsed time is not proof.
        outer.save(latest,reservation)
        receipt={'id':ident,'started_utc':started,'historical_status':'quota_paused','status_sha256':outer.sha(folder/'status.json'),
                 'attempt_sha256':outer.sha(folder/'attempt.json'),'route_sha256':outer.sha(route_path),'model_calls':0}
        try:
            snapshot=asyncio.run(query(route,root.parent))
            # A concurrent manual restart cannot turn this observation into a
            # recovery handoff. No campaign write or model dispatch occurs here.
            stopped_stack(folder,root,route,config,launch)
            metadata=classify(snapshot,route['account_id']) if not snapshot.get('error_type') else 'unknown_query_failure'
            unknown_cleanup=str(snapshot.get('cleanup','unknown')).startswith('unknown')
            if unknown_cleanup: metadata='unknown_helper_ownership'
            receipt.update(snapshot=snapshot,metadata_state=metadata,finished_utc=outer.now())
            deadline=(config.get('exam') or {}).get('submission_deadline_utc')
            expired=bool(deadline and datetime.fromisoformat(deadline)<=datetime.now(timezone.utc))
            handoff={'status':'exam_deadline_passed' if expired else 'saved_state_review_required' if metadata=='metadata_no_limit_observed' else 'quota_pause_unresolved',
                'historical_status':'quota_paused','metadata_state':metadata,'needs_attention':True,
                'observed_utc':receipt['finished_utc'],'model_availability':'UNKNOWN','automatic_restart':False,'scientific_authority':False,
                'exam':config.get('exam'),'required_next_step':'Reconcile processes, in-flight completion and saved work; independently audit an explicitly authorized native continuation with the original session and clock.'}
            receipt['handoff']=handoff
            outer.save(folder/('quota-recheck-'+ident+'.json'),receipt,exclusive=True)
            outer.save(folder/'quota-recovery-handoff.json',{**handoff,'receipt':str(folder/('quota-recheck-'+ident+'.json'))})
            outer.save(latest,{**reservation,'cleanup_unknown':unknown_cleanup,'finished_utc':receipt['finished_utc']})
            return handoff
        except BaseException:
            # The durable reservation remains unknown, preventing a scheduler
            # from blindly repeating a query that may still own a process.
            raise


def recipe(folder, route_path):
    import plistlib
    import pilot_supervisor as outer
    folder=outer.canonical(folder);route_path=outer.canonical(route_path)
    with outer.owner(folder):
        route,root,_=validate_route(folder,route_path)
        if outer.read(folder/'status.json').get('status')!='quota_paused':raise ValueError('quota recipe requires a saved quota pause')
        launch=outer.read(folder/'launch.json')
        if launch.get('attempt_sha256')!=outer.sha(folder/'attempt.json'):raise ValueError('launch binding changed')
        if outer.probe_process(launch['pid'],launch.get('process_identity')).get('alive') is not False:
            raise ValueError('live or uncertain host blocks quota recipe')
        stopped_stack(folder,root,route,outer.read(root/'host-config.json'),launch)
        plan={'route':str(route_path),'route_sha256':outer.sha(route_path),'source':outer.source_binding()}
        outer.save(folder/'quota-recheck-plan.json',plan,exclusive=True)
        value={'Label':'org.merlean.quota.'+outer.digest(str(folder).encode())[:16],
            'ProgramArguments':[sys.executable,'-B',str(outer.SOURCE/'pilot_supervisor.py'),'quota-recheck-scheduled',str(folder)],
            'WorkingDirectory':str(root.parent),'EnvironmentVariables':route['environment'],
            'StartInterval':INTERVAL_SECONDS,'RunAtLoad':True,
            'StandardOutPath':str(folder/'quota-recheck.log'),'StandardErrorPath':str(folder/'quota-recheck-error.log')}
        with (folder/'quota-recheck.plist').open('xb') as stream: plistlib.dump(value,stream)
        return {'status':'recipe_created_not_installed','path':str(folder/'quota-recheck.plist'),'model_calls':0}


def scheduled(folder):
    import pilot_supervisor as outer
    folder=outer.canonical(folder);plan=outer.read(folder/'quota-recheck-plan.json')
    outer.verify_source(plan['source'])
    if outer.sha(plan['route'])!=plan['route_sha256']:raise ValueError('scheduled quota route changed')
    return recheck(folder,Path(plan['route']))
