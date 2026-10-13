# round12_q7: answer

## Plan / statement attempted
Target: (PE0), by the Liouville/quasimode route of the brief, i.e. by contradicting the a priori estimate of GH
(primal: smooth u_n with ||u_n - c(u_n)|| = 1 in a fixed norm and Xu_n -> 0 in C^inf; dual: T_n -> 0 in (C^k)' with
T_n(1) = 0 and all primitives S_n (S_n o X = T_n) bounded below).

Verdict (proved below): **the route cannot succeed as proposed.** I prove an obstruction (option (3) of the task):
there are smooth flows with every hypothesis of (PE0) except GH, with every known GH-constraint on mu listed in the
brief (zero mean divergence, non-hyperbolic with zero transverse exponents, full support, dim M >= 4, Pesin leaves,
recurrence, J_t = o(|t|)), and for which the a priori estimate holds (C^1 level, all orders <= 1, and its dual). So no
Liouville sequence (in any fixed norm of order <= 1) and no dual sequence of order <= 1 can be manufactured from a
positive-entropy measure with zero mean divergence. A proof of (PE0) must use the *distributional* half of GH (L1,
uniqueness of invariant distributions, Theorem J-type statements), not the estimate. (PE0) itself remains open.

(Stage log: Stage 1 read the brief; Stage 2 below.)

Conventions. M compact connected, Riemannian; C^k norms with respect to fixed charts/metric; c(u) = mean of u with
respect to a fixed smooth positive density. "Estimate E(k,m)" means: there is C with
 ||u - c(u)||_{C^k} <= C ||Xu||_{C^m} for all u in C^inf(M).        (E(k,m))
Under GH, for every k there is m with E(k,m) (Text B, Lemma 2).

## 1. Both sides of the route are exactly the negation of the estimate

**Lemma 1 (proved).** Fix k, m. The following are equivalent:
(a) E(k,m) holds;
(b) every T in (C^k)' with T(1) = 0 has a primitive S in (C^m)' (S(X phi) = T(phi) for all smooth phi) with
 ||S||_{(C^m)'} <= C ||T||_{(C^k)'}, C independent of T.
In particular: a primal Liouville sequence normalised in C^k (smooth u_n, ||u_n - c(u_n)||_{C^k} = 1,
||Xu_n||_{C^m} -> 0) exists iff E(k,m) fails, iff a dual sequence (T_n(1) = 0, ||T_n||_{(C^k)'} -> 0, every primitive of
T_n of (C^m)'-norm >= 1) exists.

*Proof.* (a) => (b): define S_0 on the subspace X(C^inf) of C^m by S_0(Xu) := T(u). It is well defined: if Xu = Xu'
then by (a) u - u' is constant, and T kills constants. It is bounded: |S_0(Xu)| = |T(u - c(u))| <=
||T|| ||u - c(u)||_{C^k} <= C||T|| ||Xu||_{C^m}. Hahn–Banach extends it to C^m with the same norm.
(b) => (a): for smooth u, dist_{C^k}(u, R1) =
sup{|T(u)| : T in (C^k)', T(1) = 0, ||T|| <= 1} (Hahn–Banach on the quotient C^k/R1), and |T(u)| = |S(Xu)| <=
C||Xu||_{C^m}. Finally ||u - c(u)||_{C^k} <= (1 + ||c||_{(C^k)'}·||1||_{C^k}) dist_{C^k}(u, R1), since
u - c(u) = (u - a) - c(u - a) for every constant a. ∎

(Negative orders and L^2 are dominated by C^0, so E(0,m) excludes Liouville sequences normalised in L^2 or in any
H^{-s}; E(1,m) excludes those normalised in C^1, hence in H^1 or any H^r, r <= 1. Finite configurations of point masses,
and differences/averages of them, are order 0, so E(1,m) and Lemma 1 exclude dual sequences built from them, measured in
(C^1)'.)

## 2. Anosov flows satisfy E(1,1)

**Theorem A (proved; uses only the definition of an Anosov flow).** Let Y be a C^2 Anosov vector field on a compact
connected manifold N, with splitting TN = E^s + RY + E^u, |Dphi_t v| <= C e^{-theta t}|v| (v in E^s, t >= 0),
|Dphi_{-t} v| <= C e^{-theta t}|v| (v in E^u, t >= 0). Then for every u in C^inf(N) (complex valued allowed), every real
beta and f := Yu + i beta u:
 (i) |du_x(v)| <= (C/theta)||df||_inf |v| for v in E^s_x or E^u_x;
 (ii) du(Y) = f - i beta u;
 (iii) hence ||du||_inf <= K(||f||_{C^1} + |beta| ||u||_inf), K depending only on the flow;
 (iv) for beta = 0: ||u - c(u)||_{C^1} <= K'||Yu||_{C^1}, i.e. E(1,1) holds for Y.

*Proof.* d/dt[e^{i beta t} u(phi_t x)] = e^{i beta t} f(phi_t x), so for every real T
 u(x) = e^{i beta T} u(phi_T x) - int_0^T e^{i beta t} f(phi_t x) dt.          (2.1)
Differentiate (2.1) in x in the direction v in E^s_x (everything is C^1 in x):
du_x(v) = e^{i beta T} du_{phi_T x}(Dphi_T v) - int_0^T e^{i beta t} df_{phi_t x}(Dphi_t v) dt. The first term is
<= ||du||_inf C e^{-theta T}|v| -> 0 as T -> +inf, and the integral is bounded by ||df||_inf C|v|/theta. For v in E^u use
T -> -inf. (ii) is the equation itself. (iii): the splitting is continuous on the compact N and Y has no zeros, so
v = v_s + aY + v_u with |v_s| + |a| + |v_u| <= K_0|v|. (iv): with beta = 0, (iii) gives ||du||_inf <= K||Yu||_{C^1};
then |u(x) - u(y)| <= diam(N)||du||_inf (N connected), and c(u) is an average of values of u, so
||u - c(u)||_inf <= diam(N)||du||_inf. ∎

Remark. By the smooth Livsic regularity theorem (de la Llave–Marco–Moriyón 1986, Journé 1988; cited from memory: a
continuous solution of the cohomological equation over a transitive C^inf Anosov flow with C^inf data is C^inf) the image
X(C^inf) = {f : all periodic orbit integrals of f vanish} is closed in C^inf, and the open mapping theorem for Fréchet
spaces then gives E(k, m(k)) for all k. I use only the elementary E(1,1).

In particular the geodesic flow of a closed hyperbolic surface (N = unit tangent bundle, Liouville measure nu_N) gives a
volume-preserving flow, d = 0, with a g_1-ergodic (indeed mixing) measure of positive entropy, satisfying E(1,1). This
already kills the route for *hyperbolic* measures; but under GH such measures are excluded anyway (R6-a Theorem 5.1), so
the brief's known constraints must also be matched. That is done next.

## 3. A non-hyperbolic example: Anosov x Diophantine translation satisfies E(1,q)

**Setting.** N, Y, phi_t as in Section 2, with Y preserving a smooth probability nu_N for which phi_1 is weakly mixing
(e.g. the geodesic flow of a closed hyperbolic surface with Liouville measure: mixing, cited classical: Hopf/Hedlund).
Fix a periodic point p of phi_t with minimal period P (Anosov flows have periodic orbits; cited: closing lemma). Let
m >= 1, M = N x T^m, and X = Y + sum_j alpha_j d/dtheta_j, so g_t(x, theta) = (phi_t x, theta + t alpha). Choose
alpha in R^m with
 (D1) k.alpha not in Z for all k in Z^m \ {0} (so the rotation R_alpha of T^m is ergodic);
 (D2) ||k.(P alpha)||_{R/Z} >= c |k|^{-tau} for all k != 0, for some c > 0 and tau > m.
Lebesgue-a.e. alpha satisfies both. (D1: countably many hyperplanes. D2: for fixed k != 0 the set of alpha in [0,1]^m
with ||P k.alpha|| < eps := c|k|^{-tau} has measure <= 2(1 + 1/P) eps: pick j with k_j != 0 and use Fubini in alpha_j;
for fixed other coordinates alpha_j -> a + P k_j alpha_j is affine with slope of modulus |P k_j| >= P, so on [0,1] it
meets the eps-neighbourhood of Z in at most |P k_j| + 1 intervals of length 2 eps/|P k_j| each; summing over k the
measure of the set of alpha in [0,1]^m violating D2 for the constant c is <= 2(1 + 1/P) c sum_k |k|^{-tau} = O(c)
(tau > m), which tends to 0 with
c; so a.e. alpha satisfies D2 for some c > 0.)

**Facts about mu := nu_N x Haar (all elementary or classical).**
- X preserves the smooth volume nu_N x d theta, so with this density d = div X = 0, J_t = 0 and int J_1 dmu = 0.
- mu is g_1-ergodic: g_1 = phi_1 x R_alpha, a weakly mixing map times an ergodic map (cited classical: the product of a
  weakly mixing and an ergodic transformation is ergodic).
- h_mu(g_1) = h_{nu_N}(phi_1) + h_{Haar}(R_alpha) = h_{nu_N}(phi_1) > 0 (entropy of a product; rotation has entropy 0;
  for the hyperbolic geodesic flow h = 1 by Pesin's formula, cited).
- Lyapunov exponents of mu for g_1: +1, -1 (on E^u, E^s, for curvature -1), 0 (flow), and 0 with multiplicity m (torus
  directions, on which Dg_1 is the identity). So mu is non-hyperbolic, with a zero transverse exponent.
- supp mu = M, dim M = 3 + m >= 4, mu is flow-invariant (mu-bar = mu), recurrent; Pesin unstable leaves are
  W^{uu}(x) x {theta}, on which the planner's configurations S and primitives Q make sense.
- X is NOT GH: for the periodic orbit gamma of p, the measure mu_gamma x Haar is flow-invariant and singular, and since
  d = 0 the distribution u = (mu_gamma x Haar)/(nu_N x d theta) satisfies Xu = 0 (Observation 0), u not constant;
  this contradicts L1. So the example respects everything in the brief except GH and its distributional consequences.

**Theorem B (proved).** With q = 2j + 1 for any integer j with 2j > tau + m + 1, X satisfies E(1, q):
 ||u - c(u)||_{C^1(M)} <= C ||Xu||_{C^q(M)} for all u in C^inf(M).
Consequently (Lemma 1) every order-<=1 distribution T with T(1) = 0 has a primitive S in (C^q)' with
||S|| <= C||T||_{(C^1)'}; no primal Liouville sequence normalised in C^1, L^2 or any H^{-s} exists; no dual sequence
of order <= 1 exists.

*Proof.* Let u be smooth, f = Xu. Expand in Fourier series in theta: u = sum_k u_k(x) e_k(theta), e_k = e^{2 pi i k.theta},
u_k in C^inf(N), and f_k = Y u_k + i beta_k u_k, beta_k = 2 pi k.alpha. The series converge absolutely in every C^r.
1. *k = 0.* Y u_0 = f_0 and c(u) = c(u_0) (mean w.r.t. nu_N x d theta). By Theorem A(iv),
 ||u_0 - c(u_0)||_{C^1} <= K'||f_0||_{C^1} <= K'||f||_{C^1}.
2. *Oscillation of |u_k|.* From (2.1) with beta = beta_k: |u_k(phi_s x)| <= |u_k(x)| + |s| ||f_k||_inf for all real s
 (take T = s and moduli; |e^{i beta T}| = 1). From Theorem A(i), integrating along a C^1 curve inside a local strong
 stable (or strong unstable) leaf, tangent to E^s (resp. E^u): |u_k(x) - u_k(y)| <= (C/theta)||f_k||_{C^1} l, l the
 leaf length. Local product structure of Anosov flows (cited, standard): there are delta_0, C_0 such that for
 d(x,z) < delta_0 there are y_1 in W^{ss}_loc(x), |s| <= C_0 d(x,z), y_2 = phi_s y_1 and z in W^{uu}_loc(y_2), with leaf
 lengths <= C_0 d(x,z). Hence ||u_k(z)| - |u_k(x)|| <= C_2 ||f_k||_{C^1} d(x,z) whenever d(x,z) < delta_0. N is compact and
 connected, so there is N_0 such that any two points are joined by a chain of at most N_0 points with consecutive
 distances < delta_0 (cover N by finitely many delta_0/2-balls; the nerve is connected). Therefore
 osc_N |u_k| <= N_0 C_2 delta_0 ||f_k||_{C^1} =: C_3 ||f_k||_{C^1}.
3. *Value at the periodic point.* (2.1) with x = p, T = P: (1 - e^{i beta_k P}) u_k(p) = - int_0^P e^{i beta_k t} f_k(phi_t p) dt.
 |1 - e^{iy}| = 2|sin(y/2)| >= (2/pi) dist(y, 2 pi Z), and dist(beta_k P, 2 pi Z) = 2 pi ||k.(P alpha)|| >= 2 pi c|k|^{-tau}
 by (D2). So |u_k(p)| <= (P/(4c)) |k|^tau ||f_k||_inf for k != 0.
4. Hence ||u_k||_inf <= |u_k(p)| + osc|u_k| <= C_4 |k|^tau ||f_k||_{C^1}, and by Theorem A(iii)
 ||du_k||_inf <= K(||f_k||_{C^1} + 2 pi |k||alpha| ||u_k||_inf) <= C_5 |k|^{tau+1} ||f_k||_{C^1}.
5. *Summation.* ||u_k e_k||_{C^1(M)} <= C(||u_k||_inf + ||du_k||_inf + |k| ||u_k||_inf) <= C_6 |k|^{tau+1}||f_k||_{C^1}.
 Integrating by parts j times with the flat Laplacian Delta_theta: f_k = (-4 pi^2 |k|^2)^{-j} (Delta_theta^j f)_k, so
 ||f_k||_{C^1(N)} <= (4 pi^2 |k|^2)^{-j} ||Delta_theta^j f||_{C^1(M)} <= C_7 |k|^{-2j} ||f||_{C^{2j+1}(M)}.
 So ||u - c(u)||_{C^1} <= K'||f||_{C^1} + C_6 C_7 sum_{k != 0} |k|^{tau + 1 - 2j} ||f||_{C^{2j+1}}, and the sum
 converges because 2j - tau - 1 > m. ∎

## 4. The obstruction (consequence of Sections 1-3)

**Corollary O (proved).** Let (M, X, mu) be as in Section 3. Then:
(a) mu is a g_1-ergodic probability with h_mu(g_1) > 0 and int J_1 dmu = 0; it is non-hyperbolic (zero exponents
transverse to X), has full support, dim M >= 4; it has Pesin unstable leaves, recurrence, and J_t = 0 = o(|t|).
(b) X satisfies the a priori estimate E(1,q) and its dual (Lemma 1).
Hence any argument which derives a contradiction from "(a) + the a priori estimate of GH (in C^1, L^2, negative
Sobolev norms) or its dual for distributions of order <= 1" is invalid. In particular:
- the primal side (2) of the brief cannot produce smooth u_n with ||u_n - c(u_n)||_{L^2} = 1 (or C^1, or H^{-s}) and
  Xu_n -> 0 in C^q, by any construction (smoothed Birkhoff averages, conditional expectations along unstable leaves,
  centre-direction smoothing, ...) that uses only the properties in (a): such u_n do not exist in the example;
- the dual side (1) cannot produce point configurations T_n (order 0) with ||T_n||_{(C^1)'} -> 0 and all primitives of
  size >= 1 in (C^q)': in the example every such T has a primitive with ||S||_{(C^q)'} <= C||T||_{(C^1)'}, and the
  explicit weighted primitives Q(phi) = int_{-inf}^0 S(phi o g_t) dt of unstable-leaf configurations are among the
  (non-unique) primitives.
The only remaining freedom is to violate the estimate at high regularity (normalisation in C^k, k >= 2). For the Anosov
case this is excluded as well by the cited smooth Livsic theory (Remark in Section 2); for the product example I did not
prove E(k, m) for k >= 2 (it should follow from the same Fourier argument plus leafwise higher-order bounds and
Journé's lemma, but this is a sketch). In any case nothing in the planner's constructions is of high order.

**What a proof must use instead.** The example violates GH only through its distributional half: it has non-constant
invariant distributions (L1 fails). This is exact in the volume case:

**Proposition C (proved).** Let X preserve a smooth positive density omega (d = 0). Then X is GH iff
(i) the a priori estimate holds (for every k some m with E(k,m)), and
(ii) every X-invariant distribution density (L_X T = 0) is a constant multiple of omega.
*Proof.* GH => (i): Text B Lemma 2. GH => (ii): T/omega =: u satisfies Xu = 0 (d = 0, Observation 0), so u is constant
by L1. Conversely assume (i), (ii). By (i), X(C^inf) is closed (Text B Corollary 3, whose proof uses only the estimate),
so by Hahn–Banach it is the annihilator of the invariant distribution densities (Text A, duality consequence; its proof
uses only closedness), i.e. by (ii) X(C^inf) = {f : int f omega = 0}. Let u in D' with Xu = f smooth. Then
int f omega = <Xu, omega> = -<u, L_X omega> = 0 (pairing via omega; L_X omega = 0). So f = Xv with v smooth, and
X(u - v) = 0, i.e. (u - v)omega is an invariant distribution density, hence a multiple of omega by (ii): u - v is
constant, u is smooth. ∎

So in the volume case, (PE0) is equivalent to: **a smooth volume-preserving flow with h_top > 0 cannot satisfy both
(i) and (ii).** Corollary O shows that the C^1-level part of (i) together with positive entropy (even with all the
measure-theoretic constraints the brief derived from GH) is consistent, and for Anosov flows the full (i) holds (cited
smooth Livsic theory); hence (ii) — distributional unique ergodicity — must enter any
proof in an essential way. The quasimode route uses only (i), which is why it cannot close. (Note (ii) implies unique
ergodicity, and with (ii) the constraint "h_top > 0" becomes "h_omega > 0" by the variational principle; the product
example has many invariant measures mu_gamma x Haar, so it does not tell whether (i) + unique ergodicity + positive
entropy is consistent — that is a sharper form of the open question.)

## 5. Remarks on the specific mechanisms proposed in the brief
- Dual side, "differences of S at well-chosen times / Birkhoff averages along the orbit of a configuration": all such
  T_n are order-0 measures with T_n(1) = 0; in the example their primitives obey ||S_n||_{(C^q)'} <= C||T_n||_{(C^1)'}.
  The brief's volume-case formulation ("ergodic-integral differences int_0^tau (phi(g_s a) - phi(g_s b)) ds of order one
  while all C^k test quantities of the endpoints are small") is likewise impossible in the example for every
  phi = Xu in X(C^inf): the difference equals [u(g_tau a) - u(g_tau b)] - [u(a) - u(b)], and Theorem B gives
  ||du||_inf <= C||phi||_{C^q}, so it is <= C||phi||_{C^q}(d(g_tau a, g_tau b) + d(a,b)), uniformly in tau. (In the
  example X(C^inf) has infinite codimension, so for phi outside it ergodic integrals can differ; but those phi are
  invisible to the estimate, which is the only thing the route attacks.)
- Primal side, the derivative-growth problem identified in the brief (Bowen-ball functions have C^m norms e^{m Lip L}
  against frequencies e^{-hL}) is not a technical defect: Corollary O shows no construction from the measure alone can
  beat it, because in the example the estimate holds with loss of only q derivatives.
- Heuristic (not a theorem): an almost-invariant function (||Xu||_{C^0} = eps) is constant up to T eps along orbit
  segments of length T; if such segments are delta(T)-dense, u must have gradient >= 1/delta(1/eps) to be non-constant,
  and then ||Xu||_{C^k} is large for big k unless delta decays slowly in T. Fast orbit equidistribution (as produced by
  hyperbolicity) therefore works *against* quasimodes; quasimodes are a Liouville (slow equidistribution) phenomenon,
  the opposite regime to positive entropy.

## 6. Summary: proved / sketched / open
**Proved.**
- Lemma 1: the primal (Liouville sequence) and dual (small T, large primitives) sides of the route are both equivalent
  to the failure of an estimate E(k,m).
- Theorem A: every C^2 Anosov flow on a compact connected manifold satisfies E(1,1) (elementary, no Livsic theory).
- Theorem B: Anosov (with weakly mixing volume, e.g. hyperbolic geodesic flow) x Diophantine translation on T^m
  satisfies E(1, q), q = 2j+1, 2j > tau + m + 1; the measure mu = Liouville x Haar is g_1-ergodic, h_mu > 0,
  int J_1 dmu = 0, non-hyperbolic, full support, dim >= 4 — i.e. it meets every hypothesis of (PE0) except GH and every
  GH-constraint on mu recorded in the brief.
- Corollary O: hence the Liouville/quasimode route, primal or dual, at regularity <= 1 (L^2, H^{-s}, C^1 normalisations;
  configurations of point masses), cannot prove (PE0).
- Proposition C: in the volume case GH <=> (a priori estimate) + (every invariant distribution density is c omega); so
  the volume case of (PE0) is: positive entropy is incompatible with this pair, and the second (distributional) condition
  must be used.
(Cited, from memory: local product structure and existence of periodic orbits for Anosov flows; mixing of hyperbolic
geodesic flows; ergodicity of weakly mixing x ergodic; entropy of products; Pesin's formula for h > 0 of the geodesic
flow.)
**Sketched / cited only.** E(k,m) for all k for Anosov flows (smooth Livsic regularity, de la Llave–Marco–Moriyón,
Journé); E(k,m) for k >= 2 for the product example (not proved).
**Open.** (PE0) itself, hence the problem in dim >= 4. Sharpened open questions:
- (Q-a) Is there a smooth uniquely ergodic (or distributionally uniquely ergodic) volume-preserving flow with positive
  entropy satisfying the a priori estimate? A "no" answer is exactly the volume case of (PE0).
- (Q-b) Can positive entropy of omega produce a second invariant distribution density (of any finite order) for a
  volume-preserving flow with closed range? (Theorem J of R6-a is the only tool so far using condition (ii)/L1.)

=== END OF ANSWER round12_q7 ===
