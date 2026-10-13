kind: attempt
Open question attempted: the run's missing statement MS4 (ledger entry 17), via the hardest step of the planner's sketch posed on its own: coupling the interior of V_t to the constant factor Y_t through the degeneration of the Hodge structure along ∂V_t (Torelli at the boundary).

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

## The step to settle
Along ∂V_t = {Y_t} × C_t, the limiting mixed Hodge structure (LMHS) of the weight-one VHS H^1 over V_t has Gr^W_1 ⊇ H^1(Y_t) (the normalized component carrying Y_t), a CONSTANT pure Hodge structure along ∂V_t; for g_i = 0 or for marked points the relevant information on Y_t sits in extension classes (positions of the nodes) of the LMHS. Arakelov–Parshin rigidity fails exactly for isotrivial pieces, which is what Y_t is along ∂V_t, so Y_t can only be pinned through the INTERIOR of V_t. Note also that at t = 0 the curve Y_0 sits at a "lower level" (the limits of the differentials of the orbit closure underlying V_0 vanish on Y_0), so the rank-4 tautological sub-VHS W over V_0 probably does not see Y_0 at all; the pinning, if any, must come from the complementary part of H^1 or from the global period map.
Claim to prove or refute: under the hypotheses of the statement, the Hodge structure H^1(Y_t) (together with the extension data recording the nodes on Y_t) obtained as a limit of the period map of V_t along ∂V_t is independent of t; by Torelli (and its version for the extension data) this gives Y_t = Y_0.
Possible tools: Deligne's semisimplicity and uniqueness of VHS on a given irreducible local system (note the base V_t changes complex structure — address this), the nilpotent/SL_2-orbit theorems (Schmid, Cattani–Kaplan–Schmid) for the asymptotics of the period map near ∂V_t, the theorem of the fixed part, Griffiths transversality and curvature (Higgs field) restrictions from total geodesy at t = 0 (along V_0, the Kodaira–Spencer map of the family over V_0 in the direction normal to ∂V_0 involves only quadratic differentials of a specific form), holomorphic dependence on t and the identity theorem (it suffices to show all t-derivatives of Y_t vanish at t = 0, so a first-order argument that applies at every t would be enough; an argument that works only at t = 0 is not, since Y_t = Y_0 + t²v cannot be excluded by first order at 0 alone).
If the claim is false as posed (the limit Hodge structure on H^1(Y_t) can move with t compatibly with all hypotheses), give the precise reason — that is a result — and say whether some other piece of the LMHS or of the period map pins Y_t.

## What is asked
A complete rigorous proof of the statement via this step (or another route you find), or a precise account of where it fails, with the single missing lemma stated in full. A proof only for a sub-class of the V_0 or of the families does not settle the question but must be reported, clearly labelled. Mark every unproved step.
