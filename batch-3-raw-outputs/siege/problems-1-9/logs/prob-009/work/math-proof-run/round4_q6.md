kind: attempt
Open question attempted: the run's missing statement MS4 (ledger entry 17), via a NAMED approach not yet tried — rigidity of homotopic holomorphic maps into M_g (Imayoshi–Shiga / Arakelov–Parshin) combined with rigidity of the complex structure of the base (ledger entry 18).

## The statement to prove
**Missing statement (MS4, entry 17).** Let g ≥ 2. Let V_0 ⊂ M_g be a smooth 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric. Let 𝒱 ⊂ M_g × Δ be a complex submanifold with V_t = ψ(φ^{-1}(t)), satisfying hypotheses (i) and (ii) of the problem, and read as follows:
- (R1) closure(𝒱) ⊂ M̄_g × Δ is analytic with fibre closure(V_t) over t;
- (R2) there is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G.

Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product boundary stratum. Suppose that for every t the set ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1 and π_i(∂V_t) = {Y_t} for one fixed index i. Then the holomorphic map Δ → M_{g_i,n_i}, t ↦ Y_t, is constant.


## How the statement completes the problem (the chain)
By P-a (Lemma 1), t ↦ Y_t is a holomorphic map from the disc into M_{g_i,n_i}; the problem's conclusion π_i(∂V_t) = {Y_0} for all t is then literally the statement that this map is constant. So the missing statement below IS the problem's claim, in reduced form, under the two readings (R1),(R2) of the hypotheses that all earlier attempts adopted. If you believe a reading is unjustified or that a weaker reading suffices, say so; if your proof needs a further reading of the hypotheses, state it explicitly and argue that it is what the problem's hypotheses mean.

## Prior results (spliced verbatim from earlier answer files; they rely on readings (R1),(R2) stated in the missing statement; re-check anything you use)

### P-a. Holomorphy of Y_t, countability reduction, local insufficiency (from an earlier answer)
**Lemma 1 (holomorphy).** t ↦ Y_t is holomorphic Δ → M_{g_i,n_i}.
Proof: closure(𝒱) ∩ (Δ_Γ × Δ) is analytic; its image under π_i × id is {(Y_t,t)}. The map is proper over relatively compact pieces of Δ: the closure of ∂V_t in M̄ meets deeper strata only where factor i stays in M_{g_i,n_i}, since π_i is constant along ∂V_t. So Remmert's proper mapping theorem (cited from memory) makes the image analytic. An analytic set that is the graph of a map from a disc is the graph of a holomorphic map. ∎
Consequence: the claim is equivalent to Y_t being locally constant near t=0 (identity theorem), or to {Y_t} being countable.

**Lemma 3 (countability route).** If every V_t is totally geodesic, the claim holds. Reason: totally geodesic subvarieties are countable (Wright; Eskin–Mirzakhani–Mohammadi, cited from memory), and a continuous family taking countably many values is constant.

**Observation 4 (local arguments are insufficient).** Near ∂V_t, take coordinates (y, z, s) with y ∈ M_{g_i,n_i}, z on the other factors and s plumbing parameters. A germ y = Y_t + O(|s|) with Y_t any holomorphic arc meets every local condition imposed by (i) and (ii). Hypothesis (ii) is tautological along {Y_t} × closure(C_t). The local monodromy (Dehn twists about the pinched curves) does not see Y_t either. So any proof must use a global property of closure(V_t), such as Hodge-theoretic rigidity of the rank-4 sub-VHS W from Wright/Filip, or the vanishing in Lemma 2.

### P-b. Hypothesis (ii) along Γ is tautological (from an earlier answer)
**Lemma 1 (the deeper boundary does not pin Y_t).** Write ∂V_t = {Y_t} × C_t, where C_t is a curve in the other factors. Every point of the closure of ∂V_t in a deeper stratum Δ_{G'} comes from degenerating C_t, or from bubbling inside the remaining factors. So that point still has the component Y_t at the i-th vertex, or a stable curve obtained by degenerating Y_t if the limit also lands in the closure of M_{g_i,n_i}. If we apply (ii) only to the pair (Δ_Γ, Δ_{G'}), it says that these deeper points of V_t arise as limits of ∂V_t. That holds tautologically for every t, whatever Y_t is. So (ii) applied to Γ and its degenerations gives no constraint on Y_t.

*Proof.* The statement is local in a product chart of closure(M_{g_i,n_i}) × (the other factors). The closure of a product set is the product of the closures. ∎

### P-c. Topological constancy (from an earlier answer)
## Interpretations adopted
- I read the smooth triviality of 𝒱 → Δ, together with (i) and (ii), as follows: there is a homeomorphism (V̄_0, its boundary stratification) × Δ ≅ (closure of 𝒱, its stratification) that commutes with the maps to M̄_g up to homotopy.
- Consequently the classifying maps V_t → M_g (an orbifold) are homotopic through the family. So the monodromy ρ_t : π_1(V_t) → Sp(H^1(S_g, Z)) is independent of t up to conjugation. The same holds for the local monodromy around each boundary divisor, and in particular around the part of V̄_t near ∂V_t.

## (P1) Monodromy and weight filtrations are constant
- **Proof.** Homotopic maps induce conjugate representations. The local monodromy N around ∂V_t is the product of Dehn twists along the curves pinched in Γ, so it does not depend on t. The weight filtration W(N) is determined by N, so it is constant too. In particular Gr^W_1 of the limiting mixed Hodge structure (LMHS) is ⊕_j H^1(Ỹ_j), where Ỹ_j are the normalized components. As a local system along ∂V_t this sum is constant in t. The summand H^1(Y_t) is a constant (trivial) local system along ∂V_t.
- **Limitation.** All of this is topological. It is equally true for an arbitrary holomorphic arc t ↦ Y_t, so by itself it gives no constraint (compare context item 4).

### P-d. Pinning lemma and how (ii) transports incidences (from an earlier answer)
## Step B is rigorous once Step A holds (pinning lemma)
**Lemma B.** Suppose:
- G' is a degeneration of Γ in which the vertex carrying Y stays intact;
- P_t ∈ closure(∂V_t) ∩ Δ_{G'} depends continuously on t;
- E_t is a 1-dimensional boundary piece in a stratum Δ_G with Δ_{G'} ⊂ closure(Δ_G);
- P_t ∈ closure(E_t) for all t;
- closure(E_t) = closure(E_0) for all t.

Then Y_t = Y_0.

*Proof.* E_0 is a quasi-projective curve. So closure(E_0) \ E_0 is finite, and in particular closure(E_0) ∩ Δ_{G'} is finite. The continuous map t -> P_t takes values in this finite set and Δ is connected, so P_t = P_0 for all t. The factor of P_t at the vertex carrying Y is Y_t, by context item 2. Hence Y_t = Y_0. ∎

How the incidence P_t ∈ closure(E_t) persists:
- Hypothesis (ii), applied with the pair (Δ_G, Δ_{G'}) and a neighbourhood U of P_0, says: if near P_0 the set closure(V_0) ∩ Δ_{G'} is locally contained in the closure of the Δ_G-piece, then the same holds for every t.
- So the persistence is legitimate exactly when, locally at P_0, the deeper boundary of V_0 comes out of E_0. This holds when P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} that lies in closure(E_0).
- Continuity of P_t in t then comes from (i) applied to Δ_{G'}.

### P-e. Kobayashi contraction (from an earlier answer)
**Lemma 1 (contraction).** Let k_X denote the Kobayashi distance. For all t and all x, y in Ṽ_t, d_T(f_t x, f_t y) ≤ k_{Ṽ_t}(x, y). Hence for every γ in G the translation lengths satisfy ℓ_{Ṽ_t}(γ) ≥ ℓ_T(ρ(γ)).
*Proof.* Holomorphic maps do not increase Kobayashi distance. By Royden's theorem (cited from memory), the Kobayashi distance of T_g is the Teichmüller distance d_T. Take the infimum over orbits. ∎

**Lemma 2 (t = 0).** Suppose V_0 is totally geodesic in the sense used here: through each point and each tangent direction, the Teichmüller disc lies in V_0. Then k_{Ṽ_0} = d_T restricted to Ṽ_0.
*Proof.* Let x, y be points of Ṽ_0. The Teichmüller geodesic from x to y lies in a Teichmüller disc D. The disc D is tangent to Ṽ_0 at x, so D ⊂ Ṽ_0. D is a holomorphic isometric disc, so k_{Ṽ_0}(x, y) ≤ k_D(x, y) = d_T(x, y). Lemma 1 gives the reverse inequality. ∎

Consequence: for γ with ρ(γ) pseudo-Anosov, ℓ_{Ṽ_t}(γ) ≥ ℓ_T(ρ(γ)) ≥ … with equality at t = 0 whenever the axis lies in Ṽ_0. So the Kobayashi length spectrum of V_t dominates that of V_0. (For a pseudo-Anosov arising from an affine automorphism inside the orbit closure, the axis is a Teichmüller geodesic in a disc contained in Ṽ_0.)

## The approach to pursue (you may depart from it if you say why)
Write f_t : V_t → M_g for the inclusions (pass to a finite-index torsion-free level structure so that M_g is replaced by a fine moduli space and V_t by finite étale covers; check this is harmless). By (R2) there are diffeomorphisms Φ_t : V_0 → V_t, continuous in t, so f_t∘Φ_t is homotopic to f_0.
Step 1 (rigidity over a fixed base). State precisely and prove (or cite precisely, checking hypotheses) the rigidity theorem: if B is a connected quasi-projective manifold and h_0, h_1 : B → M_g (level structure) are homotopic holomorphic maps with h_0 non-constant on a family of curves covering B (or: with non-elementary monodromy on such curves), then h_0 = h_1. For B a finite-type Riemann surface this is Imayoshi–Shiga's theorem (equivalently Arakelov–Parshin rigidity); reduce the surface case to curves (e.g. general curve sections through every point; Lefschetz-type surjectivity of π_1 is not needed if one compares the restricted maps directly via the restricted homotopy). Check the isotrivial-direction issue: V_0 contains no curve along which the family is isotrivial? (a totally geodesic surface contains Teichmüller discs through every point in every direction, so every holomorphic curve in V_0 has non-constant image — justify).
Step 2 (the crux: the base does not move). Show that there are biholomorphisms h_t : V_0 → V_t homotopic to Φ_t; then Step 1 applied to f_t∘h_t and f_0 gives f_t∘h_t = f_0, so V_t = V_0 and Y_t = Y_0. Possible routes for Step 2, any of which you may pursue:
 (a) log-rigidity of (closure(V_0), boundary): prove H^1(T_{closure V_0}(−log D)) = 0 (after a log resolution, if needed), using that the universal cover of V_0 is a totally geodesic, Kobayashi-hyperbolic, complete Teichmüller-type domain, or using the GL(2,R)/orbit-closure structure (Wright: V_0 is the projection of a rank-2 rel-0 orbit closure; Filip: algebraic; Eskin–Filip–Wright: defined over Q̄), or Calabi–Vesentini/Siu-type vanishing arguments; then (R2) and Kodaira–Spencer/Kuranishi give V_t ≅ V_0. Check whether the deformation of the log pair induced by (R1),(R2) is really a flat deformation to which Kuranishi theory applies.
 (b) circumvent base rigidity: construct holomorphic maps V_t → V_0 directly, e.g. via a holomorphic retraction of Teichmüller space onto the totally geodesic lift Ṽ_0 that is equivariant for the stabiliser of Ṽ_0 (Teichmüller discs are holomorphic retracts of Teichmüller space by Kobayashi-extremality arguments — check what is true for totally geodesic surfaces and for equivariance), composed with the lift of f_t; a degree-one proper holomorphic map between the smooth surfaces would be biholomorphic.
 (c) any other argument that the complex structure of V_t (or a covering family of curves in it) is determined by the topological data plus the boundary hypotheses (i),(ii).

## What is asked
A complete rigorous proof of the statement along these lines (or another), or a precise account of exactly which step fails and why, with the single missing lemma stated in full. A proof only for a sub-class of the V_0 (e.g. covering constructions, where V_0 is a finite cover of a rigid M_{0,5}-type log pair) does not settle the question but must be reported, clearly labelled, with its proof. Mark every unproved step.
