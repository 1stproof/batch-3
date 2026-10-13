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

=== END OF ANSWER round9_q2 ===
