# round13_q4: answer

## Summary of outcome
- **(PE0) is NOT proved here.** Step (i) of the route is checked and correct.
- **New, fully proved (GH only, no volume, no Pesin theory): Theorem L.** For every finite linear combination of weighted exponentially asymptotic legs whose total boundary measure is zero, the boundary of the backward-asymptotic legs is zero by itself. Equivalently, under GH every exact su-loop (closing with tau = 0) with trivial Jacobian holonomy is "degenerate". In the language of the route: when tau = 0 one gets c = 0 automatically, and then the whole configuration vanishes. No integrality and no volume are needed. The holonomy condition can also be dropped once there are two loops at one base point.
- **Dead end, with reason:** the same argument cannot handle closures up to a nonzero flow shift tau. The transported seg term has a Laplace transform that diverges on both sides, a Patterson-type divergence. In the flow-box form of step (iii), size counting is exactly scale-critical: it gives O(r^{n-delta/theta}), or O(r^n) when the weights are bounded, against c·nu(B_r) ~ r^n. So step (iii) for c != 0 cannot follow from size estimates alone.
- **Reduction (proved):** (PE0) follows from the existence statement (LOOP) of §5. Every such mu would have to carry a nondegenerate exact su-loop, or two loops at one base point, or two chains closing with the same shift tau. (LOOP) is open. Its difficulty is precisely the extra zero exponent: generically, brackets do not close in the centre direction.

Conventions are those of the task: nu, d = div_nu X, J_t, P = X + d, Gamma_t phi := e^{J_t} (phi o g_t). We have d/dt Gamma_t phi = Gamma_t P phi = P Gamma_t phi, and int Gamma_t phi dnu = int phi dnu because e^{J_t} is the nu-Jacobian of g_t. (F1) and (F2) of Block R6-a are used:
- (F1) T∘P = 0 implies T = c nu.
- (F2) T∘P = c nu implies c = 0.

## 1. Step (i) of the route is correct (checked)

A *leg* is an ordered pair (a, b) with a != b, of one of two types:
- type u: d(g_t a, g_t b) <= C e^{-theta|t|} for t <= 0;
- type s: the same bound for t >= 0.

It carries weights (alpha, alpha e^{beta(a,b)}). Here beta(a,b) = int_{-inf}^0 (d(g_r b) - d(g_r a)) dr for type u, and beta(a,b) = -int_0^inf (d(g_r b) - d(g_r a)) dr for type s. The integrals converge because d is Lipschitz.

**Why the weights match.** For type u and t <= 0, J_t(b) - J_t(a) = -int_t^0 (d(g_r b) - d(g_r a)) dr. This tends to -beta, with error at most (Lip(d) C/theta) e^{-theta|t|}. For type s and t >= 0, J_t(b) - J_t(a) = int_0^t (...) dr, which also tends to -beta. So beta + J_t(b) - J_t(a) -> 0 exponentially in the asymptotic direction.

**Bound on the transported dipole.** Put
Delta(t)(phi) := alpha e^{J_t(a)} phi(g_t a) - alpha e^{beta} e^{J_t(b)} phi(g_t b).

Write it as
alpha e^{J_t(a)}[phi(g_t a) - phi(g_t b)] + alpha e^{J_t(a)}[1 - e^{beta + J_t(b) - J_t(a)}] phi(g_t b).

This gives, in the asymptotic direction,
|Delta(t)(phi)| <= C' e^{J_t(a)} e^{-theta|t|} ||phi||_{C^1}.  (1.1)

So, under the *growth hypothesis*
(G) J_t(a) <= delta|t| + C_delta in the asymptotic direction, with delta < theta,
we get |Delta(t)(phi)| <= C'' e^{-theta'|t|} ||phi||_{C^1}, where theta' = theta - delta > 0.

(G) holds when a is Birkhoff generic, in the relevant time direction, for a measure with mu(d) = 0. It also transfers from a to b, since J_t(a) - J_t(b) converges.

**Leg functional.** Define
- l(phi) := int_{-inf}^0 Delta(t)(phi) dt for type u;
- l(phi) := -int_0^inf Delta(t)(phi) dt for type s.

By (1.1), l is a distribution density of order <= 1. Since Delta(t)(Pphi) = d/dt Delta(t)(phi), and Delta vanishes at the asymptotic end, in both cases
l(P phi) = alpha phi(a) - alpha e^{beta} phi(b).  (1.2)

**The chain identity.** For the chain of the route, the weights w_{k+1} = w_k e^{beta(x_k, x_{k+1})} make the leg boundaries telescope:
(l^w)(P phi) = phi(x_0) - w_{2L} phi(x_{2L}).

Also seg^w(P phi) = e^{J_tau(x_0)} phi(g_tau x_0) - phi(x_0). So (l^w + seg^w)∘P = (e^{J_tau(x_0)} - w_{2L}) delta_{g_tau x_0}. This vanishes exactly under the holonomy condition, and then (F1) gives l^w + seg^w = c nu. Step (i) is correct.

**Value of c.** Pairing with 1 gives c nu(M) = (l^w + seg^w)(1). In the volume case (nu invariant, d = 0, all weights 1) every leg gives int (1 - 1) = 0, so **c = tau / nu(M)**. Hence c = 0 if and only if tau = 0 there.

**Transport rule (used below).** By the cocycle identity e^{J_s(x)} e^{J_t(g_s x)} = e^{J_{s+t}(x)}, we have Delta(s)(Gamma_t phi) = Delta(s+t)(phi). Hence
- l(Gamma_t phi) = int_{-inf}^t Delta(r)(phi) dr for type u;
- l(Gamma_t phi) = -int_t^inf Delta(r)(phi) dr for type s.  (1.3)

## 2. Theorem L (proved under GH)

**Theorem L.** Assume GH. Let (a_k, b_k, alpha_k), k = 1..K, be finitely many weighted legs. Each has its own type u or s, real coefficients alpha_k, and each satisfies (G). Write beta_k = beta(a_k, b_k). Suppose the total boundary measure vanishes:
m := sum_k alpha_k (delta_{a_k} - e^{beta_k} delta_{b_k}) = 0.

Then the u-part vanishes separately:
m_u := sum_{k of type u} alpha_k (delta_{a_k} - e^{beta_k} delta_{b_k}) = 0,
and hence so does the s-part m_s = m - m_u.

*Proof.*
1. Let D := sum_k l_k, with B the sum over the u-legs and F the sum over the s-legs. By (1.2), D∘P = m = 0, so D = c nu by (F1).
2. Put G_phi(t) := B(Gamma_t phi). By (1.3), G_phi is C^1 with G_phi' = G_{P phi}. It satisfies two bounds.
   - For t <= 0, (1.3) shows that G_phi(t) is a sum of tails int_{-inf}^t Delta_k. So |G_phi(t)| <= C e^{-theta'|t|} ||phi||_{C^1}.
   - For t >= 0, G_phi(t) = D(Gamma_t phi) - F(Gamma_t phi) = c int phi dnu - F(Gamma_t phi). Each term of F(Gamma_t phi) is a tail int_t^inf Delta_k. So |G_phi(t) - c nu(phi)| <= C e^{-theta' t} ||phi||_{C^1}.
3. For 0 < Re z < theta' put T_z(phi) := int_R e^{-zt} G_phi(t) dt. The integral converges absolutely.
   - Integrating G_phi' = G_{P phi} by parts, the boundary terms vanish by the bounds in step 2. Hence T_z(P phi) = z T_z(phi).
   - Splitting at t = 0 gives
     T_z(phi) = H_1(z) + c nu(phi)/z - H_2(z),
     where H_1(z) = int_{-inf}^0 e^{-zt} G_phi dt is holomorphic on Re z < theta', and H_2(z) = int_0^inf e^{-zt} (c nu(phi) - G_phi) dt is holomorphic on Re z > -theta'.
   - Both are bounded by C ||phi||_{C^1} / (distance to the edge of their half-plane). So T_z extends meromorphically to |Re z| < theta' with at most a simple pole at 0. By the identity theorem the eigen-relation T_z∘P = z T_z holds on the punctured strip.
4. *Laurent expansion at 0.* Let A_n(phi) := (2 pi i)^{-1} oint_{|z| = r} T_z(phi) z^{-n-1} dz, with 0 < r < theta'.
   - Each A_n is a distribution density of order <= 1, with A_n = 0 for n < -1 and A_{-1} = c nu.
   - The eigen-relation gives A_n(P phi) = A_{n-1}(phi).
   - So A_0∘P = c nu, and (F2) gives c = 0. Inductively, if A_{n-1} = 0 then A_n∘P = 0, so A_n = c_n nu by (F1). Then A_{n+1}∘P = c_n nu, and (F2) gives c_n = 0.
   - Hence T_z(phi) = 0 near 0, and by the identity theorem on the whole punctured strip. (This is Lemma M of R6-b, re-proved here.)
5. *Fourier step.* Fix sigma in (0, theta'). The function t -> e^{-sigma t} G_phi(t) is continuous and in L^1, and its Fourier transform y -> T_{sigma + iy}(phi) vanishes identically. Hence G_phi = 0. In particular B(phi) = G_phi(0) = 0 for every phi.
6. By (1.2), m_u(phi) = B(P phi) = 0 for every smooth phi, so m_u = 0. Also c = 0 gives D = 0, so F = 0 and m_s = 0. ∎

GH is used only through (F1) and (F2).

**Corollary L1 (exact loops with trivial holonomy).** Assume GH. There is no closed chain with all of the following properties:
- x_0, x_1, ..., x_N = x_0, with N >= 2 even;
- the leg types alternate (u, s, u, s, ...);
- the points x_0, ..., x_{N-1} are pairwise distinct;
- each leg satisfies (G);
- the Jacobian holonomy is trivial: w_N := prod_k e^{beta(x_k, x_{k+1})} = 1.

*Proof.* Take alpha_k = w_k. Then m = delta_{x_0} - w_N delta_{x_0} = 0. Because the legs alternate, each x_k is an endpoint of exactly one u-leg, with coefficient ±w_k != 0. So m_u != 0, contradicting Theorem L. ∎

Remarks on Corollary L1:
- In route terms: when tau = 0 the constant c is forced to be 0 by the pole argument. The configuration then dies by Fourier uniqueness, with no volume and no integrality.
- In the volume case the holonomy is automatic (all weights 1). So under GH a volume-preserving field has no nondegenerate exact su-loop.

**Corollary L2 (holonomy can be dropped).** Assume GH. Let L_1 and L_2 be two alternating closed chains (loops) based at the same point x_0, satisfying (G), with holonomies h_1 and h_2. Choose (a, b) != (0, 0) with a(1 - h_1) + b(1 - h_2) = 0. Then a m_u(L_1) + b m_u(L_2) = 0.

In particular this is a contradiction as soon as some u-point of L_1 other than x_0 does not occur in L_2, or vice versa, and the corresponding coefficient a or b is nonzero. (If h_1 != 1 and h_2 != 1, both a and b are nonzero.)

*Proof.* Apply Theorem L to the combined family: the legs of L_1 with coefficients a w^{(1)}_k, and those of L_2 with coefficients b w^{(2)}_k. Its boundary is (a(1 - h_1) + b(1 - h_2)) delta_{x_0} = 0. ∎

**Corollary L3 (equal shifts).** Assume GH. Suppose two chains C_1, C_2 start at x_0 and both end at the same point y, with the same terminal weight. Then m_u(C_1) = m_u(C_2). This applies in particular to y = g_tau x_0 with the same tau.

*Proof.* C_1 followed by C_2 reversed is a loop at x_0 with holonomy 1. Its u-boundary is m_u(C_1) - m_u(C_2). If the two terminal weights differ, combine as in L2. ∎

So closures "up to a flow shift" are useful exactly when two different chains realise the same shift. The seg term then cancels and Theorem L applies.

**Sanity check (Theorem L is not vacuous).** Take the suspension of A × R_alpha on T^2 × T^1, with A a linear Anosov map and alpha irrational. It is volume preserving and not GH. It has exact quadrilaterals inside the T^2-slices, given by brackets of W^u_A and W^s_A. Each has tau = 0, holonomy 1, and distinct points. So Theorem L detects non-GH here: the configuration B is a nonzero invariant distribution. Diophantine linear flows, which are GH, have no asymptotic pairs at all.

## 3. Why tau != 0 is out of reach of this argument (dead end, with reason)

With a seg term, D = l^w + seg^w, and
seg(Gamma_t phi) = int_t^{t+tau} e^{J_r(x_0)} phi(g_r x_0) dr.
This does not decay in either time direction.

Put the seg into the F-side or the B-side. Either way, the Laplace transform of the transported configuration contains the factor
((e^{z tau} - 1)/z) · int e^{-zr} e^{J_r(x_0)} phi(g_r x_0) dr
over a half-line. Since J_r(x_0) = o(|r|), this one-sided Patterson integral converges only for Re z > 0 (or only for Re z < 0). It has no meromorphic continuation across 0 in general: by Lemma D its blow-up as z -> 0 is governed by equidistribution, not by a pole. So no strip around 0 exists, and step 4 of the proof of Theorem L cannot start. This is the precise reason why tau != 0 (equivalently c != 0 in the volume case) needed a separate idea (integrality, in R12-a).

**Size counting in a flow box is scale-critical.** Let phi be a bump of height 1 on B_r(p), with ||phi||_{C^1} ~ 1/r. A crossing of B_r(p) at leg-time t lasts about r. Its dipole contributes at most about e^{delta|t|} min(r, e^{-theta|t|}).

Average over p distributed by nu. Crossings with |t| <= T_r := theta^{-1} log(1/r) are avoided except on a set of p of nu-measure O(r^{n-1} log(1/r)). A curve of length dt meets B_r(p) with probability about r^{n-1} dt. This gives
E_p |D(phi_p)| <~ int_{T_r}^inf r^{n-1} e^{(delta - theta)t} dt ~ r^{n - delta/theta},
to be compared with |c| nu(B_r) ~ r^n.

So even with bounded weights (delta = 0) both sides are of order r^n. No contradiction can come from sizes alone. The structure must be used: integrality in the volume case, or exact closure as in Theorem L.

Also, in one transversal dimension, a sum of dipoles with summable moments and real weights can represent c times a smooth positive density. Write the sum as A + ∂G with A atomic and G in L^1. The equation cρ = A + ∂G is solvable with arbitrary small intervals, for example by dyadic refinement of Riemann sums. So the flow-box form by itself carries no obstruction, and any contradiction for c != 0 must use the dynamics.

## 4. Where this leaves (PE0): a proved reduction

**Proposition R.** Assume GH. (PE0) follows from the following statement.

**(LOOP)** For every g_1-ergodic mu with h_mu(g_1) > 0 and mu(d) = 0, at least one of the following exists. In each, the legs are exponentially asymptotic and the points satisfy the growth hypothesis (G) in the asymptotic directions of their legs, which holds for points Birkhoff generic for mu.
- (a) a nondegenerate exact loop with trivial holonomy;
- (b) two exact loops at a common base point whose u-points are not the same;
- (c) two chains from x_0 to a common endpoint (for example g_tau x_0 with the same tau) whose u-boundaries differ.

*Proof.* Each case contradicts Corollary L1, L2 or L3 respectively. ∎

**Why (LOOP) is hard (honest assessment).** Take x_0 generic. Lemma 6.0 lets one choose x_1 in W^u(x_0) and x_3 in W^s(x_0) generic in the needed directions. Growth control then transfers along legs, because J_t(a) - J_t(b) converges in the asymptotic direction. So genericity of the chain points is not the obstacle.

The obstacle is closure. A positive-entropy mu with mu(d) = 0 is non-hyperbolic: it has a zero exponent besides the flow direction (Theorem 5.1). Then dim W^u + dim W^s <= n - 2, so W^s_loc(x_1) ∩ W^u_loc(x_3) is generically empty. su-paths close only up to a displacement in the centre directions (flow plus zero exponent).

In uniformly partially hyperbolic models one gets (LOOP) in both cases:
- in the jointly integrable case (as in the A × R_alpha example), from exact brackets;
- in the accessible case, from accessibility.

For a general Pesin-theoretic mu no such dichotomy is available, since leaves are only measurable and local. Closing in the centre would also need uniform control at the non-generic closing point. I could not prove (LOOP). Approximate closure (Lemma T3) cannot replace exact closure: correcting the defect delta_{x_0} - w delta_{x_N} needs a Green distribution E with E∘P equal to that defect. Its transport E(Gamma_t phi) is not controlled, so the Laplace argument of Theorem L does not apply (compare Lemma O1-O3 of round12_q5).

## 5. Status

**Proved here:**
- step (i) of the route;
- c = tau/nu(M) in the volume case;
- Theorem L and Corollaries L1-L3 (GH only);
- Proposition R, the reduction of (PE0) to (LOOP);
- the dead-end analysis for tau != 0 (Laplace divergence) and for size counting (scale-criticality). Here the claim that no meromorphic continuation exists "in general" is a heuristic statement about the method, not a theorem.

**Not proved:** (PE0) itself, and hence the problem in dim M >= 4 (beyond what earlier rounds established).

**Open questions:**
1. (LOOP) for positive-entropy ergodic mu with mu(d) = 0 under GH, or any of its variants (a)-(c).
2. The case of closures with a single shift tau != 0 in the non-volume setting. Integrality (R12-a) is unavailable for real weights, and §3 shows that both the Laplace method and size counting fail there.
3. (Q-vol) of R12-a. In the volume case, Corollary L1 now kills every nondegenerate exact loop. So (Q-vol) reduces to producing either an exact loop or two closures with equal tau.

=== END OF ANSWER round13_q4 ===
