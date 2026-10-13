# round6_q2 — answer

## Plan
I prove a new general GH-obstruction (Theorem G): under GH, no nonzero distribution can have a transfer orbit that decays exponentially in BOTH time directions. Then I build such distributions from finitely many points on one unstable leaf, weighted by divided-difference coefficients. This excludes:
- (i) the uniformly volume-contracting horseshoes (H3). Hence h_top = 0 in dimension <= 3, modulo the classical theorems already used in Theorem 4.1 of the background;
- (ii) every ergodic mu with h_mu > 0 and 0 < |sum of exponents| < (an exponent gap). This uses only Pesin theory and Ledrappier–Young;
- (iii) conditionally on normal-form theorems cited from memory: every hyperbolic mu with h_mu > 0 in any dimension, and every mu with h_mu > 0 and mu(d) != 0.

Open: non-hyperbolic ergodic mu with h_mu > 0 and mu(d) = 0, in dim >= 4.

Conventions are those of the brief. nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, and P phi = X phi + d phi. L_t phi := e^{J_t} (phi o g_t) is smooth in (t,x), and d/dt L_t phi = L_t(P phi). A "distribution density" is a continuous linear functional on C^inf(M).

## 1. Lemma Q (proved; GH)
Let S be a distribution density and c a constant such that S(P phi) = c nu(phi) for all smooth phi, where nu(phi) = int phi dnu. Then c = 0 and S = c' nu for some constant c'.

*Proof.* Define u by <u, phi nu> = S(phi). Then <Xu, phi nu> = -<u, L_X(phi nu)> = -S(P phi) = -c int phi dnu. So Xu = -c, which is smooth, and by GH u is smooth. At a maximum point p of u we have (Xu)(p) = 0, so c = 0. Then Xu = 0, so u is constant by L1, and S = u nu. ∎

## 2. Theorem G (proved; GH). No two-sided exponentially decaying transfer orbits
Assume GH. Let Theta be a distribution density, and suppose there are a > 0, k and C such that
  |Theta(L_t phi)| <= C e^{-a|t|} ||phi||_{C^k}   for all real t and all smooth phi.
Then Theta = 0.

*Proof.* Put c_phi(t) = Theta(L_t phi). This is C^1 in t: t -> L_t phi is a smooth curve in C^inf and Theta is continuous. Moreover c_phi' = c_{P phi}.

(a) For |Re z| < a set T_z(phi) = int_R e^{-zt} c_phi(t) dt. The integral converges absolutely, and |T_z(phi)| <= C ||phi||_{C^k} int e^{(|Re z| - a)|t|} dt. So T_z is a distribution density. The map z -> T_z(phi) is holomorphic on the strip, and its derivatives T_z^{(j)}(phi) = int (-t)^j e^{-zt} c_phi(t) dt are again distribution densities (dominated convergence).

(b) Integrating by parts on [-R,R] and letting R -> inf gives T_z(P phi) = z T_z(phi). The boundary terms e^{-zt} c_phi(t) tend to 0 because |Re z| < a. Differentiating j times in z:
  T_z^{(j)}(P phi) = z T_z^{(j)}(phi) + j T_z^{(j-1)}(phi).
At z = 0 this reads T_0^{(j)}(P phi) = j T_0^{(j-1)}(phi).

(c) We show by induction that T_0^{(j)} = c_j nu and c_{j-1} = 0.
- For j = 0, Lemma Q with c = 0 gives T_0 = c_0 nu.
- If T_0^{(j-1)} = c_{j-1} nu, then T_0^{(j)}(P phi) = j c_{j-1} nu(phi). Lemma Q gives c_{j-1} = 0 and T_0^{(j)} = c_j nu.

Hence T_0^{(j)} = 0 for every j. So for each phi the holomorphic function z -> T_z(phi) vanishes identically on the (connected) strip.

(d) On the line Re z = 0 this says int e^{-i omega t} c_phi(t) dt = 0 for all real omega. Since c_phi is in L^1 and continuous, Fourier uniqueness gives c_phi = 0. In particular Theta(phi) = c_phi(0) = 0, because L_0 = id. ∎

Remark. The planner's suggestion used the same Laplace-transform family. What is new here is the induction (c) on the Taylor coefficients at z = 0. It kills the family whenever 0 is an interior point of the strip of convergence. This handles the "cancellation" the planner worried about: T_0 = 0 is not the end of the argument, because it forces all higher Taylor coefficients to vanish too.

Equivalent form. With u = Theta/nu, Theta(L_t phi) = <u o g_{-t}, phi nu>. So Theorem G says that under GH, no nonzero generalized function u has <u o g_t, rho> = O(e^{-a|t|}) as t -> +-inf for all smooth densities rho, with uniform C^k control.

## 3. Theorem P (proved, modulo the cited Pesin, Oseledets and Ledrappier–Young theory). A gap condition
Cited facts (from memory):
- [Os] Oseledets: for an ergodic flow-invariant mu and mu-a.e. x, the Lyapunov exponents of g_1 exist; one of them is the flow direction exponent 0 when mu is not carried by a zero. The sum of all exponents is lim (1/t) J_t(x) = mu(d), because J_t is the log of the nu-Jacobian of g_t.
- [Rue] Ruelle's inequality, for g_1 and g_{-1}: h_mu > 0 forces a positive and a negative exponent.
- [PR] Pesin–Ruelle unstable manifolds, as in Step 2 of [R5-a]. For mu-a.e. x and eps > 0 there is a set W^u(x) containing x such that every y in W^u(x) satisfies d(g_{-t}x, g_{-t}y) <= C(x,y) e^{-(chi^+ - eps)t} for t >= 0. Here chi^+ is the smallest positive exponent.
- [LY] Ledrappier–Young (Ledrappier–Strelcyn): if h_mu(g_1) > 0, then for mu-a.e. x the conditional measures of mu on the unstable manifolds (w.r.t. a measurable partition subordinate to W^u) are non-atomic.

**Theorem P.** Assume GH and dim M >= 2. Let mu be an ergodic flow-invariant probability with h_mu(g_1) > 0, and put lambda = mu(d), the sum of the exponents. Let chi^+ > 0 be its smallest positive exponent and -chi^- < 0 its largest negative exponent. Then lambda does not lie in (-chi^+, 0) or in (0, chi^-).

*Proof.* Suppose -chi^+ < lambda < 0. Choose eps > 0 with lambda + eps < 0 and theta := chi^+ - eps > |lambda| + 2 eps.

1. **The pair.** Let G be the set of points z with J_t(z)/t -> lambda as t -> +inf and as t -> -inf. By Birkhoff, mu(G) = 1, so G has full conditional measure on a.e. unstable leaf. By [LY] (non-atomic conditionals), for mu-a.e. x in G there is y in G intersected with W^u(x) with y != x. By [PR], d(g_{-t}x, g_{-t}y) <= C0 e^{-theta t} for t >= 0. (Integer times are interpolated to real times as in [R5-a], Lemma 2.)

2. **The Jacobian offset.** As in Theorem B(a) of [R5-a], beta := lim_{s->inf} (J_{-s}(y) - J_{-s}(x)) exists, and |J_{-t}(y) - J_{-t}(x) - beta| <= K e^{-theta t} for t >= 0, with K = Lip(d) C0/theta.

3. **The functional.** Put Theta(phi) = phi(x) - e^{-beta} phi(y). This is nonzero since x != y.

4. **Backward bound** (time -t, t >= 0). Write r_t = J_{-t}(y) - J_{-t}(x) - beta, so |r_t| <= K e^{-theta t}. Then
   Theta(L_{-t}phi) = e^{J_{-t}(x)} [phi(g_{-t}x) - e^{r_t} phi(g_{-t}y)].
   The bracket is at most C0 e^{-theta t} ||d phi||_inf + K e^K e^{-theta t} ||phi||_inf.
   Also J_{-t}(x) <= (|lambda| + eps) t + C_eps, since x is in G and J_{-t}(x)/t -> -lambda.
   So |Theta(L_{-t}phi)| <= C e^{-(theta - |lambda| - eps) t} ||phi||_{C^1}.

5. **Forward bound** (t >= 0). |Theta(L_t phi)| <= (e^{J_t(x)} + e^{-beta} e^{J_t(y)}) ||phi||_inf <= C e^{(lambda + eps) t} ||phi||_inf, since x and y are in G.

6. **Conclusion.** The hypothesis of Theorem G holds with a = min(theta - |lambda| - eps, -lambda - eps) > 0 and k = 1. So Theta = 0, which contradicts step 3.

If 0 < lambda < chi^-, apply the same argument to -X. It is GH by (O4); its flow is g_{-t}, its divergence is -d, and mu is an ergodic invariant measure with the same entropy and negated exponents. ∎

Theorem P needs no hyperbolicity of mu: zero exponents other than the flow direction are allowed. It improves Theorem B of [R5-a], whose strip (lambda, lambda + theta) is exactly the strip used here. The point is that when 0 lies inside that strip, Theorem G turns the construction into a contradiction rather than into an eigen-distribution.

## 4. Theorem H (proved modulo the classical fact [AFF]). No uniformly volume-contracting hyperbolic set with 1-dimensional unstable bundle and a nontrivial unstable leaf

Let Lambda be a compact invariant hyperbolic set of the flow. That is, X != 0 on Lambda, and there is a continuous Dg_t-invariant splitting T_Lambda M = E^s + RX + E^u with ||Dg_t|E^s|| <= C e^{-theta t} and ||Dg_{-t}|E^u|| <= C e^{-theta t} for t >= 0, where theta > 0. W^uu(z) denotes the strong unstable leaf of z.

**[AFF] Affine parameters on 1-dimensional strong unstable leaves.** This is classical and cited from memory; a proof sketch follows. Assume dim E^u = 1 and X is C^inf. Fix R0 > 0. For each z in Lambda there is a C^inf embedding h_z : (-R0, R0) -> W^uu(z) with h_z(0) = z such that:
- (A1) for all t >= 0 there is a number Lam_t(z) >= theta t - c with g_{-t}(h_z(r)) = h_{g_{-t}z}(e^{-Lam_t(z)} r) whenever both sides are defined;
- (A2) for every k, sup_{z in Lambda} ||h_z||_{C^k} < inf (in a fixed finite atlas);
- (A3) for w in W^uu(z) the limit beta_z(w) := lim_{s->inf} (J_{-s}(w) - J_{-s}(z)) exists, and for every k, sup_z ||beta_z o h_z||_{C^k(-1,1)} < inf.

*Sketch.* Strong unstable leaves of a hyperbolic set of a C^inf flow are C^inf curves with uniformly bounded C^k geometry. Let s denote arc length on W^uu(z). The density
  rho_z(w) = lim_{t->inf} ||Dg_{-t}|E^u(w)|| / ||Dg_{-t}|E^u(z)||
can be written as exp of int_0^inf [a(g_{-sigma}w) - a(g_{-sigma}z)] dsigma. Here a is the infinitesimal log-contraction of E^u, which is C^inf along leaves. Backward iterates contract the leaves with all C^k derivatives decaying exponentially, so the integral converges in C^k along leaves, uniformly in z. Put h_z^{-1}(w) = int_z^w rho_z ds. In these coordinates g_{-t} has constant derivative, which is (A1). The same argument with d in place of a gives (A3).

**Theorem H.** Assume GH. There is no compact invariant hyperbolic set Lambda with the following three properties:
- (i) dim E^u = 1;
- (ii) Lambda is uniformly volume-contracting: there are a > 0 and b with J_t(z) <= b - a t for all z in Lambda and t >= 0;
- (iii) for some x in Lambda, W^uu(x) intersected with Lambda is infinite.

*Proof.* Suppose Lambda has (i)–(iii). Put A = ||d||_inf, and fix an integer k with k theta > A + a.

1. **Choice of points.** Choose distinct y_0, ..., y_k in W^uu(x) intersected with Lambda. Replace x and the y_j by g_{-T}x and g_{-T}y_j for a large T. They stay in Lambda, stay on one strong unstable leaf, stay distinct, and come within distance as small as we like of the base point. So we may assume y_j = h_x(s_j) with distinct s_j in [-1, 1].

2. **Divided-difference weights.** Let alpha_j = prod_{i != j} (s_j - s_i)^{-1}, so that sum_j alpha_j G(s_j) is the k-th divided difference G[s_0, ..., s_k]. For G in C^k[-1,1] it equals G^{(k)}(xi)/k! for some xi in [-1,1] (mean value theorem for divided differences).

3. **The functional.** Put Theta(phi) = sum_j alpha_j e^{-beta_x(y_j)} phi(y_j). Since the y_j are distinct and all alpha_j != 0, Theta != 0.

4. **The cocycle identity.** For y in W^uu(x) and t >= 0,
   J_{-t}(y) = J_{-t}(x) + beta_x(y) - beta_{x_t}(g_{-t}y),   with x_t := g_{-t}x.
   This follows from J_{-s}(y) = J_{-t}(y) + J_{-(s-t)}(g_{-t}y), applied to y and to x, by letting s -> inf.

5. **Backward bound** (time -t, t >= t0, with t0 chosen so that e^{-Lam_t} <= 1). By (A1), g_{-t}y_j = h_{x_t}(sigma s_j) with sigma = e^{-Lam_t(x)}. Hence
   Theta(L_{-t}phi) = e^{J_{-t}(x)} sum_j alpha_j F_t(sigma s_j),   where F_t(r) = e^{-beta_{x_t}(h_{x_t}(r))} phi(h_{x_t}(r)).
   - By (A2) and (A3), ||F_t||_{C^k[-1,1]} <= C ||phi||_{C^k}, uniformly in t.
   - By step 2 applied to G(s) = F_t(sigma s), the sum is at most sigma^k ||F_t||_{C^k}/k! <= C e^{-k theta t} ||phi||_{C^k}.
   - Since J_{-t}(x) <= A t, we get |Theta(L_{-t}phi)| <= C e^{-(k theta - A) t} ||phi||_{C^k}.
   For 0 <= t <= t0 the trivial bound C ||phi||_inf holds.

6. **Forward bound** (t >= 0). All y_j lie in Lambda, so by (ii), |Theta(L_t phi)| <= (sum_j |alpha_j| e^{-beta_x(y_j)}) e^{b - a t} ||phi||_inf.

7. **Conclusion.** Theorem G applies with rate min(a, k theta - A) > 0. So Theta = 0, which contradicts step 3. ∎

By (O4) the same holds with X replaced by -X. Hence Theorem H also excludes a hyperbolic set with dim E^s = 1 that is uniformly volume-expanding and has an infinite intersection with some strong stable leaf.

**Lemma I (cited [LY]).** Let Lambda be a hyperbolic set carrying an ergodic mu' with h_{mu'}(g_1) > 0. Then for mu'-a.e. x, W^uu(x) intersected with Lambda is uncountable.

*Proof.* For a uniformly hyperbolic set, the Pesin unstable manifold of g_1 at x is the strong unstable leaf W^uu(x), since E^u is the whole positive-exponent space. By [LY], the conditional measures of mu' on these leaves are non-atomic, and they are carried by supp mu', which is contained in Lambda. ∎

## 5. Corollary: the problem is solved in dimension <= 3 (modulo citations)

**Theorem 5.1.** Let M be compact connected with dim M <= 3, and let X be GH. Then h_top(g_1) = 0.

*Proof.*
- **dim M = 1.** M is the circle, and g_1 is a circle homeomorphism; such maps have zero topological entropy (classical).
- **dim M = 2.** Young's theorem (cited: continuous flows on compact surfaces have zero topological entropy; L.-S. Young, 1977).
- **dim M = 3.** Suppose h_top(g_1) > 0.
  1. Theorem 4.1 of the background [R5-d] gives, after replacing X by -X if necessary (GH is preserved by (O4)), a horseshoe Lambda != M with J_t <= b - (a/2)t on Lambda for t >= 0. Lambda is a compact invariant hyperbolic set. Since dim M = 3, E^u and E^s are both 1-dimensional.
  2. Lambda is conjugate to the suspension of a transitive SFT of positive entropy, so h_top(g_1|Lambda) > 0. By the variational principle there is an ergodic mu' on Lambda with h_{mu'} > 0.
  3. Lemma I gives x in Lambda with W^uu(x) intersected with Lambda infinite.
  4. Theorem H gives a contradiction. ∎

This closes exactly the configuration (H3) left open in [R5-d]. For the chain: in dimension <= 3, (PE) holds, because an ergodic mu with h_mu > 0 would give h_top > 0.

The citations used are [Rue], [KLY] (Katok / Lian–Young horseshoes), [HYP] and Sigmund's density (all inside Theorem 4.1), plus [LY], [AFF], Young's theorem and the variational principle.

## 6. Any dimension: what is proved and what is conditional

**(6a) Proved (modulo [Os], [Rue], [PR], [LY]):** Theorem P. Under GH, every ergodic mu with h_mu > 0 has mu(d) = sum of exponents in {0} union (-inf, -chi^+] union [chi^-, inf).

**(6b) Proved (modulo [Rue], [KLY], [HYP], [LY], [AFF]).** Under GH, every hyperbolic ergodic mu with h_mu > 0 is impossible, provided the following holds for the horseshoe Lambda given by Corollary 4.3 of [R5-d]: in the orientation (X or -X) for which Lambda is uniformly volume-contracting, the unstable bundle is 1-dimensional.

The proof is that of Theorem 5.1, using Corollary 4.3 in place of Theorem 4.1. Note that the case mu(d) = 0 is included: Corollary 4.3 and Prop 5.1 make every measure on Lambda have d-average of one strict sign.

**(6c) Conditional on uniform normal forms [NF].** Statement cited from memory; I am not sure of the exact hypotheses in the literature (Guysinsky–Katok in the narrow-band case; Kalinin–Sadovskaya, "Normal forms on contracting foliations", in general). The statement needed is this. For a hyperbolic set of a C^inf flow there are charts h_z : B(0,2) in R^u -> W^uu(z) with uniformly bounded C^k norms, in which g_{-t} acts by polynomial maps Q_{z,t} of degree <= D, with D depending only on the spectrum, and |Q_{z,t}(s)| <= C e^{-theta t}|s|. Also (A3) holds in these charts.

Theorem H then holds without assumption (i). Proof: in step 1 take N distinct points y_j = h_x(s_j) of Lambda on W^uu(x), with N > dim of the space of polynomials of degree <= D(k-1) on R^u. Take a nonzero alpha in R^N annihilating that space at the nodes s_j. Expand F_t(r) by Taylor to order k-1 at 0:
- the polynomial part contributes sum_j alpha_j (polynomial of degree <= D(k-1))(s_j) = 0;
- the remainder is at most C ||F_t||_{C^k} |Q_{x,t}(s_j)|^k <= C e^{-k theta t} ||phi||_{C^k}.
Theta = sum alpha_j e^{-beta_x(y_j)} delta_{y_j} is nonzero, and the rest of the proof is unchanged.

Consequence (conditional on [NF]): under GH, every ergodic mu with h_mu > 0 is non-hyperbolic.

**(6d) Conditional on non-uniform normal forms [NF-P].** Cited from memory: Kalinin–Sadovskaya, "Normal forms for non-uniform contractions", JMD 2017. The statement needed is measurable sub-resonance polynomial normal forms on Pesin unstable manifolds, with tempered C^k bounds.

Under [NF-P], the proof of Theorem P works with N points instead of 2. The points are all in the generic set G and on W^u(x); [LY] gives infinitely many. With k large, the backward bound becomes e^{(|lambda| + eps)t} e^{-k(chi^+ - eps)t + eps t}. Consequence (conditional): under GH, every ergodic mu with h_mu > 0 has mu(d) = 0.

Combining (6c) and (6d), (PE) would reduce, conditionally on [NF] and [NF-P], to the single case below.

## 7. What remains open

**Open question (exact point where the argument stops).** Exclude, under GH, an ergodic flow-invariant mu with:
- h_mu(g_1) > 0;
- mu(d) = 0, i.e. the sum of the exponents is zero;
- mu non-hyperbolic: some exponent other than the flow direction is zero. This needs dim M >= 4; in dim 3 such mu do not exist.

Unconditionally, also open in dim >= 4:
- the cases mu(d) <= -chi^+ or mu(d) >= chi^- without [NF-P];
- hyperbolic mu whose volume-contracting orientation has multi-dimensional unstable bundle, without [NF].

**Why the method stops at mu(d) = 0 (non-hyperbolic).** Theorem G needs Theta(L_t phi) to decay exponentially in both time directions.
- Points on one unstable leaf give backward cancellation of any order, but forward the weights e^{J_t} decay only if mu(d) < 0.
- For mu(d) = 0, forward decay needs a simultaneous cancellation along stable leaves. That means a "grid" of points p_{ij} with p_{ij} in W^ss(p_{i'j}) and p_{ij} in W^uu(p_{ij'}), with compatible Jacobian weights.
- Such grids generically do not close: the su-quadrilateral closes only up to a temporal shift, and the weight cocycle e^{beta} has a holonomy defect. Smoothing in the flow direction does not absorb the temporal shift.
- In the hyperbolic case this is bypassed by passing to a horseshoe, all of whose measures have mu(d) != 0 (Corollary D1). For non-hyperbolic mu, no such approximating set is available.

**Step 2 of the chain** (variational principle and ergodic decomposition) is correct as written. Together with Theorem 5.1 it gives the full [GOAL] for dim M <= 3. For dim M >= 4 the [GOAL] is NOT established here.

=== END OF ANSWER round6_q2 ===
