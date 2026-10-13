kind: attempt
Open question attempted: the run's missing statement MS10 (ledger entry 96, OPEN), the twin problem at non-product boundary points. This is a statements-only query. You get MS10 and the bare statements of the results the run has proved, but no proofs and no planner's sketch, so that you can approach it fresh.

## Task
1. **Derive the problem's claim from MS10.** Using only the proved statements listed below, together with the separate open input (Rig) (entry 82), derive for yourself that MS10 implies the problem's claim (under the readings (R1), (R2)).
   - If the derivation does not go through, say exactly where.
   - If you find MS10 implausible, say why.
   - Either finding is a valuable result.
2. **Attack MS10** — prove it, or refute it by an explicit admissible configuration. Your first move must be one that none of the approaches listed at the end has used, for example:
   - global Hodge theory of the twin pair (the Jacobians or Pryms of the two twin components, as sub-quotients of the limiting mixed Hodge structure);
   - the SL(2,R)-action and period coordinates on the orbit-closure side of V_0;
   - intersection theory on the compact surfaces closure(V_t), whose boundary-divisor intersection numbers are topological;
   - an arithmetic argument (fields of definition, Galois conjugation of totally geodesic surfaces);
   - a holomorphic-function or maximum-principle argument on the 3-fold 𝒳.
   Name your first move.
3. A proof only for some of the cases MS10 covers, or under an extra hypothesis, does NOT answer the question; report it as partial.

Begin with a short plan/status line. End with: proved / not proved / open.

## Readings
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


## The missing statement MS10
**Missing statement (MS10)** (new wording; OPEN entry 96, locator round10_plan; replaces MS8 = entry 68 as the missing statement).
- *Setting.*
  - g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i) and (ii) in the readings (R1), (R2), with H_0 = id. V_t is not assumed totally geodesic for t ≠ 0, and H_t need not preserve automorphism groups.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type, ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - (Rig) holds: there is a finite set 𝒦 of triples (G, M, K) with M ⊂ V(G) and K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G).
  - **t ↦ Y_t is non-constant.**
- *Data.*
  - Q ∈ B_0 := closure(V_0) ∖ V_0, lying in a stratum Δ_{G_Q} that is NOT of product type.
  - B ⊂ Def(Q), a small Aut(Q)-invariant ball.
  - Two lifted branches β̃, b̃ through 0 of branches β, b of B_0 at Q (possibly lifts of the same coarse branch).
  - They are *joined inside the chart*: there are paths γ_n: [0,1] → q^{-1}(V_0) ∩ B with γ_n(0) → a point of β̃ ∖ {0} and γ_n(1) → a point of b̃ ∖ {0}.
  - A label x of G_Q with F_x(0) ≅ Y_0 that is Y-persistent along β̃.
- *Conclusion.* x is Y-persistent along b̃. In particular, at t = 0, x is intact along b̃ and F_x ≡ Y_0 there.


## Statements of proved results the run cites (statements only, from the run's ledger; locators name the answer files, which you do not have)
19. PROVED: Repaired proof of entry 2 — A = closure(𝒱)∩(Δ_Γ×Δ) has pure dimension 2, local holomorphic sections over Δ off a discrete set plus continuity from (R2) and removable singularities make t ↦ Y_t holomorphic (the original properness argument had a gap) — round4_q3
24. PROVED: Under (R2) incidences transport automatically: for a boundary piece E_0 and P_0 ∈ closure(E_0) ∩ closure(∂V_0), P_t = H(P_0,t) lies in closure(E_t) ∩ closure(∂V_t), is continuous in t, and has vertex-i component Y_t — round4_q7
50. PROVED: Proposition K — from a generic point of ∂V_0 a compact connected set of boundary points along which the path-marked Σ_i-component stays intact and ≅ Y_0 reaches a point Q_0 carrying a boundary branch of type MERGE or MOV (Q_0 need not lie in closure(∂V_0)) — round6_q9
54. PROVED: L1 holds for pieces in product-type strata (and for Aut(G)-fixed vertices), and L1′ holds for every stratum: if pr_u is constant on every component of the 0-fibre of an irreducible lifted family W then it is constant on every component of every fibre W_t — round7_q9
70. PROVED: (F2) holds in general form (Theorem F2*), Lemma T′ is repaired, and Theorem TV holds: every 1-dimensional boundary piece of closure(V_0) in every stratum has a vertex j with π_j∘ν a proper orbifold covering of a Teichmüller curve whose universal-cover lift is the Teichmüller disc, and every end of the piece maps to a cusp (Lemma PA quoted) — round8_q10
71. PROVED: Lemma U — under (R1),(R2),(Rig) each 2-dimensional component W of each lifted boundary family has one moving set M_W and one image curve K_W for all components of all fibres at all times, so every piece is K_W × {point} — round8_q2
72. PROVED: Generic-time trichotomy — under (R1),(R2),(Rig) with Y non-constant, outside a discrete set of t no Y_t-copy anywhere merges or moves at a puncture, every copy along every branch STAYs or moves at an interior point, and every such interior move is a pure or shared crossing — round8_q2
73. PROVED: Theorem X — at an interior point Q_0 of a piece of closure(V_0) (product stratum), no sheet containing a branch of the piece carries a nonzero effective Q-Cartier divisor supported on boundary curves not over that branch (monomial form valid for any singularity), so crossings inside a common Q-factorial sheet never occur at any t (fact (Fl) cited) — round8_q1
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

Terms used in these statements:
- *Walk chain* (entry 85). From a generic point of ∂V_0, a single Teichmüller ray in V_0 gives a finite sequence of pieces D^1 ⊂ ∂V_0, D^2, …, D^k and transition points J_m, with one chart vertex x_m that is the constant Σ_i-region ≅ Y_0 on both sides of J_m. Each transition is realised by a lifted path inside a small chart ball. The endpoint Q_0 has a terminal lifted branch along which x MERGES (an edge at x unpinched) or MOVES (F_x non-constant).
- *Aligned* (entry 87). At a point Q, the automorphism g′ ∈ Aut(Q), found by a Baire argument, that relates the local components of the boundary total space through which the two branches transport, fixes the tracked label.
- *Product type.* ξ_G is injective on coarse spaces.
- *(Rig).* There is a finite set 𝒦 of triples (G, M, K) with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in the boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦. Consequence: the classes of smooth components of puncture values of non-constant vertices form a t-independent finite set F.

## Approaches already used on MS10 or its predecessors (do not start with these)
- Local chart analysis at the junction (Kuranishi charts, transport families of branches, patterns).
- Transport of Teichmüller rays and squares, with monodromy around orbifold points.
- Fixed loci of automorphisms, cases (A)/(B)/(C).
- The 3-fold component 𝒳 and Γ-orbits of lifts.
- Krull at one lift; the sealed / copy-free dichotomy.
- Star coherence and lift-curves.
- Alignment / Baire, via components of the boundary total space.
- Partner lemmas (frozen, persistent, crossing).
- Isotropy preservation.
- No-twin transport.
- The Abel–Jacobi constraint on sliding crossings.
- Normal-bundle ratios.
- Kobayashi length domination.
- Level structures, boundary-trace analysis and degree counting (attempted in parallel this round).
