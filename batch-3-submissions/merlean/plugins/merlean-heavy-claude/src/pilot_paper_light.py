"""Compact, tool-capable exam paper workflow; legacy papers keep their engine.

Independent judgments are model evidence, not a mathematical correctness proof.
The host owns identity, ordering, immutable versions, compilation and deadlines.
"""
from __future__ import annotations
import asyncio
from contextlib import nullcontext
import hashlib
import json
from pathlib import Path
import shutil
import sys

from codex_transport import call_stage, extract_answer
from pilot_exam import PaperDeadline, _write, model_timeout
from pilot_drain import DrainRequested
from pilot_paper import PaperEngine, _validate_tex

ASTRA = 'gpt-6-astra'
SOURCE = Path(__file__).resolve().parent
STAGES = ('draft', 'reader-1', 'revise-1', 'reader-2', 'revise-2', 'verify-2',
          'final-review', 'compile', 'visual')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def regular(path, root):
    path = Path(path)
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError('paper artifact is not an owned regular file')
    return path


def research_handoff(problem, runtime):
    """Revalidate native original-scope completion; never add a redundant model gate."""
    state = problem.pilot.campaign.refresh()
    cell = state['problems'][problem.ident]
    proof = problem.current.get('proof_markdown','')
    accepted = (cell.get('successful_complete') is True
        and cell.get('observations',{}).get('original',{}).get('status') == 'verified'
        and cell.get('evidence_matches_original_answer') is True
        and cell.get('answer_sha256') == hashlib.sha256(proof.encode()).hexdigest())
    if not accepted and runtime.now() < runtime.research_close:
        raise ValueError('early paper handoff requires native accepted original-scope research; return to research/attention')
    return {'kind':'accepted-original-research' if accepted else 'deadline-partial',
        'original_sha256':hashlib.sha256(problem.original_bytes).hexdigest(),
        'answer_sha256':hashlib.sha256(proof.encode()).hexdigest(),
        'manifest_sha256':cell.get('sha256') if accepted else None,
        'research_acceptance':'unchanged',
        'instruction':'Write the exact supported original answer.' if accepted else
            'Research is NOT complete. Write an honest partial/unsolved answer to the ORIGINAL problem only.'}


class LightPaper:
    command = PaperEngine.command

    def __init__(self, problem, snapshot, runtime):
        self.problem, self.runtime = problem, runtime
        self.root = runtime.paper_dir(problem.ident)
        self.snapshot = Path(snapshot)
        self.work = self.root/'light-host'
        self.author = self.root/'author'
        self.output = self.author/'paper.tex'
        self.state_path = self.root/'light-paper-ledger.json'
        if (self.root/'paper-ledger.json').exists():
            raise ValueError('lightweight policy cannot migrate a legacy paper ledger')
        self.work.mkdir(exist_ok=True)
        self.author.mkdir(exist_ok=True)
        runtime.verify_snapshot(self.snapshot)
        binding = sha(self.snapshot/'manifest.json')
        if self.state_path.exists():
            self.state = read(self.state_path)
            if self.state.get('snapshot_sha256') != binding or self.state.get('engine') != 'lightweight-v1':
                raise ValueError('saved lightweight paper evidence changed')
        else:
            self.state = {'engine':'lightweight-v1', 'snapshot_sha256':binding,
                'stage':'draft', 'writer':None, 'identities':[], 'calls':[],
                'reviews':{}, 'dispositions':{}, 'repairs':0, 'errors':[], 'pending':None}
            self.save()
        snapshot_data = read(self.snapshot/'snapshot.json')
        if (self.snapshot/'input.txt').read_bytes() != problem.original_bytes:
            raise ValueError('paper snapshot question differs from the immutable original problem')
        self.evidence = {'question':(self.snapshot/'input.txt').read_text(),
            'current':snapshot_data['current'], 'dossier':snapshot_data['dossier'],
            'findings':snapshot_data['findings'], 'research_status':snapshot_data['research_status'],
            'archive':'evidence/', 'archive_manifest_sha256':binding,
            'handoff':research_handoff(problem,runtime)}
        self.state['scope'] = self.evidence['handoff']
        self.save()
        self.policy = PaperEngine.policy(self, 'workflows/paper/lightweight.md')
        self.reader_policy = PaperEngine.policy(self, 'workflows/paper/lightweight-reader.md')

    def save(self):
        _write(self.state_path, self.state)

    def manuscript(self):
        regular(self.output, self.author)
        text = self.output.read_text()
        _validate_tex(text)
        return text

    def version(self):
        text = self.manuscript()
        digest = sha(self.output)
        target = self.work/(digest+'.tex')
        if target.exists() and target.read_text() != text:
            raise ValueError('immutable paper version changed')
        if not target.exists():
            target.write_text(text)
            target.chmod(0o444)
        return digest

    def result(self, status, terminal=False):
        return {'engine':'lightweight-v1', 'status':status, 'terminal':terminal,
            'polishing_complete':status == 'polished', 'research_acceptance':'unchanged',
            'best_available_tex':str(self.root/'paper.tex') if (self.root/'paper.tex').is_file() else str(self.root/'unresolved.tex'),
            'best_available_pdf':str(self.root/'final.pdf') if (self.root/'final.pdf').is_file() else None,
            'ledger':str(self.state_path), 'errors':self.state['errors']}

    async def call(self, stage, task, *, resume=None, workspace=None, online=False, images=None):
        """Reconcile the exact completed transport before any new admission."""
        pending = self.state['pending']
        pilot = self.problem.pilot
        if pending:
            if pending['stage'] != stage or pending['resume'] != resume:
                raise ValueError('pending paper call differs from saved stage/session')
            name = pending['name']
            folder = pilot.host/'runtime'/name
            meta_file = folder/'stage.meta.json'
            answer_file = folder/'stage.answer.json'
            if not meta_file.is_file() or not answer_file.is_file():
                raise RuntimeError('unreconciled admitted paper call; native stopped ownership recovery required')
            meta, answer = read(meta_file), read(answer_file)
            raw = regular(folder/'stage.answer.txt',folder).read_text()
            if sha(folder/'stage.answer.txt') != meta.get('answer_sha256') or extract_answer(raw)[0] != answer:
                raise ValueError('saved completed paper answer changed')
            if meta.get('name') != name:
                raise ValueError('saved paper producer name changed')
        else:
            self.runtime.paper_timeout(1)
            name = f'{self.problem.ident}/paper-{len(self.state["calls"])+1:03d}-light-{stage}'
            prompt = self.policy+'\nTASK\n'+task
            async with pilot.semaphore:
                drain = getattr(pilot, 'drain', None)
                with drain.admission('stage', name) if drain else nullcontext():
                    allowance = model_timeout(self.runtime, pilot.config, 'paper', 900)
                    self.state['pending'] = {'stage':stage, 'name':name, 'resume':resume,
                        'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(), 'prompt_chars':len(prompt),
                        'images':[{ 'sha256':sha(p)} for p in (images or [])],
                        'input_sha256':None if workspace == self.author else (self.version() if self.output.exists() else None),
                        'module':('paper-visual-review' if images is not None else 'paper-light-author' if workspace == self.author else 'paper-light-review' if workspace is not None else 'paper-light-'+stage)}
                    self.save()
                    if hasattr(pilot, 'drain_stage_names'): pilot.drain_stage_names.add(name)
                    active = getattr(self.problem, 'active_stages', set())
                    active.add(name); self.problem.active_stages = active
                    self.problem.active_stage = min(active)
                    self.problem.status('running:paper-light-'+stage)
                    extra = {'accounting_context':{'phase':'exam-paper',
                        'segment_id':str(pilot.config.get('accounting_segment_id') or 'exam-paper'),
                        'purpose':'paper-light-'+stage}}
                    if pilot.config.get('accounting_price_card'):
                        extra['accounting_price_card'] = pilot.root/pilot.config['accounting_price_card']['path']
                    if workspace is not None:
                        self.runtime.verify_snapshot(self.snapshot)
                        extra['paper_workspace'] = workspace
                        extra['paper_evidence_root'] = self.snapshot
                    if images is not None: extra['image_paths'] = images
                    module = ('paper-visual-review' if images is not None else
                        'paper-light-author' if workspace == self.author else
                        'paper-light-review' if workspace is not None else 'paper-light-'+stage)
                    try:
                        meta, answer = await call_stage(pilot.host, name, prompt, ASTRA, allowance, resume,
                            internet_browse=online, codex_binary=pilot.config.get('codex_binary','codex'),
                            module=module, **extra)
                    finally:
                        active.discard(name)
                        self.problem.active_stage = min(active) if active else None
        pending = self.state['pending']
        self.runtime.verify_snapshot(self.snapshot)
        if meta.get('status') != 'completed':
            raise ValueError('paper transport did not complete: ' + str(meta.get('status')))
        if workspace == self.author:
            expected = meta.get('paper_workspace_files')
            actual = {str(p.relative_to(self.author)):sha(regular(p,self.author)) for p in self.author.rglob('*') if p.is_file() or p.is_symlink()}
            if not expected or expected != actual:
                raise ValueError('completed author workspace differs from transport artifact binding')
        prompt_ok = meta.get('prompt_sha256') == pending['prompt_sha256']
        if pending.get('images'):
            saved = (pilot.host/'runtime'/pending['name']/'stage.prompt.txt').read_text()
            prompt_ok = (hashlib.sha256(saved[:pending['prompt_chars']].encode()).hexdigest() == pending['prompt_sha256']
                and sha(pilot.host/'runtime'/pending['name']/'stage.prompt.txt') == meta.get('prompt_sha256')
                and [x['sha256'] for x in meta.get('paper_image_inputs',[])] == [x['sha256'] for x in pending['images']])
        if pending.get('input_sha256') is not None and self.version() != pending['input_sha256']:
            raise ValueError('saved reviewer input changed before reconciliation')
        if (meta.get('status') != 'completed' or meta.get('model_actual') != ASTRA
                or meta.get('model_verified') is not True or not meta.get('session_id')
                or meta.get('resume_session') != resume or meta.get('module') != pending['module']
                or not prompt_ok):
            raise ValueError('paper call lacks exact successful model/session/prompt binding')
        identity = meta['session_id']
        if resume and identity != resume:
            raise ValueError('paper resumed another conversation')
        if not resume and identity in self.state['identities'] and identity != pending.get('meta',{}).get('session_id'):
            raise ValueError('fresh paper reviewer reused a writer/reviewer')
        if not isinstance(answer, dict):
            raise ValueError('paper response must be a JSON object')
        # Keep completed response pending until its stage effects are checkpointed.
        self.state['pending'].update(meta=meta, answer=answer)
        return identity, answer

    async def compile(self, source, label):
        # Execute the same confined fixed compiler as the scoped author tool.
        timeout = self.runtime.paper_timeout(100)
        code, stdout, stderr = await self.command([sys.executable, str(SOURCE/'pilot_paper_tools.py'),
            '--compile', str(source), '--pdf-output', str(self.root/(label+'.pdf')),
            '--timeout', str(max(1,int(timeout)))], timeout)
        try:
            report = json.loads(stdout)
        except ValueError:
            report = {'pass':False,'error':stderr or stdout}
        _write(self.work/(label+'-compile.json'),report)
        if code or report.get('pass') is not True or not isinstance(report.get('pdf_pages'),int):
            raise ValueError('confined paper compilation failed: '+str(report))
        return report

    def advance(self, stage):
        pending = self.state['pending']
        if pending:
            meta = pending['meta']
            self.state['calls'].append(meta)
            if meta['session_id'] not in self.state['identities']: self.state['identities'].append(meta['session_id'])
            if not any(c.get('name') == meta['name'] for c in self.problem.calls):
                self.problem.calls.append(meta)
            _write(self.problem.folder/(meta['name'].rsplit('/',1)[-1]+'.json'), pending['answer'])
        self.state['pending'] = None
        self.state['stage'] = stage
        self.save()
        self.problem.status('paper-light-checkpoint:'+stage)

    async def author_turn(self, stage, feedback=None):
        task = ('Write/edit paper.tex in your workspace. Use the scoped paper file tools to compose and inspect it; use the provided fixed compiler when available. '
            'Use merlean_paper.list_files/read_file/write_file/compile_paper; no shell tool is provided. '
            'Public source tools fetch_public_source/read_public_source and native web are available when enabled. '
            'Read immutable archive members with read_file path evidence/<relative>; no absolute path reads. '
            'Keep source text and bibliographic exports in references/. Return only '
            '{"summary":"what you changed or why unchanged"}; do not echo the manuscript. '
            'Read selected-evidence.json for the exact question/current supported proof/hypotheses/findings. '
            'Historical evidence is available in the evidence/ tool namespace if needed. '
            'Do not modify host state, research, independent reports or snapshot.\n')
        if self.state['pending'] is None:
            _write(self.author/'selected-evidence.json', self.evidence)
        task += '\nSUBSTANTIVE MATHEMATICAL WRITING GUIDANCE (lightweight protocol overrides legacy file instructions):\n'+PaperEngine.policy(self, 'workflows/paper/mathematical-writing.md')
        if feedback is not None: task += 'Located independent feedback / diagnostic:\n'+json.dumps(feedback)
        identity, answer = await self.call(stage, task, resume=self.state['writer'],
            workspace=self.author, online=self.problem.pilot.config.get('internet_browse',True))
        if not isinstance(answer.get('summary'), str) or not answer['summary'].strip():
            raise ValueError('author must return substantive disposition')
        self.state['dispositions'][stage] = answer
        self.state['writer'] = identity
        self.state['manuscript_sha256'] = self.version()
        (self.root/'paper.tex').write_text(self.manuscript())

    async def review(self, stage, *, resume=None, final=False):
        digest = self.version()
        task = ('Independently read the complete manuscript. The fresh reader first pass receives no author notes, '
            'research history or earlier reviewer opinions. Return JSON '
            '{"verdict":"PASS or FAIL","findings":[{"location":"specific section/claim",'
            '"issue":"precise problem", "required_change":"needed correction"}],'
            '"assessment":"substantive explanation"}. PASS means no unresolved material issue. '
            'Do not manufacture criticism or waive gaps.\n'+self.reader_policy+'\nMANUSCRIPT\n'+self.manuscript())
        workspace = None
        if stage == 'verify-2':
            task += '\nVerify both reader rounds and the author dispositions on this exact final manuscript:\n'+json.dumps({'reviews':self.state['reviews'],'dispositions':self.state['dispositions']})
        if final:
            workspace = self.work/('review-'+digest+'-'+str(len(self.state['calls'])+1))
            workspace.mkdir(exist_ok=True)
            (workspace/'paper.tex').write_text(self.manuscript())
            _write(workspace/'selected-evidence.json', self.evidence)
            refs = self.author/'references'
            if refs.exists():
                for path in refs.rglob('*'):
                    if path.is_symlink(): raise ValueError('reference cache symlink forbidden')
                    if path.is_file():
                        target = workspace/'references'/path.relative_to(refs)
                        target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(path,target)
            task += ('\nIndependently compare exact selected research evidence, hypotheses and proof steps. '
                'Verify cited claims/use-sites against actual primary PDF/TeX content and bibliographic metadata, '
                'including relevant arXiv work on both the central problem and methods. '
                'Also return original_scope_verdict: PASS or FAIL and scope_assessment explicitly comparing original '
                'objects, quantifiers, hypotheses and conclusion against the manuscript. A different problem '
                'cannot PASS, including in an honest partial report. '
                'Read supplied sources and use public tools for targeted verification as needed. '
                'Unverified essential source claims cannot PASS. Optional unavailable sources must be disclosed '
                'without invented citations. Do not modify files. Evidence is in selected-evidence.json/references/.')
        identity, answer = await self.call(stage, task, resume=resume, workspace=workspace,
            online=bool(final and self.problem.pilot.config.get('internet_browse',True)))
        if self.version() != digest:
            raise ValueError('manuscript changed during independent review')
        if (answer.get('verdict') not in ('PASS','FAIL') or not isinstance(answer.get('findings'),list)
                or not isinstance(answer.get('assessment'),str) or not answer['assessment'].strip()
                or (answer['verdict']=='PASS' and answer['findings'])):
            raise ValueError('independent review lacks explicit verdict/located findings/assessment')
        if final and (answer.get('original_scope_verdict') not in ('PASS','FAIL')
                or not isinstance(answer.get('scope_assessment'),str) or not answer['scope_assessment'].strip()):
            raise ValueError('final reviewer must explicitly verify original problem correspondence')
        for finding in answer['findings']:
            if not isinstance(finding,dict) or not all(isinstance(finding.get(k),str) and finding[k].strip()
                    for k in ('location','issue','required_change')):
                raise ValueError('review findings must be located and actionable')
        self.state['reviews'][stage] = {'session':identity, 'source_sha256':digest, 'report':answer, 'call':self.state['pending']['name'],
            'workspace':workspace.name if workspace is not None else None}
        return answer

    async def run(self):
        while True:
            stage = self.state['stage']
            if stage == 'complete':
                self.validate_complete()
                return self.result('polished',True)
            self.runtime.paper_timeout(1)
            if stage == 'scope-blocked':
                return self.result('original-scope-mismatch')
            elif stage == 'draft':
                await self.author_turn(stage); self.advance('reader-1')
            elif stage in ('reader-1','reader-2'):
                await self.review(stage)
                self.advance('revise-'+stage[-1])
            elif stage in ('revise-1','revise-2'):
                await self.author_turn(stage,self.state['reviews']['reader-'+stage[-1]])
                self.advance('reader-2' if stage=='revise-1' else 'verify-2')
            elif stage == 'verify-2':
                answer = await self.review(stage,resume=self.state['reviews']['reader-2']['session'])
                if answer['verdict'] == 'FAIL': await self.repair(answer)
                else: self.advance('final-review')
            elif stage == 'final-review':
                answer = await self.review(stage,final=True)
                if answer.get('original_scope_verdict') == 'FAIL':
                    self.advance('scope-blocked')
                elif answer['verdict'] == 'FAIL': await self.repair(answer)
                else: self.advance('compile')
            elif stage == 'repair':
                await self.author_turn(stage,self.state['repair_feedback'])
                # Any correction is checked by two new independent readers; no old PASS transfer.
                self.state['reviews'] = {}
                self.advance('reader-1')
            elif stage == 'compile':
                try:
                    report = await self.compile(self.output,'final')
                    if report['pdf_pages'] > self.runtime.config['page_limit']:
                        raise ValueError('compiled paper exceeds page limit; remove redundancy, not key steps')
                    self.state['compiled'] = {'source_sha256':self.version(),'pdf_sha256':sha(self.root/'final.pdf'), 'pages':report['pdf_pages']}
                    self.advance('visual')
                except ValueError as error: await self.repair({'compilation':str(error)})
            elif stage == 'visual':
                images_dir=self.work/'render'; images_dir.mkdir(exist_ok=True)
                code,_,error=await self.command(['pdftoppm','-png','-r','80',str(self.root/'final.pdf'),str(images_dir/'page')],120)
                images=sorted(images_dir.glob('page-*.png'))
                if code or len(images)!=self.state['compiled']['pages']: raise ValueError('complete PDF rendering failed: '+error)
                _,answer=await self.call(stage,'Inspect every rendered page for clipping, unreadable mathematics, missing glyphs and layout errors. Return {"verdict":"PASS or FAIL","assessment":"specific observations"}.',images=images)
                if not isinstance(answer.get('assessment'),str) or not answer['assessment'].strip():
                    raise ValueError('visual review must supply actual observations')
                if answer.get('verdict') != 'PASS': await self.repair({'visual':answer})
                else:
                    if (self.version()!=self.state['compiled']['source_sha256'] or sha(self.root/'final.pdf')!=self.state['compiled']['pdf_sha256']):
                        raise ValueError('compiled or reviewed artifact changed')
                    self.state['visual'] = {'source_sha256':self.version(),'report':answer,'call':self.state['pending']['name']}
                    self.advance('complete')
            else: raise ValueError('unknown lightweight paper stage')

    def validate_complete(self):
        self.manuscript()
        digest = sha(self.output)
        if sha(regular(self.work/(digest+'.tex'),self.work)) != digest:
            raise ValueError('immutable reviewed paper version changed')
        if self.state.get('scope',{}).get('kind') not in ('accepted-original-research','deadline-partial'):
            raise ValueError('original research handoff unavailable')
        if sha(regular(self.root/'paper.tex',self.root)) != digest:
            raise ValueError('published paper source differs from reviewed author manuscript')
        compiled = self.state.get('compiled',{})
        if (compiled.get('source_sha256') != digest or compiled.get('pdf_sha256') != sha(regular(self.root/'final.pdf',self.root))
                or not 0 < compiled.get('pages',0) <= self.runtime.config['page_limit']):
            raise ValueError('completed compiled artifact binding changed')
        if self.state['reviews']['final-review']['report'].get('original_scope_verdict') != 'PASS':
            raise ValueError('final original problem correspondence did not pass')
        for record in [*self.state['reviews'].values(), self.state['visual']]:
            self.authenticate_review(record)
        for stage in ('verify-2','final-review'):
            record = self.state['reviews'].get(stage,{})
            if record.get('source_sha256') != digest or record.get('report',{}).get('verdict') != 'PASS':
                raise ValueError('completed paper lacks current independent verification')
        readers = [self.state['reviews'].get(s,{}).get('session') for s in ('reader-1','reader-2','final-review')]
        if not all(readers) or len(set(readers)) != 3 or self.state['writer'] in readers:
            raise ValueError('completed paper reviewer independence changed')
        if self.state['reviews']['verify-2']['session'] != readers[1]:
            raise ValueError('second-reader verification identity changed')
        if self.state.get('visual',{}).get('source_sha256') != digest or self.state['visual']['report'].get('verdict') != 'PASS':
            raise ValueError('completed paper lacks current visual inspection')

    def authenticate_review(self, record):
        folder = self.problem.pilot.host/'runtime'/record['call']
        meta = read(regular(folder/'stage.meta.json',folder))
        raw = regular(folder/'stage.answer.txt',folder).read_text()
        if record.get('source_sha256') and meta.get('module') != 'paper-visual-review':
            prompt = regular(folder/'stage.prompt.txt',folder)
            if sha(prompt) != meta.get('prompt_sha256'):
                raise ValueError('independent reviewer prompt changed')
            frozen = self.work/(record['source_sha256']+'.tex')
            if regular(frozen,self.work).read_text() not in prompt.read_text():
                raise ValueError('reviewer prompt does not contain its complete bound manuscript')
        if meta.get('module') == 'paper-light-review':
            workspace = self.work/record['workspace']
            if workspace.resolve().parent != self.work.resolve() or workspace.is_symlink():
                raise ValueError('final reviewer workspace escapes host scope')
            actual = {str(p.relative_to(workspace)):sha(regular(p,workspace)) for p in workspace.rglob('*') if p.is_file() or p.is_symlink()}
            if actual != meta.get('paper_workspace_files'):
                raise ValueError('final reviewer evidence workspace changed')
        if (sha(folder/'stage.answer.txt') != meta.get('answer_sha256')
                or extract_answer(raw)[0] != record['report'] or meta.get('status') != 'completed'
                or meta.get('model_actual') != ASTRA or meta.get('model_verified') is not True
                or meta.get('name') != record['call']
                or (record.get('session') and meta.get('session_id') != record['session'])):
            raise ValueError('independent paper judgment no longer matches authenticated transport')

    async def repair(self, diagnostic):
        if self.state['repairs'] >= 4:
            raise RuntimeError('four contextual paper repairs exhausted; preserve incomplete artifact')
        self.state['repairs'] += 1
        self.state['repair_feedback'] = diagnostic
        self.advance('repair')


async def run_exam_paper(problem, snapshot_dir, exam_runtime):
    engine = LightPaper(problem,snapshot_dir,exam_runtime)
    try:
        return await engine.run()
    except (DrainRequested, asyncio.CancelledError):
        raise
    except PaperDeadline:
        return engine.result('deadline-partial',True)
    except Exception as error:
        engine.state['errors'].append({'type':type(error).__name__,'message':str(error),'stage':engine.state['stage']})
        engine.save()
        return engine.result('incomplete')


def verify_completed(folder, host, page_limit=16):
    """Read-only release check for native observation/export, no model or rebuild."""
    from types import SimpleNamespace
    engine = object.__new__(LightPaper)
    engine.root = Path(folder)
    engine.work = engine.root/'light-host'
    engine.author = engine.root/'author'
    engine.output = engine.author/'paper.tex'
    engine.state = read(regular(engine.root/'light-paper-ledger.json',engine.root))
    engine.problem = SimpleNamespace(pilot=SimpleNamespace(host=Path(host)))
    engine.runtime = SimpleNamespace(config={'page_limit':page_limit})
    if engine.state.get('engine') != 'lightweight-v1' or engine.state.get('stage') != 'complete':
        raise ValueError('lightweight paper has not completed')
    engine.validate_complete()
    return {'status':'PASS','source_sha256':sha(engine.output),'pdf_sha256':sha(engine.root/'final.pdf')}
