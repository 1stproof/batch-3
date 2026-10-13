# Running summary after round 10 (written at round 11 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After ten rounds (78 queries) there is no proof and no counterexample. Round 10 (10 queries) attacked MS10 (entry 96). It produced:
- Theorem X*_all, which removes the product-type hypothesis from Theorem X*. It was proved twice, independently: round10_q1 §2 and round10_q2 §3.
- A separate check of Proposition K_w (round10_q10). The proposition holds after four repairs. The key new fact is Lemma S̃′: canonical lifts keep each transition inside one upstairs irreducible component, and no extra reading is needed.
- Cor. IMOV_all (round10_q1 §4): with S̃′ and X*_all, every transition that is an interior point of an adjacent piece is trivial. All remaining twin cases are therefore at points that are punctures of both pieces.
- Two genuine gaps in the MS10 chain (round10_q3, independently round10_q2 and round10_q7), both repaired:
  - silent label switches along non-product pieces;
  - reducible transport families. This forces a component-wise notion of persistence, so MS10 as worded is replaced.
- Theorem Q (Krull linkage) and incidence propagation (round10_q7).
- A proved no-go for counting (round10_q7) and for level structures (round10_q5, round10_q6).
- Logical-status results (round10_q2, q3, q4, q8): MS10-type statements are localisations of the goal, not weakenings.
- Lemma 3.1, the cusp must move (round10_q3); Lemma D3 (round10_q6); Lemma CD for (Rig) (round10_q9).

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ. It is smooth on V_0 × Δ, preserves every stratum, and has H_0 = id (round2_q1, round3_q1).
  - This is a Thom–Mather-type strengthening of the literal (i)/(ii); the final document must say so.
  - It is the coarse reading: H_t need not preserve automorphism groups.
- The fixed index i is recovered by a Baire argument (round4_q5 §1).
- "Smooth" V_0: the quintic test surface is singular (round6_q3).
- (R2^orb)/(R2+) is NOT adopted. Under it, twins disappear (round8_q8 Cor. 1; round10_q4 §3, sketch). If it is ever used, it must be flagged.
- Extra readings: (R3) and (T4) were used in round9_q5. (T4) was used in round10_q1 Lemma 1SS, but round10_q10 Lemma S̃′ makes it unnecessary for the chain.

## Standing results (never drop; [mem] = cited from memory by the workers)
- **S1 (entries 2, 19).** t ↦ Y_t is holomorphic. So the goal holds iff Y_t lies in a countable set for t in a set accumulating in Δ.
- **S1′ (entry 34).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No local argument near ∂V_t works. The forgetful-fibre family in M_{0,7} satisfies every hypothesis except total geodesy, and its Y_t is non-constant.
- **S3′ (entry 93).** Lemma Loc: local admissible deformations at boundary points move the constant factor, so neither the goal nor (Rig) follows from local data. Also Prop. TG.
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5).** If every V_t is totally geodesic, the claim holds. Strengthened in S50: uncountably many t suffice.
- **S6/S6′ (entries 14, 24).** Pinning lemma; incidence transport.
- **S7 (entry 15).** Royden domination.
- **S7′ (entry 94).** Kobayashi lemmas K1–K3. Open: OQ-K.
- **S8 (entry 25).** Krull second branch at a cusp.
- **S9 (entry 20).** If the Douady germ is a reduced point, the claim holds.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning; a counterexample needs a varying complex structure.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t imply the claim.
- **S12 (entry 26).** Log-flow converse (not on the current line).
- **S13/S13′/S13″ (entries 29, 46, 64, 65).** Lemma R*, Theorem L, Lemma G, Prop. X (not on the current line).
- **S14 (entries 30, 47, 48).** Theorems P, P′, P″; Krull/twin pinning (not on the current line).
- **S15 (entries 31, 32, 45).** Lemma T′, Lemma V, Lemma PA.
- **S16 (entry 50).** Proposition K. Superseded by S34.
- **S17 (entries 36, 37, 60).** Covering-construction special cases; Theorem C; Theorem A of round7_q4.
- **S18 (entries 43, 44, 49).** Quintic surface (singular).
- **S19.** Picard surface: merges only in non-product strata.
- **S20 (entries 54, 55).** L1 (product strata), L1′.
- **S21 (entry 56).** L2 for product G under (H_0), (O_G).
- **S22 (entry 57).** Time-t lemmas.
- **S23 (entries 58, 59).** No-twin transport (NT*), (NT), (Lock) (not on the current line).
- **S24 (entries 61–63).** Structure of the obstruction.
- **S25 (entry 70).** (F2) in general form; Theorem TV (Teichmüller vertex of every piece).
- **S26 (entry 71).** Lemma U under (Rig).
- **S27 (entry 72).** Generic-time trichotomy under (Rig).
- **S28 (entry 73).** Theorem X (Q-Cartier). Superseded by S35/S43.
- **S29 (entry 74).** Theorem 2V; Cor. G1.
- **S30 (entries 75–77).** MS8 under (U_J)/(Lock), (SC)/(NT)/(IP), (NB)+(NB_∂). These use the unsupported (TD_J) for the K_0-chain.
- **S31 (entry 78).** Twin-jump configurations (A), (B), (C).
- **S32 (entry 79).** Crossing persistence / (PC).
- **S33 (entries 80, 81).** Lemma Red, Lemma P0, Theorem B; Examples Z, Z′ (piece-level (Rig) is false).
- **S34 (entries 85, 98).** Proposition K_w (round9_q4 §2), checked and repaired by round10_q10.
  - Repairs:
    - (R-a) extra smallness conditions;
    - (R-b) canonical chart lifts: the T_g-ray is pushed down through U → U/Tw = Def(J), so the label x is well defined across orbifold points;
    - (R-c) Lemma S̃′: the canonical lift lies on the holomorphic image of a Teichmüller disc in q^{-1}(V_0), so entering and leaving lifts lie in one upstairs irreducible component;
    - (R-d) recurrent transition types. Witnessing path sequences are per transition, not one common sequence.
  - The cited inputs remain: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T̄_g/Def chart description, the collar lemma, and continuity of hyperbolic metrics.
- **S35 (entry 84).** Theorem X*/X′ (product type). Generalised in S43.
- **S36 (entry 86).** Lemma PT, Cor. IM, Prop. CN, Count lemma (round9_q3).
- **S37 (entry 87).** Lemmas T, S, J; Theorem R (round9_q7).
- **S38 (entry 88).** Copy-free dichotomy.
- **S39 (entry 89).** Lift-curves; SC all-or-nothing; Prop. 4.
- **S40 (entry 90; readings (R3), (T4)).** (U″) suffices; Lemma TG; boundary trace trichotomy.
- **S41 (entry 91).** Γ-orbit of lifts; (IP_Γ) suffices.
- **S42 (entry 92).** Partner lemmas.
- **S43 (entry 97; round10_q1 §2, round10_q2 §3).** **Theorem X*_all.** In any stratum, at an interior point Q_0 of a piece E, an upstairs sheet containing a lift β̃ of a branch of E meets the boundary only in β̃.
  - Two lifts β̃ ≠ aβ̃ never share a sheet.
  - The proof lifts the limit disc to ∏_w M_w by the marking.
  - It includes a small correction to the homological step of round9_q4 §1.4.
- **S44 (entry 99; round10_q1 §4 with round10_q10).** **Cor. IMOV_all.** At a walk-chain transition lying in the stratum of either adjacent piece, the entering lift equals the leaving lift. So:
  - the endpoint and every genuine transition are punctures of both adjacent pieces, in every stratum;
  - there are no junction crossings, interior-MOV endpoints or turning twins;
  - the R(D)-points of S45 are trivial transitions.
- **S45 (entry 100; round10_q3 §2, round10_q2 §2).** Chain repairs.
  - Gap A: Σ is enlarged by R(D).
  - Gap B: component-wise persistence. Lemma B1 ((a) every component of Ñ_b̃ maps onto N and has an open t = 0 slice in b̃ ∖ 0; (b) Stab(b̃) permutes components transitively; (c) persistence transforms by (K3); (d) the notions agree in product type).
  - Component-wise transfer of persistence along travel intervals, via Lemma S(c).
- **S46 (entry 102; round10_q7).** Incidence propagation.
  - Lemma I0: every transport sheet contains a lift-curve.
  - Lemmas I1/I2: P(T) = Λ(λ) for boundary-type T ⊃ λ.
  - Cor. I3/I4: propagation along the incidence graph.
  - Counting no-go C3.
  - **Theorem Q**: Krull linkage under set-theoretic principality (QC) and (Sep).
  - Cor. Q2: a failure with β ≠ b needs (F1), a non-Q-factorial common component of 𝒳 at (0,0), or (F2), the sheets on different components.
  - "Stars are disjoint" is false at symmetric points.
- **S47 (entry 103).** Logical status: MS10 ⇔ MS10_w ⇔ Goal(Rig), given the chain. Refuting the twin statement means disproving the problem under (Rig). For σ-stable twin sheets, MS10 is equivalent to the problem for that V_0 (round10_q8).
- **S48 (entries 104, 106).** Level structures.
  - Theorem 1: G_m(C) = 1 for stable C, m ≥ 3.
  - Prop. L2: level charts reproduce Aut(Q) on labels.
  - Prop. L1: lifted triviality implies (IP).
  - round10_q4 Props. 3, 4 (covering-construction surfaces).
  - Lemma D3 (round10_q6).
- **S49 (entry 105; round10_q3 §3).** Lemma 3.1: the cusp Q leaves closure(V_τ) for generic τ. Prop. 3.2 (conditional): (A2-disc) is not an equisingular deformation.
- **S50 (entry 107; round10_q9).** Lemma CD and Cor. CD1–CD3 ((Rig) for a piece ⇔ countable-class membership for uncountably many t); Prop. MH; Prop. TG′.
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; S13; S14; S23; entry 66; S28; S16; round10_q2 Lemma 4.1/Prop. P1 (superseded by S44).

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness/closedness hypotheses is false** (entry 43; round6_q2).
- **The map-level Lemma R* without (O) is false** (entry 64; round7_q7 Prop X).
- **Piece-level (Rig) is false** (entry 81; round8_q9 Examples Z, Z′).
- **"A transport family Ñ_b̃ is irreducible" (R7-3 Lemma 2 step 2) is false** (entry 101; round10_q7 §3, round10_q3 §2.2). So whole-family persistence (MS10's wording) is the wrong notion at non-product pieces.

## Open gaps (routes set aside, not refuted)
- A. **The twin problem at non-product puncture points**: the missing statement MS11 (below).
- B. **(Rig)** (entry 82). It still needs global input (S33, S3′). round10_q9 reduces it to countable-class membership (Lemma CD) and shows that map-level Hodge theory proves too much. Open: K^v_t is a Teichmüller curve for uncountably many t, or no image-level type jump and m_0 = 1.
- C. Rigidity of V_0 itself (OQ-K, TG-prop).
- D. Counterexample. It would need all of the following:
  - a varying complex structure;
  - a non-product twin puncture point on every walk chain;
  - |Aut(Q_t)| < |Aut(Q)|;
  - a relevant ≥ 2-dimensional α-fixed locus;
  - the cusp Q leaving closure(V_τ) (S49);
  - for covering-construction V_0, V_t leaving the symmetric locus (S48).
- Set aside, not refuted:
  - the counting route (round10_q7 C3: every count is Γ-equivariant);
  - the level-structure route (round10_q5 L2, round10_q6 L′: equivalent to the orbifold chart);
  - arithmetic (round10_q8 §2.1: sees only t = 0);
  - Kobayashi domination (OQ-K);
  - persistence of a Teichmüller curve in V_t;
  - the multi-scale route to MS5;
  - length/area inequalities for (O);
  - Hodge rigidity of the constant factor;
  - "total release".

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No. No round-10 file proves MS10 or the goal, and none refutes the goal. Round 10 did REFUTE a step underlying MS10's wording (entry 101), so MS10 is retracted (entry 108) and the chain is re-derived for MS11.

**Definitions** (as in earlier rounds, plus the transport-sheet notion):
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w. M(E) and K(E) as before.
- *Chart at Q*: Def(Q) with plumbing coordinates s_e and q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g.
- *Labels*: vertices of G_Q. x is intact at p if s_e(p) = 0 for every edge e at x; then F_x(p) is that component with its special points.
- Lifted branches, transport families and transport sheets are as in MS11.
- *Product-type stratum*: ξ_G is injective on coarse spaces.

**Chain** (every step PROVED except MS11 and the separate open input (Rig), entry 82).
1. **Goal ⇐ MS8 + (Rig) + entry 19.** MS8 (entry 68's statement, now only an intermediate claim): under (R1), (R2) and (Rig), Y_t = Y_0 for all t. Given (Rig), MS8 is the goal; entry 19 (Y holomorphic) turns "Y constant" into Y_t = Y_0. (Rig) is entry 82, OPEN; it is the one input that remains after MS11.
2. **MS8 ⇐ MS11.** Assume MS8's setting and, for contradiction, that Y is non-constant.
   - (a) **Walk chain** (entries 85, 98: Proposition K_w as repaired in round10_q10, with canonical chart lifts and recurrent transition types; special set Σ enlarged by the finite sets R(D) of entry 100). Fix r small. There are pieces D^1 ⊂ ∂V_0, D^2, …, D^k; transition points J_1, …, J_{k−1}; an endpoint Q_0. At each J_m there are an entering lift β̃_m (branch of D^m) and a leaving lift β̃′_m (branch of D^{m+1}) in Def(J_m) with one common chart vertex x_m (the constant Y_0-vertex on both sides), and, by Lemma S̃′ (entry 98), β̃_m and β̃′_m lie in one irreducible component of q^{-1}(closure V_0) ∩ B. At Q_0 the entering lift β̃ (vertex x) and the terminal lift b̃ lie in one such component, and x is MERGE (an edge at x unpinched) or MOV (x intact, F_x non-constant) along b̃ at t = 0.
   - (b) **Interior transitions are trivial** (entry 99, Cor. IMOV_all, from Theorem X*_all, entry 97, and the common component of (a)). If J_m lies in the stratum of D^m or of D^{m+1}, then β̃′_m = β̃_m as sets, so the transport families and their sheets coincide and persistence passes unchanged. This covers the R(D)-points. Consequently Q_0 and every genuine transition are punctures of both adjacent pieces, i.e. satisfy (P).
   - (c) **Induction claim (component-wise, entry 100):** x_m is Y-persistent on some transport sheet of β̃_m.
     - Base: Δ_Γ is of product type and π_i(∂V_t) = {Y_t}, so vertex i is persistent on every sheet of every lift of a branch of D^1 (entries 24, 87; Lemma B1(d)).
     - Step at a puncture transition J_m of product type: Lemma PT (entry 86) makes J_m aligned, and Lemma J / Cor. J′ (entry 87, component-wise as in round10_q3 §2.2 item 2) give persistence on a sheet of β̃′_m.
     - Step at a puncture transition J_m of non-product type: MS11 applied to (Q, β̃, b̃, x) = (J_m, β̃_m, β̃′_m, x_m); (P) holds by (b), (S) by (a).
     - Transfer along D^{m+1} from β̃′_m to β̃_{m+1}: component-wise transfer (entry 100, round10_q3 §2.2 item 3: persistence is a property of the irreducible lifted family component, Lemma S(c) of entry 87, and the label is consistent along travel after the R(D) repair).
   - (d) **Endpoint.** By (b), Q_0 is a puncture of both pieces, so its terminal type is MERGE or puncture-MOV.
     - Product type: Q_0 is aligned (Lemma PT) and Lemma J (J1) / Theorem R (entry 87) give Y_t in a finite set on an open set of t, so Y is constant (entry 19), a contradiction.
     - Non-product type: MS11 for (Q_0, β̃, b̃, x) gives a transport sheet T of b̃ on which x is persistent; by Lemma B1(a) (entry 100) T ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0, on which x is intact with F_x ≡ Y_0; by the identity theorem along the irreducible curve b̃ (patterns are constant on b̃ ∖ 0), x is intact along b̃ with F_x ≡ Y_0. This contradicts MERGE and MOV.
   - Hence Y is constant: MS8.

So MS11 + entries 19, 24, 84–87, 97–100 give MS8, and MS8 + entry 82 give the goal. After MS11 only entry 82 ((Rig)) remains.

Remarks.
- MS11 carries (P) and (S) because the chain supplies them (entries 98, 99) and all other transitions are settled by PROVED entries (product-type points by 86/87; interior points by 99).
- MS11 has the hypothesis "Y non-constant" because it is used in contradiction form; without it MS11 is false (the walk chain's endpoint violates its conclusion). By entry 103, a counterexample to MS11 is a counterexample to the problem under (Rig).
- Component-wise persistence is forced: the whole-family notion of MS10 fails in local models (entry 101).
- Inputs cited from memory by the workers and not re-proved: Lemma PA, Lemma NH, Kerckhoff, Maskit, the augmented-Teichmüller/Def chart description, collar lemma, (Fl), (Prop), resolution facts for Theorem X*, Krull, Remmert.

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

**Why it should hold (planner's sketch; Mechanism D, connectedness of the boundary divisor — new this round).**
1. Let S be the sheet of (S). At a generic point p of S, 𝒱 is a complex 3-manifold, so q^{-1}(closure 𝒱) has a 3-dimensional irreducible component X of its germ at (0,0) with S × {0} ⊂ X. Put N := ∏_e s_e and D := X ∩ {N = 0}.
2. D has pure dimension 2 (Krull). None of its components lies in {t = 0}, because X_0 ∩ {N = 0} is at most 1-dimensional. So every component of D is a transport sheet of some lifted branch c̃ ⊂ X_0. In particular D contains a sheet of β̃ and a sheet of b̃, because β̃, b̃ ⊂ S ⊂ X_0.
3. **Grothendieck's connectedness theorem** (SGA 2, XIII 2.1; cite): if X is an analytically irreducible 3-dimensional germ and D = X ∩ {N = 0} is cut out by one equation, then D ∖ {(0,0)} is connected. So the sheets of D form a connected graph, with two sheets adjacent when they share a curve germ C through (0,0).
4. Such a C is of one of three kinds:
   - (α) a lift-curve of Q_t. Then persistence passes, by Lemmas I1 and I2 of round10_q7 (boundary-type sheets).
   - (β) a common t = 0 branch c̃. Then the two sheets are σ-related for some σ in the pointwise stabiliser of c̃ (Lemma B1(b)), and the persistent label changes from y to σy.
   - (γ) a curve fixed pointwise by some g, at interior points of a piece for t ≠ 0. This is the same-branch crossing of round10_q7 Theorem Q(b), and the label changes from y to gy.
5. So MS11 follows if, along some path in the graph from a sheet of β̃ to a sheet of b̃, the composite label change maps x into Stab(b̃)·x. That holds for instance if every (β)-edge and (γ)-edge element fixes x.
   - Total geodesy should enter at (β)-edges: σ fixes pointwise a boundary branch c̃ of the totally geodesic sheet S, so (Lemma TG) Fix(σ) ∩ S is S, a Teichmüller disc, or only c̃.
   - It should enter at (γ)-edges through Theorem X*_all and the generic-time trichotomy.
6. The failure configurations that remain are exactly (B-pure) and the same-branch crossings. The interior fixed loci (A2) do NOT appear as edges inside X. This is a different decomposition from round9_q5's square-monodromy analysis.
7. Alternative (Theorem Q route): if X is Q-factorial at (0,0), Krull linkage gives MS11 directly when β ≠ b. A failure needs (F1) a non-Q-factorial X, or (F2) different components.

**Tried so far** (on MS11 and its earlier wordings: MS10 = entry 96, MS8 = entry 68, MS6, MS5 = entry 40, (T0) = entry 28, (C-merge)/(H1); (TW*) was MS10's predecessor):

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
| round7_q1, q2, q3, q8 | closing on MS6 (no-twin transport) | MS6 under (NT)/(NT*) |
| round7_q4 | refute MS6 | Theorem C |
| round7_q5 | twin-robust transport | chart-local twin model |
| round7_q6 | time-t open/closed | Theorem T under (Lock) |
| round8_q1 | closing on MS8; Teichmüller-disc limits | Theorem X |
| round8_q2 | Stein factorisation | Lemma U; trichotomy |
| round8_q3 | analytic Y-locus | Theorem N; Cor. T |
| round8_q8 | transport families, isotropy | (SC)/(IP) suffice |
| round8_q4 | refute MS8 | no counterexample; Theorem 2V |
| round8_q5 | Aut(J) fixed points, covering lemma | (U_J) suffices; Prop D |
| round8_q6 | Minsky/Antonakoudis crossings | (CR) ⇐ (PC) |
| round8_q7 | statements only | Lemma S, junction lemma |
| round9_q1 | copy-free / Krull at one lift | dichotomy; (Seal) |
| round9_q2 | lift-curves, star | SC all-or-nothing; Prop 4 |
| round9_q3 | pole function; product strata | X′; Lemma PT; Count lemma |
| round9_q7 | components of ℬ, alignment | Lemmas T/S/J; Theorem R |
| round9_q4 | crossing step + same sheet | X*; walk chain K_w |
| round9_q5 | α-fixed loci + Lemma TG (square monodromy) | (U″) suffices; (A2)/(B)/(D3) open |
| round9_q6 | 3-fold 𝒳, Γ-orbits | (IP_Γ) suffices |
| round9_q8 | persistent/endpoint twin obstruction | partner lemmas |
| round10_q1, q2, q3 | closing on MS10 | X*_all; IMOV_all (interior cases); gaps A/B and component-wise repair; Lemma 3.1; (NoSw) analysis; local models |
| round10_q4 | refute MS10 | none; MS10 ⇔ Goal(Rig); Lemma L; covering surfaces leave Z_G |
| round10_q5 | level structures | dead end: equivalent to the orbifold chart |
| round10_q6 | trace step (Tr), cases (A2)/(B)/(D3) | Lemma D3 only |
| round10_q7 | counting / conservation of number | no-go; incidence propagation; Theorem Q (Krull linkage; F1/F2) |
| round10_q8 | statements only; arithmetic first move | arithmetic dead; σ-stable twin ⇔ problem |
| round10_q10 | chain check of K_w | repaired; Lemma S̃′ (one upstairs component) |

## Target for round 11

**Progress test.** Rounds 9 and 10 produced progress on the chain, in the sense of new PROVED results that hold for every object the hypotheses admit and that shorten the chain.
- Round 9: the walk chain K_w, Theorem X′/X*, Lemma PT, Lemmas T/S/J.
- Round 10: Theorem X*_all (all strata, two proofs) and Lemma S̃′ (canonical lifts stay in one upstairs component, no reading needed). Together these give Cor. IMOV_all. Every interior-point transition, every interior-MOV endpoint, every junction crossing and every turning twin is gone from the chain, in every stratum.
- Round 10 also found and repaired two genuine gaps (entries 100, 101). As a result the missing statement is now MS11: component-wise, at puncture points only, with the common-component hypothesis (S).

Honest caveat: the hard core is unchanged. It is the twin problem at non-product points that are punctures of both pieces, and it has resisted rounds 7–10. MS11 is narrower and corrected, but its core is the same.

What differs in my sketch from last round: Mechanism D. It applies Grothendieck connectedness to the boundary divisor of the 3-fold component X ⊃ S × {0}. In that decomposition, interior fixed loci (A2) play no role, and the failure modes are only the label changes at (β)-edges (common t = 0 branch, pointwise stabiliser) and at (γ)-edges (same-branch crossings).

**Wave (escalation rule; new wording of the missing statement):**
- q1, q2, q3, q8: the closing task on MS11, byte-identical. It splices: PR-H, R8-1, R8-2, PR-I, R7-3, R7-4, R8-3, R8-5, R8-8 and the round-9 answers (from round10_q1.md lines 104–3048), plus the round-10 answers q1, q10, q3, q7 in full, q2 §4–5 and q6 §1.
- q4: refute MS11 exactly as stated.
- q5: Mechanism D (Grothendieck connectedness of the boundary divisor in X), a named approach not yet tried.
- q6: statements only. Derive the goal from MS11, then attack with a new first move.
- q7: round10_q7's Theorem Q continued. Settle (F1)/(F2): show that X is Q-factorial along the relevant sheets, or that (F1) is incompatible with smooth V_τ, or that (F2) reduces to linked sheets.
- q9 (elsewhere 1, chain check): check entries 99 and 100 as used in chain steps 2(b)–(d), i.e. Cor. IMOV_all with Lemma S̃′ in place of (T4), and the component-wise base, transfer and endpoint.
- q10 (elsewhere 2): entry 82 (Rig), continuing round10_q9's Lemma CD. Show that image curves of the Teichmüller vertex are Teichmüller curves for uncountably many t (no image-level type jump, m_0 = 1), and then pin the other vertices.
