# round9_q5 answer

## Status in one paragraph
I did **not** prove (EF), and I found no counterexample. (EF) is not settled here. What follows is new material that is proved, plus a precise account of where it stops.
- **Lemma S.** Theorem J holds for any vector field whose transposed weighted generator has no finite-order Jordan chain at 0 ("semisimple at 0"). (K0) and (K1) are one sufficient condition, but semisimplicity is strictly weaker.
- **Proposition T (tensor-square trick; GH not used).** Take the pair S = δ_x − e^b δ_y of Theorem R. Then S⊗S is a nonzero combination of four Dirac masses on M×M. Under the flow (g_t, g_{−t}) with its Jacobian weight, it decays exponentially in **both** time directions, **whatever the value of λ = μ(d)**. More generally, any S as in (J1) for X or for −X (any strip position) gives such a two-sided decaying S⊗S.
- **Consequently** the problem, and also (EF) for all strip positions, follows from **one statement at the single spectral point 0**: (J2), or the stronger (SS_Y). These live on M×M for the field Y = (X, −X), which is not GH. I check that (SS_Y) holds for Diophantine linear flows. I explain why I could not derive it from GH: it is again a statement about the absence of continuous spectrum.
- A positivity remark (Section 5) recasts a nonzero EF as a translation (Lax–Phillips-type) model with Lebesgue spectrum.

Conventions are those of the task file: ν, d = div_ν X, J_t, P φ = Xφ + dφ, and Γ_t φ := e^{J_t}(φ∘g_t), so that d/dt Γ_t φ = Γ_t Pφ = PΓ_t φ, and F_φ(t) = S(Γ_t φ).

---

## 1. Lemma S: Theorem J under semisimplicity at 0 (proved)

Let N be a compact manifold, Z a smooth vector field on N, ν_N a smooth positive density, d_Z = div_{ν_N} Z, J^Z_t(p) = ∫_0^t d_Z(G_s p) ds (G_t the flow of Z), P_Z Φ = ZΦ + d_Z Φ, and Γ^Z_t Φ = e^{J^Z_t} Φ∘G_t.

**Definition (SS_Z).** P_Z^T is *semisimple at 0 (in finite order)* if the following holds. Whenever A, B are distribution densities of finite order on N with A∘P_Z = 0 and B∘P_Z = A, then A = 0.

**Lemma S.** Assume (SS_Z). Let S be a distribution density on N, and suppose there are ε > 0, k and C with |S(Γ^Z_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^k} for all real t and all smooth Φ. Then S = 0.

*Proof.* This is the proof of Theorem J (R6-a §2) with step 4 replaced.
1. Steps 1–3 use no hypothesis on the field. Put F_Φ(t) = S(Γ^Z_t Φ). It is C^1 with F_Φ' = F_{P_Z Φ}. The moments m_j(Φ) = ∫ t^j F_Φ dt are densities of order ≤ k. They satisfy m_0∘P_Z = 0 and m_j∘P_Z = −j m_{j−1} for j ≥ 1.
2. Induction. Suppose m_0 = … = m_{j−1} = 0; for j = 0 this is vacuous. Then m_j∘P_Z = 0 (for j ≥ 1 because m_{j−1} = 0; for j = 0 by step 1). Put B := −m_{j+1}/(j+1). Then B∘P_Z = m_j. By (SS_Z), m_j = 0. So all moments vanish.
3. Step 5 of Theorem J (Fourier transform holomorphic on |Im ξ| < ε, all Taylor coefficients at 0 equal to 0) gives F_Φ ≡ 0. Hence S(Φ) = F_Φ(0) = 0. ∎

*Remarks.*
- (K0) ∧ (K1) for Z imply (SS_Z). Indeed A∘P_Z = 0 gives A = cν_N by (K0). Then B∘P_Z = cν_N means u = B/ν_N satisfies Zu = −c, so c = 0 by (K1).
- The converse fails. For a Diophantine linear field on a torus, the field Y of Section 2 satisfies (SS_Y) (Section 3) but has an infinite-dimensional kernel, so (K0) fails for it.

## 2. Proposition T: the tensor-square trick (proved; no GH)

Let N = M×M, ν_N = ν⊗ν, and Y(x_1,x_2) = (X(x_1), −X(x_2)). Then:
- the flow is G_t = g_t × g_{−t};
- d_Y(x_1,x_2) = d(x_1) − d(x_2);
- J^Y_t(x_1,x_2) = J_t(x_1) + J_{−t}(x_2). (Check: ∫_0^t d(g_{−s}x_2) ds = −J_{−t}(x_2).)

Hence P_Y = P⊗1 − 1⊗P and Γ^Y_t = Γ_t ⊗ Γ_{−t}.

**Proposition T.** Let μ be an ergodic flow-invariant probability with h_μ(g_1) > 0, and λ = μ(d). Then there is a nonzero real distribution density S_2 on N, a combination of four Dirac masses, with
 |S_2(Γ^Y_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^1} for all t ∈ R and Φ ∈ C^∞(N),
for some ε > 0. No sign or size condition on λ is needed.

*Proof.*
1. **Inputs.** Theorem R, steps 1–3 (R8-a; Pesin, Ledrappier–Young and Lemma 6.0, cited as there) give the following, with 0 < θ < χ^+_min and 0 < δ < θ/4:
   - points x ≠ y with d(g_t x, g_t y) ≤ C_0 e^{−θ|t|} for t ≤ 0;
   - a constant b with |J_t(x) − J_t(y) − b| ≤ K e^{−θ|t|} for t ≤ 0;
   - since x and y are two-sided Birkhoff-generic for d, the bounds J_t(p) ≤ C_1 + (λ+δ)t and J_{−t}(p) ≤ C_1 + (−λ+δ)t for t ≥ 0 and p ∈ {x, y}.
2. **Definition.** Put w_x = 1 and w_y = −e^b, and S_2 := Σ_{p,q∈{x,y}} w_p w_q δ_{(p,q)} = S⊗S with S = δ_x − e^bδ_y. The four points are distinct and the weights are nonzero, so S_2 ≠ 0.
3. **Expansion.** F_2(t) := S_2(Γ^Y_t Φ) = Σ_{p,q} w_p w_q e^{J_t(p)+J_{−t}(q)} Φ(g_t p, g_{−t} q).
4. **Case t ≥ 0.** Fix p and sum over q:
   Σ_q w_q e^{J_{−t}(q)} Φ(g_t p, g_{−t} q) = e^{J_{−t}(x)} [Φ(g_tp, g_{−t}x) − Φ(g_tp, g_{−t}y) + (1 − e^{−r})Φ(g_tp, g_{−t}y)],
   where r = J_{−t}(x) − J_{−t}(y) − b and |r| ≤ K e^{−θt}.
   - The bracket is at most (C_0 + K e^K) e^{−θt} ||Φ||_{C^1}. This uses the Lipschitz bound of Φ in the second variable.
   - Multiplying by e^{J_t(p)} ≤ e^{C_1} e^{(λ+δ)t} and e^{J_{−t}(x)} ≤ e^{C_1} e^{(−λ+δ)t} gives |F_2(t)| ≤ C e^{−(θ−2δ)t} ||Φ||_{C^1}.
5. **Case t ≤ 0.** Write s = −t ≥ 0, fix q and sum over p. The same computation in the first variable, using backward asymptoticity, gives a factor e^{J_{−s}(x)} e^{−θs} ||Φ||_{C^1}, multiplied by e^{J_s(q)}. The bounds e^{J_{−s}(x)} ≤ C e^{(−λ+δ)s} and e^{J_s(q)} ≤ C e^{(λ+δ)s} give |F_2(t)| ≤ C e^{−(θ−2δ)|t|} ||Φ||_{C^1}.
6. Take ε = θ − 2δ > 0. ∎

The point is that the forward Jacobian growth of one factor is cancelled by the backward Jacobian growth of the other, because J_t(p) + J_{−t}(q) = o(|t|). So λ drops out, and the strip-position problem of (EF) disappears.

**Proposition T' (general S).** Let S be a distribution density on M with |S(Γ_t φ)| ≤ C e^{ρ(t)} ||φ||_{C^k}, where ρ(t) + ρ(−t) ≤ −ε|t|. This covers, for example, ρ(t) = a't for t ≥ 0 and ρ(t) = −b'|t| for t ≤ 0 with a' < b' (the hypothesis of (J1), any position of the interval (a', b')). Then |(S⊗S)(Γ^Y_t Φ)| ≤ C' e^{−ε|t|} ||Φ||_{C^{2k}}, and S⊗S ≠ 0 if S ≠ 0.

*Proof.*
1. Write (S⊗S)(Γ_t⊗Γ_{−t} Φ) = S(Γ_t f_t), where f_t(x_1) := S(Γ_{−t} Φ(x_1, ·)).
2. Derivatives in x_1 commute with S and with Γ_{−t} acting in x_2. So ||f_t||_{C^k} ≤ C e^{ρ(−t)} ||Φ||_{C^{2k}}. This step is the reason for the C^{2k} norm: x_1-derivatives fall on Φ, not on g_t.
3. Then |S(Γ_t f_t)| ≤ C e^{ρ(t)} ||f_t||_{C^k}, and the bound follows from ρ(t) + ρ(−t) ≤ −ε|t|. ∎

## 3. The reduction to (J2) / (SS_Y), and the model check

**(J2)** Under GH of X, no nonzero distribution density S_2 on M×M satisfies |S_2(Γ^Y_t Φ)| ≤ C e^{−ε|t|} ||Φ||_{C^k} for all t.

**(SS_Y)** Under GH of X, P_Y^T is semisimple at 0 in finite order.

**Corollary 3.1 (proved).**
(a) (SS_Y) ⇒ (J2). This is Lemma S.
(b) (J2) ⇒ every GH flow has zero topological entropy. Use step 1 of the chain and Proposition T.
(c) (J2) ⇒ (EF), for strips in any position.
 - A nonzero EF on Σ(a,b) gives, by Theorem 2.1(B) of R8-b, a nonzero S with rates a' < b'. The uniform bounds (ii) of (EF) imply (E3).
 - Proposition T' then gives a nonzero two-sided decaying S⊗S, which contradicts (J2).
So (J2) implies (EF) and is formally stronger. Its advantage is that it is a statement at the single spectral point 0, which is where Jordan-chain arguments work.

**Model check (proved).** Let X = Σ α_i ∂_i on T^n with α Diophantine, ν = Lebesgue (so d = 0), and e_k = e^{2πi k·x}. Then P_Y(e_k⊗e_l) = 2πi (k−l)·α e_k⊗e_l. Let A, B be as in (SS_Y).
- A∘P_Y = 0 gives A(e_k⊗e_l) = 0 unless (k−l)·α = 0, i.e. unless k = l.
- B∘P_Y = A gives A(e_k⊗e_k) = B(P_Y(e_k⊗e_k)) = 0.
So A vanishes on trigonometric polynomials, hence A = 0. (SS_Y) is invariant under smooth conjugacy and under ν → e^cν, because P_Y is conjugated by multiplication by e^{c(x_1)+c(x_2)}. So (SS_Y), and hence (J2), holds for every field smoothly conjugate to a Diophantine linear flow. These are the only known GH fields. By contrast, the kernel of P_Y^T is infinite-dimensional here (the e_k⊗e_k-dual functionals), so (K0) fails for Y and Theorem J cannot be used as it stands.

## 4. Where it stops (precise)

1. **Y is not GH, even in the model**, so GH of X cannot be applied on M×M directly. What GH of X gives on M×M I could identify:
   - Partial pairing. Let A^ψ(φ) := A(φ⊗ψ). Then A∘P_Y = 0 gives A^ψ∘P = A^{Pψ}, and B∘P_Y = A gives B^ψ∘P = B^{Pψ} + A^ψ.
   - In the volume case (ν = ω, P = X) take ψ = 1. Then A^1∘X = 0, so A^1 = cω by (K0). Next B^1∘X = cω, so c = 0 by (K1). So A(·⊗1) = A(1⊗·) = 0: only the "zero mode" is killed.
   - Without a volume no function ψ has Pψ = 0, and not even this step is available.
   - The remaining modes would need the joint spectrum of (X_1, X_2) near the diagonal to be "discrete". That is the same missing spectral input as in (EF): absence of continuous spectrum of P^T off the point 0.
2. **The tensor objects are exactly Jordan chains of the M-families.** If T_z is the Laplace family of S on the line Re z = c, Parseval gives
   m_0 = (1/2πi) ∫_{Re z=c} T_z⊗T_z dz and m_1 = −(1/2πi) ∫ T'_z⊗T_z dz.
   Check: (T'_z⊗T_z)∘P_Y = T_z⊗T_z, because T'_z∘P = zT'_z + T_z.
   So (SS_Y) for these particular tensors means: superposed Jordan chains (T'_z, T_z) of P^T along a vertical line cannot exist. By Prop 3.2 of R8-b, this is the same object that (EF) must exclude. The tensor trick removes the dependence on the strip's position and the sign of λ (no more λ = 0 versus λ ≠ 0 cases), but not the spectral core.
3. **Variants checked (dead ends).**
   - (X, X) with S^u⊗S^s, an unstable pair times a stable pair: two-sided decay only when |λ| is small. In the λ = 0 case it works, but X⊕X is not GH either, and its kernel contains T_z⊗T_{−z}.
   - (X, −cX), or X⊕cX with c ≠ 1: for a nonzero EF on a strip, (K0) fails for every c close to 1, because z = cw has solutions with both z and w in the strip. So "K0 for some c" is again equivalent to the spectral statement.
   - S⊗T_{z0}, with T_{z0} an eigen-distribution and Re z_0 in the strip: this decays two-sided. But its moment chain is (Taylor coefficients of T_z at z_0)⊗T_{z_0}, so (SS_Y) for it is exactly "no Jordan chain of P^T at z_0". That is Remark 3.3 of R8-b, where GH gives nothing.

## 5. A positivity reformulation (proved; recorded for future use)
Let S be real as in Proposition T', with rates a' < b', and let c ∈ (a', b'). Put ι_c(φ)(t) := e^{−ct} F_φ(t). Then:
- ι_c(φ) ∈ L^1 ∩ L^∞ ⊂ L^2(R), with ||ι_c φ||_{L^2} ≤ C ||φ||_{C^k};
- ι_c(Pφ) = (d/dt + c) ι_c(φ);
- ι_c(Γ_s φ) = e^{cs} τ_s ι_c(φ), where τ_s is translation by s.

The closure of ι_c(C^∞) is translation-invariant. By Wiener's theorem (cited: closed translation-invariant subspaces of L^2(R) are {f : f̂ = 0 a.e. off E}), it equals L^2_E. Its Fourier transforms are ξ ↦ T_{c+iξ}(φ), which are real-analytic and not all identically 0. So E has full measure, and ι_c has dense range in L^2(R).

Thus a nonzero EF is equivalent to a C^k-continuous map C^∞(M) → L^2(R) with dense range that intertwines P − c with d/dt, i.e. Lebesgue spectrum of P^T on the line Re z = c. The positive forms Q_c(φ, ψ) = ∫ e^{−2ct} F_φ \overline{F_ψ} dt satisfy Q_c∘(P⊗1 + 1⊗P̄) = 2c Q_c. GH would have to forbid this. I could not connect it to GH: no smooth density is Q_c-continuous, since point-mass orbits do not see bumps placed away from them for long times.

## 6. Summary

**Proved here:**
- Lemma S: Theorem J under semisimplicity at 0.
- Proposition T and T': a positive-entropy ergodic measure, of any λ, gives a two-sided exponentially decaying tensor S⊗S for Y = (X, −X) on M×M. So does any (J1)-type S in any strip position.
- Corollary 3.1: (SS_Y) ⇒ (J2) ⇒ zero entropy, and (J2) ⇒ (EF).
- (SS_Y) holds for all fields smoothly conjugate to Diophantine linear flows.
- (SS_Y) is reduced to the zero mode in the volume case (Section 4.1).
- The L^2 / Lebesgue-spectrum reformulation of a nonzero EF.

**Not proved / open:**
- (EF) itself.
- (J2) and (SS_Y) under GH.
- Hence the problem in dimension ≥ 4 (the case left open by Theorem 5.2 of R6-a).

**Open questions, stated precisely:**
- (Q1) Does GH of X imply that P⊗1 − 1⊗P has no finite-order Jordan chain at 0 on M×M?
- (Q2) Does GH imply that P^T has no Jordan chain (B∘P = zB, A∘P = zA + B, B ≠ 0) of order ≤ 1 at z with Re z ≠ 0? This would give (EF), by Prop 3.2 of R8-b.

I see no way to use GH at z ≠ 0, or on M×M, that is not circular.

Literature recalled from memory, unverified: the Greenfield–Wallach / Katok conjecture (GH ⇒ smoothly conjugate to a Diophantine linear flow), with results in dimension 3 by Forni and Kocsard. I do not recall any published proof of zero entropy for GH flows in general dimension.

=== END OF ANSWER round9_q5 ===
