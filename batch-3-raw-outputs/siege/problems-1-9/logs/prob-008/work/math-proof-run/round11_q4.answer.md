# round11_q4 — attempt to refute (AP); answer

## 0. Plan and verdict (written first, updated at the end)

Target: refute (AP) exactly as stated, or failing that, prove partial results and pin down where a counterexample must live.

Verdict: **(AP) is not refuted.** Section 1 shows that both refutation routes amount to disproving the Greenfield–Wallach conjecture: any GH field carrying an (AP)-pair has exponentially growing Lipschitz constants, so it is not a smooth conjugate of a Diophantine linear flow. I do not attempt that.

What is proved below:
- (§1) Lipschitz-growth lemma. Every flow whose Lipschitz constants grow subexponentially has no (AP)-pair, whether or not it is GH. This kills the isometric, Diophantine, parabolic (nilflow, horocycle) and time-changed-Diophantine templates outright.
- (§2) Elementary structure of an (AP)-pair. Neither point is a zero or a periodic point, the two points lie on different orbits, alpha(x) = alpha(y), and neither point lies on the unstable set of a zero or periodic orbit.
- (§3) Uniquely ergodic (UE) and volume-preserving classes.
  - For GH + UE, (b) and (c) hold automatically with lambda = 0. So (AP) is equivalent to "no distinct pair is exponentially asymptotic in backward time".
  - For GH + smooth invariant volume, (AP) <=> h_top = 0 <=> all Lyapunov exponents of the volume vanish <=> Lip(g_t) grows subexponentially. In that class a counterexample to (AP) is exactly a counterexample to the problem.
  - Consequences: (AP) holds for volume-preserving GH fields in dim <= 3, unconditionally given the earlier material. For UE GH fields in dim 3 it holds conditionally, on a cited closing lemma.
- (§4, recalled from R7-a) Pairs that are exponentially asymptotic in both time directions (with matched Jacobian holonomy) are excluded by Theorem J. In the volume class, therefore, the two points of an (AP)-pair are never also forward-asymptotic.
- (§5) Reduction to real eigen-distributions (Proposition 5.1). If X + kappa is injective on D' for one kappa in (lambda, lambda + theta), then no pair satisfies (a) and (b), even without (c). Conversely, a counterexample must carry nonzero real eigen-distributions Xu = -kappa u of order <= 1 for EVERY kappa in (lambda, lambda + theta).
- (§6) The suggested templates, one by one, with the hypothesis that fails.
- (§7) Summary of where a counterexample must live, and the open questions.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi, and distribution densities S are identified with u = S/nu. "Lip(f)" is the Lipschitz constant with respect to the Riemannian distance.

## 1. Why a refutation would disprove the Greenfield–Wallach conjecture

**Lemma 1.1 (Lipschitz growth).** Let g_t be any C^1 flow on a compact Riemannian manifold. Suppose x != y and dist(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0, as in (a). Then for all s >= 0,
 Lip(g_s) >= (dist(x,y)/C) e^{theta s}.
Hence lambda^* := lim_{s->inf} (1/s) log max_z ||Dg_s(z)|| >= theta > 0. The limit exists by subadditivity. Moreover Lip(g_s) = max_z ||Dg_s(z)|| on a connected Riemannian manifold, by integrating along almost-minimising curves.
*Proof.* x = g_s(g_{-s} x) and y = g_s(g_{-s} y). So dist(x,y) <= Lip(g_s) dist(g_{-s}x, g_{-s}y) <= Lip(g_s) C e^{-theta s}. ∎

**Corollary 1.2.** No flow with lambda^* = 0 has an (AP)-pair, whether or not it is GH. In particular there are no (AP)-pairs for:
- (i) any flow by isometries of some Riemannian metric, hence (Lip comparable under change of metric) any smooth conjugate of a linear flow on a torus, Diophantine or not;
- (ii) any equicontinuous flow with uniformly bounded ||Dg_t||;
- (iii) nilflows and horocycle flows (||Dg_t|| grows polynomially in t);
- (iv) smooth time changes hX_alpha (h > 0) of Diophantine linear flows X_alpha on T^n. These are smoothly conjugate to c X_alpha with c = (int h^{-1})^{-1}. Proof: solve X_alpha w = c/h - 1, whose right side has mean zero, with w smooth (Diophantine). Put Phi(z) = z + w(z) alpha. Then DPhi(hX_alpha) = h(1 + X_alpha w) alpha = c alpha. Also det DPhi = 1 + dw(alpha) = c/h > 0, so Phi is a local diffeomorphism homotopic to the identity, hence a degree-one covering, hence a diffeomorphism.

**Consequence for the two refutation routes.**
- Route (a) requires a GH field with an (AP)-pair. By Lemma 1.1 it has lambda^* > 0, so by Corollary 1.2(i) it is not a smooth conjugate of a Diophantine linear flow. It would therefore be a counterexample to the Greenfield–Wallach conjecture (GH fields are smooth conjugates of Diophantine linear flows on tori).
- Route (b) is "(AP) implies something false". If (AP) is false, some GH field carries an (AP)-pair, and the same conclusion follows.
- Conversely, the Greenfield–Wallach conjecture implies (AP), by Corollary 1.2(i).

So refuting (AP) is at least as hard as refuting a well-known open conjecture. This is not a proof that (AP) holds. But no construction is available, since the only known GH fields (Diophantine linear flows and their smooth conjugates, cited from memory as the standard examples) have no (AP)-pairs. I did not find a refutation, and the rest of this answer gives partial results.

## 2. Elementary structure of an (AP)-pair (no GH needed unless stated)

**Proposition 2.1.** Let x != y satisfy (a) and (c). Then:
1. y is not on the orbit of x.
2. Neither x nor y is a zero of X or a periodic point.
3. x is in alpha(y) and y is in alpha(x). Hence alpha(x) = alpha(y), and this set contains both points.
4. Neither point lies on the unstable set {z : dist(g_t z, gamma) -> 0 as t -> -inf} of a zero or periodic orbit gamma. (For example, pairs on the strong unstable manifold of a saddle are excluded by (c).)

*Proof.*
3. By (c) there are t_n -> -inf with g_{t_n} x -> x. By (a), dist(g_{t_n} y, g_{t_n} x) -> 0, so g_{t_n} y -> x, i.e. x is in alpha(y). Symmetrically y is in alpha(x). An alpha-limit set is closed and invariant, and contains the alpha-limit set of each of its points. So alpha(x) contains alpha(y), and conversely.
1. Suppose y = g_s x. Then dist(g_{t_n} x, g_s g_{t_n} x) -> 0. By continuity of g_s, dist(x, g_s x) = 0, so y = x, which is excluded.
2. If x is periodic or a zero, alpha(x) is its orbit O. Then y is in alpha(x) = O, which contradicts item 1 (when y = x, x != y is violated). If y is periodic, swap the roles of x and y: item 3 is symmetric.
4. If z is in that unstable set, then alpha(z) is contained in gamma. By (c), z is in gamma, which contradicts item 2. ∎

**Proposition 2.2 (the open lambda-window; recalled from the brief's remark).** Under GH, an (AP)-pair has lambda = 0 or lambda <= -theta. (This is the brief's remark: for -theta < lambda < 0, Theorem J applies to delta_x - e^b delta_y. It is re-derived as the case kappa = 0 of Proposition 5.1 below.)

## 3. The uniquely ergodic and the volume-preserving classes

Facts used from the material:
- Lemma E (GH, dim >= 2, UE with measure mu): (i) mu(d) = 0; (ii) the flow is minimal.
- (O2): GH plus a smooth invariant positive density omega gives unique ergodicity, with omega-hat = omega/omega(M) the only invariant probability, and minimality.
- [R5-a] Lemma 1, proved there with no GH: if lambda^* > 0, there is a flow-invariant probability m whose top exponent chi(z) = lim (1/n) log ||Dg_n(z)|| (it exists m-a.e., by Kingman) satisfies int chi dm >= lambda^*.
- The chain steps 1–3 of the brief (Pesin unstable manifolds plus the Ledrappier–Strelcyn partition, cited there).
- Theorem 5.2 of R6-a: GH and dim M <= 3 give h_top = 0.

**Proposition 3.1 (UE case).** Assume GH, dim M >= 2, and unique ergodicity with measure mu. Then:
- every point z satisfies (b) with lambda = 0 and satisfies (c);
- X has no zeros and no periodic orbits.
Hence, for such X, (AP) is equivalent to: **no two distinct points are exponentially asymptotic in backward time.** By Lemma 1.1 this holds whenever lambda^* = 0.

*Proof.*
1. (b): By unique ergodicity of the flow and of the reversed flow (same invariant measures), (1/t) int_0^t d(g_s z) ds -> mu(d) uniformly in z as t -> +-inf. Also mu(d) = 0 by Lemma E(i).
2. (c): By Lemma E(ii) the flow is minimal. omega(z) and alpha(z) are nonempty, closed and invariant, so both equal M, and both contain z.
3. A zero or a periodic orbit is a closed invariant set different from M (dim >= 2), which contradicts minimality. ∎

**Proposition 3.2 (volume-preserving case: (AP) is equivalent to the goal).** Assume GH, dim M >= 2, and that X preserves a smooth positive density omega. The following are equivalent:
- (1) (AP) holds for X;
- (2) h_top(g_1) = 0;
- (3) all Lyapunov exponents of g_1 with respect to omega-hat vanish omega-a.e.;
- (4) lambda^* = 0, i.e. max_z ||Dg_t(z)|| grows subexponentially.

*Proof.*
- (4) => (1): Lemma 1.1.
- (1) => (2): Suppose h_top > 0. Chain step 1 gives a g_1-ergodic nu' with h_{nu'}(g_1) > 0. Chain step 2, run with the density nu = omega, gives x != y with (a), (b) and (c), where lambda = nu'(J_1). For this density d = div_omega X = 0, so J is identically 0 and lambda = 0 <= 0. This contradicts (AP). (By the brief's remark, (AP) does not depend on the choice of density.)
- (2) => (3): Pesin's entropy formula (cited from memory: for a C^2 diffeomorphism f preserving a probability mu absolutely continuous with respect to volume, h_mu(f) = int sum_i chi_i^+ dmu) gives int sum chi_i^+ d omega-hat = 0. So there are no positive exponents a.e. With nu = omega we have J = 0, so the sum of all exponents, lim (1/n) log |det_omega Dg_n| = lim J_n/n, is 0 a.e. Hence there are no negative exponents either.
- (3) => (4): If lambda^* > 0, [R5-a] Lemma 1 gives an invariant m with int chi dm >= lambda^* > 0. By unique ergodicity m = omega-hat, so the top exponent is positive on a set of positive measure, contradicting (3). ∎

So **in the volume-preserving GH class, a counterexample to (AP) is exactly a counterexample to the problem.** Reducing the goal to (AP) loses nothing in this class, and nothing simpler than the goal itself can be refuted there.

**Corollary 3.3 (given the material; it inherits the citations of R6-a Theorem 5.2: Ruelle's inequality and the Katok / Lian–Young horseshoe theorem).** (AP) holds for every GH field with a smooth invariant volume on a manifold of dimension <= 3.
*Proof.* Theorem 5.2 of R6-a gives h_top = 0. Then apply Proposition 3.2, (2) => (1). (dim 1: a zero p would make delta_p a second invariant probability, which contradicts unique ergodicity (O2). So X does not vanish, its flow on S^1 is smoothly conjugate to a rotation flow, lambda^* = 0, and Lemma 1.1 applies.) ∎

**Proposition 3.4 (UE case: the measure is not hyperbolic; conditional on a cited closing lemma).** Cited from memory, [KC]: Katok's closing lemma, flow version (Katok 1980; Lian–Young for flows). Let mu be an ergodic invariant probability of a C^2 flow with mu(Zero(X)) = 0, all of whose Lyapunov exponents except the one in the flow direction are nonzero. Then the flow has a (hyperbolic) periodic orbit; indeed supp mu is contained in the closure of the periodic orbits.

Assume GH, dim M >= 2, UE with measure mu. Then mu has a zero exponent transverse to X. Consequently:
- if dim M = 2, then lambda^* = 0; this case is unconditional, see the proof;
- if dim M = 3, then lambda^* = 0 (conditional on [KC]).
In both cases (AP) holds for X.

*Proof.*
1. By Proposition 3.1, X has no zeros and no periodic orbits. So by [KC], mu is not hyperbolic.
2. The sum of all exponents of mu equals mu(d) = 0 (Lemma E(i)): it is lim (1/n) log |det_nu Dg_n| = lim J_n/n.
3. dim 2: the single transverse exponent equals the sum, which is 0. (The flow-direction exponent is 0 because |X| is bounded above and below on M: there are no zeros.) This step does not need [KC].
4. dim 3: the transverse exponents chi_1 + chi_2 = 0 and one of them is 0, so both are 0.
5. In either case the top exponent is 0 a.e. By [R5-a] Lemma 1 and UE, lambda^* = 0. By Lemma 1.1 there is no (AP)-pair. ∎

**Remark 3.4' (hypothesis (c) is vacuous in the core class).** In the UE class, and in particular in the volume-preserving class, every point satisfies (b) with lambda = 0 and satisfies (c) (Proposition 3.1). So in the case the Greenfield–Wallach picture singles out (smooth invariant volume, lambda = 0), (AP) is literally "no two distinct points are exponentially asymptotic in backward time". Recurrence cannot be the lever there: any proof of (AP) in the volume class must use neither (c) nor (b).

**Remark 3.5.** Without UE or a volume, an (AP)-pair still gives lambda^* >= theta (Lemma 1.1). So by [R5-a] Lemma 1 and the ergodic decomposition (chi is invariant and measurable, and int chi dm >= theta), there is an ergodic invariant m whose top exponent is >= theta a.e. The entropy of m may be 0, however. So an (AP)-pair does not by itself produce a positive-entropy measure outside the volume-preserving class.

## 4. Pairs asymptotic in both time directions (recalled; already in the material)

Corollaries G1 and G2 of R7-a (proved there from Theorem J) say the following under GH:
- no pair x != y is exponentially asymptotic in both time directions when the growth condition (R) holds at one of the points and the Jacobian holonomy vanishes, i.e. lim_{t->-inf}(J_t x - J_t y) = lim_{t->+inf}(J_t x - J_t y);
- in the volume case there is no such pair at all.

Consequence for (AP): **in the volume-preserving GH class, the two points of an (AP)-pair are never exponentially asymptotic in forward time.** More generally, by Theorem G of R7-f, any finite configuration built from (AP)-pairs and forward-asymptotic pairs of points with sub-theta Jacobian growth must form a pseudoforest. So a counterexample must have its backward-asymptotic pairs "isolated" from forward-asymptotic ones, in the sense of R7-f.

## 5. What an (AP)-pair forces spectrally (consequences of material results)

**Proposition 5.1.** Let X be any smooth field, and let x != y satisfy (a), together with the part of (b) that is actually used:
- J_t(x), J_t(y) <= C_delta + (lambda + delta) t for t >= 0;
- J_t(x) <= C_delta + (-lambda + delta)|t| for t <= 0;
for every delta > 0. Recurrence (c) is not needed. Then:
- (i) (no GH) For every complex c with lambda < Re c < lambda + theta there is an order-<=1 Jordan chain of P^T at c. In particular there is a nonzero generalized function u_c of order <= 1 with X u_c = -c u_c. The family is holomorphic in c: it is the Laplace transform of S = delta_x - e^b delta_y.
- (ii) Hence a GH field carrying such a pair has a nonzero real eigen-distribution X u = -kappa u, of order <= 1, for every kappa in (lambda, lambda + theta).
- (iii) Under GH, if 0 is in (lambda, lambda + theta), this is impossible (Lemma M / Theorem J). So lambda is not in (-theta, 0); this is the brief's remark. For lambda >= 0 the strip lies in {Re z > 0}, and for lambda <= -theta it lies in {Re z <= 0}; GH, used through (K0) and (K1) at the single point 0, excludes neither. (The restriction lambda <= 0 in (AP) is part of the statement, not a consequence of it. The chain uses -X to arrange it.)

*Proof of (i).*
1. Steps 5–10 of Theorem R' (block R9-a) use only the bounds listed. They give the family T_z(phi) = int e^{-zt} F_phi(t) dt, with F_phi(t) = e^{J_t x} phi(g_t x) - e^{b + J_t y} phi(g_t y). The family is holomorphic and order-1 bounded on closed substrips of (lambda + delta, lambda + theta - delta), satisfies T_z o P = z T_z, and is not identically 0.
2. Since the family does not depend on delta, it is one nonzero family on the strip (lambda, lambda + theta) (R10-b, side observation (b)).
3. Corollary 7.2 of R9-b (Theorem A) then gives an order-1 Jordan chain at EVERY point of that strip. The eigen-relation for u_c = B/nu is Observation 0. ∎

*Direct proof of the contrapositive of (ii) for one real kappa (self-contained; this is the shifted Theorem J).* Suppose ker(X + kappa) restricted to order-<=1 distributions is 0 for some kappa in (lambda, lambda + theta).
1. Choose delta, eps > 0 with lambda + delta + eps <= kappa <= lambda + theta - delta - eps.
2. Put G_phi(t) = e^{-kappa t} F_phi(t).
   - For t >= 0: |F_phi(t)| <= C e^{(lambda + delta)t} ||phi||_inf.
   - For t <= 0: |F_phi(t)| <= C e^{(-lambda + delta - theta)|t|} ||phi||_{C^1} (Theorem R' step 7).
   - So |G_phi(t)| <= C e^{-eps|t|} ||phi||_{C^1} for all t.
3. G_phi' = G_{(P - kappa)phi}. The moments m_j(phi) = int t^j G_phi dt are order-1 densities with m_0 o (P - kappa) = 0 and m_j o (P - kappa) = -j m_{j-1}.
4. By hypothesis, m_0 = 0 when kappa != 0. (B o (P - kappa) = 0 means X(B/nu) = -kappa B/nu.) Then m_1 o (P - kappa) = 0 gives m_1 = 0, and inductively all m_j = 0. When kappa = 0, use (F1) and (F2) as in Theorem J.
5. Fourier uniqueness on |Im xi| < eps gives G_phi = 0. So S = 0, which contradicts x != y. ∎

So a counterexample to (AP) is in particular a GH field with a holomorphic strip family of order-1 real eigen-distributions. This is the object that (EF)/(JC)/(J1-0) of rounds 8–10 tried to exclude. Proposition 5.1 adds nothing new on that front; it is recorded to make the "where must a counterexample live" list complete.

## 6. The suggested templates, one by one

**T1. Fields with zeros; hyperbolic saddles with d(p) != 0; pairs on strong unstable manifolds.**
- A pair on W^{uu}(p) of a zero or periodic point p has alpha(x) = orbit of p, so (c) forces x into that orbit. Proposition 2.1(4) excludes this for any zero or periodic orbit, hyperbolic or not.
- GH fields with a zero are never UE. If p is a zero, delta_p is invariant; UE would force mu = delta_p, and then Lemma E(i) gives d(p) = mu(d) = 0, contradicting P1. They also have no smooth invariant volume (a smooth invariant volume gives UE by (O2)). So fields with zeros live in the "no volume, several invariant measures" class. There (AP) has content for both lambda = 0 and lambda <= -theta, but its pairs must be bi-recurrent, hence away from the stable/unstable sets of the zeros.
- Which hypothesis fails for the obvious pairs: (c).

**T2. Products, skew products and suspensions over Diophantine flows.**
- (Proved) GH passes to factors. Let pi: M -> B be a smooth fibre bundle with dpi(X) = Y o pi. If X is GH, so is Y.
  *Proof.* If v in D'(B) has Yv = f smooth, then u = pi^* v satisfies Xu = (Yv) o pi = f o pi. This holds for smooth v, hence for all v by continuity of pullback by a submersion. So u is smooth, and v = u o sigma is smooth for local sections sigma. ∎
  For a product X = Y ⊕ Z on B × F, both Y and Z are GH. *Proof.* If Zw = f, then u = 1 ⊗ w satisfies Xu = 1 ⊗ f, so u is smooth, and w = int u(b, .) psi(b) db with int psi = 1 is smooth. ∎
- (Proved) Pairs project to pairs. If Y is an isometric flow (e.g. Diophantine linear) and pi is Lipschitz, then an (AP)-pair of X has pi(x) = pi(y). Indeed dist_B(h_t pi x, h_t pi y) is constant in t and bounded by Lip(pi) dist(g_t x, g_t y) -> 0.
  - So for a product X = Y ⊕ Z with Y Diophantine linear (take nu = Leb ⊗ nu_F, so that d = d_Z), an (AP)-pair of X is (b0, x_F), (b0, y_F) with (x_F, y_F) an (AP)-pair of the GH field Z, with the same lambda. Recurrence projects. **Products with a Diophantine factor reduce (AP) to lower dimension.**
- (Proved) Suspensions. For a suspension (circle-valued theta with X theta = 1), an (AP)-pair has theta(x) = theta(y), because theta(g_t x) - theta(g_t y) is constant. So the pair lies in one cross-section, and is a backward-asymptotic pair for the return map f.
  - GH of the suspension forces every f-invariant generalized function v (v o f = v) to be constant: v lifts to u(z,s) = v(z) with Xu = 0, and L1 applies.
- Which hypothesis fails: none in general. These templates only reduce the question to the fibre (or the return map), where the same problem reappears.

**T3. Time changes.** (O4) says GH is preserved under time changes. I do not prove the converse statement for (AP). Sketch: if (x, y) is an (AP)-pair for X with lambda = 0, then for Y = hX the time reparametrisations of the two orbits differ by a convergent drift, since h(g_s x) - h(g_s y) -> 0 exponentially. So y is exponentially backward-asymptotic, for Y, to a Y-time-shift x' of x. Then (x', y) satisfies (a), (b) with lambda = 0 (J changes by O(1) plus o(|t|)) and (c) for Y. So time changes do not help in either direction. Time changes of Diophantine flows are covered by Corollary 1.2(iv).

**T4. Volume-preserving flows.** Proposition 3.2: here (AP) is EQUIVALENT to the problem. A counterexample would be a GH volume-preserving flow of positive entropy. By material results it must have:
- dim M >= 4 (Corollary 3.3);
- a non-hyperbolic volume with nonzero exponents (Theorem 5.1 of R6-a);
- no continuous partially hyperbolic splitting (Theorem U of R8-f);
- no closed su-cycles through generic points (Corollary G2 of R7-a; Prop. 2.3 of R9-i);
- unique ergodicity and minimality (O2);
- every mean-zero smooth function a smooth coboundary with tame bounds (R7-d Lemma F);
- no exponential mixing of any L^1 density (Corollary E of R8-f).
So nothing short of the full problem can be refuted in this class.

**T5. Parabolic flows (nilflows, horocycle flows).** ||Dg_t|| grows polynomially, so lambda^* = 0 and there is no (AP)-pair at all (Corollary 1.2(iii)); hypothesis (a) fails. (Independently, cited from memory: Flaminio–Forni show these flows have infinite-dimensional spaces of invariant distributions. With the invariant volume that gives non-constant u in D' with Xu = 0, so they are not GH by L1.)

**T6. Partially hyperbolic and Anosov flows.**
- Uniformly partially hyperbolic fields with max_m |m(d)| < theta, in particular all volume-preserving ones, are not GH (Theorem U of R8-f).
- Anosov flows have hyperbolic periodic orbits with homoclinic points, so they are not GH (Corollary 4.2 of R6-a).
- They do carry (AP)-pairs (two generic points of a measure, on one strong unstable leaf), but GH fails.
- Partially hyperbolic flows in which some invariant measure has |m(d)| >= theta are not covered by Theorem U. For them I have nothing beyond Corollary 4.2 of R6-a, which excludes them as soon as they contain a hyperbolic periodic orbit with a homoclinic point.

**T7. Diophantine linear flows and their smooth conjugates.** These are GH, but (a) fails (Corollary 1.2(i)).

## 7. Summary: where a counterexample to (AP) must live; what is proved, sketched, open

**Necessary properties of a counterexample** (X GH on M, with an (AP)-pair (x, y, lambda, theta)). Every item is proved above or in the cited material blocks; dependence on cited literature is marked.
1. lambda^* >= theta > 0: Lip(g_t) >= c e^{theta t} (Lemma 1.1). So there is an ergodic invariant m with top exponent >= theta (R5-a Lemma 1 plus the ergodic decomposition). X is not isometric, not a smooth conjugate of any linear torus flow, not parabolic, and not a time change of a Diophantine flow (Corollary 1.2). In particular X would be a counterexample to the Greenfield–Wallach conjecture (cited from memory).
2. x and y are non-periodic and not zeros, lie on different orbits, satisfy alpha(x) = alpha(y) (containing both), and do not lie on the unstable set of any zero or periodic orbit (Proposition 2.1).
3. lambda = 0 or lambda <= -theta (Proposition 2.2 / 5.1(iii)).
4. For every c with lambda < Re c < lambda + theta, P^T has an order-1 Jordan chain at c, and X has a nonzero order-<=1 eigen-distribution X u = -c u (Proposition 5.1, from Theorem R' and Theorem A of the material). In particular: the real point spectrum of X on order-1 distributions contains the whole interval (lambda, lambda + theta).
5. If X has a smooth invariant volume:
   - X is a counterexample to the problem itself (Proposition 3.2; Pesin entropy formula cited);
   - dim M >= 4 (Corollary 3.3);
   - the volume is non-hyperbolic (R6-a Theorem 5.1; Katok / Lian–Young cited);
   - X is not partially hyperbolic (Theorem U);
   - X has no closed su-cycles (Corollary G2).
6. If X is UE (without a volume): lambda = 0, and (b), (c) hold for every point (Proposition 3.1). The UE measure is non-hyperbolic, and dim M >= 4 (Proposition 3.4, conditional on the cited closing lemma [KC]; dim M = 2 is excluded unconditionally).
7. If X has a zero, X is neither UE nor volume-preserving (T1), and the pair stays off the stable and unstable sets of zeros and periodic orbits.
8. If X = Y ⊕ Z with Y Diophantine linear, then Z is GH and carries an (AP)-pair of lower dimension (T2).

**Proved in this answer (new, as far as I can tell from the material; all elementary):**
- Lemma 1.1 and Corollary 1.2. (The material has the related band Corollary 1.2 of R9-b: an order-1 eigen-family to the right of max m(d) forces Lambda_1 > 0. Lemma 1.1 is the pair version.)
- Proposition 2.1.
- Propositions 3.1 and 3.2, Corollary 3.3, Remark 3.4'.
- Proposition 3.4 (dim 2 unconditional; dim 3 conditional on [KC]).
- The factor and product statements of T2.
- The direct shifted-Theorem-J proof in §5.

**Sketched only:** the time-change statement T3.

**Cited from memory:**
- Pesin's entropy formula;
- Katok's closing lemma for flows [KC];
- Flaminio–Forni on invariant distributions of parabolic flows (used only in a parenthetical remark);
- the statement of the Greenfield–Wallach conjecture.

**Not achieved:** a refutation of (AP). By §1 any refutation produces a GH field outside the smooth conjugacy class of Diophantine linear flows. By Proposition 3.2, in the volume-preserving class a refutation is the same thing as a counterexample to the problem. So (AP) cannot be refuted there without refuting the problem itself.

**Open questions (explicit).**
- (O-AP-vol) Under GH plus a smooth invariant volume (so UE and minimal), can two distinct points be exponentially asymptotic in backward time? This is equivalent to the problem in that class (Proposition 3.2). It is the core case and remains open.
- (O-AP-neg) Under GH without a volume, exclude (AP)-pairs with lambda <= -theta. Here (c) is not automatic; it is the only case where recurrence could help. I found no way to use it. The two-point Theorem J method is blocked because the backward growth e^{|lambda||t|} of e^{J_t(x)} beats the pair cancellation e^{-theta|t|}. Higher-order cancellation needs many points on one unstable leaf (the normal-form issue of R6-a Prop. 6.2), which (AP) as stated does not provide.
- (O-UE-3) Is Proposition 3.4 in dimension 3 provable without the closing lemma, i.e. is a UE GH field in dimension 3 free of measures with nonzero exponents?
- (O-V) Does GH imply a smooth invariant volume (statement (V) of the material)? If so, the general case of (AP) reduces to (O-AP-vol) plus the vanishing of the lambda <= -theta case, which (V) makes automatic (lambda = 0 by UE).

=== END OF ANSWER round11_q4 ===

