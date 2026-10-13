# round8_q3: answer (partial result; PE-NH not settled)

## 0. Plan and status
Target: (PE-NH). I did not find a proof or a counterexample. Below are:
- **Theorem R** (proved, modulo the standard Pesin/Ledrappier-Young citations already used in R6-a). It is a new reduction that covers every positive-entropy ergodic measure at once: hyperbolic or not, any value of mu(d). It needs no Katok/Lian-Young horseshoes. It reduces the whole problem to one spectral statement (E1-int) about real eigenvalues of the transpose of P = X + d on distributions of order <= 1. That statement is strictly weaker than the old (E1).
- **Lemma Q** (proved, volume case): the tame dual inverse gives order-shifting smallness of real eigen-distributions. I also show exactly why this does not close the argument.
- Checks of the chain, and the open questions.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t = log nu-Jacobian, P phi = X phi + d phi, and F_phi(t) = S(e^{J_t} phi o g_t). Distribution densities may be complex.

## 1. Theorem R (reduction of the problem to "no interval of real eigenvalues")

**Definition.** Sigma := { kappa in R : there is a nonzero distribution density T of order <= 1 (T in (C^1)', complex-valued allowed) with T(P phi) = kappa T(phi) for all smooth phi }.

Equivalently, kappa is in Sigma iff some nonzero u in D' of order <= 1 has Xu = -kappa u (Observation 0).

Remarks:
- 0 is always in Sigma (T = nu).
- Every ergodic mu contributes mu(d) to Sigma (Prop. 2.2 of R4-q7).
- For a Diophantine linear flow on T^n (nu = Lebesgue, so P = X) we have Sigma = {0}. Indeed, testing on e_k gives (i k.alpha - kappa) T(e_k) = 0.

**Theorem R.** Let X be any smooth vector field on a compact manifold; GH is not used. Let mu be an ergodic flow-invariant probability with h_mu(g_1) > 0. Then Sigma contains a nonempty open interval.

**Corollary R1.** Suppose (E1-int) holds: under GH, Sigma has empty interior. Then every GH vector field has a flow of zero topological entropy.
*Proof.* Theorem R gives h_mu(g_1) = 0 for every ergodic flow-invariant mu. Then apply step 4 of the chain (variational principle plus flow-ergodic decomposition). ∎

*Proof of Theorem R.*
1. *Exponents.* h_mu(g_{-1}) = h_mu(g_1) > 0. Ruelle's inequality for g_1 and for g_{-1} gives that mu has a positive exponent and a negative exponent. Let chi := chi^+_min > 0 be the smallest positive exponent and lambda := mu(d). Fix theta with 0 < theta < chi and delta with 0 < delta < theta/4.
2. *A generic pair on one unstable leaf.* Let G be the set of z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf. By Birkhoff, mu(G) = 1. We use [P], [LY] and Lemma 6.0 of R6-a for the C^inf diffeomorphism g_1. These say that, for mu-a.e. x, the unstable conditional mu^xi_x is non-atomic and carried by G. So we may pick x in G and y in G ∩ xi(x) with y != x.
   By [P], d(g_{-m}x, g_{-m}y) <= C e^{-(chi - delta')m} for integers m >= 0. Interpolating with the Lipschitz constants of g_{-s}, s in [0,1], gives d(g_t x, g_t y) <= C_0 e^{-theta|t|} for all t <= 0 (choose delta' with chi - delta' > theta).
3. *Constants.* For t <= 0, J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds, and the integrand is O(e^{-theta|s|}). So b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists and |J_t(x) - J_t(y) - b| <= K e^{-theta|t|}. Since x, y are in G, there is C_1 with
   J_t(x), J_t(y) <= C_1 + (lambda + delta) t for t >= 0, and J_t(x) <= C_1 + (-lambda + delta)|t| for t <= 0.
4. *Bounds.* Put S := delta_x - e^b delta_y, so that F_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y).
   - For t >= 0: |F_phi(t)| <= (1 + e^b) e^{C_1} e^{(lambda+delta)t} ||phi||_inf.
   - For t <= 0: |F_phi(t)| <= e^{J_t(x)} ( |phi(g_t x) - phi(g_t y)| + |1 - e^{b + J_t(y) - J_t(x)}| ||phi||_inf ) <= C_2 e^{-(theta + lambda - delta)|t|} ||phi||_{C^1}.
   This uses |1 - e^{-r}| <= |r| e^{|r|} and |r| <= K e^{-theta|t|}.
5. *Laplace family.* Let Omega := { z : lambda + delta < Re z < lambda + theta - delta }, which is nonempty since theta > 2 delta. For z in Omega put T_z(phi) := int_R e^{-zt} F_phi(t) dt.
   - The integral converges absolutely and locally uniformly in z: the exponents are -(Re z - lambda - delta)t for t >= 0 and (Re z - theta - lambda + delta)|t| for t <= 0, and both are negative.
   - So T_z is a distribution density of order <= 1, with |T_z(phi)| <= C(z) ||phi||_{C^1} and C(z) locally bounded. For each phi, z -> T_z(phi) is holomorphic on Omega.
6. *Eigen-relation.* t -> e^{J_t} phi o g_t is C^1 into C^inf with derivative e^{J_t} (P phi) o g_t (Theorem J, step 1). So F_phi' = F_{P phi}. Integrate by parts on [-R, R]:
   int e^{-zt} F_{P phi} dt = [e^{-zt} F_phi]_{-R}^{R} + z int e^{-zt} F_phi dt.
   By the bounds of step 4 for phi and for P phi, the boundary terms tend to 0 and the integrals converge. So T_z(P phi) = z T_z(phi).
7. *Non-vanishing.* Choose smooth phi_0 with phi_0(x) = 1 and phi_0(y) = 0. Then F_{phi_0}(0) = 1. Fix a real kappa_0 in Omega. Then G(t) := e^{-kappa_0 t} F_{phi_0}(t) is continuous, lies in L^1, and has G(0) = 1. Its Fourier transform is omega -> T_{kappa_0 + i omega}(phi_0). By Fourier uniqueness this transform is not identically 0, so the holomorphic function z -> T_z(phi_0) is not identically 0 on Omega. Hence its zero set D on the real segment I := Omega ∩ R is discrete and closed in I.
8. For kappa in I \ D, T_kappa is a nonzero distribution density of order <= 1 with T_kappa(P phi) = kappa T_kappa(phi), i.e. kappa is in Sigma. Finally, I \ D is a nonempty open set. ∎

**Remarks on Theorem R.**
1. Compared with Theorem J and Lemma M, the GH-part is now a single global spectral statement. The geometry of mu (zero exponents, the value of mu(d), dimension) has disappeared. The only dynamical input is one exponentially backward-asymptotic pair of forward-generic points, which positive entropy provides.
2. (E1-int) is weaker than (E1) of R4-q10. (E1) excludes every real nonzero eigenvalue; (E1-int) excludes only intervals. (E1) is in fact false in general unless GH also forces mu(d) = 0 for all mu, because mu(d) is in Sigma. (E1-int) is compatible with countably many real eigenvalues, so it does not conflict with possible zeros (d(p) is in Sigma) or with measures having mu(d) != 0.
3. With the same proof one can restrict Sigma to eigen-distributions whose Laplace-in-kappa family is holomorphic. So it suffices to exclude *holomorphic* families kappa -> T_kappa of nonzero order-1 eigen-distributions on a real interval. This is the precise form of the planner's (J1). Lemma M excludes such families exactly when the interval reaches 0 from both sides (or meromorphically).
4. Sanity check (north-south flow on S^2, not GH; heuristic, not used). For a single source-to-sink orbit, the weighted Laplace transform int e^{-zt} e^{J_t(y)} phi(g_t y) dt converges on the strip d(S) < Re z < d(N) (sink S with d(S) < 0, source N with d(N) > 0). By the same argument as steps 5-8, Sigma then contains an interval minus a discrete set. So intervals in Sigma do occur for non-GH fields, consistent with Theorem R not using GH.

## 2. Lemma Q (volume case: what the closed-range half of GH gives for eigen-distributions)
Assume GH and that X preserves a smooth positive density omega. Take nu = omega, so d = 0 and P = X.

**Lemma Q.** For every k there are m = m(k) and C_k such that every distribution density T in (C^k)' with T o X = kappa T, where kappa != 0 is complex, satisfies T(1) = 0 and
||T||_{(C^m)'} <= 2 C_k |kappa| ||T||_{(C^k)'}.
Iterating along k_0 = k, k_{j+1} = m(k_j) gives ||T||_{(C^{k_N})'} <= (prod_{j<N} 2C_{k_j}) |kappa|^N ||T||_{(C^k)'}.

*Proof.*
1. kappa T(1) = T(X1) = 0, so T(1) = 0.
2. By Lemma B(iii) of R7-d (tame dual solvability) there is S in (C^m)' with S o X = T and ||S|| <= C_k ||T||.
3. Then (S - T/kappa) o X = 0, so S - T/kappa is an invariant distribution density. By (O2) it equals c omega.
4. Evaluating at 1 gives S(1) = c omega(M), so |c| omega(M) <= ||S||_{(C^m)'}. Also ||omega||_{(C^m)'} <= omega(M).
5. Hence ||T/kappa||_{(C^m)'} <= ||S|| + |c| omega(M) <= 2||S||. ∎

**Why it stops.** Apply Lemma Q to the family T_z of Theorem R with lambda = 0, whose (C^1)'-norm is O(1/Re z) near the left edge. It gives |T_z(phi)| <= A_N(phi) |z|^N / Re z with A_N(phi) = (prod_{j<N} 2C_{k_j}) C ||phi||_{C^{k_N}}. This is Theorem V/Lemma H of R7-e in dual form: a contradiction needs the Carleman condition sum A_N^{-1/N} = inf for a C^1-dense set of phi.
- GH (closed graph theorem) gives no control on the growth of C_k or of the losses m(k) - k.
- Even with a fixed loss sigma and constants C_k <= B^k, the product is about B^{sigma N^2/2}, which is super-geometric. So no choice of phi (not even Laplace eigenfunctions, which have ||phi||_{C^j} of geometric growth) satisfies Carleman.

So the closed-range half of GH, used through tame constants alone, cannot give (E1-int) unless one has a uniform-loss, geometric-constant tame estimate. I could not derive such an estimate from GH; for Diophantine flows it holds (Fourier multiplier |k.alpha|^{-1} <= C|k|^tau, uniform in s).

## 3. Checks of the chain
- Step 2 (entry 60) and step 4 (variational principle, Jacobs): I re-checked the arguments quoted in R6-a section 5 and see no flaw.
- Theorem R gives an alternative route that bypasses step 2 and [KLY] entirely, conditional on (E1-int).
- Dimension 1: trivial. Dimension <= 3: Theorem 5.2 of R6-a, unconditional modulo citations.

## 4. What is proved, what is open
Proved here:
- Theorem R. Every positive-entropy ergodic measure of any smooth flow produces a nonempty open interval of real kappa carrying nonzero order-1 eigen-distributions T o P = kappa T, given by a holomorphic Laplace family.
- Corollary R1. (E1-int) implies the problem.
- Lemma Q (volume case) and the precise reason it does not suffice.

Open:
- **(E1-int)**: under GH, does Sigma have empty interior? Equivalently (Remark 3), is there no holomorphic family of nonzero order-1 eigen-distributions over a real interval?
- (PE-NH) itself, and hence the problem in dimension >= 4. In particular the volume-preserving core case (non-hyperbolic omega with h_omega > 0) remains open.
- Sub-question isolated in Section 2: does GH imply a tame estimate for X^{-1} with uniformly bounded derivative loss and geometrically growing constants? That would give (E1-int) in the volume case, via Lemma Q and Lemma H.

No counterexample was found. The natural candidates (skew products with zero-exponent centre directions over hyperbolic flows) fail GH through extra invariant measures and distributions (O2, Corollary G2).

=== END OF ANSWER round8_q3 ===
