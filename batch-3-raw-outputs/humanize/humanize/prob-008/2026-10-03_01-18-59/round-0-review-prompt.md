# Code Review - Round 0

## Original Implementation Plan

**IMPORTANT**: The original plan that Claude is implementing is located at:
@plan.md

You MUST read this plan file first to understand the full scope of work before conducting your review.
This plan contains the complete requirements and implementation details that Claude should be following.
Only items under `## Acceptance Criteria` and current-scope Task Breakdown rows are completion gates.
Items under `## Future Work` / `## Out of Scope`, including `FUT-*` items, are informational and MUST NOT block the COMPLETE verdict.
If a current-scope AC or current-scope task is deferred, treat it as incomplete.

Based on the original plan and @/work/first-proof-humanize-tdgou2bu/007-prob-008/.humanize/rlcr/2026-10-03_01-18-59/round-0-prompt.md, Claude claims to have completed the work. Please conduct a thorough critical review to verify this.

---
Below is Claude's summary of the work completed:
<!-- CLAUDE's WORK SUMMARY START -->
# Round 0 Summary

## What Was Implemented

A complete, rigorous proof of the prob-008 statement in `solution.tex`:
if $X$ is a globally hypoelliptic smooth vector field on a compact connected
smooth manifold $M$ with flow $g_t$, then the flow has zero topological entropy.

Proof structure (three steps):
1. **Structure theorem** (Theorem 2.1, Greenfield--Wallach, quoted precisely):
   GH forces $g_t$ to be a Diophantine one-parameter subgroup of a smooth
   action of a compact torus $\mathbb{T}^k$ on $M$.
2. **Equicontinuity** (Lemma 2.2, proved in full): averaging any Riemannian
   metric over the compact group action makes every $g_t$ an isometry, hence
   the family $\{g_t\}$ is equicontinuous.
3. **Zero entropy** (Section 3, proved in full): Bowen's
   $(n,\varepsilon)$-separated sets for an equicontinuous map are separated in
   the ordinary metric sense at time zero, hence have cardinality bounded
   independently of $n$; therefore $h_\mathrm{top}(g_1) = 0$.

Consistency checks (Remark 2.2) verify the statement is non-vacuous
(Diophantine linear flows on $\mathbb{T}^d$ satisfy GH and have zero entropy),
that the zero field is not GH, and that fields with zeros/periodic orbits/
hyperbolic pieces are never GH (their flows cannot be compact-group actions).

### Plan note / evolution
The initial plan sketched a different route: "construct a Liouvillian
distribution $u$ with $\mathcal{L}_X u = 1$ if $X \neq 0$ to force $X = 0$".
That only captures the (6.1) Liouville/suspension case. Global hypoellipticity
is also satisfied by Diophantine linear flows on tori (no periodic orbit,
dense orbits), so the proof must cover that case too. The Greenfield--Wallach
structure theorem route handles all GH vector fields uniformly, so the plan
was updated accordingly (recorded in the goal-tracker Plan Evolution Log).

## Files Changed

- `solution.tex` — replaced the stub with the full proof (4 typeset pages).

## Validation

- `pdflatex -interaction=nonstopmode -halt-on-error solution.tex` (run twice):
  compiles cleanly, no errors, no undefined references, **4 pages** (≤ 16).
- Only standard packages: amsmath, amssymb, amsthm, mathtools, geometry,
  enumitem, hyperref — all installed; no external files/fonts/shell macros.
- Line-by-line self-audit: quantifiers/logical direction checked; the
  Diophantine vs Liouville dividing line and entropy-convention independence
  explicitly addressed.

## Remaining Items

- None for the core proof; the only external input is the Greenfield--Wallach
  structure theorem, stated precisely with a reference.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: bitlesson knowledge base was empty; no new reusable lessons recorded
this round (the correction was a plan-level strategy fix, already logged in
the goal tracker's Plan Evolution Log).
<!-- CLAUDE's WORK SUMMARY  END  -->
---

## Development History (Integral Context)

Accumulated commits since loop start (oldest first):
```
8548853 Round 0: prove GH vector field flow has zero topological entropy
f627681 Ignore LaTeX build artifacts (solution.{aux,log,out,pdf})
```

### Recent Round Files
Read these files before conducting your review to understand the trajectory of work:
(first round, no prior history)

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

Read @/work/first-proof-humanize-tdgou2bu/007-prob-008/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md and verify:

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
2. **If correction is needed**: Update @/work/first-proof-humanize-tdgou2bu/007-prob-008/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md yourself with the requested changes:
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
- If after your investigation the actual situation does not match what Claude claims to have completed, or there is pending current-scope work to be done, output your review comments to @/work/first-proof-humanize-tdgou2bu/007-prob-008/.humanize/rlcr/2026-10-03_01-18-59/round-0-review-result.md.
- **CRITICAL**: Only output "COMPLETE" as the last line if ALL current-scope tasks from the original plan are FULLY completed with no deferrals
  - DEFERRED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is deferred
  - UNFINISHED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is pending
  - The ONLY condition for COMPLETE is: all current-scope original plan tasks are done, all current-scope ACs are met, no current-scope deferrals or pending work allowed
- The word COMPLETE on the last line will stop Claude.
