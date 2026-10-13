# round10_q2: attempt on MS10

## Plan / status (written first, updated at the end)
- **Status: PARTIAL.** MS10 is NOT proved in general, and no counterexample is given.
- Plan:
  - §1: logical status of MS10 (what proving or refuting it amounts to).
  - §2: audit of the chain MS10 ⇒ MS8 ⇒ goal. I found one gap (G1): silent label switches during travel along pieces in non-product strata. I give a repair. The repair creates new MS10 instances, at interior points of pieces.
  - §3: Theorem X* extended to all strata, not only product type. This was an open item of round9_q3/q4. The proof lifts the limit disc to ∏_w M_w by the marking.
  - §4: the chart switch locus. Partial result P1: MS10 holds when Q is an interior point of the piece of β or of b and the switch locus (NoSw_Q) does not accumulate at 0. P1 covers all the new instances from §2 and all iMOV/turning-twin instances, under (NoSw_Q).
  - §5: what remains open, and the final summary.

---

## 1. Logical status of MS10 (proved; elementary)

**Remark 1.1.** The setting of MS10 contains the hypothesis "t ↦ Y_t is non-constant". The other hypotheses are those of the problem, plus (Rig), plus chart data. Hence:
- (a) If the problem's claim holds for every admissible family satisfying (Rig), then the setting of MS10 is never realised, and MS10 is vacuously true.
- (b) A counterexample to MS10 requires, before any chart data are chosen, an admissible family with (Rig) for which Y is non-constant. That family is already a counterexample to the problem's claim.

So the task's alternative "give an explicit counterexample to MS10" is equivalent to refuting the problem itself, for a family that also satisfies (Rig). A general proof of MS10 is, through the chain, a proof of the problem modulo (Rig) and the chain's inputs. MS10 localises the difficulty at one chart, but it is not logically weaker than the goal in any useful sense. The conclusion of MS10 at t = 0 is a statement about V_0 alone. It cannot follow from t = 0 data alone, since without "Y non-constant" it is false (Proposition K / K_w produces violating pairs). Any proof must therefore combine time-t information with total geodesy at t = 0, by contradiction.

---

## 2. Audit of the chain (MS10 ⇒ MS8 ⇒ goal)

I re-read the chain step by step. Steps 1, 2(a) (Proposition K_w, modulo its cited inputs), 2(c) and 2(d) are correct as logic, given their cited inputs. Step 1 needs (Rig), which is entry 82 and is OPEN; the chain proves the goal only conditionally on (Rig), as the brief says. I found one gap, in step 2(b).

### 2.1 The gap G1: silent label switches during travel along non-product pieces

Step 2(b) says: "persistence passes along D^{m+1} to β̃_{m+1}, because persistence is a property of the whole component κ(D^{m+1}) (Lemma S(c)) and the chart vertex is c_{m+1} on both ends (K_w Step 3)".

What K_w actually proves:
- Inside each excursion (a ball B(J,2r), J ∈ Σ), the label is tracked by a continuous lift into Def(J). This is K_w Step 3.
- At each single travel time s, the Σ_i-side of the nearby boundary point z_s is *some* constant vertex of the coarse piece D with value ≅ Y_0. This is K_w Step 2.
- K_w does **not** show that the vertex at different travel times of one travel interval is the same vertex of the same lifted piece.

For a product-type stratum this is harmless. There ξ_G is injective, so the vertices of D are canonical labels (Lemma PT). For a non-product stratum Δ_G the situation is different:
- a "vertex of D" is defined only after choosing a lifted piece Ê ⊂ ∏_w M_w with ξ_G(Ê) = D;
- Lemma S(c) (persistence) is a statement about a vertex of a lifted component 𝒲̃ ⊂ ∏_w M_w × Δ;
- the translates σÊ, σ ∈ Aut(G), are the other lifts.

**The mechanism.** Let e ∈ Ê ∩ σÊ with σÊ ≠ Ê as germs at e. Then the coarse curve D can be a single smooth branch at ξ(e), while ξ^{-1}(D) has two branches at e: the germ of Ê and the germ of σÊ. The marked travel path, read in ∏_w M_w, can arrive near the germ of Ê and leave near the germ of σÊ. Coordinate c on σÊ is coordinate σ^{-1}c on Ê, so the tracked label switches from c to σ^{-1}c on Ê. STAY during travel (K_w Step 2) forces σ^{-1}c to be constant ≅ Y_0 on Ê. If σ^{-1}c were non-constant with value ≅ Y_0 at e, then ξ(e) would lie in Σ and would be an excursion point. So the switch is silent exactly when Ê carries two constant vertices c ≠ σ^{-1}c, both ≅ Y_0 at t = 0.

This is the persistent-twin configuration (R8-8 Prop. 3(b)), now occurring inside a travel interval. ξ(e) is in general not in Σ:
- it need not be a junction;
- it need not be a singular point of the coarse B_0;
- it need not be a puncture;
- the twin vertex is constant, so the last clause of the definition of Σ does not apply.

So the step "chart vertex c_{m+1} on both ends ⇒ persistence passes" is unsupported for non-product pieces. The persistent vertex c on 𝒲̃ ⊃ Ê need not be the label that arrives at J_{m+1}.

### 2.2 Repair of G1 (sketch, at the level of rigour of K_w)

**Enlarge the special set.** For each piece D at time 0, let Ĉ_D := ξ_G^{-1}(closure D) ⊂ ∏_w M̄_w. It is a compact analytic curve. Put
 Σ_tw := { ξ̄_G(e) : e a singular point of Ĉ_D, for some piece D }.
- Σ_tw is finite: a compact curve has finitely many singular points, and there are finitely many pieces.
- Every crossing point e ∈ Ê ∩ σÊ with σÊ ≠ Ê is a singular point of Ĉ_D, so Σ_tw contains the points of §2.1.

Replace Σ by Σ′ := Σ ∪ Σ_tw in K_w, and choose r for Σ′. Nothing in K_w Steps 0–5 uses more about Σ than finiteness, the Milnor and chart properties of the balls, and property (b) of η on K_D.

**Travel is now label-consistent.** Fix a travel interval I along D. Put K̂_D := ξ_G^{-1}(K_D) ⊂ ∏_w M_w, where K_D = closure(D) ∖ ⋃_{J∈Σ′} B(J, r/2).
- K̂_D is a compact smooth curve. Its connected pieces, one inside each translate σÊ, are pairwise disjoint, so at mutual distance ≥ δ′ > 0.
- During I the marked node multicurve 𝔠_I is constant: at γ_n(s) the short curves are exactly the node curves of z_s, by (a) of K_w.
- Fix once an identification of the components of S_g ∖ 𝔠_I with V(G). Then the marked components of z_s give a point ẑ_s ∈ K̂_D. Since z_s is defined up to ρ_n, the map s ↦ ẑ_s is defined up to o(1) and is approximately continuous.
- Once ρ_n ≪ δ′, the point ẑ_s stays near a single translate σÊ throughout I.
- So one coordinate c of one lifted piece carries the Σ_i-side for all s ∈ I.

Persistence of c is a property of the irreducible lifted component 𝒲̃ ⊃ σÊ (Lemma S(c) of round9_q7). Hence the label entering J_{m+1} is the persistent one, as step 2(b) needs.

**Cost of the repair.** Each point of Σ_tw at which a walk makes an excursion becomes a junction J with D^m = D^{m+1}. There:
- J is an interior point of the piece, i.e. J lies in the stratum of D;
- the walk enters along a lifted germ β̃ of the coarse branch of D at J and leaves along a lifted germ b̃ of the same coarse branch;
- β̃ and b̃ are joined by the walk's lifted excursion path in q^{-1}(V_0) ∩ B (K_w Step 3);
- if the stratum is non-product, this is exactly an MS10 instance with "lifts of the same coarse branch" allowed by MS10's data. If it is product type, Lemma PT and Cor. J′ apply as before.

So, after the repair, the chain (MS10 + entries 19, 24, 84–87 ⇒ MS8) is correct as logic, with these extra MS10 instances at interior points. §4 below proves MS10 for all instances at interior points, under the condition (NoSw_Q).

### 2.3 Other remarks on the chain (no further gap found)
- MS10 needs B "small". The walk's excursions live in B(J, 2r), and r may be taken as small as wanted, before δ, η, n are chosen. So this is consistent.
- In MS10's "joined" hypothesis the endpoints of γ_n converge to points of β̃ ∖ 0 and b̃ ∖ 0. These are the limits of the entry and exit points of the excursions on the shell, after passing to a subsequence. This matches K_w Steps 4–5.
- The chain depends on (Rig) (entry 82, OPEN) and on the cited inputs of Proposition K_w: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T_g ↔ Def chart description, and the collar lemma. These are unchanged here.

---

## 3. Theorem X* for arbitrary strata (proved, modulo the cited facts listed)

### 3.1 Statement
**Setting.**
- V_0 ⊂ M_g is a closed, 2-dimensional, totally geodesic subvariety. Smoothness is not needed in this section.
- Δ_G is ANY stratum.
- E is a piece of B_0 in Δ_G (coarse: a 1-dimensional irreducible component of B_0 ∩ Δ_G), and Q_0 ∈ E. So Q_0 lies in Δ_G, i.e. it is an interior point of E.
- β̃ ⊂ Def(Q_0) is a lift through 0 of a local branch β of E at Q_0. It lies in the stratum locus L_G := {s_e = 0 for all e ∈ E(G)}.
- S is an irreducible component of the germ at 0 of q^{-1}(closure V_0) with β̃ ⊂ S. ν: Ŝ → S is its normalization, with ν^{-1}(0) = {ŝ_0}, and B̂ := ν^{-1}(S ∩ {∏ s_e = 0}).

**Theorem X\*\*.** Every irreducible component of the germ (B̂, ŝ_0) maps onto β̃. In particular, every lifted boundary branch b̃ through 0 that is contained in S equals β̃. Two different lifts β̃ ≠ αβ̃ of β never lie in a common chart sheet.

This is round9_q4's Theorem X* without the product-type hypothesis. round9_q3 Remark 4 and round9_q4 Remark 4 list this extension as unchecked.

### 3.2 Additional cited facts (from memory)
- **(HK) Marked plumbing charts.** (Bers, Earle–Marden, Hubbard–Koch.) Let 𝔠 be a multicurve on S_g. Let T̄^{𝔠} be the open subset of augmented Teichmüller space consisting of marked noded surfaces whose nodes lie in 𝔠. Let Tw(𝔠) be the free abelian group generated by the Dehn twists about the curves of 𝔠. Then:
  - T̄^{𝔠}/Tw(𝔠) is a complex manifold of dimension 3g−3, containing T_g/Tw(𝔠) as an open dense subset.
  - Its 𝔠-stratum is the closed submanifold ∏_v T(Σ_v). Here Σ_v runs over the components of S_g ∖ 𝔠, with the boundary curves becoming punctures.
  - For a marked stable curve Ẑ in the 𝔠-stratum, a neighbourhood of Ẑ is a versal deformation Def(Z) of Z. The labels of the stratum locus of Def(Z) are the components Σ_v, so they are fixed by the marking.
  - The map to M̄_g is holomorphic. Near Ẑ it is the quotient map Def(Z) → Def(Z)/Aut(Z).
  This is the "standard description" already cited in R8-1 Step 2 and K_w Step 3. I use it in the stated marked form.
- **(FN) Compactness modulo twists.** Let X̃_n → P̂ in T̄^{𝔠}/Tw(𝔠), with P̂ in the 𝔠-stratum, and let Ỹ_n ∈ T_g satisfy d_T(Ỹ_n, X̃_n) ≤ ρ. Then the classes [Ỹ_n] have a subsequence converging in T̄^{𝔠}/Tw(𝔠) to a point of the 𝔠-stratum.
  - *Reason:* Use Fenchel–Nielsen coordinates for a pants decomposition containing 𝔠, together with Wolpert's lemma (lengths change by a factor at most e^{2ρ}).
  - The curves of 𝔠 get lengths → 0. The other pants curves, and their dual curves, have lengths bounded above and below.
  - So the twists about non-𝔠 curves are bounded, and the twists about 𝔠 matter only modulo Tw(𝔠).
  - The plumbing coordinates near the stratum are continuous functions of (length, twist angle) of the 𝔠-curves.

### 3.3 Proof
I follow R8-1 §3.2 (Steps 1–4) and round9_q4 §1.4 (Step 5*). Only the points where R8-1 used product type change: the global coordinate f_j in Step 3, and the choice of the point e_0 in Step 4.

**Step 0 (a lifted piece adapted to β̃).**
- Fix an identification of G_{Q_0} with G. It gives the partial normalization map Π: L_G → ∏_w M_w, with ξ_G∘Π = q.
- Π(β̃) is an irreducible curve germ at ê := Π(0), contained in ξ_G^{-1}(E). Let Ê be the irreducible component of ξ_G^{-1}(closure E ∩ Δ_G) containing it, and let Ê^ν be its normalization. Let ê_0 ∈ Ê^ν be the point corresponding to the branch Π(β̃) of Ê at ê.
- Choose a small closed disc B̂ ⊂ Ê^ν around ê_0 with the following properties:
  - its image lies in Π(β̃-neighbourhood);
  - ξ_G maps it into the chart image U = q(B);
  - B̂ ∖ {ê_0} maps into β ∖ {Q_0}.

**Step 1 (base point, approximants).** Take P̂_1 ∈ B̂ ∖ {ê_0} generic and P_1 := its image in E. Then:
- Lemma PA applies at P_1;
- P_1 lies on no other piece and on no other lifted branch;
- the points of ν^{-1}(P̃_1) lie only on components of B̂ over β̃.
Here P̃_1 ∈ β̃ is a point with Π(P̃_1) = P̂_1.

Lemma PA (PR-H §1) is proved in a Kuranishi chart Def(P_1) with plumbing coordinates. It uses only the local model of a branch along E, and never uses injectivity of ξ_G. So it applies at the generic point P_1, with approximants X_n inside the local branch N := ν(neighbourhood of a point of ν^{-1}(P̃_1)) ⊂ S. Choose X_n off the curves S ∩ S_i (other sheets) and off the non-normal locus. This gives generating pairs (X_n, q_n) whose limit (q_w) has q_j ≠ 0 at a vertex j that moves along E.

**Step 2′ (the limit disc, lifted by the marking).** Let D̃_n: 𝔻 → T_g be lifts of the Teichmüller discs D_n ⊂ V_0, with D̃_n(0) = X̃_n. Here X̃_n is a marked lift of X_n converging, in T̄^{𝔠}/Tw(𝔠), to the marked point P̂ over P_1, where 𝔠 is the node multicurve of P_1.
- I choose the identification of the components Σ_v of S_g ∖ 𝔠 with V(G) so that the induced point of ∏_w M_w is P̂_1. Two identifications differ by Aut(G), and Aut(G) permutes ξ_G^{-1}(P_1), so this is possible.
- For each w ∈ 𝔻, d_T(D̃_n(w), X̃_n) ≤ d_𝔻(0,w). By (FN), and a diagonal argument on a countable dense set together with Montel in the local charts of (HK) (exactly as in R8-1 Step 2), a subsequence of [D̃_n] converges locally uniformly to a holomorphic map L̃: 𝔻 → ∏_v T(Σ_v), the 𝔠-stratum.
- Composing with ∏_v T(Σ_v) → ∏_v M_v gives a holomorphic L̂: 𝔻 → ∏_w M_w with ξ_G∘L̂ = L. Here L is R8-1's coarse limit disc, L(𝔻) ⊂ B_0 ∩ Δ_G.
- L̂(0) = P̂_1. L̂(𝔻) lies in ξ_G^{-1}(B_0 ∩ Δ_G), whose irreducible components are locally finite. Their L̂-preimages are analytic and cover 𝔻, and P̂_1 lies on Ê only. So L̂(𝔻) ⊂ Ê, and L̂ lifts to Ê^ν (normality of 𝔻; L̂ is not contained in Sing Ê).
- By (Fl), the j-coordinate of L̂(w) is A_w·(Y_j(P_1), q_j), the Teichmüller disc τ(w) of (Y_j(P_1), q_j) in M_j. It is non-constant. The vertex j is the one defined by the marking, which is consistent with the labels of L̂.

**Step 3′ (L̂: 𝔻 → Ê^ν is surjective).** This is R8-1 Step 3 verbatim, with E^ν replaced by Ê^ν and f_j := pr_j|_Ê, which is a global holomorphic function on Ê^ν:
- τ(𝔻) ⊂ C_j° := closure(f_j(Ê)) ∩ M_j, an irreducible closed curve;
- the Teichmüller disc Δ̃ ⊂ T(Y_j) lifting τ is a component of the preimage of C_j° (by (Prop)), and 𝔻/Stab(Δ̃) → C_j° is proper;
- the set of lifts λ: 𝔻 → Ê^ν with f_j∘λ = τ is finite;
- L̂ descends to a proper map 𝔻/Γ_L̂ → Ê^ν, which is therefore surjective.

**Step 4′ (a path to ê_0).** This is R8-1 Step 4 with B replaced by B̂ ⊂ Ê^ν:
- L̂(0) = P̂_1 ∈ int B̂.
- Let W be the component of the preimage of int B̂ in 𝔻/Γ_L̂ that contains [0]. W → int B̂ is proper and non-constant, hence surjective.
- So there are w* and a path π from 0 to w* with L̂(π) ⊂ B̂ and L̂(w*) = ê_0.
- Take Ω a connected, relatively compact neighbourhood of π with L(Ω̄) ⊂ U. Then L(w*) = Q_0.

**Step 5\* (local; unchanged).**
- Lift D_n|_Ω to D̂_n: Ω → Def(Q_0)° through T_g, using (HK) for the node multicurve of Q_0, with D̂_n(0) = X̃_n ∈ S. The analytic-covering argument of R8-1 Step 5 gives D̂_n(Ω) ⊂ S: the sets D̂_n^{-1}(S_i) are analytic and cover Ω, one of them is Ω, and X̃_n lies only on S. Then D̂_n lifts to Ŝ, with image avoiding B̂.
- A subsequence converges to L̂_S: Ω → Ŝ, with ν∘L̂_S a lift of L. Near the parameter 0 it takes values in the components of B̂ over β̃ (Step 1). By the identity principle on the connected Ω (the preimages of the finitely many components of B̂ are analytic and cover Ω), L̂_S(Ω) lies in one component Ê_1 of B̂ over β̃.
- L(w*) = Q_0, and q^{-1}(Q_0) = {0}, so L̂_S(w*) = ŝ_0.
- Now round9_q4 §1.4 applies verbatim: resolution, negative definiteness and the cycle Z_n. Its only inputs are: D̂_n avoids B̂; D̂_n → L̂_S uniformly near w*; L̂_S is a non-constant disc in Ê_1 through ŝ_0. If B̂ had a component C not over β̃, the cycle Z_n would give Z_n·C′ = 0 and Z_n·C′ > 0, a contradiction. ∎

**Corollary 3.4.** In the setting above, if a chart sheet S at 0 ∈ Def(Q_0) contains β̃ and some lifted branch b̃ of B_0 through 0, then b̃ = β̃. In particular:
- (a) **no crossings:** b̃ cannot be a branch of another piece, or of another stratum;
- (b) **no turning twin inside one sheet:** b̃ cannot be another lift aβ̃ ≠ β̃ of β.

(Notation remark for Step 5*: X̃_n there denotes the Def(Q_0)-lift of X_n lying in S near P̃_1. It is obtained from the T_g-lift of Step 2′ by a deck transformation, which changes nothing in Step 5*: that step uses only the coarse disc L and the Def(Q_0)-lifts.)

---

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

=== END OF ANSWER round10_q2 ===
