# round14_q4: answer — attempt to refute (SC)

## Plan (written first)
Outcome: no counterexample to (SC) found. The work below shows where (SC) holds and what a counterexample would have to look like.
1. Note that the conclusion of (SC) does not mention mu. Give a short sufficient condition for it: a "homoclinic" configuration at one point x_0 (Lemma 1).
2. Prove the conclusion whenever M carries a hyperbolic periodic orbit or a hyperbolic zero with two homoclinic orbits and weak dissipation (Proposition 2). Proved, apart from standard stable-manifold facts.
3. Deduce (SC) for every hyperbolic mu (Theorem 3), and hence for dim M <= 3. This is conditional on a cited Katok-type horseshoe/approximation theorem for flows, quoted from memory.
4. List the necessary features of a counterexample (Section 4).
5. Examine the natural candidates: products and isometric circle/torus extensions of Anosov flows (these have no hyperbolic measures at all). Explain which mechanism produces the chains there, and the role of the "occurs exactly once" clause (Section 5, partly a sketch).
6. List the open questions.

Conventions are those of the task file: d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, J_{t+r}(x) = J_r(x) + J_t(g_r x), and ||d||_Lip is a Lipschitz constant of d.

Call the conclusion of (SC) (everything after "Then there exist ...") the **configuration property (CP)** of the flow. (CP) mentions neither mu nor the hypotheses on mu. So a counterexample to (SC) is a flow that fails (CP) at every point of M and still carries a mu with the hypotheses of (SC).

## 1. A two-leg sufficient condition

**Lemma 1 (proved).** Suppose there are x_0 in M, reals tau, tau', points q, q' and constants C >= 1, theta > 0, eta in [0, theta), C_0 >= 0 with the following properties. Write y = g_tau x_0 and y' = g_{tau'} x_0.
(i) q and q' are neither zeros of X nor periodic. Neither orbit contains x_0, and the orbits of q and q' are distinct.
(ii) For all t <= 0: d(g_t x_0, g_t q) <= C e^{-theta|t|} d(x_0, q), and the same with q'.
(iii) For all t >= 0: d(g_t q, g_t y) <= C e^{-theta t} d(q, y), and the same with q', y'.
(iv) J_t(x_0) <= C_0 + eta|t| for all real t. Also J_t(q) <= C_0 + eta t and J_t(q') <= C_0 + eta t for t >= 0.
Then (CP) holds.

*Proof.* Put a_0 = x_0, a_1 = q, a_i = y for i >= 2, and b_0 = x_0, b_1 = q', b_i = y' for i >= 2.

*(L1), (L2).* The leg (a_0, a_1) satisfies (L1) by (ii). The leg (a_1, a_2) satisfies (L2) by (iii). All later legs have length 0, so both inequalities read 0 <= 0. The same holds for (b_i).

*(L3).* The sums are finite. The limit points are p = y and p' = y'.

*(E).* d(g_t y, g_{t+tau} x_0) = 0 for all t. Likewise for y' with tau'.

*(L4).* First, J_t(y) = J_{t+tau}(x_0) - J_tau(x_0). With (iv),
J_t(y) <= C_0 + eta|t+tau| + |J_tau(x_0)| <= C_0 + eta|tau| + |J_tau(x_0)| + eta|t|,
and similarly for y'. Put C' := C_0 + eta(|tau| + |tau'|) + |J_tau(x_0)| + |J_{tau'}(x_0)|. Then:
- the even vertices are x_0, y, y, ... (resp. x_0, y', ...), and each satisfies J_t <= C' + eta|t| for t <= 0;
- the odd vertices are q, y, y, ... (resp. q', y', ...), and each satisfies J_t <= C' + eta t for t >= 0;
- J_t(x_0) <= C' + eta t for t >= 0.

*Orbit-isolated vertices.* The combined list is x_0, q, y, y, ..., x_0, q', y', y', .... By (i), q is not on the orbit of x_0, which contains x_0, y, y'. Also q differs from q' because their orbits are distinct. So q occurs exactly once, and q differs from x_0. By (i), q is not a zero and not periodic. The orbit of q contains none of x_0, y, y' (these lie on the orbit of x_0) and not q'. The limit points y, y' lie on the orbit of x_0, so they are not on the orbit of q either. The same argument applies to q'. ∎

## 2. Hyperbolic periodic orbits and zeros with homoclinic orbits

Let gamma be a hyperbolic periodic orbit of period P through p. Its transverse Floquet exponents chi_1, ..., chi_{n-1} are (1/P) log|.| of the eigenvalues of the linearised Poincaré map, all nonzero. Put
I := J_P(p) = int_gamma d,  chi_*(gamma) := min_i |chi_i|.
By Liouville's formula, I/P = sum_i chi_i, since the flow-direction exponent is 0.

A *homoclinic orbit* of gamma is an orbit O, different from gamma, contained in W^u(gamma) ∩ W^s(gamma). For a hyperbolic zero p (no eigenvalue of A = DX(p) on the imaginary axis), let chi_*(p) := min |Re lambda| over the eigenvalues of A. Note that d(p) = tr A, whatever nu is.

**Proposition 2 (proved, modulo the standard stable-manifold theorem for hyperbolic periodic orbits and zeros).**
(a) Suppose some hyperbolic periodic orbit gamma has two distinct homoclinic orbits and |I|/P < chi_*(gamma). Then (CP) holds.
(b) Suppose some hyperbolic zero p has two distinct homoclinic orbits and |d(p)| < chi_*(p). Then (CP) holds.
Transversality is not needed. If one homoclinic orbit is transverse, there are infinitely many (Smale–Birkhoff; cited).

*Standard facts used (stable-manifold theorem, cited from memory).* Fix theta with 0 < theta < chi_*(gamma). Then:
- W^u(gamma) is the union over s in [0, P) of the strong unstable manifolds W^{uu}(g_s p);
- for every w in W^{uu}(z), z in gamma, there is C_w with d(g_t w, g_t z) <= C_w e^{-theta|t|} for all t <= 0;
- symmetrically, W^s(gamma) is the union of the W^{ss}(g_s p), with forward estimates;
- g_r W^{uu}(z) = W^{uu}(g_r z).
For a hyperbolic zero, W^u(p) itself has the backward estimate at any rate theta < min{Re lambda : Re lambda > 0}, and similarly for W^s(p).

*Proof of (a).* Choose theta with |I|/P < theta < chi_*(gamma), and put eta := |I|/P < theta and x_0 := p.

*Growth at x_0.* Write t = kP + r with k an integer and 0 <= r < P. Then J_t(p) = kI + J_r(p), so |J_t(p) - tI/P| <= 2P||d||_inf. Hence J_t(x_0) <= 2P||d||_inf + eta|t| for all t.

*The vertex q.* Let O be a homoclinic orbit and pick w in O. Then w lies in W^{uu}(g_s p) for some s. Put q := g_{-s} w, which lies in W^{uu}(p) and in O. Also q lies in W^{ss}(g_tau p) for some tau. Since q is not on gamma, q ≠ p and q ≠ g_tau p. The stable-manifold estimates, divided by d(p, q) > 0 (resp. d(q, g_tau p) > 0), give (ii) and (iii) with y = g_tau x_0.

*q is not a zero and not periodic.* Its alpha- and omega-limit sets are gamma. A periodic orbit or a zero equals its own omega-limit set, so q would lie on gamma, which is false. Nor does the orbit of q contain x_0, since x_0 lies on gamma.

*Growth at q.* For t >= 0,
|J_t(q) - J_t(g_tau p)| <= ||d||_Lip int_0^t d(g_s q, g_s g_tau p) ds <= ||d||_Lip C d(q, g_tau p)/theta.
Also J_t(g_tau p) = J_{t+tau}(p) - J_tau(p) <= const + eta t. So (iv) holds for q.

*The second vertex.* Do the same with a second homoclinic orbit O' ≠ O, which gives q' and tau'. The orbits of q and q' are O and O', which are distinct. Take the maximum of the constants. Lemma 1 then applies.

*Proof of (b).* The same argument with x_0 = p, y = y' = p and eta = |d(p)|. Here J_t(p) = t d(p), q lies in W^u(p) ∩ W^s(p) with q ≠ p, and (iii) reads d(g_t q, p) <= C e^{-theta t} d(q, p). ∎

*Remark (why the rate condition matters).* Without |I|/P < chi_* the two-leg chain can fail (L4). Take a 3-dimensional flow whose periodic orbit has transverse exponents (2, -1). Then I/P = 1 and chi_* = 1, so there is no eta with I/P <= eta < theta <= 1. (L4) uses the vertices' own Jacobians, and the hypothesis mu(d) = 0 enters only through such estimates.

## 3. (SC) for hyperbolic measures, and in dimension <= 3

Call mu *hyperbolic* if all Lyapunov exponents of g_1 with respect to mu, except the one in the flow direction, are nonzero. Let chi_*(mu) be the least absolute value of these transverse exponents.

**Fact K (cited from memory; NOT verified here).** Let X be a C^2 vector field on a compact manifold. Let mu be an ergodic, hyperbolic invariant probability of the flow with positive entropy that is not carried by Zero(X). Then for every eps > 0 there is a hyperbolic periodic orbit gamma with the following properties:
- gamma has a transverse homoclinic orbit;
- the transverse Floquet exponents of gamma, counted with multiplicity and ordered, are eps-close to the transverse exponents of mu.

Sources as I remember them:
- Katok, Publ. Math. IHES 51 (1980): horseshoes and closing for C^{1+alpha} diffeomorphisms, with remarks on flows;
- Lian–Young (JAMS 2012): horseshoes for hyperbolic measures of flows and semiflows;
- Wang–Sun (TAMS 2010): exponents of hyperbolic measures approximated by those of periodic orbits, for diffeomorphisms.
I am not certain that the exponent-approximation part is stated in the literature for flows.

A weaker form suffices: a hyperbolic periodic orbit with a homoclinic orbit, chi_*(gamma) >= c > 0 for some c independent of eps, and |I/P - mu(d)| < eps. Katok's closing lemma inside a Pesin block gives the last two properties. The periodic orbit shadows a mu-generic segment of length P, so |I/P - J_P(x)/P| is at most the modulus of continuity of d at the shadowing distance. Katok's horseshoe argument gives the homoclinic orbits.

**Theorem 3 (proved modulo Fact K).** Let mu satisfy the hypotheses of (SC) and be hyperbolic. Then (CP) holds, so (SC) holds for this mu.

*Proof.*
1. *mu is not carried by Zero(X).* g_1 is the identity on Zero(X), so a measure carried by Zero(X) has entropy 0. Hence mu(Zero(X)) = 0 by ergodicity.
2. *Sum of the exponents.* int J_1 dmu = mu(d), by Fubini and invariance, so mu(d) = 0. By Oseledets and Birkhoff, the sum of all exponents of g_1 equals lim (1/k) log det_nu Dg_k = lim J_k/k = mu(d) = 0. The flow-direction exponent is 0, because |X| is bounded and, by recurrence, |X(g_k x)| >= c > 0 for infinitely many k. So the transverse exponents sum to 0.
3. *Choice of gamma.* Apply Fact K with eps < chi_*(mu)/n. Then
|I|/P = |sum_i chi_i(gamma)| <= |sum_i chi_i(mu)| + (n-1)eps = (n-1)eps < chi_*(mu) - eps <= chi_*(gamma).
4. *Conclusion.* A transverse homoclinic orbit gives infinitely many homoclinic orbits (Smale–Birkhoff, cited), in particular two. Proposition 2(a) applies. ∎

**Corollary 3' (proved modulo Fact K and Ruelle's inequality).** If dim M <= 3, (SC) holds. (If dim M = 2 its hypotheses are never met.)

*Proof.* Let mu be as in (SC). By step 1 above, mu is not carried by zeros, so the flow-direction exponent is 0.

Ruelle's inequality (cited) applied to g_1 and to g_{-1} gives 0 < h_mu(g_1) <= sum of the positive exponents. With g_{-1} it also gives 0 < sum of |negative exponents|. So mu has a positive and a negative exponent, besides the zero flow exponent.
- If n = 2, this needs three exponents. That is impossible, so h_mu(g_1) = 0 and the hypotheses are void.
- If n = 3, the exponents are exactly (+, 0, -), so mu is hyperbolic and Theorem 3 applies. ∎

So a counterexample to (SC) needs dim M >= 4 and a mu with a zero transverse exponent.

## 4. What a counterexample must look like (consequences of Sections 1-3)

A counterexample (M, X, nu, mu) to (SC) must satisfy all of the following. The (P) items are proved; the (K) items also depend on Fact K.

(P1) dim M >= 4, and mu is not hyperbolic: some transverse exponent of mu vanishes (Corollary 3').

(P2) Every hyperbolic periodic orbit gamma with at least two homoclinic orbits satisfies |int_gamma d| / P >= chi_*(gamma). This is the dissipation measured against the weakest Floquet exponent (Proposition 2(a)).

(P3) Every hyperbolic zero p with at least two homoclinic orbits satisfies |tr DX(p)| >= chi_*(p) (Proposition 2(b)).

(K1) Every ergodic hyperbolic invariant probability m with h_m > 0 satisfies |m(d)| >= chi_*(m). In words, the sum of its transverse exponents is at least, in absolute value, the smallest of their absolute values.
*Proof from Fact K.* Suppose |m(d)| < chi_*(m). Choose eps > 0 with |m(d)| + (n-1)eps < chi_*(m) - eps. The periodic orbit gamma given by Fact K then has |I|/P < chi_*(gamma), and (P2) fails. (Step 2 of Theorem 3 gives m(d) = sum of the transverse exponents of m, without assuming m(d) = 0.)

In particular, the "obvious" positive-entropy dynamics must either be absent from M or be strongly dissipative in the sense of (K1)-(P3). Wherever it is weakly dissipative, the conclusion of (SC) already holds, however small the region of M it occupies. The extreme case of (K1) is a flow with **no hyperbolic ergodic measure at all**, e.g. one in which every invariant measure has a zero transverse exponent. The most natural flows of this kind are isometric extensions of hyperbolic flows. These are the candidates suggested in the task, and Section 5 examines them.

## 5. A natural candidate class with no hyperbolic measures, where the conclusion of (SC) still holds

**Setting.**
- A in SL(2,Z) is hyperbolic, with eigenvalues lambda > 1 > lambda^{-1} and unit eigenvectors e_u, e_s.
- N is the suspension of A with roof 1: N = T^2 x [0,1] / (x,1) ~ (Ax,0). Its flow is phi_t, generated by Y = d/ds.
- M := N x T^1 with T^1 = R/Z, and X := Y + psi d/dtheta, where psi in C^inf(N) is ARBITRARY.

The flow is g_t(y, theta) = (phi_t y, theta + S_t(y)) with S_t(y) = int_0^t psi(phi_r y) dr. Here d is computed with nu = dx ds dtheta.

**Why this class is a genuine test case.**
- div_nu X = 0, so J ≡ 0.
- nu-hat := nu/nu(M) is invariant and h_{nu-hat}(g_1) = log lambda > 0. (The extension is isometric, so it adds no entropy: Abramov–Rokhlin, cited.)
- By Jacobs' theorem some g_1-ergodic component mu of nu-hat has h_mu(g_1) > 0, and int J_1 dmu = 0. So the hypotheses of (SC) hold.
- Dg_t(d/dtheta) = d/dtheta, so every invariant measure has a zero exponent in the theta-direction. Hence no measure is hyperbolic; Theorem 3 and (K1) are unavailable; and no periodic orbit is hyperbolic, so Proposition 2 is unavailable.
- For psi that is not cohomologous to a constant, the strong foliations of X are not jointly integrable. So this is not the case A x R_alpha mentioned in the task.

**Proposition 5 (proved).** For every psi, the flow above satisfies (CP). Hence (SC) holds for it.

*Notation.* For y = (x, s) in N (s in [0,1)) and alpha, beta real, write y + (alpha, beta) := (x + alpha e_u + beta e_s, s). Then phi_r(y + (alpha, 0)) is phi_r(y) displaced by lambda^{floor(s+r)} alpha along e_u, at the same level, and likewise with lambda^{-floor(s+r)} beta along e_s. Put
H^u(y, alpha) := int_{-inf}^0 [psi(phi_r(y+(alpha,0))) - psi(phi_r y)] dr,
H^s(y, beta) := - int_0^inf [psi(phi_r(y+(0,beta))) - psi(phi_r y)] dr.
Both integrals converge absolutely: the integrands are at most Lip(psi) c lambda^{-|floor(s+r)|}|alpha| (resp. |beta|), where c compares flat displacement with Riemannian distance. By dominated convergence H^u and H^s are jointly continuous. Define maps of M:
U_alpha(y, theta) := (y + (alpha,0), theta + H^u(y, alpha)),  S_beta(y, theta) := (y + (0,beta), theta + H^s(y, beta)).

**Lemma 5.1.** Fix delta_0 > 0 small, so that (alpha, beta) -> x + alpha e_u + beta e_s mod Z^2 is injective on |alpha|, |beta| < 4 delta_0 and the comparison constant c is valid there. There is C >= 1 such that for every w in M and |alpha|, |beta| < 4 delta_0, with theta := log lambda:
(a) d(g_t w, g_t U_alpha w) <= C e^{-theta|t|} d(w, U_alpha w) for t <= 0;
(b) d(g_t w, g_t S_beta w) <= C e^{-theta t} d(w, S_beta w) for t >= 0;
(c) U_{alpha'} U_alpha = U_{alpha+alpha'} and S_{beta'} S_beta = S_{beta+beta'}, and both commute with the fibre translations (y, theta) -> (y, theta + c).

*Proof.*
(c) The integrals telescope, and the fibre coordinate enters only additively.
(a) Let t <= 0. The base points of g_t w and g_t U_alpha w are at distance at most c lambda^{floor(s+t)}|alpha| <= c lambda e^{-theta|t|}|alpha|. The difference of their fibre coordinates is
H^u(y, alpha) - int_t^0 [psi(phi_r(y+(alpha,0))) - psi(phi_r y)] dr = int_{-inf}^t [...] dr,
of absolute value at most Lip(psi) c |alpha| lambda^{s+t}/theta. Finally d(w, U_alpha w) >= c^{-1}|alpha|.
(b) is symmetric. ∎

**Rectangles.** For w = (y, theta) put R_{a,b} := S_{-b} U_{-a} S_b U_a. The base point returns to y, so by (c),
R_{a,b}(y, theta) = (y, theta + D(a,b)), with
D(a,b) = H^u(y,a) + H^s(y+(a,0), b) + H^u(y+(a,b), -a) + H^s(y+(0,b), -b).
D is real-valued and continuous on [0, delta_0)^2. By (c), D(0, b) = D(a, 0) = 0. (D need not be differentiable: H^s is in general not smooth in the e_u-direction, so no Sard argument is used.)

**Lemma 5.2 (an uncountable level set).** There is c_* such that K := {(a,b) in (0, delta_0)^2 : D(a,b) = c_*} is uncountable.

*Proof.*
- If D ≡ 0 on the open square, take c_* = 0.
- Otherwise D is non-constant on the square, because it tends to 0 at the edge a = 0. Its image is then an interval with nonempty interior. Take c_* in the interior. If K were countable, the square minus K would be connected. (An open connected planar set minus a countable set is path connected: join two points by a polygonal path and replace each segment by one of uncountably many pairwise-disjoint two-segment detours, only countably many of which meet K.) But D - c_* is continuous and nonvanishing there and takes both signs, a contradiction. ∎

**The chains.** Fix x_0 = (y_0, theta_0), y_0 = (xbar, s_0), and K from Lemma 5.2 for y = y_0. For p_1 = (a_1, b_1) and p_2 = (a_2, b_2) in K, define the sequence (a_i) by
a_0 = x_0, a_1 = U_{a_1} a_0, a_2 = S_{b_1} a_1, a_3 = U_{-a_1} a_2, a_4 = S_{b_2 - b_1} a_3, a_5 = U_{a_2} a_4, a_6 = S_{-b_2} a_5, a_7 = U_{-a_2} a_6, and a_i = a_7 for i >= 7.

By (c), S_{-b_1} a_3 = R_{p_1} x_0 = (y_0, theta_0 + c_*). The legs from there are the rectangle R_{p_2} traversed backwards, i.e. U_{-a_2} S_{-b_2} U_{a_2} S_{b_2} = R_{p_2}^{-1}, which subtracts D(p_2) = c_* from the fibre. Hence a_7 = x_0 EXACTLY. The legs alternate u, s, u, s, ... as (L1)/(L2) require, starting with a u-leg (Lemma 5.1(a),(b)); the legs from index 7 on have length 0. The base points of the vertices, in the coordinates (alpha, beta) around xbar at level s_0, are
(0,0), (a_1,0), (a_1,b_1), (0,b_1), (0,b_2), (a_2,b_2), (a_2,0), (0,0).
The second sequence (b_i) is built in the same way from p_3, p_4 in K.

Then:
- (L1), (L2) hold with C from Lemma 5.1 and theta = log lambda.
- (L3) holds: the chains are finite.
- (L4) holds with C' = 0 and eta = 0 < theta, since J ≡ 0.
- (E) holds with p = x_0 and tau = 0.
It remains to choose p_1, ..., p_4 so that v_1 := a_2 (base (a_1,b_1)) and v_3 := the corresponding vertex of (b_i) (base (a_3,b_3)) are orbit-isolated.

**Orbit relations.** g_r preserves the level s_0 only for integer r. For m ≠ 0, A^m(xbar + alpha e_u + beta e_s) = xbar + alpha' e_u + beta' e_s mod Z^2 holds iff there is k in Z^2 with
alpha' = lambda^m alpha - u_{m,k},  beta' = lambda^{-m} beta - s_{m,k},
where A^m xbar - xbar + k = u_{m,k} e_u + s_{m,k} e_s for a fixed lift. Call this affine map Phi_{m,k}.

The vertex with base (a_i, b_i) is orbit-isolated if all of the following hold:
- (a_i, b_i) differs from every other base point in the combined list (then it occurs once, since distinct small parameters give distinct points);
- Phi_{m,k}(a_i, b_i) is not the base parameter of any vertex, for all m ≠ 0 and all k. This also covers non-periodicity, including Phi_{m,k}(a_i,b_i) ≠ (a_i,b_i), and the limit point x_0, whose base is (0,0).
X has no zeros. A periodic point of M has an A-periodic base, and that case is covered by the second item.

The conditions Phi_{m,k}(p_i) in {(0,0), (a_i,0), (0,b_i), (a_i,b_i)} each have exactly one solution p_i, because lambda^m ≠ 1. They exclude a countable set Sigma.

For another index j:
- Phi_{m,k}(p_i) = p_j excludes one point p_j;
- Phi_{m,k}(p_i) = (a_j, 0) forces b_i = lambda^m s_{m,k} and then excludes the vertical line a_j = lambda^m a_i - u_{m,k};
- Phi_{m,k}(p_i) = (0, b_j) forces a_i = u_{m,k}/lambda^m and then excludes the horizontal line b_j = lambda^{-m} b_i - s_{m,k}.

Let B := {lambda^m s_{m,k}} and A := {u_{m,k}/lambda^m}, both countable. Choose p_1, p_2, p_3, p_4 in this order. For j = 3 the conditions against the already chosen p_1, p_2 fix both coordinates of p_3, so they are point conditions.

*Choice.*
- Case 1: K' := K \ ((A x R) ∪ (R x B)) is uncountable. Take p_1, p_3 in K' \ Sigma and all p_j pairwise distinct. No line exclusions are triggered, and each step excludes only countably many points of the uncountable set K'.
- Case 2: otherwise K \ K' is uncountable, so some line l = {a = alpha*} (alpha* in A) or {b = beta*} (beta* in B) meets K in an uncountable set. Say l is vertical; the horizontal case is symmetric. Choose all p_j in K ∩ l \ (R x B), which is still uncountable. Since b_i is not in B, no vertical line is excluded. The horizontal lines that may be excluded meet l in one point each. So again only countably many points of an uncountable set are excluded at each step.

With these choices v_1 and v_3 are orbit-isolated, and Lemma-1-style bookkeeping gives all clauses of (CP). ∎

**What the proof shows about the mechanism.**
- The task suggested isometric extensions where every su-loop has a nonzero centre defect "of a fixed sign or in a discrete-but-nonclosing set". Neither can block (CP) by itself. Defects of su-loops in an isometric (abelian) extension are continuous functions of the loop's corners. So two DIFFERENT loops with the same defect exist as soon as the family of loops has more parameters than the centre fibre has dimensions. Running one loop forward and the other backward closes exactly.
- The clause "occurs exactly once" blocks only the degenerate version, a loop followed by itself reversed (and commutator words). It does not block concatenating two distinct loops on the same level set of the defect.
- A fixed-sign defect is impossible: the reversed loop has the opposite defect, and (L1), (L2) are symmetric in the endpoints of a leg. A "discrete" defect set is impossible too: a continuous defect on a connected family is constant on the family.

## 6. The general mechanism, and where it stops (sketch, not proved)

**Mechanism (two paths, same endpoint).** Suppose that at some x_0 there are two su-paths P and P' from x_0 with the same endpoint, or with endpoints on a common strong-stable leaf. Suppose also that P has a corner vertex that is new: its orbit avoids the vertices of P' and of P. Then P followed by P' reversed is an admissible chain closing with tau = 0. (Reversal is legitimate because (L1) and (L2) are symmetric in the two endpoints of a leg.)

In a *uniformly* partially hyperbolic flow (TM = E^s + E^c + E^u, with X in E^c, E^s and E^u nontrivial, and continuous strong foliations), su-paths with 2m small legs near x_0 form a continuous family. It is parametrised by an open set of R^{m(u+s)}, and the endpoint map goes to the n-manifold M. Once m(u+s) > n, this map is not injective on any open set. (A continuous injection from an open subset of R^{n+1} into an n-manifold would contradict invariance of domain.) So pairs of distinct paths with the same endpoint always exist. If the flow also has a smooth invariant volume, then J is bounded and (L4) holds with eta = 0.

What is missing for a full proof in this generality is the general-position step: choosing the pair so that some corner is orbit-isolated. Section 5 carried this out by hand when the base is linear and the centre fibre is a circle. In general the endpoint map is only continuous, so transversality arguments do not apply directly. Hurewicz's dimension-lowering theorem (cited) gives a fibre of dimension >= m(u+s) - n, which is a plausible starting point. **Status: sketch.** I expect (CP) to hold for every volume-preserving, uniformly partially hyperbolic flow with u, s >= 1, but I have not proved it.

**Why the non-uniform case is genuinely open.** In the situation left by (P1)/(K1), mu has positive entropy and a zero transverse exponent, and M has no weakly dissipative hyperbolic dynamics. Pesin theory gives strong stable and unstable manifolds only for mu-typical points. Points on W^{uu}(x_0) are in general not mu-typical: for non-SRB mu, the conditional measures on unstable leaves are singular. So W^{ss} of the second vertex may not exist with any uniform rate. The continuous families used above are then unavailable. Katok-type closing needs hyperbolicity in every transverse direction, and the zero exponent destroys it. Neither a construction of the chains nor a proof of their absence is available in this setting. A counterexample would have to live here, and it would have to control the strong sets of ALL points of M, not just mu-typical ones. I could not build one.

## 7. Summary

**Proved here.**
1. Lemma 1: a two-leg homoclinic configuration at any point implies (CP), the conclusion of (SC). (CP) does not involve mu.
2. Proposition 2: (CP) holds whenever M has a hyperbolic periodic orbit with two homoclinic orbits and |int_gamma d|/P < chi_*(gamma), or a hyperbolic zero with two homoclinic orbits and |tr DX(p)| < chi_*(p). The rate condition is needed: (L4) requires eta < theta.
3. Proposition 5: (CP), and hence (SC), holds for every isometric circle extension X = d/ds + psi d/dtheta of the constant-roof suspension of a hyperbolic toral automorphism, for every smooth psi. This class meets the hypotheses of (SC) and has no hyperbolic invariant measure at all. The chains are two distinct su-rectangles with equal centre defect, one traversed backwards, chosen in general position by a countability argument. This disposes of the "isometric extension with nonzero defects" candidate in this sub-class, and shows why fixed-sign or discrete defects cannot occur.

**Proved modulo cited results** (Fact K, a Katok/Lian–Young/Wang–Sun-type horseshoe and exponent-approximation theorem for flows, quoted from memory; I am unsure of the exact flow statement in the literature; and Ruelle's inequality):
4. Theorem 3: (SC) holds for every hyperbolic mu.
5. Corollary 3': (SC) holds when dim M <= 3; for dim M = 2 its hypotheses are void.
6. The necessary conditions (P1)-(P3) and (K1) for a counterexample (Section 4).

**Sketched only.** (CP) for volume-preserving, uniformly partially hyperbolic flows, with the general-position step missing (Section 6).

**Open questions.**
- (Q1) Is (SC) true when mu has a zero transverse exponent and M carries no weakly dissipative hyperbolic dynamics (the case left by (P1)-(P3), (K1))? Neither a proof nor a counterexample is known to me.
- (Q2) The flow statement of Fact K with exponent approximation, i.e. the exact reference.
- (Q3) The general-position step of Section 6, including torus fibres T^k with k >= 2, where the defect map goes to R^k and Lemma 5.2 must be replaced by a dimension argument.

**Consequence for the chain of this attempt.** No counterexample to (SC) was found. The natural candidates (products, jointly integrable systems, isometric circle extensions of linear suspensions, hyperbolic measures) all satisfy (SC). The remaining risk is concentrated in non-uniformly hyperbolic flows with zero transverse exponents. That is the same territory where (PE0) was stuck, so (SC) does not avoid that difficulty: it moves it from "entropy" to "existence of closing su-chains" in that case.

=== END OF ANSWER round14_q4 ===

