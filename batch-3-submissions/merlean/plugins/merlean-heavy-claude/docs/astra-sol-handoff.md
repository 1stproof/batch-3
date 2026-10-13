# Astra-to-Sol Lean collaboration

This protocol applies when GPT Astra main delegates bounded Lean implementation or compile repair
to Sol. Astra supplies the mathematical context and useful implementation ideas; Sol implements,
debugs, and may improve the route; Astra performs substantive review. The accounting ledger records
design, implementation, and review under their actual modules and models. Whether the complete split
saves time or money remains an empirical question.

This is a host-agent protocol. It adds no scheduler, model call, schema, online lookup, or trust
gate. Explicit model overrides still win, and Claude workflows keep their configured provider
models. Existing Lite/Heavy selection, file ownership, independent review, build, axiom, premise,
intended-model, and grade gates remain authoritative.

## Task context and advisory ideas

Before dispatch, Astra gives Sol a readable task description. It states the original mathematical
goal and hypotheses, relevant plan or paper context, the file Sol owns, established dependency
interfaces, and the checks that acceptance requires. Astra should also share its best current
implementation ideas: for example the suspected nonroutine crux, a likely decomposition, a concise
proof sketch, useful representations or tactics, possible Mathlib declarations, and coercion or
boundary risks.

Those implementation ideas are descriptive hints. They may be incomplete or wrong. They do not
bind Sol to Astra's proof route, helper structure, tactic sequence, declaration names, or proposed
Lean spelling. A possible Mathlib name should be labelled unverified unless Astra checked its exact
local type. A candidate mathematical route should be labelled tentative rather than passed to
consumers as established.

There is no compulsory handoff schema or checklist. A task can read naturally, for example:

> Prove the original finite-sum identity from hypotheses H1 and H2 in `OwnedFile.lean`. This file
> is yours; do not edit its imported dependencies. `existing_helper` is an established shared
> interface. Acceptance requires clean diagnostics, `lake build OwnedFile`, no warnings or
> `sorry`, and the existing axiom and faithfulness checks.
>
> **Implementation ideas (advisory):** I expect rewriting the indexed sum through the equivalence
> and then using a finite-set extensionality lemma to work. `Finset.sum_bij` may be relevant, but I
> have not verified that name or argument order. Watch the empty-index case and the coercion from
> the subtype. If another representation or direct induction is cleaner, use it and explain the
> evidence in your return.

The example combines the task, context, ownership, interfaces, and acceptance conditions, followed
by optional ideas. Astra need not write the complete Lean proof. It should provide useful thought
rather than merely forwarding a declaration, while being candid about uncertainty.

## What is fixed and what Sol may change

The hard boundaries are:

- the original mathematical goal and hypotheses;
- the authorized file scope;
- signatures already established as shared interfaces for other banked or parallel work; and
- the selected workflow's verification and trust gates.

A proposed signature or formalization is an implementation idea until its faithfulness and
interface status have been established. Sol may improve a proposed signature inside its owned file
when no shared consumer relies on it and the result more faithfully expresses the original goal.
If an established shared interface is wrong, Sol reports the concrete incompatibility so main can
coordinate a plan change and downstream invalidation; Sol does not edit other owners' files or
silently break consumers.

Within those boundaries, Sol may inspect, reject, revise, or replace any Astra suggestion. It may
choose a different representation, proof route, tactic structure, local helpers, or Mathlib API and
continue without asking permission merely because it deviated. Missing or flawed hints are reasons
to investigate, not automatic reasons to return `needs_update`.

Sol still must not invent an assumption, weaken a quantifier or conclusion, replace the intended
object with a toy definition, or call a sketch, `sorry`, axiom, or unverified dependency proved.
Local Lean and Mathlib inspection should verify declarations when available. Online lookup is not
required.

## Return and review

Sol reports the diagnostics and build commands it ran, the actual Mathlib declarations it used,
and any useful departure from Astra's ideas with concise evidence. It returns a mathematical
blocker only when it cannot make useful progress within the task or when a faithful solution really
requires changing the original goal/hypotheses, authorized scope, or an established shared
interface. The blocker report identifies the smallest remaining claim or interface, the relevant
compiler goal or error, and the materially different approaches already tried.

Astra reviews the resulting source against the original mathematical goal and the existing trust
gates, not against its own tentative sketch. It checks premise flow, proposition-valued record
fields, definition independence, intended-model connection, warnings, build results, and axioms.
If a real mathematical or shared-interface blocker remains, Astra revises the design or coordinates
decomposition before another implementation pass.

Where the workflow requires fresh independent acceptance, retain it after Astra's ordinary review.
The collaboration does not turn the designing main into an independent reviewer or replace Heavy's
dependency-cone and Gold audits.

Independent review findings return to the owning main with the exact reviewed revision and
unresolved history. Main distinguishes implementation repair from proof, interface or scope repair
under `workflows/common.md`. A bounded repair handoff carries the finding, current obligation,
relevant evidence and previous failed approaches, updated advisory hints, owned files and acceptance
checks. Sol returns its patch, checks and remaining blockers to main; the repaired artifact then
receives any required fresh independent review. Neither main nor Sol may close that gate by marking
the finding delivered or the implementation finished.

## Model defaults and Lite scope

For GPT workflows, every problem main may lead multiple execution subagents. Main,
research/proof-design leads, paper/referee leads, optional campaign supervisor, and independent
substantive reviewers use `gpt-6-astra` by default. Delegated execution subagents default to
`gpt-6.1-sol`, including bounded Lean implementation and compile-fix. Main supplies formalization
hints before dispatch and owns mathematical decisions; Sol implements the assigned subtasks.
A reviewer dispatched as a subagent still explicitly uses Astra. Preserve explicit model
overrides; execution defaults never replace the required independent reviewer.

Lite may use the same split for a selected weakest-link Lean spot-check: Astra explains the exact
local claim and tentative idea, Sol chooses and implements a bounded check, and Astra evaluates
what the result actually establishes. This does not authorize a full formalization campaign or
automatic Lite-to-Heavy escalation.

For a Lite local verification module, preserve this readable handoff. Its brief
adds only the exact local uncertainty, accepted premise boundary, non-goals and
expected value/cost. Host metadata owns lineage, attempts and evidence bindings.
Do not expand foundations or keep encoding after it stops reducing uncertainty;
return the full attempted work and reason to the original main for independent
retriage. Operational return is neither a proof nor permission to drop a gap.

## Selective Lite verification execution

Apply the concrete uncertainty, intended-object, noncircular-premise and feasibility/value
selection in `workflows/lite-research.md`. An already approved unchanged local module
may perform a bounded source/compile/implementation-repair cycle using its original
cumulative worker/probe limits and complete retained evidence. Prospective host workers
request this with `compile_pending`, exact row/source, `implementation_complete` and
`next_step`; no uncertainty-reduction claim is required before a diagnostic. Revalidate
task, claim, premises, scope, candidate and approval before every execution. Changed
boundaries, material adverse findings or exhausted bounds require existing reassessment.
Terminal historical returns are not reopened by this protocol. Provider-driven hosts
apply the same boundaries with their actual tools; do not claim automatic scheduler
support where absent. Clean compilation still needs independent semantic acceptance,
full-proof and two fresh original-scope reviews, and every existing Silver/Gold gate.

### Compile-pending field placement

For host-managed local Lean modules, `implementation_complete` (boolean) and
`next_step` (nonempty string) belong **inside `local_module_result`**, alongside
its module ID, outcome, scope, uncertainty and evidence fields. The exact source
`lean_probe`, singleton approved `lean_probe_rows`, and empty `python_probe`
remain at the response root. Root-level completion or next-step fields do not
satisfy the nested contract. Shape diagnostics retain the original return and
do not repair it, grant retries, execute code or certify a claim. Historical
returns retain their original interpretation and consumed budgets.
