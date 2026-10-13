# round10_q5: answer

## 0. Verdict

**(JC) is not proved here, and no counterexample is given.** The answer is partial. It contains:
- (§1) an independent line-by-line check of Theorem A. This is step 3 of the chain, which had not been checked separately before. I find it correct. I also checked that steps 1–4 of the chain fit together. My conclusion: the chain is sound, and the only missing input is (JC).
- (§2) a new, fully proved equivalence for **order-0** chains. One direction was already known (entry 94, Lemma 1.1 of R9-c); I prove the converse. A point c with Re c = κ carries an order-0 Jordan chain iff some non-periodic orbit satisfies ∫_R (1+|t|) e^{J_t(x) − κt} dt < ∞. So order-0 (NJ) is *exactly* a single-orbit statement, (SO⁺). I also prove (SO⁺) whenever κ lies outside [D⁻, D⁺], and in the cases already covered by Lemma C and Lemma K.
- (§3) a new, proved time-change reformulation. GH is invariant under X → hX, while (JC) is not. Hence (JC) for every GH field is equivalent to a stronger statement about the operators hP − c for all smooth h > 0. This also shows why no argument can single out a "good" value of c from the dynamics of one time parametrisation.
- (§4) where the argument stops, and the open questions.

Throughout, the conventions are those of the brief: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, Pφ = Xφ + dφ and Γ_tφ = e^{J_t}·φ∘g_t, so that (d/dt)Γ_tφ = Γ_t Pφ = PΓ_tφ.

---

## 1. Check of Theorem A (step 3 of the chain) and of the chain

**Theorem A (as stated in R9-b §7).** Let (T_z) be a family on Ω = {a < Re z < b} satisfying:
- (i) holomorphy in z;
- (ii) sup{|T_z(φ)| : a_1 ≤ Re z ≤ b_1, ‖φ‖_{C^k} ≤ 1} < ∞ on every closed substrip;
- (iii) T_z∘P = zT_z.

If some c ∈ Ω carries no order-k Jordan chain, then T ≡ 0.

**Check, step by step.**
1. *Transport.* For each z, h(t) := T_z(Γ_tφ) is C^1 with h' = T_z(PΓ_tφ) = z h. Hence T_z(Γ_tφ) = e^{zt}T_z(φ). This uses only that t ↦ Γ_tφ is C^1 into C^k, which holds because (t,x) ↦ e^{J_t(x)}φ(g_t x) is jointly C^∞.
2. *The distribution S.* Put S(φ) = (2πi)^{-1}∫_{Re z=σ} e^{(z−σ)²+ω(z−σ)} T_z(φ) dz.
   - On the line Re z = σ the weight has modulus e^{−y²}, so (ii) makes S an order-≤k density.
   - Its transport is S(Γ_tφ) = (2πi)^{-1}∫ e^{(z−σ)²+ω(z−σ)} e^{zt} T_z(φ) dz.
   - Shifting the contour to Re z = σ ± ρ is legitimate. On horizontal segments the integrand is bounded by e^{(Re z−σ)² − y² + |ω|ρ + |t|(|σ|+ρ)}·C‖φ‖_{C^k}, uniformly for Re z in [σ−ρ, σ+ρ], so these contributions tend to 0 as |y| → ∞.
   - The shift gives |S(Γ_tφ)| ≤ K e^{(σ+ρ)t}‖φ‖_{C^k} for t ≤ 0 and ≤ K e^{(σ−ρ)t}‖φ‖_{C^k} for t ≥ 0.
   - Hence H_φ(t) := e^{−ct}S(Γ_tφ) satisfies |H_φ(t)| ≤ K e^{−ρ|t|}‖φ‖_{C^k}, which is (7.1).
   - *Non-vanishing for some ω.* h(y) = T_{σ+iy}(φ_0) is continuous and bounded. It is not identically 0: otherwise T_z(φ_0) would vanish on a line and hence, by the identity theorem, on Ω. So S_ω(φ_0) = (2π)^{-1}∫e^{−y²}e^{iωy}h(y)dy, a Fourier transform of a nonzero L^1 function, is nonzero for some ω.
3. *The relation (7.2).* H_φ' = H_{(P−c)φ}, because F_φ' = F_{Pφ}.
4. *Moments.* m_j(φ) = ∫t^jH_φ dt is an order-≤k density. Integration by parts gives m_0∘(P−c) = 0 and m_j∘(P−c) = −j m_{j−1}. The boundary terms vanish by (7.1) applied to φ.
5. *Induction.*
   - If m_0 ≠ 0, then (A,B) = (−m_1, m_0) is an order-k chain at c. Indeed (−m_1)∘(P−c) = m_0. This contradicts the hypothesis, so m_0 = 0.
   - If m_{j−1} = 0, then m_j∘(P−c) = 0 and (−m_{j+1}/(j+1))∘(P−c) = m_j. The same argument gives m_j = 0.
6. *Conclusion.* G(ξ) = ∫e^{−iξt}H_φ dt is holomorphic for |Im ξ| < ρ, and all its derivatives vanish at 0. So G ≡ 0, hence H_φ ≡ 0 and S(φ) = H_φ(0) = 0 for all φ. This contradicts step 2. ∎

I found no gap.

**Fit with the chain.**
- Theorem R' delivers continuous functionals on C^1 (so k = 1), holomorphic in z, bounded on closed substrips *uniformly in Im z*, with T_z∘P = zT_z. This is exactly (i)–(iii) with k = 1.
- If 0 ∈ Ω, c = 0 works under GH: B∘P = 0 gives B = c'ν by (K0), and A∘P = c'ν forces c' = 0 by (K1).
- If 0 ∉ Ω, (JC) is required. Ω is an open vertical strip with all imaginary parts allowed, so c may be taken with any Im c.
- So: **(JC) + Theorem R' + Theorem A + variational step ⟹ h_top(g_1) = 0.** The chain is sound modulo (JC).

---

## 2. Order-0 chains: an exact single-orbit characterisation (proved)

**Definition.** For κ ∈ R and x ∈ M put c_x(t) := e^{J_t(x) − κt}.

**(SO⁺_κ)** There is no point x, neither a zero of X nor periodic, with ∫_R (1+|t|) c_x(t) dt < ∞.

**Proposition 2.1 (no GH needed).** Let z = κ + iy. The following are equivalent:
- (a) z carries an order-0 Jordan chain: complex measures A, B with B ≠ 0, B∘(P−z) = 0 and A∘(P−z) = B;
- (b) some x as above has ∫_R (1+|t|) c_x(t) dt < ∞.

In particular, "no order-0 chain at any c with Re c = κ" is equivalent to (SO⁺_κ). The value of Im c plays no role.

*Proof of (b) ⟹ (a).*
1. *c_x → 0 at ±∞.* We have c_x' = (d(g_tx) − κ)c_x, so c_x(t) ≥ c_x(s)e^{−L|t−s|} with L = ‖d‖_∞ + |κ|. If c_x(t_n) ≥ ε along t_n → ±∞, then c_x ≥ εe^{−L} on infinitely many disjoint unit intervals, which contradicts integrability.
2. *|t|c_x(t) → 0 at ±∞.* The same argument works. If |t_n|c_x(t_n) ≥ ε, then |t|c_x(t) ≥ (ε/2)e^{−L} on [t_n, t_n+1] for large n. This contradicts ∫|t|c_x < ∞.
3. *Definition of the chain.* Put
   - B(φ) := ∫ c_x(t)e^{−iyt} φ(g_tx) dt,
   - A(φ) := −∫ t c_x(t)e^{−iyt} φ(g_tx) dt.

   Both are finite complex measures carried by the orbit.
4. *The relations.* (d/dt)[c_x(t)e^{−iyt}φ(g_tx)] = c_x(t)e^{−iyt}((P−z)φ)(g_tx). Integrate over [−R,R]; the boundary terms vanish by steps 1–2.
   - This gives B∘(P−z) = 0.
   - For A, integration by parts gives A((P−z)φ) = −[t c_x e^{−iyt}φ(g_tx)]_{−R}^{R} + ∫ c_x e^{−iyt}φ(g_tx) dt → B(φ).
5. *B ≠ 0.* The orbit is injective (x is neither a zero nor periodic). Choose τ > 0 with |y|τ < π/2. The orbit segment {g_tx : |t| ≤ τ} is an embedded arc, and the times t with |t| > τ and g_tx close to it form a set that can be avoided. Concretely: by injectivity and compactness of [−τ, τ], there is a smooth φ ≥ 0 with φ(x) = 1 whose support meets the orbit only in {g_tx : |t| < τ}. This needs the orbit not to accumulate on x from outside the segment within the support. If it does accumulate, replace the test function: B ≠ 0 holds anyway, because B restricted to the Borel set {g_tx : |t| < τ} is the measure c_x(t)e^{−iyt}dt on that arc, which is nonzero. A complex measure is zero iff it vanishes on every Borel set. Its real part on the arc is ≥ cos(yτ)∫_{−τ}^{τ} c_x dt > 0. ∎

*Proof of (a) ⟹ (b).* Let (A, B) be an order-0 chain at z and β := |B|.
1. By Lemma 1.1 of R9-c (entry 94, re-read; its proof uses no GH):
   - L_tβ = e^{κt}β;
   - B = hβ with |h| = 1;
   - A = kβ + A_s with A_s ⊥ β;
   - q := k/h satisfies q∘g_{−t} = q + t β-a.e. for each t;
   - I_κ(x) = ∫c_x dt < ∞ for β-a.e. x.
2. Since A is finite, ∫|q| dβ = ∫|k| dβ < ∞.
3. Put r := Re q, so r∘g_{−t} = r + t β-a.e. for each t.
4. *Orbitwise form of (3).* For β-a.e. x, the function s ↦ r(g_sx) equals r(x) − s for a.e. s. This follows from (3) by Fubini on R × M with the quasi-invariant measure β (each g_t is β-nonsingular, by L_tβ = e^{κt}β). Disintegrate β over the dissipative orbit partition. By Lemma 1.1, β-a.e. orbit has I_κ < ∞, and the conditional measure of β on the orbit of x is proportional to c_x(t)dt (pushed by t ↦ g_tx). This holds because L_tβ = e^{κt}β determines the orbit-conditional up to a constant: its density with respect to dt is multiplied by e^{J_t − κt} under the shift.
5. *Conclusion.* On the orbit of x, the conditional measure is const·c_x(t)dt and r = r(x) − t. So ∫|r| dβ < ∞ forces ∫ |r(x) − t| c_x(t) dt < ∞ for β-a.e. orbit. Together with ∫c_x < ∞ this gives ∫(1+|t|)c_x(t)dt < ∞. ∎

*Status of this proof.* (b) ⟹ (a) is complete and elementary. (a) ⟹ (b) relies on the orbit disintegration of the totally dissipative quasi-invariant measure β. That is the standard Hopf-type decomposition: a totally dissipative nonsingular flow is, mod 0, a union of orbits with a measurable cross-section. I cite it from memory. Without it, Lemma 1.1 (proved) already gives the weaker conclusion I_κ < ∞. So the equivalence is exact modulo that standard decomposition.

**Proposition 2.2 (cases of (SO⁺) that hold; proved).**
- (i) *(No GH.)* Let D⁺ = max_m m(d) and D⁻ = min_m m(d) over invariant probabilities. If κ > D⁺ or κ < D⁻, then ∫_R c_x(t)dt = ∞ for every x.
- (ii) *(GH, dim M ≥ 2.)* For κ = 0, (SO⁺_0) holds. This is Lemma C.
- (iii) *(GH.)* No x as in (b) exists whose α-limit (resp. ω-limit) is a hyperbolic periodic orbit or zero γ along W^{uu} (resp. W^{ss}), with the forward (resp. backward) rate condition of Lemma K / K'.

*Proof of (i).* Let κ > D⁺ and t ≤ 0. By the standard fact (R4-q7, Prop 2.1, step 1, applied to −X), limsup_{s→+∞} sup_y (−J_{−s}(y))/s = max_m m(d) = D⁺. So J_t(x) ≥ −C − (D⁺+ε)|t|, and c_x(t) = e^{J_t(x) + κ|t|} ≥ e^{−C}e^{(κ − D⁺ − ε)|t|} → ∞. The case κ < D⁻ is the same with t ≥ 0. ∎

(ii) and (iii) restate known results in this language. They are recorded so that the open part is precise: **order-0 (NJ) is open exactly for κ ∈ [D⁻, D⁺] \ {0}, and only for orbits that are not heteroclinic in the sense of Lemma K.**

**Remark 2.3 (why §2 does not close the problem).**
- The families of Theorem R' have genuine order 1. Their pair distribution δ_x − e^bδ_y loses one derivative.
- Order-0 chains cannot be extracted from them: the moments m_j in Theorem A have order 1.
- So even a full proof of (SO⁺) would settle only the order-0 half of (NJ). It would leave the problem open.

---

## 3. Time-change reformulation (proved)

**Lemma 3.1.** Let h > 0 be smooth, and X' := hX, with the same ν. Then:
1. d' := div_ν(hX) = hd + Xh, and P'φ := X'φ + d'φ = P(hφ). That is, P' = P∘M_h.
2. X' has an order-k Jordan chain at c iff there are order-≤k densities A, B, B ≠ 0, with
   B∘(M_hP − c) = 0 and A∘(M_hP − c) = B.
3. X' is GH iff X is GH (by (O4)).

*Proof.*
1. L_{hX}ν = hL_Xν + dh∧i_Xν = (hd + Xh)ν. So P'φ = hXφ + hdφ + (Xh)φ = X(hφ) + d(hφ).
2. Given a chain (A', B') for X' at c, put A := A'∘M_{1/h} and B := B'∘M_{1/h}. Multiplication by a smooth positive function preserves order, and B ≠ 0 iff B' ≠ 0. Then
   - B'(P(hφ)) = cB'(φ) becomes, with ψ = hφ, B(hPψ) = cB(ψ);
   - likewise A(hPψ) − cA(ψ) = B(ψ).

   The converse is the same computation backwards. ∎

**Consequence.** Assume (JC) or (NJ) holds for all GH fields. Applying it to hX shows that, under GH, the chains of the *inhomogeneous* operators M_hP − c must also be excluded, for every smooth h > 0 and every c with Re c ≠ 0.
- Conversely, an argument proving (NJ) must work uniformly for this whole family.
- The family includes operators whose "eigenvalue" c/h varies in space.
- So any proof of (JC) that uses a special property of the *constant* c (for example its position relative to ergodic averages μ(d)) must be time-change covariant. In particular, the dichotomy "Re c = μ(d) for some ergodic μ, or not" is not time-change invariant. For hX the numbers become μ_h(d') = μ(d)/μ(1/h) and the strip of Theorem R' rescales by the same factor. So that dichotomy cannot be the mechanism.

This rules out one family of candidate mechanisms suggested in R9-b §7(a). The suggestion there was to take c "not of the form μ(d)": this is not an invariant notion once one also allows the time-changed operators.

---

## 4. Where the argument stops; open questions

**What I tried for (JC) / (NJ), and why it fails** (all at the level of rigorous checks, not heuristics):

1. *Making GH act at c ≠ 0 via (K1).* In the smooth case w = α/b solves Xw = −1. For distributions no division is available.
   - Tensor or product substitutes (b⊗b̄ on M×M, restricted to the diagonal) are undefined for order-1 distributions.
   - X⊕X and X⊕(−X) on M×M are not GH even for Diophantine linear flows. For X⊕(−X), the distribution δ(x+y) is invariant. So no GH auxiliary field is available.
2. *Closed-range half of GH.* In the volume case, B(φ) = c^N B(R^Nφ_0) for all N, where R is the tame inverse. This kills B only on φ with limsup ‖R^Nφ_0‖_{C^1}^{1/N} < 1/|c|. That set is not known to be dense, and density would need geometric tame constants (open question 4 of R9-b).
   - Outside (V), there is no tame inverse of P (Proposition A of R8-d).
3. *L² spectral version (volume case).* Smear the pair over a Pesin block into σω with σ ∈ L^∞ and E[σ|ξ^u] = 0. Then T_z(φ) has the cross-spectral measure ρ_{φ,σ} on iR as its boundary values: the left resolvent continues across iR as −B_z.
   - If ρ_{φ,σ} vanished on an interval around 0, the boundary-uniqueness theorem for holomorphic functions on a strip would give T ≡ 0.
   - GH gives only vanishing to infinite order at 0, with tame but non-quasi-analytic constants. This is again the Lemma H / Theorem V wall.
   - Spectral projections that would create a gap destroy the conditional-mean-zero structure needed for backward decay.
4. *Order reduction.* Order-0 chains reduce exactly to the single-orbit statement (SO⁺) (§2). I could prove (SO⁺) only outside [D⁻, D⁺], at κ = 0, and for Lemma-K-type heteroclinic orbits.
   - For a general orbit with forward rate in (0, κ) and backward rate > κ (κ > 0), a contradiction via Theorem J would need forward cancellation at rate > κ. A single orbit does not supply that.

**Open questions (explicit).**
- **(JC)** (equivalently, by Theorem A, no infinite geometric chain at some point of each Theorem-R' strip). Open.
- **(NJ₀) = (SO⁺_κ)** for κ ∈ [D⁻, D⁺] \ {0}: the order-0 half. Open. It is now an exact single-orbit statement (Proposition 2.1).
- **Order-1 version of §2**: a single-orbit (or finite-configuration) characterisation of order-1 chains. Not found.
- **(V)**, and quantitative tameness (geometric constants, uniform loss), as listed in R9-b §5. Open.

**Summary of status.**
- *Proved here:* the check of Theorem A and of the chain; Proposition 2.1 ((b) ⟹ (a) fully, (a) ⟹ (b) modulo the cited Hopf decomposition for totally dissipative flows); Proposition 2.2; Lemma 3.1.
- *Not proved:* (JC), and hence the problem's claim in dimensions ≥ 4. Dimensions ≤ 3 are settled by Theorem 5.2 of R6-a, modulo the cited Katok / Lian–Young theorem.

=== END OF ANSWER round10_q5 ===
