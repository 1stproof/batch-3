"""Small paper-only MCP file capability; no shell, arbitrary paths, or research writes."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys

SERVER='merlean_paper'
NAMESPACE='mcp__merlean_paper'
TOOLS=('list_files','read_file','write_file','compile_paper','fetch_public_source','read_public_source')

def digest(data): return hashlib.sha256(data).hexdigest()
def definitions(role):
    def tool(name,description,props,required):
        return {'name':name,'description':description,'inputSchema':{'type':'object','properties':props,'required':required,'additionalProperties':False}}
    result=[tool('list_files','List paper workspace relative files.',{},[]),tool('read_file','Read a UTF-8 paper workspace file in character ranges.',{'path':{'type':'string'},'start':{'type':'integer','minimum':0},'end':{'type':'integer','minimum':0}},['path'])]
    if role=='author':result.append(tool('write_file','Replace paper.tex or a references/ text file; no other writes.',{'path':{'type':'string'},'text':{'type':'string'}},['path','text']))
    if role=='author':result.append(tool('compile_paper','Compile paper.tex using fixed host compiler; returns diagnostics, never acceptance.',{},[]))
    result += [tool('fetch_public_source','Fetch a public mathematical source into verified cache (online only).',{'url':{'type':'string'}},['url']),tool('read_public_source','Read a verified cached public source member.',{'source_id':{'type':'string'},'member':{'type':'string'},'start':{'type':'integer'},'end':{'type':'integer'}},['source_id'])]
    return result

def compile_paper(path,pdf_destination=None,timeout=60):
    """Native Linux compiler with public installation reads and scratch-only writes."""
    import tempfile,subprocess,shutil,resource,time
    from pilot_paper import _validate_tex
    from offline_probe_linux import Policy
    text=_validate_tex(path.read_text())
    binary=Path(shutil.which('pdflatex') or '/nonexistent').resolve(strict=True)
    roots=[Path(p) for p in ('/usr/share/texlive','/usr/share/texmf','/var/lib/texmf','/etc/texmf','/usr/share/fonts','/usr/share/tex-common') if Path(p).is_dir()]
    with tempfile.TemporaryDirectory(prefix='paper-tool-compile-') as folder:
        scratch=Path(folder);(scratch/'paper.tex').write_text(text)
        policy=Policy(binary,roots+[scratch]);policy.grants.append((scratch,((1<<15)-1)&~1))
        def confine():
            resource.setrlimit(resource.RLIMIT_FSIZE,(32*1024*1024,32*1024*1024))
            resource.setrlimit(resource.RLIMIT_CPU,(45,45));policy()
        environment={'PATH':'/usr/bin:/bin','HOME':folder,'TMPDIR':folder,'openin_any':'p','openout_any':'p','TEXMFVAR':folder,'TEXMFCONFIG':folder}
        deadline=time.monotonic()+max(1,min(60,timeout))
        for _ in range(2):
            process=subprocess.run([str(binary),'-progname=pdflatex','-fmt=pdflatex','-no-shell-escape','-halt-on-error','-interaction=nonstopmode','paper.tex'],cwd=scratch,env=environment,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=max(0.01,deadline-time.monotonic()),preexec_fn=confine,close_fds=True)
            if process.returncode:break
        log=(scratch/'paper.log').read_text(errors='replace')[-16000:] if (scratch/'paper.log').is_file() else ''
        passed=process.returncode==0 and (scratch/'paper.pdf').is_file()
        pages=None
        if passed:
            info=subprocess.run(['pdfinfo',str(scratch/'paper.pdf')],env=environment,capture_output=True,text=True,timeout=10)
            import re
            match=re.search(r'^Pages:\s+(\d+)',info.stdout,re.MULTILINE)
            if info.returncode or not match:passed=False
            else:pages=int(match[1])
        if passed and pdf_destination is not None:
            destination=Path(pdf_destination)
            if destination.is_symlink():raise ValueError('PDF destination link')
            destination.write_bytes((scratch/'paper.pdf').read_bytes())
        return {'pass':passed,'pdf_pages':pages,'source_sha256':digest(text.encode()),'returncode':process.returncode,'diagnostic':log,'authority':'compiler diagnostics only; no scientific acceptance'}

class PaperTools:
    def __init__(self,scope):
        self.scope=scope;self.root=Path(scope['workspace'])
        if scope['role'] not in ('author','review') or self.root.resolve(strict=True)!=self.root or not self.root.is_dir():raise ValueError('invalid paper capability')
    def path(self,name,write=False):
        if not isinstance(name,str) or not name or Path(name).is_absolute() or any(x in ('..','.') for x in name.split('/')):raise ValueError('invalid relative path')
        if write and not (name=='paper.tex' or (name.startswith('references/') and Path(name).suffix in {'.txt','.md','.tex','.bib'})):raise ValueError('write outside author files')
        if name.startswith('evidence/'):
            if write:raise ValueError('immutable evidence')
            relative=name[len('evidence/'):];entry=self.scope.get('evidence_files',{}).get(relative)
            if entry is None:raise ValueError('unknown immutable evidence')
            path=Path(self.scope['evidence_root'])/relative
            if path.resolve(strict=True)!=path or not path.is_file() or path.stat().st_nlink!=1 or digest(path.read_bytes())!=entry:raise ValueError('immutable evidence changed')
            return path
        path=self.root/name
        for parent in [path,*path.parents]:
            if parent==self.root:break
            if parent.is_symlink():raise ValueError('link forbidden')
        if path.exists() and (not path.is_file() or path.stat().st_nlink!=1):raise ValueError('not regular single-link file')
        if not path.resolve().is_relative_to(self.root):raise ValueError('outside workspace')
        return path
    def call(self,name,args,ident):
        try:
            if name=='list_files' and not args:
                result={'files':[str(p.relative_to(self.root)) for p in sorted(self.root.rglob('*')) if p.is_file() and not p.is_symlink()]+['evidence/'+name for name in sorted(self.scope.get('evidence_files',{}))]}
            elif name=='read_file' and set(args)<= {'path','start','end'}:
                path=self.path(args['path']);fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
                with os.fdopen(fd,'rb') as stream:data=stream.read()
                if args['path'].startswith('evidence/') and digest(data)!=self.scope['evidence_files'][args['path'][9:]]:raise ValueError('immutable evidence changed during read')
                text=data.decode('utf-8');start=args.get('start',0);end=args.get('end',len(text))
                if type(start)!=int or type(end)!=int or not 0<=start<=end<=len(text):raise ValueError('invalid range')
                result={'path':args['path'],'sha256':digest(data),'start':start,'end':end,'characters':len(text),'text':text[start:end]}
            elif name=='write_file' and self.scope['role']=='author' and set(args)=={'path','text'} and isinstance(args['text'],str):
                path=self.path(args['path'],True);path.parent.mkdir(parents=True,exist_ok=True)
                path=self.path(args['path'],True);data=args['text'].encode()
                fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_TRUNC|os.O_NOFOLLOW,0o600)
                with os.fdopen(fd,'wb') as stream:stream.write(data);stream.flush();os.fsync(stream.fileno())
                result={'path':args['path'],'sha256':digest(data),'bytes':len(data)}
            elif name=='compile_paper' and self.scope['role']=='author' and not args:
                result=compile_paper(self.path('paper.tex'))
            elif name=='fetch_public_source' and self.scope['online'] and set(args)=={'url'}:
                from pilot_public_sources import fetch_public_source
                result=fetch_public_source(self.scope['public_store'],args['url'])
            elif name=='read_public_source' and set(args)<= {'source_id','member','start','end'}:
                from pilot_public_sources import read_public_source
                result=read_public_source(self.scope['public_store'],**args)
            else:raise ValueError('unsupported paper operation')
            receipt={'request_id':ident,'tool':name,'arguments_sha256':digest(json.dumps(args,sort_keys=True).encode()),'result_sha256':digest(json.dumps(result,sort_keys=True).encode()),'status':'PASS'}
            with Path(self.scope['receipt_path']).open('a') as stream:stream.write(json.dumps(receipt)+'\n')
            return {'content':[{'type':'text','text':json.dumps(result)}]}
        except (OSError,ValueError,KeyError,TypeError,subprocess.SubprocessError):return {'isError':True,'content':[{'type':'text','text':'Paper capability rejected operation'}]}

def prepare(workspace,role,artifact,online=False,evidence_root=None,paper_root=None):
    data=Path(__file__).read_bytes();server=artifact/'paper-tools.py';server.write_bytes(data)
    scope={'workspace':str(workspace),'role':role,'receipt_path':str(artifact/'paper-operations.jsonl'),'online':online,'public_store':str((Path(paper_root) if paper_root else workspace.parent)/'public-sources'),'python_path':str(Path(__file__).parent)}
    if evidence_root is not None:
        from codex_transport import paper_workspace_files
        scope.update(evidence_root=str(evidence_root),evidence_files=paper_workspace_files(evidence_root))
    raw=json.dumps(scope,sort_keys=True).encode();path=artifact/'paper-capability.json';path.write_bytes(raw)
    return {'server':str(server),'server_sha256':digest(data),'path':str(path),'sha256':digest(raw)}
def config(capability):
    if digest(Path(capability['server']).read_bytes())!=capability['server_sha256'] or digest(Path(capability['path']).read_bytes())!=capability['sha256']:raise ValueError('paper capability changed')
    return 'mcp_servers={merlean_paper={command='+json.dumps(sys.executable)+',args='+json.dumps(['-B',capability['server'],'--scope',capability['path'],'--sha256',capability['sha256']])+',required=true,default_tools_approval_mode="approve"}}'
def main():
    p=argparse.ArgumentParser();p.add_argument('--scope');p.add_argument('--sha256');p.add_argument('--compile');p.add_argument('--pdf-output');p.add_argument('--timeout',type=int,default=60);a=p.parse_args()
    if a.compile:
        print(json.dumps(compile_paper(Path(a.compile),a.pdf_output,a.timeout)));return
    if not a.scope or not a.sha256:p.error('scope and sha256 required')
    raw=Path(a.scope).read_bytes()
    if digest(raw)!=a.sha256:raise ValueError('changed capability')
    scope=json.loads(raw);sys.path.insert(0,scope['python_path']);server=PaperTools(scope)
    for line in sys.stdin:
        request=json.loads(line)
        if 'id' not in request:continue
        method=request.get('method')
        if method=='initialize':result={'protocolVersion':'2025-06-18','capabilities':{'tools':{}},'serverInfo':{'name':SERVER,'version':'1'}}
        elif method=='tools/list':result={'tools':definitions(server.scope['role'])}
        elif method=='tools/call':result=server.call(request['params'].get('name'),request['params'].get('arguments',{}),request['id'])
        elif method=='ping':result={}
        else:result={}
        print(json.dumps({'jsonrpc':'2.0','id':request['id'],'result':result}),flush=True)
if __name__=='__main__':main()
