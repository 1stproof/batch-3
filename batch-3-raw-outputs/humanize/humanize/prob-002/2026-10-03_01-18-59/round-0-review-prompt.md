# Code Review - Round 0

## Original Implementation Plan

**IMPORTANT**: The original plan that Claude is implementing is located at:
@plan.md

You MUST read this plan file first to understand the full scope of work before conducting your review.
This plan contains the complete requirements and implementation details that Claude should be following.
Only items under `## Acceptance Criteria` and current-scope Task Breakdown rows are completion gates.
Items under `## Future Work` / `## Out of Scope`, including `FUT-*` items, are informational and MUST NOT block the COMPLETE verdict.
If a current-scope AC or current-scope task is deferred, treat it as incomplete.

Based on the original plan and @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-0-prompt.md, Claude claims to have completed the work. Please conduct a thorough critical review to verify this.

---
Below is Claude's summary of the work completed:
<!-- CLAUDE's WORK SUMMARY START -->
# Round 0 Summary

## What Was Implemented

Produced a complete draft `solution.tex` proving the minimax rate
for the Darcy inverse-conductivity problem is
$n^{-2\alpha/(2\alpha+d+2)}$ up to logarithmic factors.

Key components:
- Exact linearization identity $\Delta(Tg)=g+\frac{x\cdot\nabla}{d}g$
  (Lemma 2.1) with the very-weak (integral) PDE formulation, avoiding any
  claim that $u_f\in H^1_0$.
- Transport operator $L=I+\frac{x\cdot\nabla}{d}$ shown to be a bounded
  isomorphism of $L^2(D)$ via the explicit radial inverse and a
  Cesaro/Hardy change-of-variables isometry (Lemma 2.2).
- Exact Fourier-side identity $\widehat{Lh}=-\frac1d\xi\cdot\nabla_\xi\widehat h$
  establishing $T$ is order exactly $-1$ (Lemma 3.1) plus a
  wavelet-packet scale estimate $\norm{Tg}\asymp\delta\norm{g}$ with a
  harmonic (boundary) correction (Lemma 3.2).
- Fano lower bound via Varshamov--Gilbert-separated wavelet packets and
  Gaussian-shift KL $=\frac n2\norm{u_f-u_0}^2$ (Sec 4).
- Upper bound via sieve least squares on the spectral projection of the
  white noise, a discrete inf-sup/scale inversion, bias ($L^2$ Cα→δ^α) and
  variance balancing, with the quadratic remainder controlled for α>1
  (Sec 5).

## Files Changed

- `solution.tex` (full rewrite): draft minimax solution, compiles to 10 pages.
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` (initialized).
- `.humanize/rlcr/2026-10-03_01-18-59/round-0-contract.md` (created).

## Validation

- `pdflatex solution.tex` (two passes): compiles clean, no undefined
  references, 10 pages (within the 16-page limit).

## Remaining Items

- The minimax rate up to logarithmic factors is fully established
  (matching powers of $n$; upper bound carries a stated power of $\log n$).
  Some technically-routine sub-estimates (wavelet-packet
  interference / almost-orthogonality detail in Lemma 3.2, boundary-layer
  handling in the discrete inf-sup Lemma 5.1, and the metric-entropy log
  factor) are stated with their main mechanism and sketched to a standard
  level of detail; they do not affect the stated rate and can be expanded
  if the reviewer requests. The solution compiles to 11 pages.

## Round 1 Addendum (post-review)

Applied the Round-0 review's directive plan (MG-1..MG-11, B-1..B-4):
- MG-8/MG-11: added "(External tools (precise statements))" section T1-T7.
- MG-10: transposition definition of $u_f\in L^2$ + uniqueness (§2.4);
  deleted the $H^{1+\alpha^-}$ claim.
- B-1/B-2: fixed Lemma 2.2(i) malformed display; renamed/refined the
  "Zero mean" remark to "Transport structure of L".
- MG-1/MG-6/MG-2: added Lemma (AO) `lem:ao` (separated-exponential
  almost-orthogonality with Schur/Cotlar sum); repaired U-term shells
  (off-shell decay via $\int\psi=0$ and Schwartz decay; scale factors).
- MG-3: replaced vacuous "injectivity + scale-invariance" lower bound by a
  direct rescaling argument with the scale-invariant functional
  $\mathcal J$ and $\psi$-dependent constant $c_U$.
- MG-5: rewrote Lemma `lem:invert` with (i) multi-scale lower bound,
  (ii) spectral tail via $H^{2K-1}$ inverse, (iii) subtraction.
- MG-9: corrected frequency bookkeeping ($\delta^{-1}$, eigenvalue
  $\delta^{-2}$); justified $H^{-1}$ gain for the fine bias.
- MG-4: removed circular $\|h\|_\infty\lesssim\delta^\alpha$; now
  compact-sieve ($C^\alpha\le2r$) + Gagliardo--Nirenberg interpolation +
  explicit two-regime dichotomy ($\alpha>1$ yields decay).
- MG-7/B-3: rewrote the log paragraph — noise enters as a LINEAR
  functional, no union bound needed, log-free upper bound; Theorem 1.1 and
  Prop. 5.1 now show $\Phi_n=n^{-2\alpha/(2\alpha+d+2)}$ (log-free).
- B-4: removed "harmless"/"standard-level"/"proof sketch"/"for
  completeness" hedges.

Validation: `pdflatex` two passes, 13 pages, no undefined references, no
errors/warnings. $c_U$ depends only on $(\psi,d)$; all constants
$(\alpha,d)$-dependent only; $\alpha>1$ used at Lemma 2.5, MG-3, MG-4.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: BitLesson KB is empty; no lessons applied.
<!-- CLAUDE's WORK SUMMARY  END  -->
---

## Development History (Integral Context)

Accumulated commits since loop start (oldest first):
```
21e20e5 Round 0: full draft solution.tex (minimax rate up to logs), compiles 11pp
fb9ee49 Round 0 cleanup: fix Hardy/Cesaro factors, packet framework, bias handling
fa1b81f Round 0: strengthen scale2 U-term (AO/interference), tracker update; 11pp clean
6cf12b2 Round 1: fix MG-1..MG-11, B-1..B-4 (AO lemma, rescale MG-3, compact-sieve MG-4, inf-sup proof, precise external tools, log-free)
abbe92e Round 1: rebuild artifacts (13pp clean)
13876cd Round 1: final rebuild
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

Read @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md and verify:

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
2. **If correction is needed**: Update @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md yourself with the requested changes:
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
- If after your investigation the actual situation does not match what Claude claims to have completed, or there is pending current-scope work to be done, output your review comments to @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-0-review-result.md.
- **CRITICAL**: Only output "COMPLETE" as the last line if ALL current-scope tasks from the original plan are FULLY completed with no deferrals
  - DEFERRED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is deferred
  - UNFINISHED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is pending
  - The ONLY condition for COMPLETE is: all current-scope original plan tasks are done, all current-scope ACs are met, no current-scope deferrals or pending work allowed
- The word COMPLETE on the last line will stop Claude.
