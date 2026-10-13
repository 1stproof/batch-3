# Running summary after round 12 (written at round 13 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. Setting: V_t is a holomorphic, smoothly trivial family deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii). Claim: if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After twelve rounds (98 queries) there is no proof under the run's adopted (coarse) reading and no counterexample. Round 12 (10 queries, all screened OK) produced:
- **A complete conditional theorem under the orbifold reading.** round12_q9 proved Theorem RO: under (R2^orb), formalised as an equivariant, isotropy-preserving lift of H on every boundary stratum, (Rig) holds in every stratum with M and K constant. Combined with entry 114 (MS11♭ holds under (R2^orb)) and the chain (entry 113, step 1), this proves the problem's claim under (R1) + (R2^orb). The combination has not yet been checked by a separate query.
- **Reductions of MS11♭ under the coarse reading** (round12_q1, q2, q3, q5, q6, q7, q8). Lift-curve structure (Lemma A); K_S- and Stab(b̃)-elements are harmless (Prop. B, Prop. G4, Lemma F); planner step 4 is false locally; the Φ-reformulation reduces (β)-twists to the rigid-twin case (q7); (γ°) forces a frozen twin and Y(Δ) ⊂ pr_u(K_W) (q8).
- **Twin-free route limits** (round12_q10). Necessary conditions on twin points (round12_q4: g ≥ 3).

## Readings adopted (must be stated in any proof)
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- **(R2)** There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ. It is smooth on V_0 × Δ, preserves every stratum, and has H_0 = id (round2_q1, round3_q1).
  - This is a Thom–Mather-type strengthening of the literal (i)/(ii).
  - It is the coarse reading: H_t need not preserve automorphism groups.
- **(R2^orb)** (round12_q9 §1) adds the following, for every boundary stratum G: a continuous H̃: Ã_0 × Δ → T_G = ∏_w T_w with
  - (a) H̃_t lifts H_t;
  - (b) H̃_t is Mod_G-equivariant;
  - (c) H̃_t preserves isotropy groups;
  - (d) H̃_0 = id.

  This is the natural reading if "smoothly trivial family of submanifolds" is meant in the orbifold category. It is NOT adopted as the run's formalisation of the posed claim, for two reasons:
  - "subvariety of M_g" literally refers to the coarse space;
  - (R2^orb) is a strictly stronger hypothesis: it forbids V_t from leaving a symmetric locus that contains V_0.

  round12_q9 flags a gap in the interpretation, not in the proof: whether the purely local formulation (isotropy-preserving local lifts) implies the global lift (a)–(d). The final document must present the (R2^orb) result as a conditional theorem under a stated reading.
- **Index i.** The fixed index i is recovered by a Baire argument (round4_q5 §1).
- **Smoothness of V_0.** "Smooth" is needed: the quintic test surface is singular (round6_q3).
- **(R3), (T4).** These extra readings are no longer needed (round11_q9 §1.1).

## Standing results (never drop; [mem] = cited from memory by the workers)
- **S1 (entries 2, 19).** t ↦ Y_t is holomorphic. So the goal holds iff Y_t lies in a countable set for t in a set accumulating in Δ.
- **S1′ (entry 34).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No argument local to ∂V_t works. The forgetful-fibre family in M_{0,7} satisfies every hypothesis except total geodesy, and has Y_t non-constant.
- **S3′ (entry 93).** Lemma Loc: neither the goal nor (Rig) follows from local data at boundary points. Prop. TG.
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5).** If every V_t (or uncountably many) is totally geodesic, the claim holds [countability, mem].
- **S6/S6′ (entries 14, 24).** Pinning lemma; incidence transport.
- **S7 (entry 15), S7′ (entry 94).** Royden domination; Kobayashi lemmas.
- **S8 (entry 25).** Krull second branch at a cusp.
- **S9 (entry 20), S9′ (entry 121).** If the Douady germ is a reduced point, or [closure V_0] is isolated in the Douady space, the claim holds.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning; a counterexample needs a varying complex structure.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t ⇒ claim.
- **S12–S14, S16, S23, S28 (entries 26, 29, 30, 46–48, 50, 58, 59, 64, 65, 73).** Not on the current line, except as noted. These are: log-flow converse; Lemma R*; Theorem L; Theorems P/P′/P″; Krull/twin pinning; Prop. K; no-twin transport; Theorem X. Lemma R* is re-proved with coset monodromy as Lemma R*′ in round12_q9.
- **S15 (entries 31, 32, 45).** Lemma T′; Lemma V (a constant vertex never carries area); Lemma PA.
- **S17–S19 (entries 36, 37, 43, 44, 49, 60).** Covering-construction special cases; the quintic surface (singular); the Picard surface.
- **S20–S22 (entries 54–57).** L1, L1′; L2 for product G; time-t lemmas.
- **S24 (entries 61–63).** Structure of the obstruction.
- **S25 (entry 70).** (F2) in general; Theorem TV (Teichmüller vertex of every piece; E^ν = H/Λ_E).
- **S26/S27 (entries 71, 72).** Lemma U; the generic-time trichotomy under (Rig).
- **S29–S33 (entries 74–81).** Theorem 2V; MS8 under (U_J)/(Lock), (SC)/(NT)/(IP), (NB); Lemma Red, P0, Theorem B; Examples Z, Z′ (piece-level (Rig) false).
- **S34 (entries 85, 98).** Prop. K_w with repairs; Lemma S̃′.
- **S35–S42 (entries 84, 86–92).** Theorem X*/X′; Lemma PT; Lemmas T, S, J, Theorem R; copy-free dichotomy; lift-curves; (U″); (IP_Γ); partner lemmas.
- **S43 (entry 97).** Theorem X*_all. **S44 (entry 99).** Cor. IMOV_all.
- **S45 (entry 112).** B1♭ and the Gap A repair. Entry 110 (B1(a),(b)) is refuted.
- **S46 (entry 102).** Incidence propagation; counting no-go; Theorem Q.
- **S47 (entries 103, 122).** Logical status: under (Rig), MS10/MS11/MS11♭ are each equivalent to the problem's claim.
- **S48 (entries 104, 106).** Level structures give nothing new; Lemma D3.
- **S49 (entry 105).** Lemma 3.1 (the cusp leaves closure(V_τ)).
- **S50 (entry 107).** Lemma CD.
- **S51 (entry 113).** Corrected chain: MS11♭ + entries 19, 24, 84–87, 97–99, 112 ⇒ MS8, checked step by step in round11_q9.
- **S52 (entry 114).** P(T) = C(L). MS11♭ fails only if Q_t has ≥ 2 lift-curves. MS11♭ holds under (R2^orb).
- **S53 (entries 115, 116).** Mechanism D.
- **S54 (entry 117).** Twin-free closure, Criterion R, TFM.
- **S55 (entry 118).** Rigid twin at the endpoint.
- **S56 (entry 119).** Local (β)-models.
- **S57 (entry 120).** Lemma HQ; Prop. MP/MP′/DP.
- **S58 (entry 121).** Lemma TR.
- **S59 (new; round12_q9).**
  - Lemmas CS, CL: lifting lemmas.
  - **Lemma J0**: at t = 0 the whole vertex map of every piece, in any stratum, lifts holomorphically to T_G over the Veech orbifold H/Λ_E. Its Teichmüller coordinate is an isometry onto a disc, and its monodromy is coset-valued.
  - So Example Z is not a boundary piece of a totally geodesic V_0.
- **S60 (new; round12_q9) — Theorem RO [orb].** Under (R1), (R2), (R2^orb), with TV/Φ̂ of round8_q10 used as stated and Imayoshi–Shiga finiteness [mem]:
  - (Rig) holds;
  - M(E_t) = M(E_0) and K(E_t) = K(E_0) for every piece;
  - puncture values lie in a fixed finite set.

  Inputs: Prop. T (transport of the joint lift) and Lemma R*′ (coset monodromy, orientation reversal excluded).
- **S61 (new; round12_q9) — Prop. C.** Under coarse (R2), (Rig) follows from (T_c) for every piece. (T_c) asks that the joint vertex map of E_t lifts over the transported Λ_E orbifold with constant coset monodromy. Equivalently (α) no new cone points of the joint map at t ≠ 0, and (β) constant monodromy. A sketch shows (T_c) holds under (★_J), (★∞_J).
- **S62 (new) — CONDITIONAL THEOREM.** Under (R1) + (R2^orb), the problem's claim holds.
  - Derivation: (R2^orb)(c) gives |Aut(Q_t)| = |Aut(Q)| at boundary points, hence a single lift-curve, hence MS11♭ (S52). S60 gives (Rig). S51 and chain step 1 then give the claim.
  - This is the strongest result of the run and the centre of the final document if the coarse goal is not reached.
  - It still needs: a check of the combined derivation, and a re-check of round8_q10 TV/Φ̂ as used by Lemma J0.
- **S63 (new; round12_q2, q6, q1, q5, q3).**
  - Lemma A: lift points over unibranch points of 𝒳 = q(X) form one G_X-orbit; the lift-curves in X are G_X·L_0; (1L_X) ⇔ G_X ⊆ Stab(L_0). Lemma A4.
  - Lemma G1/G2: exact criterion; (1L_X) gives MS11♭ only if τ ∈ Stab(b̃)Stab(x).
  - Prop. B / Prop. G4 / Lemma F: elements of K_S (pointwise stabiliser of S) or of Stab(b̃) never cause failure.
  - Residual failure modes: (R-a) a lost automorphism acting non-trivially on S (a "reflection") or moving S; (R-b) an initial twist τ ∉ Stab(b̃)Stab(x).
  - q3 Lemma G1: g fixing S pointwise acts trivially on X unless X_0 is non-reduced along S. That happens only if V_t loses a generic automorphism of V_0's curves; it is impossible under the orbifold reading.
  - Lemma LC/Prop. LC′ (q5): an equivalent lift-curve form.
- **S64 (new; round12_q7) — Φ-reformulation.**
  - Φ is the finite set of non-constant constant-vertex value branches φ with φ(0) = Y_0.
  - Lemma 1.1: R8-2 Theorem 1 holds for every φ ∈ Φ off a discrete set.
  - Lemma 1.2: a constant twin on an anchored sheet carries one value branch, either in Φ or ≡ Y_0.
  - Prop. 2.1/Cor. 2.2: (β)-twists and the initial twist preserve Φ-persistence unless the twin is rigid.
  - Lemma 4.1: at the endpoint the merging label is rigid on every anchored sheet of b̃, and Y_0 ∈ 𝔉.
  - UNCHECKED: that the chain entries (PT, J/J′, transfer, P(T) = C(L)) hold verbatim with Y replaced by a varying φ.
- **S65 (new; round12_q8) — (γ°) made precise.**
  - (γ°) forces a moving twin u = g^{-1}x ∈ M_W with g c̃ ≠ c̃.
  - It forces a frozen twin along the lift-curve: F_u ≡ Y_0 and F_x ≅ Y_t.
  - Y(Δ) ⊂ pr_u(K_W), a fixed closed curve.
  - α-symmetry on K_W (Lemma 5).
  - Residual open statement (O-γ°′).
- **S66 (new; round12_q4).** Twin points satisfy 2(2g_i−2+n_i) ≤ 2g−2. The problem is vacuous for g = 2 (the only candidate stratum is not of product type), so a counterexample needs g ≥ 3. Shapes of twin points for g = 3.
- **S67 (new; round12_q10).**
  - Twin-free walk: (Term) ⇒ (MS-ray) ⇒ (MS-R) ⇔ (B𝒴), each sufficient under (Rig).
  - For the non-smooth quintic all these fail although the claim holds there (sketch, via admissible covers).
  - So any twin-free argument must use smoothness of V_0, persistence, or label-level data.
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; S13; S14; S23; entry 66; S28; S16; round10_q2 Lemma 4.1/Prop. P1.

## Dead ends (REFUTED precise statements only)
- **MS5 without smoothness/closedness is false** (entry 43; round6_q2).
- **Map-level Lemma R* without (O) is false** (entry 64; round7_q7).
- **Piece-level (Rig) is false** (entry 81; round8_q9).
- **"A transport family is irreducible" is false** (entry 101; round10_q7).
- **Lemma B1(a),(b) of round10_q3 are false** (entry 110; round11_q9, q2, q3, q8).
- **"g ∈ G_X fixing S × {0} pointwise fixes the lift-curve L_0" is false as a local statement** (round12_q2 §2, round12_q1 Model M1, round12_q3 §4, round12_q6 Model G3′). This was planner step 4. Likewise (1L_X) can fail through K_S. Both are harmless by Prop. B/G4.
- **Acyclicity of the t = 0 restart graph from total geodesy plus coarse network data is false** without smoothness (round12_q10 §3.2; quintic, sketch).

## Open gaps (routes set aside, not refuted)
- **A. MS11♭ under the coarse reading (entry 124).** Residual: rigid twins (q7, q8) and (R-a)/(R-b) (q6).
- **B. (Rig) under the coarse reading (entry 82).** Equivalent route: (T_c) (Prop. C), i.e. no new cone points of joint vertex maps at t ≠ 0.
- **C. Rigidity of V_0 itself** (Douady isolation, OQ-K).
- **D. Counterexample.** It needs g ≥ 3, a twin point with a lost automorphism, a rigid twin, a varying complex structure, and a global nontrivial deformation (none has ever been constructed).
- **E. The local-to-global question for (R2^orb)** (round12_q9 open 2). It is relevant to how the conditional theorem is presented.
- **Other routes set aside:** counting; level structures; arithmetic; Kobayashi; persistence of Teichmüller curves; multi-scale route; Hodge rigidity; Douady first order; psh-isolation; the twin-free route (needs smoothness: (O-sm), (O-TF), (O-cyc) of round12_q10).

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No, not under the run's formalisation (R1) + (R2).
- Round 12 did give a complete *conditional* derivation under the stronger orbifold reading (S62).
- (R2^orb) is a strictly stronger hypothesis than the coarse reading the run adopted. So S62 is recorded as an ordinary PROVED line, not as the [GOAL].
- No round-12 file proves MS11♭ or (Rig) under the coarse reading, and none refutes anything in the chain.

**Definitions.** Pieces, charts Def(Q), labels, transport families Ñ_c̃, anchored sheets, Y-persistence, lift-curves, product type, P(T), C(L): all exactly as in round12_q1's task (round-12 summary, "Definitions").

**Chain.** Every step is PROVED except MS11♭ and the separate open input (Rig), entry 82. The chain is unchanged from round 12.
1. **Goal ⇐ MS8 + (Rig) + entry 19.**
   - MS8: under (R1), (R2), (Rig), Y_t = Y_0 for all t.
   - Given (Rig), MS8 is the goal; entry 19 turns "Y constant" into Y_t = Y_0.
2. **MS8 ⇐ MS11♭** (entry 113, round11_q9 §5). Assume MS8's setting and, for contradiction, that Y is non-constant.
   - (a) **Walk chain** (entries 85, 98, with R(D) added to Σ by entry 112).
     - Pieces D^1 ⊂ ∂V_0, …, D^k; transitions J_m; endpoint Q_0.
     - At each J_m there are lifts β̃_m, β̃′_m in one irreducible component of q^{-1}(closure V_0) ∩ B (Lemma S̃′).
     - At Q_0: entering β̃ and terminal b̃ in one such component, with x MERGE or MOV along b̃ at t = 0.
   - (b) **(P) at genuine transitions and at the endpoint** (entry 99).
   - (c) **Induction:** x_m is Y-persistent on some anchored sheet of β̃_m.
     - Base: product-type Δ_Γ.
     - Product-type transitions: entries 86, 87.
     - Non-product transitions with β̃′_m ≠ β̃_m: MS11♭.
     - Transfer along D^{m+1}: entry 112, entry 87 Lemma S(c).
   - (d) **Endpoint.**
     - Product type: entries 86, 87 and 19.
     - Non-product: MS11♭ gives x intact with F_x ≡ Y_0 along b̃, contradicting MERGE and MOV.
3. After MS11♭, what remains is **(Rig)** (entry 82). Under coarse (R2) this is equivalent, by Prop. C (S61), to (T_c) for every piece. Under (R2^orb), both MS11♭ and (Rig) hold, and so does the whole claim (S62).

**Missing statement (MS11♭)** (OPEN, entry 124, wording unchanged). Verbatim as in the round-12 summary:
- *Setting.*
  - g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i) and (ii) in the readings (R1), (R2), with H_0 = id. V_t is not assumed totally geodesic for t ≠ 0, and H_t need not preserve automorphism groups.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type, ∂V_t has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - (Rig) holds: there is a finite set 𝒦 of triples (G, M, K) with M ⊂ V(G) and K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦 up to Aut(G).
  - **t ↦ Y_t is non-constant.**
- *Data.*
  - Q ∈ B_0 := closure(V_0) ∖ V_0 lies in a stratum Δ_{G_Q} NOT of product type.
  - B ⊂ Def(Q) is a small Aut(Q)-invariant ball, and ε > 0 is small. On B, the irreducible components of q^{-1}(closure V_0) ∩ B, of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) and of every closure(Ñ_c̃) are the components of the germs at the origin, and distinct lifted branches of q^{-1}(B_0) meet only at 0.
  - β̃ ≠ b̃ are two DISTINCT lifted branches through 0 of branches β, b of B_0 at Q (possibly lifts of the same coarse branch), with:
    - (P) Q is a puncture of the piece of β and of the piece of b (some s_e ≢ 0 on β̃, and likewise on b̃);
    - (S) β̃ and b̃ lie in one irreducible component S of q^{-1}(closure V_0) ∩ B.
  - x is a label of G_Q with F_x(0) ≅ Y_0 that is Y-persistent on some anchored sheet of β̃.
- *Conclusion.* x is Y-persistent on some anchored sheet of b̃. Hence, at t = 0, x is intact along b̃ with F_x ≡ Y_0.
- MS11♭ contains "Y non-constant". So any argument that derives a contradiction from its setting proves it (vacuously). Under (Rig), MS11♭ is equivalent to the problem's claim (entry 122).

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

**Tried so far** (on MS11♭ and its earlier wordings MS11 = entry 109, MS10 = entry 96, MS8 = entry 68, MS6, MS5 = entry 40, (T0) = entry 28, (C-merge)/(H1)):

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 | — | (H1) isolated |
| round4_q7 §C | local analysis | (C-merge) not derivable locally |
| round5_q1–q4, q9 | conditional pinning under (T0) | heuristics |
| round5_q5 | analytic half | T′, V |
| round5_q8 | cyclic constructions | twin gap found |
| round6_q1, q2, q3, q8 | closing on MS5 | MS5 false for singular quintic; Krull/twin pinning |
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
| round9_q2 | lift-curves, star | SC all-or-nothing |
| round9_q3 | pole function; product strata | X′; Lemma PT |
| round9_q7 | components of ℬ, alignment | Lemmas T/S/J; Theorem R |
| round9_q4 | crossing step + same sheet | X*; walk chain K_w |
| round9_q5 | α-fixed loci + Lemma TG | (U″) suffices |
| round9_q6 | 3-fold 𝒳, Γ-orbits | (IP_Γ) suffices |
| round9_q8 | endpoint twin obstruction | partner lemmas |
| round10_q1, q2, q3 | closing on MS10 | X*_all; IMOV_all; gaps A/B |
| round10_q4 | refute MS10 | none; MS10 ⇔ Goal(Rig) |
| round10_q5 | level structures | dead end |
| round10_q6 | trace step | Lemma D3 |
| round10_q7 | counting | no-go; Theorem Q |
| round10_q8 | statements only; arithmetic | arithmetic dead |
| round10_q10 | chain check of K_w | Lemma S̃′ |
| round11_q1, q2, q3, q8 | closing on MS11 (Mechanism D) | B1 false; anchored sheets; Mechanism D; lift-curve form; rigid twin |
| round11_q4 | refute MS11 | none; (1L), twin-free closure, TFM |
| round11_q5 | Mechanism D (named) | same reduction |
| round11_q6 | statements only; Douady deformation theory | first order only; Lemma TR |
| round11_q7 | Theorem Q via Grothendieck | Theorem D |
| round11_q9 | chain check | chain correct with MS11♭ |
| round12_q1, q2, q3 | closing on MS11♭ (Mechanism G) | Lemma F, Lemma A, Prop. B, Lemma G1; step 4 false locally; K_S harmless |
| round12_q4 | refute MS11♭ | none; Euler bound, g ≥ 3 |
| round12_q5 | statements only; explicit lift-curves in stratum chart (LC) | Prop. LC′ (equivalent form) |
| round12_q6 | Mechanism G (named) | Lemma G2 (τ correction), Model G3′, Prop. G4; residual (R-a)/(R-b) |
| round12_q7 | (β)-obstruction with global input | Φ-reformulation; reduces to rigid twin |
| round12_q8 | (γ°)/(IMOV_Q) obstruction | frozen twin; Y(Δ) ⊂ pr_u(K_W); (O-γ°′) |
| round12_q10 | twin-free walk | Theorem TW; needs smoothness; quintic obstruction |

## Target for round 13

**Progress test: main line stalled — no universal progress.** Neither round 11 nor round 12 proved MS11♭, (Rig) under (R2), or the goal, or produced a strictly simpler missing statement with the chain re-derived.
- Theorem RO (S60) and the conditional theorem (S62) are major, but hold only under (R2^orb), not for every family the coarse hypotheses admit.
- Prop. C is an equivalent reformulation of (Rig).
- The MS11♭ reductions of round 12 (S63–S65) narrow the failure configuration; they do not simplify the statement.

What differs in my sketch from last round: Mechanism G (lift-curves in one 3-fold; refuted locally) is replaced by rigid-twin exclusion. All three failure modes ((β)-twists with rigid twin, (γ°), endpoint) produce one configuration (NRT-config). The proposed global mechanism is the side-swap of a reflection of S across c̃ under the deformation.

This is the second-to-last round ("one further round"). The wave:
- **q1, q2, q3:** the closing task on MS11♭ (byte-identical). It carries the round-12 closing material (chain, definitions, prior parts 1–4) plus round12_q7, q8, q6, q2, q1, q3, and the new sketch.
- **q4:** the hardest step of the sketch, posed self-contained: (NRT), with q7 and q8 spliced. Exclude the rigid-twin configuration, or sharpen it into an admissible counterexample.
- **q5:** continue q7's partial result. Verify the Φ-substitution in the chain entries, and prove "(NRT) ⇒ MS11♭ (Φ-form) ⇒ MS8". This would make (NRT) a strictly simpler missing statement.
- **q6:** the residual obstruction (R-a)/(R-b) of q6: a reflection of S across c̃ lost by Q_t. Attack it with total geodesy (Lemma TG, Lemma PA/V, the side-swap mechanism), or sharpen it into a counterexample.
- **q7:** statements only, with a first move not in the table (MS11♭ was attacked in rounds 11 and 12).
- **q8 (elsewhere 1):** (Rig) under coarse (R2) via (T_c) and Lemma J0. Exclude new cone points of joint vertex maps at t ≠ 0.
- **q9, q10 (final-two-rounds allowance: verify the standing results the final document presents).**
  - q9: an independent step-by-step check of Theorem RO (round12_q9 complete, with round8_q10 TV/Φ̂ spliced).
  - q10: a check and full write-up of the conditional theorem's derivation, (R1) + (R2^orb) ⇒ claim. It covers: (R2^orb)(c) ⇒ one lift-curve; entry 114 ⇒ MS11♭; entry 113 ⇒ MS8; RO ⇒ (Rig). It also takes up the local-to-global question for (R2^orb) and the case for (R2^orb) as the reading of "smoothly trivial family of submanifolds" in the orbifold M_g.

Round 14 (final) should conclude nothing unless a proof under (R2) appears. Otherwise the final document is built around S62 (the conditional theorem), S60, S51 and the coarse-reading reductions.

**Ledger numbers of this round's block:**
- 125: Lemma J0
- 126: Theorem RO
- 127: Prop. C
- 128: conditional theorem (S62)
- 129: Lemma A/F/G
- 130: Props. B/G4
- 131: REFUTED step 4
- 132: Lemma G1
- 133: Φ-reformulation
- 134: (γ°)
- 135: Euler bound / g ≥ 3
- 136: twin-free walk
- 137: OPEN (NRT)

[GOAL] is still entry 1 (OPEN). MS11♭ is still entry 124 (OPEN). (Rig) is still entry 82 (OPEN).
