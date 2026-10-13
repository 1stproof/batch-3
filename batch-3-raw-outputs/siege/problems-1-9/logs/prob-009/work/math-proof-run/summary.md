# Running summary after round 13 (written at round 14 plan; round 14 is the FINAL round)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. Setting: V_t is a holomorphic, smoothly trivial family deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii). Claim: if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After thirteen rounds (108 queries) there is **no proof under the run's adopted coarse reading (R1)+(R2), and no counterexample.** There IS a complete conditional proof under the orbifold reading (R1)+(R2^orb), now written out in full (round13_q10) with its main ingredient Theorem RO independently verified (round13_q9). Round 13 (10 queries, all screened OK) produced:
- round13_q5: **(NRT) ⇒ MS8** — the twin problem is reduced to a single pointwise statement at puncture points (Lemma 2: (NRT) at Q ⇔ C_Φ(L) is Aut(Q)-invariant). This replaces MS11♭ as the missing statement. Rests on inherited inputs, not separately checked.
- round13_q9: verification of round12_q9 (CS, CL, J0, Lemma 1.1, Prop. T, R*′, Theorem RO) — correct after three minor repairs (R1′ finite type via Chow; R2′ level subgroups in genus 0/(1,1); R3′ Aut(G)-relabelling in non-product strata). Prop. C's non-product clause is only a sketch.
- round13_q10: full write-up of the conditional theorem; new Theorem LG (the chart-level local orbifold reading implies the global lift (a)–(d)), Prop. 3.3 (under (R2^orb), Aut(Q_t) ≅ Aut(Q) and the lift locus is one curve), Prop. 4.3 (MS11♭ at every puncture point under (R2^orb)).
- round13_q4, q1, q3, q6: the planner's "side-swap" mechanism fails locally: chart models (consistent with (R1),(R2)) of the rigid-twin reflection exist; the lost swap is carried at t ≠ 0 by an interior curve of symmetric smooth curves (the "detaching mirror"). Lemma R / Lemma FC / Prop. D (case I/II, k ∤ M ⇒ case I) / Prop. G (global family 𝒟 of symmetric curves) / Lemma Z.
- round13_q7: Lemma 2.4 (NG): no argument from t = 0 data alone can prove MS11♭ or (NRT) (the trivial family violates the t = 0 conclusion at terminal transitions).
- round13_q8: Proposition V (pointwise, H-free sufficient condition for (Rig) of a product-type piece family) and Lemma RH; correction: Prop. C's "every g" form is false.
- round13_q2: audit only (no new mathematics).

## Readings adopted (must be stated in any proof)
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- **(R2)** There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, preserving every stratum, H_0 = id (round2_q1, round3_q1). Coarse reading: H_t need not preserve automorphism groups.
- **(R2^orb)** (round12_q9 §1; round13_q10 §0) adds, for every boundary stratum G, a continuous H̃: Ã_0 × Δ → T_G with (a) H̃_t lifts H_t, (b) Mod_G-equivariance, (c) isotropy preserved, (d) H̃_0 = id. **Theorem LG (round13_q10 §6):** this global form follows from the natural chart-level local orbifold reading (Loc) (local continuous lifts with s-constant stabilisers), so (R2^orb) is a faithful formalisation of "smoothly trivial family of sub-orbifolds". It is strictly stronger than (R2): it forbids isotropy drop at boundary points (round13_q10 §7 example). NOT adopted as the run's formalisation of the posed claim, because "subvariety of M_g" literally refers to the coarse space and the run fixed the coarse reading in round 2; the final document must present the (R2^orb) result as a conditional theorem under a stated reading and argue the reading honestly (round13_q10 §7).
- **Index i** fixed via Baire (round4_q5 §1). **Smoothness of V_0** is needed (singular quintic, round6_q3). (R3),(T4) not needed (round11_q9 §1.1).

## Standing results (never drop; [mem] = classical result cited from memory by workers)
- **S1 (entries 2, 19).** t ↦ Y_t is holomorphic; goal ⇔ Y_t in a countable set for t accumulating. **S1′ (34).** Goal ⇔ ∂V_t ∩ ∂V_0 ≠ ∅ for t accumulating.
- **S2 (3, 23).** (ii) is tautological along Γ and coarser strata; content only at isolated deeper points.
- **S3 (4, 35), S3′ (93).** No argument local to ∂V_t / boundary points works (forgetful-fibre family in M_{0,7}; Lemma Loc).
- **S4 (8, 9).** Topological data are blind to Y_t.
- **S5 (5, 107).** If uncountably many V_t are totally geodesic, the claim holds [countability, mem].
- **S6/S6′ (14, 24).** Pinning lemma; incidence transport. **S7 (15), S7′ (94).** Royden domination; Kobayashi lemmas. **S8 (25).** Krull second branch.
- **S9 (20, 121).** Claim holds if [closure V_0] is isolated/reduced in the Douady space. **S10 (21, 33).** Imayoshi–Shiga pinning; a counterexample needs a varying complex structure. **S11 (22).** Countably many isomorphism classes ⇒ claim.
- **S15 (31, 32, 45).** Lemma T′, Lemma V, Lemma PA (constant vertex carries no area; positive area at a Teichmüller vertex).
- **S17–S19 (36, 37, 43, 44, 49, 60).** Covering-construction special cases; the singular quintic; Picard surface.
- **S20 (54, 56, 57).** L1/L1′; L2 for product type; time-t criterion.
- **S25 (70).** (F2), Theorem TV (every piece has a Teichmüller vertex, E^ν = H/Λ_E) — round8_q10; NOT independently re-checked (round13_q9 lists it as a dependency).
- **S26/S27 (71, 72).** Lemma U; generic-time trichotomy under (Rig).
- **S29–S33 (74–81).** Theorem 2V; MS8 under (U_J)/(Lock), (SC)/(NT)/(IP), (NB); Lemma Red, P0, Theorem B; Examples Z, Z′ (piece-level (Rig) false).
- **S34 (85, 98).** Walk chain Prop. K_w with repairs; Lemma S̃′. **S35–S44 (84, 86–92, 97, 99).** Theorem X*/X′/X*_all, Lemma PT, Lemmas T/S/J/Theorem R, Cor. IMOV_all, etc.
- **S45 (112).** B1♭ (anchored sheets) and the Gap A repair. **S46 (102).** Incidence propagation; counting no-go; Theorem Q.
- **S47 (103, 122).** Logical status: under (Rig), MS10/MS11/MS11♭ (and (NRT)) are each equivalent to the claim.
- **S48–S50 (104–107).** Level structures give nothing; Lemma D3; Lemma 3.1; Lemma CD.
- **S51 (113).** Chain check: MS11♭ + listed entries ⇒ MS8 (round11_q9). Now superseded on the main line by S68 but still valid.
- **S52 (114).** P(T) = C(L); MS11♭ fails only if Q_t has ≥ 2 lift-curves; holds under (R2^orb).
- **S53–S58 (115–121).** Mechanism D; twin-free closure; rigid twin at the endpoint; local (β)-models; Lemma HQ, Prop. MP/DP; Lemma TR.
- **S59 (125; verified round13_q9).** Lemma J0 (+CS, CL): at t = 0 the vertex map of every piece lifts holomorphically to T_G over H/Λ_E, isometric Teichmüller coordinate, coset monodromy. Correct with repair R3′; conditional on TV/Φ̂/PA.
- **S60 (126; verified round13_q9).** Theorem RO [orb]: under (R2^orb), (Rig) holds in every stratum with M, K constant and finite puncture values. Correct after R1′, R2′; conditional on TV/Φ̂/PA and Imayoshi–Shiga [mem] (for (1,1),(0,4) vertex types replaceable by classical rigidity).
- **S61 (127, RETRACTED this round → S70).** Prop. C: valid only for product type with lifts into T_{M(E_0)}; subsumed by Prop. V.
- **S62 (128, 149) — CONDITIONAL THEOREM.** Under (R1) + (R2^orb), Y_t = Y_0. Written out in full in round13_q10 (Lemma 3.1: t ↦ Q_t holomorphic at puncture points; Lemma 3.2: Stab_{Mod_G} ≅ Aut; Prop. 3.3: one lift-curve; Lemma 4.1: every anchored sheet contains a lift-curve; Lemma 4.2: P(T) = C(L); Prop. 4.3: MS11♭ at every puncture point; then Theorem RO + walk chain). With Theorem LG, the hypothesis can be the local orbifold reading. **This is the centre of the final document if the coarse goal is not reached.** Relative to inherited inputs (walk chain, Theorem N, TV/Φ̂/PA, Imayoshi–Shiga).
- **S63 (129–132).** Lemma A, F, G1–G2; Props. B/G4; Lemma G1 (round12_q2, q6, q1, q3).
- **S64 (133).** Φ-reformulation (round12_q7). Its unchecked substitution is now replaced by S68.
- **S65 (134).** (γ°) forces a frozen twin; Y(Δ) ⊂ pr_u(K_W).
- **S66 (135).** Twin points satisfy 2(2g_i−2+n_i) ≤ 2g−2; problem vacuous for g = 2; a counterexample needs g ≥ 3.
- **S67 (136).** Twin-free walk; needs smoothness.
- **S68 (138; new, round13_q5) — Φ-chain.** Lemma 1 (each Y_0-copy along a lift-curve in a boundary-type sheet has value branch in Φ or ≡ Y_0), Lemma 2 ((NRT) at Q ⇔ C_Φ(L) Aut(Q)-invariant ⇔ independent of L), Lemma 3 (P_Φ(T) = C_Φ(L)), Prop. 4 (under (NRT): Φ-persistence passes between any two boundary-type anchored sheets at Q, any branches, product or not), Lemma 5 (Φ-transfer along a piece; the tracked branch may change within one irreducible value curve, never becomes rigid). Hence **(NRT) at puncture points + (R1),(R2),(Rig) + Y non-constant ⇒ contradiction, i.e. (NRT) ⇒ MS8.** Uses (I1)–(I6) (lift-curves one Aut(Q)-orbit; every anchored sheet contains a lift-curve; equivariance; Lemma U; round12_q7 Lemma 1.1; walk-chain skeleton with entries 85, 98, 99, B1♭, §2.7 transfer set-up) as stated, not re-derived; not yet checked by a separate query.
- **S69 (142–145; new).** Reflection-case structure: Lemma R (q4), Lemma FC (q3), Lemma E, Prop. D, Prop. G (q6): in the reflection case with smooth 3-fold component, either the mirror is a pointwise-fixed anchored sheet (case I; forced if k ∤ M) or V_t contains a curve of smooth a-symmetric curves converging to c (case II, "detaching mirror"); Lemma Z (under (T4)): V_0 ∩ Z_g components are Teichmüller curves; Lemma 2.4 (NG, q7): t = 0 data alone cannot prove MS11♭/(NRT).
- **S70 (146; new, round13_q8).** Prop. V: for a product-type piece, (Rig) for its family ⇐ for uncountably many t: (i) Teichmüller-vertex image = C, (ii) source map orbifold-unramified, (iii) joint map lifts over pulled-back orbifold. Lemma RH: under (Rig-v), punctures j-degenerate, total ramification constant, ramification over orbifold points upper semicontinuous; (ii) fails only by ramification drifting off orbifold fibres (fixed-image (ram) mechanism, locally consistent).
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12–S14, S16, S23, S28 (entries 26, 29, 30, 46–48, 50, 58, 59, 64, 65, 73); entry 66; round10_q2 Lemma 4.1/Prop. P1.

## Dead ends (REFUTED precise statements only)
- MS5 without smoothness/closedness is false (entry 43; round6_q2).
- Map-level Lemma R* without (O) is false (entry 64; round7_q7).
- Piece-level (Rig) is false (entry 81; round8_q9).
- "A transport family is irreducible" is false (entry 101; round10_q7).
- Lemma B1(a),(b) of round10_q3 are false (entry 110; round11_q9).
- "g ∈ G_X fixing S × {0} pointwise fixes L_0" is false locally (entry 131; round12_q2).
- Acyclicity of the t = 0 restart graph without smoothness is false (round12_q10 §3.2, sketch).
- **New:** the side-swap mechanism (round-13 sketch item 3) as a local argument is false (entry 142; round13_q4 §1, also round13_q1 §2, round13_q3 §1, round13_q6 §3).
- **New:** Prop. C's "every g" form of (T_c) is false when a constant vertex moves off an orbifold point (round13_q8 §1; entry 147).

## Open gaps (routes set aside, not refuted)
- **A. (NRT_P) under the coarse reading** (entry 141) — the missing statement. Residual sub-obstructions: the detaching mirror (case II, (NRT-Z) of round13_q4 §4, Prop. G of round13_q6); moved branches in case I (q6 Cor. D1); sheet-moving lost automorphisms; non-smooth 3-fold (hypothesis (Sm)/(H2) failing); the (γ°) and endpoint origins (no Lemma R input).
- **B. (Rig) under the coarse reading** (entry 82). By Prop. V: (Rig-v), no fixed-image ramification drift, no joint cone points, for uncountably many t; non-product strata (twin ambiguity) untreated.
- **C. Rigidity of V_0 itself** (Douady isolation). If smooth totally geodesic surfaces admit no admissible deformation, the claim is vacuous; no such theorem is known (round13_q1 §3, q2 §2).
- **D. Counterexample.** Needs g ≥ 3, a twin point with a lost automorphism (isotropy drop), a rigid twin, varying complex structure, a global nontrivial deformation; none constructed.
- **E. Reading question.** Settled mathematically by Theorem LG (local orbifold reading ⇒ (R2^orb)); what remains is interpretive.
- **Other routes set aside:** counting; level structures; arithmetic; Kobayashi; persistence of Teichmüller curves; multi-scale; Hodge rigidity; Douady first order; psh-isolation; twin-free route (needs smoothness); Teichmüller-disc degeneration at t = 0 (closed by NG, round13_q7 §2.2).

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No, not under the run's formalisation (R1)+(R2). Under (R1)+(R2^orb) a complete conditional proof is in hand (S62, round13_q10), but (R2^orb) is a strictly stronger hypothesis, so it is recorded as an ordinary PROVED line, not as the [GOAL]. No round-13 file proves (NRT) or (Rig) under the coarse reading, and none refutes anything in the chain.

**Definitions** (as in the round-13 task files). Piece at time t = 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G); chart Def(Q) with plumbing coordinates s_e, q: Def(Q) → Def(Q)/Aut(Q); labels = vertices of G_Q; transport family Ñ_c̃; anchored sheet T of c̃ = irreducible component of closure(Ñ_c̃) containing c̃ × {0}; boundary-type = Q not in the stratum of c; lift-curve = irreducible component through (0,0) of {(p,t): q(p) = Q_t}, Q_t := H_t(Q); puncture point = Q ∈ B_0 having a branch c of B_0 at Q with c ∖ Q in a stratum other than that of Q; Φ = finite set of local branches at t = 0 of the constant-vertex value curves Γ_{W,u} (W a component of a lifted piece family, u a constant vertex of W of type (g_i,n_i)) through (Y_0, 0) that are non-constant (Y ∈ Φ when Y is non-constant); C_Φ(L) = labels whose class along L lies on a branch in Φ.

**Chain** (statements only).
1. Goal ⇐ MS8 + (Rig) (entry 82) + entry 19. (MS8: under (R1),(R2),(Rig), Y is constant; entry 19 turns this into Y_t = Y_0.)
2. MS8 ⇐ (NRT_P) (entry 138, round13_q5 §4): assume Y non-constant.
   (a) walk chain (entries 85, 98, 112) with transitions J_m, lifts β̃_m, β̃′_m, labels x_m, endpoint (Q_0, β̃, b̃, x), x MERGE or MOV along b̃ at t = 0; (P) at every genuine transition and at the endpoint (entry 99); interior transitions trivial.
   (b) Induction (C_m): x_m ∈ P_Φ(T) for an anchored sheet T of β̃_m. Base: vertex i on ∂V_0's lifts, φ_1 = Y. Puncture transitions (any type): (NRT_P) at J_m ⇒ (Lemma 2) C_Φ(L) independent of L ⇒ (Lemma 3, Prop. 4) x_m ∈ P_Φ(T′) for every anchored sheet T′ of β̃′_m. Transfer along D^{m+1}: Lemma 5.
   (c) Endpoint: (NRT_P) at Q_0 + Prop. 4 ⇒ x intact along b̃ with F_x ≡ Y_0 ⇒ contradiction with MERGE/MOV.
3. What remains after (NRT_P): (Rig) (entry 82), open under (R2); by Prop. V (entry 146) it follows for a product-type piece family from conditions (i)–(iii) at uncountably many t; non-product strata untreated. Under (R2^orb) both (NRT_P) and (Rig) hold (S62).

**Missing statement (NRT_P)** (OPEN, entry 141, locator round14_plan; replaces MS11♭ = entry 124 and the round-13 wording (NRT) = entry 137).
- *Setting.* g ≥ 2. V_0 ⊂ M_g smooth, closed, 2-dimensional, totally geodesic for the Teichmüller metric. V_t (t ∈ Δ) a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2) with H_0 = id (coarse: H_t need not preserve automorphism groups; V_t not assumed totally geodesic for t ≠ 0). Δ_Γ ≅ ∏_j M_{g_j,n_j} of product type, dim ∂V_t = 1, π_i(∂V_t) = {Y_t} for all t, dim M_{g_i,n_i} > 0. (Rig): a finite set 𝒦 of triples (G, M, K) (M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not in the boundary) such that every piece at every time has its triple in 𝒦 up to Aut(G). t ↦ Y_t non-constant. Φ as defined above.
- *Claim.* There do not exist: a puncture point Q ∈ B_0; an automorphism a ∈ Aut(Q); a lift-curve L of Q_t; a label x of G_Q; such that for all small t ≠ 0, along L the component x is intact with class on a branch φ ∈ Φ, and the component a^{-1}x is intact with F_{a^{-1}x} ≅ Y_0.
- Equivalent form (entry 138, Lemma 2): at every puncture point Q, C_Φ(L) is Aut(Q)-invariant for one (equivalently every) lift-curve L.
- Under (Rig) it contains "Y non-constant", so it is vacuously true if the claim is; a counterexample to it is a counterexample to the problem (as for MS11♭, entry 122). A failure needs isotropy drop: a ∉ Stab(L), so Q_t has ≥ 2 lift points and |Aut(Q_t)| < |Aut(Q)|.

**Why it should hold (planner's sketch; new decomposition this round).**
1. *Case split (from round13_q5 Lemma 1, step 2).* Let L ⊂ T, T a boundary-type anchored sheet of c̃ with lifted piece family component W. Then x is a constant vertex u of W with Γ_{W,u} ∋ φ non-constant, and the rigid copy y = a^{-1}x is either (A) a constant vertex v of W with Γ_{W,v} ≡ {Y_0} × Δ (irreducibility of Γ_{W,v}), or (B) a component of a coordinate of a point of the finite t-independent set F_W = K_W ∩ ∂, i.e. Y_0 is a component of a cusp value of the moving part K_W.
2. *a must move T and L* (Lemma E / Cor. E1 of round13_q6, and C_Φ(aL) = aC_Φ(L)): aT ≠ T is an anchored sheet of ac̃, a lift of the same coarse branch c, with lifted family σW for the induced σ ∈ Aut(G_c). So in case (A) a failure needs the coarse piece family 𝒞 = H(c × Δ) to have two distinct lifted components W ≠ σW through the same t = 0 lifted piece (if σW = W with σ exchanging the vertices u, v, then Γ_{W,u} = Γ_{W,v}, impossible since one is non-constant and the other ≡ Y_0). Conjecture (A): this "split lifted family" is impossible for a boundary piece of a totally geodesic smooth V_0 — because at t = 0 the generic curve of c_0 carries both constant Y_0-vertices, and total geodesy (Lemma J0: the vertex map of c_0 lifts over the Veech orbifold with coset monodromy; Lemma TG/Z: symmetric loci meet V_0 in Teichmüller curves or points) should force the swap to act on the whole lifted family, not just at Q.
3. *Case (B):* Y_0 ∈ 𝔉_W means the constant value Y_0 of vertex x on c_0 equals a component of a cusp of the moving image K_W. Conjecture (B): the a-exchange at Q of an intact constant Y_0-vertex with a component of a degenerate moving vertex contradicts Lemma PA/V (constant vertices carry no area, the moving Teichmüller vertex does) when read along the Teichmüller discs of V_0 approaching Q from the sheets c̃ and ac̃ — but by Lemma NG (round13_q7) such a t = 0 argument must be combined with a t ≠ 0 input (Theorem N for φ, the frozen value of y).
4. *Reflection sub-case* (a fixes c̃, aS = S): Lemma R / Prop. D reduce to excluding the detaching mirror (case II, needs k | M) and moved branches; a possible global input is a negativity/homology argument for the family 𝒟 of symmetric curves (round13_q6 Prop. G). Speculative.

**Tried so far** (on (NRT_P) and its earlier wordings (NRT) = entry 137, MS11♭ = entry 124, MS11 = 109, MS10 = 96, MS8 = 68, MS6, MS5 = 40, (T0) = 28, (H1)):

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 – round5 (q1–q5, q8, q9) | incidence/pinning under (T0) | heuristics, T′, V, twin gap |
| round6_q1–q4, q6, q8, q9 | closing / refuting MS5; multi-scale; JS rays | MS5 false for singular quintic; Krull pinning; Lemma PA, Prop K |
| round7_q1–q6, q8 | closing / refuting MS6; twin-robust transport | MS6 under (NT)/(Lock); chart twin model |
| round8_q1–q8 | closing / refuting MS8; Stein factorisation; Y-locus; transport isotropy; crossings | Theorem X, Lemma U, trichotomy, Theorem N, (SC)/(IP), (U_J), Theorem 2V |
| round9_q1–q8 | copy-free; star; pole function; components of ℬ; walk chain; α-fixed loci; Γ-orbits; endpoint | X*, K_w, Lemmas T/S/J, Theorem R, (U″), (IP_Γ), partner lemmas |
| round10_q1–q8, q10 | closing/refuting MS10; level structures; trace; counting; arithmetic; chain check | X*_all, IMOV_all, gaps A/B, counting no-go, Lemma S̃′ |
| round11_q1–q9 | closing/refuting MS11 (Mechanism D); Douady; Grothendieck; chain check | B1 false; anchored sheets; rigid twin; chain correct with MS11♭ |
| round12_q1–q8, q10 | closing MS11♭ (Mechanism G); refute; LC; (β)- and (γ°)-obstructions; twin-free walk | Lemma A/F/G, Prop. B/G4; Φ-reformulation; (γ°) frozen twin; g ≥ 3; twin-free needs smoothness |
| round13_q1, q2, q3 | closing on MS11♭ with side-swap sketch | side-swap fails locally (Model R); Lemma FC; audit |
| round13_q4 | (NRT) hardest step: rigid-twin reflection | chart model; Lemma R; Lemma Z/Prop. Z; reduction to (NRT-Z) |
| round13_q5 | Φ-chain: (NRT) ⇒ MS8 | proved (Lemmas 1–3, Prop. 4, Lemma 5); (NRT) ⇔ C_Φ(L) invariant |
| round13_q6 | reflection obstruction (Refl) | Lemma E, normal form, case I/II (k ∤ M ⇒ I), Prop. G |
| round13_q7 | statements only; Teichmüller-disc degeneration at t = 0 | lift-curve form (Lift); NG: t = 0 data cannot suffice |

## Target for round 14 (FINAL round)

**Progress test.** Rounds 12–13 produced progress on the chain in the counted sense: round13_q5 replaced the missing statement MS11♭ (a sheet-to-sheet transfer statement between distinct lifted branches, with hypotheses (P), (S)) by the strictly simpler pointwise statement (NRT_P) (one puncture point, one lift-curve, one automorphism, one label; equivalently Aut(Q)-invariance of C_Φ(L)), and re-derived the chain (NRT_P) ⇒ MS8 in full. Caveat: that derivation rests on inherited inputs (I1)–(I6) and has not been checked by a separate query; one query of this wave checks it. (Rig) (entry 82) is still open on the coarse side; Prop. V weakens the sufficient condition but does not prove it.

**This is the final round:** whatever returns goes to the proof-writing steps. No complete coarse proof is in hand, so no DONE file and no goal change (the goal is the posed claim; there is no proved goal to come back to). The wave (10 queries, all "kind: attempt"):
- q1–q3: identical closing task on (NRT_P) (compact: statement, the Φ-chain of round13_q5, round13_q4/q6/q3 reflection results, round12_q7/q8, Lemma U/Theorem 1, Theorem N, round11_q4, round12_q6, round11_q9, Lemma TG spliced; sketch above).
- q4: refute (NRT_P) exactly as stated (first time posed in this wording): global construction or derivation of a falsity.
- q5: the hardest step of the sketch, cut out: case (A) (split lifted family) and case (B) (Y_0 a cusp component of K_W), as a self-contained claim.
- q6: the obstruction raised by round13_q4/q6: exclude the detaching mirror (NRT-Z / Prop. G family 𝒟) globally, or sharpen it into a counterexample.
- q7 (elsewhere 1): (Rig) under coarse (R2) via Prop. V: exclude fixed-image ramification drift and joint cone points; non-product strata.
- q8 (the one chain check): independent step-by-step check of round13_q5's derivation (NRT_P) ⇒ MS8 against its inputs.
- q9, q10 (final-round allowance: verify standing results the final document presents): q9 independent verification of the conditional theorem as written in round13_q10 (Lemma 3.1, 3.2, Prop. 3.3, Lemma 4.1, 4.2, Prop. 4.3, Theorem LG, use of Theorem RO and the chain); q10 verification of Theorem TV / Corollary Φ̂ (round8_q10) and Lemma PA (round6_q9), the unchecked dependencies of Lemma J0 and Theorem RO.

**For the final document** (if nothing coarse returns): build it around S62 (conditional theorem under (R2^orb), with Theorem LG and the reading discussion), S60/S59 (verified), the coarse reduction "(NRT_P) + (Rig) ⇒ claim" (S68 + chain), Prop. V (S70), the necessary conditions for a counterexample (S66, isotropy drop, S69), and the no-go results (S3, S3′, S4, NG). Present the coarse claim honestly as not established.

**Ledger numbers of this round's block:** 138 Φ-chain; 139 RETRACT 124; 140 RETRACT 137; 141 OPEN (NRT_P); 142 REFUTED side-swap; 143 Lemma R/FC/Z; 144 Lemma E/Prop. D/G; 145 NG; 146 Prop. V/RH; 147 RETRACT 127; 148 verification of round12_q9; 149 conditional theorem write-up + Theorem LG. [GOAL] still entry 1 (OPEN); (Rig) still entry 82 (OPEN).
