# round7_q9 — answer (partial result; (PE-NH) NOT proved, no counterexample found)

## 0. Plan and status
Target: (PE-NH). Under GH, no ergodic flow-invariant mu has h_mu(g_1) > 0 together with a zero exponent of multiplicity >= 2.
Plan: (1) re-check the chain; (2) prove a general "configuration lemma" that extends the pair/homoclinic mechanism
of Theorem J to arbitrary finite configurations of points; (3) isolate the exact missing input at mu(d) = 0;
(4) record the reductions and dead ends that were checked.

**Outcome.** (PE-NH) is not proved here, and no counterexample is given. What is new and rigorous: the Configuration
Lemma G and its corollaries (§2), and a one-sided solution / smearing identity (§4) together with the reason it does
not close. The chain itself (§1) was re-checked and no flaw was found.

## 1. Check of the chain
- Theorem J (R6-a §2). Re-checked line by line. Step 3 uses (*) for P phi, which costs one derivative
  (||P phi||_{C^k} <= C ||phi||_{C^{k+1}}); that is harmless. F1, F2 and the Fourier step are correct.
- Lemma K, Corollaries 4.1/4.2 and Theorem 5.1: correct, given the classical stable manifold theorem and the
  Katok / Lian–Young horseshoe theorem for C^2 flows with a hyperbolic ergodic measure of positive entropy that is not
  carried by Zero(X). Both are cited from memory, as in the source.
- Step 4 (variational principle via flow-ergodic decomposition and Jacobs' formula): correct.
So the chain is sound, and (PE-NH) is exactly what is missing.

**Remark 1.1 (an alternative sufficient statement, already implicit in R5-a).** The theorem of R5-a needs no GH:
lambda* = lim (1/n) max log||Dg_n|| > 0 gives a real kappa != 0 and a nonzero u in D' with Xu = kappa u. If
h_top(g_1) > 0, the variational principle and Ruelle's inequality give an ergodic measure with a positive exponent,
so lambda* > 0. Hence the following statement would also imply the goal:
(E1) under GH, X has no real nonzero eigenvalue on D'.
I could not prove (E1) either (see §5).

## 2. Configuration Lemma (proved; GH + Theorem J only)

Conventions: nu, d = div_nu X and J_t are as in the brief. Fix a Riemannian distance; L_d denotes the Lipschitz
constant of d.

**Lemma G.** Assume GH. Let z_1, ..., z_N be distinct points of M. Let ~u and ~s be two equivalence relations on
{1, ..., N}, with r_u and r_s classes respectively. Suppose there are constants C > 0, theta > 0 and 0 <= eps < theta
such that:
 (a) if i ~u j, then d(g_t z_i, g_t z_j) <= C e^{-theta|t|} for all t <= 0;
 (b) if i ~s j, then d(g_t z_i, g_t z_j) <= C e^{-theta t} for all t >= 0;
 (c) J_t(z_i) <= C + eps|t| for all real t and all i.
Then N <= r_u + r_s.

*Proof.*
1. *Jacobian defects.* Let i ~u j. For t <= 0,
   J_t(z_j) - J_t(z_i) = -int_t^0 (d(g_s z_j) - d(g_s z_i)) ds,
   and the integrand is bounded by L_d C e^{-theta|s|}. So beta_{ij} := lim_{t -> -inf} (J_t(z_j) - J_t(z_i)) exists,
   |beta_{ij}| <= L_d C/theta, and |J_t(z_j) - J_t(z_i) - beta_{ij}| <= (L_d C/theta) e^{-theta|t|} for t <= 0.
   The same holds for i ~s j as t -> +inf; call that limit beta'_{ij}.
2. *Linear algebra.* In each ~u-class U fix a representative i_U, and in each ~s-class V a representative i'_V.
   Consider the r_u + r_s linear equations in a in R^N:
   sum_{i in U} a_i e^{beta_{i_U i}} = 0 for every ~u-class U, and sum_{i in V} a_i e^{beta'_{i'_V i}} = 0 for every
   ~s-class V.
   If N > r_u + r_s, there is a nonzero solution a. Put S := sum_i a_i delta_{z_i}. Then S != 0, because the points
   are distinct.
3. *Backward decay.* Let t <= 0 and phi be smooth. Fix a ~u-class U, write z := z_{i_U} and beta_i := beta_{i_U i}.
   Using the class equation:
   sum_{i in U} a_i e^{J_t(z_i)} phi(g_t z_i) = e^{J_t(z)} sum_{i in U} a_i [ e^{J_t(z_i)-J_t(z)} phi(g_t z_i) - e^{beta_i} phi(g_t z) ].
   Each bracket is at most
   |e^{J_t(z_i)-J_t(z)} - e^{beta_i}| ||phi||_inf + e^{beta_i} ||dphi||_inf d(g_t z_i, g_t z) <= C_1 e^{-theta|t|} ||phi||_{C^1},
   because all exponents involved are bounded by 2 L_d C/theta and exp is Lipschitz on bounded sets. By (c),
   e^{J_t(z)} <= e^C e^{eps|t|}. Summing over the classes gives |F_phi(t)| <= C_2 e^{-(theta - eps)|t|} ||phi||_{C^1},
   where F_phi(t) = S(e^{J_t} phi o g_t).
4. *Forward decay.* The same computation with the ~s-classes gives |F_phi(t)| <= C_2 e^{-(theta-eps) t} ||phi||_{C^1}
   for t >= 0.
5. So (*) of Theorem J holds with k = 1 and rate theta - eps > 0. Theorem J gives S = 0, contradicting step 2. ∎

**Corollary G1.** Assume GH and let mu be ergodic with mu(d) = 0. Call z *generic* if J_t(z)/t -> 0 as t -> +-inf
(a set of full mu-measure). Then:
 (i) no three distinct generic points are pairwise exponentially asymptotic in both time directions;
 (ii) no two distinct generic points x, y are exponentially asymptotic in both directions with beta = beta' (zero
 "Jacobian holonomy");
 (iii) there is no "3 x 2 grid": distinct generic points x_1, x_2, x_3 that are pairwise backward-exponentially
 asymptotic, together with distinct generic x'_1, x'_2, x'_3 that are pairwise backward-exponentially asymptotic, such
 that x_i and x'_i are forward-exponentially asymptotic (i = 1, 2, 3).
*Proof.* For generic points, (c) holds for every eps > 0 (with C depending on eps and on the finitely many points);
take eps < theta. Case (i): N = 3, r_u = r_s = 1. Case (ii): with beta = lim (J_t(y) - J_t(x)) and S = delta_x - e^{-beta} delta_y, the two class
equations coincide, so effectively one equation in two unknowns, and steps 3–5 apply verbatim. Case (iii): N = 6,
r_u = 2, r_s = 3. ∎

(For a hyperbolic measure such grids come from local product structure. This is another proof of Theorem 5.1 that does
not go through periodic orbits, but it requires the local product structure of Pesin blocks; I do not claim it as new.)

**What Lemma G reduces (PE-NH) at mu(d) = 0 to.** (PE-NH) would follow if every non-hyperbolic positive-entropy
ergodic mu with mu(d) = 0 carried a configuration as in Lemma G (generic points, more points than classes, with a
common rate theta). For non-hyperbolic mu such configurations are not available in general. For a generic z,
dim W^s(z) + dim W^u(z) <= n - 2, because of the flow direction and at least one center direction. So stable and
unstable leaves of generic points generically do not meet, and the forward and backward classes of a finite set of
generic points are typically all singletons, giving N = r_u + r_s exactly in the best case. **This is the point where
the argument stops.**

## 3. Mechanism (i) of the planner (center smearing): why it does not close
Suppose point masses are replaced by densities spread along a disc transverse to W^s and W^u, in the center
direction, so that a "rectangle that does not close" becomes a smooth density. The center direction has zero exponent,
so a smooth bump along it is neither contracted nor expanded exponentially, and the transported distribution
S(e^{J_t} phi o g_t) keeps a non-decaying part of size comparable to the bump's mass. Its cancellation would need a
dynamically invariant identification between nearby center fibres (a commuting vector field, or an isometric center
holonomy). In the product examples (geodesic flow x Diophantine rotation) such an identification exists, and indeed
two-sided decaying S exist there: smooth mean-zero functions of the hyperbolic factor times Lebesgue, by exponential
mixing. For a general positive-entropy non-hyperbolic mu, Pesin theory provides no center foliation with any
regularity, so I could not make this work.

## 4. One-sided solutions and the smearing identity (proved; no GH needed except where stated)
**Lemma 4.1.** Let x != y with d(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0, and suppose J_t(x) <= C + eps|t| for
t <= 0, with eps < theta. Let b := lim_{t -> -inf} (J_t(x) - J_t(y)). Then
B(phi) := int_{-inf}^0 [e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y)] dt
is a distribution density of order 1 with B(P phi) = phi(x) - e^b phi(y). Equivalently, w = B/nu satisfies
Xw = -(delta_x - e^b delta_y)/nu. Under GH (by L1), w is the unique solution modulo constants.
*Proof.* Absolute convergence and the order-1 bound follow from the estimate of Lemma G, step 3. Integrating
d/dt [e^{J_t(z)} phi(g_t z)] = e^{J_t(z)} (P phi)(g_t z) over [-R, 0] and letting R -> inf gives the identity,
because the boundary term at -R tends to 0. Uniqueness: two solutions differ by an element of ker X, which consists of
constants (L1). ∎

**Smearing identity.** Let a -> (x_a, y_a) be a measurable family of such pairs over a probability space (A, da),
with constants uniform in a. Suppose the measures sigma = int delta_{x_a} da and sigma' = int e^{b_a} delta_{y_a} da
satisfy sigma - sigma' = f nu with f smooth. Then int_A B_a da = W nu, where W = lim_{R -> inf} int_0^R f o g_s ds
in D'. W solves XW = -f, so under GH W is smooth, and W o g_R -> 0 in D' as R -> inf.
*Proof.* Put (T_t m)(phi) := m(e^{J_t} phi o g_t). Then int B_a da = int_{-inf}^0 T_t(sigma - sigma') dt, which is
absolutely convergent by the uniform pair estimates. Moreover T_t(f nu)(phi) = int f e^{J_t} phi o g_t dnu
= int (f o g_{-t}) phi dnu, because e^{J_t} is the nu-Jacobian of g_t. Finally d/ds (W o g_s) = (XW) o g_s
= -f o g_s. ∎
*Why this is a dead end.* (1) Pesin unstable leaves vary only measurably, so I know of no family for which
sigma - sigma' is smooth. (2) Even then, "smooth W with W o g_R -> 0 weakly" is not contradictory by itself: it holds
for every mean-zero W when the flow is mixing for an invariant volume, and GH is not known to exclude mixing.

## 5. Attempts at (E1), and why they stop
Suppose Xu = kappa u with u in D' of order k, u != 0, kappa > 0, and put S = u nu. Then
S(e^{J_t} phi o g_t) = e^{-kappa t} S(phi): the transported distribution decays forward and grows backward, so
Theorem J does not apply. Pairing with the GH estimate |S(v - c(v))| <= C ||Xv||_{C^m} gives nothing, because the
weighted transport commutes with P = X + d, not with X: P(e^{J_t} phi o g_t) = e^{J_t} (P phi) o g_t. Hence C^m norms of
X applied to transported functions grow like ||Dg_t||^m. Conjugating X + kappa to X would need a smooth tau with
X tau = 1, and no such tau exists (integrate against an invariant probability). (E1) remains open.

## 6. Summary: proved, not proved, open
**Proved here (rigorous, given Theorem J from the brief):**
- Lemma G: under GH, no finite set of distinct points with more points than (backward classes + forward classes) can
  satisfy exponential asymptotics at a rate exceeding the Jacobian growth rate.
- Corollary G1: for an ergodic mu with mu(d) = 0, there are no three generic points pairwise doubly asymptotic, no
  doubly asymptotic generic pair with zero Jacobian holonomy, and no 3 x 2 su-grid.
- Lemma 4.1 and the smearing identity: one-sided solutions of Xw = -(delta_x - e^b delta_y)/nu, unique mod constants
  under GH.
- The chain was re-checked and is sound. (E1) alone would also imply the goal (Remark 1.1).

**Not proved:** (PE-NH) itself, i.e. the case of a non-hyperbolic ergodic mu with h_mu(g_1) > 0. This includes the case
mu(d) = 0 in every dimension >= 4, and, without the normal-form citation of R6-a Prop. 6.2, the case
|mu(d)| >= (smallest exponent on the relevant side) with higher-dimensional unstable (stable) directions. No
counterexample was found. The Greenfield–Wallach conjecture (cited from memory; a conjecture, not a theorem) predicts
that GH flows are smoothly conjugate to Diophantine linear flows on tori, and these have zero entropy, so I expect
(PE-NH) to be true.

**Open questions (explicit):**
1. (PE0) Does GH exclude an ergodic, non-hyperbolic mu with h_mu(g_1) > 0 and mu(d) = 0? A sufficient condition is a
   configuration as in Lemma G made of mu-generic points. Such configurations are missing because generic stable and
   unstable leaves do not meet in the presence of a center direction.
2. (E1) Does GH exclude real nonzero eigenvalues of X on D'? This would settle the problem directly (Remark 1.1).
3. Is there a continuation of single-orbit Laplace transforms across Re z = 0 for non-hyperbolic positive-entropy
   measures (the mechanism of Lemma M / Theorem B without periodic orbits)?

=== END OF ANSWER round7_q9 ===
