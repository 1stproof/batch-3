# Running summary after round 9 (written at round 10 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After nine rounds (68 queries) there is no proof and no counterexample. Round 9 (10 queries) attacked MS8 (entry 68). It produced:
- the removal of Q-factoriality from Theorem X, proved twice independently (Theorem X′ in round9_q3, Theorem X* in round9_q4);
- a repaired Proposition K (the walk chain K_w, round9_q4). The old reading (TD_J) of the K_0-chain was found to be unsupported;
- Lemma PT (round9_q3): twins of the tracked copy occur only at points of NON-product strata;
- Lemmas T, S, J and Theorem R (round9_q7): Y is pinned whenever the track is "aligned" at every point;
- several reductions of the twin problem (round9_q1, q2, q5, q6, q8);
- two global-input results (round9_q9 Lemma Loc; round9_q10 Kobayashi lemmas K1–K3).

Together these remove the crossing half of MS8 from the chain. The missing statement becomes the twin statement MS10, posed only at points of non-product strata (see the chain section).

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, preserving every stratum, with H_0 = id (round2_q1, round3_q1).
  - (R2) is a Thom–Mather-type strengthening of the literal (i)/(ii); the final document must say so.
  - It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- The fixed index i is recovered by a Baire argument (round4_q5 §1).
- "Smooth" V_0: the quintic test surface is singular (round6_q3). Whether a locally closed V_0 is admissible is a reading question to flag.
- (R2^orb), optional and NOT adopted: H_t preserves isotropy groups. Under it twins disappear (round8_q8 Cor. 2). If ever used, it must be flagged.
- Extra readings used only in round9_q5: (R3) φ: 𝒱 → Δ is a holomorphic submersion; (T4) Prop K's lifted track lies in one global sheet of the preimage of V_0 in T_g. Results depending on them must say so.

## Standing results (never drop; [mem] = cited from memory by the workers)
- **S1 (entries 2, 19; round4_q3).** t ↦ Y_t is holomorphic. So the goal ⇔ Y_t lies in a finite (or countable) set for t in a set accumulating in Δ.
- **S1′ (entry 34; round5_q7).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t in a set accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No local argument near ∂V_t can work. The forgetful-fibre family in M_{0,7} satisfies every hypothesis except total geodesy and has Y_t non-constant (round5_q6).
- **S3′ (entry 93; round9_q9 Lemma Loc).** Sharper: at a point of ∂V_0 (mild automorphism hypothesis) there are local stratum-preserving admissible deformations of the germ of closure(V_0), including its 2-dimensional open part, along which the constant factor moves. So neither the goal nor (Rig) follows from local data at boundary points. Also Example AR-real; and Prop TG: if every V_t is totally geodesic the goal holds (countability of totally geodesic subvarieties [mem]).
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5).** If every V_t is totally geodesic, the claim holds.
- **S6/S6′ (entries 14, 24).** Pinning lemma; incidence transport P_t = H_t(P_0).
- **S7 (entry 15).** Royden domination.
- **S7′ (entry 94; round9_q10).** K1: the lift of V_0 is Kobayashi-isometric in T_g. K2: Kobayashi translation lengths of axis classes cannot decrease under the deformation. K3: equality with attainment forces the Teichmüller disc to persist in V_t, which pins Y (K4). Open: OQ-K, a Thurston-type length-spectrum rigidity for Kobayashi metrics.
- **S8 (entry 25).** Krull gives a second branch at a cusp; a merged vertex is non-constant.
- **S9 (entry 20).** If the Douady germ is a reduced point, the claim holds.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning; a counterexample needs the complex structure of V_t to vary.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t ⇒ claim.
- **S12 (entry 26).** Log-flow converse (not on the current line).
- **S13 (entry 29).** Lemma R*: under (H_0) and (O), f_t ∘ A_t = f_0.
- **S13′ (entry 46).** Theorem L: (O) holds under (★), (★∞).
- **S13″ (entries 64, 65; round7_q7).** Lemma G ((O) generic in t, careful sketch); Prop. X (map-level R* fails without (O)).
- **S14 (entries 30, 47, 48).** Theorems P, P′, P″; Krull/twin pinning (Theorem 4).
- **S15 (entries 31, 32, 45).** Lemma T′, Lemma V, Lemma PA.
- **S16 (entry 50; round6_q9).** Proposition K ("modulo routine marking details"). Superseded for chain use by S34 (K_w).
- **S17 (entries 36, 37, 60).** Covering-construction special cases; Theorem C (Galois covers over M_{0,5}, M_{1,2}); Theorem A of round7_q4 (t = 0 merge condition (M_β) ⇒ MS6 near 0).
- **S18 (entries 43, 44, 49).** The quintic surface (singular): MS5 fails there; the conclusion holds under (O) via twins.
- **S19.** The Picard surface: merges only in non-product strata.
- **S20 (entries 54, 55).** L1 for product strata and Aut(G)-fixed vertices; L1′ for all G.
- **S21 (entry 56).** L2 for product G under (H_0), (O_G). L2′ (non-product) is only a sketch.
- **S22 (entry 57).** Time-t lemmas (round7_q6, round7_q2).
- **S23 (entries 58, 59).** No-twin transport theorems (NT*), (NT), (Lock).
- **S24 (entries 61–63).** Structure of the obstruction: MS6 ⇔ goal + MS6_0; twin dichotomy; crossings locally consistent; orbifold points of V_τ swap twins.
- **S25 (entry 70; round8_q10).** (F2) proved in general form; Theorem TV: every 1-dimensional boundary piece in every stratum has a Teichmüller vertex j, with π_j∘ν a proper orbifold covering of a Teichmüller curve; every end maps to a cusp. Lemma PA quoted.
- **S26 (entry 71; round8_q2).** Lemma U under (Rig).
- **S27 (entry 72).** Generic-time trichotomy under (Rig): outside a discrete set of t, no Y_t-copy merges or moves at a puncture; every IMOV is a pure or shared crossing.
- **S28 (entry 73; round8_q1).** Theorem X (Q-Cartier version). Superseded by S35.
- **S29 (entry 74; round8_q4).** Theorem 2V; Cor. G1 (a merged copy has a frozen class).
- **S30 (entries 75–77).** MS8 under (U_J)/(Lock), (SC)/(NT)/(IP), (NB)+(NB_∂). Caveat (round9_q4 §2.2): these use (TD_J) for the K_0-chain, which is unsupported. For the walk chain K_w the track data hold with a fixed small ball B(J, 2r), and r may be taken as small as wished.
- **S31 (entry 78).** Twin-jump structure: configurations (A), (B), (C).
- **S32 (entry 79).** Crossing persistence / (PC).
- **S33 (entries 80, 81; round8_q9).** Lemma Red, Lemma P0, Theorem B; Examples Z, Z′ (piece-level (Rig) is false).
- **S34 (entry 85; round9_q4 §2).** **Proposition K_w (walk chain).** Proved modulo the inputs of PR-H, which are cited: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T_g ↔ Def chart description, and the collar lemma.
  - Fix small r. From a generic P ∈ ∂V_0, a single approximating Teichmüller ray gives a finite chain: travel along pieces D^1 ⊂ ∂V_0, D^2, …, D^k, alternating with excursions in balls B(J_m, 2r).
  - Along travel, the Σ_i-region is a constant vertex c_m ≅ Y_0 of D^m.
  - Inside each excursion the ray lifts continuously to Def(J_m)°, and one chart vertex x_m is c_m along the entry lift and c_{m+1} along the exit lift.
  - The last excursion ends at Q_0 with a terminal lifted branch b̃ ∌ 0 on which x is MERGE (an edge at x unpinched) or MOV (all edges at x pinched, F_x non-constant).
  - Every transition is realised by a sub-path inside B(J, 2r). Hence (Lemma S′) the incoming and outgoing branches lie in a common sheet of closure(V_0) at J.
  - The K_0-chain reading (TD_J) is unsupported: a Hausdorff limit can record a transition the ray never makes locally.
  - Not yet checked by a separate query.
- **S35 (entry 84; round9_q4 §1 Theorem X*, independently round9_q3 §1 Theorem X′).** For a piece E in a product-type stratum and Q_0 ∈ E, every boundary curve through Q_0 of any sheet of closure(V_0) containing a branch β of E lies over β. This holds for any normal singularity, with no Q-Cartier or Q-factoriality hypothesis.
  - Proofs: q4 uses a resolution, negative definiteness and intersection numbers; q3 uses a pole function (Lemma P, via Grauert relative ampleness [mem]) and the maximum principle.
  - Two distinct coarse branches through an interior point of a product-type piece never share a sheet.
  - Non-product strata: Step 5′ is local, but Steps 1–4 of Theorem X are unchecked there.
- **S36 (entry 86; round9_q3 §§2–6).**
  - Lemma SS / Cor. SS′ (under (Sm)): interior paths stay in one global component of closure(V_0) ∩ U.
  - **Lemma PT:** in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type. So at product-type chain points (NT) holds, and twins occur only at non-product points.
  - Cor. IM: an interior-MOV endpoint never lies in a product-type stratum. In general (given X′ there) it is a same-branch twin.
  - Lemma E, Prop. CN: the whole chain lies in the coarse persistent network 𝒩.
  - Count lemma: at generic t, every network piece with puncture Q has exactly r Y-vertices, r = #{components of Q_t ≅ Y_t}. A twin needs r + 1 copies of Y_0 at t = 0.
  - Cor. PC: MS8 holds when the chain lies in product-type strata (a sub-class).
- **S37 (entry 87; round9_q7).** Under (R1), (R2), (Rig):
  - Lemma T: H maps each piece into one global (and one local) irreducible component of the boundary total space ℬ.
  - Lemma S: M and K are constant on all fibres of a component, including t = 0. Persistence of a Y-copy is a property of the whole component.
  - Lemma J: at a point Q, for an arriving branch with persistent vertex x and another branch b, with x̂ = g′^{-1}x for an admissible g′ ∈ Aut(Q), exactly one of three holds: (J1) pinned (x̂ merged, or puncture-move), (J2) x̂ persistent on the next component, (J3) crossing.
  - Cor. J′: at an aligned junction (g′x = x) in the middle of a track, (J2) holds.
  - **Theorem R:** if every junction and Q_0 are aligned and the terminal branch is MERGE or puncture-MOV, then Y ≡ Y_0.
- **S38 (entry 88; round9_q1).** Copy-free dichotomy: if Y is non-constant, either (I) IMOV events lie on the persistent network at every generic t near 0, or (II) B_0^∂ is sealed ((II-a) together with (Seal_Q) at every point).
  - Release criterion: if some point of B_0^∂ has no Y_0-copy, then the goal holds unless (I).
  - Seal criterion. Cor. T and Theorem 2V are special cases.
  - "Total release" is false (quintic).
- **S39 (entry 89; round9_q2).**
  - Every transport family contains a whole lift-curve λ of Q_t, so (SC) is all-or-nothing in t.
  - At a junction both transport families lie in the closure of the track's 3-fold component 𝒞°.
  - Prop. 4: the t = 0 structure forced by a counterexample, via Star(λ).
- **S40 (entry 90; round9_q5; uses readings (R3), (T4)).**
  - Theorems A″, B″: R8-5's Theorems A/B hold under (U″). So only relevant α-fixed components of dimension ≥ 2 in 𝒳 can cause a twin jump; case (C) and all α-fixed loci inside {τ = 0} are harmless.
  - Lemma TG: a totally geodesic sheet meets Fix(h) in the sheet itself, a full Teichmüller disc, or points.
  - Cor. 2: in case (A2), V_0 contains a Teichmüller curve of h-symmetric curves with cusp J, or an h-symmetric sheet.
  - Lemma 3 (boundary trace trichotomy): (Ψ-0), (Ψ-J) (pointwise Lock at a lift of J_τ), or (Ψ-Z) (Lock on an α-stable transported piece).
  - Open: O1″ (A2), O2″ (B-pure), O3″ (D3).
- **S41 (entry 91; round9_q6).**
  - The lifts of J_t in the track's 3-fold component 𝒳 form one orbit of Γ = Stab(𝒞°), and both transport families lie in 𝒳.
  - Cor. 3′: no twin jump if Γ = Γ_x·Stab_Γ(j̃(t)), e.g. under (IP_Γ) or (NT_Γ).
  - Repair: 𝒳 need not be irreducible.
- **S42 (entry 92; round9_q8).**
  - Lemma 1: at a twin jump, the partner copy carries the other value function at the same lift. On the incoming piece it is frozen, persistent, or a crossing.
  - Lemma 1′: the merging copy at an endpoint twin is frozen.
  - Lemma 2: a coherent MERGE/pMOV endpoint freezes the tracked function.
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; Theorem M; Theorems P/P′/P″; S23; entry 66 (continuity principle); S28 (superseded by S35); S16 (superseded by S34).

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness and closedness hypotheses is false** (entry 43; round6_q2). MS5 itself was abandoned (RETRACT 40).
- **The map-level Lemma R* without (O), for families of maps with a Teichmüller anchor, is false** (entry 64; round7_q7 Prop X). Realisability as boundary pieces is unchecked.
- **Piece-level (Rig) is false** (entry 81; round8_q9 Examples Z, Z′). So no proof of (Rig) may use piece data alone; round9_q9 Lemma Loc strengthens this to all local data at boundary points.
- Closed candidates, not refuted routes:
  - Kobayashi domination ⇒ equality, now reduced to OQ-K (round9_q10);
  - persistence of a Teichmüller curve inside V_t;
  - the multi-scale route to MS5;
  - length/area/Arakelov inequalities for (O);
  - Hodge rigidity / Imayoshi–Shiga applied to the constant factor (round9_q9 §4: the factor's sub-quotient has finite monodromy);
  - "total release" (round9_q1 §5, false in the quintic).

## Open gaps (routes set aside, not refuted)
- A. **The twin problem at non-product points**: the current missing statement MS10 (below). The crossing half of MS8 is gone from the chain (S34–S37).
- B. **(Rig)** (entry 82). It still needs (O_G) for every piece and L2′. By S33 and S3′ it needs global input. Untried angles: type-jump exclusion at t = 0 for Teichmüller pieces; Möller-type Hodge characterisation.
- C. Readings of Prop K: K_w is proved modulo cited inputs (S34). It has not been checked by a separate query.
- D. Rigidity of V_0 itself (gap E of earlier rounds). Reduced to OQ-K (round9_q10) and to (TG-prop), the propagation of total geodesy (round9_q9 §3).
- E. Counterexample. It would need all of the following:
  - a varying complex structure;
  - twins at a non-product point of every walk chain;
  - |Aut(J_t)| < |Aut(J)|;
  - a relevant ≥ 2-dimensional α-fixed locus of 𝒳 (S40);
  - global realisation of the local deformations of Lemma Loc (round9_q9 Q-semi-global).
- F. Non-product extension of Theorem X′ (Steps 1–4). It is no longer needed by the chain below, because non-product endpoints are covered by MS10.

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No.
- No round-9 file proves MS8 (entry 68) or the goal.
- Every round-9 result on twins is conditional: (U″) under readings (R3)/(T4); (IP_Γ)/(NT_Γ); (Seal); (Star-K); alignment.
- No file refutes anything in the chain.

**Definitions** (as in earlier rounds).
- *Piece at time t*: a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_w M_w.
- M(E) and K(E) as before.
- *Chart at Q ∈ B_0*: Def(Q), the Kuranishi space of the stable curve Q, with plumbing coordinates s_e (e ∈ E(G_Q)) and quotient map q: Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g.
- *Vertices of G_Q* are labels. A label x is *intact* at p ∈ Def(Q) if s_e(p) = 0 for every edge e at x. Then F_x(p) is the corresponding component of the curve over p, with its special points.
- *Lifted branch*: a lift b̃ ∋ 0 of a branch b of B_0 at Q.
- *Transport family* of b̃: Ñ_b̃ := the connected component, containing b̃ ∖ {0}, of q^{-1}(H((b ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε) ⊂ Def(Q) × Δ_ε, where B is a small Aut(Q)-invariant ball.
- *x is Y-persistent along b̃*: at every (p,t) ∈ Ñ_b̃, x is intact at p and F_x(p) ≅ Y_t as n_i-pointed curves (some ordering).
- *Product-type stratum*: ξ_G is injective on coarse spaces.

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

**Tried so far** (on MS10 and its earlier wordings MS8 = entry 68, MS6, MS5 = entry 40, (T0) = entry 28, (C-merge)/(H1); the twin claim (TW*) is MS10's predecessor):

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 | — | (H1) isolated |
| round4_q7 §C | local analysis | (C-merge) not derivable locally |
| round5_q1–q4, q9 | conditional pinning under (T0) | heuristics |
| round5_q5 | analytic half | T′, V |
| round5_q8 | cyclic constructions | twin gap found |
| round6_q1, q2, q3, q8 | closing on MS5 | MS5 fails for the singular quintic; Krull/twin pinning |
| round6_q4 | refute MS5 | Picard surface |
| round6_q6 | multi-scale | Lemma D, Theorem 4 |
| round6_q9 | Jenkins–Strebel rays | Lemma PA, Prop K |
| round7_q1, q2, q3, q8 | closing on MS6 (no-twin transport) | MS6 under (NT)/(NT*); continuity principle (gap) |
| round7_q4 | refute MS6 | Theorem C |
| round7_q5 | twin-robust transport | (NT) case; chart-local twin model |
| round7_q6 | time-t open/closed | Theorem T under (Lock) |
| round8_q1 | closing on MS8; Teichmüller-disc limits | Theorem X; MS7* |
| round8_q2 | Stein factorisation | Lemma U; trichotomy; Theorem S under (NB) |
| round8_q3 | analytic Y-locus | Theorem N; Cor. T |
| round8_q8 | transport families, isotropy | Theorem 1 under (SC); (IP) |
| round8_q4 | refute MS8 | no counterexample; Theorem 2V |
| round8_q5 | Aut(J) fixed points, covering lemma | Theorems A/B under (U_J); Prop D |
| round8_q6 | Minsky/Antonakoudis crossings | (CR) ⇐ (PC) |
| round8_q7 | statements only | Lemma S, junction lemma |
| round9_q1 | closing on MS8 (copy-free, Krull in every sheet at one lift) | Theorem 1 dichotomy; (Seal) reformulation (MS9) |
| round9_q2 | closing on MS8 (lift-curves, star) | SC all-or-nothing; Prop 4; (Star-K) |
| round9_q3 | closing on MS8 (pole function; product strata) | Theorem X′; Lemma PT; Prop CN; Count lemma; twins confined to non-product points |
| round9_q7 | closing on MS8 (components of ℬ, Baire alignment) | Lemmas T/S/J; Theorem R (aligned ⇒ pinned) |
| round9_q4 | crossing step + same-sheet | Theorem X*; walk chain K_w |
| round9_q5 | twin step via α-fixed loci + total geodesy (Lemma TG) | (U″) suffices; (C) harmless; (A2)/(B)/(D3) open |
| round9_q6 | twin step via the 3-fold 𝒳 and Γ-orbits | (IP_Γ) suffices; Step 4 open |
| round9_q8 | persistent/endpoint twin obstruction | partner lemmas; no realisation |

## Target for round 10

**Progress test.** Rounds 8 and 9 produced progress on the chain.
- Round 9 proved results that hold for every admissible object and shorten the chain:
  - the walk chain K_w (entry 85);
  - Theorem X′/X* without Q-factoriality (entry 84, two independent proofs);
  - Lemma PT (entry 86);
  - Lemmas T/S/J with Theorem R (entry 87).
- Together they eliminate the crossing obstacle and every product-type point. The missing statement MS8 (twins and crossings, everywhere) is therefore replaced by the strictly simpler MS10: twins only, at points of non-product strata, between two branches joined inside one chart. The chain has been re-derived above.
- Honest caveat: MS10 is still the core twin problem that has resisted rounds 7–9. Only the surrounding obstacles fell.

**Wave (escalation rule, new wording of the missing statement), 10 attempt queries:**
- q1, q2, q3: the closing task on MS10, byte-identical. Spliced in:
  - PR-H;
  - R7-3, R7-4;
  - R8-2 §1–3, R8-1 §3–4, R8-3 §0–4.1;
  - R8-5 §1–6, R8-8 §0–4;
  - round9_q4 §1–3, round9_q3, round9_q7 §1–5, round9_q5 §0–4, round9_q6, round9_q2 §1–4, round9_q1 §1–3, round9_q8 §1–2;
  - the chain and the sketch.
- q4: refute MS10 exactly as stated (new wording), by an explicit configuration with an admissible family, or by deriving something known to be false.
- q5: mechanism B, level structures. Prove a Serre-type lemma for stable curves; pass to M̄_g[m] and reduce MS10 to triviality of the lifted family, or prove it.
- q6: mechanism A, the hardest step of the sketch, cut out: a relevant ≥ 2-dimensional α-fixed component Φ through (Q,0) forces α into the stabiliser of the lift of Q_τ in closure(Ñ_β̃) (settle round9_q5 O1″–O3″).
- q7: mechanism C, counting. Conservation of the number of Y-copies along the lift-curves in 𝒳 versus the Count lemma.
- q8: statements only. MS10 plus the statements of the entries the chain cites. First derive the goal from MS10, then attack MS10 by a first move none of the listed attempts used.
- q9 (elsewhere 1): entry 82 (Rig) via exclusion of orbifold type-jumps at t = 0 for Teichmüller pieces, using the global family; or realise Prop X as a boundary piece.
- q10 (elsewhere 2; chain check): check Proposition K_w (entry 85), which no separate query has checked and on which the chain rests.
