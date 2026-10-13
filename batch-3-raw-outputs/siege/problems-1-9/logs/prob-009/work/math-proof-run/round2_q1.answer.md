# round2_q1: the Hodge-theoretic transport route. Result: partial; no complete proof

**Status.** I have no complete proof. Below I list what this route establishes (P), what is only heuristic (H), and the one lemma that is missing (M).

## Interpretations adopted
- I read the smooth triviality of 𝒱 → Δ, together with (i) and (ii), as follows: there is a homeomorphism (V̄_0, its boundary stratification) × Δ ≅ (closure of 𝒱, its stratification) that commutes with the maps to M̄_g up to homotopy.
- Consequently the classifying maps V_t → M_g (an orbifold) are homotopic through the family. So the monodromy ρ_t : π_1(V_t) → Sp(H^1(S_g, Z)) is independent of t up to conjugation. The same holds for the local monodromy around each boundary divisor, and in particular around the part of V̄_t near ∂V_t.

## (P1) Monodromy and weight filtrations are constant
- **Proof.** Homotopic maps induce conjugate representations. The local monodromy N around ∂V_t is the product of Dehn twists along the curves pinched in Γ, so it does not depend on t. The weight filtration W(N) is determined by N, so it is constant too. In particular Gr^W_1 of the limiting mixed Hodge structure (LMHS) is ⊕_j H^1(Ỹ_j), where Ỹ_j are the normalized components. As a local system along ∂V_t this sum is constant in t. The summand H^1(Y_t) is a constant (trivial) local system along ∂V_t.
- **Limitation.** All of this is topological. It is equally true for an arbitrary holomorphic arc t ↦ Y_t, so by itself it gives no constraint (compare context item 4).

## (H2) A sub-local system W over V_0
- By Wright's correspondence (cited from memory), V_0 comes from an orbit closure M with dim_C M = 4 and rank 2. Its tangent-space projection p(TM) ⊂ H^1 has dimension 4. This is for the abelian case; in the quadratic case one uses the anti-invariant part of the double cover.
- p(TM) is flat (Avila–Eskin–Möller; Filip's theorem that it is a sub-VHS), with Hodge numbers (2,2).
- Whether p(TM) depends only on X ∈ V_0, so that it descends to a rank-4 local system W on V_0, I have **not verified**. It is plausible because p(T_{(X,ω)}M) ⊇ E_X ⊕ Ē_X, and both sides have dimension 4.

## (P3, given H2) W persists over V_t
- By (P1), W is a sub-local system of H^1 over every V_t.
- By Deligne's semisimplicity theorem (from memory: on a quasi-projective base, a polarizable ℤ-VHS has a semisimple underlying local system, and its isotypic decomposition is by sub-VHS), the following holds. If W is an isotypic component of multiplicity 1, it underlies a sub-VHS over V_t.
- That VHS is unique up to a shift of the Hodge filtration (Deligne's uniqueness theorem for irreducible local systems). So over V_t, W has Hodge numbers (2,2) and a period map P_t : Ṽ_t → H_2 (the Siegel space).

## (M) The missing lemma
**Statement.** Suppose
- the period map P_t of W over V_t is non-constant, and
- the local monodromy and the boundary combinatorics are topologically those of V_0.

Then the restriction of the LMHS of W to ∂V_t forces the Y_t-summand to contain a nonzero sub-Hodge structure of H^1(Y_t) with a fixed, topologically determined endomorphism or period lattice. For example: a differential on Y_t with prescribed absolute periods, or real multiplication of a fixed type. Such Y_t lie in a countable set.

In the case g_i = 0, the analogous statement must be made for the extension classes in the LMHS, which encode cross-ratios of the nodes on Y_t.

## Why (M) is the crux, and why it is doubtful
- Whatever W "sees" of Y_t is a property of the limiting Hodge filtration F_lim. F_lim varies holomorphically with t. Only the weight filtration, N and the lattice are topological.
- A countability conclusion needs an algebraic condition on F_lim that is preserved for all t: a Hodge class, an endomorphism, or a Hodge-locus condition.
- At t = 0 such a condition might come from total geodesy, through the maximal Higgs field / Arakelov equality (Möller's argument for Teichmüller curves). But for t ≠ 0 nothing in (i) or (ii) preserves it, because V_t is not assumed totally geodesic.
- One could hope to transport an Arakelov-type equality, since its degree terms are Chern numbers of the Deligne extension, and those are topological given (P1). But Arakelov *equality* also involves the vanishing of a second fundamental form, which is not a topological condition. For base surfaces, I do not know an Arakelov-equality ⇒ rigidity statement that would apply here.

## Conclusion
- **Proved:** (P1). (P3) holds conditionally on (H2) and on W being an isotypic component of multiplicity 1.
- **Open:** (H2) and the lemma (M). Without (M), this route does not pin down Y_t.
- **Open question:** is the claim true as posed without further rigidity input, for example Teichmüller-geodesic rigidity of V_t? I suspect hypotheses (i) and (ii) are too weak as stated.

=== END OF ANSWER round2_q1 ===
