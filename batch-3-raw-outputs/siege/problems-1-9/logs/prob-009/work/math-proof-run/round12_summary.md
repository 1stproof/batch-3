# Running summary after round 11 (written at round 12 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After eleven rounds (88 queries) there is no proof and no counterexample. Round 11 (10 queries, all screened OK; round11_q2 was re-run after an API error and its re-run answer is the one used) attacked MS11 (entry 109). It produced:
- **Gap C (four independent files: round11_q2, q3, q8, q9).** Lemma B1(a),(b) of round10_q3 (entry 100) are FALSE as stated. A component of closure(Ñ_b̃) may meet {t = 0} only in another lift a·b̃ (explicit chart-level models; the connection is through a-fixed points of the transported branch at t ≠ 0). Consequently MS11 as worded does NOT imply MS8 (the transfer step 2(c) and the non-product MOV endpoint 2(d) fail; round11_q9 §2.2 model 1). Repair: *anchored sheets* (round11_q2 "anchored", q3 "proper", q8 "based", q9 "c̃-sheet": an irreducible component of closure(Ñ_c̃) containing c̃ × {0}). With that reading the whole chain 2(b)–(d) was checked and is correct (round11_q9). MS11 is replaced by MS11♭.
- **Mechanism D made rigorous** (round11_q3, q7, q1, q2, q5, q8): Grothendieck connectedness for D = X ∩ {∏ s_e = 0} in a 3-fold component X ⊃ S × {0}; all D-sheets are anchored and of boundary type (q3 Lemma 3.1, via X*_all); labels pass along every edge except (β)-twist edges and (γ°)-edges (q3 Prop. 3.2, Lemma 3.3; q7 Theorem D). This reduces MS11♭ to a composite-twist condition. Local models show (β)-twists are realisable inside one X (q7 §6, q1 §5).
- **Lift-curve reformulation** (round11_q4 §2, q1 §2): persistence on a boundary-type sheet = the Y_t-copies along any lift-curve in it; so MS11♭ holds whenever the lifts of Q_t form a single lift-curve, e.g. when |Aut(Q_t)| = |Aut(Q)| (in particular under the orbifold reading (R2^orb)).
- **Twin-free closure and TFM** (round11_q4 §3): every reachable piece has a constant vertex ≡ Y; V_0-only sufficient criteria for the goal.
- **Rigid twin at the endpoint** (round11_q1 §4).
- (Rig) side: Lemma HQ, Prop. MP/MP′, Prop. DP (round11_q10); Douady rigid case, Lemma TR under (OT) (round11_q6). Logical status: under (Rig), MS11 ⇔ the problem (round11_q1 Prop. 1.1, q4 §1, q6 §2).

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, preserving every stratum, with H_0 = id (round2_q1, round3_q1). It is a Thom–Mather-type strengthening of the literal (i)/(ii); the final document must say so. It is the coarse reading: H_t need not preserve automorphism groups.
- The fixed index i is recovered by a Baire argument (round4_q5 §1).
- "Smooth" V_0: the quintic test surface is singular (round6_q3).
- (R2^orb)/(R2+) (H_t preserves isotropy groups) is NOT adopted. Under it the twin problem disappears: MS11♭ then holds at every point (entry 114 of this round's block: one lift-curve). If it is ever used, it must be flagged. It is a natural alternative reading of "smoothly trivial" when M_g is regarded as an orbifold; the final document should present the result under it as a conditional theorem.
- Extra readings (R3), (T4) are no longer needed by the chain (Lemma S̃′ replaces (T4); round11_q9 §1.1 confirms).

## Standing results (never drop; [mem] = cited from memory by the workers)
- **S1 (entries 2, 19).** t ↦ Y_t is holomorphic. So the goal holds iff Y_t lies in a countable set for t in a set accumulating in Δ.
- **S1′ (entry 34).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No local argument near ∂V_t works; the forgetful-fibre family in M_{0,7} satisfies every hypothesis except total geodesy, with Y_t non-constant.
- **S3′ (entry 93).** Lemma Loc: neither the goal nor (Rig) follows from local data at boundary points. Prop. TG.
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5; S50).** If every V_t (or uncountably many) is totally geodesic, the claim holds [countability, mem].
- **S6/S6′ (entries 14, 24).** Pinning lemma; incidence transport.
- **S7 (entry 15), S7′ (entry 94).** Royden domination; Kobayashi lemmas K1–K3.
- **S8 (entry 25).** Krull second branch at a cusp.
- **S9 (entry 20).** Douady germ a reduced point ⇒ claim. **S9′ (round11_q6 Prop. 3.2).** [closure V_0] isolated in the Douady space ⇒ claim.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning; a counterexample needs a varying complex structure.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t ⇒ claim.
- **S12–S14, S16, S23, S28 (entries 26, 29, 30, 46–48, 50, 58, 59, 64, 65, 73).** Log-flow converse; Lemma R* (Teichmüller vertex pinned under (O)); Theorem L; Theorems P/P′/P″; Krull/twin pinning; Prop. K; no-twin transport; Theorem X. Not on the current line, except that Lemma R*/Theorem L/L2 are the natural inputs for (Rig) under an orbifold reading.
- **S15 (entries 31, 32, 45).** Lemma T′, Lemma V (constant vertex never carries area), Lemma PA.
- **S17–S19 (entries 36, 37, 43, 44, 49, 60).** Covering-construction special cases; quintic surface (singular); Picard surface.
- **S20–S22 (entries 54–57).** L1, L1′; L2 for product G under (H_0), (O_G); time-t lemmas.
- **S24 (entries 61–63).** Structure of the obstruction.
- **S25 (entry 70).** (F2) general; Theorem TV (Teichmüller vertex of every piece).
- **S26/S27 (entries 71, 72).** Lemma U; generic-time trichotomy (R8-2 Theorem 1: no MERGE/puncture-MOV of a Y_t-copy at generic t) under (Rig).
- **S29–S33 (entries 74–81).** Theorem 2V; MS8 under (U_J)/(Lock), (SC)/(NT)/(IP), (NB); twin-jump configurations; (PC); Lemma Red, P0, Theorem B; Examples Z, Z′.
- **S34 (entries 85, 98).** Proposition K_w (walk chain) with repairs (R-a)–(R-d) and Lemma S̃′ (one upstairs component; checked again in round11_q9 §1.1 with a minor repair to the choice of R).
- **S35–S42 (entries 84, 86–92).** Theorem X*/X′; Lemma PT; Lemmas T, S, J, Theorem R; copy-free dichotomy; lift-curves; (U″); (IP_Γ); partner lemmas.
- **S43 (entry 97).** Theorem X*_all (all strata; re-checked by round11_q9 §1.3 via the maximum-principle route).
- **S44 (entry 99).** Cor. IMOV_all: genuine transitions and the endpoint are punctures of both pieces (re-checked round11_q9 §1.2).
- **S45 (entries 100 → retracted; surviving parts re-entered this round).** Gap A repair (R(D) ⊂ Σ) and reducibility of transport families stand; Lemma B1(a),(b) are false and replaced by **B1♭** (round11_q9 §2.3; round11_q2 B1ᵃ; round11_q8 Lemma 1.4): anchored sheets exist, contain the germ components at generic points of c̃, form one Stab_pt(c̃)-orbit, and every component of closure(Ñ_c̃) is a·(anchored sheet).
- **S46 (entry 102).** Incidence propagation (Lemmas I0–I2), counting no-go, Theorem Q.
- **S47 (entry 103; round11 entry for MS11).** Logical status: under (Rig), MS10/MS11/MS11♭ are equivalent to the problem; a refutation is a counterexample to the problem.
- **S48 (entries 104, 106).** Level structures give nothing new; Lemma D3.
- **S49 (entry 105).** Lemma 3.1: the cusp Q leaves closure(V_τ) for generic τ.
- **S50 (entry 107).** Lemma CD: (Rig) for a piece ⇔ countable-class membership for uncountably many t.
- **S51 (round11_q9; new).** Corrected chain: MS11♭ + entries 19, 24, 84–87, 97–99 + B1♭ ⇒ MS8, checked step by step (base, product-type junction with anchored output, transfer, endpoints).
- **S52 (round11_q4 §2, round11_q1 §2; new).** Sheets contain lift-curves; P(T) = C(L) for any lift-curve L in a boundary-type sheet T (uses R8-2/R8-3 Theorem N, (Rig), Y non-constant); MS11♭ fails only if Q_t has ≥ 2 lifts (|Aut(Q_t)| < |Aut(Q)|); "MS11 up to an automorphism" always holds (q1 Prop. 2.4).
- **S53 (round11_q3, q7, q1, q2, q5, q8; new).** Mechanism D: D-sheets anchored and boundary-type; sheet graph connected (Grothendieck [mem]); edges (α) preserve labels, (γ) preserve labels unless (γ°)/(IMOV_Q), (β) twist by σ ∈ Stab_pt(c̃); MS11♭ ⇔ the composite twist (including the initial twist in Stab_pt(β̃)) maps x into Stab(b̃)·P, when (γ°) is absent.
- **S54 (round11_q4 §3; new).** Twin-free closure: every piece reachable from ∂V_0 by puncture transitions has a constant vertex with value ≡ Y (if Y non-constant); Criterion R and Theorem TFM (V_0-only sufficient conditions); necessary conditions (NC1), (NC2) for a counterexample; covering constructions over M_{0,5} under (A) satisfy TFM (sketch).
- **S55 (round11_q1 §4; new).** Rigid twin: a failure at a MERGE/pMOV endpoint forces Q_t to carry, for every t, a Y_t-component and a component frozen at Y_0, swapped at t = 0 by an automorphism of Q.
- **S56 (round11_q10; new).** Lemma HQ (isolated boundary points move holomorphically); Prop. MP/MP′ (psh-isolation ⇒ (Rig) / the goal); Prop. DP (type-(0,5) Teichmüller vertices move in pencils, so ambient geometry alone cannot give (Rig)).
- **S57 (round11_q6; new).** Lemma TR: under orbifold transport (OT), the Teichmüller-vertex map of every product-type piece is t-independent (Royden, Bers, Thurston [mem]).
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; S13; S14; S23; entry 66; S28; S16; round10_q2 Lemma 4.1/Prop. P1.

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness/closedness hypotheses is false** (entry 43; round6_q2).
- **The map-level Lemma R* without (O) is false** (entry 64; round7_q7 Prop X).
- **Piece-level (Rig) is false** (entry 81; round8_q9 Examples Z, Z′).
- **"A transport family Ñ_b̃ is irreducible" is false** (entry 101; round10_q7 §3, round10_q3 §2.2).
- **Lemma B1(a),(b) of round10_q3 are false** (round11_q9 §2.2, round11_q2 §1.2, round11_q3 §2, round11_q8 §1.2): a component of closure(Ñ_b̃) can meet {t=0} only in a·b̃ ≠ b̃, and Stab_pt(b̃) need not act transitively. Hence MS11 as worded does not give MS8.

## Open gaps (routes set aside, not refuted)
- A. **The twin problem at non-product puncture points**: MS11♭ (below). After Mechanism D it is the label-twist problem at (β)-edges and (γ°)-edges.
- B. **(Rig)** (entry 82). Needs global input (S33, S3′, S56). Criteria: Lemma CD, Prop. MP. Under an orbifold reading, Lemma R*/Theorem L/L2/Lemma TR are natural inputs — untried as a combined route.
- C. Rigidity of V_0 itself (OQ-K, TG-prop, Douady isolation, psh-isolation).
- D. Counterexample. It would need: a varying complex structure; |Aut(Q_t)| < |Aut(Q)| at a non-product point of every walk chain; (NC1), (NC2) at every point of the reachable network; a label-moving (β)-twist or a (γ°)-configuration; the cusp leaving closure(V_τ); the rigid twin at the endpoint.
- Set aside, not refuted: counting (round10_q7 C3); level structures; arithmetic; Kobayashi domination; persistence of a Teichmüller curve in V_t; multi-scale route to MS5; length/area inequalities for (O); Hodge rigidity of the constant factor; "total release"; deformation theory of closure(V_0) in the Douady space (round11_q6 §3: first order only); psh-isolation (round11_q10: fails for (0,5) vertices); the twin-free restart route (round11_q4 §3 end: termination of a twin-free Prop. K).

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No. No round-11 file proves MS11 (or its corrected form) or the goal, and none refutes the goal. Round 11 found that MS11 as worded does not give MS8 (Lemma B1(a),(b) false), so MS11 is retracted and replaced by MS11♭, for which the chain was re-checked step by step (round11_q9 §5).

**Definitions** (as before, plus anchored sheets).
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w; M(E), K(E) as before.
- *Chart at Q*: Def(Q) with plumbing coordinates s_e, N := ∏_e s_e, q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g. *Labels* = vertices of G_Q; x intact at p if s_e(p) = 0 for every edge e at x; then F_x(p) is that component with its special points.
- *Transport family* Ñ_c̃ of a lifted branch c̃ of a branch c of B_0 at Q: the connected component containing c̃ ∖ {0} of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε).
- *Anchored sheet* of c̃: an irreducible component T of closure(Ñ_c̃) (in B × Δ_ε, germ at (0,0)) with c̃ × {0} ⊂ T.
- *x is Y-persistent on T*: at every (p,t) ∈ T, x is intact at p and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).
- *Lift-curve*: an irreducible component of {(p,t) : q(p) = Q_t}, Q_t := H_t(Q).
- *Product-type stratum*: ξ_G injective on coarse spaces.

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

**Why it should hold (planner's sketch; new this round: Mechanism G, the lift-curves of the 3-fold component and their stabilisers).**
1. Reduction already proved (S52, S53): P(T) = C(L) for every lift-curve L in a boundary-type sheet T; all D-sheets of X ⊃ S × {0} are anchored and of boundary type; labels change only by (β)-twists σ ∈ Stab_pt(c̃) and at (γ°)-edges; the x-sheet of β̃ meets X after an initial twist τ ∈ Stab_pt(β̃).
2. Observation (mine, to be checked): every D-sheet contains a lift-curve lying in X, and the lift-curves in X are the gL_0 (g ∈ Aut(Q)) with gL_0 ⊂ X; they include the orbit G_X·L_0 of G_X := Stab_{Aut(Q)}(X), and any others lie in X ∩ gX for some g ∉ G_X. So P(T) = g·C(L_0) for every D-sheet T, with g ranging over A_X := {g : gL_0 ⊂ X}. Once the x-sheet of β̃ is in X (x ∈ C(L_0)), MS11♭ ⟺ some anchored sheet of b̃ contains a lift-curve gL_0 with g^{-1}x ∈ C(L_0).
3. Hence a sufficient condition is (1L_X): X contains exactly one lift-curve (round11_q4 Cor. 2.4). A failure needs g ∈ A_X with gL_0 ≠ L_0: either an element of G_X (an automorphism of Q preserving the family's local 3-fold component) that Q_t loses, or a second 3-fold component gX ≠ X meeting X along a lift-curve.
4. Candidate mechanism for (1L_X): Fix(g) ∩ X for g ∈ G_X. g acts on X_0 ⊃ S. By Lemma TG (total geodesy) Fix(g) ∩ S is S, a Teichmüller disc, or contained in the boundary curves. If g fixes S pointwise, Lemma D3 (entry 106) locks twins when g fixes a 3-dimensional component; one needs the 2-dimensional analogue: if g ∈ G_X fixes S × {0} pointwise, then g fixes the lift-curve L_0 setwise. (Local evidence: if X is smooth with t a coordinate, a finite-order g commuting with t and trivial on {t = 0} is the identity; if instead t = b² on X with g: b ↦ −b, X_0 is non-reduced and g maps the single lift-curve {b² = t} to itself; in the reduced model c = t², b = ±t, g swaps two components X ≠ gX, each with one lift-curve. In all three, (1L_X) holds.) If Fix(g) ∩ S is a Teichmüller disc or a boundary curve, g acts on S as a non-trivial (anti-)reflection, and total geodesy constrains how the twin moduli of x and gx separate along S (q1 §5: "square-root approach"); the claim to test is that this separation already at t = 0 is incompatible with Lemma PA/Lemma V (constant vertices carry no area) plus the multi-scale structure of the norming differentials.
5. The (γ°)-edges force Y(Δ) inside a fixed curve pr_u(K) of a moving vertex of a piece through Q (round11_q7 §5) and a rigid twin at Q_t (as at the endpoint, S55); both failure modes thus produce at Q_t a Y_t-component and a frozen or ψ-valued twin exchanged at t = 0 by an element of A_X. A unified attack would show that no element of A_X can exchange a Y-persistent copy with a non-persistent one.

**Tried so far** (on MS11♭ and its earlier wordings MS11 = entry 109, MS10 = entry 96, MS8 = entry 68, MS6, MS5 = entry 40, (T0) = entry 28, (C-merge)/(H1)):

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 | — | (H1) isolated |
| round4_q7 §C | local analysis | (C-merge) not derivable locally |
| round5_q1–q4, q9 | conditional pinning under (T0) | heuristics |
| round5_q5 | analytic half | T′, V |
| round5_q8 | cyclic constructions | twin gap found |
| round6_q1, q2, q3, q8 | closing on MS5 | MS5 false for the singular quintic; Krull/twin pinning |
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
| round9_q2 | lift-curves, star | SC all-or-nothing; Prop 4 |
| round9_q3 | pole function; product strata | X′; Lemma PT |
| round9_q7 | components of ℬ, alignment | Lemmas T/S/J; Theorem R |
| round9_q4 | crossing step + same sheet | X*; walk chain K_w |
| round9_q5 | α-fixed loci + Lemma TG | (U″) suffices |
| round9_q6 | 3-fold 𝒳, Γ-orbits | (IP_Γ) suffices |
| round9_q8 | endpoint twin obstruction | partner lemmas |
| round10_q1, q2, q3 | closing on MS10 | X*_all; IMOV_all; gaps A/B |
| round10_q4 | refute MS10 | none; MS10 ⇔ Goal(Rig) |
| round10_q5 | level structures | dead end |
| round10_q6 | trace step, (A2)/(B)/(D3) | Lemma D3 |
| round10_q7 | counting | no-go; incidence propagation; Theorem Q |
| round10_q8 | statements only; arithmetic | arithmetic dead |
| round10_q10 | chain check of K_w | Lemma S̃′ |
| round11_q1, q2, q3, q8 | closing on MS11 (Mechanism D) | Gap C (B1 false) and anchored-sheet repair; Mechanism D rigorous; reduction to (β)-twists and (γ°); lift-curve reformulation; rigid twin; local (β)-model |
| round11_q4 | refute MS11 | none; lift-curve form, (1L), twin-free closure, TFM, (NC1)/(NC2) |
| round11_q5 | Mechanism D (named) | same reduction, gaps (G0)/(G1)/(L5) |
| round11_q6 | statements only; Douady deformation theory | first-order only; rigid case; Lemma TR |
| round11_q7 | Theorem Q continued via Grothendieck | Theorem D: (F1)/(F2) collapse to (B-pure) twists and (IMOV_Q) |
| round11_q9 | chain check | B1 false; chain correct with MS11♭ |

## Target for round 12

**Progress test.** The last two rounds produced progress in the strict sense, but only through round 10: Theorem X*_all and Lemma S̃′ (universal, chain-shortening). Round 11 by itself produced no proof of the missing statement and no strictly simpler replacement; it produced (a) a correction (MS11 does not suffice; MS11♭ does, chain re-checked), (b) an equivalent reduction of MS11♭ to label twists at (β)- and (γ°)-edges (Mechanism D, universal and proved), and (c) twin-free results (S54, S55) that settle nothing in the chain. Honest status: the core twin-at-puncture problem has been open since round 7; if round 12 yields nothing universal, the main line is stalled.

What differs in my sketch from last round: Mechanism G replaces Mechanism D's edge-by-edge bookkeeping by a statement about the lift-curves contained in one 3-fold component X and the group elements relating them ((1L_X); the elements A_X), with a local analysis showing (1L_X) holds in the three basic local models of a component through S × {0} (smooth, non-reduced fibre, two components swapped).

Also recorded this round: under the orbifold reading (R2^orb), MS11♭ holds trivially (one lift-curve), so the goal reduces to (Rig) under that reading. Lemma R*, Theorem L, L2 and Lemma TR are proved under orbifold-transport hypotheses that (R2^orb) may supply. A complete conditional theorem "claim under (R1), (R2^orb)" is within reach if (Rig) follows from (R2^orb); that is the most valuable fallback for the final document.

**Wave (escalation rule; new wording of the missing statement, MS11♭):**
- q1, q2, q3: the closing task on MS11♭, byte-identical. Splices: the chain, definitions and sketch; earlier proofs (PR-H, R8-1, R8-2, R7-3, R7-4, R8-3, R8-8, round9_q4, q3, q7, q5, q2, q1); round 10 (q1, q10, q3, q7, q2 §4–5, q6 §1); round 11 (q9, q3, q7, q1, q4).
- q4: refute MS11♭ exactly as stated (the wording changed).
- q5: statements only (the core has been attacked since round 8): derive the goal from MS11♭ + cited statements, then attack with a first move none of the listed attempts used.
- q6: Mechanism G (named, new): lift-curves of the 3-fold components; prove (1L_X)-type statements and handle the initial twist, or MS11♭ directly.
- q7: the (β)-twist obstruction (round11_q1 (β-fail), q3 §3.6 (O1), q7 (O-Bpure)), posed as the thing to overcome or to sharpen into a counterexample, with global inputs (twin-free closure S54, rigid twin S55, Lemma TG, Lemma PA/V).
- q8: the (γ°)/(IMOV_Q) obstruction (round11_q3 Prop. 3.2, q7 §5), posed likewise.
- q9 (elsewhere 1): (Rig), entry 82; in general, and failing that under the orbifold reading (R2^orb), combining Lemma R*/Theorem L/L2/Lemma TR/Lemma CD.
- q10 (elsewhere 2): the twin-free route (round11_q4 §3): prove a V_0-only twin-free criterion (Criterion R / TFM), e.g. by a twin-free walk with a termination argument, which together with (Rig) gives the goal without MS11♭.
