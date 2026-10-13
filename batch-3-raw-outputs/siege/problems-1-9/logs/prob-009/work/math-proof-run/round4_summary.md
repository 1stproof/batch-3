# Running summary after round 3 (written at round 4 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t. No proof and no counterexample in hand after three rounds (12 queries, all partial).

## Readings adopted by all workers (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t). This is part of what "holomorphic family" must mean (round2_q3); Remmert–Stein does not give it for free.
- (R2) Smooth triviality together with (i),(ii) is read as a stratified homeomorphism closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, carrying each boundary piece closure(V_0) ∩ Δ_G to closure(V_t) ∩ Δ_G (round2_q1, round3_q1 I2).

## Standing results
(Each is a theorem under the readings (R1)/(R2); none finishes the goal.)
- **S1 (entry 2; round1_q4, reproved round3_q3 Lemma 1).** t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}. Proof: closure(𝒱) ∩ (Δ_Γ × Δ) is analytic; π_i is constant on fibres and factor i never degenerates along closure(∂V_t), so (π_i × id) is proper on the relevant piece and Remmert gives the graph {(Y_t,t)} analytic, hence the graph of a holomorphic map. So the goal ⇔ Y locally constant near 0 ⇔ {Y_t} countable.
- **S2 (entry 3; round1_q1 Lemma 1).** The closure of ∂V_t = {Y_t} × C_t in deeper strata is {Y_t} × closure(C_t). So (ii) applied to Γ and strata in its closure holds tautologically and does not constrain Y_t. Hypothesis (ii) has content only at the deeper points {Y_t} × (closure(C_t) \ C_t), about incidences with OTHER boundary pieces.
- **S3 (entry 4; round1_q3, round3_q3 Obs. 4).** No local argument near ∂V_t can work: any holomorphic arc Y_t with germ y = Y_t + O(|s|) satisfies every local constraint of (i),(ii).
- **S4 (entries 8, 9; round2_q1 P1, round2_q3).** Under (R2), the following are independent of t: the monodromy ρ: π_1(V_t) → Mod/Sp, the local monodromies, and the weight filtrations. But these topological data, the monodromy around ∂V_t, and the self-intersection numbers of boundary curves are equally compatible with any arc Y_t.
- **S5 (entry 5; round1_q1, round3_q3 Lemma 3).** If every V_t is totally geodesic, the claim holds: there are countably many totally geodesic subvarieties (Wright + Eskin–Mirzakhani–Mohammadi, cited). Trivially, the claim also holds if V_0 admits no nontrivial family of this kind (rigidity).
- **S6 (new, entry 14; round3_q1 Lemma B, pinning lemma; rigorous given R2).** Suppose:
  - G' is a degeneration of Γ in which the vertex carrying Y stays intact;
  - P_t ∈ closure(∂V_t) ∩ Δ_{G'} is continuous in t;
  - E_t is a 1-dimensional boundary piece in Δ_G with Δ_{G'} ⊂ closure(Δ_G) and P_t ∈ closure(E_t) for all t;
  - closure(E_t) = closure(E_0) for all t.

  Then Y_t = Y_0. Proof: closure(E_0) ∩ Δ_{G'} is finite, P_t is continuous, and P_t's factor at the Y-vertex is Y_t. The incidence P_t ∈ closure(E_t) persists by (ii) whenever P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} lying in closure(E_0).
- **S7 (new, entry 15; round3_q4 Lemmas 1–2; Royden cited).** For all t, d_T ≤ k_{Ṽ_t} on the lifts, so ℓ_{Ṽ_t}(γ) ≥ ℓ_T(ρ(γ)). At t = 0, if every Teichmüller disc tangent to Ṽ_0 lies in Ṽ_0, then k_{Ṽ_0} = d_T. This is not on the current line: no reverse inequality is available.

## Conditional results (not standing)
- **round3_q1 Proposition A / conditional theorem.** Under three hypotheses the claim follows from S6:
  - (H1) existence of an incidence: a boundary piece E_0 of V_0 with a non-constant projection F_0 to a component containing the Y-subsurface, and an isolated point P_0 ∈ closure(∂V_0) ∩ closure(E_0);
  - (H2) F_0 is a Teichmüller curve whose maximal-Higgs rank-2 summand has multiplicity one;
  - (H3) Möller's characterization "maximal Higgs rank-2 sub-VHS ⇒ Teichmüller curve" holds in the needed form. The extra condition on zeros of the generating section, and whether it is preserved, are unchecked.

  Euler/Toledo numbers are topological (Milnor–Wood), so maximality persists. The worker could prove none of (H1)–(H3). (H1) is the central gap: no such E_0 is known to exist.
- **round3_q2.** The claim would follow if the pointwise "directional maximality" condition (M) of the Higgs field persisted to V_t: for every ω ∈ E_X \ 0, μ ↦ θ(μ)ω is an isomorphism T_X V → Ē_X. Condition (M) is open, not closed, and not numerical. Total geodesy of V_t from (M) is sketched only.
- **round3_q3 Lemma 2.** H^0(closure(V_0), N^log) = 0 ⇒ the family is constant (standard deformation theory; not checked at non-transverse points). Vanishing to first order in Y alone is not enough (t² issue).

## Partial / heuristic material
- At t = 0 (round1, round2_q3 P3; cited from memory): V_0 comes from a rank-2, rel-0, dimension-4 orbit closure. ∂V_0 has top-level Teichmüller-type pieces, with Y_0 at lower level (zero top-level differential). In covering constructions Y_0 is a Belyi curve.
- A rank-4 sub-local system W = E ⊕ Ē over V_0 (round2_q1 H2; not verified that it descends). Given multiplicity one, it persists as a sub-VHS over V_t (Deligne). Its limit along ∂V_t varies holomorphically, so on its own it does not pin Y_t.
- The global Arakelov equality for W over V_0 is very likely strict (round3_q2 (b): equality would give a symmetric-domain uniformisation, contradicting Antonakoudis, from memory). So entry 11 is set aside, not refuted.

## Dead ends
None of the routes below is REFUTED by a precise statement. Their "dead" parts are standing negative results S2–S4 and the strictly metric observation (round3_q4 (a)–(c)):
- (ii) along Γ and its degenerations: S2.
- Local plumbing: S3.
- Monodromy, intersection numbers, topological LMHS data: S4.

## Open gaps (routes set aside, not refuted)
- A. Missing lemma of entry 6 / the goal itself: what pins Y_t.
- B. Incidence route (entry 12; round3_q1): (H1)–(H3) open.
- C. Infinitesimal rigidity (entry 13; round3_q3): H^0(N^log) = 0 not attempted concretely.
- D. Arakelov/numerical (entry 11; round3_q2): set aside; the natural equality likely fails. Persistence of (M) is an alternative, open.
- E. Kobayashi metric (round3_q4): set aside; only a one-sided inequality.
- F. Hodge transport (entry 10; round2_q1): set aside; F_lim moves holomorphically.
- G. Deformability of V_0 at all (entry 7): if V_0 is rigid, the claim holds.
- H. Whether the claim is true as posed: several workers suspect the hypotheses are too weak. A counterexample needs a deformable totally geodesic surface, and none is known.

## The chain and the missing statement
**Chain.**
- (1) By entry 2 (S1), t ↦ Y_t is holomorphic.
- (2) The goal is therefore exactly the statement that this holomorphic map is constant.
- (3) The material does not reduce the goal any further. Every conditional reduction found so far needs either more than one further statement (round3_q1 needs (H1)–(H3)) or a statement strictly stronger than the goal (total geodesy of V_t, rigidity of V_0, H^0(N^log) = 0).
- So the missing statement is the goal, in the reduced form below. A proof of it is a complete proof, with nothing remaining except stating readings (R1), (R2).

**Missing statement (MS4, entry 17).** Let g ≥ 2. Let V_0 ⊂ M_g be a smooth 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric. Let 𝒱 ⊂ M_g × Δ be a complex submanifold with V_t = ψ(φ^{-1}(t)), satisfying hypotheses (i) and (ii) of the problem, and read as follows:
- (R1) closure(𝒱) ⊂ M̄_g × Δ is analytic with fibre closure(V_t) over t;
- (R2) there is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G.

Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product boundary stratum. Suppose that for every t the set ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1 and π_i(∂V_t) = {Y_t} for one fixed index i. Then the holomorphic map Δ → M_{g_i,n_i}, t ↦ Y_t, is constant.

**Why it should hold (sketch).**
- (a) Rigidity mechanism via Imayoshi–Shiga.
  - Suppose the abstract complex manifolds V_t are biholomorphic to V_0 through maps φ_t homotopic to the trivialization. Then f_0, f_t∘φ_t : V_0 → M_g are homotopic holomorphic maps.
  - By the Imayoshi–Shiga / Arakelov–Parshin rigidity theorem (homotopic non-constant holomorphic maps from a finite-type Riemann surface to M_g coincide), restricted to the curves of a covering family of curves in V_0, they coincide. Hence V_t = V_0 and Y_t = Y_0.
  - So the true crux is whether the log pair (closure(V_0), D_0) has no deformations, e.g. H^1(T(−log D)) = 0. This is plausible for covering constructions, which are finite covers of the rigid log pair M_{0,5}.
- (b) Incidence mechanism (S6 + round3_q1).
  - Pin Y_t through a deeper point of closure(∂V_t) that lies on another boundary curve E_t with a rigid (Teichmüller, maximal-Higgs) non-constant factor containing the Y-subsurface.
  - (ii) is what transports the incidence. Milnor–Wood topological invariance is what transports maximality.
- (c) Isotrivial-part heuristic. Arakelov–Parshin rigidity fails exactly for isotrivial factors, which is what Y_t is along ∂V_t. So the constancy of Y must come from the interior of V_t through the degeneration (the LMHS of H^1 along ∂V_t contains H^1(Y_t) in Gr^W_1). Any proof must couple the interior to the boundary.

**Tried so far** (earlier wordings: the goal itself and entry 6):
- round1_q1–q4: direct attempts and plumbing → reductions S1–S3, no mechanism.
- round2_q1: Hodge transport of W and LMHS → S4, missing lemma (M).
- round2_q2: rigidity / Arakelov / normal sheaf survey → conditional reductions.
- round2_q3: t = 0 structure and topology → S4 (monodromy and intersections blind).
- round2_q4: counterexample search → none; needs a deformable V_0.
- round3_q1: incidence + Milnor–Wood + Möller → S6 and the conditional theorem under (H1)–(H3).
- round3_q2: Arakelov-equality transport → natural equality likely strict; reduction to persistence of (M).
- round3_q3: infinitesimal rigidity H^0(N^log) = 0 → reduction only.
- round3_q4: Kobayashi metric → S7, one-sided inequality.

## Target for round 4
Progress test:
- Rounds 2 and 3 produced no proof of the missing statement or the goal, and no PROVED universal result that shortens the chain. S6 and S7 are general lemmas, but neither shortens the chain.
- **Main line stalled — no universal progress.**
- What differs from last round's sketch is a new mechanism: (a), base rigidity plus Imayoshi–Shiga rigidity of homotopic holomorphic maps. It replaces "make V_t totally geodesic" by "make the abstract complex structure of V_t constant". The missing statement itself is now posed explicitly as the reduced goal MS4 (first posing as a missing statement).

Wave (escalation rule), 9 attempt queries:
- q1–q3, q9: the closing task on MS4 (identical copies).
- q4: refute MS4 by explicit construction (first posing).
- q5: statement-only fresh first move. MS4 has in substance been attacked for three rounds.
- q6: mechanism (a), the Imayoshi–Shiga route. Prove the abstract (log) complex structure of V_t is constant, or circumvent the need for it.
- q7: continuation of round3_q1. Settle (H1)–(H3), with the partial result spliced in.
- q8: mechanism (c), Torelli at the boundary. Couple the interior VHS of V_t to the Gr^W_1 piece H^1(Y_t) of the LMHS along ∂V_t, with Deligne rigidity / the period map.
