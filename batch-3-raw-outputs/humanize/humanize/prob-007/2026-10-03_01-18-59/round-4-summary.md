# Round 4 Summary

## Work Completed

Mainline objective: repair the rigor defects in `lem:allpairs` (round-3 review
Finding 1, the only blocking item) — a self-contained AC-2/AC-3 issue, no
impact on the headline results (component count {2,4} and orbit verdict, both
confirmed correct by the round-3 review, were left untouched).

- **(a) Anti-homomorphic extension + image equality proved.** `lem:allpairs`
  now states explicitly that Ψ extends to words in `E_f` via the
  anti-homomorphic (reversal) rule `Ψ(σ1σ2) = Ψ(σ2)Ψ(σ1)` proved in
  §sec:content. The image equality `Ψ(E_f) = ⟨u_0,u_2⟩ = PMCG(A)` is now
  *proved*, not asserted: every `w ∈ E_f` has `Ψ(w)` a reversed word in the
  generator images; the `x_1, x_i^{∘2}` factors contribute `e`; each
  `Ψ(a_j) ∈ ⟨u_0,u_2⟩` by the complementary-pair identification; and a
  subgroup is closed under reversal of its words, so
  `Ψ(E_f) ⊆ ⟨u_0,u_2⟩`, with the reverse inclusion from
  `u_0=Ψ(a_0), u_2=Ψ(a_2)`. (This is precisely the reversal-coincidence the
  review directed, per bitlesson BL-20261003-right-action-reversal.)

- **(b) `Ψ(x_i)=e` replaced by `Ψ(x_i^{∘2})=e`.** The undefined-quantifier
  `Ψ(x_i)` (on a twist that does not lift) is removed everywhere.
  `lem:allpairs` and `prop:contenttable` (eq:content) now use only the proved
  liftable-power statements: `Ψ(x_1)=e` (direct lift), `Ψ(x_i^{∘2})=e`
  (i≠1, smallest liftable power), and state explicitly that the unsquared
  `x_i` (i≠1) is *not* in `E_f` and `Ψ(x_i)` is *not* defined.

- **(c) `\Ef` defined once, early, single consistent generator set.** `\Ef`
  is now defined exactly once at the start of §sec:content as
  `⟨x_1, x_0^{∘2}, x_2^{∘2}, x_3^{∘2}, a_0,a_1,a_2,a_3⟩` (the LIFTABLE pair
  twists; adjacent `a_j = T_{{p_j,p_{j+1}}}`). The `u_i` (non-adjacent,
  `T_{{p_i,p_3}}`) vs `a_j` (adjacent) usage is reconciled explicitly:
  `a_i = u_i` for `i=1,3` on the nose, and under the forgetful map and under
  descent the adjacent and non-adjacent pair twists coincide on `A`
  (`T_{{p_{j+1},p_{j+2}}} = bar u_j` by the complementary-pair
  identification), so both generating sets map to the same subgroup of
  PMCG(A). The prior conflicting `E_f = ⟨x_i, u_i⟩` definition is removed.

- **Finding 2 (cheap confirmation).** Re-read `prop:contenttable`(b): the
  load is carried by the essential-twist / free-action argument and the
  topological-datum ("descended class depends only on δ, same at every
  component") justification; no semantic remnant of the deleted "conjugates
  of H" clause survives. Folded into the same edit.

## Files Changed

- `solution.tex` — as above (committed: `b8fb273`).

## Validation

- `pdflatex` ×2: **0 errors, 0 undefined references, 12 pages ≤ 16.**
- Residue sweep: no `Ψ(x_i)=` (unsquared non-`x_1`), no
  `E_f = ⟨x_i, u_i⟩`, no `cycle-pair twists u_i`, no `Ψ(x_i)=e\b`.
  `\Ef` definition is unique (one `:=`), `a_j` defined once, anti-hom rule
  and reversal-closure present. Compile independent re-check clean.
- Per the review, the component count `{2,4}` and the AC-4 orbit verdict
  (T_γ² identity, T_γ fixed-point-free 2-cycles on the honest sub-union) are
  UNTOUCHED.

## Remaining Items

- Exact `#pi_0(D_f) ∈ {2,4}` remains even but unpinned; deliberately
  unpursued (unused by every theorem and by the AC-4 verdict). Queued.
- The equalizer is the honest sub-union (round 3); the all-sheets equality is
  not asserted (correctly abandoned, unused).

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: bitlesson-selector not installed in this environment. Applied the
existing lesson (track the reversal in every word computation) to justify the
Ψ(E_f) image equality via subgroup-closure-under-reversal. No new reusable
failure mode produced beyond that lesson.
