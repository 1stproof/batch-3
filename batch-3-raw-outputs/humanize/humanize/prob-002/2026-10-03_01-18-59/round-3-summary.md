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
