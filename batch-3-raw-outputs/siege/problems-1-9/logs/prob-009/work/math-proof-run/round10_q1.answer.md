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

=== END OF ANSWER round10_q1 ===

