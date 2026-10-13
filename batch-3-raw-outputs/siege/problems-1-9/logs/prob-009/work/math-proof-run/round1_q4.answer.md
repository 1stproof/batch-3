# round1_q4 — partial result (headline claim NOT proved)

## Interpretation
I read "smoothly trivial family" to mean: there is a diffeomorphism from V_0 × Δ onto 𝒱 that commutes with the projection to Δ, and the same holds for each boundary piece. I also assume that the closure of 𝒱 in M̄_g × Δ is the union over t of (closure of V_t) × {t}. This is the natural meaning of (i). With this reading, 𝒲 := closure(𝒱) ∩ (Δ_Γ × Δ) is the union over t of ∂V_t × {t}. It is a closed analytic subset of Δ_Γ × Δ, because closures of analytic sets in a compactification are analytic here (Remmert–Stein, applied to an algebraic family; cited from memory).

## Proposition (proved): Y_t depends holomorphically on t
**Proof.** Let F = π_i × id : Δ_Γ × Δ → M_{g_i,n_i} × Δ. The closure of ∂V_t is compact in the closure of Δ_Γ, so F restricted to 𝒲 extends to a proper map on closures. By Remmert's proper mapping theorem, F(𝒲) is an analytic set. By hypothesis, F(𝒲) = {(Y_t, t) : t ∈ Δ}, which is the graph of t ↦ Y_t. An analytic set that is the graph of a map over the disc Δ is the graph of a holomorphic map. The reason: it is a one-dimensional analytic set whose projection to Δ is one-to-one. Its normalization maps to Δ by a finite map of degree 1, and such a map is biholomorphic because Δ is smooth. ∎

So {Y_t} is a holomorphic arc through Y_0. To show it is constant, it suffices to show that Y_t ranges over a countable set, or more generally a 0-dimensional analytic set.

## Where the suggested route breaks
At t = 0, Wright's theorem (cited from memory) applies: a totally geodesic complex surface V_0 is covered by a rank-2 GL(2,R)-orbit closure M. Boundary theory then describes Y_0 level by level. The relevant sources are Chen–Wright (WYSIWYG) and Benirschke–Dozier–Grushevsky with the multi-scale compactification of Bainbridge–Chen–Gendron–Grushevsky–Möller. Plausibly this shows Y_0 is rigid, for example that it lies in a countable set of "special" surfaces such as Veech surfaces or cusp curves of Teichmüller curves.

For t ≠ 0, however, V_t carries no flat or GL(2,R) structure. Hypotheses (i) and (ii) are purely topological and incidence conditions on how the boundary strata fit together. They are preserved by any small deformation that keeps the stratification combinatorics, and they impose no algebraic condition on Y_t that could single out a countable set. So "Y_0 is special" does not by itself pass to Y_t.

What closes the gap would be a deformation-theoretic statement about the global surface. Note that the closure of V_t is compact, since V_t is a deformation of the algebraic surface closure(V_0).

**Missing lemma (precise statement).** Let S_0 be the normalization of the closure of V_0. Let D be the component of S_0 lying over ∂V_0 that maps to {Y_0} × (other factors). Then every first-order deformation of the map S_0 → M̄_g that preserves the boundary incidence data (i) and (ii) has zero derivative in the M_{g_i,n_i} direction along D.

For example, this would follow if a normal-bundle or Hodge-theoretic computation showed H^0(D, π_i^* T M_{g_i,n_i}) ≅ T_{Y_0} M_{g_i,n_i} maps to zero under the obstruction-compatible restriction from the deformation space of S_0. Given the Proposition, the Missing lemma implies the claim: Y_t is holomorphic with derivative 0 at every t, applying the lemma at each base point. That last step needs the lemma at each t, which again requires total geodesicity only at t = 0. So really the lemma must be proved for every surface in the family. I could not prove it.

## Status
- **Proved:** t ↦ Y_t is holomorphic, so it suffices to show its derivative is zero, or that it lands in a countable set.
- **Open:** the rigidity step, that is, the Missing lemma above or an equivalent argument that uses (i) and (ii) for t ≠ 0. I do not know a counterexample. I suspect the claim as posed needs this extra global input, which the problem's hypotheses do not obviously provide.

=== END OF ANSWER round1_q4 ===
