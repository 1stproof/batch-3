# Code Review - Round 2

## Original Implementation Plan

**IMPORTANT**: The original plan that Claude is implementing is located at:
@plan.md

You MUST read this plan file first to understand the full scope of work before conducting your review.
This plan contains the complete requirements and implementation details that Claude should be following.
Only items under `## Acceptance Criteria` and current-scope Task Breakdown rows are completion gates.
Items under `## Future Work` / `## Out of Scope`, including `FUT-*` items, are informational and MUST NOT block the COMPLETE verdict.
If a current-scope AC or current-scope task is deferred, treat it as incomplete.

Based on the original plan and @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-prompt.md, Claude claims to have completed the work. Please conduct a thorough critical review to verify this.

---
Below is Claude's summary of the work completed:
<!-- CLAUDE's WORK SUMMARY START -->
# Round 2 Summary

## Work Completed
Round-2 contract (post audit #4) executed: the three mainline gaps (F-1,
F-2, F-3) and the blocking side issue (F-4) are all fixed at the mechanism
level.

- **F-1 (fatal / mainline — `lem:invert`(ii)/(iii)).** The old middle-band
  used the crude `C_1 δ‖h‖` bound inside a *norm-squared* subtraction,
  which collapses (`c_1²-(C_1+c/4)²<0`). Fixed by: (a) changing the sieve
  projector `P_δ` to cut at Dirichlet eigenvalue `≤ C_W δ^{-2}` (i.e.
  physical scale `≳ δ`, matching the one-degree smoothing; `dim V_δ ≍
  δ^{-d}` preserved by Weyl — `T:weyl` and §(A) updated); (b) bounding the
  spectral tail by `lem:scale2`'s own off-shell Schwartz decay
  (`eq:Uupper` tails, `∫ψ=0`), giving the new `eq:spectail`
  `‖(I-P_δ)Thᵇᵘˡᵏ‖ ≤ C̃ C_W^{-N/4} δ‖hᵇᵘˡᵏ‖`, with the fixed constant
  `C_W` chosen so the tail `≤ (c/4)δ‖h‖`; (c) step (iii) now uses
  *ordinary norm (triangle) subtraction*
  `‖P_δTh‖ ≥ ‖Th‖ - ‖(I-P_δ)Th‖ = (3c/4)δ‖h‖`, replacing the impossible
  norm-square line. The inf–sup input to `eq:infsupapp` → the basic
  inequality is now sound.
- **F-2 (mainline — `lem:origin`).** The invented two-sided interpolation
  `‖Th_λ‖ ≍ δ_λ(δ_λ+|x_λ|)‖h_λ‖` (justified only by a "one-ray"
  computation + "monotone" rhetoric) is **deleted**. Replaced by the
  one-sided bound actually used downstream, `eq:origingain`
  `‖Th_λ‖ ≳ δ_λ²‖h_λ‖` for origin-near modes, proved by re-running
  `lem:scale2`'s loaded-shell power count with the single change
  `|x_m|² ≲ δ_λ²` (one full extra power of `δ_λ`), harmonic `q` absorbed
  into `δ_0`. `rem:modewise` updated (Γ_λ phrase gone; "never inverted, no
  two-sided estimate needed"). The radial endpoint's exterior step
  (`w≡0` on `[δ,1]`) was made rigorous (`w'=0` there + `w(1)=0` instead
  of quoting scale2's annulus support fact).
- **F-3 (mainline — absorption).** The chain now cites `lem:quad`'s
  `‖ρ̃‖₂ ≲ ‖h‖_∞‖h‖₂` and the pointwise `‖h‖_∞ ≤ Σ_j‖h_j‖_∞` (L^∞
  summability since `‖h_j‖_∞ ≲ 2^{-jα}r`, `α>0`) *before* dividing by
  `δ‖h‖₂`, closing the explicitness gap; conclusion `ω_δ = rδ^{α-1} → 0`
  (`α>1`) unchanged.
- **F-4 (blocking — source sign).** Global sweep to `problem.tex`'s
  `div(f∇u)=1`: `u_0=(|x|²-1)/(2d)`, `∇u_0=x/d`, `Δu_0=1`; sign-invariance
  parenthetical deleted; `eq:u0prop` sign flipped; `lem:lin` defines `Tg`
  by `-Δw = -div(g∇u_0)` so `Δ(Tg)=+Lg` is preserved (all uses of `T`
  are norm-valued, hence sign-agnostic under `T↦-T`); `lem:apriori`
  barriers recomputed (sub `u_0/(1+r)`, super `u_0/(1-r)`); `(f-1)∇u_0
  =(f-1)x/d`; opdiff `u_m-u_0=+Δ^{-1}div((m-1)∇u_0)`;
  `div(m∇(u_m-u_0))=+div((m-1)∇u_0)`; fine-scale `div(f_0∇w)=+div(e∇u_m)`.

**Incident note.** Mid-pass a `git stash`/`pop` cycle briefly reverted the
uncommitted edits (and a dangling recovery stash was dropped). The exact
patch sequence was replayed and the work committed immediately
(`ccec7ee`, final build `d80b673`).

## Files Changed
- `solution.tex`: F-1 (`T:weyl`, §(A) `V_δ`/`P_δ`, `lem:invert` + proof
  (ii)/(iii), `eq:spectail`), F-2 (`lem:origin` statement + proof,
  `eq:origingain`, `rem:modewise`), F-3 (absorption chain), F-4 (u₀
  display, `eq:u0prop`, `lem:lin`, `lem:apriori`, `∇u₀`/opdiff/fine-scale
  sign sites); page-economy `geometry margin=0.93in`.
- Audit artifacts (`solution.pdf/.aux/.log/.out`) regenerated.

## Validation
- `pdflatex -interaction=nonstopmode` ×2: **16 pages**, 0 errors, 0
  undefined references, `pdftotext` shows 0 `??`.
- Sign-consistency grep: no residual `div(f∇u_f)=-1`, no `1-|x|²`,
  no `\Delta u_0=-1`, no `\nabla u_0(x)=-`, no "immaterial" parenthetical.
- PDF text inspection of §5.2 (Lemmas 5.2/5.3, (ii)/(iii), Remark 5.4)
  and the absorption display confirms all four fixes render correctly.
- No `\linespread`/`\setlength` hacks; article class + standard packages.
- Overfull hboxes: 7, all pre-existing in un-edited regions (non-fatal).

## Remaining Items
- Awaits independent audit #5. Within round scope: none. Out-of-scope
  (contract "queued side issues"): F-5 expository compression
  (`lem:invert`(i) cross-scale AO), Q-1/Q-2/Q-4/Q-5. The AC-3 note
  "reduce to ≤15pp for safety" is superseded: geometry `margin=0.93in`
  gives 16pp without content cuts.

## BitLesson Delta
- Action: add
- Lesson ID(s): BL-20261003-no-git-stash-mid-round
- Notes: Never run `git stash`/`git pop` while holding uncommitted
  deliverable edits in this loop — a stash conflict silently reverted an
  entire round's work; commit to a branch (or a WIP commit) before any
  compile-vs-baseline comparison. Reversible-by-commit beats stash.
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
63fe231 Round 1: audit-#3 sweep — G1 rebuild, G2 origin radial + spectral tail, G3 Poisson harmonic, B-5/6/7/8/9; 16pp clean
abbb1c8 Round 1 review (audit #4): verify audit-#3 sweep landed; force back F-1 middle-band inf-sup and F-2 origin interpolation as blocking mainline; F-3 absorption one-liner, F-4 source-sign sweep; ADVANCED not COMPLETE
ccec7ee Round 2: fix F-1 (P_delta physical-scale cutoff C_W + off-shell tail + triangle subtraction), F-2 (origin one-sided bound, drop invented interpolation), F-3 (h_infty<=sum h_j chain), F-4 (source-sign sweep to div=+1); 16pp clean
d80b673 Round 2: final validated build (16pp, 0 errors, 0 undefined refs, 0 ??)
```

### Recent Round Files
Read these files before conducting your review to understand the trajectory of work:
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
- If after your investigation the actual situation does not match what Claude claims to have completed, or there is pending current-scope work to be done, output your review comments to @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-review-result.md.
- **CRITICAL**: Only output "COMPLETE" as the last line if ALL current-scope tasks from the original plan are FULLY completed with no deferrals
  - DEFERRED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is deferred
  - UNFINISHED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is pending
  - The ONLY condition for COMPLETE is: all current-scope original plan tasks are done, all current-scope ACs are met, no current-scope deferrals or pending work allowed
- The word COMPLETE on the last line will stop Claude.
