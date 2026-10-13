# round10_q7: answer

## Plan / statement being attempted
Target: (JC) / (NJ) by order reduction through the 1-jet bundle (task steps (1)-(3)).
Outcome, in summary (details and proofs below):
- **Step (1) is false as a general statement.** I prove this rigorously (Theorem 1). For volume-preserving Anosov flows, e.g. the geodesic flow of a closed hyperbolic surface, order-1 eigen-densities and order-1 Jordan chains exist at every c with 0 < Re c < theta. But NO nonzero E*-valued measure beta satisfies beta o Gamma-hat_t = e^{ct} beta when 0 < |Re c| < theta. So no order-1 chain there has an equivariant measure representation. Corollary 1.2: every Hahn-Banach extension has an unbounded renormalised orbit in both time directions, so Banach-limit averaging and fixed-point constructions cannot work. Any equivariant representation would therefore have to be produced by GH itself.
- **Step (2) only partly holds.** I prove the lifted dissipativity lemma (Proposition 2) in the "collinear" case, and I show exactly what is left in the non-collinear case: an invariant measurable 2-plane field carrying a Jordan block, which forces nothing.
- **Step (3) contains an open order-0 question.** Proposition 3 shows that the order-0 part of (JC) already needs a tilted form of Lemma C, (SO'): no non-periodic orbit with int (1+|t|) e^{J_t - kappa t} dt < inf. Such an orbit produces an order-0 chain at every c with Re c = kappa, with no hypothesis on X. (SO') is open, so the order-reduction route cannot be closed without a new use of GH at a real point kappa != 0.
- (JC) itself remains **open**. I also checked step 3 of the chain (Theorem A) and found no flaw.

Notation as in the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P = X + d, Gamma_t phi = e^{J_t} phi o g_t. A chain at c is a pair (A, B) in (C^1)' with B != 0, B o (P - c) = 0 and A o (P - c) = B. By Lemma 1.1 of R8-b these give B o Gamma_t = e^{ct} B and A o Gamma_t = e^{ct}(A + tB).

---

## 0. The jet set-up (definitions; elementary)

E := (M x C) + T*M_C is the complexified 1-jet bundle, and j : C^1(M) -> C^0(M; E), j phi = (phi, d phi), is an isometric embedding (for the obvious norms) onto a closed subspace V. The transport lifts:

 Gamma-hat_t (f, eta)(x) = M_t(x) (f, eta)(g_t x),  M_t(x)(f, eta) := e^{J_t(x)} ( f, eta o Dg_t(x) + f dJ_t(x) ),

with M_t(x) : E_{g_t x} -> E_x linear. This gives j o Gamma_t = Gamma-hat_t o j, and Gamma-hat_{t+s} = Gamma-hat_s o Gamma-hat_t (cocycle rule).

The dual is C^0(E)' = M(E*), the E*-valued complex Borel measures. For beta = w |beta| (w a unit Borel section of E*, for a fixed continuous Hermitian metric), the transported measure beta o Gamma-hat_t is the push-forward of (N_t w)|beta| under g_t. Here N_t(x) := M_t(x)^T : E*_x -> E*_{g_t x}, and on an element (mu, v) of E*_x = C + T_xM_C,

 N_t(x)(mu, v) = e^{J_t(x)} ( mu + dJ_t(x)(v), Dg_t(x) v ).   (0.1)

(Check: <(mu, v), M_t(f, eta)> = e^{J_t}[mu f + eta(Dg_t v) + f dJ_t(v)].)

An order-1 functional B corresponds to B-hat := B o j^{-1} on V, and B-hat o Gamma-hat_t = e^{ct} B-hat on V. Step (1) asks for beta in M(E*) with beta|_V = B-hat and beta o Gamma-hat_t = e^{ct} beta on all of C^0(E).

---

## 1. Step (1) fails in general (PROVED; no GH)

**Theorem 1 (no equivariant jet-measure off the imaginary axis).** Let X generate an Anosov flow preserving a smooth positive density omega. Take nu = omega, so d = 0 and J = 0. Let TM = E^s + E^c + E^u be the continuous invariant splitting with E^c = RX, and C, theta > 0 constants with |Dg_t v| <= C e^{-theta t}|v| (v in E^s, t >= 0) and |Dg_{-t} v| <= C e^{-theta t}|v| (v in E^u, t >= 0). Then for every c in C with 0 < |Re c| < theta, every beta in M(E*) with beta o Gamma-hat_t = e^{ct} beta for all t is zero.

*Proof.* With J = 0, (0.1) reads N_t(mu, v) = (mu, Dg_t v), so the two components decouple. Write beta = (beta_0, m), with beta_0 a complex measure and m = v|m| a TM_C-valued measure (|v| = 1).

1. *Scalar part.* Test on sections (f, 0). Since Gamma-hat_t(f, 0) = (f o g_t, 0), we get (g_t)_* beta_0 = e^{ct} beta_0. The total variation of a push-forward under a Borel bijection is the push-forward of the total variation, so ||beta_0|| = e^{(Re c)t} ||beta_0|| for all t. Since Re c != 0, beta_0 = 0.
2. *Splitting the vector part.* The projections pi^s, pi^c, pi^u are continuous and commute with Dg_t. Testing on (0, eta o pi^u), with eta continuous, gives
   int eta(g_t x)(Dg_t(x) pi^u v(x)) d|m|(x) = e^{ct} int eta(pi^u v) d|m|.
   So m^u := (pi^u v)|m| satisfies (Dg_t)_# m^u = e^{ct} m^u, where (Dg_t)_# denotes the push-forward of (Dg_t v^u)|m| under g_t. The same holds for m^s and m^c.
3. *Unstable part.* For w in E^u_C and t >= 0 we have |Dg_t w| >= C^{-1} e^{theta t}|w|. This follows from the real bound applied to the real and imaginary parts, since the metric is Hermitian. Total variations of push-forwards under bijections are push-forwards of total variations, so
   e^{(Re c)t} ||m^u|| = ||(Dg_t)_# m^u|| = int |Dg_t pi^u v| d|m| >= C^{-1} e^{theta t} ||m^u||.
   Let t -> +inf. Since Re c < theta, m^u = 0.
4. *Stable part.* For w in E^s_C and t <= 0 we have |Dg_t w| >= C^{-1} e^{theta|t|}|w|. The same computation gives e^{-(Re c)|t|} ||m^s|| >= C^{-1} e^{theta|t|} ||m^s||. Let t -> -inf. Since Re c > -theta, m^s = 0.
5. *Flow part.* pi^c v |m| = X kappa for a complex measure kappa, and Dg_t X(x) = X(g_t x). So (g_t)_* kappa = e^{ct} kappa when tested on the functions eta(X), and these are all continuous functions because X has no zeros. As in step 1, kappa = 0.

Hence beta = 0. ∎

**Proposition 1.1 (the chains exist there).** In the setting of Theorem 1, every c with 0 < Re c < theta, outside a discrete set, carries a nonzero order-1 eigen-density B together with an order-1 Jordan chain (A, B). (By Cor. 7.2 of R9-b and Theorem R', chains exist at every point of the Theorem R strip.)

*Proof.* Take x != y on one strong unstable leaf. Then d(g_t x, g_t y) <= C' e^{-theta|t|} for t <= 0, by integrating the backward contraction along a leaf curve. Put T_z(phi) := int_R e^{-zt}(phi(g_t x) - phi(g_t y)) dt for 0 < Re z < theta.
- *Convergence.* The integrand is bounded by 2||phi||_inf e^{-(Re z)t} for t >= 0 and by C'||phi||_{C^1} e^{-(theta - Re z)|t|} for t <= 0.
- *Eigen-relation.* Integrating by parts, with boundary terms tending to 0, gives T_z o X = z T_z.
- *Non-vanishing.* z -> T_z(phi_0) is not identically zero, by Fourier uniqueness as in R5-a step (f). So T_z != 0 off a discrete set.
- *Chain.* A := dT_z/dz, which is -int t e^{-zt}(...) dt, satisfies A o X = zA + T_z.
All of these are bounded by C(z)||phi||_{C^1}. ∎

Hence: **the order-1 chains of this (positive-entropy, non-GH) flow at 0 < Re c < theta have no equivariant E*-measure representation.** For the geodesic flow of a hyperbolic surface, theta = 1. The strip that Theorem R' produces from Liouville measure is (delta, theta' - delta) with theta' < chi = 1, which lies inside this range. So the failure occurs for exactly the families the chain produces. Step (1) cannot be a general representation theorem: any construction of beta must use GH, and must fail for Anosov flows.

**Corollary 1.2 (averaging cannot work).** In the setting of Theorem 1 and Proposition 1.1, let beta_0 in M(E*) be any extension of B-hat (Hahn-Banach). Then
 sup_{t >= 0} e^{-(Re c)t} ||beta_0 o Gamma-hat_t|| = inf  and  sup_{t <= 0} e^{-(Re c)t} ||beta_0 o Gamma-hat_t|| = inf.

*Proof.*
1. Put Phi_t(beta) := e^{-ct} beta o Gamma-hat_t. This is a commuting family of weak*-continuous linear maps with Phi_{t+s} = Phi_t Phi_s. It preserves the weak*-closed affine set of extensions of B-hat, because Gamma-hat_t preserves V and B-hat o Gamma-hat_t = e^{ct} B-hat.
2. If {Phi_t beta_0 : t >= 0} were bounded, its weak*-closed convex hull K would be weak*-compact, convex, Phi_s-invariant for s >= 0, and would consist of extensions.
3. Markov-Kakutani would then give beta in K with Phi_s beta = beta for all s >= 0. Hence also for s <= 0, since Phi_{-s} = Phi_s^{-1}. This beta is a nonzero equivariant extension (nonzero because B != 0), contradicting Theorem 1.
4. The case t <= 0 is the same with Phi_{-t}. ∎

**Remark 1.3.**
- The "quotient construction" suggested in the task is vacuous: C^0(E)'/V-perp = V' = (C^1)', so factoring out the annihilator returns the original problem.
- In the Anosov example the defect e^{-ct} beta_0 o Gamma-hat_t - beta_0 lies in V-perp (pairs (mu_0, m) with mu_0(f) = -m(df)), as R9-g (D5) feared. Corollary 1.2 shows the defect is unbounded.
- Intuition: B = T_z is "order 0 forward" (two orbit measures) and "order 1 backward" (a current along the contracting unstable curve). These are two different jet representations of delta_x - delta_y, glued at t = 0.

---

## 2. Step (2): lifted dissipativity, collinear case (PROVED; no GH), and the gap

**Proposition 2.** Let c in C, and let beta != 0, alpha in M(E*) satisfy beta o Gamma-hat_t = e^{ct} beta and alpha o Gamma-hat_t = e^{ct}(alpha + t beta) for all t. Write beta = w|beta|, and put a_t(x) := log|N_t(x) w(x)| (jointly Borel). Then:
(a) (g_t)_*(e^{a_t}|beta|) = e^{(Re c)t}|beta|, and N_t(x)w(x)/|N_t(x)w(x)| = e^{i(Im c)t} w(g_t x) for |beta|-a.e. x, for each t.
(b) Write the Lebesgue decomposition alpha = zeta|beta| + alpha_s, with zeta a Borel section of E* and alpha_s singular to |beta|. Then for each t and |beta|-a.e. x,
   N_t(x)zeta(x) = e^{ct} rho_t(x) (zeta(g_t x) + t w(g_t x)),  where N_t(x)w(x) = e^{ct} rho_t(x) w(g_t x), rho_t > 0.
(c) (Collinear case.) If zeta = k w |beta|-a.e. for a scalar Borel function k, then for |beta|-a.e. x:
   int_R e^{a_t(x) - (Re c)t} dt < inf.

*Proof.*
(a) beta o Gamma-hat_t is the push-forward of (N_t w)|beta| under the bijection g_t. Its total variation is therefore (g_t)_*(|N_t w| |beta|), and it equals |e^{ct} beta| = e^{(Re c)t}|beta|. Since |N_t w| is bounded above and below for fixed t, (g_t)_*|beta| is equivalent to |beta|. Uniqueness of the polar decomposition of the same vector measure gives the direction identity.
(b) Write D_t := d(g_t)_*|beta| / d|beta|. Equivariance of beta gives (N_t w) o g_{-t} D_t = e^{ct} w. The push-forward of alpha_s stays singular to |beta|, since |beta| is quasi-invariant. So uniqueness of the Lebesgue decomposition in alpha o Gamma-hat_t = e^{ct}(alpha + t beta) gives (N_t zeta) o g_{-t} D_t = e^{ct}(zeta + t w). Evaluating at g_t x (g_t preserves |beta|-null sets) gives the claim with rho_t(x) = 1/D_t(g_t x).
(c) Substituting zeta = k w into (b) gives k(g_t x) = k(x) - t a.e., for each t. With r = Re k and E_n = {r in [n, n+1)}, the conformality (a) gives
   int e^{a_t} 1_{E_n} d|beta| = e^{(Re c)t} |beta|(r in [n - t, n + 1 - t)).
   By Tonelli, int_{E_n} int_R e^{a_t - (Re c)t} dt d|beta| = |beta|(M) < inf. This is the computation of Lemma 1.1(e) of R9-c, with J_t replaced by a_t. ∎

For E*-valued measures with nonzero vector part v, (0.1) gives a_t = J_t + log|Dg_t v| + O(log(1 + |t|)). So (c) is "dissipativity along the lifted orbit (x, v)", which is the planner's step (2).

**The gap (non-collinear case).** If zeta(x) is not in C w(x) on a set of positive |beta|-measure, then (b) only says the following. span(w, zeta) is an N-invariant measurable 2-plane field, and in the frame (w, zeta) the cocycle is e^{ct} rho_t [[1, t], [0, 1]]. No function k with k o g_t = k - t is produced. Unipotent derivative cocycles occur on conservative systems (e.g. Heisenberg nilflows, where Dg_t Y = Y - tZ), so no dissipativity follows. The order-0 proof used rank E* = 1 in an essential way. The quotient direction zeta-bar in E*/C w is again an eigen-object, with the same eigenvalue and base measure. Combined with Theorem 1, steps (1)-(2) are therefore not available in general.

---

## 3. Step (3) contains an open order-0 statement (PROVED reduction; no GH)

**Proposition 3.** Let x be neither a zero nor a periodic point, and kappa real with int_R (1 + |t|) e^{J_t(x) - kappa t} dt < inf. Then every c with Re c = kappa carries an order-0 (hence order-1) Jordan chain:
 B(phi) := int_R e^{J_t(x) - ct} phi(g_t x) dt,  A(phi) := -int_R t e^{J_t(x) - ct} phi(g_t x) dt.

*Proof.*
1. *Decay of the weights.* q(t) := e^{J_t(x) - kappa t} satisfies |q'| <= K q with K = ||d||_inf + |kappa|. Hence q(t) >= q(s) e^{-K|t-s|}, and integrability of q and of |t| q forces q(t) -> 0 and t q(t) -> 0 as |t| -> inf (as in Lemma C).
2. *The relations.* From d/dt[e^{J_t - ct} phi(g_t x)] = e^{J_t - ct}((P - c)phi)(g_t x) and the analogous formula for t e^{J_t - ct} phi(g_t x), integration over R gives B o (P - c) = 0 and A o (P - c) = B.
3. *B != 0.* t -> g_t x is an injective Borel map, so ||B|| = int q dt > 0 (total variation of a push-forward under an injective Borel map, by Lusin-Souslin). ∎

With Lemma 1.1 of R9-c, the order-0 part of (JC) on a strip (a, b) is therefore pinned between two orbit statements:
- it holds if, for some kappa in (a, b), int_R e^{J_t(x) - kappa t} dt = inf for every x (the planner's (SO) at kappa);
- it fails if, for every kappa in (a, b), some non-periodic orbit has int (1 + |t|) e^{J_t - kappa t} dt < inf.

So any proof of (JC), by order reduction or otherwise, contains a proof of a tilted Lemma C at some real kappa != 0 in each relevant strip. Lemma C's proof does not tilt: it uses (F1) at eigenvalue 0, while the tilted orbit measure is an eigen-measure at kappa (R9-g Remark 4). I could not prove (SO) or (SO'). The orbits it must exclude are those with 0 < r_+ < r_- (forward volume-growth rate below the backward rate). Lemma K / Corollary 4.1 of R6-a exclude them only along strong manifolds of hyperbolic periodic orbits.

---

## 4. Check of the chain (step 3 = Theorem A)

I re-read the proof of Theorem A (R9-b §7) line by line and found no flaw:
- The Gaussian contour average S_omega is legitimate under (ii), which is uniform in Im z.
- S_omega(Gamma_t phi) = (1/2 pi i) int rho_omega e^{zt} T_z(phi) dz follows from T_z o P = z T_z by the ODE argument.
- The renormalised transport H_phi(t) = e^{-ct} S(Gamma_t phi) decays two-sidedly at rate rho.
- The moments are order-k densities satisfying m_0 o (P - c) = 0 and m_j o (P - c) = -j m_{j-1}.
- A nonzero m_j would give a Jordan chain (-m_{j+1}/(j+1), m_j) at c of order k (k = 1 for the Theorem R' families).
- Fourier uniqueness then closes the argument.
Steps 1-2 and 4 of the chain I did not re-check beyond reading.

## 5. Final status
**Proved here:**
- Theorem 1: no equivariant jet-measure off iR for volume-preserving Anosov flows, 0 < |Re c| < theta.
- Proposition 1.1: chains exist there, so step (1) is false in general.
- Corollary 1.2: every extension has an unbounded renormalised orbit, so averaging and fixed-point constructions fail.
- Proposition 2: lifted dissipativity in the collinear case, with an explicit description of the non-collinear gap.
- Proposition 3: order-0 chains come from any non-periodic orbit with int (1+|t|)e^{J_t - kappa t} dt < inf, so (JC) contains a tilted Lemma C.
- A check of Theorem A.

**Open:**
1. (JC) / (NJ), and hence the problem in dimension >= 4 along this chain.
2. (SO) / (SO'): under GH, does int_R e^{J_t(x) - kappa t} dt = inf hold for all x and all real kappa != 0? This is the order-0 core that any route to (JC) must settle.
3. Whether GH, though not soft functional analysis, could force an equivariant representation (Theorem 1 shows this would be a genuinely GH-dependent statement).
4. The non-collinear case of step (2).

=== END OF ANSWER round10_q7 ===
