kind: attempt
Open question attempted: the run's missing statement MS10 (ledger entry 96, OPEN), through its hardest step: the open questions O1″, O2″ and O3″ of round9_q5 §5. Those questions record what remains of MS10 after round9_q5's Theorems A″/B″, under round9_q5's readings (R3) and (T4).

## Task
Prove MS10, stated below, exactly as stated. The intended route is to prove the cut-out claim (Tr) and then derive MS10 from it, or else to give an explicit counterexample to (Tr) or to MS10.

**Claim (Tr).** Work in MS10's setting at the point Q, with the notation of round9_q5 §0 and round9_q6 §0:
- 𝒞° is the component of the lifted interior family containing the joining paths;
- 𝒳 := closure(𝒞°);
- Γ := Stab_{Aut(Q)}(𝒞°);
- K is the kernel of the action of Γ on 𝒞°;
- Γ_x := Stab_Γ(x).

Let α ∈ Γ ∖ KΓ_x, and let Φ be a relevant irreducible component of Fix(α) ∩ 𝒳 (τ ≢ 0 on Φ, and Φ ⊄ {∏ s_e = 0}) with dim Φ ≥ 2. Then the local monodromy that Φ contributes to the lifts of the squares of round9_q5 Lemma 1/Lemma 2 lies in Γ_x·Stab_Γ(j̃(t)). Here j̃(t) is the lift of Q_t in the closure of the transport family of β̃. In other words, crossing Φ never changes which twin carries Y_t.

**Ingredients you may use** (all spliced below):
- round9_q5 Corollary 1: only such Φ obstruct.
- Lemma TG: at τ = 0, Φ_0 is a Teichmüller curve of α-symmetric curves of V_0 with cusp Q, or an α-symmetric sheet, or lies in the boundary (case (B)).
- Lemma 3: the trichotomy for the boundary trace Ψ = Φ ∩ {∏ s_e = 0}, namely (Ψ-0), (Ψ-J) or (Ψ-Z).
- round9_q6 Lemma 1: the lifts of Q_t in 𝒳 form one Γ-orbit. Cor. 3′: Γ = Γ_x·Stab_Γ(j̃(t)) suffices.
- round9_q2 Lemma 1 and Cor. 1′: lift-curves, and all-or-nothing in t.
- round9_q8 Lemmas 1 and 1′: the partner copies.

**Points to settle.**
- (a) In case (Ψ-J), show that the lift of Q_τ fixed by α is the lift j̃(τ) in closure(Ñ_β̃), or a Γ_x-translate of it.
- (b) In case (Ψ-Z), produce (L1)–(L2) of round9_q5 §4: the Lock must fall on the twin pair that matters.
- (c) Exclude, or handle, case (B-pure): α-symmetric curves of V_τ converging to an α-fixed boundary branch without boundary points near Q_τ.
- (d) Exclude, or handle, case (D3): α fixes pointwise a component of 𝒳.

Total geodesy of V_0 must enter, for instance through Lemma TG and the Teichmüller-ray structure of the walk chain (round9_q4 §2.3). Purely chart-local arguments are known to be insufficient.

If you use readings beyond (R1) and (R2), such as round9_q5's (R3) or (T4), state them explicitly and say whether they follow from the problem's hypotheses. A proof that needs a reading not implied by the problem is partial.

A proof for only some of the cases (A2), (B) or (D3), or only under an extra hypothesis, does NOT answer the question; report it as partial. Begin with a short plan/status line. End with: proved / not proved / open.

## The missing statement MS10 (verbatim from the run's summary)
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


## Readings and definitions
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


## How MS10 is used: the chain (verbatim from the run's summary; the entry numbers refer to the run's ledger, and the corresponding proofs are spliced below — entry 19 = PR-A holomorphy of Y_t; entry 24 = PR-B incidence transport; entries 84–92 = the round-9 files in part 2; entry 82 = (Rig), OPEN, a hypothesis of MS10)
**Chain.** Every step is a statement already PROVED, except MS10.
1. **Goal ⇐ MS8 + (Rig) + entry 19.** (Rig) is entry 82, still OPEN. It is the one input that remains after MS10. Given (Rig), MS8 says Y_t ≡ Y_0, and then Y_t = Y_0 for all t.
2. **MS8 ⇐ MS10.** Assume MS8's setting and that Y is non-constant.
   - (a) **Walk chain** (entry 85, K_w). Fix r small. There are:
     - pieces D^1 ⊂ ∂V_0, D^2, …, D^k;
     - transition points J_1, …, J_{k−1} and an endpoint Q_0;
     - at each transition point J_m, an entering lift β̃_m (of the branch of D^m) and a leaving lift β̃′_m (of the branch of D^{m+1}) in Def(J_m), with a common chart vertex x_m and continuous lifted interior paths in q^{-1}(V_0) ∩ B from near β̃_m ∖ 0 to near β̃′_m ∖ 0;
     - at Q_0, an entering lift β̃ with chart vertex x and a terminal lift b̃, joined by such paths, with x MERGE or MOV along b̃ at t = 0.
   - (b) **Induction claim:** x_m is Y-persistent along β̃_m.
     - Base: D^1 ⊂ ∂V_0, and H_t(D^1) ⊂ ∂V_t carries vertex i ≅ Y_t (entries 24, 87).
     - Step at J_m, product-type stratum: by Lemma PT (entry 86) every g′ ∈ Aut(J_m) fixes x_m, so J_m is aligned. Since x_m is intact and constant along β̃′_m at t = 0, Lemma J / Cor. J′ (entry 87) give (J2): x_m is persistent on the component of the next piece.
     - Step at J_m, non-product stratum: MS10.
     - In both cases persistence passes along D^{m+1} to β̃_{m+1}, because persistence is a property of the whole component κ(D^{m+1}) (Lemma S(c), entry 87) and the chart vertex is c_{m+1} on both ends (K_w Step 3).
   - (c) **Endpoint, product-type stratum.** Q_0 is aligned (Lemma PT).
     - MERGE or puncture-MOV gives (J1) of Lemma J: Y_t ∈ F on an open set, so Y is constant (entry 19), a contradiction.
     - Interior MOV cannot occur (entry 86, Cor. IM(b)). This uses Lemma S′ / Cor. SS′ (the common sheet given by K_w) and Theorem X′ (entry 84) for the product-type piece.
   - (d) **Endpoint, non-product stratum.** MS10 with (β̃, b̃) makes x intact along b̃ with F_x ≡ Y_0 there at t = 0. This contradicts MERGE (x not intact) and MOV (F_x non-constant).
   - Hence Y is constant, which is MS8.

So MS10 + entries 19, 24, 84–87 give MS8, and MS8 + entry 82 give the goal. After MS10 only entry 82 remains.

Remarks.
- MS10 is restricted to non-product strata because the product-type points are settled by the PROVED entries 84, 86, 87 (steps (b) and (c)).
- MS10 has the hypothesis "Y non-constant" because it is used in contradiction form. Without that hypothesis it is false: the walk chain's endpoint is exactly a pair that violates its conclusion.
- Non-product endpoints of interior-MOV type need no Theorem X′: MS10 covers them.


## A suggestion (the planner's sketch; you are free to discard it)
**Why it should hold (my sketch).**
1. Suppose MS10 fails.
   - By entries 72/88, at generic t every Y_t-copy at a lift STAYs along every boundary branch through that lift.
   - So along Ñ_b̃, x carries a value φ(t) ≢ Y_t, and some other label a^{-1}x (a ∈ Aut(Q)) is the persistent copy. This is a twin; Q is non-product, so Lemma PT allows it.
2. By entry 91, both families lie in the 3-fold 𝒳, the lifts of Q_t in 𝒳 are one Γ-orbit, and the failure needs γ ∈ Γ ∖ Γ_x·Stab(j̃(t)).
3. By entry 90 (readings (R3), (T4)), it needs α ∈ Γ moving x and a relevant ≥ 2-dimensional component Φ of Fix(α) ∩ 𝒳. That is: for every τ ≠ 0, a complex curve Φ_τ of α-symmetric curves of V_τ, accumulating at Q.
4. **Conjectured mechanism A (trace).**
   - At τ = 0, Lemma TG makes Φ_0 a Teichmüller curve with cusp Q, a symmetric sheet, or a boundary branch.
   - Its closure passes through Q. By Krull, the trace Ψ = Φ ∩ {∏ s_e = 0} is a curve through (0,0).
   - If Ψ contains a lift-curve of Q_τ (case (Ψ-J)), then α ∈ Aut(Q_τ) at that lift. One then shows this lift is the one in closure(Ñ_β̃), so the monodromy lies in Γ_x·Stab, and entry 91 Cor. 3′ concludes.
   - The open sub-steps are excluding (Ψ-Z) without Lock on the right pair (round9_q5 L1–L2), and the case (B-pure).
5. **Conjectured mechanism B (level structure).**
   - In the level-m cover M̄_g[m] (m ≥ 3), an automorphism of a stable curve that acts trivially on H_1(C; Z/m) should fix every component of positive genus. So positive-genus twins x, αx are never exchanged upstairs.
   - The twin problem then becomes topological triviality of the lifted family 𝒱[m] → Δ, which can fail only through the bad loci of step 3. Genus-0 Y_0 needs a separate look.
6. **Conjectured mechanism C (count).** The Count lemma (entry 86) gives r Y_t-copies at Q_t but r + 1 Y_0-copies at Q. Conservation of the intersection number of the analytic Y-locus with the lift-curves in 𝒳 (a proper finite map over Δ) could forbid this drop.


## What is already known about MS10 (do not merely re-derive it)
- MS10 holds at points of product-type strata (Lemma PT, round9_q3 §3, with Lemma J / Cor. J′ of round9_q7) — that is why MS10 is posed only at non-product points.
- MS10 holds at Q under any of: (U_J) or (Lock) (R8-5 Theorems A/B); (U″) with readings (R3),(T4) (round9_q5 Theorems A″/B″); (SC)/(NT)/(IP) (R8-8 Theorem 1); (IP_Γ) or (NT_Γ) (round9_q6 Cor. 3′); (NB)+(NB_∂) (R8-2 Theorem S, not spliced); a single lift-curve in closure(𝒞°) (round9_q2 Cor. 3); (Seal_Q) failing or a release point (round9_q1). None of these is known in general.
- A failure of MS10 forces (round9_q5, q6, q8; R8-5 Prop. D; R8-8 Prop. 3): an automorphism α ∈ Aut(Q) moving x that preserves the track's 3-fold component 𝒳, drops from Aut(Q_t) at the relevant lift, and has a relevant fixed component of dimension ≥ 2 in 𝒳 (curves of V_τ with automorphism α, for every small τ ≠ 0, accumulating at Q); a persistent or frozen partner copy; |Aut(Q_t)| < |Aut(Q)|.
- Chart-local arguments alone cannot exclude this (R7-3 §5 model; round9_q2 §5; round9_q9 Lemma Loc shows local admissible deformations moving the constant factor exist at boundary points). Total geodesy of V_0, or the global structure of the family, must enter.
- The open sub-questions recorded in round9_q5 §5 (O1″–O3″), round9_q6 §4 (Step 4) and round9_q3's final open question are all special forms of MS10.

## Prior results, part 1: earlier rounds (verbatim from earlier answer files; re-check what you use)
Labels: PR-H = Lemma PA / Proposition K file (round6_q9). PR-I = the quintic/Krull file (round6_q6); its §2, the quintic example, is not reproduced: the surface of cyclic quintic covers in M_6, totally geodesic but NOT smooth, with twin copies A, C of Y_0 at its cusp exchanged by an automorphism. PR-A = holomorphy of t ↦ Y_t (entry 19). PR-C = Lemma C1/C2. "PR-D Lemma R0" = the lifted family of a piece, an irreducible 2-dimensional analytic set proper over Δ. R7-k = round-7 files, R8-k = round8_qk. (O) is an orbifold-transport hypothesis not needed here. R7-6 (the round-7 continuity principle) is not reproduced; its chart readings are restated as (TD_J), (TD_Q) in R8-5 §1, §5 — but note that round9_q4 §2.2 (spliced below) shows that (TD_J) for the chain read off the Hausdorff limit K_0 is unsupported, and replaces that chain by the walk chain of Proposition K_w, whose transitions satisfy the track data inside a fixed small ball B(J,2r) (r arbitrary small).

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




### R8-1. Generic-time lemmas, Theorem X, Lemma S, consequences for crossings (from round8_q1, verbatim, §§1–4)
## 1. Cited standard facts (from memory; not re-proved here)

- **(Wol) Wolpert's lemma.** If d_T(X, X') ≤ d, then e^{-2d} ℓ_X(γ) ≤ ℓ_{X'}(γ) ≤ e^{2d} ℓ_X(γ) for every closed curve γ. Here ℓ is hyperbolic length.
- **(Ab) Abikoff.** Hyperbolic length functions are continuous on augmented Teichmüller space. On a noded surface, the length of a curve disjoint from the nodes is computed on its component, and the length of a node curve is 0. Finitely many length functions give local coordinates, or at least a proper injective map, on each stratum. Hence, if X_n → Z in M̄_g, the curves with ℓ → 0 are exactly the node curves of Z, and the components of Z are determined by the limits of the lengths of curves disjoint from the nodes.
- **(Prop) Teichmüller discs.** For (X, q) with q ∈ Q(X) ∖ 0, the Teichmüller disc τ̃: 𝔻 → T_g is a holomorphic isometric (Kobayashi = Teichmüller, Royden) proper embedding. Its image is a closed complex submanifold of T_g. The family of its Mod_g-translates is locally finite.
- **(Fl) Flat convergence on positive-area components.** Let X_n → P in M̄_g and q_n ∈ Q(X_n) with ‖q_n‖ = 1. Suppose the transplanted differentials ι_n^* q_n converge locally uniformly on each component Y_w of P to q_w, and Σ_w ‖q_w‖ = 1 (no area is lost in the collars). Let A ∈ SL_2(R) and let Z be any limit point of A·(X_n, q_n). If q_j ≠ 0, then Z has, at the node-pattern position of j, the component A·(Y_j, q_j). *Sketch:* the affine maps converge on compact subsets of Y_j ∖ {punctures}, and a conformal embedding between finite-type hyperbolic surfaces of the same signature that is a homotopy equivalence is onto up to punctures. I cite this as standard and have not written a full proof.
- **(PA) Lemma PA** (prior result PR-H §1, proved there modulo (Pl), (Dual), (Bun)). Let P_1 be a generic point of a piece E (product-type stratum) and fix a local branch N of closure(V_0) along E at P_1. Then there are X_n ∈ V_0 ∩ N, X_n → P_1, and generating pairs (X_n, q_n) whose transplants converge to (q_w)_w with Σ‖q_w‖ = 1 and q_j ≠ 0 for some vertex j ∈ M(E). Since V_0 is totally geodesic, the Teichmüller discs D_n of (X_n, q_n) lie in V_0.
  - The proof in PR-H uses approximants X_n = ν(s_0, τ_n) inside a chosen local branch N, so the branch can be prescribed.
  - The vertex j is a max-speed vertex. It moves along E because a_j ≠ 0.
- **Hurwitz.** If holomorphic functions h_n without zeros on a connected open Ω converge locally uniformly to h, then h ≡ 0 or h has no zeros on Ω.
- **Normal surface germs.** Let Ŝ be a normal 2-dimensional germ. A meromorphic function whose divisor is ≥ 0 is holomorphic, and the zero set of a holomorphic function is the support of its divisor. A Weil divisor C is *Q-Cartier* if mC = div(G) for some m ≥ 1 and some holomorphic G. Rational surface singularities, in particular smooth points and quotient singularities, are Q-factorial (Lipman). Normalization has the universal property for maps from normal spaces whose image is not contained in the non-normal locus.

## 2. What (Rig) gives at generic times

Throughout this section assume **Y is non-constant**, to reach a contradiction.

### 2.1 Generic times (re-check of chain step 3)
- K ∩ ∂(∏_{u∈M} M̄_u) is finite for each (G, M, K) ∈ 𝒦, because K is an irreducible compact curve not contained in the boundary.
- At a puncture p of a piece E, ν(p) ∉ ∏_w M_w. Constant vertices of E take values in M_w, since they are constant on E ⊂ ∏M_w. So some u ∈ M(E) has f_u(p) ∈ ∂M̄_u, and pr_{M(E)} ν(p) ∈ K(E) ∩ ∂.
- Hence the puncture values f_u(p), u ∈ M(E), lie in the finite t-independent set F. Let C_F be the finite set of pointed curves (in all orderings of special points) that occur as components of elements of F.
- For (G, M, K) ∈ 𝒦, u ≠ y ∈ M with pr_y|_K and pr_u|_K non-constant, put Fin(K, u, y) := pr_y(K ∩ pr_u^{-1}(C_F)). This is finite: pr_u|_K is non-constant on the irreducible curve K, so K ∩ pr_u^{-1}(finite set) is finite.
- Let Z ⊂ Δ be the set of t at which Y_t (up to relabelling) lies in C_F or in some Fin(K, u, y). It is countable, and in fact discrete, because Y is holomorphic and non-constant (PR-A). Call t ∉ Z *generic*. (The chain's step 1 is correct as stated.)

### 2.2 Lemma A (no merge, no puncture-move at generic t)
For generic t there is no Q ∈ B_t, lift q, Y_t-copy y at q, and lifted branch c̃ through q such that y is merged along c̃, or y is intact and comp_y is non-constant along c̃ with Q a puncture of the piece of c̃.

*Proof.* This is R7-4 Lemma 1, which I re-checked. In either case there are a piece E, a vertex u ∈ M(E) and a puncture p with comp_y(q) a component of f_u(p) ∈ F. So Y_t ∈ C_F, and t ∈ Z. ∎

### 2.3 Lemma B (new: interior moves at generic t are pure crossings)
Let t be generic. Let Q ∈ B_t with lift q. Let E be a piece at time t with Q ∈ E, i.e. Q is an interior point of E in its own stratum Δ_{G_Q}, with lifted branch Ẽ through q. Let x ∈ M(E) with comp_x(q) ≅ Y_t (an IMOV). Then:
1. for every u ∈ M(E) and every lifted boundary branch c̃ through q, the label u is intact along c̃;
2. if moreover Q is a puncture of the piece E_c of c̃, then comp_u is constant along c̃;
3. let Q = H_t(Q_0), where Q_0 ∈ E_0 := H_t^{-1}(E) is a point at which closure(E_0) meets the closure of another piece D_0 ≠ E_0 (a junction; there are finitely many). Then t ↦ comp_u(q(t)), u ∈ M(E), are holomorphic along a holomorphic choice of lifts, wherever such a choice exists. Concretely, the coordinates of the point Q̂_t ∈ E_t ⊂ ∏M_w over Q_t are holomorphic in t. If the IMOV occurs at this junction for a set of t with an accumulation point in Δ, then the x-coordinate of Q̂_t equals Y_t for all t.

*Proof.*
- Write k := pr_{M(E)}(Q̂) ∈ K(E), so k_x ≅ Y_t.
- (1), (2): Suppose u is merged along c̃, or intact and non-constant with Q a puncture of E_c. By Lemma A's argument, comp_u(q) = k_u ∈ C_F.
  - If u = x, then Y_t ∈ C_F, which is impossible.
  - If u ≠ x, then k ∈ K ∩ pr_u^{-1}(C_F), so Y_t ≅ k_x ∈ Fin(K(E), u, x). This is impossible for generic t.
  - Hence u is intact along c̃, and in the puncture case comp_u is constant along c̃.
- (3): The junction set J_0 := {Q_0 ∈ E_0 : Q_0 ∈ closure(D_0) for some piece D_0 ≠ E_0} is finite. H_t is a stratum-preserving homeomorphism of closures (Lemma B′ of PR-B), so H_t(J_0) is the corresponding junction set at time t.
  - The set {(Q, t) : Q ∈ E_t ∩ closure(D_t)} is the intersection of two analytic families (Lemma R0 of PR-D, and (R1)). It is an analytic set, finite over Δ.
  - t ↦ H_t(Q_0) is a continuous section of it, hence holomorphic. This is the argument of R7-3 Lemma 1(a): a continuous function whose graph lies in a 1-dimensional analytic set finite over Δ is holomorphic off a discrete set, and then everywhere by Riemann extension.
  - The final claim follows from the identity theorem in the coarse space M_x/S_{n_x}, applied to two holomorphic functions of t that agree on a set with an accumulation point. ∎

**What Lemma B leaves.** At generic t, an IMOV at Q is a *pure crossing*:
- every non-constant label of E stays intact along every branch through q, and is constant along every branch for which Q is a puncture;
- the remaining branches through q are pieces of the same stratum Δ_{G_Q} crossing E at Q.

Time-t arguments cannot exclude pure crossings: R7-2 §4.2 gives a local model compatible with (R1), (R2), (i), (ii). So total geodesy at t = 0 is needed. §3 supplies it for crossings inside a single Q-factorial sheet.

## 3. Theorem X: total geodesy forbids Q-Cartier boundary curves through interior points of a piece, inside one sheet

### 3.1 Statement
Let V_0 ⊂ M_g be a closed 2-dimensional totally geodesic subvariety. Smoothness is not needed here. Let Δ_G be a product-type stratum, E a piece of B_0 in Δ_G, and Q_0 ∈ E. Note that Q_0 lies in Δ_G itself, so it is an interior point of E, not a puncture.
- Let 𝓛_0 ⊂ Def(Q_0) be the preimage of closure(V_0) near 0. Let β be a local branch of E at Q_0, with a lift β̃ through 0.
- Let S be an irreducible component of the germ (𝓛_0, 0) containing β̃. Let ν: Ŝ → S be the normalization. Since S is an irreducible germ, ν^{-1}(0) is a single point ŝ_0.
- Let B̂ := ν^{-1}(S ∩ {∏_e s_e = 0}), a curve germ at ŝ_0. Let Ê_1, …, Ê_r be its irreducible components at ŝ_0 that map onto β̃, and C_1, …, C_m the others.

**Theorem X.** There is no holomorphic function G on a neighbourhood of ŝ_0 in Ŝ whose divisor is effective, nonzero, and supported on C_1 ∪ … ∪ C_m. Equivalently, no nonzero effective Q-Cartier divisor is supported on the C_i. In particular:
- (a) no C_i is Q-Cartier at ŝ_0;
- (b) if Ŝ is Q-factorial at ŝ_0 (e.g. smooth, a quotient singularity, or a rational singularity), then m = 0: every boundary curve of S through Q_0 lies over the branch β;
- (c) **(monomial form, valid for any singularity)** there are no integers (n_e)_{e∈E(G)} with Σ_e n_e ord_{Ê_l}(s_e) = 0 for all l, Σ_e n_e ord_{C_i}(s_e) ≥ 0 for all i, and > 0 for some i. Indeed G = ∏ s_e^{n_e} would be such a function.

### 3.2 Proof
Suppose G exists, with div G = Σ c_i C_i, all c_i ≥ 0 and some c_i > 0, defined on a neighbourhood Û of ŝ_0. Then:
- G(ŝ_0) = 0;
- the zero set of G is ∪_{c_i>0} C_i ⊂ B̂, so G has no zeros on Û ∖ B̂;
- G|_{Ê_l} ≢ 0 for every l, since Ê_l is not in the support of the divisor.

Choose a neighbourhood U of Q_0 in M̄_g such that ν^{-1}(preimage of U, intersected with S) ⊂ Û. Shrink U so that the preimage of closure(V_0) ∩ U in Def(Q_0) is a finite union of irreducible components S = S_1, S_2, …, S_k of the germ.

**Step 1 (base point and approximants).**
- Let E^ν be the normalization of E (an open Riemann surface; E ⊂ ∏_w M_w by product type). Let e_0 ∈ E^ν be the point over Q_0 corresponding to β. Choose a closed disc B ⊂ E^ν around e_0 mapping into U, with B ∖ {e_0} mapping into β ∖ {Q_0}.
- Pick P_1 ∈ B ∖ {e_0} generic:
  - Lemma PA applies at P_1;
  - P_1 lies on no other piece;
  - P̃_1 (its lift in β̃) lies on no boundary curve of S other than β̃;
  - ν^{-1}(P̃_1) consists of points on the Ê_l only, where the Ê_l are pairwise disjoint.
- Pick p̂_1 ∈ ν^{-1}(P̃_1), say on Ê_1. The image under ν of a small neighbourhood of p̂_1 is a local branch N of closure(V_0) along E at P_1.
- Apply (PA) with this N: X_n ∈ V_0, lifts X̃_n ∈ S near p̂_1's image, X_n → P_1, and generating pairs (X_n, q_n) whose limit (q_w) has q_j ≠ 0.
- In PR-H the approximants are ν(s_0, τ_n) with s_0 generic and τ_n → 0. So they can be chosen off the at most 1-dimensional analytic set made of the non-normal locus of S and the intersections S ∩ S_i, i ≥ 2.

**Step 2 (the limit disc L).** Let D_n: 𝔻 → M_g be the Teichmüller disc of (X_n, q_n), with D_n(0) = X_n. Since V_0 is totally geodesic, D_n(𝔻) ⊂ V_0. I claim: after passing to a subsequence, D_n → L locally uniformly on 𝔻, where L: 𝔻 → E is holomorphic, non-constant, and L(0) = P_1.

- *Limits stay in Δ_G, in a compact part.* Fix w and put ρ = d_𝔻(0, w). Then d_T(D_n(w), X_n) ≤ ρ.
  - By (Wol), the node curves of P_1 have ℓ_{D_n(w)} ≤ e^{2ρ} ℓ_{X_n} → 0, and every other curve has length bounded below by e^{-2ρ} times its (positive) limit at P_1.
  - By (Ab), every limit point Z of D_n(w) lies in Δ_G, and the length functions of its components are within a factor e^{2ρ} of those of P_1. So Z lies in a compact set K_ρ ⊂ Δ_G ≅ ∏M_w.
  - Also Z ∈ closure(V_0) ∖ M_g ⊂ B_0.
- *Local uniform convergence.* Orbifold charts Def(Z), Z ∈ K_ρ, can be taken of uniform size, since K_ρ is compact in the open stratum. If |w' − w| < r with r small (depending only on ρ), the same length estimate shows that D_n(w') lies in the chart of any limit point Z of D_n(w), for all large n of the subsequence.
  - Each D_n restricted to a small disc around w lifts holomorphically into Def(Z). Indeed, D_n is the image of a Teichmüller disc in T_g, and the component of the preimage in T_g of the chart's interior maps holomorphically onto Def(Z)° (standard description of the Deligne–Mumford boundary charts: Bers, Earle–Marden, Hubbard–Koch; cited).
  - The lifts are bounded, so Montel applies. A diagonal argument over a countable cover of 𝔻 gives the locally uniform limit L, holomorphic in charts, with values in B_0 ∩ Δ_G and L(0) = P_1.
- *Non-constant.* By (Fl) and q_j ≠ 0, the j-component of L(w) is A_w·(Y_j(P_1), q_j). Here w ↦ A_w·(Y_j, q_j) =: τ(w) is the Teichmüller disc of (Y_j(P_1), q_j) in M_j := M_{g_j,n_j}. It is non-constant.
- *Image in E.* B_0 ∩ Δ_G is a 1-dimensional analytic set, and L^{-1} of each of its finitely many irreducible components meeting L(closed disc of radius R) is analytic. These preimages cover the disc, so one of them is everything. P_1 lies only on E. Hence L(𝔻) ⊂ E. Since 𝔻 is normal and L(𝔻) ⊄ Sing(E), L lifts to E^ν; I keep the name L.

**Step 3 (L: 𝔻 → E^ν is surjective).**
- Let τ̃: 𝔻 → T(Y_j) be the Teichmüller disc lifting τ. By (Prop) its image Δ̃ is a closed 1-dimensional submanifold, and its Mod-translates form a locally finite family.
- τ(𝔻) ⊂ f_j(E) ⊂ C_j° := f_j(Ē) ∩ M_j, which is an irreducible closed analytic curve in M_j (j ∈ M(E), since τ is non-constant).
- So Δ̃ is an irreducible component of the preimage 𝒞 of C_j° in T(Y_j). By local finiteness, the image of Δ̃ in M_j is closed and analytic, hence equal to C_j°.
- With Γ := Stab_{Mod}(Δ̃), the map 𝔻/Γ → C_j° (via τ̃) is proper.
- τ factors through the normalization Ĉ_j of C_j°, and f_j: E^ν → Ĉ_j is a finite map of normal curves.
- The set Λ of holomorphic λ: 𝔻 → E^ν with f_j∘λ = τ is finite, with at most deg f_j elements: a lift is determined by its value at one point over an unbranched value.
- Γ acts on Λ by precomposition, since τ∘γ = τ. So Γ_L := Stab_Γ(L) has finite index, and L descends to L̄: 𝔻/Γ_L → E^ν.
- f_j∘L̄ is proper (finite index in a proper map), so L̄ is proper: L̄^{-1}(K) is a closed subset of (f_j L̄)^{-1}(f_j K).
- A proper non-constant holomorphic map to the connected Riemann surface E^ν is surjective. In particular e_0 ∈ L(𝔻).

**Step 4 (a path to the crossing point).**
- Let W be the connected component of L̄^{-1}(int B) containing [0]. Then L̄|_W: W → int B is proper and non-constant, hence surjective. Pick [w*] ∈ W with L̄([w*]) = e_0.
- Join [0] to [w*] by a path in W and lift it to a path π from 0 to w* in 𝔻. Path lifting holds for quotients by properly discontinuous actions (Bredon II.6; cited).
- Let Ω be a connected relatively compact open neighbourhood of π with L(Ω̄) ⊂ ν-image of B ⊂ U. Then L(π) ⊂ B, and w* ∈ Ω with L(w*) = e_0, i.e. L(w*) = Q_0 approached along β.

**Step 5 (Hurwitz).**
- For large n, D_n(Ω̄) ⊂ U ∩ V_0 by uniform convergence. Lift D_n|_Ω to D̃_n: Ω → Def(Q_0) as in Step 2, with D̃_n(0) = X̃_n.
- D̃_n(Ω) lies in the interior part of 𝓛_0 = S_1 ∪ … ∪ S_k. The sets D̃_n^{-1}(S_i) are analytic subsets of the connected Ω covering it, so one of them is Ω. Since X̃_n lies only in S, D̃_n(Ω) ⊂ S.
- D̃_n(Ω) ⊄ non-normal locus (it contains X̃_n), so D̃_n lifts to D̂_n: Ω → Ŝ, with D̂_n(Ω) ⊂ Û ∖ B̂.
- Hence **G∘D̂_n has no zeros on Ω**.
- Embed Û in some C^M. By Montel, a subsequence D̂_n → L̂ locally uniformly on Ω, where ν∘L̂ is a lift of L. Then:
  - L̂(w*) ∈ ν^{-1}(0) = {ŝ_0}, so **G∘L̂(w*) = 0**;
  - near 0, L̂ takes values in ν^{-1}(β̃-lift of L), which near the generic point P̃_1 is the disjoint union of the Ê_l. By connectedness L̂ maps a neighbourhood of 0 non-constantly into one Ê_l, where G ≢ 0. So **G∘L̂ ≢ 0**.
- By Hurwitz, G∘L̂ has no zeros on Ω, which contradicts G∘L̂(w*) = 0. ∎

**Remarks.**
1. *Intuition.* The Teichmüller discs D_n are holomorphic curves in the interior of the sheet S that converge to the whole branch β of E, through Q_0. Any Q-Cartier curve C through Q_0 meets β with positive local intersection number, so it would meet D_n. But C lies in the boundary and D_n does not. Total geodesy enters only through the existence of these discs: Lemma PA for positive area, then (Fl) and (Prop) to make L sweep all of E.
2. *Non-product strata.* The proof uses product type only to have the global coordinate f_j on E. For non-product G one would work on the lifted piece in ∏M_w. I have not checked this.
3. *Sanity check.* In the local crossing model of R7-2 §4.2 (the t = 0 version), S = {s_1 = z s_2} ⊂ C³ is smooth, E is the z-axis, and D = {z = s_1 = 0}. Theorem X(b) excludes it: G = z|_S has zero set exactly D. At interior points of boundary divisors of M̄_{0,5}, and in the quintic example, no second boundary curve passes through an interior point of a piece, so nothing is contradicted there.

## 4. Consequences for the crossing (IMOV) obstacle of MS8

### 4.1 Lemma S (sheets are topological and are transported by H_t)
For Q ∈ B_t, the irreducible components ("sheets") of the germ of closure(V_t) at Q are in canonical bijection with the elements of lim← π_0(V_t ∩ W), taken over neighbourhoods W of Q and keeping only components whose closure contains Q. A boundary branch b at Q lies in the sheet corresponding to a component if b ∖ {Q} lies in the closure of that component, for all W.

Consequently H_t maps sheets at Q_0 bijectively onto sheets at H_t(Q_0), compatibly with the boundary branches they contain.

*Proof.*
- For an analytic germ (X, Q), the irreducible components correspond to lim← π_0(Reg(X) ∩ W). This is the standard local description: a germ is irreducible iff its regular part is locally connected at Q.
- Here X = closure(V_t), and Reg(X) ∩ W ∖ V_t lies in the 1-dimensional boundary. That set has real codimension 2 in the manifold Reg(X), so removing it does not change π_0.
- The description is purely topological in the pair (closure(V_t), V_t). By (R2), H_t is a homeomorphism of pairs (closure(V_0), V_0) → (closure(V_t), V_t) that preserves strata and pieces (PR-B). ∎

### 4.2 Corollary X′ (crossings inside a Q-factorial sheet do not occur, at any time)
Let E_0 be a piece of B_0 in a product-type stratum, Q_0 ∈ E_0, and D_0 ≠ E_0 a piece with Q_0 ∈ closure(D_0). Suppose some sheet S of closure(V_0) at Q_0 contains a branch of E_0 and a branch of D_0. Suppose also that the normalization Ŝ is Q-factorial at the point over Q_0, or more generally that the monomial criterion of Theorem X(c) applies. Then we get a contradiction. So such (Q_0, E_0, D_0, S) do not exist.

Transported by Lemma S: let t ∈ Δ be arbitrary. If E_t := H_t(E_0) and D_t meet at Q_t = H_t(Q_0) inside a common sheet, then E_0 and D_0 meet at Q_0 inside a common sheet. The Q-factoriality condition is imposed at t = 0.

*Proof.* The lifted branch of D_0 in S gives a boundary curve C of Ŝ through ŝ_0 that does not lie over the branch β of E_0. If Ŝ is Q-factorial, some multiple mC is Cartier, and G := a local equation of mC contradicts Theorem X. ∎

### 4.3 What this does to the IMOV endpoint of the chain
Combine with Lemma B. Suppose Y is non-constant and t is generic. Then an IMOV at Q_t, with the Y_t-network entering E_t from a piece D_t on which x is constant, is a pure crossing at the junction Q_t = H_t(Q_0). By Corollary X′ it is impossible if E_0 and D_0 share a Q-factorial sheet at Q_0. **The crossing obstacle therefore reduces to:**
- **(Cr1) two-sheet crossings:** E_0 and D_0 meet at Q_0 but lie in different sheets of closure(V_0) at Q_0. Every sheet containing E_0's branch has boundary lying over E_0 at Q_0 (Theorem X(b), when Q-factorial). The network passes from E to D through a point where two different local sheets of closure(V_t) touch.
- **(Cr2) non-Q-Cartier crossings:** the common sheet has a non-Q-factorial (hence non-rational) normal singularity over Q_0, and the monomial criterion fails. That is, the normalized order vectors (ord_C(s_e)/ord_{Ê}(s_e))_e of the other boundary curves C positively span, modulo constants, a linear subspace.

Neither is excluded here.
- For (Cr1), local Krull/Hurwitz arguments cannot help: the two sheets are separate analytic germs, and the discs in the E-sheet never see the D-sheet.
- For (Cr2), the discs D_n may pass "around" C through the exceptional curves of a resolution.

**Note on Proposition K's endpoint.** If Prop K's MOV branch is "touching" (Q_0 an interior point of E_b), and Q_0 is also on the closure of the STAY piece through which K_0 arrives, in the same Q-factorial sheet as E_b, then Theorem X excludes this configuration at t = 0 already. So for those V_0, Prop K's endpoint is MERGE, puncture-MOV, or a two-sheet / non-Q-Cartier touching. This partially answers R7-2 Open question 2.


### R8-2 (excerpt). Lemma U and the generic-time trichotomy (from round8_q2, verbatim, §§1–3)
## 1. Conventions and cited facts

- Classes of pointed curves are compared in the coarse space 𝔐 := M_{g_i,n_i}/S_{n_i}. "≅ Y" means equal class.
- For a stable graph G, 𝓦_G ⊂ ∏_w M̄_w × Δ is the lifted family of R7-5 (P2). It is analytic by (R1) and proper over Δ. "W" always denotes a 2-dimensional irreducible component of some 𝓦_G.
- By R7-5 (P4), applied at every t (the argument is symmetric in t by (R2), and closure(V_t) is compact analytic by (R1)): every fibre W_t is non-empty and of pure dimension 1. Each 1-dimensional component D of W_t is the closure of a piece E at time t, so (Rig) applies to E. Write M(D) := M(E) and K(D) := K(E).
- Cited from memory (standard):
  - **Remmert's proper mapping theorem.**
  - **Cartan–Remmert.** For a holomorphic map Φ of complex spaces, {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
  - **Stein factorization** (Grauert–Remmert). A proper holomorphic map f: X → S factors as X → T → S, with X → T proper, surjective and with connected fibres, and T → S finite. If X is normal, so is T.
  - **Normal surfaces** have isolated singularities.

## 2. Lemma U (uniformity under (Rig)) — proved

**Lemma U.** Assume (R1), (R2) and (Rig). Let W be a 2-dimensional irreducible component of 𝓦_G. There are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, with the following property. For **every** t ∈ Δ and **every** 1-dimensional component D of W_t:
- M(D) = M_W and K(D) = K_W;
- every vertex u ∉ M_W is constant on D;
- D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*

**Step 1 (generic moving set).** Let n: W^ν → W be the normalization, a normal surface. Let W^ν →a T →b Δ be the Stein factorization of t∘n, which is proper. T is a normal, hence smooth, curve and b is finite.
- **Critical values are discrete.** Let C be an irreducible curve of critical points of a on W^ν_reg. Then d(a|_C) = 0, so a is constant on C. The singular points of W^ν are isolated. Hence the set of critical values of a (images of Sing W^ν, of isolated critical points, and of critical curves) is discrete in T.
- **Generic fibres are irreducible.** For τ ∈ T outside a discrete set, a^{-1}(τ) is a smooth, compact, connected curve, hence irreducible.
- **Fibres of W.** Since n is finite and surjective, for every t, W_t = ⋃_{τ ∈ b^{-1}(t)} n(a^{-1}(τ)). Every component of W_t is the image of a component of some a^{-1}(τ). For generic t the components of W_t are exactly the irreducible curves n(a^{-1}(τ)), τ ∈ b^{-1}(t).
- **The dichotomy for a vertex u.** Put Φ_u := (pr_u∘n, a): W^ν → M̄_u × T and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert.
  - If R_u = W^ν: let K be a component of a fibre a^{-1}(τ) and x ∈ K a point on no other component. The Φ_u-fibre through x lies in a^{-1}(τ) and is 1-dimensional at x, so it contains the germ of K at x. Hence pr_u is constant on K. So u is constant on every component of every fibre of a, and therefore on every component of every W_t.
  - If R_u ≠ W^ν: then dim R_u ≤ 1. Every fibre component on which pr_u is constant lies in R_u, and the components of R_u are locally finite. So this happens only for τ in a discrete subset of T.
- Put M_W := {u : R_u ≠ W^ν}. Then for t outside a discrete set Z_W ⊂ Δ, every component of W_t has moving set exactly M_W. For every t and every component of W_t, every u ∉ M_W is constant on it. M_W ≠ ∅, since components of W_t are curves.

**Step 2 (one image curve).** Let Σ := (pr_{M_W}, t)(W) ⊂ ∏_{u∈M_W} M̄_u × Δ. It is closed, analytic and irreducible (Remmert; the map is proper on W). It has dimension 2, since t is non-constant on it and its generic fibres are curves.
- For t ∉ Z_W and a component D of W_t, pr_{M_W}(D) is the closure of the image of the piece, i.e. K(D).
- By (Rig), K(D) belongs to the finite list {α^{-1}K : α ∈ Aut(G), (G, αM_W, K) ∈ 𝒦}, with factors relabelled by α. Call its members K_1, …, K_N.
- So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
- Σ is irreducible of dimension 2, so it lies in one K_j × Δ, and equals it since both are irreducible of dimension 2. Put K_W := K_j.
- For each u ∈ M_W, pr_u|_{K_W} is non-constant, because K_W = K(D) for a generic-time component D with u ∈ M(D).

**Step 3 (all times).** Let t be arbitrary and D a component of W_t.
- By Step 1 the vertices outside M_W are constant on D. So D ⊂ pr_{M_W}^{-1}(pr_{M_W}(D)) ∩ {coordinates outside M_W constant}.
- pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, so it is a point or all of K_W. If it were a point, every coordinate would be constant on the curve D, which is absurd.
- So pr_{M_W}(D) = K_W. Every u ∈ M_W is non-constant on D (end of Step 2), so M(D) = M_W and K(D) = K_W.
- D is an irreducible curve inside the irreducible curve K_W × {c_D}, so the two are equal. Here c_D ∈ ∏ M_u, because D is the closure of a subset of ∏_w M_w and the coordinates of c_D are constant on D. ∎

**Corollaries.**
- **U1 (L1′ with its converse; no non-product pathology).** For each W and vertex u, the following are equivalent:
  - u is constant on one component of one fibre;
  - u ∉ M_W;
  - u is constant on all components of all fibres.

  In particular the situation of R7-5 §1.4 (u constant on E_0 but non-constant on σE_0 inside the same W) cannot occur under (Rig). Consequently, for a component W' through a point p obtained from W by ρ ∈ Aut(G): M_{ρW} = ρM_W and K_{ρW} = ρK_W.
- **U2 (t-independent image curves; the earlier worker's Lemma 6, repaired).** The partial file's Lemma 6 asserts that "M is the same for all t by L1′". L1′ gives only one direction, and for non-product G the fibres of W can have components with different moving sets unless (Rig) is used as above. Lemma U is the correct statement.
- **U3 (puncture values).** For each W, the values pr_{M_W}(ν(p)) at punctures p of components of W_t lie in K_W ∩ ∂(∏ M̄_u). This is a finite set independent of t.
- **U4 (constant-vertex value curves).** For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t.

## 3. Generic times and the trichotomy (Theorem 1) — proved

From now on assume, for contradiction, that **Y is non-constant**. Y: Δ → 𝔐 is holomorphic by PR-A, so its graph is an irreducible curve.

**The finite set 𝔉 ⊂ 𝔐 (independent of t).**
- Let 𝒫_1 be the set of points of K ∩ ∂(∏_{u∈M} M̄_u), over all (G, M, K) ∈ 𝒦 and all Aut(G)-relabellings. It is finite: K is an irreducible compact curve not contained in the boundary.
- Let A_1 be the set of classes of the smooth components, with their special points, of all coordinates of points of 𝒫_1.
- Let 𝒫_2 be the set of points κ ∈ K such that the class of some coordinate pr_z(κ), z ∈ M, lies in A_1. It is finite, because pr_z|_K is non-constant for z ∈ M (Lemma U).
- Let 𝔉 be the set of classes of the smooth components of all coordinates of the points of 𝒫_1 ∪ 𝒫_2.

**The set Z.** Z is the set of t ∈ Δ such that one of the following holds:
- Y_t ∈ 𝔉;
- (Y_t, t) lies on the image in 𝔐 × Δ of some curve Γ_{W,u} (u ∉ M_W, M_u of type (g_i,n_i)) that is not the graph of Y.

Each W, and each such pair (W,u), contributes a discrete set: in the first case because Y is non-constant, in the second because two distinct irreducible curves meet discretely. The components W are locally finite over Δ. Hence **Z is discrete** in Δ.

Call a pair (W,u) with Γ_{W,u} ↦ graph(Y) a **Y-vertex**.

**Theorem 1.** Let t ∉ Z, Q ∈ B_t, q a lift of Q in Def(Q), and y a Y_t-copy of q (comp_y(q) ≅ Y_t). Let b̃ be a lifted branch through q of a branch b of B_t at Q. Let E be the piece of b at time t, with graph G_b and component W ⊃ E. Then exactly one of the following holds.
- **(STAY)** Every edge at y is pinched along b̃, y is a constant vertex of E, and (W, y) is a Y-vertex.
- **(IMOV)** Q is an interior point of E (so Q ∈ Δ_{G_b}), and y ∈ M_W. Moreover, for every z ∈ M_W and every other lifted branch b̃′ through q, z is neither merged along b̃′ nor non-constant at a puncture along b̃′.

In particular, a Y_t-copy is never merged along a branch (**MERGE excluded**), and never intact and non-constant at a puncture (**puncture-MOV excluded**).

*Proof.*
1. **Merge.** Suppose some edge at y is unpinched along b̃. By R7-1 Lemma 1(a) (= R7-4 Lemma 1), the point p of Ē over Q is a puncture, the vertex u ∋ y of G_b is non-constant, and comp_y(q) is a component, with the same special points, of f_u(p).
   - By Lemma U, u ∈ M_W and pr_{M_W}ν(p) ∈ 𝒫_1.
   - So Y_t ∈ A_1 ⊂ 𝔉, contradicting t ∉ Z.
2. **Puncture-move.** Suppose y is intact, {y} is non-constant, and Q ∉ Δ_{G_b}. Then p is a puncture and f_y(p) = comp_y(q) (R7-1 Lemma 1(b)). So Y_t ∈ A_1, again a contradiction.
3. **Constant.** Suppose y is intact and constant on E. Its value is comp_y(q) ≅ Y_t, so (Y_t, t) lies on the image of Γ_{W,y}. Since t ∉ Z, Γ_{W,y} maps onto graph(Y): this is STAY.
4. **Remaining case.** Here y is intact and non-constant, and Q ∈ Δ_{G_b}. So y ∈ M_W, and κ := pr_{M_W}(lift of Q) ∈ K_W.
   - Suppose some z ∈ M_W were merged, or moving at a puncture, along another branch b̃′ through q. Then, as in 1–2, comp_z(q) = pr_z(κ) has class in A_1. So κ ∈ 𝒫_2, and Y_t ≅ pr_y(κ) lies in 𝔉, a contradiction. ∎

**Remark.** Theorem 1 never compares two copies. At a generic t, *every* Y_t-copy obeys it, whatever the automorphisms of Q. Twins matter only when information is transported between t = 0 (where total geodesy is available) and generic t. That is the subject of §4.



### PR-I. The quintic-cover example, the Krull/twin mechanism, Lemma D (merge or twin), the Pinning Lemma and Theorem 4 (from round6_q6, verbatim, sections 2–4). The example surface is NOT smooth (it has a coarse A_1 point at y^5 = x^5 − x and two fixed-locus sheets crossing at the Fermat quintic; proved in round6_q3), so it is a test case, not an admissible V_0.

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




### R8-3 (excerpt). Theorem N and Corollary T (Krull pair at one lift, any automorphisms) (from round8_q3, verbatim, §§0–4.1)
## 0. Setting and conventions

The setting is MS8 exactly as in the task: (R1), (R2) with H_0 = id; V_0 is smooth, closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; ∂V_t has dimension 1; π_i(∂V_t) = {Y_t}; and (Rig) holds.

Notation:
- B_t := closure(V_t) \ V_t = closure(V_t) ∩ ∂M̄_g. This is compact, since V_t is closed in M_g. By (R2), B_t = H_t(B_0), and H_t preserves strata.
- A *coarse piece* (at time 0) is a 1-dimensional irreducible component D of B_0 ∩ Δ_G, for some stable graph G. There are finitely many. We write D_t := H_t(D).
- For Q ∈ B_t, Def(Q) is the versal deformation germ, with smoothing parameters s_e and Aut(Q) acting. Points of the locus {s_e = 0 for all e} have components comp_x labelled by x ∈ V(G_Q). A lifted branch b̃ has a constant *pattern* S_b̃ = {e : s_e ≡ 0 on b̃}.
- A label y is *intact* along b̃ if every edge at y lies in S_b̃, and *merged* otherwise.
- [Z] denotes the class of an n_i-pointed curve in M_{g_i,n_i}/S_{n_i}. A *Y_t-copy* is a component Z with [Z] = [Y_t].
- By PR-A (re-checked; it uses only (R1), (R2)), t ↦ Y_t is holomorphic, so t ↦ [Y_t] is holomorphic.

**Standard fact used (cited from memory: partial normalization of a nodal family along node sections).** For S ⊂ E(G_Q), let G_S be G_Q with the edges not in S contracted. Then there is a holomorphic map Π_S : {s_e = 0 for all e ∈ S} → ∏_{w∈V(G_S)} M̄_w with the following properties.
- It is obtained by normalizing the nodes in S of the fibre curves.
- On the locus where exactly the edges of S vanish, it takes values in ∏ M_w and ξ_{G_S}∘Π_S equals the quotient map.
- At 0, the w-coordinate is the curve glued from the comp_x(0), x ∈ w, along the edges outside S that join them. Its marked points are the half-edges of S-edges at w.

**Finite sets supplied by (Rig).**
- F := ⋃_{(G,M,K)∈𝒦} K ∩ ∂(∏_{u∈M} M̄_u). This set is finite, because each K is an irreducible curve not contained in the boundary.
- F′ := the set of isomorphism classes, as pointed curves with unordered special points, of all smooth components of all coordinates of elements of F. It is finite.
- **Fact (P), the puncture lemma from chain step 3, re-checked.** Let p be a puncture of a piece E at any time. Then pr_{M(E)}ν(p) ∈ F. Indeed, constant vertices take their value in M_w, so some coordinate in M(E) lies in the boundary. Hence pr_{M(E)}ν(p) ∈ K(E) ∩ ∂, which is a subset of F.

---

## 1. Lemma 1 (the Y-locus is analytic)

Put Ŷ := {(Q,t) ∈ M̄_g × Δ : Q has a Y_t-copy}. Then Ŷ is a closed analytic subset of M̄_g × Δ.

*Proof.*
1. Fix a stable graph G of genus g and a vertex v of type (g_i,n_i). Put A_{G,v} := {(z,t) ∈ ∏_w M̄_w × Δ : [z_v] = [Y_t]}. This is the preimage of the graph of the holomorphic map t ↦ [Y_t] under the holomorphic map (z,t) ↦ ([z_v], t). Hence it is closed analytic.
2. The map ξ̄_G × id is finite, hence proper. By Remmert's proper mapping theorem, (ξ̄_G × id)(A_{G,v}) is closed analytic.
3. Ŷ is the finite union of these images over all pairs (G, v).
   - ⊆: let Q be a curve with a Y_t-copy at the vertex v of its own dual graph. Take z = (normalized components) ∈ ∏ M_w.
   - ⊇: let (z,t) ∈ A_{G,v}. Since z_v ≅ Y_t is smooth, ξ̄_G(z) has the irreducible component z_v. Its special points are exactly the n_v half-edges of v, and nodes inside the other z_w do not affect it. So z_v is a Y_t-copy of ξ̄_G(z). ∎

Put 𝓑 := closure(𝒱) ∩ (∂M̄_g × Δ). It is analytic by (R1), and 𝓑 = H(B_0 × Δ) by (R2). Put 𝓝 := Ŷ ∩ 𝓑, which is closed analytic. Its fibre is 𝓝_t = N_t := {Q ∈ B_t : Q has a Y_t-copy}.

---

## 2. Lemma 2 (dichotomy for coarse pieces)

Let D be a coarse piece. Exactly one of the following holds.
- (N) For every t, every point of H_t(closure D) has a Y_t-copy.
- (F) There is a countable set Z_D ⊂ Δ such that for t ∉ Z_D only finitely many points of H_t(closure D) have a Y_t-copy.

*Proof.*
1. **B_0 is pure 1-dimensional.**
   - Locally in Def(Q), every irreducible component X of the preimage of closure(V_0) is 2-dimensional and contains points of V_0. (At a point of X lying on no other component, nearby points of V_0 must lie on X.)
   - So ∏ s_e is not identically 0 on X, and X ∩ {∏ s_e = 0} has pure dimension 1 (Krull).
   - Also dim B_0 ≤ 1, since V_0 is dense in closure(V_0).
2. **The set D°.** Let D° be D minus the finitely many singular points of the compact curve B_0. Then D° is connected, being an irreducible curve minus a finite set. It is also open in B_0, since near a smooth point of B_0 lying on D, B_0 coincides with D.
3. **The set M_D.** M_D := H(D° × Δ) is open in 𝓑 and is a connected topological 4-manifold. Hence 𝓑 has pure dimension 2 along M_D.
   - Sing(𝓑) ∩ M_D is a closed subset of covering dimension ≤ 2. It does not disconnect the connected 4-manifold M_D (a closed set of dimension ≤ n−2 does not separate a connected n-manifold; Hurewicz–Wallman, cited from memory).
   - So M_D ∩ Reg(𝓑) is connected. It therefore lies in the regular part of a single irreducible component W of 𝓑, and M_D ⊂ W.
4. **Case W ⊂ 𝓝.** Then M_D ⊂ 𝓝. Since 𝓝 is closed and H_t(closure D) = closure(H_t(D°)), this is (N).
5. **Otherwise.** W ∩ 𝓝 is a proper analytic subset of the irreducible 2-dimensional W, so its dimension is ≤ 1.
   - Its irreducible components form a locally finite, hence countable, family. Let Z_D be the countable set of t such that some component lies in the fibre over t.
   - For t ∉ Z_D, the fibre (W ∩ 𝓝)_t is discrete. It is also compact, being closed in the compact 𝓑_t. So it is finite.
   - It contains N_t ∩ H_t(D°). Adding the finitely many points of H_t(closure D \ D°) gives (F).
6. **(N) and (F) exclude each other.** H_t(closure D) is infinite. ∎

Define:
- 𝒩 := {D : (N) holds}, and C_t := ⋃_{D∈𝒩} H_t(closure D).
- Every component of ∂V_0 lies in 𝒩, since vertex i ≡ Y_t on ∂V_t. Hence closure(∂V_t) ⊂ C_t.

**Remark 2.1.** Let D ∈ 𝒩 and let E be any piece at time t over D_t. Then some vertex w of E has f_w ≡ Y_t, a constant on E. Indeed, E is the union of the finitely many analytic sets {f_w ≅ Y_t}, so one of them is all of E.

Note: 𝒩 and C_t are defined without choosing or tracking any copy. Twins play no role in them.

---

## 3. Theorem N (how a copy can leave the network at a generic time)

Assume Y is non-constant. Define:
- Z_1 := ⋃_{D∉𝒩} Z_D, which is countable;
- Z_2 := {t : [Y_t] ∈ F′}, which is discrete, since [Y] is holomorphic and non-constant;
- Z := Z_1 ∪ Z_2. Call t ∉ Z *generic*.

**Theorem N.** Let t be generic. Let Q ∈ B_t with lift 0 ∈ Def(Q), let y be a label with comp_y(0) ≅ Y_t, and let b be any branch of B_t at Q, with a lift b̃ through 0 of pattern S. Then y is intact along b̃, and exactly one of the following holds.
- (STAY) comp_y ≡ Y_t along b̃. Then the coarse piece D′ with b \ {Q} ⊂ D′_t lies in 𝒩, so b ⊂ C_t.
- (IMOV) S = E(G_Q), so Q is an interior point of the piece of b, which lies in the stratum of Q. Moreover comp_y is non-constant along b̃.

Moreover N_t \ C_t is finite.

*Proof.*
1. **Setting up the piece.** Let G_b := G_S. Π_S(b̃ \ 0) is a 1-dimensional germ in ξ_{G_b}^{-1}(closure(V_t) ∩ Δ_{G_b}). So it lies in a piece E at time t, and Π_S(0) = ν(p) for a point p ∈ Ē. Let u be the vertex of G_b containing y.
2. **Merge is impossible.** Suppose an edge at y is not in S.
   - f_u(p) is the curve glued from the comp_x(0), x ∈ u. It has a node, so f_u(p) ∈ ∂M̄_u.
   - Hence p is a puncture. Also u ∈ M(E): a constant f_u would take its value in M_u (Lemma C2 of PR-C).
   - comp_y(0), with all its special points (the nodes inside u and the legs from S-edges), is a component of f_u(p).
   - By Fact (P), f_u(p) is a coordinate of an element of F. So [Y_t] ∈ F′, which contradicts t ∉ Z_2.
3. **Puncture-move is impossible.** Suppose y is intact, S ≠ E(G_Q), and comp_y is non-constant along b̃.
   - Then u = {y}, and f_u = comp_y along Π_S(b̃) is non-constant, so u ∈ M(E).
   - Some edge outside S is contracted into a vertex w, so f_w(p) is nodal and p is a puncture.
   - By (P), f_u(p) = comp_y(0) ∈ F′. This again contradicts t ∉ Z_2.
4. **The remaining cases.** y is intact. If comp_y is constant along b̃, every point of b has a Y_t-copy. So N_t ∩ D′_t is infinite, and since t ∉ Z_{D′}, Lemma 2 gives D′ ∈ 𝒩. Otherwise we are in (IMOV).
5. **Finiteness.** N_t \ C_t is finite by Lemma 2 (F) and t ∉ Z_1. ∎

**Corollary N1.** Let Y be non-constant and t generic. Suppose that no point of C_t carries an IMOV copy. Then:
- C_t is open and closed in B_t, so it contains the connected component B_t^∂ of B_t that contains ∂V_t;
- every Y_t-copy at every point of B_t^∂ is intact and constant along every branch of B_t there.

*Proof.* At Q ∈ C_t, every branch is STAY for the Y_t-copy that Q carries, so it lies in C_t. Hence C_t is open in B_t, and it is closed as a finite union of compact sets. ∎

---

## 4. Consequences

### 4.1 Corollary T (twin criterion under (Rig); no (O), no Lock, no restriction on automorphisms)

Let J ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G′}. Let 𝒞 and j(S) be as in PR-I Theorem 4. Assume:
- (Tw1) there is a neighbourhood U of J with B_0 ∩ U ⊂ ∂V_0 ∪ {J};
- (Mg) for all S ≠ S′ in 𝒞, some edge at j(S) is not in S′.

Then MS8 holds: Y_t = Y_0 for all t.

*Proof.*
1. Suppose Y is non-constant and take t generic. Put J_t := H_t(J) ∈ closure(∂V_t), and let q be a lift of J_t.
2. A branch of ∂V_t at J_t lifts to a branch β̃ through q, with pattern S ∈ 𝒞. By Lemma D(1) of PR-I, y := j(S) is intact and comp_y(q) ≅ Y_t.
3. J_t ∉ Δ_Γ, so there is an edge e ∉ S. Let X be an irreducible component, at q, of the preimage of closure(V_t) containing β̃.
   - s_e is not identically 0 on X, since it is nonzero on β̃ \ q.
   - So X ∩ {s_e = 0} is pure 1-dimensional through q (Krull). It contains a branch b̃ ≠ β̃ with e ∈ S_b̃.
4. By (Tw1), transported by H_t, b̃ lies over ∂V_t. So S′ := S_b̃ ∈ 𝒞, and S′ ≠ S because e ∈ S′ \ S.
5. By (Mg), y is merged along b̃. This contradicts Theorem N. ∎

**Remarks.**
- This is PR-I Proposition 3 / Theorem 4 with (O), (Tw2)(iii) and all Teichmüller-curve input replaced by (Rig).
- It holds whether or not Aut(J) swaps the twins. Theorem N concerns every copy at the same lift q, so the identity of "the" tracked copy never enters.
- In the quintic example, 𝒞 = {{e_1},{e_2}}, j({e_1}) = A has e_1 ∉ {e_2}, and symmetrically. So (Mg) holds.



### R8-5. Twin step under (U_J): covering lemma, Theorems A and B, Corollary C, Proposition D (from round8_q5, verbatim, §§1–6)
## 1. Set-up and readings

I adopt the task's readings (R1) and (R2), with H_0 = id, and the setting of MS8. I add the following conventions.

**(C1) Charts (standard; cited from memory).** Let J be a stable curve.
- Def(J) is its versal deformation germ. Aut(J) acts on it, and we may take the action to be linear in suitable coordinates (Cartan).
- Fix an Aut(J)-invariant open ball B ⊂ Def(J) around 0 and an Aut(J)-invariant Hermitian norm |·|. Then q : B → U := B/Aut(J) is a neighbourhood of J in M̄_g.
- On U use the quotient metric d̄(q(p), q(p')) = min_α |p − α p'|. It induces the topology of U. Every lift of a point realises the distance to the orbit of any other point.
- s_e (e ∈ E(G_J)) are the smoothing parameters. B° := B ∖ {∏ s_e = 0} lies over U ∩ M_g.
- For a vertex y, L_y := {s_e = 0 for all edges e at y}. It is closed, and F_y : L_y → M_{g_y,n_y}/S_{n_y} (coarse) is continuous (holomorphic into the coarse space).
- For α ∈ Aut(J): α L_y = L_{αy} and F_y(αp) = F_{α^{-1}y}(p) (K3 of R7-3).
- On product sets B × Δ_ε, the map q × id is again written q.

**(C2) The track at a junction (reading of Proposition K / (K\*) of R7-6 / the interpretation in R7-3 §1).** Let J = J^k be a junction between D := D^{k−1} and D' := D^k. Let β̃ ⊂ Def(J) and β̃' ⊂ Def(J) be lifts of the branches of D and D' at J, and let x be a chart vertex with:
- c_{k−1} = {x} along β̃, and c_k = {x} along β̃';
- c_{k−1} constant on D and c_k constant on D'.

Shrinking B, assume B_0 ∩ U is a finite union of branches through J (cone structure). Fix generic points z̃_1 ∈ β̃ ∖ 0 and z̃_2 ∈ β̃' ∖ 0, and put z_j = q(z̃_j). The track datum (TD_J) is: for every ρ > 0 there are a path γ : [a,b] → V_0 ∩ U and a continuous lift γ̃ : [a,b] → B° such that:
- (T1) |γ̃(a) − z̃_1| < ρ and |γ̃(b) − z̃_2| < ρ;
- (T2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_b = z_2;
- (T3) for every s with d̄(z_s, J) ≥ r_1 (r_1 > 0 arbitrary, fixed before ρ), there is a lift ẑ_s ∈ L_x of z_s with |γ̃(s) − ẑ_s| < ρ and F_x(ẑ_s) ≅ Y_0. One may take ẑ_a = z̃_1 and ẑ_b = z̃_2.

(T3) is the chart form of (K\*)(b): "Σ_i ↔ a single component of z_s of class Y_0". Here the region of γ̃(s) corresponding to Σ_i is the chart region x, which is constant along the continuous lift γ̃. Away from J the nearest lift of z_s is well defined up to the stabiliser, which is harmless; see Lemma 3. Proposition K yields (T1)–(T3) "modulo routine marking details" (PR-H). I have not re-proved Proposition K, and (TD_J) is the precise form in which I use it.

**(C3) The deformed family near J.**
- Put 𝒱_U := 𝒱 ∩ (U × Δ_ε) and ℬ° := B° × Δ_ε. Then q^{-1}(𝒱_U) ⊂ ℬ°.
- V_t is closed in M_g, so closure(𝒱) ∩ (M_g × Δ) = 𝒱.
- Let 𝒞° be the connected component of q^{-1}(𝒱_U) that contains γ̃ × {0}. Passing to a subsequence ρ_n → 0, it is the same for all the paths of (TD_J), because q^{-1}(𝒱_U) has finitely many components meeting a neighbourhood of 0. (I only use this for a single ρ at a time, so the subsequence is harmless.)
- Γ := {α ∈ Aut(J) : α𝒞° = 𝒞°}, and Γ_x := {α ∈ Γ : αx = x}.

**Fact 0.** q|_{𝒞°} : 𝒞° → 𝒜 := q(𝒞°) is the quotient map by Γ, and 𝒜 is a connected component of 𝒱_U.

*Proof.*
- q restricted to the saturated set q^{-1}(𝒱_U) is open and closed onto 𝒱_U. So q(𝒞°) is open, closed and connected, i.e. a component.
- If p, p' ∈ 𝒞° and q(p) = q(p'), then p' = αp for some α ∈ Aut(J). Then α𝒞° is a component of q^{-1}(𝒱_U) containing p', so α𝒞° = 𝒞°, i.e. α ∈ Γ. ∎

Let K ⊲ Γ be the kernel of the action of Γ on 𝒞°, i.e. the generic automorphisms of the family component. It is normal, so Γ_x^+ := K·Γ_x is a subgroup of Γ.

**Hypothesis (U_J).** After shrinking B and ε, every p ∈ 𝒞° satisfies Stab_Γ(p) ⊂ K·Γ_x.

(Generic twins, i.e. elements of K moving x, are thus allowed.)

In words: no curve of V_τ near J (|τ| < ε) in the family component 𝒜 has an automorphism, induced by an element of Aut(J), that maps the region x to a different region. Two remarks:
- (NT) at J (every σ ∈ Aut(J) fixes x) implies (U_J) trivially, since then Γ_x = Γ.
- (U_J) is a germ condition at (J, 0): it fails iff (0,0) ∈ closure(Fix(α) ∩ 𝒞°) for some α ∈ Γ ∖ KΓ_x.

## 2. The covering lemma: squares lift modulo Γ_x (proved)

**Lemma 1 (intermediate quotients).** Let a finite group G act on a Hausdorff, locally compact space X, and let H ≤ G. The natural map π : X/H → X/G is a local homeomorphism at the point Hp if and only if G_p ⊂ H. If this holds at every point, then π is a finite covering map over each connected component of X/G.

*Proof.*
- Since G is finite and X Hausdorff, p has a G_p-invariant open neighbourhood V with gV ∩ V = ∅ for g ∉ G_p.
- Then V/G_p → X/G and V/H_p → X/H are open embeddings, where H_p = G_p ∩ H. In these charts π is V/H_p → V/G_p, which is a homeomorphism iff H_p = G_p.
- π is closed with finite fibres, hence proper. A proper local homeomorphism between locally compact Hausdorff spaces is a covering over each component of the base (standard). ∎

**Lemma 2 (square lifting).** Assume (U_J). Let F : [a,b] × [0,1] → 𝒜 be continuous, and let F̂_0 : [a,b] → 𝒞° be a lift of F(·,0). Then:
- for every s, every lift μ_s : [0,1] → 𝒞° of F(s,·) with μ_s(0) = F̂_0(s), and
- every lift λ : [a,b] → 𝒞° of F(·,1) with λ(a) = μ_a(1),

satisfy λ(s) ∈ Γ_x · μ_s(1) for all s.

(Lifts of paths in 𝒞° exist for any initial point, by path lifting for finite group quotients: Bredon, *Introduction to compact transformation groups*, II.6.2, cited from memory.)

*Proof.*
- By Fact 0, 𝒜 = 𝒞°/Γ. By (U_J) and Lemma 1 (with H = K·Γ_x), π : 𝒞°/(KΓ_x) → 𝒜 is a covering.
- Let F̃ be the unique lift of F to 𝒞°/(KΓ_x) with F̃(a,0) = [F̂_0(a)] (homotopy lifting for coverings).
- Uniqueness of path lifts gives:
  - [F̂_0(s)] = F̃(s,0) for all s;
  - [μ_s(τ)] = F̃(s,τ) for all τ, since both are lifts of F(s,·) from [F̂_0(s)];
  - [λ(s)] = F̃(s,1), since both are lifts of F(·,1) from [μ_a(1)] = F̃(a,1).
- Hence λ(s) = kγ μ_s(1) with k ∈ K and γ ∈ Γ_x.
- Since K is normal and acts trivially on 𝒞°, kγ μ_s(1) = γ(γ^{-1}kγ)μ_s(1) = γ μ_s(1). So λ(s) ∈ Γ_x μ_s(1). ∎

We apply this with F(s,τ) := (H(γ(s), τt), τt) and F̂_0 := γ̃ × {0}.
- F takes values in 𝒱_U for |t| small: γ([a,b]) is a compact subset of U ∩ V_0, H is uniformly continuous, and H_0 = id.
- F takes values in 𝒜, because F([a,b]×[0,1]) is connected and contains γ × {0} ⊂ 𝒜.

## 3. τ-transport away from J (proved)

Fix 0 < r_1 small. Put B_0^{U} := B_0 ∩ U ∖ {J}. By the cone structure it is a finite union of punctured branches β_1, …, β_N.

Let 𝒵 be the set of connected components of q^{-1}(H(B_0^{U} × Δ_ε)). This set is finite:
- each H(β_j × Δ_ε) is connected;
- the components of its preimage are permuted transitively by Aut(J), as in Fact 0.

Each Z ∈ 𝒵 has a constant pinching pattern S(Z), because Z is connected and lies over a single stratum (R7-4 Lemma 2(a)).

**Lemma 3 (separation).** Fix t with |t| < ε/2. Let 𝔑 := q^{-1}(H((B_0^{U} ∖ {d̄(·,J) < r_1/2}) × [0,t])), where [0,t] := {τt : τ ∈ [0,1]}. Then:
- 𝔑 is compact;
- the sets 𝔑_Z := 𝔑 ∩ Z, Z ∈ 𝒵, are compact and pairwise disjoint;
- hence d'(r_1, t) := min_{Z ≠ Z'} dist(𝔑_Z, 𝔑_{Z'}) > 0.

*Proof.*
- The set (B_0 ∩ closure(U)) ∖ {d̄ < r_1/2} is compact; take U to be the image of a closed ball. Its image under the continuous H, intersected with times in [0,t], is compact, and q is proper. So 𝔑 is compact.
- 𝔑 ⊂ q^{-1}(H(B_0^U × Δ_ε)), in which each Z is closed. So 𝔑_Z is closed in 𝔑, hence compact.
- Distinct components are disjoint. ∎

**Corollary 3′ (τ-transport near the boundary).** Let s be such that d̄(z_s, J) ≥ r_1, and let ẑ_s ∈ Z_s ∈ 𝒵 be as in (T3). Let μ_s be a lift in 𝒞° of τ ↦ F(s,τ) from γ̃(s). Let ε_1 := ε_1(ρ) be such that d̄(X, z) < ρ implies d̄(H(X,τt), H(z,τt)) < ε_1 for all τ (uniform continuity of H; ε_1 → 0 as ρ → 0). If ρ < ε_1 < d'(r_1,t)/3, then:
- μ_s(1) lies within ε_1 of a point w ∈ Z_s that is a lift of H(z_s, t);
- w ∈ L_x;
- F_x(w) ∈ S_t, where S_t is the finite set defined in §4.

*Proof.*
- For each τ, the coarse distance between q(μ_s(τ)) = H(γ(s),τt) and H(z_s, τt) is < ε_1. So μ_s(τ) lies within ε_1 of some lift of H(z_s,τt), which lies in 𝔑 (for t small, H keeps z_s at distance ≥ r_1/2 from J(τt)).
- By Lemma 3, the Z for which dist(μ_s(τ), 𝔑_Z) < ε_1 is unique. It is locally constant in τ, hence constant.
- At τ = 0, μ_s(0) = γ̃(s) is within ρ < ε_1 of ẑ_s ∈ Z_s. So Z = Z_s for all τ, and at τ = 1 we get w ∈ Z_s, a lift of H(z_s,t), with |μ_s(1) − w| < ε_1.
- **w ∈ L_x.** The pattern S(Z_s) is constant, and ẑ_s ∈ L_x. So x is intact on Z_s, i.e. Z_s ⊂ L_x.
- **F_x(w) ∈ S_t.** Let D_s be the piece of the branch β_j ∋ z_s, and v the vertex of D_s that contains x along Z_s. Then v = {x}, since x is intact.
  - If v is constant on D_s, then F_x ≡ φ_v(t) on Z_s ∩ {time t}. This is Lemma 2 of R7-3 (transport of a lifted branch): Z_s is the set Ñ there.
  - Otherwise F_x(ẑ_s) ≅ Y_0 says that z_s ∈ Sp_J, the finite set defined in §4. Then F_x(w) is the class of a component of H(z_s,t). ∎

## 4. Theorem A: no twin jump at J under (U_J) (proved, given (TD_J))

**The finite set S_t.** Let Sp_J be the set of points z ∈ B_0^U such that some vertex v that is non-constant on the piece through z has a value ≅ Y_0 at z. Sp_J is finite: f_v extends to the compact normalisation Ē of each of the finitely many pieces meeting U, and f_v^{-1} of the finitely many relabellings of Y_0 is finite. Then S_t ⊂ M_{g_i,n_i}/S_{n_i} is the finite union of:
- the values φ_v(t) of all constant vertices v of type (g_i,n_i) of the finitely many pieces with a branch in B_0^U;
- the classes of all type-(g_i,n_i) components of H(z,t), for z ∈ Sp_J;
- the classes of all type-(g_i,n_i) components of J(t) := H(J,t).

Let 2ε'(t) > 0 be the minimum distance between distinct elements of S_t (put ε'(t) = 1 if |S_t| = 1). Note that S_t does not depend on r_1.

**Theorem A.** Assume the setting of MS8, the readings (R1), (R2), (C1)–(C3), the track datum (TD_J), and (U_J). Then φ_{c_{k−1}} ≡ φ_{c_k} on Δ.

Hence, if (TD_J) and (U_J) hold at every junction J^1, …, J^m of the chain, then φ_{c_k} ≡ Y for every k, i.e. (TW1) holds. This is by induction from c_0 = i, with φ_i = Y.

Theorem A uses neither (Rig) nor the non-constancy of Y.

*Proof.* By the identity theorem (φ_c is holomorphic: R7-3 Lemma 1), it suffices to prove φ_{c_{k−1}}(t) = φ_{c_k}(t) for all t ≠ 0 in a small disc Δ_{t_0}. Here t_0 is chosen so that, for |t| < t_0, F(s,τ) := (H(γ(s), τt), τt) stays in 𝒱_U for every path of (TD_J) (uniform continuity of H on the compact closure(V_0) ∩ closure(U)). Fix such a t ≠ 0.

**Choice of constants.**
- Let d_J(t) > 0 be the minimum distance in B between distinct lifts of J(t). (The lifts form one finite Aut(J)-orbit.)
- Let ω_H be a modulus of continuity of z ↦ H(z, τt) on closure(B_0 ∩ U), uniform in τ ∈ [0,1].
- Let ω_F be a modulus of continuity of F_x on the compact set L_x ∩ closure(B).
- Choose r_1 > 0 with:
  - r_1 < min(d̄(z_1,J), d̄(z_2,J));
  - r_2 := 2ω_H(r_1) < d_J(t)/4;
  - ω_F(3r_2) < ε'(t).
- Then choose ρ so small that ρ < ε_1(ρ) < min(ω_H(r_1), d'(r_1,t)/3) (Lemma 3, Corollary 3′).
- Take γ, γ̃, z_s, ẑ_s from (TD_J) for this ρ, and define F as above.

**Lifts.**
- For each s, let μ_s be a lift in 𝒞° of F(s,·) from γ̃(s).
- Let λ be a lift in 𝒞° of F(·,1) from μ_a(1).
- By Lemma 2, for every s there is κ_s ∈ Γ_x with λ(s) = κ_s μ_s(1). Take κ_a = id.

**The class function.** For each s choose u(s) ∈ L_x with |λ(s) − u(s)| < r_2 and F_x(u(s)) ∈ S_t, as follows.
- *Regime (ii): d̄(z_s, J) ≥ r_1.*
  - Corollary 3′ gives w_s ∈ L_x, a lift of H(z_s,t), with |μ_s(1) − w_s| < ε_1 and F_x(w_s) ∈ S_t.
  - Put u(s) := κ_s w_s. The norm is Aut(J)-invariant, so |λ(s) − u(s)| = |μ_s(1) − w_s| < ε_1 < r_2.
  - Since κ_s x = x, we have u(s) ∈ L_{κ_s x} = L_x and F_x(u(s)) = F_{κ_s^{-1}x}(w_s) = F_x(w_s) ∈ S_t.
  - **This is the only place where (U_J) is used.** Without it κ_s^{-1}x could be a twin region, which need not be intact at w_s or could carry a different value.
- *Regime (i): d̄(z_s, J) < r_1.*
  - d̄(q λ(s), J(t)) ≤ d̄(H(γ(s),t), H(z_s,t)) + d̄(H(z_s,t), H(J,t)) < ε_1 + ω_H(r_1) ≤ r_2.
  - So some lift ĵ(s) of J(t) has |λ(s) − ĵ(s)| < r_2 < d_J(t)/4, and it is unique.
  - Lifts of J(t) lie in {s_e = 0 for all e} ⊂ L_x. Put u(s) := ĵ(s); then F_x(u(s)) is the class of a component of J(t), so it lies in S_t.

Put c(s) := F_x(u(s)) ∈ S_t.

**Near-continuity.**
- λ is uniformly continuous, so there is δ > 0 with |λ(s) − λ(s')| < r_2 whenever |s − s'| < δ.
- For such s, s' we get |u(s) − u(s')| < 3r_2, with both points in L_x ∩ closure(B). Hence d(c(s), c(s')) ≤ ω_F(3r_2) < ε'(t).
- Since c takes values in S_t, whose distinct elements are ≥ 2ε'(t) apart, c(s) = c(s') whenever |s − s'| < δ. So c is constant on [a,b].

**Endpoints.**
- At s = a: z_a = z_1, so we are in regime (ii), and w_a lies in the component Z_a ∈ 𝒵 containing ẑ_a = z̃_1 ∈ β̃. This component is the set Ñ of R7-3 Lemma 2 for (D, c_{k−1}, x), on which F_x ≡ φ_{c_{k−1}}(t). With κ_a = id, c(a) = φ_{c_{k−1}}(t).
- Likewise c(b) = F_x(w_b) with w_b ∈ Z_b ∋ z̃_2 ∈ β̃'. So c(b) = φ_{c_k}(t).
- Hence φ_{c_{k−1}}(t) = φ_{c_k}(t). ∎

**Remarks on Theorem A.**
1. **Which gap of R7-6 this repairs.**
   - *(Monodromy.)* R7-6 transported markings along the 2-parameter square without controlling branch points. Under (U_J), the only branch points of 𝒞° → 𝒜 have stabilisers fixing x. These are invisible in the covering 𝒞°/Γ_x, which is exactly the object the labels live on.
   - *(Uniformity near J.)* R7-6 needed charts of the boundary points z_s to have size ≫ ε uniformly, which fails as z_s → J. Here, for z_s within r_1 of J, I compare with the lifts of J(t) themselves. They are separated by d_J(t) > 0 because t is fixed first, and all regions are intact at them. The two regimes are glued by the continuity of F_x on L_x.
   - The order of choices (t, then r_1, then ρ) is essential. This is possible because the identity theorem only needs the equality for each fixed small t, and (TD_J) provides tracks for every ρ.
2. **The twin jump of R7-3 §5 is exactly a monodromy phenomenon.** In the proof, every step except the line marked in regime (ii) holds without (U_J). So a twin jump at J (φ_{c_{k−1}} ≢ φ_{c_k}) forces: for a sequence ρ → 0 (with t fixed), some κ_s ∉ Γ_x. That means a nontrivial lift-monodromy of the square F in 𝒜, coming from points of 𝒞° whose stabiliser moves x. This is the precise content of the planner's sketch, step 5(b).
3. **Relation to (Lock).** If (Lock) holds at J (R7-1), then φ_{c_{k−1}} ≡ φ_{c_k} by R7-1 Step 2. So at each junction it suffices to have **(U_J) or (Lock_J)**.
   - In the quintic example (PR-I; not smooth, so only a test case), the twins A, C at P_0 = Y_0 — B_0 — Y_0 are exchanged by automorphisms of interior curves. These are the covers of the configurations (a_1, a_2, 1, 1/a_1, 1/a_2), whose involution x ↦ 1/x lifts because all local monodromies are equal.
   - So there (U) fails, while (Lock) holds. This is a sketch; I did not check which component 𝒞° the track uses.

## 5. Theorem B: the terminal point (TW2) under (U_{Q_0})

**Endpoint datum (TD_Q).** Let Q_0, the last STAY piece D := D^m and its lift β̃ with c_m = {x}, and the terminal branch b with a lift b̃ ⊂ Def(Q_0) be as in Proposition K. So either:
- (MERGE) some edge at x is unpinched along b̃; or
- (puncture-MOV) every edge at x is pinched along b̃, F_x is non-constant along b̃, and Q_0 ∉ Δ_{G_b}.

Fix generic z̃_1 ∈ β̃ ∖ 0 and a point z̃_b ∈ b̃ ∖ 0, with z_b = q(z̃_b). (TD_Q) asks that for every r_1 > 0 small and every ρ ≤ ρ_0(r_1) there are γ : [a,e] → V_0 ∩ U and a lift γ̃ such that:
- (TQ1) |γ̃(a) − z̃_1| < ρ and |γ̃(e) − z̃_b| < ρ;
- (TQ2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_e = z_b;
- (TQ3) with s_* := sup{s : d̄(z_s, Q_0) ≤ r_1}: (T3) holds for every s < s_* with d̄(z_s, Q_0) ≥ r_1.

The point z_b is FIXED, independent of ρ. This is the difference from (K\*)(c) of R7-6, where the merge witness Q′ satisfies d(Q′, Q_0) < ρ.
- **Where it comes from (sketch, not proved).** In the proof of Proposition K, fix k and let n → ∞. The ray endpoints converge to Q_k ∈ b ∖ {Q_0}, which is at a fixed distance from Q_0. Then take z_b := Q_k.
- The price is that along the track ∂Σ_i is only Ext-short (Ext ≤ δ_k), not pinched. So (T3) holds only approximately: there is a lift with |s_e| ≤ σ_k for the edges at x, where σ_k → 0 as k → ∞.
- In regime (ii) this suffices, after choosing k large depending on r_1. On the compact part {d̄(·, Q_0) ≥ r_1/2} of the finitely many lifted branches along which x is merged, some |s_e| with e at x is bounded below by m(r_1) > 0, since s_e is a holomorphic function on the branch vanishing only at the centre. So once σ_k + ρ < m(r_1)/2, the nearby boundary lift has x intact.
- I record this as the reading (TD_Q). Its derivation from Proposition K is a sketch.

Define Γ, Γ_x, 𝒞° and (U_{Q_0}) at Q_0 exactly as in (C3), with the track of (TD_Q).

**Theorem B.** Assume the setting of MS8, (R1), (R2), (C1)–(C3) at Q_0, (TD_Q) and (U_{Q_0}). Assume also φ_{c_m} ≡ Y (for instance from Theorem A at all junctions). Then for every t in a disc Δ_{t_0}, with t ≠ 0, there are:
- a lift Q̂ of Q(t) := H(Q_0, t) with F_x(Q̂) ≅ Y_t, and
- a lifted branch Z′ of b_t := H_t(b) through Q̂ (i.e. Q̂ ∈ closure(Z′)),

such that:
- (MERGE) some edge at x is unpinched along Z′; or
- (puncture-MOV) every edge at x is pinched along Z′, and F_x is non-constant along Z′ for t outside a countable set.

In particular (TW2) holds, and by R7-4 Lemma 1 (= R7-1 Lemma 1) the MS6 configuration exists at every such t.

*Proof.* Fix t as in Theorem A. Use the same constants, with J replaced by Q_0, plus two more:
- Let 𝒵_b be the finite set of connected components of q^{-1}(H_t(b ∩ U ∖ {Q_0})). The set H_t(b ∩ U ∖ Q_0) is connected, being the image of a punctured disc.
- For a lift Q̂ of Q(t), let η_1(t) > 0 be the minimum, over all lifts Q̂ and all Z′ ∈ 𝒵_b with Q̂ ∉ closure(Z′), of dist(Q̂, closure(Z′)). It is positive because there are finitely many compact closures.
- Shrink r_1 so that also 2r_2 < η_1(t). Shrink ρ so that ε_1 < d″/3, where d″ > 0 is the minimum distance between the compact sets closure(Z′) ∩ q^{-1}(H_t(b ∩ U ∩ {d̄(·,Q_0) ≥ r_1/2})), Z′ ∈ 𝒵_b. Also require that distinct branches of B_0 in the closed annulus {r_1/2 ≤ d̄(·,Q_0) ≤ r} are > 2ρ apart.

**Step 1 (class function up to s_*).** Run the proof of Theorem A on [a, s_*]. Regime (ii) uses (TQ3) and (U_{Q_0}); regime (i) uses the lifts of Q(t), separated by d_Q(t).
- This gives c constant on [a, s_*], with c(a) = φ_{c_m}(t) = Y_t.
- At s_* we have d̄(z_{s_*}, Q_0) ≤ r_1, i.e. regime (i). So the unique lift Q̂ of Q(t) with |λ(s_*) − Q̂| < r_2 satisfies F_x(Q̂) = c(s_*) = Y_t.

**Step 2 (after s_*, the track follows b).**
- For s ∈ (s_*, e] we have d̄(z_s, Q_0) > r_1. Consider z_s inside the annulus where the branches are separated. Since γ is continuous and d̄(γ(s), z_s) < ρ, the branch carrying z_s is locally constant. It equals b, because z_e = z_b ∈ b.
- (If z_s leaves the annulus outward, it is no longer near Q_0, and the same argument applies with U large enough to contain b up to z_b.)

**Step 3 (time t).**
- For s ∈ [s_*, e], λ(s) is within ε_1 of a lift of H(z_s, t) with z_s ∈ b and d̄(z_s, Q_0) ≥ r_1. That lift lies in some Z′ ∈ 𝒵_b.
- By the d″-separation, this Z′ =: Z′_* is the same for all s ∈ [s_*, e].
- At s = e: λ(e) = κ_e μ_e(1) with κ_e ∈ Γ_x (Lemma 2). As in Corollary 3′, μ_e(1) is within ε_1 of a point w_e of the component Z_b of q^{-1}(H((b∖Q_0) × Δ_ε)) that contains z̃_b. So λ(e) is within ε_1 of κ_e w_e ∈ κ_e Z_b.
- κ_e w_e lies in some component of 𝒵_b contained in (κ_e Z_b)_t. By d″-separation it is Z′_*. Hence Z′_* ⊂ κ_e Z_b.
- The pattern of κ_e Z_b is κ_e S(b̃), and κ_e x = x.
  - (MERGE) An edge at x is unpinched along b̃, so the edge κ_e(e_0) at x is unpinched along κ_e Z_b ⊃ Z′_*.
  - (MOV) All edges at x are pinched along κ_e Z_b. Also F_x(κ_e p) = F_x(p) for p ∈ Z_b. By R7-3 Lemma 1(b), F_x is non-constant on the time-t transport of the piece of b for t outside a countable set (the identity theorem on Ē gives non-constancy on each of its branches). Hence F_x is non-constant along Z′_* for such t.

**Step 4 (Q̂ lies on Z′_*).**
- λ(s_*) is within r_2 of Q̂ and within ε_1 of Z′_*. So dist(Q̂, Z′_*) < r_2 + ε_1 < 2r_2 < η_1(t).
- Therefore Q̂ ∈ closure(Z′_*). Put Z′ := Z′_*. ∎

**Corollary C (MS8 under (U), modulo the readings).** Assume:
- the setting of MS8 with (Rig);
- (TD_J) and [(U_J) or (Lock_J)] at every junction;
- (TD_Q) and (U_{Q_0}) at the terminal point;
- that the terminal branch is MERGE or puncture-MOV.

Then Y_t = Y_0 for all t.

*Proof.*
- Theorem A, or R7-1 Step 2 under (Lock), gives φ_{c_m} ≡ Y.
- Theorem B gives, for all t in a punctured disc outside a countable set, a non-constant vertex u of a piece E at time t and a puncture p with Y_t a component of f_u(p) (R7-4 Lemma 1). Here u = [x] in the MERGE case and u = {x} in the MOV case.
- By (Rig), puncture values of non-constant vertices lie in the finite set F, so Y_t is a component of an element of F for uncountably many t accumulating at 0.
- t ↦ Y_t is holomorphic (PR-A), so it is constant. ∎

## 6. The residual case: what a twin jump requires (partly proved, partly open)

**Proposition D (necessary conditions for a twin jump; proved, given (TD_J)).** Suppose φ_{c_{k−1}} ≢ φ_{c_k} at the junction J. Then:
- (a) (Lock_J) fails, and (U_J) fails. So there is α ∈ Γ ∖ KΓ_x (in particular αx ≠ x, and α is not a generic automorphism of the family) with (0,0) ∈ closure(Fix(α) ∩ 𝒞°): curves of V_τ near J, with |τ| arbitrarily small, have an automorphism (induced by α ∈ Aut(J)) that exchanges the tracked region x with a different region αx.
- (b) Let Φ be an irreducible component, through (0,0), of the analytic germ Fix(α) ∩ closure(𝒞°) ⊂ Def(J) × Δ that is not contained in {∏ s_e = 0}. One of the following holds:
  - **(A)** Φ ∩ {τ = 0} contains points of B° near 0, arbitrarily close to 0. That is: curves of V_0 itself, arbitrarily close to J, admit an automorphism (from Aut(J) acting on Def(J)) that moves x.
  - **(B)** Φ ∩ {τ = 0} ⊂ {∏ s_e = 0} and has dimension ≥ 1. That is: some lifted branch of B_0 at J (lying in closure(𝒞°)) is fixed pointwise by α. Then every boundary point of V_0 on that branch has an automorphism exchanging the components (or merged vertices) containing x and αx.
  - **(C)** dim Φ = 1 and Φ ∩ {τ = 0} = {(0,0)}. That is: there is a holomorphic arc τ ↦ C_τ ∈ V_τ (after a base change τ = σ^k) of smooth curves with automorphism α, converging to J as τ → 0. This is invisible at t = 0.

*Proof.*
- (a) is the contrapositive of Theorem A, together with R7-1 Step 2 for (Lock). For the germ reformulation of (U_J), see (C3).
- (b) closure(𝒞°) is a 3-dimensional analytic set. It is the closure of a connected component of the preimage of the 3-dimensional manifold 𝒱 (R1); closures of unions of components of q^{-1}(𝒱_U) are analytic, as in R7-4 Lemma 2(c). Fix(α) = Fix_{Def(J)}(α) × Δ is a smooth submanifold (linear action). So Fix(α) ∩ closure(𝒞°) is analytic, and Φ has dimension 1, 2 or 3.
  - **dim 3.** Then α fixes 𝒞° pointwise, i.e. α ∈ K ⊂ KΓ_x, contradicting the choice of α. So this case does not occur.
  - **dim Φ ≥ 2.** Φ ∩ {τ = 0} has dimension ≥ 1 at (0,0) (Krull, if τ ≢ 0 on Φ; trivially otherwise). It lies in closure(𝒞°) ∩ {τ=0} ⊂ q^{-1}(closure(V_0) ∩ U), by (R2): H commutes with closures and H_0 = id. Either it meets B° arbitrarily close to 0, giving (A), or it lies in the boundary, giving (B).
  - **dim 1.** If Φ ⊂ {τ = 0}, then Φ ∖ (0,0) consists of interior points of V_0's lift, giving (A). Otherwise τ|_Φ is finite at (0,0), and since Φ ⊄ {∏s_e = 0}, Φ ∖ (0,0) ⊂ B° × Δ near (0,0) (a proper analytic subset of an irreducible curve germ is the point). This is (C), with the normalisation of Φ giving the base change. ∎

**How this relates to the planner's dichotomy (step 5(b) of the sketch, and the "named approach").**
- The first alternative, "Fix(α) ∩ 𝓛 stays away from the region swept by the transported paths", is (U_J). Under it, Theorem A makes R7-6's argument rigorous at J.
- The second alternative, "the closure of the fixed locus meets the boundary at points J′_τ near J_τ at which α exchanges two components both ≅ Y_τ", is **not** forced by the analysis above. In case (C), Φ meets the boundary only at (0,0). In case (B), it meets it only at τ = 0.
- Even when Φ ∩ {∏s_e = 0} contains an arc Ψ with τ|_Ψ non-constant, the point ψ(τ) ∈ Ψ may be:
  - a lift ĵ(τ) of J(τ). Then F_x(ĵ(τ)) = F_{αx}(ĵ(τ)): the twins are locked at that particular lift, which is a pointwise form of (Lock).
  - a point of a lifted transported branch Z. Then only the components x, αx of that boundary point are exchanged.

  In neither case did I find a way to show that the monodromy κ of the square (a product of conjugates of such α's) fixes the class F_x on the transported D'-branch. Heuristically (this is not a construction), the R7-3 §5 local model, completed by an interior 3-fold, is compatible with (C). Take Def coordinates (a, b) for the two twin components with σ(a,b) = (b,a), and let 𝒞̄ be any irreducible 3-fold containing both transported branches and meeting Fix(σ) = {a = b} in a curve through (0,0) only.

So the chart-plus-interior-local analysis does not exclude (C) either. Any proof of (TW) must use total geodesy at t = 0, or global information, to exclude (A), (B) and (C) at a twin junction, or to show that they force (Lock).

**Remark (where total geodesy could enter, not carried out).** In case (A), the lift of V_0 and Fix(α) are both totally geodesic in T_g. Fix(α) is the image of the Teichmüller space of the quotient orbifold, a holomorphic isometric embedding. So their intersection near the lift of J is a totally geodesic subvariety of V_0 consisting of α-symmetric curves, whose closure contains J. One would want to show that such a sub-locus forces the twins x, αx to stay isomorphic at J(τ) under every deformation satisfying (i), (ii). That would be a (Lock) statement, and it is the natural next target. I have no proof.


### R8-8. Theorem 1 (MS8 under star coherence), isotropy preservation, Proposition 3, pure crossings, the scale conflict (from round8_q8, verbatim, §§0–6)
## 0. Conventions and inputs

All of the following are adopted verbatim from the task: readings (R1) and (R2) with H_0 = id, B_t := closure(V_t) \ V_t, "piece", ν, puncture, f_u, M(E), K(E), and (Rig).

- For a stable curve J, Def(J) is its versal deformation germ, with smoothing parameters s_e (e ∈ E(G_J)). Aut(J) acts on Def(J), and π: Def(J) → Def(J)/Aut(J) is a neighbourhood of J in M̄_g.
- For a vertex x put L_x := {s_e = 0 for all edges e at x}. F_x: L_x → M_{g_x,n_x} is the x-component of the fibre curve.
- Facts (K1)–(K3) of R7-3 §1 are used. Cited from memory as standard:
  - (K1) the preimage of a point is one Aut(J)-orbit;
  - (K3) F_x(σq) ≅ F_{σ^{-1}x}(q).
- (K4) (standard, from memory; the local structure of the Deligne–Mumford stack M̄_g = [Def(J)/Aut(J)] near J) For q ∈ Def(J) close to 0, Aut(fibre curve at q) ≅ Stab_{Aut(J)}(q). Hence for J′ near J,
  #π^{-1}(J′) = |Aut(J)| / |Aut(J′)|.
- "≅" between pointed curves always means: isomorphic after some relabelling of the special points. Equivalently, the images [·] in the coarse space M_{g_i,n_i}/S_{n_i}, which is a reduced complex analytic space, are equal.

**Transport families** (R7-3 Lemma 2, R7-4 Lemma 2; I re-checked the steps used).
- Let J ∈ B_0, and let β̃ be a lifted branch at 0 ∈ Def(J) of a piece D. Either J is a puncture of D, or J lies on D and β̃ is the lifted germ of D.
- Put N := H((β \ {J}) × Δ_ε), and let Ñ be the connected component of π^{-1}(N) ⊂ Def(J) × Δ_ε that contains β̃ \ {0}.
- Then the pinched-edge pattern is constant on Ñ, and Ñ ∩ {t = 0} = β̃ \ {0}.
- For every t, closure(Ñ_t) contains at least one point of π^{-1}(J_t), where J_t := H_t(J).
- If D lies in a product-type stratum and the vertex c of D is constant on D with c = {x} along β̃, then Ñ_t ⊂ L_x and F_x ≡ φ_c(t) on Ñ_t. Here φ_c(t) is the (constant) value of c on the transported piece D_t = H_t(D). The proof uses L1 for product type (R7-5 §1.2), which I checked.
- t ↦ φ_c(t) is holomorphic (R7-3 Lemma 1(a)).
- Since L_x is closed and F_x is continuous on it, **F_x ≡ φ_c(t) on closure(Ñ_t) ∩ L_x = closure(Ñ_t)**. (∗)

**Input (K′) (Prop K, PR-H §3, in the reading of R7-3 §1).** Taken as input, "proved modulo routine marking details" there and not re-proved here. There are:
- points J_0 = P ∈ ∂V_0, J_1, …, J_{k−1} (junctions) and J_k = Q_0 (endpoint), all in B_0;
- pieces D^1, …, D^k at time 0, with D^1 the component of ∂V_0 through P;
- for each m, a vertex c_m of D^m that is constant on D^m with value ≅ Y_0, where c_1 = i;
- for 1 ≤ m ≤ k−1: lifted branches β̃^m_+ (of D^m) and β̃^{m+1}_− (of D^{m+1}) at 0 ∈ Def(J_m), and a chart vertex x_m of G_{J_m}, with c_m = {x_m} along β̃^m_+ and c_{m+1} = {x_m} along β̃^{m+1}_−;
- at Q_0: a lifted branch β̃^k_+ of D^k with c_k = {x}, and a lifted branch β̃^E at 0 ∈ Def(Q_0) of a piece E, of one of three types:
  - **(MERGE)** the vertex class u of E containing x contains an edge of G_{Q_0} that is unpinched along β̃^E;
  - **(pMOV)** x is intact along β̃^E, f_{\{x\}} is non-constant on E, and Q_0 ∉ stratum(E);
  - **(iMOV)** as (pMOV), but Q_0 ∈ stratum(E) (a crossing).

**Hypothesis (PT_chain).** The pieces D^1, …, D^k and E lie in product-type strata. This is needed for L1. R7-5 §1.4 shows that L1 can fail for non-product strata; this caveat is inherited from R7-1 (T2) and R7-2 (PT).

## 1. Two elementary lemmas

**Lemma 1 (identity theorem in the coarse space).** Let f, g: Δ → Z be holomorphic maps into a reduced complex space Z. If {f = g} has an accumulation point in Δ, then f ≡ g. If f takes values in a finite set A on a set with an accumulation point in Δ, then f is constant.

*Proof.*
- {f = g} is an analytic subset of Δ: locally, embed Z in C^N and compare coordinates. A proper analytic subset of the connected Δ is discrete, so one with an accumulation point is all of Δ.
- For the second claim, some a ∈ A is taken on a set with an accumulation point. Apply the first claim with g ≡ a. ∎

**Lemma 2 (the finite set from (Rig)).** Put
 F := { pr_u(κ) : (G, M, K) ∈ 𝒦, u ∈ M, κ ∈ K ∩ ∂(∏_{u∈M} M̄_u) }.
Let A ⊂ M_{g_i,n_i}/S_{n_i} be the finite set of classes of smooth components of elements of F, of type (g_i, n_i), taken with their special points.
1. F and A are finite. For every piece E at every time t, every u ∈ M(E) and every puncture p of E, f_u(p) ∈ F up to relabelling.
2. If Y is non-constant, then Z_A := {t : [Y_t] ∈ A} is a closed discrete subset of Δ.

*Proof.*
1. K is irreducible and not contained in the boundary, so K ∩ ∂ is a proper analytic subset of a compact irreducible curve, hence finite. 𝒦 is finite.
   - At a puncture p, some coordinate of ν(p) lies in a boundary. Constant vertices take values in M_w. So the boundary coordinate is some u ∈ M(E), and pr_{M(E)}ν(p) ∈ K(E) ∩ ∂.
   - (Rig) identifies (G, M(E), K(E)) with an element of 𝒦 up to Aut(G). This only renames the vertices and the marked points.
2. t ↦ [Y_t] is holomorphic (PR-A, composed with the quotient map). It is non-constant: otherwise Y_t would lie in a finite S_{n_i}-orbit, and by continuity Y would be constant. Lemma 1 then gives the claim. ∎

## 2. Theorem 1: MS8 under star coherence (proved, given the inputs listed)

**Notation.** Write Ñ^m_+ and Ñ^{m+1}_− for the transport families of β̃^m_+ and β̃^{m+1}_− at J_m. At m = k write Ñ^k_+ and Ñ^E for those of β̃^k_+ and β̃^E at Q_0. Put J_{m,t} := H_t(J_m). The two families compared at J_m are:
- Ñ^m_+ and Ñ^{m+1}_−, for m < k;
- Ñ^k_+ and Ñ^E, for m = k.

**Definition.**
- (SC_m) (*star coherence at J_m*): the set
 T_m := { t ∈ Δ_ε : closure(first family at J_m)_t ∩ closure(second family at J_m)_t ∩ π^{-1}(J_{m,t}) ≠ ∅ }
 has an accumulation point in Δ_ε.
- (NT_m): every σ ∈ Aut(J_m) fixes the tracked chart vertex (x_m, or x at m = k).
- (C_m) := (SC_m) or (NT_m).

**Theorem 1.** Assume:
- (R1), (R2) and the hypotheses of MS8, including (Rig);
- the input (K′), with endpoint of type MERGE or pMOV;
- (PT_chain);
- (C_m) for every m = 1, …, k.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*

**Step 1: [φ_{c_m}] ≡ [Y] for all m, by induction.**
- *Base.* c_1 = i on the component D^1 of ∂V_0, and vertex i is ≡ Y_t on ∂V_t. So φ_{c_1} = Y.
- *Induction step, case (SC_m).* Let t ∈ T_m and pick j̃ in the triple intersection defining T_m. By (∗), applied to both families with the same chart vertex x_m:
 F_{x_m}(j̃) ≅ φ_{c_m}(t) and F_{x_m}(j̃) ≅ φ_{c_{m+1}}(t).
 So [φ_{c_{m+1}}(t)] = [φ_{c_m}(t)] = [Y_t] for t ∈ T_m. By Lemma 1, [φ_{c_{m+1}}] ≡ [Y].
- *Induction step, case (NT_m).* Pick any j̃^+ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}) and j̃^− ∈ closure(Ñ^{m+1}_{−,t}) ∩ π^{-1}(J_{m,t}). Both sets are nonempty (§0).
  - By (K1), j̃^− = σ j̃^+ for some σ ∈ Aut(J_m).
  - By (K3) and σ^{-1}x_m = x_m: F_{x_m}(j̃^−) ≅ F_{x_m}(j̃^+).
  - Conclude as in the (SC_m) case, now for every t ∈ Δ_ε.

**Step 2: the endpoint.** Let t ∈ T_k in case (SC_k), or any t ∈ Δ_ε in case (NT_k). Choose q̃ ∈ closure(Ñ^E_t) ∩ π^{-1}(Q_t) such that F_x(q̃) ≅ φ_{c_k}(t) ≅ Y_t. This uses Step 1 and (∗), and in case (NT_k) the (K3)-trick of Step 1.
- Pattern and vertex structure are constant on Ñ^E. So along Ñ^E_t the vertex class of x is the class u that it has along β̃^E.
- Take r_n ∈ Ñ^E_t with r_n → q̃. By (PT_chain), their images lie in the lifted transported piece E_t ⊂ ∏_w M_w. By properness of ν_t they converge to ν_t(p′) for some p′ ∈ Ē_t.
- H_t preserves strata and Q_0 ∉ stratum(E). So Q_t ∉ stratum(E_t), and ν_t(p′) ∉ ∏_w M_w, because ξ̄ maps ∏_w M_w into Δ_{G_E}. Hence p′ is a puncture.
- By continuity of the plumbing (Def1), f_u(p′) is the curve glued from the components F_y(q̃), y ∈ u, along the edges of u unpinched along β̃^E. Its component F_x(q̃) keeps its special points (R7-4 Lemma 1, step 3). So F_x(q̃) ≅ Y_t is a component of f_u(p′).
- **(MERGE).** f_u(p′) has a node. A constant vertex has a smooth limit, so u ∈ M(E_t). By Lemma 2, f_u(p′) ∈ F, so [Y_t] ∈ A.
- **(pMOV).** Here u = {x}. By R7-2 Lemma 2.1, applied to the irreducible lifted family of E (product type, Lemma R0), x ∈ M(E_t) for all t outside a closed discrete set D_E. For such t, f_x(p′) ≅ Y_t lies in F, so [Y_t] ∈ A.
- In both cases [Y_t] ∈ A for all t in T_k \ D_E (or Δ_ε \ D_E). This set has an accumulation point in Δ_ε, because D_E is closed and discrete. By Lemma 1, [Y] is constant. Since Y is continuous and the map M_{g_i,n_i} → M_{g_i,n_i}/S_{n_i} has finite fibres, Y is constant, i.e. Y_t = Y_0 for all t. ∎

*Remarks.*
1. Step 1 uses neither (Rig) nor "generic t". (Rig) enters only at the endpoint, through Lemma 2.
2. Theorem 1 is the common form of R7-3 Theorem A (which assumed (NT) everywhere) and R7-1 Theorem T (which assumed (Lock)). The new point is that (SC) is exactly what the twin step needs. Below it is shown to follow from a purely group-theoretic condition, (IP).

## 3. When does (SC) hold? Isotropy preservation and the orbifold reading (proved)

**Corollary 1.** (SC_m) holds in either of the following cases.
- (a) **(IP_m)**: |Aut(J_{m,t})| = |Aut(J_m)| for t in a set with an accumulation point in Δ_ε.
- (b) The lifted branch defining one of the two families at J_m is Aut(J_m)-invariant, i.e. Stab_{Aut(J_m)}(β̃) = Aut(J_m).

*Proof.*
- (a) By (K4), #π^{-1}(J_{m,t}) = |Aut(J_m)| / |Aut(J_{m,t})| = 1 for those t. Both closures contain a point of π^{-1}(J_{m,t}) (§0), so they contain the same point.
- (b) If a ∈ Stab(β̃), then aÑ is the component of π^{-1}(N) containing aβ̃ \ {0} = β̃ \ {0}. So aÑ = Ñ.
  - Hence closure(Ñ_t) ∩ π^{-1}(J_{m,t}) is a nonempty Stab(β̃)-invariant subset of one Aut(J_m)-orbit (K1). If Stab(β̃) = Aut(J_m), it is the whole orbit.
  - So it contains the point that the other closure contains. ∎

**Corollary 2.** Assume the hypotheses of Theorem 1, but replace (C_m) by: "(NT_m), (IP_m) or Corollary 1(b) holds at each J_m". Then Y_t = Y_0 for all t. ∎

**Remark (the orbifold reading).** M̄_g is an orbifold (a DM stack). Suppose "smoothly trivial family" in the problem is read in the orbifold category: the trivialization H, restricted to each stratum, is an orbifold isomorphism, so in particular it preserves isotropy groups. Then:
- **(R2^orb)** |Aut(H_t(z))| = |Aut(z)| for every z ∈ B_0 and every t.
- (R2^orb) gives (IP_m) at every point. So under (R2^orb), **the twin obstruction disappears entirely**. MS8 then holds whenever Prop K's endpoint is MERGE or pMOV.
- The only remaining case is the interior-MOV (crossing) endpoint, together with the inherited inputs (K′) and (PT_chain).

Under the coarse reading (R2) adopted by the task, (IP) is an extra hypothesis. Automorphisms of boundary points can disappear for t ≠ 0, and this is exactly the twin mechanism: §4 shows that a failure of (C_m) forces Aut(J_{m,t}) ⊊ Aut(J_m).

## 4. What a failure of (C_m) forces (proved)

Assume Y is non-constant. Put Z := Z_A ∪ Z_φ ∪ D_all, where:
- Z_A is as in Lemma 2;
- Z_φ is the union, over the finitely many pairs (D, c) with D a piece at time 0 and c a constant vertex of D such that [φ_c] ≢ [Y], of the coincidence sets {t : [φ_c(t)] = [Y_t]}. Each is closed and discrete by Lemma 1.
- D_all is the union, over the pieces at time 0 in product-type strata and the vertices non-constant on them, of the closed discrete exceptional sets of R7-2 Lemma 2.1.

Z is a finite union of closed discrete sets, hence closed and discrete. Call t ∈ Δ_ε \ Z *generic*.

**Proposition 3.** Assume (R1), (R2), (Rig), (K′), (PT_chain, extended to D^{m+1}), and that Y is non-constant.
- **(Junction.)** Suppose [φ_{c_m}] ≡ [Y] but [φ_{c_{m+1}}] ≢ [Y] for some m ≤ k−1. Then (C_m) fails; in particular (IP_m) fails, and (NT_m) fails. Moreover, for every generic t there is a ∈ Aut(J_m) with a^{-1}x_m ≠ x_m such that one of the following holds.
  - **(b) persistent twin.** Along β̃^{m+1}_−, the chart vertex a^{-1}x_m is a single intact vertex w of D^{m+1}, constant on D^{m+1}, with [φ_w] ≡ [Y]. So D^{m+1} carries two distinct constant vertices, c_{m+1} and w, both with value ≅ Y_0 at t = 0, and with different value functions.
  - **(c) junction crossing.** J_m ∈ stratum(D^{m+1}), and a^{-1}x_m is an intact vertex of D^{m+1} that is non-constant on D^{m+1}, with value ≅ Y_0 at J_m.
- **(Endpoint.)** Suppose the endpoint is MERGE or pMOV and [φ_{c_k}] ≡ [Y]. Then (C_k) fails. For every generic t there is a ∈ Aut(Q_0) with a^{-1}x ≠ x such that, along β̃^E, a^{-1}x is a single intact vertex w of E, constant on E, with [φ_w] ≡ [Y]. So Q_0 has two Y_0-copies, x and a^{-1}x, exchanged by a ∈ Aut(Q_0). The copy x merges or moves along β̃^E, while its twin stays along β̃^E and carries Y.

*Proof (junction).*
- (C_m) fails, since otherwise Step 1 of Theorem 1 would give [φ_{c_{m+1}}] ≡ [Y].
- Fix a generic t, and pick j̃ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}). By (∗), F_{x_m}(j̃) ≅ Y_t.
- The coarse branch β^{m+1}_− (or the germ of D^{m+1}, in the interior case) is transported to a branch at J_{m,t}. Its preimage near j̃ lies in ⋃_a (aÑ^{m+1}_−)_t and has j̃ in its closure (R7-4 Lemma 2(b); the interior case is identical). Choose a with j̃ ∈ closure((aÑ^{m+1}_−)_t).
- Along aÑ^{m+1}_−, the class of x_m is a·(the class of a^{-1}x_m along Ñ^{m+1}_−), by (K3). The latter class is the vertex w of D^{m+1} containing a^{-1}x_m along β̃^{m+1}_−, because the vertex structure is constant on Ñ.
- *w merged* (contains an unpinched edge). Then J_m ∉ stratum(D^{m+1}). As in Step 2 of Theorem 1, Y_t ≅ F_{x_m}(j̃) is a component of the puncture value of the non-constant vertex w of D^{m+1}_t. So [Y_t] ∈ A, contradicting t ∉ Z_A.
- *w = {a^{-1}x_m} intact and non-constant on D^{m+1}.*
  - If J_m ∉ stratum(D^{m+1}): since t ∉ D_all, w ∈ M(D^{m+1}_t), and its puncture value is ≅ Y_t. So [Y_t] ∈ A, a contradiction.
  - Otherwise we are in (c). The value at J_m is F_{a^{-1}x_m}(0) ≅ F_{x_m}(a·0) = F_{x_m}(0) ≅ Y_0.
- *w = {a^{-1}x_m} intact and constant on D^{m+1}.*
  - By (K3) and (∗), F_{x_m} ≡ φ_w(t) on closure((aÑ^{m+1}_−)_t). So [φ_w(t)] = [Y_t], and since t ∉ Z_φ, [φ_w] ≡ [Y].
  - If a^{-1}x_m = x_m, then w = c_{m+1}, contradicting [φ_{c_{m+1}}] ≢ [Y]. So a^{-1}x_m ≠ x_m.
  - Two distinct chart vertices that are both intact along β̃^{m+1}_− are distinct vertices of G_{D^{m+1}}. So w ≠ c_{m+1}, and both are constant with value ≅ Y_0 at t = 0. This is (b).
- In cases (b) and (c), a moves x_m, so (NT_m) fails. (IP_m) fails by Corollary 1(a). ∎

*Proof (endpoint).* Identical, with E in place of D^{m+1}.
- The cases "w merged" and "w intact, non-constant" give [Y_t] ∈ A, because Q_0 ∉ stratum(E) in the MERGE and pMOV cases, so the limit point is a puncture. This contradicts genericity.
- So w = {a^{-1}x} is intact and constant with [φ_w] ≡ [Y].
- If a^{-1}x = x, then x would be intact and constant along β̃^E, which contradicts MERGE/pMOV. ∎

**Meaning.** A twin jump needs one of two things:
- a whole piece D^{m+1} that carries two constant Y_0-vertices with different deformations ("persistent twins"), which Prop K's track enters on the wrong one;
- or, at the endpoint, a boundary point Q_0 with an automorphism exchanging the merging copy with a staying twin.

In both cases the automorphism group of the junction must drop for t ≠ 0. This is consistent with R7-3 Theorem B, but here it is derived with (Rig) replacing L2. It also locates the extra structure: persistent twins live on a whole piece of the chain, not only at an isolated point.

## 5. Crossings at generic times are "pure" (proved)

**Lemma 4 (pure crossing).** Assume (Rig) and that Y is non-constant. There is a closed discrete set Z′ ⊃ Z_A such that the following holds for t ∉ Z′.
- Let Q ∈ B_t, q̃ a lift, and x a chart vertex with F_x(q̃) ≅ Y_t.
- Let γ̃ be a lifted branch through q̃ of a piece E with Q ∈ stratum(E) and x ∈ M(E) (an IMOV of x).
- Let β̃ be a lifted branch through q̃ of a piece D with Q ∉ stratum(D), along which x is intact and constant.

Then every w ∈ M(E) is, along β̃, a single intact vertex {w} of D that is constant on D. Hence pr_{M(E)} of the point of E over Q is (φ^D_w(t))_{w∈M(E)} ∈ K(E), a point whose coordinates are constant-vertex values of D.

*Proof.*
- Let F′ be the finite set of classes of components (with special points) of elements of F.
- For (G, M, K) ∈ 𝒦 and w ∈ M, pr_w is non-constant on K: otherwise f_w would be constant on every piece with that triple.
- So F″ := ⋃_{(G,M,K), w ∈ M} K ∩ pr_w^{-1}(F′) is finite. Let A″ be the set of classes of all coordinates of points of F″ of type (g_i, n_i). Put Z′ := Z_A ∪ {t : [Y_t] ∈ A″}, which is closed and discrete by Lemma 1.
- Let w ∈ M(E), and let [w] be the vertex of D containing w along β̃.
  - *[w] ∈ M(D).* Then Q is a puncture of D, and F_w(q̃) is a component of f_{[w]}(p_D) ∈ F. So the point κ := pr_{M(E)}(point of E over Q) ∈ K(E) has its w-coordinate in F′, i.e. κ ∈ F″. Its x-coordinate is F_x(q̃) ≅ Y_t, so [Y_t] ∈ A″, contradicting t ∉ Z′.
  - *[w] constant on D.* Its value is smooth and equals the curve glued from the components in [w]. So [w] = {w} is intact. ∎

So at generic t every crossing adjacent to a coarser staying branch is *pure*: the staying branch freezes every moving vertex of the crossing piece. The point of K(E) at the crossing is κ(t) = (φ^D_w(t))_w. It moves holomorphically along the fixed curve K(E), and its x-coordinate is Y_t. Nothing in (R1), (R2), (Rig) excludes this (compare the local model of R7-2 §4.2). Crossings with D in the same stratum as E are not constrained even this much: there κ(t) is an intersection point of the two fixed-type curves K(D) × {φ^D(t)} and K(E) × {φ^E(t)}.

## 6. Why (SC) is hard under plain (R2): the scale conflict (analysis; not a proof)

This section records why I could not prove (SC), so that the next attempt does not repeat it.

1. **Stars are disjoint (proved sketch).** Fix t. For small W, B_t ∩ W = H_t(B_0 ∩ W) is a cone at J_t: a union of arcs from J_t.
   - Each lifted arc starts at a lift of J_t.
   - Two lifted arcs from different lifts of J_t cannot meet. Away from J_t the stabilizer is locally constant along the arc, so lifting backwards from a common point is unique.
   - Hence π^{-1}(B_t ∩ W) is a disjoint union of "stars", one at each lift of J_t. (SC_m) says that the two transported branches lie in a common star.
2. **Fixed t: the time-t network is coherent inside each star.** At generic t, every Y_t-copy at a lift j̃ stays along every branch of the star of j̃, by Lemma 2 and R7-4 Lemma 1. So inside one star there are no twin problems.
3. **The obstruction is a monodromy.** Transport Prop K's interior path γ_ρ (within ρ of B_0) to time t, as H_t∘γ_ρ.
   - For fixed t and ρ → 0, the transported path stays near a single star, because the stars are at positive mutual distance.
   - In a twin jump, the two branches lie in different stars. So the square (s, τ) ↦ H_τ γ_ρ(s), τ ∈ [0, t], cannot lift to the orbifold chart. It must meet the orbifold locus of 𝒱 (curves with automorphisms), and the monodromy of the square moves the star.
   - These orbifold points lie at times τ where the stars at J_τ are closer together than the distance ε(ρ) of the path to B_τ.
4. **The two scales conflict.**
   - Making the transported path resolve the stars needs ρ ≪ (star separation at time t), and the separation tends to 0 as t → 0.
   - Making the square avoid orbifold points needs t ≪ ρ.
   - I found no way to reconcile the two. The defect of the square is a product of local monodromies around the 2-dimensional orbifold locus O ∩ 𝒱. Jumps at generic τ preserve the time-τ network, since automorphisms preserve isomorphism classes. Jumps at τ → 0 are uncontrolled.

So (SC) is a genuinely mixed statement: Prop K's information is at t = 0, while the coherence lives at t ≠ 0. Under (R2^orb) the problem disappears, because there are then no stars to choose between.



## Prior results, part 2: round 9 (verbatim answer files, bookkeeping line removed; re-check what you use)
In these files, "R8-k" = round8_qk (several are spliced in part 1 above), "PR-x" as in part 1, "the task file" = the round-9 query they answered (its definitions agree with part 1). Ledger numbers: round9_q4 = entries 84 (Theorem X*) and 85 (Prop. K_w); round9_q3 = entries 84 (Theorem X′) and 86; round9_q7 = entry 87; round9_q1 = entry 88; round9_q2 = entry 89; round9_q5 = entry 90; round9_q6 = entry 91; round9_q8 = entry 92.

### round9_q4 (verbatim)
# round9_q4 — answer

**Status.**
- Part 1, the claim (CR*): **proved for every normal singularity**, given Steps 1–4 of Theorem X (R8-1), which I re-checked. Q-factoriality is not needed, and neither is the monomial criterion. The new ingredient replaces Step 5 (Hurwitz applied to a Q-Cartier equation) by a homological intersection argument on a resolution of Ŝ, using Mumford's negative definiteness.
- Part 2, the same-sheet lemma: **the literal reading (TD_J) does not follow from Proposition K as written.** The chain read off the Hausdorff limit K_0 can record a transition at a point J that the approximating rays never pass near. I give a repaired version of Proposition K, the "walk chain", built from a single approximating ray. Every transition of the walk chain is realised by a sub-path that stays inside a small Milnor ball around the transition point. For the walk chain the same-sheet lemma is **proved**.
- Combination: in the walk chain, no junction or endpoint is a crossing, except in the case where the incoming and outgoing branches are the same coarse branch of the same piece. That residual case is the twin case (type (T) of R8-6), which is outside this task.

Plan, written first:
- §1: prove (CR*) in a strengthened form (Theorem X*).
- §2: same-sheet lemma: what fails, and the repair.
- §3: the combination.
- §4: summary of what is proved and what is open.

---

## 1. Part 1: (CR*) for arbitrary normal sheets

### 1.1 Statement
Setting and notation are exactly as in Theorem X (R8-1 §3.1):
- V_0 ⊂ M_g is a closed totally geodesic surface. Smoothness is not needed for this part.
- E is a piece of B_0 in a product-type stratum Δ_G.
- Q_0 ∈ E, so Q_0 lies in Δ_G.
- β is a local branch of E at Q_0, and β̃ is a lift of β to Def(Q_0).
- S is an irreducible component of the germ at 0 of the preimage of closure(V_0) in Def(Q_0), with S ⊃ β̃.
- ν: Ŝ → S is the normalisation, and ŝ_0 = ν^{-1}(0).
- B̂ = ν^{-1}(S ∩ {∏ s_e = 0}).
- Ê_1, …, Ê_r are the components of the germ (B̂, ŝ_0) that map onto β̃, and C_1, …, C_m are the others.

**Theorem X\*.** m = 0. That is, every irreducible component at ŝ_0 of the boundary curve of Ŝ maps onto the single lifted branch β̃.

In particular (CR*) holds. Any sheet S of closure(V_0) at Q_0 that contains a branch of E contains no other boundary curve through Q_0. This excludes boundary curves of other pieces, and also other branches of E itself, including other lifts αβ̃ ≠ β̃ of β.

### 1.2 What is used from Theorem X (re-checked)
Steps 1–4 of R8-1 §3.2 produce the following, and I re-checked each item:
- a connected open set Ω ⊂ 𝔻;
- holomorphic maps D̂_n: Ω → Ŝ with D̂_n(Ω) ∩ B̂ = ∅;
- a holomorphic L̂: Ω → Ŝ with D̂_n → L̂ locally uniformly;
- a point w* ∈ Ω with L̂(w*) = ŝ_0, and L̂(Ω) ⊂ Ê_1.

Here is the check, item by item.
- **L̂(Ω) ⊂ Ê_1.** L̂(Ω) ⊂ B̂, since L takes values in the boundary. The sets L̂^{-1}(Ê_l) and L̂^{-1}(C_i) are analytic and cover Ω, and L̂^{-1}(Ê_1) contains a neighbourhood of 0. By the identity principle it is all of Ω.
- **L̂ is non-constant.** Its image under ν is a lift of L, and L is non-constant by (Fl).
- **L̂^{-1}(ŝ_0) is discrete.** It is analytic and does not contain 0.
- **Surjectivity of L onto E^ν (Step 3).** This uses:
  - the closedness of Teichmüller discs and the local finiteness of their translates, (Prop);
  - finiteness of the set Λ of lifts;
  - properness of L̄.
  I re-checked each of these.
- **Lifting to Def(Q_0) and to Ŝ (Steps 2 and 5).**
  - The Teichmüller disc lifts to T_g. A component of the preimage of the chart interior maps holomorphically to Def(Q_0)°. This is cited, as in R8-1.
  - The lifted disc lies in S, by an analytic-covering argument plus the choice of X̃_n off S ∩ S_i.
  - It lifts to Ŝ by the universal property of normalisation, since X̃_n is off the non-normal locus.
- **Ŝ is smooth off ŝ_0 near ŝ_0.** A normal surface has isolated singular points, and ŝ_0 ∈ B̂. Hence D̂_n maps into the smooth part of Ŝ.

Only Step 5 of R8-1 (the Hurwitz step with a Q-Cartier equation G) is replaced.

### 1.3 Cited standard facts (from memory)
- **(Res)** Let (Ŝ, ŝ_0) be a normal surface germ. There is a resolution π: S′ → W, where W = Ŝ ∩ (closed Milnor ball) is a small closed neighbourhood of ŝ_0, such that:
  - π is an isomorphism over W ∖ {ŝ_0};
  - Exc := π^{-1}(ŝ_0) is a compact connected curve with irreducible components F_1, …, F_p, p ≥ 1. Connectedness follows from Zariski's main theorem. If ŝ_0 is a smooth point, take π to be the blow-up of ŝ_0, so that p = 1 and F_1² = −1.
  - U′ := π^{-1}(int W) deformation retracts onto Exc. Hence H_2(U′; ℤ) is free with basis [F_1], …, [F_p].
- **(Neg)** (Du Val, Mumford, Grauert.) The intersection matrix N = (F_j · F_k) is negative definite.
- **(Int)** Let A ⊂ U′ be a closed analytic curve. The intersection number with A, z ↦ z · A, is a well-defined homomorphism on H_2(U′; ℤ) (Poincaré–Lefschetz duality: A defines a Borel–Moore class). Suppose a 2-cycle z consists of pieces that are disjoint from A, together with holomorphic discs meeting A in isolated interior points. Then z · A is the sum of the local intersection multiplicities at those points, and each multiplicity is > 0.
- **(Pos)** This is elementary, and I prove it here. Let N be a negative definite symmetric real matrix whose off-diagonal entries are ≥ 0 and whose graph ({j,k} is an edge iff N_{jk} > 0) is connected. Let λ ≥ 0 with λ ≠ 0. Then x := −N^{-1}λ has all entries strictly positive.
  *Proof.*
  - Write x = x⁺ − x⁻, where x⁺ and x⁻ are non-negative with disjoint supports.
  - Then (x⁻)ᵀ N x = (x⁻)ᵀ N x⁺ − (x⁻)ᵀ N x⁻.
  - The first term is ≥ 0, because the supports are disjoint and the off-diagonal entries are ≥ 0. The second term, −(x⁻)ᵀ N x⁻, is ≥ 0, with equality only if x⁻ = 0. So (x⁻)ᵀ N x ≥ 0.
  - But (x⁻)ᵀ N x = −λ · x⁻ ≤ 0. Hence x⁻ = 0, i.e. x ≥ 0.
  - Suppose x_j = 0 for some j. Then Σ_{k≠j} N_{jk} x_k = (Nx)_j = −λ_j ≤ 0. Every term on the left is ≥ 0, so x_k = 0 for every neighbour k of j.
  - By connectedness x = 0. Then λ = −Nx = 0, a contradiction. ∎
  For the matrix N of (Neg), the off-diagonal entries F_j · F_k (j ≠ k) are ≥ 0, and the graph is connected because Exc is connected.

### 1.4 Proof of Theorem X*
Suppose m ≥ 1, and fix C := C_1.

**Choices.**
- Choose W as in (Res) so small that, inside W, C ∩ Ê_1 = {ŝ_0}. Distinct irreducible curve germs meet only at the base point.
- Choose ε > 0 so small that the closed disc Ω̄_ε := {|w − w*| ≤ ε} lies in Ω, L̂(Ω̄_ε) ⊂ int W, and L̂^{-1}(ŝ_0) ∩ Ω̄_ε = {w*}.
- For n large, D̂_n(Ω̄_ε) ⊂ int W, by uniform convergence on Ω̄_ε.

**Lifts.**
- D′_n := π^{-1} ∘ D̂_n is holomorphic, since π is an isomorphism over W ∖ {ŝ_0} ⊃ W ∖ B̂.
- Its image avoids π^{-1}(B̂). That set contains Exc, the strict transform C′ of C, and the strict transform Ê′_1.
- L̂|_{Ω_ε} takes values in the curve Ê_1, and is not contained in its singular locus. So it factors through the normalisation of Ê_1, and that normalisation maps holomorphically onto Ê′_1 ⊂ S′. This defines a holomorphic L′: Ω_ε → Ê′_1 ⊂ S′ with π ∘ L′ = L̂.
- L′(w) ∈ Exc only for w = w*.
- C′ ∩ Ê′_1 ⊂ Exc, because C ∩ Ê_1 = {ŝ_0} in W. Hence L′(Ω̄_ε) ∩ C′ = ∅.

**Boundary circles.**
- K := L̂(∂Ω_ε) is a compact subset of Ê_1 ∖ {ŝ_0}. Over a neighbourhood of K, π^{-1} is a biholomorphism. Hence D′_n → L′ uniformly on ∂Ω_ε.
- K′ := L′(∂Ω_ε) is compact and disjoint from Exc ∪ C′. Fix a Riemannian metric and a tubular neighbourhood N_K of K′ in U′ that is disjoint from Exc ∪ C′.
- For n large, the short-geodesic homotopy between D′_n|_{∂Ω_ε} and L′|_{∂Ω_ε} sweeps a singular annulus A_n ⊂ N_K with ∂A_n = L′(∂Ω_ε) − D′_n(∂Ω_ε).

**The cycle.** Put
 Z_n := D′_n(Ω̄_ε) − L′(Ω̄_ε) + A_n.
This is a singular 2-cycle in U′. By (Res), [Z_n] = Σ_j k_j [F_j] with k_j ∈ ℤ.

**Intersection with F_k.**
- The piece D′_n(Ω̄_ε) is disjoint from F_k, and so is A_n.
- L′(Ω̄_ε) meets Exc only at L′(w*), in isolated points. Put λ_k := (local intersection number of the disc L′ with F_k) ≥ 0. Then Σ_k λ_k > 0, because L′(w*) ∈ Exc and L′ ⊄ Exc.
- By (Int), Σ_j k_j (F_j · F_k) = Z_n · F_k = −λ_k for all k. That is, N k = −λ.
- N is invertible by (Neg). So k = −N^{-1}λ, and by (Pos) all k_j > 0.

**Intersection with C′.** C′ is a closed analytic curve in U′.
- Each piece of Z_n is disjoint from C′: D′_n avoids π^{-1}(B̂), L′ avoids C′, and A_n ⊂ N_K. Hence Z_n · C′ = 0.
- On the other hand, Z_n · C′ = Σ_j k_j (F_j · C′).
  - Each F_j · C′ ≥ 0, because F_j ≠ C′ are distinct curves.
  - Some F_j · C′ > 0. C passes through ŝ_0, so points of C ∖ {ŝ_0} accumulate at ŝ_0. Their preimages accumulate on the compact set Exc, and C′ is closed, so C′ ∩ Exc ≠ ∅.
  - With all k_j > 0, this gives Z_n · C′ > 0.

This contradiction proves m = 0. ∎

**Remarks.**
1. In the language of Mumford's ℚ-valued intersection theory, the proof says the following.
   - The local intersection C · L̂ at ŝ_0 is strictly positive, as always for two distinct curves through a normal surface point.
   - Mumford intersection numbers are continuous under the convergence D̂_n → L̂.
   - Mumford's pull-back π^*C = C′ + Σ a_j F_j is numerically trivial on Exc. So the homology class of the bubble Σ k_j F_j that may appear in the limit of the D′_n contributes nothing.

   The Q-Cartier equation G of Theorem X is only needed to make this continuity hold for an honest function. Q-factoriality is therefore irrelevant.
2. Only the following were used: the discs D̂_n avoid the whole boundary B̂, and their limit L̂ is a disc inside one boundary curve Ê_1 passing through ŝ_0. The second fact is the place where total geodesy enters (Lemma PA, (Fl), (Prop): the limit disc sweeps all of E).
3. Strengthening. Two different branches of the same piece E at Q_0 (or two different lifts β̃, αβ̃ of one branch) never lie in a common sheet S of the chart. Indeed, apply Theorem X* with β; the curve over the other branch would be a C_i.
4. As in R8-1 Remark 2, product type of the stratum of E is used: the global coordinate f_j on E appears in Step 3. Non-product strata are not checked.
5. From chart sheets to coarse sheets. Suppose a sheet 𝒮 of closure(V_0) at Q_0 in M̄_g contains a branch b of E and another boundary branch β′. Take a chart component S over 𝒮. The preimage of 𝒮 is ⋃_α αS, so S contains some lift of b and some lift of β′. Theorem X* then gives a contradiction, unless β′ = b as coarse branches.

---

## 2. Part 2: the same-sheet lemma

### 2.1 Sheets and Milnor balls (Lemma S, made precise)
This lemma is cited and standard (local structure of analytic germs).

Let X = closure(V_0) ⊂ M̄_g and Q ∈ B_0. Assume V_0 is smooth, so Sing X ⊂ B_0. Put Z := Sing X ∪ B_0. For W in a fundamental system of small (Milnor) neighbourhoods of Q:
- the connected components of V_0 ∩ W = (X ∖ Z) ∩ W are exactly the sets X_k ∩ W ∖ Z, where X_k runs over the irreducible components of the germ (X, Q);
- each such set is connected, and its closure in W is X_k ∩ W.

Fix such a W. Choose it also so small that B_0 ∩ W is the union of the branches of B_0 at Q, each branch minus Q lying in one stratum. Then:

**Lemma S′.** Let γ: [a,b] → V_0 ∩ W be a path. Suppose there are a sequence of such paths γ_n and points z^1 ∈ β ∖ {Q} and z^2 ∈ β′ ∖ {Q}, where β, β′ are branches of B_0 at Q, such that γ_n(a) → z^1 and γ_n(b) → z^2. Then some sheet X_k contains both β and β′.

*Proof.*
- Pass to a subsequence along which all the γ_n lie in the same component X_k ∩ W ∖ Z. There are finitely many components.
- X_k ∩ W is closed in W, so z^1 ∈ X_k.
- Near z^1, B_0 coincides with β, since z^1 is not Q and W contains no other special point.
- X_k ∩ ∂M̄_g is locally the zero set of ∏ s_e on the 2-dimensional germ X_k. So it is either empty near z^1 or of pure dimension 1 through z^1. It contains z^1, so it is the germ of β at z^1.
- So X_k contains an open piece of the irreducible germ β, hence all of β. The same argument applies to β′. ∎

### 2.2 What fails in the reading (TD_J)
Proposition K (PR-H §3) produces the continuum K_0 as a Hausdorff limit of K(δ_k, η_k). Each K(δ, η) is in turn a Hausdorff limit of the ray segments {g_s X_n : 0 ≤ s ≤ T_n}. The chain D^1, J_1, …, Q_0 is then read off from K_0.

Hausdorff convergence says nothing about the order in which a ray visits the parts of K_0. Here is a failure mode, which nothing in the proof excludes.
- Suppose the rays come near β at J, then leave every small ball around J along β, run around a loop of B_0, and re-enter the ball along β′.
- Then K_0 ⊃ (β ∪ β′) near J, and J ∈ K_0. A chain read off K_0 may record the transition D → D′ "at J".
- But no ray sub-path stays near J while passing from β to β′.

So the clause in (TD_J) that γ maps into V_0 ∩ U, with U a small neighbourhood of J, is not justified by Proposition K as written. In this situation the same-sheet conclusion at J has no support: β and β′ may lie in different sheets at J (the case Cr1). This is exactly what the "routine marking details" hide.

### 2.3 Repair: the walk chain (Proposition K_w)
**Data.**
- P (generic on ∂V_0), (X_n, q_n), the ray γ_n(s) := g_s X_n and T_n = T_n(δ, η) are as in PR-H §2–3.
- **Special set Σ.** Σ is the finite set of points of B_0 consisting of:
  - junctions (points in the closures of two distinct pieces);
  - singular points of B_0;
  - punctures of pieces;
  - points of a piece D at which some vertex non-constant on D has a value of class [Y_0].

  The last kind is finite: a non-constant vertex takes a given value at finitely many points, and there are finitely many pieces and vertices.
- Fix r > 0 so small that:
  - the balls B(J, 3r), J ∈ Σ, are pairwise disjoint;
  - each B(J, 3r) is a Milnor neighbourhood as in §2.1;
  - each B(J, 3r) lies in an orbifold chart Def(J)/Aut(J);
  - P ∉ B(J, 3r) for all J.

  Put K_D := closure(D) ∖ ⋃_J B(J, r/2). This is compact, and the K_D are pairwise disjoint. Let 4ρ_* be the least distance between distinct K_D.
- Choose δ, η small, depending on r, so that (a) and (b) hold.
  - (a) **Short curves are node curves.** If a stable curve z ∈ B_0 lies outside ⋃ B(J, r/2), and X is within distance ρ_* of z, then every curve with Ext_X ≤ δ is a node curve of z under the nearby marking. This holds by compactness of the stratum parts involved (collar lemma, cited).
  - (b) **η separates Y_0.** For every piece D and every vertex u non-constant on D, the class of u on K_D is at distance > 2η from [Y_0]. For every constant vertex of every piece whose value is not ≅ Y_0, the value is at distance > 2η from [Y_0].

**Step 0 (closeness to B_0).** ρ_n := sup_{s ≤ T_n} dist(γ_n(s), B_0) → 0.
- Let s_n ≤ T_n.
- If s_n is bounded, Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n} → 0.
- If s_n → ∞, Lemma NH(1) gives Ext(c_n) ≤ e^{−2s_n}/m → 0.
- In either case every limit point of γ_n(s_n) lies in closure(V_0) ∩ ∂M̄_g = B_0, by Maskit's comparison.

**Step 1 (travel and excursions).** Take n large, with ρ_n < min(ρ_*, r/2).
- A time s is a *travel time* if γ_n(s) lies outside ⋃ B(J, r). Then the B_0-points within ρ_n of γ_n(s) lie in a unique K_D. The piece D is locally constant on maximal intervals of travel times.
- An *excursion* at J is a maximal interval of times in B(J, 2r) that contains a time in B(J, r). Its interior endpoints are travel times on the sphere of radius 2r.
- By uniform continuity there are finitely many excursions. Every excursion crosses the shell r ≤ d ≤ 2r.
- The complement of the excursions consists of travel times, so [0, T_n] is a finite alternation: travel along D^1, excursion at J_1, travel along D^2, …. The first travel is along the piece D^1 ⊃ P of ∂V_0.

**Step 2 (STAY along travel intervals).** Let s be a travel time on D, and z_s ∈ K_D a point at distance < ρ_n from γ_n(s).
- Since Ext(∂Σ_i) ≤ δ, (a) shows that the curves of ∂Σ_i are node curves of z_s.
- ψ is continuous on augmented Teichmüller space, so the Σ_i-side of z_s is within η + o(1) of Y_0. In particular it is a single smooth component, a vertex c of D.
- By (b), c is a constant vertex of D with value ≅ Y_0.
- Consequently, at travel times Ext(∂Σ_i) = o(1) < δ and d(ψ, Y_0) = o(1) < η. So **T_n is not a travel time**, and the walk ends inside an excursion, at some Q ∈ Σ.

**Step 3 (chart consistency inside an excursion at J).**
- During the excursion, γ_n lies in the chart Def(J)/Aut(J) and lifts continuously to γ̃_n in Def(J)°. Path lifting through a finite quotient is cited (Bredon).
- The T_g-marking along γ_n is compatible with the chart. The component of the preimage of the chart in T_g covers Def(J)°, with deck group generated by the Dehn twists about the vanishing cycles and the stabiliser. So the vanishing cycle of each chart edge e is a well-defined marked curve throughout the excursion.
- At the entry time, ∂Σ_i is the set of node curves around the constant vertex c of D. A constant vertex stays intact at J, since its value lies in M_w. So c = {x} for a single chart vertex x along the entry lift β̃ (a branch of D at J), and ∂Σ_i = {vanishing cycles of the edges at x}.
- This identification persists along the whole excursion.
- At the exit time (if the excursion is not the last), Step 2 applies on the exit piece D′ along a lift β̃′. The same x satisfies c′ = {x} along β̃′.

So the walk gives a chain in the sense of (K′): constant vertices c_m ≅ Y_0, and a common chart vertex x_m at each J_m.

**Step 4 (the endpoint).** Let Q be the point of the last excursion, entered from D along β̃ with chart vertex x.
- Take a subsequence n → ∞, with (r, δ, η) fixed. The finite combinatorial data are then constant: Q, D, β̃, x.
- The nearest boundary lifts z̃_n of γ̃_n(T_n) converge to some z̃^∞ ∈ (preimage of B_0) ∩ closure(B(Q, 2r)).
- **z̃^∞ ≠ 0.**
  - F_x(0) ≅ Y_0, by continuity of F_x on L_x along β̃.
  - If z̃^∞ = 0, then near 0 every s_e with e at x tends to 0, so Ext(∂Σ_i) → 0. Also ψ → F_x(0) ≅ Y_0.
  - Both stopping conditions would then fail at T_n.
- So z̃^∞ lies on a lifted branch b̃ ∖ {0} at Q. At T_n one of the two stopping conditions holds.
  - **Ext(γ_e) = δ for some e at x.** Then s_e(z̃^∞) ≠ 0, so e is unpinched along b̃: **MERGE**.
  - **d(ψ, Y_0) = η.** Then all edges at x are pinched along b̃, and d(F_x(z̃^∞), Y_0) = η > 0 while F_x(0) ≅ Y_0: **MOV** (interior or puncture).

**Step 5 (same sheet at every transition).**
- Each junction transition of the walk chain is a sub-path of γ_n inside B(J_m, 2r) ⊂ W. It starts within ρ_n of a point of β^m ∩ shell and ends within ρ_n of a point of β^{m+1} ∩ shell.
- Over the subsequence these points converge to points of the branches other than J_m.
- Lemma S′ applies: the incoming branch and the outgoing branch lie in a common sheet at J_m.
- At the endpoint, the last excursion goes from near β to near z^∞ ≠ Q on b. So β and b lie in a common sheet at Q.

The walk chain depends on (r, δ, η, n), but it is a single finite chain with all the properties (K′) requires. **Proposition K_w (proved, modulo the inputs of PR-H: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T_g ↔ Def chart description, and the collar lemma, all cited):** there is a chain as in (K′), with endpoint MERGE or MOV, in which every transition, including the endpoint, has its incoming and outgoing branches in a common sheet.

---

## 3. Combination with Theorem X*
Assume the pieces of the chain are of product type (PT_chain), as MS8 already assumes. Use the walk chain.

**(a) No junction lies in the stratum of an adjacent piece, except along a single coarse branch.**
- Suppose J_m ∈ stratum(D^{m+1}), i.e. J_m is a point of the piece D^{m+1}.
- The common sheet at J_m contains a branch of D^{m+1} and the incoming branch β^m.
- By Theorem X* and Remark 5, β^m and the outgoing branch are the same coarse branch of the same piece, so D^m = D^{m+1}.
- The same holds with the roles of m and m+1 exchanged.

**(b) The junction crossing of R8-8 Prop. 3(c).**
- Case (c) asserts J_m ∈ stratum(D^{m+1}), with c_{m+1} = {x_m} constant on D^{m+1} along β^{m+1}_−. Strata are transported by H_t, so this is a statement at t = 0.
- By (a), D^m = D^{m+1} and the two branches coincide coarsely. Then the lifts satisfy β̃^{m+1}_− = aβ̃^m_+ for some a ∈ Aut(J_m).
- This is the same-branch twin configuration (type (T) of R8-6), not a crossing.
- So genuine junction crossings (a different piece, or a different coarse branch) do not occur.

**(c) Endpoint.**
- Suppose the endpoint is iMOV, i.e. Q ∈ stratum(E_b).
- The common sheet at Q contains b and β. By Theorem X*, β and b are the same coarse branch, so E_b = D.
- But x is constant along β̃ (STAY) and non-constant along b̃. So b̃ = aβ̃ with ax ≠ x: again the twin type (T).
- Hence the endpoint is MERGE, puncture-MOV, or a same-branch twin.

**Conclusion of the derivation.** Under MS8's hypotheses plus (PT_chain), the walk chain has no interior-MOV endpoint and no junction crossing, apart from configurations of same-branch twin type. The planner's derivation is therefore correct for the walk chain, after this caveat about twins is added. It was not correct for the K_0-chain without the repair of §2.3.

---

## 4. Summary
**Proved:**
- **Theorem X\*** ((CR*) in strengthened form) for every normal sheet. It assumes Steps 1–4 of R8-1 Theorem X (re-checked) and a product-type stratum for E. Its corollary: two distinct coarse boundary branches through an interior point of a piece never share a sheet.
- **Lemma S′** and **Proposition K_w**: the walk chain, whose transitions are local, and which therefore satisfies the same-sheet lemma. This is modulo the cited inputs of PR-H.
- The combination of §3: crossings (Cr1) and (Cr2) are eliminated for the walk chain.

**Found false or unsupported:**
- The reading (TD_J) for the chain read off the Hausdorff limit K_0. The track need not stay near J during the transition (§2.2). The repair is to replace that chain by the walk chain.

**Open / not covered:**
- (i) The same-branch twin configurations (type (T)) at junctions and at the endpoint. These were excluded from this task.
- (ii) Non-product strata (Theorem X Step 3 uses the global coordinate f_j).
- (iii) The cited inputs: (Fl), the T_g ↔ Def chart description, Proposition K's Lemmas PA and NH, and (Res), (Neg), (Int), all cited from memory.
- (iv) Entry 82 (Rig), as before.


### round9_q3 (verbatim)
# round9_q3 answer (final; PARTIAL)

## Status / plan
- MS8 is NOT proved in full here, and no counterexample is given. This file is a PARTIAL answer.
- New results in this file (full summary in §7):
  1. **Theorem X′**: Theorem X of R8-1 holds with no Q-Cartier / Q-factoriality hypothesis. So the crossing case (Cr2) of R8-1 §4.3 disappears for product-type pieces.
  2. **Lemma SS** (same sheet): if V_0 is locally irreducible at its points, every transition of Prop K's track (junction or end point) takes place inside one sheet of closure(V_0). So (Cr1) never occurs at a track transition.
  3. **Lemma PT** (product strata carry no twins): in a product-type stratum, an automorphism of a curve fixes every vertex of positive-dimensional type.
  4. **Corollary IM**: combining 1–3, an interior-MOV end point of Prop K is impossible when the stratum of the end point is of product type. In general (non-product stratum, assuming Theorem X′ extends to it) an interior-MOV end point must be a "same-branch twin" (type (T) of R8-6).
- What remains open: twins at junctions and end points lying in NON-product strata, and the non-product extension of Theorem X / X′ (stated as a remark, not proved).

Conventions: readings (R1), (R2) with H_0 = id, and the notation of the task file. "Product type" for a stratum Δ_G means: the gluing map ξ_G : ∏_w M_w → Δ_G is injective (on coarse spaces). Reading of "smooth" used in Lemma SS: **(Sm)** every point of V_0 is a locally irreducible point of V_0 (this holds if V_0 is a complex submanifold of the coarse space, and also if V_0 is an embedded suborbifold).

---

## 1. Theorem X′: Theorem X without any Q-Cartier hypothesis

### 1.1 Cited standard facts (from memory)
- **(Res)** Resolution of a normal surface germ (Ŝ, ŝ_0): for a small Stein neighbourhood W of ŝ_0 there is a proper holomorphic map π : W̃ → W, W̃ a complex manifold of dimension 2, π biholomorphic over W ∖ {ŝ_0}, with exceptional set E := π^{-1}(ŝ_0) a compact, **connected** curve (Zariski's main theorem, Ŝ normal) with irreducible components E_1, …, E_r. (If ŝ_0 is a smooth point one may take π = blow-up, r = 1.)
- **(Neg)** (Du Val, Mumford, Grauert) The intersection matrix M = (E_k · E_j) is negative definite. Its off-diagonal entries are ≥ 0, and its dual graph is connected because E is connected.
- **(Str)** For an irreducible curve germ A ⊂ Ŝ at ŝ_0, its strict transform Ã := closure of π^{-1}(A ∖ ŝ_0) is an irreducible curve germ meeting E in exactly one point (the normalization of A is a disc, the lift to W̃ of the punctured disc extends continuously by properness). The number Ã · E_j (local intersection number of a curve with a compact curve not containing it) is ≥ 0, and > 0 for some j.
- **(RA)** (Grauert; relative ampleness, from memory) Let L be a holomorphic line bundle on W̃ with deg(L|_{E_k}) > 0 for every k. Then, after shrinking W around ŝ_0, some power L^N is generated by its global holomorphic sections on W̃. (L|_E is ample on the projective curve E because its degree on each component is positive; ampleness on the only positive-dimensional fibre gives π-ampleness near E; then Cartan's Theorem A for the coherent sheaf π_*L^N on the Stein space W.)

### 1.2 An elementary lemma
**Lemma M.** Let M be a real symmetric negative definite r×r matrix with M_{kj} ≥ 0 for k ≠ j and connected graph {k ~ j iff M_{kj} > 0}. If Mc = −b with b ∈ R^r, b ≥ 0, b ≠ 0, then c_k > 0 for all k.

*Proof.* Write c = c⁺ − c⁻ with c⁺, c⁻ ≥ 0 of disjoint supports. Then (c⁻)ᵀMc = (c⁻)ᵀMc⁺ − (c⁻)ᵀMc⁻. The first term is ≥ 0 (disjoint supports, off-diagonal entries ≥ 0), and −(c⁻)ᵀMc⁻ > 0 if c⁻ ≠ 0. But (c⁻)ᵀMc = −(c⁻)ᵀb ≤ 0. Hence c⁻ = 0 and c ≥ 0; c ≠ 0 since b ≠ 0. If c_k = 0 for some k, then −b_k = (Mc)_k = Σ_{j≠k} M_{kj}c_j ≥ 0 forces b_k = 0 and c_j = 0 for all neighbours j of k; by connectedness c = 0, a contradiction. ∎

### 1.3 Lemma P (a pole function for a curve that need not be Q-Cartier)
**Lemma P.** Let (Ŝ, ŝ_0) be a normal 2-dimensional germ, W a small Stein representative, C ⊂ W a curve through ŝ_0 (a finite union of irreducible germs at ŝ_0), and A_1, …, A_l irreducible curve germs at ŝ_0 not contained in C. Then, after shrinking W, there is a holomorphic function g on W ∖ C such that for every l′ and every sequence z_n ∈ A_{l′} ∖ {ŝ_0} with z_n → ŝ_0, |g(z_n)| → ∞.

*Proof.*
1. Take π : W̃ → W as in (Res). Let C̃ be the strict transform of C (union of the strict transforms of its branches), and p_{l′} the point where Ã_{l′} meets E (Str).
2. **Mumford pull-back.** Let b_j := C̃ · E_j ≥ 0; b ≠ 0 because C passes through ŝ_0 (Str). Solve Mc* = −b (M invertible by (Neg)). By Lemma M, c*_k > 0 for all k. So π*C := C̃ + Σ_k c*_k E_k is a Q-divisor with π*C · E_j = 0 for all j.
3. **An anti-ample exceptional cycle.** Solve Mz = −(1, …, 1). By Lemma M, z_k > 0 for all k. Choose an integer d ≥ 1 with dz integral and put Z := Σ_k d z_k E_k, so Z · E_j = −d < 0 for all j.
4. **The divisor D.** Choose an integer m ≥ 1 such that m c*_k ∈ Z and m c*_k − d z_k ≥ 1 for all k. Put D := m π*C − Z = m C̃ + Σ_k (m c*_k − d z_k) E_k. It is an effective integral divisor with support exactly C̃ ∪ E, and D · E_j = −Z · E_j = d > 0 for all j.
5. **Sections.** Let L := O_{W̃}(D) and s its canonical section (div s = D). By (RA), after shrinking W, there is N with L^N globally generated; pick a global section σ of L^N with σ(p_{l′}) ≠ 0 for all l′ (a generic linear combination of generators).
6. Put g̃ := σ / s^N. It is holomorphic on W̃ ∖ supp(D) = W̃ ∖ (C̃ ∪ E). Since π maps W̃ ∖ (C̃ ∪ E) biholomorphically onto W ∖ C, g := g̃ ∘ π^{-1} is holomorphic on W ∖ C.
7. **Blow-up along A_{l′}.** Let z_n ∈ A_{l′} ∖ {ŝ_0}, z_n → ŝ_0. Then z̃_n := π^{-1}(z_n) ∈ Ã_{l′} ∖ E converges to p_{l′} ∈ E (Str). In a local trivialization of L^N near p_{l′}, σ(z̃_n) → σ(p_{l′}) ≠ 0, while s^N(z̃_n) → s^N(p_{l′}) = 0, because p_{l′} ∈ E ⊂ supp(D) (every E_k has coefficient ≥ 1 in D). Hence |g(z_n)| = |g̃(z̃_n)| → ∞. ∎

*Remark.* If C is Q-Cartier, one can take g = 1/G with G as in Theorem X. Lemma P is the replacement when it is not: g is allowed zeros (along curves not in C); only its poles are confined to C. That is all a maximum-principle argument needs.

### 1.4 Statement
Setting of Theorem X (R8-1 §3.1): V_0 ⊂ M_g closed, 2-dimensional, totally geodesic; Δ_G a product-type stratum; E a piece of B_0 in Δ_G; Q_0 ∈ E (an interior point of E); 𝓛_0 ⊂ Def(Q_0) the preimage of closure(V_0) near 0; β a local branch of E at Q_0 with a lift β̃ through 0; S an irreducible component of the germ (𝓛_0, 0) containing β̃; ν : Ŝ → S its normalization, ν^{-1}(0) = {ŝ_0}; B̂ := ν^{-1}(S ∩ {∏_e s_e = 0}).

Call an irreducible component of the germ (B̂, ŝ_0) **of type β** if its image under q∘ν (q : Def(Q_0) → M̄_g the chart map) is contained in β, and **foreign** otherwise.

**Theorem X′.** B̂ has no foreign component at ŝ_0. Equivalently: every boundary curve of the sheet S through 0 lies over the coarse branch β of E.

(Compared with Theorem X(b): no Q-factoriality, no Q-Cartier hypothesis, no monomial condition. In R8-1's notation, every C_i is a curve mapping onto a lift aβ̃, a ∈ Aut(Q_0); if aβ̃ = β̃ for all such curves, m = 0.)

### 1.5 Proof
Assume a foreign component C exists. Let A_1, …, A_l be the components of type β (there is at least one: ν^{-1}(β̃) is a curve through ŝ_0).

**Steps 1–4 of Theorem X are used unchanged.** They give (R8-1 §3.2; I re-read them and use exactly their conclusions): a connected relatively compact open set Ω ⊂ 𝔻 containing 0 and a point w*; holomorphic maps D̂_n : Ω → Ŝ ∖ B̂ (lifts of Teichmüller discs D_n ⊂ V_0, which lie in S because their base points do, and avoid B̂ because D_n ⊂ V_0 ⊂ M_g); and a locally uniform limit L̂ : Ω → Ŝ of D̂_n (Montel in an embedding Û ⊂ C^M) with:
- ν∘L̂ is a lift of L|_Ω, where L : 𝔻 → E^ν is the non-constant limit disc (via (Fl), the Teichmüller vertex j moves);
- L̂(w*) = ŝ_0;
- L(Ω) ⊂ the image of a small disc B ⊂ E^ν around the point e_0 over (Q_0, β), with B ∖ {e_0} mapping into β ∖ {Q_0}.

The only place where Theorem X used the function G is Step 5. I replace it.

**Step 5′.**
1. *L̂ near w* lies in the type-β curves.* For w ∈ Ω, q∘ν∘L̂(w) = L(w) ∈ β. So L̂(Ω) ⊂ ν^{-1}(q^{-1}(β)) ∩ Ŝ ⊂ B̂, and near ŝ_0 this set is the union of the type-β components A_1 ∪ … ∪ A_l (a foreign component maps into β only at ŝ_0, being an irreducible germ not contained in q^{-1}β ∩ …; more precisely, its intersection with ν^{-1}q^{-1}(β) is a proper analytic subset of an irreducible curve germ, hence {ŝ_0} near ŝ_0). L̂ is non-constant (ν∘L̂ lifts the non-constant L), so L̂^{-1}(ŝ_0) is discrete in Ω.
2. *Choice of the small disc.* Shrink W (the Stein representative of (Ŝ, ŝ_0)) so that W ∩ C ∩ (A_1 ∪ … ∪ A_l) = {ŝ_0}, and apply Lemma P to (W, C, A_1, …, A_l): g is holomorphic on W ∖ C and |g| → ∞ along each A_{l′} at ŝ_0. Pick a closed disc Δ* ⊂ Ω centred at w* with L̂(Δ*) ⊂ W and L̂^{-1}(ŝ_0) ∩ Δ* = {w*}. Then L̂(Δ* ∖ {w*}) ⊂ (A_1 ∪ … ∪ A_l) ∖ {ŝ_0} ⊂ W ∖ C, and K := L̂(∂Δ*) is a compact subset of W ∖ C.
3. *Uniform bound on the boundary circle.* D̂_n → L̂ uniformly on Δ*. Fix a compact neighbourhood K′ ⊂ W ∖ C of K. For n large, D̂_n(∂Δ*) ⊂ K′ and D̂_n(Δ*) ⊂ W. g is continuous on K′, so max_{∂Δ*} |g∘D̂_n| → max_{∂Δ*} |g∘L̂| =: e^{μ} < ∞.
4. *Maximum principle.* D̂_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, so g∘D̂_n is holomorphic on Δ*. By the maximum principle, |g∘D̂_n(w)| ≤ max_{∂Δ*}|g∘D̂_n| for all w ∈ Δ*.
5. *Passage to the limit.* For w ∈ Δ* ∖ {w*}, L̂(w) ∈ W ∖ C, where g is continuous, so |g(L̂(w))| = lim_n |g(D̂_n(w))| ≤ e^{μ}.
6. *Contradiction.* Take w_k → w*, w_k ≠ w*. Then L̂(w_k) ∈ (A_1 ∪ … ∪ A_l) ∖ {ŝ_0} and L̂(w_k) → ŝ_0; passing to a subsequence they lie on one A_{l′}. By Lemma P, |g(L̂(w_k))| → ∞, contradicting step 5. ∎

**Remarks.**
1. Total geodesy enters exactly as in Theorem X: through Lemma PA, (Fl), (Prop), which produce discs in the interior of the sheet converging to a parametrisation of the whole branch through Q_0. The new point is only that a holomorphic function with poles confined to C (Lemma P) exists for every curve C on a normal surface germ, whereas a holomorphic function with zeros confined to C exists only if C is Q-Cartier. Hurwitz is replaced by the maximum principle.
2. Sanity check (local crossing model of R7-2 §4.2 at t = 0, S smooth): C = {z = 0} is Cartier, g = 1/z, and the argument is the Hurwitz argument of Theorem X.
3. **Consequence for R8-1 §4.3.** Case (Cr2) ("non-Q-Cartier crossings") does not exist: for every product-type piece E and every Q_0 ∈ E, every sheet of closure(V_0) at Q_0 that contains a branch β of E has no boundary curve through Q_0 other than curves over β. In particular two different pieces never meet at an interior point of a product-type piece inside a common sheet, whatever the singularity of the sheet.
4. **Non-product strata (not proved).** R8-1 Remark 2 says Theorem X uses product type only to have the global coordinate f_j on E; one would work on the lifted piece in ∏_w M_w. The replacement Step 5′ is local in Ŝ and does not care about the stratum type. So Theorem X′ holds for non-product G as soon as Steps 1–4 of Theorem X do. I have not checked those steps for non-product G.

---

## 2. Lemma SS: interior paths stay in one sheet

**Lemma SS.** Assume (Sm). Let U be an open subset of M̄_g, and let X_1, X_2, … be the (global) irreducible components of the analytic set closure(V_0) ∩ U in U. Then V_0 ∩ U is the disjoint union of the sets V_0 ∩ X_k, each of which is open and closed in V_0 ∩ U. Hence every path γ : [a,b] → V_0 ∩ U lies in a single X_k.

*Proof.*
1. Since V_0 is closed in M_g, closure(V_0) ∩ M_g = V_0. So near a point z ∈ V_0 ∩ U the analytic set closure(V_0) coincides with V_0.
2. Each X_k is pure 2-dimensional (closure(V_0) is the closure of the 2-dimensional V_0).
3. Suppose z ∈ V_0 ∩ X_k ∩ X_l with k ≠ l. The germs (X_k, z), (X_l, z) are 2-dimensional and contained in (V_0, z), which is irreducible by (Sm) and 2-dimensional. So (X_k, z) = (V_0, z) = (X_l, z). Then X_k ∩ X_l contains a non-empty open subset of the irreducible analytic set X_k, hence X_k ⊂ X_l (identity theorem for irreducible analytic sets), and so X_k = X_l, a contradiction.
4. Each V_0 ∩ X_k is closed in V_0 ∩ U. The family {X_k} is locally finite in U, so the union of all V_0 ∩ X_l, l ≠ k, is closed too. Its complement in V_0 ∩ U is V_0 ∩ X_k (by 3), which is therefore open.
5. A path is connected, so it lies in one of these open and closed pieces. ∎

**Corollary SS′ (two branches of one transition lie in one sheet at Q_0).** Let Q_0 ∈ B_0 and let b_1, b_2 be branches of B_0 at Q_0. Fix generic points z_1 ∈ b_1, z_2 ∈ b_2 near Q_0, and a small neighbourhood U of Q_0 containing them. Suppose that for every ρ > 0 there is a path γ_ρ : [a,b] → V_0 ∩ U with d(γ_ρ(a), z_1) < ρ and d(γ_ρ(b), z_2) < ρ. (This is supplied by the track data (TD_J) at a junction and (TD_Q) at the end point of Prop K, R8-5 §1 (C2) and §5; they are readings of Proposition K, which is itself "proved modulo routine marking details".) Then:
- (a) there is a global irreducible component X of closure(V_0) ∩ U containing b_1 ∩ U and b_2 ∩ U;
- (b) for any lifts b̃_2 ⊂ Def(Q_0) of b_2 through 0 there is a lift b̃_1 of b_1 through 0 such that b̃_1 and b̃_2 lie in a common irreducible component of the germ at 0 of the preimage of closure(V_0).

*Proof.*
- (a) Only finitely many X_k meet a compact neighbourhood of {z_1, z_2}. By Lemma SS each γ_ρ lies in one X_{k(ρ)}; pass to a sequence ρ_n → 0 with k(ρ_n) = k fixed. Since X_k is closed in U, z_1, z_2 ∈ X_k. X_k ∩ B_0 is an analytic subset of B_0; near z_1 it is pure 1-dimensional (locally, in an orbifold chart, it is the zero set in the 2-dimensional preimage of X_k of the single function ∏ s_e, which is not identically zero on any component; Krull), and B_0 near the generic point z_1 is the smooth curve b_1. So X_k contains the germ of b_1 at z_1, hence the irreducible branch b_1 ∩ U (identity theorem on the normalization of b_1). Same for b_2.
- (b) Shrink U so that U = q(B), B ⊂ Def(Q_0) a small Aut(Q_0)-invariant ball, and so that the global irreducible components of q^{-1}(closure V_0) ∩ B are the germ components at 0 (for a small enough ball an irreducible germ has an irreducible representative; standard, from memory). q^{-1}(X) is a union of such components, and Aut(Q_0) permutes the components of q^{-1}(X) transitively, because X is irreducible and q is the quotient by the finite group Aut(Q_0) (standard). Each lift of a branch contained in X is an irreducible curve contained in q^{-1}(X), hence in one component. Let b̃_2 ⊂ S_2 and pick any lift b̃_1^0 ⊂ S_1 of b_1. Write S_2 = cS_1 with c ∈ Aut(Q_0). Then b̃_1 := c b̃_1^0 ⊂ S_2 is a lift of b_1. ∎

**Remark.** (b) gives a sheet containing *some* lift of b_1 together with the given lift of b_2, not necessarily the lift along which the track arrived. For the coarse statements below this is enough.

---

## 3. Lemma PT: product-type strata carry no twins of positive dimension

**Lemma PT.** Let Δ_G be of product type, Q ∈ Δ_G, and α ∈ Aut(Q). Let x be a vertex of G with dim M_{g_x,n_x} > 0. Then α maps the component Q_x to itself. More generally, the partial-normalization map Π : {s_e = 0 ∀e} ⊂ Def(Q) → ∏_w M_w (comp_y ↦ y-th factor, for a fixed identification G_Q ≅ G) satisfies ξ_G∘Π = q and is independent of the identification; so comp_x = pr_x∘Π on the stratum locus of Def(Q), and comp_x(αp) ≅ comp_x(p) for all α ∈ Aut(Q).

*Proof.*
1. α induces σ ∈ Aut(G), which acts on ∏_w M_w by permuting the factors and relabelling marked points, and ξ_G∘σ = ξ_G on all of ∏_w M_w (gluing does not see the order of the factors).
2. ξ_G is injective (product type), so σ acts as the identity on ∏_w M_w.
3. If σ(x) = x′ ≠ x, then for every z ∈ ∏_w M_w the coordinate z_{x′} would be a fixed relabelling of z_x. Since dim M_x > 0, choose z with z_x arbitrary and z_{x′} different from every relabelling of z_x (possible: the coordinates are independent and M_{x′} ≅ M_x up to relabelling is positive-dimensional). Contradiction. So σ(x) = x.
4. Two identifications G_Q ≅ G differ by some σ ∈ Aut(G); by step 2, Π does not change. By (K3), comp_x(αp) ≅ comp_{α^{-1}x}(p) = comp_x(p). ∎

**Consequences.**
- At a junction J or end point Q_0 of Prop K's chain whose stratum is of product type, (NT) holds for the tracked chart vertex (it has type (g_i,n_i) and dim M_{g_i,n_i} > 0). So no twin jump can occur there (R7-3 Theorem A, R8-8 Theorem 1 with (NT_m)).
- R8-6 type (T) ("same-branch twin") cannot occur at a point of a product-type stratum.
- Hence **every twin problem of the chain lives at points of non-product strata.** (This was used for Δ_Γ in R8-2 Step 4; here it is recorded for all strata.)

---

## 4. Corollary IM: the interior-MOV end point

**Corollary IM.** Assume (Sm), the setting of MS8, and the input (K′) of R8-8 §0 together with the track datum (TD_Q) of R8-5 §5 at the end point. Suppose the end point is of type iMOV: the last STAY piece D^k arrives at Q_0 along a lifted branch β̃^k_+ with c_k = {x} intact and constant, and Q_0 is an interior point of a piece E (Q_0 ∈ stratum(E) =: Δ_G) with lifted branch β̃^E through 0 along which x is intact and non-constant. Then:
- (a) the coarse branch of D^k at Q_0 equals the coarse branch b of E at Q_0 carried by β̃^E; in particular D^k = E;
- (b) if Δ_G is of product type, this is impossible. So **an iMOV end point never lies in a product-type stratum.**
- (c) in general (non-product Δ_G, and assuming Theorem X′ holds there, §1.5 Remark 4), β̃^k_+ = a^{-1}β̃^E for some a ∈ Aut(Q_0) with ax ≠ x: the end point is a same-branch twin (type (T) of R8-6).

*Proof.*
- (a) By (TD_Q), Corollary SS′(b) applies to b_1 := coarse branch of D^k, b_2 := b with the lift β̃^E: there is a lift b̃_1 of b_1 lying with β̃^E in one sheet S at 0. By Theorem X′ (applied to E, the branch b and the sheet S), every boundary curve of S through 0 lies over b. So b_1 ⊂ b as germs, i.e. b_1 = b, and the pieces containing them coincide: D^k = E.
- (b) Now β̃^k_+ and β̃^E are two lifts through 0 of the same coarse branch b of E, both in the stratum locus. By Lemma PT, comp_x = pr_x∘Π on the stratum locus, and Π maps both lifts onto germs of E ⊂ ∏_w M_w at the unique point ê = ξ_G^{-1}(Q_0). pr_x is constant on the germ Π(β̃^k_+), hence (identity theorem on the connected normalization of the irreducible curve E) constant on E, hence constant along Π(β̃^E). So comp_x is constant along β̃^E, contradicting the iMOV hypothesis.
- (c) The lifts of the irreducible coarse germ b through 0 are permuted transitively by Stab(0) = Aut(Q_0) (R8-6 Case 3). So β̃^E = aβ̃^k_+. By (K3), comp_x along β̃^E corresponds to comp_{a^{-1}x} along β̃^k_+; x is constant along β̃^k_+ and comp_x moves along β̃^E, so a^{-1}x ≠ x. ∎

**The same at junctions.** At a junction J_m of the chain at which J_m is an interior point of the next piece D^{m+1} (the "junction crossing" (c) of R8-8 Prop. 3), Corollary SS′ and Theorem X′ (applied to D^{m+1} at J_m) give: the coarse branch of D^m at J_m is a branch of D^{m+1}, so D^m = D^{m+1}. If the stratum of J_m is of product type, R8-8 Prop. 3(c) is impossible anyway by Lemma PT ((NT_m) holds).

**What this does to the crossing obstacle of MS8.**
- (Cr2) of R8-1 §4.3 is eliminated (Theorem X′), for product-type pieces.
- (Cr1) never occurs at a transition of Prop K's track (Corollary SS′).
- The remaining crossing configurations along the chain are same-branch twins (type (T)) at points of non-product strata, i.e. they are twin problems. **Modulo the non-product extension of Theorem X′, the crossing obstacle is absorbed into the twin obstacle.**

---

## 5. The whole chain lies in the coarse network (twin-free statement)

Notation of R8-3: 𝒩 is the set of coarse pieces D (at time 0) such that every point of H_t(closure D) has a Y_t-copy for every t; C_t := ⋃_{D∈𝒩} H_t(closure D). These are defined without tracking any copy.

**Lemma E (boundary exits of the network).** Assume Y is non-constant. Let Q ∈ C_0 and let b be a branch of B_0 at Q with Q ∉ stratum(b) (Q is a puncture of the piece of b). Then the coarse piece D_b of b lies in 𝒩.

*Proof.* Take t generic in the sense of R8-3 §3 (outside a countable set). Q_t := H_t(Q) ∈ C_t, so Q_t has a Y_t-copy; in the chart Def(Q_t) (lift 0) there is a label y with comp_y(0) ≅ Y_t. H_t(b) is a branch of B_t at Q_t with Q_t ∉ stratum(H_t(b)), since H_t preserves strata; let b̃ be any lift of it through 0. By Theorem N (R8-3), y is intact along b̃ and either STAY, or IMOV; IMOV needs Q_t ∈ stratum(H_t b), which is false. So STAY holds, and Theorem N says that the coarse piece D′ with H_t(b) ∖ {Q_t} ⊂ D′_t lies in 𝒩. That piece is D_b. ∎

(No automorphism, no chosen copy and no track enters: Theorem N is about every Y_t-copy at the same lift.)

**Proposition CN (the chain stays in 𝒩).** Assume (Sm), the setting of MS8, Y non-constant, and the chain input (K′) of R8-8 §0 with the track data (TD_J) at each junction and (TD_Q) at the end point. Assume moreover:
- **(X′-strata)** Theorem X′ holds for the pieces D^{m+1} at the junctions J_m with J_m ∈ stratum(D^{m+1}), and for E at the end point if it is of type iMOV. (This is proved in §1 when these strata are of product type.)

Then every piece D^1, …, D^k of the chain lies in 𝒩, every junction and the end point lie in C_0, and the terminal piece (the piece E of the terminal branch β̃^E) lies in 𝒩.

*Proof.* Induction on m. D^1 is a component of ∂V_0, which lies in 𝒩 (vertex i ≡ Y_t). Suppose D^m ∈ 𝒩; then J_m ∈ closure(D^m) ⊂ C_0.
- If J_m ∉ stratum(D^{m+1}), Lemma E gives D^{m+1} ∈ 𝒩.
- If J_m ∈ stratum(D^{m+1}), Corollary SS′(b) (with (TD_J)) puts a lift of the branch of D^m and the lift of the branch of D^{m+1} in one sheet at 0 ∈ Def(J_m); Theorem X′ for D^{m+1} at J_m forces the branch of D^m to lie over the branch of D^{m+1}, so D^m = D^{m+1} ∈ 𝒩.

At the end point Q_0 ∈ closure(D^k) ⊂ C_0: for MERGE and pMOV the terminal branch is a boundary branch at Q_0 (Q_0 ∉ stratum(E)), so E ∈ 𝒩 by Lemma E; for iMOV, Corollary IM(a) gives E = D^k ∈ 𝒩. ∎

**What is left: the label-level twin problem, precisely.** Under the hypotheses of Proposition CN, R8-8 Proposition 3 now reads as follows (its case (c), a junction crossing, is reduced by Proposition CN to D^m = D^{m+1}). If Y is non-constant, there is a point J ∈ C_0 (a junction or the end point) in a **non-product** stratum (Lemma PT), an automorphism a ∈ Aut(J) moving the tracked label x, and a piece D ∈ 𝒩 through J such that along the lift used by the track:
- (b) **persistent twin**: x is an intact constant vertex of D with value ≅ Y_0 at t = 0 but with [φ_x] ≢ [Y], while a^{-1}x is a Y-vertex of D (φ ≡ Y); or
- (e) **end-point twin**: J = Q_0, D = E, x merges or moves along β̃^E, while a^{-1}x is a Y-vertex of E; or
- (T) **turning twin** (only if Theorem X′ is needed at J in a non-product stratum): the track arrives and leaves along two lifts of the same coarse branch, x constant on one and a^{-1}x moving on it.

In all cases the coarse pieces involved are network pieces; the failure is only that Prop K's marking, at a point with a non-trivial automorphism, continues along a copy that is Y_0 at t = 0 but is not one of the copies that deform as Y_t.

**Count lemma (a constraint on such points; proved).** Let Y be non-constant and t generic (outside the countable set Z of R8-3 §3 and the discrete coincidence set Z_φ of R8-8 §4). Let Q ∈ C_t, with chart Def(Q) and Λ := {y : comp_y(0) ≅ Y_t}. For every boundary branch b at Q (Q ∉ stratum(b)) and every lift b̃ through 0, the set of labels that are intact and constant ≡ Y_t along b̃ is exactly Λ. Consequently all network pieces having Q_0 := H_t^{-1}(Q) as a puncture have the same number r of Y-vertices, namely r = |Λ| = the number of components of Q_t isomorphic to Y_t; and in cases (b), (e) above, the piece D (resp. E) has at least r + 1 constant vertices of value ≅ Y_0 at t = 0, or (case (e)) J has at least r + 1 components ≅ Y_0.

*Proof.* Each y ∈ Λ is STAY along b̃ (Theorem N, IMOV excluded at a puncture), so it is intact and constant ≡ Y_t. Conversely a label intact and constant ≡ Y_t along b̃ has comp_y(0) ≅ Y_t by continuity. The Y-vertices of the piece of b at generic t are exactly its constant vertices with value Y_t (a constant vertex with [φ] ≢ [Y] has value ≠ Y_t at generic t), and intact labels along b̃ correspond bijectively to singleton vertices. In cases (b), (e), the label x is a further Y_0-copy outside the limit of Λ. ∎

This does not by itself exclude (b) or (e): it says that at t = 0 the junction (resp. the end point) carries strictly more copies of Y_0 than J_t carries copies of Y_t, and that the extra copy is exchanged with a network copy by an automorphism of J that does not survive for t ≠ 0. (In case (b) the count "r + 1 constant Y_0-vertices of D" is meant for J a puncture of D; if J is an interior point of D we are in case (T).)

---

## 6. A conditional corollary (partial; labelled as such)

**Corollary PC (MS8 when the chain avoids non-product strata).** Assume (Sm), the setting of MS8 (including (Rig)), the chain input (K′) with track data (TD_J), (TD_Q), and that all junctions J_m, the end point Q_0, and all pieces D^m, E of the chain lie in product-type strata. Then Y_t = Y_0 for all t.

*Proof.* By Lemma PT, (NT_m) holds at every junction and at the end point (the tracked label has type (g_i, n_i) with dim M_{g_i,n_i} > 0). By Corollary IM(b), the end point is not iMOV, so it is MERGE or pMOV. R8-8 Theorem 1 (hypotheses: (R1), (R2), MS8 with (Rig), (K′) with end point MERGE or pMOV, (PT_chain), and (C_m) ⇐ (NT_m)) gives Y_t = Y_0. ∎

This is a sub-class result in the sense of the task ("proofs for some strata only"), so it does NOT answer MS8. It is recorded because the crossing hypothesis of earlier versions is no longer needed in it: R8-8 Theorem 1 needed MERGE/pMOV as an assumption; here iMOV is excluded.

---

## 7. Summary

**Proved here (modulo the cited standard facts, and modulo the prior results used as stated: Steps 1–4 of Theorem X (R8-1), Theorem N (R8-3), R8-8 Theorem 1 / Prop. 3, and the readings (K′), (TD_J), (TD_Q) of Proposition K, which are themselves "proved modulo routine marking details"):**
1. Lemma M and **Lemma P**: on a normal surface germ, for any curve C through the point and finitely many other curve germs A_l, there is a holomorphic function on W ∖ C that tends to ∞ along every A_l at the point. No Q-Cartier hypothesis.
2. **Theorem X′**: for a product-type piece E and Q_0 ∈ E, every boundary curve through Q_0 of any sheet of closure(V_0) containing a branch β of E lies over β. This removes the Q-factoriality hypothesis of Theorem X(b) and eliminates case (Cr2) of R8-1 §4.3.
3. **Lemma SS / Corollary SS′**: under (Sm), an interior path stays in one global irreducible component of closure(V_0) ∩ U; so the two branches of every transition of Prop K's track lie in one sheet. This eliminates (Cr1) at track transitions.
4. **Lemma PT**: in a product-type stratum no automorphism moves a vertex of positive-dimensional type. So twins of the tracked copy occur only at points of non-product strata.
5. **Corollary IM**: an iMOV end point is impossible in a product-type stratum; in general (given Theorem X′ there) it is a same-branch twin.
6. **Lemma E, Proposition CN, Count lemma**: if Y is non-constant, Prop K's whole chain (pieces, junctions, end point, terminal piece) lies in the coarse network 𝒩 of R8-3; failures can only be label-level twins at non-product points, with the stated count constraint.
7. **Corollary PC** (sub-class, does not answer MS8): MS8 holds when the chain lies in product-type strata.

**Not proved / open:**
- **MS8 itself.** The remaining case is exactly the label-level twin problem of §5 ((b) persistent twin, (e) end-point twin, (T) turning twin) at junctions or end points lying in **non-product strata**. Neither (Lock), (U_J), (SC), (IP) nor any substitute is established for it. I found no argument and no counterexample.
- **Theorem X′ for non-product strata**: needs Steps 1–4 of Theorem X on the lifted piece in ∏_w M_w (R8-1 Remark 2). Step 5′ itself is stratum-independent. Not checked.
- The inputs (K′), (TD_J), (TD_Q) (readings of Proposition K) remain "modulo routine marking details", as before.
- Entry 82 ((Rig) for every admissible family) is untouched; it is not part of MS8.

**On the chain's derivation of the problem from MS8:** I found no new flaw. The derivation still needs entry 82 (open) in addition to MS8, as the task file says.

**Open question (precise form of what is missing).** Let J ∈ B_0 lie in a non-product stratum, let D, D′ ∈ 𝒩 be network pieces having J as a puncture whose branches lie in a common sheet of closure(V_0) at J, and let x be a label at a lift of J that is a Y-vertex along a lift of D and an intact constant vertex with [φ_x] ≢ [Y] along a lift of D′ in the same sheet (or merges/moves along it). Can this happen for a smooth closed totally geodesic V_0 and a family V_t satisfying (R1), (R2), (Rig)? A negative answer, together with the non-product extension of Theorem X′, would prove MS8 (modulo the Prop K readings), by Proposition CN and R8-8 Theorem 1 / Proposition 3.


### round9_q7 (verbatim)
# round9_q7 — answer (MS8)

**Status: PARTIAL.** I do not prove MS8 in full and I do not give a counterexample. What I do:
- I prove three structural lemmas (T, S, J) from (R1), (R2) and (Rig).
- From them I get a reduction (Theorem R): MS8 holds unless the Prop K track meets one of two explicitly described configurations, (R-tw) "twin switch" and (R-cr) "interior MOV crossing".
- Both residual configurations stay OPEN. Inside the reduction they are the precise forms of the chain's "residual twins" and "residual crossings".

New compared with the round-8 material:
- **Lemma T.** H transports each piece into a single irreducible component of the boundary total space, both globally and locally at a point. The proof uses a non-separation argument from dimension theory. Before this, transport through crossings was not controlled.
- **Lemma S.** Under (Rig), a component of the boundary total space has the same non-constant vertex set M and the same curve K on *every* fibre, including t = 0.
- **Consequence.** A "crossing" can occur only at a twin switch or at the final branch of the track. It cannot occur in the middle of an aligned track.

Readings: (R1), (R2) as in the task, with H_0 = id. (Rig) as in MS8. Throughout, F denotes the finite set of pointed curves (with all orderings of special points) that occur as a smooth component of some coordinate of some point of K ∩ ∂(∏_{u∈M} M̄_u), for (G,M,K) ∈ 𝒦. It is finite because 𝒦 is finite and each K is an irreducible curve not contained in the boundary.

**Pinning principle (P).** If Y_t ∈ F for all t in a nonempty open set U ⊂ Δ, then Y ≡ Y_0.

*Proof.* Y is continuous and takes values in a finite set on a connected open subset of U, so it is constant there. By holomorphy (PR-A) and the identity theorem, which applies in an orbifold chart, Y is constant on Δ. ∎

## 1. Notation

- ℬ := closure(𝒱) ∩ (∂M̄_g × Δ). By (R1) it is analytic. By (R2) it is homeomorphic over Δ to B_0 × Δ, hence of pure dimension 2.
- Every irreducible component of ℬ dominates Δ, since fibres are 1-dimensional. So by Krull every fibre of every component is pure 1-dimensional.
- For a stratum Δ_G put ℬ_G := ℬ ∩ (Δ_G × Δ). This is an analytic subset of Δ_G × Δ.
- A *component of ℬ_G* means an irreducible component of ℬ_G. It has dimension 2, because H maps (B_0 ∩ Δ_G) × Δ onto it and B_0 ∩ Δ_G is 1-dimensional or empty.
- A *piece* at time 0 is an irreducible component E of B_0 ∩ Δ_G.

## 2. Lemma T (transport respects components)

**Lemma T.** Let E be a piece at time 0 in Δ_G.
(a) There is a unique component κ(E) of ℬ_G with H(E × Δ) ⊂ κ(E).
(b) Every component 𝒲 of ℬ_G satisfies 𝒲 = ∪_{κ(E)=𝒲} H(E × Δ). In particular 𝒲_0 = ∪_{κ(E)=𝒲} E, and a piece E lies in 𝒲_0 iff κ(E) = 𝒲.
(c) (Local version.) Let Q ∈ B_0 and let β be a branch at Q of a piece E. Let ℬ^{(1)}, …, ℬ^{(m)} be the local irreducible components at (Q,0) of the germ of ℬ_{G_β} ∪ {deeper strata}, i.e. of ℬ. For a small closed sub-branch β′ ∋ Q and a small disc D ∋ 0, H(β′ × D) lies in exactly one ℬ^{(k(β))}. Hence (H_t(Q), t) ∈ ℬ^{(k(β))} for t ∈ D. Moreover ℬ^{(k(β))} is a local component at (Q,0) of closure(κ(E)).

*Proof.*
1. Let E° be E minus the singular points of the analytic set B_0 ∩ Δ_G. This removes finitely many points of E. E° is a connected real 2-manifold, because E is irreducible and its regular locus minus a finite set is connected. So E° × Δ is a connected real 4-manifold.
2. Let Σ := Sing(ℬ_G). This includes all pairwise intersections of components. It is analytic of complex dimension ≤ 1, so its covering dimension is ≤ 2.
3. H^{-1}(Σ) ∩ (E° × Δ) is closed in E° × Δ and homeomorphic to a subset of Σ, so its dimension is ≤ 2 = 4 − 2.
4. Cited from memory (Hurewicz–Wallman, *Dimension Theory*, Thm IV 4): a closed subset of dimension ≤ n − 2 does not separate a connected n-manifold. So R := (E° × Δ) \ H^{-1}(Σ) is connected.
5. H(R) is a connected subset of Reg(ℬ_G). Each connected component of Reg(ℬ_G) lies in exactly one irreducible component. So H(R) lies in one component 𝒲 = κ(E).
6. R is dense in E × Δ, since a closed set of dimension ≤ 2 has empty interior in a 4-manifold, and E° is dense in E. Taking closures in Δ_G × Δ gives H(E × Δ) ⊂ 𝒲, because 𝒲 is closed there. Uniqueness: H(R) is not contained in Σ. This proves (a).
7. For (b), let x ∈ 𝒲 lie on no other component. By (R2), x = H(e,t) with e in some piece E′ of B_0 ∩ Δ_G. By (a), H(E′ × Δ) ⊂ κ(E′), and x is on no other component, so κ(E′) = 𝒲. So 𝒲 \ (other components) ⊂ ∪_{κ(E′)=𝒲} H(E′ × Δ).
8. The right-hand side is closed in Δ_G × Δ: it is a locally finite union of images of the relatively closed sets E′ × Δ under the homeomorphism H. The left-hand side is dense in 𝒲. This gives (b). If E ⊂ 𝒲_0 = ∪_{κ(E′)=𝒲} E′, then E = E′ for one of them, by irreducibility.
9. (c) is the same argument. Replace E° × Δ by β°′ × D, where β°′ = β′ \ {Q} is a punctured disc. Replace Σ by the singular locus of the germ union the pairwise intersections of the ℬ^{(k)}. Continuity of H at (Q,0) keeps H(β′ × D) inside a representative neighbourhood. Then (H_t(Q),t) ∈ closure(H(β°′ × {t})) ⊂ ℬ^{(k(β))}. The last claim holds because H(β′ × D) ⊂ κ(E). ∎

**Remark.** Lemma T is exactly what is needed to transport "which sheet" a branch lies on, using only the coarse homeomorphism H. It does not give vertex labels: H says nothing about the action of Aut(Q). That is where twins enter.

## 3. Lemma S (structure of components under (Rig))

Let 𝒲 be a component of ℬ_G. Let 𝒲̃ be an irreducible component of its preimage in ∏_{w∈V(G)} M_w × Δ; this is a finite map, and the preimage is permuted by Aut(G). Write f_u for the coordinate maps.

**Lemma S.**
(a) There are a set M = M(𝒲) ⊂ V(G) and an irreducible curve K = K(𝒲) with (G,M,K) ∈ 𝒦 such that:
- for every t, every 1-dimensional irreducible component E of 𝒲̃_t has M(E) = M and K(E) = K;
- t = 0 is included.
(b) For u ∉ M, the map (f_u, t): 𝒲̃ → M_u × Δ has 1-dimensional image 𝒞_u. So f_u is constant on each connected component of each fibre 𝒲̃_t, taking finitely many values c_u(t) that vary in t as a multivalued holomorphic function.
(c) Let x ∉ M. Suppose f_x ≅ Y_t (as pointed curves, some ordering) on a subset of 𝒲̃ of real dimension 4. Then it holds on all of 𝒲̃.

*Proof.*
1. Let M be the set of u such that f_u is non-constant on the components of the generic fibre. For u ∉ M, the image of (f_u,t) is 1-dimensional: its fibres over t are finite for generic t, and it is irreducible. So the image is a curve finite over Δ near generic points. Its closure meets each {t} in a discrete set, for every t, because the image is an irreducible curve that is not a vertical line. A vertical line would need f_u to be non-constant on fibre components. So f_u takes finitely many locally constant values on 𝒲̃_t for every t. This is (b).
2. By (Rig), for generic t the pieces of 𝒲̃_t carry curves from the finite set 𝒦. So by irreducibility and continuity one K works for all generic t, and 𝒲̃ maps into K × ∏_{u∉M} M_u × Δ (a closed condition), for all t.
3. Let E be any 1-dimensional component of a fibre, including t = 0. By (b), the vertices u ∉ M are constant on E. Since E is 1-dimensional, its image in K is not a point, hence it is dense in K. Each u ∈ M has non-constant projection on K, by the definition of M. So M(E) = M and K(E) = K. This is (a).
4. (c): {p ∈ 𝒲̃ : f_x(p) ≅ Y_{t(p)}} is analytic, since Y is holomorphic. An analytic subset of an irreducible 2-dimensional space that has real dimension 4 is the whole space. ∎

**Definition (persistent).** Call 𝒲 *persistent* if its generic points have a Y_t-copy. Equivalently, by S(c) and the Lemma D(1) argument, some vertex x ∉ M(𝒲) has f_x ≡ Y_t on 𝒲̃. Such an x is a *persistent vertex*.
- Every component κ(E), with E a component of ∂V_0, is persistent with persistent vertex i: H_t(E) ⊂ ∂V_t, and vertex i of ∂V_t is Y_t.
- Locally at a point (Q,0) with Q ∈ Δ_{G_Q}: let 𝒲̃^a be a germ component of the preimage of closure(𝒲) in Def(Q) × Δ. If 𝒲 is persistent, there is a vertex y_a of G_Q such that all edges at y_a are identically 0 on 𝒲̃^a and z_{y_a} ≅ Y_t on 𝒲̃^a.
  - Proof: limits of smooth Y_t-copies at nearby points are smooth, so as in Lemma D(1) the copy comes from a single intact vertex. Finitely many vertices cover the irreducible germ, so one vertex works everywhere on it.

## 4. Lemma J (junction trichotomy)

**Setting.**
- Q ∈ B_0 lies in Δ_{G_Q}.
- β is a branch at Q of a piece E. Let 𝒲̃^a be a germ component at (0,0) ∈ Def(Q) × Δ of the preimage of ℬ^{(k(β))}, containing a lift β̃ of β. Assume 𝒲̃^a has persistent vertex x.
- b is another branch at Q, of a piece E″ in stratum Δ_{G″}. Let 𝒲̃″ be a germ component of the preimage of ℬ^{(k(b))} containing a lift b̃ of b.
- U_b := the edges of G_Q that are not identically 0 on b̃. Then G″ = G_Q / U_b.
- Write [y] for the vertex of G″ containing y.

**Lemma J.** There are g′ ∈ Aut(Q) and a nonempty open set U ⊂ Δ \ {0} near 0 such that, with x̂ := g′^{-1}x, exactly one of the following holds.
- **(J1) pinned:** Y_t ∈ F for t ∈ U. Hence Y ≡ Y_0 by (P). This happens whenever, along b̃ (equivalently, generically on 𝒲̃″), x̂ is merged, i.e. [x̂] ≠ {x̂}. It also happens whenever [x̂] = {x̂} ∈ M(κ(E″)) and U_b ≠ ∅ (puncture-move).
- **(J2) persistent:** [x̂] = {x̂} ∉ M(κ(E″)). Then x̂ is a persistent vertex of 𝒲̃″, so κ(E″) is persistent.
- **(J3) crossing:** U_b = ∅, so b lies in the stratum of Q and Q is an interior point of E″, and x̂ ∈ M(κ(E″)).

*Proof.*
1. **Finding g′ and U.** Put Q_t := H_t(Q). By Lemma T(c), (Q_t,t) ∈ ℬ^{(k(β))} ∩ ℬ^{(k(b))} for t ∈ D. The preimage of ℬ^{(k(β))} is ∪_g g𝒲̃^a, because Aut(Q) permutes the preimage components of an irreducible germ transitively, and similarly for ℬ^{(k(b))}.
   - For g, h ∈ Aut(Q), let T_{g,h} := {t ∈ D* : some lift of Q_t lies in g𝒲̃^a ∩ h𝒲̃″}. These are finitely many sets covering D*.
   - Each is closed in D*: lifts of Q_t stay in a compact neighbourhood of 0, since the preimage of Q is {0}.
   - By Baire, some T_{g,h} has interior. Put g′ := g^{-1}h. Then for t in an open set U there is q_t ∈ 𝒲̃^a ∩ g′𝒲̃″ over (Q_t,t).
   - Shrink U to avoid the discrete set of t over which some germ component has a fibre component inside a deeper stratum. Then for t ∈ U, q_t is a limit of points of the fibre at t of g′𝒲̃″ that lie in the generic stratum Δ_{G″} (relabelled by g′).
2. **At q_t.** Since q_t ∈ 𝒲̃^a, vertex x is intact at q_t and z_x(q_t) ≅ Y_t. On g′𝒲̃″ the role of x is played by the vertex x̂ = g′^{-1}x of 𝒲̃″. So in what follows, "x on g′𝒲̃″" is "x̂ on 𝒲̃″".
3. **Merged.** Suppose [x̂] ≠ {x̂}.
   - (i) [x̂] ∈ M″. If not, the [x̂]-coordinate is constant, equal to c, a smooth curve, on fibre components at t. Its limit at q_t is the curve assembled from the components in [x̂]. That curve contains an edge at x̂, which is pinched at q_t because x is intact there, so it is nodal and differs from c. Contradiction.
   - (ii) So the limit at q_t of the M″-coordinates is a point of K(κ(E″)) whose [x̂]-coordinate is nodal. That is a point of K ∩ ∂, and z_x(q_t) ≅ Y_t is a smooth component of it. Hence Y_t ∈ F. This is (J1).
4. **Puncture-move.** Suppose [x̂] = {x̂} ∈ M″ and U_b ≠ ∅. Some edge e ∈ U_b lies inside some vertex group [w] of G″. As in step 3(i), [w] ∈ M″. So the limit point of K at q_t lies in K ∩ ∂, and its x̂-coordinate is z_x(q_t) ≅ Y_t. Hence Y_t ∈ F. This is (J1).
5. **Constant.** Suppose [x̂] = {x̂} ∉ M″. By Lemma S(b), z_x is constant on the fibre components of g′𝒲̃″ through q_t, and q_t lies in the closure of their generic part. So the constant is z_x(q_t) ≅ Y_t, for every t ∈ U. The union of these fibre components over t ∈ U has real dimension 4. By S(c), applied to the germ and then to the global irreducible component, x̂ is persistent on 𝒲̃″ and κ(E″) is persistent. This is (J2).
6. **The remaining case** is [x̂] = {x̂} ∈ M″ with U_b = ∅, which is (J3).
7. **Generic behaviour equals behaviour along b̃.** The generic points of b̃ and of 𝒲̃″ lie in the same stratum Δ_{G″}, because E″ ⊂ κ(E″)_0 ∩ Δ_{G″}. So U_b is the set of edges not identically 0 on 𝒲̃″. By Lemma S(a), the piece E″ has M(E″) = M(κ(E″)). So "x̂ merged / moving / constant along b at t = 0" coincides with the generic behaviour on 𝒲̃″. ∎

**Corollary J′ (aligned junctions).** In Lemma J, suppose x̂ = x, i.e. g′ fixes the vertex x. Suppose also that x is intact and constant along b at t = 0, as happens in the middle of a Prop K track. Then (J2) holds with persistent vertex x on 𝒲̃″ ⊃ b̃.
- (J3) cannot occur: x constant along b implies x ∉ M(κ(E″)), by Lemma J step 7.
- (J1) cannot occur either: under the hypothesis x is neither merged nor moving along b.

So **in an aligned track, crossings never occur in the middle**. They can occur only at a non-aligned junction (g′x ≠ x) or at the terminal branch.

## 5. Theorem R (reduction of MS8)

**Input from Prop K (PR-H §3), used as stated there, "modulo routine marking details".**
- There is a compact connected K_0 ⊂ B_0 containing a generic point P of ∂V_0, and a point Q_0 ∈ K_0 with a terminal branch b_* of type MERGE or MOV.
- The labeled Σ_i-vertex x is intact and ≅ Y_0 along K_0, consistently with the path marking.
- A closed connected subset of the finite topological graph B_0 is path-connected through finitely many vertices. So there is an embedded arc in K_0 from P to Q_0, passing through finitely many junction points Q_1, …, Q_r. At each Q_k the arc arrives along a branch β_k and leaves along a branch b_k. Lifts β̃_k, b̃_k carry the *same* labeled track vertex x; this is the marking consistency.
- Inside a piece the persistent vertex does not change. By Lemma S(c) it is a global property of the lifted component κ(E) with the labeling of E.

**Definitions.**
- A junction (including the terminal point Q_0 with b = b_*) is *aligned* if, in Lemma J applied with x the track vertex, some admissible g′ fixes x.
- Otherwise it is *non-aligned*. Then g′x ≠ x for every admissible g′, so x and x̂ = g′^{-1}x are two distinct components of Q exchanged by an automorphism of Q. These are twins in the sense of PR-I.

**Theorem R.** Assume (R1), (R2), (Rig) and the conclusion of Prop K. Suppose every junction Q_1, …, Q_r is aligned, Q_0 is aligned, and the terminal branch b_* is MERGE or MOV with b_* not contained in the stratum of Q_0 (puncture-MOV). Then Y_t = Y_0 for all t.

*Proof.*
1. **Base.** The arc starts in a component of ∂V_0, whose κ is persistent with persistent vertex i = x (§3).
2. **Induction.** Inside a piece the persistent vertex is unchanged. At an aligned junction Q_k, Corollary J′ either pins Y (and we are done by (P)) or makes x persistent on the germ containing b̃_k, hence on κ of the next piece.
3. **Terminal point.** At Q_0, alignment gives x̂ = x.
   - If b_* is MERGE for x, then x is merged along b_*, which is case (J1) step 3.
   - If b_* is puncture-MOV, then x ∈ M with U_b ≠ ∅, which is case (J1) step 4.
   - Either way Y_t ∈ F for t in an open set, and (P) gives Y ≡ Y_0. ∎

**What Theorem R does not cover: the residual configurations (OPEN).**
- **(R-tw) Twin switch.** Some junction Q (possibly Q_0) is non-aligned. Then Q has a nontrivial automorphism g′ with g′x ≠ x. Along the outgoing branch, the persistent copy is x̂ = g′^{-1}x, whose value is ≡ Y_t on its component, while the track copy x is not persistent there. Its constant c(t) satisfies c(0) = Y_0 and c ≢ Y_t, or x is merged/moving generically but not at t = 0.
  - Lemma J still gives (J1), (J2) or (J3) for x̂. In case (J2) the network of *persistent* pieces continues, but on a different copy than the track. Prop K says nothing about where x̂ eventually merges or moves.
  - Restarting Prop K from the piece with the copy x̂ (Lemma PA applies to any piece, PR-H Remark) produces a new track that can switch again. I found no well-founded quantity that rules out infinitely many switches or cycles.
- **(R-cr) Interior MOV / crossing.** Either the terminal branch b_* (aligned) lies in the stratum of Q_0 and x moves along it, or a non-aligned junction falls into (J3). Then Y_t ∈ pr_x(K) for a fixed K ∈ 𝒦 and t near 0. This is a curve condition, not a finiteness condition, so no pinning follows. Excluding it would need more: either that a Prop K track can be continued past an interior MOV point, or a further geometric property of totally geodesic V_0. Theorem X (R8-1) covers only crossings inside a common Q-factorial sheet.

**Relation to the chain.**
- Lemma T shows that the coarse homeomorphism H always respects irreducible components, globally and locally. So "crossings" in the sense of H mixing sheets do not occur.
- Lemmas S and J then show that the only crossings that matter are (J3)-crossings, and Corollary J′ shows these occur only at non-aligned junctions or at the terminal branch.
- So the open part of MS8 is exactly (R-tw) together with the terminal (R-cr). This matches the chain's list of "residual twins and residual crossings", in a sharper form.
- I found no flaw in the chain's derivation of the problem's claim from MS8 in the part I used: holomorphy of Y_t (PR-A) and the finiteness of F under (Rig). I did not audit the rest of the chain.

## 6. Summary

**Proved here** (from (R1), (R2), (Rig); dimension-theory and analytic-geometry facts cited from memory as indicated):
- Lemma T: H maps each piece into a unique global, and local, irreducible component.
- Lemma S: M and K are constant on all fibres of each component, including t = 0. Constant vertices vary along a curve 𝒞_u finite over Δ. Persistence of a Y-copy is a property of the whole component.
- Lemma J: the junction trichotomy pinned / persistent / crossing, for the transported vertex x̂ = g′^{-1}x.
- Corollary J′: there are no crossings inside an aligned track.
- Theorem R: MS8 holds whenever the Prop K track is aligned at all its junctions and its terminal branch is a MERGE or a puncture-MOV.

**Not proved: MS8 in full.** The open cases are (R-tw), a non-aligned (twin) junction, and (R-cr), a terminal interior MOV or a (J3) crossing after a twin switch. Theorem R depends on these extra conditions, so by the task's rules it is a partial result, not a proof of MS8.

**No counterexample** was constructed.



### round9_q5 (verbatim)
# round9_q5 — the twin step (TW*): fixed loci of automorphisms

## Status / plan (written first; updated at the end)

**Final status: (TW\*) is NOT proved and NOT refuted.**

Proved (sections 1–3):
- **Case (C)** of R8-5 Prop. D is not an obstruction.
- Any α-fixed locus contained in {τ = 0} is not an obstruction.
- So a twin jump requires a family of α-symmetric curves in V_τ, τ ≠ 0, near J of complex dimension at least 2 (cases (D2), (D3)).
- In case (A2), total geodesy forces this family to restrict at τ = 0 to a Teichmüller curve of α-symmetric curves of V_0 with cusp J, or to an α-symmetric sheet of V_0.
- A boundary-trace trichotomy (Lemma 3) gives pointwise Lock at J(τ), or Lock on α-stable transported pieces. But it does not reach the persistent twin pair of the chain.

Open questions are listed in §5.

Plan:
1. Sharpen R8-5 Theorem A, and Theorem B, by a general-position argument. Branch points of 𝒞° → 𝒜 matter only if they form a **2-dimensional** set at times τ ≠ 0. This removes case (C) of R8-5 Prop. D. It also removes every bad locus lying in {τ = 0}: a whole α-fixed sheet of V_0, or an α-fixed curve of V_0 that does not deform.
2. Use total geodesy (Teichmüller uniqueness) to show the following. In the surviving case (A), the τ = 0 slice of the bad locus is the lift of a **Teichmüller curve of α-symmetric curves of V_0 with cusp J**.
3. Analyse the boundary trace Ψ of a surviving 2-dimensional bad component Φ. Ψ forces either α ∈ Aut(J(τ)) at a lift of J(τ), or a **locked pair of vertices on a whole transported piece**. Record what is missing to close (TW*).

Departure from the named approach: case (C) is not excluded by total geodesy. It is excluded by a dimension count (real codimension 4 in a 6-manifold), which makes it invisible to the 2-parameter squares of Theorem A. Total geodesy enters only in step 2.

---

## 0. Setting, readings and notation

Everything is as in the task. That is: MS8 with (Rig); readings (R1), (R2) with H_0 = id; the chain of Proposition K in the chart forms (TD_J), (TD_Q) of R8-5 §1, §5; and the chart conventions (C1)–(C3) of R8-5 §1. In particular, at a junction J:
- B ⊂ Def(J) is an Aut(J)-invariant ball and q : B → U the quotient. 𝒱_U = 𝒱 ∩ (U × Δ_ε).
- 𝒞° is the connected component of q^{-1}(𝒱_U) containing γ̃ × {0}, and 𝒜 = q(𝒞°) = 𝒞°/Γ (Fact 0 of R8-5).
- Γ = Stab_{Aut(J)}(𝒞°), K is the kernel of Γ acting on 𝒞°, and Γ_x = Stab_Γ(x).

As the task allows, I assume no junction crossings: each J_m is a puncture of every piece through it. So J is isolated in B_0 ∩ Δ_{G_J}.

Two further readings are made explicit, because they are used below.
- **(R3)** φ : 𝒱 → Δ is a holomorphic submersion. This is the natural reading of "smoothly trivial family of submanifolds" (Ehresmann). It is used only in Lemma 1, to perturb squares inside the time slices.
- **(T4)** The lifted track γ̃ of (TD_J) (resp. (TD_Q)) lies in a single *global sheet*. That is, near each of its points it lies on the image in Def(J) of one fixed component S of the preimage of V_0 in T_g. Prop. K's tracks are Teichmüller ray segments, so they lie in one Teichmüller disc and hence in one such S (this is the input of R8-2 §4.3 Step 1). "Totally geodesic" is read as in the literature: every component S of the preimage of V_0 in T_g is a complex submanifold that contains every real Teichmüller geodesic tangent to it.

**Bad sets.** For α ∈ Γ \ KΓ_x let Fix(α) := Fix_B(α) × Δ_ε. This is a smooth submanifold, since the action is linear in suitable coordinates. closure(𝒞°) is a 3-dimensional analytic set (R8-5 Prop. D proof). Shrink B and ε once and for all, so that:
- every irreducible component of every Fix(α) ∩ closure(𝒞°) passes through (0,0);
- every such component with τ ≢ 0 on it has the following property: if it has dimension 1, then τ restricted to it is a finite map.

Both are possible by the local finiteness of germs. As in R8-5, I assume the tracks of (TD_J) exist in the shrunken chart.

Call such a component Φ **relevant** if Φ ⊄ {∏ s_e = 0} and τ|_Φ ≢ 0.

**Hypothesis (U″_J).** For every α ∈ Γ \ KΓ_x, every relevant component of Fix(α) ∩ closure(𝒞°) has dimension 1.

Compare R8-5's (U_J): there are no α-fixed points in 𝒞° near (J,0) at all, i.e. no component of Fix(α) ∩ closure(𝒞°) meets 𝒞°. (U″_J) is much weaker:
- it allows α-fixed points at τ = 0 (any dimension);
- it allows 1-dimensional fixed loci at τ ≠ 0 (case (C) of Prop. D).

## 1. Squares only see 2-dimensional bad loci (proved)

Put
- 𝔅_all := {p ∈ 𝒞° : Stab_Γ(p) ⊄ KΓ_x} = ⋃_{α ∈ Γ∖KΓ_x} Fix(α) ∩ 𝒞°;
- 𝔅^+ := the union of Φ ∩ 𝒞° over the relevant 1-dimensional components Φ;
- A := q(𝔅^+) ⊂ 𝒜.

**Lemma 0.** Assume (U″_J). Then:
- (a) 𝔅_all ∩ {τ ≠ 0} ⊂ 𝔅^+;
- (b) A is a closed analytic subset of 𝒜 of dimension ≤ 1, contained in {τ ≠ 0}, and A ∩ 𝒜_τ is finite for every τ;
- (c) over 𝒜^good := 𝒜 ∩ {τ ≠ 0} ∖ A, the map π : 𝒞′ := 𝒞°/(KΓ_x) → 𝒜 is a covering map on each connected component.

*Proof.*
- (a) Let p ∈ 𝒞° with τ(p) ≠ 0 and α ∈ Stab_Γ(p) \ KΓ_x. Then p lies on some component Φ of Fix(α) ∩ closure(𝒞°). Φ ⊄ {∏ s_e = 0}, because p ∈ B°, and τ(p) ≠ 0. So Φ is relevant, hence 1-dimensional by (U″_J), and p ∈ 𝔅^+.
- (b) 𝔅^+ is closed in 𝒞° and analytic. q|_{𝒞°} is the finite quotient map by Γ (Fact 0). So A is closed (q is closed) and analytic of dimension ≤ 1 (Remmert, finite maps).
  - Each relevant 1-dimensional Φ meets {τ = 0} only in (0,0) ∉ 𝒞°, and τ|_Φ is finite. Hence A ⊂ {τ ≠ 0}, and its τ-fibres are finite.
- (c) By (a), every p ∈ q^{-1}(𝒜^good) has Stab_Γ(p) ⊂ KΓ_x. Apply Lemma 1 of R8-5 (intermediate quotients) with H = KΓ_x, over the open set 𝒜^good. ∎

**Lemma 1 (general position, time-preserving).** Assume (R3). Let Q := [a,b] × [0,1], fix t ≠ 0, and let F : Q → 𝒜 be smooth with φ(F(s,τ)) = τt and F(Q) ∩ A = ∅ near the bottom edge. Then for every η > 0 there are τ_1 > 0 and a smooth F′ : Q → 𝒜 such that:
- φ(F′(s,τ)) = τt;
- F′ = F on [a,b] × [0,τ_1];
- d̄(F′, F) < η uniformly;
- F′(Q) ∩ A = ∅.

*Proof.*
1. F^{-1}(A) is compact and misses the bottom edge (A ⊂ {τ ≠ 0}). So it lies in {τ ≥ 2τ_1} for some τ_1 > 0.
2. Let N be a relatively compact neighbourhood of F(Q) in 𝒜. By (R3), ker dφ is a smooth real rank-4 subbundle of T𝒜. Choose finitely many smooth vertical vector fields v_1, …, v_k on N spanning ker dφ at every point of closure(N).
3. Let χ : [0,1] → [0,1] be smooth, with χ = 0 on [0,τ_1] and χ = 1 on [2τ_1,1]. For p ∈ P := {p ∈ R^k : |p| < p_0} put
 G(s,τ,p) := time-1 flow of χ(τ) Σ_j p_j v_j, applied to F(s,τ).
   - For p_0 small this is defined and lies in N.
   - Vertical flows preserve φ, so φ∘G = τt. Also G_p = F on τ ≤ τ_1, and G_p → F uniformly as p → 0.
4. On {τ ≤ 2τ_1}: F misses the closed set A there, so G_p does too for p small (compactness).
5. On Q′ := [a,b] × [2τ_1,1], χ = 1, and ∂G/∂p spans ker dφ at G(s,τ,p) for p small (true at p = 0, and surjectivity is open). Let 𝒜_seg := φ^{-1}({σt : σ ∈ [0,1]}), a real 5-manifold with boundary. Then Ĝ := G|_{Q′×P} : Q′ × P → 𝒜_seg is a submersion: the p-directions give ker dφ, and ∂_τ G has dφ(∂_τ G) = t ≠ 0.
6. A_seg := A ∩ 𝒜_seg ∩ closure(N) is the preimage of a real segment under the finite holomorphic map φ|_A. So it is a compact semianalytic set of real dimension ≤ 1, a finite union of points and smooth arcs (stratification of semianalytic sets; standard, cited from memory).
   - Since Ĝ is a submersion, Ĝ^{-1}(arc) and Ĝ^{-1}(point) are submanifolds of codimension 4 and 5 in Q′ × P, i.e. of dimension ≤ (k+2) − 4 = k − 2.
   - Their projections to P are smooth images of manifolds of dimension < k, hence of measure zero.
7. So for almost every small p, G_p misses A. Take F′ := G_p with p so small that d̄(G_p, F) < η. ∎

**Lemma 2 (branching over τ = 0 is harmless).** Assume (U″_J), (R3) and (T4). Let F′ be as in Lemma 1, with F′(s,0) = γ(s), and with γ̃ a lift of γ as in (TD_J) satisfying (T4) and the genericity condition (G) below. Let λ be a lift in 𝒞° of the top edge F′(·,1) with λ(a) = μ_a(1), where μ_a is a lift of F′(a,·) from γ̃(a). Then for every s there are:
- a lift μ_s in 𝒞° of F′(s,·) with μ_s(0) = γ̃(s), and
- κ_s ∈ Γ_x,

with λ(s) = κ_s μ_s(1).

**(G)** γ̃ avoids the set Bad_0 ⊂ 𝒞°_0 := 𝒞° ∩ {τ = 0} of points p that satisfy one of:
- p is a singular point of q^{-1}(V_0 ∩ U);
- p lies on two different local sheets;
- Stab_Γ(p) is strictly larger than the pointwise stabiliser of its local sheet.

Bad_0 is an analytic subset of 𝒞°_0 of dimension ≤ 1. By (T4), γ̃ moves inside one global sheet S, a smooth complex surface, in which Bad_0 ∩ S is a proper analytic subset. So γ̃ can be perturbed inside S, by an arbitrarily small amount, to satisfy (G). This is the argument of R8-2 §4.3 Step 1, which also checks that (TD_J)'s conditions (T1)–(T3) survive, with ρ replaced by 2ρ, since they are open.

*Proof.*
1. **The covering of the τ = 0 slice.** Let R_0 := 𝒞°_0 \ Bad_0, which is Γ-invariant.
   - At p ∈ R_0, G_p := Stab_Γ(p) acts trivially on the unique smooth local sheet X through p. Take a G_p-invariant neighbourhood W of p with gW ∩ W = ∅ for g ∉ G_p.
   - Then W ∩ 𝒞°_0 = W ∩ X maps homeomorphically onto its image in 𝒜_0 := 𝒜 ∩ {τ = 0}, both from 𝒞°_0 and from 𝒞′_0 := 𝒞°_0/(KΓ_x).
   - So 𝒞′_0 → 𝒜_0 is a local homeomorphism at the classes of points of R_0. Since R_0 is saturated, it is a covering over q(R_0). In particular, lifts to 𝒞′_0 of paths in q(R_0) are unique given their initial point.
2. **Lifting the half-open square.** Q^+ := [a,b] × (0,1] is contractible, and F′(Q^+) ⊂ 𝒜^good (Lemma 1: φ∘F′ = τt ≠ 0 and F′ misses A). By Lemma 0(c) there is a lift L̂ : Q^+ → 𝒞′ with L̂(a,τ) = [μ_a(τ)].
3. **Extension to τ = 0.** Fix s.
   - π : 𝒞′ → 𝒜 is a finite quotient map of Hausdorff spaces. So a small neighbourhood N of γ(s) has preimage a disjoint union of neighbourhoods N_j of the finitely many fibre points.
   - The connected set F′([s−δ, s+δ] × (0,δ]) lies in N for δ small, so its lift lies in a single N_j.
   - Hence L̂ extends continuously to Q, and L̂(·,0) is a continuous lift of γ to 𝒞′_0.
4. **The extended bottom edge is [γ̃].** At s = a, L̂(a,0) = [γ̃(a)]. Both L̂(·,0) and s ↦ [γ̃(s)] are lifts of γ to 𝒞′_0, and γ(s) ∈ q(R_0) by (G). By uniqueness (step 1), L̂(s,0) = [γ̃(s)] for all s.
5. **The vertical lifts.**
   - Path lifting for finite group quotients (Bredon, II.6.2, cited from memory) gives a lift ν_s : [0,1] → 𝒞° of the path τ ↦ L̂(s,τ) in 𝒞′, through the quotient 𝒞° → 𝒞′. It starts at ν_s(0) = m γ̃(s) with m ∈ KΓ_x. Put μ_s := m^{-1} ν_s. This is a lift of F′(s,·) with μ_s(0) = γ̃(s).
   - L̂(·,1) and [λ] are both lifts of F′(·,1) to the covering over 𝒜^good, starting at [μ_a(1)]. So they coincide.
   - Hence λ(s) ∈ KΓ_x ν_s(1) = KΓ_x m μ_s(1) = KΓ_x μ_s(1). As K is normal and acts trivially on 𝒞°, λ(s) = κ_s μ_s(1) with κ_s ∈ Γ_x (as in R8-5 Lemma 2). ∎

Note the difference from R8-5 Lemma 2: there the vertical lift μ_s was arbitrary. Here it is *some* lift from γ̃(s). This suffices, because R8-5 Corollary 3′ holds for **every** lift of F(s,·) from γ̃(s): its proof only uses that the lift starts at γ̃(s), within ρ of ẑ_s.

**Theorem A″.** R8-5 Theorem A holds with (U_J) replaced by (U″_J), assuming (R3) and (T4). That is, under (TD_J), (T4), (R3) and (U″_J) at J we get φ_{c_{k−1}} ≡ φ_{c_k} on Δ.

*Proof.* Run the proof of R8-5 Theorem A with the following changes.
1. Fix t, r_1 and ρ as there, and take the track. Make γ smooth and generic, satisfying (G), by Lemma 2's remark. Then F(s,τ) := H(γ(s), τt) is smooth, because H is smooth on V_0 × Δ.
2. Replace F by the F′ of Lemma 1, with η < ε_1. F′ is still time-preserving, and its bottom edge is still γ.
3. Corollary 3′ of R8-5 applies to F′ with ε_1 replaced by 2ε_1: every point of the vertical path F′(s,·) is within ε_1 + η < 2ε_1 of H(z_s, τt). Accordingly, require ρ < 2ε_1 < d′(r_1,t)/3 in the choice of constants.
4. Take the lifts μ_s and κ_s ∈ Γ_x from Lemma 2 instead of R8-5 Lemma 2.
5. Everything after "**Lifts.**" in R8-5's proof is then unchanged:
   - regime (ii) uses κ_s ∈ Γ_x and Corollary 3′;
   - regime (i) uses d̄(qλ(s), J(t)) < η + ε_1 + ω_H(r_1) ≤ r_2, after adjusting the constant;
   - then near-continuity, and the endpoints s = a and s = b. ∎

**Theorem B″.** R8-5 Theorem B holds with (U_{Q_0}) replaced by (U″_{Q_0}), the same hypothesis written in the chart at Q_0, assuming (R3) and (T4).

*Proof.* Its proof uses only:
- the class-function argument of Theorem A on [a, s_*], to which the changes above apply verbatim;
- the identity λ(e) = κ_e μ_e(1) with κ_e ∈ Γ_x and μ_e a vertical lift from γ̃(e), which Lemma 2 provides;
- the separation constants d″ and η_1(t), which are unaffected by a perturbation of size η < ε_1. ∎

**Corollary 1 (R8-5 Prop. D sharpened).** Assume (R3) and (T4). If a twin jump occurs at a junction J (φ_{c_{k−1}} ≢ φ_{c_k}), then there are α ∈ Γ \ KΓ_x and a relevant component Φ of Fix(α) ∩ closure(𝒞°) with dim Φ ≥ 2. The same holds at the endpoint Q_0 if the conclusion of Theorem B fails. In particular:
- **case (C) of R8-5 Prop. D is not an obstruction;**
- nor is any α-fixed locus contained in {τ = 0}. This includes the α-symmetric curves of V_0 that do not deform, and whole α-symmetric sheets of V_0.

The surviving obstructions are:
- **(D3)** dim Φ = 3: α fixes pointwise a whole irreducible component of closure(𝒞°) (possible only if 𝒞° is reducible, since α ∉ K);
- **(D2)** dim Φ = 2 and τ|_Φ ≢ 0. Then Φ_0 := Φ ∩ {τ = 0} has pure dimension 1 (Krull), and either
  - **(A2)** Φ_0 meets B° arbitrarily close to 0, or
  - **(B)** Φ_0 ⊂ {∏ s_e = 0}.

  In both cases, for each small τ ≠ 0, Φ_τ is a complex curve of α-symmetric curves in (the lift of) V_τ near J.

*Proof.* Contrapositive of Theorems A″ and B″, together with the dimension count of R8-5 Prop. D(b). ∎

## 2. Total geodesy: the τ = 0 slice in case (A2) (proved, modulo cited Teichmüller facts)

**Cited facts (from memory, standard).**
- (Te1) *Teichmüller's theorem.* For X ∈ T_g and every unit tangent direction v at X there is exactly one real Teichmüller geodesic ray from X with initial direction v.
  - The map (r, v) ↦ (point at distance r on that ray) is a homeomorphism from T_X T_g ≅ R^{6g−6} onto T_g.
  - This uses the fact that q ↦ [q̄/|q|] is a homeomorphism from the unit sphere of Q(X) onto the unit sphere of T_X T_g, which holds by strict convexity of the L^1 norm on Q(X) and the infinitesimal Teichmüller theorem.
- (Te2) The Teichmüller disc of (X, q) is the union of the real geodesics from X in the directions e^{iθ}v_q. It is a closed, properly embedded holomorphic disc, the image of a holomorphic isometry H → T_g.
- (Te3) For a finite-order mapping class h with Fix(h) ≠ ∅, Fix(h) ⊂ T_g is a closed connected complex submanifold (Cartan linearisation; it is the Teichmüller space of the quotient orbifold).

**Lemma TG.** Let S be a component of the preimage of V_0 in T_g, which is totally geodesic in the sense of §0 (T4). Let h be as in (Te3). Then every irreducible component I of S ∩ Fix(h) is one of:
- a point;
- a single full Teichmüller disc D ⊂ S ∩ Fix(h);
- S itself.

*Proof.*
1. **Fix(h) is totally geodesic.** Let X ∈ Fix(h) and v ∈ T_X Fix(h), i.e. dh_X(v) = v. The isometry h maps the ray from X in direction v to the ray from hX = X in direction v. By uniqueness (Te1) these coincide, and h fixes the ray pointwise.
2. **The tangent intersection.** Let X be a smooth point of I lying on no other component of S ∩ Fix(h), and put L := T_X S ∩ T_X Fix(h), a complex subspace. For v ∈ L the ray in direction v lies in S (total geodesy of S) and in Fix(h) (step 1).
3. **Case L = T_X S.** The restriction of the homeomorphism of (Te1) to the real 4-dimensional subspace T_X S is injective and continuous, with image in S. By invariance of domain its image contains a neighbourhood of X in S, and that neighbourhood lies in Fix(h). So I contains a non-empty open subset of the connected complex manifold S, and I = S.
4. **Case dim_C L = 1 and dim I = 1.** By (Te2) the disc D tangent to L at X is a union of rays with directions in L, so D ⊂ S ∩ Fix(h). Since X lies on I only, D ⊂ I near X. Then:
   - D is irreducible and closed, and it shares an open piece with the irreducible 1-dimensional I, so D ⊂ I;
   - D is 1-dimensional and closed, so I = D.
5. **Remaining cases.**
   - If dim I = 2, then I = S, since I is closed analytic in the connected surface S.
   - If dim I = 1, step 3 cannot occur (it would give I = S), and T_X I ⊂ L. So step 4 applies.
   - Otherwise I is a point. ∎

**Corollary 2 (structure of case (A2)).** In case (A2) of Corollary 1, let p ∈ Φ_0 ∩ B° be a point near 0 that lies on no boundary component of Φ_0. Near p, the chart is a neighbourhood in T_g of a marked lift of the curve C_p, α corresponds to a mapping class h fixing that lift, and q^{-1}(V_0) corresponds to the union of the components S of the preimage of V_0. So by Lemma TG one of the following holds.
- **(A2-disc)** The interior part of Φ_0 lies on lifts of a **Teichmüller curve 𝒯 ⊂ V_0 all of whose curves carry the automorphism h**, and J ∈ closure(𝒯) is a cusp of 𝒯. Indeed:
  - the image in M_g of the disc D lies in V_0 ∩ M_g^{[h]}, where M_g^{[h]} is the closed algebraic locus of curves admitting an automorphism of type [h];
  - the component of V_0 ∩ M_g^{[h]} containing it is a closed algebraic curve whose lift contains D, i.e. a Teichmüller curve.
- **(A2-sheet)** Φ_0 lies inside a sheet of q^{-1}(V_0) that is fixed pointwise by α. Then every curve of V_0 on that sheet near J has the automorphism h, and Φ_τ is the part of it that stays α-symmetric for τ ≠ 0.

In both cases the automorphism exchanges the regions x and αx. Since F_x(0) = F_{α^{-1}x}(0) by (K3), every Aut(J)-translate of x is a Y_0-copy of J.

So total geodesy turns the vague "α-symmetric curves of V_0 near J" into a rigid object: a Teichmüller curve with cusp J, or a whole symmetric sheet. Neither, by itself, says anything about the deformed V_τ, which is not totally geodesic. That is why §3 turns to the boundary trace of Φ at τ ≠ 0.

## 3. The boundary trace of a surviving 2-dimensional bad locus (proved)

Let (α, Φ) be as in (D2). Put Ψ := Φ ∩ {∏ s_e = 0}. Φ is irreducible of dimension 2, not contained in the hypersurface {∏ s_e = 0}, and (0,0) ∈ Φ. So Ψ has pure dimension 1 at (0,0) (Krull).

Moreover Ψ ⊂ closure(𝒞°) ∩ {∏ s_e = 0} ⊂ q^{-1}(𝓑), where 𝓑 := closure(𝒱) ∩ (∂M̄_g × Δ) = H(B_0 × Δ) (R2). Near (J,0) the preimage q^{-1}(𝓑) is the disjoint union of:
- 𝒥 := q^{-1}(H({J} × Δ_ε)), the set of lifts of the points J(τ) := H_τ(J). Because J is isolated in B_0 ∩ Δ_{G_J} (no crossing), H({J} × Δ_ε) = 𝓑 ∩ (Δ_{G_J} × Δ_ε) near (J,0), and no deeper stratum meets a small neighbourhood of J. So this is an analytic curve, finite over Δ_ε, and 𝒥 is analytic.
- the components Z ∈ 𝒵 of q^{-1}(H(B_0^U × Δ_ε)) (R8-5 §3). Each Z has a constant pattern S(Z), and Z_0 = Z ∩ {τ = 0} is a lifted punctured boundary branch.

**Lemma 3 (trichotomy for the trace).** Let Ψ_1 be an irreducible component of the germ of Ψ at (0,0). Exactly one of the following holds.
- **(Ψ-0)** Ψ_1 ⊂ {τ = 0}. Then Ψ_1 is a lifted boundary branch of B_0 at J, fixed pointwise by α.
- **(Ψ-J)** Ψ_1 ⊂ 𝒥 and τ|_{Ψ_1} ≢ 0. Then for every small τ ≠ 0 some lift ĵ(τ) of J(τ) is fixed by α. So α ∈ Stab(ĵ(τ)) ≅ Aut(J(τ)) (K4), and F_x(ĵ(τ)) ≅ F_{αx}(ĵ(τ)): the twins x, αx of J(τ) are isomorphic at that lift ("pointwise Lock").
- **(Ψ-Z)** Ψ_1 \ {(0,0)} ⊂ Z for a single Z ∈ 𝒵, τ|_{Ψ_1} ≢ 0, and αZ = Z. Let D_Z be the piece of the branch underlying Z and G_Z its graph. Then α induces an automorphism ᾱ of G_Z, and:
  - (i) if ᾱ[x] ≠ [x] and both [x], [αx] are constant on D_Z, then φ_{[x]} ≡ φ_{[αx]} on Δ. This is **(Lock) of the pair on the whole transported piece D_{Z,τ}**;
  - (ii) if exactly one of them, say w, is constant and the other, u, is moving, then for every small τ the value φ_w(τ) is the u-coordinate of a point of the fixed curve K_W (Lemma U of R8-2). This is a coincidence of exactly the type excluded by (NB_∂) of R8-2;
  - (iii) if both are moving, the point of K_W over Ψ_1 ∩ {τ} has isomorphic [x]- and [αx]-coordinates for every τ.

*Proof.*
1. If τ ≡ 0 on Ψ_1, then Ψ_1 ⊂ closure(𝒞°) ∩ {τ = 0} ∩ {∏ s_e = 0}. This set lies over B_0 by (R2), since H_0 = id and H commutes with closures. A 1-dimensional germ there is a lifted branch of B_0, and it lies in Fix(α). This is (Ψ-0).
2. Otherwise τ|_{Ψ_1} is finite, and Ψ_1 ∩ {τ = 0} = {(0,0)} near (0,0). The germ Ψ_1 \ {(0,0)} is connected (an irreducible curve germ minus its centre is a punctured disc, after shrinking). Either Ψ_1 ⊂ 𝒥, or Ψ_1 ∩ 𝒥 is a proper analytic subset of the irreducible curve germ, hence ⊂ {(0,0)}.
   - In the first case, every point of Ψ_1 is an α-fixed lift of some J(τ), and τ(Ψ_1) is a neighbourhood of 0. Lifts of J(τ) lie in {s_e = 0 for all e} ⊂ L_x ∩ L_{αx}. By (K3) with σ = α^{-1} and α^{-1}ĵ = ĵ: F_x(ĵ) = F_x(α^{-1}ĵ) = F_{αx}(ĵ).
   - In the second case, Ψ_1 \ {(0,0)} lies in the disjoint union of the relatively open sets Z, so it lies in one of them. Take p ∈ Ψ_1 \ {(0,0)}. αZ is the component of q^{-1}(H(B_0^U × Δ)) containing αp = p, so αZ = Z.
3. **(Ψ-Z), the graph automorphism.** αZ = Z gives αS(Z) = S(Z). So α permutes the edges outside S(Z), and it descends to an automorphism ᾱ of G_Z = G_J/(E \ S(Z)) with ᾱ[y] = [αy].
4. **The comparison.** At p ∈ (Ψ_1)_τ, α is an automorphism of the fibre curve C_p. It maps the partial normalisation of C_p along the nodes in S(Z) to itself, and it carries the [x]-part isomorphically onto the [αx]-part. So, in the lifted transported piece over D_{Z,τ}, the [x]- and [αx]-coordinates of the point over p are isomorphic as pointed curves up to relabelling.
   - (i) Both coordinates are the constant values φ_{[x]}(τ), φ_{[αx]}(τ). They agree for all small τ ≠ 0, and both are holomorphic (R7-3 Lemma 1(a)), so they agree identically (identity theorem in the coarse space, R8-8 Lemma 1).
   - (ii) The moving coordinate at the point over p is a coordinate of a point of K_W, where W is the component of the lifted boundary family containing D_{Z,τ} (R8-2 Lemma U: D = K_W × {c_D}).
   - (iii) This is the same statement as (ii) with both coordinates on K_W. ∎

**Where the Ψ-components come from.**
- In case (A2) with Φ_0 ∩ {∏ s_e = 0} = {(0,0)} near 0, every component of Ψ is of type (Ψ-J) or (Ψ-Z), and there is at least one.
- In case (B), Ψ ⊇ Φ_0, and it can happen that Ψ = Φ_0. I call this **(B-pure)**: for τ ≠ 0, the α-symmetric curves Φ_τ ⊂ V_τ are disjoint from the boundary near J, and they converge, as τ → 0, to the α-fixed lifted boundary branch Φ_0. Lemma 3 gives no information at τ ≠ 0 in (B-pure).

## 4. Consequences for (TW*), and why (Lock) does not yet follow

**Corollary 3 (conditional (TW*), proved).** Assume the setting of (TW*), with no crossings, together with (R3) and (T4).
- If (U″_{J_m}) holds at every junction, then (TW*)(a) holds: [φ_{c_m}] ≡ [Y] for all m. This follows by induction from φ_{c_1} = Y and Theorem A″.
- If moreover (U″_{Q_0}) holds, then (TW*)(b) holds for all t in a punctured disc minus a countable set, by Theorem B″. So MS8 holds in this case (R8-5 Corollary C).
- At each junction, (U″_J) may be replaced by (Lock_J), using R7-1 Step 2 as in R8-5 Remark 3.

In words: **a counterexample to (TW*)(a) at J requires α ∈ Γ \ KΓ_x such that, for every small τ ≠ 0, V_τ contains near J a whole complex curve (case D2) or an open set (case D3) of curves on which α acts as an automorphism moving the tracked region x.** Isolated α-symmetric curves of V_τ (case (C)), or α-symmetry present only at τ = 0, do not suffice.

**What (D2) looks like, combining §§2–3.**
- (A2-disc): V_0 contains a Teichmüller curve 𝒯 of h-symmetric curves with cusp J. 𝒯 deforms to curves Φ_τ ⊂ V_τ ∩ M_g^{[h]}. The boundary trace gives either α ∈ Aut(J(τ)) at a lift (Ψ-J), or an α-stable transported branch Z on which the pair ([x],[αx]) is locked or (NB_∂)-coincident (Ψ-Z).
- (A2-sheet): the same, with 𝒯 replaced by a curve inside an α-symmetric sheet of V_0.
- (B): an α-fixed boundary branch at τ = 0, possibly with no boundary trace at τ ≠ 0 (B-pure).

**Why this does not give (Lock) of the persistent twin.** By R8-8 Prop. 3(b), a twin jump at J_m means the following. D^{m+1} carries two constant vertices, c_{m+1} = {x_m} and w = {a^{-1}x_m} along β̃^{m+1}, with [φ_w] ≡ [Y] ≢ [φ_{c_{m+1}}]. The jump is excluded exactly by (Lock) of this pair on D^{m+1}.

Lemma 3 (Ψ-Z)(i) produces (Lock) of a pair ([x],[αx]), but only on the pieces D_Z that the trace Ψ of a bad locus enters. To conclude, one would need:
- (L1) some bad component Φ, for an α whose conjugacy class contributes to the monodromy κ_b of the square, has a (Ψ-Z) trace in a translate g·Ñ^{m+1}_− of the D^{m+1}-family;
- (L2) with g^{-1}{x, αx} = {x_m, a^{-1}x_m}.

Neither (L1) nor (L2) follows from the construction. The monodromy κ_b is a product of local monodromies at the isolated points where the (perturbed) square crosses the real-codimension-2 set q(Φ). These crossings can lie in regime (i), near J(τt), where they are unrelated to any particular Z. This is the scale conflict of R8-8 §6, now localised: by Lemma 1 it concerns **only** 2-dimensional bad loci.

**Status of the three configurations of the task.**
- **Case (C):** *not an obstruction* (Theorem A″/B″, Corollary 1). Proved, given (R3), (T4) and the inputs (TD_J)/(TD_Q).
- **Case (A):** the part with Φ ⊂ {τ = 0} is *not an obstruction* (Lemma 2). The part with τ|_Φ ≢ 0 (A2) is reduced to a Teichmüller curve 𝒯 ⊂ V_0 of α-symmetric curves with cusp J (Lemma TG), or a symmetric sheet, deforming inside V_τ ∩ M_g^{[h]}. It is **not excluded**.
- **Case (B):** **not excluded**. Its sub-case (B-pure) is invisible to the boundary-trace argument.
- **Endpoint (TW*)(b):** the same statements hold at Q_0 (Theorem B″).

## 5. Summary: proved / not proved / open

**Proved here** (given the task's inputs (TD_J), (TD_Q), (R1), (R2), and the explicit readings (R3), (T4)):
1. Lemma 0, Lemma 1 (time-preserving general position), Lemma 2 (branching over τ = 0 is harmless).
2. Theorems A″ and B″. R8-5's Theorems A and B hold under the much weaker (U″): every relevant fixed-point component is 1-dimensional.
3. Corollary 1. Case (C) of Prop. D, and every α-fixed locus inside {τ = 0}, are not obstructions to (TW*). A twin jump needs a ≥ 2-dimensional family of α-symmetric curves of 𝒱 at τ ≠ 0 near (J,0).
4. Lemma TG (from Teichmüller uniqueness): the intersection of a totally geodesic sheet with Fix(h) is the sheet, a full Teichmüller disc, or points. Hence Corollary 2: in case (A2), V_0 contains a Teichmüller curve of h-symmetric curves with cusp J, or an h-symmetric sheet.
5. Lemma 3: trichotomy for the boundary trace of a surviving bad locus. In particular, (Lock) of the pair ([x],[αx]) holds on every α-stable transported piece that the trace enters with both vertices constant.
6. Corollary 3: (TW*) holds, hence MS8 holds in the no-crossing case, whenever (U″) or (Lock) holds at every junction and (U″) holds at the endpoint.

**Not proved:** (TW*) itself. I found neither a proof nor a counterexample. No configuration violating (TW*) was constructed: realising (D2) needs an actual smooth totally geodesic V_0 together with a deformation, which is out of reach here.

**Open questions (precise):**
- **(O1″)** Case (D2)/(A2): let V_0 contain a Teichmüller curve 𝒯 of h-symmetric curves with cusp J, where h exchanges two Y_0-copies x, αx of J, and let 𝒯 deform to h-symmetric curves Φ_τ ⊂ V_τ. Does this force (Lock) of the persistent twin pair (c_{m+1}, w) on D^{m+1}, or (IP) at J (|Aut J(τ)| = |Aut J|)? A positive answer would need (L1)–(L2) above.
- **(O2″)** Case (B-pure): can the α-symmetric curves Φ_τ ⊂ V_τ (τ ≠ 0) converge to an α-fixed boundary branch of V_0 without having boundary points near J(τ)? Neither (R1), (R2), (Rig) nor Lemma U seems to exclude this.
- **(O3″)** Case (D3): can a component of closure(𝒞°) be fixed pointwise by α ∉ K, which needs 𝒞° to be reducible over orbifold points of 𝒱?
- **(O4″)** The inputs (TD_J), (TD_Q) and (T4) are inherited from Proposition K "modulo routine marking details" and are not re-proved here. The reading (R3) is adopted.



### round9_q6 (verbatim)
# round9_q6 — the twin step (TW*) via the lifted 3-fold component

**Status.** (TW*) is NOT proved in general. Proved here: planner Steps 1–3, with two repairs, and the analogue at the endpoint (Step 5). Together they reduce (TW*) to a precise coset condition on the stabiliser group Γ. Step 4 (the case where automorphisms in Γ drop) stays open, and I explain where each suggested tool fails. No counterexample is given.

Readings: (R1), (R2) with H_0 = id, (TD_J)/(TD_Q) of R8-5 §1 and §5, and (PT_chain). Notation q : B → B/Aut(J), F_x, L_x, (K1)–(K4), transport families Ñ as in R8-8 §0.

---

## 0. Two repairs to the planner's set-up

**(Rep1) Define 𝒜 by the sheet, not as a component of 𝒱 ∩ (U×Δ_ε).**
- Choose a closed conic (Milnor) neighbourhood U'' ⋐ U of J. Then closure(V_0) ∩ U'' is the union of its local sheets S at J, and V_0 ∩ U'' is the disjoint union of the connected sets S° := S ∖ B_0. This uses that V_0 is smooth and that an irreducible germ minus a proper analytic subset is locally connected.
- The track γ of (TD_J) is a path in V_0 ∩ U''. Take z_1, z_2 close enough to J for this.
- So γ lies in ONE sheet S_0°. This is the "same-sheet property"; it is automatic.
- Put 𝒜 := H((S_0° ∩ U'') × Δ_ε). For ε small, 𝒜 ⊂ 𝒱 ∩ (U×Δ_ε). It is connected, and open in 𝒱.
- Let 𝒞° be the connected component of q^{-1}(𝒜) that contains γ̃ × {0}. There are finitely many components, so after passing to a subsequence ρ_n → 0 it is independent of ρ.
- Put Γ := Stab_{Aut(J)}(𝒞°) and 𝒳 := closure(𝒞°) ⊂ B × Δ_ε.
- As in R8-5 Fact 0, q : 𝒞° → 𝒜 is the quotient by Γ.

Why the repair is needed: a component of 𝒱 ∩ (U×Δ_ε) can contain several sheets at (J_t, t). Step 1 below needs local connectivity at (J_t, t), and the sheet version has it.

**(Rep2) 𝒳 need not be an irreducible germ.**
- The planner calls 𝒳 an irreducible 3-dimensional germ. That is not justified: 𝒞° can be reducible. Example: the preimage of the smooth curve {ab = 0}/swap.
- What is true: 𝒳 is analytic of pure dimension 3. Near any point, q^{-1}(closure 𝒜) is analytic, because closure(𝒜) is locally a union of local irreducible components of closure(𝒱) (Lemma S of R8-1 together with (R2)). Each local irreducible component L′ of q^{-1}(closure 𝒜) has L′ ∖ {∏ s_e = 0} connected, so it lies in one component of q^{-1}(𝒜). Hence 𝒳 is, locally, the union of those L′ whose interior lies in 𝒞°.
- Nothing below needs irreducibility.

**(Rep3) Genericity of z̃_1, z̃_2.**
- Choose z̃_1 ∈ β̃ ∖ 0 such that Stab_{Aut(J)}(z̃_1) equals the pointwise stabiliser of β̃. Only finitely many points of β̃ near 0 fail this, because stabiliser jumps form an analytic subset of the curve.
- Choose z̃_2 on β̃′ in the same way.
- This is part of "generic" in (TD_J).

---

## 1. Lemma 1 (Step 1: one Γ-orbit) — proved

**Lemma 1.** Let y = (H(z,τ), τ) with z ∈ S_0 ∩ U'' and |τ| < ε, and suppose S_0 is locally irreducible at z. (This holds for z = J, since S_0 is irreducible at J by definition.) Then the points of 𝒳 lying over y form a single Γ-orbit. In particular, for every t the lifts of J_t = H_t(J) lying in 𝒳_t form one Γ-orbit.

*Proof.*
1. **𝒜 is locally connected at y.** Let W be a neighbourhood of y.
   - Since H is a homeomorphism, there are a conic neighbourhood W_0 of z (on which S_0° ∩ W_0 is connected, by local irreducibility at z) and a disc D ∋ τ with H(W_0 × D) ⊂ W.
   - H((W_0 ∩ S_0)×D) contains 𝒜 ∩ W′ for a smaller neighbourhood W′ of y, because H is open onto closure(𝒱).
   - So 𝒜 ∩ W′ lies in the connected set H((S_0° ∩ W_0) × D) ⊂ 𝒜 ∩ W.
2. **Set-up near a lift.** Let p ∈ 𝒳 lie over y and put G_p := Stab_{Aut(J)}(p).
   - Take a G_p-invariant neighbourhood N_p of p with αN_p ∩ N_p = ∅ for α ∉ G_p. Then q|N_p is the quotient by G_p, and q(N_p) is a neighbourhood of y.
   - By step 1, choose W′ such that 𝒜 ∩ W′ lies in a single component 𝒦 of 𝒜 ∩ q(N_p).
3. **The components of q^{-1}(𝒦) ∩ N_p are permuted transitively by G_p.** The argument is that of R7-4 Lemma 2(a): q is open and closed on saturated sets, the domain is locally connected, and 𝒦 is connected.
4. **One of them lies in 𝒞°.** Points of 𝒞° arbitrarily close to p map into 𝒜 ∩ W′ ⊂ 𝒦. So some component L of q^{-1}(𝒦) ∩ N_p meets 𝒞°. L is a connected subset of q^{-1}(𝒜), so L ⊂ 𝒞°.
5. **Comparing two lifts.** Let p′ = αp also lie in 𝒳. As in step 4, some component L′ of q^{-1}(𝒦) ∩ αN_p lies in 𝒞°.
   - α^{-1}L′ is a component of q^{-1}(𝒦) ∩ N_p, so α^{-1}L′ = gL with g ∈ G_p.
   - Then α^{-1}𝒞° ∩ g𝒞° ≠ ∅, so α^{-1}𝒞° = g𝒞°, i.e. αg ∈ Γ.
   - Finally αg·p = αp = p′. ∎

## 2. Lemma 2 (Step 2: the transport families lie in 𝒳) — proved

**Lemma 2.** Some irreducible component Ñ^1 of Ñ lies in 𝒳. Likewise some irreducible component Ñ′^1 of Ñ′ lies in 𝒳. For every t:
- closure(Ñ^1_t) contains a lift of J_t, and F_x ≡ φ_{c_m}(t) on closure(Ñ^1_t);
- the same holds for Ñ′^1 with φ_{c_{m+1}}.

*Proof.*
1. **z̃_1 ∈ 𝒳.** γ̃(a) ∈ 𝒞° and |γ̃(a) − z̃_1| < ρ_n → 0 by (T1).
2. **A 3-dimensional local component.** Let L be a local irreducible component of 𝒳 at (z̃_1, 0). It is 3-dimensional and not contained in {∏ s_e = 0} (Rep2).
   - By Krull, L ∩ {∏ s_e = 0} is pure 2-dimensional at (z̃_1, 0).
   - It lies in q^{-1}(closure(𝒜) ∖ 𝒜) ⊂ q^{-1}(H(B_0 × Δ)).
   - Near (z_1, 0), the set H(B_0 × Δ) equals N := H((β ∖ J) × Δ), because z_1 is a smooth point of B_0 on β.
3. **Near z̃_1, the preimage of N is Ñ.** Near (z̃_1, 0), q^{-1}(N) is the union of the translates aÑ with a ∈ Stab(z̃_1). By (Rep3), such an a fixes β̃ pointwise. So aÑ = Ñ, since both are the component of q^{-1}(N) containing β̃ ∖ 0.
4. **Conclusion.** Hence 𝒳 ∩ Ñ is an analytic subset of Ñ containing a 2-dimensional germ at (z̃_1, 0). That germ contains a local irreducible component of Ñ, which lies in a unique global irreducible component Ñ^1. By the identity principle for the irreducible set Ñ^1, Ñ^1 ⊂ 𝒳.
5. **Properties of Ñ^1.**
   - N is a connected topological 4-manifold. A 4-manifold germ minus a set of real dimension ≤ 2 is connected, so N is locally irreducible, and hence irreducible.
   - So q(Ñ^1) = N, by Remmert applied to the finite map q together with dimension.
   - closure(Ñ^1_t) ∋ lift of J_t, by the argument of R7-3 Lemma 2 step 5.
   - F_x ≡ φ_{c_m}(t) on Ñ_t ⊃ Ñ^1_t, by (∗) of R8-8 §0.
6. **Remark.** The same argument at time 0 shows β̃, β̃′ ⊂ closure(C_0), where C_0 is the component of q^{-1}(S_0°) containing γ̃. ∎

## 3. Step 3: the reduction — proved

**Proposition 3.** For every t there are:
- j̃ ∈ closure(Ñ^1_t) ∩ q^{-1}(J_t),
- j̃′ ∈ closure(Ñ′^1_t) ∩ q^{-1}(J_t),
- γ_t ∈ Γ with j̃′ = γ_t j̃,

and then [φ_{c_{m+1}}(t)] = [F_{γ_t^{-1}x}(j̃)], while [φ_{c_m}(t)] = [F_x(j̃)].

*Proof.* By Lemmas 1 and 2, together with (K3). ∎

**Corollary 3′ (new sufficient conditions for no twin jump at J).** Suppose that, for t in a set accumulating in Δ, Γ = Γ_x · Stab_Γ(j̃(t)). Then [φ_{c_{m+1}}] ≡ [φ_{c_m}]. This holds in particular under either of the following.
- **(IP_Γ)** Γ fixes j̃(t), i.e. the automorphisms of J that preserve the track's family component 𝒞° survive on J_t.
- **(NT_Γ)** Γ fixes x.

*Proof.* Choose γ_t ∈ Γ_x. Then F_{γ_t^{-1}x} = F_x. Conclude with Lemma 1 of R8-8. ∎

Comparison with known results:
- (IP_Γ) is strictly weaker than (IP_m), because only Γ ⊂ Aut(J) has to be preserved, not all of Aut(J).
- (NT_Γ) is a special case of (U_J).
- So this is a modest strengthening of R8-8 Corollary 1 and R8-5 Theorem A. It does NOT answer the question.

**Endpoint (Step 5).** Lemmas 1 and 2 hold verbatim at Q_0, applied to Ñ^k_+ and Ñ^E and using the sheet of the (TD_Q)-track. Hence (b) of (TW*) holds at every t at which γ_t can be chosen in Γ_x; Step 2 of Theorem 1 in R8-8 then applies.

## 4. Step 4 (Γ ⊄ Γ_x·Stab(j̃)) — open; what is shown

Assume Y is non-constant, t is generic, and (a) fails at J. By Proposition 3 and R8-8 Proposition 3 we get the following.
- There is γ ∈ Γ (fixed for t in an uncountable set) with γx ≠ x.
- Along β̃′, γx is an intact constant vertex w of D^{m+1} with [φ_w] ≡ [Y]. This is the persistent twin.
- The twin-jumping automorphism is moreover forced to preserve the 3-fold family component 𝒞° of the track. This is new information beyond R8-8 Prop. 3, which only had γ ∈ Aut(J).

Status of the planner's four tools:
1. **Krull/Hurwitz inside 𝒳.** 𝒳 is γ-invariant and contains Ñ^1, Ñ′^1, γÑ^1 and γ^{-1}Ñ′^1. The labels are:
   - along Ñ: x ↦ Y;
   - along Ñ′: x ↦ φ_{c_{m+1}}, γx ↦ Y;
   - along γ^{-1}Ñ′: x ↦ Y.

   This is exactly the R7-3 §5 model with σ = γ ∈ Γ. Every incidence constraint that Krull gives in 𝒳 is satisfied by the model, so it gives no contradiction. (I did not write down an explicit 3-fold realising the model; this point is heuristic, as in R8-5 §6.)
2. **Generic-time trichotomy at every lift.** It is satisfied, because the Y-network continues on the twin γx (R8-4 §5 check).
3. **The same-sheet property.** It holds automatically (Rep1), and Lemma 2's remark puts β̃ and β̃′ in one lifted sheet closure(C_0) at time 0. But γ need not stabilise C_0 (Γ ≠ Γ_0 := Stab(C_0) is possible). Even when it does, the case of R8-5 Prop. D (A)/(B) is not excluded.
4. **Lock via Γ.** Γ permutes lifts and labels, but F_x(γj̃) = F_{γ^{-1}x}(j̃), and nothing forces F_{γ^{-1}x}(j̃) ≅ F_x(j̃) when γ ∉ Stab(j̃).
5. **Lemma U.** It constrains only non-constant vertices; here all vertices involved are constant.

**Open question (sharpened).** For γ ∈ Γ = Stab(𝒞°) with γx ≠ x, can γ ∉ Aut(J_t) for t ≠ 0? Equivalently, can the automorphisms of J that preserve the track's family component drop along H_t(J)?
- If no, then (IP_Γ) holds and (TW*) follows.
- A proof must use total geodesy of V_0, or global data. The 𝒳-picture is chart-plus-family-local and consistent with the twin-jump model.

## Summary
- **Proved:** Steps 1–3 and 5 (with Rep1–Rep3); Corollary 3′ ((IP_Γ) or (NT_Γ) ⇒ no twin jump).
- **Not proved:** (TW*) in general.
- **Open:** Step 4, i.e. the drop of Γ-automorphisms at J_t.


### round9_q2 (verbatim)
# round9_q2: attempt on MS8

**Status line.** PARTIAL. I did **not** prove MS8 and I did **not** find a counterexample.

What this file adds:
- two small proved lemmas that sharpen the twin analysis (Lemmas 1 and 2, plus Corollary 3);
- a twin-free reformulation of what a counterexample must look like at t = 0 (Proposition 4). This is proved from earlier results;
- a precise statement of the residual case.

The open cases are exactly those listed in the task: residual twins (R8-5 §6, R8-8 §4) and residual crossings (R8-1 §4.3, R8-6 §3). Neither is closed here.

Throughout I use readings (R1) and (R2) with H_0 = id, the setting of MS8, and (Rig). I use the notation of the task file: Def(Q), π, s_e, labels, F_x, L_x, transport families Ñ, F_0, (K1)–(K4).

---

## 0. The chain's derivation from MS8

I re-read the section "The missing statement MS8, and how it is used" and found no flaw.
- MS8 assumes everything the problem assumes, plus (Rig). So MS8 together with entry 82 ((Rig) holds for every admissible family) gives the problem's claim.
- The case dim M_{g_i,n_i} = 0 is trivial: M_{g_i,n_i} is then a point.
- Step 1 (identity theorem for t ↦ Y_t) is correct as stated (PR-A).

The real gaps are entry 82 and MS8 itself.

---

## 1. Lemma 1: transport families contain whole lift-curves, so star coherence is all-or-nothing (proved)

**Setting.** Let Q ∈ F_0, i.e. a junction, a puncture point or an isolated stratum point, as in R8-6 §3.1. By R8-6 Lemma 3.1, t ↦ Q_t := H_t(Q) is holomorphic.

Put
 𝒥_Q := {(q,t) ∈ Def(Q) × Δ_ε : π(q) = Q_t}.

Properties of 𝒥_Q:
- It is the preimage of the holomorphic graph {(Q_t, t)} under the finite map π × id, so it is a 1-dimensional analytic set.
- Since π^{-1}(Q) = {0} and π is proper, every lift of Q_t tends to 0 as t → 0. So, after shrinking ε and the ball, 𝒥_Q is the union of its finitely many irreducible germ components λ at (0,0).
- Each component λ is finite over Δ_ε and surjects onto it (open mapping theorem plus properness).
- Aut(Q) permutes the components transitively. Indeed, for t ≠ 0 the fibre of 𝒥_Q over t is one Aut(Q)-orbit (K1). Fix a component λ_0. Every point lies in some component, and a·λ_0 is a component, so the translates of λ_0 cover a full fibre. Since the components are finitely many and each surjects onto Δ_ε, every component is a translate.

**Lemma 1.** Let b be a branch of B_0 at Q, with lift b̃ and transport family Ñ_b. Here b is either a boundary branch at Q or, in the interior case, the germ of the piece through Q. Then for every component λ of 𝒥_Q there is a ∈ Aut(Q) with λ ⊂ closure(a Ñ_b).

*Proof.*
1. Take (q,t) ∈ λ with t ≠ 0. By R7-4 Lemma 2(b) (interior case identical), some translate aÑ_b has q in the closure of its t-slice.
2. Hence λ ∖ {(0,0)} ⊂ ⋃_{a ∈ Aut(Q)} closure(aÑ_b).
3. Each closure(aÑ_b) is analytic (R7-4 Lemma 2(c)). So λ is a finite union of the analytic subsets λ ∩ closure(aÑ_b).
4. λ is irreducible, so one of these subsets is all of λ. ∎

**Corollary 1′ (star coherence is all-or-nothing).** Let Ñ, Ñ′ be two transport families at Q. Then exactly one of the following holds.
- There is a component λ of 𝒥_Q with λ ⊂ closure(Ñ) ∩ closure(Ñ′). Then, for **every** small t, closure(Ñ)_t and closure(Ñ′)_t contain a common lift of Q_t.
- closure(Ñ) ∩ closure(Ñ′) ∩ 𝒥_Q = {(0,0)} near (0,0). Then for no small t ≠ 0 do they share a lift of Q_t.

In particular the set T_m in R8-8's (SC_m) is either a punctured neighbourhood of 0 or empty near 0. So "(SC_m) on a set accumulating at 0" is equivalent to (SC_m) for all small t.

*Proof.* closure(Ñ) ∩ closure(Ñ′) ∩ 𝒥_Q is an analytic subset of the 1-dimensional germ 𝒥_Q at (0,0). So it is either a union of components of 𝒥_Q or the single point (0,0). ∎

(Slice remark. By continuity of F_x on the closed set L_x, the identity (∗) of R8-8 §0, namely F_x ≡ φ_c(t), holds on closure(Ñ) ∩ {time t}, which contains closure(Ñ_t). So nothing changes if one uses slices of closures instead of closures of slices.)

---

## 2. Lemma 2: the two families at a junction lie in the track's 3-fold (proved, given (TD_J))

Use the setting of R8-5 §1, (C2) and (C3):
- J is a junction, with lifted branches β̃ (of D) and β̃′ (of D′) at 0 ∈ Def(J);
- the track lift γ̃ ⊂ B°;
- 𝒞° is the connected component of π^{-1}(𝒱_U) containing γ̃ × {0}.

**Lemma 2.** Assume, as (TD_J) provides for a sequence ρ → 0, that the track runs from within ρ of a generic point z̃_1 ∈ β̃ to within ρ of a generic point z̃_2 ∈ β̃′, inside 𝒞°_0. Then the transport families Ñ (of β̃) and Ñ′ (of β̃′) are contained in closure(𝒞°).

*Proof (for Ñ; Ñ′ is the same).*
1. **Choice of a point.** Pick a generic coarse point p ∈ β ∖ {J} with lift p̃ ∈ β̃. Take p̃ close enough to z̃_1 that track points γ̃(s) come arbitrarily close to it as ρ → 0. Put S := Stab_{Aut(J)}(p̃). On a small S-invariant ball V around p̃, π restricted to V is the quotient by S.
2. **A sheet of 𝒞°_0 at p̃.** V_0 is smooth, so near p the sheets of closure(V_0) are the closures of the components of V_0 ∩ π(V) (R8-1 Lemma S). The track points near p̃ lie in 𝒞°_0. A subsequence of them lies in one lifted local sheet σ at p̃, with σ° ⊂ 𝒞°_0. The sheet σ contains β̃ near p̃: boundary points of σ near p̃ lie on lifted branches of B_0 through p̃, and for generic p the only such branch is β̃.
3. **Transporting the sheet.** Let Σ be the connected component of π^{-1}(H(π(σ°) × Δ_ε)) ∩ (V × Δ_ε) that contains σ° × {0}.
   - Σ is connected and contains points of 𝒞°, so Σ ⊂ 𝒞°.
   - π is proper and H commutes with closures. So π(closure Σ) contains the full saturated image, which is H(π(σ) × Δ_ε) ⊇ H((β ∩ π(V)) × Δ_ε) =: N_p.
4. **closure(Σ) contains a 2-dimensional piece of Ñ.** The set closure(Σ) ∩ π^{-1}(N_p) is analytic and maps onto the topological 4-manifold N_p.
   - So it contains a 2-dimensional local component of π^{-1}(N_p) at (p̃, 0).
   - Every such local component meets {t = 0} inside π^{-1}(β) ∩ V. For generic p this set is β̃ ∩ V, since the lifted curve is smooth at p̃. So the component contains β̃ ∖ {0} near p̃, and therefore lies in Ñ (by the definition of Ñ as a connected component).
5. **Conclusion.** Ñ is irreducible (R7-3 Lemma 2, step 2). It shares a 2-dimensional open subset with the analytic set closure(𝒞°), hence Ñ ⊂ closure(𝒞°). ∎

**Combined with Lemma 1.** Let λ ⊂ closure(Ñ) and λ′ ⊂ closure(Ñ′) be components of 𝒥_J. Both lie in closure(𝒞°), and λ′ = aλ for some a ∈ Aut(J). A twin jump (failure of (SC)) therefore means:

> The irreducible 3-fold closure(𝒞°) contains two distinct lift-curves λ ≠ λ′ of J_t. The sheet of 𝒞° that carries the track at t = 0 splits, for t ≠ 0, into local sheets at the distinct points λ(t) and λ′(t), and these collide at 0.

At t = 0 both β̃ and β̃′ lie in the single sheet. This is the "star" picture of R8-8 §6, now with the extra information that only one 3-fold component is involved.

---

## 3. Corollary 3 (a refinement of R8-5's (U_J))

In the situation of Lemma 2, suppose closure(𝒞°) ∩ 𝒥_J is a single component λ of 𝒥_J. Then (SC) holds at J for all small t. Hence there is no twin jump at J, and φ_c ≡ φ_{c′} for the tracked constant vertices of D and D′.

*Proof.*
1. By Lemma 1, closure(Ñ) and closure(Ñ′) each contain a component of 𝒥_J.
2. By Lemma 2, each such component lies in closure(𝒞°) ∩ 𝒥_J = λ. So both contain λ.
3. Apply R8-8 Theorem 1, Step 1 (case (SC)) together with Corollary 1′. ∎

The hypothesis of Corollary 3 depends only on the family germ at (J,0). It is implied by:
- "Stab_{Aut(J)}(𝒞°) fixes λ" together with "the components of 𝒥_J lying in closure(𝒞°) form one Γ-orbit". This holds, for instance, when Γ acts trivially on the set of components of 𝒥_J.

I could not verify this hypothesis in general, so Corollary 3 is only another sufficient condition, in the same family as (U_J), (SC) and (IP).

---

## 4. Proposition 4: twin-free t = 0 structure forced by a counterexample (proved from R8-3 and R8-6)

**Definition (star of a lift-curve).** For Q ∈ F_0 and a component λ of 𝒥_Q, put
 Star(λ) := { a·b̃ : b a branch of B_0 at Q, a ∈ Aut(Q), λ ⊂ closure(aÑ_b) }.
By Lemma 1, Star(λ) contains a lift of every coarse branch b at Q.

**Proposition 4.** Assume MS8's hypotheses, that Y is non-constant, and alternative (a) of R8-2 Proposition 7 (IMOV events only at a countable set of times; by R8-6 Corollary 3 this holds unless V_0 has a persistent residual crossing). Let B_0^∂ be the connected component of B_0 containing ∂V_0. Let Q ∈ F_0 ∩ B_0^∂ and let λ be a component of 𝒥_Q. Then:
1. **(i)** some label y has F_y(q) ≅ Y_t for all (q,t) ∈ λ;
2. **(ii)** every label y with property (i) is intact along every a·b̃ ∈ Star(λ). Moreover F_y ≡ Y_t on (aÑ_b)_t for all t, so F_y ≡ Y_0 along a·b̃ at t = 0.

*Proof.*
1. **Generic times.** Let 𝔗 be the complement in Δ_ε of the countable union of three sets:
   - the generic-time exceptional set Z of R8-3 §3;
   - the IMOV times;
   - the countable sets of R7-3 Lemma 1(b) for the finitely many relevant pieces.

   For t ∈ 𝔗, R8-3 Corollary N1 applies: every point of B_t^∂ = H_t(B_0^∂) has a Y_t-copy, and every Y_t-copy is intact and constant along every branch of B_t through the lift that carries it.
2. **Proof of (i).** Let n: λ^ν → λ be the normalization, with parameter σ.
   - For t(σ) ∈ 𝔗, the lift n(σ) of Q_t carries a Y_t-copy at some label.
   - There are finitely many labels, and 𝔗 is uncountable. So one label y works for uncountably many σ.
   - The set {σ : F_y(n(σ)) ≅ Y_{t(σ)}} is analytic in the connected curve λ^ν: compare in the coarse space; F_y is holomorphic on the stratum locus ⊇ λ. Since it is uncountable, it is everything.
3. **Proof of (ii): the label is intact.** Fix a·b̃ ∈ Star(λ) and t ∈ 𝔗. Pick (q,t) ∈ λ with q ∈ closure((aÑ_b)_t). Near q, (aÑ_b)_t is a union of lifted branches of H_t(b) ending at q.
   - By step 1, y is intact along such a branch.
   - The pattern is constant on aÑ_b (R7-4 Lemma 2(a)), so y is intact on all of aÑ_b, in particular along a·b̃.
4. **Proof of (ii): the value is Y.** The set A := {p ∈ aÑ_b : F_y(p) ≅ Y_{t(p)}} is analytic in the irreducible 2-dimensional set aÑ_b (R7-3 Lemma 2).
   - By step 1, A contains a 1-dimensional subset of the t-slice for every t ∈ 𝔗, which is uncountable.
   - A proper analytic subset has dimension ≤ 1 and countably many components, so it contains only countably many such slice curves. Hence A = aÑ_b.
   - At t = 0, F_y ≡ Y_0 along a·b̃ by continuity. ∎

**Consequences.**
- (a) **The twin problem, stated without tracking.** Let Q_0 be Prop K's end point, x the tracked label, β̃^k_+ the arriving branch, and assume φ_{c_k} ≡ Y. Let λ_+ ⊂ closure(Ñ^k_+) be a lift-curve (Lemma 1).
  - By (∗), x has property (i) for λ_+. So by (ii), x is intact and constant along every branch of Star(λ_+).
  - In the MERGE and pMOV cases x is not intact-constant along β̃^E. So **β̃^E ∉ Star(λ_+)**, at every small t (Corollary 1′).
  - Star(λ_+) does contain some a·β̃^E with a ∉ Stab(β̃^E) and a^{-1}x ≠ x, along which x is intact and constant.

  This is R8-8 Proposition 3 (endpoint), but now without "generic t" quantifiers and with the junction case handled identically. The same holds at each junction.
- (b) **Exactly what MS8 still needs.** Under the hypotheses of Proposition 4, MS8 follows from either of the following t = 0 statements.
  - **(Star-K)** For Prop K's track, at the end point and at each junction, the leaving branch lies in Star(λ) of a lift-curve λ contained in the closure of the arriving family. This is (SC), via Corollary 1′.
  - **(Star-free)** There are Q ∈ F_0 ∩ B_0^∂ and a coarse branch b at Q such that, for every component λ of 𝒥_Q and every label y with F_y(0) ≅ Y_0, y is merged or moving along the lift of b in Star(λ).

  The proof is immediate from Proposition 4(ii).

  But Star(λ) is defined through the family at t ≠ 0. It is **not** determined by t = 0 data: see §5.

---

## 5. Why t = 0 data alone cannot decide Star(λ) (analysis; heuristic, not a theorem)

In the situation of Lemma 2, let a ∈ Aut(J) preserve the t = 0 sheet X ⊃ β̃, β̃′.
- At t = 0 the three branches β̃, β̃′ and aβ̃′ all lie in X.
- Along β̃′ and along aβ̃′ the relevant labels are constant with value ≅ Y_0 at t = 0.
- Every t = 0 invariant (the germ of closure(V_0), its Teichmüller discs, Prop K's ray dynamics) is a-equivariant.

Which of β̃′ and aβ̃′ lies in Star(λ_+) is decided only by the deformation, i.e. by which lift-curve of J_t the transported family closure(Ñ′) contains. Two things can happen:
- Prop K's track can choose β̃′ while the deformation puts aβ̃′ in the star.
- The a-image of the whole t = 0 picture, track included, is another legitimate track. It is genuine exactly where the original was not.

So a proof of (Star-K) cannot be "local at t = 0 within one sheet". It needs either a global argument, or time-t information beyond Krull at one lift (which R8-3 Corollary T uses, and which settles the quintic test case). This matches R8-8 §6 (scale conflict) and R8-5 §6 (cases (A), (B), (C)). I have no construction of an actual family realizing such a split, so this is not a counterexample.

---

## 6. Summary: proved / not proved / open

**Proved here** (modulo the cited prior results, which I re-read but did not re-derive):
- Lemma 1: every transport family contains a whole lift-curve of Q_t.
- Corollary 1′: star coherence (SC) is all-or-nothing in t.
- Lemma 2: at a junction, both transported branch families lie in the closure of the single 3-fold component 𝒞° that carries Prop K's track.
- Corollary 3: no twin jump when closure(𝒞°) ∩ 𝒥_J is a single lift-curve.
- Proposition 4: the twin-free t = 0 structure forced by a counterexample (under Proposition 7(a)), and its consequences (a) and (b).
- §0: the chain's derivation from MS8 is correct.

**Not proved:** MS8.

**Open** (unchanged in substance, sharpened in form):
1. **Twins.** Prove (Star-K), or (Star-free), or the hypothesis of Corollary 3, for smooth closed totally geodesic V_0. Equivalently, exclude a 3-fold component closure(𝒞°) containing two distinct lift-curves λ ≠ λ′ of a junction or end point, with the arriving family through λ and the leaving family through λ′ only.
2. **Crossings.** Exclude persistent residual crossings (R8-6 (PC)): the two-sheet and non-Q-Cartier crossings of R8-1 §4.3, and the shared crossings with equal projected curves. Without this, Proposition 4 is not available, and R8-2 Proposition 7(b) (Y(Δ) inside a fixed curve pr_y(K_W)) is not excluded.
3. Entry 82 ((Rig) for every admissible family), which is outside MS8.

No counterexample to MS8 is known. Every local model of a twin split or a crossing that I or earlier rounds examined is consistent with (R1), (R2), (i), (ii) and (Rig), but none has been realized globally.


### round9_q1 (verbatim)
# round9_q1 — attempt on MS8

**Status: MS8 is NOT proved in full. This is a PARTIAL result. It contains no counterexample.**

What is new here, and proved (given the cited prior results, whose steps I re-checked as I used them):
- **Theorem 1 (copy-free dichotomy).** If t ↦ Y_t is non-constant, then one of two things happens:
  - (I) a crossing (IMOV) event lies on the persistent network at every generic time near 0;
  - (II) a "sealed" configuration exists, made of conditions that can be checked at t = 0 only: (II-a) and (Seal_Q).
- **Corollary 2 (release criterion).** MS8 holds, unless case (I) occurs, whenever some point of the connected component of B_0 through ∂V_0 has no component isomorphic to Y_0.
- **Corollary 3 (seal criterion).** MS8 holds, unless case (I) occurs, whenever (Seal_Q) fails at some point Q of that component. R8-3 Corollary T and R8-4 Theorem 2V are special cases of Corollary 3.
- So the twin obstruction becomes a statement about V_0 alone: "(Seal) holds everywhere on B_0^∂". That statement does not refer to the deformation.

Still open:
- the crossing case (I);
- the sealed case (II), i.e. excluding (Seal_Q) at every point of B_0^∂.

§5 records a dead end. The natural strengthening of Proposition K ("total release") is false in the quintic test case.

---

## 0. Setting, notation, and the prior results used

The setting is MS8 exactly as in the task, in readings (R1) and (R2):
- H is the stratified homeomorphism, with H_0 = id.
- V_0 is smooth, closed, 2-dimensional and totally geodesic.
- Δ_Γ is of product type, ∂V_t has dimension 1, and π_i(∂V_t) = {Y_t}.
- (Rig) holds.

Notation:
- B_t := closure(V_t) \ V_t. By (R2), H_t : B_0 → B_t is a homeomorphism preserving strata.
- B_0^∂ is the connected component of B_0 that contains ∂V_0. Put B_t^∂ := H_t(B_0^∂); this is the connected component of B_t containing ∂V_t.
- N_t := {Q ∈ B_t : Q has a Y_t-copy}.
- For Q ∈ B_0, the chart is Def(Q), with Aut(Q) acting and quotient map π.
  - Labels are the vertices of G_Q.
  - F_z is the z-component on L_z = {s_e = 0 for all e at z}.
  - A lifted branch c̃ has a constant pattern S_c̃.
  - A label z is *intact* along c̃ if every edge at z lies in S_c̃.

Prior results used. I re-checked each step that I use.
- **(TN) = R8-3 Theorem N, and R8-3 Lemma 2.**
  - Lemma 2 says each coarse piece D satisfies exactly one of (N) and (F):
    - (N): for every t, every point of H_t(closure D) has a Y_t-copy;
    - (F): for t outside a countable set Z_D, only finitely many points of H_t(closure D) have a Y_t-copy.
  - Put 𝒩 := {D : (N) holds} and C_t := ⋃_{D∈𝒩} H_t(closure D) = H_t(C_0). Then closure(∂V_t) ⊂ C_t.
  - Assume Y is non-constant. Then there is a countable set Z ⊂ Δ such that, for t ∉ Z ("generic"), the following holds. Let Q ∈ B_t, let q be a lift of Q, let y be a label with F_y(q) ≅ Y_t, and let c̃ be any lifted branch of B_t through q. Then y is intact along c̃, and exactly one of the following holds:
    - **STAY**: F_y ≡ Y_t along c̃, and the coarse piece of c̃ lies in 𝒩;
    - **IMOV**: Q lies in the stratum of the piece of c̃, and F_y is non-constant along c̃.
  - *Re-check.*
    - A merge, or a non-constant intact y at a puncture, would make [Y_t] a component class of a puncture value of a non-constant vertex. By (Rig) that class lies in a fixed finite set F′, which is excluded for generic t.
    - If y is intact and constant along c̃, infinitely many points of the piece D′ have a Y_t-copy. For t ∉ Z_{D′}, Lemma 2 then forces D′ ∈ 𝒩.
- **(Fam) = R7-4 Lemma 2 / R7-3 Lemma 2 (transport families).** Let b be a branch of B_0 at Q with lift b̃.
  - Let Ñ be the component of π^{-1}(H((b∖Q) × Δ_ε)) containing b̃ ∖ 0.
  - Every lifted branch of H_t(b) through a lift q of Q_t (t small) lies in (aÑ)_t for some a ∈ Aut(Q).
  - The pattern, and the partition of labels into vertices, are constant on aÑ, and the t = 0 slice of aÑ is a b̃ ∖ 0.
- **(LU) = Lemma U of R8-2 and its corollary U1.** A vertex is constant on one component of one fibre of a 2-dimensional family W iff it is constant on all of them.
  - The time-t and time-0 pieces of a family aÑ lie in one such W. Π_S(Ñ) is a connected topological 4-manifold, so its regular part lies in a single irreducible component, as in R8-3 Lemma 2, step 3.
  - Hence a label {z} is constant along (aÑ)_t iff it is constant along a b̃.
- **(Sh) = R8-1 Lemma S.** Sheets (irreducible components of the germ of closure(V_t) at a point) are transported by H_t, compatibly with the boundary branches they contain.
- **Krull (cited, standard).** Let X be an irreducible 2-dimensional germ and h a holomorphic function with h ≢ 0 on X and h(x) = 0. Then X ∩ {h = 0} has pure dimension 1 at x.
- **Closedness = R7-1 Lemma 2** (equivalently, the analytic set 𝓝 of R8-3 Lemma 1). If t_n → t, Q_n ∈ B_{t_n} has a Y_{t_n}-copy and Q_n → Q, then Q has a Y_t-copy.

---

## 1. Lemma 1 (sheet Krull at one lift) — proved

**Lemma 1.** Fix t. Let Q ∈ B_0, let q ∈ Def(Q) be a lift of Q_t := H_t(Q) (t small enough that Q_t lies in the chart), and let Σ_t be a sheet of closure(V_t) at Q_t. Then:
- (a) the preimage of the germ Σ_t at q is a non-empty union of irreducible 2-dimensional germs X^1, …, X^r, and **each X^k maps onto Σ_t**;
- (b) for every boundary branch b of Σ_t at Q_t, each X^k contains a lifted branch of b through q;
- (c) for every edge f ∈ E(G_Q), each X^k contains a lifted branch through q whose pattern contains f;
- (d) every 1-dimensional germ of X^k ∩ {∏ s_e = 0} at q is a lifted branch through q of a boundary branch of Σ_t.

*Proof.*
1. **(a).** Near q, π is the quotient by Stab(q), a finite map, and π(q) = Q_t ∈ Σ_t. So the preimage germ is non-empty and of pure dimension 2.
   - The image of an irreducible component X^k is an irreducible analytic germ of dimension 2 (Remmert), contained in the irreducible 2-dimensional germ Σ_t. So it equals Σ_t.
2. **(b).** b ⊂ Σ_t = π(X^k). So π^{-1}(b) ∩ X^k is a 1-dimensional germ at q that maps onto b. Its components are lifted branches of b through q.
3. **(d).** Near q, π^{-1}(B_t) is the union of the lifted branches through q of the branches of B_t at Q_t. A 1-dimensional germ of X^k inside it is one of these lifted branches, and its image lies in Σ_t ∩ B_t. So it lifts a boundary branch of Σ_t.
4. **(c).** By (a), X^k maps onto Σ_t, whose generic points lie in V_t ⊂ M_g. So s_f ≢ 0 on X^k, while s_f(q) = 0 because q lies over the stratum of Q.
   - By Krull, X^k ∩ {s_f = 0} is pure 1-dimensional at q, and it lies in {∏ s_e = 0}.
   - By (d) it consists of lifted branches through q, and s_f ≡ 0 on each of them. ∎

---

## 2. Theorem 1 (copy-free dichotomy) — proved

Assume Y is non-constant, and let Z be the countable set of (TN). Let I be the set of t ∈ Δ ∖ Z at which some point Q ∈ C_t, some lift q, some Y_t-copy y at q and some lifted branch through q are in the IMOV case.

**Theorem 1.** One of the following holds.
- **(I) Crossings near 0.** There is r > 0 such that every t ∈ Δ_r ∖ (Z ∪ {0}) lies in I. In particular, IMOV events on the persistent network C_t occur at uncountably many times accumulating at 0. R8-6 Propositions 1 and 2 then apply: these events are pure crossings (P), shared crossings (S) or same-branch twins (T), with the persistence conclusions (Pers 1)–(Pers 3) stated there.
- **(II) Sealed configuration.** All of the following hold.
  - **(II-a)** Every point of B_0^∂ has a Y_0-copy, and every coarse piece contained in B_0^∂ belongs to 𝒩. So it carries a constant vertex whose value function is ≡ Y.
  - **(II-b) (Seal_Q) holds at every Q ∈ B_0^∂.** (Seal_Q) means that there are a non-empty set Π of labels of G_Q and, for every sheet Σ of closure(V_0) at Q, a set 𝒫_Σ of lifted branches at 0 ∈ Def(Q), with the following properties:
    1. 𝒫_Σ contains at least one lift of every boundary branch of Σ at Q, and every member of 𝒫_Σ lifts a boundary branch of Σ;
    2. ⋃_{c̃∈𝒫_Σ} S_c̃ = E(G_Q) (every edge is pinched along some member);
    3. every z ∈ Π satisfies F_z(0) ≅ Y_0. Moreover, along every member c̃ of 𝒫 := ⋃_Σ 𝒫_Σ, the label z is intact and {z} is a constant vertex of the piece of c̃;
    4. if Q ∈ closure(∂V_0), then for every member c̃ ∈ 𝒫 that lifts a branch of ∂V_0, the label carrying vertex i along c̃ belongs to Π.

*Proof.*
**Step 0 (the dichotomy).** If (I) fails, there are t_n ∈ Δ ∖ (Z ∪ I ∪ {0}) with t_n → 0. Fix such t = t_n.
- *Claim:* C_t ⊇ B_t^∂, and at every lift q of every point of B_t^∂, every Y_t-copy is in the STAY case along every lifted branch through q.
- This is R8-3 Corollary N1. I re-check it:
  - at Q ∈ C_t, every branch is STAY by (TN), because t ∉ I, so it lies in C_t;
  - hence C_t is open in B_t; it is also closed, being a finite union of compact sets;
  - it contains ∂V_t, so it contains the connected component B_t^∂;
  - the second part is (TN) again.

**Step 1 (II-a).**
- C_t = H_t(C_0) ⊇ H_t(B_0^∂), so C_0 ⊇ B_0^∂.
- A coarse piece D ⊂ B_0^∂ is irreducible and lies in the finite union of the closures of 𝒩-pieces. So D ⊂ closure(D′) for one D′ ∈ 𝒩. This forces D = D′: the closure of a piece of a different stratum meets the stratum of D in a finite set.
- Every point of C_{t_n} has a Y_{t_n}-copy. Let Q ∈ B_0^∂. Then H_{t_n}(Q) → Q has Y_{t_n}-copies, and Closedness gives a Y_0-copy at Q.

**Step 2 (II-b).** Fix Q ∈ B_0^∂. For n large, Q_n := H_{t_n}(Q) lies in the chart Def(Q). Pick a lift q_n of Q_n.
- Let Π_n be the set of labels z with F_z(q_n) ≅ Y_{t_n}. It is non-empty, since Q_n ∈ B_{t_n}^∂ ⊂ C_{t_n}.
- For each sheet Σ of closure(V_0) at Q, let Σ_n be its transport at Q_n (by (Sh)). Choose an irreducible component X_n of the preimage of Σ_n at q_n (Lemma 1(a)).
- By Lemma 1(b), (c), (d), the lifted branches of B_{t_n} through q_n that lie in X_n include at least one lift of every boundary branch of Σ_n. Their patterns cover E(G_Q).
- By (Fam), each such lifted branch lies in a family aÑ_b, where b is the corresponding branch of Σ at Q (sheets and branches are transported together by (Sh) and PR-B). Record the t = 0 slices a b̃. The patterns are the same.
- There are finitely many labels, families and sheets. So, after passing to a subsequence, Π_n = Π and the sets of recorded families are independent of n. Let 𝒫_Σ be the set of their t = 0 slices.

Now check the four conditions.
- **Condition 1** holds by Lemma 1(b), (d).
- **Condition 2** holds by Lemma 1(c).
- **Condition 3.**
  - For z ∈ Π, F_z(q_n) ≅ Y_{t_n} → Y_0. Since q_n → 0 and F_z is continuous on the closed set L_z (all lifts lie over the stratum of Q), F_z(0) ≅ Y_0.
  - By Step 0 every z ∈ Π is STAY along every recorded lifted branch through q_n. So z is intact there, and {z} is constant on the time-t_n piece.
  - The pattern is constant on the family (Fam), and constancy transfers to t = 0 by (LU). So z is intact along the t = 0 slice, and {z} is constant on its piece.
- **Condition 4.**
  - Suppose c̃ ∈ 𝒫 is the slice of a family aÑ_b with b a branch of ∂V_0. Then the time-t_n lifted branch through q_n lifts a branch of ∂V_{t_n}.
  - Along it, vertex i is a single label j with F_j ≡ Y_{t_n} (PR-I Lemma D(1)). By continuity at q_n, F_j(q_n) ≅ Y_{t_n}, so j ∈ Π.
  - The label carrying vertex i is constant along the family, so it is j at t = 0 as well. ∎

**Remarks.**
1. No automorphism, marking or track enters Theorem 1. Twins are handled automatically: Π is the set of all Y_t-copies at one lift, and Krull is applied at that same lift (this is the idea of R8-3 Corollary T, carried out in every sheet).
2. Theorem 1 does not use total geodesy. Total geodesy is needed only to rule out (I) and (II) for the given V_0.

---

## 3. Corollaries — proved

**Corollary 2 (release criterion; t = 0 only).** Suppose some point of B_0^∂ has no component isomorphic to Y_0 (with its special points, in some order). Then either Y_t = Y_0 for all t, or (I) holds.

*Proof.* (II-a) fails, so if Y is non-constant, Theorem 1 gives (I). ∎

Equivalently, the hypothesis says that some coarse piece of B_0^∂ has no constant vertex of class [Y_0], or that some isolated stratum point of B_0^∂ has no Y_0-copy. It is a condition on V_0 alone. Under it, **twins play no role at all**: the only remaining obstruction is a crossing.

**Corollary 3 (seal criterion; t = 0 only).** Suppose that for some Q ∈ B_0^∂ no data (Π, (𝒫_Σ)_Σ) satisfy (Seal_Q). Then either Y_t = Y_0 for all t, or (I) holds. ∎

**Corollary 3 recovers the earlier twin criteria.**
- **R8-3 Corollary T.** Hypotheses: (Tw1) all branches at J ∈ closure(∂V_0) ∖ ∂V_0 lie in ∂V_0; (Mg) for S ≠ S′ in 𝒞, some edge at j(S) is not in S′.
  - Suppose (Seal_J) held. Every member of 𝒫 has pattern in 𝒞 (Lemma D(1)), and each pattern is ≠ E(G′).
  - By Condition 2 for a sheet Σ, 𝒫_Σ contains two members with patterns S ≠ S′.
  - By Condition 4, j(S) ∈ Π. By Condition 3, j(S) is intact for S′. This contradicts (Mg).
  - In particular, Corollary 3 covers the quintic test case of PR-I.
- **R8-4 Theorem 2V.** Hypotheses (Tw1), (C1), (C2).
  - Suppose (Seal_{P_0}) held, and take S ∈ 𝒫 (pattern). Then j(S) ∈ Π.
  - By Condition 3, any z ∈ Π is intact and constant along the member with pattern S. By (C1), the only constant vertex there is i. So Π = {j(S)}.
  - By (C2) choose e ∉ S lying in no S′ ∈ 𝒞_{j(S)}. By Condition 2, e ∈ S″ for a member with pattern S″ ∈ 𝒞, and j(S″) ∈ Π = {j(S)}. So S″ ∈ 𝒞_{j(S)} and contains e, a contradiction.

So Theorem 1 contains both earlier twin criteria, with neither (Tw1) nor (C1)/(C2) imposed globally. They become one point-wise t = 0 test.

---

## 4. What remains (precise)

MS8 follows from the following two statements, both open.
- **(X) No persistent crossing.** Case (I) is impossible. By R8-6 Proposition 2, this reduces to excluding the t = 0 configurations (Pers 1)–(Pers 3) and the persistent same-branch twin coincidence of R8-6 §3.3. Theorem X of R8-1 excludes those that lie inside one Q-factorial sheet. Open: two-sheet crossings, and crossings in non-Q-factorial sheets.
- **(MS9) Unsealability.** For every smooth closed totally geodesic V_0 satisfying the problem's hypotheses, at least one of the following holds:
  - some point of B_0^∂ has no Y_0-copy;
  - some coarse piece of B_0^∂ has no constant vertex of class [Y_0];
  - (Seal_Q) fails at some Q ∈ B_0^∂.

  Note that (II-a) also requires the constant vertices to be persistent (value function ≡ Y). That requirement cannot be tested at t = 0, so MS9 is a sufficient condition and is stronger than needed.

**How Proposition K relates to (MS9) (analysis; not a proof).**
- In case (II), the chain of Proposition K lies in B_0^∂, because K_0 ⊂ B_0 is connected and contains P.
- At its MERGE or pMOV endpoint Q_0, let Σ be the ray's sheet. Condition 1 provides a member σβ̃^E ∈ 𝒫_Σ along which all of Π stays. Since x merges or moves along β̃^E, σ^{-1}Π ∌ x.
- So the copy that Proposition K tracks is never in the pulled-back persistent set at the endpoint: a "frozen twin". This is consistent with R8-4 Corollary G1 and R8-8 Proposition 3, but it is not a contradiction.
- A contradiction would follow if the ray's lifted sheet at t = 0 contained only members of a single 𝒫_Σ ("unsplit sheet"). This is (SC) of R8-8 in sheet form. It fails exactly in the "star splitting" picture of R8-8 §6.

---

## 5. Dead end: "total release" (Proposition K for all copies at once) is false

Natural idea: stop Proposition K's rays at the first time at which **no** subsurface is Y_0-like, instead of following one marked copy.
- If that stopping time T_n were finite, the endpoint Q_0 would have a branch along which no point has a Y_0-copy. Corollary 2's mechanism, or its proof at Q_0, would then finish without twins.
- **This conclusion is false in general.** In the quintic test case (PR-I; totally geodesic but not smooth), closure(V_0) ∖ V_0 = ∂V_0 ⊔ {P_0}. Every point of ∂V_0 has the Y_0-copy at vertex i, and P_0 has the twins A ≅ C ≅ Y_0. So B_0^∂ ⊂ N_0: no point of B_0 releases every copy.
  - There MS8 holds through Condition 2 of (Seal) (Krull at one lift), not through total release.
- **Where the proof attempt breaks.** For a fixed ray, the all-copies stopping time can be infinite. A lower-level component (Y, η) whose own differential is Strebel (all horizontal leaves closed and peripheral) is fixed, up to scale, by g_s. Also, new Y_0-like subsurfaces can be split off at junctions while older ones are released.

So no t = 0 argument based only on "some point releases every copy" can work. Case (II) needs Krull at one lift (Condition 2), combined with total geodesy, and that combination is MS9.

---

## 6. Summary

**Proved:**
- Lemma 1: at one lift q, every lifted sheet germ covers its coarse sheet, contains lifts of all of that sheet's boundary branches, and its boundary patterns cover all edges.
- Theorem 1: if Y is non-constant, then (I) crossings occur near 0, or (II) holds, i.e. (II-a) together with (Seal_Q) at every point of B_0^∂.
- Corollary 2 (release criterion) and Corollary 3 (seal criterion), both checkable at t = 0.
- R8-3 Corollary T and R8-4 Theorem 2V are special cases of Corollary 3.
- "Total release" is false in general (quintic test case).

**Not proved / open:**
- (X): exclusion of persistent crossings (pure, shared, same-branch twin) for smooth totally geodesic V_0.
- (MS9): unsealability of B_0^∂ for smooth totally geodesic V_0.
- MS8 itself, in full generality.
- The inherited inputs are not re-proved: (Rig) (entry 82), Proposition K with its "routine marking details" (used only in §4's analysis, not in Theorem 1), and Lemma PA / Theorem TV.

**Chain check.** I found no flaw in the derivation of the problem's claim from MS8 together with entry 82 (chain steps 1–4). Theorem 1 and Corollaries 2–3 use only (R1), (R2), (Rig) and the cited prior lemmas.


### round9_q8 (verbatim)
kind: attempt (round9_q8)

## Status line
Plan: (1) record two short lemmas that hold in configuration (PT): the partner of the twin on the incoming side, and the frozen terminal function; (2) push Option 1 (several mechanisms, each tested); (3) Option 2 (what a realisation needs).
Outcome: **(PT) is neither excluded nor realised.** MS8 stays OPEN. What is proved is structural information that every realisation of (PT) must have (§§1–2). §3 records why each Option-1 mechanism I tried does not close the gap, and §4 does the same for Option 2.

Throughout, the readings (R1), (R2) with H_0 = id, the hypotheses of MS8 including (Rig), the input (K′) of R8-8, and (PT_chain) are assumed as in the task file. Notation is as in R8-8: Ñ^m_+, Ñ^{m+1}_−, Ñ^E are the transport families, (∗) is the identity F_x ≡ φ_c(t) on closure(Ñ_t), (K3) is F_x(σq) ≅ F_{σ^{-1}x}(q), A is the finite class set of R8-8 Lemma 2, and "generic t" is as in R8-8 §4 (t ∉ Z = Z_A ∪ Z_φ ∪ D_all). [·] denotes the class in M_{g_i,n_i}/S_{n_i}.

## 1. Proved: the twin partner on the incoming side (Lemma 1)

**Setting.** We are in case (i) of (PT), i.e. R8-8 Proposition 3, junction case (b). So [φ_{c_m}] ≡ [Y] and [φ_{c_{m+1}}] ≢ [Y]. Fix a generic t and a point j̃ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}). Pick a ∈ Aut(J_m) with j̃ ∈ closure((aÑ^{m+1}_−)_t), as in the proof of Proposition 3.

**Lemma 1.**
- (a) F_{x_m}(j̃) ≅ Y_t and F_{a x_m}(j̃) ≅ φ_{c_{m+1}}(t). In particular a x_m ≠ x_m.
- (b) Let v be the vertex of D^m that contains the chart vertex a x_m along β̃^m_+. Exactly one of the following holds.
  - (α) *Frozen partner.* v is merged along β̃^m_+, or v = {a x_m} is intact and non-constant on D^m with J_m ∉ stratum(D^m). Then [φ_{c_{m+1}}] ≡ [Y_0] is constant.
  - (β) *Persistent partner.* v = {a x_m} is intact and constant on D^m, v ≠ c_m, and [φ_v] ≡ [φ_{c_{m+1}}]. So D^m carries two distinct constant vertices, c_m and v, both ≅ Y_0 at t = 0, with value functions [Y] and [φ_{c_{m+1}}].
  - (γ) *Incoming crossing.* v = {a x_m} is intact and non-constant on D^m, and J_m ∈ stratum(D^m).

*Proof.*
(a)
- a acts on Def(J_m) only, not on t. Hence a^{-1}·closure((aÑ^{m+1}_−)_t) = closure(Ñ^{m+1}_{−,t}), so a^{-1} j̃ ∈ closure(Ñ^{m+1}_{−,t}).
- c_{m+1} = {x_m} along β̃^{m+1}_−. By (∗), F_{x_m}(a^{-1}j̃) ≅ φ_{c_{m+1}}(t).
- By (K3) with σ = a^{-1}, F_{x_m}(a^{-1}j̃) ≅ F_{a x_m}(j̃).
- By (∗) on Ñ^m_+, F_{x_m}(j̃) ≅ φ_{c_m}(t) ≅ Y_t.
- If a x_m = x_m, then [Y_t] = [φ_{c_{m+1}}(t)]. That is excluded since t ∉ Z_φ.

(b) The three cases exhaust the possibilities. Either v contains an unpinched edge, or v is a singleton {a x_m}, which is then constant or non-constant on D^m.
- (α), merged case.
  - An unpinched edge along β̃^m_+ means J_m ∉ stratum(D^m). So the limit of the transported branch at j̃ is a puncture p′ of D^m_t (R8-8 Theorem 1, Step 2).
  - f_v(p′) is glued from the F_y(j̃), y ∈ v. It contains F_{a x_m}(j̃) as a component with its special points (R7-1 Lemma 1(a)).
  - f_v(p′) is nodal, so v ∈ M(D^m_t). By R8-8 Lemma 2, f_v(p′) ∈ F.
  - Hence [φ_{c_{m+1}}(t)] ∈ A. Here a x_m has the type (g_i,n_i) of x_m, since a is an automorphism.
- (α), non-constant singleton case. Since t ∉ D_all, v ∈ M(D^m_t). Then f_v(p′) = F_{a x_m}(j̃) ∈ F, and again [φ_{c_{m+1}}(t)] ∈ A.
- (α), conclusion. In both sub-cases [φ_{c_{m+1}}(t)] ∈ A for all generic t, a set accumulating at 0. By R8-8 Lemma 1, [φ_{c_{m+1}}] is constant, and its value at t = 0 is [Y_0].
- (β).
  - By (∗) applied to (Ñ^m_+, v), F_{a x_m} ≡ φ_v(t) on closure(Ñ^m_{+,t}). So [φ_v(t)] = [φ_{c_{m+1}}(t)] for every small t, and the identity theorem gives [φ_v] ≡ [φ_{c_{m+1}}].
  - v ≠ c_m, because a x_m ≠ x_m and distinct intact chart vertices are distinct vertices of G_{D^m}.
  - At t = 0, φ_v(0) ≅ F_{a x_m}(0) ≅ F_{x_m}(a·0) = F_{x_m}(0) ≅ Y_0. ∎

**Endpoint analogue (Lemma 1′).** Case (ii) of (PT): Q_0 has copies x and x′ = a^{-1}x, x merges (or puncture-moves) along β̃^E, and x′ is intact and constant on E with [φ_{x′}] ≡ [Y]. Choose q̃(t) ∈ closure(Ñ^E_t) ∩ π^{-1}(Q_t) with F_{x′}(q̃(t)) ≅ Y_t. Then for all small t:
- [F_x(q̃(t))] = [Y_0] (**the merging copy is frozen**);
- at the D^k-side lift a q̃(t), the chart vertex x is the Y_t-copy and the chart vertex a x has frozen class [Y_0].

*Proof.*
- q̃(t) lies over Q_t ∈ Δ_{G_{Q_0}}, so q̃(t) ∈ L_x. Its pinching pattern is that of β̃^E, so x is merged (or moving at a puncture) along Ñ^E_t.
- By R7-1 Lemma 1 and R8-8 Lemma 2, [F_x(q̃(t))] ∈ A for every t.
- F_x is continuous on L_x, and q̃(t) → 0, so [F_x(q̃(t))] → [Y_0]. A is finite, hence [F_x(q̃(t))] = [Y_0] for small t.
- The last claim follows from (K3): F_x(a q̃) ≅ F_{a^{-1}x}(q̃) = F_{x′}(q̃) ≅ Y_t, and F_{ax}(a q̃) ≅ F_x(q̃) ≅ Y_0. ∎

## 2. Proved: the tracked function is frozen at a coherent endpoint (Lemma 2)

**Lemma 2.** Suppose the endpoint is MERGE or pMOV and (C_k) holds, i.e. (SC_k) or (NT_k). Then [φ_{c_k}] ≡ [Y_0]. **No assumption [φ_{c_k}] ≡ [Y] is needed.**

*Proof.* This is R8-8 Theorem 1, Step 2, with Y_t replaced by φ_{c_k}(t).
- Step 2 uses only (∗) for (Ñ^k_+, c_k), giving a q̃ with F_x(q̃) ≅ φ_{c_k}(t), together with R8-8 Lemma 2.
- It yields [φ_{c_k}(t)] ∈ A for t in a set accumulating at 0.
- By R8-8 Lemma 1, [φ_{c_k}] is constant, and its value at t = 0 is [Y_0]. ∎

**Corollary 3 (bookkeeping along the chain).** Put f_m := [φ_{c_m}], so f_1 = [Y]. By R8-8 Theorem 1, Step 1, f_{m+1} = f_m whenever (C_m) holds. Assume Y is non-constant. Then:
- either the endpoint is a twin (case (ii)), with a frozen merging copy by Lemma 1′;
- or (C_k) holds and f_k ≡ [Y_0] is constant (Lemma 2), so f jumps at least once on its way from the non-constant [Y] to a constant.

At the first jump m_1, Lemma 1 applies (when the jump is of type (b)). It shows that the twin pair at J_{m_1} carries, at a single lift j̃, the two classes [Y_t] and f_{m_1+1}(t). The partner of the Y-copy is either frozen (α), persistent on D^{m_1} (β), or a crossing (γ).

**Consequence.** Every realisation of (PT) has a point of B_0 with an automorphism a exchanging two Y_0-copies whose deformations differ, one ≅ Y_t and the other of another class (often the frozen class Y_0). By R8-8 §3 this is possible only if |Aut(J_{m,t})| < |Aut(J_m)| for generic t, i.e. only under the coarse reading (R2). This sharpens R8-4 (T1)–(T2), but it is not a contradiction.

## 3. Option 1: mechanisms tried, and where each one stops

**3.1 Interior paths (thin squares). Reduction proved; it lands on R8-5 Proposition D.**
- At t = 0, β̃^m_+ and β̃^{m+1}_− lie on a common irreducible component X_0 of the lifted germ S̃_0 at 0 ∈ Def(J_m). So their interior neighbourhoods are joined by paths γ in X_0 ∖ {∏ s_e = 0} inside B(0, ρ), for every ρ.
- Fix a generic t. Let d(t) > 0 be the minimal distance between distinct lifts of J_{m,t}. Use the quotient metric, so that π^{-1}(B(J_{m,t}, r)) is the union of the balls B(ℓ, r) around the lifts ℓ.
- H is uniformly continuous on closure(V_0) × Δ̄_r. Hence for ρ small, H_t(π(γ)) ⊂ B(J_{m,t}, d(t)/3), and every lift of it lies in a single ball.
- If the square (τ, s) ↦ H_s(γ(τ)), s ∈ [0, t], lifts to Def(J_m) without monodromy, then:
  - the left edge, the transport of a point near β̃^m_+, ends in the ball of j^m(t);
  - the right edge ends in the ball of j^{m+1}(t);
  - so j^m(t) = j^{m+1}(t), which is (SC_m).
- The monodromy is non-trivial only if the square meets the branch locus. The branch locus consists of curves of V_σ that have an automorphism coming from Aut(J_m) and moving x_m, at points within distance ω(ρ) of J_{m,σ}.
- For σ bounded away from 0, a small ρ avoids such points. As σ → 0 it does not. This is exactly Proposition D, cases (A), (B), (C), of R8-5.
- So 3.1 gives no new exclusion. It does give a clean reformulation: **a twin jump at J_m happens only if curves of V_σ with an extra automorphism moving x_m accumulate at J_m as σ → 0.**

**3.2 Lock from a persistent automorphism along D^{m+1}. Dead.**
- By Lemma 1(a), at generic t the two copies at j̃ have different classes, Y_t and φ_{c_{m+1}}(t).
- So no automorphism exchanging c_{m+1} and w can persist along the transported piece D^{m+1}_t.
- An automorphism exchanging them along D^{m+1} at t = 0 (which total geodesy might supply) is not transported, because H_t need not preserve automorphism groups under (R2).
- Under (R2^orb) it would be transported, and the twin problem disappears altogether (R8-8 §3).

**3.3 Restarting Prop K on the partner. Reduces to MS7.**
- Lemma PA and Prop K apply to any piece and any constant vertex. Restarting from (D^{m+1}, w) with [φ_w] ≡ [Y] gives a new chain, which may jump again.
- The set of pairs (D, c) at time 0 is finite, so the restarts eventually cycle. I found no quantity that decreases strictly along a restart, for example one tied to Teichmüller levels.
- This is MS7 of R7-3: the Y-network is an Aut-closed set.

**3.4 Krull pair at one lift (endpoint case). Consistent, so no contradiction.**
- At generic t, at q̃(t) (Lemma 1′), x′ is the Y_t-copy.
- By Lemma G (R8-4), every boundary branch through q̃(t) keeps x′ intact.
- Let X be an irreducible component, through q̃(t), of the preimage of closure(V_t). Then X ∩ {∏ s_e = 0} = X ∩ L_{x′} = X ∩ {s_f = 0} for each edge f at x′. All of these sets are 1-dimensional, by Krull.
- This holds only in a ball whose size depends on t, and the time-0 limit of these balls is the point 0. It is compatible with the R7-3 §5 local model.

**3.5 Total geodesy in case (A) of Proposition D. Sketch only.**
- Fix(α) lifts to a totally geodesic complex submanifold of T_g, the image of the Teichmüller space of the quotient orbifold.
- Teichmüller geodesics are unique, so Fix(α) ∩ (lift of V_0) is geodesically convex. Hence any 1-dimensional component of it is a Teichmüller disc, so Fix(α) ∩ V_0 near J is a union of Teichmüller curves of α-symmetric curves, with J in their closure.
- I could not show that such a curve forces the twins at J_{m,t} to stay isomorphic (Lock).
- Cases (B) and (C) are untouched. Case (C) is invisible at t = 0.

## 4. Option 2: what a realisation of (PT) needs; not achieved

A counterexample to MS8 through (PT) needs all of the following.
1. A smooth closed totally geodesic V_0 whose network has a point J (or Q_0) with an automorphism a exchanging two Y_0-copies. At a junction, one copy is the tracked copy x_m, and by Lemma 1 the incoming piece carries a frozen, persistent or crossing partner. At the endpoint, one copy merges.
2. At every cusp of ∂V_0, the conditions (Tw1)+(C1)+(C2) must fail (R8-4 Theorem 2V), and so must (IP), (U_J) and (NB).
3. A family V_t satisfying (R1), (R2) and (Rig) with the following properties:
   - |Aut(J_t)| < |Aut(J)| for generic t;
   - the copies separate as Y_t versus φ′(t) (Lemma 1), where φ′ is often the frozen constant Y_0;
   - curves with an automorphism moving x_m accumulate at J as t → 0 (§3.1).

What is known about each of these:
- Item 1 is typical for Galois covering constructions, where deck groups permute boundary components. But the run found merges at cusps of ∂V_0 for every Galois construction over M_{0,5} and M_{1,2}, so these constructions do not obviously satisfy item 2. Item 2 is unchecked for any smooth example. The quintic example (PR-I) is not smooth, and it satisfies Theorem 2V anyway.
- Item 3 is entirely open. The local chart models (R7-3 §5, R8-4 §5, R8-5) satisfy every local constraint known, including (Rig), Lemma G, Lemma X and Krull. But I know no method to build a non-totally-geodesic deformation V_t whose boundary is controlled stratum by stratum.
- **No counterexample is claimed.**

## 5. Summary

**Proved.**
- Lemma 1 and Lemma 1′: the twin partner at a jump carries the other class function at the same lift. On the incoming side it is frozen (constant [Y_0]), persistent, or a crossing. The merging copy at an endpoint twin is frozen.
- Lemma 2: at a coherent MERGE/pMOV endpoint, the tracked function is frozen, [φ_{c_k}] ≡ [Y_0].
- Corollary 3: the bookkeeping of value functions along Prop K's chain.
- §3.1: the reformulation of a twin jump as accumulation of symmetric curves of V_σ at J_m.

**Not proved / open.**
- Whether (PT) can occur, i.e. the twin half of MS8.
- MS7: no Aut-closed Y-network exists.
- Lock in cases (A), (B), (C) of Proposition D.
- Entry 82 ((Rig) itself).
- A realisable family V_t for any candidate V_0.

**Conditional.** Under the orbifold reading (R2^orb), twin jumps cannot occur (R8-8 Corollary 1(a)), and MS8 then reduces to the interior-MOV endpoint case.



## Reminder
- Never assume V_t totally geodesic for t ≠ 0, and never assume H_t preserves automorphism groups (the orbifold reading (R2^orb) is NOT adopted).
- A proof for a sub-class, or under an extra hypothesis, does not answer the question; report it as partial.
- Begin with a plan/status line. End with: proved / not proved / open.
