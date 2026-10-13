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

=== END OF ANSWER round11_q9 ===
