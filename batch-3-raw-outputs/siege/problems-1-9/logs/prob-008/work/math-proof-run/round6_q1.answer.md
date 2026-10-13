# round6_q1: answer (final; partial result — (PE) proved for hyperbolic measures and for dim M <= 3, open case (PE0) isolated)

## Plan / statement being attempted
Target: (PE) under GH. New tool found: **Theorem J** ("no two-sided exponentially decaying transported distribution"), proved by a Jordan-chain argument at the eigenvalue 0 (L1 + GH applied to Xw = const) together with Fourier uniqueness. It replaces the missing step "T_0 is not a multiple of nu" in the planner's sketch. Consequences pursued:
(a) a periodic-orbit version (Lemma K) using Cayley-Hamilton on jets (no normal forms needed), giving: GH => no hyperbolic periodic orbit has a homoclinic orbit;
(b) hence (PE) for every hyperbolic ergodic measure (via the Katok / Lian-Young horseshoe theorem), and h_top = 0 when dim M <= 3;
(c) a pair version for non-hyperbolic measures with 0 < |mu(d)| < (smallest exponent on the relevant side).

Conventions: as in the brief. nu smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (log nu-Jacobian of g_t), P phi = X phi + d phi, so that d/dt [e^{J_t} (phi o g_t)] = e^{J_t} (P phi) o g_t. A *distribution density* is a continuous linear functional S on C^inf(M); S/nu is the generalized function u with <u, phi nu> = S(phi), and <Xu, phi nu> = -S(P phi) (Observation 0).

## 1. Two elementary facts used repeatedly (GH assumed)

**(F1)** If T is a distribution density with T(P phi) = 0 for all smooth phi, then T = c nu for a constant c.
*Proof.* u = T/nu satisfies <Xu, phi nu> = -T(P phi) = 0, so Xu = 0 and u is constant by L1. ∎

**(F2)** If T is a distribution density and c' a constant with T(P phi) = c' int phi dnu for all phi, then c' = 0 (and then T = c nu by F1).
*Proof.* u = T/nu satisfies <Xu, phi nu> = -c' int phi dnu, i.e. Xu = -c' (a constant, smooth function). By GH u is smooth and Xu = -c' holds pointwise. At a point q where u attains its maximum, s -> u(g_s q) has a maximum at s = 0, so (Xu)(q) = 0. Hence c' = 0. ∎

## 2. Theorem J (no two-sided exponentially decaying transported distribution)

**Theorem J.** Assume GH. Let S be a distribution density on M. For smooth phi put
 F_phi(t) := S( e^{J_t} (phi o g_t) ),  t in R.
(Equivalently F_phi(t) = <u_0 o g_{-t}, phi nu> with u_0 = S/nu: it is the pairing of the transported generalized function with phi nu.) Suppose there are eps > 0, k and C with
 |F_phi(t)| <= C e^{-eps |t|} ||phi||_{C^k}  for all t in R and all smooth phi.  (*)
Then S = 0.

*Proof.*
1. *Regularity in t.* The map t -> e^{J_t}(phi o g_t) is C^1 (indeed C^inf) from R into C^inf(M): the function (t,x) -> e^{J_t(x)} phi(g_t x) is jointly C^inf, so difference quotients in t converge in every C^m on compact t-sets (Taylor's formula with integral remainder). Its derivative is e^{J_t}(P phi) o g_t. Since S is continuous and linear, F_phi is C^1 and
 F_phi'(t) = F_{P phi}(t).
2. *Moments.* For j = 0,1,2,... define m_j(phi) := int_R t^j F_phi(t) dt. By (*), |m_j(phi)| <= C ||phi||_{C^k} int |t|^j e^{-eps|t|} dt, so each m_j is a distribution density (of order <= k).
3. *Jordan relations.* By (*) applied to P phi, F_{P phi} = F_phi' is also O(e^{-eps|t|}), and t^j F_phi(t) -> 0 as |t| -> inf. Integrating by parts on [-R, R] and letting R -> inf:
 m_0(P phi) = int F_phi' dt = 0,  and for j >= 1:  m_j(P phi) = int t^j F_phi'(t) dt = -j m_{j-1}(phi).
4. *Induction: m_j = 0 for every j.* By (F1), m_0 = c_0 nu. Then m_1(P phi) = -m_0(phi) = -c_0 int phi dnu, so c_0 = 0 by (F2); thus m_0 = 0. Suppose m_{j-1} = 0. Then m_j(P phi) = 0, so m_j = c_j nu by (F1), and m_{j+1}(P phi) = -(j+1) c_j int phi dnu, so c_j = 0 by (F2). Hence m_j = 0 for all j.
5. *Fourier uniqueness.* Fix phi. F_phi is continuous and |F_phi(t)| <= C' e^{-eps|t|}, so G(xi) := int e^{-i xi t} F_phi(t) dt extends holomorphically to the strip |Im xi| < eps, and G^{(j)}(0) = (-i)^j m_j(phi) = 0 for all j. So G = 0 on the strip, in particular on R. By uniqueness of the Fourier transform on L^1 and continuity, F_phi = 0 identically. In particular S(phi) = F_phi(0) = 0. As phi is arbitrary, S = 0. ∎

*Remarks.* (i) Only L1 and GH for constant right-hand sides are used (via F1, F2). (ii) The proof shows more: if F_phi is merely rapidly decreasing (with continuous dependence on phi), then all moments int t^j F_phi dt vanish. Exponential decay is used only in step 5 (quasi-analyticity of the Fourier transform). (iii) Sanity check: Lemma C of the background is the special case S = delta_x when int e^{J_t(x)} dt < inf with exponential decay at both ends; the north-south flow on S^2 (not GH) gives such an S = delta_y for y on a source-to-sink orbit.
(iv) This is exactly what closes the gap in the planner's sketch (b): the pair distribution T_z is the Laplace transform z -> int e^{-zt} F_phi(t) dt of a pair S = delta_x - e^b delta_y; when 0 lies in the open strip of convergence, (*) holds and S = 0, impossible for x != y. One does not need to show "T_0 is not a multiple of nu": the Jordan chain at z = 0 kills all Taylor coefficients.

## 3. Lemma K (orbits backward-asymptotic to a periodic point) — proved, elementary

**Lemma K.** Assume GH. Let p in M and P > 0 with g_P(p) = p (p may be a zero of X or a periodic point; no hyperbolicity assumed). Put I := J_P(p). There is no point y != p such that
 (a) d(g_{-mP} y, p) <= C kappa^m for all integers m >= 0, for some C and some kappa in (0,1); and
 (b) J_t(y) <= C - eps t for all t >= 0, for some eps > 0.

*Proof.* Suppose y is such a point.
1. *A weighted Koopman operator.* For Psi in C^inf(M) put (L Psi)(v) := e^{J_{-P}(v)} Psi(g_{-P} v). By the cocycle identity J_{-(m+1)P}(v) = J_{-P}(v) + J_{-mP}(g_{-P}v), induction gives (L^m Psi)(v) = e^{J_{-mP}(v)} Psi(g_{-mP} v). L is continuous on each C^K(M).
2. *Jets and Cayley-Hamilton.* Fix K >= 1 (chosen in step 6). Let I_K be the space of smooth functions all of whose derivatives of order < K vanish at p. Since g_{-P}(p) = p, L(I_K) ⊂ I_K. So L induces a linear map L_K on the finite-dimensional space C^inf(M)/I_K (the (K-1)-jets at p), of dimension N = binom(n+K-1, n). Let Q(zeta) = sum_{j=0}^N q_j zeta^j be the characteristic polynomial of L_K (monic: q_N = 1). By Cayley-Hamilton Q(L_K) = 0, i.e. Q(L) Psi in I_K for every smooth Psi. Since Q(L) is a finite combination of the L^j, ||Q(L)Psi||_{C^K} <= C_1 ||Psi||_{C^K}. Taylor's formula in a coordinate ball B around p gives |G(v)| <= C_2 ||G||_{C^K} d(v,p)^K for G in I_K and v in B.
3. *The distribution.* Let y_j := g_{-jP} y (j = 0..N) and w_j := q_j e^{J_{-jP}(y)}, and S := sum_j w_j delta_{y_j}. The y_j are pairwise distinct: if g_{-aP}y = g_{-bP}y with a < b, then y is fixed by g_{-(b-a)P}, so g_{-l(b-a)P} y = y for all l, and (a) forces y = p, excluded. Since w_N = e^{J_{-NP}(y)} != 0, S != 0.
4. *Backward decay.* Let t <= 0 and write t = -mP - r with m >= 0 an integer and r in [0, P). Put Phi_r(v) := e^{J_{-r}(v)} phi(g_{-r} v); then ||Phi_r||_{C^K} <= C_3 ||phi||_{C^K} uniformly in r in [0,P]. Using J_t(g_{-jP}y) = J_{t-jP}(y) - J_{-jP}(y) and J_{-(m+j)P - r}(y) = J_{-(m+j)P}(y) + J_{-r}(g_{-(m+j)P} y):
 w_j e^{J_t(y_j)} phi(g_t y_j) = q_j e^{J_{-(m+j)P}(y)} Phi_r(g_{-(m+j)P} y) = q_j (L^{m+j} Phi_r)(y).
Summing over j: F_phi(t) = S(e^{J_t} phi o g_t) = (L^m G_r)(y) = e^{J_{-mP}(y)} G_r(g_{-mP} y), where G_r := Q(L) Phi_r lies in I_K.
5. *Estimating the two factors.* By (a), for m >= m_0 the point g_{-mP}y lies in B and |G_r(g_{-mP}y)| <= C_2 C_1 C_3 ||phi||_{C^K} C^K kappa^{mK}. Also J_{-mP}(y) = -sum_{i=1}^m J_P(g_{-iP} y), and |J_P(g_{-iP}y) - I| <= Lip(J_P) C kappa^i, so J_{-mP}(y) <= -mI + C_4. Hence for t <= -m_0 P:
 |F_phi(t)| <= C_5 ||phi||_{C^K} exp( m (-I - K log(1/kappa)) ).
6. *Choice of K.* Choose K with K log(1/kappa) > max(0, -I) + 1. Then |F_phi(t)| <= C_6 e^{-|t|/P} ||phi||_{C^K} for t <= 0 (the finitely many m < m_0 are absorbed into C_6).
7. *Forward decay.* For t >= 0: J_t(y_j) = J_{t - jP}(y) - J_{-jP}(y). For t >= jP, (b) gives J_{t-jP}(y) <= C - eps(t - jP); for 0 <= t < jP it is bounded by ||d||_inf N P. So |F_phi(t)| <= sum_j |w_j| e^{J_t(y_j)} ||phi||_inf <= C_7 e^{-eps t} ||phi||_inf.
8. By 6 and 7, S satisfies (*) of Theorem J (with k = K and rate min(eps, 1/P)). So S = 0, contradicting step 3. ∎

**Lemma K' (time-reversed form).** Assume GH. There is no p with g_P p = p (P > 0) and y != p such that d(g_{mP} y, p) <= C kappa^m (m >= 0) and J_t(y) <= C - eps|t| for all t <= 0.
*Proof.* Apply Lemma K to -X, which is GH by (O4). Its flow is g_{-t}, its nu-divergence is -d, and its log-Jacobian at time t is J_{-t}. Condition (b) for -X reads J_{-t}(y) <= C - eps t for t >= 0. ∎

*Remark.* Lemma K needs no normal forms: Cayley-Hamilton on the finite-dimensional jet space at the fixed point p of g_{-P} annihilates, in one stroke, all the "slowly decaying modes" e^{-mI} mu^alpha (products of eigenvalues of Dg_{-P}(p)) of the backward sequence. This is where periodicity of p is essential (Section 7).

## 4. Consequences for connecting orbits (proved; uses only the classical stable manifold theorem for hyperbolic periodic orbits / zeros)

Cited [SM] (stable manifold theorem, classical). Let gamma be a hyperbolic periodic orbit of period P (resp. a hyperbolic zero p; then read gamma = {p}, P = 1). Then W^s(gamma) := {y : dist(g_t y, gamma) -> 0 as t -> +inf} is the union over q in gamma of W^{ss}(q), and there is c > 0 such that for y in W^{ss}(q), d(g_t y, g_t q) <= C_y e^{-ct} for t >= 0 ("asymptotic phase"). Likewise W^u(gamma) = union of W^{uu}(q), with d(g_{-t} y, g_{-t} q) <= C_y e^{-ct} for t >= 0.

Notation: for gamma as above put I(gamma) := J_P(q) = int_0^P d(g_s q) ds (independent of q in gamma; for a zero, I = d(p)). Note J_{mP}(q) = m I(gamma) for q in gamma, hence J_t(q) = (t/P) I(gamma) + O(1) for all real t, uniformly.

**Corollary 4.1 (connections).** Assume GH. Let gamma_1, gamma_2 be hyperbolic periodic orbits or hyperbolic zeros (possibly gamma_1 = gamma_2), and let y in W^u(gamma_1) ∩ W^s(gamma_2), y not in gamma_1 ∪ gamma_2. Then I(gamma_2) >= 0 and I(gamma_1) <= 0 (that is, I(gamma_2) < 0 is impossible, and I(gamma_1) > 0 is impossible).
*Proof.* Choose q_1 in gamma_1 and q_2 in gamma_2 with y in W^{uu}(q_1) ∩ W^{ss}(q_2) ([SM]). Since d is Lipschitz, |J_t(y) - J_t(q_2)| <= Lip(d) C_y / c for t >= 0 and |J_t(y) - J_t(q_1)| <= Lip(d) C_y / c for t <= 0. Let P_1 be the period of gamma_1.
- If I(gamma_2) < 0: J_t(y) <= C + (t/P_2) I(gamma_2) for t >= 0, which is (b) of Lemma K with eps = |I(gamma_2)|/P_2; and d(g_{-mP_1} y, q_1) = d(g_{-mP_1} y, g_{-mP_1} q_1) <= C_y e^{-c m P_1}, which is (a) with p = q_1, P = P_1, kappa = e^{-cP_1}; and y != q_1. Lemma K gives a contradiction.
- If I(gamma_1) > 0: for t <= 0, J_t(y) <= C + (t/P_1) I(gamma_1) = C - (I(gamma_1)/P_1)|t|; and d(g_{mP_2} y, q_2) <= C_y e^{-c m P_2}. Lemma K' (with p = q_2) gives a contradiction. ∎

So under GH every connection between hyperbolic periodic orbits/zeros goes from a volume-contracting one (I < 0) to a volume-expanding one (I > 0). (This strengthens Prop. 4.0 of [R5-d], which excluded only I(gamma_1) > 0 > I(gamma_2).)

**Corollary 4.2 (no homoclinic orbits).** Assume GH and dim M >= 2. No hyperbolic periodic orbit and no hyperbolic zero has a homoclinic point (a point of W^u(gamma) ∩ W^s(gamma) outside gamma), transverse or not.
*Proof.* With gamma_1 = gamma_2 = gamma, Corollary 4.1 gives I(gamma) >= 0 and I(gamma) <= 0, so I(gamma) = 0; and I(gamma) = 0 is excluded by Observation P (periodic orbits, dim >= 2) or by P1 (zeros: d(p) != 0). ∎

## 5. (PE) for hyperbolic measures; zero topological entropy in dimension <= 3 (proved modulo cited classical theorems)

Cited (from memory, standard):
- [Ru] Ruelle's inequality: for a C^1 diffeomorphism f of a compact manifold and an f-invariant ergodic mu, h_mu(f) <= sum of the positive Lyapunov exponents of mu (with multiplicity).
- [KLY] Katok's horseshoe theorem, flow version (Katok, Publ. IHES 51 (1980), including flows on 3-manifolds; Lian-Young for C^2 flows in any finite dimension): if mu is an ergodic invariant probability of a C^2 flow with h_mu(g_1) > 0, mu(Zero(X)) = 0, and all Lyapunov exponents of mu other than the (zero) exponent in the flow direction are nonzero, then the flow has a horseshoe: a compact invariant hyperbolic set Lambda on which the flow is conjugate to a suspension of a transitive subshift of finite type of positive entropy. In particular Lambda contains a hyperbolic periodic orbit gamma and a point x not in gamma whose alpha- and omega-limit sets are gamma (in the symbolic model: a sequence that agrees with the periodic sequence of gamma in the far past and far future but not everywhere; it exists because the SFT is transitive and not a single periodic orbit). By [SM], x is a homoclinic point of gamma.
- Variational principle and the reduction to ergodic flow-invariant measures (step 2 of the chain; I checked it and see no flaw: mu-bar = int_0^1 (g_s)_* mu ds is flow-invariant because (g_1)_* mu = mu; h_{(g_s)_* mu}(g_1) = h_mu(g_1) because g_s conjugates g_1 to itself; entropy is affine and satisfies the integral formula over decompositions into g_1-invariant measures (Jacobs), applied to the flow-ergodic decomposition of mu-bar).

**Theorem 5.1.** Assume GH and dim M >= 2. Let mu be an ergodic flow-invariant probability with h_mu(g_1) > 0. Then mu is not hyperbolic: besides the flow direction, mu has a zero Lyapunov exponent.
*Proof.* As in Theorem 4.1 of [R5-d]: mu(Zero(X)) = 0 (otherwise mu is carried by the closed invariant set Zero(X) on which g_1 = id, so h_mu = 0); the exponent in the flow direction is 0 for mu-a.e. x; by [Ru] for g_1 and for g_{-1}, mu has a positive and a negative exponent. If all other exponents were nonzero, [KLY] would give a hyperbolic periodic orbit with a homoclinic point, contradicting Corollary 4.2. ∎

**Theorem 5.2 (the problem, for dim M <= 3).** Assume GH and dim M <= 3. Then h_top(g_1) = 0.
*Proof.* By step 2 of the chain it suffices that h_mu(g_1) = 0 for every ergodic flow-invariant mu. Suppose h_mu(g_1) > 0. As above, mu(Zero(X)) = 0, the flow direction carries the exponent 0, and [Ru] (for g_1 and g_{-1}) gives a positive and a negative exponent. If dim M <= 2 there is at most one further exponent, which cannot be both positive and negative: contradiction. If dim M = 3 the exponents are chi^+ > 0 = 0 > chi^-, so mu is hyperbolic, contradicting Theorem 5.1 (dim M = 3 >= 2). ∎

Remark. In dimension 3 this does not use Theorem 4.1(ii) of [R5-d] (uniform sign of volume contraction on the horseshoe): a single hyperbolic periodic orbit with a single homoclinic point is already excluded by Lemma K / K', whatever the sign of I(gamma).

## 6. Non-hyperbolic measures: the pair version (proved modulo cited Pesin / Ledrappier-Young facts)

Cited:
- [P] Pesin theory for f = g_1 (C^inf diffeo) and an ergodic mu: for mu-a.e. x there is a local unstable manifold W^u_loc(x) (an embedded C^1 disc tangent to the sum of the Oseledets spaces of positive exponents) such that for every delta > 0 and y in W^u_loc(x): d(f^{-m}x, f^{-m}y) <= C(x,delta) e^{-(chi^+_min - delta) m} for m >= 0, where chi^+_min is the smallest positive exponent of mu.
- [LY] (Ledrappier-Strelcyn, Ledrappier-Young) There is a measurable partition xi subordinate to W^u (xi(x) ⊂ W^u_loc(x), xi(x) contains a neighbourhood of x in W^u(x)) with h_mu(f) = H_mu(xi | f xi). If the conditional measures mu^xi_x were Dirac masses delta_x for a.e. x, xi would be the point partition mod mu and h_mu(f) = 0. Hence h_mu(f) > 0 implies mu^xi_x(xi(x) \ {x}) > 0 for a.e. x.

Let lambda := mu(d); by Birkhoff J_t(x)/t -> lambda as t -> +inf and as t -> -inf for mu-a.e. x. (lambda is the sum of all Lyapunov exponents of mu; it does not depend on nu.) Let chi^-_max denote the negative exponent of mu closest to 0.

**Proposition 6.1.** Assume GH. Let mu be ergodic with h_mu(g_1) > 0. Then lambda = mu(d) satisfies neither -chi^+_min < lambda < 0 nor 0 < lambda < |chi^-_max|.
*Proof.* Case -chi^+_min < lambda < 0. Fix delta > 0 with lambda + 3 delta < 0 and chi^+_min - 2delta > |lambda| + 2delta. Let G be the set of points z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf; mu(G) = 1. By [P] and [LY], for mu-a.e. x (so we may take x in G) the conditional mu^xi_x gives positive mass to xi(x) \ {x} and full mass to G, so there is y in G ∩ W^u_loc(x), y != x. Put theta := chi^+_min - delta. Interpolating between integer times as in [R5-a] Lemma 2: d(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0. Then b := lim_{t -> -inf} (J_t(x) - J_t(y)) exists and |J_t(x) - J_t(y) - b| <= C e^{-theta|t|} for t <= 0 ([R5-a] Step 4(a)). Let S := delta_x - e^b delta_y (nonzero, as x != y), so F_phi(t) = e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y).
- t >= 0: since x, y in G, J_t(x), J_t(y) <= C + (lambda + delta) t, so |F_phi(t)| <= C e^{(lambda+delta)t} ||phi||_inf.
- t <= 0: as in [R5-a] Step 4(c), |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|} ||phi||_{C^1}, and J_t(x) <= C + (|lambda| + delta)|t| for t <= 0 (x in G, lambda < 0). So |F_phi(t)| <= C e^{-(theta - |lambda| - delta)|t|} ||phi||_{C^1}, and theta - |lambda| - delta > 0 by the choice of delta.
So (*) of Theorem J holds and S = 0: contradiction.
Case 0 < lambda < |chi^-_max|: apply the first case to -X (GH by (O4)); mu is ergodic for the reversed flow with the same entropy, its exponents are the negatives of those of mu, so its smallest positive exponent is |chi^-_max|, and its lambda is -lambda. ∎

So for a GH flow, an ergodic measure of positive entropy must be non-hyperbolic (Theorem 5.1) and must have lambda = 0, or lambda <= -chi^+_min, or lambda >= |chi^-_max| (Proposition 6.1).

**Lemma 6.0 (non-atomic unstable conditionals; proved from the Ledrappier-Strelcyn formula).** In the setting of [LY] with h_mu(f) > 0, the conditional measures mu^xi_x are non-atomic for mu-a.e. x.
*Proof.* xi is increasing: (f xi)(fx) = f(xi(x)) ⊃ xi(fx), so xi refines f xi. Put w(x) := mu^xi_x({x}). By invariance mu^{f xi}_{fx} = f_* mu^xi_x, so mu^{f xi}_{fx}({fx}) = w(x); and mu^xi_{fx} is mu^{f xi}_{fx} restricted to xi(fx) and normalised. Hence w(fx) = w(x) / mu^{f xi}_{fx}(xi(fx)) >= w(x). Since w is bounded and mu is invariant, int (w o f - w) dmu = 0 with a nonnegative integrand, so w o f = w a.e., and w = w_0 a.e. by ergodicity. If w_0 > 0, equality forces mu^{f xi}_{fx}(xi(fx)) = 1 a.e., i.e. xi = f xi mod mu, so h_mu(f) = H_mu(xi | f xi) = 0, a contradiction. So w = 0 a.e. Finally the mu-measure of the set of points z which are atoms of their own conditional is int w dmu = 0, while it also equals int mu^xi_x(atoms of mu^xi_x) dmu(x); so a.e. conditional has no atoms. ∎

**Proposition 6.2 (one-dimensional unstable direction; proof sketched, modulo standard Pesin-theory estimates).** Assume GH. Let mu be ergodic with h_mu(g_1) > 0 and lambda = mu(d) < 0, and suppose mu has exactly one positive exponent chi, of multiplicity one. This is impossible. Symmetrically (apply to -X), lambda > 0 is impossible when mu has exactly one negative exponent, simple.
*Sketch.*
1. *Affine parameters (standard for 1-dimensional unstable leaves).* For a.e. x the global unstable leaf W^u(x) is a C^inf curve, and there is a C^inf parameter H_x : W^u(x) -> R, H_x(x) = 0, with H_{g_{-m}x}(g_{-m} y) = A_m(x) H_x(y) for m >= 0, where |A_m(x)| <= C(x) e^{-(chi - delta)m}. (Construction: with a(z) := log |Dg_{-1}(z) e(z)|, e(z) the unit tangent to the leaf, take H_x(y) = int_x^y exp( sum_{m >= 0} [a(g_{-m} z) - a(g_{-m} x)] ) dz along the leaf; the series converges in C^K along the leaf by the 1-dimensional distortion estimates, and the change of variables w = g_{-1} z shows the linearisation identity, as checked in the derivation: H_{g_{-1}x}(g_{-1}y) = e^{a(x)} H_x(y).) The charts H_{g_{-m}x}^{-1} have C^K norms on intervals of radius rho(g_{-m}x) bounded by C(x) e^{delta m}, with rho(g_{-m}x) >= rho(x) e^{-delta m} (tempered Pesin bounds).
2. *Removing the Jacobian weight.* For w in W^u(z) put beta_z(w) := -int_{-inf}^0 (d(g_s w) - d(g_s z)) ds. Then J_{-m}(y) - J_{-m}(x) = beta_x(y) - beta_{g_{-m}x}(g_{-m}y) (direct computation from the definition), and beta_{g_{-m}x} has tempered C^K norms along the leaf.
3. *The distribution.* By Lemma 6.0 there are K+1 distinct points y_0..y_K in xi(x) whose forward Birkhoff averages of d converge to lambda. Let s_j = H_x(y_j) (distinct), choose a nonzero vector (a_j) with sum_j a_j s_j^i = 0 for i = 0..K-1 (K equations, K+1 unknowns), put w_j := a_j e^{-beta_x(y_j)}, S := sum_j w_j delta_{y_j} != 0.
4. *Backward estimate.* For t = -m - r (m >= 0 integer, r in [0,1)), exactly as in Lemma K step 4 and by step 2:
 S(e^{J_t} phi o g_t) = e^{J_{-m}(x)} sum_j a_j theta_{m,r}(A_m(x) s_j),
 where theta_{m,r}(sigma) := e^{-beta_{g_{-m}x}(w)} Phi_r(w) at w = H^{-1}_{g_{-m}x}(sigma), Phi_r(w) = e^{J_{-r}(w)} phi(g_{-r} w). By the vanishing moments, Taylor's formula of order K at sigma = 0 gives |sum_j a_j theta_{m,r}(A_m s_j)| <= C |A_m|^K ||theta_{m,r}||_{C^K} <= C(x) e^{-(K(chi - delta) - delta) m} ||phi||_{C^K}. Also e^{J_{-m}(x)} <= C e^{(|lambda| + delta) m}. Choosing K with K chi > |lambda| + 1 and delta small, S(e^{J_t} phi o g_t) decays exponentially as t -> -inf, with a C^K bound.
5. *Forward estimate.* Each y_j has J_t(y_j) <= C + (lambda + delta) t for t >= 0, so |S(e^{J_t} phi o g_t)| <= C e^{(lambda+delta)t} ||phi||_inf.
6. Theorem J gives S = 0, a contradiction. ∎
The only non-elementary inputs are the tempered C^K bounds in steps 1-2 (standard Pesin theory for C^inf flows, 1-dimensional leaves). For higher-dimensional unstable manifolds the same argument goes through verbatim if one has C^K-tempered non-stationary normal form coordinates along W^u in which g_{-1} is a polynomial map of uniformly bounded degree r (non-uniform sub-resonance normal forms, Guysinsky-Katok / Kalinin-Sadovskaya type; cited from memory, hypotheses not checked): one then imposes vanishing moments against all polynomials of degree < rK. **If that citation is granted, every ergodic mu with h_mu > 0 under GH has mu(d) = 0.** I mark this extension as conditional.

**Corollary 6.3 (dimension 4, modulo the same Pesin estimates).** If dim M = 4 and GH holds, every ergodic mu with h_mu(g_1) > 0 has exponents chi^+ > 0 = 0 = 0 > chi^- = -chi^+ (all simple), i.e. it is non-hyperbolic with lambda = mu(d) = 0; consequently (Corollary D1 of the background) supp mu = M.
*Proof.* Theorem 5.1 gives a second zero exponent; the remaining two are chi^+ > 0 > chi^- by [Ru], each simple; Proposition 6.2 and its symmetric form exclude lambda < 0 and lambda > 0. ∎

## 7. What remains open, and where the argument stops

**Unconditionally open case of (PE).** Under GH, exclude an ergodic mu with h_mu(g_1) > 0 such that
 (i) mu has a zero Lyapunov exponent transverse to X (non-hyperbolic; forced by Theorem 5.1), and
 (ii) either lambda = mu(d) = 0, or lambda <= -chi^+_min with no 1-dimensional simple unstable direction (resp. lambda >= |chi^-_max| with no 1-dimensional simple stable direction), the latter only modulo the cited normal forms of Prop. 6.2.
With the normal-form citation granted, the single remaining case is:
**(PE0)** GH excludes an ergodic, non-hyperbolic mu with h_mu > 0 and mu(d) = 0. (Such a mu has supp mu = M by Corollary D1; the volume-preserving case, where every invariant measure has mu(d) = 0, is inside (PE0); this is the old core #16.) **(PE0) is open; I could not prove it.** So the problem's claim is proved here only for dim M <= 3 (Theorem 5.2), and in every dimension for hyperbolic measures (Theorem 5.1); in dim 4 it is reduced (modulo standard Pesin estimates) to (PE0).

**Why the method stops at lambda = 0.** Theorem J needs a nonzero S with |S(e^{J_t} phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k} in BOTH time directions.
- If lambda != 0, one direction is free (e.g. lambda < 0: forward decay of e^{J_t} at generic points), and the other is obtained by cancellation inside one unstable leaf (pairs, or vanishing moments in an affine/normal-form parameter, or Cayley-Hamilton on jets at a periodic point).
- If lambda = 0, e^{J_t} = e^{o(|t|)} in both directions at generic points, so S needs cancellation forward (clusters of forward-asymptotic points, inside stable leaves) and backward (clusters inside unstable leaves) at the same time. For a combination of point masses this requires closed su-cycles of points x_{11} ~s x_{12} ~u x_{22} ~s x_{21} ~u x_{11} with consistent weights; the weights are consistent only if the Jacobian holonomy around the cycle vanishes: b^s_1 + b^u_2 = b^u_1 + b^s_2, where b^s, b^u are the limits of J_t(.) - J_t(.) along the stable/unstable sides. Generic su-paths do not even close up (temporal distance), and when they close the cycle condition is an extra codimension-one condition. Spreading S along unstable discs gives forward decay only at the speed of equidistribution of unstable discs, which is not exponential in general (no mixing rates are available for general positive-entropy measures).
- Remark (ii) after Theorem J shows that rapid (super-polynomial) two-sided decay already forces all moments int t^j F_phi dt to vanish; but for sub-exponential decay this does not force F_phi = 0 (no quasi-analyticity), so even a weaker decay statement would not suffice without a further idea.
- The planner's observation applies: under the strong hypothesis H (smooth invariant volume, unique ergodicity, all mean-zero smooth functions are smooth coboundaries) the pair transform T_z, 0 < Re z < theta, has the formal Taylor expansion 0 at z = 0 (all Jordan coefficients vanish, consistently with Theorem J's step 4), but T_z is not known to extend holomorphically across Re z = 0, so no contradiction follows.

**Status of the chain.** Step 2 is correct (checked in Section 5). Step 1 (PE) is proved for: all hyperbolic ergodic measures (any dimension; cited [KLY]); all ergodic measures when dim M <= 3; all ergodic measures with -chi^+_min < mu(d) < 0 or 0 < mu(d) < |chi^-_max| (Prop. 6.1, cited [P], [LY]); all ergodic measures with mu(d) < 0 and a single simple positive exponent, or mu(d) > 0 and a single simple negative exponent (Prop. 6.2, sketched modulo standard Pesin estimates). It remains open in the case (PE0) (and, without the normal-form citation, in the non-1-dimensional large-|lambda| case).

## Summary of what is proved (new in this round)
1. **Theorem J (fully proved, GH + L1 only):** no nonzero distribution density S has S(e^{J_t} phi o g_t) = O(e^{-eps|t|}) ||phi||_{C^k} for t -> +inf and t -> -inf. Proof: the moments m_j(phi) = int t^j F_phi(t) dt form a Jordan chain m_j(P phi) = -j m_{j-1}(phi); L1 and "Xw = const => const = 0" kill it; Fourier uniqueness finishes.
2. **Lemma K / K' (fully proved):** no point y != p, p a periodic point or a zero, with g_{-mP} y -> p exponentially and forward exponential volume contraction along y (resp. the time-reversed version). Proof: Cayley-Hamilton on the jet space at p for the weighted Koopman operator L Psi = e^{J_{-P}} Psi o g_{-P} produces a finite combination of Dirac masses on the backward orbit of y satisfying Theorem J.
3. **Corollary 4.1/4.2 (proved, modulo the classical stable manifold theorem):** under GH, every connection between hyperbolic periodic orbits/zeros goes from I < 0 to I > 0; in particular no hyperbolic periodic orbit or hyperbolic zero has a homoclinic point.
4. **Theorem 5.1 / 5.2 (proved modulo Ruelle's inequality and the Katok / Lian-Young horseshoe theorem):** under GH every positive-entropy ergodic measure is non-hyperbolic; **h_top(g_1) = 0 whenever dim M <= 3.**
5. **Prop. 6.1 (proved modulo Pesin theory and Ledrappier-Strelcyn), Lemma 6.0 (proved), Prop. 6.2 and Cor. 6.3 (sketched):** restrictions on mu(d) for non-hyperbolic positive-entropy measures; in dimension 4 only mu(d) = 0 survives.
**Open:** (PE0), hence the problem in dimension >= 4.

=== END OF ANSWER round6_q1 ===

