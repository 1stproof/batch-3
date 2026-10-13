# round14_q1 — answer

## Status in one paragraph
I could neither prove the missing statement (SC) in general nor find a counterexample to it, and I did not find a direct proof of the problem's claim. Below are: (0) a structural remark: the conclusion of (SC) does not mention mu, so mu only certifies existence; (1) **Proposition H (fully proved, using only the classical stable-manifold theorem for hyperbolic periodic orbits):** the conclusion of (SC) holds for **every** smooth flow that has a hyperbolic periodic orbit gamma with |I(gamma)|/P(gamma) < kappa(gamma) (weakest hyperbolic rate) and two distinct homoclinic orbits; (2) **Corollary H' (proved modulo a cited flow version of Katok's horseshoe theorem with measure and exponent control):** (SC) holds when mu is hyperbolic. By R6-a Theorem 5.1 (quoted in the brief) this case never occurs under GH, so it adds nothing to the chain; it is reported only as the sub-class result it is. (3) **Proposition P (proved):** a test family that Proposition H cannot handle: products X = (Y, alpha) on N x T^k (alpha with two nonzero, rationally independent components; Y with a hyperbolic horseshoe). For these, (SC) is **equivalent** to a statement about Y alone: exact *zero-time* return of an su-chain to W^ss(y_0). This isolates the "temporal-drift steering" problem that any proof of (SC) has to solve, even in a uniformly hyperbolic base. (4) What is open.

I did not re-verify Theorem IC2 (Block R13-a) or Block R11-a; I read only the parts of the brief quoted at the top and the R6-a block. Granting those, I see no logical gap in the chain as stated: step 3 feeds exactly the hypotheses of IC2, with the same constants for both chains. But I did not check that against IC2's exact wording.

---

## 0. Remark: (SC) is a pure existence statement for the flow
The conclusion of (SC) (the point x_0, the two chains, (L1)–(L4), (E), orbit-isolated vertices) never mentions mu. So (SC) is equivalent to:

> (SC') Every smooth flow on a compact manifold of dimension >= 2 that admits a g_1-ergodic mu with h_mu(g_1) > 0 and int J_1 dmu = 0 admits a configuration (x_0; (a_i), (b_i)) as in (SC).

So a counterexample has to be a flow with such a mu and **no configuration anywhere in M**, not even far from supp mu. By Proposition H, such a flow has no hyperbolic periodic orbit gamma with two homoclinic orbits and |I(gamma)| < kappa(gamma) P(gamma). By Corollary H' (and the cited horseshoe theorem), it has no hyperbolic ergodic measure of positive entropy with mu(d) = 0.

---

## 1. Proposition H (configurations from one hyperbolic periodic orbit)

**Notation.** Let gamma be a periodic orbit of minimal period P > 0, and x_0 in gamma. gamma is *hyperbolic* if the linear map induced by Dg_P(x_0) on T_{x_0}M / R X(x_0) has no eigenvalue of modulus 1. We assume that both the stable part (eigenvalues of modulus < 1) and the unstable part are nontrivial. Put
- kappa_s := min{ -log|sigma| : sigma a stable eigenvalue } / P > 0,
- kappa_u := min{ log|sigma| : sigma an unstable eigenvalue } / P > 0,
- kappa(gamma) := min(kappa_s, kappa_u),
- I(gamma) := J_P(x_0) = int_0^P d(g_s x_0) ds, which is independent of x_0 in gamma.

For x in gamma and theta in (0, kappa(gamma)) define
- W^ss(x) := { y : sup_{t>=0} e^{theta t} d(g_t y, g_t x) < infinity },
- W^su(x) := { y : sup_{t<=0} e^{theta|t|} d(g_t y, g_t x) < infinity }.

**Cited [SM]** (classical stable manifold theorem for a hyperbolic periodic orbit; from memory). These sets do not depend on theta in (0, kappa). W^s(gamma) := { y : dist(g_t y, gamma) -> 0 as t -> +inf } equals the union of the W^ss(x) over x in gamma, and likewise W^u(gamma) is the union of the W^su(x). Also g_s W^ss(x) = W^ss(g_s x) and g_s W^su(x) = W^su(g_s x). (The last two statements are immediate from the definitions, because g_s is Lipschitz on M with a constant depending only on s.)

A *homoclinic point* of gamma is a point h not in gamma with h in W^s(gamma) ∩ W^u(gamma).

**Proposition H.** Let X be a smooth vector field on a compact manifold M of dimension n >= 2 (no further assumption). Suppose X has a hyperbolic periodic orbit gamma with
 (J) |I(gamma)| < kappa(gamma) P,
and two homoclinic points h, h' of gamma lying on different orbits. Then the conclusion of (SC) holds: there are C, theta, eta, C', x_0 and two chains satisfying (L1)–(L4), (E), each with an orbit-isolated vertex.

*Proof.*
1. *Constants.* Put eta := |I(gamma)|/P and fix theta with eta < theta < kappa(gamma). Then 0 <= eta < theta, as (SC) requires. Fix x_0 in gamma.

2. *Moving the homoclinic points onto W^su(x_0).* By [SM] there are a, b in R with h in W^su(g_a x_0) ∩ W^ss(g_b x_0). Put q := g_{-a} h and c := b - a. Then q is in W^su(x_0) ∩ W^ss(g_c x_0), q is not in gamma, and q lies on the orbit of h. In the same way, h' gives q' in W^su(x_0) ∩ W^ss(g_{c'} x_0), with q' not in gamma and q' on the orbit of h'. Hence q and q' lie on different orbits, and neither orbit meets gamma.

3. *q is neither a zero nor periodic.* Suppose g_T q = q for some T > 0 (this covers zeros too, which are fixed by every g_T). Then d(q, g_{-mT} x_0) = d(g_{-mT} q, g_{-mT} x_0) -> 0 as m -> inf, because q is in W^su(x_0). Since gamma is closed, q would lie in gamma, which is false. The same holds for q'.

4. *The chains.* Define
 a_0 = x_0, a_1 = q, a_i = g_c x_0 for i >= 2;
 b_0 = x_0, b_1 = q', b_i = g_{c'} x_0 for i >= 2.
 Only legs 0 and 1 have positive length; all later legs are constant, which is allowed.

5. *(L1), (L2), (L3).* For chain (a_i): leg 0 joins x_0 to q in W^su(x_0). So there is C_q with d(g_t x_0, g_t q) <= C_q e^{-theta|t|} for t <= 0. Since d(x_0, q) > 0, this reads d(g_t x_0, g_t q) <= (C_q / d(x_0,q)) e^{-theta|t|} d(x_0, q). Leg 1 joins q to g_c x_0, and q is in W^ss(g_c x_0). So d(g_t q, g_t g_c x_0) <= C''_q e^{-theta t} for t >= 0, which gives the analogous inequality with constant C''_q / d(q, g_c x_0). Here q ≠ g_c x_0 because q is not in gamma. For the constant legs both sides of (L1) and (L2) vanish. Do the same for chain (b_i) and let C be the largest of the four constants (and at least 1). (L3) holds because the sums are finite. The limit points are p = g_c x_0 and p' = g_{c'} x_0.

6. *(E).* Take tau = c. Then d(g_t p, g_{t+c} x_0) = 0 for all t. Similarly tau' = c' for (b_i).

7. *(L4).* For x in gamma and real t, write t = kP + r with k in Z and r in [0, P). The cocycle identity and g_{kP} x = x give J_t(x) = k I(gamma) + J_r(x). Also |J_r| <= P ||d||_inf, and k I = (t - r) I / P with |r I / P| <= |I| <= P ||d||_inf. Hence
 J_t(x) <= 2P ||d||_inf + eta |t| for all real t and all x in gamma.
 For q and t >= 0: |J_t(q) - J_t(g_c x_0)| <= int_0^t Lip(d) d(g_s q, g_s g_c x_0) ds <= Lip(d) C''_q / theta. So J_t(q) <= C' + eta t for t >= 0, with C' := 2P ||d||_inf + Lip(d) max(C''_q, C''_{q'}) / theta. Now check every vertex:
 - the even-index vertices x_{2i} are x_0 (i = 0) or points of gamma (i >= 1), so the bound for t <= 0 holds;
 - the odd-index vertices x_{2i+1} are q or q' (i = 0) or points of gamma (i >= 1), so the bound for t >= 0 holds;
 - J_t(x_0) <= C' + eta t for t >= 0 holds since x_0 is in gamma.

8. *Orbit-isolated vertices.* The combined vertex list consists of x_0, q, q', and points of gamma. For (a_i) take v = q:
 - v ≠ x_0;
 - q occurs exactly once, because q ≠ q' (different orbits) and q is not in gamma;
 - q is neither a zero nor periodic, by step 3;
 - the orbit of q contains no other vertex and neither limit point: the other vertices and both limit points lie on gamma or on the orbit of q', and the orbit of q is disjoint from both.
 Symmetrically, v' = q' works for (b_i). ∎

**Remark H.1.** Under GH, Proposition H is consistent with the rest of the ledger: R6-a Corollary 4.2 says that under GH no hyperbolic periodic orbit has a homoclinic point at all.

---

## 2. Corollary H' (hyperbolic measures)

**Cited [KH-flow]** (Katok's horseshoe/approximation theorem, flow version; from memory. For diffeomorphisms it is Katok, Publ. IHES 51 (1980) and Katok–Hasselblatt, Supplement S.5; for C^2 flows in any dimension I attribute it to Lian–Young, with weak-* and exponent control as in the diffeomorphism case. **I have not checked that the flow version in the literature contains (ii) and (iii) in exactly this form; this is the weakest point of H'.**) Let mu-bar be a flow-ergodic invariant probability of a C^2 flow with h(g_1) > 0, mu-bar(Zero X) = 0, and all exponents nonzero except the flow direction. Let chi_min > 0 be the smallest absolute value of these nonzero exponents. Then for every eps > 0 there is a compact invariant hyperbolic set Lambda with the following properties:
 (i) the flow on Lambda is conjugate to a suspension of a transitive subshift of finite type with positive entropy;
 (ii) every invariant probability on Lambda is eps-close to mu-bar on a prescribed finite set of continuous functions;
 (iii) on Lambda the strong stable and strong unstable rates are at least chi_min - eps. In particular kappa(gamma) >= chi_min - eps for every periodic orbit gamma in Lambda.

**Corollary H'.** If the mu of (SC) is hyperbolic (all exponents of g_1 nonzero except the flow direction), the conclusion of (SC) holds.

*Proof.*
- Put mu-bar := int_0^1 (g_s)_* mu ds. It is flow-invariant, and flow-ergodic because mu is g_1-ergodic. As noted in R6-a §5, h_{mu-bar}(g_1) = h_mu(g_1) > 0. mu-bar has the same exponents as mu, and mu-bar(d) = int J_1 dmu = 0. Also mu-bar(Zero X) = 0, since otherwise h = 0.
- Apply [KH-flow] with eps < chi_min / 2 and the test function d. Pick a periodic orbit gamma in Lambda. Its normalised orbit measure m_gamma satisfies m_gamma(d) = I(gamma)/P, so |I(gamma)|/P < eps < chi_min - eps <= kappa(gamma). This is (J).
- In the symbolic model, a periodic point has infinitely many homoclinic points on pairwise distinct orbits. Take sequences equal to the periodic sequence outside a window, filled inside the window with distinct admissible loops, which exist by transitivity and positive entropy.
- By hyperbolicity of Lambda (local product structure, shadowing), a point of Lambda whose symbolic forward (backward) tail agrees with the periodic one lies in W^s(gamma) (W^u(gamma)).
- Proposition H applies. ∎

Under GH this case is empty (R6-a Theorem 5.1). So Corollary H' gives the chain nothing new. It shows only that the (SC) problem lives entirely in the non-hyperbolic world, which the planner already knew.

---

## 3. Proposition P: a test family where single loops fail, and what (SC) means there

Let Y be a smooth vector field on a compact manifold N with flow phi_t. Let alpha in R^k (k >= 2) have two nonzero coordinates alpha_1, alpha_2 with alpha_1/alpha_2 irrational. On M = N x T^k with the product Riemannian metric, put X = (Y, alpha), so that g_t(y, th) = (phi_t y, th + t alpha). Take nu = nu_N x Leb; then d_X(y, th) = d_Y(y). If mu_Y is phi_1-ergodic with positive entropy and int J_1 dmu_Y = 0, then mu = mu_Y x Leb is g_1-invariant with h_mu(g_1) >= h_{mu_Y}(phi_1) > 0 (it has the factor mu_Y) and int J_1 dmu = 0. Ergodicity of mu for g_1 can be arranged by choosing alpha generic with respect to the eigenvalues of phi_1; otherwise use an ergodic component, which still projects to mu_Y. This product flow is a legitimate test case for (SC).

**Proposition P (proved).**
(a) X has no zeros and no periodic orbits. So Proposition H never applies to X.
(b) In any chain for X satisfying (L1), (L2), all vertices and the limit p have the same T^k-coordinate as x_0.
(c) If (E) holds for such a chain, then tau = 0, and the N-components satisfy d_N(phi_t p_N, phi_t y_0) <= C e^{-theta t} for t >= 0, where x_0 = (y_0, th_0).
(d) Hence a configuration for X exists iff Y admits a point y_0 and two chains satisfying (L1)–(L4) in N, with the following properties:
 - their limit points lie in the **strong** stable set of y_0 itself (zero time shift);
 - each chain has a vertex v ≠ y_0 that occurs once in the combined list and differs from both limit points.
 In X the orbit-isolation condition reduces to this. The Jacobian conditions are unchanged because d_X = d_Y.

*Proof.*
(a) A zero would need alpha = 0. If g_T(y, th) = (y, th) with T ≠ 0, then T alpha is in Z^k, so T alpha_1 and T alpha_2 are nonzero integers and alpha_1/alpha_2 is rational, which is false.
(b) The T^k-distance between g_t(y, th) and g_t(y', th') equals dist_{T^k}(th, th') for all t, because rotation is an isometry. The product distance dominates it. So (L1) or (L2) with right-hand side tending to 0 forces th = th'.
(c) (E) gives dist_{T^k}(th_0, th_0 + tau alpha) <= C e^{-theta t} -> 0, so tau alpha is in Z^k, and tau = 0 as in (a). Then the N-part of (E) reads d_N(phi_t p_N, phi_t y_0) <= C e^{-theta t}.
(d) "If": lift the vertices with th = th_0. (L1)–(L3) transfer because d_M ≍ d_N on a fixed T^k-slice. (L4) is unchanged. For the orbit-isolated vertex v = (v_N, th_0):
 - g_t v has T^k-coordinate th_0 + t alpha, which equals th_0 only for t = 0. So the orbit of v contains a point of the slice {th = th_0}, where all vertices and limit points lie, only at t = 0. The orbit condition therefore reduces to "v is no other vertex and no limit point".
 - v is never a zero or periodic, by (a).
 "Only if": project, using (b) and (c). ∎

**Consequence.** For a product with Y uniformly hyperbolic (say Y has a horseshoe Lambda_Y with periodic orbits satisfying (J)), (SC) for X is the statement: *some y_0 carries two non-backtracking su-chains whose limits lie exactly in W^ss(y_0), with zero time shift.*

When it is easy:
- If the strong foliations of Y are jointly integrable near Lambda_Y, the temporal distance vanishes. Example: a suspension with constant roof, where W^ss and W^su lie in the level sets of the suspension coordinate. Then a homoclinic point q in W^su(y_0) ∩ W^ss(y_0) with zero phase exists (take a symbolic homoclinic sequence at the same phase), and (d) is satisfied as in Proposition H with c = 0.

When it is not easy:
- In general every homoclinic point of a periodic y_0 has a phase c(q) in R/PZ, and these phases form a countable set that need not contain 0. Then no finite chain of the form used in Proposition H works.
- What is needed is **steering of the temporal drift to exactly 0**: a summable chain made of small su-quadrilaterals whose temporal drifts, of both signs, add up to the required correction.
- Both signs are available: running a quadrilateral backwards, preceded by a constant u-leg, reverses the sign of its drift.
- I expect a greedy argument to work when the set of drift values at scale r has bounded gap ratios, as it does for horseshoes with bounded geometry. I have **not** written such a proof: one needs control of the nonlinear (second-order) error terms of the drift and of exact convergence of the limit point into W^ss(y_0).
- This is exactly Prop CP of Block R13-a in the simplest possible setting: one centre dimension, the flow direction, with a uniformly hyperbolic base. It is a natural first test for the planner's step (1).

So even in this uniformly hyperbolic product family (SC) is not trivial. I could neither prove it nor refute it there. A counterexample in this family would need a horseshoe for Y in which no summable chain has total temporal drift exactly 0. I found no mechanism forcing that, because both signs of drift occur at all small scales.

---

## 4. Dead ends checked on the way to a direct proof (recorded briefly)
- **Equicontinuity from the a priori estimate.** u(g_t x) - u(g_t y) = S_{x,y}((Xu) o g_t) with ||S_{x,y}||_{(C^m)'} <= C d(x,y) (Observation O1). Bounding this uniformly in t needs ||(Xu) o g_t||_{C^m} bounded, i.e. equicontinuity already. Circular.
- **Spectral route (volume case).** With a smooth invariant volume, every smooth mean-zero f equals X u_j-iterates with tame bounds. So the spectral projection E_delta of the generator onto |lambda| < delta satisfies ||E_delta f||_{L^2} <= C_j delta^j ||f||_{H^{s_j}}, hence ||g||_{H^{-s_j}} <= C_j delta^j ||g|| on range(E_delta). Positive entropy gives a Lebesgue-spectrum component (Rokhlin; flow version cited from memory), but that is not contradicted unless some element of that component near lambda = 0 has a quantitative smooth approximation (polynomial rate in H^s with exponent beating s_j / 2j). I could not produce one.
- **Kozlovski's formula** (cited from memory: for C^inf maps, h_top(f) = lim (1/n) log int ||Lambda Df^n|| dvol). It reduces the goal to subexponential growth of int ||Lambda^k Dg_t|| dnu. I found no way to get that from GH. The lifted vector field on Grassmann bundles is never GH (functions on the fibre are invariant for linear torus flows), so GH cannot be transported there.

---

## 5. Summary: proved / cited / open
**Proved here:**
- Remark 0 ((SC) is equivalent to (SC'));
- Proposition H (every flow with a hyperbolic periodic orbit satisfying (J) and two homoclinic orbits has a configuration as in (SC));
- Proposition P (for products (Y, alpha) with alpha_1/alpha_2 irrational, (SC) is equivalent to zero-time-shift su-returns in the base; Proposition H never applies there).

**Proved modulo a citation:** Corollary H' ((SC) for hyperbolic mu), modulo [KH-flow] with weak-* and exponent control, whose exact flow formulation I have not verified. This case is empty under GH.

**Not checked:** Theorem IC2 (Block R13-a) and Block R11-a. I took them as stated, and under that assumption the chain steps 1–4 fit together.

**Open:**
1. (SC) in general, for non-hyperbolic mu.
2. Already open: (SC) for the product family of §3 with a non-jointly-integrable hyperbolic base. Concretely: does every hyperbolic horseshoe of a 3-dimensional flow carry a point y_0 with a non-backtracking summable su-chain ending exactly in W^ss(y_0)? A positive answer would be the first non-hyperbolic-measure instance of (SC). A negative answer for some horseshoe (made robust under the product with an irrational rotation) would be a GH-free counterexample to (SC), killing this decomposition.
3. The problem's claim in dimension >= 4 (by R6-a it is proved for dim M <= 3) remains open along this route.

=== END OF ANSWER round14_q1 ===
