# Running summary after round 1 (written at round 2 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed — for the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i),(ii), if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

## Round 1 (four exploratory attempts; none proved or refuted the claim)
All four answers (round1_q1..q4) are short partial results converging on the same picture.

### Established (modulo stated readings)
1. Holomorphy of t -> Y_t (round1_q2, round1_q3, round1_q4). Reading used: closure(𝒱) ⊂ M̄_g × Δ is analytic and its fibre over t is closure(V_t) (q4 makes this explicit as the natural meaning of (i)). Then 𝒲 = closure(𝒱) ∩ (Δ_Γ × Δ) is analytic, its image under π_i × id is the graph {(Y_t,t)} (analytic by Remmert's proper mapping theorem applied on compact closures, q4), and an analytic graph over the disc is the graph of a holomorphic map. So the claim ⇔ dY_t/dt ≡ 0 ⇔ Y_t lies in a countable set.
2. Deeper strata of Γ are useless (round1_q1, Lemma 1). ∂V_t = {Y_t} × C_t (C_t a curve in the other factors); its closure in deeper strata is {Y_t} × closure(C_t); factor i never degenerates along it; (ii) for the pair (Δ_Γ, Δ_G') holds tautologically whatever Y_t is.
3. ∂V_t is a boundary curve of the surface closure(V_t), not the limit of a boundary piece of another stratum (dimension reasons; round1_q2). So (ii) only constrains how finitely many deeper points {Y_t} × (closure(C_t) \ C_t) lie on closures of OTHER boundary curves of V_t.
4. Purely local arguments fail (round1_q3): near a generic point of ∂V_t, in coordinates (y on M_{g_i,n_i}, z other factors, plumbing s), any germ y = Y_t + O(σ) with Y_t any holomorphic arc satisfies all local constraints of (i),(ii).
5. Conditional (round1_q1): if every V_t were totally geodesic, the claim follows (orbit closures, hence totally geodesic subvarieties, are countable — EMM + Wright, cited from memory — so a continuous family of them is constant).

### Heuristics at t = 0 (not proved, cited from memory by workers)
- Wright: a 2-dim totally geodesic V_0 is the image of a GL(2,R)-orbit closure M of quadratic differentials of dimension 4, rank 2 (rel 0).
- Chen–Wright / Mirzakhani–Wright / multi-scale differentials (BCGGM): the boundary curve ∂V_0 corresponds to a rank-1 boundary orbit closure (Teichmüller curve) on top-level components; since Y_0 does not move, its limit differential is zero (Y_0 is at lower level); plausibly the lower-level piece is projectively 0-dimensional, so (Y_0, η) with its lower-level differential η is rigid/isolated, perhaps Y_0 defined over Q-bar. In covering-construction examples the constant factor is a Belyi-type cover of M_{0,3}.
- None of this transfers to t ≠ 0 since V_t carries no flat structure.

### Dead ends
- (ii) applied to Γ and its degenerations (item 2).
- Local plumbing analysis near ∂V_t (item 4).
- "Y_0 is special (Q-bar / isolated)" alone: says nothing about Y_t without a mechanism transporting the defining condition to V_t.

### Planner's own observations (unverified, for next queries)
- Topological transport: the smooth trivialization identifies V_t with V_0, so the monodromy representation π_1(V_t) -> Mod(S_g) (and the local system H^1 over V_t) is the same as over V_0. The rank-4 sub-local system W (from the rank-2 orbit closure: span of Re, Im of the 2-dim space of forms) persists topologically over every V_t; by Deligne semisimplicity it may be a sub-VHS over V_t. Its limiting mixed Hodge structure along ∂V_t could carry information about Y_t. Unexplored.
- Pencil example: in M̄_2 a divisor V_0 moves only in its linear system (Pic discrete); for level sets of a regular function the boundary stays put. Suggests counterexamples are hard; M_2 strata all have finite quotients, so excluded anyway.
- If totally geodesic surfaces are rigid as subvarieties (no nontrivial deformation V_t), the claim holds trivially; Teichmüller curves are rigid (Möller, via Arakelov equality / maximal Higgs), the analogous statement for surfaces is unknown to this run.

## Open gaps
A. (entry for missing lemma) Find a datum preserved for all t by smooth triviality + (i),(ii) (incidence of boundary pieces, monodromy, local systems/Hodge data) that pins Y_t to a discrete set.
B. Rigidity of V_0: does a 2-dim totally geodesic V_0 admit nontrivial holomorphic deformations V_t at all (with the boundary hypotheses)? A proof of rigidity proves the claim; a nontrivial deformation moving Y_t refutes it.
C. Is the claim actually true as posed? No counterexample known; no worker has constructed one.

## Next round target
Still exploratory but sharper: (1) Hodge/monodromy transport — sub-local system W persists over V_t; use limiting MHS at ∂V_t to pin Y_t (gap A); (2) global rigidity — show V_t = V_0, e.g. V_t inherits a structure forcing total geodesicity, then countability (gap B); (3) structure at t=0 plus a topological characterization of Y_0 (monodromy of the family over a neighbourhood of ∂V_0 / of other boundary curves through deeper points) that transfers (gap A); (4) counterexample search: a nontrivial deformation of a totally geodesic surface moving a constant factor while keeping (i),(ii), or proof none exists in known example classes (gap B/C).
