# Code Review - Round 3

## Original Implementation Plan

**IMPORTANT**: The original plan that Claude is implementing is located at:
@plan.md

You MUST read this plan file first to understand the full scope of work before conducting your review.
This plan contains the complete requirements and implementation details that Claude should be following.
Only items under `## Acceptance Criteria` and current-scope Task Breakdown rows are completion gates.
Items under `## Future Work` / `## Out of Scope`, including `FUT-*` items, are informational and MUST NOT block the COMPLETE verdict.
If a current-scope AC or current-scope task is deferred, treat it as incomplete.

Based on the original plan and @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-3-prompt.md, Claude claims to have completed the work. Please conduct a thorough critical review to verify this.

---
Below is Claude's summary of the work completed:
<!-- CLAUDE's WORK SUMMARY START -->
# Round 3 Summary

## Mainline objective
Close the three blocking upper-bound defects flagged in the review-phase
audit #5 so that Proposition 5.1's risk analysis is a complete proof of
the minimax upper bound `n^{-2α/(2α+d+2)}` (log-free), while keeping the
(sound) lower bound and the answer intact. Capability anchor: N/A (plan
has no capability map).

## Blocking issues fixed

### [P1] Intractable rδ^α discrepancy term (lines 1460–1474, 1490–1494)
**Diagnosis.** The crude estimate `‖e∇u_m‖_{H^{-1}} ≤ ‖e∇u_m‖₂ ≤
r‖∇u_m‖_∞` over the boundary collar injected a non-absorbable `rδ^α`
into the right side of `eq:basic`, which (after the δ-inversion) yields a
risk term `r²δ^{2α-2}` strictly larger than the claimed rate — the sieve
was oversmoothed where the noise is dominated by the collar bias.

**Fix.** The mechanism was a sieve-design defect, not a constant issue.
The sieve `F_δ` and the projection `Π_δ f` are now **interior**:
`Π_δ f := 1 + φ₀(f_{≤δ}−1)` with `φ₀ ≡ 0` on `B_{c_1/2} ∪ {|x|>3/4}`,
so the comparison point `m = Π_δ f_0` is constant-medium near origin and
boundary, and all perturbation comparisons happen in the interior. The
fine-scale bias paragraph is rewritten with an interior/collar split:
- *interior*: each scale-δ bump of `e` is mean-zero at `dist ≳ s` from
  `∂D`, so Lemma `lem:scale2`'s exact Fourier shell mechanism
  (`\abs ξ^{-1}` gain; harmonic correction `eq:qbound`) gives
  `‖G_int‖_{H^{-1}} ≲ δ‖e‖₂ = δ^{α+1}`;
- *collar*: Hölder + Nikolskii,
  `‖e‖_{L²(S)} ≲ s^{1/2−1/p}δ^α ≲ δ^{α+1/4} = o(δ^α)` —
  **no `rδ^α` term survives** (the earlier false clause
  "`∇u_m→0`, tangential vanishes" was removed and replaced by this
  robust `L^p` remainder; the boundary-layer content is projected into
  `Π_δ`). Hence `Z = ‖P_δ(u_{f₀}−u_m)‖₂ ≲ δ^{α+1}`, and `eq:basic`'s
  right side is `noise + δ^{α+1}`.

### Origin-mode inversion gap (lines 1385–1397)
**Diagnosis.** `lem:invert`'s lower bound held only on the annulus bulk
(gain `~δ`), while the sieve allowed `h` to live at the origin where the
exact radial gain is only `≍δ²`; triangle subtraction against the
`O(δ)` noise/bias then failed (`δ² < (c−Cr)δ`), leaving an r²δ^{2α−4}
blow-up parallel to P1 for origin-supported `h`.

**Fix.** Because the sieve is now interior (`F_δ` built from
bulk-annulus packets), every sieve error `h = f̂−m` is supported in the
bulk annulus by construction — **no origin modes are estimated**. The
`eq:infsupapp` lower bound now applies to the *whole* `h` (and
`lem:invert`'s statement/proof and `rem:modewise` were rewired to say
the subfamily *is* the sieve error). The "origin modes handled
identically, larger gain, never inverted" sentence is replaced by the
honest mechanism: origin/boundary content is projected into `Π_δ`
(hence into the bias), whose `u`-image is handled by the interior
degree-one gain `eq:finebias`, not inverted. `lem:origin`'s one-sided
`eq:origingain` remains as the record of the degeneracy.

### [P2] Line-1518 accounting dropped secondary terms
**Diagnosis.** The final display kept only `δ^{2α}` (bias) and
`δ^{-d-2}/n` (noise), silently dropping the discrepancy
`Θ(r²δ^{2α−2})` and an `O(r)` `(u_m−u_0)` offset "absorbed" by the
mathematically wrong step `rδ_∗^α ≤ δ_∗^{2α}`.

**Fix.** With the P1 repair, `eq:basic`'s right side is
`noise + δ^{α+1}` (the `rδ^α` generator of `r²δ^{2α−2}` is gone); the
bogus "`r ≤ δ_∗^α`" absorption step is removed, and the `(u_m−u_0)`
offset is now noted as lying inside `‖u_m−u_{f₀}‖`, already bounded by
`eq:finebias` at `δ^{α+1}`. The final display is recomputed: after
absorption and dividing by δ, `‖h‖₂ ≲ δ^{-1}(noise + δ^{α+1})`, so
`E‖h‖² ≲ δ^{-d-2}/n + δ^{2α}`, and every contributing term (bias,
discrepancy, noise) is `≲ δ_∗^{2α}` at the balance — log-free.

## How each was resolved (mechanism level)
- Sieve/projection: interior `Π_δ` (patch `φ₀`), `Π_δ f ∈ F(α,2r)`;
  `m` Dirichlet via the very-weak form (both solutions trace 0).
- Bias/discrepancy: interior shell gain + collar `L^p` remainder.
- Inversion: bulk sieve ⇒ `lem:invert` lower bound on the whole `h`.
- Sign conventions: `div(f∇u)=1` (source =1) preserved throughout;
  `m∈F(α,2r)` consistency at §(C).

## Issues reclassified as queued follow-up
None new. Existing queued items remain queued (Q-1 exact log power; F-5
expository compression of `lem:invert`(i) cross-scale AO; Q-2/Q-4/Q-5):
they do not block the round objective.

## Issues that could not be resolved
None blocking. Transparent caveat a reviewer may still press: (a) the
`opdiff`/`eq:opdiff` upper bound relies on a boundary Schauder estimate
for `u_m−u_0` on the collar (`m≡1` there, `u_0` known) — a true general
statement, quoted via T6; (b) the collar remainder's `p>d` Nikolskii
smallness and the `s=s(δ)` choice are stated with constants `(α,d,ψ)`
recorded; (c) the interior shell mechanism is applied at the compressed
level already used in `lem:scale2` (this is the F-5 queued item).

## Files changed
- `solution.tex`: §5.1(A) sieve/`Π_δ` (`eq:Pidelta`, `eq:approx`);
  `lem:invert` statement + proof opening; `lem:origin` wording;
  `rem:modewise`; §5.3(C) `m∈F(α,2r)`, `(u_m−u_0)` offset,
  `eq:basic0`/`eq:basic`/`eq:finebias` and the collar split, final
  accounting display; geometry `margin=0.85in`.
- `round-3-contract.md` (written), `goal-tracker.md` (Round-3 tasks +
  Plan Evolution), this summary.

## Validation
- `pdflatex -interaction=nonstopmode` ×2: **16 pages**, 0 errors, 0
  undefined references, `pdftotext` shows 0 `??`.
- Sign sweep: no residual `div(f∇u_f)=-1`, `1−|x|²`, `Δu₀=−1`, or
  `\nabla u_0(x)=-`.
- Overfull hboxes ≤ ~22pt (prose margin overflow at 0.85in; non-fatal).

## BitLesson Delta
- Action: add
- Lesson ID(s): BL-20261003-sieve-design-before-energy,
  BL-20261003-commit-each-wip
- Notes: two durable mathematical-workflow lessons recorded in
  bitlesson.md (project degenerate regions into the comparison point
  rather than proving uniform estimates; commit each WIP of the single
  deliverable).
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
6239eee Round 3 WIP: P1 collar→interior sieve/Pi_delta+fine-scale bias rewrite (r delta^alpha -> delta^{1+alpha}), origin-mode bulk sieve, P2 accounting; 16pp clean
70280ad Round 3 WIP2: fine-bias collar/interior split tightened (Dirichlet very-weak + collar eps_s + interior scale2 gain)
8c4a937 Round 3 WIP3: collar remainder made rigorous (Hold/Nikolskii s^{1/2-1/p}, no false nabla u_m->0; r delta^alpha eliminated)
5b33e37 Round 3 WIP4: coherence pass (sieve/lem:invert interior rewiring, modewise/origin wording); 16pp clean
370d363 Round 3: final (m in F(alpha,2r) consistency; 16pp clean, 0 undef, 0 ??)
192c2e9 Round 3 final: validated 16pp build (P1/P2/origin fixes), r delta^alpha eliminated, delta^{1+alpha} discrepancy; goal-tracker+round-3-summary+bitlesson updates
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
- If after your investigation the actual situation does not match what Claude claims to have completed, or there is pending current-scope work to be done, output your review comments to @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-3-review-result.md.
- **CRITICAL**: Only output "COMPLETE" as the last line if ALL current-scope tasks from the original plan are FULLY completed with no deferrals
  - DEFERRED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is deferred
  - UNFINISHED current-scope items are considered INCOMPLETE - do NOT output COMPLETE if any current-scope task is pending
  - The ONLY condition for COMPLETE is: all current-scope original plan tasks are done, all current-scope ACs are met, no current-scope deferrals or pending work allowed
- The word COMPLETE on the last line will stop Claude.
