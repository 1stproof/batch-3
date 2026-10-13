kind: attempt
Open question attempted: the run's missing statement MS4 (ledger entry 17) via the incidence route, continued from its partial result; specifically the open hypotheses (H1) (ledger entry 16), (H2), (H3) left by that partial result, and the induction needed when the pinning boundary curve has constant factors of its own.

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

## The partial result this query continues (spliced verbatim from the earlier answer)
## Step A: conditional rigidity of a non-constant factor
**Proposition A.** Let F_t := π_j(E_t) ⊂ M_{h,m} be a non-constant factor of E_t. Assume:
- (H2) F_0 is a Teichmüller curve, and its maximal-Higgs rank-2 summand L is a multiplicity-one isotypic component of the local system R^1 over F_0. More generally: L is the unique rank-2 sub-local system with its monodromy representation, up to isomorphism.
- (H3) Möller's characterization applies in M_{h,m}. From memory (Möller, "Variations of Hodge structures of a Teichmüller curve", JAMS 19 (2006)): a curve C -> M_g is a Teichmüller curve iff its VHS contains a rank-2 sub-VHS with maximal Higgs field. I am not certain whether the statement needs an extra condition, namely that the zeros of a generating section of L^{1,0} form sections, i.e. lie at marked points in the M_{h,m} setting.
  - If it does, that condition is NOT obviously preserved by the topological transport. This must be checked against the source.

Then F_t = F_0 for all t.

*Proof sketch.*
1. By (I2) the local system over F_t is the transport of the one over F_0, so it contains a sub-local system L_t with the same representation ρ_L.
2. By Deligne's semisimplicity theorem, the isotypic decomposition of a polarizable ℤ-VHS is a decomposition into sub-VHS. With multiplicity one this makes L_t a sub-VHS of weight 1, rank 2.
3. For a rank-2 weight-1 real VHS on a punctured curve, 2 deg L^{1,0} (Deligne extension) equals the Euler/Toledo number of ρ_L, up to sign. The Euler/Toledo number is a topological invariant of the representation.
4. At t = 0 it equals |χ(F_0)|; that is Arakelov equality, i.e. maximal Higgs field. Hence it equals |χ(F_t)| as well: the punctured curves F_t are homeomorphic by (I2). So L_t has maximal Higgs field.
5. By (H3), F_t is a Teichmüller curve.
6. Teichmüller curves are countable: each is the image of a closed SL(2,ℝ)-orbit, and there are only countably many by Eskin–Mirzakhani–Mohammadi (or already because Veech groups are finitely generated lattices defined over number fields).
7. The family t -> F_t is continuous, takes values in a countable set and is non-constant only if it jumps, so it is constant. ∎

If every factor of E_t is either constant or of this rigid type, Step A applies to each non-constant factor.
- Induction on the number of constant factors would still need each constant factor of E_t to be pinned by an incidence with yet another boundary piece. This is the same problem again, in a stratum of higher codimension.
- An induction on codimension terminates in the 0-dimensional strata of closure(V_t). These are finite and continuous in t, hence constant. But it only closes up if the incidence structure (H1) is available at every level.

## Conditional theorem
**Theorem (conditional).** Assume:
- **(H1)** There exist G', P_0 and E_0 as in Lemma B such that:
  - P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} lying in closure(E_0);
  - the vertex carrying Y in G' lies, in G, inside a component on which E_0 has a non-constant projection F_0;
  - and the needed P_t ∈ closure(E_t) follows from (ii).
- (H2) and (H3) hold for that F_0.
- Pinning works through that factor: the finitely many points of closure(F_0) at the relevant boundary stratum of M_{h,m} have their Y-component determined. This is true because the boundary point of closure(F_0) restricts to Y_t on the subsurface.

Then π_i(∂V_t) = {Y_0} for all t.

*Proof.*
1. By Proposition A, closure(F_t) = closure(F_0).
2. Project P_t to the component of G that contains Y. The projection is a point of closure(F_t) in a deeper boundary stratum, so it lies in a finite set and is continuous in t, hence constant.
3. Its factor at the vertex of Y is Y_t. Hence Y_t = Y_0.

Note that this only needs the single factor F_t to be constant, not all of E_t. ∎

## What fails or remains open
1. **(H1), the missing lemma.** I cannot prove that some boundary piece of V_0 has a varying component that degenerates to a curve containing Y_0 as a component.
   - In the multi-scale picture (heuristic 7), Y_0 is a lower-level component at ∂V_0. A boundary curve E_0 where Y's subsurface is top-level and varies would have to be found, e.g. at cusps of C_0 where the level structure rearranges. Its existence is not established.
   - Configurations where the mechanism fails: every boundary piece of V_0 whose closure contains a point with Y_0 as a component has a constant projection there, or an isolated-incidence point P_0 does not exist. In those cases Step B gives nothing.
2. **(H2), multiplicity.** For arithmetic (square-tiled) Teichmüller curves, L may occur with multiplicity greater than 1 in R^1. Then L_t need not be a sub-VHS; only the isotypic component is. Maximality of some rank-2 sub-VHS inside it can fail.
3. **(H3).** The exact form of Möller's characterization (extra condition on zeros; versions for marked points and for quadratic differentials) has to be checked against the source. Preservation of the extra condition under topological transport is open.
4. The whole argument uses the strong reading (I2) of "smoothly trivial" together with (i) and (ii).

**Status.**
- Proved: Lemma B (rigorous, given (I2)).
- Proved conditionally: Proposition A and the conditional Theorem, under (H1)–(H3), with (H3) cited from memory.
- Open: the claim as posed, specifically (H1).


## What is asked
Continue this route to a complete proof of the statement, or show precisely that it cannot work.
1. (H1) Prove, using the structure of totally geodesic surfaces at t = 0 (Wright's correspondence with rank-2 rel-0 orbit closures; Chen–Wright / Mirzakhani–Wright boundary; multi-scale differentials of Bainbridge–Chen–Gendron–Grushevsky–Möller; cylinder deformations), that a suitable boundary piece E_0 and isolated deeper point P_0 always exist — or, if not always, find a replacement pinning mechanism for the configurations where it fails (e.g. chains of incidences through several boundary pieces, ending at 0-dimensional boundary points of closure(V_t), which are finite and continuous in t hence constant; or incidences in which the Y-subsurface is part of a component varying along E_t only after an induction on constant factors).
2. (H2)/(H3) State Möller's characterization of Teichmüller curves exactly (with all hypotheses, including any condition on the zeros of the generating differential and versions with marked points / quadratic differentials), and decide whether maximal Higgs persistence along the topologically trivial family F_t really forces F_t to be a Teichmüller curve; if the extra condition is not topologically preserved, find another rigidity argument for the non-constant factor (e.g. Imayoshi–Shiga rigidity, or Arakelov equality alone forcing a Kobayashi-geodesic curve; McMullen/Möller rigidity of Kobayashi geodesic curves) and handle multiplicity >1.
A result covering only part of the configurations does not settle the question but must be reported, labelled, with proof. Mark every unproved step.
