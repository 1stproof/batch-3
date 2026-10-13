# Code Review - Round 3

## Original Implementation Plan

**IMPORTANT**: The original plan that Claude is implementing is located at:
@plan.md

You MUST read this plan file first to understand the full scope of work before conducting your review.
This plan contains the complete requirements and implementation details that Claude should be following.
Only items under `## Acceptance Criteria` and current-scope Task Breakdown rows are completion gates.
Items under `## Future Work` / `## Out of Scope`, including `FUT-*` items, are informational and MUST NOT block the COMPLETE verdict.
If a current-scope AC or current-scope task is deferred, treat it as incomplete.

Based on the original plan and @/work/first-proof-humanize-tdgou2bu/006-prob-007/.humanize/rlcr/2026-10-03_01-18-59/round-3-prompt.md, Claude claims to have completed the work. Please conduct a thorough critical review to verify this.

---
Below is Claude's summary of the work completed:
<!-- CLAUDE's WORK SUMMARY START -->
# Round 3 Summary

## Work Completed

Mainline objective: repair the round-0 heritage over-commitment in
`lem:sheets`(c) (round-2 review Finding 1) and residual `lem:descend`
self-citation (Finding 2 / R1-F1(d)).

- **Finding 1 (component-count).** Strengthened the theorem set AND made the
  count rigorously honest. Added `lem:allpairs` proving
  `Ψ(E_f) = PMCG(A)` (the descended pullback map from
  `E_f = ⟨x_i, a_j⟩` hits every mapping class of `A`; the eight pair twists
  lift with computed classes). However, a careful operator-convention audit
  (carried out this round) shows that the naive identity
  `f*(τ·w) = f*(τ)·Ψ(w)` on the *full* sheet set does NOT force every sheet
  into the equalizer — the selected components are a union of possibly
  several H-sheets. The honest, verifiable statement is therefore restored:
  **π_0(D_f) is a nonempty right-H-invariant SUBSET of the sheet space
  H\PMCG(B)** (a union of full H-cosets), with bounds
  `2 ≤ #π_0(D_f) ≤ [PMCG(B):H] ≤ 4`, the number **even** (in `{2,4}`).
  `lem:sheets`(c) now states and proves exactly this (base membership
  `τ0 ∈ D_f` is given as a one-line lemma, per the review's note).
- **Orbit behavior on the honest sub-union (new, needed by the weakening).**
  `cor:index` now proves that `T_γ = x_2` *does* permute the selected
  components: the monodromy loop at the double zero of `s_2` has winding
  number 2, so the two lifts of a parametrized small loop starting at `τ0`
  and at `τ0·x_2` agree, whence the sheets through both are simultaneously
  selected; right-H-invariance plus `x_2² ∈ H` then pair up the whole
  selected set. The action is **fixed-point-free** (`ch_2` is
  conjugacy-invariant on PMCG(B), pure braids fix the labels `v,p_2`;
  `gx_2 g^{-1} ∈ H∩K ⊆ F` would contradict `ch_2 = 1` odd). Hence every
  `T_γ`-orbit on `π_0(D_f)` has size exactly 2 and `T_γ²` acts as the
  identity — so **no infinite orbit** exists, and the AC-4 verdict is
  re-proved (not assumed) on the honest component set, exactly as the
  review's Finding 3 anticipated.
- **Finding 2 / R1-F1(d) resolved.** `lem:descend`'s proof no longer cites
  itself: the two internal references were replaced by `prop:preimage`
  (the model disc computation) and by `def:descend` + `thm:halflift`
  (peripheral ambiguity invisible on A / the d=2 half-twist).
  `grep` confirms the only `Lemma~\ref{lem:descend}` occurrences are in
  *later* results, never inside its own proof.
- **Consistency/cleanup.** `thm:components`, `cor:answer` restated to the
  honest sub-union (removed "number of components is [PMCG(B):H]"); deleted
  the redundant, unproved "none of the conjugates of H contains
  T_δ^∘m …" clause in `prop:contenttable`(b) (queued R2-Q3), replaced by the
  correct topological-datum justification that the descended class is the
  same at every component.

## Files Changed

- `solution.tex` — as above (committed: `30186cc`, `c3fb0e2`).

## Validation

- `pdflatex` ×2: **0 errors, 0 undefined references, 12 pages ≤ 16.**
- Residue sweep clean: no "between 2 and 8", no "Schreier", no
  "number of components is [PMCG(B):H]", no "every sheet lies in D_f", no
  self-citation inside `lem:descend`, no `x_0'`, no "conjugates of H"
  clause, no "wait/FIXME" artifacts.
- Operator-convention audit (reverse-composition for simultaneous right
  actions) redone this round; conclusion: component-count equality NOT
  derivable by the naive formula, so the sub-union bound is the honest
  statement.

## Remaining Items

- Exact count `π_0(D_f) ∈ {2,4}` remains provably even but not pinned to a
  single value; deliberately unpursued (unused by any theorem or by the
  AC-4 verdict). Queued.
- Whether the equalizer is in fact all sheets (`D_f = π^{-1}(M_f)`) is NOT
  asserted anywhere now; the sub-union formulation is sufficient and proved.

## BitLesson Delta

Action: add
Lesson ID(s): BL-20261003-right-action-reversal
Notes: Simultaneous right actions on Teichmüller space make the descended
pullback map Ψ reverse composition (Ψ(σ1σ2)=Ψ(σ2)Ψ(σ1)), because
(φσ1)σ2 = φ(σ1σ2). When using Ψ to detect which sheets of a covering lie in
an equalizer `{f* = i*}`, the naive "Ψ(w) word-agrees with bar w" criterion
must be evaluated with this reversal; overlooking it silently upgrades a
sub-union statement into a false all-sheets equality. Verify orbit/stabilizer
claims on the *actual* component set (the sub-union), not just the ambient
sheet set, using monodromy-lift arguments (e.g. even winding gives simultaneous
selection of swapped sheets).
<!-- CLAUDE's WORK SUMMARY  END  -->
---

## Development History (Integral Context)

Accumulated commits since loop start (oldest first):
```
8f920a2 prob-007: deformation space of quadratic rational map with period-4 critical cycle
27fec33 round 1: repair monodromy census and H-structure (review findings 1-2)
afb735b round-1 followup: tighten no-fixed-coset argument in cor:index (pure braid conjugacy preserves linking invariants)
50d1168 round 2: remove repair residue (review findings R1-F1, R1-F2)
30186cc round 3 checkpoint: lem:allpairs (Psi-surjectivity), Finding-2 self-citation fix, base membership; D_f=sub-union of sheets (honest bound)
c3fb0e2 round 3: honest component sub-union 1<=#<=4 (even, {2,4}); x2 acts fixed-point-free on selected sheets via double-winding; Finding-2 fixed; drop unproved conjugates clause
```

### Recent Round Files
Read these files before conducting your review to understand the trajectory of work:
- @.humanize/rlcr/2026-10-03_01-18-59/round-2-summary.md
- @.humanize/rlcr/2026-10-03_01-18-59/round-2-review-result.md
- @.humanize/rlcr/2026-10-03_01-18-59/round-1-summary.md
- @.humanize/rlcr/2026-10-03_01-18-59/round-1-review-result.md
- @.humanize/rlcr/2026-10-03_01-18-59/round-0-summary.md
- @.humanize/rlcr/2026-10-03_01-18-59/round-0-review-result.md


Use this history to identify patterns across rounds: recurring issues, stalled progress, or drift from the mainline objective. Weight recent rounds more heavily but watch for systemic trends in the full commit log.

## Part 1: Implementation Review

- Your task is to conduct a deep critical review, focusing on finding implementation issues and identifying gaps between "plan-design" and actual implementation.
- Relevant top-level guidance documents, phased implementation plans, and other important documentation and implementation references are located under @docs.
- If Claude planned to defer any current-scope tasks to future phases in its summary, DO NOT follow its lead. Instead, you should force Claude to complete ALL current-scope tasks as planned.
  - Such deferred tasks are considered incomplete work and should be flagged in your review comments, requiring Claude to address them.
  - If Claude planned to defer any current-scope tasks, please explore the codebase in-depth and draft a detailed implementation plan. This plan should be included in your review comments for Claude to follow.
  - Do NOT draft implementation plans solely for `FUT-*`, `## Future Work`, or `## Out of Scope` deferrals unless they block a current-scope AC or current-scope task.
  - Your review should be meticulous and skeptical. Look for any discrepancies, missing features, incomplete implementations.
- If Claude does not plan to defer any current-scope tasks, but honestly admits that some current-scope tasks are still pending (not yet completed), you should also include those pending tasks in your review.
  - Your review should elaborate on those unfinished tasks, explore the codebase, and draft an implementation plan.
  - A good engineering implementation plan should be **singular, directive, and definitive**, rather than discussing multiple possible implementation options.
  - The implementation plan should be **unambiguous**, internally consistent, and coherent from beginning to end, so that **Claude can execute the work accurately and without error**.

## Part 2: Goal Alignment Check (MANDATORY)

Read @/work/first-proof-humanize-tdgou2bu/006-prob-007/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md and verify:

1. **Acceptance Criteria Progress**: For each AC, is progress being made? Are any ACs being ignored?
2. **Forgotten Items**: Are there tasks from the original plan that are not tracked in Active/Completed/Deferred?
3. **Deferred Items**: Are deferrals justified? Do they block any ACs?
4. **Plan Evolution**: If Claude modified the plan, is the justification valid?

Include a brief Goal Alignment Summary in your review:
```
ACs: X/Y addressed | Forgotten items: N | Unjustified deferrals: N
```

## Part 3: Capability Map Alignment Check (MANDATORY when present)

If the original plan contains `## Feature Map / Capability Map`, verify:

1. **Capability Anchor**: Did Claude's round contract and Active Tasks identify the relevant capability node(s)?
2. **Context Preservation**: Did the implementation preserve the anchored capability's business, design, and implementation context?
3. **Dependency Respect**: Did Claude respect capability dependencies instead of skipping prerequisite nodes?
4. **Scope Control**: Did Claude avoid drifting into unrelated or future-scope capability nodes?

Include a brief Capability Alignment Summary:
```
Capability anchor: cap-id/name or N/A | Dependency gaps: N | Scope drift: yes/no
```

## Part 4: Required Finding Classification

You MUST classify your findings into these lanes:
- **Mainline Gaps**: plan-derived work or AC progress that is missing, incomplete, or regressing
- **Blocking Side Issues**: bugs or implementation issues that block the current mainline objective from succeeding safely
- **Queued Side Issues**: valid non-blocking follow-up issues that should be documented but must NOT take over the next round

Also include a one-line verdict:
```
Mainline Progress Verdict: ADVANCED / STALLED / REGRESSED
```

This verdict line is mandatory. If you omit it, the Humanize stop hook will block the round and require the review to be rerun.

If Claude mostly worked on queued side issues and failed to advance the mainline, say so explicitly.

## Part 5: ## Goal Tracker Update Requests (YOUR RESPONSIBILITY)

Claude should normally keep the **mutable section** of `goal-tracker.md` up to date directly. If Claude's summary contains a "Goal Tracker Update Request" section, or if you detect tracker drift during review, YOU must:

1. **Evaluate the tracker state**: Is the mutable section still aligned with the Ultimate Goal and current AC progress?
2. **If correction is needed**: Update @/work/first-proof-humanize-tdgou2bu/006-prob-007/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md yourself with the requested changes:
   - Move tasks between Active/Completed/Deferred sections as appropriate
   - Add entries to "Plan Evolution Log" with round number and justification
   - Add new issues to "Blocking Side Issues" or "Queued Side Issues" as appropriate
   - **NEVER modify the IMMUTABLE SECTION** (Ultimate Goal and Acceptance Criteria)
3. **If you reject a requested tracker change**: Include in your review why it was rejected

Common update requests you should handle:
- Task completion: Move from "Active Tasks" to "Completed and Verified"
- New blocking issues: Add to "Blocking Side Issues"
- New queued issues: Add to "Queued Side Issues"
- Plan changes: Add to "Plan Evolution Log" with your assessment
- Deferrals: Only allow with strong justification; add to "Explicitly Deferred"

## Part 6: Output Requirements

- In short, your review comments can include: problems/findings/blockers; claims that don't match reality; implementation plans for deferred current-scope work (to be implemented now); implementation plans for unfinished current-scope work; goal alignment issues.
- Your output should be structured so Claude can tell which items are mainline gaps, blocking side issues, and queued side issues.
- If after your investigation the actual situation does not match what Claude claims to have completed, or there is pending current-scope work to be done, output your review comments to @/work/first-proof-humanize-tdgou2bu/006-prob-007/.humanize/rlcr/2026-10-03_01-18-59/round-3-review-result.md.
- **CRITICAL**: Only output "COMPLETE" as the last line if ALL current-scope tasks from the original plan are FULLY completed with no deferrals
  - DEFERRED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is deferred
  - UNFINISHED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is pending
  - The ONLY condition for COMPLETE is: all current-scope original plan tasks are done, all current-scope ACs are met, no current-scope deferrals or pending work allowed
- The word COMPLETE on the last line will stop Claude.
