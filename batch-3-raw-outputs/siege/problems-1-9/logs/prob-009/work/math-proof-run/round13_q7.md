kind: attempt
Open question attempted: the run's missing statement MS11♭ (OPEN, ledger entry 124, locator round12_plan). Its core, the twin problem at non-product puncture points, has been attacked in rounds 8–12 under several wordings. So this query gives you only the statement and the statements of the results it is meant to be combined with: no proofs and no planner's sketch.

## Task
1. Derive for yourself, from the statements listed below (and only those, plus standard facts you cite), that MS11♭ together with (Rig) (entry 82) would give the problem's claim.
   - Write the derivation step by step.
   - If it does not go through, or if MS11♭ looks implausible to you, say so precisely and explain why. The run will act on that result.
2. Then attack MS11♭: prove it, or refute it exactly as stated.
   - Use a FIRST MOVE that none of the approaches under "Approaches already tried" used, and name it at the start.
   - Moves that the table shows are tried include: Mechanism D/G (3-fold components and lift-curves), the Φ-reformulation, twin-free walks, counting, level structures, arithmetic, Douady deformation theory, Krull linkage, lift-curves in the stratum chart.
   - Moves not yet tried include, for example:
     - degenerating the Teichmüller discs of V_0 that pass near Q and comparing their limits on the two sides of a boundary curve;
     - holomorphic sections and residues of the norming quadratic differentials along the boundary of closure(V_0) at Q;
     - an intersection-number or degree argument on the compact surface closure(V_t) using the twin components;
     - deformation of the admissible-cover or multi-scale structure at Q.

     You are not limited to these.
- A proof for only some of the cases MS11♭ covers does not answer the question; report it as partial if that is all you find. This includes:
  - a sub-class of points Q, surfaces V_0, families, labels or branch pairs;
  - an extra hypothesis such as (R2^orb), "no twins" or "a single lift-curve".
- Note: MS11♭ contains "Y non-constant". So under (Rig) it is equivalent to the problem's claim (vacuous if the claim holds), and a counterexample to it is a counterexample to the problem.
- Purely chart-local arguments are known to be insufficient.
- Begin with a short plan/status line. End with an explicit list: proved / not proved / open.

## The missing statement MS11♭ (verbatim from the run's summary)
**Missing statement (MS11♭)** (OPEN, this round's block, locator round12_plan; replaces MS11 = entry 109).
- *Setting.*
  - g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i) and (ii) in the readings (R1), (R2), with H_0 = id. V_t is not assumed totally geodesic for t ≠ 0, and H_t need not preserve automorphism groups.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type, ∂V_t has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - (Rig) holds: there is a finite set 𝒦 of triples (G, M, K) with M ⊂ V(G) and K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G).
  - **t ↦ Y_t is non-constant.**
- *Data.*
  - Q ∈ B_0 := closure(V_0) ∖ V_0 in a stratum Δ_{G_Q} NOT of product type.
  - B ⊂ Def(Q) a small Aut(Q)-invariant ball (irreducible components of q^{-1}(closure V_0) ∩ B, of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) and of every closure(Ñ_c̃) are the components of the germs at the origin; distinct lifted branches of q^{-1}(B_0) meet only at 0), ε > 0 small.
  - Two DISTINCT lifted branches β̃ ≠ b̃ through 0 of branches β, b of B_0 at Q (possibly lifts of the same coarse branch) with
    - (P) Q is a puncture of the piece of β and of the piece of b (some s_e ≢ 0 on β̃, and likewise on b̃);
    - (S) β̃ and b̃ lie in one irreducible component S of q^{-1}(closure V_0) ∩ B.
  - A label x of G_Q with F_x(0) ≅ Y_0 that is Y-persistent on some anchored sheet of β̃.
- *Conclusion.* x is Y-persistent on some anchored sheet of b̃ (hence, at t = 0, x is intact along b̃ with F_x ≡ Y_0).

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.


**Definitions** (as in earlier rounds).

**Definitions** (as before, plus anchored sheets).
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w; M(E), K(E) as before.
- *Chart at Q*: Def(Q) with plumbing coordinates s_e, N := ∏_e s_e, q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g. *Labels* = vertices of G_Q; x intact at p if s_e(p) = 0 for every edge e at x; then F_x(p) is that component with its special points.
- *Transport family* Ñ_c̃ of a lifted branch c̃ of a branch c of B_0 at Q: the connected component containing c̃ ∖ {0} of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε).
- *Anchored sheet* of c̃: an irreducible component T of closure(Ñ_c̃) (in B × Δ_ε, germ at (0,0)) with c̃ × {0} ⊂ T.
- *x is Y-persistent on T*: at every (p,t) ∈ T, x is intact at p and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).
- *Lift-curve*: an irreducible component of {(p,t) : q(p) = Q_t}, Q_t := H_t(Q).
- *Product-type stratum*: ξ_G injective on coarse spaces.
- Older spliced files use "transport sheet" for any irreducible component of closure(Ñ_c̃) and sometimes "Y-persistent along b̃" for the whole family; both older notions are superseded: the chain and MS11♭ use anchored sheets. *Boundary-type* sheet: its generic pattern is not all of E(G_Q), i.e. Q is not in the stratum of its branch. P(T) := the set of labels Y-persistent on T; C(L) := the set of labels y with F_y ≅ Y_t along a lift-curve L.

## Statements of the run's results you may use (ledger lines, verbatim; proofs exist in the run but are not given here)
2. PROVED: Under the reading that closure(𝒱) in M̄_g×Δ is analytic with fibre over t equal to closure(V_t), the map t -> Y_t is a holomorphic map Δ -> M_{g_i,n_i} (graph of a continuous map that is an analytic set / Remmert proper image) — round1_q4
5. PROVED: If every V_t were totally geodesic, the claim would follow from countability of totally geodesic subvarieties (via Wright's correspondence with orbit closures and Eskin–Mirzakhani–Mohammadi countability, cited not reproved) — round1_q1
14. PROVED: Pinning lemma — if a deeper point P_t ∈ closure(∂V_t) ∩ Δ_{G'} (Y-vertex intact) is continuous in t and lies on closure(E_t) for a 1-dim boundary piece E_t with closure(E_t) = closure(E_0) for all t, then Y_t = Y_0, and by (ii) the incidence persists when P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} lying in closure(E_0) — round3_q1
19. PROVED: Repaired proof of entry 2 — A = closure(𝒱)∩(Δ_Γ×Δ) has pure dimension 2, local holomorphic sections over Δ off a discrete set plus continuity from (R2) and removable singularities make t ↦ Y_t holomorphic (the original properness argument had a gap) — round4_q3
23. PROVED: Hypothesis (ii) is vacuous or tautological for every pair (Δ_G, Δ_Γ) with G a contraction of Γ, so (ii) has content only at isolated points of deeper strata — round4_q2
24. PROVED: Under (R2) incidences transport automatically: for a boundary piece E_0 and P_0 ∈ closure(E_0) ∩ closure(∂V_0), P_t = H(P_0,t) lies in closure(E_t) ∩ closure(∂V_t), is continuous in t, and has vertex-i component Y_t — round4_q7
25. PROVED: At every cusp of closure(∂V_t) there is a further boundary branch b of closure(V_t) pinching an extra edge, and if b has the merge property then the merged projection π_v(E) is a curve whose limit at the cusp has vertex-i component Y_t — round4_q7
45. PROVED: Lemma PA — at a generic point of any 1-dim boundary piece E of closure(V_0)∩Δ_G (product type), norming differentials of tangent vectors of V_0 have full-area limits supported on the vertices of maximal Teichmüller speed along E, so some vertex has positive area and the constant vertex i of ∂V_0 has none — round6_q9
48. PROVED: Krull pinning (Lemma D, Pinning Lemma, Theorem 4) — at each time t every node of a point of closure(∂V_t)\∂V_t is kept along some boundary branch, ∂V_t-branches have a clean vertex ≅ Y_t, and if near P_0 the boundary is only ∂V_0∪{P_0} and condition (Tw2) holds with Lemma R for the host vertex, then Y_t ≡ Y_0 — round6_q6
54. PROVED: L1 holds for pieces in product-type strata (and for Aut(G)-fixed vertices), and L1′ holds for every stratum: if pr_u is constant on every component of the 0-fibre of an irreducible lifted family W then it is constant on every component of every fibre W_t — round7_q9
57. PROVED: Time-t criterion — at any t, a merge of any Y_t-copy along a boundary branch, or an intact moving Y_t-copy along a branch whose piece has the point as a puncture, yields the MS6 configuration at t; if it fails at t, every copy along every branch STAYs or moves at an interior point (IMOV), and absent IMOV the boundary points with a Y_t-copy form a union of connected components of B_t — round7_q6
70. PROVED: (F2) holds in general form (Theorem F2*), Lemma T′ is repaired, and Theorem TV holds: every 1-dimensional boundary piece of closure(V_0) in every stratum has a vertex j with π_j∘ν a proper orbifold covering of a Teichmüller curve whose universal-cover lift is the Teichmüller disc, and every end of the piece maps to a cusp (Lemma PA quoted) — round8_q10
71. PROVED: Lemma U — under (R1),(R2),(Rig) each 2-dimensional component W of each lifted boundary family has one moving set M_W and one image curve K_W for all components of all fibres at all times, so every piece is K_W × {point} — round8_q2
72. PROVED: Generic-time trichotomy — under (R1),(R2),(Rig) with Y non-constant, outside a discrete set of t no Y_t-copy anywhere merges or moves at a puncture, every copy along every branch STAYs or moves at an interior point, and every such interior move is a pure or shared crossing — round8_q2
74. PROVED: Theorem 2V — under (R1),(R2),(Rig), Y_t ≡ Y_0 whenever some cusp of ∂V_0 satisfies (Tw1),(C1),(C2), in particular when Γ has two vertices and near one cusp the boundary of closure(V_0) is only ∂V_0 plus the cusp — round8_q4
80. PROVED: Lemma Red (reduced central fibre), Lemma P0 (which vertices degenerate at a puncture is t-invariant) and Theorem B ((Rig) for a piece whose Teichmüller-vertex map is birational, under (Σ-fixed)) — round8_q9
81. REFUTED: Piece-level (Rig) — for holomorphic families of maps of a piece with fixed Teichmüller vertex, trivial source, fixed punctures and (O) for that vertex, the joint image curve (Example Z) and the puncture values of non-constant vertices (Example Z′) need not be t-independent (realisability by an admissible V_t unchecked) — round8_q9
82. OPEN: (Rig) holds for every admissible family — (F2) is now proved (entry 70), it still needs (O_G) for every piece and L2′, and by entry 81 it cannot be derived from piece-level data alone — round9_plan
84. PROVED: Theorem X*/X′ — for a piece E in a product-type stratum and Q_0 ∈ E, every boundary curve through Q_0 of any sheet of closure(V_0) containing a branch β of E lies over β, for any normal singularity and with no Q-Cartier hypothesis (proved independently in round9_q3 §1 by a pole function and the maximum principle) — round9_q4
85. PROVED: Proposition K_w — from a generic point of ∂V_0 a single Teichmüller ray yields a walk chain (pieces from ∂V_0, transition points with a common chart vertex and continuous lifted interior paths inside a small chart ball, endpoint MERGE or MOV), every transition having its two branches in a common sheet, while the K_0-chain reading (TD_J) of Proposition K is unsupported (modulo the cited inputs of PR-H) — round9_q4
86. PROVED: Lemma PT — in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type, so twins occur only at non-product points; with Lemma SS/Cor. SS′ and Theorem X′, an interior-MOV endpoint never lies in a product-type stratum, the chain lies in the persistent network (Prop. CN), and the Count lemma holds — round9_q3
87. PROVED: Lemmas T, S, J and Theorem R — under (R1),(R2),(Rig), H sends each piece into one global and local component of the boundary total space, M and K and persistence are constant on whole components, the junction trichotomy pinned/persistent/crossing holds, and Y_t ≡ Y_0 if the track is aligned at every junction and at Q_0 with terminal MERGE or puncture-MOV — round9_q7
89. PROVED: Every transport family contains a whole lift-curve of Q_t so star coherence is all-or-nothing in t, both families at a junction lie in the track's 3-fold component, and Proposition 4 gives the t=0 structure forced by a counterexample — round9_q2
90. PROVED: Under the extra readings (R3),(T4), Theorems A/B of round8_q5 hold with (U_J) weakened to (U″), so only relevant α-fixed components of dimension ≥2 can cause a twin jump; Lemma TG (a totally geodesic sheet meets Fix(h) in itself, a Teichmüller disc, or points) and the boundary-trace trichotomy hold — round9_q5
91. PROVED: The lifts of J_t in the track's 3-fold component form one orbit of Γ = Stab(𝒞°), both transport families lie in it, and no twin jump occurs when Γ = Γ_x·Stab_Γ(j̃(t)) (e.g. under (IP_Γ) or (NT_Γ)) — round9_q6
92. PROVED: At a twin jump the partner copy at the same lift carries the other value function and is frozen, persistent or a crossing on the incoming piece, the merging copy of an endpoint twin is frozen, and a coherent MERGE/pMOV endpoint freezes the tracked function — round9_q8
97. PROVED: Theorem X*_all — for a piece E in ANY stratum (product type not needed) and Q_0 ∈ E, every irreducible component of the germ of q^{-1}(closure V_0) at 0 ∈ Def(Q_0) that contains a lift β̃ of a branch of E meets {∏ s_e = 0} near 0 only in β̃ (independent second proof in round10_q2 §3, Theorem X**) — round10_q1
98. PROVED: Proposition K_w holds after repairs (R-a)–(R-d) (extra smallness conditions, canonical chart lifts through augmented Teichmüller space, recurrent transition types with per-transition witnessing path sequences), and Lemma S̃′: the entering and leaving (or terminal) lifts of each walk-chain transition lie in one irreducible component of q^{-1}(closure V_0) ∩ B, with no reading beyond (R1),(R2) — round10_q10
99. PROVED: Cor. IMOV_all — by entry 97 and the common component of entry 98 (or Lemma 1SS of round10_q1 under reading (T4)), a walk-chain transition point lying in the stratum of either adjacent piece has equal entering and leaving lifts, so in every stratum the endpoint and every genuine transition are punctures of both adjacent pieces, and junction crossings, interior-MOV endpoints and turning twins do not occur — round10_q1
102. PROVED: Incidence propagation (every transport sheet contains a lift-curve; P(T) = Λ(λ) for boundary-type T ⊃ λ under (Rig) with Y non-constant), the counting no-go (every conserved count is Γ-equivariant and consistent with a failure), and Theorem Q (two boundary-type sheets on a common 3-fold component of 𝒳 on which one is set-theoretically principal share a lift-curve, or give a same-branch crossing) — round10_q7
103. PROVED: Logical status of the twin statement — given the chain, any counterexample to MS10 is a counterexample to the problem under (Rig), MS10 is equivalent to its restriction to walk-chain data, and for a σ-stable twin sheet MS10 is equivalent to the problem for that V_0 (round10_q8 Prop. T) — round10_q4
105. PROVED: Lemma 3.1 — if Q is isolated in B_0 ∩ Δ_{G_Q} and Y is non-constant, then Q ∉ closure(V_τ) for τ outside a discrete set, and (conditional on cited McMullen/Möller rigidity) a case-(A2-disc) failure cannot come from an equisingular deformation of the Teichmüller curve — round10_q3
106. PROVED: Lemma D3 — if α ∈ Γ ∖ KΓ_x fixes pointwise a 3-dimensional component of the germ of 𝒳 at (0,0), then every V_τ lies in the symmetric locus M_g([α]) and the twins x, αx are locked on that component — round10_q6
107. PROVED: Lemma CD — for a piece's lifted family, {t : K^M_t ⊂ C} is all of Δ or discrete, so (Rig) for a piece holds iff its joint image lies in a countable class of curves for uncountably many t, and the goal holds if V_t is totally geodesic for uncountably many t (countability cited) — round10_q9
110. REFUTED: Lemma B1(a),(b) of round10_q3 (every component of a transport family Ñ_b̃ has t = 0 slice open in b̃ ∖ 0, and Stab_pt(b̃) permutes its components transitively) is false, by explicit chart-level models in which a component of closure(Ñ_b̃) meets {t = 0} only in another lift a·b̃, so MS11 as worded does not imply MS8 — round11_q9
112. PROVED: Lemma B1♭ with the Gap A repair — anchored sheets of c̃ (components of closure(Ñ_c̃) containing c̃ × {0}) exist, contain every germ component of the transport family at a generic point of c̃, form one orbit of the pointwise stabiliser of c̃, every component of closure(Ñ_c̃) is a·T for an anchored sheet T and a ∈ Aut(Q), and adding the finite sets R(D) to Σ keeps the walk's label on one lifted curve — round11_q9
113. PROVED: Chain check — with "transport sheet" read as "anchored sheet" (MS11♭), steps 2(b)–(d) hold (Lemma S̃′ supplies Theorem X*_all's hypothesis without (T4); IMOV_all at all transitions, R(D)-points and the endpoint; base; product-type junctions with anchored output; transfer; both endpoints), so MS11♭ + entries 19, 24, 84–87, 97–99, 112 imply MS8 — round11_q9
114. PROVED: Every transport sheet contains a lift-curve, and under (Rig) with Y non-constant the labels Y-persistent on a boundary-type sheet are exactly the Y_t-copies along any lift-curve in it, so MS11♭ can fail at Q only if Q_t has at least two lift-curves (|Aut(Q_t)| < |Aut(Q)|), and it holds at every point under the orbifold reading (R2^orb) — round11_q4
115. PROVED: Mechanism D — for an irreducible 3-fold component X ⊃ S × {0} of q^{-1}(closure 𝒱), D = X ∩ {∏ s_e = 0} is pure 2-dimensional, its components are anchored sheets of boundary type (via Theorem X*_all), it contains anchored sheets of β̃ and b̃, and its sheet graph is connected (Grothendieck connectedness, cited) — round11_q3
116. PROVED: Label transport in D — across a shared curve not in {t = 0} the persistent label set passes unchanged except in configuration (γ°) (T′ = gT with g fixing the curve pointwise and a persistent IMOV of a Y_t-copy at points tending to Q), and across a shared t = 0 branch c̃ one has T′ = σT with σ ∈ Stab_pt(c̃), so MS11♭ fails only through (γ°) or a label-moving composite of such twists (including the initial twist in Stab_pt(β̃)) — round11_q3
117. PROVED: Twin-free closure — under (R1), (R2), (Rig) with Y non-constant, every piece reachable from ∂V_0 by puncture transitions has a constant vertex with value ≡ Y, so Y_t ≡ Y_0 whenever some reachable piece has no constant vertex ≅ Y_0 or the V_0-only condition (TF) holds at some point — round11_q4
118. PROVED: Rigid twin — if MS11 fails at a MERGE or puncture-MOV endpoint, then for every t the cusp Q_t has a component ≅ Y_t and a different component frozen at Y_0, exchanged at t = 0 by an automorphism of Q — round11_q1
119. PROVED: Label-moving (β)-twists inside one 3-fold component are realised by chart-level models satisfying (R1), (R2), (i), (ii) with V_t coarse-smooth, so MS11♭ cannot be proved by arguments local to the 3-fold — round11_q7
120. PROVED: Lemma HQ (points of closure(V_0) isolated in their stratum move holomorphically under H_t), Prop. MP/MP′ (psh-isolation of an image curve or of closure(V_0) implies (Rig) or the goal) and Prop. DP (type-(0,5) Teichmüller curves move in pencils, so no such criterion holds there) — round11_q10
121. PROVED: The claim holds when [closure(V_0)] is an isolated point of the Douady space, and Lemma TR: under orbifold transport (OT) the Teichmüller-vertex map of every product-type piece is independent of t — round11_q6
Further statements recorded at round 13 (ledger lines 125–137, verbatim):
125. PROVED: Lemma J0 with Lemmas CS/CL — at t = 0 the whole vertex map of every piece in every stratum lifts holomorphically to T_G over the Veech orbifold H/Λ_E, with isometric Teichmüller coordinate and coset-valued monodromy, so Example Z is not a boundary piece of a totally geodesic V_0 (TV/Φ̂ of round8_q10 used as stated) — round12_q9
126. PROVED: Theorem RO — under (R1), (R2) and the orbifold reading (R2^orb) (a Mod_G-equivariant, isotropy-preserving lift of H on every boundary stratum, round12_q9 §1), (Rig) holds for every piece in every stratum with M(E_t), K(E_t) constant and puncture values in a fixed finite set (Imayoshi–Shiga finiteness and Thurston/Royden/Bers cited from memory) — round12_q9
127. PROVED: Proposition C — under the coarse reading (R2), (Rig) follows from the transport hypothesis (T_c) (the joint vertex map of E_t lifts over the transported Λ_E orbifold with t-independent coset monodromy) for every piece — round12_q9
128. PROVED: Conditional theorem — under (R1) and (R2^orb) the problem's claim holds, since (R2^orb) gives (Rig) by entry 126 and a single lift-curve at every boundary point hence MS11♭ by entry 114, and entry 113 with chain step 1 then gives Y_t = Y_0 (derivation not yet checked by a separate query) — round12_q9
129. PROVED: Lemma A and Lemmas F, G1–G2 — lift points of Q_t in a 3-fold component X form one G_X-orbit, the lift-curves in X are G_X·L_0, (1L_X) holds iff G_X ⊆ Stab(L_0), and MS11♭ at Q depends only on Stab(b̃)-orbits with (1L_X) sufficient only when the initial twist lies in Stab(b̃)Stab(x) — round12_q2
130. PROVED: Propositions B and G4 — automorphisms of Q in the pointwise stabiliser K_S of the t = 0 sheet (or in Stab(b̃)) never make MS11♭ fail, so a failure needs a lost automorphism acting non-trivially on S or moving S, or an initial twist outside Stab(b̃)Stab(x) — round12_q6
131. REFUTED: "an automorphism g ∈ G_X fixing S × {0} pointwise fixes the lift-curve L_0" (planner's step 4) is false as a local statement, by chart-level models consistent with (R1), (R2) in which MS11♭ still holds — round12_q2
132. PROVED: Lemma G1 — an automorphism fixing the t = 0 sheet S pointwise acts trivially on the 3-fold component X unless X_0 is non-reduced along S, which happens only when V_t loses a generic automorphism of the curves of V_0 — round12_q3
133. PROVED: Φ-reformulation — the generic-time trichotomy holds for every non-constant constant-vertex value branch φ with φ(0) = Y_0, (β)-twists and the initial twist preserve Φ-persistence unless the twin is rigid (≡ Y_0), and at the endpoint the merging label is rigid on every anchored sheet of b̃ (that the chain entries hold with Y replaced by φ is unchecked) — round12_q7
134. PROVED: Configuration (γ°) forces a moving twin u = g^{-1}x ∈ M_W, two distinct lifts c̃ ≠ g c̃, a frozen twin with F_u ≡ Y_0 and F_x ≅ Y_t along the lift-curve, and Y(Δ) ⊂ pr_u(K_W) — round12_q8
135. PROVED: A twin point satisfies 2(2g_i−2+n_i) ≤ 2g−2, and the problem is vacuous for g = 2, so any counterexample has g ≥ 3 — round12_q4
136. PROVED: Twin-free walk — (Term) ⇒ (MS-ray) ⇒ (MS-R) ⇔ (B𝒴), each of which gives the claim under (Rig), while for the non-smooth quintic surface all of them fail although the claim holds there (quintic part a sketch), so twin-free arguments must use smoothness of V_0, persistence or label-level data — round12_q10
137. OPEN: (NRT) no rigid twin — under (R1), (R2), (Rig) with Y non-constant there are no Q ∈ B_0, a ∈ Aut(Q), lift-curve L of Q_t and label x ≠ a^{-1}x such that along L the component x has a non-constant value φ(t) with φ(0) = Y_0 (a constant-vertex value branch, φ ∈ Φ) while a^{-1}x has value ≡ Y_0 for all t — round13_plan

122. PROVED: Under (Rig), MS11 and MS11♭ are equivalent to the problem's claim (vacuous when the claim holds), so a refutation of either is a counterexample to the problem — round11_q1
124. OPEN: MS11♭ — MS11 with "transport sheet" replaced by "anchored sheet" (an irreducible component of closure(Ñ_c̃) containing c̃ × {0}) in both hypothesis and conclusion: at a non-product puncture point Q of two distinct lifted branches β̃ ≠ b̃ lying in one component of q^{-1}(closure V_0) ∩ B, under (R1), (R2), (Rig) and Y non-constant, a label Y-persistent on an anchored sheet of β̃ is Y-persistent on an anchored sheet of b̃ — round12_plan

Notes on the lines above: entry 100 (Lemma B1 of round10_q3) is retracted — its parts (a),(b) are false (entry 110) and entry 112 replaces it; entry 109 (MS11) is retracted and replaced by MS11♭ (entry 124). 'Theorem N' / 'R8-2 Theorem 1' (entry 72): at generic t, a Y_t-copy at a point P of B_t is intact along every lifted branch through a lift of P and either stays constant ≅ Y_t along it or moves, the latter only if P lies in the stratum of that branch's piece (so never at a puncture).


## Approaches already tried on MS11♭ and its earlier wordings (do not reuse as your first move)

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 | — | (H1) isolated |
| round4_q7 §C | local analysis | (C-merge) not derivable locally |
| round5_q1–q4, q9 | conditional pinning under (T0) | heuristics |
| round5_q5 | analytic half | T′, V |
| round5_q8 | cyclic constructions | twin gap found |
| round6_q1, q2, q3, q8 | closing on MS5 | MS5 false for singular quintic; Krull/twin pinning |
| round6_q4 | refute MS5 | Picard surface |
| round6_q6 | multi-scale | Lemma D, Theorem 4 |
| round6_q9 | Jenkins–Strebel rays | Lemma PA, Prop K |
| round7_q1, q2, q3, q8 | closing on MS6 | MS6 under (NT)/(NT*) |
| round7_q4 | refute MS6 | Theorem C |
| round7_q5 | twin-robust transport | chart-local twin model |
| round7_q6 | time-t open/closed | Theorem T under (Lock) |
| round8_q1 | closing on MS8; Teichmüller-disc limits | Theorem X |
| round8_q2 | Stein factorisation | Lemma U; trichotomy |
| round8_q3 | analytic Y-locus | Theorem N; Cor. T |
| round8_q8 | transport families, isotropy | (SC)/(IP) suffice |
| round8_q4 | refute MS8 | Theorem 2V |
| round8_q5 | Aut(J) fixed points, covering lemma | (U_J) suffices |
| round8_q6 | Minsky/Antonakoudis crossings | (CR) ⇐ (PC) |
| round8_q7 | statements only | Lemma S, junction lemma |
| round9_q1 | copy-free / Krull at one lift | dichotomy; (Seal) |
| round9_q2 | lift-curves, star | SC all-or-nothing |
| round9_q3 | pole function; product strata | X′; Lemma PT |
| round9_q7 | components of ℬ, alignment | Lemmas T/S/J; Theorem R |
| round9_q4 | crossing step + same sheet | X*; walk chain K_w |
| round9_q5 | α-fixed loci + Lemma TG | (U″) suffices |
| round9_q6 | 3-fold 𝒳, Γ-orbits | (IP_Γ) suffices |
| round9_q8 | endpoint twin obstruction | partner lemmas |
| round10_q1, q2, q3 | closing on MS10 | X*_all; IMOV_all; gaps A/B |
| round10_q4 | refute MS10 | none; MS10 ⇔ Goal(Rig) |
| round10_q5 | level structures | dead end |
| round10_q6 | trace step | Lemma D3 |
| round10_q7 | counting | no-go; Theorem Q |
| round10_q8 | statements only; arithmetic | arithmetic dead |
| round10_q10 | chain check of K_w | Lemma S̃′ |
| round11_q1, q2, q3, q8 | closing on MS11 (Mechanism D) | B1 false; anchored sheets; Mechanism D; lift-curve form; rigid twin |
| round11_q4 | refute MS11 | none; (1L), twin-free closure, TFM |
| round11_q5 | Mechanism D (named) | same reduction |
| round11_q6 | statements only; Douady deformation theory | first order only; Lemma TR |
| round11_q7 | Theorem Q via Grothendieck | Theorem D |
| round11_q9 | chain check | chain correct with MS11♭ |
| round12_q1, q2, q3 | closing on MS11♭ (Mechanism G) | Lemma F, Lemma A, Prop. B, Lemma G1; step 4 false locally; K_S harmless |
| round12_q4 | refute MS11♭ | none; Euler bound, g ≥ 3 |
| round12_q5 | statements only; explicit lift-curves in stratum chart (LC) | Prop. LC′ (equivalent form) |
| round12_q6 | Mechanism G (named) | Lemma G2 (τ correction), Model G3′, Prop. G4; residual (R-a)/(R-b) |
| round12_q7 | (β)-obstruction with global input | Φ-reformulation; reduces to rigid twin |
| round12_q8 | (γ°)/(IMOV_Q) obstruction | frozen twin; Y(Δ) ⊂ pr_u(K_W); (O-γ°′) |
| round12_q10 | twin-free walk | Theorem TW; needs smoothness; quintic obstruction |


## Reminder
- Never assume V_t totally geodesic for t ≠ 0, and never assume H_t preserves automorphism groups (the orbifold reading (R2^orb) is NOT adopted).
- Use anchored sheets; do not use Lemma B1(a),(b) of round10_q3 (false); use B1♭ of round11_q9 §2.3.
- A proof for a sub-class, or under an extra hypothesis, does not answer the question; report it as partial.
- Begin with a plan/status line. End with: proved / not proved / open.
