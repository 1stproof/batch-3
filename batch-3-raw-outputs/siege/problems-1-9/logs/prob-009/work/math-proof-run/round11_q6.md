kind: attempt
Open question attempted: the run's missing statement MS11 (ledger entry 109, OPEN): the twin problem at non-product boundary points that are punctures of both adjacent pieces. This is a statements-only query. You get MS11 and the bare statements of the results the run has proved, with no proofs and no planner's sketch, so that you can approach it fresh. Earlier wordings of this statement (MS8, MS10) have been attacked in rounds 8, 9 and 10.

## Task
1. **Derive the problem's claim from MS11.** Use only the proved statements listed below, together with the separate open input (Rig) (entry 82), and derive for yourself that MS11 implies the problem's claim under the readings (R1), (R2).
   - If the derivation does not go through, say exactly where.
   - If you find MS11 implausible, say why.
   - Either finding is a valuable result.
2. **Attack MS11.** Prove it, or refute it by an explicit admissible configuration. Your first move must be one that none of the approaches listed at the end has used. Name your first move. Examples:
   - intersection theory on the compact surfaces closure(V_t), or on the 3-fold closure(𝒱), using that boundary intersection numbers are topological;
   - the SL(2,R)/period-coordinate structure of the orbit closure attached to V_0, and how its cylinder deformations see the twin components;
   - a holomorphic-function or maximum-principle argument on the 3-fold component containing S × {0};
   - local cohomology / connectedness theorems for the boundary divisor of that 3-fold;
   - a monodromy argument for the family of stable curves over the lift-curves of Q_t.
3. A proof for only some of the cases MS11 covers, or under an extra hypothesis, does NOT answer the question; report it as partial.

Begin with a short plan/status line. End with: proved / not proved / open.

## The missing statement MS11
**Missing statement (MS11)** (OPEN entry 109, locator round11_plan; replaces MS10 = entry 96, retracted by entry 108).
- *Setting.*
  - g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i) and (ii) in the readings (R1), (R2), with H_0 = id. V_t is not assumed totally geodesic for t ≠ 0, and H_t need not preserve automorphism groups.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type, ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - (Rig) holds: there is a finite set 𝒦 of triples (G, M, K) with M ⊂ V(G) and K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G).
  - **t ↦ Y_t is non-constant.**
- *Data.*
  - Q ∈ B_0 := closure(V_0) ∖ V_0, lying in a stratum Δ_{G_Q} that is NOT of product type.
  - B ⊂ Def(Q), a small Aut(Q)-invariant ball (small enough that the irreducible components of q^{-1}(closure V_0) ∩ B are the irreducible components of the germ at 0, and that distinct lifted branches of q^{-1}(B_0) meet only at 0), and ε > 0 small.
  - Two DISTINCT lifted branches β̃ ≠ b̃ through 0 of branches β, b of B_0 at Q (possibly lifts of the same coarse branch) such that:
    - (P) Q is a puncture of the piece of β and of the piece of b, i.e. Q lies in the stratum of neither: some smoothing parameter s_e is not identically 0 on β̃, and likewise on b̃;
    - (S) β̃ and b̃ lie in one irreducible component S of q^{-1}(closure V_0) ∩ B.
  - A label x of G_Q with F_x(0) ≅ Y_0 that is Y-persistent on some transport sheet of β̃.
- *Conclusion.* x is Y-persistent on some transport sheet of b̃. (Then, by Lemma B1(a), at t = 0 x is intact along b̃ and F_x ≡ Y_0 there.)
- *Definitions used.* Transport family Ñ_c̃ of a lifted branch c̃ of a branch c: the connected component containing c̃ ∖ {0} of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε). A *transport sheet* of c̃: an irreducible component of closure(Ñ_c̃) in B × Δ_ε. *x is Y-persistent on a sheet T*: at every (p,t) ∈ T, x is intact at p (s_e(p) = 0 for every edge e at x) and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).

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
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w.
- M(E) and K(E) as before.
- *Chart at Q ∈ B_0*: Def(Q), the Kuranishi space of the stable curve Q, with plumbing coordinates s_e (e ∈ E(G_Q)) and quotient map q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g.
- *Vertices of G_Q* are labels. A label x is *intact* at p ∈ Def(Q) if s_e(p) = 0 for every edge e at x. Then F_x(p) is the corresponding component of the curve over p, with its special points.
- *Lifted branch*: a lift b̃ ∋ 0 of a branch b of B_0 at Q.
- *Transport family* of b̃: Ñ_b̃ := the connected component, containing b̃ ∖ {0}, of q^{-1}(H((b ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε) ⊂ Def(Q) × Δ_ε, where B is a small Aut(Q)-invariant ball.
- *x is Y-persistent along b̃*: at every (p,t) ∈ Ñ_b̃, x is intact at p and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).
- *Product-type stratum*: ξ_G is injective on coarse spaces.

- *Transport sheet* of a lifted branch c̃: an irreducible component of closure(Ñ_c̃) in B × Δ_ε. *x is Y-persistent on a sheet T*: at every (p,t) ∈ T, x is intact at p and F_x(p) ≅ Y_t. The whole-family notion "Y-persistent along b̃" above is used in earlier files and in MS10. It is superseded by the sheet-wise notion, because transport families can be reducible (round10_q3 §2.2, round10_q7 §3). MS11 and the chain use the sheet-wise notion.
- *Lift-curve*: an irreducible component of {(p,t) ∈ B × Δ_ε : q(p) = Q_t}, where Q_t := H_t(Q). *Boundary-type* sheet: its generic pattern is not all of E(G_Q), i.e. Q is not in the stratum of its branch (round10_q7 §1).

## Statements proved by the run (ledger lines, verbatim; '—' is followed by the locator; proofs omitted)
2. PROVED: Under the reading that closure(𝒱) in M̄_g×Δ is analytic with fibre over t equal to closure(V_t), the map t -> Y_t is a holomorphic map Δ -> M_{g_i,n_i} (graph of a continuous map that is an analytic set / Remmert proper image) — round1_q4
5. PROVED: If every V_t were totally geodesic, the claim would follow from countability of totally geodesic subvarieties (via Wright's correspondence with orbit closures and Eskin–Mirzakhani–Mohammadi countability, cited not reproved) — round1_q1
14. PROVED: Pinning lemma — if a deeper point P_t ∈ closure(∂V_t) ∩ Δ_{G'} (Y-vertex intact) is continuous in t and lies on closure(E_t) for a 1-dim boundary piece E_t with closure(E_t) = closure(E_0) for all t, then Y_t = Y_0, and by (ii) the incidence persists when P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} lying in closure(E_0) — round3_q1
19. PROVED: Repaired proof of entry 2 — A = closure(𝒱)∩(Δ_Γ×Δ) has pure dimension 2, local holomorphic sections over Δ off a discrete set plus continuity from (R2) and removable singularities make t ↦ Y_t holomorphic (the original properness argument had a gap) — round4_q3
23. PROVED: Hypothesis (ii) is vacuous or tautological for every pair (Δ_G, Δ_Γ) with G a contraction of Γ, so (ii) has content only at isolated points of deeper strata — round4_q2
24. PROVED: Under (R2) incidences transport automatically: for a boundary piece E_0 and P_0 ∈ closure(E_0) ∩ closure(∂V_0), P_t = H(P_0,t) lies in closure(E_t) ∩ closure(∂V_t), is continuous in t, and has vertex-i component Y_t — round4_q7
25. PROVED: At every cusp of closure(∂V_t) there is a further boundary branch b of closure(V_t) pinching an extra edge, and if b has the merge property then the merged projection π_v(E) is a curve whose limit at the cusp has vertex-i component Y_t — round4_q7
48. PROVED: Krull pinning (Lemma D, Pinning Lemma, Theorem 4) — at each time t every node of a point of closure(∂V_t)\∂V_t is kept along some boundary branch, ∂V_t-branches have a clean vertex ≅ Y_t, and if near P_0 the boundary is only ∂V_0∪{P_0} and condition (Tw2) holds with Lemma R for the host vertex, then Y_t ≡ Y_0 — round6_q6
54. PROVED: L1 holds for pieces in product-type strata (and for Aut(G)-fixed vertices), and L1′ holds for every stratum: if pr_u is constant on every component of the 0-fibre of an irreducible lifted family W then it is constant on every component of every fibre W_t — round7_q9
57. PROVED: Time-t criterion — at any t, a merge of any Y_t-copy along a boundary branch, or an intact moving Y_t-copy along a branch whose piece has the point as a puncture, yields the MS6 configuration at t; if it fails at t, every copy along every branch STAYs or moves at an interior point (IMOV), and absent IMOV the boundary points with a Y_t-copy form a union of connected components of B_t — round7_q6
70. PROVED: (F2) holds in general form (Theorem F2*), Lemma T′ is repaired, and Theorem TV holds: every 1-dimensional boundary piece of closure(V_0) in every stratum has a vertex j with π_j∘ν a proper orbifold covering of a Teichmüller curve whose universal-cover lift is the Teichmüller disc, and every end of the piece maps to a cusp (Lemma PA quoted) — round8_q10
71. PROVED: Lemma U — under (R1),(R2),(Rig) each 2-dimensional component W of each lifted boundary family has one moving set M_W and one image curve K_W for all components of all fibres at all times, so every piece is K_W × {point} — round8_q2
72. PROVED: Generic-time trichotomy — under (R1),(R2),(Rig) with Y non-constant, outside a discrete set of t no Y_t-copy anywhere merges or moves at a puncture, every copy along every branch STAYs or moves at an interior point, and every such interior move is a pure or shared crossing — round8_q2
74. PROVED: Theorem 2V — under (R1),(R2),(Rig), Y_t ≡ Y_0 whenever some cusp of ∂V_0 satisfies (Tw1),(C1),(C2), in particular when Γ has two vertices and near one cusp the boundary of closure(V_0) is only ∂V_0 plus the cusp — round8_q4
78. PROVED: A twin jump at a chain junction forces failure of (IP),(NT),(Lock),(U_J), a persistent twin (a piece with two constant Y_0-vertices of different value functions) or a junction crossing, and an automorphism α moving the tracked region whose fixed locus in the lifted 3-fold accumulates at (J,0) in one of the configurations (A),(B),(C) — round8_q8
80. PROVED: Lemma Red (reduced central fibre), Lemma P0 (which vertices degenerate at a puncture is t-invariant) and Theorem B ((Rig) for a piece whose Teichmüller-vertex map is birational, under (Σ-fixed)) — round8_q9
81. REFUTED: Piece-level (Rig) — for holomorphic families of maps of a piece with fixed Teichmüller vertex, trivial source, fixed punctures and (O) for that vertex, the joint image curve (Example Z) and the puncture values of non-constant vertices (Example Z′) need not be t-independent (realisability by an admissible V_t unchecked) — round8_q9
82. OPEN: (Rig) holds for every admissible family — (F2) is now proved (entry 70), it still needs (O_G) for every piece and L2′, and by entry 81 it cannot be derived from piece-level data alone — round9_plan
84. PROVED: Theorem X*/X′ — for a piece E in a product-type stratum and Q_0 ∈ E, every boundary curve through Q_0 of any sheet of closure(V_0) containing a branch β of E lies over β, for any normal singularity and with no Q-Cartier hypothesis (proved independently in round9_q3 §1 by a pole function and the maximum principle) — round9_q4
85. PROVED: Proposition K_w — from a generic point of ∂V_0 a single Teichmüller ray yields a walk chain (pieces from ∂V_0, transition points with a common chart vertex and continuous lifted interior paths inside a small chart ball, endpoint MERGE or MOV), every transition having its two branches in a common sheet, while the K_0-chain reading (TD_J) of Proposition K is unsupported (modulo the cited inputs of PR-H) — round9_q4
86. PROVED: Lemma PT — in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type, so twins occur only at non-product points; with Lemma SS/Cor. SS′ and Theorem X′, an interior-MOV endpoint never lies in a product-type stratum, the chain lies in the persistent network (Prop. CN), and the Count lemma holds — round9_q3
87. PROVED: Lemmas T, S, J and Theorem R — under (R1),(R2),(Rig), H sends each piece into one global and local component of the boundary total space, M and K and persistence are constant on whole components, the junction trichotomy pinned/persistent/crossing holds, and Y_t ≡ Y_0 if the track is aligned at every junction and at Q_0 with terminal MERGE or puncture-MOV — round9_q7
88. PROVED: Copy-free dichotomy — under (R1),(R2),(Rig), if Y is non-constant then either interior-move events lie on the persistent network at every generic t near 0 or B_0^∂ is sealed ((II-a) and (Seal_Q) everywhere), with t=0 release and seal criteria — round9_q1
89. PROVED: Every transport family contains a whole lift-curve of Q_t so star coherence is all-or-nothing in t, both families at a junction lie in the track's 3-fold component, and Proposition 4 gives the t=0 structure forced by a counterexample — round9_q2
90. PROVED: Under the extra readings (R3),(T4), Theorems A/B of round8_q5 hold with (U_J) weakened to (U″), so only relevant α-fixed components of dimension ≥2 can cause a twin jump; Lemma TG (a totally geodesic sheet meets Fix(h) in itself, a Teichmüller disc, or points) and the boundary-trace trichotomy hold — round9_q5
91. PROVED: The lifts of J_t in the track's 3-fold component form one orbit of Γ = Stab(𝒞°), both transport families lie in it, and no twin jump occurs when Γ = Γ_x·Stab_Γ(j̃(t)) (e.g. under (IP_Γ) or (NT_Γ)) — round9_q6
92. PROVED: At a twin jump the partner copy at the same lift carries the other value function and is frozen, persistent or a crossing on the incoming piece, the merging copy of an endpoint twin is frozen, and a coherent MERGE/pMOV endpoint freezes the tracked function — round9_q8
93. PROVED: Lemma Loc — at a point of ∂V_0 (mild automorphism hypothesis) there are local stratum-preserving admissible deformations of the germ of closure(V_0) moving the constant factor, so neither the goal nor (Rig) follows from local data at boundary points; and the goal holds if every V_t is totally geodesic (countability cited) — round9_q9
94. PROVED: The lift of V_0 is Kobayashi-isometric in T_g, Kobayashi translation lengths of axis classes cannot decrease under the deformation, and equality with attainment forces the Teichmüller disc to persist in V_t (which pins Y) — round9_q10
97. PROVED: Theorem X*_all — for a piece E in ANY stratum (product type not needed) and Q_0 ∈ E, every irreducible component of the germ of q^{-1}(closure V_0) at 0 ∈ Def(Q_0) that contains a lift β̃ of a branch of E meets {∏ s_e = 0} near 0 only in β̃ (independent second proof in round10_q2 §3, Theorem X**) — round10_q1
98. PROVED: Proposition K_w holds after repairs (R-a)–(R-d) (extra smallness conditions, canonical chart lifts through augmented Teichmüller space, recurrent transition types with per-transition witnessing path sequences), and Lemma S̃′: the entering and leaving (or terminal) lifts of each walk-chain transition lie in one irreducible component of q^{-1}(closure V_0) ∩ B, with no reading beyond (R1),(R2) — round10_q10
99. PROVED: Cor. IMOV_all — by entry 97 and the common component of entry 98 (or Lemma 1SS of round10_q1 under reading (T4)), a walk-chain transition point lying in the stratum of either adjacent piece has equal entering and leaving lifts, so in every stratum the endpoint and every genuine transition are punctures of both adjacent pieces, and junction crossings, interior-MOV endpoints and turning twins do not occur — round10_q1
100. PROVED: Two gaps of the MS10 chain at non-product pieces, with repairs: the walk's label can switch silently where Aut(G)-translates of a lifted piece cross (repair: add the finite set R(D) of such points to Σ, making them interior transitions), and a transport family can be reducible, so persistence must be read on irreducible components (Lemma B1: Stab(b̃) permutes the components of Ñ_b̃ transitively; component-wise transfer along travel intervals) — round10_q3
101. REFUTED: R7-3 Lemma 2 step 2 ("a transport family Ñ_b̃ is irreducible"), and with it the adequacy of MS10's whole-family notion of persistence, by explicit local germ models in which Ñ_b̃ is reducible and literal MS10 fails while the component-wise version holds — round10_q7
102. PROVED: Incidence propagation (every transport sheet contains a lift-curve; P(T) = Λ(λ) for boundary-type T ⊃ λ under (Rig) with Y non-constant), the counting no-go (every conserved count is Γ-equivariant and consistent with a failure), and Theorem Q (two boundary-type sheets on a common 3-fold component of 𝒳 on which one is set-theoretically principal share a lift-curve, or give a same-branch crossing) — round10_q7
103. PROVED: Logical status of the twin statement — given the chain, any counterexample to MS10 is a counterexample to the problem under (Rig), MS10 is equivalent to its restriction to walk-chain data, and for a σ-stable twin sheet MS10 is equivalent to the problem for that V_0 (round10_q8 Prop. T) — round10_q4
104. PROVED: Level structures give nothing new at Q — every automorphism of a stable curve acting trivially on H_1(·;Z/m), m ≥ 3, is the identity, yet the deck stabiliser of a point of M̄_g[m] over Q surjects onto Aut(Q) and acts on labels as Aut(Q) does, an H-compatible lifted trivialisation forces (IP), and for V_0 a component of a pure 2-dimensional symmetric locus either Y is constant or V_t leaves the locus — round10_q5
105. PROVED: Lemma 3.1 — if Q is isolated in B_0 ∩ Δ_{G_Q} and Y is non-constant, then Q ∉ closure(V_τ) for τ outside a discrete set, and (conditional on cited McMullen/Möller rigidity) a case-(A2-disc) failure cannot come from an equisingular deformation of the Teichmüller curve — round10_q3
106. PROVED: Lemma D3 — if α ∈ Γ ∖ KΓ_x fixes pointwise a 3-dimensional component of the germ of 𝒳 at (0,0), then every V_τ lies in the symmetric locus M_g([α]) and the twins x, αx are locked on that component — round10_q6
107. PROVED: Lemma CD — for a piece's lifted family, {t : K^M_t ⊂ C} is all of Δ or discrete, so (Rig) for a piece holds iff its joint image lies in a countable class of curves for uncountably many t, and the goal holds if V_t is totally geodesic for uncountably many t (countability cited) — round10_q9

How these are used by the run's own chain (statements only; you should check this yourself): K_w (entries 85, 98) gives a finite chain of boundary pieces from ∂V_0 to an endpoint Q_0 at which the tracked Y_0-component MERGEs or MOVEs, with transitions whose entering and leaving lifts lie in one upstairs component (S); entry 99 makes every transition that is an interior point of an adjacent piece trivial, so the remaining transitions and Q_0 satisfy (P); product-type transitions are handled by entries 86, 87; persistence is transferred sheet-wise along travel intervals (entry 100); MS11 handles non-product puncture transitions and the endpoint, where its conclusion contradicts MERGE/MOV; so Y is constant under (Rig).

## Approaches already used on MS11 and its earlier wordings (do not start with these)
Local chart analysis and chart models; conditional pinning; cyclic covering constructions; multi-scale differentials; Jenkins–Strebel / Teichmüller rays and Hausdorff limits; no-twin transport and continuity principles; time-t open/closed arguments; Stein factorisation; the analytic Y-locus and generic-time trichotomy; isotropy preservation / star coherence; fixed loci of automorphisms with the covering lemma (square monodromy); Minsky/Antonakoudis product regions; Krull at one lift; lift-curves and stars; pole functions and the maximum principle on sheets; components of the boundary total space and alignment; α-fixed loci with Lemma TG and boundary traces; the lifted 3-fold and Γ-orbits; partner copies; level structures; counting / conservation of number; Krull linkage (Theorem Q); arithmetic (fields of definition).

## Reminder
- Never assume V_t totally geodesic for t ≠ 0, and never assume H_t preserves automorphism groups.
- A proof for a sub-class, or under an extra hypothesis, does not answer the question; report it as partial.
