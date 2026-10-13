# Answer to round1_q4

## Part A (proved, modulo two standard results quoted from memory)

**Claim.** σ is a strictly convex rational polyhedral cone and Σ is a fan with |Σ| = σ, ordered by c' ≤ c iff c' is a face of c. Let r(c) be the smallest face of σ containing c. Then for every G : Faces(σ)^op → Ab we have R lim_{Σ^op} G∘r = G(σ), concentrated in degree 0.

**Cited results (from memory).**
(Q) Homotopy-initial functors (Quillen's Theorem A, version for limits). Let f : C → D be a functor of small categories. Suppose that for every d the comma category f/d, whose objects are pairs (c, f(c) → d), has a contractible nerve. Then R lim_D G → R lim_C f^*G is an isomorphism for every abelian-group-valued G.
(H) Let K be a regular CW complex (for example a polytopal complex) and L a subcomplex. Then the order complex of the poset of cells of K that are not in L is homotopy equivalent to |K| \ |L|; in fact it is a deformation retract of it inside the barycentric subdivision.

**Step 1: reduction to contractibility.** Write f = r : Σ^op → D := Faces(σ)^op. In D the object σ is initial, because τ ⊆ σ for every face τ. Hence R lim_D G = G(σ) in degree 0. Fix a face τ. A morphism f(c) → τ in D means τ ⊆ r(c). So f/τ is the poset U_τ = {c ∈ Σ : r(c) ⊇ τ}, with the order of Σ reversed, and its nerve is the same as the nerve of U_τ. By (Q) it therefore suffices to show that every U_τ is contractible.

**Step 2: identifying U_τ.**
- Take a cone c ∈ Σ and a face F of σ. If relint c meets F, then c ⊆ F, because F is a face and c is convex. So r(c) is the unique face F of σ with relint c ⊆ relint F. Each face of σ is a union of cones of Σ, so it is a subfan.
- Hence r(c) ⊉ τ iff c ⊆ F for some face F with F ⊉ τ. So U_τ = Σ \ L_τ, where L_τ is the subfan made of the cones lying in the union Z_τ of the faces of σ that do not contain τ.
- If τ = 0, then L_τ = ∅ and U_τ = Σ. This poset has the least element {0}, so it is contractible.
- If τ ≠ 0, then {0} ∈ L_τ. Choose a linear form ℓ that is positive on σ \ 0, and slice at ℓ = 1. The slices give a polytopal complex K subdividing the polytope Δ = σ ∩ {ℓ = 1}, and K has the same poset as Σ \ {0}. The subcomplex L_τ becomes L, the union of the faces of Δ that do not contain τ' = τ ∩ {ℓ = 1} ≠ ∅. By (H), U_τ ≃ Δ \ |L|.

**Step 3: Δ \ |L| is star-shaped, hence contractible.** Choose p ∈ relint τ', and let x ∈ Δ \ |L| and y = (1−t)p + tx with t ∈ [0,1].
- If t = 1, then y = x, which is not in |L|.
- If t < 1 and y lies in a face F of Δ, then p ∈ F. For t = 0 this is because y = p. For 0 < t < 1 it holds because y is an interior point of the segment [p, x] and F is a face.
- Since p ∈ relint τ' ∩ F, we get τ' ⊆ F, so F is not one of the faces making up L. Hence y ∉ |L|.

So Δ \ |L| is star-shaped about p and contractible, which proves the claim. ∎

## Part B: not done

I did not prove the reduction. The following steps are still open:
(i) charts of a subdivision form birhizomic covers of P;
(ii) every birhizomic cover of P is refined by a subdivision cover, possibly combined with localizations;
(iii) a Čech-to-derived comparison, with Čech nerves computed by the finite posets of Part A;
(iv) the values of π^{-1}F on the chart objects after sheafification.

Assuming (i)–(iv), Part A gives that the cohomology at P equals F(P) in degree 0, for P finitely generated.

## Status

- **Proved:** Part A.
- **Not proved:** Part B. So the headline question, even for fine P, depends on the open steps (i)–(iv). Non-finitely-generated P is not touched at all.

=== END OF ANSWER round1_q4 ===
