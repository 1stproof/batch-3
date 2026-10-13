# round9_q6 — the twin step (TW*) via the lifted 3-fold component

**Status.** (TW*) is NOT proved in general. Proved here: planner Steps 1–3, with two repairs, and the analogue at the endpoint (Step 5). Together they reduce (TW*) to a precise coset condition on the stabiliser group Γ. Step 4 (the case where automorphisms in Γ drop) stays open, and I explain where each suggested tool fails. No counterexample is given.

Readings: (R1), (R2) with H_0 = id, (TD_J)/(TD_Q) of R8-5 §1 and §5, and (PT_chain). Notation q : B → B/Aut(J), F_x, L_x, (K1)–(K4), transport families Ñ as in R8-8 §0.

---

## 0. Two repairs to the planner's set-up

**(Rep1) Define 𝒜 by the sheet, not as a component of 𝒱 ∩ (U×Δ_ε).**
- Choose a closed conic (Milnor) neighbourhood U'' ⋐ U of J. Then closure(V_0) ∩ U'' is the union of its local sheets S at J, and V_0 ∩ U'' is the disjoint union of the connected sets S° := S ∖ B_0. This uses that V_0 is smooth and that an irreducible germ minus a proper analytic subset is locally connected.
- The track γ of (TD_J) is a path in V_0 ∩ U''. Take z_1, z_2 close enough to J for this.
- So γ lies in ONE sheet S_0°. This is the "same-sheet property"; it is automatic.
- Put 𝒜 := H((S_0° ∩ U'') × Δ_ε). For ε small, 𝒜 ⊂ 𝒱 ∩ (U×Δ_ε). It is connected, and open in 𝒱.
- Let 𝒞° be the connected component of q^{-1}(𝒜) that contains γ̃ × {0}. There are finitely many components, so after passing to a subsequence ρ_n → 0 it is independent of ρ.
- Put Γ := Stab_{Aut(J)}(𝒞°) and 𝒳 := closure(𝒞°) ⊂ B × Δ_ε.
- As in R8-5 Fact 0, q : 𝒞° → 𝒜 is the quotient by Γ.

Why the repair is needed: a component of 𝒱 ∩ (U×Δ_ε) can contain several sheets at (J_t, t). Step 1 below needs local connectivity at (J_t, t), and the sheet version has it.

**(Rep2) 𝒳 need not be an irreducible germ.**
- The planner calls 𝒳 an irreducible 3-dimensional germ. That is not justified: 𝒞° can be reducible. Example: the preimage of the smooth curve {ab = 0}/swap.
- What is true: 𝒳 is analytic of pure dimension 3. Near any point, q^{-1}(closure 𝒜) is analytic, because closure(𝒜) is locally a union of local irreducible components of closure(𝒱) (Lemma S of R8-1 together with (R2)). Each local irreducible component L′ of q^{-1}(closure 𝒜) has L′ ∖ {∏ s_e = 0} connected, so it lies in one component of q^{-1}(𝒜). Hence 𝒳 is, locally, the union of those L′ whose interior lies in 𝒞°.
- Nothing below needs irreducibility.

**(Rep3) Genericity of z̃_1, z̃_2.**
- Choose z̃_1 ∈ β̃ ∖ 0 such that Stab_{Aut(J)}(z̃_1) equals the pointwise stabiliser of β̃. Only finitely many points of β̃ near 0 fail this, because stabiliser jumps form an analytic subset of the curve.
- Choose z̃_2 on β̃′ in the same way.
- This is part of "generic" in (TD_J).

---

## 1. Lemma 1 (Step 1: one Γ-orbit) — proved

**Lemma 1.** Let y = (H(z,τ), τ) with z ∈ S_0 ∩ U'' and |τ| < ε, and suppose S_0 is locally irreducible at z. (This holds for z = J, since S_0 is irreducible at J by definition.) Then the points of 𝒳 lying over y form a single Γ-orbit. In particular, for every t the lifts of J_t = H_t(J) lying in 𝒳_t form one Γ-orbit.

*Proof.*
1. **𝒜 is locally connected at y.** Let W be a neighbourhood of y.
   - Since H is a homeomorphism, there are a conic neighbourhood W_0 of z (on which S_0° ∩ W_0 is connected, by local irreducibility at z) and a disc D ∋ τ with H(W_0 × D) ⊂ W.
   - H((W_0 ∩ S_0)×D) contains 𝒜 ∩ W′ for a smaller neighbourhood W′ of y, because H is open onto closure(𝒱).
   - So 𝒜 ∩ W′ lies in the connected set H((S_0° ∩ W_0) × D) ⊂ 𝒜 ∩ W.
2. **Set-up near a lift.** Let p ∈ 𝒳 lie over y and put G_p := Stab_{Aut(J)}(p).
   - Take a G_p-invariant neighbourhood N_p of p with αN_p ∩ N_p = ∅ for α ∉ G_p. Then q|N_p is the quotient by G_p, and q(N_p) is a neighbourhood of y.
   - By step 1, choose W′ such that 𝒜 ∩ W′ lies in a single component 𝒦 of 𝒜 ∩ q(N_p).
3. **The components of q^{-1}(𝒦) ∩ N_p are permuted transitively by G_p.** The argument is that of R7-4 Lemma 2(a): q is open and closed on saturated sets, the domain is locally connected, and 𝒦 is connected.
4. **One of them lies in 𝒞°.** Points of 𝒞° arbitrarily close to p map into 𝒜 ∩ W′ ⊂ 𝒦. So some component L of q^{-1}(𝒦) ∩ N_p meets 𝒞°. L is a connected subset of q^{-1}(𝒜), so L ⊂ 𝒞°.
5. **Comparing two lifts.** Let p′ = αp also lie in 𝒳. As in step 4, some component L′ of q^{-1}(𝒦) ∩ αN_p lies in 𝒞°.
   - α^{-1}L′ is a component of q^{-1}(𝒦) ∩ N_p, so α^{-1}L′ = gL with g ∈ G_p.
   - Then α^{-1}𝒞° ∩ g𝒞° ≠ ∅, so α^{-1}𝒞° = g𝒞°, i.e. αg ∈ Γ.
   - Finally αg·p = αp = p′. ∎

## 2. Lemma 2 (Step 2: the transport families lie in 𝒳) — proved

**Lemma 2.** Some irreducible component Ñ^1 of Ñ lies in 𝒳. Likewise some irreducible component Ñ′^1 of Ñ′ lies in 𝒳. For every t:
- closure(Ñ^1_t) contains a lift of J_t, and F_x ≡ φ_{c_m}(t) on closure(Ñ^1_t);
- the same holds for Ñ′^1 with φ_{c_{m+1}}.

*Proof.*
1. **z̃_1 ∈ 𝒳.** γ̃(a) ∈ 𝒞° and |γ̃(a) − z̃_1| < ρ_n → 0 by (T1).
2. **A 3-dimensional local component.** Let L be a local irreducible component of 𝒳 at (z̃_1, 0). It is 3-dimensional and not contained in {∏ s_e = 0} (Rep2).
   - By Krull, L ∩ {∏ s_e = 0} is pure 2-dimensional at (z̃_1, 0).
   - It lies in q^{-1}(closure(𝒜) ∖ 𝒜) ⊂ q^{-1}(H(B_0 × Δ)).
   - Near (z_1, 0), the set H(B_0 × Δ) equals N := H((β ∖ J) × Δ), because z_1 is a smooth point of B_0 on β.
3. **Near z̃_1, the preimage of N is Ñ.** Near (z̃_1, 0), q^{-1}(N) is the union of the translates aÑ with a ∈ Stab(z̃_1). By (Rep3), such an a fixes β̃ pointwise. So aÑ = Ñ, since both are the component of q^{-1}(N) containing β̃ ∖ 0.
4. **Conclusion.** Hence 𝒳 ∩ Ñ is an analytic subset of Ñ containing a 2-dimensional germ at (z̃_1, 0). That germ contains a local irreducible component of Ñ, which lies in a unique global irreducible component Ñ^1. By the identity principle for the irreducible set Ñ^1, Ñ^1 ⊂ 𝒳.
5. **Properties of Ñ^1.**
   - N is a connected topological 4-manifold. A 4-manifold germ minus a set of real dimension ≤ 2 is connected, so N is locally irreducible, and hence irreducible.
   - So q(Ñ^1) = N, by Remmert applied to the finite map q together with dimension.
   - closure(Ñ^1_t) ∋ lift of J_t, by the argument of R7-3 Lemma 2 step 5.
   - F_x ≡ φ_{c_m}(t) on Ñ_t ⊃ Ñ^1_t, by (∗) of R8-8 §0.
6. **Remark.** The same argument at time 0 shows β̃, β̃′ ⊂ closure(C_0), where C_0 is the component of q^{-1}(S_0°) containing γ̃. ∎

## 3. Step 3: the reduction — proved

**Proposition 3.** For every t there are:
- j̃ ∈ closure(Ñ^1_t) ∩ q^{-1}(J_t),
- j̃′ ∈ closure(Ñ′^1_t) ∩ q^{-1}(J_t),
- γ_t ∈ Γ with j̃′ = γ_t j̃,

and then [φ_{c_{m+1}}(t)] = [F_{γ_t^{-1}x}(j̃)], while [φ_{c_m}(t)] = [F_x(j̃)].

*Proof.* By Lemmas 1 and 2, together with (K3). ∎

**Corollary 3′ (new sufficient conditions for no twin jump at J).** Suppose that, for t in a set accumulating in Δ, Γ = Γ_x · Stab_Γ(j̃(t)). Then [φ_{c_{m+1}}] ≡ [φ_{c_m}]. This holds in particular under either of the following.
- **(IP_Γ)** Γ fixes j̃(t), i.e. the automorphisms of J that preserve the track's family component 𝒞° survive on J_t.
- **(NT_Γ)** Γ fixes x.

*Proof.* Choose γ_t ∈ Γ_x. Then F_{γ_t^{-1}x} = F_x. Conclude with Lemma 1 of R8-8. ∎

Comparison with known results:
- (IP_Γ) is strictly weaker than (IP_m), because only Γ ⊂ Aut(J) has to be preserved, not all of Aut(J).
- (NT_Γ) is a special case of (U_J).
- So this is a modest strengthening of R8-8 Corollary 1 and R8-5 Theorem A. It does NOT answer the question.

**Endpoint (Step 5).** Lemmas 1 and 2 hold verbatim at Q_0, applied to Ñ^k_+ and Ñ^E and using the sheet of the (TD_Q)-track. Hence (b) of (TW*) holds at every t at which γ_t can be chosen in Γ_x; Step 2 of Theorem 1 in R8-8 then applies.

## 4. Step 4 (Γ ⊄ Γ_x·Stab(j̃)) — open; what is shown

Assume Y is non-constant, t is generic, and (a) fails at J. By Proposition 3 and R8-8 Proposition 3 we get the following.
- There is γ ∈ Γ (fixed for t in an uncountable set) with γx ≠ x.
- Along β̃′, γx is an intact constant vertex w of D^{m+1} with [φ_w] ≡ [Y]. This is the persistent twin.
- The twin-jumping automorphism is moreover forced to preserve the 3-fold family component 𝒞° of the track. This is new information beyond R8-8 Prop. 3, which only had γ ∈ Aut(J).

Status of the planner's four tools:
1. **Krull/Hurwitz inside 𝒳.** 𝒳 is γ-invariant and contains Ñ^1, Ñ′^1, γÑ^1 and γ^{-1}Ñ′^1. The labels are:
   - along Ñ: x ↦ Y;
   - along Ñ′: x ↦ φ_{c_{m+1}}, γx ↦ Y;
   - along γ^{-1}Ñ′: x ↦ Y.

   This is exactly the R7-3 §5 model with σ = γ ∈ Γ. Every incidence constraint that Krull gives in 𝒳 is satisfied by the model, so it gives no contradiction. (I did not write down an explicit 3-fold realising the model; this point is heuristic, as in R8-5 §6.)
2. **Generic-time trichotomy at every lift.** It is satisfied, because the Y-network continues on the twin γx (R8-4 §5 check).
3. **The same-sheet property.** It holds automatically (Rep1), and Lemma 2's remark puts β̃ and β̃′ in one lifted sheet closure(C_0) at time 0. But γ need not stabilise C_0 (Γ ≠ Γ_0 := Stab(C_0) is possible). Even when it does, the case of R8-5 Prop. D (A)/(B) is not excluded.
4. **Lock via Γ.** Γ permutes lifts and labels, but F_x(γj̃) = F_{γ^{-1}x}(j̃), and nothing forces F_{γ^{-1}x}(j̃) ≅ F_x(j̃) when γ ∉ Stab(j̃).
5. **Lemma U.** It constrains only non-constant vertices; here all vertices involved are constant.

**Open question (sharpened).** For γ ∈ Γ = Stab(𝒞°) with γx ≠ x, can γ ∉ Aut(J_t) for t ≠ 0? Equivalently, can the automorphisms of J that preserve the track's family component drop along H_t(J)?
- If no, then (IP_Γ) holds and (TW*) follows.
- A proof must use total geodesy of V_0, or global data. The 𝒳-picture is chart-plus-family-local and consistent with the twin-jump model.

## Summary
- **Proved:** Steps 1–3 and 5 (with Rep1–Rep3); Corollary 3′ ((IP_Γ) or (NT_Γ) ⇒ no twin jump).
- **Not proved:** (TW*) in general.
- **Open:** Step 4, i.e. the drop of Γ-automorphisms at J_t.

=== END OF ANSWER round9_q6 ===
