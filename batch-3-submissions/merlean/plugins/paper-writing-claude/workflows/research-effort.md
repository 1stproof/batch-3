# Research effort: spend more inference on useful scientific work

Read `common.md`, the provider adapter, and the selected Lite/Heavy procedure first.
“Token maxxing” can be useful: a large research question often needs more representations,
more independent attacks, more repairs, and more sustained reasoning than a single answer.
The objective is scientific claim gain under the user's constraints, not token consumption
itself. This is an actionable host-agent protocol, not an implemented autonomous scheduler,
model-call loop, fleet meter, or new public agent.

## The working cycle

1. **Reconstruct the live question.** Read the dossier, selected routes, failure log and
   current evidence. Name the present uncertainty: truth of a conjecture, a representation,
   a quantitative constant, physical applicability, prior-art overlap, or proof completion.
   A checkpoint records progress; it does not end an unfinished authorized goal. Continue
   useful work within the user's authorization, resource limits and host availability.
2. **Allocate for the selected mode.** In Lite, start from the best current candidate and
   preserve one actor's context and progress across local repairs. Open distinct routes,
   representations, counterexample searches or literature audits only when they answer a
   live uncertainty: no promising candidate, representation obstruction, repeated
   unproductive repair, disputed premise/novelty, or an explicit request for alternatives.
   In Heavy, retain its established decomposition and signature-locked parallel work.
   Every task remains bounded, independently useful and uniquely owned; parallelize only
   genuinely independent work supported by the host.
   GPT main/worker defaults remain `gpt-6-astra`; preserve explicit model choices and
   provider/host concurrency limits. Main alone edits the plan and checkpoint sidecar.
3. **Use a meaningful deliverable.** Each worker receives the exact current obligation or
   bounded research question, assumptions, known failures, owned files, expected evidence,
   and a decision its result will inform. A route scout should offer a different core idea,
   a weakest step and a kill-test, not another wording of the same stalled argument.
   Separate independent routes from dependent proof leaves and from broad literature work.
4. **Run review–repair cycles.** Lite gives each revised candidate to a fresh substantive
   review context to locate the earliest currently live substantive invalid or missing
   inference, whether carried or new, while preserving
   every known unresolved finding. Resume the same actor for a local, provenance-bound
   repair, and widen the search only on evidence. Supply the reviewer the exact artifact,
   public evidence and prior stable findings, without an intended verdict or private actor
   reasoning. Disclose a host failure to provide fresh context; provisional review can guide
   work but cannot satisfy the Lite fresh-review gate. If the host cannot resume the actor,
   provide a replacement the exact artifact, feedback, public working notes and failure
   history, disclose the continuity loss, and preserve valid progress. Heavy follows its
   selected proof and audit procedure. Extend promising work when it resolves objections or makes the remaining
   obstruction more precise. Do not impose a universal round cap across all research
   problems, and do not mandate identical retries forever. Apply every selected workflow
   debate, triage, pivot and trust gate. A surviving objection is information, not a reason
   to buy a favorable review by repetition.
5. **Bank and redirect.** Inspect outputs, preserve exact statement versions and relevant
   data/model assumptions, and bank counterexamples, failed routes and verified artifacts.
   Reuse accepted facts only with matching obligations, assumptions and current evidence.
   A failed route normally changes the next allocation, not the user's entire goal. Main
   may choose a rival representation, a smaller decisive subquestion, or a verified
   refutation route under the existing pivot/scope rules. Do not silently weaken the target.
6. **Reallocate deliberately.** Reconcile running/queued jobs before launching more.
   Continue independent local reasoning while workers run. Spare capacity does not require
   a scout, rival, reviewer, or repeated cycle. Before increasing width or effort, state the
   evidence trigger, what the work can produce, and whether it affects the main claim or a
   necessary consumer. Preserve output
   and checkpoints across integration failures; repair integration without automatically
   restarting accepted mathematics. Revalidate the combined result before promotion.
7. **Assess the research outcome.** A new bound, necessary assumption, verified refutation,
   better physical model, or substantive novelty subtraction may matter more than many
   easy lemmas. Ask whether the work improves the actual question and the coherence of a
   possible paper. Complete the appropriate audits before claiming resolution or a grade.
   If an explicit limit or interruption ends the allocation, leave an honest resumable
   state; do not reinterpret spent compute as success.

## Candidate success and accepted closure

Use two stages so persistence does not become unnecessary alternative work, and an attractive
partial result does not prematurely end the research.

- **Candidate success:** when a route appears sufficient for the exact current goal version,
  pause launching new alternatives that only duplicate that route's conclusion. Preserve
  mandatory independent audits, integration, composition and counterexample validation.
  This is a scheduling judgment by main, not a success verdict. A partial lemma, conditional
  milestone, worker claim, or plan node marked completed does not establish goal closure.
- **Accepted closure:** stop redundant work only after main checks the exact authorized goal
  version and deliverables against the current mode's completion gates. Conditional results
  close only a goal that actually asks for that implication. Retain any remaining authorized
  task and proceed to the next already-authorized goal when applicable; otherwise finish.
  Do not invent new sharpness, generalization or alternative-proof goals merely to keep
  capacity busy. Conversely, retain a sharpness, novelty or robustness branch when it is
  needed for the actual authorized claim or deliverable. An explicitly requested second
  independent proof remains required even after the first proof is accepted.

For running workers, first identify shared consumers: work still needed by another live
obligation is not redundant. Collect completed results; request a bounded handoff of useful
partial artifacts, failure evidence and precise remaining obligations from workers whose
work is no longer needed. Use owned-job cancellation through the host where appropriate,
confirm its acknowledged state, and preserve the handoff. Do not issue broad process kills,
delete losing-route evidence, assume a cancellation succeeded, or blindly relaunch an
uncertain job. A short continuation is justified by useful evidence still to collect, not
by sunk cost alone.

A new substantive objection or changed source/dependency reopens the affected checks and
work; retain unaffected artifacts and reassess the goal's closure before relying on it.
Neither stage implements automatic dispatch, cancellation, grading, or a token-saving meter.

## Decisions at each allocation

| Observation | Next useful action | Avoid |
|---|---|---|
| One candidate is making useful progress | Preserve its actor context; use fresh review and local repair | Mandatory rivals or restarting valid work |
| No promising route, representation uncertainty, fatal representation flaw, or repeated unproductive repair | Open bounded diverse scouts/kill-tests within the selected workflow's fallback budget | Breadth merely to fill available slots |
| A proof improves under specific objections | Continue persistent-actor/fresh-review repair; test the new crux | Stopping just because a checkpoint was written |
| A route appears sufficient for the current goal | Pause new redundant alternatives; finish required validation and integration | Treating candidate success as accepted closure |
| Exact goal and mode gates have closed | Stop redundant owned work after evidence handoff; continue only remaining authorized tasks | Inventing extra goals to consume spare capacity |
| Another live consumer still needs a worker's result | Retain that work and make its relevance explicit | Cancelling by route label alone |
| New objection or changed evidence affects an accepted result | Reopen the affected checks and reassess closure | Reusing stale acceptance or restarting all unrelated work |
| The same mathematical obstruction survives | Change representation, inspect assumptions, or independently test a counterexample | Classifying mathematical failure as transient capacity |
| Candidate disproof or changed hypothesis | Verify independently; apply pivot/scope gates and version the obligation | Silently changing a frozen theorem |
| A lemma is correct but irrelevant to current roots | Preserve it; redirect effort toward the claim's actual dependency or uncertainty | Treating lemma count as research value |
| Proof accepted, merge/integration fails | Retain artifacts, repair the integration, rerun the required combined checks | Reproving the theorem on every Git failure |
| Explicit transient model-capacity failure | Follow `common.md` recovery with job reconciliation and cancellation checks | Duplicate dispatch or account/model substitution |
| Rate limit, context/auth failure, or unknown infrastructure error | Apply the classified host recovery/diagnosis policy | The capacity retry loop for every error |
| User budget, host capacity, or memory limit binds | Reduce width/effort, select the next decisive task, or checkpoint at the limit | Inventing permission or claiming a universal fleet budget |

## Resource policy and honesty

When reporting cost or comparing research allocations, use the per-response bookkeeping
in `docs/api-accounting.md`. Group the actual mixed-model calls by module and model,
preserve retries and missing-usage records, and expose the live known-cost subtotal
alongside pending/unmetered work. Freeze the price source and pricing scenario before
comparing dollar totals. Standard API-equivalent pricing can compare subscription
work without pretending that it is an actual invoice or quota conversion.

Increase useful inference through sustained candidate development, fresh independent
criticism, targeted experiments, and evidence-triggered route diversity when their expected
contribution justifies the resource. More reasoning on one hard crux may be better than more
parallel workers; conversely, uncertainty about the representation often favors breadth.
Research benefit is assessed against the main claim,
its assumptions, limitations, novelty and consumer—not output length, turn count, or number
of compiled files. This judgment is an explicit allocation rationale, not a fabricated
numeric expected-value score.

Respect explicit token/time budgets and the host's actual concurrency, cancellation and
memory constraints. If the host exposes token usage, report what it measures, including
known exclusions. If aggregate usage across workers is unavailable, say it is unknown;
do not invent a fleet total, a hard remaining budget, or billing equivalence from per-turn
`max_tokens`. A per-response limit, reasoning effort, parallel width and cumulative spend
are different controls. The checkpoint commands neither meter nor enforce them.

Time spent alone does not identify a stale mathematical route. Distinguish long productive
reasoning, transient dispatch capacity, active compilation, repeated identical errors and
permanent infrastructure failure. The existing host and workflow limits govern continuation;
this protocol supplies neither a fixed universal round cap nor an unconditional infinite loop.

## Keep Lite and Heavy distinct

In **Lite**, default to sustained NL development of the best current candidate: a persistent
actor, fresh substantive review of each revision, local repair of the earliest material
inference gap, and discriminating probes. Representation search, parallel adversarial lenses
and alternative routes remain available when live evidence triggers them. On GPT, actor and
reviewer default to `gpt-6-astra`, while `gpt-6.1-sol` performs only explicitly bounded
execution under fixed goal/interface boundaries; Astra's hints are descriptive and rejectable,
and Astra reviews the result. Claude keeps its inherited provider models, and explicit model
overrides are preserved. Use Lean at selected weakest links under the existing triage gate.
Do not turn every promising large conjecture into a full formalization campaign before its
mathematics and value are clear. Lite's ceiling is SILVER; more tokens do not change it or
authorize an automatic switch to Heavy.

In explicitly selected **Heavy**, persist through decomposition, proof repair, compilation
and independent semantic checks for the frozen obligation, with useful signature-locked
parallel work and final checks over the entire dependency cone. Preserve the full target,
premise, intended-model and Gold audit gates. If the conjecture is false or the model needs
revision, use the research controller's existing evidence/scope process rather than a
mechanical proof loop. Neither a worker's confidence nor an accepted checkpoint awards Gold.

## Relationship to checkpoints and inspiration

`research-checkpoints.md` provides optional offline memory for this activity; it does not
execute this protocol. Current evidence checkpoints and subsequent progress/failure events
serve different purposes. The latest applicable `evidence_checkpoint` is selected for reuse;
a later integration failure or progress note does not erase it. Main must still inspect
live mathematical or verification objections. Byte-current evidence is not a verdict that
an objection is resolved, and changed artifacts/dependencies make recorded bindings stale.

Humanfia's [Humanize2](https://github.com/humanfia/humanize2/tree/3e0e6edf1d47ae27a70c1a334ee6cf364d05f59b)
and [Flowverse](https://github.com/humanfia/flowverse/tree/1dd53c4437e62934ed053bf28fbcdfd0ffa6bbcd)
inspired this explicit treatment of sustained inference, parallel investigations and durable
work. This is an original adaptation to MerLean's evolving research questions and trust
gates, not a wholesale runtime import or a claim of demonstrated budget-normalized gains.
