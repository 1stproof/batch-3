kind: attempt
Open question attempted: (NRT_P), "no rigid twin at puncture points" — the run's missing statement (OPEN, ledger entry 141, locator round14_plan). By the derivation spliced below (round13_q5), (NRT_P) together with the run's earlier results gives MS8, and MS8 together with (Rig) gives the problem's claim.

## Task
Give a complete proof of (NRT_P) exactly as stated below, or an explicit counterexample to it (an admissible family V_t and data Q, a, L, x realising the configuration), with every step written out.

- A proof of the statement for only some of the cases it covers — a sub-class of its objects (some Q, some V_0, some families, the reflection case only, a smooth 3-fold component only, case (A) or case (B) only, …) or a sub-range of its parameters — does NOT answer the question, though it should be reported if it is all that was found.
- Purely chart-local arguments, and arguments that use only t = 0 data, are known to be insufficient (round13_q4 §1, round13_q6 §3, round13_q3 §1 give chart-level models; round13_q7 Lemma 2.4 (NG) shows t = 0 data cannot suffice). Global input is needed: total geodesy and smoothness of V_0, the global family (R1)/(R2), (Rig) (Lemma U: pieces are K_W × {c_t}), the generic-time trichotomy / Theorem N for every φ ∈ Φ, Y non-constant.
- Do not assume the orbifold reading (R2^orb) (H lifting equivariantly with isotropy preserved): under it the statement is known to hold (a failure needs |Aut(Q_t)| < |Aut(Q)|), and it is NOT the reading adopted here.
- If you find the derivation "(NRT_P) ⇒ MS8 ⇒ claim" (below) flawed, say exactly where.
- Begin with a plan/status line. End with: proved / not proved / open.

## The missing statement (verbatim from the run's summary)
**Missing statement (NRT_P)** (OPEN, entry 141, locator round14_plan; replaces MS11♭ = entry 124 and the round-13 wording (NRT) = entry 137).
- *Setting.* g ≥ 2. V_0 ⊂ M_g smooth, closed, 2-dimensional, totally geodesic for the Teichmüller metric. V_t (t ∈ Δ) a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2) with H_0 = id (coarse: H_t need not preserve automorphism groups; V_t not assumed totally geodesic for t ≠ 0). Δ_Γ ≅ ∏_j M_{g_j,n_j} of product type, dim ∂V_t = 1, π_i(∂V_t) = {Y_t} for all t, dim M_{g_i,n_i} > 0. (Rig): a finite set 𝒦 of triples (G, M, K) (M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not in the boundary) such that every piece at every time has its triple in 𝒦 up to Aut(G). t ↦ Y_t non-constant. Φ as defined above.
- *Claim.* There do not exist: a puncture point Q ∈ B_0; an automorphism a ∈ Aut(Q); a lift-curve L of Q_t; a label x of G_Q; such that for all small t ≠ 0, along L the component x is intact with class on a branch φ ∈ Φ, and the component a^{-1}x is intact with F_{a^{-1}x} ≅ Y_0.
- Equivalent form (entry 138, Lemma 2): at every puncture point Q, C_Φ(L) is Aut(Q)-invariant for one (equivalently every) lift-curve L.
- Under (Rig) it contains "Y non-constant", so it is vacuously true if the claim is; a counterexample to it is a counterexample to the problem (as for MS11♭, entry 122). A failure needs isotropy drop: a ∉ Stab(L), so Q_t has ≥ 2 lift points and |Aut(Q_t)| < |Aut(Q)|.

## Readings of the problem's hypotheses (adopted throughout)
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


**Further definitions used in the statement.**
**Definitions** (as in the round-13 task files). Piece at time t = 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G); chart Def(Q) with plumbing coordinates s_e, q: Def(Q) → Def(Q)/Aut(Q); labels = vertices of G_Q; transport family Ñ_c̃; anchored sheet T of c̃ = irreducible component of closure(Ñ_c̃) containing c̃ × {0}; boundary-type = Q not in the stratum of c; lift-curve = irreducible component through (0,0) of {(p,t): q(p) = Q_t}, Q_t := H_t(Q); puncture point = Q ∈ B_0 having a branch c of B_0 at Q with c ∖ Q in a stratum other than that of Q; Φ = finite set of local branches at t = 0 of the constant-vertex value curves Γ_{W,u} (W a component of a lifted piece family, u a constant vertex of W of type (g_i,n_i)) through (Y_0, 0) that are non-constant (Y ∈ Φ when Y is non-constant); C_Φ(L) = labels whose class along L lies on a branch in Φ.

## How (NRT_P) is used: the chain
**The chain (statements; ledger numbers: 19 holomorphy of t ↦ Y_t; 82 (Rig), open; 85, 98, 99, 112 walk chain, Lemma S̃′, Cor. IMOV_all, B1♭; 138 = round13_q5 below; 146 = Prop. V).**
**Chain** (statements only).
1. Goal ⇐ MS8 + (Rig) (entry 82) + entry 19. (MS8: under (R1),(R2),(Rig), Y is constant; entry 19 turns this into Y_t = Y_0.)
2. MS8 ⇐ (NRT_P) (entry 138, round13_q5 §4): assume Y non-constant.
   (a) walk chain (entries 85, 98, 112) with transitions J_m, lifts β̃_m, β̃′_m, labels x_m, endpoint (Q_0, β̃, b̃, x), x MERGE or MOV along b̃ at t = 0; (P) at every genuine transition and at the endpoint (entry 99); interior transitions trivial.
   (b) Induction (C_m): x_m ∈ P_Φ(T) for an anchored sheet T of β̃_m. Base: vertex i on ∂V_0's lifts, φ_1 = Y. Puncture transitions (any type): (NRT_P) at J_m ⇒ (Lemma 2) C_Φ(L) independent of L ⇒ (Lemma 3, Prop. 4) x_m ∈ P_Φ(T′) for every anchored sheet T′ of β̃′_m. Transfer along D^{m+1}: Lemma 5.
   (c) Endpoint: (NRT_P) at Q_0 + Prop. 4 ⇒ x intact along b̃ with F_x ≡ Y_0 ⇒ contradiction with MERGE/MOV.
3. What remains after (NRT_P): (Rig) (entry 82), open under (R2); by Prop. V (entry 146) it follows for a product-type piece family from conditions (i)–(iii) at uncountably many t; non-product strata untreated. Under (R2^orb) both (NRT_P) and (Rig) hold (S62).

**The previous form of the chain** (with MS11♭ in place of (NRT_P)), quoted because round13_q5 refers to its skeleton as input (I6):
## How MS11♭ is used: the chain (verbatim from the run's summary). Ledger entry numbers: 19 = holomorphy of t ↦ Y_t (PR-A, from (R1),(R2) via Remmert/removable singularities); 24 = incidence transport P_t = H_t(P_0); 82 = (Rig), OPEN, a hypothesis of MS11♭; 84 = Theorem X*/X′ (round9_q4 §1, round9_q3); 85, 98 = Proposition K_w, walk chain, with repairs and Lemma S̃′ (round9_q4 §2, round10_q10); 86 = Lemma PT (round9_q3); 87 = Lemmas T, S, J, Theorem R (round9_q7); 97 = Theorem X*_all, 99 = Cor. IMOV_all (round10_q1); 112 = Lemma B1♭ and the Gap A repair, 113 = the chain check (round11_q9). (In this file only some of these are spliced; see the prior-results section.)
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


**The derivation (NRT_P) ⇒ MS8: round13_q5 (verbatim).** (Its (NRT) "at Q" is exactly (NRT_P) at the puncture point Q; only puncture points are used.)
# round13_q5 — answer: (NRT) ⇒ MS8 (the Φ-chain)

**Status line.** PROVED (modulo the run's cited inputs listed in §0, which I use as stated and did not re-derive): under (R1), (R2), (Rig), a smooth closed totally geodesic V_0, Δ_Γ of product type with ∂V_t ≡ Y_t on factor i, and **(NRT)**, the assumption "t ↦ Y_t non-constant" leads to a contradiction. So (NRT) ⇒ MS8, and with (Rig) and entry 19 this gives the goal.

The route is shorter than the one the brief proposes:
- (NRT) is *equivalent* to the following statement at each point Q ∈ B_0 that has a boundary-type anchored sheet: the set C_Φ(L) of Φ-labels of a lift-curve L does not depend on L (Lemma 2).
- With that, MS11♭_Φ holds at **every** puncture point, product type or not, for any two lifted branches. It follows in a few lines from three facts: the lift-curves form one Aut(Q)-orbit, every sheet contains a lift-curve, and P_Φ = C_Φ (Prop. 3).
- The chain therefore does not need Mechanism D, the (β)-twists, (γ°), Lemma PT, Lemma J / Cor. J′, or Lemma 4.1. The residual cases (R-a), (R-b) of round12_q6 and (R1), (R2) of round12_q2 never arise. For completeness, §5 checks that each of them, and (γ°), is an instance of the (NRT) configuration.
- The only chain step that needs a new Φ-argument is the transfer along a piece (Lemma 5). There the tracked function may change from φ to another branch ψ ∈ Φ, and it can never become rigid.

No strengthening (NRT′) is needed.

---

## 0. Setting, notation, cited inputs

Readings and notation:
- Readings (R1), (R2) with H_0 = id; (Rig).
- Q ∈ B_0, chart Def(Q) with ball B, q, plumbing coordinates s_e, labels, F_y.
- Transport family Ñ_c̃, anchored sheet, lift-curve, Q_t := H_t(Q). All as in the task file.
- 𝔐 := M_{g_i,n_i}/S_{n_i}. [Z] denotes the class of an n_i-pointed curve Z in 𝔐.
- Y is assumed non-constant, for contradiction.

**Φ** (round12_q7 §1). Φ is the finite set of local branches φ at t = 0 of value curves Γ_{W,u} with:
- (g_u, n_u) = (g_i, n_i);
- φ(0) = Y_0;
- φ non-constant.

Here W ranges over the irreducible components of the lifted families 𝒲_G (all strata G; finitely many after shrinking Δ) and u over the constant vertices of W (u ∉ M_W). Γ_{W,u} := (pr_u, t)(W), mapped to 𝔐 × Δ, is an irreducible analytic curve, finite over Δ (R8-2 Lemma U). Y ∈ Φ: Y is holomorphic (entry 19), non-constant, and its graph is the value curve of vertex i of the lifted family of ∂V_t.

**P_Φ, C_Φ.**
- For an anchored sheet T: P_Φ(T) is the set of labels z that are Φ-persistent on T. That means there is φ ∈ Φ such that at every (p,t) ∈ T, z is intact and ([F_z(p)], t) lies on the branch φ.
- For a lift-curve L: C_Φ(L) is the set of labels z such that ([F_z(p)], t) lies on some branch φ ∈ Φ for all (p,t) ∈ L.

**Cited inputs, used as stated:**
- (I1) Lift-curves. Λ := {(p,t) : q(p) = Q_t}. Its components through (0,0) (the lift-curves) form **one Aut(Q)-orbit** (round11_q4 §2, notation; round12_q6 Lemma G1(a)). Λ ∩ {t = 0} = {(0,0)}. Every label is intact at every point of Λ, because Q_t ∈ Δ_{G_Q} (H preserves strata), so all s_e vanish there.
- (I2) Every anchored sheet (a 2-dimensional irreducible germ at (0,0)) contains a lift-curve (round11_q4 Lemma 2.1).
- (I3) Equivariance (K3): F_y(ap) ≅ F_{a^{-1}y}(p), and y is intact at ap iff a^{-1}y is intact at p, for a ∈ Aut(Q). Hence C_Φ(aL) = a·C_Φ(L), and aT is an anchored sheet of ac̃ if T is one of c̃ (round12_q1 Lemma F, whose proof does not use a c̃ = c̃ for these two statements).
- (I4) Lemma U / U3 of R8-2 under (Rig): let T be a boundary-type anchored sheet of a lifted branch c̃.
  - The map Π (partial normalisation) sends a dense open subset of T into one component W of the lifted family of the piece of c (round12_q7 Lemma 1.2, proof).
  - Every fibre component of W_t is K_W × {c_t}, with K_W a fixed irreducible compact curve and c_t[w] ∈ M_w holomorphic in t for w ∉ M_W.
  - F_W := K_W ∩ ∂(∏_{w∈M_W} M̄_w) is finite and independent of t.
- (I5) Lemma 1.1 of round12_q7 (R8-2 Theorem 1 for every φ ∈ Φ). Take t ∉ Z_Φ (a discrete set) and a φ(t)-copy y at a lift q of a point of B_t. Then along every lifted branch through q, y is STAY (intact, constant value φ(t), and (W, y) a φ-vertex) or IMOV. IMOV is impossible along a lifted branch of a piece having the point as a puncture.
- (I6) The chain's t = 0 skeleton, unchanged (entries 85, 98, 99; round11_q9 §§1, 2.3–2.5, 2.7, 2.8):
  - the walk chain with transitions J_m, lifts β̃_m, β̃′_m, labels x_m, and endpoint (Q_0, β̃, b̃, x) with x MERGE or MOV along b̃;
  - interior transitions are trivial (β̃′_m = β̃_m, same label);
  - (P) holds at every genuine transition and at the endpoint;
  - B1♭ (anchored sheets of any lifted branch exist, B1♭(a″)), and the transfer set-up of §2.7 (the sheet maps into a global component 𝒲̃ with 𝒲̃_0 ⊃ E, and the R(D)/marking identification x_m ↔ c ↔ x_{m+1}).

"Boundary-type" anchored sheet: an anchored sheet of a lifted branch c̃ whose piece has Q as a puncture.

---

## 1. Lemma 1 (values along a lift-curve: Φ or rigid) — proved

**Lemma 1.** Let Q ∈ B_0. Let L be a lift-curve contained in a boundary-type anchored sheet T, and let y be a label with F_y(0) ≅ Y_0. Then the germ of {([F_y(p)], t) : (p,t) ∈ L} is either a branch φ ∈ Φ or the constant germ {Y_0} × Δ. In the first case y ∈ C_Φ(L); in the second, y is a rigid Y_0-copy along L.

*Proof.*
1. *Labels along L.* By (I1), y is intact along L, and p ↦ F_y(p) is holomorphic on L. So λ_y : L → 𝔐 × Δ, (p,t) ↦ ([F_y(p)], t), is holomorphic. Since t|_L is finite, its image is an irreducible curve germ at ([F_y(0)], 0) = (Y_0, 0).
2. *Components of Q_t.* Let (p_*,t) ∈ L with t ≠ 0.
   - T is 2-dimensional and irreducible, and t ≢ 0 on T. So T_t has dimension ≥ 1 at p_*.
   - Λ_t is finite. So p_* is a limit of points p_n ∈ T_t lying over c_t ∖ Q_t, i.e. in the stratum of the piece of c.
   - By (I4), Π(p_n) = (κ_n, c_t) with κ_n ∈ K_W. Pass to a subsequence with κ_n → κ_∞ ∈ K_W, which is compact.
   - ξ̄ is continuous, so ξ̄(κ_∞, c_t) = Q_t. Q_t ∉ Δ_{G_c}, since Q is a puncture of the piece and H preserves strata. Hence κ_∞ lies in the boundary, i.e. κ_∞ ∈ F_W.
   - So every irreducible component of Q_t, with its special points, is of one of two kinds:
     - (a) a constant-vertex value c_t[w], w ∉ M_W, of class on Γ_{W,w}(t);
     - (b) a component of a coordinate of a point of F_W. Its class lies in the finite, t-independent set 𝔉_W.
3. *The dichotomy.* By step 2, the image of λ_y lies in the analytic curve 𝒢 := ⋃_{w∉M_W} Γ_{W,w} ∪ (𝔉_W × Δ) ⊂ 𝔐 × Δ.
   - An irreducible germ inside an analytic germ lies in one of its irreducible branches. That branch passes through (Y_0, 0).
   - So the branch is either a branch of some Γ_{W,w} at (Y_0, 0), or a constant germ {Y_0} × Δ (from 𝔉_W, or a constant branch of some Γ_{W,w}).
   - In the first case, if the branch is non-constant, it lies in Φ: w is a constant vertex of type (g_i, n_i), the type of F_y. Otherwise the branch is ≡ Y_0. ∎

## 2. Lemma 2 ((NRT) ⇔ C_Φ independent of the lift-curve) — proved

**Lemma 2.** Let Q ∈ B_0 have at least one boundary-type anchored sheet. Then (NRT) at Q is equivalent to: C_Φ(L) is Aut(Q)-invariant for one (equivalently, every) lift-curve L. In that case C_Φ(L′) = C_Φ(L) for all lift-curves L, L′ at Q.

*Proof.*
- Let T be a boundary-type anchored sheet. By (I2) it contains a lift-curve L_1.
- By (I1) every lift-curve is aL_1 for some a ∈ Aut(Q). It lies in aT, which is a boundary-type anchored sheet of ac̃ by (I3). So Lemma 1 applies to every lift-curve L at Q.

(⇒) Let x ∈ C_Φ(L) and a ∈ Aut(Q). If a^{-1}x = x, there is nothing to prove. Otherwise:
- F_{a^{-1}x}(0) ≅ F_x(a·0) = F_x(0) ≅ Y_0, by (I3), since a fixes the origin.
- By Lemma 1, a^{-1}x is either in C_Φ(L) or rigid (≡ Y_0) along L.
- The rigid case is exactly the configuration excluded by (NRT): Q ∈ B_0, a ∈ Aut(Q), a lift-curve L of Q_t, x ≠ a^{-1}x, x intact along L with value on a non-constant φ ∈ Φ, and a^{-1}x intact along L with value ≡ Y_0, for all small t.
- Hence a^{-1}x ∈ C_Φ(L). So C_Φ(L) is Aut(Q)-invariant.
- Then C_Φ(aL) = aC_Φ(L) = C_Φ(L) by (I3), and by (I1) this covers all lift-curves.

(⇐) Suppose an (NRT) configuration (a, L, x) exists. Then x ∈ C_Φ(L). But a^{-1}x ∉ C_Φ(L), since its value is the constant germ, which is not a branch in Φ. So C_Φ(L) is not invariant. ∎

## 3. Lemma 3 (P_Φ = C_Φ) and Proposition 4 (MS11♭_Φ everywhere) — proved

**Lemma 3 (Φ-version of round11_q4 Lemma 2.2).** Let T be a boundary-type anchored sheet at Q and L ⊂ T a lift-curve. Then P_Φ(T) = C_Φ(L). Moreover the function of y ∈ P_Φ(T) on T is its branch along L.

*Proof.*
- (⊂) Restrict to L ⊂ T.
- (⊃) Let y ∈ C_Φ(L) with branch φ. Let Γ ⊂ 𝔐 × Δ be the (closed analytic, after shrinking) union of the finitely many value curves. Put A_y := {(p,t) ∈ T : y intact at p and ([F_y(p)], t) ∈ Γ}. This is a closed analytic subset of T.
- For t ∉ Z_Φ (Z_Φ discrete), (p,t) ∈ L, y is a φ(t)-copy at the lift p of Q_t.
  - Every branch of T_t at p is a lifted branch of the transported piece c_t, and Q_t is a puncture of c_t.
  - By (I5), y is STAY along it: intact, with constant value φ(t).
  - So A_y contains the germ of T_t at (p,t), which is 1-dimensional (as in Lemma 1, step 2).
- This holds for uncountably many t. An analytic set of dimension ≤ 1 contains 1-dimensional t-slices for at most countably many t. Hence dim A_y = 2, and A_y = T by irreducibility.
- The map (p,t) ↦ ([F_y(p)], t) is holomorphic on the irreducible germ T and lands in Γ. So it lands in a single branch of Γ at (Y_0, 0) (the preimages of the branches are analytic and cover T).
- That branch contains the image of L, which is the branch φ. So it is φ, and y ∈ P_Φ(T) with function φ. ∎

**Proposition 4 (MS11♭_Φ, in a strong form).** Assume (NRT). Let Q ∈ B_0, let T and T′ be boundary-type anchored sheets at Q (of any lifted branches c̃, c̃′, equal or not, product type or not), and let x ∈ P_Φ(T). Then x ∈ P_Φ(T′). Moreover, if T′ is an anchored sheet of c̃′, then at t = 0 the label x is intact along c̃′ near 0 with F_x ≡ Y_0.

*Proof.*
- Choose lift-curves L ⊂ T and L′ ⊂ T′ (I2).
- By Lemma 3, x ∈ C_Φ(L). By Lemma 2, C_Φ(L′) = C_Φ(L) ∋ x. By Lemma 3 for T′, x ∈ P_Φ(T′).
- For the last claim, let ψ be the function of x on T′. Then c̃′ × {0} ⊂ T′ and x is intact on T′.
- ψ is a branch of a curve finite over Δ, so its germ meets {t = 0} only in (Y_0, 0). Hence [F_x] ≡ Y_0 on c̃′ near 0. ∎

In particular, MS11♭_Φ holds for every admissible datum. Note that (S) is not needed, and neither is β̃ ≠ b̃.

## 4. The Φ-chain — the derivation (NRT) + (R1), (R2), (Rig), Y non-constant ⇒ contradiction

**Induction claim (C_m).** x_m ∈ P_Φ(T) for some anchored sheet T of β̃_m, with some function φ_m ∈ Φ, which may vary with m.

1. **Base.** Δ_Γ is of product type. Vertex i is Y-persistent on every sheet of every lift of a branch of D^1 (round11_q9 §2.5). Since Y ∈ Φ, (C_1) holds with φ_1 = Y.
2. **Interior transitions and R(D)-points.** By (I6), β̃′_m = β̃_m and the label is unchanged. So the anchored sheets are the same, and the claim passes unchanged.
3. **Puncture transitions** (product or non-product, β̃′_m ≠ β̃_m or not). J_m is a puncture of D^m and of D^{m+1} (I6). So the anchored sheets of β̃_m and β̃′_m are of boundary type, and anchored sheets of β̃′_m exist (B1♭(a″)). Proposition 4 gives x_m ∈ P_Φ(T′) for every anchored sheet T′ of β̃′_m. (Lemma PT and Lemma J / Cor. J′ are not used. The question whether "pinned" contradicts a varying φ therefore does not arise.)
4. **Transfer along D^{m+1}** (Lemma 5 below): (C_m) on β̃′_m gives (C_{m+1}).
5. **Endpoint** (product or non-product). (P) holds at Q_0 (I6), so anchored sheets of b̃ are of boundary type. By (C_k) and Proposition 4, x is intact along b̃ near 0 with [F_x] ≡ Y_0.
   - The pattern is constant on b̃ ∖ 0, and F_x is holomorphic on L_x. So, by the identity theorem along the normalisation of b̃ (as in round11_q9 §2.8), x is intact along all of b̃ ∩ B with [F_x] ≡ [Y_0].
   - This contradicts MERGE (an edge at x is unpinched along b̃) and MOV ([F_x(z̃^∞)] ≠ [Y_0]).

Hence Y is constant, i.e. MS8 holds, and Y_t = Y_0 by entry 19. ∎

**Lemma 5 (Φ-transfer).** Let T be an anchored sheet of β̃′_m with x_m ∈ P_Φ(T), function φ. Then there is an anchored sheet T″ of β̃_{m+1} with x_{m+1} ∈ P_Φ(T″), with some function ψ ∈ Φ (possibly ψ ≠ φ).

*Proof.*
- Follow round11_q9 §2.7 verbatim:
  - Π_S of the relevant component of Ñ_{β̃′_m} lies in one global component 𝒲̃ of the lifted family of D^{m+1}, with 𝒲̃_0 ⊃ E.
  - x_m corresponds to a vertex c. c is constant on E with value Y_0 (x_m is intact with [F] ≡ Y_0 along β̃′_m, by the last clause of Prop. 4 applied to T itself). So c ∉ M_{𝒲̃} by U1.
  - At J_{m+1} there is a β̃_{m+1}-sheet T″ = closure(Ñ″^1) with Π(Ñ″^1) ⊂ 𝒲̃.
  - On T″ the label x_{m+1} ↔ c is intact (constant pattern; closedness), and ([F_{x_{m+1}}(p)], t) = ([c_t[c]], t) lies on Γ := Γ_{𝒲̃,c} (closedness again).
- The only change from the Y-version is the replacement of Lemma S(c) ("persistence holds on all of 𝒲̃"). It is replaced by the following observation.
  - Γ is irreducible, as the image of the irreducible 𝒲̃ under the proper map (pr_c, t).
  - The image of T contains the non-constant branch φ, so Γ ≠ {Y_0} × Δ.
  - If Γ had a constant branch {Y_0} × D at (Y_0, 0), then Γ ∩ ({Y_0} × Δ) would be a 1-dimensional analytic subset of the irreducible curve Γ, hence all of Γ. That is a contradiction.
  - So **every** branch of Γ at (Y_0, 0) is non-constant, i.e. lies in Φ (𝒲̃ is one of the W defining Φ).
- T″ is an irreducible germ, and its value map is holomorphic into Γ, with value (Y_0, 0) at the origin. At t = 0, x_{m+1} is intact at 0 with F ≅ Y_0, the constant value of c on E.
- So the image of T″ lies in a single branch ψ of Γ at (Y_0, 0), and ψ ∈ Φ. Hence x_{m+1} ∈ P_Φ(T″) with function ψ. ∎

**Product-type endpoint and genericity.** These are now covered by step 5 and by Lemma 3 (Z_Φ discrete). The "Y_t lies in a finite set on an open set" argument of the original product-type endpoint is not needed.

## 5. The items of the brief, and the residual cases

- **Lemma PT, Lemma J / Cor. J′.** Not used; step 3 covers product-type puncture transitions as well. (So the question whether "pinned" still gives a contradiction for a varying φ does not have to be decided.)
- **Transfer.** Lemma 5. The tracked function can change, but only to another branch of the same irreducible value curve, and it can never become rigid.
- **P(T) = C(L), Φ-version.** Lemma 3 (from (I5) = round12_q7 Lemma 1.1).
- **Mechanism D, (β)-twists, initial twist, (γ°).** Not used. Consistency checks:
  - (β)/initial twist with a rigid twin y = σ^{-1}x on T (round12_q7 (R-twin)): restricted to a lift-curve L ⊂ T (I2), this is an (NRT) configuration with a = σ. With a non-rigid twin, Prop. 2.1 of round12_q7 already passes it.
  - (γ°): round12_q8 Lemma 3 gives, along a lift-curve λ ⊂ T_1, F_x(λ(t)) on the tracked branch and F_{g^{-1}x}(λ(t)) ≡ Y_0, with g^{-1}x ≠ x (Lemma 1 there).
    - Its proof uses only that x is persistent on T_1 with its function (the value of x along λ is then that function, φ or Y) and that u = g^{-1}x ∈ M_W (a value in a finite set, hence ≡ Y_0). So it holds verbatim for a tracked φ ≠ Y.
    - So (γ°) is an (NRT) configuration (a = g, L = λ).
  - Endpoint rigidity (round12_q7 Lemma 4.1): L_b = aL_β with x rigid along L_b, i.e. a^{-1}x rigid along L_β while x ∈ C_Φ(L_β). This is an (NRT) configuration.
- **(R-a), (R-b)** (round12_q6 §4) and **(R1), (R2)** (round12_q2 §3). These are failure modes of particular routes to MS11♭ (through a 3-fold component X, an initial twist, or Stab(b̃)-transfer). The derivation of §4 does not go through any of them. More precisely, any failure of MS11♭_Φ at (Q, β̃, b̃, x), whatever its mechanism, gives an (NRT) configuration. Take lift-curves L_β ⊂ T_β, L_b ⊂ T_b, and a with L_b = aL_β (I1). If x ∉ C_Φ(L_b), then a^{-1}x ∉ C_Φ(L_β), so by Lemma 1 a^{-1}x is rigid along L_β, while x ∈ C_Φ(L_β).

## 6. Summary

**Proved** (modulo the cited inputs (I1)–(I6): R8-2 Lemma U/U3 and Theorem 1 under (Rig), round12_q7 Lemma 1.1, round11_q4 Lemma 2.1, round12_q6 Lemma G1(a), the walk chain with entries 85, 98, 99, B1♭ and the §2.7 transfer set-up and marking identification, entry 19):
- Lemma 1: along a lift-curve, every Y_0-copy has value either in Φ or ≡ Y_0.
- Lemma 2: (NRT) at Q ⇔ C_Φ(L) is Aut(Q)-invariant ⇔ C_Φ(L) is independent of L.
- Lemma 3: P_Φ(T) = C_Φ(L) for boundary-type anchored sheets.
- Proposition 4: under (NRT), Φ-persistence passes between any two boundary-type anchored sheets at Q; this gives MS11♭_Φ in full, without (S) and without the product/non-product distinction.
- Lemma 5: the Φ-transfer along a piece. The function may change within one irreducible value curve, all of whose branches at (Y_0, 0) are non-constant.
- §4: **(NRT) + (R1), (R2), (Rig) + Y non-constant ⇒ contradiction**, i.e. (NRT) ⇒ MS8, and with entry 82 ((Rig)) and entry 19 the problem's conclusion follows.

**Not proved / open:**
- (NRT) itself: exclude a rigid Y_0-copy and a Φ-copy of Y_0 exchanged by some a ∈ Aut(Q) along a lift-curve. By Lemma 2 this is now the single remaining twin statement. It is needed only at the finitely many puncture transitions and at the endpoint of the walk. By §5, every earlier residual obstruction is an instance of it.
- (Rig) (entry 82): untouched.
- The inherited inputs (I1)–(I6) were not re-derived here. In particular the marking identification x_m ↔ c ↔ x_{m+1} of §2.7 / R(D) was flagged earlier as "routine, inherited".

proved: the implication (NRT) ⇒ MS8 (Φ-chain), in the form above. not proved: (NRT). open: (NRT), (Rig).


## A suggestion (the planner's sketch; you are free to discard it)
**Why it should hold (planner's sketch; new decomposition this round).**
1. *Case split (from round13_q5 Lemma 1, step 2).* Let L ⊂ T, T a boundary-type anchored sheet of c̃ with lifted piece family component W. Then x is a constant vertex u of W with Γ_{W,u} ∋ φ non-constant, and the rigid copy y = a^{-1}x is either (A) a constant vertex v of W with Γ_{W,v} ≡ {Y_0} × Δ (irreducibility of Γ_{W,v}), or (B) a component of a coordinate of a point of the finite t-independent set F_W = K_W ∩ ∂, i.e. Y_0 is a component of a cusp value of the moving part K_W.
2. *a must move T and L* (Lemma E / Cor. E1 of round13_q6, and C_Φ(aL) = aC_Φ(L)): aT ≠ T is an anchored sheet of ac̃, a lift of the same coarse branch c, with lifted family σW for the induced σ ∈ Aut(G_c). So in case (A) a failure needs the coarse piece family 𝒞 = H(c × Δ) to have two distinct lifted components W ≠ σW through the same t = 0 lifted piece (if σW = W with σ exchanging the vertices u, v, then Γ_{W,u} = Γ_{W,v}, impossible since one is non-constant and the other ≡ Y_0). Conjecture (A): this "split lifted family" is impossible for a boundary piece of a totally geodesic smooth V_0 — because at t = 0 the generic curve of c_0 carries both constant Y_0-vertices, and total geodesy (Lemma J0: the vertex map of c_0 lifts over the Veech orbifold with coset monodromy; Lemma TG/Z: symmetric loci meet V_0 in Teichmüller curves or points) should force the swap to act on the whole lifted family, not just at Q.
3. *Case (B):* Y_0 ∈ 𝔉_W means the constant value Y_0 of vertex x on c_0 equals a component of a cusp of the moving image K_W. Conjecture (B): the a-exchange at Q of an intact constant Y_0-vertex with a component of a degenerate moving vertex contradicts Lemma PA/V (constant vertices carry no area, the moving Teichmüller vertex does) when read along the Teichmüller discs of V_0 approaching Q from the sheets c̃ and ac̃ — but by Lemma NG (round13_q7) such a t = 0 argument must be combined with a t ≠ 0 input (Theorem N for φ, the frozen value of y).
4. *Reflection sub-case* (a fixes c̃, aS = S): Lemma R / Prop. D reduce to excluding the detaching mirror (case II, needs k | M) and moved branches; a possible global input is a negativity/homology argument for the family 𝒟 of symmetric curves (round13_q6 Prop. G). Speculative.

## What is already known (do not merely re-derive it)
- A failure of (NRT_P) needs isotropy drop at Q: a ∉ Stab(L) (if aL = L then C_Φ(L) = C_Φ(a^{-1}L) = a^{-1}C_Φ(L) ∋ a^{-1}x, contradicting that a^{-1}x is rigid along L), so Q_t has ≥ 2 lift points and |Aut(Q_t)| < |Aut(Q)| for t ≠ 0. a must also move every anchored sheet carrying x along L (round13_q6 Lemma E / Cor. E1).
- Under (R2^orb) the lift locus at a puncture point is a single Aut(Q)-fixed curve, so (NRT_P) holds (round13_q10 Prop. 3.3); under the coarse reading this is exactly what can fail.
- Chart-level models of the rigid-twin reflection exist, consistent with (R1), (R2) (round13_q4 §1, round13_q3 §1, round13_q6 §3, round13_q1 §2): the lost swap is carried at t ≠ 0 by an interior curve of a-symmetric smooth curves ("detaching mirror"). The side-swap argument ("H_t glues the two sides of c̃") is refuted as a local argument.
- Lemma R (round13_q4) / Lemma FC (round13_q3) / Prop. D, Prop. G (round13_q6): in the reflection case with smooth 3-fold component, either a mirror anchored sheet is pointwise fixed (case I; forced when k ∤ M) or the mirror detaches into V_t (case II), giving a global 2-dimensional family 𝒟 of symmetric curves with 𝒟_0 ⊃ c.
- Lemma NG (round13_q7): t = 0 data alone cannot prove the statement.
- A counterexample needs g ≥ 3 (round12_q4 Euler bound), a varying complex structure of V_t (entry 33), and is a counterexample to the problem itself (under (Rig)).
- (γ°) configurations and the MERGE/MOV endpoint failure are instances of the (NRT_P) configuration (round13_q5 §5; round12_q8; round12_q7 Lemma 4.1).

## Prior results (verbatim answer files, bookkeeping lines removed; re-check what you use)

### round13_q4 (verbatim)
# round13_q4 — attempt on (NRT)

**Plan/status line.** (NRT) is **not proved and not refuted** here. What this file does:
1. §1: an explicit chart-level model of the *rigid-twin* (β)-reflection configuration (frozen twin, not just the (β)-twist of round11_q7 §6), and a check that it satisfies every chart-level constraint named in the brief. It shows *precisely where the planner's item 3 (side-swap) mechanism fails*: the sides of c_t are not glued by a label-preserving path; the swap is carried at t ≠ 0 by a curve of **interior** curves with the lost automorphism.
2. §2: **Lemma R (proved)**: in the reflection case of the (β)-origin, whenever the 3-fold component X is smooth at a generic point of c̃ × {0} and contains its own reflection, V_t contains, for every small t ≠ 0, a curve F_t of smooth curves admitting (a K_S-modification of) the lost automorphism a, with F_t → c as t → 0. This is forced, not an artefact of the model.
3. §3: **Lemma M (proved)**: the label monodromy statement behind item 3: the label permutation of a small loop around c_t in V_t is trivial on {x, y} for t ≠ 0, while at t = 0 it is the swap; the discrepancy is exactly accounted for by F_t. So item 3, as stated, is flawed (it would also "prove" the impossibility of the model in §1).
4. §4: the global object 𝒵 (the family of a-symmetric curves) and what total geodesy says about its central fibre (**Lemma Z, proved under (T4)**): the components of V_0 ∩ Z_a are Teichmüller curves or points. Reduction of the reflection case of (NRT) to a precisely stated open question (NRT-Z).
5. §5: what is not touched: the (γ°) origin, the endpoint origin, the sheet-moving case of (R-a)/(R-b), and singular X.

Readings: (R1), (R2) with H_0 = id, coarse reading (H_t need not preserve automorphism groups); (Rig); Y non-constant; and, only in Lemma Z, (T4) of round10_q1 §1 (every component of the preimage of V_0 in T_g is a totally geodesic complex submanifold). The family is assumed smoothly trivial in the sense of the footnote, in particular φ: 𝒱 → Δ is a submersion, so the coarse central fibre is reduced (this is the run's Lemma Red, entry 80).

---

## 1. A chart-level model of the rigid-twin reflection (proved as a local statement)

This sharpens round11_q7 §6. In that model the twin σy has value −t, so it is not frozen. Here the twin is frozen at Y_0, as (NRT) requires.

**Data.** P is a generic point of the piece c with Aut(P) = ⟨a⟩, a² = 1. a swaps two constant vertices x, y of type (g_i, n_i) with F_x(P) ≅ F_y(P) ≅ Y_0, and swaps their edges. Def(P) has coordinates including:
- m_x, m_y: one coordinate each on a fixed holomorphic curve germ through Y_0 in M_{g_i,n_i}, transported to the x- and y-slots, with value 0 at Y_0 (the other moduli of x, y are set to 0);
- s_e (e an edge at x) and s_{a e}; to keep notation light, all edges of the pattern of c are smoothed by the same function below;
- v: a coordinate of the moving vertex along c̃.

a acts by (m_x, m_y, s_e, s_{ae}, v) ↦ (m_y, m_x, s_{ae}, s_e, v).

**The 3-fold.** Let X be the image of (v, u, t) under
- m_x = (u + t)/2, m_y = (t − u)/2, v = v;
- s_e = u² − t² for every edge e of the pattern of c.

**Checks.**
1. *Embedding and equivariance.* (v, u, t) is recovered from (v, m_x − m_y, m_x + m_y), so this is an embedding. The image of (v, −u, t) is a·(image of (v, u, t)), so a preserves X and acts on it by u ↦ −u.
2. *Coarse family.* X/⟨a⟩ has coordinates (v, U = u², t), so it is smooth and t is a submersion on it. Coarse V_t ≅ {(v, U)} is smooth, with boundary {U = t²} ≅ (v-line) lying in the stratum of c. H_t(v, U) := (v, U + t²) is a stratum-preserving homeomorphism, smooth on the interior, with H_0 = id. The coarse central fibre is reduced. So the local versions of (R1), (R2), (i), (ii) and Lemma Red hold.
3. *t = 0.* S = X_0 = {(v, u)}, with c̃ = {u = 0}. a acts on S as the reflection u ↦ −u fixing c̃ pointwise, and x, y are intact constant Y_0-copies along c̃: the (β)-origin of (NRT).
4. *Anchored sheets and labels.* The boundary {N = 0} ∩ X is T ∪ aT, with T = {u = t} and aT = {u = −t}; both contain c̃ × {0}.
   - On T: F_x has coordinate m_x = t, so F_x = φ(t) with φ non-constant, φ(0) = Y_0. F_y has coordinate m_y = 0, so F_y ≡ Y_0: the **rigid twin**.
   - On aT: the roles are exchanged.
   - Both labels are constant along the piece (independent of v), as Lemma U requires of constant vertices.
5. *The symmetric curve.* Fix(a) ∩ X = F := {u = 0}. On F, s_e = −t² ≠ 0 for t ≠ 0. So F_t = {u = 0, t} is a curve of **smooth** curves in V_t admitting the automorphism a, at plumbing distance |s_e| = |t|² from the boundary curve c_t. On F_t the two subsurfaces have equal moduli m_x = m_y = t/2: "halfway" between φ(t) and Y_0.

So the rigid-twin (β)-configuration at a generic point of c̃ is consistent with every chart-level constraint. The only feature of V_t that distinguishes it from V_0 near P is item 5.

### 1.1 Label monodromy in the model (Lemma M, proved)
Fix v and t ≠ 0, and let γ_r be the loop U = t² + r e^{iθ}, θ ∈ [0, 2π], in coarse V_t around c_t. Lift it to X_t by u = √(t² + r e^{iθ}).
- If r < |t|², the lift is a closed loop around u = t (resp. u = −t), so the label permutation is trivial.
- If r > |t|², the lift runs from u_0 to −u_0, so the label permutation is a, which swaps x and y.
- At t = 0 every small loop around c (U = r e^{iθ}) has label permutation a.

So small loops around c_t do **not** swap the twins at t ≠ 0. The swap of t = 0 survives only on loops that also encircle the symmetric curve F_t (U = 0), a locus of orbifold points of V_t.

**Consequence for the planner's item 3.** Item 3 argues that the two sides of c̃ are glued continuously by H_t, so φ(t) and Y_0 would be values of the same constant vertex along a connected family. The model refutes this inference at the chart level. The two sides of c_t are joined inside V_t only through the region swept by loops of radius > |t|² around c_t, which crosses F_t, where Aut jumps. Under the coarse reading, H_t is not required to respect this jump. Any proof along the lines of item 3 must therefore show that the symmetric curve F_t cannot exist **globally**. §2 shows that F_t is forced in general, not only in the model.

---

## 2. Lemma R: the reflection forces a curve of symmetric smooth curves in V_t (proved under (H2))

**Setting.** This is the (β)-origin of (NRT), reflection case. Q, G := Aut(Q), B, q, 𝒳 := q^{-1}(closure 𝒱) ∩ (B × Δ_ε), and D := 𝒳 ∩ {N = 0}, as in the brief. c̃ is a lifted branch through 0 of a branch c of B_0, and S is a chart sheet (a component of q^{-1}(closure V_0) ∩ B) containing c̃. K_S is the pointwise stabiliser of S, and a ∈ G.
- **(H1)** a fixes c̃ pointwise, aS = S, and a|_S ≠ id (the "reflection" case of round12_q2 (R2) / round12_q6 (R-a)).
- **(H2)** X is a component of 𝒳 containing S × {0}. For p in a dense open subset of c̃ ∖ {0}: X is smooth at (p, 0), X ∩ {t = 0} = S near (p, 0) (no other G_X-translate of S contains c̃), and S and c̃ are smooth at p.

**Lemma R.** Under (H1), (H2) there are a′ ∈ a·K_S with a′ ∈ G_X = Stab_G(X), and an analytic set F ⊂ X (the union of the components of Fix(a′) ∩ X containing c̃ × {0}), such that:
1. a′|_S = a|_S. In particular a′ fixes c̃ pointwise and acts non-trivially on S.
2. Near (p, 0), for p as in (H2), F is a smooth surface, F ∩ {t = 0} = c̃ × {0}, and t|_F is non-constant. So F_t := F ∩ {t} is a non-empty curve for every small t, and F_t → c̃ as t → 0.
3. Dichotomy:
   - (R-i) either F ⊄ D, and then for p as in (H2) (outside a further discrete set) and small t ≠ 0, the points of F_t near (p, t) are **smooth curves in V_t admitting the automorphism induced by a′**;
   - (R-ii) or F ⊂ D, and then F is a 2-dimensional germ of D containing c̃ × {0} and pointwise fixed by a′. On F the labels z and a′z have isomorphic components at every point and every t.

*Proof.*
- **Step 0 (getting into G_X).** aX is a component of 𝒳 containing aS × {0} = S × {0}. Let z ∈ S be generic: interior, X smooth at (z, 0), Stab_G(z) = K_S. Near (z, 0), q^{-1}(𝒳) is the preimage of the irreducible germ (𝒳, (q(z), 0)) under the quotient by K_S, so its components through (z, 0) form one K_S-orbit (standard; this is the argument of round12_q2 Lemma A4). Hence aX = k_1X for some k_1 ∈ K_S, and a″ := k_1^{-1}a ∈ G_X with a″|_S = a|_S.
- **Step 1 (the order of t along S).** Put H := G_X ∩ K_S. It fixes S pointwise, so it acts on the normal line of S in X by a character χ, constant along S. Let m′ := |χ(H)|.
  - Near (z, 0), the coarse germ of 𝒱 is X/H. This is the quotient of a component by its stabiliser in Stab(z) = K_S.
  - Let y be a local equation of S in the smooth germ X. Then X/H is smooth with coordinate Y = y^{m′} transverse to S (Chevalley; the non-trivial elements of χ(H) are pseudo-reflections along S).
  - t|_X vanishes exactly on S near (z, 0), so t = unit · y^M, and hence t = unit · Y^{M/m′} on X/H.
  - The coarse central fibre is reduced, because φ is a submersion. So M = m′.
  - At (p, 0), X is smooth and X_0 = S, so t = u_0 · y^M there as well, with u_0 a unit and the same M (compare at nearby generic z).
- **Step 2 (normalising a″).** a″ preserves S and t, and fixes (p, 0). So y∘a″ = λ′y with λ′ a unit, λ := λ′(p, 0), and u_0 = (u_0∘a″)·λ′^M. Evaluating at the fixed point gives λ^M = 1. Since χ(H) = μ_M, pick k_2 ∈ H with χ(k_2) = λ and put a′ := k_2^{-1}a″. Then a′ ∈ G_X, a′|_S = a|_S, and a′ acts trivially on T_{(p,0)}X / T_pS. Also a′ ∈ a·K_S, which proves item 1.
- **Step 3 (linearisation).** By Cartan's theorem, a′ is linear in suitable coordinates on the smooth germ (X, (p, 0)). Its eigenvalues are:
  - 1 on T_pc̃, since a′ fixes c̃ pointwise;
  - ζ ≠ 1 on T_pS / T_pc̃. If dа′ were the identity on T_pS, then a′|_S would be the identity by Cartan's theorem on the smooth germ (S, p), contradicting item 1;
  - 1 on TX / TS, by Step 2.

  a′ has finite order, so it is semisimple. Its fixed set near (p, 0) is the smooth surface F with tangent space the 2-dimensional eigenspace E_1, and E_1 ∩ T_pS = T_pc̃. So F ⊄ S × {0}, and F ∩ S = Fix(a′|_S) = c̃ near p: a smooth curve contained in the fixed set, which is 1-dimensional because ζ ≠ 1. Hence F ∩ {t = 0} = c̃ × {0}. Since F ⊄ {t = 0}, t|_F is non-constant and vanishes on c̃ × {0}, so it takes every small value on F near (p, 0). This proves item 2.
- **Step 4 (dichotomy).** F ∩ D is analytic in F and contains c̃ × {0}.
  - If F ⊄ D, then c̃ × {0} is a component of the curve F ∩ D. Other components meet it in a discrete set of the punctured germ. For p off that set, F ∩ D = c̃ × {0} near (p, 0). So the points of F_t near (p, t), t ≠ 0, lie off {N = 0}, i.e. over V_t, and are fixed by a′. A point of the Kuranishi family fixed by g ∈ G is a curve admitting the automorphism induced by g (standard property of the Kuranishi family; (K1) in the run's notation). This is (R-i).
  - If F ⊂ D, then F is a 2-dimensional germ of D containing c̃ × {0} and pointwise fixed by a′. The label statement follows from equivariance (K3): F_{a′z}(a′w) ≅ F_z(w), and a′w = w on F. This is (R-ii). ∎

**Remarks.**
- In (NRT) with the (β)-origin, (R-ii) can only occur on an anchored sheet different from T and aT. On T itself the twins x, y = a^{-1}x have different values φ(t) ≠ Y_0 for small t ≠ 0, so T is not pointwise fixed by any element mapping y to x. Whether (R-ii) happens on some third anchored sheet is not decided here; in the §1 model it does not.
- The label action of a′ is k_2^{-1}k_1^{-1}a. It swaps x and y whenever K_S preserves x and y, for instance when K_S = 1, which is the typical situation of a "lost" automorphism.
- Lemma R needs no total geodesy. It is the general form of item 5 of §1.

---

## 3. The global object 𝒵 and what total geodesy says about its central fibre

### 3.1 Lemma Z (proved under (T4))
Let g ∈ Mod_g have finite order. Let Z_g ⊂ M_g be the locus of curves admitting an automorphism whose class in Mod_g is conjugate to g, and Z̄_g its closure in M̄_g. Z_g is a closed analytic (indeed algebraic) subset of M_g; its preimage in T_g is ⋃_h Fix(h), the union over the conjugates h of g (standard, cited from memory). Assume (T4). Then every 1-dimensional irreducible component of V_0 ∩ Z_g is the image of a Teichmüller disc, i.e. a Teichmüller curve, and V_0 ∩ Z_g has no 2-dimensional component unless V_0 ⊂ Z_g.

*Proof.*
- Fix(h) ⊂ T_g is a closed complex submanifold, namely the Teichmüller space of the quotient orbifold (cited, standard).
- It contains every Teichmüller disc tangent to it. Let X ∈ Fix(h) and v ∈ T_X Fix(h), v ≠ 0. The Teichmüller disc D_v through X tangent to v is unique: it is generated by the norming quadratic differential of v, which is unique (cited in PR-H §1.1, (Dual)). h is an isometry fixing X with dh(v) = v, so h(D_v) = D_v. Since h acts on D_v as a holomorphic self-map fixing X with derivative 1, and h has finite order, h|_{D_v} = id (Cartan). So D_v ⊂ Fix(h).
- Let C̃ be a 1-dimensional component of Ṽ ∩ Fix(h), where Ṽ is a component of the preimage of V_0, and let X be a smooth point of C̃ with tangent v. Then D_v ⊂ Fix(h). Also D_v ⊂ Ṽ by (T4), since D_v is the union of the real Teichmüller geodesics through X in the directions e^{iθ}v, all tangent to Ṽ.
- So D_v ⊂ Ṽ ∩ Fix(h). D_v is irreducible, 1-dimensional, closed, and contains the germ of C̃ at X. Hence C̃ = D_v. The image of C̃ in M_g is a closed algebraic curve (V_0 ∩ Z_g is algebraic), so it is a Teichmüller curve.
- If V_0 ∩ Z_g had a 2-dimensional component, it would be open in the irreducible V_0, hence V_0 ⊂ Z_g by the identity theorem. ∎

### 3.2 The family of symmetric curves
Assume (R-i) of Lemma R. Let g be the class of the automorphism induced by a′ on the smooth curves of F_t. Let 𝒵 be an irreducible component of the analytic set closure(𝒱) ∩ (Z̄_g × Δ) containing the germ q(F) at a point (q(p), 0), with p as in (H2).

**Proposition Z (proved, given Lemma R and Lemma Z).**
1. dim 𝒵 ≥ 2. If dim 𝒵 = 3, then 𝒵 = closure(𝒱) and V_0 ⊂ Z̄_g. Then every curve of V_0 has an automorphism of type g. Near a generic point z of S, that automorphism comes from Stab(z) = K_S, so some element of K_S is conjugate in Mod_g to the class of a′. Call this the **degenerate case**.
2. Otherwise dim 𝒵 = 2, 𝒵 is not contained in {t = 0}, and its central fibre 𝒵_0 is a pure 1-dimensional compact analytic subset of closure(V_0) ∩ Z̄_g. It contains the whole closure c̄ of the piece c.
3. For t ≠ 0 small, 𝒵_t ⊄ B_t. Near c_t, 𝒵_t contains q(F_t), a curve of smooth curves with an automorphism of type g, approaching c_t as t → 0.
4. Under (T4), every component of 𝒵_0 is either a boundary curve of closure(V_0) contained in Z̄_g (c̄ is one of them), or the closure of a Teichmüller curve contained in V_0 ∩ Z_g.

*Proof.*
- (1) closure(𝒱) is irreducible, because 𝒱 ≅ V_0 × Δ with V_0 connected and smooth. So a 3-dimensional component is all of it. The rest is the definition of Stab(z).
- (2) A 2-dimensional irreducible 𝒵 meeting {t = 0} in the curve c (locally), and not contained in it, has central fibre of pure dimension 1 (Krull). It is closed in the compact set closure(V_0) ∩ Z̄_g. It contains a non-empty open subset of the irreducible curve c̄, hence all of c̄.
- (3) This is Lemma R (R-i).
- (4) This is Lemma Z applied to V_0 ∩ Z_g: components of 𝒵_0 inside the boundary are boundary curves; the others are 1-dimensional components of V_0 ∩ Z_g, i.e. Teichmüller curves. ∎

**Remark (why this is the right global object).** In the §1 model, 𝒵 = q({u = 0}). The planner's item 3 implicitly assumes that 𝒵 does not exist. Lemma R shows that in the reflection case (with (H2)) 𝒵 always exists. So the reflection case of (NRT) is exactly the question of whether such a 𝒵 is compatible with total geodesy and smoothness of V_0, with (Rig) and with Y non-constant.

---

## 4. The residual open question (reflection case)

**(NRT-Z), open.** In the setting of (NRT), (β)-origin, reflection case with (H2), and outside the degenerate case: show that there is no irreducible 2-dimensional analytic 𝒵 ⊂ closure(𝒱) with the following properties:
- 𝒵_t ⊂ Z̄_g for all t;
- 𝒵_0 ⊃ c̄;
- near generic points of c, 𝒵_t (t ≠ 0) consists of smooth curves at plumbing distance → 0 from c_t, on which the two subsurfaces carried by x and y are exchanged by the automorphism;
- along the lift-curve L at the puncture Q, the boundary components x, y of Q_t have the distinct values φ(t), Y_0.

What I could not do:
- A degree argument (δ·𝒵_t = δ·𝒵_0, λ·𝒵_t = λ·𝒵_0) gives no contradiction. 𝒵_0 contains boundary curves, whose δ-degree has no sign.
- Following 𝒵_t to Q_t: Q_t lacks the automorphism, so 𝒵_t passes near Q_t without meeting it. I found no constraint on how it does so. The §1 model, extended to the puncture by adding a factor in which c̃ ends, gives no contradiction at chart level.
- Total geodesy enters only through Lemma Z, i.e. through the structure of 𝒵_0. That alone does not exclude 𝒵, since 𝒵_0 may consist of boundary curves only.

---

## 5. Not treated
- **Singular X**, i.e. (H2) failing: X singular along c̃ × {0}, X_0 ⊋ S near c̃, or S singular along c̃. Lemma R needs the linearisation on a smooth germ.
- **Sheet-moving twists:** aS ≠ S (round12_q2 (R1); round12_q6 (R-a), second bullet; (R-b) with τS ≠ S).
- **The (γ°) origin** (round12_q8) and **the endpoint origin** (round12_q7 Lemma 4.1). Here the frozen twin lives along a lift-curve without a (β)-twist at a generic point of a branch, and Lemma R has no input.
- The unchecked Φ-substitution of round12_q7 §3, and (Rig) (entry 82).

## Summary: proved / not proved / open

**Proved** (modulo cited standard facts: Cartan linearisation, Chevalley, Krull, uniqueness of Teichmüller discs, the Kuranishi family properties (K1), (K3); and round12_q2 Lemma A4's orbit argument):
- §1: an explicit chart-level model of the rigid-twin (β)-reflection configuration, consistent with all chart-level constraints. With it, Lemma M: at t ≠ 0, small loops around c_t have trivial label monodromy, while at t = 0 they swap the twins. Consequence: **the planner's item 3 (side-swap) argument is flawed as stated.** The sides of c_t are joined only across a curve F_t of orbifold points of V_t.
- §2, Lemma R: in the reflection case, under (H2), V_t contains for every small t ≠ 0 either a curve F_t of smooth curves admitting the lost automorphism (modified by K_S), converging to c (R-i), or an anchored sheet pointwise fixed by it (R-ii).
- §3, Lemma Z (under (T4)): the components of V_0 ∩ Z_g are Teichmüller curves. Proposition Z: the global 2-dimensional family 𝒵 of symmetric curves and the structure of its central fibre.

**Not proved:** (NRT) in any of its three origins. No counterexample is given.

**Open:** (NRT-Z) of §4; the cases listed in §5; and (R-ii) on a third anchored sheet.

**Verdict: not proved** (partial: a reduction of the reflection case of the (β)-origin to (NRT-Z), and a refutation of item 3's mechanism at chart level).



### round13_q6 (verbatim)
# round13_q6: attempt on (Refl), the reflection case of MS11♭

**Status line.** NOT PROVED. What this file gives:
- (1) an exact equivariance lemma (Lemma E), which disposes of every h that stabilises the relevant sheet;
- (2) a local normal form at generic points of the mirror curve c̃, under an explicit smoothness hypothesis (Sm), with a dichotomy (Prop. D). Case I is harmless. Case II is the only surviving local mechanism. A numerical criterion forces case I whenever k ∤ M;
- (3) the exact point where the planner's "two sides of c̃" mechanism (sketch item 3) breaks down: in case II the mirror of h *detaches from the boundary* for t ≠ 0. There is an explicit chart-level model of this, consistent with every local constraint, including Lemma TG at t = 0;
- (4) the global necessary condition that a failure forces;
- (5) a list of open items.

Readings (R1), (R2) and the notation of the task file are used throughout. G := Aut(Q) acts on Def(Q) × Δ_ε by g·(p,t) = (gp, t). No result is cited from the literature except standard facts named where they are used (Cartan linearisation, Weierstrass preparation), which I cite from memory.

---

## 1. Lemma E (equivariance of persistence sets)

**Lemma E.** Let g ∈ G and let c̃ be a lifted branch at Q.
1. g maps Ñ_c̃ onto Ñ_{g c̃}, and maps anchored sheets of c̃ bijectively onto anchored sheets of g c̃.
2. For every anchored sheet T, P(gT) = g·P(T).
3. If g fixes T pointwise, then F_{gx}(p) ≅ F_x(p) (as pointed curves, for some ordering) at every (p,t) ∈ T at which x is intact.
4. Items 2 and 3 also hold for any irreducible 2-dimensional germ T (for example a local branch of an anchored sheet at a point (p_0,0) ≠ (0,0)), with P(T) defined in the same way.

*Proof.*
- (1) The set q^{-1}(H((c∖Q)×Δ_ε)) ∩ (B×Δ_ε) is G-invariant, because q∘g = q and B is G-invariant. So g permutes its connected components and sends the one containing c̃∖{0} to the one containing g c̃∖{0}. Being a biholomorphism, g preserves closures, irreducible components, and the property "contains c̃×{0}" (sending it to "contains gc̃×{0}").
- (2) g acts on the universal family over Def(Q), covering its action on the base. For p ∈ Def(Q) it gives an isomorphism C_p → C_{gp} that sends the component with label x to the component with label g·x. Here G acts on the labels V(G_Q) through its action on the dual graph of Q, and s_{g e}(gp) = 0 iff s_e(p) = 0, so intactness is transported.
  - Let x ∈ P(T) and (p,t) ∈ gT. Then (g^{-1}p, t) ∈ T, so x is intact at g^{-1}p and F_x(g^{-1}p) ≅ Y_t.
  - Hence gx is intact at p and F_{gx}(p) ≅ F_x(g^{-1}p) ≅ Y_t, with the special points transported (the definition allows some ordering).
  - So gx ∈ P(gT). The reverse inclusion follows by applying this to g^{-1}.
- (3) This is the same computation with gp = p.
- (4) Only the G-action and the universal family were used. ∎

**Corollary E1 (sheet-stabilising reflections are harmless).** In (Refl)(a), let L be an x-good lift-curve lying in an anchored sheet T, with x ∈ P(T) (P(T) = C(L) on boundary-type sheets, as recorded in the task file). If h(T) = T, then hL ⊂ T and x ∈ P(T). So h carries L to a lift-curve inside a sheet on which x **is** persistent, and in addition hx ∈ P(T).
- In the (NRT-config) of the planner's sketch, the sheet carries x with F_x ≅ φ(t) non-constant and y = h^{-1}x with F_y ≡ Y_0. If h fixes that sheet T, or merely stabilises it, Lemma E(2) gives h^{-1}x ∈ P(T): F_y ≅ Y_t on T, so Y_t ≅ Y_0 up to reordering for all t. That puts Y_t in a finite set, so Y would be constant (entry 19), which contradicts the hypothesis "Y non-constant".
- **Hence any failure of (Refl)(a) needs h ∉ Stab(T) for every anchored sheet T carrying x along the relevant lift-curves.** The same holds for the local branches of T at generic points of c̃ (Lemma E(4)).

---

## 2. Local normal form along the mirror c̃ and the dichotomy

**Setting of this section.**
- h ∈ G with h(S) = S, h|_S ≠ id, and h fixing the boundary curve c̃ ⊂ S pointwise (case (a)).
- E_c ⊂ E(G_Q) is the set of edges with s_e ≡ 0 on c̃, and N_c := ∏_{e∈E_c} s_e.
- p_0 is a generic point of c̃∖{0}: it lies on no other lifted branch, at p_0 the curve c̃ is smooth and the germ (S,p_0) is smooth, and Stab_G(p_0) = Stab_pt(c̃).
- X is a 3-dimensional irreducible component of q^{-1}(closure 𝒱) ∩ (B×Δ_ε) with X ⊃ S×{0} and h(X) = X. (h(X) = X is automatic if S×{0} lies in only one 3-fold component.)
- k ≥ 2 is the order of h|_S.
- M := ord_{c̃}(N_c|_S) = Σ_{e∈E_c} ord_{c̃}(s_e|_S) ≥ 1.

**Hypothesis (Sm) (extra; not known in general).** At (p_0,0), X is smooth and t|_X is a submersion, with X ∩ {t=0} = S near p_0 (reduced).

**Lemma LN (normal form).** Under (Sm) there are holomorphic coordinates (z,σ,t) on X near (p_0,0) such that:
- t is the time coordinate;
- S = {t=0} and c̃×{0} = {σ = t = 0};
- h(z,σ,t) = (z, ζσ, t), with ζ a primitive k-th root of unity.

Moreover N_c|_X = U·W, where U is a unit and W is a Weierstrass polynomial of degree M in σ with W(σ; z, 0) = σ^M. Finally:

  **W(σ) = σ^r · W_1(σ^k; z, t),** where 0 ≤ r < k, r ≡ M (mod k), and W_1 is a Weierstrass polynomial in τ = σ^k.

*Proof.*
- **Linearising h.** By Cartan's linearisation theorem (cited from memory: a finite group fixing a point of a complex manifold is linearisable there), h is linear in suitable coordinates at (p_0,0). The function t is h-invariant and dt ≠ 0 on T X, so the line T X / T S ≅ C (via dt) is a trivial representation. T S splits h-invariantly as T c̃ ⊕ ν, with h trivial on T c̃. On ν it acts by a primitive k-th root ζ: it is non-trivial because h|_S ≠ id and finite-order maps are determined by their derivative at a fixed point, and k is the order of h|_S.
- So Fix(dh) is 2-dimensional, and Fix(h) ∩ X = D is a smooth surface tangent to T c̃ ⊕ (an invariant complement of T S). Take linear coordinates (z, σ, w) with D = {σ = 0}.
- **Making t a coordinate.** h-invariance of t gives t = f(z, σ^k, w). Since dt|_{T D} ≠ 0 and t vanishes on c̃×{0} ⊂ D, we may replace w by t.
- **The function N_c.** Each g ∈ G permutes the divisors {s_e = 0}, so s_e∘h = (unit)·s_{π(e)}, where π is a permutation of E_c (h fixes c̃ pointwise, so it preserves its pattern). Hence N_c∘h = v·N_c with v a unit.
- **Weierstrass form.** At t = 0, N_c|_S = (unit)·σ^M. Weierstrass preparation in σ gives N_c|_X = U·W.
- **The shape of W.** ζ^{-M}W(ζσ) is again a Weierstrass polynomial in σ, and it differs from W by a unit. By uniqueness in the preparation theorem it equals W. Write W = Σ_j a_j(z,t) σ^j. Then a_j(ζ^j − ζ^M) = 0, so a_j = 0 unless j ≡ M (mod k). Hence W = σ^r W_1(σ^k). ∎

**Lemma B0 (boundary branches near (p_0,0)).** Let U be a small neighbourhood of (p_0,0). Every irreducible component B of X ∩ {N_c = 0} ∩ U has the following properties:
- it is a local branch at (p_0,0) of an anchored sheet of c̃;
- all s_e, e ∈ E_c, vanish on B;
- B ∩ {t=0} = c̃ near p_0.

*Proof.*
- By (R2), closure(𝒱) ∩ (∂M̄_g × Δ) ∩ q(U) = H((c ∩ U')×Δ) for a small neighbourhood U' of Q' := q(p_0). Here we use that p_0 is generic, so c is the only boundary branch of closure V_0 at Q'. H preserves strata, so q(B) lies in the stratum of c, and every s_e, e ∈ E_c, vanishes on B.
- The set B ∩ {t=0} is ≥ 1-dimensional (a hypersurface section of a surface through (p_0,0)) and lies in S ∩ ∂ = c̃ near p_0.
- B ∖ {t=0} is connected (an irreducible germ minus a proper analytic subset) and lies in q^{-1}(H((c∖Q)×Δ_ε)). Its closure meets c̃∖{0} ⊂ Ñ_c̃. So B ⊂ closure(Ñ_c̃), and B lies in some irreducible component T of it containing c̃×{0}. ∎

**Proposition D (dichotomy under (Sm)).** Let D = Fix(h) ∩ X = {σ = 0}. Then D is a smooth surface, transverse to {t = 0}, with D ∩ {t=0} = c̃ near p_0. Exactly one of the following holds.
- **Case I (σ | W, i.e. r ≥ 1 or W_1(0;z,t) ≡ 0).** D ⊂ X ∩ {N_c = 0}. So D is a local branch at (p_0,0) of an anchored sheet T_D of c̃, and h fixes D pointwise. By Lemma E(3,4), P(D) is h-invariant, and on D one has F_{hx} ≅ F_x at every point where x is intact.
- **Case II (σ ∤ W; this forces k | M).** For t ≠ 0 small, D_t := D ∩ {t} is a curve in the interior part q^{-1}(V_t) that converges to c̃ as t → 0. So V_t contains a curve q(D_t) of smooth curves admitting the automorphism h, accumulating on c as t → 0. The boundary branches near (p_0,0) are the branches of {W_1(σ^k) = 0}, and h permutes them.

In particular: **if k ∤ M, then case I holds.**

*Proof.* The statement about D is part of Lemma LN. If σ | W then D ⊂ {N_c = 0}, and Lemma B0 applies. If σ ∤ W then r = 0, so k | M. Moreover W_1(0; z, t) ≢ 0, while W_1(0; z, 0) = 0 (because W(σ;z,0) = σ^M). So N_c ≠ 0 on D at generic points with t ≠ 0, i.e. D_t is interior there. ∎

**Corollary D1 (what survives locally).** Assume (Sm) at a generic p_0. Let T be an anchored sheet with x ∈ P(T) and let B_x be any local branch of T at (p_0,0). The planner's configuration fails at T only if both of the following hold:
- B_x ≠ D (otherwise Lemma E(3) gives F_{hx} ≅ F_x ≅ Y_t on D);
- h(B_x) ≠ B_x (otherwise Lemma E(4)).

So, besides the condition h ∉ Stab(T) of Cor. E1, a failure needs the x-carrying local branches at generic points of the mirror to be non-fixed branches of {W_1(σ^k) = 0} that h moves.
- In Puiseux terms: B_x lies over a branch R of {W_1(τ) = 0} ⊂ (z,τ,t)-space, and the cyclic k-fold cover σ ↦ σ^k = τ restricted over R splits. For example, when R = {τ = t^a u} with u a unit, the cover splits only if gcd(a,k) > 1.
- In case I the fixed branch D is itself a boundary sheet, and on it hx is persistent iff x is.

---

## 3. Where the planner's mechanism (sketch item 3) fails

The planner's mechanism has two ingredients:
1. a loop around c in the coarse sheet Σ_0 = q(S) lifts in S to a path from p to hp, so h swaps the two sides of c̃;
2. H_t is a homeomorphism, so at time t the meridian of c_t should again swap the sides, which would force φ(t) ≅ Y_0.

Step 2 fails exactly in case II.

**The rigorous half (proved, under (Sm)).**
- Lift the meridian of c_t to Def(Q). Let it be a small loop at time t around c_t near Q'_t, radius r → 0, and let p* be the limit point of the lifts on a boundary branch.
- For r small, q^{-1}(small ball around q(p*)) is a disjoint union of small balls around the points of G·p*. So the lifted path stays in one of them, and its monodromy g satisfies g·p* = p*. That is, g ∈ Aut(curve at p*).
- If g moved x to y, then F_x(p*) ≅ F_y(p*), and φ(t) ≅ Y_0 up to reordering. So **step 2 would be correct if the monodromy of the small meridian of c_t were still h (modulo K_S)**.

**Why it is not.**
- The big loop (radius r_0 fixed, t → 0) does have monodromy in hK_S, by continuity of the endpoint and the fact that generic points of S have stabiliser K_S.
- But the big loop and the small meridian of c_t are homotopic in Σ_t ∖ c_t only through the interior branch locus of q, and in case II that locus contains q(D_t). Crossing it multiplies the monodromy by h^{±1}.
- So at time t the h-swap belongs to the mirror q(D_t), not to c_t. On each lift of c_t the labels x, y are no longer exchanged by anything.

**Chart-level model of case II (consistent with all local constraints, not globalised).**
- Coordinates. X = C³_{(z,σ,t)} ⊂ Def(Q)×Δ (locally near (p_0,0)), S = {t=0}, h(z,σ,t) = (z,−σ,t), so k = 2.
- Edges. E_c = {e, e'} with e at x and e' = h(e) at y, and s_e|_X = s_{e'}|_X = σ² − t² (up to units). Then M = 4, k | M, and r = 0: case II.
- At t = 0. N_c|_S = σ⁴, Fix(h) ∩ S = c̃ = {σ = 0}, and h acts on S as a reflection fixing c̃. This is allowed by Lemma TG ("a union of points and boundary curves").
- At t ≠ 0. The stratum of c is cut out on X by s_e = s_{e'} = 0, i.e. by {σ = t} ∪ {σ = −t}. These are two anchored sheets T_± = {σ = ±t}, both containing c̃×{0}, exchanged by h. Both e and e' are pinched on each, so H preserves the stratum, as (R2) requires.
- Labels. Put F_x = φ(t), F_y ≡ Y_0 on T_+. By Lemma E(2), F_y = φ(t), F_x ≡ Y_0 on T_−. This is consistent.
- The mirror. D = {σ = 0} has s_e = s_{e'} = −t² ≠ 0: it is interior.
- The coarse picture. With w = σ², Σ_t is (z,w)-space with boundary c_t = {w = t²} and an interior curve {w = 0} of h-symmetric smooth curves. So Σ_0 → Σ_t is the homeomorphism w ↦ w + t², which is compatible with (R2) locally. V_t is smooth (the quotient by a reflection is smooth).
- Conclusion of the model. x is persistent on T_+ but not on T_− = hT_+. This is exactly the (R-a) failure.

This model is chart-local, so by the task's rules it is not a counterexample. It shows that **no argument using only the germ of the family at points of c̃ can prove (Refl)(a)**, even with total geodesy at t = 0, since Lemma TG constrains only Fix(h) ∩ S. This agrees with round11_q7 §6 and round11_q1 §5, and pins the obstruction to the detaching mirror.

---

## 4. Global necessary condition for a failure (proved, under (Sm) at one generic point of c̃)

**Proposition G.** Suppose (Refl)(a) fails through h and mirror curve c̃, and (Sm) holds at some generic p_0 ∈ c̃. Then either:
- (i) the failure is through a moved branch of {W_1(σ^k)=0} in case I (Cor. D1); or
- (ii) case II holds.

In case II, for all small t ≠ 0, V_t contains smooth curves admitting an automorphism of the topological type of h, arbitrarily close to c_t. Their limit set as t → 0 contains c.
- So the closed analytic set 𝒜 := closure(𝒱) ∩ (M̄_g^{[h]} × Δ) has a 2-dimensional irreducible component 𝒟 with 𝒟_t ⊄ ∂M̄_g for t ≠ 0 and 𝒟_0 ⊃ c. Here M̄_g^{[h]} is the closed locus of stable curves with an automorphism of the type of h.
- The fundamental classes of the curves H_t^{-1}(𝒟_t) ⊂ closure(V_0) are constant in H_2(closure V_0) and equal [𝒟_0], a cycle that contains the boundary curve c with positive multiplicity.

*Proof.* Case II is Prop. D. 𝒜 is closed analytic because M̄_g^{[h]} is closed analytic: it is the image of a proper map from a moduli space of stable curves with a Z/k-action, which I cite from memory as standard. q(D) ⊂ 𝒜 is 2-dimensional, and its closure gives 𝒟. Constancy of homology classes in a flat analytic family of 1-cycles over a disc, transported by the homeomorphism H, is standard. ∎

**Remarks on using Prop. G (unproved routes).**
- At t = 0, the interior part of 𝒟_0 consists of h-symmetric curves of V_0. By total geodesy (the fixed set of h on the lifted Teichmüller disc structure), it is a union of Teichmüller curves and points. But 𝒟_0 may lie entirely in B_0, so this gives no contradiction.
- A contradiction would follow from a **negativity statement**: if the boundary curves of closure(V_0) through q(c) (or the relevant component of B_0) had negative definite intersection matrix, then an effective cycle supported on B_0 could not be homologous to the effective cycle H_t^{-1}(𝒟_t) meeting the interior.
  - Sketch: Z := 𝒟_0 = Σ a_j C_j. Then Z² = Σ a_j Z·C_j = Σ a_j W·C_j ≥ 0 when W shares no component with B_0, which contradicts Z² < 0.
  - Caveats: W may contain boundary components; the closure may be singular, so intersection numbers need Mumford's rational intersection theory on normal surfaces; and negativity is false in general (λ is positive on boundary curves whose moving part has positive genus). So this route is open and probably needs extra structure.
- Constancy of λ·𝒟_t and δ·𝒟_t gives numerical constraints only.

---

## 5. What is proved, what is not, open questions

**Proved.**
- Lemma E and Cor. E1: persistence sets are G-equivariant. Reflections, or any lost automorphisms, that stabilise the x-carrying anchored sheet (or one of its local branches) never cause a failure. In particular the planner's (NRT-config) is contradictory whenever h stabilises the sheet that carries x.
- Lemma LN, Lemma B0, Prop. D, Cor. D1, under (Sm) at a generic point of c̃:
  - the normal form, with N_c|_X = U·σ^r W_1(σ^k);
  - the dichotomy case I / case II;
  - **k ∤ M ⇒ case I**;
  - in case I the mirror is a pointwise-h-fixed boundary sheet on which hx is persistent iff x is;
  - a failure needs moved branches.
- Section 3: the precise failure point of the planner's sketch item 3 (the detaching mirror), with a chart-level model of case II consistent with (R2), the stratum condition and Lemma TG.
- Prop. G: the global necessary condition (a 2-dimensional family of h-symmetric curves of V_t degenerating onto c).

**Not proved.**
- (Refl)(a) in general.
- (Refl)(b) (h(S) ≠ S): only Lemma E applies, giving no failure when h stabilises the x-carrying sheet.
- The initial-twist clause τ ∉ Stab(b̃)Stab(x): not treated beyond Lemma E.
- MS11♭, hence MS8 and the problem's claim: not proved here.

**Open questions.**
1. Exclude case II globally. Show that a totally geodesic smooth V_0 admits no deformation satisfying (R1), (R2) in which the mirror of a reflection h of a sheet S, fixing a boundary curve, detaches into V_t. Prop. G's family 𝒟 with 𝒟_0 ⊂ B_0 is the object to rule out (negativity, or a Teichmüller-disc argument at t = 0 applied to H_t^{-1}(𝒟_t)).
2. Exclude, or realise globally, the moved-branch configuration of Cor. D1 in case I.
3. Remove hypothesis (Sm), e.g. by working on the normalisation of X. Its singular locus may contain the curve over c̃, so this is not automatic.
4. Settle whether k | M can actually occur for (S, h, c̃) arising from a totally geodesic smooth V_0. This is a t = 0 question about vanishing orders of plumbing coordinates along a mirror curve, and the plumbing description of Teichmüller discs near c (Lemma PA style) might decide it. If k ∤ M always held, case II would be excluded, and only the moved-branch configuration of case I would remain to exclude (Cor. D1).

Outcome: **not proved** (partial results above; the obstruction is sharpened to the detaching-mirror configuration of Prop. D, case II, plus moved branches).


### round13_q3 (verbatim)
# round13_q3: attempt on MS11♭ (rigid-twin / reflection case)

**Status line.** PARTIAL. I do not prove MS11♭ and I do not give a global counterexample. I read only the task part of the brief, the chain, and the round-12 file round12_q7 (Φ-persistence, Lemma 1.2, Prop. 2.1, Lemma 4.1). I did not re-read the rest of the 5000-line prior-results file.

What this file contains:
- (§1) Step 3 of the planner's sketch ("the two sides of c̃ are swapped by the reflection, so φ(t) and Y_0 are forced onto one constant vertex") does not work. In a complex surface a complex curve has no two sides. More importantly, there is an explicit **local model near a generic point of the piece c**, not only near Q. In it the reflection case with a rigid twin occurs, and it is compatible with (R1) and (R2) in the chart. So step 3 cannot be proved by any argument that is local along c.
- (§2) A new proved necessary condition (Lemma FC), under a smoothness hypothesis on the 3-fold component. In a reflection-type failure, one of two things happens. Either there is a third anchored sheet of c̃ fixed pointwise by σ, on which x and y have equal value functions. Or, for every small t ≠ 0, V_t contains a holomorphic curve of smooth curves admitting the automorphism σ, and these curves converge to c as t → 0. In words: the automorphism that is "lost" on the boundary reappears on interior curves of V_t.
- (§3) Chain check. I found no new flaw. I re-state the dependence on (Rig).
- (§4) Proved / not proved / open.

Readings (R1), (R2), and all the definitions (pieces, Def(Q), labels, anchored sheets, Φ, rigid copies), are those of the task file.

---

## 1. The planner's step 3 fails: a local model of a reflection with a rigid twin near a generic point of c

### 1.1 Two corrections to the picture in step 3
- c̃ is a complex curve in the complex surface germ S, so S ∖ c̃ is connected near any point of c̃: a punctured disc bundle has no "two sides".
  - A finite-order σ ∈ Stab_pt(c̃) acting non-trivially on a smooth local branch S_1 ⊃ c̃ is linearised (Cartan) as (u, w) ↦ (u, ζw), with ζ ≠ 1 a root of unity. Here c̃ = {w = 0}.
  - "Approaching from the two sides" should therefore read: the subsurface Σ_x of the curve at (u, w) is carried by σ to the subsurface Σ_y of the curve at (u, ζw), which is the same coarse point.
- Hence the right question is: does the monodromy "x ↦ y" of the small coarse loop around c in V_0 survive in V_t? The model below shows that it need not survive near c_t. What it does force is an interior orbifold point (§2).

### 1.2 The model
Setting at a generic point p ∈ c̃, p ≠ 0. Assumptions on the curve P at p:
- P has two components x, y ≅ Y_0 (dim M_{g_i,n_i} = d > 0). Each is attached by one node, e = (x, r_1) and σe = (y, r_2), to a component R.
- There is an automorphism σ of P of order 2. It swaps x and y, preserves R, and swaps r_1 and r_2.
- The moving part of c lies in the remaining coordinates and keeps σ. That is, the curves of c all admit σ, as they must for σ ∈ Stab_pt(c̃).

Coordinates on Def(P):
- z_x, z_y ∈ C^d: local moduli coordinates of the two components, chosen σ-equivariantly, so that σ*z_y = z_x.
- s_e, s_{σe}: plumbing parameters, with node coordinates chosen σ-equivariantly (possible because σ² = id), so that s_{σe}∘σ = s_e.
- u: the remaining coordinates (the moving part; σ acts trivially on the u-locus used).
- All further edges are treated like e, σe below; I suppress them.

Define X ⊂ Def(P) × Δ as the image of (u, w, t) ↦ point with
- s_e = s_{σe} = w(w − t);
- z_x = Y_0 + a(t − w), z_y = Y_0 + a·w, where a ∈ C^d ∖ {0} is fixed;
- remaining coordinates K(u).

Checks:
1. **σ-invariance.** σ(u, w, t) = (u, t − w, t). Indeed, s_e and s_{σe} are both invariant under w ↦ t − w, and z_x(u, t − w, t) = Y_0 + a·w = z_y(u, w, t). So σ(X_t) = X_t for each t.
2. **t = 0.** S := X_0 is given by s_e = s_{σe} = w², z_x = Y_0 − a w, z_y = Y_0 + a w. Along c̃ = {w = 0}, both x and y are intact, constant, ≅ Y_0. σ fixes c̃ pointwise and acts on S by w ↦ −w. This is the **reflection case (R-a)**.
3. **Boundary at time t.** N = 0 on X_t exactly on T_t = {w = 0} and σT_t = {w = t}.
   - T := {w = 0}: x is intact with value φ(t) = Y_0 + a t (non-constant), and y is intact with value ≡ Y_0.
   - σT = {w = t}: x is intact with value ≡ Y_0, so x is **rigid** there.
   - Both T and σT contain c̃ × {0}, so both are anchored sheets of c̃. This is exactly the rigid-twin (β)-edge of round12_q7 Prop. 2.1(3), second alternative.
4. **(R1), (R2) in the chart.** Assume Aut(P) = ⟨σ⟩. Then the coarse germ of closure(V_t) at c_t is X_t/⟨σ⟩, with coordinates (u, v), v = (w − t/2)².
   - The coarse boundary is {v = t²/4}. At t = 0, the coarse V_0 is {(u, v)}, v = w², with boundary {v = 0}.
   - H_t(u, v) := (u, v + t²/4) is a homeomorphism, smooth (indeed holomorphic) in (u, v, t). It preserves the open stratum and the boundary stratum, and H_0 = id.
   - The coarse 𝒱 is the smooth 3-fold {(u, v, t)}. So the chart-level content of (R1), (R2) holds.
5. **Where the swap went.** For t ≠ 0, σ fixes the interior curve {w = t/2} of X_t. There N = s_e s_{σe} ≠ 0, s_e = −t²/4, and z_x = z_y = Y_0 + a t/2. These are smooth curves of V_t with the extra automorphism σ. They converge to c as t → 0.
   - The coarse loop around c in V_0 has monodromy x ↦ y. At time t, a small loop around c_t has no swap. A loop of the original size encloses the orbifold point v = 0 and does have the swap.
   - Nothing forces φ(t) = Y_0: the values agree only at the σ-fixed interior curve, where both equal Y_0 + a t/2.

**Conclusion of §1.** The mechanism proposed in step 3 does not hold in this model. The reflection σ, a non-constant Φ-copy x on T and a rigid copy on σT all coexist, near a generic point of c, with (R1) and (R2) satisfied in the chart. Any proof of (R-a) must therefore use information that is global along c or global on V_0: total geodesy, the global walk, or the behaviour at the punctures of c.
- Total geodesy of S at t = 0 is not tested by the model. I give no argument that this S can be totally geodesic, nor that it cannot. A proof of (R-a) through total geodesy would have to exclude an S of exactly this shape: the reflection w ↦ −w, with z_x − z_y vanishing to first order along c̃.

## 2. Lemma FC: the lost automorphism reappears on interior curves of V_t

**Lemma FC (fixed-curve dichotomy).** Let c̃ be a lifted branch of a piece c, p ∈ c̃ ∖ {0} a point, and σ ∈ Stab_pt(c̃). Let X be an irreducible component of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) through (p, 0). Assume:
- (a) near (p, 0), X is a complex manifold, t|_X is a submersion, and X ∩ {t = 0} = S_1 is a smooth local branch at p of the t = 0 sheet;
- (b) σ(X) = X and σ|_{S_1} ≠ id (the reflection case).

Then Fix(σ) ∩ X =: Ψ is, near (p, 0), a 2-dimensional complex submanifold with Ψ ∩ {t = 0} = c̃ and t|_Ψ a submersion. Moreover exactly one of the following holds:
- (FC1) Ψ ⊂ {N = 0}. Then Ψ is a 2-dimensional germ of X ∩ {N = 0} containing c̃ × {0}, fixed pointwise by σ. At every point of Ψ, F_y ≅ F_{σy} for every label y. In particular, if σ swaps x and y, then x and y have the same value function on Ψ.
- (FC2) For every small t ≠ 0, the curve Ψ_t := Ψ ∩ {t} contains points r with N(r) ≠ 0. Each such r is a smooth curve of V_t (after applying q) admitting the automorphism induced by σ. As t → 0 these curves converge to c.

*Proof.*
1. σ ∈ Aut(Q) acts on B × Δ_ε as σ_B × id, so t∘σ = t, and σ preserves X and each X_t. Since X is a manifold and σ has finite order, Cartan's linearisation theorem applies at the fixed point (p, 0). So Fix(σ|_X) is a submanifold whose tangent space is the eigenvalue-1 space E of dσ on T := T_{(p,0)}X (dim 3).
2. σ preserves X_0 = S_1, so dσ preserves T S_1 = ker(dt|_T). This is 2-dimensional, because t|_X is a submersion and X_0 = S_1 is smooth. On T S_1:
   - dσ fixes T c̃, since σ fixes c̃ pointwise;
   - dσ ≠ id, since σ|_{S_1} has finite order and is not the identity, and by Cartan a finite-order map with identity differential at a fixed point is the identity near it. So the eigenvalues on T S_1 are 1 and ζ ≠ 1.
3. On T/T S_1 ≅ C (via dt), σ acts trivially, because t∘σ = t. As dσ is diagonalisable (finite order), its eigenvalues on T are 1, ζ, 1. So dim E = 2, and E ⊄ T S_1, i.e. dt|_E ≠ 0.
4. Hence Ψ is a 2-dimensional submanifold and t|_Ψ is a submersion. Ψ_0 = Fix(σ|_{S_1}) is a 1-dimensional submanifold of S_1 containing c̃, so it equals c̃ near p.
5. Ψ is a connected manifold germ, hence irreducible. So either Ψ ⊂ {N = 0}, which is (FC1), or Ψ ∩ {N = 0} is a proper analytic subset of dimension ≤ 1.
6. In the second case, the components of the 1-dimensional germ (Ψ ∩ {N = 0}, (p, 0)) are c̃ × {0} and curves on which t is non-constant: a curve inside {t = 0} lies in Ψ_0 = c̃. So for small t ≠ 0, Ψ_t ∩ {N = 0} is finite while Ψ_t is a curve. The other points r of Ψ_t lie in q^{-1}(V_t), because H preserves the open stratum and X ∩ {N ≠ 0} lies over 𝒱. Since σ(r) = r with σ ∈ Aut(Q), σ induces an automorphism of the curve at r.
7. As t → 0, Ψ_t → Ψ_0 = c̃, so q(r) → c.
8. In case (FC1), σ fixes each point r of Ψ. Then σ induces an automorphism of the curve at r that maps the component labelled y to the one labelled σy, by (K3) of the brief. So F_y(r) ≅ F_{σy}(r). ∎

**Consequences for MS11♭.**
- In a reflection-type rigid-twin failure that satisfies (a) and (b), alternative (FC1) produces a third anchored sheet Ψ of c̃. On Ψ the Φ-copy and the rigid copy have the **same** value function, so it is either in Φ or ≡ Y_0.
  - If it is in Φ, then x is Φ-persistent on Ψ, by round12_q7 Lemma 1.2 applied on Ψ. Then x survives the twist at c̃ in the Φ-sense, *provided* Ψ is reachable in the sheet graph from the x-carrying sheet. I could not prove that reachability.
- Alternative (FC2) is what happens in the model of §1. It gives a new **necessary condition** for a counterexample:
  - *(NC-Fix) V_t (t ≠ 0 small) contains a holomorphic curve of smooth curves with an automorphism exchanging the Y_0-subsurfaces Σ_x and Σ_y, and this curve tends to the boundary piece c as t → 0. On these curves F_x ≅ F_y.*
  - (NC-Fix) is not contradictory by itself. V_t is not totally geodesic, and nothing in (R1) and (R2) forbids V_t from meeting the σ-symmetric locus of M_g in a curve that degenerates into c. By the upper semicontinuity of fibre dimension, the analytic set closure(𝒱) ∩ (closure(M_g^σ) × Δ) may have fibre c at t = 0 and an interior curve at t ≠ 0.
- Hypothesis (a) is a genuine restriction. It fails, for example, if X_0 is non-reduced or contains S_1 together with other sheets at p. So Lemma FC covers only part of (R-a), and **this section is partial by the task's own criteria**.

## 3. Chain check
- I re-read the chain steps 1, 2(a)–(d) as stated in the brief. Within the scope of what I read I found no new flaw.
- The logical dependence is unchanged.
  - Step 1 uses (Rig) (entry 82), which is open and does not follow from MS11♭. So even a full proof of MS11♭ would leave (Rig) open, and the problem would still not be settled.
  - The Φ-version of the chain (round12_q7 §3) still has the unchecked substitutions: Lemma PT, Lemma J / Cor. J′, and the transfer along D^{m+1}. I did not check them.
- The model of §1 is local at a generic point of a piece. So it is **not** a counterexample to MS11♭: MS11♭ concerns a puncture Q with conditions (P) and (S), and the global hypotheses (total geodesy, smoothness of V_0, Y non-constant). It shows only that the rigid-twin twist can occur in the middle of a piece, and so must be excluded by global arguments if it is to be excluded at all.
- Remark (orientation only, not proved). The monodromy picture of §1.1 explains why the orbifold reading (R2^orb) helps. A failure needs the swap monodromy of a coarse loop around c to be realised, at time t, by an interior orbifold point, i.e. alternative (FC2). Under the coarse reading (R2) nothing forbids this. That is consistent with the brief's record that MS11♭ holds under (R2^orb) but is open under (R2).

## 4. Proved / not proved / open

**Proved:**
- §1: an explicit chart-level model in which the reflection case (R-a) and the rigid-twin (β)-edge occur near a generic point of c, compatible with (R1) and (R2) in the chart.
  - Hence step 3 of the planner's sketch, as a local mechanism, is false.
  - The model leaves open whether its t = 0 sheet can be totally geodesic.
- §2, Lemma FC (under hypotheses (a), (b)): the dichotomy (FC1) / (FC2), and the necessary condition (NC-Fix) for reflection-type failures in case (FC2).

**Not proved:**
- MS11♭ in general, or even in the reflection case (R-a).
- The reachability in the sheet graph of the σ-fixed sheet Ψ in case (FC1).
- The Φ-chain substitutions (unchanged from round12_q7).

**Open (named):**
- (R-a) as a global statement. One must exclude, using total geodesy of V_0 or the global walk, a reflection σ ∈ Stab_pt(c̃) together with a rigid twin. By §1, no argument local along c can do this.
- Whether a totally geodesic S can have the shape of §1 at t = 0: a reflection w ↦ −w with z_x − z_y vanishing to first order on c̃.
- (NC-Fix): can a smooth totally geodesic V_0 admit a deformation satisfying (R1) and (R2) in which interior σ-symmetric curves of V_t degenerate onto c? A negative answer, or exclusion of (FC2) by any means, together with the reachability needed in (FC1), would settle (R-a) under hypothesis (a).
- (Rig) (entry 82), as before.


### round13_q7 (verbatim)
# round13_q7 — answer

**Plan/status.** (1) I re-derive "MS11♭ + (Rig) ⇒ claim" step by step from the listed statements. (2) I attack MS11♭. My first move is not in the tried table: *degenerate the Teichmüller discs of V_0 near Q on the two sides β̃, b̃ of the t = 0 sheet S (area functions of labels).* I combine it with a reformulation of the failure as a choice of lift of the coarse branch b.
Status: (1) done, modulo the cited entries. (2) partial: one reformulation and one t = 0 lemma are proved, and I explain exactly why this move cannot close MS11♭. MS11♭ remains OPEN.

Readings used throughout: (R1) and (R2) as stated in the query, with H_0 = id. The orbifold reading (R2^orb) is **not** used.

---

## 1. Derivation: MS11♭ + (Rig) ⇒ the problem's claim

**Step 0 (trivial case).** If dim M_{g_i,n_i} = 0, then (g_i,n_i) = (0,3) and M_{0,3} is a point, so Y_t = Y_0 trivially. From here on, dim M_{g_i,n_i} > 0, which is the setting of MS11♭.

**Step 1 (holomorphy).** By entries 2/19, t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}. So either Y ≡ Y_0, or Y_t ≠ Y_0 for all t outside a discrete set. Suppose, for contradiction, that Y is non-constant. Then every hypothesis of MS11♭ that concerns the family holds: (R1), (R2), (Rig) (assumed), product type of Δ_Γ, dim ∂V_t = 1, and Y non-constant.

**Step 2 (the walk chain at t = 0).** By Prop. K_w with repairs (entries 85, 98), a Teichmüller ray in V_0 from a generic point of ∂V_0 gives a finite walk chain:
- pieces E^0 = ∂V_0, E^1, …, E^m;
- transition points Q^1, …, Q^m, each with an entering lift β̃^k and a leaving lift b̃^k (or a terminal lift);
- the label x tracked by the walk;
- an endpoint of type MERGE or MOV.

Lemma S̃′ (entry 98) puts the entering and leaving lifts of each transition in one irreducible component of q^{-1}(closure V_0) ∩ B. This is hypothesis (S) of MS11♭. Cor. IMOV_all (entry 99) makes every genuine transition and the endpoint a puncture of both adjacent pieces. This is hypothesis (P), and it excludes interior-MOV endpoints, so the endpoint is a MERGE or a puncture-MOV.

**Step 3 (base).** On ∂V_0 the constant vertex i is intact with value Y_0. By (R2) and entry 24, H_t carries ∂V_0 to ∂V_t, on which vertex i has value Y_t. Hence vertex i, read as a label x in the chart at Q^1, is Y-persistent on an anchored sheet of the entering lift β̃^1. Anchored sheets exist by entry 112 (Lemma B1♭).

**Step 4 (induction over transitions).** Suppose x is Y-persistent on an anchored sheet of β̃^k.
- If Q^k lies in a non-product stratum, MS11♭ applies with data (Q^k, β̃^k, b̃^k, x). Its hypotheses (P) and (S) come from Step 2. Its conclusion is that x is Y-persistent on an anchored sheet of b̃^k.
- If Q^k lies in a product-type stratum, Lemma PT (entry 86) says no automorphism moves a positive-dimensional vertex. So there are no twins, the label is unambiguous, and the product-type junction step of entry 113 gives persistence on an anchored sheet of b̃^k. That step uses entries 84–87 and Theorem X′.
- Along a piece between transitions, persistence is constant on whole components of the boundary total space (Lemmas T/S, entry 87). By B1♭ (entry 112), adding the finite sets R(D) keeps the label on one lifted curve. So x is Y-persistent on an anchored sheet of the entering lift β̃^{k+1}.

This is exactly entry 113's chain check, which says MS11♭ supplies steps 2(b)–(d).

**Step 5 (endpoint).** By induction, the track is aligned at every junction, and the endpoint is a MERGE or puncture-MOV of the persistent label x. Theorem R (entry 87) then gives Y_t ≡ Y_0, contradicting Step 1. Hence Y ≡ Y_0.

**Verdict on part 1.**
- The derivation goes through as a formal combination of the listed statements. I could not re-check the proofs of entries 85/98 (walk chain), 87 (Theorem R) and 113 (chain check), since they are not supplied. The derivation is only as sound as those entries.
- MS11♭ is **not implausible in itself**. Its hypothesis contains "Y non-constant", so under (Rig) it is vacuously true if the problem's claim is true (entry 122). Any refutation of MS11♭ would be a counterexample to the problem. Its plausibility is therefore exactly that of the problem's claim.
- The full proof of the claim also needs (Rig) (entry 82), which is still OPEN under the coarse reading (R2).

---

## 2. Attack on MS11♭

**First move (new): degenerate the Teichmüller discs of V_0 near Q on the two sides β̃ and b̃ of the t = 0 sheet S, and compare which labels carry zero limiting area on each side.** Before using it, §2.1 pins down exactly what a failure of MS11♭ looks like.

### 2.1 Lift-curve reformulation (proved from entries 112 and 114)

**Conventions.**
- Aut(Q) acts on Def(Q) and on the labels.
- The stable curve over h·p is identified with the curve over p, with the component labelled hy over h·p corresponding to the component y over p. So F_{hy}(h·p) ≅ F_y(p).

**Lemma 2.1.** Assume the MS11♭ setting with Y non-constant. Let T be an anchored sheet of β̃ on which x is Y-persistent. Let L ⊂ T be a lift-curve of Q_t, and set Λ := Λ(L), the set of labels y with F_y ≅ Y_t along L. Then:

(a) Every lift-curve of Q_t is h·L for some h ∈ Aut(Q). Moreover Λ(hL) = hΛ.

(b) For every h ∈ Aut(Q) and every lifted branch c̃: h maps the anchored sheets of c̃ bijectively onto the anchored sheets of hc̃, and P(hT″) = hP(T″).

(c) x ∈ Λ. Every anchored sheet T′ of b̃ contains some lift-curve hL, and P(T′) = hΛ.

(d) MS11♭ holds at this datum ⇔ there is an anchored sheet T′ ⊇ hL of b̃ with h^{-1}x ∈ Λ.
- In every case, x is Y-persistent on the anchored sheet h^{-1}T′ of the lift h^{-1}b̃ of the same coarse branch b.
- So a failure means precisely this: the lift of b that carries x is h^{-1}b̃, not the lift b̃ that lies in S together with β̃.

*Proof.*

(a)
- q is the quotient by Aut(Q), so q^{-1}(Q_t) = Aut(Q)·(L ∩ {t}).
- Hence ⋃_h hL is the whole analytic set {(p,t) : q(p) = Q_t}.
- Its irreducible components are the irreducible curves hL. This gives the first claim.
- The second claim follows from F_{hy}(hp) ≅ F_y(p).

(b)
- B is Aut(Q)-invariant and q∘h = q.
- So h preserves q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε), and it sends the connected component containing c̃ ∖ 0 to the one containing hc̃ ∖ 0. Thus hÑ_{c̃} = Ñ_{hc̃}.
- Closures, irreducible components, and the condition "⊇ c̃ × {0}" are transported by h.
- Persistence is transported by the label convention.

(c)
- By (P), Q is not in the stratum of the piece of β or of b. So all anchored sheets of β̃ and b̃ are of boundary type.
- Entry 114 gives: every transport sheet contains a lift-curve, and P = Λ(λ) for any lift-curve λ in a boundary-type sheet.
- With (a), this gives P(T) = Λ, hence x ∈ Λ, and P(T′) = hΛ.

(d)
- By (c), x ∈ P(T′) ⇔ h^{-1}x ∈ Λ. This is the stated equivalence.
- For the second claim: by (b), h^{-1}T′ is an anchored sheet of h^{-1}b̃ that contains L.
- By (c), P(h^{-1}T′) = Λ ∋ x. ∎

**Corollary 2.2 (t = 0 trace of non-constancy).** Under the hypotheses of Lemma 2.1, at t = 0 the labels in hΛ (with hL ⊂ T′ as above, so hΛ ≠ ∅) are intact along b̃ with constant value Y_0.

So whenever Y is non-constant, *some* Y_0-copy stays intact and constant along b̃ at t = 0. A failure of MS11♭ forces x ∉ hΛ, so this copy is a label y = hx″ ≠ x with x″ ∈ Λ, i.e. a twin of a Y_t-label.

*Proof.* Persistence at (p, 0), p ∈ b̃, means that y is intact and F_y(p) ≅ Y_0. ∎

### 2.2 The first move: Teichmüller-disc degeneration at t = 0

**Set-up.**
- For p ∈ S ∖ {N = 0} (lifted points of V_0) and a unit vector v ∈ T_pS, let q_{p,v} be the unit-area norming differential of the Teichmüller disc of V_0 through (p, v). This exists because V_0 is totally geodesic.
- For a label y, let A_y(p, v) be the q_{p,v}-area of the thick region of the plumbing chart belonging to y.

**Lemma 2.3 (area on the two sides; consequence of Lemma PA, entry 45, read in the chart).** Let c̃ ∈ {β̃, b̃}. If a label y is intact along c̃ with π_y constant on the piece of c, then A_y(p, v) → 0 as p → a generic point of c̃, uniformly in v. Some label intact along c̃ has positive limiting area.

So, by the hypothesis on x and by Corollary 2.2:
- on the β̃ side, x has zero limiting area;
- under Y non-constant, on the b̃ side, the labels of hΛ have zero limiting area.

S ∖ {N = 0} is connected, since it is an irreducible germ minus a proper analytic subset. So the normalised flat structures can be followed continuously from the β̃ side to the b̃ side.

**Why this move cannot close MS11♭ (proved no-go).**

**Lemma 2.4 (NG).** Let (Q, β̃, b̃, x) be any t = 0 datum satisfying all t = 0 conditions of MS11♭ (closure(V_0), Q non-product, (P), (S)), with x intact and ≡ Y_0 along β̃, but with x not intact and constant along b̃. Then the trivial family V_t ≡ V_0 (H = id) satisfies:
- (R1), (R2), (i), (ii);
- (Rig), with 𝒦 the finite set of pieces of V_0;
- the persistence hypothesis on β̃;
and it violates the conclusion of MS11♭. Only "Y non-constant" fails.

*Proof.*
- For the trivial family, Ñ_{c̃} = (c̃ ∖ 0) × Δ_ε. Distinct lifted branches meet only at 0, and c̃ ∖ 0 is a punctured disc, hence connected.
- So the unique anchored sheet of c̃ is c̃ × Δ_ε. Then x is Y-persistent on it iff x is intact along c̃ with F_x ≡ Y_0.
- (Rig) holds because closure(V_0) meets each of the finitely many strata in finitely many components.
- By assumption, the persistence hypothesis holds on β̃ and the conclusion fails on b̃. ∎

Such t = 0 data exist at the terminal transition of any walk chain whose endpoint lies in a non-product stratum:
- Lemma S̃′ (entry 98) gives the common component.
- Entry 99 gives (P).
- At a MERGE endpoint, x is not intact along the terminal lift. At a puncture-MOV endpoint, F_x is non-constant along it.

**Consequences.**
1. Any proof of MS11♭ must use "Y non-constant" essentially, even for the t = 0 part of its conclusion ("x intact along b̃ with F_x ≡ Y_0").
2. Lemma 2.3, and any argument that uses only the totally geodesic geometry of closure(V_0) at Q, involves only data that the trivial family shares. Such an argument therefore cannot prove MS11♭: it would prove the t = 0 statement that Lemma 2.4 refutes at terminal transitions.
3. The Teichmüller-disc move can contribute only as a supplement to a t ≠ 0 argument. Specifically, it would have to show the following:

   (★) at t = 0, a label of zero limiting area on the β̃ side that is Y_0-twinned (via h ∈ G_X) with a zero-area label on the b̃ side must be that same label.

   That (★) is false in general is again shown by terminal MERGE data: there x has zero area on the β̃ side, merges on the b̃ side, and other Y_0-copies may stay. So the move gives no new constraint on its own.

### 2.3 What would close the gap

By Lemma 2.1(d), MS11♭ at a datum is equivalent to **(Lift)**: the lift-curve hL contained in an anchored sheet of b̃ can be chosen with h^{-1}x ∈ Λ(L).

By entries 114 and 129, (Lift) is automatic if Q_t has a single lift-curve in X (that is, G_X ⊆ Stab(L)). The residual case is the rigid-twin configuration (NRT), entry 137:
- at Q_t, x ≅ Y_t;
- a twin x′ = h^{-1}-related to x is frozen at Y_0;
- the two are exchanged at t = 0 by an automorphism of Q that is lost for t ≠ 0.

My attempt gives nothing beyond Corollary 2.2 against (NRT). Under (NRT) the twin y on b̃ in Corollary 2.2 is exactly the image of the Y_t-label, and x on b̃ is either merging, moving, or frozen. In all three cases every t = 0 condition is met: Lemma 2.4 for the first two, and for the third the t = 0 picture is identical to the non-failing one.

---

## 3. Summary lists

**Proved here** (modulo the cited ledger entries):
- §1: the step-by-step derivation that MS11♭ + (Rig) + entries 2/19, 24, 45, 85–87, 98, 99, 112–114 imply the claim, including the trivial case dim M_{g_i,n_i} = 0.
- Lemma 2.1: the lift-curve reformulation of MS11♭ as (Lift). A failure means that the lift of the coarse branch b carrying x is h^{-1}b̃ ≠ b̃.
- Corollary 2.2: under Y non-constant, some Y_0-copy stays intact and constant along b̃ at t = 0.
- Lemma 2.3: zero-area labels on both sides (a reading of Lemma PA).
- Lemma 2.4 (NG): the trivial family satisfies every hypothesis of MS11♭ except "Y non-constant" and violates its conclusion at any terminal-transition datum in a non-product stratum. So t = 0-only arguments, including Teichmüller-disc degeneration, cannot prove MS11♭, not even its t = 0 part.

**Not proved:**
- MS11♭ itself.
- The rigid-twin exclusion (NRT).
- (★), which is false as a t = 0 statement.

**Open:**
- MS11♭ (entry 124), equivalently (NRT) (entry 137), equivalently (under (Rig)) the problem's claim.
- (Rig) under the coarse reading (R2) (entry 82).
- Whether walk-chain endpoints in non-product strata actually occur for some totally geodesic V_0. This is only relevant to how sharp Lemma 2.4 is.


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



### round9_q5 (verbatim excerpt: §0 setting and §2 Lemma TG)
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


## Reminder
Prove (NRT_P) exactly as stated, or give an explicit counterexample. A proof of the statement for only some of the cases it covers — a sub-class of its objects or a sub-range of its parameters — does not answer the question, though it should be reported if it is all that was found. End with: proved / not proved / open.
