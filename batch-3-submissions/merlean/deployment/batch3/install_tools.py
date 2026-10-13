import json,sys,subprocess,hashlib,pathlib,os
arch=sys.argv[1];assets=json.loads(pathlib.Path('/opt/environment/release-lock.json').read_text())[arch]
for name in ('lean','codex'):
 item=assets[name];archive=pathlib.Path('/tmp/'+name+'.tar.zst')
 subprocess.run(['curl','--fail','--location','--connect-timeout','20','--max-time','600','--retry','0','-o',str(archive),item['url']],check=True)
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==item['digest'].split(':',1)[1]
 target=pathlib.Path('/opt')/name;target.mkdir()
 args=['tar','--zstd','-xf',str(archive),'-C',str(target)]
 if name=='lean':args+=['--strip-components=1']
 subprocess.run(args,check=True);archive.unlink()
 if name=='codex':
  candidates=[p for p in target.rglob('codex') if p.is_file() and os.access(p,os.X_OK)]
  assert len(candidates)==1, candidates
  pathlib.Path('/usr/local/bin/codex').symlink_to(candidates[0])
  print('CODEX_ENTRYPOINT',candidates[0],flush=True)
subprocess.run(['/opt/lean/bin/lean','--version'],check=True)
subprocess.run(['/usr/local/bin/codex','--version'],check=True)
