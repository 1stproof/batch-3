# Lite default: develop, review, repair

Lite starts with the most promising candidate proof. Develop a coherent argument and its
step ledger, then obtain fresh substantive review. Prioritize the first material invalid
or missing inference, retain the rest of the candidate and its evidence, and repair the
objection in context. A promising candidate is not accepted closure: all known objections,
premises, citations, intended-object bindings, dependencies, and final composition checks
still have to pass the existing Lite gates.

This is the default allocation policy, not a prescribed mathematical proof route. Use
uncertainty ranking, alternative representations, targeted adversarial probes, or a bounded
route portfolio when there is no promising candidate, a representation-level defect, or
repeated repair fails to reduce the obstruction. Preserve usable facts and failed-route
evidence when changing course. Do not keep repairing an invalid representation merely to
preserve continuity, or discard a working proof merely to satisfy a diversity quota.

The maintained execution details are in `workflows/lite-research.md`, `roles/nl-prover.md`,
and `roles/skeptic.md`. Shared scope and resource limits in `workflows/common.md` govern
every loop. Heavy keeps its own procedure; Lite does not pursue full formalization unless
the user selects Heavy.

## Research progress and selective certification

The unit of progress is a better mathematical argument for the frozen question. Develop a
viable NL candidate before selecting certificates. A **research gap** is missing or invalid
mathematics: an unproved novel inference, unjustified range reduction, mismatched citation,
or broken composition. A **certification gap** is missing selected formal evidence for an
otherwise reviewed argument. Both must be reported, but compiler trouble is not itself a
refutation and certificate production does not discharge the open mathematical crux.

L3 records a reason for each row's selection or nonselection, tied to the current argument,
review findings and existing evidence. Select the few fragile inferences whose faithful
local Lean proofs materially reduce uncertainty. Zero to three is typical, not a quota or
maximum. Additional certificates need individual reasons. Routine justified mathematics,
exact exhaustive computation with independently checked coverage and implementation, and
exact audited citations ordinarily remain NL evidence. Sampling is support, not exhaustive
proof. A theorem's importance, a `NOVEL` label or many downstream uses does not by itself
justify formalizing its entire dependency tree. Keep accepted dependencies as explicit
certificate premises and audit their transitive manifest.

Retriage retains the previous decisions and all certificate attempts, then explains what
changed: the argument, exact evidence, citation match, or faithful encoding cost. Independent
substantive review must justify the change. All unresolved mathematical findings survive
retriage; deleting a selected row cannot convert an unproved inference into an accepted one.
When faithful encoding is itself a large project, record the certification limitation and
the supported grade. This escape prevents accidental Heavy work; it is not a SILVER waiver.

Intended objects must always be faithfully identified and bound in NL, with explicit
premises and audited use-site meaning. Lite requires hashed Lean adapters for selected
certificate interfaces and their SILVER certification, not for every object mentioned in
the ledger. This preserves the intended-model gate without turning preliminary research
into full formalization. A toy model, hidden premise or invented instantiation remains
unacceptable; full Gold adapter closure is an authorized Heavy obligation.

Intermediate fresh reviews focus on the first substantive gap while retaining every known
finding and any later defect actually noticed. They guide repair; they do not stand in for
the final comprehensive audit of all rows, premises, citations, interfaces and composition.
The independent original-question comparison and selected-grade gates still apply.

## When local repair stops helping

Main chooses whether to continue, refine or change the approach from the current
obstruction and actual evidence. Continuation prompts offer options; a checkpoint count
does not rotate the mathematical strategy. When scouts return, compare what each proposal
removes, what it leaves open and the hypotheses it needs. Record the chosen next move and
its reason in the existing notes or research work. A rejected shortcut can be useful
evidence, and a promising route still needs development and independent review. Neither
scout dispatch nor adoption is a quota.

Before another auxiliary repair, check whether successive repairs have left the same novel
crux open without useful new evidence. If so, explicitly reconsider the research route:
record the crux, auxiliary progress and why it has not reduced the obstruction. Choose a
concrete mathematical move, such as developing the crux, testing a different representation,
locating an exact applicable theorem, or abandoning the route when the evidence warrants it.
Retain useful facts and every substantive objection. Further auxiliary work needs an explicit
explanation of how it now helps resolve the crux.

This trigger concerns the relation between work and the obstruction, not a universal number
of rounds, certificates or tokens. It does not manufacture a counterexample, pronounce an
open route impossible, or turn a deadline into proof. At a real limit, preserve an honest
partial checkpoint. Sustained development remains the default while it improves the argument;
endless certificate repair around an untouched research gap does not count as that progress.

### Reuse established mathematical background

Before reconstructing general machinery, identify the exact missing justification: the
theorem's statement or status, a hypothesis or convention at its use site, required source
evidence, or faithful certificate encoding. Use an established standard theorem by its
precise statement with checked applicability when the existing background policy permits
it. A difficult proof of the theorem does not by itself make a justified application novel.
This does not turn a research result or an uncertain specialized variant into `ROUTINE`;
the `CITED` source, trust and use-site requirements remain unchanged. A theorem name alone
does not establish an unfamiliar statement or the application-specific bridge. If required
source evidence is unavailable under the current access policy, retain that limitation
honestly. Main may seek permitted evidence, prove a bounded missing implication, develop
another route or preserve a partial result; lack of access does not force rebuilding an
entire theory or authorize an unsupported premise. Accepted inputs may remain explicit
certificate hypotheses under the existing premise and intended-object checks.

## Models, continuity, and evidence

On GPT hosts, Astra leads mathematical reasoning and substantive review; Sol handles
bounded implementation and execution. Astra supplies useful descriptive hints with the
task, and Sol may correct or replace them under `docs/astra-sol-handoff.md`. Preserve
explicit model overrides and other providers' models.

Retain the actor session where the host supports continuation. Otherwise reconstruct it
from the exact candidate, complete reviewer feedback, and relevant failure history. A fresh
review uses an independent context rather than the actor's private reasoning or an intended
verdict. Report host limitations honestly: prompt labels and review receipts do not
authenticate session freshness or mathematical correctness. The optional receipt validator
in `docs/lite-review-rounds.md` continues to track every live finding across revisions.

For costed work, record host-reported usage as it arrives, by module and actual model, under
`docs/api-accounting.md`. Include cached input, distinguish API-equivalent costs from actual
billing, and preserve unknown usage. Accounting and these workflow instructions do not
implement a model launcher or recover telemetry the host does not expose.

## Decision and limits

The September 2026 bounded comparison used six First Proof questions, with both policies
receiving the same allocation within each paired question. Both produced accepted complete
natural-language answers on four questions and neither achieved the defined breakthrough
on the other two. Candidate-first was earlier on three of the four solved questions;
uncertainty-first was earlier on one. On the final prospectively selected pair,
candidate-first met the predeclared speed/token criterion on both questions without a worse
correctness outcome. This supports candidate-first as the practical Lite default while
retaining the other policy's tools.

The experiment used one run per policy/question, several successive protocol versions,
and natural-language judgments rather than full Lean certification. Both arms retained
actor context and used fresh feedback; actor persistence, reviewer freshness, and the
Astra/Sol split were not separately ablated. Their individual causal benefits, optimal
review frequency, and universal superiority remain unestablished. They are optional future
research questions, not requirements to postpone this default. Do not transfer experiment
scores into research grades or import its fixed time limits and judge counts into ordinary
campaigns.

This closes the current default-policy decision. Reopen it when concrete failures or new
comparative evidence warrant a change, without automatically launching more benchmarks.

### Bounded local verification modules (Lite)

A selected Lean check is a small internal module for one materially uncertain local
claim. It is not a new problem or a requirement to formalize the proof's foundations.
Keep the readable main-owned handoff and advisory hints; Sol may revise tentative
signatures and tactics within the independently reviewed claim, explicit premises,
owned scope and acceptance conditions. Accepted mathematical inputs may remain
explicit hypotheses with exact applicability and the existing premise checks.

The main supplies a short scope/value brief and proportionate worker/probe bounds.
The host records exact claim, dependent-premise, candidate, task and approval
bindings, a stable lineage, all attempts and complete returned evidence. Existing
independent triage admits only high material local uncertainty. The same guard
serves Sol implementation and main inline Lean; no extra bookkeeping reviewer is
required. Mechanical checks bind exact interfaces and records; independent review
judges mathematical scope and whether a changed approach adds real value.

Return to the original main on foundational scope expansion, disproportionate
faithful encoding, exhausted agreed local bounds, or no uncertainty reduction.
Retain code, diagnostics, findings and costs. This operational exit never proves
or resolves the claim. A still-needed check remains an unresolved obligation.
The existing independent review can instead justify a replacement or removal of
a now-unnecessary check from current substantive evidence, explicitly mapping all
prior modules and findings. Labels, budgets and candidate churn do not erase a
lineage or its spent history; reentry requires current evidence and new value.

Natural-language research continues after a module returns. Zero Lean modules is
valid when current independent review selects none: the existing nonempty closed
ledger, full proof, original-scope and grade gates still apply. No grade semantics,
Heavy/Gold requirements, paper behavior or human-readable handoff style change.

### Select only checks with a concrete verification benefit

Before approving a new Lite Lean task, identify the exact unresolved uncertainty after
natural-language development and independent review, the evidence already available,
the actual intended objects and use-site map, and the noncircular accepted premise
boundary. State what a faithful certificate would newly establish, how its encoding
can fit the proposed local bounds, and why that value warrants the expected cost.
Novelty, importance, dependency fan-out, or a wish to accumulate certificates alone
is not selection evidence. Zero new Lean tasks is valid when independently justified.
This does not retire existing obligations: preserve their failed attempts and require
substantive independent reassessment before replacement or deselection. No automatic
retriage, retrospective approval, downgrade, or change to Silver requirements follows.

### Coherent execution inside an approved local module

An unchanged independently approved local task may run a bounded worker/source → host
compiler → implementation-repair cycle before returning for scientific acceptance.
In the host protocol, `compile_pending` explicitly requests that cycle and supplies
source, the exact selected row, `implementation_complete` and a concrete `next_step`.
It need not claim uncertainty reduction before receiving its first real diagnostic.
`implementation_complete` is the worker's coverage claim, not acceptance: a clean
compile of a full implementation stops for independent premise, intended-object and
certificate assessment. A failed compile or compiled incomplete implementation can
receive the next bounded repair with all exact prior source and diagnostics.
Generic `local_evidence` alone does not request repeated implementation. Identical
source resubmission supplies no new diagnostic work and stops the cycle.

Keep the same immutable task, claim, actual-object interface, premise closure, owned
scope, candidate and independent approval binding throughout that cycle. Count every
worker call and probe against the original cumulative module limits. Retain every
attempt and failure; replacement generations inherit consumed counters, never a new
allowance merely for changed wording. Every dispatch and compiler invocation must
revalidate those bindings and respect the host's drain, deadline and resource controls.
Where workers cannot invoke Lean directly, returned source is a request to the host,
not a failed compilation. Reconstructed worker contexts must receive the full retained
implementation evidence with continuity loss disclosed.

Goal/premise/interface/scope/budget changes, material mathematical counterissues,
encoding infeasibility, no-value evidence, missing host execution, and exhausted bounds
return to main under the existing independent reassessment rule. Terminal historical
reports, including `returned_to_main`, remain terminal; protocol migration does not
relabel them as pending or authorize replay. No scientific reviewer is required merely
between source and its first authorized compiler diagnostic. Independent acceptance
after the resulting certificate, comprehensive full-proof review, two fresh original-
scope reviews and all selected-grade gates remain unchanged.

### Compile-pending field placement

For host-managed local Lean modules, `implementation_complete` (boolean) and
`next_step` (nonempty string) belong **inside `local_module_result`**, alongside
its module ID, outcome, scope, uncertainty and evidence fields. The exact source
`lean_probe`, singleton approved `lean_probe_rows`, and empty `python_probe`
remain at the response root. Root-level completion or next-step fields do not
satisfy the nested contract. Shape diagnostics retain the original return and
do not repair it, grant retries, execute code or certify a claim. Historical
returns retain their original interpretation and consumed budgets.
