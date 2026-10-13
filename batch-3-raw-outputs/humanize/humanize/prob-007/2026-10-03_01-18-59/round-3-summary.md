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
