# Code Review Findings

You are in the **Review Phase**. Codex has performed a code review and found issues that need to be addressed.

## Required Re-anchor

Before touching code:
- Re-read the original plan at @plan.md
- Re-read the goal tracker at @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Refresh the current round contract at @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md

The round contract must preserve a single mainline objective. Code review findings do NOT automatically become the new round objective.
If the original plan contains `## Feature Map / Capability Map`, the refreshed contract must also preserve or update the current Capability Anchor intentionally.

## Review Results

## Codex Review Issues

- [P1] Intractable rδ^α discrepancy term blocks the δ∗ balance in the upper bound — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1460-1474
  In the risk bound, equation (eq:basic) (line 1470) inserts the discrepancy estimate ‖u_{f_0}−u_m‖₂ ≲ δ^{1+α} + rδ^α, so the right side scales like δ^α·r whereas the left side is (c/4)δ‖h‖₂. The final balance then asserts (line 1518) E‖h‖₂² ≲ δ∗^{-d-2}/n with δ∗ = n^{-1/(2α+d+2)} chosen by δ∗^{2α} = δ∗^{-d-2}/n (line 1521), which ignores the rδ^α term. Dividing (eq:basic) through by δ gives ‖h‖₂ ≲ δ^{-1}(n^{-1/2}‖ξ_δ‖₂ + rδ^α), i.e. ‖h‖₂ ≲ rδ^{α-1}, so E‖h‖₂² ≲ max(δ∗^{-d-2}/n, r²δ∗^{2α-2}); when n^{-1/2}‖ξ_δ‖₂ ≤ Crδ^α (equivalently n ≳ r^{-(2α+d+2)} — increasingly relevant as r→0 with the claimed r₀ fixed), the sieve is oversmoothed and the risk blows up at least as r²·δ∗^{2α-2} = Θ(n^{-2(α-1)/(2α+d+2)}), exceeding the claimed rate by the factor Θ(n^{2/(2α+d+2)}) (roughly the inverse of one smoothing degree). There is no way to absorb rδ^α into the left side, since it does not vanish with h; hence Proposition prop:upper does not establish an estimator achieving n^{-2α/(2α+d+2)}, which is the paper's main upper-bound claim. The supporting 'fine-scale bias' paragraph (lines 1490–1494) also merely asserts the boundary-collar improvement to δ^{1+α}—the same argument would apply verbatim to the lower-bound packet bumps near ∂D to give ‖T g‖ ≲ δ²‖g‖ there, contradicting the analysis—so even the proven part of the bound is only δ^α, not δ^{1+α}.

- [] Handle origin-near modes consistently in the recovery lower bound — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1385-1397
  ## Finding
  Lemma\ref{lem:invert} (eq:infsup) proves the inversion inequality cδ‖h^bulk‖₂ ≤ ‖P_δ T h^bulk‖₂ only for packet pieces whose centres lie in the annulus c₀ ≤ |x_λ| ≤ 1/2, and Lemma\ref{lem:origin} deliberately grants origin-near modes only a one-sided gain (‖T h_λ‖₂ ≳ δ_λ²‖h_λ‖₂). But in §(C) the sieve element h = \widehat f − Π_δ f_0 is arbitrary, so h (and P_δ T h) can be supported entirely on origin-near modes, for which the lower side of (eq:infsupapp) provides no cδ‖h‖₂ term: the only derivable lower bound is ‖P_δ T_m h‖₂ ≳ δ²‖h^origin‖₂ − C r δ‖h‖₂, and because (c − Cr)·δ < δ² for the relevant δ, triangle subtraction does not recover per-mode gains. The text says origin modes 'are handled identically with a larger gain and never inverted' (lines 1394–1397) and hence 'no two-sided estimate for them is needed' (line 1311), but the basic inequality requires exactly the missing two-sided (lower-side) control on those modes: if h lives at the origin, ‖h‖₂ ≤ Cδ^{-2}(noise + bias) ≈ Crδ^{α-2}, an r²δ^{2α-4} blow-up parallel to the P1 issue above. There is no constraint keeping \widehat f's wavelet content away from the origin (the sieve spans all packets of scale ≥ δ over D), so the risk bound as written does not hold for adversarial f₀ with origin-supported differences.
  
  ## Note
  This shares the same underlying mechanism (a term scaling like δ^{-1}×(bias at α order) not controlled by the signal side) as the rδ^α discrepancy issue at lines 1460–1474, but it is a separate defect located at the inf–sup step (this location) — fixing the discrepancy bound would not close this gap for origin-supported h.
  
  (Flagged at the lower-severity tier since it is potentially curable by combining the origin gain with the outer-ball gain via a patched inf–sup argument, but as the text stands the claim 'handled identically' is unsupported.)

- [P2] Line 1518 ignores secondary balance terms besides noise and bias — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1516-1522
  The displayed risk summary at line 1518, E‖\widehat f − f_0‖₂² ≲ δ∗^{2α} + δ∗^{-d-2}/n ≍ n^{-2α/(2α+d+2)}, retains only the approximation bias ‖e‖₂² and the pure-noise term. It silently drops two other pieces that (eq:basic) actually produces: (i) the discrepancy contribution ‖Z‖₂² = O((rδ^α)²) routed through ‖h‖₂, which per the finding at lines 1460–1474 contributes Θ(r²δ^{2α-2}) to the mean-squared error and is strictly larger than the stated rate for all r > 0 at δ = δ∗, and (ii) the 'additional O(r) offset' from (T_m − T)0 = u_m − u_0 which the text itself parks inside u_m − u_{f_0} (lines 1380–1384) but then does not carry into the final display — that offset is O(r) in L², hence O(r²) in squared risk, and it cannot be 'absorbed since rδ∗^α ≤ δ∗^{2α}' because δ∗^α ≫ δ∗^{2α} (δ∗ < 1, α > 0). The claim (line 1522) that 'the two terms are of equal order precisely at δ∗' is therefore an incomplete accounting: at best the argument yields risk ≲ δ∗^{2α} + r²δ∗^{2α-2} + r², and the conclusion that the stated log-free rate is achieved is not supported by the terms derived in the text.
The deliverable solution.tex is a 16-page proof that compiles cleanly, but the upper-bound (existence of an estimator attaining n^{-2α/(2α+d+2)}) contains an unabsorbable Θ(r²δ∗^{2α−2}) risk contribution from the rδ^α discrepancy term in equation (eq:basic): the sieve balance δ∗^{2α} = δ∗^{-d−2}/n is only valid when the noise dominates this term, otherwise the stated estimator's risk exceeds the claimed rate by Θ(n^{2/(2α+d+2)}). The origin-mode exclusion from the inversion lemma leaves an analogous gap, and the boundary gain δ ↦ δ^{1+α} in the fine-scale bias step is asserted without a valid mechanism (and would contradict the stated rate if it were available). Consequently the main theorem's upper bound — and with it the claimed minimax rate — is not established as written.

Full review comments:

- [P1] Intractable rδ^α discrepancy term blocks the δ∗ balance in the upper bound — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1460-1474
  In the risk bound, equation (eq:basic) (line 1470) inserts the discrepancy estimate ‖u_{f_0}−u_m‖₂ ≲ δ^{1+α} + rδ^α, so the right side scales like δ^α·r whereas the left side is (c/4)δ‖h‖₂. The final balance then asserts (line 1518) E‖h‖₂² ≲ δ∗^{-d-2}/n with δ∗ = n^{-1/(2α+d+2)} chosen by δ∗^{2α} = δ∗^{-d-2}/n (line 1521), which ignores the rδ^α term. Dividing (eq:basic) through by δ gives ‖h‖₂ ≲ δ^{-1}(n^{-1/2}‖ξ_δ‖₂ + rδ^α), i.e. ‖h‖₂ ≲ rδ^{α-1}, so E‖h‖₂² ≲ max(δ∗^{-d-2}/n, r²δ∗^{2α-2}); when n^{-1/2}‖ξ_δ‖₂ ≤ Crδ^α (equivalently n ≳ r^{-(2α+d+2)} — increasingly relevant as r→0 with the claimed r₀ fixed), the sieve is oversmoothed and the risk blows up at least as r²·δ∗^{2α-2} = Θ(n^{-2(α-1)/(2α+d+2)}), exceeding the claimed rate by the factor Θ(n^{2/(2α+d+2)}) (roughly the inverse of one smoothing degree). There is no way to absorb rδ^α into the left side, since it does not vanish with h; hence Proposition prop:upper does not establish an estimator achieving n^{-2α/(2α+d+2)}, which is the paper's main upper-bound claim. The supporting 'fine-scale bias' paragraph (lines 1490–1494) also merely asserts the boundary-collar improvement to δ^{1+α}—the same argument would apply verbatim to the lower-bound packet bumps near ∂D to give ‖T g‖ ≲ δ²‖g‖ there, contradicting the analysis—so even the proven part of the bound is only δ^α, not δ^{1+α}.

- [] Handle origin-near modes consistently in the recovery lower bound — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1385-1397
  ## Finding
  Lemma\ref{lem:invert} (eq:infsup) proves the inversion inequality cδ‖h^bulk‖₂ ≤ ‖P_δ T h^bulk‖₂ only for packet pieces whose centres lie in the annulus c₀ ≤ |x_λ| ≤ 1/2, and Lemma\ref{lem:origin} deliberately grants origin-near modes only a one-sided gain (‖T h_λ‖₂ ≳ δ_λ²‖h_λ‖₂). But in §(C) the sieve element h = \widehat f − Π_δ f_0 is arbitrary, so h (and P_δ T h) can be supported entirely on origin-near modes, for which the lower side of (eq:infsupapp) provides no cδ‖h‖₂ term: the only derivable lower bound is ‖P_δ T_m h‖₂ ≳ δ²‖h^origin‖₂ − C r δ‖h‖₂, and because (c − Cr)·δ < δ² for the relevant δ, triangle subtraction does not recover per-mode gains. The text says origin modes 'are handled identically with a larger gain and never inverted' (lines 1394–1397) and hence 'no two-sided estimate for them is needed' (line 1311), but the basic inequality requires exactly the missing two-sided (lower-side) control on those modes: if h lives at the origin, ‖h‖₂ ≤ Cδ^{-2}(noise + bias) ≈ Crδ^{α-2}, an r²δ^{2α-4} blow-up parallel to the P1 issue above. There is no constraint keeping \widehat f's wavelet content away from the origin (the sieve spans all packets of scale ≥ δ over D), so the risk bound as written does not hold for adversarial f₀ with origin-supported differences.
  
  ## Note
  This shares the same underlying mechanism (a term scaling like δ^{-1}×(bias at α order) not controlled by the signal side) as the rδ^α discrepancy issue at lines 1460–1474, but it is a separate defect located at the inf–sup step (this location) — fixing the discrepancy bound would not close this gap for origin-supported h.
  
  (Flagged at the lower-severity tier since it is potentially curable by combining the origin gain with the outer-ball gain via a patched inf–sup argument, but as the text stands the claim 'handled identically' is unsupported.)

- [P2] Line 1518 ignores secondary balance terms besides noise and bias — /work/first-proof-humanize-tdgou2bu/001-prob-002/solution.tex:1516-1522
  The displayed risk summary at line 1518, E‖\widehat f − f_0‖₂² ≲ δ∗^{2α} + δ∗^{-d-2}/n ≍ n^{-2α/(2α+d+2)}, retains only the approximation bias ‖e‖₂² and the pure-noise term. It silently drops two other pieces that (eq:basic) actually produces: (i) the discrepancy contribution ‖Z‖₂² = O((rδ^α)²) routed through ‖h‖₂, which per the finding at lines 1460–1474 contributes Θ(r²δ^{2α-2}) to the mean-squared error and is strictly larger than the stated rate for all r > 0 at δ = δ∗, and (ii) the 'additional O(r) offset' from (T_m − T)0 = u_m − u_0 which the text itself parks inside u_m − u_{f_0} (lines 1380–1384) but then does not carry into the final display — that offset is O(r) in L², hence O(r²) in squared risk, and it cannot be 'absorbed since rδ∗^α ≤ δ∗^{2α}' because δ∗^α ≫ δ∗^{2α} (δ∗ < 1, α > 0). The claim (line 1522) that 'the two terms are of equal order precisely at δ∗' is therefore an incomplete accounting: at best the argument yields risk ≲ δ∗^{2α} + r²δ∗^{2α-2} + r², and the conclusion that the stated log-free rate is achieved is not supported by the terms derived in the text.

## Issue Classification

Classify each review finding before acting on it:
- **blocking side issue**: prevents the current mainline objective from succeeding safely or prevents review acceptance
- **queued side issue**: valid follow-up, but does not block the current round objective

Queued issues may be documented, but they must NOT take over the round.

## Task Rules

Every task must use one lane tag:
- `[blocking]` for review findings that must be fixed now
- `[queued]` for non-blocking follow-up work

Do not create new `[mainline]` tasks in review phase unless the review proves the previous mainline objective was incomplete.

## Instructions

1. **Refresh the round contract** at `/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md`
2. **Address blocking issues first** and keep the mainline objective stable
3. **Keep fixes inside the Capability Anchor** unless the review proves the anchor was wrong
4. **Focus on fixes only** - do not add new features or make unrelated changes
5. **Commit your changes** after fixing the issues
6. **Write your summary** to: `/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-3-summary.md`

## Summary Template

Your summary should include:
- The mainline objective for this round
- Which blocking issues were fixed
- Which issues were reclassified as queued follow-up
- How each fixed issue was resolved
- Any issues that could not be resolved (with explanation)
- Confirmation that `goal-tracker.md` was updated if the blocking/queued issue lists changed
- A Goal Tracker Update Request only if tracker reconciliation still needs Codex help

## Important Notes

- The COMPLETE signal has no effect during the review phase
- You must address the code review findings to proceed
- After you commit and write your summary, Codex will perform another code review
- The loop continues until no `[P0-9]` issues are found

## BitLesson Selection (REQUIRED FOR EACH FIX TASK)

Before implementing each fix task, you MUST:

1. Read @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each fix task/sub-task to select relevant lesson IDs
3. Follow the selected lesson IDs (or `NONE`) during implementation

Reference: @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/bitlesson.md

## Task Tag Routing Reminder

Follow the plan's per-task routing tags strictly:
- `coding` task -> Claude executes directly
- `analyze` task -> execute via `/humanize:ask-codex`, then integrate the result
- Keep Goal Tracker Active Tasks columns `Tag` and `Owner` aligned with execution

## Capability Anchor Reminder

If the plan contains `## Feature Map / Capability Map`:
- The round contract must name the relevant Capability ID(s) or capability/feature name(s)
- Goal Tracker Active Tasks must keep their `Capability` column aligned with the round contract
- Mainline work must preserve the selected capability's business, design, and implementation context
- Do not let queued or future-scope capability work take over the current round
