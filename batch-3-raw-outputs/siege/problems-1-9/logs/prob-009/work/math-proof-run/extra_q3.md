kind: write-up (consolidation into a complete, self-contained proof)

## Task
A research document on the problem stated below records, besides a conditional theorem, an exact REDUCTION of the problem under the coarse reading:

**Theorem B (reduction).** Assume the problem's hypotheses, read as (R1), (R2) (coarse reading: H a stratum-preserving homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, H_0 = id; no preservation of automorphism groups), with Δ_Γ of product type and dim M_{g_i,n_i} > 0. Assume moreover (Rig) and (NRT_P) (both stated in the spliced material). Then Y_t = Y_0 for all t ∈ Δ. Moreover, under (Rig), (NRT_P) is implied by the problem's conclusion (it contains "Y non-constant" as a hypothesis), so a counterexample to (NRT_P) is a counterexample to the problem.

Its proof ("the Φ-chain") was found and refereed in earlier analyses; the material is spliced verbatim below: the derivation (round13_q5), its referee report with repairs (R-i)–(R-v), and the inputs (I1)–(I6) it uses.

Your job: write ONE coherent Markdown text "Part III" giving a complete, self-contained proof of Theorem B, in consistent notation, with all repairs incorporated, so that a referee who sees ONLY your text, the problem statement, and the black-box statements listed below can check every step. Rules:
- You may take as given ONLY: (a) the black-box results listed below (written up separately with full proofs; quote them by label and state precisely the form you use); (b) classical theorems, cited explicitly with precise statements. Everything else — Lemma 1 (values along a lift-curve: Φ or rigid), Lemma 2 ((NRT) ⇔ C_Φ(L) Aut(Q)-invariant), Lemma 3 (P_Φ(T) = C_Φ(L)), Proposition 4, Lemma 5 (Φ-transfer), the Φ-version of the generic-time trichotomy (I5) (derive it from the black-box Theorem 1 by the substitution Y ↦ φ, including multivalued Puiseux branches as in repair (R-ii)), (I1) lift-curves form one Aut(Q)-orbit, (I2) every anchored sheet contains a lift-curve, (I3) C(aL) = aC(L) and aT anchored sheet of ac̃, the induction along the walk chain and the endpoint — must be proved in your text.
- The "marking identification x_m ↔ c ↔ x_{m+1}" along travel intervals has never been written out in the material; if your proof needs it beyond the black-box statement BB1, mark it "GAP:" precisely.
- Do not refer to the spliced analyses by name; write each argument out. Mark any step you cannot complete with "GAP:".
- Also state (Rig), (NRT_P), Φ, C_Φ(L), puncture point, lift-curve, anchored sheet, persistence precisely, and explain briefly why a failure of (NRT_P) forces an isotropy drop |Aut(Q_t)| < |Aut(Q)|.

## Black-box results (taken as given; statements only)
- BB1 (walk chain; t = 0 geometry of V_0): from a generic point of ∂V_0 there are pieces D^1 ⊂ ∂V_0, D^2, …, D^k of closure(V_0), transition points J_1, …, J_{k−1} and an endpoint Q_0; at J_m an entering lift β̃_m (of a branch of D^m) and a leaving lift β̃′_m (of a branch of D^{m+1}) in a chart Def(J_m) with common chart label x_m, both in one irreducible component of q^{-1}(closure V_0) ∩ B; along each travel interval the tracked label is a constant vertex c of the piece with value ≅ Y_0, and the chart labels correspond to c at both ends (marking identification x_m ↔ c ↔ x_{m+1}); at Q_0 an entering lift β̃ (label x) and terminal lift b̃ in one such component, x MERGE or MOV along b̃ at t = 0. Corollary IMOV_all: a transition point lying in the stratum of either adjacent piece has β̃′_m = β̃_m with the same label; Q_0 and every genuine transition satisfy (P) (puncture of both adjacent pieces). Lemma PT (product-type strata: no automorphism moves a positive-dimensional vertex).
- BB2 (holomorphy, coarse): under (R1), (R2), t ↦ Y_t ∈ M_{g_i,n_i} is holomorphic.
- BB3 (Lemma U, coarse, under (Rig)): each 2-dimensional component W of each lifted boundary family 𝒲_G ⊂ ∏_w M̄_w × Δ has one moving set M_W and one image curve K_W for all components of all fibres at all times; every fibre component is K_W × {c_D}; F_W = K_W ∩ ∂ is finite and t-independent; the constant-vertex value curves Γ_{W,u} are irreducible curves finite over Δ.
- BB4 (generic-time trichotomy, Theorem 1, coarse, under (Rig), Y non-constant): as in the spliced R8-2 §3.
- BB5 (Theorem N and its Lemma 1, coarse): as in the spliced R8-3.
- BB6 (transport families, coarse): closure(Ñ_c̃) is analytic of pure dimension 2, contained in Ñ_c̃ ∪ 𝒥 near (0,0); Lemma B1♭ (anchored sheets exist, contain every germ component of the transport family at a generic point of c̃, form one orbit of the pointwise stabiliser of c̃); the base step (vertex i persistent on every sheet of every lift of a branch of D^1) and the product-type junction step (Lemma J / Cor. J′), and the product-type endpoint (Lemma J (J1) / Theorem R) — as in the spliced chain check.

Output format: a single Markdown document headed "Part III", with numbered conventions, statements and proofs, ending with "Proof of Theorem B", then "Cited classical facts" and "GAPs" (possibly empty). Up to about 15,000 words. Begin with a one-paragraph status line.

## Spliced material (verbatim; bookkeeping lines removed)
## The statement (NRT_P) (verbatim from the run's summary)
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

## The chain as it previously stood (round13_q5's input (I6) refers to this skeleton)
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


## round13_q5 (verbatim) — the derivation to be checked
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


## Inputs (verbatim prior results; bookkeeping lines removed)

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




### Referee report on the derivation (verbatim)
# round14_q8 — check of round13_q5 ((NRT_P) ⇒ MS8)

**Plan/status.** I checked round13_q5 step by step against the spliced inputs: Lemma 1, Lemma 2, Lemma 3, Prop. 4, §4 (base, interior transitions, puncture transitions, Lemma 5, endpoint) and §5.

**Verdict in one line.** CORRECT after five minor repairs (R-i)–(R-v) below. None of the repairs changes a statement; they only make explicit points that were implicit. round13_q5 proves:
- (NRT_P) + (R1), (R2) (with H_0 = id) + (Rig) + "Y non-constant" ⇒ contradiction;
- hence (NRT_P) ⇒ MS8;

modulo the cited inputs (I1)–(I6), entry 19, and the inherited marking identification (round11_q9 §2.4, "routine", not re-derived by anyone). (NRT) is used only at puncture points, so it may be read as (NRT_P).

Readings throughout: (R1), (R2) with H_0 = id, (Rig), and the definitions of the task file. [Z] is the class in 𝔐 = M_{g_i,n_i}/S_{n_i}.

---

## 0. The cited inputs: located and checked against their use

- **(I1)** Located: round11_q4 §2 (notation) and round12_q6 Lemma G1(a).
  - G1(a) says exactly what is used: Λ = ⋃_{g∈A} gL_0 near (0,0), i.e. the lift-curves form one Aut(Q)-orbit, and Λ ∩ {t=0} = {(0,0)} because q^{-1}(Q) = {0}.
  - Its proof is valid. Λ is the preimage of the irreducible germ {(Q_t,t)} under the finite quotient q × id, and t|_{L_0} is finite.
  - "Every label is intact on Λ" is also valid. Q_t ∈ Δ_{G_Q} because H preserves strata, and the points of Def(Q) over Δ_{G_Q} are exactly {s_e = 0 for all e}.
- **(I2)** Located: round11_q4 Lemma 2.1 (stated for sheets as germs at (0,0), which covers anchored sheets).
  - Proof re-checked. Σ_c is irreducible: its dense part H((c∖Q)×Δ) is a connected 4-manifold and the rest has real codimension 2. Then (q×id)(T) = Σ_c by Remmert, so T ∩ Λ surjects onto a t-neighbourhood of 0 and contains a lift-curve.
  - One point is implicit there: the points of T ∩ Λ tend to (0,0) as t → 0. This holds after shrinking ε relative to B, because q^{-1}(Q) = {0}. Valid.
- **(I3)** Located: round12_q1 Lemma F. Lemma F is stated under a c̃ = c̃, but the two facts round13_q5 needs do not use that hypothesis.
  - **C(aL) = aC(L).** Lemma F(4) uses only (K3) and the Aut(Q)-invariance of Λ. Its Φ-version C_Φ(aL) = aC_Φ(L) is the same computation.
  - **aT is an anchored sheet of ac̃.** In the proof of F(1), aÑ_c̃ is the connected component of the a-invariant set q^{-1}(H((c∖Q)×Δ_ε)) ∩ (B×Δ_ε) that contains a(c̃∖0), so aÑ_c̃ = Ñ_{ac̃}. Then a maps closure(Ñ_c̃) to closure(Ñ_{ac̃}) component by component, and aT ⊃ ac̃ × {0}.
  - Moreover ac̃ is a lift of the same coarse branch c. So aT is again of boundary type. Valid.
- **(I4)** Located: R8-2 Lemma U, U1, U3, U4, and the proof of round12_q7 Lemma 1.2.
  - They say what is used: each fibre component of W_t is K_W × {c_D} with c_D ∈ ∏_{w∉M_W} M_w; F_W = K_W ∩ ∂ is finite and t-independent; Γ_{W,u} is an irreducible curve, finite over Δ.
  - See (R-i) for a strengthening of "dense open subset of T ↦ W".
- **(I5)** Located: round12_q7 Lemma 1.1. It is stated exactly as used. Its proof is R8-2 Theorem 1 with Y replaced by φ. See (R-ii) for multivalued branches.
- **(I6)** Located: round11_q9.
  - Walk chain: §1.1, S̃′.
  - Interior transitions and R(D)-points are trivial: §1.2.
  - Genuine transitions satisfy (P), as the contrapositive of IMOV_all(a), §1.2. So J_m is a puncture of **both** D^m and D^{m+1}.
  - (P) at the endpoint (Q_0 a puncture of D^k and of E_b): §1.2.
  - B1♭(a″): §2.3. The §2.7 transfer set-up: 𝒲̃ with 𝒲̃_0 ⊃ E, and Π(Ñ″^1) ⊂ 𝒲̃.
  - The marking identification x_m ↔ c ↔ x_{m+1}: §2.4. It is accepted there as "routine, inherited" and I did not re-derive it.
  - Side remark (an identification of definitions): a c̃-sheet (its t=0 slice contains an open subset of c̃∖0) is the same as an anchored sheet. The sheet is closed and c̃ ∩ B is irreducible, so the sheet contains c̃ × {0}. The converse is clear. So B1♭(a″) supplies anchored sheets.

---

## 1. Lemma 1 — CORRECT (with repair (R-i))

**Step 1.** L is an irreducible curve germ and y is intact on L (I1). F_y is holomorphic on the locus L_y where y is intact, so λ_y is holomorphic. t|_L is finite, so the image is an irreducible 1-dimensional germ at (Y_0,0). Valid.

**Step 2.** Brief's points: limits κ_n → κ_∞ ∈ F_W; continuity of ξ̄; use of Q_t ∉ Δ_{G_c}. All are valid, once the following is made explicit.

- **(R-i) Π is defined and continuous on all of T, and (Π,t)(T) ⊂ W.** Let S be the generic pattern of T (the pattern of c̃). By closedness, T ⊂ {s_e = 0 for all e ∈ S}, which is the domain of the continuous map Π = Π_S into ∏M̄_w. Since W is closed and (I4) gives a dense open subset of T mapping into W, we get (Π,t)(T) ⊂ W.
- So there is no need to know whether the p_n lie in "the" dense open set. In fact Π(p_*) = lim Π(p_n) directly.
- **Choice of fibre component.** W_t may have several components K_W × {c_D}. Pass to a subsequence lying in one of them. "c_t" in the text should be read as this c_D.
- **Why κ_∞ is in the boundary.** ξ̄_G : ∏M̄_w → M̄_g is the continuous gluing morphism, and ξ̄∘Π = q on the closure. So ξ̄(κ_∞, c_D) = q(p_*) = Q_t.
  - Q ∉ Δ_{G_c} by boundary type, and H_t preserves strata. So Q_t ∉ Δ_{G_c} = ξ(∏M_w).
  - c_D has interior coordinates, so κ_∞ ∈ ∂. Hence κ_∞ ∈ F_W. Correct.
- **The components of Q_t.** Every component of the glued curve ξ̄(κ_∞,c_D), with its special points, is either some c_D[w] (w ∉ M_W) or a component of a coordinate of κ_∞. Gluing turns marked points into nodes and leaves the set of special points of a component unchanged, as in R8-3 Lemma 1 (⊇). F_y(p_*) is a component of q(p_*) = Q_t. So the dichotomy (a)/(b) holds.

**Step 3.**
- 𝒢 is closed analytic: it is a finite union of the curves Γ_{W,w} (images under proper maps, contained in M_w × Δ, mapped to 𝔐) and of finitely many lines {f} × Δ.
- Only vertices w of type (g_i,n_i) matter, because the type of F_y is constant along L.
- The image germ minus the origin lies in 𝒢, and 𝒢 is closed. So the image germ lies in one irreducible branch of 𝒢 through (Y_0,0).
- A non-constant such branch belongs to Φ, since Φ ranges over all components of all 𝒲_G. Otherwise the image germ is {Y_0} × Δ.
- The image germ is irreducible and 1-dimensional, so "contained in φ" means "equal to φ". Valid.

---

## 2. Lemma 2 — CORRECT

- A boundary-type anchored sheet exists at every puncture point (B1♭(a″)). By (I2) it contains a lift-curve L_1. By (I1) and (I3), every lift-curve aL_1 lies in the boundary-type sheet aT. So Lemma 1 applies to every lift-curve.
- **(⇒).** The step F_{a^{-1}x}(0) ≅ F_x(a·0) = F_x(0) ≅ Y_0 is valid: (I3) with p = 0, and F_x(0) ≅ Y_0 because φ(0) = Y_0.
  - By Lemma 1, a^{-1}x is either in C_Φ(L) or rigid along L. The rigid case is literally the configuration excluded by (NRT_P), with Q a puncture point.
  - The case a^{-1}x = x is trivial. A label cannot be both on a non-constant branch and ≡ Y_0.
  - Invariance under Aut(Q) then gives C_Φ(aL) = aC_Φ(L) = C_Φ(L).
- **(⇐).** Valid.
- "Puncture point" (some branch c with c∖Q in a stratum other than Δ_{G_Q}) is equivalent to "Q ∉ Δ_{G_c}", i.e. to boundary type. Valid.

---

## 3. Lemma 3 — CORRECT (with repairs (R-ii), (R-iii))

**(⊂).** Restrict to L ⊂ T.

**(⊃), analyticity.** A_y is a closed analytic subset of T: L_y is closed analytic, F_y is holomorphic on it, and Γ is a finite union of closed analytic curves.

**(⊃), the generic slice.**
- q(T) ⊂ closure H((c∖Q)×Δ), which equals H(c×Δ) near Q. So T_t ⊂ q^{-1}(c_t), where c_t = H_t(c) is one irreducible branch at Q_t (a disc).
- T_t is 1-dimensional at p, since t ≢ 0 on the irreducible 2-dimensional T. So every branch of T_t at p is a lifted branch of c_t.
- Q_t ∉ Δ_{G_c} ⊃ c_t ∖ Q_t, so Q_t is a puncture of the piece. IMOV requires Q ∈ Δ_{G_b}, so IMOV is excluded and (I5) gives STAY.
- So y is intact with constant value [F_y(p)], and ([F_y(p)],t) ∈ φ ⊂ Γ. Hence A_y contains the germ of T_t at p.

**(R-ii) Multivalued branches.** A branch φ ∈ Φ may be a Puiseux branch of degree > 1, so "φ(t)" is multivalued.
- Read "φ(t)-copy" as "class equal to a point of φ over t".
- Read Z_φ as the set of t such that some point of φ over t lies in 𝔉, or lies on a value curve that does not contain the germ φ, or lies on another φ′ ∈ Φ. Each irreducible value curve either contains φ or meets it only at the origin after shrinking, so Z_φ is still discrete.
- With this reading the proof of R8-2 Theorem 1 goes through unchanged: steps 1, 2, 4 use the value ∉ 𝔉, and step 3 uses that Γ_{W,y} ∋ (value, t) forces Γ_{W,y} ⊃ φ. So (I5) holds as used.

**The countability argument.** If dim A_y ≤ 1, a 1-dimensional slice A_y ∩ {t = t_0} means that some 1-dimensional component of A_y lies in {t = t_0}. There are countably many components, each in at most one level. Valid.

**(R-iii) Germ conventions.** To conclude A_y = T from dim A_y = 2, use a representative of the irreducible germ T on a small neighbourhood U on which T ∩ U is irreducible; such U exist for an irreducible germ (local parametrisation). The uncountably many slices occur inside every such U, because L reaches every small t. So A_y ∩ U = T ∩ U.

**Single branch.** The preimages of the finitely many branches of Γ at (Y_0,0) are analytic germs covering the irreducible germ T, so one of them is T. That branch contains the image of L, which is the 1-dimensional germ φ, so it equals φ. Valid.

---

## 4. Proposition 4 — CORRECT

- The first part is Lemma 3, then Lemma 2 at Q (which has the boundary-type sheet T), then Lemma 3 again.
- **Last clause.** ψ is a branch of a curve finite over Δ, so a representative meets {t=0} only in (Y_0,0). [F_x] is continuous on c̃′ and lies on ψ, so [F_x] ≡ Y_0 on c̃′ near 0.
- Moreover x is intact on all of c̃′ ∩ B, because c̃′ × {0} ⊂ T′. This clause uses only x ∈ P_Φ(T′), **not** (NRT). That matters for Lemma 5, where it is applied with T′ = T.

---

## 5. §4, the induction — CORRECT (with repairs (R-iv), (R-v))

- **Base.**
  - Vertex i is constant on the pieces of ∂V_t in Δ_Γ, so i ∉ M_W.
  - Γ_{W,i} is the graph of the holomorphic, non-constant Y (entry 19), so Y ∈ Φ.
  - Y-persistence is Φ-persistence with φ = Y (round11_q9 §2.5 gives it on every sheet). Anchored sheets of β̃_1 exist (B1♭(a″)). Valid.
- **Interior and R(D) transitions.** (I6) gives β̃′_m = β̃_m with the same label. So a sheet of one is a sheet of the other. Valid.
- **(R-iv) Puncture transitions.** Step 3 says "J_m is a puncture of D^m and of D^{m+1}" for every transition, "β̃′_m ≠ β̃_m or not". That is not justified for a non-genuine transition lying in the stratum of D^m or of D^{m+1}. Repair: split the transitions.
  - (a) J_m lies in the stratum of D^m or of D^{m+1}. Then β̃′_m = β̃_m (entry 99), and step 2 applies.
  - (b) Otherwise J_m is a puncture of both. Then Prop. 4 applies at the puncture point J_m, whether or not β̃′_m = β̃_m.
  
  The two cases are exhaustive, so nothing is lost.
- **Lemma 5.** Brief's points: the identification x_{m+1} ↔ c, the value of x_m on β̃′_m, and "every branch of Γ is non-constant".
  - **Value of x_m on β̃′_m.** By the last clause of Prop. 4 with T′ = T (no NRT needed), x_m is intact with [F] ≡ Y_0 along β̃′_m. Intactness makes c = {x_m} a single vertex of G_S, whose coordinate is F_{x_m}. It is constant on the open arc Π(β̃′_m) ⊂ E, hence constant on the component E of 𝒲̃_0, and c ∉ M_𝒲̃ by U1. Valid.
  - **(R-v) What the step "Γ ⊃ φ" uses.** It uses the identification x_m ↔ c **at J_m**, as well as at J_{m+1}: on Ñ′^1, F_{x_m} is the c-coordinate of Π_S, which lies in Γ_{𝒲̃,c}. Both identifications are the inherited marking identification of round11_q9 §2.4/§2.7. Given that, x_m ∈ P_Φ(T) with function φ, and closedness gives φ ⊂ Γ := Γ_{𝒲̃,c}.
  - **Irreducibility of Γ.** 𝒲̃ is irreducible and (pr_c,t) is proper on it (𝒲 is proper over Δ), so Γ is irreducible. This must be read over the disc on which 𝒲̃ is irreducible; it is a global, not a germ, statement. The argument uses only that.
  - **No constant branch.** Suppose Γ had a constant branch at (Y_0,0). Then Γ ∩ ({Y_0}×Δ) would be a 1-dimensional analytic subset of the irreducible 1-dimensional Γ, hence all of Γ. That contradicts Γ ⊃ φ with φ non-constant.
  - **So every branch of Γ at (Y_0,0) lies in Φ.** The vertex c has type (g_i,n_i), and 𝒲̃ is a 2-dimensional component of some 𝒲_G. Valid.
  - **T″.** On Ñ″^1, x_{m+1} ↔ c is intact: c is a single vertex, the pattern is constant on Ñ″, and intactness is closed. Its value lies on Γ, and by continuity on all of T″.
  - The value at the origin is Y_0, as the limit along β̃_{m+1} ⊂ Π^{-1}(E) of c ≡ Y_0.
  - If the global T″ has a reducible germ at (0,0), take the germ component containing β̃_{m+1} × {0}; it is an anchored germ sheet.
  - The value map on that irreducible germ lands in a single branch ψ ∈ Φ. Valid.
- **Endpoint.**
  - (P) at Q_0 (I6) makes the anchored sheets of β̃ and of b̃ of boundary type. Q_0 is a puncture point.
  - Prop. 4 gives x intact on b̃ ∩ B and [F_x] ≡ Y_0 near 0. MERGE is contradicted at once.
  - **MOV.** b̃ ∩ B is irreducible in a Milnor ball, so its normalisation is a connected disc. [F_x] is a holomorphic map from it into the analytic space 𝔐 that is constant on an open set. By the identity theorem it is constant, so [F_x(z̃^∞)] = [Y_0], which contradicts MOV. Valid.
  - The case k = 1 (no transitions) is the same argument.
- **Only puncture points are used.** (NRT) enters only through Lemma 2, which is invoked only inside Prop. 4. Prop. 4 is used only at puncture transitions (case (b)) and at Q_0, which is a puncture point by (P). So "(NRT) at Q" may be read as (NRT_P). Confirmed.

---

## 6. §5 — consistent; not load-bearing

The reductions of (β)/initial twists, (γ°) and Lemma 4.1 to (NRT_P) configurations are consistent with Lemma 1 and (I1). They are not used in §4, so they need no check for the chain.

---

## 7. Verdict / repairs / remaining dependencies

**Verdict.** round13_q5 proves exactly the following: under (R1), (R2) with H_0 = id and (Rig), with V_0 smooth, closed and totally geodesic and Δ_Γ of product type, **(NRT_P) + "t ↦ Y_t non-constant" ⇒ contradiction**. Hence (NRT_P) ⇒ MS8, and with entry 19, Y_t = Y_0.

**Repairs** (all minor, all made above):
- **(R-i)** (Π,t)(T) ⊂ W on all of T, by continuity and closedness. Pass to a subsequence inside one fibre component K_W × {c_D}.
- **(R-ii)** Reading of φ(t) and Z_φ for multivalued Puiseux branches. (I5) holds in this reading.
- **(R-iii)** Germ-representative conventions in Lemma 3, and in Lemma 5 for T″.
- **(R-iv)** Step 3 is restricted to transitions where J_m is a puncture of both pieces; the others fall under step 2.
- **(R-v)** Lemma 5 uses the marking identification x_m ↔ c at J_m as well as at J_{m+1}, and the irreducibility of 𝒲̃ over the disc in use.

**Remaining dependencies.**
- Cited inputs, used as stated and not re-derived here:
  - (I1) round12_q6 G1(a);
  - (I2) round11_q4 L2.1;
  - (I3) round12_q1 Lemma F, proof;
  - (I4) R8-2 Lemma U/U1/U3/U4 and round12_q7 L1.2;
  - (I5) round12_q7 L1.1 / R8-2 Theorem 1;
  - (I6) round11_q9 §§1.2, 2.3–2.5, 2.7, 2.8, i.e. the walk chain with entries 85, 98, 99 and S̃′;
  - entry 19.
  
  I re-checked the proofs of (I1), (I2), (I3) and the Lemma U statements as spliced.
- The marking identification of round11_q9 §2.4: inherited as "routine" and never re-derived. It is used twice in Lemma 5.
- **Open:** (NRT_P) itself (entry 141).
- **Open:** (Rig) (entry 82). It is needed for the problem's conclusion in addition to MS8.
- The problem's hypotheses are used only through the readings (R1), (R2).

