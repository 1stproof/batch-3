# Exam execution and delivery

Research convergence is enabled by default in every mode. The exam profile adds a
shared deadline and a separate paper-writing phase. Ordinary research remains uncapped
by this profile.
An exam timer is an operational constraint, never a proof or grade rule.

## Official Batch 3 requirements

The [First Proof Batch 3 call for submissions](https://1stproof.org/assets/docs/batch3-call-for-submissions.pdf)
specifies at most **24 hours of wall-clock time for the system receiving all ten
problems**, and ten LaTeX solution documents of **at most 16 pages each**. Its
12-page figure concerns human problem selection, not the system's solution limit.
Correctness, exposition and attribution are scored separately; incorrect answers
can receive negative correctness scores compared with blank answers.

Our fresh-run default writing transition is at **hour 22.75 of that shared clock**, reserving
the final 75 minutes for writing and delivery. This is a scheduling default, not an
official requirement or a guarantee of completion within the reserve. Independently
accepted research may enter paper writing earlier; pending problems enter at the
shared research deadline. Call durations include tools and provider waiting, not
just model computation.
A problem started late inherits the same deadline. Resuming a process or continuing
a campaign must not grant another 22.75 or 24 hours. Saved clocks and explicit overrides stay unchanged.

## Select and launch

`scripts/merlean-agent --exam` selects the profile and reports the applicable runtime
entrypoint. Like other selector flags it launches no model and starts no timer.
The executable Codex Lite host defaults to exam mode on a fresh `--problems` run;
`--exam` remains an explicit spelling of that default:

```sh
scripts/merlean-codex-pilot /outside/tool/tree/exam \
  --problems /outside/tool/tree/originals.json --exam \
  --internet-browse on --codex /absolute/path/to/audited/codex
```

Public internet access is on by default for a fresh exam. Search or download only
when it resolves a concrete research or attribution need; an unavailable optional
source must not stall the run. An explicit offline choice remains available.
New paper runs still require the relevance-search/read gate in
`workflows/paper/references.md`. A blocked search allows other drafting work to continue,
not a claim that final literature checks passed. Reuse valid cached evidence where possible.

The existing Codex host's authentication, tool and platform constraints still apply;
this feature does not claim deployment of an AWS/API competition container. The
selector exposes the same profile contract for other modes/providers, but does not
pretend to supply an automatic runtime where none is implemented. Standalone
`paperctl --profile exam` controls writing policy; it does not independently start
the whole-exam timer.

Existing started runs retain their frozen policy. Do not enable exam mode by mutating
a live configuration or silently reinterpret an old run's start time.
Existing-run, continuation, and watchdog-inspection commands reject both mode flags
and new exam-hour options; they do not start a new clock. On a fresh run,
`--exam-research-hours` and `--exam-total-hours` may configure the default exam clock.
Use `--no-exam` to opt out on a fresh run. It also permits an optional `--minutes N`
allowance; `--minutes` without explicit `--no-exam` is an error.

Paper recovery preserves its saved workflow stage, writer/reviewer sessions and
completed steps. Transport call numbers advance beyond both the paper ledger and
inherited immutable paper-stage directories; research-call filtering never frees
an old paper number. An admitted call without terminal evidence, or a completed
response not yet reconciled into the paper checkpoint, blocks another dispatch.
Do not delete a stage, manufacture a completion, or replay a completed step to
resolve a numbering conflict. Native continuation also authenticates opaque
review-evidence text slices copied into the immutable paper snapshot; this does
not exempt ordinary control JSON from validation.

## Research convergence

This policy applies with or without `--exam`. Enter convergence when a coherent,
promising high-level proof skeleton appears, before full proof or final review.
Prioritize its necessary gaps and pause nonessential parallel alternatives; reopen
targeted exploration when concrete evidence defeats or undermines the route. See
`docs/research-convergence.md` and the all-mode contract in `workflows/common.md`.

Preserve a durable best-reviewed candidate and the exact evidence attached to it.
Keep original-scope uncertainty, mathematical gaps, selected certificate deficits
and manuscript/delivery deficits separate. A later conditional generalization does
not erase a better original-scope candidate or inherit its review authority.

Scope decisions need independent, artifact-bound reasons. Reopen them for a real
change in hypotheses, a counterexample, new contrary evidence or a substantive
review finding, not merely because a still weaker interpretation can be imagined.
Never freeze a mistaken interpretation against new evidence.

Before a substantial auxiliary or formalization project, name the live original
consumer it can resolve, the hypotheses it adds, the existing usable infrastructure
and the evidence that would settle its usefulness. Retriage is independently
reviewed; an expensive encoding does not erase an unproved mathematical inference.
New lemmas, rejected shortcuts and clarified obstructions can all be useful progress.
Revision counts, elapsed time and proof length alone cannot certify progress.

## Automatic writing and honest output

At the writing boundary the host closes new research admission, persists returned
work and available accounting, and gives the writer an immutable source snapshot.
The writing stage is an actual model workflow; a handoff JSON is not a completed paper.
The original phase clocks govern model admission so research does not consume the
reserved writing window. No submission or publication to an external service is implied.

Each problem receives an initial honest LaTeX artifact before waiting on writer
capacity. A fallback with no justified result reports the question as unresolved.
Available partial or conditional results may be developed only with their actual
hypotheses, gaps and evidence status retained. Unreviewed research is not promoted
to a proved theorem, SILVER, GOLD or full original-problem completion.

The Astra writer performs the existing paper workflow: faithful raw translation,
mathematical and premise checks, clear exposition, compression, two distinct
sequential fresh readers with revisions and verification of the second revision,
compilation, visual/layout checks, reference checks and release audits. The exam
profile disables novelty assessment and human literature waits; it does not disable
these polishing steps. Optional unavailable citations may be omitted with reasons;
essential proof dependencies and known credit cannot be concealed.

Compilation determines the actual page count; a configuration value of 16 is not
evidence that a PDF has 16 or fewer pages. Do not shrink fonts or remove indispensable
proof steps merely to claim compliance. Our conservative counting policy counts the entire
PDF, including appendices and references, without assuming an unstated exclusion. Plan proof
space first and use the first complete draft's compiled count before polishing. The optional
14-page working target in `workflows/paper/exam-mode.md` leaves revision room when feasible;
it is our planning choice, not an official cap or a requirement to shorten a complete answer
already within 16 pages. Recount after reader repairs and final layout. Our template and margin
choices are not official Batch 3 formatting rules. Compile/render/tool failures remain explicit.

Persist the best supported artifact throughout writing. At the terminal deadline,
return the available artifact and its true validation state, including unfinished
polishing or unresolved proof obligations. Do not mark an incomplete workflow as
fully audited because the clock ran out. A guaranteed fallback file is not a guarantee
that every proof and every polishing gate will finish within the reserved writing window.

Research acceptance, manuscript audit status and submission readiness have separate
receipts and accounting. A paper can accurately report partial research without
settling the original problem; a polished file never changes the research grade.

### Paper ownership and interrupted evidence reads

After research returns, the host registers a separate in-memory paper-task grant
with the watchdog. The grant binds the retained task, paper phase, and terminal
controller evidence. Completed research is never reopened to obtain a research
claim. Paper processes remain subject to process identity checks and the original
stage and exam deadlines; the grant is revoked when paper dispatch returns or is
cancelled. A restarted host cannot adopt a grant from saved stage metadata.

An interrupted paper evidence-read loop resumes its verified writer/reviewer
session. The ledger retains requested evidence and the four-turn budget, including
admitted interrupted turns. Legacy checkpoints can be reconciled only from exact
completed evidence-request responses and terminal incomplete turns in the same
session; full or ambiguous responses require explicit reconciliation. Prior
partial reads do not count as complete delivery in the resumed turn. Research,
manuscript, completed reviews, and the original exam clock remain preserved.

### Paper stage allowance and completion authority

Fresh exam campaigns select `exam_model_time_policy: formal-clock`. Every main,
reviewer, route scout and execution worker may think until the original research
close; every paper writer, reader and audit model may think until the original
submission deadline. The existing 15-second cleanup reserve is retained at each
boundary. There is no default 300-, 600- or 900-second model cutoff, and paper
fair-share estimates do not terminate healthy reasoning. The shared semaphore
still limits concurrency; waiting work checks the remaining clock after admission.
Scheduling and stage order do not grant additional time or weaken acceptance gates.

Short model calls are an explicit testing policy, separate from formal exam timing:

```sh
scripts/merlean-codex-pilot /outside/tool/tree/test-exam \
  --problems /outside/tool/tree/originals.json --exam \
  --exam-model-time-policy test-cap --exam-test-call-timeout-seconds 900
```

The test cap is finite (1–86400 seconds), applies to **all** model roles, and is still
clipped to the original phase deadline. It is never an official exam constraint.
Authentication checks, document-tool startup, network/protocol setup, local Python
or Lean probes, TeX compilation/rendering, process inspection and cleanup retain
separate technical timeouts. Those timers bound the technical operation, not a
subsequent period of healthy model reasoning. Local module task/action limits and
review-attempt limits remain unchanged.

Saved runs without a model-time policy retain `legacy-caps`: their recorded main
and paper caps, reviewer/worker caps and paper fair-share allocation retain their
historical meanings. Native continuation preserves this policy unless explicitly
instructed, for example `--exam-model-time-policy formal-clock`. It records the
prospective policy change while preserving the original clock, models, account,
scientific progress, historical deadlines and counters. Stored legacy main/paper
cap fields remain as historical configuration but are ignored in formal/test mode;
new conflicting main/paper cap overrides are rejected. Live configurations cannot
be changed through these options. A new policy cannot extend an already admitted
call or change a frozen run.

A test or legacy per-stage timeout is not evidence that infrastructure is broken
or that the mathematics needs repair. Paper timeout leaves the paper incomplete,
requires terminal process/response reconciliation, and triggers no automatic paid
retry or writer repair. Resuming a saved deadline-censored retrieval requires the
same audited session, remaining historical admissions, an explicit cap/policy
change, and a new actual grant at least 30 seconds or 25 percent larger than the
prior allowance, whichever is greater. This is a recovery precondition, not a new
formal time cap. The four-turn retrieval limit still includes admitted interrupted
turns. Exhausting the actual phase clock cannot renew it or trigger a paid retry.

Paper admissions preserve their allocation and session; the paper ledger records the
current stage, completed stages and consumed retrieval turns. Research `status` keeps
its original meaning. Exam results also expose `research_complete`, `paper_complete`,
`deliverable_complete` (full paper release audit), and `exam_complete` (both research
and paper complete). Internal readers and proof auditors execute only after their
required manuscript stages. The supervisor reports an unfinished paper as requiring
attention; successful research or a zero host exit cannot certify the paper.

The Pilot's deterministic watchdog validates its snapshot on the owning event loop
so a paper phase transition or grant revocation cannot race ownership validation.
This changes only the Pilot monitor; the generic campaign monitor remains separate.
Local filesystem locks and process inspection may briefly block the event loop; this
is not a guarantee of nonblocking inspection or elimination of natural child-exit races.

Paper handoff uses the controller's terminal `complete` or `partial` state. A retained
research claim token is historical evidence after release and finish, not an active
research claim. The host still needs its current retained task and a separate paper
grant; the grant remains bound to that terminal controller state and is invalidated
by a reopened or changed claim. Running and reconciliation-required research cannot
obtain a paper grant. These ownership checks do not award research or paper acceptance.

Paper continuation preserves completed raw-fidelity work. A validated frozen raw
checkpoint can finish its deterministic handoff without requesting another model
audit or replacing a saved manuscript with an initialization placeholder. Native
continuation moves the editable candidate and its seed storage into the verified
copy while preserving immutable raw evidence. Changed or ambiguous artifacts require
reconciliation; an invalid tool call is not silently accepted or replayed. These
resume operations do not install an automatic paper-repair or restart service.

### Explicit delivery remediation for an unaccepted reconstruction

A completed transport response is not an accepted manuscript when mandatory scoped
material was not delivered. The host retains the raw response and quarantines a
verified same-writer reconstruction as `UNACCEPTED`; it does not write that draft to
`paper.tex`, assign an accepted writer session, advance the stage, or change research
acceptance. Missing delivery is a paper attention state, not an instruction to run
infrastructure diagnostics or an automatic content repair.

For this narrow failure shape, an explicitly authorized native continuation may use
`--paper-delivery-remediation /path/to/request.json`. The request binds the stopped
parent manifest, problem, exact completed reconstruction, verified writer, raw and
parsed response, prompt, capability, snapshot, original required evidence hashes,
consumed retrieval checkpoint and historical call prefix. The runtime copies the
request into the continuation and records the policy delta. This path supports a
known resumed writer's initial reconstruction only; it grants no research capability
to fresh readers and does not reopen an accepted manuscript or completed reviews.

One separate corrective admission preserves the original retrieval count, including
an exhausted four-turn checkpoint. Its scope contains every original required artifact
with the same bytes, plus the quarantined draft as an additional mandatory artifact.
The same writer must read all of them before confirming or revising the reconstruction.
The host's ordinary delivery, identity, author-artifact, raw-audit, reader, proof-audit
and release gates still apply. A timeout or repeated missing delivery consumes the
single admission and stops; another continuation cannot reset it.

A completed corrective response interrupted before application is reconciled without
another model call. The host revalidates its prompt, producer, material scope, full
delivery and raw/parsed response. Partially written author files must equal either
the recorded prior bytes or the exact corrective output; divergent edits block the
operation. The original rejected response is never promoted or blindly replayed.

### Scoped reads and exact completed-response reconciliation

Writers and reviewers can read an approved artifact with
`read_artifact({"artifact_id": "listed-id"})`, optionally adding `start` or `end`.
Omitted `start` means character 0; omitted `end` means the complete text length.
Bounds are Unicode character offsets and must satisfy `0 <= start <= end <= length`.
The host resolves the file and verifies its saved version; the model does not need
to supply a hash. An optional hash from an older caller must still match. The
`read_required_evidence` page interface visits the complete required set. Prompts
and tool schemas permit both interfaces. These tools grant no arbitrary filesystem
access. Native event previews are diagnostic; persisted complete tool outputs and
durable receipts determine delivery.

A legacy corrective reconstruction could read every original source but fail only
to reread its own quarantined earlier response because its prompt omitted the hash
then required by the direct-read interface. An explicit
`--paper-delivery-contract-reconciliation /path/to/request.json` supports that exact
known producer and defect. It grants **zero model admissions**. The host replays the
original delivery audit, requires complete original-source delivery, authenticates
the same writer and exact response, and proves that the sole missing artifact is
that writer's earlier response added solely for preservation. It retains the old
missing-delivery verdict, original retrieval count, and consumed corrective admission.
An unexpected failed source read, changed source, extra missing artifact, or ambiguous
identity blocks reconciliation.

The prospective amendment admits only a candidate to the normal manuscript pipeline.
Unrecognized artifact names in the exact response are preserved as inert, untrusted
attachments under host-selected names outside manuscript state. Their original labels,
values and full response remain visible to the mandatory raw-fidelity reviewer; the
host does not infer their meaning or map them into trusted review files. Normal TeX,
allowed author-file, fidelity, independent reader and release validation still apply.
Partially applied candidates and attachments must match the authenticated bytes on
restart. No paid reconstruction retry, retrieval reset, or mathematical acceptance
is supplied by this path.
