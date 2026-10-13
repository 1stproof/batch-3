# Answer to round12_q3: attempt on (PE0)

## 0. Status

(PE0) is **not proved** here, and I found no counterexample. What I add:

- **Theorem T (fully proved; GH plus a smooth invariant volume).** Take an su-chain x_0 ->u x_1 ->s x_2 ->u ... ->s x_{2L}, with exponentially asymptotic pairs, which closes up to a flow shift: x_{2L} = g_tau x_0. Then tau = 0. Combined with Theorem J, the signed point configuration sum_i (-1)^i delta_{x_i} vanishes. The new ingredient is an **integrality argument**: in a flow box, the cycle functional is the product of ds with a sum of integer dipoles, and GH forces this to equal tau times a smooth transversal density. A sum of integer dipoles of finite total length cannot equal a nonzero smooth density.
  So in the volume case the "temporal distance" obstruction to the su-cycle method is gone. The only obstruction left is the displacement in the centre direction transverse to X.
- **Corollary T2 (proved, volume case).** su-classes (of the relations "exponentially asymptotic in the past/future") meet every orbit in at most one point, are measure-theoretically null, and carry no nondegenerate closed chains. So the volume case of (PE0) reduces to the purely dynamical question (Q-vol) of Section 4.2.
- A precise account of why neither Theorem T nor its argument reaches (PE0) (Section 4), and the open questions (Section 6).

The chain itself (variational principle, then entry 113, then (PE0), giving the claim) looks logically correct to me as stated; see Section 5.

Conventions are as in the brief: nu is a smooth positive density, d = div_nu X, J_t is the log-Jacobian, P phi = X phi + d phi. "Volume case" means X preserves a smooth positive probability density omega. By (O2) the flow is then uniquely ergodic and has no zeros (dim M >= 2), and every smooth f with omega(f) = 0 is f = Xu with u smooth. By Lemma 2 (Text B) with k = 1, ||u||_{C^1} <= C ||f||_{C^m} when u is normalised by omega(u) = 0.

## 1. Statement

Fix a Riemannian distance on M. Every Lipschitz phi satisfies |phi(y) - phi(z)| <= Lip(phi) d(y,z).

**Definition (su-chain closing up to a flow shift).** Let L >= 1, C_0 > 0 and theta > 0. A tuple (x_0, x_1, ..., x_{2L}) of points of M is a *chain with constants (C_0, theta)* if for i = 0, ..., L-1:
- (u) d(g_t x_{2i}, g_t x_{2i+1}) <= C_0 e^{-theta |t|} for all t <= 0;
- (s) d(g_t x_{2i+1}, g_t x_{2i+2}) <= C_0 e^{-theta t} for all t >= 0.

Trivial legs (x_{2i+1} = x_{2i}, etc.) are allowed. The chain *closes up to the flow shift tau* (tau real) if x_{2L} = g_tau x_0.

(Pesin theory supplies such legs: two points on one global Pesin unstable leaf of a regular point satisfy (u) with some constants, and likewise for stable leaves. Finitely many legs give common constants.)

**Theorem T.** Assume GH, dim M >= 2, and that X preserves a smooth positive probability density omega. Let (x_0, ..., x_{2L}) be a chain closing up to the flow shift tau. Then
 (a) tau = 0, and
 (b) sum_{i=0}^{2L-1} (-1)^i delta_{x_i} = 0 as a measure. That is, every point occurs among x_0, x_2, ..., x_{2L-2} exactly as often as among x_1, x_3, ..., x_{2L-1}.

Consequences (immediate from (b)):
- In the volume case there is no pair x != y with d(g_t x, g_t y) <= C e^{-theta|t|} for all real t (L = 1, x_2 = x_0).
- There is no nondegenerate su-quadrilateral x_0 ->u x_1 ->s x_2 ->u x_3 ->s g_tau x_0 with x_1 != x_0, x_2 != x_1, x_3 != x_2, x_0 != x_3 (closing exactly or up to a flow shift). Indeed (a) gives tau = 0, and then (b) requires {x_0, x_2} = {x_1, x_3} as multisets. Since x_0 != x_1 and x_0 != x_3, this is impossible.

## 2. The integrality lemma (elementary, fully proved)

**Lemma I.** Let m >= 1 and R > 0, and let B(r) denote the open Euclidean ball of radius r about 0 in R^m. Suppose we are given:
- a finite family (zeta_j, e_j), j in F, with zeta_j in R^m and e_j in Z;
- a sequence of pairs (a_k, b_k), k in N, of points of R^m with sum_k |a_k - b_k| < infinity.

For a Lipschitz function eta on R^m put
 Lambda(eta) := sum_{j in F} e_j eta(zeta_j) + sum_k (eta(a_k) - eta(b_k)).
The series converges absolutely, since its terms are bounded by Lip(eta) |a_k - b_k|. Let w be continuous on B(R), and suppose that Lambda(eta) = int eta w dz for every Lipschitz eta with compact support in B(R). Then int_{B(r)} w dz is an integer for almost every r in (0, R).

*Proof.* For 0 < eps < r < R put eta_{r,eps}(x) := H_eps(r - |x|), where H_eps(s) := min(1, max(0, s/eps)). Then eta_{r,eps} is Lipschitz with support in the closed ball of radius r, which lies inside B(R). Pointwise, eta_{r,eps}(x) -> 1[|x| < r] as eps -> 0, because H_eps(s) -> 1[s > 0] for every real s.

Set alpha_k = |a_k|, beta_k = |b_k| and d_k = |a_k - b_k|, so that |alpha_k - beta_k| <= d_k. Write I_k for the closed interval between alpha_k and beta_k. Define
 G_k(r, eps) := eta_{r,eps}(a_k) - eta_{r,eps}(b_k),  g_k(r) := 1[alpha_k < r] - 1[beta_k < r].
We have |G_k| <= min(1, d_k/eps). Also G_k(r, eps) = 0 unless r lies in (min I_k, max I_k + eps). Finally g_k(r) = 0 unless r lies in I_k, and |g_k| <= 1. Hence
 int_0^R |G_k(r,eps) - g_k(r)| dr <= min(1, d_k/eps)(d_k + eps) + d_k <= 3 d_k.
For each fixed k the left side tends to 0 as eps -> 0: the integrand tends to 0 for every r outside {alpha_k, beta_k}, and it is bounded by 2 on a bounded interval. Since sum_k d_k < infinity, dominated convergence (over k) gives
 E(eps) := int_0^R sum_k |G_k(r,eps) - g_k(r)| dr -> 0 as eps -> 0.
Also int_0^R sum_k |g_k(r)| dr <= sum_k d_k < infinity, so sum_k |g_k(r)| < infinity for a.e. r. Choose eps_l -> 0 with sum_l E(eps_l) < infinity. Then for a.e. r we have sum_k |G_k(r, eps_l) - g_k(r)| -> 0 as l -> infinity. For such r, if moreover r differs from every |zeta_j|,
 Lambda(eta_{r,eps_l}) -> N(r) := sum_{j in F} e_j 1[|zeta_j| < r] + sum_k g_k(r).
This N(r) is an integer, because only finitely many g_k(r) are nonzero and they lie in {-1, 0, 1}. On the other hand Lambda(eta_{r,eps_l}) = int eta_{r,eps_l} w dz -> int_{B(r)} w dz by dominated convergence. ∎

**Corollary I'.** In Lemma I let w = tau w_0, with tau real and w_0 continuous and positive on B(R). Then tau = 0.
*Proof.* f(r) := tau int_{B(r)} w_0 is continuous on [0, R) with f(0) = 0, and it is strictly monotone if tau != 0. So 0 < |f(r)| < 1 for all r in some interval (0, r_1). There f(r) is not an integer, contradicting Lemma I. ∎

(This is the one-codimensional form of the fact that a 0-dimensional boundary of an integer 1-current of finite mass cannot be a nonzero absolutely continuous measure. The elementary proof above avoids the Federer-Fleming boundary rectifiability theorem.)

## 3. Proof of Theorem T

Throughout, (x_0, ..., x_{2L}) is a chain with constants (C_0, theta) and x_{2L} = g_tau x_0. Call a pair (a, b; H) a *u-leg* if it is (x_{2i}, x_{2i+1}; (-inf, 0]), and an *s-leg* if it is (x_{2i+2}, x_{2i+1}; [0, inf)). Note the order in the s-leg. In both cases d(g_t a, g_t b) <= C_0 e^{-theta|t|} for t in H.

**Step 1 (the cycle functional).** For Lipschitz phi define
 l(phi) := sum over the 2L legs (a, b; H) of int_H (phi(g_t a) - phi(g_t b)) dt.
Each integral converges absolutely, being bounded by Lip(phi) C_0/theta. So |l(phi)| <= 2L C_0 Lip(phi)/theta, and l(1) = 0. Also put
 seg(phi) := int_0^tau phi(g_s x_0) ds  (with the usual orientation if tau < 0).

**Step 2 (telescoping; no GH).** For smooth u,
 l(Xu) = u(x_0) - u(x_{2L}) = u(x_0) - u(g_tau x_0) = -seg(Xu).
*Proof.* Since (Xu)(g_t a) = d/dt u(g_t a):
- For a u-leg: int_{-inf}^0 ((Xu)(g_t a) - (Xu)(g_t b)) dt = u(a) - u(b) - lim_{t -> -inf} (u(g_t a) - u(g_t b)) = u(a) - u(b). The limit is 0 because d(g_t a, g_t b) -> 0 and u is uniformly continuous.
- For an s-leg (a, b) = (x_{2i+2}, x_{2i+1}): the integral is lim_{t -> inf}(u(g_t a) - u(g_t b)) - (u(a) - u(b)) = u(x_{2i+1}) - u(x_{2i+2}).
Summing, sum_i [u(x_{2i}) - u(x_{2i+1})] + sum_i [u(x_{2i+1}) - u(x_{2i+2})] = u(x_0) - u(x_{2L}). Finally u(g_tau x_0) - u(x_0) = int_0^tau (Xu)(g_s x_0) ds. ∎

**Step 3 (the GH identity).** For every Lipschitz phi,
 l(phi) = tau omega(phi) - seg(phi).   (3.1)
*Proof.* First let phi be smooth. Then f := phi - omega(phi) is smooth with omega(f) = 0, so f = Xu with u smooth (volume case, (O2)). Since l(1) = 0, Step 2 gives l(phi) = l(f) = -seg(f) = -seg(phi) + tau omega(phi).
Now let phi be Lipschitz. Mollifying in finitely many charts with a partition of unity gives smooth phi_j -> phi uniformly with sup_j Lip(phi_j) < infinity. Both sides of (3.1) pass to the limit: on the left by dominated convergence in each leg integral (the integrands are bounded by sup_j Lip(phi_j) C_0 e^{-theta|t|}), on the right trivially. ∎

**Step 4 (flow box).** Let K := {x_0, ..., x_{2L}} ∪ {g_s x_0 : s between 0 and tau}. This is a compact set with empty interior (dim M >= 2), so pick p not in K. Then X(p) != 0 (no zeros in the volume case).
By the flow box theorem there are delta > 0, R > 0, a smooth embedded disc sigma: B(3R) -> M transverse to X with sigma(0) = p (B(r) the ball in R^{n-1}, n = dim M), and a map Psi(s, z) := g_s(sigma(z)) which is a diffeomorphism from (-3 delta, 3 delta) x B(3R) onto an open set. Shrinking delta and R we may assume that U' := Psi((-2delta, 2delta) x B(2R)) does not meet K.
Since Psi_* (d/ds) = X and L_X omega = 0, we have Psi^* omega = w_0(z) ds dz with w_0 smooth and positive, independent of s.
Since Psi^{-1} is smooth on a neighbourhood of the compact set Psi([-delta, delta] x closed B(3R/2)), there are c_2 > 0 and C_1 such that for y in that set and d(y, y') < c_2, the point y' lies in the image of Psi and |Psi^{-1}(y) - Psi^{-1}(y')| <= C_1 d(y, y').

Test functions: for chi in C_c^inf((-delta, delta)) with int chi = 1 and eta Lipschitz with support in B(R), let phi := (chi ⊗ eta) ∘ Psi^{-1} on Psi((-delta,delta) x B(R)), extended by 0. This phi is Lipschitz on M, with support in U' and away from K. So seg(phi) = 0, and
 omega(phi) = int chi(s) ds · int eta w_0 dz = int eta w_0 dz.   (3.2)

**Step 5 (crossings).** Fix a leg (a, b; H). Here a and b are among the x_i, so they are not in U'. Say that a *crosses* at time t if g_t a = Psi(0, z) for some z in B(2R), and write z = z(t).
- (i) If a crosses at time t, then |t| >= 2delta. Otherwise a = g_{-t} Psi(0, z) = Psi(-t, z) would lie in U'.
- (ii) Distinct crossing times of a differ by at least 2delta. If t < t' < t + 2delta were both crossing times, then Psi(t' - t, z(t)) = g_{t'} a = Psi(0, z(t')), contradicting injectivity of Psi.
- (iii) If t is in H and g_t a lies in supp phi, so that g_t a = Psi(s, z) with |s| < delta and z in B(R), then t_c := t - s is a crossing time of a with z(t_c) = z. By (i), |t_c| >= 2delta > |t - t_c|, so t_c has the same sign as t and lies in H. So the time set {t in H : phi(g_t a) != 0} is contained in the disjoint union of the windows (t_c - delta, t_c + delta) over crossing times t_c in H. On each window, phi(g_t a) = chi(t - t_c) eta(z(t_c)), so the window contributes eta(z(t_c)) to int phi(g_t a) dt.
The same holds for b.

*Matching.* Choose T_1 such that C_1 C_0 e^{-theta(T_1 - delta)} < min(delta/2, R/4, c_2). Let t_c in H with |t_c| >= T_1 be a crossing time of a with z := z(t_c) in B(3R/2). Then g_{t_c} b = Psi(s', z') with |s'| + |z' - z| <= C_1 C_0 e^{-theta|t_c|} < delta/2. So t_c - s' is a crossing time of b with z(t_c - s') = z'. Conversely, every crossing time t' of b in H with |t'| >= T_1 + delta and z(t') in B(5R/4) arises in this way from a crossing time of a, by the symmetric argument. Crossings of a with z outside B(3R/2), and crossings of b with z outside B(5R/4), contribute 0, because eta vanishes outside B(R).

*Conclusion for one leg.* Let (alpha_k, beta_k) := (z(t_c), z(t_c - s')) run over the matched pairs, that is, over the crossing times t_c in H of a with |t_c| >= T_1 + 2delta and z(t_c) in B(3R/2). Their partners occur at times |t| >= T_1 + 3delta/2. Every crossing of b at a time |t'| >= T_1 + 3delta with z(t') in B(5R/4) is such a partner, since its a-partner has |t_c| >= T_1 + 5delta/2. Let (zeta_j, e_j) run over the crossings of a (with e_j = +1) and of b (with e_j = -1) at times |t| < T_1 + 3delta that are not used in a matched pair; there are finitely many by (ii). All remaining crossings have z outside B(R), and they contribute 0. Then
 int_H (phi(g_t a) - phi(g_t b)) dt = sum_j e_j eta(zeta_j) + sum_k (eta(alpha_k) - eta(beta_k)),
 with sum_k |alpha_k - beta_k| <= sum_k C_1 C_0 e^{-theta |t_k|} < infinity,
because the t_k are 2delta-separated by (ii).
To justify this rearrangement, integrate over H ∩ [-T, T] and let T -> infinity. For T in the gap between windows the truncated integral equals the finite version of the right side, up to at most one matched pair whose two windows straddle ±T. The contribution of that pair is at most Lip(phi) C_0 e^{-theta(T - delta)} · 2delta + Lip(eta) |alpha_k - beta_k|, which tends to 0. The data (zeta_j, e_j, alpha_k, beta_k) depend only on the leg and the chart, not on chi or eta.

**Step 6 (end of proof of (a)).** Sum Step 5 over the 2L legs. This gives finite data (zeta_j, e_j) with e_j in {±1} and a summable family of pairs (alpha_k, beta_k) such that, for every Lipschitz eta with support in B(R),
 l(phi) = Lambda(eta)  (notation of Lemma I).
By (3.1), (3.2) and seg(phi) = 0, we get Lambda(eta) = tau int eta w_0 dz. Corollary I' (m = n - 1 >= 1) gives tau = 0.

**Step 7 (proof of (b)).** Now tau = 0, so x_{2L} = x_0. Take nu = omega, so d = 0 and J_t = 0. Let S := sum_{i=0}^{2L-1} (-1)^i delta_{x_i}. Then F_phi(t) = S(phi ∘ g_t) satisfies:
- for t <= 0, grouping into u-legs: |F_phi(t)| <= sum_i |phi(g_t x_{2i}) - phi(g_t x_{2i+1})| <= L ||phi||_{C^1} C_0 e^{-theta|t|};
- for t >= 0, grouping into s-legs and using x_{2L} = x_0: F_phi(t) = -sum_i (phi(g_t x_{2i+1}) - phi(g_t x_{2i+2})), so |F_phi(t)| <= L ||phi||_{C^1} C_0 e^{-theta t}.
So (*) of Theorem J holds with k = 1, and Theorem J (quoted in the brief, R6-a, proved there from GH and L1) gives S = 0. ∎

**Remarks on Theorem T.**
1. Where GH enters: only through (3.1) (closed range with one-dimensional cokernel, spanned by omega) and through Theorem J. Without GH, (3.1) fails. For a contact Anosov flow on a 3-manifold, su-quadrilaterals close up to a nonzero flow shift (Brin's temporal distance), and nothing forbids that. For the suspension of a hyperbolic toral automorphism with constant roof, quadrilaterals close with tau = 0, and the point configuration S then has two-sided exponential decay, which is allowed because that flow is not GH. So both halves of Theorem T genuinely use GH.
2. Exponential convergence is used only to make sum_k |alpha_k - beta_k| finite (2delta-separated crossing times) and in Step 7. Any summable rate would do for (a).
3. As a check, this reproves the volume case of Theorem 5.1 in dimension 3 without Katok's horseshoe theorem. Let mu = omega be hyperbolic with exponents chi > 0 = 0 > -chi, and take x_0, x_1 in W^u_loc(x_0), x_2 in W^s_loc(x_1) in a Pesin block, with x_1 != x_0 and x_2 != x_1. The local unstable leaf of x_2 meets the 2-dimensional local weak-stable leaf W^{cs}_loc(x_0) = union of W^s_loc(g_s x_0), |s| small, at a point x_3. This uses transversality and the uniform size of local leaves on Pesin blocks (standard, cited). Then x_3 is in W^s(g_tau x_0) for some small tau. Theorem T(a) gives tau = 0, and (b) gives {x_0, x_2} = {x_1, x_3}, which requires either x_0 = x_1 or (x_0 = x_3 and x_2 = x_1). Both are excluded. Contradiction.

## 4. Consequences in the volume case, and why this does not reach (PE0)

### 4.1 su-classes (fully proved)

Define relations on M by:
- x ~_u y iff there are C, theta > 0 with d(g_t x, g_t y) <= C e^{-theta|t|} for all t <= 0;
- x ~_s y iff the same holds for all t >= 0.

Each of these is an equivalence relation. Transitivity: add the constants and take the smaller rate. Neither needs Pesin theory, though Pesin leaves of regular points lie inside these classes. Let ~ be the equivalence relation they generate, and A(x) the ~-class of x. A finite chain of ~_u and ~_s steps is a chain in the sense of Section 1 with common constants, after inserting trivial legs where two steps of the same type are adjacent.

The classes are equivariant: A(g_t x) = g_t A(x). Indeed, if d(g_s a, g_s b) <= C e^{-theta|s|} for s <= 0, then for s <= 0 we have d(g_s g_t a, g_s g_t b) <= C' e^{-theta|s|}, with C' := max(C e^{theta|t|}, diam(M) e^{theta|t|}). The same holds for s >= 0.

**Corollary T2.** Assume GH, dim M >= 2 and a smooth invariant volume omega. Then for every x in M:
 (i) A(x) ∩ {g_t x : t in R} = {x};
 (ii) every omega-measurable set E contained in A(x) has omega(E) = 0;
 (iii) every closed chain (x_0, ..., x_{2L} = x_0) built from ~_u and ~_s steps is degenerate: sum_{i<2L} (-1)^i delta_{x_i} = 0.
*Proof.* (i) If g_t x is in A(x), there is a chain from x to g_t x, so t = 0 by Theorem T(a). (Here x is not periodic: there are no periodic orbits in the volume case by (O2), so g_t x = x forces t = 0.) (ii) For t != 0 the classes A(x) and A(g_t x) = g_t A(x) are disjoint: a common point would put g_t x in A(x), contradicting (i). Hence the sets g_t E, t in [0, 1), are pairwise disjoint and measurable, and all have measure omega(E) by invariance. Uncountably many disjoint sets of equal measure in a probability space must have measure 0. (iii) is Theorem T(b). ∎

So in the volume case under GH the su-relation (with no restriction to Pesin blocks) is "thin" (null classes, each meeting every orbit at most once) and "acyclic" (no nondegenerate closed chains). For comparison, consider the non-GH example: the suspension, with constant roof, of A x R_alpha on T^3 (A hyperbolic on T^2, R_alpha an irrational rotation). It has positive entropy, a zero exponent transverse to the flow, and its volume is a (PE0)-type measure. Its su-classes are the 2-tori T^2 x {y} x {s}: they are null and meet each orbit only once, so (i) and (ii) hold. But they contain nondegenerate closed su-quadrilaterals, so (iii) fails. Hence (i)-(ii) alone are compatible with positive entropy plus a centre, and (iii) is the operative constraint.

### 4.2 The remaining gap in the volume case

By Corollary T2, (PE0) restricted to the volume case would follow from:

**(Q-vol)** Let omega be a smooth invariant volume of a C^inf flow on a compact manifold, ergodic (indeed uniquely ergodic and minimal) with h_omega(g_1) > 0, and with a zero exponent transverse to X. Then there is a nondegenerate closed chain of ~_u and ~_s steps (sum_i (-1)^i delta_{x_i} != 0), or a chain from some x to g_t x with t != 0.

I could not prove (Q-vol). The obstruction is exactly the centre displacement. For a non-hyperbolic measure, a chain that starts at x_0 ends at x_{2L}, and generically x_{2L} lies neither on the orbit of x_0 nor at x_0 itself. There is no dynamically defined centre-stable lamination along which one could slide the endpoint back. Points of a (non-unique) centre manifold are not asymptotic to each other, so they cannot be legs.

A quantitative version of (3.1) handles approximate closing, but only up to compactness:

**Lemma T3 (proved).** Under the hypotheses of Theorem T, but without assuming closure, for every smooth phi and every real tau,
 |l(phi) - tau omega(phi) + seg_tau(phi)| <= C ||phi||_{C^m} d(g_tau x_0, x_{2L}),
with C, m from Lemma 2 (k = 1) and seg_tau(phi) = int_0^tau phi(g_s x_0) ds.
*Proof.* Step 2 gives l(phi) = u(x_0) - u(x_{2L}) with u = X^{-1}(phi - omega(phi)) normalised to mean 0. Also u(x_0) = u(g_tau x_0) + tau omega(phi) - seg_tau(phi). Finally |u(g_tau x_0) - u(x_{2L})| <= ||u||_{C^1} d(g_tau x_0, x_{2L}) <= 2C ||phi||_{C^m} d(g_tau x_0, x_{2L}). ∎

Suppose one has a sequence of chains whose legs are local Pesin leaves inside a fixed Pesin block (so with uniform constants), whose length L is bounded, and whose closing defects tend to 0. Pass to a limit: local leaves vary continuously on a Pesin block, so the limit is an exactly closed chain (up to a flow shift), to which Theorem T applies. But the limit chain may be degenerate even when every approximating chain is not. So approximate closing helps only if non-degeneracy survives the limit, for example if some leg of length >= rho_0 > 0 cannot cancel in the limit configuration. Positive entropy alone does not seem to provide such a sequence when there is a centre.

### 4.3 Why the argument does not extend to the non-volume case of (PE0)

In (PE0) the measure mu has mu-mean of J_1 equal to 0, but X need not preserve a smooth volume. Two things break.
1. The identity (3.1) used that the annihilator of X(C^inf) is spanned by omega. In general, the unweighted functional l + seg always annihilates X(C^inf); that is just Step 2, and no GH is needed. GH says only that X(C^inf) is closed, with annihilator the space of all invariant distribution densities, which may be large. The weighted version, with weights e^{J_t} on the legs and L1/(F1) in place of (O2), needs the weights to be consistent around the cycle: a holonomy condition sum of b-values = 0, one real equation. It then gives l^w + w_0 seg^w = c nu.
2. Even then, Lemma I fails for real weights. The transversal functional becomes sum_k (c_k delta_{alpha_k} - c'_k delta_{beta_k}) with real c_k = w e^{J_{t_k}(a)}. In one transversal dimension, sum_k c_k (delta_{a_k} - delta_{b_k}) = -(sum_k c_k 1_{[b_k, a_k]})', and every L^1 function is such a sum. So nothing prevents a weighted dipole sum from equalling a smooth density, and the integrality mechanism is lost. Only Theorem J (exact closure with tau = 0 plus the holonomy condition) survives, as in the earlier rounds.

### 4.4 Remarks on the planner's two mechanisms (heuristic, not proved)

- **Mechanism A (r -> 0 arrays).** All the estimates the sketch asks for (Pesin blocks, normal-form moments, subexponential centre defect) are GH-free. Only the final appeal to Theorem J uses GH. Any configuration family S_r satisfying the conjectured uniform two-sided bounds would therefore also exist for non-GH flows, such as the A x R_alpha suspension above. There Theorem J is not available, so nothing is contradicted, but the existence claim must hold there too. Further, if the diameter of S_r tends to 0, any normalised weak* limit is supported at one point, i.e. it is a finite-order jet distribution at a point p of the Pesin block. Two-sided exponential decay of such a jet would mean a nonzero vector of the (weighted) jet cocycle along the orbit of p decaying in both time directions. At an Oseledets-regular point this is impossible: forward decay forces all components to have negative exponents, and backward decay forces the lowest one to be positive. So either the bounds are not uniform in r, or the normalised limit is 0. Either way the "nonzero limit" step cannot work at r -> 0. The configuration has to stay at a fixed scale, where the centre defect is of order 1. This is consistent with Section 4.2: at fixed scale, what is needed is exact closure, and in the volume case exact closure up to a flow shift is all that is needed (Theorem T).
- **Mechanism B (spectral).** In the volume case GH gives bounded ergodic integrals and spectral measures flat to infinite order at 0. Lebesgue spectrum on the orthocomplement H_L of the Pinsker algebra does not contradict flatness of individual vectors. In the time-domain (innovation) representation, a vector of H_L with compactly supported, or exponentially decaying two-sided, innovation profile cannot be flat (Paley-Wiener plus quasi-analyticity, which is Theorem J in spectral form). One-sided exponential decay only gives a Hardy-space boundary value, and those can vanish to infinite order at a point. So mechanism B needs two-sided rates for the conditional expectations of a smooth f along the unstable filtration. Pesin theory gives these only on Pesin blocks, with no control of the tails. I see no way around this.

## 5. Check of the chain (as requested)

1. Variational step: h_top(g_1) = sup over g_1-invariant mu of h_mu(g_1). By the ergodic decomposition and Jacobs' theorem, some g_1-ergodic mu has h_mu(g_1) > 0. This is correct.
2. Entry 113 (cited; it relies on the Kalinin-Sadovskaya/Melnick non-stationary normal forms, which I did not re-verify) gives int J_1 dmu = 0 for such mu under GH.
3. (PE0) forbids such mu.
Hence (PE0) plus entry 113 plus step 1 give h_top(g_1) = 0. The topological entropy of the flow is by definition that of g_1. The derivation is logically sound, conditional on entry 113's citations. I found no flaw.

## 6. Summary: proved, not proved, open

**Proved here (complete proofs above):**
- Lemma I and Corollary I' (integrality of finite-length integer dipole sums against smooth densities).
- Theorem T. Under GH with a smooth invariant volume, every su-chain (exponentially asymptotic legs) closing up to a flow shift g_tau has tau = 0, and its signed point configuration vanishes.
- Lemma T3 (approximate-closure identity).
- Corollary T2. In the volume case, every su-class meets each orbit in at most one point, its measurable subsets are null, and its closed chains are degenerate.
- As a by-product (Remark 3 of Section 3), a Katok-free proof that in the volume case under GH, dim 3, the volume has zero entropy. The local-product facts on Pesin blocks used there are cited.

**Not proved:** (PE0). Neither its volume-case core nor the general case is settled.

**Open questions, precisely:**
- (Q-vol) (Section 4.2): does every positive-entropy smooth volume of a C^inf flow with a transverse zero exponent admit a nondegenerate closed su-chain, or a chain from x to g_t x with t != 0? A yes would prove (PE0) in the volume case, by Theorem T. A no would show that the su-cycle method cannot settle even the volume case.
- (Q-gen): find a substitute for the integrality Lemma I for Jacobian-weighted cycles. This is needed for the non-volume case of (PE0), where in addition the holonomy condition sum b = 0 must be met.
- Still open from earlier rounds: (E1), the absence of real eigen-distributions under GH. It would give lambda* = 0, and hence the full claim, via R5-a.

=== END OF ANSWER round12_q3 ===


