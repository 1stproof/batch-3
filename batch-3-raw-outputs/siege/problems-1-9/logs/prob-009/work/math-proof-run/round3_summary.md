# Running summary after round 2 (written at round 3 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

## Established (modulo the stated readings)
1. **t -> Y_t is holomorphic** (round1_q2, q3, q4; rechecked in round2_q2, q3). The reading used: closure(𝒱) in M̄_g×Δ is analytic, with fibre over t equal to closure(V_t). round2_q3 notes this is part of what "holomorphic family" must mean; Remmert–Stein does not give it in general. The argument then runs through Remmert's proper mapping theorem: an analytic graph over the disc is the graph of a holomorphic map. So the claim ⇔ dY/dt ≡ 0 ⇔ {Y_t} is countable. By the identity theorem it is enough to show this near t = 0.
2. **(ii) is tautological along Γ** (round1_q1). The closure of ∂V_t = {Y_t}×C_t in deeper strata is {Y_t}×closure(C_t), so factor i never degenerates along it.
3. **∂V_t is a boundary curve of closure(V_t)**, not a limit of a boundary piece of another stratum (round1_q2). So (ii) only says something at the deeper points {Y_t}×(closure(C_t)\C_t), and only about incidences with OTHER boundary pieces.
4. **No local argument works** (round1_q3; round2_q3 P2, round2_q4 §1). Near ∂V_t and near the deeper points, any holomorphic arc Y_t is compatible with every local constraint from (i) and (ii). Two further invariants are insensitive to moving Y_t (round2_q3): the monodromy around ∂V_t (Dehn twists acting trivially on the Y-subsurface) and the self-intersection numbers of boundary curves.
5. **Topological constancy** (round2_q1 P1). Read smooth triviality plus (i),(ii) as a stratified homeomorphism commuting with the maps to M̄_g up to homotopy. Then the monodromy ρ: π_1(V_t) → Sp(2g,Z), the local monodromies and the weight filtrations are all independent of t. Planner's addition (not yet checked by a worker): integer characteristic numbers that vary continuously are constant in t. Examples are Chern numbers of Deligne extensions of a sub-VHS that persists, log Chern numbers of (closure(V_t), boundary), and Euler/Toledo numbers.
6. **Conditional results** (round1_q1, round2_q2 B/C, round2_q4 §3). If every V_t is totally geodesic, the claim holds: there are countably many totally geodesic subvarieties (Wright + EMM, cited). If V_0 is rigid, the claim holds trivially. If Y_t ranges in a countable set (for example curves over Q̄), the claim holds.

## Partial / heuristic material
- At t = 0 (round1, round2_q3 P3; cited from memory): V_0 comes from a rank-2, rel-0, 4-dimensional orbit closure. ∂V_0 has a Teichmüller curve on top level. Y_0 sits at lower level with zero top-level differential. In covering constructions Y_0 is a Belyi cover, so it has no moduli; in those examples, deformations staying inside the covering locus keep Y fixed (planner check on the M_{0,6}/involution model).
- Hodge route (round2_q1). (H2) A rank-4 W = E⊕Ē over V_0, Hodge numbers (2,2); unverified that it descends to V_0. (P3) Given H2 and multiplicity one, W is a sub-VHS over every V_t (Deligne). The missing lemma (M) is that the LMHS of W along ∂V_t pins Y_t. The worker doubts this, since F_lim moves holomorphically.
- Rigidity route (round2_q2). No known Arakelov-type characterization of totally geodesic surfaces. The Higgs field gives T_V → Hom(E,Ē) with 2-dim image in a 3-dim symmetric part, so it is not "maximal" in the Shimura sense. The normal-sheaf cohomology has not been computed.
- Counterexample requirements (round2_q4 §2). A counterexample needs a non-rigid closure(V_0): a normal-sheaf section that integrates, keeps the stratification, and projects nontrivially to T_{Y_0}. round2_q4 gave a heuristic M_{0,6} model {c = λ_t a}, with no total geodesy checked. Nobody has a counterexample.

## New planner leads (round 3 targets, unverified)
- **Incidence + rigid non-constant boundary curves.** Other boundary curves E_t of closure(V_t) have non-constant projections, which at t = 0 are Teichmüller curves. A rank-2 sub-local system L with maximal Euler number (Milnor–Wood/Goldman) is topological. So maximal Higgs persists, and Möller's characterization might make π_j(E_t) Teichmüller, hence constant. If some E_t passes through a deeper point P_t = (Y_t, c_t) of closure(∂V_t) (an incidence preserved by (ii)) with the Y-subsurface inside a varying component, then P_t ∈ closure(E_0) ∩ Δ_{G'}, which is finite, so Y_t = Y_0. This is the first mechanism in which hypothesis (ii) does real work. Open: the exact form of Möller's criterion, whether a suitable E_t exists, and an induction to handle constant factors of E_t.
- **Arakelov-equality transport for surfaces.** Integer Chern numbers are constant in t. If total geodesy of a surface were characterized by an equality of Chern numbers, V_t would be totally geodesic, and context 6 finishes.
- **Infinitesimal rigidity.** H^0(closure(V_0), N^log) = 0 ⇒ the Douady/log-deformation germ is a fat point ⇒ the family is constant. Vanishing of the differential of Y alone is not enough (t² issue).
- **Kobayashi metric.** Royden: Teichmüller = Kobayashi. Kobayashi contraction plus fixed monodromy make V_t's length spectrum dominate V_0's; seek a Thurston-type or volume-extremality rigidity.

## Dead ends
- Using (ii) along Γ and its degenerations alone (item 2).
- Local plumbing near ∂V_t and near the deeper points (item 4).
- Monodromy around ∂V_t, and intersection numbers of boundary curves (round2_q3): blind to Y_t.
- "Y_0 is special (Belyi / Q̄ / isolated at lower level)" with no transport mechanism.
- Topological LMHS data (N, W(N), lattice) alone (round2_q1): the same for any arc Y_t.

## Open gaps
A. The missing lemma (entry 6): a datum preserved by the hypotheses that pins Y_t. Candidates are now the incidence + rigid-boundary-curve mechanism, and Hodge data.
B. Rigidity of V_0 (entry 7): infinitesimal (normal sheaf), numerical (Arakelov), or metric (Kobayashi).
C. Whether the claim is true as posed: four workers suspect the hypotheses are too weak; there is no counterexample.

## Next round target
Round 3: four attempt queries.
- q1: incidence + topological rigidity of the non-constant boundary curves (Milnor–Wood + Möller), with (ii) transporting incidences. This is the most promising, since it is the first route in which (ii) has content.
- q2: Arakelov-equality transport to make V_t totally geodesic.
- q3: infinitesimal rigidity H^0(N^log) = 0.
- q4: the Kobayashi-metric rigidity lens.

If q1 gives a precise conditional result (for example, the claim whenever a suitable incidence exists), round 4 should exploit it: prove the existence of the incidence at t = 0 from the multi-scale-differential structure, and handle the remaining configurations.
