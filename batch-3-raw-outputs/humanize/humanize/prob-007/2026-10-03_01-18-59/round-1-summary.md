# Round 1 Summary

## What Was Implemented

Repaired the two blocking proof gaps from the Round-0 review, keeping
every theorem true but correcting one over-claim that the honest local
computation overturns:

1. **Finding 1 (Schreier / free factor, Corollary `cor:Hstruct`).**
   The claimed `ch^{-1}(2Z) = <x0,x1,x2^2>` (index 2, free on three
   generators) was false (the index-2 kernel of F3 -> Z/2 has Schreier
   rank 5) and internally contradictory. Replaced by the rigorous
   lattice bound: with `K = F3` on the consecutive basis
   `<x0,x1,x2>` and `chi` the exponent-sum (= `(v,p_i)`-linking)
   homomorphisms, the census generators lie in
   `F = ch_0^{-1}(2Z) ∩ ch_2^{-1}(2Z)` (index 4), and
   `H = <x1, x0^2, x2^2, (x0x1x2)^{-2}, u0, u2, u3>`; since
   `(ch_0,ch_2)` is a homomorphism to an abelian group, `H∩K ⊆ F`.
   Hence `x2 ∉ H`, `x2^2 ∈ H`, and `2 ≤ [PMCG(B):H] = [K:H∩K] ≤ 4`.

2. **Finding 2 (puncture census, Theorem `thm:monodromy-full`).**
   Items (i) and (vii) are now derived, not asserted. For (i): with
   `t = λ-c`, the vanishing `v = R(λ) = κ t^2 (1+O(t))`,
   `κ = -s_0'(c)^2/D(c) ≠ 0`, is of order exactly 2; along the small
   λ-loop, `p3` traces a contractible circle (no marked point inside)
   while `v` winds *twice* around `p0`, so the monodromy is the honest
   `x0^2` — **the reviewer's anticipated `x0` is not what the local
   model gives**; the paper now states the true `x0^{◦2}`.
   For (vii): in the `w=1/λ` chart, `R(λ) = -λ/8 (1+O(w))`,
   `v/p3 → -1/8`, `(R-1)/(R-λ) → 1`, so `p3,v` wind once around
   `p1 = ∞` in phase, giving `u3 x1 ∈ H` and hence `u3 ∈ H`. The
   undetermined exponents `a, b`, the unused element `x0'`, and the
   mis-stated derivative parenthetical are all removed.

3. **Downstream alignment.** Component count stated as the proved
   bound `2 ≤ #π0(D_f) ≤ 4` (the exact count is unused);
   `T_γ^{◦2}` fixes every component (it ∈ H), `T_γ` acts on
   components with orbits of size exactly 2; the AC-4
   no-infinite-orbit verdict (Corollary `cor:answer`) is retained and
   is now fully proved from the census + structural form. Unused
   macros `\Dfz,\Dfo` deleted.

## Files Changed

- `solution.tex` (repairs as above; 11 typeset pages).
- `.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md` (contract).
- `.humanize/rlcr/2026-10-03_01-18-59/round-1-summary.md` (this file).

## Validation

- `pdflatex solution.tex` run ×2: 0 errors, 0 undefined references, 11
  pages ≤ 16 (AC-5).
- Independent re-verification: Schreier basis rank for index-2 kernel
  in F3 is indeed 5 (confirming the original claim was wrong and the
  repair was necessary); the local models for census items (i) and
  (vii) were re-derived step by step (content of the branch disc,
  winding numbers, cross-ratio `(R-1)/(R-λ) → 1`).
- Sweep for residual objectionable text: none (`??`, "quick read",
  "not the claimed", "Schreier", "second branch", "Df 0/1", "≤ 8",
  "exactly two", `x_0'`, undetermined exponents — all absent).

## Remaining Items

- The exact value of `[\PMCG(B):H] ∈ {2,4}` is open (not needed for
  any theorem: the orbit conclusion only uses `x2∉H`, `x2^2∈H`).
  Flagged honestly in the text.
- No other pending or blocking issues.

## BitLesson Delta

Action: none  
Lesson ID(s): NONE  
Notes: no bitlesson-selector tool is installed in this environment; no
reusable lesson was produced this round (the repairs are specific to
this proof).
