# round10_q3: answer

## Status in one paragraph
I did **not** prove (JC), (NJ) or zero entropy, and I found no counterexample. What this file adds:
1. **§1, an independent line-by-line check of step 3 of the chain (Theorem A, block R9-b §7).** The brief marks this step as never checked separately. It is **correct as stated**, with k = 1 and with chains of order ≤ 1 exactly as (JC) defines them. So (JC) does deliver the hypothesis Theorem A needs. I did not re-check steps 1–2; they were checked by round9_q10 and others.
2. **§2, the order-0 case of (NJ), pinned down to a statement about single orbits.** (Proposition 2.1 and Corollary 2.2, proved.) Fix a line Re c = κ ≠ 0.
   - If (SO) holds at κ, there are no order-0 chains on that line. This direction is the existing Lemma 1.1 of R9-c (block R9-c). (SO) at κ says: ∫_R e^{J_t(x) − κt} dt = ∞ for every x.
   - Conversely, a single orbit with ∫(1+|t|) e^{J_t(x) − κt} dt < ∞ gives an order-0 chain at **every** point of that line.
   - So, up to the factor (1+|t|), order-0 (NJ) is the same as (SO).
3. **§3, (SO) for orbits running from one hyperbolic critical element to another (proved).** "Critical element" means a periodic orbit or a zero of X. The proof uses Corollary 4.1 of R6-a.
4. **§4, why the order-1 case does not reduce to this, and the dead ends I checked.** I checked three:
   - smooth-coefficient combinations of b and α;
   - time changes and changes of ν (neither can move Re c to 0);
   - contour superpositions (they never give two-sided decay when 0 is outside the strip).
   §4 also lists the open questions.

Conventions are those of the brief: P = X + d, Γ_t φ = e^{J_t} φ∘g_t, d/dt Γ_t φ = Γ_t Pφ = P Γ_t φ.

---

## 1. Independent check of Theorem A (step 3 of the chain)

**Statement checked.** This is Theorem A of R9-b §7, with k = 1. Let (T_z), z ∈ Ω = {a < Re z < b}, be continuous functionals on C^1 such that:
- (i) z ↦ T_z(φ) is holomorphic on Ω;
- (ii) T_z is bounded on closed substrips, uniformly over ‖φ‖_{C^1} ≤ 1;
- (iii) T_z∘P = z T_z.

Suppose one point c ∈ Ω carries no order-1 Jordan chain. Then T ≡ 0.

**Checks, step by step.**

(0) *Transport identity.* T_z(Γ_t φ) = e^{zt} T_z(φ).
- The map t ↦ Γ_t φ is C^1 into C^1(M), indeed into C^∞, with derivative Γ_t Pφ.
- Γ_t commutes with P, because P is the generator of the group Γ_t.
- So h(t) = T_z(Γ_t φ) satisfies h′ = T_z(PΓ_t φ) = z h, with h(0) = T_z(φ).
- This identity is what makes F_φ(t) = S(Γ_t φ) computable by moving the contour. The bound obtained involves ‖φ‖_{C^1}, not ‖Γ_t φ‖_{C^1}. That is essential, and the identity provides it.

(1) *Contour integral.* Put S(φ) = (1/2πi) ∫_{Re z = σ} e^{(z−σ)² + ω(z−σ)} T_z(φ) dz.
- On Re z = σ + s with |s| ≤ ρ:
  - |e^{(z−σ)²}| = e^{s² − y²}, which is Gaussian in y;
  - |e^{ω(z−σ)}| = e^{ωs};
  - T_z is bounded by (ii).
- So S is a continuous functional on C^1, and
  F_φ(t) = (1/2πi) ∫ e^{(z−σ)² + ω(z−σ)} e^{zt} T_z(φ) dz.
- Shifting the contour to Re z = σ ± ρ is legitimate. The integrand is holomorphic by (i). On the horizontal segments it is bounded by C e^{ρ² − Y²} e^{|ω|ρ + (|σ|+ρ)|t|} ‖φ‖_{C^1}, which tends to 0 as Y → ∞ for fixed t.
- Hence |F_φ(t)| ≤ K e^{(σ±ρ)t} ‖φ‖_{C^1}, with the sign chosen according to the sign of t. K depends on ω, which is fixed.
- So H_φ(t) = e^{−ct} F_φ(t) satisfies |H_φ(t)| ≤ K e^{−ρ|t|} ‖φ‖_{C^1}.

*Non-vanishing.*
- If T ≢ 0, pick φ_0 and z_0 with T_{z_0}(φ_0) ≠ 0. By the identity theorem, y ↦ T_{σ+iy}(φ_0) is not identically 0. It is continuous and bounded.
- S_ω(φ_0) = (1/2π) ∫ e^{−y²} e^{iωy} T_{σ+iy}(φ_0) dy. This is the Fourier transform of a nonzero L^1 ∩ C^0 function, so it is ≠ 0 for some ω.
- Fix that ω. Checked.

(2) *Moments.* H_φ′ = H_{(P−c)φ}, since F_φ′ = F_{Pφ}. Both H_φ and H_{(P−c)φ} are O(e^{−ρ|t|}), so the boundary terms t^j H_φ(t) vanish at ±∞. Integration by parts gives:
- m_0∘(P−c) = 0;
- m_j∘(P−c) = −j m_{j−1} for j ≥ 1.

Each m_j is bounded by K ∫ |t|^j e^{−ρ|t|} dt · ‖φ‖_{C^1}, so each m_j is continuous on C^1, i.e. of order ≤ 1. Checked.

(3) *Induction.*
- If m_0 ≠ 0, then (A, B) = (−m_1, m_0) is an order-1 chain at c. Indeed (−m_1)∘(P−c) = m_0 and m_0∘(P−c) = 0. This is exactly the chain of (JC):
  - B∘P = cB;
  - A∘P = cA + B.
- So m_0 = 0.
- Inductively, if m_{j−1} = 0, then (−m_{j+1}/(j+1), m_j) is a chain at c, so m_j = 0. Checked.

(4) *Fourier uniqueness.* G(ξ) = ∫ e^{−iξt} H_φ(t) dt is holomorphic on |Im ξ| < ρ, and all its derivatives vanish at 0. So G ≡ 0, hence H_φ ≡ 0, hence S(φ) = H_φ(0) = 0 for every φ. This contradicts (1). Checked.

**Compatibility with the chain.** Theorem R′ (as quoted in the chain) supplies (i)–(iii) with order 1, which is exactly the order in (JC). In step 4 of the chain the strip is Ω = Σ(λ+δ, λ+θ−δ), so applying (JC) with a = λ+δ and b = λ+θ−δ provides the needed point c.

**Verdict:** step 3 is sound. Combined with steps 1–2 as checked by others, the problem is equivalent, along this chain, to (JC).

---

## 2. Order-0 chains: (NJ) at order 0 versus single-orbit integrability

Let κ ∈ R. Put I_κ(x) = ∫_R e^{J_t(x) − κt} dt and I^{(1)}_κ(x) = ∫_R (1+|t|) e^{J_t(x) − κt} dt.

**Proposition 2.1 (no GH needed).** Suppose x is neither a zero of X nor periodic, and I^{(1)}_κ(x) < ∞. Then every z with Re z = κ carries an order-0 Jordan chain. Explicitly:
- B_z(φ) = ∫_R e^{J_t(x) − zt} φ(g_t x) dt;
- A_z(φ) = −∫_R t e^{J_t(x) − zt} φ(g_t x) dt;
- B_z ≠ 0, B_z∘P = z B_z and A_z∘P = z A_z + B_z.

*Proof.*

*Boundary decay.* Put e(t) = (1+|t|) e^{J_t(x) − κt}.
- Since |d/dt (J_t − κt)| ≤ ‖d‖_∞ + |κ| =: L, and log(1+|t|) is 1-Lipschitz, we have e(t) ≥ e(s) e^{−(L+1)|t−s|}.
- If e(t_n) ≥ ε along t_n → ±∞, then e ≥ ε e^{−(L+1)} on infinitely many disjoint unit intervals. That contradicts ∫ e < ∞.
- Hence e(t) → 0 as |t| → ∞. This is the argument of Lemma C.

*Eigen-relations.* For smooth φ, d/dt [e^{J_t(x)} φ(g_t x)] = e^{J_t(x)} (Pφ)(g_t x).
- For B_z, integrate by parts on [−R, R]: B_z(Pφ) = [e^{J_t − zt} φ(g_t x)]_{−R}^{R} + z B_z(φ). The boundary term tends to 0.
- For A_z, the same computation gives
  A_z(Pφ) = −∫ t e^{−zt} d/dt[e^{J_t} φ(g_t x)] dt = ∫ (1 − zt) e^{J_t − zt} φ(g_t x) dt = B_z(φ) + z A_z(φ).
  The boundary terms t e^{J_t − zt} φ(g_t x) tend to 0 because e(t) → 0.
- All integrals converge absolutely, because |e^{−zt}| = e^{−κt}.
- Both functionals are complex measures, i.e. of order 0.

*B_z ≠ 0.*
- Let π: R → M, π(t) = g_t x. It is continuous, and injective because x is neither periodic nor a zero.
- Put w(t) = e^{J_t(x) − zt}. This is continuous with |w| integrable, and w(0) = 1.
- By dominated convergence, B_z extends from smooth to continuous φ. It is then the complex Radon measure π_*(w dt).
- Suppose B_z = 0. For a compact interval I, π(I) is compact, hence Borel, and π^{−1}(π(I)) = I by injectivity. So 0 = B_z(π(I)) = ∫_I w dt for every compact interval I.
- Hence w ≡ 0, contradicting w(0) = 1. ∎

**Corollary 2.2 (order-0 (NJ) on a line is sandwiched between two single-orbit statements).** Fix κ ≠ 0.
- (a) (Lemma 1.1 of R9-c, quoted, no GH.) If an order-0 chain exists at some z with Re z = κ, then I_κ(x) < ∞ for |B|-a.e. x. Hence (SO_κ) ⇒ no order-0 chain on the line Re z = κ, where
  - (SO_κ): I_κ(x) = ∞ for every x ∈ M.
- (b) (Proposition 2.1.) If some non-stationary, non-periodic x has I^{(1)}_κ(x) < ∞, then every point of the line Re z = κ carries an order-0 chain. Hence order-0 (NJ) on that line ⇒ (SO′_κ), where
  - (SO′_κ): I^{(1)}_κ(x) = ∞ for every x ∈ M.
  Zeros and periodic points have I_κ = ∞ automatically, as in Lemma 1.1.
- Consequence: under GH, order-0 (NJ) is equivalent to (SO) up to the polynomial factor (1+|t|).
- Dynamical meaning (a heuristic only, not used anywhere): an orbit with I_κ(x) < ∞ has, on average, backward Jacobian slope at least κ and forward slope at most κ. So (SO_κ) forbids orbits whose backward limit measures have strictly larger mean of d than their forward limit measures, uniformly in the sense of the integral.

---

## 3. (SO) for orbits between hyperbolic critical elements (proved under GH)

**Proposition 3.1.** Assume GH. Let γ_1 and γ_2 be hyperbolic periodic orbits or hyperbolic zeros (possibly γ_1 = γ_2). Let x ∈ W^u(γ_1) ∩ W^s(γ_2), with x ∉ γ_1 ∪ γ_2. Then I_κ(x) = ∞ for every real κ.

*Proof.* Take the asymptotic phases q_i as in Corollary 4.1 of R6-a.
- J_t(x) = (t/P_2) I(γ_2) + O(1) for t ≥ 0.
- J_t(x) = (t/P_1) I(γ_1) + O(1) for t ≤ 0. For a zero, read I/P as d(p).
- Hence I_κ(x) < ∞ iff I(γ_2)/P_2 < κ < I(γ_1)/P_1.
- Corollary 4.1 of R6-a (proved under GH) gives I(γ_2) ≥ 0 ≥ I(γ_1). So no κ satisfies the condition. ∎

So by Corollary 2.2(a), no order-0 chain can be carried by such connecting orbits. In particular it cannot be carried by any Morse–Smale-type part of the dynamics. This does **not** cover order-0 chains carried by other orbits, and it says nothing about order 1.

---

## 4. Order 1: dead ends checked, and where it stops

Let b = B/ν and α = A/ν, so that Xb = −cb, Xα = −cα − b, with Re c ≠ 0.

(D1) *Smooth-coefficient combinations are information-free.* Let u = f b + g α with f, g smooth. Then
X u = (Xf − cf − g) b + (Xg − cg) α.
- For GH to act we would need Xu smooth. If b and α are "independent" modulo smooth functions, that forces Xg = cg and Xf − cf = g.
- A smooth g with Xg = cg vanishes: at a maximum point of |g|², X|g|² = 2 Re c |g|² must be 0.
- Then g = 0, so Xf = cf and f = 0 likewise.
- So no non-trivial combination exists. This confirms the "Leibniz is information-free" verdict of round9_q7.

(D2) *Changes of ν, conjugations and time changes cannot move Re c to 0.*
- Changing ν changes J_t by a bounded coboundary.
- A time change Y = hX turns an X-eigen-distribution into one transported by Y as b∘g^Y_{−t} = e^{cτ(·,t)} b, where τ(x,t) = ∫_0^t h(g^Y_s x) ds is the elapsed X-time.
  - τ has the sign of t, and |τ| ≍ |t|.
  - So the transport grows in one time direction and decays in the other, exactly as before.
  - Correspondingly, B∘P_Y = c B∘M_h is not an eigen-relation for Y.
- To shift the eigenvalue to 0 one would need a smooth a with Xa = c on supp b. That is impossible: supp b is closed and invariant, so it carries an invariant probability μ, and μ(Xa) = 0.

(D3) *Superpositions over c cannot give two-sided decay when 0 ∉ Ω.*
- For S = ∫ ψ(z) T_z dz over a vertical line in Ω, the bounds after contour shifting are e^{a′t} for t ≥ 0 and e^{b′t} for t ≤ 0, with a′ and b′ in (a, b).
- Both bounds decay only if a′ < 0 < b′, i.e. 0 ∈ Ω.
- So Theorem J (the c = 0 mechanism) never applies directly. Theorem A's renormalisation by e^{−ct} trades this for a chain at c, which is exactly (JC). This is circular.

**Where it stops.** Every construction I tried makes GH act either at the spectral point 0, through (K0)/(K1), or not at all. The only proved exclusions at Re c ≠ 0 are:
- order 0 in the volume case (Corollary 7.4 of R9-b);
- order-0 chains carried by connecting orbits (§3 above).

**Open questions (explicit).**
1. **(JC)/(NJ) at order 1.** Open. Along the checked chain this is equivalent to the problem.
2. **(SO_κ), κ ≠ 0, under GH.** Is ∫_R e^{J_t(x) − κt} dt = ∞ for every x? Open in general. It is proved in §3 for orbits between hyperbolic critical elements, and by Lemma C for κ = 0. It would settle order-0 (NJ) (Corollary 2.2), but not order 1.
3. **A jet-bundle version of Lemma 1.1** (the planner's route (1b)). It would need an equivariant measure representation of order-1 chains on the 1-jet bundle. Not attempted beyond the observation that Hahn–Banach extensions are not equivariant.

=== END OF ANSWER round10_q3 ===
