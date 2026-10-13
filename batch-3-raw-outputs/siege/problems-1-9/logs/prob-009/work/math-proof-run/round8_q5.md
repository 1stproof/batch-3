kind: attempt
Open question attempted: the twin step of the run's missing statement MS8 (ledger entry 68), together with the open ledger claim that the "continuity principle" of round7_q1 (tracking the marked subsurface Σ_i along H-transported interior paths) can be made rigorous — i.e. that the boundary network produced by Proposition K cannot make a "twin jump" when t ↦ Y_t is non-constant.

## Task
Prove or refute the following claim (TW), which is the hardest single step of the planner's sketch for MS8 (the full MS8, its chain and the sketch are given below for context).

**Claim (TW).** Assume the setting and hypothesis (Rig) of MS8, and assume t ↦ Y_t is NOT constant. Let the Proposition K data at t = 0 be as in PR-H §3 / R7-2 §3.1: a chain of STAY pieces D^0 ⊂ ∂V_0, D^1, …, D^m with junction points J^k ∈ closure(D^{k−1}) ∩ closure(D^k), a terminal point Q_0 with a MERGE or MOV branch b, and the path-marked subsurface Σ_i, which along D^k is a constant vertex c_k (value ≅ Y_0; c_0 = i). For a constant vertex c of a piece D let φ_c(t) be its value on the transported piece D_t = H_t(D) (a holomorphic function of t; R7-3 Lemma 1). Then:
 (TW1) φ_{c_k} ≡ Y for every k (no twin jump at any junction J^k — in R7-3's notation, the case "σ x_m ≠ x_m" of Theorem B cannot be the only continuation);
 (TW2) at Q_t = H_t(Q_0), for t outside a countable set, the copy of Y_t carried by c_m (if Q_0 ∉ interior of b's piece) lies in the merged vertex (MERGE) or is the moving vertex at a puncture (MOV) of the transported branch b_t — i.e. the automorphism ambiguity at Q_0 (Aut(Q_0) moving the tracked copy) does not move it out.
(With (Rig), TW1+TW2 give the MS6 configuration at generic t, hence Y_t in a finite set, contradicting non-constancy; so TW proves MS8 except for interior-MOV endpoints, which another query treats.)

A proof of (TW) only under extra hypotheses ("no twins", (NT), (Lock), product strata only, a sub-class of V_0) does not answer the question (those cases are already known: R7-1, R7-2, R7-3); report such a result only as partial and say exactly what remains. A counterexample to (TW) must satisfy all hypotheses including (Rig), smoothness and total geodesy of V_0.

**Named approach (not yet tried; you may depart from it if you say why).** Twin jumps are invisible to chart-local analysis at the junction (R7-3 §5 model), but they are global: the marked path of Proposition K runs through the INTERIOR of V_0. Transport it by H to time t (R7-6, the "continuity principle"). R7-6's argument has a gap: the 2-parameter family (s,τ) ↦ H_{τt}(γ(s)) meets the orbifold locus of M_g at isolated points, whose local monodromy is an automorphism that may swap Σ_i with a twin (R7-2 §4.3), and its choice of ρ is not uniform near junctions. Repair it by analysing these orbifold points directly: near a junction J with σ ∈ Aut(J) exchanging twin copies x, σx, let 𝓛 ⊂ Def(J) × Δ be the preimage of closure(𝒱) — it is Aut(J)-invariant for every t. A twin jump at time t requires (s,τ)-squares to meet points of the fixed locus Fix(α) ∩ 𝓛 for elements α ∈ Aut(J) exchanging x and σx (curves near J with an automorphism close to α). Study the analytic set Fix(α) ∩ 𝓛 (its dimension, how it meets the boundary divisor {∏ s_e = 0} and the fibres over t): e.g. show that either it stays away from the region swept by the transported paths for small t (then R7-6's argument works near J), or its closure meets the boundary at points J′_τ near J_τ at which α exchanges two components both ≅ Y_τ (so the twins are "locked", the merged twin is a Y_τ-copy, and Lemma 1 of R7-1 plus (Rig) give the contradiction). Also handle Aut(Q_0) at the terminal point in the same way. Uniformity: you may change the choice of the Proposition K paths (they exist for every ρ > 0) or replace the marked path near a junction by a path inside a fixed chart Def(J).

Write any proof in full. Cite literature theorems by name with exact hypotheses. Begin with a plan/status line; end with proved / not proved / open.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G (including the open stratum M_g). Write H_t = H(·,t); one may assume H_0 = id. (This is our formalisation of "smoothly trivial" together with (i), (ii).)
- Notation: B_t := closure(V_t) \ V_t; a "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## The missing statement MS8, and how it is used

**Definitions used below.**
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w, for some stable graph G (any G, product type not required).
- ν: Ē → ∏M̄_w is the normalization of its closure. A *puncture* is a point p ∈ Ē with ν(p) ∉ ∏M_w. Put f_u = pr_u∘ν.
- M(E) := {u ∈ V(G) : f_u non-constant}. K(E) := the closure of the image of E in ∏_{u∈M(E)} M̄_u.

**Chain.**
1. Entry 19 (S1): t ↦ Y_t is holomorphic. So if Y_t lies in a finite set for t in a set accumulating in Δ, then Y ≡ Y_0. Equivalently, if Y is non-constant, Y_t avoids any prescribed countable set of values for all t outside a countable set Z ("generic t").
2. Entries 45 (Lemma PA) and 31 (Lemma T′, modulo (F2)): every piece at time 0 has a Teichmüller vertex in the orbifold sense (on the lift, for non-product G).
3. Entry 56 (L2 for product G, under (O_G)), the L2′ sketch (non-product G), and entry 54 (L1′): the maps (f_u^t ∘ A_t)_{u∈M(E)} lie in a t-independent finite set. Hence:
   - **(Rig)**: there is a finite set 𝒦 of triples (G, M, K), up to Aut(G), with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in its boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦.
   - This is ledger entry 69 (OPEN): it still needs (O_G) for every piece, (F2), and L2′.
   - Consequence of (Rig) used below: at a puncture p of E, some non-constant vertex hits the boundary (constant vertices take values in M_w), so pr_{M(E)}ν(p) ∈ K ∩ ∂(∏M̄_u), a finite set. Hence all puncture values of non-constant vertices lie in a finite set F, independent of t.
4. **MS8** (below; ledger entry 68): (Rig) ⇒ Y_t = Y_0 for all t.

Steps 1–4 give the goal from MS8 together with entry 69. MS8 is the strongest intermediate claim the main line needs next. It is the geometric core, containing the twin and crossing problems. After MS8, only entry 69 remains: the analytic input (O_G), (F2), and L2′.

MS8 is an implication quantified over all admissible V_0 and families. It is not a restriction to a sub-class. Its hypothesis (Rig) is exactly what step 3 supplies.

**Missing statement (MS8).**
- *Setting.* g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2), with H_0 = id.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type. ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - V_t is not assumed totally geodesic for t ≠ 0.
- *Hypothesis (Rig)*, as in chain step 3: there is a finite set 𝒦 of triples (G, M, K), M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that for every t ∈ Δ and every piece E at time t, (G, M(E), K(E)) ∈ 𝒦 up to the action of Aut(G).
- *Conclusion.* Y_t = Y_0 for all t ∈ Δ.

(Entered as OPEN entry 68, locator round8_plan. It replaces MS6, entry 52, which is retracted.)


Key to the ledger numbers cited in the chain above: entry 19 = holomorphy of t ↦ Y_t (PR-A below); entry 45 = Lemma PA (PR-H §1 below); entry 31 = Lemma T′ of an earlier file (positive area at a vertex at one point of a piece ⇒ that vertex is an orbifold-unramified Teichmüller curve; its limit fact (F2) is only sketched; not reproduced); entry 56 = L2 for product strata (rigidity: under an orbifold-transport hypothesis (O_G) the maps of the non-constant vertices of a transported piece, composed with biholomorphisms A_t: Ē_0 → Ē_t, lie in a t-independent finite set — proof via Lemma R*, Selberg, Bers embedding, Imayoshi–Shiga); entry 54 = L1′ (R7-5 below); entry 57 = the time-t criterion (R7-1 §1 below); entry 68 = MS8; entry 69 = the open input "(Rig) holds for every admissible family". You do NOT need to prove entry 69 or anything about (O_G): (Rig) is a hypothesis of MS8.

## Prior results (spliced verbatim from earlier answer files)
## Prior results (spliced verbatim from earlier answer files)
All assume readings (R1) and (R2) (stated above). Results marked as cited from memory are not verified; re-check anything you use. Labels inside them refer to each other as follows: PR-1 = holomorphy (PR-A); Lemma B′ of PR-3 = PR-B; Lemma C1/C2 of PR-3 = PR-C; PR-D = Lemma R/R0 (round5_q1); PR-E = Lemma R* (round5_q4); PR-F = Lemma G, T′, V (round5_q5); PR-G = an earlier file on the twin issue in cyclic covers (not reproduced; its point is that automorphisms of a boundary point can swap a merged copy of Y_0 with an unmerged twin). 'P-b Lemma 1' says the closure of ∂V_t = {Y_t} × C_t in deeper strata is {Y_t} × closure(C_t), so every point of closure(∂V_t) has a smooth component ≅ Y_t at vertex i. Earlier files call the old missing statement 'MS5' or '(T0)': it asked, at t = 0, for a point of closure(∂V_0) where EVERY copy of Y_0 in EVERY lift is merged into a Teichmüller vertex; it is now known to fail for a (singular) totally geodesic surface (PR-I) and is no longer the target.

Round-7 files below (R7-1 … R7-6) use these names: "PR-H" = Lemma PA / Proposition K file; "PR-I" = the quintic/Krull file; "PR-C" = Lemma C1/C2; "PR-A" = holomorphy; "PR-D Lemma R0" = the lifted family 𝓦 of a piece (closure in ∏M̄_w × Δ of the lift of H(E_0 × Δ); an irreducible 2-dimensional analytic set, proper over Δ); "PR-J germ argument" = limits of lifts along transported branches converge to the lift along the original branch; "L1", "L2", "MS6", "(O)" refer to the previous round's chain: MS6 was the statement "for t in a set accumulating in Δ some component ≅ Y_t lies in a puncture value f_u(p) of a vertex u non-constant on some piece at time t"; L1 = constancy of a vertex along a transported piece persists (proved for product strata, L1′ in R7-5 for all strata); L2 = rigidity of the maps of non-constant vertices (in the present task replaced by the hypothesis (Rig)). "(O)" is an orbifold-transport hypothesis that the present task does not need.

### PR-A. Holomorphy of Y_t (from round4_q3, verbatim)
## (A) Lemma 1 (holomorphy of Y_t), proved from (R1) and (R2)

**Lemma 1.** t -> Y_t is a holomorphic map Delta -> M_{g_i,n_i}.

*Proof.*
1. **Continuity.** Fix p in dV_0. By (R2), Phi(p,t) lies in dV_t for every t, so Y_t = pi_i(Phi(p,t)). This is continuous in t because Phi is continuous.
2. **The analytic set A.** Let A = closure(calV) cap (Delta_Gamma x Delta). By (R1), A is a closed analytic subset of the complex manifold Delta_Gamma x Delta. By (R2), A is homeomorphic to dV_0 x Delta. The set dV_0 is a 1-dimensional analytic set, so every nonempty open subset of A has real topological dimension 4. Hence A has pure complex dimension 2.
3. **The projection to Delta.** Each fibre A_t = dV_t has dimension 1. So no irreducible component of A lies in a fibre of phi : A -> Delta.
4. **The bad set.** Let B be the union of Sing(A) and the critical set of phi restricted to Reg(A). Then B is a closed analytic subset of dimension at most 1.
   - It is a proper subset in each component. Otherwise phi would be locally constant on an open subset of Reg(A), and that would force a component into a fibre.
   - The 1-dimensional irreducible components of B form a locally finite family. Those contained in fibres of phi lie over a discrete set D in Delta.
   - For t not in D, the fibre A_t (dimension 1) is not contained in B. Indeed, the intersection of A_t with B is a union of fibre-contained components of B, which do not occur over such t, and of finitely many points locally.
5. **Local sections.** For t_0 not in D, pick a in A_{t_0} \ B. Near a, A is a manifold and phi is a submersion. So there is a holomorphic local section s of phi with s(t_0) = a, and Y_t = pi_i(s(t)) is holomorphic near t_0.
6. **Conclusion.** Y is continuous on Delta and holomorphic on Delta \ D with D discrete. By the removable singularity theorem (in local coordinates of M_{g_i,n_i}, which is an orbifold, so work in a local manifold chart / finite cover near Y_{t_0}), Y is holomorphic on Delta. ∎

**Corollary.** MS4 is equivalent to "Y_t = Y_0 for all t in some neighbourhood of 0", by the identity theorem.

---



### PR-B. Incidence transport (from round4_q7, verbatim)
## B. Under (R2), incidences are transported automatically

**Lemma B′.** Let H : closure(V_0) × Δ → closure(𝒱) be the stratified homeomorphism of (R2). Let E_0 be a 1-dimensional piece of closure(V_0) ∩ Δ_{G''}, and let P_0 ∈ closure(E_0) ∩ closure(∂V_0) ∩ Δ_{G'}. Put E_t := H(E_0 × {t}) and P_t := H(P_0, t). Then:
- E_t ⊂ Δ_{G''};
- P_t ∈ closure(E_t) ∩ closure(∂V_t) ∩ Δ_{G'};
- t ↦ P_t is continuous.

*Proof.*
1. H is a homeomorphism over Δ that maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G.
2. A homeomorphism commutes with closures. Hence H(closure(E_0) × {t}) = closure(E_t), and H(closure(∂V_0) × {t}) = closure(∂V_t).
3. Continuity of P_t follows from continuity of H. ∎

So neither hypothesis (ii) nor the "isolated point" condition in (H1) is needed under (R2). Under a weaker reading one would fall back on (ii) as in P-d. By P-b, the component of P_t at the vertex i of G' is Y_t: the vertex i stays intact because π_i is constant along ∂V_t.

### PR-C. Local structure at a cusp; merge property (from round4_q7, verbatim)
## C. Local structure at a cusp of ∂V_t (partial (H1))

Fix t and a point P ∈ closure(∂V_t) \ ∂V_t. Then P lies in some Δ_{G'}, where G' degenerates Γ: it has edge set E(Γ) ∪ X with X ≠ ∅, and vertex i is intact. Let S be the germ of closure(V_t) at P. It is pure 2-dimensional, because V_t is dense in it.

**Lemma C1.** S has a 1-dimensional boundary branch b through P, other than the branches of closure(∂V_t), such that some edge e ∈ X is pinched along b.

*Proof.*
1. closure(∂V_t) \ ∂V_t is a proper analytic subset of a 1-dimensional analytic set, hence discrete.
2. So a branch β of closure(∂V_t) at P satisfies β \ {P} ⊂ Δ_Γ. Let X_S be an irreducible component of S containing β.
3. Take e ∈ X. On β \ {P} exactly the edges of Γ are pinched, so s_e ≠ 0 there. Hence s_e|_{X_S} is a non-unit that is not identically zero on the irreducible 2-dimensional germ X_S.
4. Its zero set is therefore of pure dimension 1 (Krull's principal ideal theorem / Weierstrass preparation; standard).
5. That zero set meets β only at P. So it contains a branch b ≠ β, and b lies in the boundary with s_e ≡ 0 on b. ∎

**Definition (merge property).** Let b be a boundary branch at P, and let G_b be the dual graph of a generic point of b. Equivalently, G_b is G' with the edges unpinched along b contracted. Let v be the vertex of G_b containing vertex i of G'. Say b has the *merge property* if v is strictly bigger than {i}, that is, some edge of G' incident to i is unpinched along b.

**Lemma C2 (merging forces variation).** Suppose b has the merge property. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing b. Then π_v(E) is not a point. Moreover, the limit Q of π_v along b at P is a boundary point of M̄_{h,m}, where M_{h,m} is the factor of vertex v. The dual graph of Q is the subgraph of G' contracted into v, and its component at vertex i is Y_t.

*Proof.*
1. As a point of b tends to P, the edges of G' inside v get pinched. So π_v tends to the stable curve Q described in the statement. Q lies in ∂M̄_{h,m}, because v contains at least one such edge.
2. Its component at vertex i is the component of P at vertex i, which is Y_t.
3. If π_v were constant on E, equal to some Z ∈ M_{h,m}, then its limit along b would be Z ∈ M_{h,m}, not a boundary point. Contradiction. ∎

**What C1 does not give.** C1 produces a branch b on which an extra edge e is pinched. It does not control the edges at vertex i. The merge property fails exactly when every edge of G' incident to i is pinched along b. Lemma C1 cannot exclude this. Example: in local coordinates (u,v) on a smooth germ, s_γ = uv and s_e = v, with β = {u=0} and b = {v=0} ⊂ Δ_{G'}. Nothing in (i), (ii), (R1) or (R2) rules out a surface whose boundary branches all look like this at every cusp of ∂V_0; compare Observation 4 of P-a. Define:

**(C-merge)** There is a cusp P_0 of ∂V_0 and a boundary branch b of closure(V_0) at P_0 with the merge property.

(C-merge) is the precise residue of (H1). It is not proved in general.



### PR-H. Lemma PA (positive area at generic boundary points), Lemma NH and Proposition K (the Y_0-network reaches a MERGE or MOV branch) (from round6_q9, verbatim, sections 1–3)
## 1. Gap (d): Lemma PA (proved, modulo cited standard facts)

### 1.1 Cited standard facts (from memory)
- **(Pl) Plumbing chart.** Near P ∈ Δ_Γ there is a holomorphic orbifold chart of M̄_g with coordinates (z, t) = (z, (t_e)_{e∈E(Γ)}), built as follows. z ranges over a neighbourhood of P in ∏_w T_w (or a Kuranishi chart of the product); the component Y_w(z) is obtained from the fixed Y_w = Y_w(0) by a quasiconformal deformation whose Beltrami differential is supported in a fixed compact set K_w ⊂ Y_w, disjoint from fixed coordinate discs {|z_e| < 1} around the punctures. The surface X(z,t) is obtained by plumbing z_e w_e = t_e in these discs. (Masur 1976; Bers; Wolpert. Cited from memory.) Consequently:
  - the tangent vector ∂/∂z_k at (z,t) is represented on X(z,t) by the transplanted Beltrami differential of the deformation of the components, supported in ι(K_w) and with sup norm bounded uniformly in t;
  - the vector ∂/∂t_e at (z,t) is represented by a Beltrami differential supported in the collar of e (computed in 1.2).
- **(Dual) Teichmüller norm.** For a tangent vector v at X represented by a Beltrami μ, ‖v‖_T = sup{Re ∫ μφ : φ ∈ Q(X), ‖φ‖_1 = 1}, where Q(X) is the space of integrable holomorphic quadratic differentials (at most simple poles at punctures). The supremum is attained at a unique φ = q_v (the norming differential), and the Teichmüller disc through X tangent to v is the disc generated by q_v. (Teichmüller, Hamilton–Krushkal, Royden; classical.)
- **(Bun) Quadratic differentials at a stable curve.** For the plumbing family, π_*(ω^{⊗2}) is a vector bundle of rank 3g−3 whose fibre at P is H^0(P, ω_P^{⊗2}): differentials on the components with at most double poles at the node branches, with equal leading (double-pole) coefficients a_e on the two branches of each node. The functionals a_e (leading coefficient in the plumbing coordinate z_e, i.e. a_e(φ) = (2πi)^{-1}∮_{|z_e|=r_0} z_e φ/dz_e) are holomorphic on the bundle and linearly independent at P; their common kernel at P is ⊕_w Q(Y_w). (Standard; dimension count Σ_w(3g_w−3+n_w) = 3g−3−|E(Γ)|.)

### 1.2 The collar Beltrami
In the collar of e at X(z,t_0), use the coordinate z = z_e on {|t_0| < |z| < 1} (with w_e = t_0/z). For t near t_0 define F_t(z) = z·exp(c·λ(z)), λ(z) = log|z| / log|t_0|, c = log(t/t_0), and F_t = id off the collar. Then F_t is the identity at |z| = 1, and in the w-coordinate it is w ↦ w (t/t_0)^{1−λ}, the identity at |w| = 1. So F_t: X(z,t_0) → X(z,t) is quasiconformal. Its Beltrami coefficient is
 μ_t = (z/z̄) · (c/(2 log|t_0|)) / (1 + c/(2 log|t_0|)).
Differentiating at t = t_0 (c ≈ δ := (t − t_0)/t_0): the vector δ·t_0 ∂/∂t_e is represented by the Beltrami (δ/(2 log|t_0|))·(z/z̄) on the collar, with sup norm |δ|/(2 log(1/|t_0|)). Hence

 **(C)** ‖b ∂/∂t_e‖_T ≤ |b| / (2 |t_e| log(1/|t_e|)).

### 1.3 The statement
**Lemma PA.** Let P be a generic point of ∂V_0 (outside a discrete subset of ∂V_0). There are X_n ∈ V_0, X_n → P, and generating pairs (X_n, q_n), ‖q_n‖_1 = 1, such that, after passing to a subsequence, the transplanted differentials ι_n^*q_n converge locally uniformly on each component Y_w of P to q_w ∈ Q(Y_w) with:
1. Σ_w ‖q_w‖_1 = 1 (no area is lost in the collars);
2. q_w ≠ 0 only for vertices w at which ∂V_0 moves (in a sense made precise below); in particular q_i = 0;
3. there is a vertex j ≠ i with q_j ≠ 0, i.e. j carries positive area in the sense of PR-F (F) with s_n = 1.
In particular hypothesis (PA) of PR-F holds, at every generic point of ∂V_0.

*Proof.*
**Step 1 (local model).** Let ν: N → closure(V_0) be the normalization of a local irreducible component (branch) of the germ of closure(V_0) along ∂V_0 near P, lifted to the manifold chart of (Pl). Normal surfaces have isolated singular points, and the preimage of ∂V_0 is a curve; so for generic P, N is smooth at the point over P, with coordinates (s, τ) in which the preimage of ∂V_0 is {τ = 0}. The plumbing coordinates pull back to holomorphic functions t_e(s,τ) vanishing on {τ = 0}; write t_e = u_e(s,τ) τ^{m_e} with m_e ≥ 1 and u_e not divisible by τ. The zero set of u_e meets {τ = 0} in a discrete set, which we avoid (genericity). Also z(s,0) parametrizes ∂V_0, and for generic P, a := ∂_s z(s_0,0) ≠ 0 (the parametrization of the curve ∂V_0 is an immersion off a discrete set). Since π_i is constant on ∂V_0, the i-component of a is 0: a = (a_w)_w with a_i = 0.

**Step 2 (the vectors v_n).** Take τ_n → 0 and X_n := ν(s_0, τ_n) ∈ V_0 (points with τ ≠ 0 are in V_0 since t_e ≠ 0 there). Let v_n := dν(∂_s) at (s_0,τ_n), a tangent vector to V_0. In plumbing coordinates v_n = (∂_s z(s_0,τ_n), (∂_s t_e(s_0,τ_n))_e), with ∂_s z(s_0,τ_n) → a and ∂_s t_e = (∂_s u_e) τ^{m_e}, so |∂_s t_e| ≤ C|t_e| because u_e is a unit near (s_0,0). By (Pl) and (C), v_n is represented by a Beltrami differential μ_n = Σ_w ι_n^* μ_w^{(n)} + ν_n, where μ_w^{(n)} is supported in K_w, depends continuously on the vector and converges to a Beltrami μ_w on Y_w representing a_w (take μ_i^{(n)} → 0, since a_i = 0), and ‖ν_n‖_∞ ≤ C' / log(1/max_e|t_e(X_n)|) → 0.

**Step 3 (upper bound).** Put A := max_w ‖a_w‖_{T(Y_w)} > 0 (a ≠ 0). Let φ_n ∈ Q(X_n), ‖φ_n‖_1 = 1. By normal families (an L^1-bounded family of holomorphic quadratic differentials is locally uniformly bounded), after a subsequence ι_n^*φ_n → φ_w locally uniformly on each Y_w. By Fatou on the disjoint images ι_n(K) of exhausting compacts, Σ_w ‖φ_w‖_{L^1(Y_w)} ≤ 1; in particular φ_w is integrable, hence φ_w ∈ Q(Y_w). Then
 Re ∫ μ_n φ_n → Σ_w Re ∫_{Y_w} μ_w φ_w ≤ Σ_w ‖a_w‖ ‖φ_w‖ ≤ A Σ_w ‖φ_w‖ ≤ A,
using |∫ ν_nφ_n| ≤ ‖ν_n‖_∞ → 0 and (Dual) on Y_w. Hence limsup ‖v_n‖_T ≤ A.

**Step 4 (lower bound).** Let j attain the maximum, and φ ∈ Q(Y_j) with ‖φ‖ = 1 and Re ∫ μ_j φ = A. The element φ ⊕ 0 lies in the fibre at P of the subbundle ker(a_e : e ∈ E(Γ)) of (Bun); extend it to a holomorphic section of that subbundle and let φ_n be its value at X_n. Then ι_n^*φ_n → φ on Y_j and → 0 on the other components, locally uniformly. **Collar mass.** In the collar {|t|/r_0 < |z| < r_0} of an edge e write φ_n = Σ_k c_k z^k dz². By construction c_{−2} = a_e(φ_n) = 0. The coefficients c_k, k ≥ −1, are bounded by C r_0^{−k} (Cauchy estimates on |z| = r_0, where φ_n is uniformly bounded). The terms with k ≤ −3 are, in the coordinate w = t/z, the terms c_k t^{k+2} w^{−k−4} dw² with −k−4 ≥ −1, bounded likewise by Cauchy on |w| = r_0. Since ∫_{|z|<ρ}|z|^k dA ≤ 2πρ^{k+2}/(k+2) ≤ 2πρ for k ≥ −1, ρ ≤ 1, the mass of φ_n in {|t|/ρ < |z| < ρ} is ≤ Cρ for ρ ≤ r_0/2, uniformly in n. With convergence on the thick parts this gives ‖φ_n‖_1 → ‖φ‖ = 1. Then Re ∫ μ_n φ_n → Re ∫ μ_j φ = A. So liminf ‖v_n‖_T ≥ A, and ‖v_n‖_T → A.

**Step 5 (the norming differentials).** Let q_n be the norming differential of v_n (‖q_n‖ = 1). By (Dual) the Teichmüller disc tangent to v_n is generated by q_n; since v_n is tangent to V_0 and V_0 is totally geodesic, (X_n,q_n) is a generating pair. Pass to a subsequence with ι_n^*q_n → q_w on each Y_w. As in Step 3,
 A = lim Re ∫ μ_n q_n = Σ_w Re ∫ μ_w q_w ≤ Σ_w ‖a_w‖‖q_w‖ ≤ A Σ_w ‖q_w‖ ≤ A.
All inequalities are equalities. Hence Σ_w ‖q_w‖ = 1 (item 1); q_w = 0 unless ‖a_w‖ = A (item 2; in particular q_i = 0 since a_i = 0 and A > 0); and some q_j ≠ 0, j ≠ i (item 3); moreover q_w norms a_w whenever q_w ≠ 0. ∎

**Remarks.**
- This closes gap (d) of PR-F §6 completely, at every generic point of ∂V_0, with positive area located at a vertex j where the tangent vector of ∂V_0 has maximal Teichmüller norm.
- By Proposition C of PR-F, π_j(E) is then a Teichmüller curve (E the component of ∂V_0 through P), π_j|_E is orbifold-unramified onto it, and closure(∂V_0) ≠ ∂V_0 has cusps. (PR-F's Lemma T' depends on (F2), which PR-F only sketched; I have not re-proved (F2).)
- Corollary (full area): the area of the limit sits entirely on the moving vertices at maximal speed; in particular for the generic P the limit differential (q_w)_w on P is a genuine area-1 integrable differential on the stable curve P, with q_i = 0.
- The same proof applies verbatim to **any** 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, for any product-type stratum Δ_G and any generic point of E (only the local model of Step 1 was used, plus a ≠ 0). Used in §4.

## 2. Gap (c), first half: choice of direction (proved)

Setting: P, (X_n,q_n), (q_w)_w and j as in Lemma PA. For e ∈ Γ_i (edges at i) let γ_e be the core curve of the e-collar of X_n. Transport curves along Teichmüller maps X_n → g_s X_n, where g_s = diag(e^{-s}, e^{s}) contracts horizontal and expands vertical q-lengths ("path marking").

**Lemma NH.** After passing to a subsequence and replacing q_n by e^{-2iθ_n} q_n with θ_n → 0 (which keeps all conclusions of Lemma PA, the rotation being absorbed in the limit), we may assume:
1. there is an essential, non-peripheral curve c of Y_j (hence of S_g, not homotopic to any Γ-curve) and m > 0 such that each q_n has a horizontal cylinder in the class c_n of c of modulus ≥ m; hence Ext_{g_sX_n}(c_n) ≤ e^{-2s}/m for all s ≥ 0;
2. there is e_0 ∈ Γ_i such that the q_n-geodesic representative of γ_{e_0} is not horizontal; hence Ext_{g_sX_n}(γ_{e_0}) → ∞ as s → ∞, for each n.

*Proof.*
- (Cited from memory: Masur.) Cylinder directions of a finite-area quadratic differential are dense in RP^1. A cylinder core of (Y_j,q_j) is non-peripheral: a flat cylinder boundary bounding a disc with at most one simple pole contradicts Gauss–Bonnet (PR-F, Step 5 of Lemma T').
- For each e ∈ Γ_i, the q_n-geodesic representative of γ_e is a chain of saddle connections or a cylinder core. If all its segments are parallel, call their direction θ_n(e) ∈ RP^1; otherwise θ_n(e) is undefined. Pass to a subsequence along which, for e = e_0 fixed, either θ_n(e_0) is always undefined or θ_n(e_0) → θ_∞(e_0).
- Choose a cylinder direction of q_j different from θ_∞(e_0) and rotate so that it is horizontal. Let A be the open horizontal cylinder, A' ⋐ A a compact sub-annulus of modulus m' > 0. On ι_n(A') the differentials q_n converge to q_j in C^1; √q_n is defined on ι_n(A') for large n (the sign holonomy is discrete), so the developing map of ι_n(A') is equivariant under a translation v_n → v ∈ R \ {0}. Its image contains a straight strip in direction v_n of width close to that of A', so q_n has a cylinder in the class of c of modulus ≥ m := m'/2, in direction arg v_n → 0. Put θ_n := arg v_n and rotate. Then this cylinder is exactly horizontal. Under g_s its modulus is multiplied by e^{2s}, giving item 1.
- Since arg v_n → 0 ≠ θ_∞(e_0), for large n γ_{e_0} is not horizontal for the rotated q_n. So some saddle connection of its geodesic has nonzero vertical component, and its vertical measure v := i(γ_{e_0}, F_hor(q_n)) is > 0. (The q-geodesic realizes the intersection numbers with both measured foliations; standard, cited.) Then ℓ_{g_sq_n}(γ_{e_0}) ≥ e^{s}v, and Ext ≥ ℓ²/Area = ℓ² ≥ e^{2s}v² → ∞. ∎

**Remark.** This bypasses gaps (a) and (b) of PR-F §6. Item 1 needs only one exactly horizontal cylinder, obtained by a rotation tending to 0, and not a Jenkins–Strebel q_n. No interchange of the limits is needed below, because I work with connected limit sets instead of the Jenkins–Strebel limits Z_n.

## 3. Proposition K: Y_0 merges or moves somewhere on its own boundary network (proved, modulo routine marking details)

Notation:
- B := closure(V_0) \ V_0. This is a compact 1-dimensional analytic set; work on a level cover if needed.
- Σ_i ⊂ S_g is the subsurface of vertex i, and ∂Σ_i = {γ_e : e ∈ Γ_i}. Both are path-marked.
- ψ(X) ∈ M̄_{g_i,n_i} is the "Σ_i-part" of X. Fix a pants decomposition of Σ_i. ψ(X) is the surface with the Fenchel–Nielsen coordinates of X inside Σ_i and boundary lengths set to 0. It is continuous on augmented Teichmüller space near points where ∂Σ_i is pinched, and there it equals the stable curve on the Σ_i-side.
- d is a metric on M̄_{g_i,n_i}.

**Cited facts (from memory).**
- Kerckhoff: Ext_Y(γ) ≤ e^{2 d_T(X,Y)} Ext_X(γ).
- Maskit's comparison (Ext) of PR-F.
- Lemma G / G′ of PR-F: limits of g_{s_n}X_n with s_n → s* < ∞ lie in ∂V_0. Each such limit equals φ(g_{s*}), up to a subsequence of the φ's.

For δ, η > 0 let T_n = T_n(δ,η) be the first s ≥ 0 at which max_{e∈Γ_i} Ext_{g_sX_n}(γ_e) = δ or d(ψ(g_sX_n), Y_0) = η.

**Step 1 (T_n is finite and tends to ∞).** By Lemma NH(2), Ext(γ_{e_0}) → ∞ along the ray, so T_n < ∞. For s in a compact set, g_sX_n converges to points of ∂V_0, uniformly in s (Lemma G′). At those points ∂Σ_i is pinched and ψ = Y_0, because vertex i of every point of ∂V_0 is Y_0. Hence T_n → ∞.

**Step 2 (the continuum).** Let K = K(δ,η) be a Hausdorff limit (subsequence) of the compact connected sets {g_sX_n : 0 ≤ s ≤ T_n}. Then K is compact and connected, and it contains P. Every point of K is a limit of g_{s_n}X_n with s_n ≤ T_n:
- if s_n stays bounded, the limit lies in ∂V_0 ⊂ B;
- if s_n → ∞, the curve c is pinched by Lemma NH(1), so the limit lies in B.

So K ⊂ B. On K, every ∂Σ_i curve has Ext ≤ δ (in the limit sense along the approximating sequences) and d(ψ, Y_0) ≤ η. Let Q = Q(δ,η) ∈ K be a limit of the endpoints g_{T_n}X_n. Then Q ∈ B, and either
- (a) some γ_e, e ∈ Γ_i, has Ext = δ > 0 at Q, so it is unpinched at Q; or
- (b) d(ψ(Q), Y_0) = η.

**Step 3 (δ_k, η_k → 0).** Pass to a subsequence with K(δ_k,η_k) → K_0 and Q_k := Q(δ_k,η_k) → Q_0. Then K_0 ⊂ B is compact and connected, and contains P and Q_0. At every point of K_0 the curves ∂Σ_i are pinched (Ext ≤ δ_k → 0 along approximating sequences) and the Σ_i-side is the single smooth component Y_0. So vertex "i" is intact, ≅ Y_0, at every point of K_0, consistently with the path marking.

**Proposition K.** There are a compact connected set K_0 ⊂ B containing ∂V_0's point P, along which the Σ_i-component is intact and equal to Y_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B at Q_0 such that one of the following holds:
- **(MERGE)** along b \ {Q_0} some curve of ∂Σ_i is unpinched, i.e. the Y_0-component of Q_0 is merged with other components along b (the merge property of PR-C, at Q_0);
- **(MOV)** along b all of ∂Σ_i stays pinched, but the Σ_i-component is non-constant along b, with limit Y_0 at Q_0.

*Proof.*
- In case (a) for infinitely many k, Q_k ≠ Q_0, because γ_e is pinched at Q_0 and unpinched at Q_k. Put Q̃_k → Q̃_0 in augmented Teichmüller space by choosing lifts and applying mapping classes, so that the path markings converge; this is possible since M̄_g is the quotient of augmented Teichmüller space.
- Near Q_0, B is a finite union of branches, each of which minus Q_0 lies in one stratum. Infinitely many Q_k lie on one branch b, and γ_e is unpinched on b \ {Q_0}: (MERGE).
- In case (b) for infinitely many k: if some ∂Σ_i curve is unpinched at infinitely many Q_k, argue as before to get (MERGE).
- Otherwise ∂Σ_i is pinched at the Q_k, so the Σ_i-side of Q_k is a union of components with ψ(Q_k) at distance η_k > 0 from Y_0 = ψ(Q_0). Again Q_k ≠ Q_0, and the Q_k lie on one branch b, along which ψ is non-constant: (MOV). ∎

**What Proposition K does not give.**
- Q_0 need not lie in closure(∂V_0). K_0 can leave closure(∂V_0) through "STAY" branches: branches of B at points of closure(∂V_0) along which the Y_0-vertex stays intact and constant, but which are not contained in closure(∂V_0).
- The ρ-variant settles nothing. Add the stopping condition "g_sX_n leaves the ρ-neighbourhood of closure(∂V_0)", with η ≪ ρ. That variant shows: **at some point Q ∈ closure(∂V_0) there is a branch of B, not contained in closure(∂V_0), of type MERGE, MOV or STAY.** This is only Lemma C1 of PR-C with the extra edge located; it does not exclude STAY.
- Heuristic for why STAY should really occur, from the multi-scale picture, not proved. Suppose the zero-area part of the limit at P has two levels below the top: a vertex w at level −1 and the vertex i at level −2, attached below w. Along the ray, lower levels are "released" (become commensurate with the contracted top-level skeleton) top-down. w merges with the top-level skeleton first, along a branch b_w at the cusp Q of ∂V_0, and the Y_0-vertex is still intact and constant along b_w. The merge of Y_0 then happens at a cusp of b_w, which is in general not in closure(∂V_0).



### PR-I. The quintic-cover example, the Krull/twin mechanism, Lemma D (merge or twin), the Pinning Lemma and Theorem 4 (from round6_q6, verbatim, sections 2–4). The example surface is NOT smooth (it has a coarse A_1 point at y^5 = x^5 − x and two fixed-locus sheets crossing at the Fermat quintic; proved in round6_q3), so it is a test case, not an admissible V_0.
## 2. Example: the surface of cyclic quintic covers in M_6 (MS5 fails; V_0 is not smooth)

### 2.1 Construction
- For distinct a = (a_1, …, a_5) on P^1, let X_a be the smooth projective model of y^5 = ∏_{j=1}^5 (x − a_j), with the obvious change if some a_j = ∞.
- X_a → P^1 is a Z/5-cover, totally ramified over a_1, …, a_5 with local monodromy 1 ∈ Z/5 at each, and unbranched elsewhere. The degree of the polynomial is 5 ≡ 0 mod 5, so ∞ is unbranched.
- Riemann–Hurwitz gives 2g − 2 = 5·(−2) + 5·4 = 10, so g = 6.
- This defines Φ : M_{0,5} → M_6, invariant under S_5 because all five monodromies are equal. Put V_0 := Φ(M_{0,5}).

### 2.2 V_0 is totally geodesic and 2-dimensional (standard; cited from memory)
- Let q be an integrable quadratic differential on (P^1; a_1, …, a_5), so it has at most simple poles at the a_j. Its pullback f^*q has order e(−1 + 2) − 2 = 3 ≥ 0 at each ramification point (e = 5). So f^*q is a holomorphic quadratic differential on X_a.
- The Teichmüller map of the base with initial differential q lifts to an affine map for f^*q, which is a Teichmüller map upstairs. Hence the lifting map T_{0,5} → T_6 is a holomorphic isometric embedding (classical).
- Every tangent direction of T_{0,5} at a point is the Teichmüller direction of a unique (up to positive scaling) q. The Teichmüller disc of T_6 in the image direction is the disc of f^*q, which is the image of the disc of q. So every Teichmüller disc tangent to V_0 lies in V_0.
- Φ is finite-to-one: X_a has finitely many automorphism subgroups, and the quotient by one of them recovers the unordered branch set. So dim V_0 = 2.

### 2.3 Boundary (admissible covers; Harris–Mumford, cited from memory)
- An abelian cover has a unique admissible cover over each stable 5-pointed tree. This gives a continuous extension Φ̄ : M̄_{0,5} → M̄_6, sending a stable tree to the stabilized admissible cover.
- Then closure(V_0) = Φ̄(M̄_{0,5}), since the image is compact and contains V_0 as a dense subset.
- Boundary points go to nodal curves (computed below), so Φ̄^{-1}(M_6) = M_{0,5}. Hence V_0 is closed in M_6.
- **Local monodromies.** On every component of an admissible cover, the local monodromies at the special points sum to 0 in Z/5. Here every local monodromy is nonzero, hence a generator. So each component cover is connected and totally ramified over every special point.

**Over D_{ab}° (base A ∪ B, with A ∋ a_a, a_b and B ∋ the other three points):**
- Over A the monodromies are (1, 1, 3). Riemann–Hurwitz gives 2g − 2 = −10 + 12, so g = 2, with one point over the node.
- Over B they are (1, 1, 1, 2), so 2g − 2 = −10 + 16 and g = 4, again with one point over the node.
- The stable curve is a genus-2 curve and a genus-4 curve glued at one point. Its dual graph Γ has vertices of genus 2 and 4 joined by one edge, and Δ_Γ = M_{2,1} × M_{4,1}. This is of product type: the gluing map is bijective onto Δ_Γ because the two vertices have different genera.
- The genus-2 component is the Z/5-cover of a 3-pointed sphere with monodromy (1, 1, 3), marked at the point over the third point. It is the same pointed curve Y_0 ∈ M_{2,1} for every (a, b) and every point of D_{ab}°, namely y^5 = x(x − 1) marked over x = ∞. So π_1 ≡ Y_0.
- The genus-4 component is the covering construction with data (1, 1, 1, 2) over the 4-pointed sphere B, marked over the node. Let C ⊂ M_{4,1} be its image as B runs over M_{0,4}. The map M_{0,4} → C is finite-to-one by the argument of 2.2, so dim C = 1.
- Hence Φ̄(D_{ab}°) = {Y_0} × C for all ten pairs (a, b).

**Over the 15 points D_{ab} ∩ D_{cd} (base chain A(a_a, a_b) — B(a_m) — C(a_c, a_d)):**
- The monodromies are (1, 1, 3) on A, (2, 1, 2) on B and (3, 1, 1) on C.
- The covers over A and C are both Y_0. The cover over B has genus 2 (2g − 2 = −10 + 12) and two points over the nodes; call this 2-pointed curve B_0.
- So all 15 points map to one stable curve P_0 = Y_0 — B_0 — Y_0, a chain of three genus-2 curves. Its dual graph is G' (path with 3 vertices).

**Conclusion.**
- closure(V_0) \ V_0 = ({Y_0} × C) ⊔ {P_0}.
- ∂V_0 = closure(V_0) ∩ Δ_Γ = {Y_0} × C is irreducible, because it is the image of the irreducible D_{12}°. It has dimension 1, and π_1(∂V_0) = {Y_0} with dim M_{2,1} = 4 > 0.
- closure(∂V_0) = ∂V_0 ⊔ {P_0}.

### 2.4 MS5 fails for this V_0
- The strata meeting closure(V_0) are M_6, Δ_Γ and Δ_{G'}.
  - closure(V_0) ∩ M_6 = V_0 is irreducible of dimension 2, so it has no 1-dimensional components.
  - closure(V_0) ∩ Δ_{G'} = {P_0}.
  - Hence the only 1-dimensional piece in any stratum is E = ∂V_0 ⊂ Δ_Γ.
- So the only candidate in MS5 is G = Γ, E = ∂V_0, P_0 the point above. Lemma 1 (u = genus-2 vertex) shows that clause (a) fails there. Concretely, the lift R = (Y_0, B_0 ∪ Y_0) ∈ {Y_0} × closure(C) has R_1 = Y_0 smooth.
- **All hypotheses of MS5 hold except smoothness:** g = 6 ≥ 2; V_0 is closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; dim ∂V_0 = 1; π_1(∂V_0) = {Y_0} with dim M_{2,1} > 0.

### 2.5 Caveat: this V_0 is not smooth (sketch)
- **Fermat point, orbifold sense.** The Fermat quintic F : x^5 + y^5 + z^5 = 0 has genus 6 and lies in V_0 in three ways. The quotients by z ↦ ζz, by y ↦ ζy and by x ↦ ζx are each P^1, totally branched over 5 points.
  - In a Teichmüller chart at a lift of F, the preimage of V_0 therefore contains the three fixed loci Fix(H_x), Fix(H_y), Fix(H_z) of these order-5 subgroups. Each is a smooth 2-dimensional germ.
  - They are distinct germs. If two coincided, the generic X_a would carry a second Z/5 acting nontrivially on X_a/H ≅ P^1 and preserving the branch set, and a generic 5-point configuration has no nontrivial symmetry.
  - So V_0 is not a smooth sub-orbifold at F.
- **The point c_4 = {0, ±1, ±i}, coarse sense.** Its stabilizer in PGL_2 is Z/4, generated by z ↦ iz. (0 is the only point lying on no harmonic 4-subset, so it is fixed. The symmetries of the square fixing 0 are the rotations.)
  - The induced action on T_{c_4} M_{0,5} has eigenvalues (i, −1). Compute T = (⊕_j T_{p_j} P^1)/sl_2 with characters {i, 1, i, −1, −i} − {i, 1, −i}.
  - So the coarse germ of M_{0,5}/S_5 there is C^2/(Z/4) with weights (1, 2). This is an A_1 singularity, since the group is not generated by reflections.
  - I expect the coarse germ of V_0 at Φ(c_4) to be this quotient. This needs the generic automorphism group of X_a to be exactly Z/5, which I have not checked.

So the example is a counterexample to **MS5 with the smoothness hypothesis removed**, not to MS5 as stated. Smoothness of V_0 is an interior condition, while everything in MS5 concerns the boundary. I see no way smoothness could create the missing boundary curves of Corollary 1. But I have not found a smooth example in which they are missing.

## 3. In the example the problem's conclusion still holds: the twin mechanism

**Proposition 3.** Let V_0 be the surface of Section 2. Let V_t be a family as in the problem, with readings (R1), (R2), and with ∂V_t := closure(V_t) ∩ Δ_Γ 1-dimensional and π_1(∂V_t) = {Y_t}. Assume condition (O) of PR-E for the piece E_0 = ∂V_0 and the genus-4 vertex. Then Y_t = Y_0 for all t ∈ Δ.

(Smoothness of V_0 plays no role in the argument.)

*Proof.*

**Step 0 (rigid factor).**
- π_2 : ∂V_0 = {Y_0} × C → C is a bijection, and C is the covering-construction curve from M_{0,4}.
- The lift T_{0,4} → T_{4,1} is a holomorphic isometric embedding. It is equivariant for the subgroup of Mod_{0,4} that preserves the monodromy data. So hypothesis (H_0) of PR-E holds: π_2(∂V_0) is a Teichmüller curve in the orbifold sense. Its normalization is the quotient of the disc by the stabilizer of the Teichmüller disc (standard).
- By Lemma R\* (PR-E, under (O)), K := closure(π_2(∂V_t)) = closure(C) ⊂ M̄_{4,1} for every t.
- K is an irreducible compact curve meeting M_{4,1}, so K_∂ := K ∩ ∂M̄_{4,1} is finite.
- Let F ⊂ M_{2,1} be the finite set of 1-pointed curves that occur as a smooth component of a point of K_∂, marked at one of its special points.

**Step 1 (the transported cusp).**
- Put P_t := H_t(P_0). Since H_t preserves strata, closure(V_t) ∩ Δ_{G'} = {P_t}, closure(V_t) \ V_t = ∂V_t ⊔ {P_t}, and P_t ∈ closure(∂V_t).
- So P_t is a chain A_t — B_t — C_t of genus-2 curves. A_t and C_t each carry one node point, and B_t carries two.

**Step 2 (local chart).**
- Let Def(P_t) be the versal deformation germ of P_t, a smooth germ of dimension 15 on which Aut(P_t) acts. The germ of M̄_6 at P_t is Def(P_t)/Aut(P_t).
- Let s_1, s_2 be the smoothing parameters of the nodes A–B and B–C. The locus {s_1 = 0 ≠ s_2} maps to Δ_Γ, with genus-2 vertex the deformation of A_t. The locus {s_2 = 0 ≠ s_1} also maps to Δ_Γ, with genus-2 vertex the deformation of C_t. The locus {s_1 = s_2 = 0} maps to Δ_{G'}.
- Let S̃ ⊂ Def(P_t) be the preimage of the germ of closure(V_t). It is analytic by (R1), since a fibre of an analytic set is analytic. It is of pure dimension 2, since V_t is a dense 2-dimensional manifold in closure(V_t) and the quotient map is finite.
- Moreover S̃ ∩ {s_1 s_2 = 0} is the preimage of ∂V_t ∪ {P_t}, and S̃ ∩ {s_1 = s_2 = 0} = {0}.

**Step 3 (A_t ≅ Y_t).**
- Since P_t ∈ closure(∂V_t), S̃ ∩ {s_1 s_2 = 0} has a branch β̃ through 0.
- β̃ \ {0} is connected and lies in the disjoint union of the relatively open sets {s_1 = 0 ≠ s_2} and {s_2 = 0 ≠ s_1}. Renaming A ↔ C if needed, β̃ \ {0} ⊂ {s_1 = 0 ≠ s_2}.
- Points of β̃ \ {0} lie over ∂V_t, so their genus-2 component (the A-side one) is Y_t. That component depends continuously on the point of the chart, and its value at 0 is A_t. Hence A_t ≅ Y_t as 1-pointed curves.

**Step 4 (the second branch; Lemma C1 of PR-C).**
- Let X_S be an irreducible component of S̃ containing β̃. The function s_2 is not identically 0 on X_S, because it is nonzero on β̃ \ {0}, and s_2(0) = 0.
- So {s_2 = 0} ∩ X_S is of pure dimension 1 through 0. It does not contain β̃, so it contains a branch b̃ ≠ β̃ with b̃ \ {0} ⊂ {s_2 = 0 ≠ s_1}, using S̃ ∩ {s_1 = s_2 = 0} = {0}.
- Points of b̃ \ {0} lie over closure(V_t) ∩ Δ_Γ = ∂V_t, so their genus-2 component, now the C-side one, is Y_t. Letting the point tend to 0 gives C_t ≅ Y_t.

**Step 5 (pinning).**
- Along β̃, π_2 takes values in π_2(∂V_t) ⊂ K: the genus-4 curve obtained by smoothing B ∪ C.
- Its limit at 0 is W_t := B_t ∪ C_t, glued at the B–C node and marked at the point of B_t over the A–B node. So W_t ∈ K ∩ ∂M̄_{4,1} = K_∂.
- C_t is a smooth component of W_t, marked at its special point, so C_t ∈ F. By Step 4, Y_t ∈ F for every t ∈ Δ.
- t ↦ Y_t is continuous (PR-A) and takes values in a finite set, so it is constant on the connected set Δ. ∎

**Remarks.**
1. Lemma 1 shows that the lift R = (Y_t, W_t) has an *unmerged* copy of Y_t at vertex 1, so Theorem P's (T0-a) fails. The pinning instead comes from a *second* copy (twin) C_t of Y_t, which sits inside the boundary point W_t of the *rigid* Teichmüller factor at the other vertex. Step 4 forces this twin to exist at every t: it is the local analytic Lemma C1 combined with the fact that no other boundary curves exist near P_t.
2. Proposition 3 needs neither t small nor hypothesis (ii) beyond (R2). It uses the totally geodesic structure of V_0 only through Step 0.

## 4. General consequences: a dichotomy, a pinning lemma, and a twin criterion

Throughout this section assume (R1), (R2) and the problem's hypotheses. Write P_t := H_t(P_0).

**Lemma D (merge or twin).** Fix t. Let P ∈ closure(∂V_t) \ ∂V_t lie in Δ_{G'}. Let S̃ be the preimage of the germ of closure(V_t) in the versal deformation germ Def(P), and let s_e (e ∈ E(G')) be the smoothing parameters. For a boundary branch c̃ of S̃ through 0, let S_c ⊂ E(G') be the set of edges with s_e ≡ 0 on c̃. Let β̃ be a branch lying over ∂V_t. Then:
1. The edges of G' not in S_β are contracted by the induced contraction c_β : G' → Γ. Its preimage c_β^{-1}(i) is a single vertex j with no loops and no contracted edges, and the component P_j is isomorphic to Y_t.
2. Let b̃ be another boundary branch with the merge property, i.e. some edge f of G' at j has f ∉ S_b. Then exactly one of the following holds.
   - **(D1) Merge.** b̃ lies over a 1-dimensional piece E of closure(V_t) ∩ Δ_{G_b} with G_b ≠ Γ. Then π_v(E) is non-constant, where v is the vertex of G_b containing j (Lemma C2 of PR-C).
   - **(D2) Twin.** b̃ lies over ∂V_t. Then c_b^{-1}(i) is a single loop-free vertex j' ≠ j, and P_{j'} ≅ Y_t. So P has a second component isomorphic to Y_t.

*Proof.*
1. Along β̃ \ {0}, the i-coordinate is the constant smooth curve Y_t. Its limit at 0 is the stable curve assembled from the components P_k, k ∈ c_β^{-1}(i), glued along the edges of G' contracted into i.
   - This limit is the smooth curve Y_t. So the assembled curve has no node, which means c_β^{-1}(i) is one vertex j with no contracted edges or loops, and P_j ≅ Y_t.
2. The coarse image of b̃ \ {0} lies in a single stratum, by connectedness. If that stratum is not Δ_Γ we are in (D1).
   - Otherwise b̃ lies over closure(V_t) ∩ Δ_Γ = ∂V_t. Part 1, applied to b̃, gives the single loop-free vertex j' = c_b^{-1}(i) with P_{j'} ≅ Y_t.
   - The edge f at j is contracted by c_b (f ∉ S_b). So the vertex c_b(j) contains a contracted edge, hence c_b(j) ≠ i, i.e. j ≠ j'. ∎

**Lemma (Pinning).** Let 𝒰 be a finite set of pairs (E_0, u). Here E_0 is a 1-dimensional component of closure(V_0) ∩ Δ_{G}, G product type, u is a vertex of G, π_u(E_0) is a Teichmüller curve in the orbifold sense, and condition (O) of PR-E holds for (E_0, u). Put E_t := H_t(E_0). Suppose:

**(Pin)** For every t in a disc around 0 there is (E_0, u) ∈ 𝒰 such that Y_t is isomorphic, after relabelling, to a smooth component of a point of closure(π_u(E_t)) ∩ ∂M̄_u.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. By Lemma R\* (PR-E), closure(π_u(E_t)) = closure(π_u(E_0)) =: K_u for all t. Each K_u ∩ ∂M̄_u is finite.
2. So Y_t lies in a fixed finite set for t in the disc. By continuity (PR-A) it is constant there.
3. By holomorphy (PR-A) and the identity theorem, Y_t = Y_0 on Δ. ∎

The step-3 argument of Theorem P shows that **(T0) ⇒ (Pin)**. Proposition 3 shows that **(Pin) holds in the example of Section 2**, where (T0) fails. The following criterion abstracts Proposition 3. Like (T0), it is a condition on V_0 alone.

**Theorem 4 (twin criterion).** Let P_0 ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G'}. Let 𝒞 be the set of edge sets S ⊂ E(G') such that contracting E(G') \ S gives a graph identified with Γ, by an identification compatible with ξ_Γ, in which the preimage of vertex i is a single loop-free vertex j(S). Assume:
- **(Tw1)** There is a neighbourhood U of P_0 with (closure(V_0) \ V_0) ∩ U ⊂ ∂V_0 ∪ {P_0}.
- **(Tw2)** For all S ≠ S' in 𝒞:
  - j(S) ≠ j(S');
  - the vertex w = w(S, S') of Γ that contains j(S') under the contraction by S has an edge of G' among the edges contracted into it;
  - for every component E_0 of ∂V_0 with P_0 ∈ closure(E_0), π_w(E_0) is a Teichmüller curve in the orbifold sense satisfying (O).

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Transport.** By (R2), H_t maps closure(V_0) ∩ U onto a neighbourhood of P_t in closure(V_t), preserving strata. So near P_t, closure(V_t) \ V_t ⊂ ∂V_t ∪ {P_t}, and in Def(P_t) we have S̃ ∩ {all s_e = 0, e ∈ E(G')} = {0}.
   - G' and its combinatorics are the same at P_t as at P_0, because the stratum is preserved. The set 𝒞 depends only on G' and Γ.
2. **The branch β̃.** Take a branch β̃ of the preimage of ∂V_t through 0. By Lemma D(1), S_β ∈ 𝒞, and P_t has the component Y_t at j := j(S_β).
   - S_β ≠ E(G'), since P_t ∉ Δ_Γ.
3. **The branch b̃.** Pick e ∉ S_β. Lemma C1 of PR-C, as in Step 4 of Proposition 3, gives a boundary branch b̃ ≠ β̃ through 0 with e ∈ S_b.
   - By Step 1, b̃ lies over ∂V_t. So S_b ∈ 𝒞 by Lemma D(1), S_b ≠ S_β, and P_t has the component Y_t at j' := j(S_b) ≠ j, by (Tw2).
4. **The good vertex.** Let E_t = H_t(E_0) be the component of ∂V_t containing the image of β̃, so P_0 ∈ closure(E_0). Let w = w(S_β, S_b).
   - Along β̃ the w-coordinate converges to the stable curve assembled from the components of P_t over w, which include P_{j'} ≅ Y_t.
   - That curve has a node, by (Tw2). So it lies in closure(π_w(E_t)) ∩ ∂M̄_w, and Y_t is one of its smooth components.
5. **Conclusion.** This is (Pin) with 𝒰 the finite set of pairs (E_0, w) allowed by (Tw2), and it holds for every t. The Pinning Lemma concludes. ∎

**Check against Section 2.**
- G' is the chain A — e_1 — B — e_2 — C, and 𝒞 = {{e_1}, {e_2}} with j({e_1}) = A and j({e_2}) = C.
- w({e_1}, {e_2}) is the genus-4 vertex, which contains the edge e_2. Symmetrically, w({e_2}, {e_1}) contains e_1.
- π_2(∂V_0) = C is a Teichmüller curve. (Tw1) holds because closure(V_0) \ V_0 = ∂V_0 ⊔ {P_0}.
- So Proposition 3 is the case (Tw) of Theorem 4, modulo (O).

**What this means for MS5 and the chain.**
- MS5 (= (T0)) is not the right missing statement. It is false without smoothness (Section 2), and the problem's conclusion survives there via (Tw).
- The correct target is **(Pin)**, or the V_0-only disjunction **"(T0) or (Tw) holds at some point P_0 of closure(∂V_0)"**. Both are still open in general.
- Lemma D explains why a disjunction is natural. At a cusp, Lemma C1 always produces a second boundary branch b̃. If b̃ has the merge property, it is either a genuinely new boundary curve (D1, the (T0) mechanism) or ∂V_t again with a twin (D2, the (Tw) mechanism).
- What neither mechanism covers:
  - a cusp where no branch b̃ merges vertex j and no twin arises: the non-merge case of PR-C, still open;
  - (D1)-branches whose merged vertex is not a Teichmüller curve: positive area not established, (PA) of PR-F;
  - (D2)-twins whose host vertex w is not a Teichmüller curve or carries no node.



### R7-1. Time-t lemmas, constant vertices at junctions, and Theorem T (MS6 near t = 0 under (Lock)) (from round7_q6, verbatim, sections 1–3)
## 1. Fixed-t local lemmas (proved)

Fix t. Let Q ∈ B_t, let x ∈ V(G_Q) be a vertex with Q_x a Y_t-copy, and let b be a 1-dimensional branch of B_t at Q. Let b̃ be a branch at a lift q of Q in Def(Q) of π^{-1}(b), with pinched set S_b := {e : s_e ≡ 0 on b̃} and U_b := E(G_Q) \ S_b. Let G_b := G_Q/U_b; this is the dual graph along b̃ \ {q}, which lies in one stratum. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing π(b̃ \ {q}), lifted to ∏_w M_w in the way the local labelling of b̃ induces. Let p ∈ Ē be the point over Q determined by b. Write [x] for the vertex of G_b containing x.

**Lemma 1 (merges and puncture-moves give MS6).**
- (a) Suppose some edge of G_Q at x lies in U_b ("merge"). Then f_{[x]} is non-constant on E, p is a puncture of E, and f_{[x]}(p) has the component Q_x with the same special points. So MS6 holds at t, witnessed by (E, [x], p).
- (b) Suppose all edges at x lie in S_b, Q ∉ Δ_{G_b} (i.e. U_b ≠ ∅), and f_{[x]} = f_x is non-constant on E. Then p is a puncture and f_x(p) = Q_x ≅ Y_t. So MS6 holds at t.

*Proof.*
- (a) By (Def1), as r → q along b̃ the [x]-component of C_r tends to the curve glued from the components Q_y, y ∈ [x], along the edges of U_b inside [x]. This set of edges contains an edge at x, so the limit is a nodal curve in ∂M̄_{[x]}. Off q the [x]-component lies in M_{[x]}. So f_{[x]} is non-constant (PR-C, Lemma C2), and ν(p) ∉ ∏_w M_w, so p is a puncture.
  - Q_x is a component of the limit curve f_{[x]}(p). Its special points there are the branches of nodes internal to [x] together with the marked points coming from edges leaving [x]. Together these are exactly the node branches of Q at Q_x. So the pointed curve is unchanged.
- (b) Here [x] = {x}, and by (Def1) f_x(p) = Q_x. Some edge of G_Q lies in U_b, so it is contracted into some vertex w of G_b, and f_w(p) is nodal. Hence ν(p) ∉ ∏ M_w, and p is a puncture. ∎

**Lemma 2 (closedness).** N_t := {Q ∈ B_t : Q has a Y_t-copy} is closed in B_t. More generally: if t_n → t, Q_n ∈ B_{t_n}, Q_n → Q, and Q_n has a Y_{t_n}-copy, then Q has a Y_t-copy.

*Proof.*
- Lift to Def(Q): r_n → q. Pass to a subsequence with U(r_n) = U constant, and with the copy of Q_n at a fixed vertex V of G_Q/U.
- By (Def1), the V-component of C_{r_n} converges to the curve glued from the Q_y, y ∈ V, along the edges of U inside V. Since Y_{t_n} → Y_t (PR-A) and Y_t is smooth, this limit is smooth.
- So V is a single vertex y, with no edge of U at y forming a node inside V, and Q_y ≅ Y_t. ∎

**Lemma 3 (dichotomy at a point of N_t).** Suppose MS6 fails at t. Let Q ∈ N_t, let x be any Y_t-copy of Q, and let b be any branch of B_t at Q (any lift b̃). Then exactly one of the following holds:
- (STAY) all edges at x are pinched along b̃, and f_x is constant (≡ Q_x) on the piece E of b; or
- (IMOV, interior move) all edges at x are pinched along b̃, U_b = ∅ (so Q ∈ E is an interior point of the piece, in the same stratum), and f_x is non-constant on E.

Consequently, if moreover no IMOV occurs at points of N_t, then N_t is open in B_t. By Lemma 2 it is then a union of connected components of B_t, and it contains the connected component C_t of B_t containing ∂V_t (on which vertex i is a copy).

*Proof.*
- Lemma 1(a) excludes a merge, and Lemma 1(b) excludes a non-constant f_x with U_b ≠ ∅. What remains is STAY or IMOV.
- Openness: near Q, B_t is the union of its finitely many branches b. If b is STAY for some copy x, the points of b near Q carry the constant component Q_x, so they lie in N_t. ∎

**Remarks on the approach of the task.**
1. IMOV cannot be excluded by Lemma 1: an interior point is not a puncture. L1 and L2 give only that Y_t lies on the t-independent curve closure(π_x(E_0)), with value Y_t = g(σ(t)) where g is one of finitely many maps (L2) and σ(t) := A_t^{-1}(Q̃_t) ∈ Ē_0. The point σ(t) is the transported "junction point" Q_t on E_t. Nothing ties it to a puncture or to a cone point of Ē_t, because A_t is the Thurston/Teichmüller identification and not H_t. So the IMOV case is **not pinned** by these tools. It remains open (see §4).
2. **Step 2(b) is dead in the stated generality (heuristic, not proved).** At a fixed t ≠ 0, V_t is an arbitrary algebraic surface: total geodesy is not available. The only time-t inputs are (R1) and the local analytic structure. A configuration in which a connected component C of the boundary carries a fixed isolated constant component Y is not locally contradictory. Near such a component, closure(V_t) looks like a smoothing of "Y glued to a moving family", with the normal direction contracting (negative normal degree, -ψ·C < 0, so Grauert contractibility is consistent). I did not construct a global algebraic example, so this is only a heuristic. But it shows that any contradiction must come from t = 0, as in option (a), and hence must face the twin problem. §2 explains exactly where that problem enters, and §3 bypasses it under (Lock).

## 2. Where option 2(a) breaks: twins (analysis)

Suppose MS6 fails, and Lemma 3 gives N_{t_n} ⊇ C_{t_n} = H_{t_n}(C_0) for generic t_n → 0. Pass to t = 0, and fix Q_0 ∈ C_0 together with the MERGE branch b of Proposition K, in which the tracked copy c of Q_0 merges along a lift b̃.
- For lifts q_n → q_0 of Q_{t_n}, every lift-branch b̃_n of b_{t_n} at q_n converges into a lift γ b̃ of b, for some γ ∈ Aut(Q_0). By the edge count of Step 3 below, its pinched set is S_{b̃_n} = γ S_b̃. So the label γc merges along b̃_n.
- The Y_{t_n}-copies of Q_{t_n} converge to Y_0-copies of Q_0 (Lemma 2), so the limiting labels lie in Λ(Q_0) := {ℓ ∈ V(G_{Q_0}) : Q_{0,ℓ} is a Y_0-copy}.
- But γc need not be among them. Q_0 may have several Y_0-copies, a merged one and an unmerged twin, and for t ≠ 0 these may stop being isomorphic. Then the merged one is not a Y_t-copy, and no contradiction arises.

This is exactly the twin phenomenon of PR-G/PR-I. Option (a) and the direct transport of §3 fail or succeed at the same place. I therefore isolate the needed property as a hypothesis.

**Definition (Lock).** Let R ∈ B_0 ∩ Δ_{G'}, let q_0 ∈ Def(R) be a lift, and let Λ(R) ⊂ V(G') be the set of labels of Y_0-copies of R. Note that Λ(R) is Aut(R)-invariant. R is *locked* if there is ε > 0 such that, for |t| < ε and every lift q of R_t := H_t(R) in a fixed small neighbourhood of q_0 in Def(R), the components C_{q,ℓ}, ℓ ∈ Λ(R), are pairwise isomorphic as pointed curves up to reordering.
- (Lock) holds trivially if |Λ(R)| = 1, i.e. R has a unique Y_0-copy.
- It holds at the point P_0 of the quintic example (PR-I, Proposition 3, Steps 3–4: A_t ≅ C_t ≅ Y_t for all t, and Λ(P_0) = {A, C} since B_0 has two special points).
- Note that R_t ∈ Δ_{G'} for all t by (R2), so its lifts lie in D' := {s_e = 0 for all e} ⊂ Def(R), where the labels make sense.

## 3. Theorem T: MS6 near t = 0 under (Lock) (proved modulo Proposition K and the cited standard facts)

### 3.1 Two auxiliary lemmas

**Lemma 4 (connected subsets of B_0).** B_0 is a compact analytic set of pure dimension 1. A compact connected K ⊂ B_0 is either a point or a finite union of closed arcs, each contained in the closure of one piece and meeting that piece in the arc minus finitely many points.

*Proof.*
- **Pure dimension 1.** closure(V_0) is pure 2-dimensional, and locally (in Def) B_0 is cut out by the single equation ∏ s_e = 0. So by Krull every component of B_0 has dimension ≥ 1, and dim B_0 ≤ 1.
- **Graph structure.** A compact 1-dimensional analytic set is triangulable as a finite graph. Its vertices include the singular points and the points where the stratum changes, and each open edge lies in a single piece.
- **K ∩ an edge.** Let e be a closed edge (an interval) and J a component of K ∩ e. If J missed both endpoints of e, apply the boundary-bumping theorem for the continuum K and an open interval U ⊃ J in e°. The component of K ∩ closure(U) containing J meets ∂U, so it is an interval strictly larger than J inside K ∩ e. This is a contradiction.
- So each component of K ∩ e contains an endpoint of e. Hence K ∩ e is a union of at most two closed intervals, or all of e.
- **Conclusion.** K is a finite union of points and closed arcs. Since K is connected, it is a single point or has no isolated points. ∎

**Lemma 5 (constant vertices at a junction).** Let E_0 be a piece of B_0 in a product-type stratum Δ_G, and x a vertex of G with π_x ≡ z_0 on E_0, where z_0 is a Y_0-copy-class. Put E_t := H_t(E_0). Then:
- (i) π_x is constant on E_t, with value z(t). The map t ↦ z(t) is continuous, and z(0) = z_0.
- (ii) Let R ∈ closure(E_0) ∩ Δ_{G'}, R_t := H_t(R), and q any lift of R_t. Then there is a label ℓ ∈ V(G') with C_{q,ℓ} ≅ z(t), as pointed curves up to reordering.
- (iii) If t_n → 0 and lifts q_n of R_{t_n} converge to the lift q_0 of R, then for large n every label ℓ_n as in (ii) lies in Λ(R).

*Proof.*
- **(i).** This is L1. **Check of L1 (I verified it).**
  - 𝓦 (the closure of the lift of H(E_0 × Δ); Lemma R0) is irreducible, 2-dimensional and proper over Δ, and pr_x(𝓦_0) = {z_0}.
  - Take an affine neighbourhood U of z_0 in the coarse space. By properness, pr_x(𝓦_t) ⊂ U for |t| small. Compact curves map to points of an affine variety, so the image Z := (pr_x, t)(𝓦) is finite over a small disc.
  - Z is analytic and irreducible by Remmert, so dim Z = 1. Hence Z is finite over all of Δ, and pr_x is constant on every compact irreducible curve in every fibre 𝓦_t.
  - For product type, closure(E_t) ⊂ 𝓦_t up to finitely many points (R0 with base point t; (R2) is symmetric in t), and E_t is irreducible (PR-D, Step 1). So π_x|_{E_t} ≡ z(t).
  - Continuity: z(t) = π_x(H(e, t)) for any fixed e ∈ E_0, and H is continuous.
- **(ii).**
  - R_t ∈ closure(E_t), by (R2) together with the fact that homeomorphisms commute with closures. Let β be a branch of closure(E_t) at R_t. The germ π^{-1}(β) is nonempty at every point of the fibre π^{-1}(R_t), since π^{-1}(β) is Aut(R)-invariant. Let β̃ be a branch of π^{-1}(β) at q.
  - Along β̃ \ {q}, the curve C_r has a component ≅ z(t). It sits at some vertex V(r) of G'/U, where U is the unpinched set of β̃.
  - The set {r ∈ β̃ : C_{r,V} ≅ z(t)} is analytic for each V (by (Def1)), and the union over the finitely many V is all of β̃. So one V works on all of β̃.
  - By (Def1), the limit at q of C_{r,V} is the curve glued from the C_{q,y}, y ∈ V, along the internal edges of U. It equals z(t), which is smooth. So V = {ℓ} is a single label, with no edge of U forming a node inside V, and C_{q,ℓ} ≅ z(t).
- **(iii).**
  - Suppose not. Pass to a subsequence with ℓ_n = ℓ ∉ Λ(R) fixed.
  - The q_n lie in D' (strata are preserved), on which ℓ ↦ C_{q,ℓ} is continuous by (Def1). So C_{q_0,ℓ} = lim C_{q_n,ℓ} ≅ lim z(t_n) = z_0, a Y_0-copy class. Hence ℓ ∈ Λ(R), a contradiction. ∎

(For pieces in non-product strata, replace E_t by an irreducible component of the lift of H((E_0 \ S_0) × Δ) to ∏_w M_w, as in R0, Step 3. The same proof applies. I have only checked this routinely.)

### 3.2 Statement and proof

**Input from t = 0 (Proposition K, PR-H §3, "proved modulo routine marking details" there; not re-verified here).** There are:
- a compact connected K_0 ⊂ B_0 with P ∈ K_0 ∩ ∂V_0, every point of which has a Y_0-copy;
- a point Q_0 ∈ K_0, and a branch b of B_0 at Q_0 with a lift b̃ at q_0 ∈ Def(Q_0), and a label c ∈ Λ(Q_0), such that along b̃ either (MERGE) some edge at c is unpinched, or (MOV) all edges at c are pinched and the c-component is non-constant along b̃.

Theorem T uses only these properties, and not the path-marking ("tracking") in Proposition K.

**Theorem T.** Assume (R1), (R2), the hypotheses of the problem, and the input above. Assume moreover:
- (T1) b is MERGE, or b is MOV with Q_0 ∉ Δ_{G_b} (Q_0 is a puncture of the piece of b; "puncture-MOV");
- (T2) the finitely many pieces met by the arcs of K_0 (Lemma 4) lie in product-type strata (removable, see the parenthetical remark after Lemma 5);
- (T3) (Lock) holds at P, at Q_0 and at the finitely many junction points R_1, …, R_{m-1} chosen in Step 0 below.

Then there is ε > 0 such that for every |t| < ε, MS6's witness exists at t. That is, there are a piece E at time t, a vertex u non-constant on E, and a puncture p of E such that f_u(p) has a Y_t-copy. In particular MS6 holds, with T ⊇ {|t| < ε}.

*Proof.*

**Step 0 (chain).**
- If K_0 = {P}, then Q_0 = P; put m := 0 and skip Steps 1–2.
- Otherwise, by Lemma 4, K_0 = A_1 ∪ … ∪ A_N is a finite union of closed arcs. Their intersection graph is connected, since K_0 is connected and the arcs are closed. So there is a chain of arcs A_1, …, A_m with P ∈ A_1, Q_0 ∈ A_m, and junction points R_k ∈ A_k ∩ A_{k+1}. Put R_0 := P and R_m := Q_0.
- Let A_k ⊂ closure(E^k), where E^k is a piece and A_k \ E^k is finite.
- Every point of A_k ∩ E^k has a Y_0-copy, and the copy is one of the finitely many vertex coordinates of the point. So for some vertex x_k, the analytic set {e ∈ E^k : π_{x_k}(e) is a Y_0-copy class} contains an open sub-arc, and hence equals E^k.
- Thus π_{x_k} ≡ z_k(0), a Y_0-copy class, on E^k_0. Let z_k(t) be as in Lemma 5(i).

**Step 1 (start).**
- P_t := H_t(P) ∈ ∂V_t, and the component of P_t at vertex i is Y_t. Apply Lemma 5(ii),(iii) to the component of ∂V_0 through P with the constant vertex i. For small |t| and every lift q of P_t near q_0, Y_t ≅ C_{q,ℓ_0} for some ℓ_0 ∈ Λ(P).
- Lemma 5(ii),(iii) for (E^1, x_1, R_0 = P) gives, for small |t| and lifts near q_0, a label ℓ ∈ Λ(P) with C_{q,ℓ} ≅ z_1(t). By (Lock) at P, z_1(t) ≅ C_{q,ℓ_0} ≅ Y_t.
- In detail: if this failed along t_n → 0, choose lifts q_n of P_{t_n} converging to q_0. This is possible since P_{t_n} → P, the fibres of π accumulate on π^{-1}(P) = Aut(P)·q_0, and we may translate by Aut(P). Lemma 5(iii) and (Lock) then give a contradiction.

**Step 2 (induction along the chain).** At R_k (1 ≤ k ≤ m−1), apply Lemma 5(ii),(iii) to (E^k, x_k) and to (E^{k+1}, x_{k+1}) at the same lift q of R_{k,t} near q_0(R_k). For small |t|, z_k(t) ≅ C_{q,ℓ} and z_{k+1}(t) ≅ C_{q,ℓ'} with ℓ, ℓ' ∈ Λ(R_k). By (Lock) at R_k, z_{k+1}(t) ≅ z_k(t). (Argue by contradiction along sequences, as in Step 1.) By induction, z_m(t) ≅ Y_t for |t| < ε.

**Step 3 (the end point; MERGE).**
- Let t_n → 0 and let q_n be lifts of Q_{t_n} := H_{t_n}(Q_0) converging to q_0. The branch b_{t_n} := H_{t_n}(b) is a branch of B_{t_n} at Q_{t_n}, lying in Δ_{G_b} by (R2). Let b̃_n be a branch of π^{-1}(b_{t_n}) at q_n, with pinched set S_n. Pass to a subsequence with S_n = S constant.
- **Limit branch.** Points of b̃_n map to H_{t_n}(b). Since H^{-1} is continuous and H_0 = id, every limit point of ∪_n b̃_n lies in π^{-1}(b).
  - Each b̃_n is connected, passes through q_n, and leaves the ball of radius r around q_0 (for r small and n large, because H_{t_n} → id uniformly near Q_0). So the limit set contains points at every small distance r from q_0.
  - These points lie in π^{-1}(b) ∩ {s_e = 0, e ∈ S}. So some branch γb̃ of π^{-1}(b) at q_0 (γ ∈ Aut(Q_0); the branches of the preimage of the irreducible germ b are permuted transitively by Stab(q_0) = Aut(Q_0)) meets this closed analytic set in infinitely many points accumulating at q_0. Hence γb̃ ⊂ {s_e = 0, e ∈ S}, i.e. S ⊂ γS_b̃.
- **Edge count.** Both b̃_n \ {q_n} and γb̃ \ {q_0} lie over Δ_{G_b}. Along such a branch the pinched edges are exactly the nodes of the generic curve, so |S| = |E(G_b)| = |γS_b̃|. Hence S = γS_b̃, and the unpinched set is U_n = γU_b̃.
- **The merged label is a Y_t-copy.**
  - In the MERGE case, U_b̃ contains an edge at c, so U_n contains an edge at γc. Moreover γc ∈ Λ(Q_0), since automorphisms preserve isomorphism classes of components.
  - By Step 2 and Lemma 5(ii),(iii) for (E^m, x_m) at R_m = Q_0, some label ℓ ∈ Λ(Q_0) has C_{q_n,ℓ} ≅ z_m(t_n) ≅ Y_{t_n}. (If m = 0, use the label i as in Step 1.)
  - By (Lock) at Q_0, C_{q_n,γc} ≅ Y_{t_n}.
- **Conclusion.** Lemma 1(a), applied at time t_n to Q = Q_{t_n}, x = γc and the branch b_{t_n} with lift b̃_n, gives MS6's witness at t_n.
- Since t_n → 0 was an arbitrary sequence (and the subsequence extraction is harmless), the witness exists for all small |t|.

**Step 3′ (the end point; puncture-MOV).**
- Proceed as in Step 3 up to S = γS_b̃. In the MOV case all edges at c lie in S_b̃, so all edges at γc lie in S: the label γc is intact along b̃_n. As before, (Lock) gives C_{q_n,γc} ≅ Y_{t_n}.
- Since Q_0 ∉ Δ_{G_b} and strata are preserved, Q_{t_n} ∉ Δ_{G_b}. So Lemma 1(b) applies at t_n, provided the γc-component is non-constant along b̃_n.
- Suppose instead it is constant along b̃_n for infinitely many n. Then it is ≡ C_{q_n,γc} ≅ Y_{t_n}.
  - On the closed set {s_e = 0 for e at γc}, which contains all b̃_n and γb̃, the γc-component is continuous (Def1).
  - Every limit point y of the b̃_n then has γc-component ≅ lim Y_{t_n} = Y_0. These limit points include infinitely many points of γb̃ accumulating at q_0, as in Step 3.
  - Hence the γc-component is constant (≅ Y_0) on γb̃, by the identity theorem on the normalized branch. Applying γ^{-1}, the c-component is constant on b̃, contradicting MOV.
- So for large n the γc-component moves along b̃_n, and Lemma 1(b) gives the witness at t_n. ∎

**Corollary T′ (the problem's claim under the same hypotheses).** Under the hypotheses of Theorem T, together with the chain's inputs (Teichmüller vertices for the pieces, (O) and (F2), as in step 5 of the chain), Y_t = Y_0 for all t ∈ Δ.

*Proof.* By the chain derivation 1–4 of the task, MS6 with T ⊇ {|t| < ε} gives Y_t ∈ F (a finite set) for |t| < ε. By continuity Y is constant near 0, and by PR-A and the identity theorem, Y_t = Y_0 on Δ.
- Directly: in the MERGE case the witness piece at t is H_t(E_b), where E_b is the piece of b. Its vertex [γc] is non-constant at t = 0 by C2, and L2 pins its puncture values. ∎

**Remark (a reduction of (Lock)).** Lock at R only needs to be proved for some sequence t_n → 0, not for all small t, provided the copies are given by holomorphic functions. Precisely: if a lift curve t ↦ q(t) of R_t can be chosen holomorphic on a small disc, which is the case when R is isolated in B_0 ∩ Δ_{G'}, because then t ↦ R_t is the analytic curve closure(𝒱) ∩ (Δ_{G'} × Δ) locally, then the set {t : C_{q(t),ℓ} ≅ C_{q(t),ℓ'}} is analytic. So it suffices that it has an accumulation point at 0.
- In particular, (Lock) at an isolated point R follows from the PR-I mechanism (Lemma C1 + Lemma D(D2)), whenever near R the only boundary branches are branches of ∂V_t: each such branch forces its own label in Λ(R) to be a Y_t-copy (Theorem 4 of PR-I, condition (Tw1)).
- I state this only as a sketch.

**Remark (what Theorem T removes).** Theorem T needs no tracking of "the" Y-component and no transport of branch identities. Only isomorphism classes are transported, and they are insensitive to automorphisms of R. The only places where twins can still hurt are the finitely many points of (T3), and the IMOV alternative is excluded by (T1).


### R7-2. Auxiliary lemmas, Theorem A (MS6 without twins), the open cases (twins, crossings), and why transporting Teichmüller rays meets orbifold points (from round7_q8, verbatim, sections 2–4)
## 2. Auxiliary lemmas (proved)

Notation:
- "Component ≅ Y_0" means: an irreducible component which, with its special points in some order, is isomorphic to Y_0. Equivalently, its class in M_{g_i,n_i}/S_{n_i} equals that of Y_0.
- Fix a metric d on the compact space M̄_{g_i,n_i}/S_{n_i}.
- Choose ε > 0 so small that the closed ball B̄_{3ε}(Y_0) lies in the open part M_{g_i,n_i}/S_{n_i}.

**Lemma 2.1 (non-constancy persists off a discrete set).** Let 𝓦 be an irreducible 2-dimensional analytic set, closed in ∏_w M̄_w × Δ (hence proper over Δ), with t non-constant on 𝓦. Let u be a vertex. Suppose pr_u is non-constant on some 1-dimensional component of 𝓦_0. Then the set of t such that pr_u is constant on some 1-dimensional component of 𝓦_t is discrete in Δ.

*Proof.*
1. Let Φ = (pr_u, t) and Σ = {p ∈ 𝓦 : dim_p Φ^{-1}Φ(p) ≥ 1}. Σ is analytic (Cartan–Remmert).
2. Suppose t_n → t* ∈ Δ, with t_n pairwise distinct, and pr_u constant on a component C_n of 𝓦_{t_n}. Then C_n ⊂ Σ.
3. If dim Σ ≤ 1, then each C_n is an irreducible component of Σ. Infinitely many of them meet the compact set 𝓦 ∩ {|t − t*| ≤ r}, contradicting local finiteness of the components.
4. So Σ = 𝓦. The last bullet of §1.1 then shows that pr_u is constant on every component of every fibre, including 𝓦_0. This contradicts the hypothesis. ∎

**Lemma 2.2 (limits of components).** Let C_n → C in M̄_g. Let c_n be a component of C_n of type (g_i, n_i) with class in B̄_{3ε}(Y_0). Then, after passing to a subsequence, c_n converges in M̄_{g_i,n_i}/S_{n_i} to the class of a smooth component c of C.

*Proof.*
1. In a versal chart Def(C), for n large, C_n is a smoothing of a subset of the nodes of C. A component c_n of C_n is a smoothing of a connected subcurve A_n of C. After passing to a subsequence, A_n = A is fixed.
2. In the chart, c_n with its special points converges to A, stabilised and pointed by the nodes of C that leave A. This is continuity of the gluing/plumbing maps.
3. If A had two components or an internal node, the limit would lie in the boundary of M̄_{g_i,n_i}. But the limit lies in B̄_{3ε}(Y_0) ⊂ M_{g_i,n_i}/S_{n_i}. So A is a single smooth component c of C. ∎

**Lemma 2.3 (finitely many isolated Y_0-points).** Let F_0 ⊂ B_0 be the union of the following finitely many sets:
- (i) for each stratum G, the isolated points of B_0 ∩ Δ_G (the 0-dimensional components of the compact analytic set B_0 ∩ closure(Δ_G) that lie in Δ_G);
- (ii) the singular points of each 1-dimensional set B_0 ∩ Δ_G;
- (iii) for each piece E (lift of a 1-dimensional component, as in MS6) and each vertex y non-constant on E, the images of the points of E at which f_y takes the value Y_0 (up to relabelling).

Then F_0 is finite.

*Proof.*
- (i) A compact analytic set has finitely many components.
- (ii) Each 1-dimensional set has finitely many singular points on the compact closure.
- (iii) f_y : Ē → M̄_y is a non-constant holomorphic map from a compact Riemann surface. The fibre over each of the finitely many relabellings of Y_0 is finite. ∎

---

## 3. Theorem A (partial result: MS6 without twins)

### 3.1 The input from t = 0 (Proposition K, PR-H, used as a prior result)
I use the following output of Proposition K, which was proved there modulo routine marking details. I did not re-prove it.

**(K)** There are:
- a compact connected set K_0 ⊂ B_0 containing a point P ∈ ∂V_0;
- for every Q ∈ K_0, a component x_Q of Q with x_Q ≅ Y_0 (the "Σ_i-component"), such that at P it is the vertex-i component;
- a point Q_0 ∈ K_0;
- a 1-dimensional branch b of B_0 at Q_0, of one of two types:
  - **(MERGE)** some node of Q_0 at x_{Q_0} is smoothed along b;
  - **(MOV)** all nodes at x_{Q_0} stay pinched along b, and the component carried by x is non-constant along b.

Call the MOV case **at a puncture** if b \ {Q_0} lies in a stratum strictly coarser than that of Q_0, and **interior** otherwise.

### 3.2 Hypotheses
- **(NT\*)** No point of B_0 has two distinct components that are both ≅ Y_0.
  This is a condition on V_0 alone. It FAILS in the quintic example of PR-I, where the point P_0 = Y_0 — B_0 — Y_0 has two components ≅ Y_0.
- **(PT)** Every stratum Δ_G such that K_0 ∩ Δ_G is infinite is of product type.
- **(E)** The endpoint in (K) is of type MERGE, or MOV at a puncture.

**Theorem A.** Assume (R1), (R2), the problem's hypotheses, (K), (NT\*), (PT) and (E). Then there are t_0 > 0 and a discrete set D ⊂ Δ such that the configuration of MS6 exists for every t with |t| < t_0 and t ∉ D.

In the MERGE case D = ∅. In particular MS6 and MS6′ hold under these hypotheses, and with them the problem's claim (via the chain, modulo (O) and (F2)).

### 3.3 Proof of Theorem A

**Step 1 (uniform separation at t = 0).** There is ε > 0, which we may shrink to satisfy §2, such that for every Q ∈ K_0, every component of Q of type (g_i, n_i) other than x_Q has class at distance ≥ 3ε from Y_0.

*Proof.*
1. Otherwise there are Q_n ∈ K_0 and components y_n ≠ x_{Q_n} with y_n → Y_0. Pass to a subsequence with Q_n → Q ∈ K_0 (K_0 is compact).
2. By Lemma 2.2, applied to x_{Q_n} and to y_n (both classes are in B̄_{3ε}(Y_0) for n large), both converge to smooth components of Q isomorphic to Y_0.
3. These limit components are distinct:
   - In a chart Def(Q), for n large, the Q_n lie in a fixed locus of the chart, in which their components are smoothings of fixed disjoint connected subcurves A_x, A_y of Q. Here A_x ≠ A_y because x_{Q_n} ≠ y_n are distinct components.
   - By Lemma 2.2 both are single components, so they are distinct components of Q.
4. So Q has two components ≅ Y_0, contradicting (NT\*). ∎

**Step 2 (uniform separation for small t).** There is t_0 > 0 such that for |t| ≤ t_0 and every Q ∈ K_0, the curve H_t(Q) has exactly one component of type (g_i, n_i) whose class lies in B̄_{2ε}(Y_0), and that component lies in B̄_ε(Y_0). Write λ_t(Q) for its class.

*Proof.* Suppose not. Take t_n → 0 and Q_n ∈ K_0 violating the claim, with Q_n → Q ∈ K_0. Then H_{t_n}(Q_n) → Q, by continuity of H and H_0 = id.

- *Two components in B̄_{2ε}.* Lemma 2.2 and the argument of Step 1 give two distinct components of Q in B̄_{2ε}(Y_0). This contradicts Step 1.
- *None in B̄_ε.* Work in Def(Q).
  1. The path τ ↦ H_τ(Q_n), τ ∈ [0, t_n], has small diameter by uniform continuity of H on compact sets. So it lifts to a path in Def(Q) near 0, by path lifting for finite group quotients (Bredon, *Introduction to compact transformation groups*, II.6, cited from memory).
  2. The whole path lies in one stratum, because H is stratum preserving. Along it, the component that is a smoothing of a fixed connected subcurve A of Q varies continuously.
  3. At τ = 0 the component x_{Q_n} ≅ Y_0 is the smoothing of some A. By Lemma 2.2 and Step 1, A is the single component x_Q.
  4. The A-component of H_{t_n}(Q_n) is close to the A-component at the chart point of H_{t_n}(Q_n), and that point tends to 0. So it converges to x_Q ≅ Y_0, and it lies in B̄_ε(Y_0) for n large. Contradiction. ∎

**Step 3 (λ_t is continuous on K_0 for each fixed |t| ≤ t_0).**
1. Let Q_n → Q in K_0. Then H_t(Q_n) → H_t(Q).
2. By Lemma 2.2, every subsequence of the components realising λ_t(Q_n) has a further subsequence converging to a smooth component of H_t(Q) whose class lies in B̄_ε(Y_0).
3. By Step 2 that component is the one realising λ_t(Q). Hence λ_t(Q_n) → λ_t(Q). ∎

**Step 4 (λ_t takes finitely many values on K_0).** Enlarge F_0 by the finitely many points of K_0 that lie in strata Δ_G with K_0 ∩ Δ_G finite. Call the result F_0′; it is finite. Let Q ∈ K_0 \ F_0′, lying in Δ_G.
1. By (PT), Δ_G is of product type. So ξ_G : ∏M_w → Δ_G is a homeomorphism, the pieces in Δ_G are just the 1-dimensional components of B_0 ∩ Δ_G, and vertex labels are canonical.
2. Since Q ∉ F_0, Q is a smooth point of B_0 ∩ Δ_G on a unique piece D. Its component x_Q is the value at Q of a vertex y_0 of G.
3. Since Q ∉ F_0(iii), y_0 is constant on D, with value ≅ Y_0.
4. Let 𝓦 be the closure of H(D × Δ) in ∏M̄_w × Δ. It is irreducible by Lemma R0 (PR-D). By L1 (§1.1), y_0 is constant on every component of every fibre of 𝓦.
5. D_t = H_t(D) is irreducible (PR-D, Step 1). So y_0 has a single constant value z_{D,y_0}(t) on D_t.
6. The vertex values of H_τ(Q), τ ∈ [0, t], are continuous in τ. By Step 2, for each τ exactly one vertex has value in B̄_{2ε}(Y_0), and that value lies in B̄_ε(Y_0).
7. Hence, for each vertex y, the set {τ : value of y ∈ B̄_ε} equals {τ : value of y ∈ B̄_{2ε}}. It is therefore both closed and open in [0, t]. So the distinguished vertex is y_0 for all τ.
8. Therefore λ_t(Q) = z_{D,y_0}(t).

So λ_t(K_0) is contained in the finite set {z_{D,y}(t)} ∪ {classes of components of H_t(Q′) : Q′ ∈ F_0′}. ∎

**Step 5 (λ_t ≡ Y_t on K_0).**
1. K_0 is connected, and λ_t is continuous (Step 3) with finite image (Step 4). So λ_t is constant on K_0.
2. H_t(P) ∈ ∂V_t by (R2). Its vertex-i component is Y_t.
3. By PR-A, after shrinking t_0, d(Y_t, Y_0) ≤ ε for |t| ≤ t_0. By the uniqueness in Step 2, λ_t(P) = Y_t.
4. Hence **λ_t(Q_0) = Y_t** for |t| ≤ t_0. ∎

**Step 6 (the branch at time t).**

*Setting.*
- Let Q_0 ∈ Δ_{G′}. Let Def(Q_0) be the versal deformation germ, with Aut(Q_0) acting, and smoothing parameters s_e for e ∈ E(G′). Put Q_τ := H_τ(Q_0).
- By (NT\*), every σ ∈ Aut(Q_0) fixes the component x := x_{Q_0}. Indeed σ permutes components preserving isomorphism class, and x is the only component ≅ Y_0.
- Let G_b be the stratum of b \ {Q_0}. Let A′ := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ) and A″ := closure(𝒱) ∩ (closure(Δ_{G′}) × Δ). Both are analytic by (R1), and A″ ∩ (Δ_{G_b} × Δ) = ∅.
- Put N_b := H((b \ {Q_0}) × Δ).

*N_b is a union of irreducible germs of A′.*
1. Since H is a stratum-preserving homeomorphism, near (Q_0, 0) the set N_b is open and closed in A′ \ A″. Its closure is H(b̄ × Δ).
2. An irreducible germ minus a proper analytic subset is connected. So closure(N_b) is a finite union of irreducible 2-dimensional germs W^1, …, W^m of A′ at (Q_0, 0).
3. The τ = 0 fibre of each W^j is of pure dimension 1 (Krull). It is contained in b̄. It is not contained in A″, because b̄ ∩ A″_0 = {Q_0}.
4. Let W̃^j be an irreducible component of the preimage of W^j in Def(Q_0) × Δ.
5. On the connected set W̃^j \ (preimage of A″), the set of edges e with s_e = 0 is locally constant. The loci "exactly S vanish", over subsets S of a fixed size, are disjoint and relatively open. So this set is a constant S_j.
6. At τ = 0 those points lie over b \ {Q_0}. So S_j is the pinched set of a lift σ(b̃) of b, for some σ ∈ Aut(Q_0).
7. Since σ fixes x:
   - in the MERGE case some edge at x is not in S_j;
   - in the MOV case every edge at x is in S_j.

*Limits along b_τ.*
1. Fix τ with |τ| < t_0 (shrunk if necessary), and take R_n ∈ b_τ \ {Q_τ} with R_n → Q_τ. These points lie in N_b.
2. Pass to a subsequence lying in one W^j. Their lifts r̃_n lie in ρ(W̃^j) for a fixed ρ ∈ Aut(Q_0), and converge to a lift q̃ of Q_τ.
3. R_n is the smoothing of q̃ along the edges not in ρ(S_j). Its component containing the deformation of the x-labelled component of q̃ is a smoothing of the connected subcurve A ∋ x spanned by the edges not in ρ(S_j).
4. The x-labelled component of the fibre over q̃ is isomorphic to the one over a continuous lift p_τ (p_0 = 0) of Q_τ, because the relating automorphism fixes x. That one has class close to Y_0 for small τ. By Step 2 its class is λ_τ(Q_0), which equals Y_τ by Step 5.

*Passing to the piece.*
1. Let E be a piece at time τ containing lifts R̂_n of the R_n (finitely many pieces; pass to a subsequence). Let v be the vertex of G_b whose coordinate on R̂_n is the component from item 3 above (fixed after a subsequence).
2. R̂_n converges to ν(p) for some p ∈ Ē. Since Q_τ ∉ Δ_{G_b}, p is a puncture of E.
3. By plumbing continuity (as in Lemma 2.2), f_v(p) = A, pointed by the nodes of Q_τ that leave A. So f_v(p) has the component x(τ) ≅ Y_τ, with its special points.

**Step 7 (conclusion).**
- **MERGE.** A has a node, because some edge at x is not in ρ(S_j). So f_v(p) ∈ ∂M̄_v.
  - f_v is non-constant on E, by Lemma C2: a constant value Z ∈ M_v would have limit Z ∉ ∂M̄_v.
  - So MS6 holds at τ, for every |τ| < t_0.
- **MOV at a puncture.** Here A = {x}, so f_v(p) ≅ Y_τ. It remains to show that f_v is non-constant on E.
  - The vertex receiving x is locally constant on the connected set W̃^j \ (preimage of A″). It equals the MOV vertex at τ = 0.
  - By (PT), G_b is of product type, so vertex labels are canonical. Then E = H_τ(E_b), where E_b is the piece containing b. The family closure(H(E_b × Δ)) is irreducible (Lemma R0).
  - By Lemma 2.1, f_v is non-constant on E for τ outside a discrete set D.
  - So MS6 holds for |τ| < t_0, τ ∉ D. ∎

### 3.4 Remarks on Theorem A
1. **Holomorphy is not used.** The proof never uses that Y is holomorphic. The labels are pinned down by continuity on the connected set K_0, together with finiteness of the label set at a FIXED t (Step 4). In particular Theorem A gives MS6 itself, not only MS6′. It also holds for constant families, where it proves MS6_0 under (K), (NT\*), (PT), (E).
2. **Theorem A gives the problem's claim directly**, without L2, in the MERGE case, provided the vertex v at Q_0 is a Teichmüller vertex satisfying (O). Then f_v(p_τ) ranges in a finite set (L2, or Lemma R\* for v itself), so Y_τ does too, and Y is constant. In general one goes through the chain (§1).
3. **Where each hypothesis is used.**
   - (NT\*) is used in Step 1 (separation), and in Step 6 to make Aut(Q_0) fix x.
   - (PT) is used in Step 4 and in the MOV case of Step 7.
   - (E) is used in Step 7.

### 3.5 Removing (PT) (sketch only, not claimed)
- For a non-product stratum one would replace ∏M_w by Ω_{y} := ∏M_w / Stab_{Aut(G)}(y), the space of points of Δ_G together with a chosen component in the orbit of y. The coordinate p_y is well defined on Ω_y.
- Under (NT\*), at points of K_0 the map Ω_{y_0} → Δ_G is a local homeomorphism near (Q, x_Q). Every automorphism fixing a lift fixes y_0, since x_Q is the only component ≅ Y_0.
- The remaining point is L1 for the sheet (D, x_Q) of the lifted family. One must show that the irreducible family component containing this sheet has no other sheet (D, x′) over τ = 0 on which p_{y_0} is non-constant. That is a monodromy statement about the complement of the ramification locus in the 2-dimensional family. I believe it follows from (NT\*), but I have not written it.

---

## 4. What remains open, and why

### 4.1 Twins (removing (NT\*))
Without (NT\*), Step 1 fails, and λ_t becomes a multivalued function on K_0.
- At a point J ∈ K_0 with two components x, y ≅ Y_0, the continuations x(t) and y(t) can carry different holomorphic labels: z_D(t) from one adjacent STAY piece D, and z_{D′}(t) from another adjacent STAY piece D′.
- The Y_0-network of Proposition K is only "consistent with the path marking". Path markings at a boundary point are defined only up to Aut(J) and the approximating sequence. So the network may jump from x to y at J.
- At time t ≠ 0 the automorphism realising the jump may disappear. Then the copy of Y_t being followed is lost.
- The quintic example (PR-I) shows that such twin points really occur, although on a non-smooth V_0. There the problem's claim is rescued by a different mechanism: the twin sits in a puncture value of a rigid vertex (PR-I, Theorem 4).
- **Open question 1.** Is (NT\*) dispensable? Concretely: at a twin junction J, does one of the following always happen at time t?
  - the Y_t-copy continues along a STAY piece carrying the label Y;
  - the Y_t-copy enters a non-constant vertex at a puncture (that is, MS6).

  The only other possibility is a crossing (4.2). I have no argument.

### 4.2 Crossings (removing (E))
Suppose the endpoint is of type MOV-interior. Then Q_0 ∈ E_b, where E_b is a piece in the stratum of Q_0, and the vertex x is non-constant on E_b with f_x(Q_0) = Y_0. Also, Q_0 lies in the closure of an adjacent STAY piece.

Under (NT\*) and (PT), Steps 1–5 still give λ_t(Q_0) = Y_t. That is:

  **Y_t = f_x^t(H_t(Q_0))**, the value of the non-constant vertex x at the INTERIOR point H_t(Q_0) of the transported piece E_{b,t}.

This is not the MS6 configuration. Nor does it yield rigidity:
- If x is a Teichmüller vertex of E_b satisfying (O), Lemma R\* only gives that Y_t moves inside the fixed curve closure(π_x(E_{b,0})).
- H_t(Q_0) is an uncontrolled point of E_{b,t}.

**A crossing is locally consistent (so no Krull-type argument can exclude it).**
- Take a smooth germ of closure(V_t) with coordinates (σ, ρ).
- Put s_e = ρσ for the edges e at x, and s_f = ρ for the other edges. Let the x-coordinate equal σ.
- Then {ρ = 0} is E_b: all edges are pinched and x moves.
- {σ = 0} is the STAY piece: the edges at x are pinched, the others are smoothed, and x is constant.
- Points with ρσ ≠ 0 lie in M_g.

This is compatible with (R1), (R2), (i) and (ii), at t = 0 and at every t. It is the same phenomenon as in PR-C.

- **Open question 2.** Can Proposition K be sharpened (choice of rays, or of stopping rule) so that its endpoint is never a crossing? Equivalently, for smooth totally geodesic V_0: does every Y_0-network reach a MERGE, or a MOV at a puncture?
- Note that MS6 for constant families (MS6_0, §1.4) requires a positive answer, or an argument that handles crossings differently.

### 4.3 Why I did not transport the Teichmüller rays to time t (a dead end, recorded)
The natural route to removing (NT\*) is to transport the marked ray segments g_s X_n of Proposition K by H_t, and to follow the marked Σ_i along them at time t. Continuity in s of the marked Σ_i-part, together with finiteness of the label set (Step 4), would then remove the ambiguity at twin junctions.

This breaks down for the following reason.
- The marking at H_t(g_s X_n) must be defined by lifting the square (s, τ) ↦ H_τ(g_s X_n) to Teichmüller space.
- The square can meet orbifold points of the moving surfaces V_τ. These are points with extra automorphisms, which (unlike at τ = 0) move with τ and sweep real hypersurfaces of V_0 under H^{-1}. So they cannot be avoided by perturbing the ray.
- The monodromy of the lift around such a point is an automorphism α of a curve close to the boundary. It can send Σ_i to a twin subsurface α(Σ_i). Its part is isomorphic at that moment, but it is continued by a *different* label afterwards.
- So the transported-ray argument meets exactly the twin problem again, now at interior times τ ∈ (0, t).
- Passing to level-N covers does not help. The pull-back to V_0 × Δ of the branched cover M_g[N] → M_g need not be a product, because its branch locus varies with τ.

---


### R7-3. Kuranishi-chart transport lemmas, (TR) without twins, the twin dichotomy, and a chart-local twin-jump model (from round7_q5, verbatim, sections 1–5)
## 1. Set-up: Kuranishi charts and chart components

**Standard facts (cited from memory).**

(K1) Let J be a stable curve. It has a universal deformation over a smooth germ Def(J), with smoothing parameters s_e for the nodes e ∈ E(G_J), and Aut(J) acts on Def(J). A neighbourhood of J in M̄_g is Def(J)/Aut(J). So the preimages in Def(J) of a point J′ near J form one Aut(J)-orbit.

(K2) Let x be a vertex of G_J, and let L_x := {s_e = 0 for every edge e at x}, a smooth subgerm. Over L_x the fibre curve has a component "x", deforming J_x. This gives a holomorphic map F_x : L_x → M_{g_x,n_x}. Its special points are labelled by the half-edges at x.

(K3) For σ ∈ Aut(J) and q ∈ L_x we have σq ∈ L_{σx}, and σ induces an isomorphism of fibre curves taking component x to component σx. Hence

 F_x(σq) ≅ F_{σ^{-1}x}(q)  (as pointed curves, after relabelling).

Throughout, "≅ Y" means isomorphic as an n_i-pointed curve up to relabelling. Equivalently, we compare images in the coarse space M_{g_i,n_i}/S_{n_i}, which is an analytic space. All identity-theorem arguments below take place there.

**Interpretation of the hypotheses of (TR).** "The c_m-limit along D^m and the c_{m+1}-limit along D^{m+1} are the same component of J_m (tracked by path markings)" is read as follows. There are lifts β̃^m, β̃^{m+1} ⊂ Def(J_m), through 0, of the relevant branches of ξ(D^m) and ξ(D^{m+1}) at J_m, and a vertex x_m of G_{J_m}, such that:
- c_m is the single chart vertex x_m along β̃^m;
- c_{m+1} is the single chart vertex x_m along β̃^{m+1}.

This is what continuity of the marking inside the chart gives. The merge at Q_0 is read the same way: there are lifts β̃^k, β̃^E ⊂ Def(Q_0) and a chart vertex x with c_k = {x} along β̃^k and x ∈ class(u) along β̃^E.

A constant vertex c has a smooth limit at J. So c corresponds to a single chart vertex with no contracted edges, and the branch lies in L_x.

## 2. Transport lemmas

**Lemma 1 (constant values are holomorphic; generic constancy).** Let D be a piece at time 0, D_t := H_t(D) its transport, and c a vertex of D's graph.
(a) If c is constant on D, then c is constant on D_t for every t. Its value φ_c(t) is a holomorphic function of t.
(b) If c is non-constant on D, then c is non-constant on D_t for all t outside a countable set.

*Proof.* (a) Constancy is L1. Fix p ∈ D. Then φ_c(t) = pr_c of a lift of H(p,t). This is continuous in t, because H is continuous and lifts through the finite map ξ can be chosen continuously along paths.

Let 𝓦 be the irreducible 2-dimensional analytic set of Lemma R0 (PR-D) for D. Then Γ := (pr_c, t)(𝓦) is an irreducible analytic set (Remmert), whose fibre over each t is finite by L1. So Γ is a curve, finite over Δ. A continuous function whose graph lies in such a curve is holomorphic off a discrete set, where the curve is locally a union of graphs, and hence everywhere by Riemann extension.

(b) Let C ⊂ 𝓦 be the analytic set where (pr_c, t) has rank ≤ 1. Suppose pr_c is constant on the fibre components over uncountably many t. Then C contains uncountably many fibre curves. A ≤ 1-dimensional analytic set contains only countably many of them, so C = 𝓦. By the rank theorem the image Γ is then an irreducible curve that is not contained in a fibre of t, so it is finite over Δ. Hence pr_c is constant on every fibre component, including at t = 0. ∎

**Lemma 2 (transport of a lifted branch in a fixed chart).** Let J ∈ closure(V_0) \ V_0 and J(t) := H_t(J). Let β̃ ⊂ Def(J) be a lifted branch at 0 of a piece D, where either J is a puncture of D, or J ∈ ξ(D) and β̃ is the lifted germ of D itself. Let x be a chart vertex such that a vertex c, constant on D, equals {x} along β̃. Then for |t| < ε there is a set Ñ ⊂ Def(J) × Δ_ε with the following properties:
- Ñ is a connected analytic set with Ñ ∩ {t = 0} = β̃ \ {0}, or β̃ itself in the interior case;
- for each t, closure(Ñ_t) contains a lift J̃_β(t) of J(t), and Ñ_t ∪ {J̃_β(t)} ⊂ L_x;
- F_x ≡ φ_c(t) on Ñ_t ∪ {J̃_β(t)}.

*Proof (puncture case; the interior case is the same with D's own lifted family).*

1. Let β be the image branch of ξ(D) at J. Then N := H((β \ {J}) × Δ_ε) is a topologically trivial family of punctured discs. By (R2), near J(t) we have closure(ξ(D_t)) ∩ Δ_{G_J} = {J(t)}, because closure(ξ(D)) \ ξ(D) is finite and H_t is a stratum-preserving homeomorphism.
2. Let Ñ be the connected component of the preimage of N in Def(J) × Δ_ε that contains β̃ \ {0}. The preimage of the analytic family of D is analytic (Lemma R0 and Remmert), and N is open and closed in it near (J,0). So Ñ is analytic. Ñ is a connected topological 4-manifold, being a cover of a punctured disc times a disc. Hence Ñ is irreducible: removing a singular set of real codimension ≥ 2 does not disconnect it.
3. The pinching pattern {e : s_e ≡ 0} is constant on the irreducible set Ñ. At t = 0 it contains every edge at x, so Ñ ⊂ L_x.
4. Fix once and for all an identification of the contracted graph with D's graph. This gives a holomorphic map from Ñ to ∏_w M_w. Its image is irreducible and meets the lift of D at t = 0. So it lies in the lifted family 𝓦 of D, and F_x = pr_c on Ñ. By L1 and Lemma 1, pr_c ≡ φ_c(t) on 𝓦_t.
5. Ñ_t → N_t = β_t \ {J(t)} is proper and finite (K1). So points of Ñ_t approaching J(t) accumulate at lifts of J(t). Pick one, J̃_β(t). It lies in L_x because L_x is closed, and F_x(J̃_β(t)) = φ_c(t) by continuity of F_x. ∎

**Remark.** The same proof applies when the vertex containing x along β̃ is a non-constant vertex u. Then the u-limit at J̃_β(t) is the curve obtained by gluing the chart components in class(u) at J̃_β(t). This is a puncture value f_u^t(p) of D_t, at the puncture of D_t lying over J(t). Moreover u is non-constant on D_t whenever class(u) contains a contracted edge: a constant smooth curve cannot have a nodal limit (Lemma C2 of PR-C).

**Lemma 3 (twist).** Let β̃, β̃′ be lifted branches at 0 ∈ Def(J), with transports Ñ, Ñ′ and lifts J̃_β(t), J̃_{β′}(t). Then for each t there is σ_t ∈ Aut(J) with J̃_{β′}(t) = σ_t J̃_β(t). Some single σ occurs for all t in a set T_σ that is uncountable, and in particular accumulates at 0.
Moreover σ_t^{-1}·closure(Ñ′_t) is a lifted branch of D′_t through J̃_β(t). Along it, the vertex containing a chart vertex y is the σ_t^{-1}-image of the vertex of Ñ′_t containing σ_t y.

*Proof.* The two lifts of J(t) lie in one Aut(J)-orbit by (K1). Aut(J) is finite, and a finite union of the sets T_σ covers the uncountable disc. Aut(J) preserves the preimage of closure(V_t). The last statement is (K3). ∎

## 3. Theorem A: (TR) holds without twins

**Hypothesis (NT).**
- For each junction J_m (m < k): every σ ∈ Aut(J_m) fixes the chart vertex x_m.
- At Q_0: every σ ∈ Aut(Q_0) fixes x.

A sufficient condition: no other component of J_m (respectively Q_0) is isomorphic to the x_m-component (respectively the x-component), as a curve with unordered special points.

**Theorem A.** Assume the hypotheses of (TR), L1, and (NT). Then:
- φ_{c_m} ≡ Y for every m;
- for all t in a disc around 0 minus a countable set, the transported piece E_t has a vertex u that is non-constant on E_t and a puncture p′ such that f_u^t(p′) has a component isomorphic to Y_t.

*Proof.*
1. **Junctions.** Fix m < k. Apply Lemma 2 at J = J_m to (β̃^m, c_m, x_m) and to (β̃^{m+1}, c_{m+1}, x_m). This gives
 F_{x_m}(J̃^m(t)) = φ_{c_m}(t) and F_{x_m}(J̃^{m+1}(t)) = φ_{c_{m+1}}(t).
 By Lemma 3, J̃^{m+1}(t) = σ_t J̃^m(t). By (K3) and (NT),
 F_{x_m}(σ_t J̃^m(t)) = F_{σ_t^{-1}x_m}(J̃^m(t)) = F_{x_m}(J̃^m(t)).
 So φ_{c_{m+1}}(t) = φ_{c_m}(t) for all small t, and both functions are holomorphic (Lemma 1). Hence φ_{c_{m+1}} ≡ φ_{c_m} on Δ by the identity theorem.
 By induction from φ_{c_1} = Y (since c_1 = i on ∂V_t), we get φ_{c_k} ≡ Y.
2. **The merge at Q_0.** Apply Lemma 2 at Q_0 to (β̃^k, c_k, x), and apply the Remark after Lemma 2 to (β̃^E, u). Then F_x(Q̃^k(t)) = Y_t.
 Let Q̃^E(t) = σ_t Q̃^k(t). The u-limit of E_t at the puncture over Q(t) is the gluing of the components in class(u) at Q̃^E(t). This class contains x, whose component is
 F_x(σ_t Q̃^k(t)) = F_{σ_t^{-1}x}(Q̃^k(t)) = F_x(Q̃^k(t)) = Y_t, by (NT).
 Q(t) is not in ξ(E_t), because H_t preserves strata and Q_0 ∉ ξ(E). So this limit is a puncture value f_u^t(p′).
3. **u is non-constant.** In the MERGE case, class(u) contains a contracted edge, and the Remark after Lemma 2 shows that u is non-constant on E_t for every t. In the puncture-MOV case (u = {x} along β̃^E), u is non-constant on E_0, so it is non-constant on E_t for all t outside a countable set, by Lemma 1(b). ∎

**Corollary A.** Combine Theorem A with chain steps 1–4 (which use L1, L2 and (O)). If Prop K's configuration at t = 0 satisfies (NT) and ends in MERGE or in puncture-MOV, then Y_t = Y_0 for all t.

Note that (NT) **fails** in the quintic example (PR-I). There P_0 = A–B–C with A ≅ C ≅ Y_0, and the symmetric chain has an automorphism exchanging A and C. That example is settled by a different, time-t Krull argument (see §5).

## 4. The twin case: a robust analysis

From now on we argue by contradiction and **assume Y is non-constant**. Let Φ be the finite family of holomorphic functions consisting of:
- Y;
- the φ_c for all pieces D at time 0 and all vertices c constant on D;
- the constant functions given by the (finitely many) components of the elements of the finite sets F(E_0,u) of L2.

Let Z ⊂ Δ be the countable set of t at which one of the following happens:
- two distinct functions of Φ take the same value;
- some vertex changes from non-constant to constant (Lemma 1(b)).

Call t ∉ Z *generic*.

**Lemma 4 (closedness of the Y-network at generic time).** Let t be generic, J ∈ closure(V_0) \ V_0, and let q ∈ Def(J) be a lift of J(t). Let β̃_t, β̃′_t be two transported lifted branches through q, i.e. sets of the form ρ·closure(Ñ_t) with ρ ∈ Aut(J). Let y be a chart vertex that is, along β̃_t, a single constant vertex c with φ_c ≡ Y. Let w be the vertex of the piece D′ of β̃′_t that contains y. Then one of the following holds.
- (a) w = {y} is a constant vertex of D′ with φ_w ≡ Y.
- (b) J(t) ∈ ξ(D′_t) is an interior point of D′_t, and w = {y} is non-constant on D′_t with pr_y(J(t)) ≅ Y_t. Call this *interior-MOV*.

In particular, (i) w never contains a contracted edge, and (ii) w is never a non-constant vertex at a puncture.

*Proof.*
- F_y(q) ≅ φ_c(t) = Y_t.
- Suppose w contains a contracted edge, or w is non-constant on D′_t with J(t) a puncture. Then Y_t is a component of a puncture value f_w^t(p), which lies in a finite set F(D′_0, w) by L2 (and L1). So Y_t equals one of the constant functions in Φ, which is impossible for generic t because Y is non-constant.
- Suppose w is constant. Then w = {y} (its limit is smooth) and φ_w(t) = Y_t. For generic t this forces φ_w ≡ Y.
- The remaining case is (b). ∎

**Theorem B (twin dichotomy).** Assume Y is non-constant. Let a junction J_m satisfy φ_{c_m} ≡ Y. Then:
- either φ_{c_{m+1}} ≡ Y;
- or there is σ ∈ Aut(J_m) with σ x_m ≠ x_m (a *twin jump*) such that, along the t = 0 branch β̃^{m+1}, the chart vertex σx_m is a single constant vertex c′ of D^{m+1} with φ_{c′} ≡ Y. The exception is an interior-MOV event at J_m.

Similarly, at Q_0: either the conclusion of (TR) holds for all generic t (impossible, since it forces Y_t into a finite set), or there is σ ∈ Aut(Q_0) with σx ≠ x such that, along β̃^E, σx is a single constant vertex of E with φ ≡ Y (again up to interior-MOV).

Hence, if Y is non-constant and there is no interior-MOV event, the Y-network performs at least one twin jump along the chain of (TR).

*Proof.*
1. Take t ∈ T_σ (Lemma 3) generic, q = J̃^m(t), β̃_t = closure(Ñ^m_t), β̃′_t = σ^{-1}closure(Ñ^{m+1}_t), and y = x_m.
2. Lemma 4 says the vertex of β̃′_t containing x_m is a Y-network constant. By (K3), that vertex is the σ^{-1}-image of the vertex of Ñ^{m+1}_t containing σx_m.
3. The pinching pattern and the vertex structure are constant along Ñ^{m+1}, so the same holds on β̃^{m+1} at t = 0.
4. If σx_m = x_m, this vertex is c_{m+1}, and φ_{c_{m+1}} ≡ Y.
5. At Q_0, run the same argument with β̃′ = σ^{-1}·(transport of β̃^E). If σx = x, the vertex containing x is u, which contradicts Lemma 4 (i)/(ii). ∎

**What a twin jump means.** At t = 0 the curve J_m has two components x_m ≠ σx_m, both isomorphic to Y_0 and exchanged by an automorphism. The marked track of Prop K continues along x_m into a constant vertex c_{m+1} with φ_{c_{m+1}} ≢ Y. The deformation, however, carries the Y-network on to the twin σx_m. For t ≠ 0 the automorphism σ no longer exists: J(t) has two different components φ_{c_m}(t) = Y_t and φ_{c_{m+1}}(t), which coincide at t = 0.

## 5. Why (TR) is not decided here: a local model and a t = 0 reformulation

**Local model (twin jump, consistent in the chart).**
- Let Def(J_0) contain coordinates (a, b) of the two Y_0-components x, y, with σ(a, b) = (b, a). Let J(t) have lifts J̃(t) = (t, −t, …) and σJ̃(t) = (−t, t, …).
- Suppose the transported D^m passes through J̃(t), with constant vertex at x of value Y_0 + t (= Y_t) and constant vertex at y of value Y_0 − t.
- Suppose the transported D^{m+1} passes through σJ̃(t), with c_{m+1} at x of value Y_0 − t, and a network vertex at y of value Y_0 + t.
- At t = 0 both branches pass through 0, and c_m, c_{m+1} both sit at x. So the hypotheses of (TR) at this junction hold.
- Lemma 4 is satisfied at every time, because D^m has a network vertex at y as well. Krull's theorem at time t gives no further constraint unless the global stratum structure is known, as in PR-I.

So no argument confined to the Kuranishi charts at the junctions can prove (TR). Any proof must use global information about how the marked Teichmüller track of Prop K sits relative to the deformation. Constructing an actual family V_t realizing this model is out of reach; I have **no counterexample**.

**How the quintic example escapes.** There the extra input is Krull at time t in Def(P_t) (PR-I Prop 3), together with the knowledge that every boundary branch near P_t lies over ∂V_t. This produces, at the same point q at time t, a branch with the opposite pinching pattern. Its network vertex lies inside the non-constant vertex of the first branch, which is the violation (ii) of Lemma 4. The general version of this observation: Krull at time t produces coherent pairs of branches (pairs through the same lift) with a prescribed pinched edge, but it does not control which pieces they belong to.

**A t = 0 statement that would suffice (MS7, open).** Call a set 𝒩 of pairs (D, c) — D a piece at time 0, c constant on D with value ≅ Y_0, containing (each component of ∂V_0, i) — **Aut-closed** if the following holds. For every J ∈ closure(V_0) \ V_0, every lifted branch β̃ at 0 ∈ Def(J) of some (D, c) ∈ 𝒩 with c = {x}, and every lifted branch β̃′ at 0 of any piece D′ through J, there is τ ∈ Aut(J) such that the vertex of D′ containing τx along β̃′ is a single constant vertex c′ with (D′, c′) ∈ 𝒩. (Interior points of D′ are included.)

- Lemma 4, transported to t = 0 as in Theorem B, shows: **if Y is non-constant and no interior-MOV event occurs, then the Y-network {(D, c) : φ_c ≡ Y} is Aut-closed.**
- So MS7 — "no Aut-closed set 𝒩 exists" — implies Y_t = Y_0, modulo the interior-MOV case.
- Prop K does not prove MS7. Its track follows the marking, which at a twin junction may continue along x_m rather than along σx_m (§4). If the track always stays inside 𝒩, Prop K does give a contradiction (Theorem A is the special case where this is automatic).


### R7-4. Time-t criterion, transport of branch patterns, total-merge transport, spreading of Y_t-copies (from round7_q2, verbatim, sections 0–4)
## 0. Notation used throughout

- B_t := closure(V_t) \ V_t. This is a compact analytic set of dimension ≤ 1. By (R2), H_t(B_0) = B_t, and H_t preserves strata.
- For a point Q ∈ B_0, put Q_t := H_t(Q).
- Def(Q) is the versal deformation germ of the stable curve Q, with smoothing parameters s_e, e ∈ E(G_Q). The group 𝔅 := Aut(Q) acts on Def(Q). The germ of M̄_g at Q is q : Def(Q) → Def(Q)/𝔅.
- On the locus {s_e = 0 for all e ∈ E(G_Q)} ≅ ∏_{x ∈ V(G_Q)} Def(Q_x), each point p has components comp_x(p), labelled by the vertices x of G_Q. Each comp_x(p) is a smooth curve carrying its special points, and it depends holomorphically on p.
- An element a ∈ 𝔅 acts on labels, and comp_x(a p) ≅ comp_{a^{-1}x}(p) as pointed curves.
- The fibre q^{-1}(Q) is {0}. Since q is proper, every lift of Q_t tends to 0 as t → 0.
- **Pattern.** For a point p of Def(Q) put S(p) := {e : s_e(p) = 0}. For S ⊂ E(G_Q):
  - an edge not in S is *unpinched*;
  - a vertex x is *intact* for S if every edge at x lies in S, and *merged* otherwise;
  - M(S) denotes the set of merged vertices.
- A *Y_t-copy* of a point P is a component of P that is isomorphic to Y_t as an n_i-pointed curve, in some order of its special points.
- C_0(Q) := {x ∈ V(G_Q) : comp_x(0) is a Y_0-copy}. This set is 𝔅-invariant.
- A *boundary branch* at Q is a local branch b at Q of B_0 with Q ∉ the stratum of b. Equivalently, Q is a puncture of the piece E_b that contains b.
  - A lift b̃ ⊂ Def(Q) has constant pattern S_b̃. The other lifts are the translates a b̃, with patterns a S_b̃.
  - M^+(b̃) := M(S_b̃) ∪ {x intact for S_b̃ : comp_x is non-constant along b̃}.

## 1. Lemma 1 (time-t criterion for MS6)

**Lemma 1.** Fix t. Suppose there are:
- a point P ∈ B_t,
- a lift P̃ ∈ Def(P),
- a Y_t-copy y of P̃,
- a lift c̃ through P̃ of a boundary branch c at P,

such that y ∈ M(S_c̃), or y is intact for S_c̃ and comp_y is non-constant along c̃. Then the MS6 configuration exists at time t.

*Proof.*
1. Let E be the piece at time t that contains c̃. Concretely, E is the irreducible component, in ∏_w M_w of the stratum Δ_{G_c}, of the lift of closure(V_t) ∩ Δ_{G_c} that contains the image of c̃. Here the stratum locus S_c̃ of Def(P) is mapped to ∏_w M_w by taking partial normalizations. This is compatible with ξ_{G_c}, after identifying G_P / (E(G_P) \ S_c̃) with G_c.
2. P is not in Δ_{G_c}. So the endpoint of c̃ corresponds to a puncture p of Ē.
3. Let u be the vertex of G_c that contains y. Then f_u(p) is the curve obtained by gluing the components comp_x(P̃), x ∈ u, along the unpinched edges between them.
   - comp_y(P̃) is an irreducible component of f_u(p).
   - Its special points in f_u(p) are its special points in P. A half-edge at y is either part of an unpinched edge inside u, which becomes a node of f_u(p), or a half-edge of a pinched edge, which becomes a marked point of M̄_u.
   - So it is a Y_t-copy.
4. **Case y merged.** f_u(p) has a node, so f_u(p) ∈ ∂M̄_u. On E the values of f_u lie in M_u. So f_u is not constant. This is Lemma C2 of PR-C.
5. **Case y intact.** u = {y}, and f_u = comp_y along c̃ is non-constant by hypothesis. In both cases (E, u, p) is an MS6 configuration at time t. ∎

**Remark.** The converse does not hold in the relevant sense. A configuration "Y_t-copy y at an interior point P ∈ E, with the vertex of E carrying y non-constant" (called **MOV-interior** below) is NOT an MS6 configuration. At an interior point there is no puncture, and the moving value lies on a curve, not in a finite set.

## 2. Lemma 2 (transport of branch patterns)

**Lemma 2.** Let Q ∈ B_0 and let b be a boundary branch at Q. Put N := H((b \ {Q}) × Δ) near (Q,0). Then:
- (a) the components of q^{-1}(N) ⊂ Def(Q) × Δ are permuted transitively by 𝔅, and the pattern is constant on each of them. So the components are the a Ñ, with patterns a S, where Ñ ⊃ b̃ has pattern S = S_b̃;
- (b) for every t and every lift Q̃_t of Q_t, some a Ñ has Q̃_t in the closure of its t-slice. For that a, the lift of the branch H_t(b) through Q̃_t has pattern a S;
- (c) the closure of N near (Q,0) is a union of irreducible 2-dimensional germs of an analytic set. The same holds for q^{-1}(N).

*Proof.*
(a) **Patterns are constant on components.**
- The sets {S(p) = S'} for distinct S' with isomorphic contracted graphs are pairwise disjoint.
- Each is relatively open in the union of all strata of that graph type, because a nearby point has fewer zero coordinates unless it is in the same stratum.
- So S(·) is locally constant on q^{-1}(N) ⊂ q^{-1}(Δ_{G_b} × Δ), and hence constant on each component.

**Transitivity.**
- q restricted to q^{-1}(N) is open and closed (finite quotient), and q^{-1}(N) is locally connected (semi-analytic). So each component maps onto N, which is connected: it is homeomorphic to a punctured disc times a disc.
- If Z_1, Z_2 were components with 𝔅Z_1 ∩ 𝔅Z_2 = ∅, take a point n ∈ N. Its fibre is a single 𝔅-orbit, and it would have to lie in both 𝔅Z_1 and 𝔅Z_2, a contradiction.

(b) Q_t ∈ closure(H_t(b)). Hence the closure of q^{-1}(H_t(b)) contains a point of q^{-1}(Q_t) = 𝔅 Q̃_t. By 𝔅-invariance it contains Q̃_t. Near Q̃_t the set q^{-1}(H_t(b)) is contained in ⋃_a (a Ñ)_t. Apply (a).

(c) **The set 𝒜.** Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ). It is analytic by (R1). Let 𝒵 be the part of 𝒜 over strata deeper than Δ_{G_b}; it is analytic.

**N is open and closed in 𝒜 \ 𝒵.**
- Near (Q,0), 𝒜 \ 𝒵 = H((closure(V_0) ∩ Δ_{G_b} ∩ U) × Δ) by (R2).
- For U small, closure(V_0) ∩ Δ_{G_b} ∩ U is a disjoint union of punctured branches at Q, since Q ∉ Δ_{G_b}.
- So N is open and closed in 𝒜 \ 𝒵.

**Conclusion.**
- Let X be an irreducible component of 𝒜 not contained in 𝒵. The set X minus (𝒵, Sing 𝒜, and the other components) is connected and dense in X.
- Hence the closure of a union of connected components of 𝒜 \ 𝒵 is a union of such X.
- Preimages under the finite map q of analytic sets are analytic. ∎

## 3. Theorem 3 (total-merge transport)

**Theorem 3.** Let Q ∈ B_0. Assume:
- (Y) there is a sequence t_n → 0, t_n ≠ 0, such that Q_{t_n} has a Y_{t_n}-copy;
- (TM) for every y ∈ C_0(Q) there is a boundary branch b at Q, with a lift b̃, such that 𝔅·y ⊂ M^+(b̃).

Then for all but finitely many n, the MS6 configuration exists at time t_n. In particular MS6 holds, with T = {t_n : n ≥ n_0} minus a finite set. T accumulates at 0 ∈ Δ.

Hypothesis (Y) holds whenever Q ∈ closure(∂V_0), as shown in the proof.

*Proof.*
1. **Hypothesis (Y) for Q ∈ closure(∂V_0).**
   - Q_t ∈ closure(∂V_t), because H_t commutes with closures and preserves Δ_Γ.
   - Take a branch of ∂V_t at Q_t, and lift it to Def(Q) through a lift Q̃_t. Along it, the vertex-i curve is the constant Y_t ∈ M_{g_i,n_i}.
   - In the chart, the vertex-i curve converges to the curve glued from the components over the contracted vertex. That curve is Y_t, which is smooth, so it is a single component (Lemma D(1) of PR-I; re-checked).
2. **Choice of a limit copy.** Fix lifts Q̃_{t_n} and Y_{t_n}-copies y_n.
   - Pass to a subsequence along which y_n = y is constant and the ordering of special points is fixed.
   - Q̃_{t_n} → 0, and comp_y is continuous. M_{g_i,n_i} is Hausdorff and Y_{t_n} → Y_0 (PR-A). So comp_y(0) ≅ Y_0, i.e. y ∈ C_0(Q).
   - Arguing by contradiction on subsequences, it suffices to show that MS6 holds at t_n for all large n in this subsequence.
3. **Applying (TM).** Take b, b̃ as in (TM) for this y.
   - By Lemma 2(b), at time t_n there is a lift of H_{t_n}(b) through Q̃_{t_n} with pattern a_n S_b̃, lying in a_n Ñ.
   - Pass to a subsequence with a_n = a. Then a^{-1} y ∈ 𝔅y ⊂ M^+(b̃).
4. **Case a^{-1}y ∈ M(S_b̃).** Then y ∈ M(a S_b̃): y is merged along the lift through Q̃_{t_n}. Lemma 1 gives MS6 at t_n. (Q_{t_n} ∉ Δ_{G_b}, because H_t preserves strata.)
5. **Case a^{-1}y intact, with comp_{a^{-1}y} non-constant along b̃.** Then y is intact for a S_b̃, and comp_y is non-constant along a b̃.
   - Let W̃ be any irreducible germ of closure(a Ñ) at (0,0) (Lemma 2(c)). φ := comp_y is holomorphic on W̃, because y is intact for the constant pattern a S_b̃.
   - t is non-constant on W̃, so W̃_0 has pure dimension 1 (Krull). Its components are lifts a′b̃ with a′S_b̃ = a S_b̃, and along each of them φ = comp_{a′^{-1}y} along b̃.
   - a′^{-1}y ∈ 𝔅y is intact for S_b̃, so it is not in M(S_b̃). Hence comp_{a′^{-1}y} is non-constant along b̃. So φ is non-constant on every component of W̃_0.
6. **Generic rank of Φ = (φ, t) on W̃ is 2.**
   - Otherwise every fibre of Φ has dimension ≥ 1 at every point (semicontinuity of fibre dimension).
   - The fibre of Φ through a point of W̃_0 \ {0} lies in W̃_0 ∩ {φ = const}, which is 0-dimensional there. Contradiction.
7. **Only finitely many bad times.**
   - The set Σ := {p ∈ W̃ : dim_p Φ^{-1}Φ(p) ≥ 1} is analytic (Cartan–Remmert, cited from memory). It is a proper subset, so dim Σ ≤ 1.
   - So only finitely many 1-dimensional components of Σ lie in t-fibres, and φ is non-constant on W̃_t for t outside a finite set.
   - There are finitely many germs W̃. So for large n, φ is non-constant along the lift through Q̃_{t_n}, and Lemma 1 (intact case) gives MS6 at t_n. ∎

**Corollary 3′.** If 𝔅 = Aut(Q) fixes every element of C_0(Q), then (TM) reads: every Y_0-copy of Q is merged, or is intact and moving, along some boundary branch at Q. Hence MS6 holds if some Q ∈ closure(∂V_0) with this property exists.

**How Theorem 3 relates to Prop K and to PR-I.**
- Prop K (PR-H) produces a MERGE or MOV branch at a point Q_0 for the *path-marked* copy x_0 only. In general:
  - (G1) Q_0 ∉ closure(∂V_0), so (Y) is not automatic;
  - (G2) other Y_0-copies at Q_0, or 𝔅-translates of x_0, need not be merged (TM fails);
  - (G3) the MOV branch may have Q_0 in its own stratum (MOV-interior), which is excluded from M^+.
- In the quintic example of PR-I (not smooth), at P_0 = A—B—C one has C_0 = {A, C}, branch β (S = {e_1}) with M = {B, C}, and branch β′ (S = {e_2}) with M = {A, B}.
  - If Aut(P_0) does not swap A and C, (TM) holds and Theorem 3 applies.
  - If it does swap them, (TM) fails, and one needs PR-I's Krull-at-time-t argument (Lemma D) instead.
- So Theorem 3 does not supersede PR-I's Theorem 4. It is a different sufficient condition.

## 4. Lemma 4 (spreading of Y_t-copies at a time t where MS6 fails)

Call a coarse piece D (an irreducible 1-dimensional component of closure(V_t) ∩ Δ_G) **MOV-blocked at P** if P ∈ D and no vertex of a lift of D that is constant along D takes a value at P isomorphic to Y_t.

**Lemma 4.** Fix t, and suppose there is NO MS6 configuration at time t. Let P ∈ B_t have a Y_t-copy, and let D be a coarse piece with P ∈ closure(D). Assume that either
- (a) P ∉ D, or
- (b) P ∈ D and D is not MOV-blocked at P.

Then some lift-piece E of D has a vertex u with f_u ≡ const ≅ Y_t, and every point of closure(D) has a Y_t-copy.

*Proof.*
1. **Case (a).** Lift a branch of D at P to Def(P) through a lift P̃ carrying a Y_t-copy y. This is possible by the argument of Lemma 2(b) at fixed t.
   - Since MS6 fails at t, Lemma 1 says that y is intact for the branch pattern, and that comp_y is constant along the branch.
   - So the vertex u = {y} of the lift-piece E containing the branch has f_u constant on a branch, hence on E by the identity theorem on Ē. Its value is comp_y(P̃) ≅ Y_t.
2. **Case (b).** The vertex given by the hypothesis is constant along D with value ≅ Y_t.
3. **Every point of closure(D) has a Y_t-copy.**
   - ξ_G(E) = D, since ξ_G(E) ⊂ D, both are irreducible, and ξ_G(E) contains a branch of D.
   - Every R ∈ closure(D) is ξ̄_G(ν(r)) for some r ∈ Ē, and the u-coordinate of ν(r) is the smooth curve Y_t ∈ M_u.
   - So R has a component ≅ Y_t, carrying the same special points as in the proof of Lemma 1. ∎

**Corollary 4′.** Let B_t^∂ be the connected component of B_t containing ∂V_t. Note B_t^∂ = H_t(B_0^∂). Suppose MS6 fails at t and no coarse piece in B_t^∂ is MOV-blocked at a point of B_t^∂. Then:
- every point of B_t^∂ has a Y_t-copy;
- every coarse piece in B_t^∂ has a lift with a vertex that is constant and ≅ Y_t.

*Proof.*
1. B_t^∂ is a finite union of closures of coarse pieces. A compact analytic set of dimension ≤ 1 has 1-dimensional irreducible components, each the closure of the piece of its generic stratum, together with isolated points. The component containing the 1-dimensional set ∂V_t is a union of the former, and their incidence graph (two pieces adjacent if their closures meet) is connected.
2. Start from the pieces of ∂V_t, whose vertex i is ≡ Y_t, and apply Lemma 4 along the incidence graph. ∎

**What Lemma 4 shows.** If MS6 fails, the Y_t-copies are never "lost" at a puncture. They can be lost only at MOV-blocked incidences, i.e. MOV-interior configurations. They can also be carried by a component different from the one at t = 0 (twins). Lemma 4 is purely a time-t statement and uses neither total geodesy nor L2.


### R7-5. L1 and L1′ (constancy persists) with the non-product caveat (from round7_q9, verbatim, section 1)
## 1. L1

Notation. G is a stable graph, and ξ̄ = ξ̄_G : ∏_w M̄_w → M̄_g is the gluing map. It is finite, and ξ̄ maps ∂(∏_w M̄_w) into strata deeper than Δ_G, since a boundary point of some M̄_w carries an extra node. Hence ξ̄^{-1}(Δ_G) = ∏_w M_w. On coarse spaces, ξ = ξ̄|_{∏M_w} : ∏M_w → Δ_G is the quotient by the finite group Aut(G) (standard; cited from memory). Aut(G) acts by permuting factors and relabelling marked points. In particular ξ is finite and open.

Put A := closure(𝒱) ∩ (Δ_G × Δ) and C := closure(V_0) ∩ Δ_G. By (R2), A = H(C × Δ).

### 1.1 Preliminaries

**(P1) closure(C) \ C is finite.** closure(V_0) is a compact analytic subset of M̄_g by (R1). The set C has dimension ≤ 1. Its 1-dimensional components are open dense subsets of irreducible compact curves, and each such curve meets the deeper strata (a closed analytic set not containing the curve) in finitely many points. The isolated points of C are closed. Since ξ̄ is finite, ξ̄^{-1}(closure(C)) = ξ^{-1}(C) ∪ (a finite set).

**(P2) The lifted family is analytic.** Put 𝓑 := (ξ̄ × id)^{-1}(closure(𝒱)) ∩ (ξ̄^{-1}(closure Δ_G) × Δ). It is analytic in ∏M̄_w × Δ by (R1). Put Z := ∂(∏M̄_w) × Δ, and let 𝓦_G be the closure of 𝓑 \ Z = (ξ×id)^{-1}(A).
- 𝓦_G is the union of the irreducible components of 𝓑 not contained in Z, so it is analytic.
- An irreducible component of 𝓑 minus a proper analytic subset stays irreducible. Hence the irreducible components of 𝓑 \ Z are the traces of these components.
- So the closure of any union of components of 𝓑 \ Z is analytic.
- 𝓦_G → Δ is **proper**, because 𝓦_G is closed in ∏M̄_w × Δ and ∏M̄_w is compact.

**(P3) Local purity.** Near a point of (C^{1} \ Sing) × {t}, where C^{1} is the 1-dimensional part, A is a topological 4-manifold. It is therefore pure 2-dimensional analytic there. Since ξ × id is finite and open, its preimage is also pure 2-dimensional there.

**(P4) Fibres of 2-dimensional components.** Let W be a 2-dimensional irreducible component of 𝓦_G.
- The coordinate t is non-constant on W, because every fibre of 𝓦_G → Δ has dimension ≤ 1: it lies in ξ̄^{-1}(H_t(closure C)), which is 1-dimensional plus a finite set.
- So every fibre W_t is either empty or of pure dimension 1. Fibres of a non-constant holomorphic function on an irreducible 2-dimensional space have pure dimension 1. By properness and the open mapping property, W_t is in fact nonempty for all t.
- By (P1), W_0 ⊂ ξ^{-1}(C) ∪ (finite set). Being pure 1-dimensional, **W_0 is a finite union of closures of pieces at time 0.**
- **Every piece E at time t is dense in a component of W_t for some such W.** Take a generic point x of E, i.e. not over Sing(C_t) and not on other pieces. By (P3), the germ of 𝓦_G at (x, t) is pure 2-dimensional, so E × {t} lies in the union of the fibres of the finitely many 2-dimensional components through nearby points. Since E is irreducible, E ⊂ W_t for one W. Then closure(E) is a component of the pure 1-dimensional set W_t.

### 1.2 L1 in the product case (proved)

Suppose G is of product type, so ξ is injective. By Lemma R0 (PR-D), the 2-dimensional components W are the 𝓦^{(a)}, and W_0 ⊂ 𝐂_0^{(a)} = closure(E_0^{(a)}). By (P4), W_0 is pure 1-dimensional, so **W_0 = closure(E_0)**. Likewise W_t = closure(E_t) with E_t = H_t(E_0): W_t contains the lift of E_t and lies in closure(E_t) ∪ (finite set).

**Lemma L1 (product case).** Suppose pr_u is constant on E_0, equal to Z_0 ∈ M_u. Then for every t, pr_u is constant on every 1-dimensional irreducible component of W_t; here W_t = closure(E_t).

This is the special case of L1′ below in which W_0 has a single component.

### 1.3 L1′ (all G, proved)

**Lemma L1′.** Let W be a 2-dimensional irreducible component of 𝓦_G, and u a vertex of G. Suppose pr_u is constant on each 1-dimensional component of W_0. Then for every t ∈ Δ, pr_u is constant on each 1-dimensional component of W_t.

*Contrapositive (the form used).* Let E be a piece at time t with E ⊂ W_t. If f_u is non-constant on E, then f_u is non-constant on some piece at time 0 contained in W_0.

*Proof.*
1. Let K_1, …, K_r be the components of W_0. The values z_j := pr_u(K_j) lie in M_u, not ∂M̄_u, because K_j is the closure of a subset of ∏M_w and pr_u is continuous.
2. **Affine neighbourhood.** M̄_u (coarse space) is projective (Knudsen–Mumford; from memory), and ∂M̄_u is closed. Choose a homogeneous polynomial vanishing on ∂M̄_u but at none of the z_j. Such a polynomial exists by prime avoidance applied to the homogeneous ideal of ∂M̄_u and the finitely many points z_j. Let U be the complement of its zero set in M̄_u. Then U is affine, U ⊂ M_u, and {z_j} ⊂ U.
3. **Small t.** pr_u(W_0) = {z_j} ⊂ U, and W → Δ is proper. So the set of t with pr_u(W_t) ⊄ U is the image of the closed set W ∩ pr_u^{-1}(M̄_u \ U) under a proper map. It is closed and misses 0, so pr_u(W_t) ⊂ U for |t| < ε.
4. **Compact curves in an affine set.** Each component K of W_t is a compact irreducible curve. Its normalization is a compact connected Riemann surface, and the coordinate functions of U are holomorphic on it, hence constant. So pr_u is constant on each component of W_t for |t| < ε.
5. **Fibre dimension.** Let Φ := (pr_u, t) : W → M̄_u × Δ, a holomorphic map of complex spaces. By the Cartan–Remmert theorem (upper semicontinuity of fibre dimension; from memory), R := {x ∈ W : dim_x Φ^{-1}(Φ(x)) ≥ 1} is an analytic subset of W. By step 4, R contains W ∩ {|t| < ε}, which is a nonempty open subset of the irreducible W. Hence R = W.
6. **All t.** Let K be a component of W_t and x a point of K on no other component of W_t. Near x, Φ^{-1}(Φ(x)) = (pr_u|_K)^{-1}(pr_u(x)), and this has dimension 1 at x. So the analytic subset (pr_u|_K)^{-1}(pr_u(x)) of the irreducible curve K contains a 1-dimensional germ, hence equals K. So pr_u is constant on K. ∎

*Remarks.*
- (a) This rank argument replaces "rank ≤ 1 on an open set, hence everywhere", which is awkward because M̄_u is singular.
- (b) The contrapositive follows from L1′ and (P4).

### 1.4 Why L1 as stated fails for non-product G

The lift of the irreducible family A^{(a)} can have an irreducible component W whose 0-fibre has several components σE_0, σ ∈ Stab(W) ⊂ Aut(G), while W_t is irreducible for t ≠ 0. Then pr_u ∘ σ = r ∘ pr_{σ^{-1}u}, with r a relabelling. So u can be constant on E_0 and non-constant on σE_0, and hence non-constant on W_t for t ≠ 0. Upstairs there is then also no homeomorphism Ē_0 → Ē_t. Nothing in (i), (ii), (R1), (R2) excludes this, since the topology of the finite cover W_t → C_t can change at t = 0.

Local model, ignoring global realizability: σ is the swap on ℂ², and W = {(x − y)^2 = t}. Then W_t (t ≠ 0) is a pair of lines swapped by σ, while W_0 is the diagonal. Combining this with a family in which the two branches over C_0 separate shows that the number of components of W_t can differ from that of W_0.

Indeed, W_0 is a single Stab(W)-orbit of components. Let K be a component of W_0. For generic x ∈ W_0, the point ξ(x) = ξ(k) for some k ∈ K, so x = σk with σ ∈ Stab(W). A component K′ therefore meets σK in infinitely many points, so K′ = σK. The orbit can have several elements.


### R7-6. The "continuity principle" (from round7_q1, verbatim, section 2). PLANNER WARNING: this argument has a suspected gap. Its Steps 4–5 assume that the markings obtained by transporting along τ ↦ H_{τt}(γ(s)) are coherent in s; but a 2-parameter family (s,τ) ↦ H_{τt}(γ(s)) generically meets the orbifold locus of M_g (curves with extra automorphisms) in isolated points, whose local monodromy is an automorphism that may exchange Σ_i with a twin subsurface (see R7-2 §4.3); also the chart sizes needed in (Tr) degenerate near junction points, so the choice of ρ is not uniform there. Do not use Theorem A of R7-6 without repairing this.
## 2. The continuity principle: tracking Σ_i through the interior

### 2.0 What is used from Proposition K (PR-H §3)

Notation: B_0 = closure(V_0) \ V_0. Σ_i ⊂ S_g is the subsurface of vertex i at a point P ∈ ∂V_0, and ∂Σ_i is its boundary multicurve. For a stable curve Z, a marked smooth surface X close to Z, and a multicurve m, write "m ⊂ N_X(Z)" if, in the marking of X, the curves of m are vanishing curves of Z. This is well defined for X in a versal-chart neighbourhood of Z, up to the local monodromy (twists about vanishing curves and Aut(Z)); that monodromy preserves N_X(Z) as a set. If moreover a subsurface Σ is a complementary region of N_X(Z) containing no other vanishing curve, write "Σ ↔ Z_x", where Z_x is the corresponding component of Z. The component is well defined up to Aut(Z), so its *class* is well defined.

Proposition K's proof (rays g_s X_n with path marking; continua K(δ_k, η_k) → K_0; endpoints Q_k → Q_0 on a branch b) provides the following. I did not re-verify Proposition K; its author lists it as "proved, modulo routine marking details".

**(K\*)** There are a compact connected set K_0 ⊂ B_0, a point P ∈ K_0 ∩ ∂V_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B_0 at Q_0, with the following property. For every ρ > 0 there are a path γ : [0,1] → V_0 with a continuous marking (a lift to T_g) and a point Q′ ∈ b \ {Q_0} with d(Q′, Q_0) < ρ, such that:
- (a) d(γ(0), P) < ρ, and in the marking of γ(0), Σ_i ↔ the vertex-i component of P;
- (b) for every s there is z ∈ K_0 with d(γ(s), z) < ρ, ∂Σ_i ⊂ N_{γ(s)}(z) and Σ_i ↔ a (smooth) component of z of class Y_0; for s = 1 one may take z = Q_0;
- (c) d(γ(1), Q′) < ρ, and either
  - **(MERGE)** some curve of ∂Σ_i is not in N_{γ(1)}(Q′), or
  - **(MOV)** ∂Σ_i ⊂ N_{γ(1)}(Q′) and Σ_i ↔ a component of Q′ of class ≠ Y_0.

(The paths are the ray segments for (δ_k, η_k) with k and then n large. In case (a) of Prop K, γ_e has extremal length δ_k > 0 at the endpoint, so it is not a vanishing curve of Q_k: this is (MERGE). Case (b) gives (MOV).) In the MOV case, Prop K's branch b lies in a piece E of some stratum G_b on which the Σ_i-vertex is non-constant. Call the MOV case **touching** if Q_0 ∈ Δ_{G_b}, i.e. Q_0 is an interior point of E, and **puncture-MOV** otherwise.

**Hypothesis (P′).** K_0 \ Sp is a finite union of open arcs (Sp is the finite set below), each inside a single piece D at time 0 (stratum G_D). Require: for every such D and every vertex w of G_D with π_w ≡ class Y_0 on D, w is fixed by Aut(G_D). This holds automatically if G_D is of product type (Remark 1.3).

**The special set Sp ⊂ K_0.** K_0 is a subcontinuum of the compact 1-dimensional analytic set B_0, which is topologically a finite graph. So K_0 is a finite subgraph after subdivision. Let Sp consist of:
- P and Q_0;
- the endpoints of the arcs;
- the singular points of B_0 lying in K_0;
- the isolated points of the sets B_0 ∩ Δ_G that lie in K_0;
- for each arc in a piece D: the points of K_0 ∩ closure(D) \ D, and the points of D ∩ K_0 at which some *non-constant* vertex u of D has a value of class Y_0. These are finitely many, because f_u : Ē → M̄_u is non-constant, so f_u^{-1}(finite set) is finite.

Sp is finite.

### 2.1 Two local facts

**(Ch) Chart lemma.** Let Z ∈ M̄_g and ε′ > 0. There is a neighbourhood U of Z with the following property. Let X ∈ U ∩ M_g be marked, and let Z′, Z″ ∈ U be such that, in the marking of X, ∂Σ_i ⊂ N_X(Z′) ∩ N_X(Z″), Σ_i ↔ Z′_{x′} and Σ_i ↔ Z″_{x″}. Then the classes of Z′_{x′} and Z″_{x″} are within ε′ of each other in M̄_{g_i,n_i}/S_{n_i}.

*Proof.* Work in a versal chart Def(Z) (smooth; M̄_g = Def(Z)/Aut(Z) locally) and lift X, Z′, Z″ into it. The vanishing curves of Z′ and Z″ are vanishing curves of Z, and collapse maps compose (X → Z′ → Z is isotopic to X → Z). So both Z′_{x′} and Z″_{x″} are deformations, inside Def(Z), of the stable curve Z_Σ obtained by gluing the components of Z that lie in Σ_i. The class of the Σ_i-part depends continuously on the point of the boundary stratum of Def(Z) where ∂Σ_i stays nodal (gluing is continuous). Shrinking U makes both classes ε′/2-close to the class of Z_Σ. ∎

**(Tr) Transport of vanishing data.** Fix t. By uniform continuity of H on the compact set closure(V_0) × {τt : τ ∈ [0,1]}, the following holds for each ε > 0: there is ρ > 0 such that d(X, z) < ρ (X ∈ V_0, z ∈ closure(V_0)) implies d(H_{τt}X, H_{τt}z) < ε for all τ.

Transport the marking of X along τ ↦ H_{τt}(X), a path in the interior. For ε small (charts around the compact set H({τt} × K_0)), the set N_{H_{τt}X}(H_{τt}z) is constant in τ. Indeed, H_{τt}z stays in one stratum by (R2), and near a stratum the vanishing multicurve of nearby marked surfaces is locally constant along continuous paths. Likewise "Σ_i ↔ a single component" persists in τ.

*Proof sketch of the last two claims (standard plumbing).* Near a point of Δ_G, surfaces close to the stratum have exactly the G-vanishing curves short, and these vary continuously along paths. ∎

### 2.2 Theorem A

**Theorem A.** Assume (R1), (R2), the problem's hypotheses, (K\*) and (P′). Then for **every** t ∈ Δ, the component of Q_t := H_t(Q_0) that corresponds to Σ_i (in the marking transported along H_t ∘ γ, for ρ small enough depending on t) has class Y_t.

*Proof.* Fix t.

**Step 1 (the finite set S_t).** Let S_t be the union of two sets:
- for every arc-piece D of K_0 and every vertex w of G_D with π_w ≡ class Y_0 on D_0: the value π_w(D_t). This is a single class, by L1 in the form of 1.1/Remark 1.3, which applies thanks to (P′). Put D_t := H_t(D_0).
- the classes of all components of H_t(z), for z ∈ Sp.

S_t is finite. It contains Y_t: the vertex i of the product-type stratum Δ_Γ is constant ≡ Y_0 on ∂V_0, and ∂V_0 ∩ K_0 contains P. If P is special, Y_t is a component class of H_t(P) = P_t ∈ ∂V_t; otherwise use the arc-piece ∂V_0 with w = i. Let 2ε′ be the minimal distance between distinct elements of S_t, or ε′ = 1 if S_t = {Y_t}.

**Step 2 (choice of ρ).** Cover the compact set K_t := H_t(K_0) by finitely many neighbourhoods U as in (Ch) for this ε′, and let λ be a Lebesgue number. Choose ε < λ/4, small enough also for (Tr), and then ρ by (Tr), with ρ < ε. Take γ, Q′ from (K\*) for this ρ.

**Step 3 (the class function).** For s ∈ [0,1], pick z_s ∈ K_0 as in (K\*)(b), with z_1 = Q_0. Put X_s := H_t(γ(s)), marked by transport, and Z_s := H_t(z_s). Then d(X_s, Z_s) < ε. By (Tr), ∂Σ_i ⊂ N_{X_s}(Z_s) and Σ_i ↔ a single smooth component of Z_s. Let c(s) be its class.

**Step 4 (c(s) ∈ S_t).**
- If z_s ∈ Sp, this holds by definition.
- Otherwise z_s lies on an arc in a piece D. Follow τ ↦ H_{τt}(z_s), which stays in Δ_{G_D}, together with τ ↦ H_{τt}(γ(s)).
  - By (Tr), Σ_i corresponds for every τ to a single component of H_{τt}(z_s).
  - Components at vertices that are Aut(G_D)-fixed are canonically labelled by vertices of G_D (Remark 1.3). At τ = 0 the component is of class Y_0, at a vertex w of D. Since z_s ∉ Sp, w is not a non-constant vertex with value Y_0 at z_s, so π_w ≡ Y_0 on D_0. By (P′), w is Aut(G_D)-fixed. So the label w is canonical at every τ.
  - The correspondence "Σ_i ↔ label w" is locally constant along the continuous path, by working in charts with canonical labels. So at τ = 1, Σ_i ↔ the w-component of Z_s, and c(s) = π_w(D_t) ∈ S_t.

**Step 5 (near-continuity).** Let s, s′ be close enough that d(X_s, X_{s′}) < ε. The marking of X_{s′} is the continuation of that of X_s along the short path. Then X_s, Z_s, Z_{s′} all lie in the ball of radius 3ε < λ around Z_s. That ball lies in one chart U of (Ch), and U also contains X_{s′}. Move the marking from X_{s′} to X_s inside U: the local monodromy preserves the correspondences. By (Ch), d(c(s), c(s′)) < ε′.

**Step 6 (conclusion).**
- c(0) = Y_t. Indeed, by (K\*)(a) and (Tr), Σ_i ↔ the vertex-i component of H_t(z_0) near P_t. This component is labelled canonically in the product-type Δ_Γ (Remark 1.3), or z_0 is special with the same conclusion, and vertex i is constant ≡ Y_t on ∂V_t. Strictly, z_0 can be any point near P. By Step 4 applied with D = ∂V_0 (or z_0 special), c(0) is the vertex-i value Y_t.
- The values c(s) lie in the finite set S_t, and values at nearby parameters differ by less than ε′, which is at most half the gap. Covering [0,1] by finitely many short intervals, c is constant.
- Hence c(1) = Y_t. And c(1) is the class of the component of Q_t = Z_1 corresponding to Σ_i. ∎

**Why twins do no harm here.** Suppose a point of K_t carries several components of class near Y_0 (twins at t = 0 that separate at t ≠ 0). The class c(s) is still determined by the *specific interior path* H_t ∘ γ, and it can change only continuously. A swap at a junction would have to be a jump between two distinct elements of the finite set S_t, which near-continuity forbids. (Loops in V_0 whose monodromy exchanges twins are transported by H to loops with the same monodromy. At time t that monodromy is realised by an automorphism of the transported boundary point, so the twins there stay isomorphic. This is consistent with the above.)

---


## A suggested mechanism (the planner's sketch; you are free to discard it)

**Why it should hold (my sketch).**
1. Suppose Y is non-constant. Generic t avoids the countable set Z of times at which:
   - Y_t is a component of an element of F;
   - Y_t lies in a 0-dimensional intersection of two curves of 𝒦 (projected to factors of type (g_i,n_i));
   - Y_t = φ_c(t) for a constant-vertex value function φ_c ≢ Y (these are holomorphic, round7_q5 Lemma 1).
2. At generic t no Y_t-copy merges or moves at a puncture (entry 57 + F). So every copy along every branch is STAY or IMOV.
3. **IMOV at generic t, at Q_t ∈ E_t, moving vertex x.**
   - Suppose some other y ∈ M(E) has its Q_t-component inside a merged or puncture-moving vertex of an adjacent piece. Then pr_{M(E)}(Q_t) ∈ K(E) ∩ {y-coordinate ∈ finite set}, which is finite. So Y_t is in a finite set: impossible at generic t.
   - Otherwise H_t^{-1}(Q_t) = Q_0 is a *pure crossing* of V_0: every moving vertex of E is intact and constant along the adjacent STAY piece D.
   - Exclude pure crossings by total geodesy. Near Q_0, Minsky's product-region theorem makes V_0 coarsely a product (Teichmüller disc in M_x) × (cusp of the D-plumbing). Total geodesy forces the Teichmüller discs in mixed directions to stay in V_0. The aim is to contradict uniqueness of Teichmüller geodesics, the non-existence of isometric bidiscs (Antonakoudis), or Lemma PA's area localisation in mixed directions.
4. **Without IMOV.** N_t ⊇ C_t = H_t(C_0), and ALL Y_t-copies of every point of C_t stay along all branches.
5. **Twin step.** Let J be a junction of Prop K's network, and σ ∈ Aut(J) move the tracked copy x.
   - (a) If x and σx stay isomorphic for t near 0 (Lock), the merged copy at the end is a Y_t-copy, contradicting step 2.
   - (b) If not, the twin jump needed to escape requires orbifold points of V_τ near J with automorphism ≈ σ (round7_q8 §4.3). These are σ-fixed points of the Aut(J)-invariant lifted family 𝓛 ⊂ Def(J) × Δ. Their absence makes the interior-path continuity principle (round7_q1 §2) valid near J. Their presence should force a σ-symmetric boundary point near J_t, i.e. Lock again.
6. So the Prop K track stays among the copies of type Y, and its MERGE or puncture-MOV terminal contradicts step 2.


## Reminder
- The target is MS8 exactly as stated, for every admissible V_0 and family satisfying (Rig). Arguing by contradiction (assume t ↦ Y_t non-constant, work at "generic" t outside a countable set) is allowed and encouraged: MS8 needs no statement at t = 0 when Y is constant.
- Never assume V_t totally geodesic for t ≠ 0. Total geodesy is available only at t = 0; information reaches t ≠ 0 only through (R1), (R2), (Rig), L1′, Krull-type local arguments at time t, and analytic continuation in t.
- The two known obstacles: twins (several components ≅ Y_0 at a boundary point, exchanged by automorphisms that may disappear for t ≠ 0; R7-2 §4.1 and §4.3, R7-3 §4–5) and crossings / interior-MOV (R7-2 §4.2). A proof must handle both, or show one cannot occur for smooth closed totally geodesic V_0.
- Beware: limits of Teichmüller discs asserted to be Teichmüller discs without proof; "area leakage" into collars; claims that a merge must exist derived from purely local analysis (impossible: PR-C, R7-2 §4.2); path markings transported through orbifold points (R7-2 §4.3).
- Begin your answer with a plan/status line, and end with a clear list: proved / not proved / open.
