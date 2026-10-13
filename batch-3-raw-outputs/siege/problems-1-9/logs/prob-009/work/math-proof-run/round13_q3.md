kind: attempt
Open question attempted: the run's missing statement MS11♭ (OPEN, ledger entry 124, locator round12_plan). Under the run's adopted readings (R1), (R2), it is, together with the separate input (Rig) (entry 82), the single statement that stands between the proved results below and the problem's claim. Rounds 11 and 12 attacked it. Round 12 reduced every known failure mode to a "rigid twin" (see the sketch and part 5), but did not close it.

## Task
Prove MS11♭ exactly as stated below, or give an explicit counterexample to it. A counterexample is an admissible configuration that satisfies all its hypotheses and violates its conclusion, with every step written out.

- A proof of MS11♭ for only some of the cases it covers does NOT answer the question. This includes:
  - proofs for a sub-class of the points Q, of the surfaces V_0, of the families V_t, of the labels x, or of the branch pairs;
  - proofs under an extra hypothesis such as Q-factoriality, (U_J), (U″), (SC), (IP), (IP_Γ), (NT), (Lock), (NB), (R2^orb), "no twins", "a single lift-curve", "no reflection of S", or "Y_0 of positive genus".

  If that is all you find, report it, labelled as partial.
- MS11♭ contains the hypothesis "t ↦ Y_t is non-constant". So a valid proof may also derive a contradiction from its setting, e.g. by showing that under (R1), (R2), (Rig) the function Y must be constant. Such a proof also proves the problem's claim under (Rig), and it is welcome.
  - In particular, you may run the chain below with Φ-persistence (round12_q7, part 5) in place of Y-persistence. If you do, you must check every chain step that you use in its Φ-form; round12_q7 §3 lists which steps those are.
- Also check the chain below, which derives the problem's claim from MS11♭ together with (Rig). If that derivation is flawed, say exactly where; that is a result too.
- Logical status (proved; round11_q1 Prop. 1.1, round11_q4 §1):
  - A counterexample to MS11♭ is a counterexample to the problem for a family satisfying (Rig).
  - A proof must use global information: total geodesy of V_0, the global family, smoothness of V_0, or "Y non-constant".
  - Arguments local to the chart Def(Q) × Δ, or to one 3-fold component there, are known to be insufficient (local models in round11_q7 §6, round11_q1 §5, round12_q1 §3, round12_q2 §2, round12_q3 §4, round12_q6 Model G3′).
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

## How MS11♭ is used: the chain (verbatim from the run's summary). Ledger entry numbers: 19 = holomorphy of t ↦ Y_t (PR-A, from (R1),(R2) via Remmert/removable singularities); 24 = incidence transport P_t = H_t(P_0); 82 = (Rig), OPEN, a hypothesis of MS11♭; 84 = Theorem X*/X′ (round9_q4 §1, round9_q3); 85, 98 = Proposition K_w, walk chain, with repairs and Lemma S̃′ (round9_q4 §2, round10_q10); 86 = Lemma PT (round9_q3); 87 = Lemmas T, S, J, Theorem R (round9_q7); 97 = Theorem X*_all, 99 = Cor. IMOV_all (round10_q1); 112 = Lemma B1♭ and the Gap A repair, 113 = the chain check (round11_q9). All are spliced below.
**Chain** (every step PROVED except MS11♭ and the separate open input (Rig), entry 82).
1. **Goal ⇐ MS8 + (Rig) + entry 19.** MS8: under (R1), (R2), (Rig), Y_t = Y_0 for all t. Given (Rig), MS8 is the goal; entry 19 turns "Y constant" into Y_t = Y_0.
2. **MS8 ⇐ MS11♭** (round11_q9 §5, this round's entry 113). Assume MS8's setting and, for contradiction, that Y is non-constant.
   - (a) **Walk chain** (entries 85, 98; Σ enlarged by the finite sets R(D), Gap A repair). Pieces D^1 ⊂ ∂V_0, D^2, …, D^k; transitions J_1, …, J_{k−1}; endpoint Q_0. At J_m: entering lift β̃_m, leaving lift β̃′_m, common chart vertex x_m, both lifts in one irreducible component of q^{-1}(closure V_0) ∩ B (Lemma S̃′). At Q_0: entering β̃ (vertex x) and terminal b̃ in one such component, x MERGE or MOV along b̃ at t = 0.
   - (b) **Interior transitions trivial** (entry 99): at J_m in the stratum of D^m or D^{m+1}, β̃′_m = β̃_m, so anchored sheets coincide. Hence Q_0 and every genuine transition (β̃′_m ≠ β̃_m) satisfy (P). Transitions with β̃′_m = β̃_m need nothing.
   - (c) **Induction claim:** x_m is Y-persistent on some anchored sheet of β̃_m.
     - Base: Δ_Γ product type; vertex i persistent on every sheet of every lift of a branch of D^1 (round11_q9 §2.5).
     - Product-type puncture transition: Lemma PT (entry 86), Lemma J / Cor. J′ (entry 87); weak input suffices and the output is an anchored sheet of β̃′_m (round11_q9 §2.6).
     - Non-product puncture transition with β̃′_m ≠ β̃_m: MS11♭ for (J_m, β̃_m, β̃′_m, x_m); (P) by (b), (S) by (a).
     - Transfer along D^{m+1}: from an anchored sheet of β̃′_m to an anchored sheet of β̃_{m+1} (round11_q9 §2.7, using B1♭ and Lemma S(c) of entry 87).
   - (d) **Endpoint.** Product type: Lemma PT + Lemma J (J1)/Theorem R give Y_t in a finite set on an open set, contradiction (entry 19). Non-product: MS11♭ gives an anchored sheet T ⊃ b̃ × {0} of b̃ with x persistent; restricting to t = 0, x is intact along b̃ with F_x ≡ Y_0, contradicting MERGE and MOV (round11_q9 §2.8).
   - Hence Y is constant: MS8.

So MS11♭ + entries 19, 24, 84–87, 97–99 + B1♭ (this round's entry 112) give MS8, and MS8 + entry 82 give the goal. After MS11♭ only entry 82 ((Rig)) remains.


## A suggestion (the planner's sketch; you are free to discard it)
Label key for the sketch: S63 = round12_q2 Lemma A and Prop. B, round12_q6 Lemmas G1–G2 and Prop. G4, round12_q1 Lemma F (all in part 5); S64 = round12_q7 (Φ-reformulation, part 5); S65 = round12_q8 (configuration (γ°), part 5); Lemma TG = round9_q5 (part 2); Lemma S = round8_q7 / round9_q7 (pieces are K × {c_t} under (Rig)); Theorem N = R8-3 (part 1); Prop. B = round12_q2 §3.

**Why it should hold (planner's sketch; NEW mechanism this round: rigid-twin exclusion through Φ-persistence. It replaces Mechanism G, whose step 4 was refuted locally.)**
1. *Every failure is a rigid twin.* By S63, failures can only come from lost automorphisms a ∉ K_S·Stab(b̃) of Q. By S64, a (β)-twist or the initial twist preserves persistence in the Φ-sense unless the twin is rigid; at the endpoint the merging label is rigid. By S65, a (γ°)-edge forces a frozen twin along the lift-curve. So, granted the Φ-version of the chain (S64's unchecked substitution), every failure produces the configuration **(NRT-config)**:
   - a point Q ∈ B_0 and a ∈ Aut(Q);
   - a lift-curve L;
   - labels x ≠ y = a^{-1}x;
   - along L, F_x ≅ φ(t) with φ ∈ Φ non-constant, and F_y ≡ Y_0 for all t;
   - at t = 0, x and y are intact constant Y_0-copies along a lifted branch c̃, exchanged by a.
2. *What the rigid copy is.* Along L, y is frozen, so Y_0 ∈ 𝔉 (a puncture value of a moving vertex of some piece through Q_t; q7 Lemma 4.1). On the anchored sheet T of c̃, y is a constant vertex of the transported piece c_t whose value is EXACTLY Y_0 for all t (S64 Lemma 1.2). So c_t has, for every t, two constant vertices x, y of the same type: one with value φ(t), one frozen at Y_0. At t = 0 they are exchanged by a ∈ Stab_pt(c̃), a generic automorphism of the curves of c.
3. *Candidate contradiction (to test).* Take the generic curves of the piece c at t = 0. They admit a, which swaps the two constant Y_0-components.
   - Total geodesy at t = 0 forces the a-action on the sheet S through c̃ to be either trivial on S (harmless: Prop. B) or a reflection of S fixing c̃ (Lemma TG).
   - In the reflection case, the two constant components x, y appear as limits of the SAME family of subsurfaces of the nearby smooth curves of V_0, approached from the two sides of c̃ (the plumbing parameter s ↦ −s).
   - The deformation V_t then has to separate them: on one side the copy follows φ(t), on the other it stays at Y_0.
   - The pieces of V_t near c_t have the form K × {c_t} (Lemma S), and the two sides of c̃ in S are glued by H_t continuously.
   - So the side-swap should force φ(t) and Y_0 to be values of the same constant vertex along a connected family. Since φ is non-constant, Theorem N should then make that copy merge or move at a puncture at generic t, contradicting the generic-time trichotomy.
   - This is my conjecture for (R-a) (the reflection case). (R-b) and (γ°) reduce to it by S63/S65.
4. *Fallback.* Prove (NRT): the configuration of item 1 does not occur. With S64's substitution check, (NRT) gives MS11♭ (in its Φ-form), hence MS8.


## What is already known (do not merely re-derive it)
- At product-type points the twin problem does not arise (Lemma PT, round9_q3 §3; Lemma J / Cor. J′, round9_q7).
- At points interior to an adjacent piece, in any stratum, entering and leaving lifts coincide (round10_q1 §4, Cor. IMOV_all; Theorem X*_all, round10_q1 §2; Lemma S̃′, round10_q10 §6.3; all re-checked in round11_q9 §1). That is why MS11♭ assumes (P) and (S).
- Lemma B1(a),(b) of round10_q3 are FALSE (round11_q9 §2.2, round11_q2, round11_q3, round11_q8): a component of closure(Ñ_b̃) may meet {t = 0} only in another lift a·b̃. Hence the anchored-sheet wording; B1♭ (round11_q9 §2.3) is the correct replacement, and the chain was re-checked with it (round11_q9 §§2, 5).
- Persistence on a boundary-type sheet is read off any lift-curve in it: P(T) = C(L) (round11_q4 Lemma 2.2, round11_q1 Lemma 2.3; uses R8-2 Theorem 1 / R8-3 Theorem N under (Rig), Y non-constant). Hence MS11♭ holds at Q whenever Q_t has a single lift-curve, e.g. when |Aut(Q_t)| = |Aut(Q)| for generic t; so a failure needs Q_t to lose automorphisms of Q. (Under the orbifold reading (R2^orb), NOT adopted, MS11♭ would therefore hold everywhere.)
- Mechanism D (round11_q3, round11_q7; also round11_q1 §3, q5, q8): in a 3-fold component X ⊃ S × {0}, D = X ∩ {∏ s_e = 0} has a connected sheet graph (Grothendieck connectedness); all D-sheets are anchored and of boundary type; persistent labels pass along lift-curve edges and along edges through curves at t ≠ 0 except in configuration (γ°); at a shared t = 0 branch c̃ they are twisted by σ ∈ Stab_pt(c̃); the x-carrying anchored sheet of β̃ meets X after an initial twist in Stab_pt(β̃). So MS11♭ fails only through a label-moving composite of (β)-twists or through (γ°). Both are realisable in chart-level models (round11_q7 §6, round11_q1 §5, round11_q2 §1.2), so global input is needed.
- Twin-free results (round11_q4 §3): every piece reachable from ∂V_0 by puncture transitions has a constant vertex with value ≡ Y; Criterion R and the twin-free merge criterion TFM. Rigid twin at the endpoint (round11_q1 §4).
- Logical status (round11_q1 Prop. 1.1, round11_q4 §1, round10_q4): under (Rig), MS11♭ is equivalent to the problem's claim; a counterexample to MS11♭ is a counterexample to the problem.
- Older sufficient conditions, none known in general: Krull linkage (round10_q7 Theorem Q), (U_J)/(Lock), (U″), (SC)/(NT)/(IP), (IP_Γ).
- Necessary conditions for a failure: an automorphism of Q moving x and lost by Q_t; the cusp Q leaving closure(V_τ) for generic τ (round10_q3 Lemma 3.1); (NC1), (NC2) of round11_q4 at every point of the reachable network.
- Routes shown to give nothing new: counting (round10_q7 §2); level structures (round10_q5, round10_q6); arithmetic of fields of definition (round10_q8); first-order Douady deformation theory (round11_q6 §3); psh-isolation for type-(0,5) vertices (round11_q10 Prop. DP).

- **New in round 12 (all spliced in part 5):**
  - Lemma F, Lemma A, Prop. B, Prop. G4: automorphisms in K_S (the pointwise stabiliser of the t = 0 sheet S) or in Stab(b̃) never cause a failure. The lift-curves in a 3-fold component X form one G_X-orbit.
  - A failure needs (R-a) a lost automorphism acting non-trivially on S (a "reflection") or moving S, or (R-b) an initial twist τ ∉ Stab(b̃)Stab(x) (round12_q6 §4).
  - Planner's previous step 4 ("g fixing S pointwise fixes L_0") is false locally, but this is harmless.
  - Φ-reformulation (round12_q7): (β)-twists preserve Φ-persistence unless the twin is rigid (value ≡ Y_0). At the endpoint the merging label is rigid. The chain's Φ-version is unchecked.
  - (γ°) (round12_q8): it forces a moving twin u ∈ M_W, a frozen twin F_u ≡ Y_0 along the lift-curve, and Y(Δ) ⊂ pr_u(K_W).
  - Euler bound for twin points; the problem is vacuous for g = 2 (round12_q4).
  - Twin-free routes cannot work without using smoothness of V_0, persistence, or label-level data (round12_q10; quintic obstruction).
- **Under the orbifold reading (R2^orb)** (H lifts equivariantly with isotropy preserved on boundary strata), MS11♭ holds everywhere. (Rig) also holds there (round12_q9 Theorem RO), so the claim holds. This is NOT the adopted reading, and it must not be assumed here.

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




## Prior results, part 3: round 10 (verbatim answer files or sections, bookkeeping line removed; re-check what you use)

### round10_q1 (verbatim): Theorem X*_all, Lemma 1SS, Cor. IMOV_all, chain check
# round10_q1 — attempt on MS10

## Status / plan
- **Outcome: PARTIAL.** I neither prove MS10 in full nor give a counterexample.
- **What is new and proved here** (modulo cited standard facts and the run's inputs, listed in §6):
  1. **Theorem X\*\_all.** Theorem X\* of round9_q4 holds for pieces in **every** stratum, not only product-type ones (§2). Steps 1–4 of R8-1 Theorem X are redone on a lifted piece Ê ⊂ ∏_w M_w. This was listed as open in round9_q3 (Remark 4, "Not proved") and round9_q4 (open item (ii)). I also correct a small slip in the homological step of X\*. The slip does not affect its conclusion.
  2. **Lemma 1SS (one chart sheet per excursion).** Assume the reading (T4) of round9_q5 (every component of the preimage of V_0 in T_g is a totally geodesic complex submanifold). Then every excursion of the walk chain (Prop. K_w) lifts into a **single irreducible component S** of the preimage of closure(V_0) in the chart, and S contains both the entering lift and the leaving lift (§3). Before this, round9_q3 (Cor. SS′(b)) and round9_q4 (Lemma S′) only placed *some* lift of the entering branch in a common sheet with the leaving lift.
  3. **Corollary IMOV\_all (§4).** Combine 1 and 2. In the walk chain, at every junction and at the endpoint, **in every stratum**: if Q lies in the stratum of the entering or of the leaving piece, then the entering and leaving lifted branches coincide as sets. Consequences:
     - the endpoint is never interior-MOV;
     - there are no junction crossings;
     - the "turning twin" (T) never occurs.
     So the MS10 instances that the chain uses are **proved whenever Q is an interior point of the piece of β̃ or of the piece of b̃**. For walk-chain data the IMOV part of chain step (d) is settled for non-product strata.
  4. **Residual (precisely located).** MS10 for walk-chain data is open only when Q is a **puncture of both** adjacent pieces. Equivalently, these are the persistent twin (b) at a junction and the endpoint twin (e) with MERGE or puncture-MOV, at a point Q of a non-product stratum.
- **Chain check (§5).** I found no logical flaw in the derivation "MS10 + (Rig) + proved entries ⇒ claim". But **MS10 as worded is stronger than what the chain uses.** It allows arbitrary joining paths in q^{-1}(V_0) ∩ B. The walk chain supplies Teichmüller-ray paths, which satisfy one-sheet property 2. I recommend replacing MS10 by MS10′ (§5), which carries that property. MS10′'s open part is exactly item 4.
- I also re-derived the "global tracking along Prop.-K segments + finite-set continuity" argument independently. It coincides with R8-5 Theorem A, so it is not claimed as new; see §6.

---

## 1. Conventions

- Readings (R1), (R2) with H_0 = id, as in the task file. The orbifold reading (R2^orb) is **not** used.
- **(T4)** (round9_q5 §0). Every component S_T of the preimage of V_0 in Teichmüller space T_g is a complex submanifold that contains every real Teichmüller geodesic tangent to it.
  - This is the literature's meaning of "totally geodesic subvariety": the image of a totally geodesic complex submanifold of T_g.
  - Smoothness of V_0 in the coarse space alone would not give it, so I state it as a reading.
  - It is used only in §3.
- **Charts.** For a stable curve Q:
  - Def(Q) is the Kuranishi germ, with smoothing parameters s_e, e ∈ E(G_Q).
  - q : B → B/Aut(Q) is the chart on a small Aut(Q)-invariant ball B.
  - The stratum locus is L := {s_e = 0 ∀e}.
  - Fix an identification G_Q ≅ G of the dual graph. Partial normalisation gives the holomorphic map Π : L → ∏_{w∈V(G)} M_w, with ξ_G ∘ Π = q on L. Here ξ_G : ∏_w M_w → Δ_G is the gluing map. It is finite, and on coarse spaces it is the quotient by Aut(G).
- **Pieces and lifted pieces.**
  - A *piece* is a 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G, for some stratum Δ_G (product type **not** assumed).
  - A *lifted piece* is an irreducible component Ê of the 1-dimensional analytic set ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ ∏_w M_w with ξ_G(Ê) dense in E.
  - Ē̂ denotes the closure of Ê in ∏_w M̄_w. It is a compact irreducible curve, being a component of the compact analytic set ξ̄_G^{-1}(closure(V_0) ∩ closure(Δ_G)). Here ξ̄_G is finite, hence proper.
  - Ê^ν denotes the normalisation of Ê, a connected Riemann surface.
- **Sheet.** A *sheet* at Q is an irreducible component of the germ at 0 of q^{-1}(closure V_0). For B small these are the global irreducible components of q^{-1}(closure V_0) ∩ B.

## 2. Theorem X\*\_all: Theorem X\* in every stratum

**Setting** (as in R8-1 §3.1 and round9_q4 §1.1, but with **no product hypothesis**):
- V_0 ⊂ M_g is closed, 2-dimensional and totally geodesic.
- E is a piece in a stratum Δ_G, and Q_0 ∈ E. So Q_0 is an interior point of E in its own stratum.
- β is a local branch of E at Q_0, and β̃ ⊂ L ⊂ Def(Q_0) is a lift of β through 0.
- S is a sheet at Q_0 containing β̃.
- ν : Ŝ → S is the normalisation, ŝ_0 := ν^{-1}(0), and B̂ := ν^{-1}(S ∩ {∏ s_e = 0}).
- Ê_1, …, Ê_r are the components of the germ (B̂, ŝ_0) that map onto β̃. C_1, …, C_m are the others. **The others include any component mapping onto a different lift aβ̃ ≠ β̃ of the same coarse branch.**

**Theorem X\*\_all.** m = 0. Every component of the boundary curve of Ŝ at ŝ_0 maps onto β̃. Equivalently, S ∩ {∏ s_e = 0} = β̃ near 0.

The proof of round9_q4 has two parts:
- Steps 1–4 of R8-1 Theorem X, which produce discs D̂_n → L̂;
- the homological step, which is local in Ŝ and uses no product hypothesis.

Product type was used only in Step 3 (R8-1 Remark 2), through a global coordinate f_j on E ⊂ ∏ M_w. I redo Steps 1–4 with E replaced by a lifted piece.

### 2.1 Steps 1–4 for an arbitrary stratum

**Step 1 (base point, approximants).**
- Ê := the lifted piece containing the germ Π(β̃). Π(β̃) is a curve germ at ẑ_0 := Π(0) inside ξ_G^{-1}(E), so it lies in a lifted piece.
- e_0 ∈ Ê^ν is the point over ẑ_0 on the branch Π(β̃).
- B ⊂ Ê^ν is a small closed disc around e_0. Its image in Ê is a neighbourhood of ẑ_0 on the branch Π(β̃). It maps under ξ_G into a small neighbourhood U of Q_0, and B ∖ {e_0} maps into β ∖ {Q_0}.
- Pick P_1 ∈ β ∖ {Q_0}, with lift P̃_1 ∈ β̃ and Π(P̃_1) in the image of B ∖ {e_0}. Take P_1 generic in the sense of R8-1 Step 1, and also require that Π(P̃_1) lie on no other component of ξ_G^{-1}(closure V_0 ∩ Δ_G). The excluded set is discrete in β.
- **Lemma PA holds at P_1.** Its proof (PR-H §1) uses only:
  - the local plumbing chart at P_1 (Def(P_1) with coordinates (z, s_e));
  - a normalised local branch N of closure(V_0) along E at P_1;
  - a ≠ 0, where a is the s-derivative of z.

  None of these needs product type. In particular a possible generic automorphism group of the piece is harmless, since one works in Def(P_1).

  So there are X_n ∈ V_0 ∩ N with X_n → P_1, and generating pairs (X_n, q_n), with transplanted limits (q_w)_w satisfying Σ‖q_w‖ = 1. There is a vertex j with q_j ≠ 0 and ‖a_j‖ = A > 0, so the j-coordinate moves along E at P_1. The approximants can be chosen in the sheet S, as in R8-1 Step 1.

**Step 2 (the limit disc and its lift).**
- Let D_n : 𝔻 → V_0 be the Teichmüller disc of (X_n, q_n). It lies in V_0 by total geodesy.
- Let D̃_n ⊂ T_g be its lift through a lift of X_n. This gives a marking along all of D_n.
- R8-1 Step 2 is local and stratum-independent. Each D_n(w) stays within Teichmüller distance ρ = d_𝔻(0,w) of X_n, so by Wolpert and Abikoff every limit point lies in a compact part K_ρ of Δ_G. A subsequence converges locally uniformly to L : 𝔻 → B_0 ∩ Δ_G with L(0) = P_1.
- **The lift L̂.** For w ∈ 𝔻, the node curves of L(w) are, under the disc's marking, exactly those of P_1 (same estimate). So the components of L(w) are labelled by the vertex subsurfaces of P_1.
  - Label those subsurfaces by V(G) through the chart Def(Q_0) at the lift X̃_n near P̃_1. This is the identification fixed in Π.
  - This defines L̂(w) ∈ ∏_w M_w with ξ_G ∘ L̂ = L and L̂(0) = Π(P̃_1).
  - Locally near w, L̂ equals Π_Z ∘ (limit of the chart lifts of D_n into Def(Z)), with Z a limit point and Π_Z the partial normalisation of Def(Z) under the marking-induced labels. Chart lifts are images of the T_g-lift (T_g ↔ Def chart description, cited as in R8-1). So L̂ is well defined and holomorphic.
- **L̂(𝔻) ⊂ Ê.**
  - L̂^{-1}(Ê) is an analytic subset of 𝔻, since Ê is closed analytic in ∏_w M_w.
  - Near w = 0, L̂ takes values in ξ_G^{-1}(E) near Π(P̃_1), and that point lies only on Ê. So L̂^{-1}(Ê) contains a neighbourhood of 0.
  - By the identity theorem, L̂^{-1}(Ê) = 𝔻.
  - L̂ is not contained in Sing(Ê), so it lifts to Ê^ν. I keep the name L̂.
- **Non-constancy.** By (Fl), the j-component of L(w), labelled through the marking, is A_w·(Y_j(P_1), q_j). So pr_j ∘ L̂ = τ, the Teichmüller disc of (Y_j(P_1), q_j) in M_j := M_{g_j,n_j}. It is non-constant.

**Step 3 (L̂ : 𝔻 → Ê^ν is surjective).**
- C_j := pr_j(Ē̂) is a compact irreducible curve in M̄_j: it is the image of an irreducible compact curve (Remmert), and it is not a point because τ is non-constant.
- Put C_j° := C_j ∩ M_j. It is irreducible, and τ(𝔻) ⊂ pr_j(Ê) ∩ M_j ⊂ C_j°.
- Let τ̃ : 𝔻 → T_j lift τ, and put Δ̃ := τ̃(𝔻).
  - By (Prop), Δ̃ is a closed 1-dimensional submanifold, and its Mod-translates form a locally finite family.
  - So Δ̃ is an irreducible component of the preimage of C_j° in T_j.
  - Its image in M_j is closed and analytic, hence equal to C_j° by irreducibility.
  - With Γ := Stab(Δ̃), the map 𝔻/Γ → C_j° is proper.
- Let Λ be the set of holomorphic λ : 𝔻 → Ê^ν with pr_j ∘ λ = τ.
  - The map pr_j : Ê^ν → Ĉ_j (normalisation of C_j°) is the restriction of the finite map of compact Riemann surfaces (Ē̂)^ν → Ĉ_j to an open subset. So its fibres have at most deg elements.
  - A lift is determined by its value at one point over an unbranched value. Hence |Λ| ≤ deg, and L̂ ∈ Λ.
- Γ acts on Λ by precomposition. So Γ_L := Stab_Γ(L̂) has finite index, and L̂ descends to L̄ : 𝔻/Γ_L → Ê^ν.
- **L̄ is proper.** For compact K ⊂ Ê^ν, L̄^{-1}(K) is closed in (pr_j ∘ L̄)^{-1}(pr_j K). The latter is compact, because pr_j ∘ L̄ : 𝔻/Γ_L → Ĉ_j is proper (finite index in a proper map).
  - This needs **no** properness of pr_j on Ê, so it is unaffected by punctures of Ê at which only other coordinates degenerate. This is the same argument as R8-1.
- A proper non-constant holomorphic map to the connected Ê^ν is surjective.

**Step 4 (a path to Q_0).** Verbatim as R8-1 Step 4, with Ê^ν and e_0 from Step 1.
- Let W be the component of L̄^{-1}(int B) containing [0]. L̄|_W : W → int B is proper and non-constant, hence onto. Pick [w*] ∈ W with L̄([w*]) = e_0.
- Lift a path from [0] to [w*] in W to a path π ⊂ 𝔻 from 0 to w*. This is path lifting for properly discontinuous actions (Bredon, cited).
- Choose Ω ⊃ π connected and relatively compact, with L̂(Ω̄) ⊂ image of B.
- Then L(w*) = ξ_G(ẑ_0) = Q_0, and L(Ω) lies in β (coarse) ∪ {Q_0}.
- **Chart lift.** For n large, D_n(Ω̄) ⊂ U ∩ V_0. Lift D_n|_Ω to D̃_n : Ω → Def(Q_0) with D̃_n(0) = X̃_n. It lies in S (R8-1 Step 5; under (T4) also automatic, see §3). A subsequence converges to L̃, a lift of L|_Ω.
  - L̃(Ω) ⊂ ⋃_a aβ̃, and L̃^{-1}(0) = L^{-1}(Q_0) ∩ Ω is discrete, since q^{-1}(Q_0) = {0}.
  - The sets aβ̃ ∖ {0} are pairwise disjoint near 0, because distinct irreducible curve germs at 0 meet only at 0 in a small ball. Ω minus a discrete set is connected and its image contains P̃_1 ∈ β̃. Hence L̃(Ω) ⊂ β̃.
  - L̃(w*) = 0.

This gives exactly the data used by round9_q4 §1.2, with no product hypothesis:
- D̂_n : Ω → Ŝ ∖ B̂;
- D̂_n → L̂_S (the lift of L̃ to Ŝ);
- L̂_S(w*) = ŝ_0 and L̂_S(Ω) ⊂ Ê_1.

### 2.2 The homological step, with a small correction

I re-checked round9_q4 §1.4. One sentence is not justified as written, but the argument survives.
- **The sentence.** "C′ ∩ Ê′_1 ⊂ Exc, hence L′(Ω̄_ε) ∩ C′ = ∅." The strict transforms C′ and Ê′_1 may meet at a point of Exc, unless the resolution separates them. In that case the disc L′ passes through C′ at L′(w*).
- **Why the argument survives.**
  - The cycle is Z_n := D′_n(Ω̄_ε) − L′(Ω̄_ε) + A_n. Its pieces D′_n and A_n are disjoint from C′, and the disc L′ meets C′ at most at the isolated interior point w*, with local multiplicity μ ≥ 0.
  - By (Int), Z_n · C′ = −μ ≤ 0.
  - On the other hand, [Z_n] = Σ_j k_j[F_j] with all k_j > 0 (by (Neg) and (Pos), unchanged). Also F_j · C′ ≥ 0 for all j and > 0 for some j. So Z_n · C′ > 0.
  - This is still a contradiction. Alternatively, blow up further so that C′ and Ê′_1 are disjoint.

Hence **m = 0 in every stratum.** ∎

**Corollary X′\_all.** Theorem X′ (round9_q3) and all corollaries of X\* (round9_q4 §3: no junction crossing in a different coarse branch, no interior-MOV end except a same-branch twin) hold for non-product strata. In particular, R8-1 Remark 2, round9_q3 Remark 4 and round9_q4 open item (ii) are settled. The cited inputs remain those listed in §6.

---

## 3. Lemma 1SS: a walk excursion lies in one chart sheet (assuming (T4))

**Set-up.** This is the walk chain of Prop. K_w (round9_q4 §2.3), with r fixed. Let J be a transition point (a junction, or the endpoint Q_0).
- Take the chart ball B ⊂ Def(J) small, with q(B) ⊃ B(J, 3r). Here r is taken small enough for the following to hold.
  - The global irreducible components S_1, …, S_k of q^{-1}(closure V_0) ∩ B are the sheets at J.
  - q^{-1}(B_0) ∩ B is the union of the finitely many lifted branches at 0, and any two distinct ones meet only at 0.
- Let I = [s_1, s_2] be the excursion interval of the ray γ_n(s) = g_s X_n.
- γ_n is the projection of the T_g-ray γ̂_n.
- The canonical chart lift is γ̃_n := p_c ∘ γ̂_n on I. Here 𝔘_c is the component of the preimage in T_g of q(B) ∩ M_g that contains γ̂_n(I), and p_c : 𝔘_c → B° := B ∖ {∏ s_e = 0} is the holomorphic local biholomorphism with q ∘ p_c = (T_g → M_g). This is the T_g ↔ Def chart description, cited exactly as in R8-1 Step 2 and in the walk chain, Step 3.

**Lemma 1SS.** Assume (T4). Then:
- for each n, γ̃_n(I) lies in a single sheet S = S_{k(n)};
- after passing to a subsequence (already done in K_w to fix the combinatorial data), S is independent of n;
- S contains the entering lift β̃, and S contains the leaving lift β̃′ at a junction, or the terminal lift b̃ at the endpoint.

*Proof.*
1. **The ray lies in one T_g-sheet.**
   - X_n is a generic point of V_0, not an orbifold point, so exactly one component S_T of the preimage of V_0 passes through the lift X̂_n.
   - The vector v_n of Lemma PA is tangent to V_0, so its lift is tangent to S_T. q_n is its norming differential, possibly rotated by e^{−2iθ_n} as in Lemma NH. The Teichmüller geodesic of q_n is therefore tangent to the complex line spanned by v_n, which lies in T S_T.
   - By (T4), the whole ray γ̂_n lies in S_T.
2. **One global component in the chart.** Let W be the connected component of S_T ∩ 𝔘_c containing γ̂_n(I). It is a connected complex surface, and p_c|_W is a holomorphic immersion into A := q^{-1}(V_0) ∩ B°.
   - The components of A are A_l := S_l ∩ B°. Each is irreducible: an irreducible analytic set minus a proper analytic subset stays irreducible.
   - For w ∈ W and a small connected neighbourhood P of w in W, the analytic sets P ∩ p_c^{-1}(A_l) cover P. One of them has interior, hence equals P (identity theorem).
   - Let K(w) be the set of l with p_c(P) ⊂ A_l for some neighbourhood P of w. If l ∈ K(w) and w′ ∈ P, then P′ ∩ p_c^{-1}(A_l) has interior in P′, so l ∈ K(w′). So K is locally constant, hence constant on the connected W.
   - Thus p_c(W) ⊂ A_l for one l, and γ̃_n(I) ⊂ S_l.
3. **Entering lift.**
   - At the entry time s_1, γ̃_n(s_1) lies within ρ_n → 0 of a point z̃_n ∈ β̃ with d̄(q z̃_n, J) ∈ [r, 2r]. Pass to a limit z̃^1 ∈ β̃ ∖ {0}. Since S is closed in B, z̃^1 ∈ S.
   - Near z̃^1, q^{-1}(B_0) coincides with β̃, by the choice of B.
   - ∏ s_e vanishes at z̃^1. It vanishes identically on no local component of S at z̃^1, because dim(S ∩ {∏ s_e = 0}) ≤ 1. So S ∩ {∏ s_e = 0} is pure 1-dimensional at z̃^1 (Krull).
   - Hence S contains the germ of β̃ at z̃^1. Then S ⊃ β̃: the normalisation of the irreducible germ β̃ is a disc, and S ∩ β̃ is an analytic subset of it with interior.
4. **Leaving lift.**
   - At a junction, the exit point gives z̃^2 ∈ β̃′ ∖ {0} in the same way, so S ⊃ β̃′.
   - At the endpoint, z̃^∞ ∈ b̃ ∖ {0} is the limit of the nearest boundary lifts of γ̃_n(T_n) (K_w Step 4), so z̃^∞ ∈ S. Near z̃^∞ the only lifted branch is b̃, and the same argument gives S ⊃ b̃. ∎

**Remark.**
- Lemma 1SS replaces the coarse Lemma S′ / SS′ of round9_q3 and round9_q4. Those lemmas allowed the track's chart lift to change sheet at interior orbifold points of q^{-1}(V_0). That is where the same-branch twin (T) came from.
- (T4) excludes such sheet changes for the *canonical* lift of a Teichmüller ray. At an orbifold point the ray continues in the same T_g-sheet S_T, by uniqueness of geodesics.

---

## 4. Corollary IMOV\_all: no interior transitions, no interior-MOV endpoint, in any stratum

**Corollary IMOV\_all.** Assume (T4), the walk chain K_w, and Theorem X\*\_all. Let J be a transition point with entering lift β̃ (piece D) and leaving lift β̃′ (piece D′; at the endpoint, b̃ and E_b).
- (a) If J lies in the stratum of D or in the stratum of D′, then β̃′ = β̃ as sets. Then D′ = D, and x is intact and constant ≡ Y_0 along β̃′ = β̃.
- (b) Consequently, at the endpoint Q_0 is a **puncture of both D and E_b**. In particular the endpoint is MERGE or puncture-MOV, never interior-MOV, whatever the type of the stratum of Q_0.
- (c) Every junction at which the walk changes piece or lift is a puncture of both adjacent pieces. Junction crossings (R8-8 Prop. 3(c), Lemma J (J3)) and the turning twin (T) do not occur.

*Proof.*
- (a) Suppose J lies in the stratum of D, so J is an interior point of D.
  - By Lemma 1SS, S ⊃ β̃ ∪ β̃′.
  - Theorem X\*\_all, applied to (E, β, S) := (D, the coarse branch of β̃, S), gives S ∩ {∏ s_e = 0} = β̃ near 0.
  - β̃′ is an irreducible curve germ at 0 inside that set, so β̃′ = β̃.
  - The case of the stratum of D′ is symmetric.
  - Equal sets have equal patterns, so the pieces coincide. x is constant ≡ Y_0 along β̃ (STAY on the entering piece), hence along β̃′.
- (b) Suppose Q_0 lay in the stratum of D or of E_b. By (a), b̃ = β̃, so x would be intact and constant along b̃. This contradicts MERGE and MOV (K_w Step 4).
- (c) This follows from (a). ∎

**Consequence for MS10.**
- The instances of MS10 that the chain uses are walk-chain data: β̃, b̃, x as produced by K_w at a non-product point Q.
- If Q is an interior point of the piece of β̃ or of b̃, then β̃ = b̃ as sets. The transport families coincide, Ñ_b̃ = Ñ_β̃, so Y-persistence along β̃ **is** Y-persistence along b̃, and MS10's conclusion holds.
- At the endpoint this case does not even arise, by (b).
- The non-constancy hypothesis on Y is not needed for this part.
- **What remains of MS10 (walk-chain form):** Q a puncture of both adjacent pieces. These are exactly the persistent-twin junction (R8-8 Prop. 3(b), round9_q3 §5(b)) and the endpoint twin with MERGE or puncture-MOV (R8-8 Prop. 3, endpoint; round9_q3 §5(e)), at points of non-product strata.

---

## 5. Check of the chain

I re-read chain steps 1, 2(a)–(d) against the spliced proofs.

1. **Step 1** (Goal ⇐ MS8 + (Rig) + PR-A) is correct as stated.
   - MS10 has the hypothesis "Y non-constant". So if (Rig) holds and the problem's claim is true, MS10 is vacuously true.
   - Conversely, any configuration violating MS10 under (Rig) would contradict the claim. MS10 is therefore not easier than the problem in the hard case. A "counterexample to MS10" would be a counterexample to the problem, given (Rig).
2. **Steps 2(a)–(c)** use only the entries cited. I found no gap in their logic, but they inherit two cited inputs:
   - the K_w inputs (Lemma PA, Lemma NH, (Fl), Kerckhoff, Maskit, the T_g ↔ Def chart description, the collar lemma);
   - for Theorem X′ / X\*: (Res), (Neg), (Int), (RA).
3. **Step 2(d) and the wording of MS10.**
   - MS10 allows the joining paths γ_n to be *arbitrary* paths in q^{-1}(V_0) ∩ B. Such paths may change sheet at interior orbifold points.
   - The chain applies MS10 only to walk-chain data. There the paths are canonical lifts of Teichmüller ray segments, and by Lemma 1SS (under (T4)) they stay in one sheet.
   - This is not an error, since a stronger statement is asked than is needed. But it hides that the IMOV and turning-twin part of step (d) is settled by §4.
   - I propose the following replacement, which suffices for the chain verbatim.

> **MS10′.** As MS10, with "joined inside the chart" replaced by "β̃ and b̃ are the entering and leaving (or terminal) lifts of an excursion of the walk chain K_w at Q (so they lie in one sheet S by Lemma 1SS), and Q is a puncture of the pieces of both β̃ and b̃".

   By §4, MS10 for walk-chain data at points Q that are interior to one of the two pieces is **proved**, under (T4) and the inputs of §6. So MS10′ is all that remains of MS10 for the chain.
4. **Readings.**
   - The chain implicitly uses the reading (Sm) or (T4) for "smooth totally geodesic V_0" (round9_q3, round9_q5).
   - I use (T4) explicitly.
   - Without (T4), Lemma 1SS is unavailable, and the same-branch twin (T) of round9_q3 Cor. IM(c) returns for non-product strata (now with Theorem X\*\_all available).
5. **Remaining dependence.** As the task file says, the chain still needs entry 82 ((Rig)) in addition to MS10/MS10′.

---

## 6. What I re-derived and found not to be new; inputs used

- **Global tracking (not new).** My first approach transported the Prop.-K Teichmüller segments to time t:
  - (s,τ) ↦ H_τ(g_s X_n);
  - with a class function that lies, at fixed t, in a finite set S_t;
  - and is hence constant along the segment.

  This is exactly R8-5 Theorem A (with round9_q5's general-position refinement). It reduces the twin problem to the lift monodromy of the transport square. The monodromy is non-trivial only if 2-dimensional families of α-symmetric curves of V_τ (α ∈ Aut(J) moving x) accumulate at J (cases (A2), (B), (D3) of round9_q5). I have nothing new to add on these cases.
- **Frozen merging copy (not new).** By the generic-time Theorem N applied to the value function of the merging label instead of Y, an endpoint twin forces a component frozen at Y_0 at the relevant lift for all t. This is round9_q8 Lemma 1′.
- **Inputs used in §§2–4, cited from memory or taken from the run as stated:**
  - Lemma PA (PR-H §1), whose proof is local;
  - (Fl) (sketched in R8-1, cited);
  - (Prop) (Teichmüller discs are closed, with locally finite translates);
  - Wolpert's lemma and Abikoff's continuity;
  - the T_g ↔ Def(Q) chart description;
  - path lifting for properly discontinuous actions (Bredon);
  - (Res), (Neg), (Int), (Pos) of round9_q4;
  - Krull's theorem and Remmert's proper mapping theorem;
  - Proposition K_w (round9_q4, proved there modulo PR-H's inputs);
  - the reading (T4).

---

## 7. Summary

**Proved here** (given the inputs of §6):
1. **Theorem X\*\_all** (§2). For a piece E in **any** stratum and Q_0 ∈ E, every sheet of closure(V_0) at Q_0 containing a lift β̃ of a branch of E meets the boundary near Q_0 only in β̃. This settles the non-product extension of Theorems X, X′ and X\* left open in R8-1 Remark 2, round9_q3 Remark 4 and round9_q4 open item (ii).
2. A correction to round9_q4 §1.4. L′ may meet C′ on the exceptional set. The sign argument still gives the contradiction.
3. **Lemma 1SS** (§3, under (T4)). Each excursion of the walk chain lifts into one sheet, which contains the entering and leaving (or terminal) lifts.
4. **Corollary IMOV\_all** (§4).
   - In every stratum, the walk chain has no interior-MOV endpoint, no junction crossing and no turning twin (T).
   - Every genuine transition happens at a point that is a puncture of both adjacent pieces.
   - Hence MS10 holds, for the data the chain feeds it, whenever Q is an interior point of the piece of β̃ or of b̃.

**Not proved:**
- MS10 in full.
- MS10′, i.e. the twin case at points Q of non-product strata that are punctures of both pieces: the persistent twin (b) at junctions and the endpoint twin (e). No counterexample was found either.

**Open (precise):**
1. **MS10′** (§5). Equivalently, exclude for smooth totally geodesic V_0 the following situation:
   - a 2-dimensional family of α-symmetric curves of V_τ, τ ≠ 0, with α ∈ Aut(J) moving x;
   - accumulating at a point J that is a puncture of both pieces of a walk transition;
   - in one of the forms (A2) (Teichmüller curve of symmetric curves of V_0 with cusp J, or a symmetric sheet), (B) (an α-fixed boundary branch, including (B-pure)), or (D3) of round9_q5.

   Alternatively, prove (Lock) of the twin pair in these cases.
2. **Entry 82 (Rig)** for every admissible family. This is still needed by the chain after MS10′.
3. The reading (T4). It is needed for Lemma 1SS. Without it, the turning twin (T) at non-product points is open again; Theorem X\*\_all reduces it to a same-coarse-branch twin.
4. The inputs inherited from Proposition K and PR-H, listed in §6.



### round10_q10 (verbatim): chain check of Proposition K_w, repairs (R-a)–(R-d), Lemma S̃′ (canonical lifts stay in one upstairs component)
**Plan/status.** This is a chain check of Proposition K_w and Lemma S′ (round9_q4 §2). I check every step against points 1–7 of the brief.

**Verdict in brief: REPAIRED.** Proposition K_w holds in the form the chain uses, but only after four repairs:
- (R-a) the choice of η and ρ_* needs three extra small conditions;
- (R-b) Step 3: the chart lift must be the *canonical* lift through augmented Teichmüller space, not an arbitrary Bredon lift. With an arbitrary lift, the label x can change at orbifold points;
- (R-c) Step 5, upstairs: an arbitrary lifted path need *not* lie in a single irreducible component of q^{-1}(closure V_0). The canonical lift does lie in one, because it lies on the image of a Teichmüller disc. This also needs r small enough that distinct lifted branches meet only at the chart centre;
- (R-d) the chain's combinatorics are not uniform in n. The number of excursions can grow with n. A single chain with all the properties is obtained by keeping only "recurrent" transition types.

The inputs are taken as given, as in the text: Lemma PA, Lemma NH, Kerckhoff, Maskit, the plumbing/Kuranishi charts and the collar lemma. Below, "cited" means cited from memory.

---

## 0. Conventions made explicit

- **Pieces.** B_0 = closure(V_0) ∖ V_0 is the intersection of the irreducible 2-dimensional analytic set closure(V_0) with ∂M̄_g. Locally, ∂M̄_g is the zero set of the Aut-invariant function N = ∏_{g∈Aut(J)} g^*(∏_e s_e), which descends to the coarse chart. Hence B_0 has pure dimension 1. A *piece* is a 1-dimensional irreducible component of B_0 ∩ Δ_G, for some stratum Δ_G.
  - closure(D) ∖ D consists of punctures of D, which lie in Σ.
  - So K_D ⊂ D, the K_D are compact, and they are pairwise disjoint: common points of two closures are junctions.
- **Vertices of a piece.** For the strata Δ_G of the pieces (which may be quotient strata), "vertex of D" means an orbit of vertices under the monodromy of D. "Constant vertex" and "value class" are monodromy-invariant, so nothing below changes.
- **The metric d.** Σ is finite. I take a metric d on M̄_g which, near each J ∈ Σ, is the quotient of an Aut(J)-invariant Euclidean metric on Def(J). Then small metric balls B(J,ρ) are images of round Aut-invariant balls B̃(J,ρ) ⊂ Def(J). For small ρ these are Milnor balls for the germs (X,J) downstairs and (q^{-1}X, 0) upstairs. (Milnor's conic structure theorem, cited.)

## 1. Step 0 (point 1): correct

Let s_n ≤ T_n. Since (X_n, q_n) is a generating pair and V_0 is totally geodesic, γ_n(s_n) ∈ V_0, so every limit point lies in closure(V_0).
- If s_n stays bounded: Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n}(Γ-curves) → 0, since X_n → P ∈ Δ_Γ.
- If s_n → ∞: Lemma NH(1) gives Ext(c_n) ≤ e^{-2s_n}/m → 0.
- In both cases some curve has Ext → 0. By Maskit's comparison its hyperbolic length → 0, so the limit lies in ∂M̄_g.

Hence every limit point lies in closure(V_0) ∩ ∂M̄_g = B_0. Here V_0 is closed in M_g (an algebraic subvariety), so closure(V_0) ∩ M_g = V_0.

Uniformity follows by contradiction. If ρ_n ↛ 0, choose s_n ≤ T_n with dist(γ_n(s_n), B_0) ≥ ε along a subsequence. A further subsequence converges, by compactness of M̄_g, to a point of B_0, which is a contradiction. **Verified.**

## 2. Step 1 (point 2, first half): correct

- **T_n is finite.** This is Lemma NH(2), an input. So [0,T_n] is compact and γ_n|[0,T_n] is uniformly continuous into (M̄_g, d).
- **Finitely many excursions.** γ_n(0) = X_n is near P, and P ∉ B(J,3r). So every excursion is entered from the sphere d(·,J) = 2r and must reach d < r. Each excursion therefore contains a sub-interval crossing the shell r ≤ d ≤ 2r. By uniform continuity such a crossing takes time ≥ τ_n > 0. The balls B(J,3r) are disjoint, so excursions at different J are disjoint, and there are at most T_n/τ_n + 1 excursions.
- **Times outside the excursions are travel times.** Suppose γ_n(s) ∈ B(J,r). Then the maximal interval of times in B(J,2r) containing s contains a time in B(J,r), so it is an excursion. Hence a time outside all excursions lies outside ⋃_J B(J,r).
- **The piece at a travel time is unique.** Let s be a travel time and z ∈ B_0 with d(z, γ_n(s)) ≤ ρ_n < r/2. Then d(z,J) > r/2 for all J, so z ∈ K_D for some D, since closure(D) ∖ ⋃B(J,r/2) = K_D. Two such points are within 2ρ_n < 4ρ_* of each other, so they lie in the same K_D. By continuity the same holds on whole travel intervals, so D is locally constant there.
- **First piece.** P ∉ Σ, so the first travel is along the piece D^1 ∋ P, and D^1 ⊂ ∂V_0.

**Verified.** The claim that the walk ends inside an excursion is Step 2.

## 3. Step 2 (points 2 and 3): correct after repair (R-a)

**Repair (R-a).** Add three conditions, all depending only on r:
- **(a′)** Shrink ρ_* if necessary so that the closed ρ_*-neighbourhood N_D of each K_D lies in the open set O_{G_D} of points whose dual graph is a contraction of G_D. This is possible because K_D is compact and K_D ⊂ Δ_{G_D} ⊂ O_{G_D}.
  - Choose ρ_* also below the Lebesgue number of a finite cover of K_D by plumbing charts.
  - Then for z ∈ K_D and X ∈ M_g with d(X,z) ≤ ρ_*, X lies in a chart at z. The node curves of z are well defined on X, up to Aut(z).
  - The non-node curves have hyperbolic length ≥ ℓ_0(r) > 0, by continuity of the hyperbolic metric in plumbing families (Wolpert/Masur, cited) and compactness of N_D.
  - Hence Ext_X ≥ ℓ_0²/(2π(2g−2)) for non-node curves, and (a) holds with δ below this bound. As stated, (a) silently needs this shrinking: points within the original ρ_* of K_D can lie near deeper strata.
- **(b0)** 2η < d(Y_0, ∂M̄_{g_i,n_i}).
- **(b1)** 2η < min{ d(σY_0, Y_0) : σ ∈ S_{n_i}, σY_0 ≠ Y_0 }. This is the labelled versus unlabelled issue: the stopping rule uses labelled distance, while "≅ Y_0" is unlabelled.

**Check of the step.** Let s ≤ T_n be a travel time on D, and z_s ∈ K_D with d(z_s, γ_n(s)) ≤ ρ_n.
- Since s ≤ T_n, every curve of ∂Σ_i has Ext ≤ δ at γ_n(s). By (a)/(a′) they are node curves of z_s.
- Hence ψ(z_s) ∈ M̄_{g_i,n_i} is defined.
- **Uniform continuity of ψ.** ψ depends on (X, isotopy class of Σ_i). It is continuous near pinched points, and the dependence on the auxiliary pants decomposition disappears in the limit ℓ(∂Σ_i) → 0. There are finitely many Mod-classes of pairs (z, subsurface bounded by node curves of z), and the z range over the compact set ⋃K_D. So ψ is uniformly continuous there, and d(ψ(γ_n(s)), ψ(z_s)) = o(1) uniformly in s.
- So d(ψ(z_s), Y_0) ≤ η + o(1) < 2η. By (b0), ψ(z_s) is smooth: Σ_i contains no node curve of z_s, and the Σ_i-side is a single vertex c of D.
- By (b), c is a constant vertex of D whose value class is [Y_0]. By (b1), and continuity of the labelled value along the travel, its labelled value is Y_0.
- Then Ext_{γ_n(s)}(∂Σ_i) = o(1), because these are node curves of z_s and d → 0 uniformly on the compact set N_D. Also d(ψ(γ_n(s)), Y_0) = o(1).
- So for n large, neither stopping condition holds at a travel time. T_n lies in an excursion, at some Q ∈ Σ.

**Verified with (R-a).**

## 4. Step 3 (point 4): gap for an arbitrary lift; repaired by the canonical lift (R-b)

**The gap.** Lifting through Def(J) → Def(J)/Aut(J) (Bredon, cited: paths lift through quotients by compact groups) is not unique. At a time s where γ_n(s) = q(ỹ) with Stab(ỹ) ≠ 1, a lift may continue as h·(lift), h ∈ Stab(ỹ). Then:
- h acts on the fibre curve as an automorphism and permutes the vanishing cycles, e ↦ h(e);
- after the switch, the T_g-marked curves ∂Σ_i correspond to the edges at h(x), not at x.

So with an arbitrary Bredon lift the chart label x is **not** well defined. The text's sentence "the T_g-marking along γ_n is compatible with the chart" is true only for a specific lift, which it does not specify.

**Repair (R-b).** The facts below are cited from memory (Abikoff, Bers; Hubbard–Koch's analytic construction of M̄_g; Wolpert).
- Let J̃ be a point of augmented Teichmüller space T̄_g over J.
- Stab(J̃) ⊂ Mod_g sits in an exact sequence 1 → Tw → Stab(J̃) → Aut(J) → 1, where Tw ≅ Z^{E(J)} is generated by the Dehn twists about the node curves α_e.
- There is a Stab(J̃)-invariant neighbourhood U of J̃, precisely invariant (gU ∩ U = ∅ for g ∉ Stab(J̃)), with:
  - U/Tw ≅ Def(J) (the plumbing/Kuranishi chart);
  - U/Stab(J̃) ≅ Def(J)/Aut(J), a neighbourhood of J in M̄_g;
  - U° := U ∩ T_g → Def(J)° a covering. Tw is torsion-free and acts properly, hence freely.

Construction of the canonical lift:
- The ray γ_n is given in T_g from the start, as the Teichmüller geodesic of the marked (X̃_n, q_n). This is the path marking.
- During an excursion at J the T_g-path is connected and lies in the preimage of B(J,2r) ⊂ B(J,3r) ⊂ image of U. That preimage is the disjoint union of the translates gU, so the path lies in a single translate. Replace J̃ by gJ̃ (relabel the marking).
- Define γ̃_n := image of the T_g-path under U → U/Tw = Def(J). This is a continuous lift into Def(J)°, determined up to one global element of Aut(J). No choice is made at orbifold points.

Consequences:
- Each node curve α_e of J̃ is a fixed marked curve on S_g. It is pinched exactly where s_e = 0, and it is Tw-invariant.
- The components of S_g ∖ ⋃_e α_e are marked subsurfaces Σ_y, one for each vertex y of J.

**Entry.** Let s be the entry time, a travel time on D. Let z_s be as in Step 2, and z̃_s the lift of z_s close to γ̃_n(s); it lies on a lifted branch β̃ of D at J. The node curves of z_s, in the marking of U, are the α_e with s_e(z̃_s) = 0. The Σ_i-side is the constant vertex c ≅ Y_0, and it corresponds to a connected subgraph S_c of J.
- **S_c is a single vertex x with no internal edge.** Suppose S_c had an edge f. Then s_f ≠ 0 along β̃ ∖ {0}, but s_f → 0 at 0. So the hyperbolic length of α_f inside the c-component would tend to 0 (continuity of hyperbolic metrics on plumbing families, cited). That component is constant, equal to Y_0, and α_f is essential and non-peripheral in it, so its length is the constant ℓ_{Y_0}(α_f) > 0. Contradiction.
- Hence c = {x}, all edges of J at x are pinched along β̃, and **Σ_i = Σ_x as marked subsurfaces**, with ∂Σ_i = {α_e : e at x}.

**Persistence.** Σ_i (path marking) and Σ_x (marking of U) are both fixed marked subsurfaces, and the path stays in U. So the identity Σ_i = Σ_x holds throughout the excursion.

**Exit.** Step 2 on D′ gives c′ = {x′} along the lifted branch β̃′ through z̃_{s′}, with Σ_i = Σ_{x′}. Then Σ_x = Σ_{x′}, so x′ = x.
- Remark: equality of the boundary-curve sets alone would not suffice. If J has two vertices joined by all its edges, x and x′ have the same edge set. The subsurface identity is what fixes the label.

**Verified with (R-b).** Orbifold points cause no trouble for the canonical lift, because it is never produced by lifting through T_g → M_g. It is the given T_g-path, pushed down by an honest covering.

## 5. Step 4 (point 5): correct, given (R-b)

- Fix (r, δ, η). Endpoint types (Q, D, Aut-orbit of (β̃, x)) form a finite set. Pass to a subsequence of n on which the type is constant, and normalise lifts by the global Aut(J) element.
- Let z̃_n be a lift of a boundary point within ρ_n of γ_n(T_n), chosen near γ̃_n(T_n). A subsequence converges to z̃^∞ ∈ q^{-1}(B_0) ∩ closure(B̃(Q,2r)).
- **F_x(0) = Y_0.** On L_x := {s_e = 0 for all e at x} the x-component F_x is holomorphic, and β̃ ⊂ L_x with F_x ≡ Y_0 on β̃ ∖ {0}.
- **z̃^∞ ≠ 0.** Suppose z̃^∞ = 0. Then γ̃_n(T_n) → 0, so Ext(α_e) → 0 for every e at x, and ψ(γ_n(T_n)) → ψ(J̃) = F_x(0) = Y_0. Both use Σ_i = Σ_x from (R-b). For large n both stopping conditions then fail at T_n, a contradiction.
- So z̃^∞ ∈ b̃ ∖ {0} for a lifted branch b̃ at Q. In the chosen ball, B_0 ∩ B(Q,3r) is the union of the branches. Pass to a further subsequence on which one stopping condition holds for all n.
  - **Ext(α_e) = δ for some e at x.** If s_e(z̃^∞) = 0, then Ext_{γ_n(T_n)}(α_e) → 0 (Maskit), contradicting = δ. So s_e(z̃^∞) ≠ 0. Since b̃ ∖ {0} lies in one stratum, e is unpinched on all of b̃ ∖ {0}: **MERGE**.
  - **d(ψ, Y_0) = η.** If some edge at x is unpinched along b̃, we are in MERGE. Otherwise b̃ ⊂ L_x, and continuity of ψ with Σ_i = Σ_x gives d(F_x(z̃^∞), Y_0) = η > 0, while F_x(0) = Y_0. Here F_x(z̃^∞) is a smooth curve because all edges at x are pinched. So F_x is non-constant on b̃: **MOV**.
- In particular b̃ ≠ β̃, as it must be.

**Verified.**

## 6. Lemma S′ and Step 5 (point 6)

### 6.1 The coarse Lemma S′ is correct
- **γ_n avoids Z.** V_0 is smooth, so V_0 ⊂ Reg X and V_0 ∩ W = (X ∖ Z) ∩ W.
- **Local sheets.** Each irreducible germ X_k has connected regular part in a Milnor ball. Its normalisation over the ball is connected, and removing a proper analytic subset keeps it connected. Distinct X_k meet inside Sing X ⊂ Z. So the components of V_0 ∩ W are the X_k ∩ W ∖ Z.
- **One sheet along a subsequence.** Each γ_n is connected, so it lies in one X_k ∩ W ∖ Z. There are finitely many, so pass to a subsequence with k fixed.
- **Limit points.** X_k ∩ W is closed in W, so z^1 ∈ X_k; note z^1 ∈ W, since it is at distance 2r from Q.
- **Near z^1.** N|_{X_k} is not identically zero on any local component of X_k at z^1, since X_k is the closure of X_k ∖ Z ⊂ M_g. So X_k ∩ ∂M̄_g is empty or of pure dimension 1 at z^1 (active lemma), and it contains z^1.
- Near z^1, B_0 = β, a smooth curve (W ∩ Σ = {Q}). So X_k ⊃ a neighbourhood of z^1 in β. β ∩ W is irreducible, so X_k ⊃ β ∩ W. The same holds for β′.

**Verified** (coarse statement: β and β′ lie in a common sheet X_k of (X, J)).

### 6.2 Upstairs: an arbitrary lift can change component
Here is a local model of reflection type. Let q(u,v_1,v_2) = (u², v_1, v_2) be the quotient by the reflection u ↦ −u. The smooth coarse surface V = {w = v_2²} (w = u²) has preimage {u = v_2} ∪ {u = −v_2}: two smooth sheets exchanged by the reflection, crossing along {u = v_2 = 0} inside the fixed hyperplane.

If V_0 passes through such a point of the reflection locus inside Def(J)°, then q^{-1}(V_0) is locally reducible there. A Bredon lift may arrive along one sheet and leave along the other. So for an **arbitrary** lift, γ̃_n need **not** lie in a single irreducible component of q^{-1}(closure V_0) ∩ B̃. The coarse conclusion of 6.1 then gives only the weaker statement:

> **(W)** some component of q^{-1}(X_k) contains β̃, and the same component contains g·β̃′ for some g ∈ Aut(J).

Proof of (W): the components of q^{-1}(X_k) are permuted transitively by Aut(J). Two distinct orbits of components would both map onto X_k, and a generic fibre is a single Aut-orbit, which forces them to share a component.

### 6.3 Repair (R-c): the canonical lift stays in one component
**Lemma S̃′.** Choose r so small that, in addition:
- B̃(J,3r) is a Milnor ball for (X̃ := q^{-1}X, 0). The irreducible components X̃_1, …, X̃_p of X̃ ∩ B̃ are then representatives of the germ components (cited, conic structure).
- Distinct lifted branches of q^{-1}(B_0) meet only at 0 in B̃, and each lifted branch minus 0 is smooth. There are finitely many pairs of distinct irreducible curve germs at 0, and each pair meets only at 0 in a small enough ball; Puiseux parametrisations give smoothness.

Let the γ̃_n be canonical lifts (R-b) of transition paths whose endpoints converge to z̃^1 ∈ β̃ ∖ {0} and z̃^2 ∈ β̃′ ∖ {0}. Then some X̃_l contains both β̃ and β̃′.

*Proof.*
1. **The path lies on a holomorphic curve in q^{-1}(V_0).** Let F: H → T_g be the Teichmüller disc of (X̃_n, q_n). Since V_0 is totally geodesic and (X_n,q_n) is generating, F(H) lies over V_0. Let R be the connected component of F^{-1}(gU) containing the parameters of the excursion; R is a connected Riemann surface. Put f := (U° → Def(J)°) ∘ F|_R. Then f is holomorphic, f(R) ⊂ q^{-1}(V_0) ∩ B̃, and γ̃_n ⊂ f(R).
2. **f(R) lies in one component.** Each f^{-1}(X̃_l) is an analytic subset of R, and their finite union is R. So one of them has interior, and by the identity theorem it is all of R. Hence γ̃_n ⊂ X̃_{l(n)}, even if f(R) passes through crossing points such as those in 6.2: a smooth connected curve germ cannot change sheets.
3. **Conclusion.** Pass to a subsequence with l(n) = l. X̃_l is closed in B̃, so z̃^1, z̃^2 ∈ X̃_l. X̃_l is irreducible of dimension 2, so X̃_l ∩ {∏ s_e = 0} is nowhere dense in it and has pure dimension 1 at z̃^1. Near z̃^1, q^{-1}(B_0) = β̃, a smooth curve, by the choice of r. So X̃_l contains an open piece of β̃, hence all of β̃. The same argument gives β̃′. ∎

**Step 5 then holds upstairs for every transition, and at the endpoint.** At the endpoint, z̃^2 = z̃^∞ ∈ b̃ ∖ {0}.

## 7. Point 7: dependence on (r, δ, η, n), and existence of one chain

**Order of choices.**
- First r: all conditions of §2.3, the Milnor conditions up- and downstairs, and the branch-separation condition of 6.3.
- Then δ, η, depending on r: (a), (a′), (b), (b0), (b1).
- Then n_0 such that, for n ≥ n_0, ρ_n < min(ρ_*, r/2) and the o(1) terms of Step 2 are below δ and η.

**The gap.** The text implicitly treats the chain as fixed while n → ∞, both in Step 4 and in Step 5 ("over the subsequence these points converge"). But T_n → ∞, and the number of excursions in [0,T_n] can be unbounded in n: the walk may loop around B_0. So the chains for different n need not agree, and "the same transition along a subsequence" is not automatic.

**Repair (R-d).**
- A *transition type* is an Aut(J)-orbit of (J, β̃, β̃′, x); an *endpoint type* is an orbit of (Q, D, β̃, x). Both sets are finite.
- Call a type recurrent if it occurs in the walks of infinitely many n. Let N ≥ n_0 exceed the last n at which any non-recurrent type occurs.
- Fix any n ≥ N and take its walk chain. Every transition of this chain has a recurrent type τ.
  - Along the infinite set of n′ where τ occurs, the corresponding excursions are canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃(J,2r). Their entry and exit boundary points lie at distance ≈ 2r from 0.
  - A subsequence converges to points of β̃ ∖ {0} and β̃′ ∖ {0}. This is the sequence of paths the chain form requires, and Lemma S̃′ applies to it.
- The terminal type τ_end of the chosen n is also recurrent. Step 4, run along the n′ of type τ_end, supplies b̃, the MERGE/MOV dichotomy and the convergent terminal paths.

So a single finite chain with all required properties exists. The only caveat: the witnessing sequences of paths at different transitions come from different subsequences of walks, not from one common sequence.
- If the downstream argument needs one common sequence n′ for all transitions at once, this is **not** established: the chain combinatorics need not stabilise.
- As far as I can see, the per-transition form listed in the brief needs only per-transition sequences, and that is what is proved.

## 8. Final verdict

**Proved, with repairs (R-a)–(R-d), modulo the cited inputs** (Lemma PA, Lemma NH, Kerckhoff, Maskit, the T̄_g/Def chart description, collar and continuity of hyperbolic metrics in plumbing families, local analytic geometry). There is a chain:
- pieces D^1 ∋ P (D^1 ⊂ ∂V_0), D^2, …, D^k; transition points J_1, …, J_{k−1}; an endpoint Q_0;
- at each J_m: lifts β̃_m, β̃′_m and a single chart vertex x_m, which is the constant vertex ≅ Y_0 (labelled, = Y_0) of D^m along β̃_m and of D^{m+1} along β̃′_m;
- witnessing sequences of canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃, with endpoints converging to points of β̃_m ∖ {0} and β̃′_m ∖ {0};
- β̃_m and β̃′_m lie in a common irreducible component of q^{-1}(closure V_0) at 0 (upstairs, by Lemma S̃′), and hence in a common sheet downstairs;
- at Q_0, the entering lift β̃ with vertex x and the terminal lifted branch b̃ are joined in the same way, and along b̃ the vertex x is MERGED or MOVING.

**What the original text gets wrong or leaves implicit.**
- (R-a): three extra smallness conditions.
- (R-b): the chart label x is ill-defined for arbitrary Bredon lifts through orbifold points. The canonical lift through augmented Teichmüller space fixes this.
- (R-c): the upstairs same-component claim is false for arbitrary lifts (reflection model). For them only the weaker (W) holds. It is true for the canonical lift, because that lift lies on a Teichmüller disc.
- (R-d): chain combinatorics depend on n. Fixed by recurrent types; the witnessing sequences are per transition.

**Open / not established.**
- A single subsequence n′ witnessing all transitions of one chain simultaneously.
- Anything about the cited inputs themselves (in particular Lemma NH and the T̄_g/Def(J) chart description, which I used in the form stated in §4).

Overall result: **repaired**.


### round10_q3 (verbatim): logical status, Gap A and Gap B with repairs, Lemma B1, component-wise chain, Lemma 3.1, Prop. 3.2, local merging model
# round10_q3 — attempt on MS10

**Plan/status line.** MS10 is NOT proved here, and no counterexample is given. This is a PARTIAL answer. The file contains:
- §1: the logical status of MS10. A counterexample to MS10 is the same thing as a counterexample to the problem, for families satisfying (Rig). So the "counterexample" option of the task cannot be easier than disproving the problem.
- §2: an audit of the chain MS10 ⇒ MS8 ⇒ goal. I found **two places where the derivation is incomplete, both at non-product pieces**:
  - (Gap A) the walk chain's special set Σ misses the points where two lifts of a non-product piece cross. At such a point the tracked label can switch sheets in the middle of a "travel" interval.
  - (Gap B) under the coarse reading (R2), a transport family Ñ need **not** be irreducible. The claim in R7-3 Lemma 2, step 2, that it is irreducible is false in general (explicit local model below). As a result, MS10's notion of "Y-persistent along β̃", which quantifies over every point of Ñ, can fail along a non-product piece even when no twin jump occurs. So the induction claim (b) of the chain is false as worded in such configurations.
  
  I give repairs for both: enlarge Σ, and use a component-wise notion of persistence. After the repairs the chain reduces the problem to a component-wise variant MS10′ of MS10, at points of non-product strata.
- §3: an attempt on MS10/MS10′, and an explicit local model (coarse-smooth, totally-geodesic-compatible at t = 0) of the interior mechanism that a failure needs. The model shows exactly what a proof must exclude.
- §4: proved / not proved / open.

Throughout: the readings (R1), (R2) with H_0 = id, the notation of the task file, and (Rig). Facts cited from memory are marked as such.

---

## 1. The logical status of MS10

**Proposition 1.1.** Fix an admissible configuration: V_0, a family V_t satisfying the problem's hypotheses in the readings (R1), (R2), Γ, i with dim M_{g_i,n_i} > 0, and (Rig).
- (a) If the problem's conclusion Y_t ≡ Y_0 holds for this family, then MS10 holds for every choice of the data (Q, B, β̃, b̃, γ_n, x) in this family, vacuously.
- (b) Any counterexample to MS10 is a family satisfying all the problem's hypotheses, plus (Rig), with Y non-constant. That is, it is a counterexample to the problem.
- (c) Assume the chain's derivation (MS10 + (Rig) ⇒ goal) is correct, after the repairs of §2. Then, for the class of families satisfying (Rig), "MS10 holds for all configurations" is equivalent to "the problem's claim holds for all families".

*Proof.* MS10 has the hypothesis "t ↦ Y_t is non-constant". (a): that hypothesis fails, so the implication holds. (b): a counterexample satisfies all the hypotheses of MS10, which include all the problem's hypotheses, (Rig), and the non-constancy of Y. (c): one direction is (a), the other is the chain. ∎

**Consequences.**
- The task's option "give an explicit counterexample to MS10" is exactly as hard as disproving the problem for (Rig)-families. In particular it needs an actual deformable smooth totally geodesic surface, and none is known (round9_q8 §4).
- MS10 is not a reduction to a *weaker* statement. It is a *localisation*: it says where, in a hypothetical counterexample, the contradiction must be found. A proof of MS10 has to exclude a configuration that, by (a), cannot exist at all if the problem is true. So a proof must derive a contradiction from data that includes "Y non-constant". It cannot be a pure t = 0 statement about V_0.
- Remark (repeated from the task file, re-checked): MS10 without the hypothesis "Y non-constant" is false, because Prop K's endpoint violates its conclusion.

---

## 2. Audit of the chain (MS10 ⇒ MS8 ⇒ goal)

Notation. For a stable graph G, Δ_G ≅ (∏_w M_w)/Aut(G) (standard, cited from memory; Aut(G) acts by permuting factors and relabelling marked points), with quotient map ξ = ξ_G. For a piece D ⊂ Δ_G at t = 0, ξ^{-1}(D) = E_1 ∪ … ∪ E_r, irreducible curves permuted transitively by Aut(G). κ(D) is the component of ℬ_G containing H(D × Δ) (round9_q7 Lemma T). A *lifted family component* of D is an irreducible component 𝒲̃ of (ξ × id)^{-1}(κ(D)) ⊂ ∏_w M_w × Δ. Persistence of a label is a property of a lifted family component *together with the labelling of ∏_w M_w* (round9_q7 Lemma S(c)). It is not a property of the coarse κ(D). For product-type G, ξ is injective, so the two notions coincide. For non-product G they do not, and the two gaps below come from this.

### 2.1 Gap A: sheet switching in the middle of a travel interval

**The step concerned.** Chain step (b): "persistence passes along D^{m+1} to β̃_{m+1}, because persistence is a property of the whole component κ(D^{m+1}) (Lemma S(c)) and the chart vertex is c_{m+1} on both ends (K_w Step 3)."

**What is missing.** Along a travel interval of the walk chain (round9_q4 §2.3), the track stays near K_D, and its marking gives a continuous lift to ∏_w M̄_w near ξ^{-1}(D). The tracked subsurface Σ_i corresponds to one fixed factor c of ∏_w M_w along the whole interval, by continuity. But the lift can pass from one lifted curve E_k to another one, σE_k (σ ∈ Aut(G)), at a point z ∈ E_k ∩ σE_k. Then:
- before z, the track's label is c on E_k;
- after z, the label is still the factor c, but now on σE_k. In terms of E_k, the factor c of σE_k is the factor σ^{-1}c of E_k.

So the label the track follows after z is the twin σ^{-1}c, not c. The special set Σ of the walk chain consists of junctions, singular points of B_0, punctures, and points where a non-constant vertex has value [Y_0]. It does **not** contain such crossing points in general.

**Local model showing that such a point need not be in Σ (proved, local).** Take G non-product with σ ∈ Aut(G) exchanging two vertices c, c′ = σc of type (g_i, n_i), and exchanging two further vertices m, m′ of the same type. Assume near the point z the other factors are σ-fixed. Use local coordinates a on M_m and b on M_{m′} centred at z, with σ(a, b) = (b, a). Let
- E_k := {z_c = z_{c′} = Y_0, (a, b) = (s, 2s), other coordinates fixed}, so on E_k both c and c′ are constant with value Y_0, and m, m′ move;
- σE_k = {z_c = z_{c′} = Y_0, (a, b) = (2s, s), …}.

They meet at z (s = 0), which is fixed by σ. In the quotient coordinates (u, v) = (a + b, ab), E_k maps to u = 3s, v = 2s² = 2u²/9, a smooth curve. So, if Stab(z) = ⟨σ⟩, D = ξ(E_k) is **smooth** at ξ(z). ξ(z) is not a junction, not a puncture, not singular on B_0, and the non-constant vertices m, m′ have value z_m = z_{m′} there, which need not be ≅ Y_0. So ξ(z) ∉ Σ.

At the family level, let 𝒲̃ ⊃ E_k × {0} be the lifted family component on which c is persistent. Then σ𝒲̃ ⊃ σE_k × {0}, and on σ𝒲̃ the factor c carries the value function of c′ on 𝒲̃. If c′ is a "persistent twin" with [φ_{c′}] ≢ [Y] (round9_q3 §5(b)), the track's label is no longer persistent after z. Nothing in the chain's step (b) detects this.

**Repair (proved, given the walk-chain inputs).** For each piece D let R(D) be the set of P ∈ D such that, near ξ^{-1}(P), the set ξ^{-1}(D) is not a disjoint union of smooth arcs each mapped homeomorphically onto a neighbourhood of P in D.
- R(D) is finite. It consists of images of singular points of the compact curve ξ̄^{-1}(closure D) ⊂ ∏ M̄_w, and of ramification points of the finite maps from the normalisations of its components to the normalisation of closure(D). Both sets are finite.
- Replace Σ by Σ ∪ ⋃_D R(D) in round9_q4 §2.3, before choosing r. Everything there goes through unchanged: Σ is still finite.
- Then, over a neighbourhood of K_D, ξ^{-1}(D) is a disjoint union of compact arcs at positive mutual distance. By continuity, the track's lift stays near one arc of one lifted curve E for the whole travel interval, and its label is a fixed factor c. (This is a "routine marking detail" of the same kind as K_w Step 3. I use it in the same way.)
- The new transition points P ∈ R(D) are interior points of D. The track arrives along a lift β̃ and leaves along a lift b̃ of a branch of D at P, possibly of the same coarse branch, joined inside the chart (K_w Steps 3 and 5 apply verbatim). If the two lifts lie on different lifted curves, ξ is not injective, so Δ_G is non-product. Then this is exactly an MS10 configuration. MS10 explicitly allows "lifts of the same coarse branch", so it already covers these points. If both lifts lie on the same E_k at a ramification point, the label is unchanged and nothing is needed.

So Gap A is a gap in the walk-chain bookkeeping. It does not change the missing statement, but **the list of points where MS10 is invoked must include R(D) for every non-product piece D of the chain.**

### 2.2 Gap B: transport families can be reducible, and then "persistent along β̃" is the wrong notion

**The claim concerned.** R7-3 Lemma 2, step 2: "Ñ is a connected topological 4-manifold, being a cover of a punctured disc times a disc. Hence Ñ is irreducible." This is used, for instance, in round9_q2 Lemma 2 step 5 and Proposition 4 step 4. MS10's definition of "x is Y-persistent along b̃" quantifies over *every* point of Ñ_b̃.

**Claim B0.** Under the coarse reading (R2), q^{-1}(N) → N is a finite quotient map, but *not* a covering, wherever stabilisers jump. Ñ can then be reducible, and the step-2 claim is false.

**Local model (proved, local).** Let D be a piece in a non-product stratum. Suppose every curve of D has an automorphism inducing σ ∈ Aut(G), where σ exchanges two vertices c, c′ of type (g_i, n_i) that are both constant on D with value Y_0. Suppose also that the lifted curve E is fixed pointwise by σ. Near a generic point P of D, use coordinates on the stratum locus of Def(P): e along E, p on the c-factor, p′ on the c′-factor (with Y_0 ↔ 0), and w for the remaining coordinates. Here σ acts by p ↔ p′, and E = {p = p′ = 0, w = 0}. Choose the deformation
- E_t^+ := {p = t, p′ = −t, w = 0} (c has value "Y_t" ↔ t, c′ has value "φ(t)" ↔ −t), and E_t^− := σE_t^+ = {p = −t, p′ = t, w = 0}.

The coarse coordinates are (e, s, y²) with s = p + p′ and y = p − p′. The coarse transported piece is {s = 0, y² = 4t², w = 0}: a smooth, topologically trivial family of smooth curves, with H_t(e, 0, 0) = (e, 0, 4t²). Its preimage is
 q^{-1}(N) = {p = t, p′ = −t, w = 0} ∪ {p = −t, p′ = t, w = 0} =: G_+ ∪ G_−.
This is connected, since the two pieces meet along {t = 0} = E. It is reducible. It is not a manifold along E × {0}. So Ñ = G_+ ∪ G_−. The same picture occurs along the lifted branch β̃ at a puncture J of D, at generic points of β̃.

In this model:
- on G_+ the chart label x (↔ c) has F_x ≅ Y_t, and on G_− it has F_x ≅ φ(t);
- for the twin label αx (↔ c′, α ∈ Aut(J) realising σ and fixing β̃ pointwise), the roles are exchanged.

So **neither x nor αx is Y-persistent along β̃ in MS10's sense**, although every point of the transported piece carries a Y_t-copy, D ∈ 𝒩, and no twin jump has happened anywhere. The model is consistent with (R1), (R2), Lemma U (D = K_W × {c_D}, with c_D = (Y_t, φ(t)) on G_+) and (Rig), which constrains only non-constant vertices. Whether it occurs for an actual totally geodesic V_0 is not known. Covering constructions, whose boundary curves carry deck automorphisms permuting components, are the natural candidates.

**Consequence for the chain.** If some D^{m+1} of the chain is a piece of this kind, the induction claim (b), "x_{m+1} is Y-persistent along β̃_{m+1}", is false. MS10's hypothesis at J_{m+1} is then never available, and MS10 is vacuous there. So **the derivation "MS8 ⇐ MS10" is not correct as worded.** It has to be rephrased component-wise, as follows.

**Lemma B1 (components of a transport family; proved).** Let Q ∈ B_0, b a branch of B_0 at Q with lift b̃, Ñ := Ñ_b̃, and let Stab(b̃) ⊂ Aut(Q) be the pointwise stabiliser of b̃. Then:
- (a) every irreducible component Ñ^1 of Ñ maps onto N = H((b ∖ Q) × Δ_ε), and Ñ^1 ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0;
- (b) Stab(b̃) permutes the irreducible components of Ñ transitively;
- (c) for α ∈ Stab(b̃) and every component Ñ^1: x is Y-persistent on Ñ^1 iff α x is Y-persistent on α Ñ^1;
- (d) if Δ_{G_Q} is of product type, then a label of positive-dimensional type is Y-persistent on one component iff it is Y-persistent on all of them. Hence the component-wise notion agrees with MS10's.

*Proof.*
- (a) N is a topological 4-manifold (H is a homeomorphism), so its germs are irreducible. By Remmert, q(Ñ^1) is an irreducible analytic set of dimension 2 in N, hence all of N. So Ñ^1 meets {t = 0}, where Ñ ∩ {t = 0} = b̃ ∖ 0. Since t is non-constant on Ñ^1, Krull makes the slice pure 1-dimensional. A 1-dimensional analytic subset of the irreducible curve germ b̃ ∖ 0 contains an open subset of it.
- (b) Let p̃ ∈ b̃ ∖ 0 be generic, so Stab(p̃) = Stab(b̃) (stabiliser jumps on the curve b̃ form a discrete set). Near (p̃, 0), q is the quotient by Stab(p̃). So the germ components of q^{-1}(N) at (p̃, 0) are permuted transitively by Stab(p̃), because the germ of N there is irreducible (R7-4 Lemma 2(a) argument). Each of them has its t = 0 slice in b̃ (by (a), applied to the germ), so it lies in Ñ. Every global component of Ñ contains such a germ for generic p̃, by (a). An element α ∈ Stab(b̃) maps Ñ to Ñ, because αÑ is the component of q^{-1}(N) containing αb̃ ∖ 0 = b̃ ∖ 0. So α maps global components to global components. Transitivity on germs at (p̃, 0) therefore gives transitivity on global components.
- (c) By (K3), F_x(αp) ≅ F_{α^{-1}x}(p), and α preserves intactness patterns. So persistence of y on Ñ^1 is persistence of αy on αÑ^1.
- (d) By Lemma PT (round9_q3 §3), every α ∈ Aut(Q) fixes x. Combine with (b) and (c). ∎

**Repaired notion and repaired missing statement.**
- *x is Y-persistent on a component*: there is an irreducible component Ñ^1 of Ñ_b̃ such that x is intact and F_x(p) ≅ Y_t at every (p, t) ∈ Ñ^1.
- **MS10′** is MS10 with both the hypothesis and the conclusion read in this component-wise sense. Hypothesis: x is Y-persistent on some component of Ñ_β̃. Conclusion: x is Y-persistent on some component of Ñ_b̃.
- At product-type points MS10 and MS10′ coincide, by B1(d). At non-product points neither implies the other formally.

**The chain with MS10′ (checked).**
1. *Base.* Δ_Γ is of product type, so by B1(d) nothing changes.
2. *Product-type junctions.* round9_q7 Lemma J and Corollary J′ are already component-wise: they use a germ component 𝒲̃^a ⊃ β̃ with persistent vertex x. Their conclusion, persistence on a germ component 𝒲̃″ ⊃ b̃, gives persistence on the global component of Ñ_b̃ that contains that germ, by the identity principle (the persistence set is analytic, round9_q7 Lemma S(c)).
3. *Transfer along a travel interval* (this is what step (b) asserts, now proved component-wise, given the Gap A repair). Let Ñ′^1 be a component of the leaving family at J_m on which x_m ↔ c is persistent, and let 𝒲̃ be the lifted family component containing Π_S(Ñ′^1). Its t = 0 slice contains an arc of the track's lifted curve E, hence all of E. Let p̃ ∈ β̃_{m+1} ∖ 0 be generic at J_{m+1}, with Π_S(p̃) = z ∈ E.
   - Near p̃, Def(J_{m+1}) is a versal deformation of the curve C_p̃.
   - Near (p̃, 0), Π_S maps the germ components of q^{-1}(N″) finitely onto the germ components of ξ^{-1}(κ(D)) at (z, 0). So some germ component maps into 𝒲̃.
   - Its t = 0 slice lies on β̃_{m+1}, so it lies in Ñ″ := Ñ_{β̃_{m+1}}. Let Ñ″^1 be the global component containing it.
   - By the identity principle, Π_S(Ñ″^1) ⊂ 𝒲̃.
   - The chart label x_{m+1} corresponds to the factor c, by K_w Step 3 and the Gap A repair.
   - By Lemma S(c) (persistence is global on the irreducible 𝒲̃), x_{m+1} is Y-persistent on Ñ″^1.
4. *Non-product junctions and R(D)-points:* MS10′.
5. *Endpoint.* MS10′ gives a component Ñ^1 of Ñ_b̃ on which x is Y-persistent. By B1(a), its t = 0 slice is an open subset of b̃ ∖ 0, on which x is intact with F_x ≡ Y_0. By the identity theorem on the irreducible curve b̃ and the constancy of the pattern, x is intact along b̃ and F_x ≡ Y_0 there. This contradicts MERGE and MOV, as in chain step (d).
6. Product-type endpoint, (c) of the chain: unchanged, by B1(d).

So, after the repairs of 2.1 and 2.2, **the chain reduces the goal to (Rig) + MS10′, invoked at non-product junctions, non-product endpoints and the points of R(D).** I found no other flaw in the parts I checked (steps (a)–(d) and the base). I did not re-derive Prop K_w's marking details, Lemma PA, or the cited Teichmüller facts.

---

## 3. Attempt on MS10 / MS10′

Setting: as in MS10′. Q ∈ B_0 lies in a non-product stratum, x is Y-persistent on a component Ñ^1_β̃ of Ñ_β̃, Y is non-constant, and Q_t := H_t(Q).

### 3.1 The deformation must move Q off itself (proved)

**Lemma 3.1.** Assume Q is isolated in B_0 ∩ Δ_{G_Q}, i.e. Q is a puncture of every piece through it. This holds at every junction and endpoint of the walk chain that is not a crossing. Then:
- (a) for small τ, B_τ ∩ Δ_{G_Q} ∩ U = {Q_τ} for a fixed neighbourhood U of Q;
- (b) F_x(q_τ) ≅ Y_τ at some lift q_τ of Q_τ;
- (c) the set T_Q := {τ : Q ∈ closure(V_τ)} is closed and discrete near 0. More generally, no point Q′ of Δ_{G_Q} near Q lies in closure(V_τ) for τ in a set accumulating at 0, unless [Y_τ] = [F_x(q′)] there for a lift q′ of Q′.

*Proof.*
- (a) Choose U with B_0 ∩ Δ_{G_Q} ∩ closure(U) = {Q}. Suppose P_n ∈ B_0 ∩ Δ_{G_Q} and τ_n → 0 with H_{τ_n}(P_n) ∈ U converging to Q. Since H is a homeomorphism with H(Q, 0) = (Q, 0), (P_n, τ_n) → (Q, 0), so P_n = Q for n large. H_τ maps B_0 ∩ Δ_{G_Q} onto B_τ ∩ Δ_{G_Q} by (R2). So (a) holds.
- (b) By Lemma B1(a), q(Ñ^1) = N := H((β ∖ Q) × Δ_ε). For fixed τ the slice N_τ accumulates at Q_τ, and q is proper. So the closure of Ñ^1_τ contains a lift q_τ of Q_τ. F_x ≅ Y_τ on Ñ^1_τ, and F_x is continuous on the closed set L_x ∋ q_τ.
- (c) If Q ∈ closure(V_τ), then Q ∈ B_τ ∩ Δ_{G_Q} ∩ U, so Q = Q_τ by (a). Then q_τ = 0, because q^{-1}(Q) = {0}, and (b) gives [Y_τ] = [F_x(0)] = [Y_0]. Since [Y] is holomorphic and non-constant (PR-A), this happens only on a closed discrete set. The general statement is the same argument with Q′ in place of Q. ∎

So, in MS10's setting, the cusp Q of V_0 is not a boundary point of V_τ for generic small τ. Every object attached to Q at τ = 0 must move with Q_τ.

### 3.2 Consequence for the surviving obstruction (A2-disc), using rigidity of Teichmüller curves (conditional)

Recall round9_q5 Corollary 2. A failure of MS10 at Q (under the readings (R3), (T4) used there) needs α ∈ Γ moving x and a 2-dimensional relevant component Φ of Fix(α) ∩ 𝒳. In case (A2-disc), Φ_0 lies on the lift of a Teichmüller curve 𝒯 ⊂ V_0 of α-symmetric curves with cusp Q. For each small τ ≠ 0, Φ_τ is a curve of α-symmetric curves in V_τ.

**Cited fact (Rigidity of Teichmüller curves; from memory: McMullen, "Rigidity of Teichmüller curves", 2009; also Möller 2006 via variations of Hodge structure).** Let f: C → M_g be (the normalisation of) a Teichmüller curve. If f_s: C_s → M_g, s ∈ Δ, is a holomorphic family of holomorphic maps, defined on a holomorphic family of Riemann surfaces of finite type C_s with C_0 = C, and f_0 = f, then f_s(C_s) = f(C) for all s. I state this in the form I need. I have not checked whether the published statements are literally this form, in particular in the orbifold sense.

**Proposition 3.2 (conditional; partial).** In the setting of MS10/MS10′ with Q isolated in its stratum, suppose case (A2-disc) occurs. Let Φ^glob be the irreducible component of 𝒱 ∩ (M_g^{[h]} × Δ) containing q(Φ), where M_g^{[h]} is the closed locus of curves admitting an automorphism of the topological type h of α. Assume:
- **(Eq)** after a base change τ = s^k, the family of curves Φ^glob_τ is the image of a holomorphic family f_s: C_s → M_g as in the cited fact, with f_0 the normalisation of 𝒯.

Then (Eq) is impossible. So in case (A2-disc), the α-symmetric curves Φ_τ ⊂ V_τ do **not** form an equisingular deformation of the Teichmüller curve 𝒯.

*Proof.* By rigidity, f_s(C_s) = 𝒯 for all s, so 𝒯 ⊂ V_τ for all small τ. Q is a cusp of 𝒯, so Q ∈ closure(𝒯) ⊂ closure(V_τ) for all small τ. This contradicts Lemma 3.1(c). ∎

**What this means.** In a hypothetical failure of MS10 of type (A2-disc), the closure of Φ^glob is a 2-dimensional analytic family of curves, proper over Δ. Its central fibre contains closure(𝒯) but is not an equisingular limit of the Φ_τ. Either:
- the central fibre has other components, which by Lemma TG are further Teichmüller curves of h-symmetric curves of V_0, or boundary curves (case (B)); or
- closure(𝒯) appears with multiplicity, or the family acquires extra cusps that move into the boundary at τ = 0.

In every case Φ_τ must "let go" of the cusp Q (Lemma 3.1). This is new information on (O1″) of round9_q5, but it does not exclude (A2-disc). Removing (Eq) would need a rigidity statement for Teichmüller curves that appear as one component of a degenerate fibre. I do not know such a statement, and I suspect it is false in general.

### 3.3 The interior mechanism of a twin jump is locally realisable with V_0 coarse-smooth (proved, local model)

This explains why, once more, local arguments cannot finish. The model is in the right dimension: complex surfaces, so that the bad locus has real codimension 2 in the 3-fold family and the squares of R8-5 / round9_q5 do meet it.

Let α act linearly on C^n ⊃ (germ of T_g) with fixed space F, of dimension k, and (−1)-eigenspace N, of dimension r ≥ 1. The coarse germ is F × (N/±1). Embed N/±1 by n ↦ n ⊗ n. Pick d ∈ F and v = v_F + v_N with v_N ≠ 0 and v_F ∉ C·d. Put
- S := {a d + b v : a, b ∈ C} and αS = {a d + b(v_F − v_N)}. Both contain the line D := C·d ⊂ F, and S ≠ αS;
- V_0 := image of S = {(a d + b v_F, b² v_N ⊗ v_N)}. The map (a, b) ↦ this is an injective immersion, so V_0 is a **smooth** surface germ in the coarse space, and its preimage is S ∪ αS, two sheets crossing along D;
- V_τ := {(a d + b v_F, (b² + τ) v_N ⊗ v_N)}. This is again an injective immersion, so a smooth surface germ, and τ ↦ V_τ is a smooth, topologically trivial family. Its preimage is {a d + b v_F + c v_N : c² = b² + τ}, which is **irreducible** for τ ≠ 0: the two sheets S, αS merge;
- V_τ ∩ (image of F) = {b² = −τ}, a curve for each τ ≠ 0. So Fix(α) meets the family in a 2-dimensional relevant set Φ with Φ_0 = D. This is case (D2)/(A2-disc) of round9_q5, with D playing the role of the lifted Teichmüller curve 𝒯 (Lemma TG says S ∩ Fix(α) is a Teichmüller disc when S is totally geodesic; in the linear model S, αS are linear subspaces).

So two lifted sheets of a coarse-smooth V_0 that cross along a curve of symmetric curves can be merged by a coarse-smooth deformation. On the merged sheet, a label carried along S continues onto αS, i.e. onto its twin. Total geodesy of V_0 at τ = 0 constrains only S and αS (both totally geodesic, meeting along a Teichmüller disc). It says nothing about the merging, because V_τ is not totally geodesic. Excluding the twin jump therefore needs **global** input: for instance a global form of Proposition 3.2 (what the symmetric curves Φ_τ can converge to), or a global count. I could not supply it.

### 3.4 Where a proof of MS10′ would have to come from (analysis, not proved)

Combining §1, §3.1–3.3 with the prior results:
- A failure of MS10′ at Q needs, in the 3-fold 𝒳, two lift-curves λ ≠ λ′ of Q_t (round9_q2 Lemma 2), an α ∈ Γ moving x, and a 2-dimensional α-fixed family Φ (round9_q5). In case (A2-disc) it also needs a non-equisingular degeneration of α-symmetric curves of V_τ onto a Teichmüller curve 𝒯 ⊂ V_0 with cusp Q, which must leave Q (Prop 3.2, Lemma 3.1).
- Each of these is locally realisable (§3.3, R7-3 §5, round9_q6 §4).
- By §1, a proof must use "Y non-constant". The only global consequence of Y non-constant used so far is genericity (finiteness via (Rig)). Lemma 3.1 is a second, different use: the cusp moves. A possible route, which I did not complete: the curve τ ↦ Q_τ is holomorphic (round9_q2 §1, R8-6 Lemma 3.1), non-constant by Lemma 3.1, and its x-twins satisfy [F_x(q_τ)] = [Y_τ] ≠ [F_{α^{-1}x}(q_τ)] at generic τ (round9_q8 Lemma 1′). Comparing this with the h-symmetric curves Φ_τ, which accumulate at a point of B_τ near Q_τ (by Lemma 3.1 not at Q), might force (Ψ-J) at a lift of Q_τ, and with it α ∈ Aut(Q_τ). That would contradict the separation of the twins. The missing step is to show that the trace Ψ of Φ is of type (Ψ-J), i.e. to exclude (Ψ-Z) and (B-pure). This is exactly the open part of round9_q5 §§3–4, and I could not close it.

---

## 4. Summary

**Proved here** (modulo the cited standard facts and the prior results used as stated):
1. **Proposition 1.1.** MS10 is vacuous whenever the problem's claim holds. Any counterexample to MS10 is a counterexample to the problem for (Rig)-families. So the counterexample option is equivalent to disproving the problem.
2. **Gap A in the chain** (walk chain / step (b)): at points of R(D) of a non-product piece D, the tracked label can switch to a twin in the middle of a travel interval. Such points need not lie in the special set Σ; a smooth local model is given. **Repair:** add the finite sets R(D) to Σ. The new transitions are MS10 configurations at non-product points, which MS10 already allows.
3. **Gap B in the chain:** under (R2), a transport family Ñ can be reducible. R7-3 Lemma 2, step 2 ("Ñ is a connected 4-manifold, hence irreducible") is false in general; an explicit local model is given. In that model no label is Y-persistent along β̃ in MS10's sense, although no twin jump occurs. So chain step (b), as worded, can fail at non-product pieces.
   - **Lemma B1:** the components of Ñ are permuted transitively by the pointwise stabiliser of b̃, and persistence transforms by (K3). In product-type strata the component-wise and the global notions agree.
   - **Repair:** the component-wise MS10′. The chain then goes through: base, product-type junctions (round9_q7 Lemma J is already component-wise), transfer along travel intervals (proved here component-wise, given the Gap A repair), and the endpoint.
4. **Lemma 3.1:** in MS10's setting, with Q isolated in its stratum, Q ∉ closure(V_τ) for τ outside a discrete set, i.e. the cusp must move.
5. **§3.3:** an explicit coarse-smooth local model in which a deformation merges two lifted sheets of V_0 crossing along a curve of symmetric curves. This is the interior mechanism of a twin jump, case (D2)/(A2-disc).

**Proved only conditionally (partial):**
- **Proposition 3.2:** case (A2-disc) cannot occur through an equisingular deformation (Eq) of the Teichmüller curve 𝒯. This depends on a rigidity theorem for Teichmüller curves (McMullen / Möller), cited from memory in a form I did not verify, and on the extra hypothesis (Eq).

**Not proved:**
- MS10 and MS10′ themselves. I give no proof and no counterexample; by Proposition 1.1, a counterexample would disprove the problem.

**Open (precise):**
- (Q1) MS10′ at non-product junctions, endpoints and R(D)-points.
- (Q2) Case (A2-disc) without (Eq): can the h-symmetric curves Φ_τ ⊂ V_τ degenerate non-equisingularly onto a configuration containing a Teichmüller curve 𝒯 ⊂ V_0 with cusp Q, while leaving Q (Lemma 3.1)?
- (Q3) Cases (A2-sheet), (B-pure) and (D3) of round9_q5, untouched here.
- (Q4) Entry 82, (Rig), still needed in addition to MS10′.
- (Q5) Whether the Gap B configuration (a non-product piece all of whose curves carry an automorphism exchanging two Y_0-copies) actually occurs for a smooth totally geodesic V_0. If it never occurs, MS10 can be used as originally worded.
- The inputs inherited from earlier rounds (Prop K_w's marking details, Lemma PA, (Fl), (R3), (T4)) are not re-proved here.



### round10_q7 (verbatim): incidence propagation, counting no-go, local model refuting irreducibility of transport families, Theorem Q (Krull linkage)
# round10_q7 — attempt on MS10 via counting (conservation of number)

**Final status: NOT PROVED; partial.** The counting route is shown to be a no-go (§2). The literal MS10 is shown to be too strong, by a local model (§3). A Krull-linkage theorem proves the corrected MS10′ under Q-factoriality (§4). Full summary in §5.

**Original plan (stage 2).** Read the whole brief. Plan:
1. §1: an incidence lemma (proved). Persistent label sets propagate along chains "transport family ⊃ lift-curve ⊂ transport family". This is the part of the counting idea that really works.
2. §2: the counting route itself. I show that every count in the suggested list is Γ-equivariant and is conserved, with multiplicity, in a failure configuration. So counting alone cannot contradict a failure of MS10 (a precise "no-go" statement, proved).
3. §3: a definitional problem with MS10 as literally worded (Ñ_b̃ is a *connected* component). I give an explicit local analytic model in which the literal conclusion fails, while the hypotheses that can be checked locally hold. In the same model the corrected version (irreducible component inside 𝒳) holds. This also shows that the claim "Ñ is irreducible" in R7-3 Lemma 2, step 2, is false in general.
4. §4: an attempt at an explicit local model of a genuine (corrected) failure, if time permits.
5. Summary: proved / not proved / open.

Notation and readings are those of the task file: (R1), (R2) with H_0 = id, Def(Q), q, s_e, labels, F_y, L_y, (K1)–(K4), transport families, lift-curves λ ⊂ 𝒥_Q, the 3-fold 𝒳 = closure(𝒞°), and Γ = Stab_{Aut(Q)}(𝒞°).

---

## 1. Incidence propagation (proved)

**Setting.** Q ∈ B_0, with chart Def(Q) ⊃ B (a small Aut(Q)-invariant ball) and ε small.
- 𝒥 = 𝒥_Q := {(q,t) ∈ B × Δ_ε : q(q) = Q_t}, where Q_t := H_t(Q). Its irreducible components are the **lift-curves** λ. Each is finite over Δ_ε and surjects onto it (round9_q2 §1).
- A **transport sheet** is an irreducible component T of closure(aÑ_c), where c is a branch of B_0 at Q (boundary or interior) and a ∈ Aut(Q). It is a 2-dimensional irreducible analytic germ at (0,0) (R7-4 Lemma 2(c)).
- The pinching pattern is constant on aÑ_c (R7-4 Lemma 2(a)). Hence T has a well-defined generic pattern S(T). Call T of **boundary type** if S(T) ≠ E(G_Q), i.e. Q ∉ stratum(c), and of **interior type** otherwise.
- For a lift-curve λ put Λ(λ) := {y : [F_y(q)] = [Y_t] for all (q,t) ∈ λ}. This makes sense because λ lies in the stratum locus {all s_e = 0} ⊂ L_y.
- For a transport sheet T put P(T) := {y : y is intact for S(T) and [F_y(p)] = [Y_{t(p)}] for all p ∈ T}. If y is intact for S(T), then T ⊂ L_y, because L_y is closed and T ∩ aÑ_c is dense in T.

**Lemma I0 (every transport sheet contains a lift-curve).** Let T be a transport sheet. Then T ∩ 𝒥 contains a lift-curve λ.

*Proof.*
- closure(aÑ_c) ∖ aÑ_c ⊂ 𝒥 ∪ {|t| = ε} inside B × Δ_ε. Indeed, its points lie over closure(N_c) ∖ N_c with N_c = H((c ∖ Q) × Δ_ε), and near (Q,0) that set is H({Q} × Δ_ε).
- t is non-constant on T: T ∩ {t = 0} ⊂ closure(c̃ ∖ 0) up to Aut(Q), which is a curve, and T is 2-dimensional. So for every small t ≠ 0, T_t := T ∩ {t} is a non-empty curve (Krull and openness of t|_T).
- Each component of T_t ∖ 𝒥 is a union of lifted branches of H_t(c). By the cone structure of B_t at Q_t, each such branch has a lift of Q_t in its closure.
- So T ∩ 𝒥 is an analytic subset of the curve 𝒥 that meets every fibre t ≠ 0. It therefore contains a component of 𝒥. ∎

**Lemma I1 (one inclusion, no hypotheses).** If λ ⊂ T, then P(T) ⊆ Λ(λ).

*Proof.* Let y ∈ P(T). Then T ⊂ L_y, and the set {p ∈ T : [F_y(p)] = [Y_{t(p)}]} is closed, because F_y is continuous on L_y and t ↦ [Y_t] is continuous (PR-A). It is all of T by definition, so it contains λ. ∎

**Lemma I2 (the converse at boundary sheets).** Assume Y is non-constant and (Rig) holds, so that R8-3 Theorem N applies at generic t. Let T be a transport sheet of boundary type with λ ⊂ T. Then Λ(λ) ⊆ P(T). Hence P(T) = Λ(λ) for every lift-curve λ ⊂ T. In particular, all lift-curves contained in one boundary-type sheet have the same Λ.

*Proof.* Let y ∈ Λ(λ), and let t ∉ Z be generic and small, with Z the countable exceptional set of Theorem N. Put q := λ(t), a lift of Q_t, so [F_y(q)] = [Y_t].
- T_t is a curve through q (Lemma I0, proof). Its germ at q minus q lies in aÑ_c ∩ {t}, so it consists of lifted branches c̃_t of H_t(c) through q.
- Q_t ∉ stratum(H_t(c)), because H_t preserves strata and T is of boundary type. By Theorem N, y is intact along c̃_t and we are in case STAY: F_y ≡ Y_t along c̃_t.
- y is intact along c̃_t, and the pattern is constant on the dense subset T ∩ aÑ_c. So y is intact for S(T), and T ⊂ L_y.
- The analytic set A := {p ∈ T : [F_y(p)] = [Y_{t(p)}]} contains a curve in T_t for uncountably many t. A proper analytic subset of the irreducible 2-dimensional T has at most countably many 1-dimensional components. So A = T, i.e. y ∈ P(T). ∎

**Corollary I3 (propagation along the incidence graph).** Let 𝔊 be the bipartite graph whose vertices are the transport sheets and the lift-curves at Q, with T — λ iff λ ⊂ T. Assume Y is non-constant and (Rig). Let
 T_0 — λ_1 — T_1 — λ_2 — ⋯ — λ_k — T_k
be a path in 𝔊 with T_1, …, T_k of boundary type. Then P(T_0) ⊆ P(T_k).

*Proof.* P(T_0) ⊆ Λ(λ_1) by Lemma I1. Then Λ(λ_j) = P(T_j) = Λ(λ_{j+1}) by Lemma I2, and Λ(λ_k) = P(T_k). ∎

**Corollary I4 (MS10 under linkage).** In the data of MS10, let T_β ⊂ closure(Ñ_β̃) be a transport sheet with x ∈ P(T_β) (one exists whenever x is Y-persistent along β̃). Let b be a boundary branch, and suppose **every** transport sheet contained in closure(Ñ_b̃) is joined to T_β in 𝔊 by a path through boundary-type sheets. Then x is Y-persistent along b̃: x is intact on Ñ_b̃ and F_x ≅ Y_t there. ∎

Remarks.
- The joining hypothesis of MS10 is not used in I3/I4. It is replaced by linkage in 𝔊.
- Corollary I4 contains round9_q2 Corollary 3 (a single lift-curve in closure(𝒞°)) and Proposition 4(ii). The new point is that linkage may pass through several lift-curves, through transport sheets that are not in the track's 3-fold, and through other branches at Q.
- Consequently, **a failure of MS10 at a boundary branch b forces some sheet T_b ⊂ closure(Ñ_b̃) to lie in a different connected component of 𝔊_∂ (𝔊 restricted to the boundary-type sheets and the lift-curves) from every sheet carrying x.** Since T_b contains some λ′ (Lemma I0), and the lift-curves in 𝒳 form one Γ-orbit (round9_q6 Lemma 1), this means: λ′ = γλ for some γ ∈ Γ, Λ(λ′) = γΛ(λ) by (K3), and x ∉ γΛ(λ).

---

## 2. The counting route: a no-go statement (proved)

The task suggests building finite analytic families over Δ_ε and comparing degrees at t = 0 with generic t. Here is what all such counts give.

**Lemma C1 (dichotomy along a lift-curve).** For a lift-curve λ and a label y, A_y(λ) := {(q,t) ∈ λ : [F_y(q)] = [Y_t]} is either all of λ (iff y ∈ Λ(λ)) or a finite set.

*Proof.* A_y(λ) is analytic in the irreducible curve λ, since F_y is holomorphic into the coarse space on the stratum locus and [Y] is holomorphic. ∎

**Lemma C2 (equivariance).** For γ ∈ Aut(Q): γλ is a lift-curve and Λ(γλ) = γΛ(λ). For transport sheets, P(γT) = γP(T).

*Proof.* (K3): F_y(γq) ≅ F_{γ^{-1}y}(q). The pattern of γT is γS(T). ∎

**Proposition C3 (all suggested counts are conserved, also in a failure configuration).** Let λ_1, …, λ_k be the lift-curves in 𝒳 (one Γ-orbit), d_j := deg(λ_j → Δ_ε), and r := |Λ(λ_1)| = ⋯ = |Λ(λ_k)| (Lemma C2). Consider the analytic set
 𝒜 := {((q,t), y) : (q,t) ∈ 𝒥 ∩ 𝒳, [F_y(q)] = [Y_t]} ⊂ (𝒥 ∩ 𝒳) × V(G_Q).
1. Its 1-dimensional part 𝒜¹ is ⋃_j λ_j × Λ(λ_j). It is finite over Δ_ε of degree r·Σ_j d_j. By conservation of number for finite maps of curves, its fibre over t = 0, counted with multiplicity, has the same degree. The label y occurs there with multiplicity Σ_{j : y ∈ Λ(λ_j)} d_j, and the set of labels that occur is ΓΛ(λ_1).
2. Its 0-dimensional part sits over t = 0 (and over a finite set of other times). It consists of the Y_0-copies at Q that lie in no Λ(λ_j). It is not flat over Δ, so conservation of number says nothing about it.
3. The same holds for the counts of pairs (lift, persistent label), (boundary branch of 𝒳_t through a lift, persistent label), and for the multiplicity of {F_x ≅ Y_t} ∩ 𝒳 along λ_j. Each is a Γ-invariant function of the configuration. Its value at generic t is r times a Γ-invariant number (the number of lifts, or of branches), and the t = 0 limit is the same number counted with multiplicities.

*Proof.* (1) and (2) follow from Lemma C1 applied to each λ_j and each label. For (3), every count listed is a sum over the Γ-orbit of lift-curves of a quantity that Lemma C2 makes constant along the orbit. ∎

**Consequence (the no-go).** In a failure of MS10 at a boundary branch b (§1, last remark), x ∈ Λ(λ) and x ∉ Λ(λ′) = γΛ(λ). The "(r+1)-st copy" of the Count lemma (round9_q3 §5) is the label x seen from λ′. In the set 𝒜 above it is **not** an extra point. It is carried by the 1-dimensional component λ × {x}, through the other lift-curve λ. So:
- the count r at a single lift and the count |ΓΛ(λ)| ≥ r + 1 at t = 0 are different quantities, and neither is violated;
- a conservation-of-number contradiction would need a Y_0-copy at Q lying in no Λ(λ_j). Its existence is neither forced nor forbidden by a failure of MS10, and its existence alone contradicts nothing (part 2).

So **every count built from the families of move 1 is consistent with a failure of MS10.**

**Ledger correction.** The (r+1)-st copy described in the task's opening paragraph ("A failure of MS10 at Q forces Q to carry at least r + 1 components isomorphic to Y_0 at t = 0") is not a drop in any conserved count. It is the union over the Γ-orbit of the persistent sets. What distinguishes failure from success is *which* labels are persistent at which lift-curve (Λ(λ) is not Γ-invariant), not *how many* there are. Counts are invariant under the symmetry γ that exchanges the two situations. The counting route cannot decide MS10 without further input, and that input must break the Γ-symmetry. Total geodesy of V_0 is Γ-symmetric at t = 0 too, so it has to enter through something non-numerical, for example the position of the track.

---

## 3. The literal wording of MS10 is too strong: a local model, and a flaw in R7-3 Lemma 2 (proved, as a local statement)

MS10 defines Ñ_b̃ as the **connected** component of q^{-1}(H((b ∖ Q) × Δ_ε)) ∩ (B × Δ_ε) that contains b̃ ∖ 0. It defines "x Y-persistent along b̃" as a condition at **every** point of Ñ_b̃. R7-3 Lemma 2, step 2, asserts that Ñ is a topological 4-manifold ("being a cover of a punctured disc times a disc") and hence irreducible. The following explicit germ shows that this is false. In the germ, the literal conclusion of MS10 fails while every hypothesis of MS10 that can be checked in the chart holds.

### 3.1 The model
- **Graph.** G_Q has vertices x, x′, w, z and edges e_1 = {x,w}, e_2 = {x′,w}, e_3 = {w,z}. The components x, x′ have the type (g_i,n_i) of Y and are isomorphic at Q. There is σ ∈ Aut(Q) of order 2 with σ(x) = x′, σ(e_1) = e_2, σ(e_3) = e_3. The stratum Δ_{G_Q} is not of product type, since σ exchanges two vertices of positive-dimensional type.
- **Chart coordinates.** The relevant chart coordinates are (s_1, s_2, s_3, a, b). Here s_j smooths e_j, a is a local coordinate of [F_x] near [Y_0] (so [F_x] = [Y_0] ⇔ a = 0), and b = a∘σ is the same for x′. For simplicity take dim M_{g_i,n_i} = 1 and put [Y_t] ↔ a = t. The remaining chart coordinates are set to 0. σ acts by (s_1, s_2, s_3, a, b) ↦ (s_2, s_1, s_3, b, a).
- **The 3-fold.** In (s,a,b,t)-space put
 𝒳′ := {s_1 = s_2 s_3, a = t, b = 0}, a smooth 3-fold (a graph over (s_2, s_3, t)),
 and let the preimage of closure(𝒱) near (0,0) be 𝒳′ ∪ σ𝒳′, with σ𝒳′ = {s_2 = s_1 s_3, b = t, a = 0}.

**Elementary checks.**
1. 𝒳′ ∩ σ𝒳′ = {s_1 = s_2 = 0, a = b = t = 0} = D̃ × {0}, where D̃ := {(0,0,r,0,0)}. Indeed a = t and a = 0 give t = 0. Then s_1 = s_2 s_3 and s_2 = s_1 s_3 give s_1(1 − s_3²) = 0, so s_1 = s_2 = 0 near 0. The set D̃ is fixed pointwise by σ, and it lies in the boundary {s_1 s_2 s_3 = 0}.
2. So q|_{𝒳′} is injective (q(p) = q(p′) means p′ ∈ {p, σp}, and σp ∈ 𝒳′ forces σp = p). The coarse family closure(𝒱) near (Q,0) is q(𝒳′), homeomorphic to C³ by the graph coordinates (s_2, s_3, t).
3. Interior points of 𝒳′ (s_1 s_2 s_3 ≠ 0) have trivial stabiliser. So V_t is smooth there, and so is V_0.
4. **H.** Define H_t(q(s_2, s_3, 0)) := q(s_2, s_3, t). The zero pattern of (s_1, s_2, s_3) = (s_2 s_3, s_2, s_3) depends only on (s_2, s_3). Hence H is a stratum-preserving homeomorphism, smooth on the interior. This gives (R1), (R2), (i) and (ii) locally, and H_t(Q) = Q_t := q(0,0,0,t,0).
5. **Boundary at t ≠ 0.** 𝒳′_t ∩ {s_1 s_2 s_3 = 0} = {s_2 s_3 = 0} has two branches through λ(t) := (0,0,0,t,0):
   - T_F := {s_1 = s_3 = 0, s_2 = r, a = t, b = 0}, with pattern {e_1, e_3};
   - T_D := {s_1 = s_2 = 0, s_3 = r, a = t, b = 0}, with pattern {e_1, e_2}.
   Their σ-images pass through σλ(t) = (0,0,0,0,t). At λ(t) the unique Y_t-copy is x (a = t, b = 0 ≠ t), so r = 1, and x is intact and ≡ Y_t along both branches. Krull at the lift (round9_q1 Lemma 1(c)) holds: the patterns cover e_1, e_2, e_3.
6. **The pieces.**
   - Pattern {e_1,e_3} contracts e_2. The stratum has vertices x, w ∪ x′, z, and x is constant ≡ Y_t. This plays the role of ∂V_t ⊂ Δ_Γ, a stratum that can be of product type.
   - Pattern {e_1,e_2} contracts e_3. Its vertices are x, x′, w ∪ z. This is a non-product piece D with constant vertices x (≡ Y_t) and x′ (≡ Y_0, "frozen") and moving vertex w ∪ z. Both constant vertices are ≅ Y_0 at t = 0. At t = 0, D̃ is fixed pointwise by σ: every point of D has the extra automorphism σ at t = 0, and it is lost for t ≠ 0 (allowed under (R2)).

### 3.2 Literal MS10 fails in the model
- Take β̃ := F̃ = T_F ∩ {t = 0} = {(0, r, 0, 0, 0)} and b̃ := D̃. Both lie in the smooth connected surface 𝒳′_0, whose interior {s_2 s_3 ≠ 0} is connected. So they are joined inside the chart by paths in q^{-1}(V_0) ∩ B.
- **Ñ_β̃ = T_F.** q^{-1}(N_f) = T_F ∪ σT_F, and these are disjoint (s_2 = r ≠ 0 on T_F, s_2 = 0 on σT_F). So x is Y-persistent along β̃ (s_1 = 0 and a = t on T_F).
- **Ñ_b̃ = T_D ∪ σT_D.** q^{-1}(N_d) = T_D ∪ σT_D, and T_D ∩ σT_D = D̃ × {0} ≠ ∅. So the connected component containing D̃ ∖ 0 is the union. It is reducible, and it is not a topological manifold along D̃ × {0}: two real 4-planes meet in a real 2-plane. Its quotient by σ, which is N_d, is a manifold.
- On σT_D, x is intact but F_x ↔ a = 0 ≠ t. So **x is not Y-persistent along b̃ in the literal sense**. The same holds for x′. MS10's conclusion fails, while Q is non-product, β̃ and b̃ are joined, x is persistent along β̃, and Y (a = t) is non-constant.
- **The corrected reading holds in the model.** The track's component is 𝒞° = 𝒳′ ∖ {s_1 s_2 s_3 = 0} (𝒳′° and σ𝒳′° are disjoint), so 𝒳 = 𝒳′, Γ = {1}, and the component of Ñ_b̃ in 𝒳 is T_D, along which x ≡ Y_t.

This is a germ, not a global V_0. Total geodesy and (Rig) for global pieces cannot be checked in it. So it is **not** a counterexample to the problem. It shows two things:
- the literal MS10 cannot be proved by arguments that see only the chart;
- R7-3 Lemma 2 step 2 ("Ñ is irreducible") is false whenever the pointwise stabiliser of b̃ at t = 0 is larger than the generic stabiliser along the family, and moves one irreducible component of Ñ to another.
  - In R8-8 §0, the identity (∗) ("F_x ≡ φ_c(t) on closure(Ñ_t)") is stated only for D of product type. There Lemma PT makes every such stabiliser element fix x, so F_x agrees on the components and (∗) survives.
  - In non-product strata, which is where MS10 lives, the analogue of (∗) fails: in the model it fails on σT_D.

### 3.3 The corrected statement
**MS10′.** Same setting and data as MS10. Let 𝒞° be the connected component of q^{-1}(𝒱) ∩ (B × Δ_ε) that contains the interior paths γ_n (after passing to a subsequence; finitely many components meet a neighbourhood of 0), let 𝒳 := closure(𝒞°), and replace "Y-persistent along c̃" by:
- *(Pers_𝒳)* x is intact, and F_x ≅ Y_t, on every irreducible component of closure(Ñ_c̃) that is contained in 𝒳.

Conclusion: if (Pers_𝒳) holds for β̃, it holds for b̃.

Comments.
- round9_q2 Lemma 2 and round9_q6 Lemma 2 show that some irreducible component of each of closure(Ñ_β̃) and closure(Ñ_b̃) lies in 𝒳. With (Rep3)-generic base points, Stab(z̃) is the pointwise stabiliser, which may permute the components; the q6 proof only gives "some component".
- Every later use of (∗), R7-3 Lemma 2 and R8-8 §0 should be read for irreducible components. In the chain this matters exactly at branches that are σ-fixed pointwise at t = 0. I have not re-audited every such use; this is recorded as an open bookkeeping item.

---

## 4. Where a conservation law does work: Krull linkage in the 3-fold (proved)

Section 2 says that numerical counts are blind to *which* label persists. One intersection-theoretic statement is not blind: two divisors on a 3-fold that is Q-factorial at a point meet in a curve through that point. Applied to two transport sheets inside the track's 3-fold, this curve is forced to be a common lift-curve, and Corollary I3 then transports the label. This is the "conservation of number" that the task asks for, in its correct form: the intersection T_β · T_b is non-empty at every time t if it is non-empty at t = 0 and one of the sheets is Cartier.

**Theorem Q.** Assume Y is non-constant and (Rig) holds. Let Q ∈ B_0 (any stratum). Let T_β and T_b be transport sheets at Q, both of boundary type, contained in a common irreducible component X of the germ (𝒳,(0,0)), with x ∈ P(T_β). Assume:
- (QC) there is a holomorphic h on a neighbourhood of (0,0) in X with Z(h) ∩ X = T_b (set-theoretically) near (0,0). This holds, for instance, if X is smooth at (0,0), or normal and Q-factorial there;
- (Sep) T_β ∩ T_b ∩ {t = 0} = {(0,0)} near (0,0). This holds automatically if β and b are distinct coarse branches.

Then one of the following holds.
- (a) T_β and T_b contain a common lift-curve λ. Hence x ∈ P(T_b): x is intact and F_x ≅ Y_t on T_b (MS10′'s conclusion for this sheet).
- (b) *Same-branch crossing.* β = b as coarse branches, and there are g ∈ Aut(Q) with T_b = gT_β and an irreducible curve germ C ⊂ T_β, finite over Δ_ε and not contained in 𝒥, fixed pointwise by g. Moreover, for all t outside a countable set, the label g^{-1}x is an IMOV copy of Y_t at the point q(C_t) ∈ H_t(β ∖ Q). That is, q(C_t) is an interior point of its piece, g^{-1}x has value ≅ Y_t there and moves along the branch.

*Proof.*
1. **Krull.** T_β ≠ T_b by (Sep), and T_β ⊄ T_b since both are irreducible of dimension 2. So h|_{T_β} ≢ 0 and h(0,0) = 0. By Krull, T_β ∩ Z(h) = T_β ∩ T_b has pure dimension 1 at (0,0). Let C be an irreducible component of its germ at (0,0).
2. **C is finite over Δ.** C ∩ {t = 0} ⊂ T_β ∩ T_b ∩ {t = 0} = {(0,0)} by (Sep). So t|_C is non-constant and finite, and C_t ≠ ∅ for every small t.
3. **Case C ⊂ 𝒥.** Then C is a lift-curve λ with λ ⊂ T_β ∩ T_b. By Lemma I1, x ∈ P(T_β) ⊆ Λ(λ). By Lemma I2 (T_b is of boundary type), Λ(λ) = P(T_b). This is (a).
4. **Case C ⊄ 𝒥.** C ∩ 𝒥 is a proper analytic subset of the irreducible germ C, hence {(0,0)}. Take p ∈ C_t with t ≠ 0 small.
   - p ∈ T_β ∖ 𝒥 ⊂ ⋃_a aÑ_β, so q(p) ∈ H_t(β ∖ Q). Likewise q(p) ∈ H_t(b ∖ Q).
   - H_t is injective and H_t(β ∖ Q) ∩ H_t(b ∖ Q) = ∅ for distinct coarse branches. So β = b.
   - Near p, the slices T_{β,t} and T_{b,t} are lifted local branches through p of the coarse curve H_t(β) at q(p). Stab(p) permutes these lifts transitively. So there is g_t ∈ Stab(p) mapping the germ of T_{β,t} at p onto the germ of T_{b,t} at p.
   - Aut(Q) is finite. So one g occurs for infinitely many points p = p_n ∈ C, accumulating at (0,0) and with distinct times.
   - Then gT_β ∩ T_b contains infinitely many distinct 1-dimensional germs. So it is 2-dimensional, and gT_β = T_b by irreducibility.
   - Fix(g) ∩ C is analytic in C and contains the p_n, which accumulate at (0,0). So C ⊂ Fix(g).
5. **The label.** For p ∈ C_t we have p ∈ T_β ⊂ L_x and F_x(p) ≅ Y_t. Since gp = p, (K3) gives that g^{-1}x is intact at p and F_{g^{-1}x}(p) ≅ F_x(gp) = F_x(p) ≅ Y_t.
   - Apply R8-3 Theorem N at the point q(p) (generic t) to the label g^{-1}x and the branch T_{β,t} through p. Either STAY or IMOV.
   - If STAY holds for uncountably many t, then the analytic set {F_{g^{-1}x} ≅ Y_t} ⊂ T_β contains uncountably many slice curves. So g^{-1}x ∈ P(T_β) and x ∈ gP(T_β) = P(T_b) (Lemma C2): conclusion (a) for T_b.
   - Otherwise IMOV holds for all t outside a countable set, which is (b). q(p) is an interior point of its piece because it lies on H_t(β ∖ Q). ∎

**Corollary Q1 (MS10′ under Q-factoriality).** In the setting of MS10′, with b a boundary branch and β ≠ b as coarse branches: suppose every irreducible component of closure(Ñ_b̃) lying in 𝒳 lies on a common irreducible component X of 𝒳 with some sheet T_β ⊂ closure(Ñ_β̃) satisfying x ∈ P(T_β), and suppose X is Q-factorial at (0,0) (e.g. smooth). Then MS10′'s conclusion holds at (β̃, b̃). ∎

**Corollary Q2 (shape of a failure of MS10′).** Let b be a boundary branch with β ≠ b, and suppose MS10′ fails at (β̃, b̃) with Y non-constant. Then for some sheet T_b ⊂ closure(Ñ_b̃) ∩ 𝒳 with x ∉ P(T_b), and every sheet T_β ⊂ closure(Ñ_β̃) ∩ 𝒳 with x ∈ P(T_β), one of the following holds:
- **(F1)** T_β and T_b lie on a common irreducible component X of 𝒳, and T_b is not set-theoretically principal on X at (0,0). In particular X is not Q-factorial at (0,0): the track's 3-fold has a non-Q-factorial singularity at (0,0), of 3-fold-node type or worse;
- **(F2)** T_β and T_b lie on no common irreducible component of 𝒳.

*Proof.* Otherwise Theorem Q applies, and (b) is excluded because β ≠ b. ∎

**Remarks.**
- In (F2), 𝒞° is connected, so the components of 𝒳 are linked through interior points. At such a point p, Stab(p) permutes the local components transitively, because the coarse germ of 𝒱 at q(p) is irreducible. So the joining happens at interior points fixed by elements of Γ that exchange components of 𝒳. This matches the known necessary condition (an α ∈ Γ moving x with an interior fixed locus).
- The local model of (F1) is the 3-fold node 𝒳 = {xy = zw}. The two planes {x = z = 0} and {y = w = 0} (same ruling) meet only at 0. For t := x + y, the slices 𝒳_t (t ≠ 0) are smooth quadrics in which the two lines are disjoint, while at t = 0 they meet at the vertex of the A_1 cone 𝒳_0. This is exactly the "star splitting" of R8-8 §6.
- An involution that exchanges the two planes and preserves the node is of the form M ↦ AMB on 2×2 matrices M = [[x,z],[w,y]] of rank ≤ 1, since it preserves the ruling. Its fixed locus in 𝒳 is a finite union of lines. So, in a slice 𝒳_t, it has isolated fixed points, and the coarse quotient V_t would have A_1 points there unless those points lie in the boundary. Together with round9_q5 Corollary 1 (a twin jump needs a ≥ 2-dimensional relevant fixed component), this suggests that (F1) may be incompatible with smoothness of V_t. I have **not** proved this: a non-Q-factorial X need not be a node, and Γ need not preserve X.
- Theorem Q does not use total geodesy. Total geodesy can only enter through (QC), i.e. through the singularity type of the track's 3-fold at (0,0), or through (F2).

**A side correction (R8-8 §6, item 1, "stars are disjoint").** That sketch argues that two lifted arcs starting at different lifts of J_t cannot meet, "because away from J_t the stabiliser is locally constant along the arc". This fails at isolated points of an arc with a larger stabiliser.

*Example.* Def = C² ∋ (u,v), σ(u,v) = (−u,v), and the line L = {u = v − c}.
- q(L) = {(w,v) = ((v − c)², v)} is a smooth arc in C²/σ.
- Its two lifts L and σL start at the different points (−c,0) and (c,0), and they meet at the σ-fixed point (0,c).

So two stars can touch at symmetric points of an arc. This is precisely alternative (b) of Theorem Q. Nothing proved above relies on disjointness of stars.

**What (F2) reduces to, in the simplest combinatorics (analysis; sketched, not proved in general).** Let X ∋ T_β be a component of 𝒳 all of whose boundary sheets keep the edges E_x at x pinched. Let σ ∈ Γ with σx ≠ x, and let Σ ⊂ X ∩ Fix(σ) be a relevant 2-dimensional fixed component.
- For an edge f, Krull gives a curve Σ ∩ Z(s_f) through (0,0). At its points with t ≠ 0, the edges E_x ∪ σE_x are pinched.
- If f together with E_x ∪ σE_x exhausts E(G_Q), the curve lies in 𝒥. Then σ fixes a lift-curve of X, which gives "pointwise Lock" (round9_q5 (Ψ-J)) and kills the failure.
- Otherwise the curve lies in T ∩ σT for a boundary sheet T ⊂ X: a same-branch crossing as in Theorem Q(b). Or it lies in {t = 0}: (B-pure), round9_q5 (O2″).

So, in that case, a failure of MS10′ always ends in one of the two configurations the run already lists as open: same-branch IMOV crossings near Q at generic t, or (B-pure). This also assumes Q is isolated in B_0 ∩ Δ_{G_Q}; otherwise interior pieces through Q add a third possibility.

---

## 5. Summary

**Outcome: MS10 is NOT proved, and no global counterexample is given.**
- The assigned counting route provably cannot settle MS10 by itself (§2).
- MS10 as literally worded is too strong. A local model satisfies all of its chart-checkable hypotheses and violates its conclusion (§3). The corrected statement MS10′ is proposed.
- MS10′ is proved under a Q-factoriality hypothesis on the track's 3-fold (§4). Without it, a failure is reduced to two explicit shapes.

**Proved** (from (R1), (R2), (Rig), R8-3 Theorem N, and the cited standard facts of Krull's theorem and the identity theorem):
1. **Lemma I0–I2, Corollaries I3–I4.** Every transport sheet contains a lift-curve. P(T) ⊆ Λ(λ) for λ ⊂ T, with equality for boundary-type T when Y is non-constant. Persistent labels propagate along paths of the incidence graph 𝔊, so MS10 holds whenever the sheets of b̃ are 𝔊-linked to a sheet carrying x through boundary-type sheets. A failure of MS10 at a boundary branch means that T_b contains a lift-curve γλ (γ ∈ Γ) with x ∉ γΛ(λ).
2. **Proposition C3 and the no-go.** Every count in the task's list is conserved and Γ-equivariant, and remains consistent in a failure configuration:
   - lifts × persistent labels;
   - boundary branches through lifts × persistent labels;
   - multiplicities of {F_x ≅ Y_t} along lift-curves.
   The "(r+1)-st copy" of the Count lemma is carried by the other lift-curve of the Γ-orbit, not by an isolated point. A counting argument cannot distinguish which label persists.
3. **§3 model.** An explicit germ in which:
   - Ñ_b̃ (a connected component) is reducible and not a manifold;
   - the literal conclusion of MS10 fails;
   - the corrected statement MS10′ holds.
   Consequences:
   - R7-3 Lemma 2 step 2 ("Ñ irreducible") is false in general.
   - Every analogue of (∗) in non-product strata must be read on irreducible components.
   - In product strata (∗) survives, by Lemma PT.
4. **Theorem Q (Krull linkage).** Suppose two boundary sheets T_β ∋ x-persistence and T_b lie on a common irreducible component X of 𝒳 on which T_b is set-theoretically principal (e.g. X smooth or Q-factorial at (0,0)), and their t = 0 slices meet only at 0. Then either they share a lift-curve, so x is persistent on T_b, or there is a same-branch IMOV crossing near Q at generic t (alternative (b), possible only when β = b coarsely).
   - **Corollary Q1:** MS10′ holds when β ≠ b and the relevant component of 𝒳 is Q-factorial.
   - **Corollary Q2:** a failure with β ≠ b forces (F1) a non-Q-factorial component of 𝒳 at (0,0) containing both sheets, or (F2) the two sheets on different components of 𝒳, joined through interior fixed loci of elements of Γ.
5. Side correction: the "stars are disjoint" sketch of R8-8 §6 is false at isolated symmetric points (explicit example). Theorem Q(b) is exactly this phenomenon.

**Sketched only.**
- The reduction of (F2), in the simplest combinatorics, to the already-open same-branch crossings or (B-pure) (§4, last paragraph).
- The heuristic that (F1) of 3-fold-node type is incompatible with smoothness of V_t (the ruling-preserving involutions of a node have only 1-dimensional fixed loci).

**Open (named).**
- **(O-MS10′)** MS10′ itself.
- **(O-F1)** Can a component of the track's 3-fold 𝒳 be non-Q-factorial at (0,0), with T_b not principal on it, for smooth V_t and totally geodesic V_0? A negative answer would leave only (F2).
- **(O-F2)** (F2), equivalently round9_q5's (D2)/(B-pure) and the same-branch IMOV crossings.
- **(O-audit)** Re-audit of the uses of R7-3 Lemma 2 and (∗) at branches fixed pointwise at t = 0 by a label-moving automorphism (non-product strata).
- Entry 82 ((Rig)) is untouched.

proved: Lemmas I0–I2, Corollaries I3–I4, Proposition C3 and the counting no-go, the §3 local model with the R7-3 Lemma 2 correction, Theorem Q with Corollaries Q1–Q2, the star-disjointness correction.
not proved: MS10, and MS10′, in general.
open: O-MS10′, O-F1, O-F2, O-audit (and entry 82).


### round10_q2 §§4–5 (verbatim): the chart switch locus, Lemmas 4.1, 4.2, Proposition P1, what remains
## 4. The chart switch locus, and MS10 at interior points (partial result P1)

### 4.1 Joined versus same chart sheet
MS10's hypothesis "joined inside the chart" says the following: paths γ_n in q^{-1}(V_0) ∩ B run from near β̃ ∖ 0 to near b̃ ∖ 0. This does **not** put β̃ and b̃ into one chart sheet. q^{-1}(V_0) can be locally reducible at interior points, even though V_0 is smooth in the coarse space.

Example: in coordinates (z_1, z_2, z_3) let h(z) = (−z_1, z_2, z_3). The smooth coarse surface {w_1 = z_2²}, with w_1 = z_1², has preimage {z_1 = z_2} ∪ {z_1 = −z_2}. These are two sheets exchanged by h, crossing along the curve {z_1 = z_2 = 0} ⊂ Fix(h).

Let S_1, …, S_k be the irreducible components of q^{-1}(closure V_0) ∩ B. Take B so small that they are the germ components at 0 and are irreducible in B. This is standard and is used in round9_q3 SS′(b). Aut(Q) permutes the S_l.

**Definition.**
- The *switch locus* is Sw(Q) := ⋃_{k≠l} (S_k ∩ S_l) ∖ {∏_e s_e = 0}.
- **(NoSw_Q)** means: 0 ∉ closure(Sw(Q)). Equivalently, every 1-dimensional component through 0 of every S_k ∩ S_l lies in {∏ s_e = 0}. After shrinking B, (NoSw_Q) then means Sw(Q) = ∅.

**Lemma 4.1 (joined ⇒ same sheet under (NoSw_Q)).** Assume (NoSw_Q), and shrink B so that Sw(Q) ∩ B = ∅. If β̃ and b̃ are joined inside B in the sense of MS10, then some S_l contains both β̃ and b̃.

*Proof.*
- Since Sw(Q) ∩ B = ∅, q^{-1}(V_0) ∩ B is the disjoint union of the sets S_l ∩ B°, where B° := B ∖ {∏ s_e = 0}. Each is closed in q^{-1}(V_0) ∩ B, and there are finitely many, so each is also open. Each path γ_n therefore lies in one S_{l(n)}. Pass to a subsequence with l(n) = l.
- S_l is closed in B, so the limit point z ∈ β̃ ∖ 0 of γ_n(0) lies in S_l.
- Near z, S_l ∩ {∏ s_e = 0} is of pure dimension 1 (Krull: S_l is 2-dimensional and not contained in the hypersurface). It is contained in q^{-1}(B_0), whose germ at z is the germ of β̃: in a small ball, distinct lifted branches meet only at 0.
- So S_l contains a germ of β̃, hence all of β̃ (irreducible curve germ). The same argument applies to b̃. ∎

**Lemma 4.2 (what a failure of (NoSw_Q) is).** Assume V_0 is smooth. Adopt the reading (T4) of round9_q5: every component of the preimage of V_0 in T_g is a complex submanifold containing every Teichmüller geodesic tangent to it. (A caveat: smoothness of the coarse V_0 alone does not make the lifted components smooth. For example, {w_1 = z_2³} with w_1 = z_1² lifts to the cusp z_1² = z_2³. So (T4) is a genuine reading of "totally geodesic". Lemma 4.2 is descriptive only and is NOT used in the proof of P1.) Suppose (NoSw_Q) fails. Then there are h ∈ Aut(Q) ∖ {1}, sheets S_k ≠ S_l = hS_k, and an irreducible curve germ C at 0, not contained in {∏ s_e = 0}, with C ⊂ S_k ∩ hS_k ∩ Fix(h). Moreover, near any point of C ∖ 0, the sheet S_k corresponds to a component S̃ of the preimage of V_0 in T_g, and h to a finite-order mapping class ĥ. The component I of S̃ ∩ Fix(ĥ) containing the lift of C is a full Teichmüller disc. So q(C ∖ 0) lies in the image in M_g of a Teichmüller disc contained in V_0 ∩ M_g^{[ĥ]}: these are curves of V_0 with an automorphism of type [ĥ], and they accumulate at Q.

*Proof.*
1. **Switch points have stabilisers.** Let p ∈ (S_k ∩ S_l) ∩ B°, with k ≠ l, and put G_p := Stab_{Aut(Q)}(p).
   - Near p, q is the quotient by G_p, and q(p) ∈ V_0 is a smooth point of the coarse V_0.
   - The germ of q^{-1}(V_0) at p is the preimage of the irreducible germ (V_0, q(p)), so its irreducible components are permuted transitively by G_p. (Standard: preimage of an irreducible germ under a finite quotient map.)
   - Pick germ components A ⊂ (S_k, p) and A′ ⊂ (S_l, p). Then A′ = hA for some h ∈ G_p.
   - hS_k is a global sheet sharing the 2-dimensional germ A′ with S_l, so hS_k = S_l. Since k ≠ l, h ≠ 1, and p ∈ Fix(h).
2. **A curve inside Fix(h).** If (NoSw_Q) fails, some S_k ∩ S_l (k ≠ l) has a 1-dimensional component C through 0 that is not in the boundary.
   - By step 1, every p ∈ C ∖ 0 lies in Fix(h_p) for some h_p with h_p S_k = S_l.
   - There are finitely many h, and the sets C ∩ Fix(h) are analytic and cover C ∖ 0. So C ⊂ Fix(h) for one such h, by irreducibility of C.
3. **Total geodesy.** Near a generic point p ∈ C ∖ 0, Def(Q)° is locally biholomorphic to T_g ((HK), with h corresponding to a mapping class ĥ fixing the lift p̃). S_k corresponds to a component S̃ of the preimage of V_0, which is totally geodesic.
   - Apply Lemma TG (round9_q5 §2; it uses Teichmüller's uniqueness theorem (Te1)–(Te3), cited there) to S̃ ∩ Fix(ĥ). The component I containing the lift of C is not a point.
   - It is not S̃: otherwise S_k ⊂ Fix(h) near p, so hS_k ∩ S_k would contain an open set and hS_k = S_k, contradicting step 1.
   - Hence I is a full Teichmüller disc, and q(I) ⊂ V_0 ∩ M_g^{[ĥ]}. ∎

So (NoSw_Q) can fail only through "case (A)" of R8-5 Prop. D at t = 0. That is, V_0 must contain a Teichmüller disc, hence (when V_0 ∩ M_g^{[ĥ]} is 1-dimensional there) a Teichmüller curve, of ĥ-symmetric curves accumulating at Q, along which two lifted sheets exchanged by h cross.

### 4.2 Partial result P1
**Proposition P1 (MS10 at interior points under (NoSw_Q)).** Assume MS10's setting and data, and in addition:
- (i) Q lies in the stratum of the piece of β, or in the stratum of the piece of b (interior case: crossing, iMOV, or turning twin);
- (ii) (NoSw_Q) holds.

Then b̃ = β̃, so x is Y-persistent along b̃ and the conclusion of MS10 holds. Neither "Y non-constant", nor (Rig), nor smoothness of V_0 is needed for this.

*Proof.*
- Shrink B as in Lemma 4.1. MS10's ball may be taken as small as wanted (§2.3): the walk chain exists for every small r.
- By Lemma 4.1, β̃, b̃ ⊂ S_l for one chart sheet S_l.
- If Q lies in the stratum of the piece E of β, Corollary 3.4 (Theorem X** applied to E, β̃ and S_l) gives b̃ = β̃.
- If Q lies in the stratum of the piece of b, the same corollary with the roles exchanged gives β̃ = b̃.
- Then Ñ_b̃ = Ñ_β̃, and Y-persistence along b̃ is the hypothesis. ∎

**Consequences for the chain (under (NoSw) at the points concerned).**
1. The new junctions created by the repair of G1 (§2.2) are interior points with b̃ and β̃ lifts of one coarse branch. Under (NoSw_J), P1 gives b̃ = β̃: the walk cannot switch lifted germs there. The label is then consistent, with no use of MS10.
2. A non-product endpoint of iMOV type (x constant along β̃, x non-constant along b̃, Q in the stratum of the piece of b) is impossible under (NoSw_{Q_0}). P1 gives b̃ = β̃, which contradicts "x constant along β̃, non-constant along b̃". This holds at t = 0 alone.
3. A turning twin of type (T), at an interior point under (NoSw), is impossible for the same reason.

So the interior-point part of MS10 reduces exactly to points Q at which V_0 contains a Teichmüller disc of h-symmetric curves through which two lifted sheets cross and accumulate at Q (Lemma 4.2). The puncture-point part of MS10 (Q in the stratum of neither piece) is untouched by P1.

P1 is a sub-case result (an extra hypothesis (NoSw_Q) and a sub-class of points). By the task's rules it is PARTIAL and does not answer MS10.

### 4.3 The interior case without (NoSw_Q): what is left (reduction, proved)
Let Q be an interior point of the piece E of β, and drop (NoSw_Q).
- Let g ∈ Aut(Q) be any element with b̃ ⊂ gS, where S ⊃ β̃ is a chart sheet. Such a g exists because the sheets permuted by the path γ_n differ by products of switch elements h (Lemma 4.2, step 1).
- Theorem X** in gS ⊃ gβ̃ gives b̃ = gβ̃.
- By (K3), x is Y-persistent along gβ̃ iff g^{-1}x is Y-persistent along β̃.

So MS10 at an interior point is equivalent to the following statement: *the vertex g^{-1}x of the lifted piece through β̃ is also Y-persistent*. That is, the two constant vertices x and g^{-1}x of the lifted piece have the same value function (Lock on E). Here g is a product of automorphisms h, each fixing a curve of h-symmetric curves of V_0 that lies on a Teichmüller disc in V_0 and accumulates at Q (Lemma 4.2). This is the interior-point form of R8-5 Prop. D case (A) / round9_q5 (A2-disc). I could not close it.

---

## 5. What remains, and summary

### 5.1 Why the puncture case is not reached
At a point Q lying in the stratum of neither piece, chart sheets at a cusp always contain several boundary branches (Krull). So no analogue of Theorem X** can hold there, and "same chart sheet" gives no identification of b̃ with β̃. The remaining configuration is exactly the endpoint/junction twin of R8-8 Prop. 3 and round9_q8 Lemma 1′:
- Q has twins x, x′ = a^{-1}x with a ∈ Stab(𝒳);
- along b̃, x merges or moves (and is frozen at class [Y_0] at the b̃-side lift for small t), while x′ is persistent;
- the lift-curves of Q_t in closure(Ñ_β̃) and in closure(Ñ_b̃) differ for t ≠ 0, so |Aut(Q_t)| < |Aut(Q)|.

Nothing in §§2–4 excludes this, with or without (NoSw_Q). Corollary 3.4 and Lemma 4.1 are t = 0 statements. Their t ≠ 0 analogues would need total geodesy of V_t, which is not assumed.

### 5.2 Summary

**Proved here** (modulo the cited facts (HK), (FN), the standard facts on normal surface germs and resolutions used in round9_q4 §1.4, and the prior inputs Lemma PA, (Fl), (Prop), (Te1)–(Te3) as cited by earlier rounds):
1. **Remark 1.1:** a counterexample to MS10 is a counterexample to the problem (for a family with (Rig)). A general proof of MS10 is, through the chain, as strong as the goal modulo (Rig).
2. **Chain audit, gap G1 (§2.1):** step 2(b)'s claim that "the chart vertex is c_{m+1} on both ends" is unsupported for pieces in non-product strata. The walk's label can switch silently, inside a travel interval, from a persistent constant vertex c to a twin constant vertex σ^{-1}c at crossing points of the lifted piece with an Aut(G)-translate. **Repair (§2.2, sketch at the level of K_w):** enlarge Σ by the finite set Σ_tw of images of singular points of ξ_G^{-1}(closure D). Travel is then label-consistent, and the chain becomes correct as logic, at the price of extra MS10 instances at interior points (lifts of one coarse branch). No other gap was found. The dependence on (Rig) (entry 82, open) remains.
3. **Theorem X\*\* (§3):** round9_q4's Theorem X* holds in every stratum, not only product-type ones. The proof lifts the limit disc to ∏_w M_w through the marking ((HK), (FN)). Corollary 3.4: within one chart sheet at an interior point of a piece, there are no crossings and no turning twins.
4. **Lemma 4.1:** joined ⇒ same chart sheet, under (NoSw_Q). **Lemma 4.2** (descriptive, under the reading (T4)): failure of (NoSw_Q) means that V_0 contains a Teichmüller disc of h-symmetric curves accumulating at Q, along which two lifted sheets exchanged by h cross.
5. **Proposition P1 (PARTIAL):** MS10 holds whenever Q lies in the stratum of the piece of β or of b, and (NoSw_Q) holds. Consequently, under (NoSw) at the relevant points:
   - non-product iMOV endpoints and turning twins (T) are impossible already at t = 0;
   - the new junctions created by the G1 repair are trivial.
6. **§4.3:** without (NoSw_Q), MS10 at interior points is equivalent to Lock of the twin constant vertices x, g^{-1}x on the lifted piece, with g generated by the switch automorphisms.

**Not proved:**
- MS10 in general. In particular:
  - (a) all instances at points Q lying in the stratum of neither piece (puncture junctions and MERGE/pMOV endpoints with twins);
  - (b) instances at interior points where (NoSw_Q) fails.
- No counterexample was constructed. By Remark 1.1, it would be a counterexample to the problem itself.

**Open questions (precise):**
- **(O1)** MS10 at puncture points: exclude a Stab(𝒳)-element a moving x for which the lift-curves of Q_t in closure(Ñ_β̃) and closure(Ñ_b̃) differ (round9_q6 Step 4 / round9_q2 open 1). This is unchanged.
- **(O2)** Interior points with switching: show that a Teichmüller disc of h-symmetric curves in V_0, accumulating at an interior point Q of a piece E and exchanging two lifted sheets, forces Lock of the constant vertices x, h^{-1}x on the lifted family of E. Alternatively, show that (NoSw_Q) always holds for smooth totally geodesic V_0.
- **(O3)** Entry 82 ((Rig)), on which the whole chain depends.
- **(O4)** The cited inputs of Proposition K_w ("routine marking details"), and the reading (T4).

### round10_q6 §1 (verbatim): Lemma D3
## 1. Case (D3): what it forces (proved)

**Setting.** As in MS10 and (Tr). Q ∈ B_0 lies in a non-product stratum. B ⊂ Def(Q) is a small Aut(Q)-invariant ball. 𝒞° ⊂ (B∖{∏s_e=0}) × Δ_ε is the component of q^{-1}(𝒱) that contains the joining paths, and 𝒳 = closure(𝒞°). The other notation is Γ, K, Γ_x as in the task.

**Lemma D3.** Let α ∈ Γ ∖ KΓ_x. Suppose α fixes pointwise an irreducible component X′ of the germ of 𝒳 at (0,0), with dim X′ = 3. Then:
1. α ∉ K. So 𝒳 is reducible at (0,0), and X′ ≠ 𝒳.
2. Let [α] be the topological type of α, meaning its conjugacy class in Mod_g after identifying a nearby smooth fibre with S_g. Let M_g([α]) ⊂ M_g be the closed analytic locus of curves admitting an automorphism of type [α]. Then V_τ ⊂ M_g([α]) for every τ with |τ| < ε. In particular V_0 ⊂ M_g([α]).
3. Let p ∈ X′ be a point at which x is intact. Then F_x(p) ≅ F_{αx}(p). So on X′ the twins x and αx are locked.

*Proof.*
1. K is the kernel of the action on the connected set 𝒞°. Suppose α fixed 𝒳 pointwise. Then it would fix 𝒞° pointwise, so α ∈ K, which is a contradiction.
2. Fibres of X′ over τ.
   - X′ is irreducible of dimension 3, and X′ ⊄ {τ = τ_0} for any τ_0, since 3 > 2 = dim of a fibre of 𝒳. So by Krull every fibre X′_τ near τ = 0 has pure dimension 2.
   - X′ is a component of the closure of the interior set 𝒞°, so X′ ⊄ {∏s_e = 0}. The set X′ ∩ {∏ s_e = 0} has dimension ≤ 2. If it contained a whole 2-dimensional fibre component X′_τ, then by (R2) the closure of V_τ would have 2-dimensional boundary near Q_τ, which is false (B_τ = H_τ(B_0) is 1-dimensional). Hence X′_τ contains points of 𝒞° for every small τ.
   - Each such point lies in Fix(α). By (K4) (Aut(C_p) ≅ Stab_{Aut(Q)}(p), cited in R8-8 §0), the curve C_p has an automorphism, induced by α, of type [α].
   - So an open subset of the 2-dimensional V_τ lies in the closed analytic set M_g([α]).
   - M_g([α]) is the image of the Teichmüller space of the quotient orbifold, a closed subvariety (standard, cited from memory). V_τ is connected and smooth, hence irreducible, so V_τ ⊂ M_g([α]).
3. At p ∈ Fix(α) ∩ L_x, (K3) gives F_x(p) = F_x(αp) ≅ F_{α^{-1}x}(p). Also α^{-1}x = αx when α has order 2. In general, apply (K3) repeatedly along the ⟨α⟩-orbit of x: all labels in that orbit carry isomorphic curves at p. ∎

**Consequence for (D3).** A configuration of type (D3) needs:
- the whole family V_τ to consist of α-symmetric curves;
- 𝒳 to be reducible at (0,0), with the α-fixed sheet X′ different from at least one of the sheets that contain the transport families Ñ_β̃ and Ñ_b̃.

Suppose both transport families lie in X′. On X′ the labels in ⟨α⟩x carry isomorphic curves (item 3). So crossing the α-locus does not change the class F_x along either family, and the conclusion of (Tr) holds trivially for this α.

I have **not** excluded the remaining sub-case, in which the transport families lie in sheets other than X′. Total geodesy does not obviously exclude V_0 ⊂ M_g([α]): such loci are themselves totally geodesic (holomorphic isometric images of Teichmüller spaces of quotient orbifolds). So (D3) remains **open** in that sub-case. The smoothness of V_0 (in the coarse space) does not immediately rule out a reducible lift at an interior orbifold point either: the preimage of a smooth germ in a quotient C^n/G can be reducible.

---



## Prior results, part 4: round 11 (verbatim answer files, bookkeeping line removed; re-check what you use). NOTE: four round-11 files (round11_q2, q3, q8, q9) found that Lemma B1(a),(b) of round10_q3 (spliced in part 3) are FALSE as stated; use B1♭ / anchored sheets (round11_q9 §2.3) instead. Files written before that finding (round10_q3, round10_q7, and round11_q7, round11_q1, round11_q4 where they cite B1(a),(b)) should be read with 'transport sheet' replaced by 'anchored sheet'.

### round11_q9 (verbatim)
# round11_q9: check of chain steps 2(b)–2(d) (entries 99, 100), MS11 ⇒ MS8

**Plan/status.** I checked every item of the brief against the spliced proofs:
- round10_q1 §2 and §4;
- round10_q10 §6.3;
- round10_q3 §2;
- round9_q7 Lemmas S, J and Cor. J′;
- round9_q3 Lemma PT, Lemma P, Theorem X′.

**Verdict: correct after named repairs.** With MS11 worded as it is, the chain has a gap at two places: step 2(c), the transfer along a travel interval, and step 2(d), the MOV case of the endpoint. Both come from Lemma B1(a), which is false as stated. The repair is to replace "transport sheet of c̃" by "c̃-sheet" (defined in §2) in MS11 and in the induction claim; the repaired statement is called MS11♭ below. With that change every step 2(b)–(d) goes through. Everything else checks, modulo the inherited cited inputs and one inherited "routine marking detail" (§4).

Readings throughout: (R1), (R2) with H_0 = id, (Rig), and the notation of the task file. [Z] is the class in 𝔐 = M_{g_i,n_i}/S_{n_i}.

---

## 1. Item 1: Lemma S̃′ ⇒ Theorem X*_all ⇒ Cor. IMOV_all (entry 99). Correct.

### 1.1 Lemma S̃′ supplies exactly the hypothesis of Theorem X*_all
Theorem X*_all needs three things:
- a point Q_0 lying in the stratum of a piece E;
- a lift β̃ ⊂ L (the stratum locus) of a branch β of E;
- a sheet S, i.e. an irreducible component of the germ at 0 of q^{-1}(closure V_0), with S ⊃ β̃.

Its conclusion is S ∩ {∏ s_e = 0} = β̃ near 0.

Lemma S̃′ gives a component X̃_l of q^{-1}(closure V_0) ∩ B̃ with X̃_l ⊃ β̃ ∪ β̃′. Because B̃(J,3r) is taken to be a Milnor ball, X̃_l represents a germ component, i.e. a sheet.

I re-checked the proof of S̃′.
- **Step 1.** The ray g_s(X_n,q_n) lies on the Teichmüller disc F of the generating pair. The rotation by e^{-2iθ_n} from Lemma NH does not change the disc. F lies over V_0 by total geodesy, in the form already used in Lemma PA Step 5. (T4) is **not** needed, so S̃′ really replaces Lemma 1SS.
- **Minor repair in Step 1.** R should be the component of F^{-1}(gU ∩ (preimage of B̃(J,3r))) that contains the excursion arc, not the component of F^{-1}(gU). Otherwise f(R) need not lie in B̃, which is where the X̃_l live. The excursion arc lies in B(J,2r), so this changes nothing else.
- **Step 2.** The sets f^{-1}(X̃_l) are analytic subsets of the connected Riemann surface R and cover it, so one of them is R. Correct.
- **Step 3.** z̃^1 lies in X̃_l because X̃_l is closed in B̃. X̃_l ∩ {∏ s_e = 0} is pure 1-dimensional at z̃^1: no local component of X̃_l at z̃^1 can lie in the 1-dimensional set q^{-1}(B_0). Near z̃^1, q^{-1}(B_0) = β̃, because distinct lifted branches meet only at 0. So X̃_l contains a neighbourhood of z̃^1 in β̃, hence all of β̃, since β̃ ∩ B̃ is irreducible in a Milnor ball. Correct.

### 1.2 Cor. IMOV_all(a) at every transition in the stratum of an adjacent piece
- **J in the stratum of D (entering piece).** Apply X*_all to (D, coarse branch of β̃, S = X̃_l). Then β̃′ ⊂ S ∩ {∏ s_e = 0} = β̃ near 0. Both are irreducible representatives in B̃, so β̃′ = β̃.
- **J in the stratum of D′ (leaving piece).** Symmetric: apply X*_all to D′.
- **The label.** The label does not change, independently of S̃′. By (R-b), Σ_x = Σ_i = Σ_{x′}, so x′ = x.
- **Consequences.** The coarse branches coincide, so the transport families Ñ_β̃ and Ñ_β̃′ coincide, and so do their sheets. Persistence passes unchanged.
- **R(D)-points.** These are interior points of D. Entering and leaving lifts are lifts of branches of D; in the Gap A model they lie over E_k and σE_k. The same argument gives β̃′ = β̃. So the walk never switches lifted curve at an R(D)-point, and these transitions are trivial. Correct.
- **Endpoint.** S̃′ also holds with z̃^2 = z̃^∞ ∈ b̃ ∖ 0. If Q_0 were in the stratum of D^k or of E_b, then b̃ = β̃, so x would be intact and ≡ Y_0 along b̃, contradicting MERGE/MOV. So Q_0 satisfies (P). A genuine transition (β̃′ ≠ β̃) also satisfies (P), by contraposition of (a).
- **Small addition.** A puncture transition with β̃′_m = β̃_m needs nothing. MS11 requires β̃ ≠ b̃, so it is invoked only at transitions with β̃′_m ≠ β̃_m. The chain should say this explicitly.

### 1.3 Theorem X*_all where it departs from round9_q4
- **(i) The lift L̂ to ∏_w M_w.**
  - By Wolpert and Abikoff, the node curves of every limit L(w), under the disc's marking, are exactly those of P_1.
  - The vertex subsurfaces are invariant under the twist group Tw, so the labelling does not depend on twisting.
  - The labels are fixed once, by the chart Def(Q_0) at X̃_n near P̃_1. This is consistent in n, because all the lifts X̃_n converge to P̃_1 in one chart.
  - Locally, L̂ = Π_Z ∘ (limit of the chart lifts), so it is holomorphic.
  - The step L̂(𝔻) ⊂ Ê uses that Π(P̃_1) lies on Ê only.
  - Step 3 is correct as written: properness of L̄ is obtained through pr_j ∘ L̄, with no properness of pr_j on Ê needed, and Γ acts on the finite set Λ.
  - Step 4's new point is that the chart limit L̃ lands in the **specific** lift β̃, not only in ⋃_a aβ̃. It is proved correctly: the sets aβ̃ ∖ 0 are pairwise disjoint and closed in B ∖ 0, Ω minus a discrete set is connected, and L̃(0) = P̃_1.
  - Verified, modulo the cited T̄_g ↔ Def chart description.
- **(ii) The homological step.** The corrected sign argument is plausible. If L′ meets C′ only at the isolated point w*, then Z_n · C′ = −μ ≤ 0, while Σ k_j F_j · C′ > 0. But the text of round9_q4 §1.4, with (Int) and (Pos), is not spliced into my brief, so I cannot check it line by line.
- **It is not needed.** The maximum-principle route of round9_q3 (Step 5′ with Lemma P) proves X*_all directly from Steps 1–4. I checked this as follows.
  - Call a component of B̂ at ŝ_0 *of type β̃* if it maps onto β̃. These are the Ê_l. Let C be the union of all the other components; this includes components over aβ̃ ≠ β̃.
  - By Step 4, L̂_S(Ω) ⊂ ν^{-1}(β̃). The germ of ν^{-1}(β̃) at ŝ_0 is ⋃_l Ê_l, because ν is finite and β̃ is irreducible. A component over aβ̃ meets ν^{-1}(β̃) only in ν^{-1}(aβ̃ ∩ β̃) = {ŝ_0}.
  - Lemma P applies to (W, C, Ê_1, …, Ê_r). I re-checked its proof: Lemma M; the Mumford pull-back; the anti-ample cycle Z; D = mπ*C − Z effective with support C̃ ∪ E and D·E_j > 0; (RA); g = σ/s^N. It is correct given (Res), (Neg), (RA).
  - Steps 5′.2–5′.6 then go through verbatim: D̂_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, the maximum principle bounds |g ∘ D̂_n|, and |g| → ∞ along Ê_l at ŝ_0 gives the contradiction.
  - **So X*_all holds in every stratum, with or without the homological correction.**

---

## 2. Item 2: Lemma B1 is false as stated in (a) and (b), and the repair

### 2.1 Where the proof of B1(a) fails
The proof of B1(a) says: "So Ñ^1 meets {t = 0}, **where Ñ ∩ {t = 0} = b̃ ∖ 0**." Nothing justifies the bold claim.
- Ñ = Ñ_b̃ is the connected component of q^{-1}(N) containing b̃ ∖ 0.
- Its t = 0 slice lies in q^{-1}(b ∖ Q) = ⋃_a (ab̃ ∖ 0).
- Ñ can contain a second lift ab̃ ≠ b̃, joined to b̃ ∖ 0 through points with t ≠ 0.
- Then Ñ_{ab̃} = Ñ_b̃, and Ñ can have an irreducible component whose t = 0 slice lies in ab̃ and misses b̃ ∖ 0.
- The proof of (b) uses (a) ("every global component of Ñ contains such a germ"), so (b) fails too.

### 2.2 Local model 1 (chart-level, consistent with (R2); it refutes B1(a), (b) and the MOV endpoint step under MS11's weak notion)
**Coordinates and branches.**
- Def(Q) has coordinates (s_1, s_2, p, p′, u, …). The labels x and x′ = ax have the same type, with moduli coordinates p and p′; Y_0 ↔ 0, and Y_t ↔ t (to first order).
- a ∈ Aut(Q) acts by p ↔ p′ and u ↦ −u, and fixes s_1, s_2.
- Put b̃ := {s_1 = 0, p = s_2², p′ = 0, u = s_2} and ab̃ = {s_1 = 0, p′ = s_2², p = 0, u = −s_2}.
- These are distinct lifts with the same pattern {e_1}. Q is a puncture: s_2 ≢ 0.
- Along b̃, x is intact and **moving** (MOV), and x′ is constant ≅ Y_0.

**Transport.**
- A := {s_1 = 0, p = t + s_2(s_2+t), p′ = t, u = s_2 + t, s_2 ≠ 0}, and aA := {s_1 = 0, p′ = t + s_2(s_2+t), p = t, u = −(s_2+t), s_2 ≠ 0}.
- A ∩ {t = 0} = b̃ ∖ 0 and aA ∩ {t = 0} = ab̃ ∖ 0.
- For t ≠ 0, A and aA meet at the a-fixed point P_t = (s_2 = −t, p = p′ = t, u = 0), which has s_2 ≠ 0.

**Coarse smoothness.**
- q is injective on A_t, because A_t ∩ aA_t = {P_t} and P_t is a-fixed.
- s_2 is an a-invariant coordinate that restricts to a coordinate on A_t. So N_t := q(A_t) is a smooth coarse curve, a graph over s_2.
- H_t(q(b̃(s_2))) := q(A_t(s_2)) is a smooth trivialisation of N = ⋃_t N_t. The lift of Q_t is s_2 = 0, i.e. p = p′ = t, u = ±t. So |Aut(Q_t)| < |Aut(Q)|, which matches the known necessary conditions.

**Conclusions in the model.**
- Ñ_b̃ = A ∪ aA. It is connected (through P_t) and has two irreducible components, one of which has slice ab̃ ∖ 0. The pointwise stabiliser of b̃ does not contain a. So **(a) and (b) of B1 fail.**
- x is Y-persistent on aA: F_x = p = t ↔ Y_t, and x is intact. So **x is Y-persistent on a transport sheet of b̃ in MS11's sense, while x MOVES along b̃.**
- The model is chart-level only. It satisfies every chart-checkable constraint I know of, the same way the Gap B model of round10_q3 does. The point is that the step "B1(a) ⇒ the endpoint contradiction" is not a valid inference.

### 2.3 The repaired lemma (B1♭), proved
**Definition.** Let c̃ be a lifted branch. A *c̃-sheet* is an irreducible component of closure(Ñ_c̃) in B × Δ_ε whose t = 0 slice contains a non-empty open subset of c̃ ∖ 0.

**Lemma B1♭.** Let Ñ = Ñ_b̃.
- (a′) Every irreducible component Ñ^1 of Ñ maps onto N. Its t = 0 slice is a non-empty union of open subsets of finitely many lifts ab̃ ∖ 0, each with ab̃ ⊂ closure(Ñ) and with aS_b̃ = S_b̃.
- (a″) b̃-sheets exist. For generic p̃ ∈ b̃ ∖ 0 near 0, every germ component of q^{-1}(N) at (p̃, 0) lies in a b̃-sheet, and every b̃-sheet contains such a germ.
- (b′) The pointwise stabiliser Stab(b̃) permutes the b̃-sheets transitively.
- (c), (d) as in round10_q3. In (d), at product-type points every a ∈ Aut(Q) fixes x (Lemma PT). So persistence of x on an ab̃-sheet T is equivalent to persistence of a^{-1}x = x on the b̃-sheet a^{-1}T, and the weak and strong notions agree there.

*Proof.*
- **(a′).** Ñ^1 maps onto N by Remmert: N is a connected topological 4-manifold, hence an irreducible analytic set, and q is finite on Ñ^1. So t is non-constant on Ñ^1, and by Krull its slice is pure 1-dimensional. The slice lies in ⋃_a ab̃ ∖ 0, and these sets are pairwise disjoint and closed in B ∖ 0. The pattern is constant on the connected set Ñ (R7-4 Lemma 2(a)), which gives aS_b̃ = S_b̃.
- **(a″).** Near (q(p̃), 0) the set N is the whole of ℬ. Near p̃, q^{-1}(b) = b̃. So every germ component of q^{-1}(N) at (p̃, 0) has its t = 0 slice in b̃, lies in Ñ (q^{-1}(N) is locally connected at (p̃,0) ∈ Ñ), and lies in one global component, which is then a b̃-sheet. Conversely, a b̃-sheet contains a generic point (p̃, 0) of its slice in b̃ ∖ 0, and with it a germ component there.
- **(b′).** This is the original proof of (b), restricted to b̃-sheets, which is where it is valid. For generic p̃, Stab(p̃) equals the pointwise stabiliser of b̃ and permutes the germ components at (p̃, 0) transitively. Each element of it maps Ñ to itself. ∎

### 2.4 Gap A repair (R(D) added to Σ): correct
- R(D) is finite. It consists of the singular points of ξ̄^{-1}(closure D), which include the crossings E_k ∩ σE_k, together with the images of ramification points of the normalisation maps.
- With R(D) ⊂ Σ chosen before r, ξ^{-1}(K_D) is a disjoint union of compact pieces at positive mutual distance, each mapped by a covering onto K_D. So the marking lift stays on one lifted curve E with a fixed factor c.
- The new transitions are trivial by §1.2.
- The step "marking lift continuous along travel, label = c" is a routine marking detail of the K_w kind. I accept it as inherited; I did not re-derive it.

### 2.5 Base step: correct, and gives the strong notion
- Δ_Γ is of product type, so Aut(Γ) acts trivially on ∏ M_w (Lemma PT, steps 1–2) and Π_S is canonical.
- At every (p,t) ∈ Ñ_{β̃_1}, q(p) ∈ H_t(β_1 ∖ J_1) ⊂ ∂V_t (R2), and the pattern is constant. So x_1 = {i} is intact and F_{x_1}(p) = pr_i Π_S(p) = Y_t.
- Closedness passes this to closure(Ñ). So x_1 is persistent on **every** sheet, in particular on β̃_1-sheets. (B1(d) is not even needed.)

### 2.6 Product-type puncture junction (Lemma J / Cor. J′): correct; weak input suffices, strong output
**Input.**
- Let T be any sheet of Ñ_{β̃_m} on which x is persistent; it may be an aβ̃-sheet.
- T ⊂ q^{-1}(closure H((β∖J)×Δ_ε)), and by Lemma T(c) this lies in q^{-1}(ℬ^{(k(β))}) near (0,0). Also (0,0) ∈ T, since lifts of J_t accumulate there.
- So any germ component of T at (0,0) is a germ component 𝒲̃^a of q^{-1}(ℬ^{(k(β))}) with persistent vertex x.
- Lemma J never uses β̃ ⊂ 𝒲̃^a. Its step 1 uses only that Aut(Q) permutes the preimage germ components transitively, and step 2 uses only persistence on 𝒲̃^a.

**Conclusion.**
- By Lemma PT, x̂ = x.
- x = x_m is intact and constant ≅ Y_0 along b̃ = β̃′_m: this is the track's c′ = {x_m}. So (J1) and (J3) are excluded (Cor. J′), and (J2) holds: x is persistent on a germ component 𝒲̃″ ⊃ b̃ at (0,0).

**Strong output.**
- Take p̃ ∈ b̃ ∖ 0 generic and close enough to 0 that a representative of 𝒲̃″ is defined near (p̃, 0).
- Near (q(p̃), 0), ℬ = N, so the germ of 𝒲̃″ at (p̃,0) is a union of germ components of q^{-1}(N) at (p̃,0). By B1♭(a″) these lie in b̃-sheets.
- The persistence set is analytic: intactness is the pattern, and {[F_x] = [Y_t]} is analytic because [Y] is holomorphic. Persistence holds on an open subset of the irreducible component, hence on all of it (identity principle), and on its closure by continuity.
- So x is persistent on a **β̃′_m-sheet**.

I also checked Lemma J step 5 (Lemma S(b), continuity of F_x on L_x at q_t) and step 7. Both use (Rig) through Lemma S(a), and (Rig) is part of MS8's setting.

### 2.7 Transfer along a travel interval: correct for c̃-sheets, unsupported for MS11's notion
**Proof with the strong notion.**
- Let Ñ′^1 be a component whose closure is a β̃′_m-sheet with x_m ↔ c persistent.
- Π_S(Ñ′^1) is irreducible and 2-dimensional, inside (ξ×id)^{-1}(κ(D)), so it lies in one global component 𝒲̃.
- By B1♭(a′), and **because the sheet is a β̃′_m-sheet**, 𝒲̃_0 contains an open arc of Π_S(β̃′_m), which lies on the track's E. Hence 𝒲̃_0 ⊃ E.
- At J_{m+1}, take p̃ ∈ β̃_{m+1} ∖ 0 generic, with z = Π(p̃) ∈ E under the track's identification. Near p̃, Π is a finite open map from the stratum locus of Def(C_p̃), and q^{-1}(ℬ_G) ∩ L = (Π×id)^{-1}((ξ×id)^{-1}ℬ_G). Near (q(p̃),0), ℬ_G = κ(D), a 4-manifold.
- So the germ components of q^{-1}(N″) at (p̃,0) map onto the germ components at (z,0), and (z,0) ∈ 𝒲̃. Some germ component maps into 𝒲̃. By B1♭(a″) it lies in a β̃_{m+1}-sheet Ñ″^1, and by the identity principle Π(Ñ″^1) ⊂ 𝒲̃.
- c is constant (c ∉ M), so Lemma S(c) applies: persistence of c holds on all of 𝒲̃. Hence x_{m+1} ↔ c is persistent on Ñ″^1, intact by the constant pattern, and persistent on its closure.
- The output is again a **β̃_{m+1}-sheet**.

**Why the weak notion fails.** If the persistent sheet T at J_m is only an aβ̃′_m-sheet with ax_m ≠ x_m, then 𝒲̃ ⊃ Π(T) has its slice on āE, not on E. Equivalently, the persistent label on β̃′_m-sheets is a^{-1}x_m, by (K3), and the transfer carries the factor of the twin a^{-1}x_m. At J_{m+1} the track label is x_{m+1} ↔ c, so MS11's hypothesis there is not supplied.

So step 2(c) is **not** established from MS11 as worded. It is established from MS11♭.

### 2.8 Endpoint 2(d)
- **Product type: correct** with the weak input. Lemma PT makes Q_0 aligned, and Lemma J (J1) applies.
  - MERGE: [x] ≠ {x}.
  - Puncture-MOV: {x} ∈ M(κ(E_b)), using U_b ≠ ∅, (P) and step 7.
  - In both cases Y_t ∈ F on an open set, and (P) with PR-A gives that Y is constant: a contradiction.
- **Non-product, MERGE: correct even with MS11 as worded.** Let T be any sheet of Ñ_b̃ on which x is persistent. Then x is intact on T. The pattern is constant (= S_b̃) on the connected set Ñ_b̃, and T ∩ Ñ_b̃ ≠ ∅. So every edge at x lies in S_b̃, which contradicts MERGE.
- **Non-product, MOV: gap with MS11 as worded.** Local model 1 (§2.2) satisfies "x persistent on a transport sheet of b̃" through the ab̃-sheet aA, while x moves along b̃.
  - The chain's sentence "by Lemma B1(a), T ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0" is false for such T. One only gets F_{a^{-1}x} ≡ Y_0 along b̃, which is the endpoint twin and no contradiction.
  - With MS11♭ the step is correct. T is a b̃-sheet, so its slice contains an open subset of b̃ ∖ 0 on which x is intact and F_x ≅ Y_0. The pattern is constant on b̃ ∖ 0, and F_x is holomorphic on L_x ⊃ b̃. The identity theorem in 𝔐 along the normalisation of b̃ gives [F_x] ≡ [Y_0] along b̃.
  - This contradicts MOV. Here MOV means d(F_x(z̃^∞), Y_0) = η with 0 < 2η < min d(σY_0, Y_0) by (b1), so [F_x(z̃^∞)] ≠ [Y_0].

---

## 3. Item 3: interaction with the repairs (R-a)–(R-d): nothing needs a common sequence
- Each use of S̃′ in 2(a)/(b) concerns one transition.
  - Its witnessing sequence comes from the n′ of that transition's recurrent type τ.
  - The data are normalised by a global a ∈ Aut(J). Since a permutes components, a^{-1}X̃_l contains walk n's own pair (β̃, β̃′).
- Theorem X*_all is a pure t = 0 statement and involves no walks.
- The induction 2(c) uses:
  - the per-transition sheet data;
  - the labels along travel intervals of the **single fixed walk n ≥ N**: canonical lifts for that n, Σ_i = Σ_{x_m}, and the marking lift on E;
  - global analytic objects (𝒲̃, κ(D)).
  None of these refers to other walks.
- The endpoint uses the n′ of type τ_end only to obtain b̃ and the MERGE/MOV dichotomy.
- Shrinking ε finitely many times is harmless. A c̃-sheet for the old ε contains the germ at a generic (p̃,0), hence a c̃-sheet for the new ε, and persistence passes by the identity principle.

So no common subsequence is needed. This confirms round10_q10's remark.

---

## 4. Item 4: other points in 2(a)–(d)
- **Puncture transitions with β̃′_m = β̃_m** are trivial and must be excluded from the MS11 invocations, since MS11 requires distinct branches. This is a wording point only.
- **Inherited, not re-derived:**
  - the marking-continuity detail along travel intervals (round10_q3 §2.1, "routine");
  - the cited inputs: Lemma PA, Lemma NH, (Fl), (Prop), Kerckhoff, Maskit, the T̄_g/Def chart description, Wolpert/Abikoff, (Res)/(Neg)/(RA), Krull, Remmert, Milnor conic structure.
- **(T4)** is not needed by the chain: S̃′ replaces Lemma 1SS.
- **The step "Goal ⇐ MS8 + (Rig) + entry 19"** is unaffected.

---

## 5. Corrected missing statement and corrected chain
**MS11♭ (replaces MS11; same setting and data, including "Y non-constant", (P) and (S)).**
- *Hypothesis:* x is Y-persistent on some **β̃-sheet**, i.e. a component of closure(Ñ_β̃) whose t = 0 slice contains a non-empty open subset of β̃ ∖ 0.
- *Conclusion:* x is Y-persistent on some **b̃-sheet**.

**Chain with MS11♭.** Induction claim: x_m is Y-persistent on some β̃_m-sheet.
- Base: §2.5.
- Interior transitions and R(D)-points: §1.2.
- Product-type puncture junctions: §2.6, which outputs a β̃′_m-sheet.
- Non-product puncture junctions with β̃′_m ≠ β̃_m: MS11♭ (§5).
- Transfer: §2.7.
- Endpoint: §2.8.

So **MS11♭ + entries 19, 24, 84–87, 97–100 (with B1 replaced by B1♭) ⇒ MS8**, and MS8 + (Rig) ⇒ the goal.

**Relation between MS11 and MS11♭.** Neither formally implies the other: MS11♭ has a stronger hypothesis and a stronger conclusion. MS11 alone does not suffice, by §§2.7–2.8 and model 1. MS11♭ is still vacuous whenever the problem's claim holds. Its failure configurations are the same twin configurations as before: an a ∈ Aut(Q) moving x, together with a stabiliser jump of the transported branch at t ≠ 0, as in model 1.

---

## 6. Summary
**Proved / checked:**
- Lemma S̃′ (with the minor repair to R) gives exactly the sheet hypothesis of Theorem X*_all, without (T4).
- Theorem X*_all holds in every stratum. Its new lifting step is checked. The homological correction is plausible but not checkable from the brief, and it is superseded by the Lemma P / maximum-principle route, which I verified for type-β̃ components.
- Cor. IMOV_all(a)–(c) is correct, including at R(D)-points and at the endpoint. So (P) holds wherever MS11 is invoked.
- The Gap A repair, the base step, the product-type junction step (Lemma J / Cor. J′, with weak input and strong output), the product-type endpoint and the non-product MERGE endpoint are correct.
- No common witnessing sequence is needed.

**Found false:**
- Lemma B1(a) and (b) of round10_q3, as stated. Explicit chart-level model in §2.2.
- Corrected version: B1♭ (§2.3), proved.

**Gap at named steps (with MS11 as worded):**
- 2(c), the transfer along a travel interval;
- 2(d), the non-product MOV endpoint.

Both are closed by replacing "transport sheet" by "c̃-sheet", i.e. MS11 by MS11♭.

**Verdict:** the chain proves MS8 from MS11♭ (with entries 19, 24, 84–87, 97–100, B1 replaced by B1♭), modulo the inherited cited inputs and marking details. It does **not** prove MS8 from MS11 exactly as stated.

**Open:**
- MS11♭ itself;
- entry 82 (Rig);
- the inherited inputs listed in §4.

**Status: proved (the corrected derivation MS11♭ ⇒ MS8); not proved (MS11 ⇒ MS8 as worded); open (MS11♭, (Rig)).**


### round11_q3 (verbatim)
# round11_q3 answer

Status: MS11 is NOT proved and no counterexample is given. I found and repaired a flaw in the chain: Lemma B1(a)/(b) is wrong as stated, so the chain's endpoint step needs "proper" sheets (§2). I verified Mechanism D, steps 1–3, with one correction (§1). Using Theorem N, I proved that the lift-curve edges and the interior/IMOV edges never change the persistent label (§3). What is left is two explicit edge types, both coming from automorphisms that fix a curve pointwise (§3.6). There is a partial result, Corollary 3.5. Lists are in §4.

Plan followed: (1) check Mechanism D (connectedness of D = X ∩ {N=0}); (2) handle the edges with Theorem N (R8-3, PROVED under (Rig), generic t), which keeps the exact label; (3) find exactly which edges can still change the label; (4) check the chain.

## 1. Mechanism D, steps 1–3: verified (with one correction; step 4's edge list is revised in §3)

Setting of MS11. Let S be the component of (S). Let X be a 3-dimensional irreducible component of the germ of q^{-1}(closure 𝒱) at (0,0) ⊂ Def(Q) × Δ_ε with S × {0} ⊂ X (exists: the germ is pure 3-dimensional, since 𝒱 is a 3-manifold dense in closure(𝒱) and q is finite; the irreducible 2-dim set S × {0} lies in the union of the finitely many components, hence in one). N := ∏_e s_e, D := X ∩ {N = 0}.

(D1) D has pure dimension 2 (Krull: N ≢ 0 on X since X contains points over 𝒱, and N(0,0) = 0). No component of D lies in {t = 0}, because X ∩ {t=0} ∩ {N=0} ⊂ q^{-1}(B_0) is at most 1-dimensional.

(D2) Every component T of D is a transport sheet of a lifted branch c̃ with c̃ × {0} ⊂ T. Proof: T ∩ {t = 0} is a curve germ through (0,0) (dimension drops by exactly one), contained in q^{-1}(B_0), hence a union of lifted branches c̃ × {0}. Near (Q,0), closure(𝒱) ∖ 𝒱 = H(B_0 × Δ_ε) is the disjoint union of the lift-curve set {Q_t} and of the sets N_c = H((c ∖ Q) × Δ_ε) over the branches c of B_0 at Q; these are pairwise disjoint and each is relatively open and closed in the complement of the Q_t-curve. T minus the (at most 1-dimensional) preimage of the Q_t-curve is connected (T is irreducible), lies in q^{-1}(⋃ N_c), and contains c̃ ∖ 0 × {0} in its closure... more precisely it contains points of c̃ ∖ 0 × {0}; hence it lies in the connected component Ñ_c̃ of q^{-1}(N_c). So T ⊂ closure(Ñ_c̃); both are 2-dimensional and T irreducible, so T is an irreducible component, i.e. a transport sheet of c̃. ∎

(D3) Since β̃, b̃ ⊂ S, D contains a sheet T_β ⊃ β̃ × {0} and a sheet T_b ⊃ b̃ × {0}.

(D4) Grothendieck's connectedness theorem (cited from memory, SGA 2 XIII 2.1 / Hartshorne "Complete intersections and connectedness" Prop. 2.1 + 3.1 form): if A is a complete local noetherian domain of dimension d and f ∈ m, then Spec(A/f) ∖ {m} is connected when d ≥ 3. The analytic local ring of the irreducible germ X is a domain whose completion is a domain (analytic local rings are excellent and an irreducible analytic germ is analytically irreducible). Hence D ∖ {(0,0)} is connected; equivalently the graph whose vertices are the components of D, two being adjacent when they share a curve germ through (0,0), is connected. (Connectedness in dimension 1 of D: components can be chained so that consecutive ones meet in dimension ≥ 1.)

**Correction 1.** The sheet on which x is assumed persistent in MS11 need not lie in X: (S) only places β̃, b̃ in S, and q^{-1}(closure 𝒱) may have several 3-dimensional components through S × {0} (e.g. X and gX with g fixing S pointwise; local model: Def ∋ (a,b), g: b ↦ −b, quotient coordinate c = b², 𝒱-sheet {c = t²} lifts to b = ±t). Lemma 3.4 below handles this, at the price of relabelling x by an element of Stab_pt(β̃). (The connectedness in (D4) is for small conic representatives: if two sheets meet away from the origin, the curve selection lemma gives a common curve germ through (0,0).)

## 2. A flaw in Lemma B1(a)/(b) (round10_q3), and its effect on the chain and on MS11

Lemma B1(a) asserts that every irreducible component Ñ^1 of Ñ_b̃ meets {t = 0} in a non-empty open subset of b̃ ∖ 0; its proof says "Ñ ∩ {t = 0} = b̃ ∖ 0". That equality is not justified: Ñ_b̃ is the connected component of q^{-1}(N) containing b̃ ∖ 0, and it may also contain σb̃ ∖ 0 for σ ∈ Aut(Q) with σb̃ ≠ b̃, the connection being made at t ≠ 0 through points with extra automorphisms.

**Chart-local model (consistent with the chart data).** Coordinates (z, w, …) on Def(Q), where z is a smoothing parameter s_e of an edge unpinched along b (b̃ ∖ 0 ⊂ {z ≠ 0}), σ ∈ Aut(Q) acts by w ↦ −w (fixing z), b̃ = {w = z} and σb̃ = {w = −z} (two distinct lifts of the same coarse branch b; other coordinates frozen). Downstairs coordinates (z, u = w², t). Let the transported coarse branch be N = {u = (z + t)²}, the graph of a function of (z,t), hence a topologically trivial family of punctured discs as required by (R2). Then
 q^{-1}(N) = T_1 ∪ σT_1, T_1 = {w = z + t}, σT_1 = {w = −z − t},
and T_1 ∩ σT_1 = {w = 0, z = −t}, which lies in the region z ≠ 0 for t ≠ 0. So q^{-1}(N) is connected, Ñ_b̃ = T_1 ∪ σT_1, and its component σT_1 meets {t = 0} only in σb̃. (At time t the boundary curve H_t(b) passes through the point z = −t with the extra automorphism σ; nothing in the chart data forbids this.)

Consequences.
- B1(a) is false as stated in this model, and B1(b) (transitivity of Stab_pt(b̃) on components) fails too: σT_1 is not a Stab_pt(b̃)-translate of T_1. B1(c) and B1(d) are unaffected (B1(d) at product type: every α fixes the label, Lemma PT).
- **Chain step (d) and MS11's parenthetical conclusion.** If the sheet T delivered by MS11 is of the type σT_1 (meets t = 0 only in σb̃), persistence of x on T gives, at t = 0, that x is intact with F_x ≡ Y_0 along σb̃, i.e. that σ^{-1}x is intact with F ≡ Y_0 along b̃. This does not contradict MERGE/MOV of x along b̃ unless σ fixes x. So the step "MS11 ⇒ contradiction at the endpoint" is not valid with the current definition of transport sheet.
- **Repair (proposed, checked against the chain's other steps that I read).** Call a transport sheet T of c̃ *proper* if c̃ × {0} ⊂ T. Read MS11's hypothesis and conclusion with proper sheets. Then the endpoint step is valid: x persistent on a proper sheet T of b̃ gives at t = 0 that x is intact with F_x ≡ Y_0 on b̃ ∖ 0 (closed conditions, b̃ × {0} ⊂ T), contradicting MERGE and MOV. The transfer step of the chain (round10_q3 §2.2 item 3) produces a global component containing a germ at (p̃, 0), p̃ ∈ β̃_{m+1} generic, whose t = 0 slice lies on β̃_{m+1}; that component contains β̃_{m+1} × {0}, so it is proper. The base step is unaffected (product type). I have not re-checked Lemma J / Cor. J′ for properness of the sheet they produce; this is a point to verify.

## 3. New results on the sheet graph of D

Standing assumptions for §3: the MS11 setting, (Rig), Y non-constant, so Theorem N (R8-3 §3, PROVED there under (Rig)) is available at every generic t (t outside a countable set Z). Notation: P(r) := {e ∈ E(G_Q) : s_e(r) = 0}; P(T) := the pattern at generic points of a sheet T (constant on T minus the preimage of the lift-curve, by R7-4 Lemma 2(a)); Π(T) := the set of labels persistent on T. By (K3), Π(hT) = hΠ(T) for h ∈ Aut(Q).

### Lemma 3.1 (every sheet of D is puncture-type). Proved, using Theorem X*_all.
For every sheet T of D, P(T) ≠ E(G_Q).

*Proof.* q(X) is an irreducible 3-dimensional germ of closure(𝒱) at (Q,0) (Remmert), so a local irreducible component 𝒮 of closure(𝒱). By the topological description of local components (R8-1 Lemma S, applied to closure(𝒱) with the homeomorphism H of pairs from (R2)), 𝒮 = H(Σ × Δ_ε) for a local sheet Σ of closure(V_0) at Q, so 𝒮 ∩ {t = 0} = Σ (H_0 = id). Then S × {0} ⊂ X_0 ⊂ q^{-1}(Σ), so q(S) = Σ, and q^{-1}(Σ) = ⋃_{g∈Aut(Q)} gS (components of the preimage of an irreducible germ are permuted transitively). By (D2), T ∩ {t = 0} ⊃ c̃ × {0} with c̃ a boundary branch of some gS, and P(T) = P(c̃). If P(c̃) = E(G_Q), then c̃ is a lifted branch of a piece containing Q in its stratum, and Theorem X*_all (round10_q1 §2: a sheet containing such a branch has no other boundary curve through 0) applied to gS contradicts gβ̃ ≠ gb̃ ⊂ gS (two distinct boundary curves). ∎

### Proposition 3.2 (edges along curves not in {t = 0}). Proved.
Let T_1 ≠ T_2 be sheets of D sharing an irreducible curve germ C through (0,0), C ⊄ {t = 0}, and let x ∈ Π(T_1). Then x ∈ Π(T_2), unless the following configuration (γ°) occurs: T_2 = gT_1 for some g ∈ Aut(Q) fixing C pointwise, P(T_1) = P(T_2) = gP(T_1), and for all t in a co-countable subset of a punctured disc, at the points r ∈ C_t the label x is intact, F_x(r) ≅ Y_t, and x is non-constant along T_{2,t} (IMOV in Theorem N), the point q(r) lying in the stratum of the coarse piece of T_1. In case (γ°), gx ∈ Π(T_2).

*Proof.* 𝔛 := {(p,t) ∈ D : p ∈ L_x, [F_x(p)] = [Y_t]} is closed analytic, and T_1 ⊂ 𝔛. For small t ≠ 0, C_t is finite and non-empty. Let t be generic and r ∈ C_t, R := q(r) ∈ B_t. Then x is intact at r and F_x(r) ≅ Y_t. The chart Def(Q) near r is a universal deformation of R, so Theorem N applies at R with the lift r, the copy x and any branch of T_{2,t} at r (a lifted branch of B_t at R): x is intact along it and either STAY (F_x ≡ Y_t on it) or IMOV (P(T_2) = P(r), F_x non-constant on it); here the pattern of the branch minus r is P(T_2).
- If STAY occurs for uncountably many t, then T_2 ∩ 𝔛 contains curve germs in uncountably many t-fibres; an analytic set of dimension ≤ 1 cannot (countably many components, each in one fibre or finite over t), so T_2 ∩ 𝔛 is 2-dimensional and T_2 ⊂ 𝔛: x ∈ Π(T_2).
- Otherwise IMOV holds for t in a co-countable set. Two sub-cases at such (r,t):
  - (B1) the germs of T_{1,t} and T_{2,t} at r map to different coarse germs at R. Then R ∈ D_{2,t} (stratum part, since P(r) = P(T_2)) is either in closure(D_{1,t}) with D_1 ≠ D_2, or a point where closure(D_{2,t}) has ≥ 2 local branches. Both sets are H_t(F) for a finite F ⊂ D_2 (H_t is a stratum- and piece-preserving homeomorphism, PR-B, and the number of local branches of a curve is topological). If B1 holds for t_n → 0 with r_n ∈ C_{t_n}, pass to R_{t_n} = H_{t_n}(f) with fixed f ∈ F; then H_{t_n}(f) → f and q(r_n) → Q, so Q = f ∈ D_2, i.e. T_2 is interior-type, contradicting Lemma 3.1.
  - (B2) otherwise, for t in a co-countable subset of a smaller punctured disc, both germs map to the same coarse germ, so (transitivity of Stab(r) on the components of the preimage of an irreducible germ) T_{2,t}-germ = g_t·T_{1,t}-germ with g_t ∈ Stab(r). Some g occurs for uncountably many t; then T_2 ∩ gT_1 is 2-dimensional, so T_2 = gT_1, and Fix(g) ∩ C is infinite, so C ⊂ Fix(g). P(T_1) ⊂ P(r) = P(T_2) = gP(T_1) forces equality. gx ∈ gΠ(T_1) = Π(T_2) by (K3). This is (γ°). ∎

*Remark (strengthening inside (γ°)).* Since g fixes r, every label g^k x is a Y_t-copy at r (F_{g^kx}(r) ≅ F_x(g^{-k}r) = F_x(r)), so Theorem N applies to each of them along both T_{1,t} and T_{2,t}; in particular if g changed the pattern (gP(T_1) ≠ P(T_1)) then IMOV would be impossible at r for every label and x ∈ Π(T_2) would follow — which is why (γ°) requires gP(T_1) = P(T_1). (Consequence: the "same coarse branch, twin MERGE" variant of the §2 model is impossible inside D. Suppose b̃ = σβ̃ with σ an involution, x ∈ Π(T_1) for a proper sheet T_1 of β̃, x merged along b̃ at t = 0 (MERGE endpoint), and T_1, σT_1 meet along a curve C ⊂ Fix(σ) not in {t = 0}. Then σx is merged along β̃ = σb̃, i.e. some edge at σx is not in P(T_1) = P(β̃). At r ∈ C_t (generic t), σx is an intact Y_t-copy (σ fixes r), and it is merged along the branch of T_{1,t} at r — contradicting Theorem N. So in this variant the twin edge must be a (β)-edge, C = c̃ × {0}.)

### Lemma 3.3 (edges along t = 0 curves). Proved.
If T_1 ≠ T_2 share C = c̃ × {0}, then T_2 = σT_1 with σ ∈ Stab_pt(c̃), and σΠ(T_1) = Π(T_2).

*Proof.* For generic p ∈ c̃ ∖ 0, Stab(p) = Stab_pt(c̃), q near (p,0) is the quotient by Stab(p), and the germ of N_c at (q(p),0) is irreducible (it is a topological 4-manifold). So the germs of q^{-1}(N_c) at (p,0) are hG_0, h ∈ Stab(p). T_1 ⊃ h_1G_0, T_2 ⊃ h_2G_0, hence T_2 = h_2h_1^{-1}T_1 (identity principle for irreducible germs sharing an open set). ∎

### Lemma 3.4 (Correction 1 made precise). Proved.
The proper sheets of β̃ (§2) are exactly the hT*, h ∈ Stab_pt(β̃), for any one of them T* (same proof as 3.3). Hence if x is persistent on some proper sheet of β̃, then hx ∈ Π(T_β) for the proper sheet T_β ⊂ D of (D3) and some h ∈ Stab_pt(β̃).

### Corollary 3.5 (partial result toward MS11, proper reading).
In the setting of MS11 with proper sheets, suppose every element of Aut(Q) that fixes pointwise a curve germ through (0,0) contained in q^{-1}(closure 𝒱 ∖ 𝒱) — more precisely: the elements h of Lemma 3.4, σ of Lemma 3.3 and g of (γ°) arising in D — fixes the label x. Then x is persistent on a proper sheet of b̃, i.e. the conclusion of MS11 holds.

*Proof.* Start at T_β with x ∈ Π(T_β) (Lemma 3.4 and h x = x). Walk along a path of the connected sheet graph (D4) to T_b. At each edge the persistent label is preserved (Prop. 3.2) or replaced by its image under an element that fixes the shared curve pointwise (Lemma 3.3, case (γ°)), which by hypothesis fixes x. So x ∈ Π(T_b), and T_b ⊃ b̃ × {0}. ∎

### 3.6 What remains: the (β)-twin edge (why I could not close it)
After 3.1–3.4 the only label-changing edges are (β)-edges T_1 — σT_1 along c̃ × {0}, σ ∈ Stab_pt(c̃), and (γ°)-edges. At a (β)-edge: since c̃ × {0} ⊂ T_1 ∩ σT_1, P(T_1) = P(c̃) = σP(T_1), so y := σ^{-1}x is intact along T_1 as well (x ∈ Π(T_2) ⟺ y ∈ Π(T_1)). Via Π_{P} the sheet T_1 maps into a component W_1 of the lifted family of the piece of c (round8_q2 Lemma U). At t = 0, F_y = F_x∘σ ≡ Y_0 on c̃, so y ∉ M_{W_1} and y is a constant vertex of every fibre of W_1, with a holomorphic value φ(t), φ(0) = Y_0. The failure configuration is exactly φ ≢ Y, i.e. y ∉ Π(T_1): the two twin components of the curves over c (Y_0 and Y_0 at t = 0, swapped by σ which fixes c̃ pointwise) deform to (Y_t, φ(t)). Theorem N is silent here (φ(t) is not a Y_t-copy), Krull/connectedness is already used up, and Theorem X*_all does not apply (puncture-type sheets). Total geodesy would have to enter through Fix(σ) ∩ S (planner's Lemma TG); I did not obtain a usable statement. So this is the precise remaining obstruction for MS11 inside one 3-fold component X: **(β)-twin edges, and (γ°)-edges** (the latter: an interior self-crossing of a lifted piece at a g-fixed point, with g^{-1}x moving along T_1).

Remark on Corollary 3.5: it is PARTIAL (an extra hypothesis of the type excluded by the task), but it is strictly weaker than (NT): only automorphisms of Q fixing pointwise a curve of the lifted boundary family 𝓑 near 0 matter, and Lemma 3.1 / Prop. 3.2 remove the lift-curve edges (α) and the IMOV/interior obstruction entirely.

## 4. Summary

**Proved here** (under the run's readings (R1), (R2); §3 also uses (Rig) and "Y non-constant" through Theorem N; cited facts: Grothendieck connectedness, Remmert, curve selection, Kuranishi universality at nearby points, all from memory):
1. Mechanism D, steps 1–3 (§1, D1–D4). D = X ∩ {∏s_e = 0} has pure dimension 2. Its components are transport sheets that contain their t = 0 branch. Its sheet graph is connected. Correction: the hypothesis sheet of MS11 need not lie in X (handled by Lemma 3.4).
2. Lemma B1(a)/(b) of round10_q3 is false as stated: a transport family can contain sheets that meet {t = 0} only in a different lift σb̃ (explicit chart model in §2). As a result, chain step (d) ("MS11 ⇒ contradiction at the endpoint") is invalid with the current definition of sheet. Repair: read MS11's hypothesis and conclusion with *proper* sheets (sheets containing c̃ × {0}). With that reading, step (d) is valid, and so is the transfer step of round10_q3 §2.2(3).
3. Lemma 3.1: every sheet of D is puncture-type (uses Theorem X*_all).
4. Proposition 3.2: along a shared curve not contained in {t = 0}, persistence of the *same* label passes, except in configuration (γ°). In particular lift-curve edges (α) never change the label, and IMOV/interior edges cannot occur. This replaces the planner's step 4(α) and corrects 4(γ).
5. Lemma 3.3: a (β)-edge is T_1 — σT_1 with σ ∈ Stab_pt(c̃). Lemma 3.4: proper sheets of β̃ form one Stab_pt(β̃)-orbit.
6. Corollary 3.5 (PARTIAL): MS11 (proper reading) holds whenever the automorphisms of Q that fix pointwise a curve of the lifted boundary family (the h, σ, g above) fix x.
7. The "same coarse branch, twin MERGE" variant with a dominating fixed curve is impossible (remark after Prop. 3.2).

**Not proved:**
- MS11 itself, in either reading.
- That Lemma J / Cor. J′ (round9_q7), used at product-type junctions of the chain, produce *proper* sheets. I did not re-check this. It is needed for the repaired chain.
- Theorem N and Theorem X*_all were used as PROVED by earlier rounds; I did not re-prove them.

**Open (precise):**
- (O1) (β)-twin edges. Let c̃ be a boundary branch of a translate gS with σ ∈ Stab_pt(c̃), and let T_1, σT_1 ⊂ D be sheets with x ∈ Π(T_1). Show that σ^{-1}x ∈ Π(T_1), i.e. that the constant twin value φ(t) of §3.6 equals Y_t, or that the composite of such relabellings along some path to T_b lies in Stab(x)·Stab_set(b̃). Total geodesy has to enter here, presumably through Fix(σ) ∩ S.
- (O2) (γ°)-edges: a self-crossing of a lifted piece, at points interior to its stratum, through g-fixed points C_t → 0, with g^{-1}x moving along T_1.
- (O3) The global input (Rig) (entry 82), unchanged.

No counterexample to MS11 or to the problem is claimed. The chart-local models (§2; §3.6) only show that chart-local reasoning cannot close (O1).


### round11_q7 (verbatim)
# round11_q7: attempt on MS11 (Mechanism D, connectedness of the boundary divisor)

**Status: PARTIAL. MS11 is NOT proved in full, and no counterexample is given.**

What is proved here (from (R1), (R2), (Rig), "Y non-constant", the prior lemmas named below, and standard facts cited from memory):
- **Theorem D.** Under MS11's hypotheses, the old failure shapes (F1) and (F2) of round10_q7 Cor. Q2 collapse into one shape. Q-factoriality is no longer needed. There is always a path of transport sheets from a sheet of β̃ to a sheet of b̃ inside a single 3-fold component X ⊃ S × {0}. Along this path the persistent label set is preserved, except at two kinds of steps:
  - **(B-pure)** two sheets T, σT of the same lifted branch c̃, with σ in the pointwise stabiliser Stab(c̃), meeting only in {t = 0}. Here the label set is twisted by σ.
  - **(IMOV_Q)** a persistent IMOV event near Q at all times outside a countable set.
- **Corollary D′.** MS11 holds whenever (IMOV_Q) fails and the composite twist (defined precisely in §4) maps x into Stab(b̃)·P(T^b). In particular it holds when every σ met at a (B-pure) step, and the initial σ at β̃, fixes the label it acts on.
- **The label issue of (F2)** (point 1 of the brief) is exactly a (B-pure)-type step at β̃ itself.
- **(F1)** (point 2) disappears as a separate case.
- A local model shows that (B-pure) steps with a label-moving σ can occur *inside one* 3-fold component, with all chart-checkable hypotheses satisfied. So the remaining obstruction cannot be removed by an argument local to a generic point of c̃.

Open: (B-pure) twists and (IMOV_Q). See §7.

Readings and notation are as in the brief: (R1), (R2) with H_0 = id; Def(Q), q, s_e, N := ∏_{e∈E(G_Q)} s_e; labels, intactness, F_y, L_y; transport families Ñ_c̃; transport sheets; lift-curves λ ⊂ 𝒥 = 𝒥_Q; P(T) and Λ(λ) as in round10_q7 §1. B and ε are chosen small, so that:
- the global irreducible components of every analytic set used below, in B × Δ_ε, are the components of its germ at (0,0);
- distinct lifted branches meet only at 0.

There are finitely many such sets, so this is a finite list of conditions.

---

## 0. Inputs used (re-checked as used; not re-derived)
- **(TN)** R8-3 Theorem N, in the form quoted in round9_q1 §0. Y is non-constant and (Rig) holds. There is a countable Z ⊂ Δ such that for t ∉ Z the following holds. Let P ∈ B_t, let p be a lift, let y be a label with F_y(p) ≅ Y_t, and let c̃ be a lifted branch of B_t through p. Then y is intact along c̃ and exactly one of the following holds:
  - STAY: F_y ≡ Y_t along c̃;
  - IMOV: P lies in the stratum of the piece of c̃, and F_y is non-constant along c̃.
- **Lemma B1** (round10_q3).
  - (a) Every component of Ñ_c̃ maps onto N_c, and its t = 0 slice is open in c̃ ∖ 0.
  - (b) Stab(c̃), the pointwise stabiliser, permutes the components of Ñ_c̃ transitively.
  - (c) P(σT) = σP(T). This is (K3): F_y(σp) ≅ F_{σ^{-1}y}(p).
- **Lemmas I0, I1, I2** (round10_q7 §1).
  - I0: every sheet contains a lift-curve.
  - I1: λ ⊂ T implies P(T) ⊆ Λ(λ).
  - I2: if T is of boundary type and λ ⊂ T, then Λ(λ) ⊆ P(T).
- **Krull's principal ideal theorem** (analytic form), **Remmert's proper mapping theorem**, the identity theorem.
- **Grothendieck's connectedness theorem** (SGA 2, Exp. XIII, Thm 2.1; cited from memory). Let A be a complete Noetherian local domain of dimension d, and let I be generated by r elements with r ≤ d − 2. Then the punctured spectrum Spec(A/I) ∖ {m} is connected.
  - *Analytic translation used.* Let X be an irreducible germ of complex space of dimension 3, and h a function vanishing at the point. Then the irreducible components D_1, …, D_m of the germ X ∩ {h = 0} form a connected graph, where D_i and D_j are adjacent when the germ D_i ∩ D_j has dimension ≥ 1.
  - *Justification (standard, cited).* Analytic local rings are excellent and Henselian. For an irreducible germ the normalisation is local, so the completion Â of O_{X,0} is a domain of dimension 3. The minimal primes of Â/(h) correspond to the analytic components D_i, because irreducible analytic germs stay irreducible after completion, by the same argument. Also dim Â/(p_i + p_j) = dim(D_i ∩ D_j). Apply the theorem with r = 1 ≤ 3 − 2. If the graph were disconnected, the punctured spectrum would be the disjoint union of the closed sets coming from the two groups of components, and these would meet only at m.

---

## 1. Lemma D1 (a 3-fold component through S, and its boundary divisor) — proved

Put 𝒳 := q^{-1}(closure 𝒱) ∩ (B × Δ_ε), a pure 3-dimensional analytic set.

**Lemma D1.** Let S be the component given by (S).
- (a) Some irreducible component X of 𝒳 contains S × {0}.
- (b) N ≢ 0 on X, and D := X ∩ {N = 0} has pure dimension 2. No component of D lies in {t = 0}.
- (c) Every irreducible component T of D is a transport sheet of a lifted branch c̃ ⊂ X_0 := X ∩ {t = 0}, and T ∩ {t = 0} = c̃ as germs.
- (d) For every lifted branch c̃ ⊂ X_0, in particular for β̃ and b̃, D contains a sheet of c̃ as a component.

*Proof.*
- (a)
  - Let p ∈ S be a generic point: a smooth point of S, with N(p) ≠ 0, lying on no other component of q^{-1}(closure V_0).
  - By (R2), closure(𝒱) ∩ (M_g × Δ) = H(V_0 × Δ) = 𝒱, which near (q(p), 0) is a 3-dimensional manifold. So its germ there is irreducible.
  - Let W be a local component of 𝒳 at (p,0). By Remmert, q(W) is a 3-dimensional germ in the irreducible germ of 𝒱, hence all of it. So t ≢ 0 on W.
  - By Krull, W_0 := W ∩ {t = 0} has pure dimension 2 at (p,0). By (R1), W_0 ⊂ q^{-1}(closure V_0), which near p is the smooth germ S. So W_0 = S near p.
  - The global component X of 𝒳 containing W therefore contains a non-empty open subset of S × {0}. Since S is irreducible, X ⊃ S × {0}.
  - By the choice of B and ε, X is a germ component at (0,0), and (0,0) ∈ X.
- (b)
  - q(X) is a 3-dimensional irreducible subset of closure 𝒱. The boundary part H(B_0 × Δ) has dimension 2, so the generic points of q(X) lie in 𝒱 ⊂ M_g × Δ, and N ≢ 0 on X. Krull gives pure dimension 2.
  - By (R1), X_0 ⊂ q^{-1}(closure V_0), and X_0 ∩ {N = 0} ⊂ q^{-1}(B_0) has dimension ≤ 1. So no 2-dimensional component of D lies in {t = 0}.
- (c)
  - For each branch c of B_0 at Q, put N_c := H((c ∖ Q) × Δ_ε).
  - Near (0,0), q(D) ⊂ H(B_0 × Δ_ε) = H({Q} × Δ_ε) ∪ ⋃_c N_c. Since q^{-1}(H({Q} × Δ_ε)) = 𝒥 is a curve, the set T ∖ (𝒥 ∪ {t = 0}) is dense in T and lies in ⋃_c q^{-1}(N_c).
  - Each q^{-1}(N_c) is closed analytic in the complement of 𝒥, since H(c × Δ) is closed. T is irreducible, so T ⊂ closure q^{-1}(N_c) for a single c. Being 2-dimensional, T is a component of it.
  - Every irreducible component of q^{-1}(N_c) maps onto N_c. Indeed, N_c ≅ (c ∖ Q) × Δ_ε is a connected topological manifold, hence an irreducible analytic set, and q is finite; then apply Remmert. So every component meets {t = 0}, where its points lie on lifted branches of c. Hence every component lies in some Ñ_c̃.
  - So T is a component of closure(Ñ_c̃), i.e. a sheet of c̃.
  - The points of closure(Ñ_c̃) ∖ Ñ_c̃ near (0,0) lie over H({Q} × Δ_ε), and at t = 0 that is only the point 0. So T ∩ {t = 0} ⊂ c̃. It is 1-dimensional (by Krull, t ≢ 0 on T), and c̃ is irreducible, so it equals c̃ as germs.
  - Finally c̃ ⊂ X_0, since T ⊂ X.
- (d)
  - Let p ∈ c̃ ∖ 0 be generic: a smooth point of c̃, on no other lifted branch, with Stab(p) = Stab(c̃).
  - Take a local component W of X at (p,0). It is a local component of 𝒳, and as in (b), N ≢ 0 on W. By Krull, W ∩ {N = 0} has pure dimension 2 at (p,0). Let G be a 2-dimensional germ in it.
  - Near (q(p),0), H(B_0 × Δ) = N_c, because near q(p) the set B_0 is c and H is continuous. Also 𝒥 is far from (p,0), since p ≠ 0. So G ⊂ q^{-1}(N_c).
  - G lies in the germ at (p,0) of a component of q^{-1}(N_c). That component contains (p,0) ∈ c̃ ∖ 0, so it lies in Ñ_c̃.
  - So G lies in a sheet T of c̃. Since T ∩ X ⊇ G is 2-dimensional and T is irreducible, T ⊂ X. Also T ⊂ {N = 0}. Hence T is a component of D.
  - Since β̃, b̃ ⊂ S ⊂ X_0, this applies to β̃ and b̃. ∎

**Remark.** (d) is all that point 1 of the brief asks for in (F2). The sheet of β̃ found in X is τT_β for some τ ∈ Stab(β̃) (B1(b)), so it carries τx (B1(c)). That is the label issue, now located precisely. It is treated together with the other twists in §4.

---

## 2. Lemma D2 (the sheet graph of D is connected) — proved, given Grothendieck

**Lemma D2.** Let 𝔊_X be the graph whose vertices are the components (sheets) of D, with T ~ T′ when T ≠ T′ and the germ T ∩ T′ at (0,0) has dimension ≥ 1. Then 𝔊_X is connected.

*Proof.* X is an irreducible 3-dimensional germ and D = X ∩ {N = 0}. Apply the analytic translation of Grothendieck's theorem (§0) with h = N. ∎

This uses no Q-factoriality. It replaces Krull linkage (Theorem Q), whose hypothesis (QC) was the source of (F1).

---

## 3. Lemma D3 (what links two adjacent sheets) — proved

**Lemma D3.** Let T ~ T′ in 𝔊_X, with T a sheet of c̃ and T′ a sheet of c̃′, and let C be an irreducible curve germ in T ∩ T′ at (0,0). Exactly one of the following holds.
- **(α)** C ⊂ 𝒥, and C is a lift-curve λ ⊂ T ∩ T′.
- **(γ)** C is finite over Δ_ε and C ⊄ 𝒥. Then c and c′ are the same coarse branch, and T′ = gT for some g ∈ Aut(Q) fixing C pointwise.
- **(β)** C ⊂ {t = 0}. Then c̃ = c̃′ = C, and T′ = σT for some σ ∈ Stab(c̃).

*Proof.*
- **Two cases.** Either C ⊂ {t = 0}, or t|_C is non-constant. In the second case C is finite over Δ_ε, because C ∩ {t = 0} is a proper analytic subset of an irreducible curve germ, hence the point (0,0).
- **(α).** An irreducible curve germ inside the curve 𝒥 is a component of 𝒥, i.e. a lift-curve.
- **(γ).** This is the argument of round10_q7 Theorem Q, step 4, re-checked.
  - For p ∈ C_t with t ≠ 0, p lies in T ∖ 𝒥 and in T′ ∖ 𝒥. So q(p) ∈ H_t(c ∖ Q) ∩ H_t(c′ ∖ Q). Since H_t is injective, c = c′.
  - The coarse curve H_t(c) is a topological manifold at q(p), hence locally irreducible. So Stab(p) permutes transitively the lifted branch germs at p. Choose one in T_t and one in T′_t. Some g_p ∈ Stab(p) maps the first onto the second.
  - Aut(Q) is finite, so a single g serves for points p_n ∈ C with pairwise distinct times t_n → 0.
  - Then gT ∩ T′ contains curve germs inside infinitely many distinct slices {t = t_n}. A 1-dimensional analytic set has finitely many components, and only finitely many of them lie in slices. So gT ∩ T′ is 2-dimensional, and gT = T′ by irreducibility.
  - Fix(g) ∩ C is analytic and contains the p_n, which accumulate at (0,0). So C ⊂ Fix(g).
- **(β).** By Lemma D1(c), C ⊂ T ∩ {t = 0} = c̃ and C ⊂ c̃′. Distinct lifted branches meet only at 0, so c̃ = c̃′ = C. Both T and T′ are components of closure(Ñ_c̃), so T′ = σT with σ ∈ Stab(c̃), by B1(b). ∎

**Definition.** An edge T ~ T′ is **good** if T ∩ T′ contains some curve germ of type (α) or (γ). Otherwise it is **(B-pure)**: T ∩ T′ = c̃ × {0} as a germ, and T′ = σT with σ ∈ Stab(c̃).

---

## 4. Proposition D4 (label propagation along edges) and Theorem D — proved

**(IMOV_Q).** This is the following statement. There are a countable set Z′ ⊂ Δ_ε and a curve germ C ⊂ B × Δ_ε at (0,0), finite over Δ_ε, such that for every t ∈ Δ_ε ∖ Z′ there are a point p ∈ C_t, a label y and a lifted branch c̃_t of B_t through p with:
- F_y(p) ≅ Y_t;
- q(p) in the stratum of the piece of c̃_t;
- F_y non-constant along c̃_t.

This is an IMOV event of R8-3 at all times outside a countable set, located on a curve through (Q, 0). It is the local form of round9_q1's case (I).

**Proposition D4.** Let T ~ T′ be a good edge. Then P(T) = P(T′), or (IMOV_Q) holds.

*Proof.* By symmetry it suffices to show y ∈ P(T) ⇒ y ∈ P(T′), unless (IMOV_Q) holds.
- **Case (α), with λ ⊂ T ∩ T′.** By I1, y ∈ Λ(λ).
  - If T′ is of boundary type, I2 gives y ∈ P(T′).
  - If T′ is of interior type (Q in the stratum of c′), fix t ∉ Z, put p := λ(t), and apply (TN) at q(p) = Q_t to y and to the lifted branch (T′_t near p).
    - If STAY occurs for uncountably many t, the analytic set {p′ ∈ T′ : y intact, [F_y(p′)] = [Y_{t(p′)}]} contains slice curves for uncountably many t. As in the proof of I2, it is then all of T′, so y ∈ P(T′).
    - Otherwise, for all t outside a countable set, IMOV occurs at λ(t), with Q_t in the stratum of the piece of c′. This is (IMOV_Q) with C = λ.
- **Case (γ), with T′ = gT and C ⊂ Fix(g).** For p ∈ C_t we have p ∈ T, so y is intact at p and F_y(p) ≅ Y_t. Since gp = p, (K3) gives that g^{-1}y is intact at p with F_{g^{-1}y}(p) ≅ F_y(gp) ≅ Y_t.
  - Apply (TN) at q(p) to g^{-1}y and the branch T_t through p.
  - If STAY occurs for uncountably many t, the same analytic-set argument gives g^{-1}y ∈ P(T). Hence y ∈ gP(T) = P(gT) = P(T′), by B1(c).
  - Otherwise IMOV occurs for all t outside a countable set: (IMOV_Q) with this C. ∎

**Theorem D.** Assume MS11's setting and data, and let X be as in Lemma D1. Then there are:
- sheets T^β (of β̃) and T^b (of b̃), both in X;
- τ ∈ Stab(β̃) with T^β = τT_β, where T_β is the given sheet with x ∈ P(T_β);
- a path T^β = T_0 ~ T_1 ~ ⋯ ~ T_k = T^b in 𝔊_X.

Let j_1 < ⋯ < j_m be the indices at which T_{j−1} ~ T_j is (B-pure), with T_j = σ_j T_{j−1} and σ_j ∈ Stab(c̃_j). Put w := σ_{j_m} ⋯ σ_{j_1}. If (IMOV_Q) fails, then:
- P(T^b) = wτ P(T_β) ∋ wτx;
- MS11's conclusion holds **iff** x ∈ Stab(b̃)·P(T^b);
- in particular it holds if wτx ∈ Stab(b̃)·x.

*Proof.*
- The sheets T^β and T^b come from D1(d), and τ from B1(b). The path comes from Lemma D2.
- Along good edges P is unchanged (D4). Along (B-pure) edges P(T_j) = σ_j P(T_{j−1}) (B1(c)). Also P(T^β) = τP(T_β).
- The sheets of b̃ are the ρT^b, ρ ∈ Stab(b̃) (B1(b)), with P(ρT^b) = ρP(T^b). So x is persistent on some sheet of b̃ iff x ∈ Stab(b̃)P(T^b). ∎

**Corollary D′ (sufficient conditions for MS11).** Assume (IMOV_Q) fails. MS11 holds if either:
- (i) some path in 𝔊_X from a sheet of β̃ carrying x to a sheet of b̃ uses only good edges; or
- (ii) every element of Stab(c̃) fixes every label of P(T), for every lifted branch c̃ ⊂ X_0 and every sheet T of c̃ in X, and also for c̃ = β̃ (for the initial τ).

*Proof.* In both cases the composite twist fixes x, so x ∈ P(T^b). ∎

**What happens to (F1) and (F2).**
- (F1) of Cor. Q2 is not a separate obstruction. Non-Q-factoriality of X costs nothing, because Grothendieck connectedness needs only irreducibility of X.
- (F2) is resolved by D1: X ⊃ S × {0} always carries sheets of both β̃ and b̃. All that remains of it is the initial twist τ, which is a (B-pure)-type step at β̃.
- So every failure of MS11 is (IMOV_Q), or a non-trivial composite twist through (B-pure) steps and τ.

---

## 5. The same-branch case (point 3 of the brief): reduction, partly sketched

Theorem Q(b) is case (γ) of D3, so by D4 it either passes the label or gives (IMOV_Q). I record what (IMOV_Q) of type (γ) forces. This is **sketched**: it uses Lemma U / Lemma S(c) of earlier rounds as quoted in the brief, and I have not re-derived those.

- At p ∈ C_t, the two lifted branches T_t and gT_t of H_t(c) through p cross. Along T_t the label y is constant ≡ Y_t, and along gT_t it moves. In the lifted family of the piece D of c in ∏_w M_w × Δ, this is a crossing E_t ∩ σE_t of two lifts of the time-t piece. It is the Gap A configuration of round10_q3 §2.1, at points that tend to the puncture Q as t → 0.
- The label u := g^{-1}y is then a non-constant vertex of the piece D_t with value Y_t at the crossing point. By (Rig), its projection pr_u(K) is a fixed curve. So **Y(Δ) ⊂ pr_u(K) for a moving vertex u of the piece of c**, which at t = 0 is a curve containing Y_0. This is the R8-2 Prop. 7(b) alternative ("Y moves inside a fixed curve").
- I could not exclude it. If the vertex u has maximal speed at a generic point of D_0, then by Lemma PA / Prop. C pr_u(K) is a Teichmüller curve, and Y moves along it. Nothing proved so far forbids that.

So point 3 reduces to the known open problem (round9_q1 case (I), R8-2 Prop. 7(b)). It is not closed here.

---

## 6. (B-pure) twists inside one component X are locally realisable (local model, proved as a local statement)

At a generic point p of a lifted branch c̃, take local coordinates (u, v, t) on a smooth local component W of X. Let σ ∈ Stab(c̃) act by u ↦ −u. Put s_e := u² − t² for the edges e of the pattern of c̃ (σ-invariant; the other s_f are units), and let a := u and b := −u be local coordinates of [F_y] and [F_{σy}], with [Y_t] ↔ t.
- **Coarse picture.** Put U = u². The coarse image W/σ has coordinates (U, v, t), so it is smooth. Its boundary is {U = t²}, a smooth surface ≅ (v, t). The t = 0 sheet {t = 0} has boundary {U = 0}. H_t(U, v) := (U + t², v) is a smooth stratum-preserving trivialisation. So (R1), (R2), (i) and (ii) hold locally, and V_t is smooth.
- **Upstairs.** D ∩ W = T ∪ σT with T = {u = t} and σT = {u = −t}. These are two sheets of c̃ meeting exactly along c̃ × {0} = {u = t = 0}: a (B-pure) edge inside one component.
- **Labels.** On T, a = t, so y ∈ P(T). On σT, b = −u = t, so σy ∈ P(σT), while a = −t ≠ t, so y ∉ P(σT). At t = 0 both y and σy are ≅ Y_0 along c̃, and σ fixes c̃ pointwise.

So no argument local to generic points of c̃ (or to the 3-fold X) can exclude the twist. Any proof must use the global position of the sheets at (0,0), together with total geodesy of S, or global input at t ≠ 0. This is consistent with round10_q3 §3.3 and round10_q7 §5.

---

## 7. Summary: proved / not proved / open

**Proved** (modulo the inputs of §0, cited as stated there):
1. Lemma D1: a component X ⊃ S × {0} of the track 3-fold exists. Its boundary divisor D is pure 2-dimensional, consists of transport sheets of lifted branches of X_0, and contains sheets of β̃ and of b̃. This settles the geometric half of point 1.
2. Lemma D2: the sheet graph of D is connected (Grothendieck connectedness, cited). No Q-factoriality is needed, so (F1) disappears as a separate case (point 2).
3. Lemma D3: adjacent sheets are linked by a lift-curve (α), by a pointwise g-fixed curve finite over Δ with the same coarse branch (γ), or only by their common t = 0 branch, with T′ = σT and σ ∈ Stab(c̃) ((β), "B-pure").
4. Proposition D4: good edges preserve the persistent label set, interior-type sheets included, unless (IMOV_Q) holds.
5. Theorem D and Corollary D′: the exact criterion "x ∈ Stab(b̃)·wτP(T_β)" for MS11 when (IMOV_Q) fails, and two sufficient conditions.
6. §6: a local model of a label-twisting (B-pure) edge inside one 3-fold component.

**Sketched only:** §5, the consequence Y(Δ) ⊂ pr_u(K) of a type-(γ) (IMOV_Q).

**Not proved:** MS11 in full.

**Open (named):**
- **(O-Bpure)** Show that the composite twist wτ maps x into Stab(b̃)·P(T^b). For example, show that the σ at (B-pure) steps in X fix the persistent labels, or that a path with good edges only exists. This needs total geodesy of S or global input; §6 shows that local arguments do not suffice.
- **(O-IMOV_Q)** Exclude persistent IMOV events on curves through (Q, 0). Equivalently, locally, round9_q1 case (I) and R8-2 Prop. 7(b) ("Y moves inside a fixed curve pr_u(K)").
- Entry 82 ((Rig)) remains a separate input of the chain, untouched here.

proved: Lemmas D1–D3, Proposition D4, Theorem D, Corollary D′, the §6 local model.
not proved: MS11.
open: O-Bpure, O-IMOV_Q (and entry 82).


### round11_q1 (verbatim)
# round11_q1 — answer

**Status: PARTIAL.** I neither prove MS11 nor give a counterexample. What I add:
- §1: a logical remark. Under (Rig), MS11 is *equivalent* to the problem's claim, not merely sufficient for it. So the chain is a correct reduction (I found no flaw in the steps I re-checked, §6), but MS11 carries the full difficulty of the problem.
- §2: a copy-free reformulation of MS11 by lift-curves and stars (Lemmas 2.1–2.4, proved). In particular MS11 always holds "up to an automorphism".
- §3: a complete and corrected write-up of the planner's Mechanism D (Grothendieck connectedness in the 3-fold). It is proved down to a trichotomy of failure configurations, (β) / (γ) / (ι) (Theorem 3.6). I also record one gap in the planner's sketch and how it is absorbed.
- §4: a new necessary condition at the chain's endpoint, the *rigid twin* (Lemma 4.1). If MS11 fails at a MERGE/pMOV endpoint, then Q_t has, for every t, both a component ≅ Y_t and a component ≅ Y_0 (constant in t). Consequently Y_0 ∈ F′.
- §5: an explicit local model (smooth 3-fold, involution σ) showing that the (β)-failure is consistent with every chart-and-family-local constraint, including (R1), (R2), Theorem N and the pattern rules. It also isolates the Teichmüller-geometric feature that a proof would have to exclude ("square-root approach" of twin moduli).
- §6: chain check; §7: proved / not proved / open.

Readings: (R1), (R2) with H_0 = id, exactly as in the task. Notation is as in the task file: Def(Q), q, B, s_e, N := ∏_e s_e, labels, L_y := {s_e = 0 for all e at y}, F_y, (K1)–(K4), transport families Ñ_c̃, transport sheets, lift-curves. "Generic t" means: outside the countable exceptional set of Theorem N (R8-3 §3), the discrete sets Z_A, Z_φ of R8-8 §4, and the countable sets of R7-3 Lemma 1(b) for the finitely many (piece, vertex) pairs. Cited results of the run that I use as stated are named at the point of use: Theorem N (R8-3), Lemma U (R8-2), Lemma T (round9_q7), R7-4 Lemma 2, round9_q2 Lemma 1.

---

## 1. Logical status of MS11

**Proposition 1.1.** Assume the problem's hypotheses together with (Rig). Then the following are equivalent:
- (a) MS11 holds for every admissible datum (Q, B, β̃, b̃, x);
- (b) Y_t = Y_0 for all t.

*Proof.*
- (a) ⇒ (b) is the chain (§6 re-checks it).
- (b) ⇒ (a): MS11 has "t ↦ Y_t is non-constant" among its hypotheses. If (b) holds, no family satisfies that hypothesis, so MS11 is vacuously true. ∎

**Consequences.**
1. A proof of MS11 is a proof of the problem under (Rig). Any such proof must derive a contradiction from "Y non-constant" at some point.
2. The t = 0 shadow of MS11's conclusion is false in general: at the walk chain's endpoint, x is MERGE/MOV along b̃. So no argument that uses only t = 0 data and never uses the non-constancy of Y can work.
3. Hence the "missing statement" format (MS8, MS10, MS11, all containing "Y non-constant") does not reduce the logical difficulty. It localises where the contradiction has to be found. A statement that genuinely reduced the problem would be of the type of MS7 (a property of V_0 alone), or a statement about families that does not mention Y.

---

## 2. Copy-free reformulation: lift-curves and stars

Fix Q, B, ε as in MS11. Let 𝒥 := {(p,t) ∈ B × Δ_ε : q(p) = Q_t}, Q_t := H_t(Q). Its irreducible components through (0,0) are the lift-curves; let 𝔏 denote the set of lift-curves. By round9_q2 Lemma 1 (re-checked):
- 𝔏 is finite and permuted transitively by Aut(Q);
- each L ∈ 𝔏 is finite over Δ_ε and surjects onto it;
- after shrinking, every point of 𝒥 lies on some L.

A lift-curve lies in the locus {all s_e = 0}, so every label is intact on it and F_y is continuous on L.

**Definition.**
- For L ∈ 𝔏, C(L) is the set of labels y with F_y(p) ≅ Y_t for all (p,t) ∈ L.
- For a transport sheet Σ (of any lifted branch at 0), P(Σ) is the set of labels Y-persistent on Σ.
- Σ is *of boundary type* if its branch c̃ is a boundary branch at Q (Q is a puncture of the piece of c), and *of interior type* otherwise.

**Lemma 2.1 (sheets contain lift-curves; t = 0 slices).** Let Σ be a transport sheet of a lifted branch c̃.
- (a) Σ is an irreducible 2-dimensional analytic germ, and t is not identically 0 on Σ.
- (b) Σ ∩ {t = 0} is a union of lifted branches at 0.
- (c) Σ contains at least one lift-curve.

*Proof.*
- (a) Σ is a component of closure(Ñ_c̃), which has pure dimension 2 (R7-4 Lemma 2(c)). Its generic points lie in Ñ_c̃, which is open in a set fibred over t with 1-dimensional fibres. So t ≢ 0 on Σ.
- (b) By Krull, Σ_0 := Σ ∩ {t = 0} is a curve germ at (0,0). It lies in q^{-1}(B_0) by (R2) (H_0 = id, and H commutes with closures). Hence it is a union of lifted branches.
- (c) For small t ≠ 0, Σ_t ≠ ∅ (a non-constant holomorphic function on an irreducible germ is open). Every irreducible curve of Σ_t lies in a lift of a punctured branch H_t(c′) ∖ {Q_t} of the cone B_t ∩ U. A connected finite cover of a punctured disc is a punctured disc, so the closure of that curve adds exactly one point, a lift of Q_t. Hence Σ ∩ 𝒥 has points over every small t ≠ 0. It is analytic of dimension ≤ 1, since 𝒥 is a curve. So it contains a component of 𝒥 through (0,0). ∎

**Lemma 2.2 (all sheets of c̃ form one Stab_pt(c̃)-orbit).** Let G_c̃ ⊂ Aut(Q) be the pointwise stabiliser of c̃. Then the transport sheets of c̃ are exactly the sets σΣ_1, σ ∈ G_c̃, for any one sheet Σ_1. Moreover, every irreducible 2-dimensional germ at (0,0) of q^{-1}(closure 𝓑) (with 𝓑 = H(B_0 × Δ)) that contains c̃ × {0} is a transport sheet of c̃.

*Proof.*
1. Pick a generic p ∈ c̃ ∖ 0. Then Stab(p) = G_c̃, since stabilisers are generically constant along an irreducible curve. Also no other lifted branch passes through p, since distinct lifted branches meet only at 0.
2. Near (q(p), 0), 𝓑 coincides with N_c := H((c ∖ Q) × Δ_ε), a topological 4-manifold. A pure 2-dimensional analytic germ that is a topological manifold is irreducible: two components would meet in a set of real dimension ≤ 2, whose removal disconnects the union but cannot disconnect a 4-manifold (Hurewicz–Wallman).
3. Hence the local irreducible components of q^{-1}(N_c) at (p,0) are permuted transitively by Stab(p) = G_c̃ (quotient of an irreducible germ by a finite group).
4. Each of these local components meets {t = 0} in the germ of q^{-1}(c) at p, which is c̃. Their union is therefore connected and contains c̃ ∖ 0, so it lies in Ñ_c̃. So near (p,0), closure(Ñ_c̃) = q^{-1}(N_c).
5. Let Σ, Σ′ be sheets of c̃, i.e. irreducible germs containing c̃ × {0}. Each contains some local component at (p,0); say ℓ ⊂ Σ and ℓ′ ⊂ Σ′, with ℓ′ = σℓ, σ ∈ G_c̃. Then σΣ ∩ Σ′ contains the 2-dimensional ℓ′. Both are irreducible of dimension 2, so σΣ = Σ′.
6. The last claim: such a germ coincides near (p,0) with a union of local components of q^{-1}(N_c) ⊂ closure(Ñ_c̃). By irreducibility it lies in closure(Ñ_c̃), and being 2-dimensional it is a component. ∎

Consequently P(σΣ) = σP(Σ), by (K3).

**Lemma 2.3 (persistence is read off any lift-curve).** Let Y be non-constant. Let Σ be a transport sheet of boundary type and L ⊂ Σ a lift-curve. Then P(Σ) = C(L).

*Proof.*
- ⊆: if y is intact on Σ with F_y ≅ Y_t, the same holds on the closed set L ⊂ Σ, by continuity of F_y on the closed set L_y.
- ⊇: let y ∈ C(L) and let t be generic. Take p ∈ L_t. The curves of Σ_t ending at p are lifted branches through p of transported boundary branches; Q_t is a puncture of their pieces because H_t preserves strata. By Theorem N, the Y_t-copy y is intact and STAY along each of them, i.e. y is intact with F_y ≡ Y_t there.
- So the analytic set A_y := {(p′,t′) ∈ Σ ∩ L_y : F_y(p′) ≅ Y_{t′}} contains, for uncountably many t, a curve of Σ_t. Hence dim A_y = 2, and A_y = Σ by irreducibility. (A_y is analytic because t ↦ [Y_t] is holomorphic; R8-3 Lemma 1.) ∎

**Proposition 2.4 (MS11 in incidence form).** Assume MS11's setting (Y non-constant). Put (c̃, L) ∈ I iff some transport sheet of c̃ contains L, and Star(L) := {c̃ : (c̃, L) ∈ I}. Then:
1. x is Y-persistent on some sheet of b̃ iff there is L with x ∈ C(L) and b̃ ∈ Star(L).
2. The hypothesis gives L_1 with x ∈ C(L_1) and β̃ ∈ Star(L_1).
3. For every L and every coarse branch c at Q, Star(L) contains some lift of c.
4. (MS11 up to automorphism.) There is a ∈ Aut(Q) such that a^{-1}x is Y-persistent on some sheet of b̃. Explicitly, a b̃ ∈ Star(L_1).

*Proof.*
1. Combine Lemmas 2.1(c) and 2.3.
2. The hypothesis sheet T contains some L_1 (Lemma 2.1(c)), and x ∈ P(T) = C(L_1).
3. Q_t ∈ closure(H_t(c)), so the closure of q^{-1}(H_t c) contains a lift of Q_t. By Aut(Q)-invariance it contains every lift, in particular L(t). Then some component a Ñ_b̃ has L(t) in the closure of its t-slice (R7-4 Lemma 2(b)). Take an irreducible component of its closure containing the analytic set of such points (round9_q2 Lemma 1 argument).
4. By item 3 there is a with a b̃ ∈ Star(L_1). So x ∈ P(Σ) for a sheet Σ of a b̃, and a^{-1}Σ is a sheet of b̃ with a^{-1}x ∈ P(a^{-1}Σ). ∎

So **the entire content of MS11 is to take a ∈ Stab(x)**. Its failure is a twin phenomenon, as known; Proposition 2.4 states it without tracks or squares. This is the form used in §§3–4.

---

## 3. Mechanism D, written out, with its failure trichotomy

### 3.1 Set-up
- Let S be the component in (S). The analytic set q^{-1}(closure 𝒱) ∩ (B × Δ_ε) has pure dimension 3 (R1), and S × {0} is an irreducible 2-dimensional subset of it. So S × {0} ⊂ X for some irreducible 3-dimensional germ component X at (0,0). Fix one.
- X_0 := X ∩ {t = 0} is pure 2-dimensional (Krull; t ≢ 0 on X since X ⊄ {t = 0}). It is contained in q^{-1}(closure V_0), and S ⊂ X_0.
- N ≢ 0 on X, because S contains points over V_0. Put D := X ∩ {N = 0}, of pure dimension 2 (Krull).

**Lemma 3.1.** Every irreducible component (call it a *D-sheet*) of the germ D is a transport sheet of a lifted branch c̃ ⊂ X_0. Some D-sheet is a transport sheet of β̃, and some D-sheet is a transport sheet of b̃.

*Proof.*
- Let Σ be a D-sheet. Σ ⊄ {t = 0}, since X_0 ∩ {N = 0} is at most 1-dimensional (V_0 is dense in each component of X_0).
- So Σ ∩ {t = 0} is a curve in X_0 ∩ {N = 0}, i.e. a union of lifted branches c̃ ⊂ X_0.
- Σ ⊂ q^{-1}(closure 𝓑), since X ∖ q^{-1}(𝒱) lies over the boundary. By Lemma 2.2, Σ is a transport sheet of c̃.
- β̃ × {0} ⊂ S × {0} ∩ {N = 0} ⊂ D lies in some D-sheet, and that sheet is a sheet of β̃ by Lemma 2.2. The same holds for b̃. ∎

**Gap in the planner's sketch (step 2), and how it is absorbed.** The D-sheet of β̃ need not be the sheet T on which x is persistent: X ⊃ S × {0} was chosen independently of T. By Lemma 2.2 it is σT with σ ∈ G_β̃, carrying the label σx. Either σx = x, or this is already a configuration of type (β) below, with c̃ = β̃. Choosing X ⊃ T instead loses (S), because X_0 then contains β̃ but need not contain S.

### 3.2 Connectedness

**Cited (from memory): Grothendieck's connectedness theorem** (SGA 2, Exp. XIII, Thm 2.1; also Brodmann–Sharp, *Local cohomology*, Ch. 19). Let A be a complete local noetherian domain of dimension d and f_1, …, f_r ∈ m with r ≤ d − 2. Then Spec(A/(f_1, …, f_r)) ∖ {m} is connected.

Apply it with A = Ô_{X,(0,0)}, d = 3, r = 1, f = N. A is a domain: X is an irreducible complex-analytic germ, so O_X is a henselian excellent local domain with a single point in its normalisation, hence analytically irreducible.

The formal components of D are its analytic components, and two of them meet in the punctured spectrum iff they share a curve germ through (0,0). Hence:

**Lemma 3.2.** The graph 𝔊 whose vertices are the D-sheets, with an edge when two D-sheets share a curve germ through (0,0), is connected.

### 3.3 The edges

**Lemma 3.3 (edge types).** Let Σ ≠ Σ′ be D-sheets sharing an irreducible curve germ C through (0,0). Then exactly one of the following holds.
- (α) C is a lift-curve.
- (β) C ⊂ {t = 0}. Then C = c̃ is a lifted branch, both Σ and Σ′ are sheets of c̃, and Σ′ = σΣ with σ ∈ G_c̃.
- (γ) C ⊄ {t = 0} and C is not a lift-curve. Then C ∖ (0,0) lies in q^{-1}(N_c) for a single coarse branch c, both sheets are sheets of lifts of c, and Σ′ = gΣ near the generic point of C, for some g ∈ Aut(Q) fixing C pointwise.

*Proof.*
- (β): C is a curve in Σ ∩ {t = 0}, hence a lifted branch (Lemma 2.1(b)). Lemma 2.2 gives the rest.
- (γ): near a generic point p of C with t(p) ≠ 0, the set q^{-1}(closure 𝓑) is q^{-1}(N_c) for the coarse branch c through q(p), because B_t ∩ U is a cone at Q_t. Its local components at p are permuted transitively by Stab(p), as in Lemma 2.2. So the local components of Σ and Σ′ at p satisfy ℓ′ = gℓ, g ∈ Stab(p). Generic points of C have a common stabiliser, so g fixes C pointwise, and Σ′ = gΣ by irreducibility.
- (α) is what remains, since C ⊂ q^{-1}(𝓑) and q^{-1}(𝓑) near (0,0) consists of 𝒥 and the sets q^{-1}(N_c). ∎

**Lemma 3.4 (label rules).** Let Y be non-constant.
- (α) If Σ, Σ′ share a lift-curve L and both are of boundary type, then P(Σ) = C(L) = P(Σ′).
- (β), (γ): P(Σ′) = σP(Σ), respectively gP(Σ).

*Proof.* (α) is Lemma 2.3. (β) and (γ) follow from Σ′ = σΣ and (K3). ∎

### 3.4 The failure trichotomy

Call a D-sheet *good* if it is of boundary type and x ∈ P.

**Lemma 3.5.**
- (β-fail) Suppose a (β)-edge joins a good Σ to Σ′ = σΣ that is not good. Then y := σ^{-1}x ≠ x. Along c̃ at t = 0, both x and y are intact and constant with value ≅ Y_0. On Σ (as on every sheet of the transported piece containing it), y is intact and constant with a value function ψ satisfying ψ(0) = Y_0 and [ψ] ≢ [Y]. In short: **the piece of c carries, at t = 0, a pair of twin constant vertices exchanged by the generic automorphism σ of its curves, and the deformation separates them.**
- (γ-fail) Suppose a (γ)-edge joins a good Σ to Σ′ = gΣ that is not good. Then for generic t and p ∈ C_t, the label y := g^{-1}x is a Y_t-copy at p that is IMOV along Σ_t at p. It is a moving vertex of the lifted family W ⊃ Π(Σ), and the point of K_W over p has y-coordinate ≅ Y_t. Moreover p → 0 as t → 0. That is, the transported piece has, for every small t ≠ 0, a self-crossing at a g-symmetric curve near Q_t, at which a moving vertex passes through Y_t; the crossing disappears into the cusp Q at t = 0.
- (ι-fail) Suppose an (α)-edge joins a good Σ to an interior-type sheet Σ′, and Σ′ contains a further lift-curve L′ with x ∉ C(L′). Then x is IMOV along Σ′_t at L(t) for generic t: Q_t is an interior point of the piece E′ of Σ′ (Q ∈ stratum(E′)), x is a moving vertex of E′, and F_x(L(t)) ≅ Y_t while F_x(L′(t)) ≇ Y_t.

*Proof.*
- (β-fail).
  - x ∉ σP(Σ) means y ∉ P(Σ); and y ≠ x since x ∈ P(Σ).
  - σ fixes c̃ pointwise, so F_y(p) = F_x(σp) = F_x(p) ≅ Y_0 for p ∈ c̃, and y is intact along c̃ because x is (σ maps L_x to L_{σx}).
  - The pattern is constant on Ñ_c̃, so y is intact on Σ. y is constant along c̃, hence constant on every fibre of the component W of the lifted boundary family that contains Π(Σ) (Lemma U, Cor. U1). Its value function ψ is holomorphic with ψ(0) = Y_0.
  - [ψ] ≢ [Y]: otherwise y ∈ P(Σ).
- (γ-fail).
  - At p ∈ C_t, g ∈ Stab(p), so y is intact at p and F_y(p) = F_x(gp) = F_x(p) ≅ Y_t.
  - Here p is a point of a transported punctured branch, so it is an interior point of its piece, and Theorem N applies with "interior" allowed. If y were STAY along Σ_t at p for uncountably many t, the argument of Lemma 2.3 would give y ∈ P(Σ), i.e. x ∈ P(Σ′). So y is IMOV, and by Lemma U, y ∈ M_W.
  - C is a curve germ through (0,0) not in {t = 0}, so p → 0 as t → 0.
- (ι-fail). x ∈ C(L) by Lemma 2.3 applied to Σ. Along Σ′_t at L(t), Theorem N gives STAY or IMOV. STAY would give, by the argument of Lemma 2.3 inside the irreducible Σ′, x intact with F_x ≡ Y_t on Σ′, hence x ∈ C(L′). So x is IMOV, which requires Q_t ∈ stratum of the piece, i.e. Σ′ is of interior type. ∎

**Theorem 3.6 (failure trichotomy for MS11; proved).** Assume MS11's setting, and suppose its conclusion fails for (Q, β̃, b̃, x). Then for every choice of X ⊃ S × {0}, the boundary D of X contains a configuration of type (β-fail) (possibly with c̃ = β̃), (γ-fail) or (ι-fail).

*Proof.*
- If no D-sheet of β̃ is good: the D-sheet of β̃ is σT with σ ∈ G_β̃ (Lemma 2.2) and x ∉ σP(T). Then T and σT are joined by the common t = 0 branch β̃, and this is (β-fail) with c̃ = β̃, applied to Σ = T. (T need not lie in D, but Lemma 3.5(β-fail) only uses Σ, σΣ and c̃.)
- Otherwise there is a good D-sheet. No D-sheet of b̃ is good, since MS11 fails (Proposition 2.4, item 1).
- 𝔊 is connected (Lemma 3.2), so some edge joins a good D-sheet Σ to a non-good D-sheet Σ′.
  - If it is a (β)- or (γ)-edge, Lemma 3.5 applies.
  - If it is an (α)-edge, Σ′ is not of boundary type (Lemma 3.4(α)). So Σ′ is of interior type, and x ∈ C(L) for the shared L.
  - If moreover x ∈ C(L′) for every lift-curve L′ ⊂ Σ′, then all boundary-type neighbours of Σ′ through (α)-edges are good. Replace Σ′ by the next sheet: the bad set is reached only through (β), (γ) or (ι)-fail edges.
  - Formally: let 𝔊_x be the set of good sheets together with the interior-type sheets all of whose lift-curves L′ have x ∈ C(L′). This is a non-empty proper subset of the vertices of 𝔊, so some edge leaves it. Checking the three types as above gives (β-fail), (γ-fail) or (ι-fail). ∎

**Comparison with the planner's sketch.**
- Steps 1–4 hold, with the correction of §3.1 and with (ι) added. The sketch omits the case where an (α)-edge passes through an interior-type sheet, where Theorem N allows IMOV.
- Step 5's sufficient condition, "every (β)- and (γ)-edge element fixes x", must be supplemented by "no (ι)-fail".
- Step 6's identification of the residual configurations with (B-pure) and same-branch crossings is consistent with Lemma 3.5:
  - (β-fail) is the τ = 0 trace of a (B)-type fixed locus, Fix(σ) ⊃ c̃;
  - (γ-fail) is the same-branch crossing at t ≠ 0;
  - (ι-fail) is an interior-MOV through the cusp of a non-product piece.

None of the three is excluded here.

---

## 4. The rigid twin at a MERGE / pMOV endpoint (new necessary condition)

**Lemma 4.1.** Assume MS11's setting, (Rig), Y non-constant, and moreover that at t = 0 the label x is MERGE along b̃ (some edge at x is unpinched on b̃) or pMOV along b̃ (x intact, F_x non-constant along b̃, Q not in the stratum of b). This is the situation at the chain's endpoint. Then for every lift-curve L′ contained in a transport sheet of b̃:

 F_x(p) ≅ Y_0 for all (p,t) ∈ L′  (independently of t).

Consequently, if MS11 fails there, then with L_1 as in Proposition 2.4 and a ∈ Aut(Q) with a b̃ ∈ Star(L_1) (so ax ≠ x):
- for every t, the curve Q_t has a component ≅ Y_t (label x at L_1(t)) and a different component ≅ Y_0 (label ax at L_1(t));
- these two components are exchanged at t = 0 by a^{-1} ∈ Aut(Q). Precisely, F_{ax}(0) = F_x(a^{-1}·0) = F_x(0).

In particular **Y_0 ∈ F′** (the finite (Rig)-set of classes of components of puncture values).

*Proof.*
1. Let T′ ⊃ L′ be a sheet of b̃, and let t be generic. Take p ∈ L′_t. The pattern on T′ equals that of b̃. Q_t is a puncture of the transported piece E_t of b, since strata are preserved.
2. **MERGE.** The vertex u ∋ x of E_t contains an unpinched edge. Its limit at p is the curve glued from the F_y(p), y ∈ u, which is nodal. So u is non-constant (Lemma C2 of PR-C), and that nodal curve is the puncture value f_u(p′), which lies in F by (Rig) (R8-8 Lemma 2). Hence [F_x(p)] ∈ F′.
3. **pMOV.** u = {x} is non-constant on E_0, hence x ∈ M_W for the component W of the lifted boundary family containing Π(T′), hence non-constant on every fibre (Lemma U). Its puncture value at p′ is F_x(p), which lies in F′ by (Rig).
4. So [F_x] takes values in the finite set F′ at all points of L′ over generic t. F_x is continuous on L′ (L′ ⊂ {all s_e = 0} ⊂ L_x), and the points over generic t are dense in the irreducible curve L′. Hence [F_x] is constant on L′, equal to [F_x(0)] = [Y_0]. Since M_{g_i,n_i} → M_{g_i,n_i}/S_{n_i} has finite fibres and F_x is continuous, F_x itself is constant up to the fixed relabelling.
5. For the consequence: a b̃ ∈ Star(L_1) means some sheet T″ of a b̃ contains L_1, so a^{-1}T″ is a sheet of b̃ containing a^{-1}L_1.
   - By 1–4, F_x ≡ Y_0 on a^{-1}L_1.
   - By (K3), F_{ax}(p) = F_x(a^{-1}p) for p ∈ L_1, so F_{ax} ≡ Y_0 on L_1.
   - Also F_x ≡ Y_t on L_1, and ax ≠ x because [Y] is non-constant.
   - Y_0 ∈ F′ by step 2 or 3 at t = 0 (or by closedness). ∎

**Remarks.**
- At the endpoint, the twin that takes over the network along b is the Y-copy x seen from the frame L_1. The copy that merges is a *rigid* copy, whose class is Y_0 for all t, not some other moving function. This sharpens R8-8 Prop. 3 (endpoint), which only gave a second copy with [φ] ≡ [Y] on the piece of b. Here, in the frame of L_1, we get a constant copy at the cusp point Q_t itself.
- So a counterexample would have two components of Q_t, one moving as Y_t and one frozen at Y_0, exchanged by an automorphism of Q_0. The frozen one is a component of a cusp value of a (Rig)-curve.
- This does not by itself contradict anything. Y_0 ∈ F′ is a t = 0 statement, whereas pinning needs Y_t ∈ F′ for t in an open set.

---

## 5. A local model for (β-fail)

The model shows that (β-fail) is compatible with every chart-and-family-local constraint used in the run. It concerns an edge configuration, not an entire V_0. All claims are direct computations.

**The model.**
- Coordinates (u, v, w) near 0 on a smooth 3-fold X ⊂ Def(Q) × Δ, with t = u + v.
- σ is an involution of Def(Q) acting on X by (u, v, w) ↦ (v, u, w) and preserving t.
- Two twin labels x, y = σx, exchanged by σ, with all their edges pinched on {uv = 0}: for those edges, s_e|_X = uv (σ swaps the edges e ↔ σe; both restrict to uv).
- An antisymmetric coordinate m_x − m_y = u − v (twin moduli difference), and a symmetric one m_x + m_y = 2Y_0 + (u + v)(…).
- w is the coordinate along the branch c̃ = {u = v = 0}.

**Checks.**
- D = X ∩ {N = 0} ⊇ {uv = 0} = Σ ∪ σΣ, with Σ = {u = 0} and σΣ = {v = 0}. Each is smooth, and on each, t-slices are w-lines (v = t on Σ). So these are transport sheets of c̃ with constant pattern; the pattern is constant on each sheet, as required.
- Σ ∩ σΣ = c̃ × {0} ⊂ {t = 0}: a (β)-edge.
- X_0 = {v = −u} is a smooth surface S′ with boundary c̃, and N|_{S′} vanishes to even order (s_e = −u²).
- σ acts on S′ as the reflection u ↦ −u, fixing only c̃. So the coarse V_0 near c is S′/σ, which is smooth (coordinate u²). This is consistent with V_0 smooth in the coarse space.
- On Σ: F_x − F_y = (u − v)|_{u=0} = −t, so F_x ≠ F_y for t ≠ 0. Choose F_x|_Σ = Y(t) and F_y|_Σ = ψ(t) := Y(t) + t(…). Then x ∈ P(Σ), y ∉ P(Σ), and on σΣ the roles are swapped. This is exactly (β-fail).
- Fix(σ) ∩ X = {u = v} is 2-dimensional. Its t-slices for t ≠ 0 are the curves {u = v = t/2}, with uv = t²/4 ≠ 0, i.e. *interior* σ-symmetric curves of V_t. They converge to c̃ at t = 0 and have no boundary points near Q_t. This is precisely R9-5's (B-pure).
- Theorem N holds at every time: at points of Σ_t, the Y_t-copy x is STAY along Σ_t. The copy y has value ψ(t) ≠ Y_t, so Theorem N says nothing about it.

**What a proof would have to exclude (heuristic, not proved).** In the model, V_0 approaches the boundary piece c along S′ with:
- plumbing parameter ≈ u² for the edges at the twins;
- twin moduli difference ≈ u.

That is, the two Y_0-regions are pinched at equal rates, while their conformal types differ at the order of the *square root* of the plumbing parameter.

For a totally geodesic V_0, the tangent direction ∂_u at points near c is dominated in Teichmüller norm by the plumbing part. Its norm is of order 1/(|u| log(1/|u|)) by (C) of PR-H §1.2, while the twin-difference part is O(1). The Teichmüller disc it generates is a "cusp disc" pinching the twin collars. One expects, for instance from Lemma PA and the flat-limit description (Fl), that along such a disc the conformal types of the intact zero-area components converge to their limit at a rate polynomial in the cusp parameter, *holomorphically* in it. In S′/σ the cusp parameter is u² up to a power. A twin difference ≈ u = (u²)^{1/2} would then require the cusp parameter's relevant power to be even, an arithmetic condition on the cylinder moduli of e and σe.

I have not been able to turn this into a contradiction. It is recorded as the most concrete lead for (β-fail).

---

## 6. Chain check

Re-checked, with no flaw found:
- Step 1 (Goal ⇐ MS8 + (Rig) + PR-A), and Proposition 1.1's converse.
- Step 2(c), the "Base" and the "(α)-type" propagation. Lemma 2.3 above gives a self-contained proof that persistence is a property of the sheet and equals C(L) for any lift-curve in it. This is the "component-wise" reading.
- Step 2(d), non-product endpoint. Given a sheet T of b̃ with x ∈ P(T), T ∩ {t = 0} ⊇ b̃ (Lemma 2.1(b) and Lemma 2.2: every sheet of b̃ contains b̃ × {0}), and x intact with F_x ≡ Y_0 along b̃ contradicts MERGE/MOV. (Lemma B1(a)'s "non-empty open subset" is in fact all of b̃ ∖ 0.)
- Step 2(c), "Transfer along D^{m+1}". A sheet T′ of β̃′_m maps under Π into one component W of the lifted boundary family, with W_0 ⊇ the lifted piece Ê of D^{m+1}.
  - W, being irreducible with W_0 ⊇ Ê, has a local component along Ê near the J_{m+1}-end. By Lemma 2.2 at J_{m+1}, this is the image of a sheet of β̃_{m+1}.
  - Persistence of the vertex u = Π-image of x_m holds on all of W (Lemma U, Cor. U1). So x_{m+1}, the label of u along β̃_{m+1}, is persistent on that sheet.
  - The step therefore holds *provided* the identification of x_m and x_{m+1} with the same vertex u of W is the one used by the walk (the "R(D) repair"). I did not re-audit that repair.
  - **Caution:** if Ê lies in two components W ≠ σ̄W (σ̄ ∈ Aut(G) fixing Ê pointwise), the transfer must use the sheet over W, not over σ̄W. Otherwise one lands in a (β-fail) configuration along D^{m+1}. Lemma 2.2 shows that a sheet over W exists, so the step is correct as long as "some sheet" is used throughout, as MS11 does.

Not re-checked: Prop K_w and the R(D) repair, Theorem X*_all (non-product), Lemma S̃′ (the (S) property via canonical lifts), and the cited inputs.

One point to watch in Lemma S̃′: V_0 smooth in the coarse M_g does not make its preimage in Def(J) locally irreducible at interior orbifold points. For example, {ab = 0} ⊂ C² is the preimage of a smooth curve under the swap (a,b) ↦ (b,a). So a lifted path can change lifted components at such points. The (S) property therefore really needs the canonical lift of the Teichmüller track (a lift through one smooth component of the preimage in T_g, reading (T4)), not an arbitrary path lift. As far as the task file states it, round10_q10 §6.3 uses canonical lifts, so I flag this only as a point to keep explicit.

---

## 7. Summary

**Proved here** (modulo the cited results of the run named in each proof, and Grothendieck's connectedness theorem, cited from memory):
1. Proposition 1.1: under (Rig), MS11 ⇔ the problem's claim.
2. Lemmas 2.1–2.3 and Proposition 2.4:
   - sheets contain lift-curves;
   - all sheets of a lifted branch form one orbit of its pointwise stabiliser;
   - P(Σ) = C(L) for every lift-curve L in a boundary-type sheet Σ;
   - MS11 in incidence form, with "MS11 up to an automorphism" always true.
3. Lemmas 3.1–3.5 and Theorem 3.6: Mechanism D written out, with:
   - the correction that the D-sheet of β̃ need not be the persistent one (absorbed into (β-fail));
   - the omitted (ι) case added.

   Failure of MS11 forces a (β-fail), (γ-fail) or (ι-fail) configuration in the boundary of any 3-fold component X ⊃ S × {0}.
4. Lemma 4.1 (rigid twin): at a MERGE/pMOV endpoint, failure forces Q_t to carry, for all t, both a Y_t-component and a component frozen at Y_0, exchanged at t = 0 by an automorphism of Q. In particular Y_0 ∈ F′.
5. §5: an explicit local model realising (β-fail), compatible with every local constraint used so far, including (B-pure).

**Not proved:** MS11, hence (by Prop. 1.1) the problem itself, under (Rig) or otherwise. No counterexample is given.

**Open questions (precise):**
- (Q1) (β-fail): can a boundary piece c of a smooth totally geodesic V_0 at a non-product cusp Q consist of curves with a generic automorphism σ exchanging two Y_0-components, with the sheet of V_0 along c being σ-reflected (as in §5: plumbing ≈ u², twin moduli difference ≈ u)? Lead: a Teichmüller-norm computation of the cusp discs tangent to ∂_u (§5, heuristic).
- (Q2) (γ-fail): can the transported piece self-cross, for every small t ≠ 0, at a g-symmetric curve near Q_t at which a moving vertex passes through Y_t, the crossing collapsing into Q at t = 0?
- (Q3) (ι-fail): can a non-product piece E′ with Q ∈ stratum(E′) carry, at Q_t, an interior-MOV of the Y_t-copy at one lift-curve but not at another?
- (Q4) Whether Lemma 4.1's rigid twin (a component of Q_t frozen at Y_0, which is a component of a cusp value of a (Rig)-curve) can be combined with total geodesy at t = 0 to force Y_t ∈ F′ for t near 0.
- (Q5) (Rig) (entry 82), untouched.


### round11_q4 (verbatim)
# round11_q4 — attempt to REFUTE MS11

**Status line.** No counterexample and no contradiction were found: MS11 is **not refuted**. Its status stays **open**. Along the way I prove four things.
- (§1) Logical status. Refuting MS11, by either route, is the same as finding a counterexample to the problem under (Rig). The "derivation" route cannot succeed unless the problem itself is false or some PROVED entry is wrong.
- (§2) An exact reformulation of MS11 in terms of **lift-curve components**: the Y-persistent labels of a transport sheet are exactly the "Y-labels" Y(L) of any lift-curve component L contained in the sheet. This gives a clean proved sufficient condition (1L) and an exact description of what a failure needs.
- (§3) A **twin-free closure theorem**. If Y is non-constant, every piece reachable from ∂V_0 by puncture transitions has a constant vertex φ ≡ Y. There is also a **twin-free t=0 criterion (TFM)** that forces Y to be constant. Both are proved modulo R8-2 Theorem 1 (which uses (Rig)).
- (§4) As a sketch: covering constructions from M_{0,5} satisfy TFM, so they cannot be counterexamples. The flex and gothic loci are not candidates as stated, since they live in M_{1,3}.

The chain question (component-wise wording) is answered in §5. Open questions are listed in §6.

Throughout I use the run's readings (R1), (R2), H_0 = id, (Rig), and its notation (B_t, pieces, Def(Q), q, labels, F_x, transport family Ñ, transport sheet, lift-curve). Results used from earlier rounds are cited by their run labels and were re-read from the brief; they are not re-proved here. Standard analytic-geometry facts are cited from memory: Remmert's finite mapping theorem; the open mapping property of a non-constant holomorphic function on an irreducible germ; the fact that an analytic germ whose complement of a real-codimension-2 set is a connected manifold is irreducible.

**Convention (germs).** As in MS11's choice of B, transport sheets and 3-fold components are taken as irreducible components of germs at (0,0) ∈ Def(Q) × Δ. MS11 already shrinks B so that components of q^{-1}(closure V_0) ∩ B are germ components; I assume the same for closure(Ñ_c̃) and q^{-1}(closure 𝒱). If a sheet as defined in the brief (a component of the closure in B × Δ_ε) does not pass through (0,0), it is irrelevant for MS11 after shrinking B and ε. Write G := Aut(Q), acting on Def(Q) × Δ trivially in t.

## 1. Logical status of a refutation

MS11's setting contains the hypothesis "t ↦ Y_t is non-constant".
- If the problem's conclusion holds for every admissible family satisfying (Rig), then MS11's setting is empty and MS11 is vacuously true. Nothing false can then be derived from MS11 together with true statements.
- Hence route 2 of the task ("derive a known-false statement from MS11 + proved results") can succeed only if (a) the problem is false under (Rig), or (b) one of the PROVED entries used is wrong.
- Route 1 (an explicit configuration) is, by round10_q4 Prop. 1, a counterexample to the problem under (Rig).

So both routes require a counterexample to the problem itself, or an error in the ledger. This explains why local chart models (round10_q3 §3.3, round10_q7 §3, R7-3 §5, round9_q9) never refute MS11: refutation is a global question. The useful outputs of a "refutation attempt" are therefore sharpened **necessary conditions for a counterexample** (§§2–4).

## 2. Lift-curve reformulation of MS11 (proved, modulo R8-2 Theorem 1)

**Notation.**
- Q_t := H_t(Q). It is holomorphic in t (PR-B / R7-3 Lemma 1) and lies in Δ_{G_Q}, since H preserves strata.
- The *lift locus* is Λ := {(p,t) ∈ B × Δ_ε : q(p) = Q_t}. Its irreducible components through (0,0) are the lift-curve components. G permutes them transitively: Λ is the preimage of the irreducible curve germ {(Q_t,t)} under the quotient map q × id, and components of the preimage of an irreducible germ under a finite group quotient form one orbit.
- Fix one lift-curve component L_0 and put H_L := Stab_G(L_0). The lift-curve components are gL_0, g ∈ G/H_L.
- Every point of Λ lies in {s_e = 0 ∀ e}, so every label is intact there.
- For a lift-curve component L, let **Y(L)** be the set of labels y with F_y(p) ≅ Y_t at all (p,t) ∈ L. This is an analytic condition, equivalent to holding at generic points of L.
- By (K3) of R7-3, Y(gL) = g·Y(L). In particular Y(L) is H_L-invariant.
- For a lifted branch c̃ through 0 (Q a puncture of the piece of c), let **𝓛(c̃)** be the set of lift-curve components contained in some transport sheet of c̃.

**Lemma 2.1 (every sheet contains a lift-curve component).** Let c̃ be a lifted branch of a branch c of B_0 at Q, and T a transport sheet of c̃ (a germ at (0,0)). Then T contains some lift-curve component.

*Proof.*
- Let Σ_c be the germ at (Q,0) of closure(H(c × Δ_ε)) ⊂ M̄_g × Δ. By (R1) and (R2) it is a 2-dimensional analytic germ: it is the germ of a component of closure(𝒱) ∩ (closure(Δ_{G_c}) × Δ).
- Σ_c contains the dense subset H((c∖Q) × Δ_ε), which is a connected topological 4-manifold. The rest, {(Q_t,t)}, has real codimension 2. Hence Σ_c is an irreducible germ.
- T ⊂ (q × id)^{-1}(Σ_c), and q × id is finite. By Remmert's finite mapping theorem, (q × id)(T) is a 2-dimensional analytic subgerm of the irreducible 2-dimensional germ Σ_c, so it equals Σ_c.
- In particular, for every small t there is (p,t) ∈ T with q(p) = Q_t. So T ∩ Λ is an analytic subset of T whose projection to t contains a neighbourhood of 0. Hence T ∩ Λ contains a curve through (0,0) not contained in {t = 0}, i.e. a lift-curve component. ∎

**Lemma 2.2 (persistent labels of a sheet).** In the situation of Lemma 2.1, assume (P): Q is a puncture of the piece of c. Let T be a transport sheet of c̃, L ⊂ T a lift-curve component, and y a label. Then
 y is Y-persistent on T ⟺ y ∈ Y(L).
In particular, Y(L) is the same for all lift-curve components L ⊂ T.

*Proof.*
- (⇒) Evaluate the persistence condition at the points of L ⊂ T.
- (⇐) Let A_y := {(p,t) ∈ T : s_e(p) = 0 for all e at y, and class F_y(p) = class Y_t in 𝔐}. This is a closed analytic subset of T (F_y is holomorphic on L_y, and Y is holomorphic by PR-A).
- Let t be generic in the sense of R8-2 §3, i.e. t ∉ Z, where Z is discrete. Let (p,t) ∈ L. Then Q_t is a puncture of the transported piece (H preserves strata and pieces), and y is a Y_t-copy at p.
- Every branch of the curve T_t = T ∩ {t} at p is a lifted branch of the transported branch c_t at Q_t, because T_t ⊂ q^{-1}(closure c_t). By R8-2 Theorem 1 (IMOV is excluded at a puncture), y is STAY along each such branch: it is intact, and F_y is constant, equal to F_y(p) ≅ Y_t.
- So A_y contains the germ of T_t at (p,t). This germ is 1-dimensional, because T is an irreducible 2-dimensional germ and t ≢ 0 on T.
- This holds for all t ∉ Z near 0, an uncountable set. An analytic set of dimension ≤ 1 has 1-dimensional fibres over at most countably many t. Hence dim A_y = 2, and A_y = T since T is irreducible. ∎

**Proposition 2.3 (exact reformulation).** Under the hypotheses of MS11 the following hold.
- The labels Y-persistent on some transport sheet of c̃ are exactly ⋃_{L ∈ 𝓛(c̃)} Y(L).
- MS11 for (Q, β̃, b̃, x) is equivalent to: if x ∈ Y(L) for some L ∈ 𝓛(β̃), then x ∈ Y(L′) for some L′ ∈ 𝓛(b̃).

*Proof.* Combine Lemmas 2.1 and 2.2. ∎

**Corollary 2.4 (sufficient condition (1L), proved).** Suppose some irreducible 3-dimensional component X of the germ of q^{-1}(closure 𝒱) at (0,0) satisfies:
- X contains a transport sheet of β̃ on which x is persistent, and some transport sheet of b̃;
- X contains exactly one lift-curve component.

Then MS11 holds for (Q, β̃, b̃, x).

*Proof.* Both sheets lie in X, so by Lemma 2.1 both contain the unique lift-curve component L ⊂ X. By Lemma 2.2, x ∈ Y(L) is persistent on the b̃-sheet. ∎

**Corollary 2.5 (anatomy of a failure, proved).** Suppose MS11 fails for (Q, β̃, b̃, x), and let L ∈ 𝓛(β̃) with x ∈ Y(L). Then:
1. L ∉ 𝓛(b̃): no sheet of b̃ contains L. In particular |G·L| ≥ 2, i.e. H_L ≠ G. This recovers the necessary condition |Aut(Q_t)| < |Aut(Q)|.
2. 𝓛(b̃) ≠ ∅ (Lemma 2.1), and every element of 𝓛(b̃) is gL with x ∉ g·Y(L). The persistent labels gx on b̃-sheets are twins of x, Y_0-copies different from x. The required α moving x is any such g.
3. By Lemma B1(a), at t = 0 the labels in g·Y(L) are intact and ≡ Y_0 along b̃. So the piece E_b of b has a constant vertex with φ ≡ Y that is **not** x along b̃ (a "staying twin").
4. The persistent sheet of β̃ and every sheet of b̃ contain disjoint sets of lift-curve components. So any 3-fold component X containing sheets of both contains at least two lift-curve components L, gL. Hence (1L) fails, by one of two mechanisms:
   - **(F-a)** S × {0} lies in two different 3-fold components X ≠ X′. This needs S to lie in the fixed locus of some σ ∈ G that is not in the generic stabiliser of the time-t surfaces (the planner's (β)-edges).
   - **(F-b)** a single X contains several lift-curve components.

**Relation to the planner's Mechanism D.** In this language the label-change rule of the planner's sketch (§4 of the brief) is automatic.
- Two sheets that share a lift-curve component have the same persistent labels (Lemma 2.2). This is the (α)-edge statement, without Lemmas I1/I2.
- Labels change only between sheets that contain different lift-curve components L ≠ gL, and the change is y ↦ gy.
- Grothendieck connectedness of X ∩ {N = 0} ∖ {(0,0)} therefore yields MS11 only if one can show that the lift-curve components met along a connecting path are related by elements g with x ∈ g·Y(L). Connectedness alone does not give this, and I found no global input that does. This is where the Mechanism-D attempt stops.

## 3. Twin-free closure of the Y-network, and a twin-free t = 0 criterion (proved, modulo R8-2 Theorem 1)

The twin problem comes from following the *marked* copy x. Membership statements that do not track a particular label can be transported with no twin problem at all. This section makes that precise. It yields necessary conditions for a counterexample that involve V_0 only.

**Definitions.**
- For a piece E at t = 0 and a vertex c constant on E, φ_c(t) is the value of c on E_t = H_t(E). It is holomorphic by R7-3 Lemma 1(a).
- 𝒩 is the set of pieces E (at t = 0) having a constant vertex c with φ_c ≡ Y.
- 𝒩_0 ⊃ 𝒩 is the set of pieces having a constant vertex with value ≅ Y_0.
- A *puncture* of E is a point of closure(ξ(E)) outside the stratum Δ_{G_E}. Pieces are closed in their stratum, so this is the same as a point of closure(ξ(E)) ∖ ξ(E).
- **ℛ** is the smallest set of pieces with these two properties:
  - it contains every piece of ∂V_0;
  - **(PT)** if E ∈ ℛ, Q ∈ closure(ξ(E)), and E′ is a piece of which Q is a puncture, then E′ ∈ ℛ.

**Proposition 3.1 (ℛ ⊂ 𝒩).** Assume (R1), (R2), (Rig), and that Y is non-constant. Then every piece in ℛ has a constant vertex c with φ_c ≡ Y. In particular ℛ ⊂ 𝒩_0.

*Proof.* Pieces of ∂V_0 lie in 𝒩, via the vertex i. It remains to show that 𝒩 is closed under (PT). Let E ∈ 𝒩 with constant vertex c, φ_c ≡ Y. Let Q ∈ closure(ξ(E)), and let E′ be a piece with Q as a puncture.
- Let t ∉ Z be generic (R8-2 §3) and let q be any lift of Q_t = H_t(Q).
- Take a lifted branch of E_t through q, or the lifted germ of E_t if Q_t ∈ ξ(E_t). Along it, the constant vertex c is a single label z, intact at q, with F_z(q) = φ_c(t) = Y_t: a constant vertex has a smooth limit (R7-3 §1).
- E′_t has Q_t as a puncture, since H preserves strata and closures (PR-B). E′_t has a lifted branch through q, because q is an open map.
- By R8-2 Theorem 1, IMOV is impossible since Q_t is a puncture of E′_t. So z is STAY: z is a constant vertex of E′_t with value Y_t, and (W, z) is a Y-vertex.
- E′_t has finitely many vertices, identified with those of E′ by transport. So some vertex c′ of E′ is constant with φ_{c′}(t) = Y_t for uncountably many t. By the identity theorem φ_{c′} ≡ Y, i.e. E′ ∈ 𝒩. ∎

Note that no label is tracked across Q here: q is an arbitrary lift, and the conclusion is about *some* vertex of E′. This is why twins play no role.

**Corollary 3.2 (criterion R).** Under (R1), (R2), (Rig): if some piece reachable from ∂V_0 by puncture transitions has no constant vertex isomorphic to Y_0, then Y_t = Y_0 for all t.

*Proof.* Proposition 3.1 shows that Y is constant, and Y_t = Y_0 by PR-A. ∎

**Theorem 3.3 (twin-free merge criterion, TFM).** Assume (R1), (R2), (Rig). Suppose there are a point Q ∈ B_0, a piece E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and a piece E″ of which Q is a puncture, such that the following condition holds.
- **(TF)** For every lifted branch (or lifted germ) ẽ′ of E′ at 0 ∈ Def(Q), every label z that is intact and ≡ Y_0 along ẽ′, and every lifted branch ẽ″ of E″ at 0, the label z is *not* intact-and-≡ Y_0 along ẽ″.

Then Y_t = Y_0 for all t.

(TF) holds vacuously if E′ has no constant vertex ≅ Y_0. It concerns V_0 and t = 0 only.

*Proof.* Suppose Y is non-constant. By Proposition 3.1, E′ has a constant vertex c with φ_c ≡ Y.
1. Let 𝔗′ (respectively 𝔗″) be the germ at (0,0) of the closure of q^{-1}(H(β′ × Δ_ε)), where β′ ranges over the branches of E′ at Q (respectively of E″). Each is a finite union of irreducible 2-dimensional germs ("sheets"), by the argument of Lemma 2.1.
2. For each generic t near 0, pick a lift q_t of Q_t.
   - As in the proof of 3.1, there is a branch of 𝔗′_t through (q_t,t) along which some label z_t is intact with F ≡ Y_t (the label of c).
   - There is also a branch of 𝔗″_t through (q_t,t) along which z_t is STAY (R8-2 Theorem 1).
3. There are finitely many sheets, labels and lift-curve components, and uncountably many t. So we may fix a sheet T′ ⊂ 𝔗′, a sheet T″ ⊂ 𝔗″, a label z and a lift-curve component L, such that for uncountably many t the point (q_t,t) lies on L, with both branches in T′ and T″ respectively and z_t = z. Then L ⊂ T′ ∩ T″, since an irreducible curve meeting an analytic set in uncountably many points lies in it.
4. The argument of Lemma 2.2 (the analytic set A_z is 2-dimensional) applies on T′ and on T″. So z is intact with F_z ≅ Y_t on all of T′ and on all of T″.
5. T′ ∩ {t = 0} and T″ ∩ {t = 0} are 1-dimensional, since t ≢ 0 on these irreducible 2-dimensional germs. By H_0 = id they lie in the union of the lifted branches of E′, respectively of E″, at 0. So some lifted branch ẽ′ ⊂ T′_0 and some ẽ″ ⊂ T″_0 carry z intact and ≡ Y_0.
6. This contradicts (TF). Hence Y is constant, and Y_t = Y_0 by PR-A. ∎

**Corollary 3.4 (necessary conditions for a counterexample to the problem, under (Rig)).** If Y is non-constant, then V_0 satisfies both of the following.
- **(NC1)** Every piece reachable from ∂V_0 by puncture transitions carries a constant component ≅ Y_0.
- **(NC2)** For every Q ∈ closure(⋃_{E∈ℛ} ξ(E)), every E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and every piece E″ of which Q is a puncture, there are lifts ẽ′ of E′ and ẽ″ of E″ at 0 ∈ Def(Q), and a label z, intact and ≡ Y_0 along both. That is, every Y_0-copy can be "continued" from E′ to E″ by some twin.

These are V_0-only conditions; no deformation appears in them. Any explicit counterexample to MS11 (hence to the problem) must satisfy them at every point of the reachable network, not just at one non-product point Q. In particular, at the chain endpoint where MS11 would fail, Corollary 2.5(3) and (NC2) agree: E_b carries a staying twin.

## 4. Candidate surfaces

### 4.1 Covering constructions from M_{0,5} (sketch: they satisfy TFM, so they are not counterexamples)
**Setting and assumptions (A).**
- V_0 is the image in M_g of the covering construction attached to a branched cover C → P^1 whose branch locus is the five marked points, each genuinely branched.
- closure(V_0) is described by admissible covers over M̄_{0,5}, followed by stabilisation. This is standard, cited from memory.
- Assume moreover that over the boundary points of M̄_{0,5} used below, every component of the admissible covering curve is already stable, so stabilisation contracts nothing.
- Let Δ_Γ be the stratum of the image of D_{12}°: the points 1, 2 collide, the base is R_{12} ∪_{n} R_{345}, and the pieces of ∂V_0 come from D_{12}. Y_0 is a component over R_{12}, with its node points as special points.
- Smoothness of V_0 is not used. (Covering constructions are often not smooth, e.g. the quintic example of PR-I.)

**Argument.**
- Let Q be the image of D_{12} ∩ D_{34}. The base is R_{12} —n1— R_5 —n2— R_{34}.
- Q is a puncture of the ∂V_0 piece E″ (the D_{12} piece) and of the piece E′ of D_{34}. Hence E′ ∈ ℛ by (PT).
- The constant vertices of E′ are the components over R_{34}: they cover a fixed 3-pointed sphere. The components over the moving 4-pointed component R_{125} are the non-constant ones (generically).
- Every component z over R_{34} maps onto R_{34}, so it carries a preimage of n2, and that is a node of the covering curve (by (A) this node survives stabilisation).
- Moving from Q into D_{12} smooths n2, hence smooths every node over n2. So such a z is merged along **every** lift of the E″ branch.
- Thus (TF) holds: vacuously if no component over R_{34} is ≅ Y_0, and because every such twin merges otherwise.
- By Theorem 3.3, Y_t = Y_0 under (Rig).

This recovers PR-I Proposition 3 (the quintic case, where the twin C over R_{34} sits inside the moving vertex along ∂V_0) without using (O) or Krull at time t, and extends it to all covering constructions from M_{0,5} satisfying (A).

The sketch status is due to (A) and to the admissible-cover description, which are cited, not proved. Without (A), a rational bridge over R_5 could be contracted. A component over R_{34} might then stay intact and constant along D_{12}, giving a staying twin, and (TF) can fail. I did not analyse that case.

### 4.2 Other candidates
- **Loci in the hyperelliptic locus of genus 3** (round10_q4 §4(c)). The totally geodesic surfaces I know there are covering constructions from M_{0,5} (cited from memory, not checked). For them §4.1 applies when (A) holds. I could not determine whether smooth examples violating (A) exist.
- **Flex and gothic loci** (cited from memory: Mirzakhani–McMullen–Mukamel–Wright / Eskin–McMullen–Mukamel–Wright). These are primitive totally geodesic surfaces in **M_{1,3}**, not in M_g. They are not admissible V_0 for the problem as stated, which concerns closed subvarieties of M_g, so they are not candidates here. I do not know a primitive totally geodesic surface in an unmarked M_g to test.
- **Explicit configuration for MS11.** By Corollaries 2.5 and 3.4, a counterexample needs all of the following:
  - a V_0 satisfying (NC1) and (NC2) at every point of the reachable network (staying twins everywhere);
  - a non-product point Q with |G·L| ≥ 2;
  - a failure of (1L) via (F-a) or (F-b).

  I found no surface with even (NC1) together with a non-product twin point, other than symmetric covering constructions. Those violate (NC2) by §4.1 (under (A)). **Attempt stopped here: no counterexample.**

## 5. Is the component-wise wording enough for the chain (steps 2(c), 2(d))?

Yes, as far as I can check, provided Lemma B1(a) and entry 100's transfer hold as stated.
- **Endpoint 2(d).** The chain needs one sheet T of b̃ on which x is persistent. Lemma B1(a) gives a non-empty open subset of b̃ ∖ 0 at t = 0 on which x is intact and ≡ Y_0. The identity theorem along b̃ then contradicts MERGE or MOV. "Some sheet" is exactly what is needed.
  - Lemma 2.2 gives an independent route to the open set: T ∩ {t = 0} is 1-dimensional and contained in the lifted branches of b, and A_x = T.
  - One point should be checked in B1(a): that T ∩ {t = 0} lies in b̃ itself and not in another lift σb̃. If it lay in σb̃, one would get x intact along σb̃, i.e. σ^{-1}x along b̃. That is a twin, not x, and the contradiction would be lost.
- **Transfer 2(c).** Persistence of x on a sheet of β̃′_m is an analytic identity (A_x = sheet) on an irreducible set. It therefore continues along the irreducible travel family of D^{m+1} (entry 100; R7-3 Lemma 2, steps 3–4, where pattern and label data are constant on irreducible families) to every sheet of β̃_{m+1} contained in that travel family. "Some sheet" again suffices.
  - The point to watch is the same: the label carried along must be the t = 0 continuation of x_m, not an Aut(G)-relabelling. For non-product strata of D^{m+1}, the sheet's slice may lie over ρE_t rather than E_t inside the same lifted family W (R8-2 Lemma U). I did not re-verify the R(D) repair that is said to fix the label; I flag it.
- **Simplification.** By Lemma 2.2, the induction claim can be stated as "x_m ∈ Y(L) for some L ∈ 𝓛(β̃_m)", and MS11 as Proposition 2.3. By Proposition 3.1, the piece-level statement (every chain piece lies in 𝒩) is already proved without MS11. Only the label-level statement needs MS11.

## 6. Summary: proved / sketched / open

**Proved** (modulo the cited R8-2 Theorem 1, PR-A, PR-B, R7-3 Lemmas 1–2, Lemma B1(a), and standard analytic facts):
- §1: refuting MS11, by either route, amounts to a counterexample to the problem under (Rig), or an error in a PROVED entry.
- Lemma 2.1: every transport sheet contains a lift-curve component.
- Lemma 2.2: the persistent labels of a sheet are exactly Y(L) for any lift-curve component L in it.
- Proposition 2.3: the exact reformulation of MS11.
- Corollary 2.4: the sufficient condition (1L).
- Corollary 2.5: the anatomy of a failure, with mechanisms (F-a) and (F-b).
- Proposition 3.1: ℛ ⊂ 𝒩, twin-free.
- Corollary 3.2: criterion R.
- Theorem 3.3: the twin-free t = 0 criterion TFM.
- Corollary 3.4: the necessary conditions (NC1), (NC2) for a counterexample.

**Sketched:**
- §4.1: covering constructions from M_{0,5} under (A) satisfy TFM, hence the conclusion under (Rig).
- §5: the component-wise wording suffices for the chain, with two flagged checks (B1(a) lands in b̃ itself; label consistency in the transfer for non-product pieces).

**Not proved / open:**
- **MS11 itself: open, neither proved nor refuted.** Precisely where each attempt stopped:
  - Mechanism D: connectedness does not control which lift-curve components are met (§2, end).
  - (1L): no general reason why a 3-fold component should contain only one lift-curve component; both (F-a) and (F-b) are unexcluded.
  - Counterexample search: no V_0 known satisfying (NC1) and (NC2) with a non-product twin point.
- **New open targets, V_0-only (t = 0), twin-free, and each sufficient for the problem under (Rig):**
  - (MS-R): ℛ ⊄ 𝒩_0;
  - more generally (MS-TF): the hypothesis of Theorem 3.3 holds at some point.

  A twin-free version of Proposition K would prove (MS-R). It would use the Mod-invariant functional 𝔪(X) = inf over subsurfaces Σ of type Σ_i of [max Ext(∂Σ) + d(ψ_Σ(X), Y_0)] instead of the marked Σ_i. Its endpoint branch would lie on a piece with no constant Y_0-component, i.e. outside 𝒩_0. The gap is termination: along the chosen Teichmüller rays some twin subsurface might keep a short boundary and ψ ≈ Y_0 forever. Lemma NH only lengthens ∂Σ_i of the marked subsurface. Interior (IMOV) transitions would also have to be handled, as in entry 99.
- (Rig) (entry 82) remains open, as before.




## Prior results, part 5: round 12 (verbatim answer files, bookkeeping line removed; re-check what you use). These are the round-12 attacks on MS11♭; their labels (Lemma F, Lemma A, Prop. B, Lemma G1–G4, Φ, Lemma 1.1/1.2, Prop. 2.1, Lemma 4.1, (R-twin), (γ°) Lemmas 1–5) are used in the sketch.

### round12_q7 (verbatim)
# round12_q7 — attempt on the (β)-twist obstruction to MS11♭

**Status line.** PARTIAL. I do not prove MS11♭, and I do not build a counterexample. What I do: I replace the single function Y by the finite family Φ of all *non-constant* constant-vertex value functions with value Y_0 at t = 0 ("Φ-persistence"). In this reformulation every (β)-twist (and the initial twist) whose twin y has a **non-constant** value function ψ is harmless: persistence passes the twist, though its function changes from Y to ψ. The only surviving form of the (β)-obstruction is the **rigid-twin case**: on T the twin y has value ≡ Y_0 for all t. The same dichotomy holds at the endpoint: the merging label x is rigid on every anchored sheet of b̃. So the obstruction is sharpened from "an automorphism of Q lost by Q_t" to "a Φ-copy and a rigid copy of Y_0 exchanged by an automorphism at t = 0". The rigid-twin case stays open. The task's own criteria make this a partial answer.

Readings (R1), (R2) and the definitions (pieces, charts, labels, anchored sheets, lift-curves, P(T), C(L)) are those of the task file. Throughout: (Rig) holds, Y is non-constant (for contradiction), and the disc Δ is shrunk where needed.

---

## 1. The family Φ and Φ-persistence

**Constant-vertex value curves (R8-2, Lemma U and U4; re-checked).** Let W be a 2-dimensional irreducible component of a lifted family 𝒲_G, and u ∉ M_W a constant vertex. Then Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t. Near t = 0, Γ_{W,u} (mapped to the coarse space 𝔐_u = M_u/S_{n_u}) is a finite union of irreducible local branches. Each branch is the graph of a multivalued (Puiseux) function of t.

**Definition.** Φ is the set of local branches φ at t = 0 of the curves Γ_{W,u} with
- (g_u, n_u) = (g_i, n_i),
- φ(0) = Y_0 (as classes in 𝔐 = M_{g_i,n_i}/S_{n_i}),
- φ not constant.

Here W ranges over the finitely many components of the 𝒲_G meeting {t = 0} near the relevant compact set, after shrinking Δ. So Φ is finite. Y ∈ Φ: Y is the value curve of the constant vertex i of ∂V_t, and it is non-constant by assumption.

A label z (chart vertex) at a point is a **rigid Y_0-copy** along something if its value is ≡ Y_0 there for all t.

**Definition (Φ-persistence).** Let T be an anchored sheet (germ at (0,0) of an irreducible 2-dimensional analytic set in B × Δ_ε) and z a label. z is **Φ-persistent on T, with function φ ∈ Φ**, if at every (p,t) ∈ T, z is intact at p and (class of F_z(p), t) lies on the branch φ. Put P_Φ(T) := {z : z is Φ-persistent on T with some φ ∈ Φ}. Since T is irreducible and the branches are finitely many, the function φ is determined by (z, T). Also P(T) ⊂ P_Φ(T): P(T) is the set of z with φ = Y.

**Generic times for Φ.** Put Z_Φ := ⋃_{φ∈Φ} Z_φ. Here Z_φ is the set Z of R8-2 §3 with Y replaced by φ:
- φ(t) ∈ 𝔉; or
- (φ(t), t) lies on some Γ_{W,u} whose branch through it is not φ; or
- φ(t) = φ′(t) for some φ′ ∈ Φ ∖ {φ}.

Each condition gives a discrete set, because φ is non-constant and distinct irreducible curves meet discretely. Φ is finite, so Z_Φ is discrete.

**Lemma 1.1 (Theorem 1 of R8-2 for every φ ∈ Φ).** Let t ∉ Z_Φ, and let y be a φ(t)-copy at a lift q of Q ∈ B_t, with φ ∈ Φ. Let b̃ be a lifted branch through q. Then y is either STAY along b̃, with (W,y) a φ-vertex (its value curve is the branch φ), or IMOV.

*Proof.* This is the proof of R8-2 Theorem 1 verbatim, with Y_t replaced by φ(t). The proof uses only three facts:
- φ(t) ∉ 𝔉 (for steps 1, 2 and 4);
- (φ(t), t) lies on no other value curve (for step 3);
- 𝔉 is a finite, t-independent set (from (Rig), through Lemma U).

The remark after Theorem 1 ("never compares two copies") applies unchanged. ∎

**Lemma 1.2 (constant vertices of a piece carry their value curve along a whole sheet).** Let c be a piece at t = 0, c̃ a lifted branch of c at Q, and T an anchored sheet of c̃. Let y be a label that is intact and constant along c̃ at t = 0, with F_y ≅ Y_0 there. Then T determines one branch ψ of a value curve Γ_{W,y} with ψ(0) = Y_0, such that at every (p,t) ∈ T, y is intact with F_y(p) of class ψ(t). Consequently exactly one of the following holds:
- ψ is non-constant, so ψ ∈ Φ and y ∈ P_Φ(T);
- ψ ≡ Y_0, and y is a rigid Y_0-copy on T.

*Proof.*
- T is irreducible. Its generic points (t ≠ 0) lie over the transported piece c_t = H_t(c). Fixing the identification of the generic pattern with G_c gives a holomorphic map from a dense open subset of T to ∏_w M_w. Its image is irreducible, so it lies in one component W ⊃ ĉ × {0} of 𝒲_{G_c}.
- y is constant on ĉ, so y ∉ M_W by U1 (constancy on one fibre component is equivalent to constancy on all).
- So on T over c_t, y is intact with constant value, and that value lies on Γ_{W,y}.
- At the points of T over Q_t (the lift-curves), y is still intact, and its value is the limit of the constant value. This uses c_D ∈ ∏ M_u (Lemma U), so constant values are smooth curves and no edge at y opens.
- T is irreducible, so the value t ↦ F_y lies on a single branch ψ.
- At t = 0, y is intact with F_y ≅ Y_0 along c̃, so ψ(0) = Y_0. ∎

## 2. The (β)-twist in the Φ-reformulation

**Proposition 2.1 (twists with a non-rigid twin are harmless).** Let T, σT be a (β)-edge: anchored sheets of one lifted branch c̃, with σ ∈ Stab_pt(c̃). Let x ∈ P_Φ(T), and put y := σ^{-1}x.
1. P_Φ(σT) = σP_Φ(T). If z ∈ P_Φ(T) has function φ on T, then σz has the same function φ on σT.
2. x ∈ P_Φ(σT) if and only if y ∈ P_Φ(T). In that case the function of x on σT is the function ψ of y on T.
3. In the task's failure configuration (x and y intact constant twins ≅ Y_0 along c̃ at t = 0, with x ∈ P(T) and y ∉ P(T)), Lemma 1.2 gives exactly one of:
   - ψ non-constant: then x ∈ P_Φ(σT) with function ψ, and the twist does **not** break Φ-persistence;
   - ψ ≡ Y_0: the **rigid-twin case**.

*Proof.*
1. σ ∈ Aut(Q) acts on B × Δ_ε, preserving t and the boundary. By (K3), F_{σz}(σp) ≅ F_z(p), and σ maps intact labels to intact labels. Applying this pointwise on T gives the claim.
2. This follows from (1): x ∈ σP_Φ(T) ⟺ σ^{-1}x ∈ P_Φ(T).
3. Combine (2) with Lemma 1.2 applied to y, which is intact and constant along c̃ at t = 0. ∎

The same argument applies verbatim to the **initial twist** τ ∈ Stab_pt(β̃): there the x-carrying anchored sheet of β̃ reaches X only after the twist τ.

**Corollary 2.2 (composites).** Take a path T_0, T_1, …, T_k in the sheet graph of D (inside a 3-fold component X ⊃ S × {0}), together with the initial twist. Suppose:
- every edge is a lift-curve edge, a t ≠ 0 curve edge outside (γ°), or a (β)-edge;
- at every (β)-edge (T_{j}, σ_jT_{j}), the label σ_j^{-1}x_j is not rigid on T_j, where x_j is the image of x after the earlier twists.

Then x_k := σ_{k}⋯σ_1x ∈ P_Φ(T_k). For lift-curve edges, P_Φ(T) = C_Φ(L) = P_Φ(T′) for a common lift-curve L; this is the Φ-version of round11_q4 Lemma 2.2 and is discussed in §3. For t ≠ 0 curve edges outside (γ°), persistence passes as in round11 Mechanism D, whose argument uses only Lemma 1.1.

So in the Φ-reformulation, the "label-moving composite of (β)-twists" obstruction reduces exactly to the rigid-twin case.

## 3. The Φ-version of the chain (what must be re-checked)

The chain of the task (steps 1–2 (a)–(d)) is phrased with "Y-persistent". Define **MS11♭_Φ**: the same as MS11♭, with
- hypothesis: "x Φ-persistent on some anchored sheet of β̃";
- conclusion: "x Φ-persistent on some anchored sheet of b̃".

The conclusion still gives, at t = 0, that x is intact along b̃ with F_x ≡ Y_0, and so still contradicts MERGE and MOV at the endpoint.

Uses of Y in the chain, with their Φ-versions:
- **Base.** Vertex i with φ = Y ∈ Φ. Unchanged.
- **Genericity.** Replace Z by Z_Φ (§1), which is still discrete.
- **Product-type endpoint (d).** It derives "Y_t lies in a finite set on an open set". The same argument gives "φ_t lies in a finite set on an open set" for the current function φ ∈ Φ. That is a contradiction because φ is non-constant.
- **P(T) = C(L)** (round11_q4 Lemma 2.2, round11_q1 Lemma 2.3). Its input is R8-2 Theorem 1 / Theorem N at generic t. Lemma 1.1 supplies this for every φ ∈ Φ, so P_Φ(T) = C_Φ(L) for boundary-type sheets, where C_Φ(L) is the set of labels whose value along L lies on some branch of Φ.
- **Lemma PT, Lemma J / Cor. J′, the transfer along D^{m+1} (B1♭, Lemma S(c)).** I have **not** re-read these proofs line by line; the file is too large to verify all of them here. Their statements use "Y" only as the value function of a constant vertex that is non-constant and generic. If any of them uses a property of Y that a general φ ∈ Φ lacks, the Φ-chain needs a repair there. I flag this as **to be checked**. I expect it to be routine, because R7-3 §4 already worked with the full family of constant-vertex functions.
- **One genuine change.** The function attached to the persistent label may change along the chain, from Y to ψ at a non-rigid twist. Every endpoint argument uses only that the current function is non-constant, so this is harmless.

**Conclusion of §§2–3.** If the substitutions above are valid (to be checked), then MS11♭_Φ, and with it MS8 and the goal under (Rig), hold unless one of the following occurs:
- the rigid-twin configuration of §4;
- the separate obstruction (γ°), not treated here.

## 4. The endpoint, and the remaining case stated precisely

**Lemma 4.1 (rigidity at the endpoint).** Let Q_0 be the endpoint of the walk, b̃ the terminal lift, and x the label that merges or moves along b̃ at t = 0. Then for every anchored sheet T_b of b̃ and every lift-curve L_b ⊂ T_b, x is a rigid Y_0-copy along L_b: on L_b, F_x ≡ Y_0, which lies in 𝔉. In particular, a (Rig) counterexample needs Y_0 ∈ 𝔉.

*Proof.*
- Take a lift-curve L. Q_t is a puncture of a piece through it. So every component of Q_t on L is either:
  - a constant vertex of that piece, whose value lies on a value curve; or
  - a component of a puncture value f_u(p), u ∈ M_W, whose class lies in the finite t-independent set 𝔉 (Lemma U3).
- Hence the value of x along L is a branch of a value curve, or a constant in 𝔉. Since F_x(0) ≅ Y_0, it is either in Φ or ≡ Y_0.
- Suppose it were in Φ along some L_b ⊂ T_b. Lemma 1.1 at generic t makes x STAY along the branches of T_b through L_b(t) (IMOV is excluded, because Q is a puncture of b by (P)). So x is intact and constant on T_b, and at t = 0 it is intact and constant along b̃. This contradicts MERGE/MOV of x along b̃.
- For the last clause: if Y_0 ∉ 𝔉, steps 1–2 of the proof of R8-2 Theorem 1 apply to the Y_0-copy x at t = 0 itself. They show that x neither merges nor puncture-moves at Q_0, so the endpoint could only be an interior MOV. ∎

So a counterexample must have, at the endpoint, a Φ-copy x along L_β ⊂ T_β and a rigid Y_0-copy a^{-1}x along L_β, where L_b = aL_β and a ∈ Aut(Q_0). This is again a rigid twin.

**Open case (R-twin).** Q ∈ B_0, a lifted branch c̃ through 0 of a piece c, a label pair x ≠ y = σ^{-1}x with σ ∈ Stab_pt(c̃) (or, at the endpoint, a ∈ Aut(Q)), and an anchored sheet T of c̃ such that:
- (i) at t = 0, x and y are intact constant Y_0-copies along c̃, exchanged by σ;
- (ii) on T, x has a non-constant value function φ ∈ Φ;
- (iii) on T, y has value ≡ Y_0 for all t (rigid), and Y_0 ∈ 𝔉.

Equivalently: the transported piece c_t has, for every t, one constant vertex of value exactly Y_0 and one of value φ(t), and these two vertices become exchanged by a generic automorphism of the curves of c at t = 0.

**Observations on (R-twin)** (true, but none of them closes the case):
1. (R-twin) is invisible at t = 0. Total geodesy (Lemma TG, Lemma PA, Lemma V) sees only V_0. At t = 0 the Φ-copy and the rigid copy are both intact constant Y_0-components exchanged by an automorphism. Distinguishing them needs first-order information in t, which round11_q6 §3 found to give nothing.
2. **Counting.** At t ∉ Z_Φ, the number m_t(q) of labels at a lift point q whose value lies on Φ is the same along every lifted branch through q at which Q is a puncture (Lemma 1.1). So m is locally constant on the Φ-network at generic t. Consequently every D-sheet T of X has the same |P_Φ(T)| = m*. A twist edge with rigid twin y swaps a Φ-label and a rigid label; it does not change the count. So counting alone cannot exclude (R-twin).
3. If no rigid Y_0-copy occurs anywhere along the walk (for instance if the only Y_0-copies of points of the walk with constant value curve are excluded by some other means), the chain closes, modulo §3's checks and (γ°).

## 5. Summary list

**Proved here.**
- Lemma 1.1: R8-2 Theorem 1 holds for every non-constant constant-vertex value function φ with φ(0) = Y_0, at t ∉ Z_Φ (Z_Φ discrete).
- Lemma 1.2: on an anchored sheet, a constant twin label carries a single value branch ψ; it is either non-constant (in Φ) or ≡ Y_0.
- Proposition 2.1 / Corollary 2.2: with Φ-persistence, a (β)-twist, or the initial twist, preserves persistence whenever the twin is not rigid. The persistent function changes from φ to ψ.
- Lemma 4.1: at the endpoint, the merging label is rigid on every anchored sheet of b̃, and a counterexample needs Y_0 ∈ 𝔉.

**Not proved / to be checked.**
- That Lemma PT, Lemma J / Cor. J′, the transfer along D^{m+1}, and round11_q4 Lemma 2.2 go through verbatim with Y replaced by a varying φ ∈ Φ (§3). I expect this to be routine, but I have not verified it.

**Open.**
- (R-twin), §4: a non-constant constant-vertex function φ and a rigid copy ≡ Y_0, exchanged at t = 0 by an automorphism σ of the curves of a piece.
- (γ°), untouched.
- (Rig) (entry 82), untouched.
- Realisability of (R-twin) by an admissible family with smooth totally geodesic V_0: no counterexample is constructed.


### round12_q8 (verbatim)
kind: answer (round12_q8)

**Plan/status.** Status: PARTIAL. I do not exclude (γ°)/(IMOV_Q), and I do not construct a counterexample. What this file does:
- §2 makes the sketched part of round11_q7 §5 precise and proves it. It turns (γ°) into a configuration stated purely in terms of the (Rig) data (M_W, K_W) of one lifted family W: the "frozen twin" and "Y inside a fixed curve" (Lemmas 1–4).
- §3 proves an extra rigidity statement: α-symmetry holds on all of K_W except for mixed pairs (Lemma 5).
- §4 explains why these data contain no contradiction by themselves, and states the precise residual open statement (O-γ°′).

Readings: (R1), (R2) with H_0 = id, (Rig), and Y non-constant (for contradiction), as in the task file. Cited inputs are used as stated in the task file and were not re-proved:
- R8-2 Lemma U and corollary U3;
- R8-3 Theorem N;
- round10_q7 Lemma I0 (every sheet contains a lift-curve);
- round11_q3 Lemma 3.1 and Prop. 3.2;
- (K3): F_y(hp) ≅ F_{h^{-1}y}(p) for h ∈ Aut(Q);
- R7-3 Lemma 1 (values of constant vertices are holomorphic in t).

## 1. The configuration (γ°), restated

The data are as follows.
- X is the 3-fold component of Lemma D1, and D = X ∩ {N = 0}.
- T_1 ≠ T_2 = gT_1 are sheets of D, with g ∈ Aut(Q).
- C ⊂ T_1 ∩ T_2 is an irreducible curve germ at (0,0), finite over Δ_ε, with C ⊂ Fix(g).
- x ∈ Π(T_1), i.e. x is Y-persistent on T_1.
- P := P(T_1) = P(T_2) = gP.
- For t outside a countable set Z″ and r ∈ C_t, x is non-constant along the branch of T_{2,t} through r, and q(r) lies in the stratum Δ_{G_c} of the coarse piece of T_1.

Further notation.
- c̃ := T_1 ∩ {t = 0} is a lifted branch of a branch c of B_0 at Q.
- Q is a puncture of the piece of c (round11_q3 Lemma 3.1: Q ∉ Δ_{G_c}).
- G_c is G_Q with the edges outside P contracted. Since gP = P, g induces an automorphism α of G_c.
- Π: L_P → ∏_{w∈V(G_c)} M̄_w is the partial normalisation map (holomorphic into ∏M_w off the locus where extra edges are pinched).
- By round11_q3 §3.6 / Lemma U, (Π, t)(T_1) lies in a 2-dimensional component W of the lifted family of the piece of c. Every fibre component is K_W × {c_t}: the coordinates in M_W run over the fixed curve K_W, and the coordinates w ∉ M_W are constants c_t[w], holomorphic in t (R7-3 Lemma 1).
- Since x is persistent on T_1, the vertex {x} is constant on the fibres, so x ∉ M_W and c_t[x] ≅ Y_t.

## 2. Proved consequences of (γ°)

**Lemma 1 (the moving twin).** Put u := g^{-1}x. Then:
1. u is intact at every point of T_1, so {u} is a single vertex of G_c;
2. F_u(p) ≅ F_x(gp) on T_1;
3. u ≠ x, and u ∈ M_W, i.e. u is a moving vertex of the fibres of W.

*Proof.*
- The edges at x lie in P, because x is intact on T_1. Hence the edges at u = g^{-1}x lie in g^{-1}P = P. The pattern at every point of T_1 contains P (closed condition), so u is intact on T_1. This gives item 1.
- Item 2 is (K3).
- For generic t, x is non-constant along T_{2,t} = gT_{1,t}. By item 2, F_u is then non-constant along T_{1,t}. Since F_x is constant along T_{1,t}, we get u ≠ x. Since u is non-constant on the fibre components for uncountably many t, U1 of Lemma U gives u ∈ M_W. ∎

**Lemma 2 (the coarse branch has two distinct lifts at 0).** g c̃ ≠ c̃. Both are lifted branches of c through 0, contained in T_2 and T_1 respectively.

*Proof.* Along c̃, F_x is constant (≅ Y_0). Along g c̃, F_x(gp) ≅ F_u(p) for p ∈ c̃, and F_u is non-constant along c̃ because u ∈ M_W and U1 applies at t = 0 too. ∎

**Lemma 3 (frozen twin at the lift-curve).** Let λ ⊂ T_1 be a lift-curve (it exists by I0), so q(λ(t)) = Q_t. Then for all small t:
- F_u(λ(t)) ≅ Y_0;
- F_x(λ(t)) ≅ Y_t.

So Q_t has two distinct components (labels x ≠ u), isomorphic to Y_t and to Y_0. Moreover Y_0 = pr_u(κ_0) for a point κ_0 ∈ K_W ∩ ∂(∏_{w∈M_W} M̄_w) at which the u-coordinate is interior.

*Proof.*
- **Intactness.** By Lemma 1, u is intact at λ(t), and F_u is continuous on L_u ⊃ T_1.
- **Limit points are punctures.** Let p_n ∈ T_{1,t} ∖ λ tend to λ(t), and let k be a limit point of Π(p_n) in ∏M̄_w. The gluing map ξ̄ is continuous, so ξ̄(k) = Q_t. Since H_t preserves strata and Q ∉ Δ_{G_c}, we have Q_t ∉ Δ_{G_c} = ξ(∏M_w). Hence k ∉ ∏M_w.
- **The M_W-part lies in a finite set.** The constant coordinates of k are the c_t[w] ∈ M_w. So some coordinate in M_W is in the boundary, and pr_{M_W}(k) ∈ F_W := K_W ∩ ∂, which is a finite set independent of t (U3).
- **The u-coordinate.** It equals F_u(λ(t)), by continuity of F_u. So t ↦ F_u(λ(t)) is a continuous function on the connected punctured germ λ ∖ {(0,0)} with values in the finite set pr_u(F_W) ∩ M_u. Hence it is constant, equal to its value at λ(0) = 0, namely F_u(0) ≅ F_x(g·0) = F_x(0) ≅ Y_0.
- **The x-coordinate.** F_x(λ(t)) ≅ Y_t because x is persistent on T_1 ∋ λ(t). ∎

This is the "rigid twin" of round11_q1 §4, now derived inside (γ°) itself.

**Lemma 4 (Y inside a fixed curve; round11_q7 §5 made precise).** Let 𝒴 be the image of pr_u(K_W) ∩ M_u in 𝔐 = M_{g_i,n_i}/S_{n_i}. It is a closed analytic curve in 𝔐. Then:
- Y(Δ) ⊂ 𝒴;
- Y_0 ∈ 𝒴, as the u-value at a puncture point κ_0 ∈ F_W;
- more precisely, for small t, Y_t = pr_u(κ(s(t))), with κ(s(t)) ∈ K_W tending to the points of F_W with u-value Y_0.

*Proof.*
- **Closedness of 𝒴.** K_W is compact, so pr_u(K_W) is closed analytic in M̄_u by Remmert. Its intersection with M_u is closed analytic there, and the image in the quotient by S_{n_i} is closed analytic.
- **Crossing points.** Let t be generic and r ∈ C_t. Since g fixes r, F_u(r) ≅ F_x(gr) = F_x(r) ≅ Y_t. Also Π(r) ∈ K_W × {c_t}, so Y_t ∈ 𝒴.
- **All of Δ.** This holds for co-countably many small t. The set 𝒴 is closed, so it holds for all small t. Then Y^{-1}(𝒴) is an analytic subset of Δ containing an open set, so it is all of Δ.
- **Limit of the crossing points.** As t → 0, r → (0,0), so Π(r) accumulates only at points of closure(Ê_0) over Q. These lie in F_W × {c_0} by the argument of Lemma 3. ∎

## 3. Symmetry forced on K_W

The point k_t := Π(r) is fixed by α, because g ∈ Stab(r). That is, k_t[αw] ≅ α_* k_t[w] for every vertex w of G_c, with the special points relabelled by α. Classify the vertices w by whether w and αw lie in M_W.

**Lemma 5.**
- (a) For every w with w, αw ∈ M_W, the identity κ[αw] ≅ α_*κ[w] holds on all of K_W.
- (b) For every w with w, αw ∉ M_W, c_t[αw] ≅ α_*c_t[w] holds for all t.
- (c) The only conditions that depend jointly on (κ, t) come from the mixed pairs. Among them is (u, x): pr_u(κ) ≅ c_t[x] = Y_t.

*Proof.*
- (a) The set A ⊂ K_W where the identities hold is closed analytic. It contains the points κ(s(t)) for co-countably many t. These points are pairwise distinct for distinct values of Y_t, since their u-coordinates are the Y_t, which take infinitely many values (Y is non-constant). So A is infinite, and A = K_W because K_W is an irreducible curve.
- (b) Both sides are holomorphic in t (R7-3 Lemma 1) and agree for co-countably many t. Apply the identity theorem.
- (c) This is what remains after (a) and (b). ∎

## 4. Why §§2–3 give no contradiction, and the residual statement

**No contradiction from these data alone.** Take local coordinates (s, t) on W near (κ_0, 0), where s is a local parameter of a branch of K_W at κ_0. Then:
- λ maps to {s = 0};
- c̃ maps to {t = 0};
- C maps into {f(s) = Y_t}, where f := pr_u∘κ and f(0) = Y_0.

If 𝒴 is a curve, Y is non-constant with Y(Δ) contained in the branch f(s), and every mixed pair (w, αw) gives an equation κ(s)[w] = φ_{αw}(t) that shares the solution curve s = s(t), then every constraint proved so far is met. So no contradiction follows from the (Rig) data, Theorem N, or the chart and sheet structure.

**Total geodesy cannot be applied directly.**
- At t = 0 the crossing points collapse into the puncture Q, where g ∈ Aut(Q) already exists. Total geodesy at t = 0 sees only that c̃ and g c̃ are two lifts of c through 0 (Lemma 2), with x constant on one and moving on the other.
- Theorem X*_all does not apply, because both sheets are of puncture type.
- The extra automorphism g of R_t = q(r_t) is not a topological invariant under the coarse reading (R2). So Lemma S cannot transport it back to t = 0.

**Residual open statement (O-γ°′), to which (γ°) is now reduced (equivalent data, by §§2–3).** Exclude the following:
- a piece E of B_0 with puncture Q, and a component W of its lifted family with (Rig) data (M_W, K_W);
- a Y-vertex x ∉ M_W and a moving vertex u ∈ M_W, exchanged by the automorphism α of G_c induced by some g ∈ Aut(Q);
- a puncture point κ_0 ∈ K_W ∩ ∂ with pr_u(κ_0) ≅ Y_0;
- such that Y(Δ) ⊂ 𝒴 = pr_u(K_W), and for all small t there is κ(s(t)) → κ_0 with (κ(s(t)), c_t) α-fixed. In particular, (a) and (b) of Lemma 5 hold, and every mixed pair satisfies κ(s(t))[w] ≅ φ_{αw}(t).

**Partial exclusion.** If dim M_{g_i,n_i} ≥ 2 and 𝒴 is a Teichmüller curve (the case where u is a max-speed vertex, Lemma PA / Prop. C), then Y moves along a Teichmüller curve in M_{g_i,n_i}. I could not exclude this.

## 5. Proved / not proved / open

**Proved** (under (R1), (R2), (Rig), Y non-constant, with the cited lemmas as inputs):
- Lemma 1 (moving twin u = g^{-1}x ∈ M_W);
- Lemma 2 (g c̃ ≠ c̃);
- Lemma 3 (frozen twin: F_{g^{-1}x}(λ(t)) ≅ Y_0 and F_x(λ(t)) ≅ Y_t for all t; Y_0 is a puncture u-value of K_W);
- Lemma 4 (Y(Δ) ⊂ pr_u(K_W), a fixed closed curve; this proves the sketched step of round11_q7 §5);
- Lemma 5 (α-symmetry on all of K_W for pairs inside M_W, and in t for pairs outside M_W).

**Not proved:**
- that (γ°) cannot occur;
- that (γ°) never obstructs MS11♭;
- MS11♭ itself;
- any counterexample.

**Open:**
- (O-γ°′) as stated in §4, equivalently "Y moves inside the fixed curve pr_u(K_W) with a frozen twin at the puncture";
- the (β)-twist obstruction (O-Bpure), untouched;
- (Rig) (entry 82), untouched.


### round12_q6 (verbatim)
# round12_q6 — Mechanism G (lift-curves in a 3-fold component X and their stabilisers)

## Status (final)
**MS11♭ is NOT proved here and NOT refuted.** What this file does:
- It describes the lift-curves exactly (Lemma G1).
- It gives an exact criterion for MS11♭ in terms of lift-curves (Lemma G2).
- It corrects the planner's observation: (1L_X) gives MS11♭ only when the initial twist τ satisfies an extra condition (Lemma G2(c)). So (1L_X) alone is not sufficient.
- It determines the local structure of 𝒳 at generic points of S × {0} (Lemma G3). The planner's three cases are not exhaustive. In particular "t = b², a single lift-curve" is false in general: an irreducible X can contain two lift-curves exchanged by an element of K_S, the pointwise stabiliser of S (Model G3′).
- It shows that such K_S-multiplicities are harmless (Proposition G4).
- It isolates what remains (§4): an element of A_X that acts non-trivially on S or moves S, or a twist τ ∉ Stab(b̃)·Stab(x).

Global input (total geodesy, Lemma TG) would be needed exactly for the residual case of §4. I could not make it work.

Conventions. I use the run's readings (R1), (R2) with H_0 = id, (Rig), and the notation of the task: A := Aut(Q) acting on the ball B ⊂ Def(Q); q : B → B/A; 𝒳 := q^{-1}(closure 𝒱) ∩ (B × Δ_ε); Λ := {(p,t) : q(p) = Q_t}; L_0 is a lift-curve. A acts on B × Δ_ε by g(p,t) = (gp,t).

The following facts are taken from the run as given (spliced in the task file). I did not re-prove them.
- (F1) Every anchored sheet contains a lift-curve (round11_q4 L2.1).
- (F2) If T is a boundary-type sheet and L ⊂ T is a lift-curve, then P(T) = C(L) (round11_q4 L2.2, round11_q1 L2.3).
- (F3) Equivariance (K3): F_{gy}(gp) ≅ F_y(p). Hence C(gL) = g·C(L), P(gT) = g·P(T), and g maps anchored sheets of c̃ to anchored sheets of gc̃.
- (F4) By (P), every anchored sheet of β̃ or of b̃ is of boundary type.
- (F5) Mechanism D: D = X ∩ {∏ s_e = 0} has a connected sheet graph. Its vertices are anchored boundary-type sheets, including anchored sheets of β̃ and of b̃. Moreover τT_x ⊂ X with τ ∈ Stab_pt(β̃) (round11_q7 D1(d)).

## 1. Lemma G1 (lift-curves) — proved
Assume, as in the run's definition, that Λ is a closed analytic subset of B × Δ_ε. Let L_0 be one irreducible component of its germ at (0,0), and put A_L := Stab_A(L_0).
- (a) Near (0,0), Λ = ⋃_{g∈A} gL_0. The lift-curves are exactly the distinct gL_0, and they correspond bijectively to A/A_L.
- (b) Put A_X := {g ∈ A : gL_0 ⊂ X}. Then G_X·A_X·A_L = A_X, where G_X := Stab_A(X). Moreover A_X = ⋃_{X′} {g : gX′ = X}, the union taken over the components X′ of 𝒳 that contain L_0. Each set {g : gX′ = X} is either empty or a coset G_X h. The number of lift-curves in X is |A_X|/|A_L|. If g ∈ A_X ∖ G_X, then L_0 ⊂ X ∩ g^{-1}X with g^{-1}X ≠ X.

*Proof.*
- (a) We have q^{-1}(Q) = A·0 = {0}, since 0 is A-fixed. So Λ ∩ {t = 0} = {(0,0)}. Hence t|_{L_0} is non-constant, and it is a finite map of an irreducible curve germ, so t(L_0) contains a neighbourhood of 0.
- Let (p,t) ∈ Λ with |t| small. Choose (p′,t) ∈ L_0. Then q(p′) = Q_t = q(p), so p = gp′ for some g ∈ A, and (p,t) ∈ gL_0.
- Each gL_0 is an irreducible curve germ, so the components of Λ are the distinct gL_0. Their stabiliser structure is the standard orbit–stabiliser count.
- (b) gL_0 ⊂ X ⟺ L_0 ⊂ g^{-1}X. Since g^{-1}X is a component of 𝒳 (𝒳 is A-invariant), this proves the union formula. The coset statement holds because gX′ = X = hX′ ⟺ gh^{-1} ∈ G_X. The rest is immediate. ∎

## 2. Lemma G2 (exact criterion; the role of τ) — proved from (F1)–(F5)
Fix a lift-curve L_1 ⊂ T_x (one exists by (F1)). Then x ∈ P(T_x) = C(L_1) by (F2) and (F4). Call a lift-curve L *x-good* if x ∈ C(L). Let Λ_b be the set of lift-curves that lie in some anchored sheet of b̃.
- (a) MS11♭ ⟺ Λ_b contains an x-good lift-curve.
- (b) gL_1 is x-good ⟺ g^{-1}x ∈ C(L_1); in particular this holds for g ∈ Stab_A(x). Λ_b is invariant under Stab_A(b̃), the setwise stabiliser of b̃. Hence MS11♭ holds as soon as Λ_b ∩ Stab_A(b̃)·Stab_A(x)·L_1 ≠ ∅.
- (c) **Correction to the planner's observation.** Assume (1L_X), i.e. X contains exactly one lift-curve L_X. Then τx ∈ P(T) for every D-sheet T of X, and in particular for every anchored sheet T_b of b̃ in X. MS11♭ follows if τ ∈ Stab_A(b̃)·Stab_A(x), e.g. if τx = x or τb̃ = b̃. Without this condition, (1L_X) only gives "x is persistent on an anchored sheet of τ^{-1}b̃". That is a different lifted branch of b, lying in τ^{-1}S.

*Proof.*
- (a) "⇐": an x-good L ⊂ T_b gives x ∈ C(L) = P(T_b) by (F2) and (F4). "⇒": x ∈ P(T_b) = C(L) for any L ⊂ T_b, and such an L exists by (F1).
- (b) C(gL_1) = gC(L_1) by (F3). If k ∈ Stab_A(b̃) and L ⊂ T_b, then kL ⊂ kT_b, which is an anchored sheet of kb̃ = b̃.
- (c) Every D-sheet T is anchored (F5), so it contains a lift-curve (F1). That lift-curve lies in X, so it is L_X, and P(T) = C(L_X).
  - τT_x ⊂ X is 2-dimensional and lies in {∏ s_e = 0}, so it is a D-sheet. Hence C(L_X) = P(τT_x) = τP(T_x) ∋ τx.
  - Write τ = k s with k ∈ Stab(b̃) and s ∈ Stab(x). Then k^{-1}T_b is an anchored sheet of b̃, and P(k^{-1}T_b) = k^{-1}P(T_b) ∋ k^{-1}τx = sx = x. ∎

Remark. In the chain's endpoint use, (τ^{-1}b̃, x) and (b̃, τx) are A-equivalent pairs. So the twisted conclusion contradicts MERGE/MOV of x along b̃ only if τ ∈ Stab(b̃)Stab(x). The twist is therefore a genuine part of the problem and is not just bookkeeping.

## 3. Local structure along S × {0} — proved
Let K_S ⊂ A be the pointwise stabiliser of S. Let p ∈ S × {0} be generic: off {∏ s_e = 0}, off the singular set, with Stab_A(p) = K_S, and S smooth at p.

**Lemma G3.** Read Lemma Red as "the central fibre of the coarse 𝒱 → Δ is reduced" (ledger entry 80), and assume 𝒱 is smooth in the coarse space near q(p).
- (a) Near p, 𝒳 = S × Λ_p, where Λ_p is the K_S-invariant lift, to the normal slice N × Δ, of a smooth coarse curve t ↦ (c(t), t). Its components are Puiseux curves, permuted transitively by K_S. So K_S permutes transitively the components of 𝒳 that contain S × {0}. In particular K_S ⊂ G_X if 𝒳 has a single component through S × {0}, for instance under the orbifold reading (Orb), in which q^{-1}(𝒱) is smooth.
- (b) Under (Orb): X is smooth at p, with coordinates (s_1, s_2, y), S = {y = 0}, and t = unit·y^m. Here m = |image of K_S in Aut(X,p)|, and K_S acts by y ↦ ζy, ζ ∈ μ_m. In particular m = 1 (t is a coordinate) iff K_S acts trivially on X.
- (c) (Tool (a)(1) of the task.) Let X be smooth at p with dt|_X ≠ 0, and let g ∈ G_X have finite order, fix S × {0} pointwise, and preserve t. Then g = id on X.

*Proof.*
- (c) By Cartan, g is linearisable at p. dg_p is the identity on ker dt_p = T_pS, and dt∘dg_p = dt. So dg_p = I + N with N(T_pX) ⊂ ker dt_p and N|_{ker dt_p} = 0. Then N² = 0. A unipotent matrix of finite order is the identity, so g = id near p. Fix(g) ∩ X is analytic and contains an open subset of the irreducible germ X, so it is all of X.
- (b) Here X = q^{-1}(𝒱) is smooth of dimension 3 near p, and X ∩ {t = 0} = q^{-1}(V_0) = K_S·S = S near p.
  - K_S fixes the smooth hypersurface S of X pointwise. After linearisation its image acts on the normal line through a faithful character group μ_{m′}. So X/K_S has coordinates (s, Y = y^{m′}).
  - t is K_S-invariant and vanishes exactly on S, so t = unit·Y^k with m = km′.
  - The coarse fibre {t = 0} is reduced, which forces k = 1.
- (a) In coarse coordinates near q(p), B/K_S ≅ S × (N/K_S), and coarse 𝒱 ⊃ V_0 = S × {0}. Coarse 𝒱 is smooth with reduced central fibre, so t|_{coarse 𝒱} is a submersion at generic points. So coarse 𝒱 is, generically over S, a family of smooth curves t ↦ (s, c_s(t), t) depending holomorphically on s.
  - The preimage of each such curve in N × Δ is a union of Puiseux curves, permuted transitively by K_S (the argument of Lemma G1(a)). For generic s the combinatorics is locally constant in s, which gives the product description.
  - A component of the germ of 𝒳 at (0,0) that contains S × {0} is, near p, a union of local components. Transitivity at p therefore gives transitivity on the global components. ∎

**The planner's three cases are not exhaustive.**
- Under (Orb) only "t = y^m, K_S ≅ μ_m on X" occurs, for every m ≥ 1. The case "X ≠ gX, t = ±b" cannot occur.
- Under the coarse reading, more general K_S-orbits of Puiseux curves occur, for example a non-reflection K_S acting on a normal plane.
- More importantly, the generic structure along S × {0} says nothing about the lift-curves. Those curves meet {t = 0} only at the origin, where X need not be a product.

**Model G3′ (proved, chart-level): an irreducible X with two lift-curves exchanged by k ∈ K_S.**
- Take chart coordinates (a, b, y, …) with k : y ↦ −y, and S = {y = 0} (coordinates a, b). Let Q_t lie on {a = b = 0}.
- Let X := {y² = t² + t a} (other coordinates 0).
  - X is irreducible, because t(t+a) is not a square.
  - X is k-invariant, and its central fibre is supported on S.
  - At generic points (a ≠ 0), X is smooth with t = y²/a·unit, which is case (b) with m = 2.
  - Its coarse image {Y = t² + ta} (Y = y²) is smooth, with reduced central fibre.
- X ∩ {a = b = 0} = {y = ±t}. These are two lift-curves L, kL ≠ L, both in X, and Q_t loses k.

So (1L_X) fails here, contrary to the planner's local evidence for the case "t = b²". The failure is harmless, by the next proposition.

**Proposition G4 (proved from (F1)–(F5)).** Put L_1′ := τL_1 ⊂ τT_x ⊂ X. Suppose:
- (i) every lift-curve of X that lies in an anchored sheet of b̃ inside X has the form kL_1′ with k ∈ Stab_A(b̃) (for instance, all lift-curves of X are K_S-translates of L_1′; note that K_S ⊂ Stab_A(b̃) because b̃ ⊂ S); and
- (ii) τ ∈ Stab_A(b̃)·Stab_A(x).

Then MS11♭ holds.

*Proof.* By (F5) there is an anchored sheet T_b of b̃ in X. It contains a lift-curve (F1), which lies in X, so by (i) it is kτL_1. Then kτ ∈ Stab(b̃)Stab(x) by (ii), and Lemma G2(b) applies to the curve kτL_1 ∈ Λ_b. ∎

So the K_S-part of A_X never matters, even under the coarse reading. In that reading the components kX (k ∈ K_S) through S × {0} are just as good as X, since k fixes β̃ and b̃ pointwise.

## 4. What remains (residual configuration) — not proved
By G2 and G4, a failure of MS11♭ needs at least one of the following.
- **(R-a)** A lift-curve gτL_1 ⊂ X lying in an anchored sheet of b̃, with g ∉ Stab(b̃)·K_S. This needs one of:
  - g ∈ G_X acting non-trivially on S (g ∈ Stab(S) ∖ K_S, a "reflection" of S); by Lemma TG, Fix(g) ∩ S is then a Teichmüller disc or consists of boundary curves;
  - g ∉ G_X, with X ∩ g^{-1}X ⊃ L_0, i.e. two 3-fold components meeting along a lift-curve, where g^{-1}X ⊃ g^{-1}S × {0} and g^{-1}S ≠ S.

  In either case g ∉ Aut(Q_t) for generic t: Q_t loses g.
- **(R-b)** The initial twist τ ∈ Stab_pt(β̃) does not lie in Stab(b̃)·Stab(x). Since τ fixes β̃ pointwise, either τS ≠ S, or τ is a reflection of S whose fixed set contains β̃.

**Where global input must enter.** All the constraints used in G1–G4 are chart-local. The run already has chart-level models realising (R-a)/(R-b) failures (round11_q7 §6, round11_q1 §5, round11_q2 §1.2). So no chart-local argument can exclude them.
- The candidate global input is total geodesy: Lemma TG applied to g on S, together with Lemma PA (constant vertices carry no area).
- One would need: a reflection g of S that fixes the boundary curve β̃ (or a Teichmüller disc), and is lost by Q_t, cannot exchange a Y-persistent copy with a non-persistent one.
- I could not derive this. In particular, I found no mechanism linking the action of g on S at t = 0 to which labels are persistent at t ≠ 0. Persistence is read off the lift-curves, which see S only at the origin.

## Summary
**Proved** (modulo the run's facts F1–F5, cited not re-proved):
- Lemma G1: lift-curves form one A-orbit; the lift-curves in X form a union of cosets G_X h.
- Lemma G2: an exact criterion for MS11♭; (1L_X) implies MS11♭ only under τ ∈ Stab(b̃)Stab(x). The planner's observation needed this correction.
- Lemma G3: the local structure along S × {0}. The three-case list is not exhaustive. Tool (a)(1) is proved.
- Model G3′: (1L_X) can fail through K_S even for irreducible X.
- Proposition G4: K_S-multiplicity is harmless.

**Not proved:** MS11♭. Steps 2 and 3 of the task are not achieved; (1L_X) is false in general, as Model G3′ shows.

**Open:**
- (O-G1) Exclude (R-a): an element of A acting non-trivially on S, or moving S, that relates the x-good lift-curve to the lift-curves of the anchored b̃-sheets.
- (O-G2) Exclude (R-b), or show that τ can always be chosen in Stab(b̃)Stab(x).
- (O-G3) The run's open (Rig) (entry 82).

No counterexample was constructed.


### round12_q2 (verbatim)
# round12_q2 — attempt on MS11♭

**Status line.** MS11♭ is **neither proved nor refuted** here. I prove one new structural lemma about the 3-fold component X: its lift-curves form a single G_X-orbit (Lemma A). This merges the planner's two failure modes into one and reduces (1L_X) to a group-theoretic condition. I also show that the planner's step-4 claim ("if g ∈ G_X fixes S × {0} pointwise, then g fixes L_0") is **false** in a local model that is consistent with every constraint used so far. The model is the natural "V_0 lies in a symmetric locus" situation, which covering constructions produce. Finally I re-check the logic of the chain at the points where MS11♭ is used. I found no flaw there, but I did not re-audit the entries it cites.

Readings: (R1), (R2) with H_0 = id, as in the brief. Notation: G := Aut(Q), q: Def(Q) → Def(Q)/G, B, ε, S, lift-curves, C(L), P(T), anchored sheets — all as in the brief. 𝒮 := q(S) is a coarse sheet (irreducible germ) of closure(V_0) at Q.

---

## 1. Lemma A (lift points in a 3-fold component form one G_X-orbit) — proved

**Setting.** X is an irreducible component of q^{-1}(closure 𝒱) ∩ (B × Δ_ε), with X ⊃ S × {0}. (By the choice of B and ε in MS11♭, such components are the germ components at (0,0).) Put G_X := Stab_G(X).

**Step 0 (coarse sheets of closure 𝒱; standard facts plus (R2)).**
- Let 𝒮_1, …, 𝒮_r be the irreducible components of the germ of closure(V_0) at Q.
- Standard fact (cited from memory): for a pure-dimensional germ (A, z) and a nowhere dense analytic Z ⊇ Sing A, and for a cofinal system of small neighbourhoods U, the connected components of (A ∖ Z) ∩ U correspond bijectively to the irreducible components of the germ. Their closures are the components. Inclusions between members of the system induce these bijections.
- V_0 is smooth, so V_0 ∩ 𝒮_k ∩ 𝒮_l = ∅ near Q for k ≠ l, and the components of V_0 ∩ W are the sets 𝒮_k ∩ V_0 ∩ W.
- 𝒱 is a manifold, so Sing(closure 𝒱) lies in the boundary. The sets H(W × D) (W a neighbourhood of Q in closure(V_0), D a disc about 0) form a neighbourhood basis of (Q,0), since H is a homeomorphism. Also 𝒱 ∩ H(W × D) = H((V_0 ∩ W) × D), whose components are the sets H((𝒮_k ∩ V_0 ∩ W) × D).
- Sandwiching this system between Milnor balls of closure(𝒱) gives the following. The irreducible components of the germ of closure(𝒱) at (Q,0) are exactly the sets 𝒳_k := H(𝒮_k × Δ_ε) (germs).
- 𝒳_k ∩ {t = 0} = 𝒮_k. Since q(X) is an irreducible component containing 𝒮 × {0}, we get q(X) = 𝒳 := H(𝒮 × Δ_ε).

**Step 1 (𝒳 is unibranch along the section).** For every small t, the germ (𝒳, (Q_t,t)) is irreducible, where Q_t = H_t(Q).
- *Proof.* Use the neighbourhoods H(W × D_t), with D_t a small disc around t. Then (𝒳 ∖ ∂) ∩ H(W × D_t) = H((𝒮 ∩ V_0 ∩ W) × D_t). This set is connected for a cofinal family of W, because 𝒮 is an irreducible germ (Step 0 applied to 𝒮). It lies in Reg(𝒳), because at points of 𝒱 only one component passes. By the standard fact, the germ is irreducible. ∎
- The same argument shows that 𝒳 is unibranch at (z, t) for every z ∈ 𝒮 ∩ V_0 near Q.

**Lemma A.** Let z ∈ 𝒳 be a point at which the germ of 𝒳 is irreducible, e.g. z = (Q_t, t) for small t, or z ∈ H((𝒮 ∩ V_0) × Δ_ε). Then the points of X over z form a single G_X-orbit.

*Proof.*
- Let p, p′ ∈ X with q(p) = q(p′) = z. Then p′ = gp for some g ∈ G.
- Let X_p be an irreducible component of the germ of X at p. Then q(X_p) is an irreducible 3-dimensional germ at z inside the irreducible 3-dimensional germ (𝒳, z), so q(X_p) = (𝒳, z).
- Near p′, q is the quotient by Stab(p′) (standard for finite group actions). The irreducible components at p′ of q^{-1}(𝒳, z) therefore form one Stab(p′)-orbit (standard: the preimage of an irreducible germ under a finite quotient).
- Both gX_p and any component X_{p′} of the germ of X at p′ are such components. Hence X_{p′} = k g X_p for some k ∈ Stab(p′).
- Then kg·X and X are irreducible components of the G-invariant set q^{-1}(closure 𝒱) ∩ (B × Δ_ε), and they share the 3-dimensional germ X_{p′}. Hence kgX = X, i.e. kg ∈ G_X, and kg·p = k p′ = p′. ∎

**Corollary A1 (lift-curves of X).**
- (a) X contains a lift-curve.
- (b) If L_0 ⊂ X is one, the lift-curves contained in X are exactly the hL_0 with h ∈ G_X.
- (c) Consequently (1L_X), "X contains exactly one lift-curve", holds iff G_X ⊆ H := Stab_G(L_0).
- (d) The planner's set A_X = {g : gL_0 ⊂ X} equals G_X·H.
- (e) The planner's second failure mode ("a second 3-fold component gX ≠ X meeting X along a lift-curve") is **subsumed** by the first: if gL_0 ⊂ X, then gL_0 = hL_0 with h ∈ G_X.

*Proof.*
- (a) (Q_t, t) ∈ 𝒳 = q(X), so X contains lifts of Q_t for every t. X ∩ 𝒥 is analytic and surjects onto Δ_ε, so it contains a curve not lying in {t = 0}.
- (b) Let L ⊂ X be a lift-curve. For each t ≠ 0, a point of L over t equals h_t·p_t with p_t ∈ L_0 and h_t ∈ G_X (Lemma A). Some h occurs for uncountably many t, so L ∩ hL_0 is infinite, and L = hL_0 since both are irreducible curve germs.
- (c), (d) follow from (b). (e) is (b) applied to L = gL_0. ∎

**Corollary A2 (MS11♭ in terms of G_X).** Suppose the x-persistent anchored sheet T of β̃ lies in X (as the brief notes, this can be arranged after an initial twist τ ∈ Stab_pt(β̃)), and let L_0 ⊂ T. Then:
- every D-sheet Σ of X of boundary type has P(Σ) = h·C(L_0) for some h ∈ G_X (Lemma 2.3 of round11_q1 / Lemma 2.2 of round11_q4, together with A1(b));
- MS11♭ holds for (Q, β̃, b̃, x) as soon as **C(L) is the same for all lift-curves L ⊂ X**, i.e. h·C(L_0) = C(L_0) for all h ∈ G_X. A sufficient condition is (1L_X).

**Corollary A3 (monodromy form of (1L_X)).**
- Fix t_* ≠ 0 small and let F be the set of lift points of Q_{t_*} lying in X. As a G_X-set, F ≅ G_X / A, where A := Stab_{G_X}(p) for p ∈ F.
- The monodromy μ of the finite covering {lift points in X} → Δ_ε^* around t = 0 commutes with G_X (G acts trivially on t). So μ is right multiplication by some n ∈ N_{G_X}(A)/A.
- The lift-curves in X correspond to the ⟨μ⟩-orbits on F.
- Hence (1L_X) holds iff ⟨n⟩ acts transitively on G_X/A. That requires A ⊲ G_X and G_X/A = ⟨n⟩ cyclic.
- In particular (1L_X) **fails whenever G_X/A is not cyclic** (for example G_X ⊇ (ℤ/2)² acting freely on F).

**Lemma A4 (X_0 and G_S).** Let K_S be the pointwise stabiliser of S, which equals the stabiliser of a generic point of S. Then:
- X_0 := X ∩ {t = 0} equals ⋃_{h ∈ G_X} hS as a set;
- G_S := Stab_G(S) ⊆ K_S·G_X.

*Proof.*
- Let z ∈ 𝒮 ∩ V_0 be generic and p ∈ S a lift of z. Then Stab(p) = K_S.
- First claim. Let g′S ⊂ X_0 be a translate. By Lemma A at (z,0), g′p = hp with h ∈ G_X. So h^{-1}g′ ∈ K_S, and g′S = hS. Conversely X_0 ⊇ S is G_X-invariant, so it contains every hS with h ∈ G_X.
- Second claim. Let g ∈ G_S. Then gX ⊇ S × {0} as well, so gX and X both contain the germ of S × {0} at (p,0).
  - Near (p,0), q^{-1}(𝒳) is the preimage of the manifold germ 𝒱 at (z,0). Its irreducible components at (p,0) form one Stab(p) = K_S-orbit.
  - A component of gX at (p,0) is therefore k times a component of X at (p,0), for some k ∈ K_S. So gX = kX, i.e. k^{-1}g ∈ G_X. ∎

## 2. The planner's step 4 is false in a consistent local model

**Claim (planner, step 4, 2-dimensional analogue of Lemma D3).** If g ∈ G_X fixes S × {0} pointwise, then gL_0 = L_0.

**Local model (counterexample to the claim).**
- Let k ≥ 2 and ζ = e^{2πi/k}.
- Let X be the smooth 3-fold germ with coordinates (a, w_1, w_2), with t = a^k on X. So X_0 = {a = 0} =: S, set-theoretically.
- Let G = ⟨g, h⟩ ≅ (ℤ/k)², acting by g(a, w_1, w_2) = (ζa, w_1, w_2) and h(a, w_1, w_2) = (ζa, ζw_1, w_2). Both preserve t.
- Let L_0 := {w_1 = a, w_2 = 0}, a curve on which t = a^k has degree k.

**Checks.**
- g fixes X_0 = {a = 0} pointwise, and g ∈ G_X = G.
- hL_0 = L_0, since h(a, a, 0) = (ζa, ζa, 0).
- gL_0 = {w_1 = ζ^{-1}a, w_2 = 0} ≠ L_0.
- The orbit of (a, a, 0) with a^k = t is {(ζ^{i+j}a, ζ^j a, 0)}, which has k² = |G| points. So the lift points over t form one G-orbit with trivial stabiliser, as (K1), (K4) require when Aut(Q_t) is trivial in this chart. The lift-curves are L_0, gL_0, …, g^{k−1}L_0, all in X, exactly as Lemma A predicts. Here G_X/A = G is not cyclic, so (1L_X) fails, consistently with A3.
- Coarse picture. Locally Def ≅ (a, w)-space and the coarse family near a generic point of S is X/⟨g⟩ with coordinate α = a^k = t. This is smooth with t a submersion. So the coarse family V_t = {α = t} is a smooth family of smooth surfaces. V_0 = {α = 0} lies in the locus of curves admitting the automorphism g, and V_t (t ≠ 0) leaves it.
- This is the typical behaviour when V_0 lies inside a symmetric locus: a covering construction, all of whose curves carry a deck group, deformed out of that locus.
- If g swaps two Y_0-labels x, gx of Q, it can happen that C(L_0) ∋ x and C(gL_0) = gC(L_0) ∌ x. Nothing local forbids this.

So "g fixes S pointwise" gives no control of lift-curves. Mode (F-a)/(F-b) of round11_q4 is exactly the situation "V_0 ⊂ Fix(g), V_t ⊄ Fix(g)", which is natural rather than exotic.

(Remark. The model contains no boundary data, i.e. no plumbing coordinates s_e. It only tests the group-theoretic claim. A version with boundary is obtained by adding coordinates on which N vanishes along curves in S; this changes nothing above.)

However, §3 shows that this symmetric-locus mechanism is **harmless for MS11♭**. The failure of step 4 does not produce a failure of MS11♭.

## 3. Proposition B: elements of K_S never cause a failure — proved (partial result)

**Proposition B.** Assume MS11♭'s setting. Suppose:
- (h1) some x-persistent anchored sheet T of β̃ lies in a 3-fold component X with X ⊇ S × {0};
- (h2) for some lift-curve L_0 ⊂ T, every h ∈ G_X lies in K_S·Stab_G(L_0).

Then MS11♭'s conclusion holds for (Q, β̃, b̃, x).

More precisely, (h2) can be weakened to:
- (h2′) there is a D-sheet Σ_b of b̃ in X whose lift-curve hL_0 (h ∈ G_X, Corollary A1) satisfies h ∈ Stab_pt(b̃)·Stab_G(L_0).

*Proof.*
1. By round11_q1 Lemma 3.1 (re-checked), D = X ∩ {N = 0} has a D-sheet Σ_b that is a transport sheet of b̃ and contains b̃ × {0}. The argument: b̃ × {0} ⊂ (S × {0}) ∩ {N = 0} ⊂ D; the D-sheet containing it is a 2-dimensional irreducible germ in q^{-1}(closure 𝓑) containing b̃ × {0}, so it is a transport sheet of b̃ by round11_q1 Lemma 2.2. So Σ_b is anchored.
2. By Lemma 2.1(c) of round11_q1, Σ_b contains a lift-curve, which lies in X. By Corollary A1(b) it is hL_0 with h ∈ G_X.
3. Write h = k h′ with k ∈ Stab_pt(b̃) and h′ ∈ Stab(L_0). Under (h2), k ∈ K_S ⊆ Stab_pt(b̃), since b̃ ⊂ S. Then hL_0 = kL_0.
4. k fixes b̃ pointwise, so kÑ_b̃ is the component of q^{-1}(N_b) containing k(b̃ ∖ 0) = b̃ ∖ 0. Hence kÑ_b̃ = Ñ_b̃.
   - Therefore k^{-1}Σ_b is an irreducible component of closure(Ñ_b̃) containing k^{-1}(b̃ × {0}) = b̃ × {0}, i.e. an anchored sheet of b̃.
   - It contains k^{-1}hL_0 = L_0.
5. By (P), Q is a puncture of the piece of b, so k^{-1}Σ_b is of boundary type. By round11_q1 Lemma 2.3 (P(Σ) = C(L) for every lift-curve L in a boundary-type sheet; this uses Y non-constant, which is part of MS11♭'s setting), P(k^{-1}Σ_b) = C(L_0).
6. x ∈ P(T) and L_0 ⊂ T, so x ∈ C(L_0) (evaluate on L_0). Hence x is Y-persistent on the anchored sheet k^{-1}Σ_b of b̃. ∎

**Consequence (what a failure of MS11♭ now requires).** Every 3-fold component containing S × {0} is of the form kX with k ∈ K_S: at a generic (p,0), p ∈ S, the components of q^{-1}(𝒳) form one K_S-orbit (proof of Lemma A4). If MS11♭ fails, then one of the following holds.
- **(R1) sheet-switching initial twist.** No x-persistent anchored sheet of β̃ lies in any 3-fold component containing S × {0}.
  - Let T ⊂ X_T. Then X_T ∩ {t = 0} ⊇ β̃ consists of chart sheets, and the one through β̃ that matters, S_T, is ≠ S.
  - So β̃ lies in two distinct chart sheets S ≠ S_T. (If S_T = S, then X_T ⊇ S × {0} and (h1) holds.)
  - Typical case: S_T = σS with σ ∈ Stab_pt(β̃) ∖ G_S. This is the "initial twist" of the brief, which must therefore also move the sheet S.
- **(R2) a local, non-global symmetry.** (h1) holds but (h2′) fails. Then some h ∈ G_X ∖ K_S·Stab(L_0) carries L_0 into a b̃-sheet. Such an h acts **non-trivially on X_0 = G_X·S** (Lemma A4):
  - either h ∈ G_S ∖ K_S acts on S as a non-trivial automorphism (e.g. the reflection of round11_q1 §5);
  - or hS ≠ S is another chart sheet in X_0.

  Moreover h ∉ Stab_pt(b̃)·Stab(L_0).

Compared with the planner's analysis, this removes all automorphisms of Q that are **global symmetries of the sheet** (elements of K_S: automorphisms of every curve of V_0 near Q on that sheet, for instance deck groups of covering constructions), whether or not V_t keeps them. In particular the §2 model, where G_X = K_S·H, is harmless. What remains is the case where the lost automorphism acts non-trivially on the t = 0 sheet (R2), or where β̃ lies in two chart sheets interchanged by a twist (R1).

This is a partial result in the sense of the task: it proves MS11♭ under the extra hypotheses (h1), (h2′). It does not answer the question.

**Remark (where (R1) might be removed: a suggestion, not proved).**
- MS11♭ as stated gives only *some* x-persistent anchored sheet T of β̃. In the chain, β̃_m comes with the chart sheet S_m of the canonical lift (Lemma S̃′).
- If the chain's induction claim were strengthened to "x_m is Y-persistent on an anchored sheet of β̃_m lying in a 3-fold component containing S_m × {0}", then (R1) would never arise, and Proposition B would reduce each non-product transition to (R2).
- This needs two things, neither of which I have proved:
  - (i) the base case (product-type Δ_Γ, where every sheet of every lift of ∂V_0 carries vertex i, so the base case is automatic);
  - (ii) the transfer along D^{m+1} preserving "lies in a 3-fold component containing the canonical sheet". This is a local question at generic points of the lifted piece: which 3-fold components through (p,0) contain a given transport sheet.
- The case of a product-type transition (Lemma PT / Cor. J′) would also have to output this stronger form.

## 4. Re-check of the chain at the points where MS11♭ enters

I checked the logic of steps 2(b)–(d) as stated in the brief. I did not re-audit the cited entries 84–87, 97–99, 112 (Prop. K_w and the R(D) repair, Lemma S̃′, Theorem X*_all).
- **(P) at genuine transitions.** If β̃′_m ≠ β̃_m, then J_m is in neither stratum(D^m) nor stratum(D^{m+1}). This is the contrapositive of entry 99, as used in 2(b). So J_m is a puncture of both pieces. Correct as stated.
- **(P) at the endpoint.**
  - For MERGE/pMOV, Q_0 ∉ stratum(E).
  - If Q_0 ∈ stratum(D^k), entry 99 gives b̃ = β̃. Then x is intact and constant along β̃ = b̃ and also MERGE/MOV along it, which is absurd.
  - An iMOV endpoint (Q_0 ∈ stratum(E)) likewise gives b̃ = β̃ by entry 99, and the same contradiction.
  - So in every surviving case Q_0 is a puncture of both pieces, as MS11♭ requires.
- **Use of the conclusion at the endpoint.** An anchored sheet contains b̃ × {0} by definition. So x Y-persistent on it gives x intact with F_x ≡ Y_0 along b̃, contradicting MERGE/MOV. Correct; no use of the false B1(a),(b).
- **Inductive use.** MS11♭'s output (an anchored sheet of the outgoing lift β̃′_m) is exactly the input format of the transfer step 2(c). This matches.
- **Logical status.** MS11♭ contains "Y non-constant". So, as the brief says, proving it amounts to proving the problem under (Rig). Proposition B is consistent with this: it uses Y non-constant only through round11_q1 Lemma 2.3.

No flaw found in the parts checked.

## 5. Summary

**Proved here** (modulo the cited run lemmas named in each proof — round11_q1 Lemmas 2.1(c), 2.2, 2.3, 3.1 — and standard local analytic geometry cited from memory):
1. **Lemma A**: for every point z of 𝒳 = q(X) at which 𝒳 is unibranch, the points of X over z form one G_X-orbit. In particular this holds at (Q_t, t) for all small t: 𝒳 = H(𝒮 × Δ) is unibranch there by a topological argument from (R2).
2. **Corollaries A1–A3**:
   - the lift-curves in X are exactly G_X·L_0;
   - (1L_X) ⇔ G_X ⊆ Stab_G(L_0) ⇔ the local monodromy of lift points is transitive on G_X/A, which forces G_X/A to be cyclic;
   - the planner's second failure mode reduces to the first.
3. **Lemma A4**: X_0 = G_X·S, and G_S ⊆ K_S·G_X.
4. **§2**: the planner's step-4 claim ("g ∈ G_X fixing S × {0} pointwise fixes L_0") is false in a consistent local model with V_0 inside a symmetric locus.
5. **Proposition B (partial)**: MS11♭ holds under (h1) together with (h2′), in particular when G_X ⊆ K_S·Stab(L_0). So automorphisms of Q that fix the t = 0 sheet pointwise, such as global symmetries like deck groups of covering constructions, never cause a failure, even when V_t loses them.

**Not proved:** MS11♭ itself, and hence the problem under (Rig). No counterexample is given.

**Open (precise):**
- **(R1)**: the x-persistent sheets of β̃ lie only in 3-fold components over chart sheets S_T ≠ S through β̃. This would be removed by the strengthened induction invariant of the Remark in §3, if the transfer step can be shown to preserve it.
- **(R2)**: an element h ∈ G_X ∖ K_S·Stab(L_0) that acts non-trivially on X_0 (as an automorphism of S, or by moving S to hS ≠ S) carries L_0 into a b̃-sheet. The known (β-fail) local model (round11_q1 §5, the reflection u ↦ −u) is of this type. Total geodesy (e.g. Lemma TG on Fix(h) ∩ S) is the natural tool, but I could not make it bite.
  - Heuristic I could not complete: in the reflection case the loop around the boundary curve in coarse V_0 has impure monodromy (it swaps the twin regions). Loops realised by cylinder shears or level rotation are pure. So such loops must wind an even number of times, which is an arithmetic (parity) condition on prong/plumbing orders rather than a contradiction.
- **(Rig)** (entry 82): untouched.



### round12_q1 (verbatim)
# round12_q1 — attempt on MS11♭

## 0. Status (read this first)

- **MS11♭ is NOT proved and NOT refuted here.** This file is PARTIAL. It contains no proof of the problem's claim and no counterexample.
- What the file does contain:
  1. **Lemma F** (proved): stabiliser transfer for anchored sheets. MS11♭ for (β̃, b̃, x) depends only on the Stab(b̃)-orbit of x. This gives a sufficient criterion (Cor. F2) that covers every case in which the "twin" automorphism fixes b̃.
  2. **Model M1** (proved, chart level): an explicit local model showing that the planner's proposed "2-dimensional analogue" in suggestion step 4 is false *as a local statement*. The claim was that g ∈ G_X fixing S × {0} pointwise fixes the lift-curve L_0. In M1 it does not. MS11♭ still holds in M1, by Lemma F. So step 4 of the suggestion has to be reformulated, and Lemma F shows that the reformulated version is automatic in the pointwise-fixed case.
  3. **Chain check** (§4): no flaw found in the steps I re-checked (2(b) at the endpoint, 2(d), step 1). I record two dependencies the chain must keep explicit.
  4. **A dead end** (§5): a "copy-free" variant of Proposition K that would avoid labels altogether. I say exactly where it fails.
- Readings throughout: (R1), (R2) with H_0 = id, the definitions of the brief (piece, chart Def(Q), labels, transport family Ñ_c̃, anchored sheet, Y-persistent, lift-curve, P(T), C(L)), and (Rig) and "Y non-constant" as hypotheses of MS11♭.

Plan as executed: (a) read the brief; (b) look for a global argument (total geodesy, or Y non-constant) that controls which lift-curve an anchored sheet of b̃ contains; (c) failing that, isolate what is provable and check the chain.

---

## 1. Inputs used (from the brief; not re-proved here unless said)

- (K1) The preimages in Def(Q) of a point near Q form one Aut(Q)-orbit. (K3) F_x(a p) ≅ F_{a^{-1}x}(p), and s_e(p) = 0 ⟺ s_{ae}(ap) = 0. Here a ∈ Aut(Q) acts on Def(Q), on labels (vertices of G_Q) and on edges. These are standard and are restated in R7-3 §1.
- Transport family Ñ_c̃: the connected component, containing c̃ ∖ {0}, of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε). B is Aut(Q)-invariant.
- **(PC)** "P(T) = C(L)": for a boundary-type anchored sheet T and any lift-curve L ⊂ T, the set of labels Y-persistent on T equals the set of labels y with F_y ≅ Y_t along L. The brief attributes this to round11_q4 Lemma 2.2 and round11_q1 Lemma 2.3, under (Rig) and Y non-constant. **I have not re-checked (PC).** The brief's extract does not contain its proof. Only Cor. F2 below uses it; Lemma F does not.
- Every anchored sheet of b̃ contains at least one lift-curve. (This is round9_q2 Lemma 1, and B1♭ as used in the brief; again not re-checked by me.)

---

## 2. Lemma F (stabiliser transfer) — proved

**Lemma F.** Let c̃ be a lifted branch through 0 ∈ Def(Q). Let a ∈ Aut(Q) satisfy a c̃ = c̃ (setwise). Then:
1. a Ñ_c̃ = Ñ_c̃, so a permutes the irreducible components of closure(Ñ_c̃);
2. a maps anchored sheets of c̃ to anchored sheets of c̃;
3. for every anchored sheet T of c̃, P(aT) = a·P(T);
4. for every lift-curve L, C(aL) = a·C(L), and aL is again a lift-curve.

*Proof.*
1. The set q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε) is Aut(Q)-invariant, because q∘a = q and B is invariant. So a maps its connected components onto its connected components. a Ñ_c̃ is the component that contains a(c̃ ∖ {0}) = c̃ ∖ {0}, so it is Ñ_c̃. Since a is a biholomorphism of B × Δ_ε (acting trivially on t), it maps closure(Ñ_c̃) onto itself and permutes its irreducible components.
2. If T ⊃ c̃ × {0}, then aT ⊃ a c̃ × {0} = c̃ × {0}.
3. Let (p,t) ∈ T and y a label. By (K3):
   - y is intact at ap ⟺ every edge e at y has s_e(ap) = 0 ⟺ every edge a^{-1}e at a^{-1}y has s_{a^{-1}e}(p) = 0 ⟺ a^{-1}y is intact at p;
   - F_y(ap) ≅ F_{a^{-1}y}(p).

   Hence y is Y-persistent on aT ⟺ a^{-1}y is Y-persistent on T.
4. The set {(p,t) : q(p) = Q_t} is Aut(Q)-invariant, so a permutes its irreducible components. The identity for C is (K3) again. ∎

**Corollary F1.** Fix β̃, b̃, x as in MS11♭. The statement "x is Y-persistent on some anchored sheet of b̃" depends only on the orbit Stab(b̃)·x. Likewise, the hypothesis "x is Y-persistent on some anchored sheet of β̃" depends only on Stab(β̃)·x.

*Proof.* By Lemma F(2),(3), the union ⋃_T P(T) over the anchored sheets T of b̃ is Stab(b̃)-invariant. ∎

**Corollary F2 (a sufficient criterion for MS11♭; uses (PC)).** Let Λ_β^x be the set of lift-curves L contained in some anchored sheet T_β of β̃ with x ∈ P(T_β). Let Λ_b be the set of lift-curves contained in anchored sheets of b̃. If
  Λ_b ∩ Stab(b̃)·Λ_β^x ≠ ∅,
then the conclusion of MS11♭ holds for (β̃, b̃, x).

*Proof.*
- Let L = aL′ ∈ Λ_b with a ∈ Stab(b̃) and L′ ∈ Λ_β^x. By Lemma F(2), a^{-1} maps the anchored sheet T ⊃ L of b̃ to an anchored sheet a^{-1}T ⊃ L′ of b̃.
- Anchored sheets of b̃ are of boundary type: their pattern is the pattern of b̃, and that pattern is not all of E(G_Q), by (P).
- By (PC), P(a^{-1}T) = C(L′) = P(T_β) ∋ x. ∎

**What this says about failures.** A counterexample to MS11♭ needs every lift-curve met by an anchored sheet of b̃ to lie outside Stab(b̃)·Λ_β^x. In particular:
- If the automorphisms responsible for the twin (the g with g^{-1}x ∉ C(L_0)) all fix b̃ setwise, then no failure occurs. This holds, for example, when they lie in the pointwise stabiliser Stab_pt(S) of the common sheet S ⊃ β̃, b̃.
- So the case "g ∈ G_X fixes S × {0} pointwise" in the planner's step 4 is harmless, *whatever* g does to L_0. A failure needs a twin automorphism that moves b̃ (or β̃), i.e. one acting non-trivially on S or not preserving S.

This is consistent with the brief's description of Mechanism D, where labels change only by (β)-twists σ ∈ Stab_pt(c̃) and at (γ°)-edges. Lemma F is the elementary reason why a twist by an element of Stab(b̃) can always be undone.

---

## 3. Model M1: "g fixes S × {0} pointwise" does not imply "g fixes L_0" — proved (chart level)

The planner's step 4 asks for a 2-dimensional analogue of Lemma D3: *if g ∈ G_X fixes S × {0} pointwise, then g fixes the lift-curve L_0 setwise.* As a statement about local configurations this is false.

**The model.**
- Coordinates (u, v, w) on X ≅ C³, with t|_X = w².
- Def(Q) has coordinates (z_1, z_2, s_1, s_2, …). Embed X by ι(u,v,w) = (z_1 = u, z_2 = w, s_1 = v, s_2 = u² − w², other coordinates 0), together with t = w². This is injective and an immersion.
- G_Q has two edges e_1, e_2 with smoothing parameters s_1, s_2. Aut(Q) ⊇ ⟨g, h⟩ ≅ (Z/2)², acting by g: z_2 ↦ −z_2 and h: z_1 ↦ −z_1, fixing s_1 and s_2. On X: g(u,v,w) = (u,v,−w) and h(u,v,w) = (−u,v,w). Both preserve X, t, s_1 and s_2.
- S := X_0^{red} = {w = 0}, with coordinates (u, v). **g fixes S pointwise**; h acts on S by u ↦ −u.

**t = 0.** On S: s_1 = v and s_2 = u². The boundary curves of S are:
- β̃ = {v = 0} (the u-axis), with pattern {e_1};
- b̃ = {u = 0} (the v-axis), with pattern {e_2}.

Both pass through 0 and lie in S, so (S) holds. Q is a puncture of the piece of each, so (P) holds. They are distinct lifts (indeed lifts of different coarse branches).

**Coarse picture.** Take G_X = ⟨g, h⟩ and X the only component. Then q(X) = X/⟨g,h⟩ ≅ C³ with coordinates (U = u², v, t = w²): a smooth trivial family of planes over Δ.
- At time t the boundary is {v = 0} ∪ {U = t}.
- Q_t = (U, v) = (t, 0).
- The translation U ↦ U + t gives a homeomorphism H with H_0 = id that preserves the two strata {v = 0}, {U = t} and the point Q_t, as (R2) requires. It is holomorphic in t.

**Lift-curves.** {(p,t) ∈ X : q(p) = Q_t} = {v = 0, u² = w²} = L_0 ∪ L_1, with L_0 = {u = w, v = 0} and L_1 = {u = −w, v = 0}.
- gL_0 = L_1 = hL_0 ≠ L_0, although g fixes S × {0} pointwise. This refutes the proposed 2-dimensional analogue.

**Anchored sheets.**
- Of β̃: the preimage of the transported branch {v = 0} is T_β = {v = 0} ⊂ X, which is irreducible and contains both L_0 and L_1.
- Of b̃: the preimage of {U = t, v ≠ 0} is {u² = w², v ≠ 0}. It is connected (its two components meet along b̃ × {0}), so it is Ñ_b̃. Its closure has two irreducible components, T⁺ = {u = w} ⊃ L_0 and T⁻ = {u = −w} ⊃ L_1. Both contain b̃ × {0}, so both are anchored, and gT⁺ = T⁻ (Lemma F, g ∈ Stab(b̃)).

**MS11♭ in M1.** If x is persistent on T_β, then by (PC) x ∈ C(L_0) = P(T⁺). So MS11♭ holds in M1. This is consistent with §2: the automorphism g that moves L_0 fixes b̃.

**Moral.** In the pointwise-fixed case, (1L_X) can fail (here X contains two lift-curves), but this does no harm. The planner's sufficient condition (1L_X) is therefore stronger than needed. The right target is the condition of Cor. F2.

M1 is a chart-level model only. I do not claim that it is realised by a smooth, closed, totally geodesic V_0 and an admissible family. It is used only to show that a proposed local implication is false.

---

## 4. Check of the chain (problem ⇐ MS11♭ + (Rig))

I re-checked the following steps against the statements quoted in the brief.
- **Step 2(d), non-product endpoint.**
  - MS11♭ gives an anchored sheet T ⊃ b̃ × {0} with x Y-persistent on T. Restricting to t = 0: at every p ∈ b̃, x is intact and F_x(p) ≅ Y_0.
  - MERGE (some edge at x unpinched along b̃) contradicts intactness.
  - Puncture-MOV (x intact, F_x non-constant along b̃) contradicts F_x ≡ Y_0.
  - This step is correct.
- **(P) at the endpoint.** An iMOV endpoint (Q_0 in the stratum of b) is not covered by MS11♭, because (P) fails for b̃. It is removed by step 2(b): Theorem X*_all forces every boundary curve of the common sheet through Q_0 to lie over the branch of the piece containing Q_0, and Remark 3 there excludes two distinct lifts of one branch in one sheet. So b̃ = β̃, which contradicts "x constant along β̃, moving along b̃".
  - The same argument covers the case in which Q_0 is an interior point of the *entering* piece: then b̃ = β̃ again, and the endpoint is not a MERGE or MOV.
  - This relies on Theorem X*_all for non-product strata (entry 97, round10_q1), which I did not re-read; the brief records it as proved.
- **Step 1.** "Goal ⇐ MS8 + (Rig) + entry 19" is correct as a logical implication. It needs (Rig) **for the given family**, i.e. entry 82. That entry is OPEN, and it is not a consequence of MS11♭. So **even a proof of MS11♭ would not settle the problem**: (Rig) remains.
  - Remark from memory, not used: (Rig) is a rigidity statement for the moving parts of 1-dimensional boundary pieces. For a piece whose moving part is a Teichmüller curve in its max-speed factor, McMullen's rigidity theorem for Teichmüller curves (C. McMullen, "Rigidity of Teichmüller curves", 2009; quoted from memory) suggests that the max-speed projection cannot deform. The slower moving factors and the joint curve K ⊂ ∏_{u∈M} M̄_u are not covered by it. I did not pursue this.
- **Logical status.** MS11♭ assumes "Y non-constant", so *any* proof that Y is constant (under (R1), (R2), (Rig)) proves MS11♭ vacuously. Conversely, a counterexample to MS11♭ is a counterexample to the problem. MS11♭ is therefore exactly as hard as the problem under (Rig). Its value is only as a localisation of where a proof must act.

**Verdict:** no flaw found in the parts re-checked. The derivation does depend on entries 82 (open), 97–99 and (PC), which I did not re-check.

---

## 5. Dead end: a copy-free Proposition K

**Idea.** Replace the marked subsurface Σ_i in Prop K by the copy-free defect
  E(X) := min over subsurfaces Σ of the topological type of Σ_i of max(Ext_X(∂Σ)/δ, d(ψ_Σ(X), Y_0)/η).
Stop the ray at the first time T_n with E = 1. Twins would then never matter: switching from one Y_0-copy to another costs nothing.

**What works.**
- For a cylinder direction (Lemma NH(1)), the whole ray γ_n([0,∞)) stays within ρ_n → 0 of B_0, hence of B_0^∂:
  - for s ≤ S, by convergence to ∂V_0 (Lemma G′);
  - for s ≥ S, because Ext(c) ≤ e^{−2S}/m.
- In the sealed case (II-a) of round9_q1, every point of B_0^∂ has a Y_0-copy. By compactness E < 1 along the whole ray.
- A **single** subsurface Σ cannot remain a (δ,η)-copy for all s ≥ s_0. Sketch, not fully written out: its core part has fixed positive flat area, and the Teichmüller deformation of a positive-area flat subsurface has unbounded displacement. This is incompatible with ψ_Σ staying η-close to the fixed point Y_0, unless the area escapes into the boundary collars. Escaping area forces non-peripheral horizontal cylinders inside Σ, which pinch curves of Σ. This is the copy-free version of Lemma NH(2).

**Where it fails.**
- (a) For a cylinder direction, the copies may *switch* infinitely often (Σ_1, Σ_2, … with s → ∞), and E never reaches 1. This is exactly the "no well-founded quantity" problem of round9_q7 (R-tw), now at t = 0. Nothing in the argument bounds the number of switches.
- (b) For a recurrent direction (Kerckhoff–Masur–Smillie, quoted from memory: for a.e. direction the ray returns to a compact part of M_g), E does reach 1. But at that time the ray need not be close to B_0: with δ fixed and n → ∞ the stopping points converge to points of V_0, not of B_0. Taking δ → 0 afterwards produces a point of B_0 but no MERGE branch. The MERGE/MOV conclusion of Prop K needs the stopping point to lie *on* B_0, which only the cylinder direction provides.

So the copy-free stopping rule and Prop K's localisation on B_0 pull in opposite directions. Combining them would need a direction that is both cylinder-like (to stay near B_0) and releasing for every Y_0-copy. I could not find one.

---

## 6. Summary

**Proved here:**
- Lemma F and Cor. F1: anchored sheets and persistence sets are equivariant under Stab(c̃). MS11♭ depends only on the Stab(b̃)-orbit of x.
- Cor. F2 (uses (PC), which is cited and not re-checked): MS11♭ holds whenever Λ_b ∩ Stab(b̃)·Λ_β^x ≠ ∅. In particular it holds when every twin automorphism fixes b̃, e.g. when it lies in Stab_pt(S).
- Model M1: the implication "g ∈ G_X fixes S × {0} pointwise ⇒ gL_0 = L_0" (planner's step 4) is false in a chart-level model consistent with (R1), (R2). (1L_X) fails there, yet MS11♭ holds.

**Not proved:**
- MS11♭ itself, in any generality. Cor. F2 is a sufficient condition, i.e. a partial result in the sense of the task.
- No counterexample to MS11♭, or to the problem, was constructed.

**Open (precise):**
1. **(Twin-moves-b̃)** Exclude: a lift-curve met by the anchored sheets of b̃ lies outside Stab(b̃)·Λ_β^x. By Lemma F, any such failure needs an automorphism of Q that moves x to a non-persistent label and moves b̃ (or does not preserve the 3-fold component X).
2. **(Rig)** (entry 82). It is needed for the goal independently of MS11♭.
3. The cited prior inputs (PC), B1♭ and Theorem X*_all, which I did not re-check.
4. The copy-free variant of Prop K (§5): bound the number of copy switches along a cylinder-direction ray, or find a direction that both stays near B_0 and releases every Y_0-copy.


### round12_q3 (verbatim)
# round12_q3 — attempt on MS11♭

Plan/status: (1) read the spliced material on the chain (round11_q9 §§2,5) and the
planner's Mechanism G; (2) try to prove MS11♭ via (1L_X) / lift-curve stabilisers;
(3) if not possible, check the chain and record precisely what is and is not proved.
Statement being attempted: MS11♭ exactly as in the task file.

**Outcome: MS11♭ is NOT proved here and no counterexample is given.** What follows is a
partial result on the planner's Mechanism G, item 4: the claimed "2-dimensional analogue of
Lemma D3". It holds exactly when the t = 0 fibre of X is generically reduced along S. When
that fails it is false, already in a local model, and I identify the global meaning of the
failure. I did not re-check the chain beyond what is used here.

## 1. Setting
- X is an irreducible component of the germ of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) at (0,0) with
  X ⊃ S × {0}.
- g ∈ Aut(Q) acts on B × Δ_ε by g × id, and gX = X.
- X_0 := X ∩ {t = 0}, with its scheme structure, i.e. with ideal I_X + (t).
- dim X = 3. Indeed every fibre of closure 𝒱 over Δ has dimension 2, so no 3-dimensional
  component lies in {t = 0}. Hence t ≢ 0 on X, and S is an irreducible component of X_0.

## 2. Lemma G1 (proved)
Assume g fixes S × {0} pointwise. Then at least one of the following holds:
- (a) g acts as the identity on X. Then g fixes every lift-curve in X (in fact every point of X).
- (b) The scheme X_0 is non-reduced at every point of a dense open subset of S. Moreover
  Fix(g) ∩ X is a proper analytic subset of X; it contains S × {0} and has dimension 2. So
  for small t ≠ 0, the generic point of X_t is not fixed by g.

*Proof.* Suppose X_0 is reduced at some point p of S that is a smooth point of S and lies on
no other component of X_0. Such points form a dense open subset of S as soon as one of them
exists. Then O_{X,p}/(t) = O_{S,p} is regular of dimension 2, and t lies in the maximal ideal.
So the embedding dimension of O_{X,p} is at most 3 = dim O_{X,p}, and X is smooth at p with
local coordinates (s_1, s_2, t), where s_1, s_2 restrict to coordinates on S.

Now g fixes p and preserves X, so g is a finite-order automorphism of the smooth germ (X,p).
- By Cartan's linearisation (cited from memory), g is conjugate to its linear part dg_p.
- dg_p is the identity on T_pS, because g fixes S pointwise.
- dt_p ∘ dg_p = dt_p, because t ∘ g = t. Since T_pS = ker dt_p, dg_p induces the identity on
  T_pX / T_pS.
- So dg_p is unipotent and of finite order, hence the identity, and g = id near p.

The set {x ∈ X : gx = x} is analytic and contains a nonempty open subset of X_reg. The regular
locus of an irreducible germ (on a suitable representative) is connected, so this set is all
of X. That is (a).

So if g ≠ id on X, no such p exists, i.e. X_0 is non-reduced at generic points of S. In that
case Fix(g) ∩ X is a proper analytic subset of the irreducible 3-fold X,
so it has dimension ≤ 2, and it contains S × {0}. ∎

(The two cases can overlap only formally: (a) can hold with X_0 non-reduced. The content is
that "g ≠ id on X" forces non-reducedness along S.)

## 3. Global meaning of case (b)
If g fixes S pointwise, then g lies in the automorphism group of the curve at a generic point
of S, i.e. g is a generic automorphism of the curves of V_0 near Q. Case (b) says that V_t
(t ≠ 0) leaves the locus of curves admitting g. Concretely:
- If 𝒱 is read as an orbifold submanifold whose chart preimages are smooth with φ submersive,
  case (b) is impossible at generic interior points, since there X is smooth with t a
  coordinate. So under that (orbifold) reading, every g ∈ G_X fixing S pointwise fixes every
  lift-curve in X.
- Under the coarse reading (R2) adopted by the run, case (b) can occur. Example: coarse M_3
  is smooth along the hyperelliptic divisor, where the hyperelliptic involution ι acts on the
  1-dimensional normal direction by z ↦ −z, with coarse coordinate y = z². A family 𝒱 that is
  smooth in the coarse space, with V_0 inside the hyperelliptic locus and V_t = {y = t}, has
  chart preimage {z² = t}, which is non-reduced at t = 0. I have not checked whether a totally
  geodesic V_0 can actually sit in such a locus.

## 4. Local model: case (b) can exchange lift-curves
Work in chart coordinates (u, w, z, …), with g: z ↦ −z (other coordinates fixed), and let
X = {z² = t·u} (× fixed other coordinates).
- X is irreducible. Its fibre X_0 = {z² = 0} is the double plane S = {z = 0}, and g fixes S
  pointwise.
- X/g = {Z = t u}, with Z = z², is a smooth graph, so the coarse family is smoothly trivial
  near here.
- L_0 = {u = t, w = 0, z = t} and gL_0 = {u = t, w = 0, z = −t} both lie in X, are distinct,
  and have the same image Q_t in the quotient. So both are lift-curves.

Hence the planner's local evidence for item 4 is incomplete. The "t = b²" model has a single
lift-curve, but this variant of it has two lift-curves exchanged by an element fixing S
pointwise. So (1L_X) cannot be derived from item 4 by local arguments alone, consistent with
the run's general finding that MS11♭ needs global input. The global input that would close
this sub-case is "V_t keeps the generic automorphisms of V_0", which is not available under (R2).

## 5. Status
- **Proved:** Lemma G1, i.e. elements g ∈ G_X fixing S pointwise act trivially on X (hence on
  all lift-curves) unless X_0 is non-reduced along S. That non-reduced case happens only if
  V_t loses a generic automorphism of the curves of V_0. Under the orbifold reading of
  "submanifold 𝒱" it never happens.
- **Shown (local model):** under (R2) the non-reduced case can exchange two lift-curves, so
  item 4 of the planner's sketch is false as a local statement.
- **Not addressed:** the elements g ∈ G_X acting on S as non-trivial (anti-)reflections; second
  components gX ≠ X meeting X along a lift-curve; whether the exchanged lift-curves actually
  carry different persistence sets (and so violate MS11♭); the chain check.
- **Open:** MS11♭ itself; (Rig).




## Reminder
- Never assume V_t is totally geodesic for t ≠ 0. Never assume H_t preserves automorphism groups: the orbifold reading (R2^orb) is NOT adopted.
- Use anchored sheets. Do not use Lemma B1(a),(b) of round10_q3, which are false; use B1♭ of round11_q9 §2.3.
- A proof for a sub-class, or under an extra hypothesis, does not answer the question; report it as partial.
- Begin with a plan/status line. End with: proved / not proved / open.
