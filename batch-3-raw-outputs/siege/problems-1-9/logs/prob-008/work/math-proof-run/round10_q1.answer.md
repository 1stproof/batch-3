# round10_q1 — answer

## Plan
1. Check step 3 of the chain (Theorem A, block R9-b §7), which has not had a separate check.
2. Attempt (JC)/(NJ): find a way for GH to act at a point c with Re c != 0.
3. Record partial results and dead ends.

## 1. Check of Theorem A (step 3 of the chain): correct

I re-derived Theorem A line by line, in the setting of the chain: k = 1, Omega = Sigma(a,b), and a family (T_z) satisfying (i), (ii) and (iii). The proof is correct. Points checked:

- **Step 1 (Gaussian contour).** By Lemma 1.1 of R8-b, T_z(Gamma_t phi) = e^{zt} T_z(phi). Here Gamma_t phi is smooth, so (iii) applies. Write sigma = Re c and rho_omega(z) = exp((z-sigma)^2 + omega(z-sigma)). On the strip a' <= Re z <= b', |rho_omega| <= e^{rho^2 + |omega| rho} e^{-y^2}, and |T_z(phi)| <= C ||phi||_{C^1} by (ii). So the horizontal segments contribute nothing, and Cauchy's theorem moves the line Re z = sigma to Re z = b' (used for t <= 0) or to Re z = a' (used for t >= 0). This gives |S(Gamma_t phi)| <= K e^{b't} ||phi||_{C^1} for t <= 0 and <= K e^{a't} ||phi||_{C^1} for t >= 0.
  - S has order <= 1.
  - S is nonzero for a suitable omega, by Fourier uniqueness applied to the continuous L^1 function e^{-y^2} T_{sigma+iy}(phi_0). That function is not identically 0: otherwise T_z(phi_0) would vanish on a whole vertical line, hence on Omega by the identity theorem.
- **Renormalisation.** Put H_phi(t) = e^{-ct} S(Gamma_t phi). Since |e^{-ct}| = e^{-sigma t}, this gives |H_phi(t)| <= K e^{-rho|t|} ||phi||_{C^1} for all real t, and H_phi' = H_{(P-c)phi}.
  - The bound extends from C^inf to C^1 by density, because S is (C^1)-continuous and Gamma_t is bounded on C^1 for fixed t.
  - Hence the moments m_j(phi) = ∫ t^j H_phi dt are continuous on C^1, i.e. they are exactly functionals of the kind allowed in (JC).
- **Jordan relations.** m_0∘(P-c) = 0 and m_j∘(P-c) = -j m_{j-1}. Boundary terms vanish because of the two-sided exponential bound applied to phi; the integrals converge because the bound also applies to (P-c)phi, which is smooth.
  - If m_0 != 0, then (A,B) = (-m_1, m_0) satisfies B(P phi) = c B(phi) and A(P phi) = c A(phi) + B(phi). This is exactly the definition of an order-1 Jordan chain in (JC).
  - Induction: if m_{j-1} = 0, then m_j∘(P-c) = 0 and (-m_{j+1}/(j+1))∘(P-c) = m_j, so m_j = 0.
- **Quasi-analyticity.** The Fourier transform of H_phi is holomorphic on |Im xi| < rho and all its Taylor coefficients at 0 vanish. So H_phi = 0, and S(phi) = H_phi(0) = 0. This contradicts Step 1.

Conclusion: **step 3 of the chain is correct as stated.** If one point c of the strip of Theorem R' carries no order-1 Jordan chain in the sense of (JC), then the family vanishes identically.

Corollary 7.2 of R9-b is also correct, and it uses no GH: whenever some g_1-ergodic nu has positive entropy, *every* point of the strip Omega of Theorem R' carries an order-1 Jordan chain. So (JC) restricted to the strips of Theorem R' is literally equivalent to the problem's conclusion, via this chain.

I also re-read the other steps of the chain against the material.
- Step 1 (variational principle plus Jacobs' formula) is correct.
- Step 2 (Theorem R', the repaired form for g_1-ergodic nu) delivers exactly the hypotheses (i)-(iii) of Theorem A with k = 1:
  - holomorphy holds for all C^1 phi;
  - the bound on closed substrips is uniform in Im z;
  - T_z is nonzero off a discrete set.
- I found no flaw in the chain. **Its only missing link is (JC).**

## 2. Attempts on (JC)/(NJ) in this round: no proof

I could not prove (JC) or (NJ), nor zero entropy by any other route, and I found no counterexample. Below are the routes I checked, with the precise reason each one stops. None of them is new in substance. They only confirm the obstruction already recorded, namely that GH acts only at the spectral point 0.

### 2.1 Time changes cannot create a real tilt (computation, proved)
Let h > 0 be smooth and X' = hX. X' is GH by (O4). Write its flow as g'_{t'}x = g_{tau}x, with d tau/dt' = h(g_tau x). Then div_nu X' = h d + Xh, and the substitution ds = dr/h(g_r x) gives

 J'_{t'}(x) = J_tau(x) + log h(g_tau x) - log h(x).

Hence

 ∫_R e^{J'_{t'}(x) - kappa t'} dt' = h(x)^{-1} ∫_R exp( J_tau(x) - kappa ∫_0^tau (1/h)(g_r x) dr ) d tau.

So a constant tilt kappa for X' is the *variable* tilt kappa/h for X.
- At kappa = 0 the statement for X' (Lemma C applied to X') is the same as the statement for X. Time changes therefore give no new information at kappa = 0.
- At kappa != 0 the problem is unchanged: (SO) for all time changes is just (SO) with arbitrary positive variable tilts.
- This complements (D3) of R9-g. That remark showed that constant time changes and conjugations cannot move a strip horizontally. The computation above shows the same for non-constant time changes, at the level of the single-orbit integrals that govern order-0 chains (R9-c Lemma 1.1).

### 2.2 Volume case, absolutely continuous S: reduces to the known "coarse tail" obstruction
Assume GH and that X preserves a smooth positive density omega. Take nu = omega, so d = 0.

**Construction.** Let xi be the Ledrappier-Young unstable partition of omega for g_1 (or for a g_1-ergodic component; the unique ergodicity of (O2) makes omega flow-ergodic). Take a Pesin set A on which the backward contraction constants are bounded by C_0, and let A' be its xi-saturation. Put w := 1_{A'} (psi - E_omega[psi | xi]) with psi bounded. Then S := w omega satisfies:
- |S(phi o g_t)| <= 2 C_0' e^{-theta|t|} ||w||_inf ||phi||_{C^1} for t <= 0. Points of one cell converge backward; argue by the triangle inequality through the base point of the cell.
- |S(phi o g_t)| <= ||w||_{L^1} ||phi||_inf for t >= 0.
- S != 0 for suitable psi, because the conditionals are non-atomic (Lemma 6.0).

This construction uses only Rokhlin disintegration. It does **not** use absolute continuity of the unstable lamination.

**Spectral form.** In L^2(omega) terms, the forward Laplace transform of S is <(z - X)^{-1} phi, w-bar>. The family T_z is then the jump across iR of the Cauchy transform of the spectral measure sigma_{phi, w-bar}, and the backward half continues across iR.

**Why it stops.** GH makes the density of sigma_{phi, w-bar} flat at 0, tamely in phi (R7-b Prop. 3.1, R8-e Prop. 3.1). Varying w over all such balanced functions shows exactly this: smooth phi lie exponentially close, in L^1 on Pesin sets, to functions measurable for the fine partitions g_{-n} xi. That is the "fine-tail" property of R8-e §4. R8-e Lemma 4.1 shows that fine-tail control together with infinite divisibility does not contradict a nonzero spectral density. So no contradiction arises without coarse-scale (mixing-rate) information, and GH supplies none.

### 2.3 Where every route stops (summary)
At a point c with Re c != 0, a chain reads X b = -c b, X alpha = -c alpha - b. These right-hand sides are not smooth, so GH cannot be applied. Every transformation that preserves GH leaves the real part of the spectral parameter at 0 fixed:
- conjugation by e^a;
- time change (§2.1);
- X -> -X, which only reflects;
- multiplication by smooth eigenfunctions, which only shifts vertically (R9-h B3).

Positivity and the Leibniz identities carry no information (R9-g). So a proof of (JC) needs a genuinely new mechanism, transferring GH at 0 to some c with Re c != 0. Remark 3.3 of R8-b and (D7) of R9-g indicate that the direct mechanism (hypoellipticity of P - c) is circular.

## 3. Final status

**Proved / checked in this round.**
1. Theorem A (step 3 of the chain) is correct (Section 1). It applies to the families of Theorem R' with k = 1, and the moments it produces are (C^1)'-functionals of exactly the kind (JC) quantifies over.
2. Consequently the chain is sound: steps 1, 2 and 3 together with (JC) imply h_top(g_1) = 0. By Corollary 7.2 of R9-b (re-checked; it uses no GH), (JC) on the strips of Theorem R' is also *necessary* for the chain's conclusion. Whenever a positive-entropy g_1-ergodic measure exists, every point of its strip carries an order-1 Jordan chain.
3. The time-change computation of §2.1 (a dead end, proved).

**Not proved (open).**
- (JC): under GH, every open vertical strip contains a point c that carries no order-1 Jordan chain of P^T. This is open; as before, only strips containing 0 are settled (c = 0, by (K0) and (K1)).
- (NJ): no order-1 Jordan chain at any c with Re c != 0. Open. Its order-0 part is settled only under (V) (R9-c Cor. 1.2(iii), R9-b Cor. 7.4).
- (SO): under GH, ∫_R e^{J_t(x) - kappa t} dt = infinity for all x and all real kappa != 0. Open. It would settle order-0 chains (R9-c).
- (J1-0), (V), (J2)/(SS_Y): open, as recorded in R9-b §5 and R9-d.
- Hence the problem itself (zero topological entropy of a GH flow) is proved here only where earlier rounds proved it: dim M <= 3 (R6-a Theorem 5.2), and for hyperbolic measures in every dimension (R6-a Theorem 5.1, modulo the cited Katok / Lian-Young theorem). **The general case remains open in this attempt.**

=== END OF ANSWER round10_q1 ===

