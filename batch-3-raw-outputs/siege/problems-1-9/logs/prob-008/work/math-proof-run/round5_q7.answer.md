# round5_q7 — attempt on (Lambda) / zero entropy under GH

## Plan (stage 1)
Target: (Lambda), or zero topological entropy directly, under GH (no volume).
Route: (i) record what can be proved without (Lambda): new GH consequences (no wandering points, ...);
(ii) analyse what the Pesin/unstable-structure approach can and cannot produce: which non-smooth u with
Xu smooth can be manufactured, and where it fails; (iii) settle low dimensions / special cases rigorously.
Results are appended below as they are obtained.

Conventions as in the brief: nu smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds,
"L1" = (ker X on D' = constants), Lemma C (int_R e^{J_t(x)} dt = infinity for every x, dim >= 2),
Corollary D1 (ergodic mu with mu(d) = 0 has full support).

## 1. Step 2 of the chain is correct; what exactly (Lambda) is needed for
Step 2 is fine: for a Lipschitz map f of a compact n-manifold, h_top(f) <= n log^+ Lip(f) (classical, cited
from memory), and h_top(g_T) = |T| h_top(g_1). Hence h_top(g_1) <= (n/T) log^+ max_x ||Dg_T(x)|| for
every T > 0, and (Lambda) gives h_top = 0.
Remark. (Lambda) is equivalent (Oseledets + the standard identity
lambda* = max over ergodic mu of the top exponent of mu, proved by taking weak* limits of empirical measures
on the unit sphere bundle) to: no invariant probability has a positive exponent. By the variational principle
and Ruelle's inequality, zero entropy needs only: no invariant probability of POSITIVE ENTROPY has a positive
exponent; since positive entropy forces a positive exponent (Ruelle), zero entropy <=> no ergodic mu with
h_mu > 0. So (Lambda) is formally stronger than the problem, but every route to zero entropy known to me
goes through the measures with positive exponents anyway; I keep both targets in view below.

## 2. A correction to the planner's sketch, step (c): the curve-current route only works for n = 2
Claim (proved). Let n = dim M >= 3. In step (b) the limit C is a 1-current (a continuous functional on
smooth 1-forms) with C(df) = 0 for all f (closed) and C(L_X beta) = s0 C(beta). As the sketch says, this forces
C(beta) = 0 for closed beta (L_X beta = d i_X beta for closed beta, and C(d .) = 0). But a closed 1-current
that annihilates closed 1-forms is, by de Rham's theorem for currents (cited), a BOUNDARY C = dR of a
2-dimensional current R, i.e. C(beta) = R(d beta), where R is an (n-2)-form with distribution coefficients.
It is of the form "C = dW with W a generalized function" only when n - 2 = 0, i.e. n = 2.
Precisely: a k-dimensional current on M^n is an (n-k)-form with distributional coefficients, and generalized
functions are the n-dimensional currents. The eigen-relation then reads: L_X R - s0 R (or + s0 R, with the
sign conventions) is a CLOSED 2-dimensional current, an (n-2)-form-valued distribution — not a scalar
equation XW = kappa W. GH is a statement about functions (0-forms); its extension to currents is known only
for closed 1-forms (Lemma B of [R4-q10], whose proof uses that the primitive of an exact 1-form is a
function). So for n >= 3 the route (a)-(d) does not even reach the statement (E1); it reaches an
eigen-problem for (n-2)-currents on which GH gives no information. For n = 2 the conclusion (h_top = 0) is
true for all flows anyway (L.-S. Young, flows on surfaces have zero topological entropy; cited).
Equivalent bookkeeping: via contraction with nu, 1-currents C correspond to distributional vector fields V
(C(beta) = <beta(V), nu>), C closed <=> div_nu V = 0 in D'. The curve currents thus produce divergence-free
distributional vector fields V with [X, V] + (twist by d) = -s0 V, i.e. eigen-objects for the action of
the flow on vector fields, never on functions.
(Check of the twist: L_X(i_V nu) = i_{[X,V]} nu + i_V L_X nu = i_{[X,V] + dV} nu.)

## 3. The top eigenmeasure on SM (no volume needed) and why it gives no contradiction by itself
Notation: SM unit sphere bundle, A_t(v) = log|Dg_t v|, ghat_t v = Dg_t v/|Dg_t v|, L_t Psi(v) = e^{A_t(v)} Psi(ghat_t v)
(positive operators on C(SM), L_t L_s = L_{t+s}), lambda* = lim (1/t) log max_x ||Dg_t(x)|| = inf_t (1/t) log max ||Dg_t||.

Lemma 3.1 (proved). There is a positive Borel measure S' != 0 on SM with L_s^* S' = e^{lambda* s} S' for all s >= 0.
Proof. Put L = L_1, r = e^{lambda*}. Since ||L^n||_{C->C} = ||L^n 1||_inf = max_v e^{A_n(v)} = max_x ||Dg_n(x)||,
the spectral radius of L is r, and by subadditivity max_v e^{A_n(v)} >= r^n for every n.
(a) For rho > r put R_rho = sum_{n>=0} rho^{-n-1} L^n (positive, norm-convergent). Claim: sup_{rho > r} ||R_rho 1||_inf = infinity.
If not, ||R_rho 1|| <= B for all rho > r, and by monotone convergence G := sum_n r^{-n-1} e^{A_n} <= B pointwise; in particular
e^{A_n(v)} <= B r^{n+1} for all n, v. Fix N, pick v_N with e^{A_N(v_N)} >= r^N. For n <= N the cocycle identity gives
A_N(v_N) = A_n(v_N) + A_{N-n}(ghat_n v_N) <= A_n(v_N) + log(B r^{N-n+1}), so e^{A_n(v_N)} >= r^{n-1}/B and
G(v_N) >= (N+1)/(B r^2), contradicting G <= B for N large.
(b) Take rho_j decreasing to r with c_j := ||R_{rho_j} 1|| -> infinity, w_j a maximum point of R_{rho_j} 1, and the
probabilities m_j := R_{rho_j}^* delta_{w_j} / c_j. From L R_rho = rho R_rho - I: L^* m_j = rho_j m_j - delta_{w_j}/c_j.
L^* is weak*-continuous (L maps C(SM) to itself), so a weak* limit point S of (m_j) is a probability with L^* S = r S.
(c) S' := int_0^1 e^{-lambda* t} L_t^* S dt. Using L_{t'}^* S = e^{lambda*} L_{t'-1}^* S for t' in [1, 2] one checks
L_s^* S' = e^{lambda* s} S' for s in [0,1], hence for all s >= 0; S' >= 0 and S'(1) > 0. QED

Consequences (proved). T(beta) := int beta(v) dS'(v) (beta a smooth 1-form, beta(v) evaluated on unit vectors) is a
1-current of order 0 with T(g_t^* beta) = e^{lambda* t} T(beta); its boundary tau(phi) := T(dphi) is a distribution
density of order 1 with tau(phi o g_t) = e^{lambda* t} tau(phi), tau(X phi) = lambda* tau(phi), tau(1) = 0.

Lemma 3.2 (the borderline; proved). Let tau be a distribution density of order k (|tau(phi)| <= K ||phi||_{C^k}) with
tau(X phi) = kappa tau(phi) for all smooth phi. (i) tau(phi o g_t) = e^{kappa t} tau(phi) for all real t.
(ii) If k = 0 and kappa != 0, then tau = 0. (iii) If k >= 1 and kappa > k lambda*, then tau = 0; likewise if
kappa < -k lambda*_-, where lambda*_- is the exponent of -X.
Proof. (i) F(t) = tau(phi o g_t) is differentiable with F' = tau((X phi) o g_t) = tau(X(phi o g_t)) = kappa F
(difference quotients of phi o g_t converge in every C^k). (ii) |F(t)| <= K ||phi||_inf for all t, so e^{kappa t}
is bounded on R unless tau(phi) = 0. (iii) Standard jet estimate (induction on j with the variational equations
and Duhamel's formula): for every eps > 0, ||D^j g_t|| <= C_{j,eps} e^{j(lambda* + eps) t}, t >= 0, j >= 1; hence
||phi o g_t||_{C^k} <= C e^{k(lambda* + eps) t} and |tau(phi)| = e^{-kappa t}|tau(phi o g_t)| -> 0. QED

So the eigen-distribution tau built from the top exponent sits EXACTLY on the borderline kappa = lambda*, k = 1 of
Lemma 3.2: growth considerations alone can never kill it, and to obtain a contradiction from it one needs both
(N) tau != 0 (fails e.g. when S' is invariant under v -> -v, which happens whenever the top Oseledets direction is
only defined up to sign and S' is symmetrised; by Lemma 3.1 S' can be replaced by its symmetrisation, so (N)
is a genuine choice problem), and
(E1') GH excludes nonzero distribution densities tau with tau o X = kappa tau, kappa real nonzero.
Note: (E1') is about the transposed operator without d-twist; in the function picture u = tau/nu it reads
(X + d + kappa) u = 0, i.e. it concerns P + kappa with P = X + d (Lemma F), not X. Under (V) the two coincide.
I found no way to derive (E1') from GH; see Section 6.

## 4. Dimension 3: reduction to one configuration (proved, modulo cited classical theorems)
Cited from memory (no GH involved):
 [Rue] Ruelle's inequality: for a C^1 diffeomorphism f of a compact manifold and ergodic mu,
   h_mu(f) <= sum of positive Lyapunov exponents of mu.
 [KLY] Katok's horseshoe theorem, flow version (Katok 1980 for diffeomorphisms; Lian-Young, J. AMS 2012, for C^2 flows):
   if mu is an ergodic invariant probability of a C^2 flow, mu is not supported on a zero of X, all exponents of mu
   other than the flow direction are nonzero, and h_mu > 0, then there is a compact invariant hyperbolic set Lambda
   on which the flow is topologically conjugate to a suspension of a transitive subshift of finite type of positive
   entropy (a "horseshoe"); Lambda is locally maximal and transitive, its periodic orbits are dense in it, and
   its cross-sections are Cantor sets, so Lambda != M.
 [HYP] For a hyperbolic basic set of a flow: stable manifold theorem (W^s(O) of a periodic orbit O in Lambda is the
   union of the strong stable leaves W^ss(y), y in O, and d(g_t x, g_t y) <= C e^{-ct} for x in W^ss(y)); any two
   periodic orbits O, O' of Lambda satisfy W^u(O) cap W^s(O') != empty (in the symbolic model take a point whose past
   code is that of O and whose future code is that of O'); periodic orbit measures are weak*-dense in the invariant
   probabilities on Lambda (Sigmund).

Proposition 4.0 (heteroclinic part of Corollary C1, now with full proof). Assume GH, dim M >= 2. Let O1, O2 be
hyperbolic periodic orbits (periods P1, P2) with I1 := int_0^{P1} d(g_s p1) ds > 0 and I2 := int_0^{P2} d(g_s p2) ds < 0.
Then W^u(O1) cap W^s(O2) is empty.
Proof. Let x be in the intersection; x is not a zero, and not periodic (its alpha- and omega-limit sets are the
disjoint orbits O1, O2). Choose y2 in O2 with x in W^ss(y2), so d(g_t x, g_t y2) <= C e^{-ct} for t >= 0; then
|J_t(x) - J_t(y2)| <= Lip(d) C / c for t >= 0, while J_t(y2) = (t/P2) I2 + O(1). So J_t(x) <= b - a t for t >= 0, some a > 0.
Symmetrically, x is in the strong unstable leaf of some y1 in O1, d(g_t x, g_t y1) <= C e^{ct} for t <= 0, and
J_t(y1) = (t/P1) I1 + O(1) for t <= 0 (note J_t = -int_t^0 d o g_s for t < 0), so J_t(x) <= b + a t = b - a|t| for t <= 0.
Hence int_R e^{J_t(x)} dt < infinity, contradicting Lemma C. QED

Theorem 4.1 (proved, modulo [Rue], [KLY], [HYP]). Assume GH, dim M = 3, and h_top(g_1) > 0. Then, after replacing X
by -X if necessary (GH is preserved, (O4)), there are a horseshoe Lambda != M as in [KLY] and a > 0, b such that
 (i) every periodic orbit O in Lambda has int_O d < 0;
 (ii) mu(d) <= -a for every invariant probability mu carried by Lambda; equivalently J_t(x) <= b - (a/2) t for all
     x in Lambda, t >= 0 (Lambda is uniformly volume-contracting);
 (iii) Lambda is not an attractor and its stable set W^s(Lambda) is nu-null;
 (iv) X has periodic orbits; the flow is neither minimal nor uniquely ergodic.
Proof. By the variational principle there is an ergodic mu with h_mu(g_1) > 0. mu gives no mass to the zero set Z
of X (Z is invariant and closed; if mu(Z) > 0 then mu(Z) = 1 and g_1 = id on supp mu, so h_mu = 0). For mu-a.e. x the
exponent in the flow direction is 0 (|Dg_t X(x)| = |X(g_t x)|, and by Poincare recurrence X(g_t x) returns near
X(x) != 0 along a sequence t -> infinity). By [Rue] for g_1 and for g_{-1}, mu has a positive and a negative exponent;
in dimension 3 the exponents are therefore lambda_1 > 0 = lambda_2 > lambda_3, so [KLY] applies and gives Lambda != M.
By [HYP], any two periodic orbits of Lambda are heteroclinically related in both orders, so by Proposition 4.0 and
Observation P (no periodic orbit with int_O d = 0) all int_O d (O in Lambda) have the same strict sign; changing
X to -X changes every int_O d to its negative, so we may assume (i). By Sigmund's density, mu(d) <= 0 for every
invariant mu on Lambda. The maximum of mu -> mu(d) on the compact convex set of invariant probabilities on Lambda is
attained at an extreme point mu0, which is ergodic. If mu0(d) = 0, Corollary D1 gives supp mu0 = M, impossible since
supp mu0 is contained in Lambda != M. So max = -a < 0, and the standard identity
limsup_{t -> inf} max_{x in Lambda} J_t(x)/t = max_{mu on Lambda} mu(d) (weak* limits of empirical measures, as in
Prop. 2.1 of [R4-q7]) gives (ii). (iii): B3 of [R4-q4] (the basin of a proper closed invariant set is nu-null), and
an attractor has a basin with nonempty interior. (iv): Lambda contains periodic orbits; dim M = 3 > 1. QED

Corollary 4.2 (proved, modulo the same citations). Under GH with dim M <= 3, if the flow has no periodic orbit —
in particular if it is uniquely ergodic (Lemma E: then it is minimal) — then h_top(g_1) = 0.
(dim 1: trivial; dim 2: Young's theorem; dim 3: Theorem 4.1(iv).)

Corollary 4.3 (any dimension; proved modulo citations). Assume GH. If mu is an ergodic invariant probability with
h_mu > 0 whose exponents are all nonzero except the flow direction, then the conclusions (i)-(iii) of Theorem 4.1
hold for a horseshoe Lambda (for X or -X). In particular, if GH holds and the flow is uniquely ergodic with
invariant measure mu, then h_top = h_mu and either h_top = 0 or mu is NON-hyperbolic with h_mu > 0, which needs
dim M >= 4 (one positive, one negative, the flow-direction zero, and one more zero exponent).
Proof. Same as Theorem 4.1, using [KLY] directly (hyperbolicity is now assumed). Under unique ergodicity a
horseshoe would carry many invariant measures, so a positive-entropy mu must be non-hyperbolic. QED

So in dimension 3 the problem reduces EXACTLY to excluding the following configuration under GH:
 (H3) a non-attracting horseshoe Lambda != M which is uniformly volume-contracting (J_t <= b - a t on Lambda), all of
 whose periodic orbits are volume-contracting, in a flow which is nu-ergodic and conservative, has dense nu-typical
 orbits, and all of whose ergodic measures with mu(d) = 0 have full support.

## 5. Dead ends of the "manufacture a non-smooth solution from unstable structure" approach (proved statements)
Lemma 5.1 (Jacobian cancellation). Let psi be bounded Borel with compact support, tau: M -> [0, infinity] Borel, and
T(phi) := int_M psi(x) int_0^{tau(x)} e^{J_t(x)} phi(g_t x) dt dnu(x) (whenever absolutely convergent). Then T = u nu with
 u(y) = int_0^infinity psi(g_{-t} y) 1[t < tau(g_{-t} y)] dt,
and, for smooth phi and tau < infinity a.e., T(X phi + d phi) = int psi(x) [e^{J_{tau(x)}(x)} phi(g_{tau(x)} x) - phi(x)] dnu(x).
Proof. Fubini, and the change of variables y = g_t x, dnu(y) = e^{J_t(x)} dnu(x) (J_t is the log nu-Jacobian of g_t);
the second formula integrates d/dt[e^{J_t(x)} phi(g_t x)] = e^{J_t(x)}(X phi + d phi)(g_t x) over [0, tau(x)]. QED
Meaning. Every construction "spread Patterson/conformal weights e^{J_t} over a smooth family of initial points"
(this includes integrating over Pesin unstable disks thickened to open sets, and Abel-regularised forward orbit
integrals with smooth initial densities) produces the function u above: the Jacobian weights cancel exactly.
(a) If tau = infinity identically and psi >= 0, psi != 0 is continuous, then u is not in L^1(nu): by conservativity
(N2, applied to -X) nu-a.e. point of {psi > 2c} returns to it at arbitrarily large negative times, each return
contributes at least c*delta to the integral (delta = dist({psi > 2c}, {psi < c}) / max|X|), so u = infinity a.e. there.
(b) If tau < infinity, the source term in Lemma 5.1 is psi nu minus the "exit distribution"
(g_tau)_*(e^{J_tau} psi nu), which is smooth only if x -> g_{tau(x)} x is smooth on supp psi; then u itself is
smooth wherever this holds. Singularities of u can only come from the set where tau is infinite or non-smooth,
and exactly there the source is singular.
So with smooth sources one never escapes the conservativity/Lemma C dichotomy: a contradiction with GH needs
cancellations (genuinely distributional objects), not positive measures. The only positive-measure objects with
smooth (namely zero) source are the nu-conformal measures, and these are completely controlled by Lemma C /
Corollary D1 — which is exactly what produced Theorem 4.1, and what stops at (H3).
(c) Using the formula in (iii) of the task: if Xu = f with u smooth and y in the strong unstable leaf of x, then
u(x) - u(y) = int_{-inf}^0 (f(g_t x) - f(g_t y)) dt; combined with the dual estimate (O1) this only yields
|int_{-inf}^0 (f(g_t x) - f(g_t y)) dt| <= C d(x,y) ||f||_{C^m} for f in X(C^inf), which is automatically true when
d(g_t x, g_t y) decays exponentially as t -> -inf. Similarly the derivative-loss route: the tame estimate
||u - c||_{C^k} <= C ||Xu||_{C^m} applied to u = int_0^T phi o g_s ds or u o g_t only compares quantities that both
grow like ||Dg_T||^{power}, with the larger power on the right, so it never contradicts exponential growth.
These are the checks behind the statement that I could not turn hyperbolic structure into a GH violation
beyond Theorem 4.1.

## 6. Status: what is proved, what is open

NOT settled: (Lambda), and zero topological entropy in general. I have neither a proof nor a counterexample.

Proved here (beyond the background):
 - Section 1: step 2 of the chain is correct. (Lambda) <=> no invariant measure has a positive exponent;
   zero entropy <=> no ergodic measure of positive entropy (formally weaker than (Lambda)).
 - Section 2: the curve-current step (c) of the sketch is wrong for n >= 3. The limit current is a boundary dR of
   an (n-2)-form-valued distribution, not dW for a function W. So that route never reaches a scalar equation
   XW = kappa W, and GH says nothing about the resulting object.
 - Section 3: existence of a top eigenmeasure S' on SM with L_t^* S' = e^{lambda* t} S' (elementary proof, no
   volume needed). The associated eigen-distribution tau(phi) = int dphi dS' satisfies tau o X = lambda* tau and has
   order 1. Lemma 3.2: eigen-distributions of order k with eigenvalue kappa > k lambda* vanish, and order-0
   eigen-measures with kappa != 0 vanish. So tau sits exactly on the borderline, and growth alone cannot
   exclude it. Two things are needed and both are open: (N) tau != 0, and (E1') GH excludes real nonzero
   eigenvalues of the transpose of X. Note that (E1') concerns P = X + d, not X.
 - Section 4: Proposition 4.0, a complete proof of the heteroclinic part of Corollary C1.
   Theorem 4.1 (dim 3, using the classical [Rue], [KLY], [HYP]): GH together with positive entropy forces
   configuration (H3). This is a non-attracting horseshoe Lambda != M that is uniformly volume-contracting
   (for X or for -X), all of whose periodic orbits are volume-contracting, and whose stable set is nu-null. The
   flow then has periodic orbits and is neither minimal nor uniquely ergodic.
   Corollary 4.2: under GH, if dim M <= 3 and there is no periodic orbit (e.g. the flow is uniquely ergodic),
   then h_top = 0.
   Corollary 4.3: in any dimension, under GH every hyperbolic ergodic measure of positive entropy produces a
   configuration (H3). Under GH plus unique ergodicity, positive entropy is possible only for a non-hyperbolic
   measure, so only in dim >= 4.
 - Section 5: Lemma 5.1 (Jacobian cancellation). Every construction that spreads conformal weights e^{J_t} over
   smooth families of initial points yields u(y) = int psi(g_{-t}y)(...) dt. Such a u is either smooth where the
   source is smooth, or ruled out by conservativity. A GH violation therefore needs genuinely signed or
   distributional objects. The planner's options (i) and (iii) were checked and give no contradiction.

Open questions (explicit):
 (Q1) [the dimension-3 case] Can a GH flow contain a uniformly volume-contracting, non-attracting horseshoe as in
      (H3)? A negative answer gives h_top = 0 for dim M = 3 (via Theorem 4.1).
      Sub-case analysis left open. Either some ergodic mu has mu(d) > 0, and one would want an orbit backward-generic
      for such a measure that lies in W^s(Lambda); then Lemma C applies, as in Proposition 4.0. Or
      max_mu mu(d) = 0, attained only by fully supported ergodic measures (Corollary D1), and then
      J_t <= eps t + C_eps uniformly. In that sub-case I found no contradiction with any proved consequence of GH.
      All the GH consequences in hand (L1, the tame estimate, N1, N2, B3, B4, Lemmas C and D) are either
      measure-level statements or C^infinity-uniform estimates. I found no way to make either kind interact with
      a Cantor-like hyperbolic set.
 (Q2) [dim >= 4] Exclude, under GH, ergodic measures of positive entropy that have zero exponents transverse to the
      flow. Katok-type horseshoes are not available for them.
 (Q3) The two missing statements of the eigen-current route: (N), producing a top eigenmeasure whose
      boundary distribution tau is nonzero; and (E1'). Both together would give (Lambda) directly by Section 3.
      Caution: by Prop. 2.2 of [R4-q7], the d-twisted analogue of (E1') contains the statement that mu(d) = 0 for
      every invariant mu. That is at least as strong as what is missing in (Q1).

=== END OF ANSWER round5_q7 ===

