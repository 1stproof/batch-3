# round6_q10 — answer (final; partial result)

## Plan / current status
Target (PE): under GH every ergodic flow-invariant mu has h_mu(g_1) = 0.

Plan: (1) a new GH-uniqueness lemma, Lemma M: under GH there is no nonzero family of distributions T_z that is
meromorphic in z near 0 and satisfies T_z(X phi + d phi) = z T_z(phi). (2) Feed Lemma M with
(a) generic pairs (closes the planner's case -theta < lambda < 0 completely), and
(b) heteroclinic orbits between periodic orbits, using a weighted transfer operator on local strong unstable/stable
discs to continue the orbit integrals meromorphically to all of C.
Consequence: GH excludes every horseshoe. So every positive-entropy ergodic measure is non-hyperbolic, and
h_top = 0 when dim M <= 3. The general non-hyperbolic case stays open; see the last section.

## 0. Summary of the outcome
- The problem is NOT fully solved. Proved (some steps rely on cited standard theorems, named where used):
 * **Lemma M** (new, short, uses only GH): under GH, no nonzero family of distributions T_z, meromorphic in z
  near 0, satisfies T_z(X phi + d phi) = z T_z(phi).
 * **Theorem A / Corollary A**: under GH, a positive-entropy ergodic mu cannot have
  -chi^+ < mu(d) < 0 or 0 < mu(d) < |chi^-|. This removes the obstacle "show T_0 is not c nu" in the planner's
  sketch (b).
 * **Theorem B**: under GH there is no orbit going from a periodic orbit (along its strong unstable manifold) to a
  periodic orbit (along its strong stable manifold), whatever the signs of int_O d. Proved via a weighted transfer
  operator on local strong discs (Hennion + analytic Fredholm theory, cited) and Lemma M.
 * **Corollary 5.1**: under GH every ergodic measure of positive entropy is non-hyperbolic. So (PE) holds for all
  hyperbolic measures (via Katok / Lian–Young horseshoes).
 * **Corollary 5.2**: under GH, h_top(g_1) = 0 when dim M <= 3. This removes the configuration (H3) of [R5-d].
 * Step 2 of the chain is correct (Section 6).
- **Open:** (PE-rest) of Section 7. It concerns positive-entropy ergodic measures that are non-hyperbolic (so
 dim >= 4) with mu(d) = 0, or with |mu(d)| at least the relevant smallest exponent. For the latter, a
 normal-form/moment-cancellation route is sketched only.

## 1. Conventions
These are as in the brief. nu is a smooth positive density, d = div_nu X, P phi := X phi + d phi, and
J_t(x) = int_0^t d(g_s x) ds for real t. The cocycle rule is J_{a+b}(x) = J_b(x) + J_a(g_b x). A distribution
density T (a continuous linear functional on C^inf(M)) gives the generalised function u = T/nu, and
<Xu, phi nu> = -T(P phi) (Observation 0). For z in C we write T(P phi) = z T(phi) as "T is a z-eigenfamily member".
For any point w and smooth phi, d/dt [e^{J_t(w)} phi(g_t w)] = e^{J_t(w)} (P phi)(g_t w).   (1.1)

## 2. Lemma M (proved): no meromorphic eigen-family through z = 0

**Lemma M.** Assume GH. Let r > 0. For 0 < |z| < r let T_z be a distribution density with
 (a) for each smooth phi, z -> T_z(phi) is holomorphic on 0 < |z| < r and meromorphic at 0;
 (b) there are K and C with |T_z(phi)| <= C ||phi||_{C^K} for |z| = r/2;
 (c) T_z(P phi) = z T_z(phi) for all smooth phi and 0 < |z| < r.
Then T_z = 0 for all 0 < |z| < r.

*Proof.* For n in Z put A_n(phi) = (1/2 pi i) oint_{|z| = r/2} T_z(phi) z^{-n-1} dz. By (b), each A_n is a
distribution (|A_n(phi)| <= C (r/2)^{-n} ||phi||_{C^K}). By (a), T_z(phi) = sum_n A_n(phi) z^n is the Laurent
expansion on 0 < |z| < r. Multiply (c) by z^{-n-1} and integrate over the circle. This gives
 A_n(P phi) = A_{n-1}(phi) for all n in Z and all phi.   (2.1)
*Finite order.* E_m = {phi : A_n(phi) = 0 for all n < -m} is a closed subspace of C^inf(M) (an intersection of
kernels of continuous functionals). By (a), the union of the E_m is C^inf(M). By Baire, some E_m has interior, so
E_m = C^inf(M). Hence A_n = 0 for n < -m.
Suppose some A_n is nonzero, and let n0 be the least such index. By (2.1), A_{n0}(P phi) = A_{n0-1}(phi) = 0 for all
phi. So u = A_{n0}/nu satisfies Xu = 0. By L1, u is a constant c, i.e. A_{n0} = c nu. By (2.1) again,
A_{n0+1}(P phi) = c nu(phi) = c int phi dnu. So w = A_{n0+1}/nu satisfies <Xw, phi nu> = -c int phi dnu, i.e.
Xw = -c, a smooth (constant) function. By GH, w is smooth. Let mu be any flow-invariant Borel probability (one
exists, M being compact). Then int Xw dmu = d/dt|_{t=0} int w o g_t dmu = 0, so c = 0 and A_{n0} = 0. This
contradicts the choice of n0. Hence all A_n = 0 and T_z = 0. ∎

Remarks.
1. Only L1 and GH applied to a constant right-hand side are used. The argument uses neither dimension, nor volume,
nor Pesin theory.
2. Without GH the lemma fails. For the north–south flow, the weighted orbit integral over a source-to-sink orbit is
an entire eigen-family of this kind, and its value at z = 0 is a non-constant solution of Xu = 0.
3. If the family is holomorphic on a connected open set Omega containing 0 (respectively meromorphic on Omega with
the bounds (b) near 0), then T_z(phi) = 0 near 0. By the identity theorem it vanishes on all of Omega, for each phi.

## 3. Theorem A (generic pairs): the planner's case -theta < lambda < 0 is excluded

**Theorem A (deterministic form; proved).** Assume GH. Suppose x != y in M, and constants C, theta > 0, alpha < 0,
kappa >= 0 with kappa < theta, satisfy:
 (i) d(g_{-t}x, g_{-t}y) <= C e^{-theta t} for t >= 0;
 (ii) J_t(x) <= C + alpha t and J_t(y) <= C + alpha t for t >= 0;
 (iii) J_t(x) <= C + kappa |t| for t <= 0.
This is impossible.

*Proof.*
1. As in R5-a Step 4(a), |d(g_s x) - d(g_s y)| <= Lip(d) C e^{-theta|s|} for s <= 0. So
b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists, and |J_t(x) - J_t(y) - b| <= K0 e^{-theta|t|} for t <= 0.
2. Put c_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y). By (1.1), c_phi' = c_{P phi}.
 For t >= 0, (ii) gives |c_phi(t)| <= (1 + e^b) e^C ||phi||_inf e^{alpha t}.
 For t <= 0, (i), step 1 and (iii) give |c_phi(t)| <= C1 ||phi||_{C^1} e^{(kappa - theta)|t|}, exactly as in
 R5-a Step 4(c).
3. For alpha < Re z < theta - kappa (a strip that contains 0), T_z(phi) := int_R e^{-zt} c_phi(t) dt converges
absolutely and locally uniformly. So z -> T_z(phi) is holomorphic, and |T_z(phi)| <= C(z) ||phi||_{C^1} with C(z)
locally bounded. Integrating (1.1) by parts on [-R, R], the boundary terms tend to 0 by step 2. Hence
T_z(P phi) = z T_z(phi).
4. By Lemma M and Remark 3, T_z(phi) = 0 for every phi and every z in the strip.
5. Choose phi0 smooth with phi0(x) = 1 and phi0(y) = 0. Fix real z0 in the strip. Then G(t) = e^{-z0 t} c_{phi0}(t)
is continuous and lies in L^1(R). Its Fourier transform is omega -> T_{z0 + i omega}(phi0) = 0. So G = 0, which
contradicts G(0) = 1. ∎

**Corollary A (proved modulo cited Pesin / Ledrappier–Young theory).** Assume GH. Let mu be an ergodic flow-invariant
probability with h_mu(g_1) > 0, and let lambda = mu(d), which is the sum of the Lyapunov exponents of mu. Let
chi^+ > 0 be the smallest positive exponent of mu and chi^- < 0 the negative exponent closest to 0. Then
 lambda = 0, or lambda <= -chi^+, or lambda >= |chi^-|.
*Proof.* Suppose -chi^+ < lambda < 0. Pick theta with |lambda| < theta < chi^+, and eps > 0 small.
- Cited (Pesin; Ledrappier–Young, Ann. Math. 1985, Part I): for mu-a.e. x, the Pesin unstable manifold W^u(x) of
 g_1 consists of points y with d(g_{-n}x, g_{-n}y) <= C(x, y) e^{-theta n}. Moreover, h_mu(g_1) > 0 implies that the
 conditional measures of mu on unstable leaves (for a subordinate partition) are non-atomic for mu-a.e. x.
- Hence for mu-a.e. x there is y != x in W^u(x) that is mu-generic in forward time, because the set of
 forward-generic points has full mu-measure and therefore full conditional measure.
- Take x generic in both time directions. Then J_t(x) = lambda t + o(|t|) as t -> +-inf, and
 J_t(y) = lambda t + o(t) as t -> +inf.
- So (i) holds, after passing from integer to real times as in R5-a Lemma 2; (ii) holds with alpha = lambda + eps;
 and (iii) holds with kappa = |lambda| + eps < theta. Theorem A gives a contradiction.
- The case 0 < lambda < |chi^-| follows by applying this to -X, which is GH by (O4). Under -X the exponents change
 sign, d becomes -d, and stable manifolds become unstable ones. ∎

So the strip obstruction of the planner's sketch at -theta < lambda < 0 is removed. The idea is Lemma M: one never
has to show that T_0 is not a multiple of nu, because the z-derivatives of the family force that multiple to
vanish. The cases lambda = 0 and |lambda| >= theta remain. Section 4 removes them whenever periodic orbits with
strong unstable and stable discs are available.

## 4. Theorem B (proved modulo two cited functional-analytic facts): GH excludes heteroclinic connections between periodic orbits

**Definition.** Let O be a periodic orbit of period P > 0 and x in O. A *contracting backward disc* at x is a
C^inf embedded closed disc Dbar containing x such that g_{-P}(Dbar) ⊂ Dbar, with a flat Riemannian metric on Dbar
(a chart metric) in which Dbar is a convex ball and ||D(g_{-P}|_Dbar)|| <= rho1 < 1 pointwise. A *contracting
forward disc* at x' in O' (period P') is defined the same way with g_{P'} in place of g_{-P}.

**Existence (cited, standard).** Suppose the linearised return map Dg_P(x) has an eigenvalue of modulus > 1. Then
the strong unstable manifold W^{uu}(x) of the fixed point x of g_P (for the part of the spectrum outside the unit
circle) is a C^inf injectively immersed submanifold. (Strong unstable manifold theorem, e.g. Hirsch–Pugh–Shub; strong
manifolds are as smooth as the map.) g_{-P} restricted to it is a contraction at x with spectral radius rho < 1.
Choosing a norm on T_x W^{uu} in which ||Dg_{-P}(x)|| < rho1 < 1, a small ball in a chart is a contracting backward
disc. Every y in W^{uu}(x) has g_{-nP} y in Dbar for all large n. For a hyperbolic periodic orbit O, W^u(O) is the
union of the W^{uu}(x), x in O. The same holds with s/forward in place of u/backward.

**Theorem B.** Assume GH. There are no periodic orbits O, O' (possibly O = O'), points x in O and x' in O',
contracting backward and forward discs Dbar at x and Dbar' at x', and a point y not in O ∪ O', such that
g_{-nP} y is in Dbar and g_{n P'} y is in Dbar' for some n >= 0 (equivalently for all large n).
In particular, GH excludes every orbit that is homoclinic or heteroclinic, along strong unstable and strong stable
manifolds, between periodic orbits whose linearised return maps have an eigenvalue outside, respectively inside,
the unit circle. No sign condition on int_O d is needed, so this contains Proposition 4.0.

**Cited facts.**
(H) Hennion's theorem (Proc. AMS 1993), quoted from memory. Let (B, ||.||) be a Banach space and |.| a norm on B
such that bounded subsets of (B, ||.||) are relatively compact for |.|. Let L be bounded on (B, ||.||) and on
(B, |.|) (more precisely, L: (B, ||.||) -> (B, |.|) compact), with
 ||L^n f|| <= R_n ||f|| + C_n |f| for all n,
and set r = liminf R_n^{1/n}. Then the essential spectral radius of L on B is at most r.
(F) Riesz–Schauder / analytic Fredholm theory. If r_ess(L) <= r, then the spectrum of L in {|s| > r} consists of
isolated eigenvalues of finite algebraic multiplicity, and the resolvent s -> (s - L)^{-1} is meromorphic on
{|s| > r} with finite-rank principal parts. Hence q -> (I - qL)^{-1} = q^{-1}(q^{-1} - L)^{-1} is meromorphic on
{|q| < 1/r}, and holomorphic near q = 0, where it is given by the Neumann series.

*Proof of Theorem B.*

**Step 1 (transfer operator on the backward disc).** Put G = g_{-P}|_Dbar and j = J_{-P}|_Dbar (smooth). Fix K >= 1
and let B_K = C^K(Dbar), with ||f||_K = max_{i <= K} sup |D^i f|, derivatives taken in the flat metric. Define
 (L f)(w) = e^{j(w)} f(G w).
By the cocycle rule, (L^n f)(w) = e^{J_{-nP}(w)} f(g_{-nP} w). Indeed J_{-(m+1)P}(w) = J_{-mP}(w) + J_{-P}(g_{-mP} w).
- *Lasota–Yorke bound.* D^K(L^n f) = e^{J_{-nP}} (D^K f)(G^n)[DG^n, ..., DG^n] + (terms containing only D^i f with
 i < K, with coefficients bounded for fixed n). Here ||DG^n|| <= rho1^n by the chain rule, and
 e^{J_{-nP}} <= E^n with E = max_Dbar e^j. So ||L^n f||_K <= E^n rho1^{nK} ||f||_K + C_n ||f||_{K-1}.
- *Compactness.* C^K(Dbar) embeds compactly in C^{K-1}(Dbar) (Arzelà–Ascoli), and L is bounded on both.
- By (H), r_ess(L on B_K) <= r_K := E rho1^K. By (F), q -> (I - qL)^{-1} is meromorphic on {|q| < 1/r_K} as a family
 of bounded operators on B_K.

**Step 2 (backward orbit integrals continue meromorphically to C).** For smooth phi, z in C and w in Dbar put
 Phi_z(w) = int_{-P}^0 e^{-zt} e^{J_t(w)} phi(g_t w) dt.
This is in C^inf(Dbar). It is entire in z as a B_K-valued map, with ||Phi_z||_K <= C(z) ||phi||_{C^K} and C(z) locally
bounded. Splitting (-inf, 0] into the intervals [-(n+1)P, -nP] and using the cocycle rule:
 int_{-inf}^0 e^{-zt} e^{J_t(w)} phi(g_t w) dt = sum_{n >= 0} e^{znP} (L^n Phi_z)(w),   (4.1)
which converges absolutely when Re z < -(log E)/P. (Then ||L^n||_{C^0} <= E^n, and the left side converges
absolutely too.) Fix n0 with y0 := g_{-n0 P} y in Dbar. Define, for Re z < -(log E)/P,
 B_z(phi) := int_{-inf}^0 e^{-zt} e^{J_t(y)} phi(g_t y) dt
  = int_{-n0P}^0 e^{-zt} e^{J_t(y)} phi(g_t y) dt + e^{z n0 P + J_{-n0P}(y)} [(I - e^{zP} L)^{-1} Phi_z](y0).
The second equality uses the shift t = s - n0 P and (4.1) at w = y0.
The right side is meromorphic in z on the half-plane H_K = {Re z < (-log r_K)/P} by Step 1. (Here z -> e^{zP} is
entire, Phi_z is entire, and evaluation at y0 is continuous on B_K.) Since r_K -> 0 as K -> inf and the
continuations for different K agree on a common left half-plane (the Neumann region), B_z(phi) extends to a
meromorphic function on C.
For K fixed and z in a compact set avoiding the poles of the K-resolvent (a set independent of phi),
|B_z(phi)| <= C ||phi||_{C^K}.
*Eigen-identity.* For Re z very negative, integrate (1.1) for w = y by parts over [-R, 0] and let R -> inf. The
boundary term at -R tends to 0 in the Neumann region. This gives
 B_z(P phi) = phi(y) + z B_z(phi);
by uniqueness of meromorphic continuation the identity holds on all of C (both sides are meromorphic in z, since
P phi is smooth).

**Step 3 (forward part).** In the same way, with G' = g_{P'}|_{Dbar'}, j' = J_{P'}, L' f = e^{j'} f o G' and
Phi'_z(w) = int_0^{P'} e^{-zt} e^{J_t(w)} phi(g_t w) dt, the forward integral
 F_z(phi) = int_0^inf e^{-zt} e^{J_t(y)} phi(g_t y) dt
(absolutely convergent for Re z large) extends meromorphically to C, with the analogous bounds and
 F_z(P phi) = -phi(y) + z F_z(phi).

**Step 4 (the eigen-family).** R_z := F_z + B_z is meromorphic on C (weakly), and R_z(P phi) = z R_z(phi). Fix K
large. On the closed unit disc the K-level families have finitely many poles, so there is r in (0, 1) with no pole
in 0 < |z| <= r. Then (a)–(c) of Lemma M hold (with the order bound C||phi||_{C^K} on |z| = r/2). Lemma M gives
R_z(phi) = 0 for 0 < |z| < r and every smooth phi.

**Step 5 (R is not zero).** delta := dist(y, O ∪ O')/3 > 0. Since g_t y -> O as t -> -inf and g_t y -> O' as
t -> +inf (in distance), there is T0 with dist(g_t y, O ∪ O') < delta for |t| >= T0. Shrink Dbar, Dbar' (still
contracting discs) so that g_t w is within delta of O for w in Dbar, t in [-P, 0], and similarly for Dbar'. Take n0,
n0' with n0 P, n0' P' >= T0. Let phi0 >= 0 be smooth, supported in the ball B(y, delta), with phi0(y) = 1. Then
Phi_z = 0 and Phi'_z = 0 for phi0, and phi0(g_t y) = 0 for |t| >= T0. Hence
 R_z(phi0) = int_{-n0P}^{n0'P'} e^{-zt} e^{J_t(y)} phi0(g_t y) dt,
which is entire in z and strictly positive at every real z: the integrand is >= 0 and positive near t = 0. This
contradicts Step 4. ∎

**Remarks.**
1. *Sanity check.* For the north–south flow on S^2 (not GH) the analogous family along a source-to-sink orbit is
entire, and its value at 0 is a non-constant solution of Xu = 0. Lemma M is exactly where GH enters.
2. Theorem B uses no information on the signs of int_O d or int_{O'} d, no volume, and no dimension restriction.
3. The meromorphic continuation in Step 2 is the only place where periodicity is used. It supplies the exact
self-similarity that a generic Pesin point lacks.

## 5. Consequences

**Corollary 5.1 (proved modulo [KLY]: Katok's horseshoe / closing theorem for hyperbolic measures of C^2 flows; Katok
1980 for dimension 3 and C^{1+alpha}, Lian–Young in general).** Assume GH. Then every ergodic flow-invariant
probability mu with h_mu(g_1) > 0 is non-hyperbolic. That is, besides the flow direction it has a zero Lyapunov
exponent.
*Proof.* mu is not carried by the zero set of X; otherwise g_1 = id on supp mu and h_mu = 0 (see the proof of
Theorem 4.1 in [R5-d]). By Ruelle's inequality for g_1 and g_{-1}, mu has a positive and a negative exponent. Suppose
all non-flow exponents are nonzero. [KLY] gives a horseshoe Lambda: a hyperbolic basic set, not a single orbit,
with dense hyperbolic periodic orbits. Take two distinct periodic orbits O, O' in Lambda. By local product
structure, W^u(O) ∩ W^s(O') ∩ Lambda contains a point y. The point y lies on neither orbit, since its alpha-limit is
O and its omega-limit is O'. Since W^u(O) is the union of the W^{uu}(x), x in O, and W^s(O') is the union of the
W^{ss}(x'), the data of Theorem B exist (Section 4, Existence). Theorem B gives a contradiction. ∎

**Corollary 5.2 (proved modulo the same citations).** If dim M <= 3 and X is GH, then h_top(g_1) = 0.
*Proof.* dim 1: g_1 is a circle homeomorphism (or X = 0), entropy 0. dim >= 2: by the variational principle it
suffices to show h_mu(g_1) = 0 for ergodic mu (step 2 of the chain). If dim M = 2, an ergodic mu not carried by
zeros has exponents {0 (flow), chi}, and Ruelle for g_{±1} forces h_mu = 0. If dim M = 3 and h_mu > 0, the
exponents are chi_u > 0 = 0 > chi_s, so mu is hyperbolic. This contradicts Corollary 5.1. ∎
This also removes the configuration (H3) of [R5-d] Theorem 4.1, which was the exact remaining obstruction in
dimension 3.

**Corollary 5.3.** Under GH: (PE) holds for every ergodic mu that is hyperbolic (Corollary 5.1), and also for every
ergodic mu with -chi^+ < mu(d) < 0 or 0 < mu(d) < |chi^-| (Corollary A). Moreover, X has no transverse homoclinic
orbit of any hyperbolic periodic orbit (Theorem B with O = O').

## 6. Step 2 of the chain (checked; no flaw)
- By the variational principle, h_top(g_1) = sup h_m(g_1) over g_1-invariant m.
- For g_1-invariant m, put mbar = int_0^1 (g_s)_* m ds. It is flow-invariant.
- g_s conjugates g_1 to itself, so h_{(g_s)_* m}(g_1) = h_m(g_1).
- Write mbar as an integral of measures mu_omega that are flow-ergodic (hence g_1-invariant). Refining each by its
 g_1-ergodic decomposition gives the g_1-ergodic decomposition of mbar, by uniqueness. So Jacobs' formula
 h_mbar(g_1) = int h_{mu_omega}(g_1) holds for both decompositions.
- Hence h_m(g_1) = h_mbar(g_1) <= sup over flow-ergodic mu of h_mu(g_1).
So (PE) implies the [GOAL]. Step 2 is correct.

## 7. What remains open (precisely)

By Corollaries A, 5.1 and 5.3, (PE) — and hence the problem — is reduced to the following statement. It is NOT
proved here.

**(PE-rest).** Under GH, there is no ergodic flow-invariant mu with h_mu(g_1) > 0 such that mu is non-hyperbolic
(it has a zero exponent besides the flow direction; this forces dim M >= 4) and lambda := mu(d) (the sum of the
exponents) satisfies lambda = 0, or lambda <= -chi^+, or lambda >= |chi^-|.

Notes on the two remaining sub-cases.

(R1) |lambda| >= theta (say lambda <= -chi^+ < 0). This is a sketch only, and I expect it is provable. Theorem A
needs backward cancellation at a rate > |lambda|. With k+1 points y_0 = x, y_1, ..., y_k on one unstable leaf, all
forward-generic (available by the non-atomic conditionals), and weights w_i, the combination
sum_i w_i e^{J_t(y_i)} phi(g_t y_i) decays backward like e^{-k theta |t|} times e^{J_t(x)}, provided:
- the leaf maps g_{-t} are written in normal-form coordinates along the leaf, in which they are polynomial maps of
 bounded degree; these are nonstationary normal forms for non-uniform contractions (Kalinin–Sadovskaya, cited from
 memory, not checked);
- the weights solve a moment (Vandermonde-type) system in those coordinates.
In 1-dimensional leaves an affine structure suffices and the weights are divided-difference weights. Then
Theorem A, with kappa < k theta, applies verbatim and Lemma M finishes. Two points are not checked: tempered bounds
on the normal-form charts, and the possibility that the generic points y_i lie on an algebraic subvariety of the
leaf, which would degenerate the moment system.

(R2) lambda = 0, non-hyperbolic, positive entropy. Here supp mu = M (Corollary D1). The obstruction is genuine:
- for generic pairs the eigen-family T_z lives only on the strip 0 < Re z < theta;
- its forward part diverges as z -> 0+ (Patterson behaviour: normalised, it converges to nu-hat, by the one-sided
 version of Lemma D);
- so Lemma M cannot be applied at 0.
Theorem B circumvents this only when exact self-similarity (periodic orbits) gives meromorphic continuation across
Re z = 0. Non-hyperbolic positive-entropy measures need not have periodic orbits nearby: there are C^inf minimal
flows with positive entropy. A forward cancellation by a "quadrilateral" of four points (pairwise backward and
forward asymptotic) would also give a family holomorphic across 0. But it needs the Jacobian-cycle constant and the
temporal-distance constant of the quadrilateral to vanish simultaneously, and I could not produce such
configurations.
This sub-case contains the old core #16 and the volume-preserving case (C) of R4-q10.

=== END OF ANSWER round6_q10 ===
