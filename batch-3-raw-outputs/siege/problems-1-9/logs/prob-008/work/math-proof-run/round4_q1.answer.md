# round4_q1: statement (V) (GH => smooth invariant positive density)

## Plan (written first, updated as I go)
1. Check the planner lemmas C-F; note any errors.
2. Prove new, simpler reductions of (V) that use GH directly, in particular a version that needs only the boundedness of ONE real function of t.
3. Try to prove that bound from GH. If that fails, record exactly where it stops.

Conventions are those of the planner: nu is a smooth positive density, nu^ = nu/nu(M), d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, S_t f(x) = int_0^t f(g_s x) ds (so J_t = S_t d, and S_{t+r} f = S_r f + (S_t f) o g_r). Also g_t^* nu = e^{J_t} nu, and so (g_t)_* nu = e^{J_{-t}} nu. A distribution u means the functional phi -> <u, phi nu>, and <Xu, phi nu> = -<u, (X phi + d phi) nu>.

## 1. Check of the planner lemmas C-F
I checked each step of C, C1 (the first sentence only), D, D1, D2, E and F, and I found no error. The details:
- **C.** c(t) = e^{J_t(x)} satisfies |log c(t) - log c(s)| <= ||d||_inf |t-s|. So if c is integrable, then c -> 0 at +-inf. The boundary terms vanish, so T(X phi + d phi) = 0 and T = K nu. But an injectively immersed line is a countable union of compact C^1 arcs, hence nu-null when n >= 2. This is a contradiction. Correct.
- **C1, first sentence.** This is immediate from C, because the integral of e^{b - a|t|} is finite. I did not use the horseshoe claims and I do not vouch for them.
- **D.** The Leibniz identity gives T_s(X phi + d phi) = s P(s)^{-1} int sign(t) c_s phi(g_t x) dt, which is bounded by s ||phi||_inf. Correct. **D1** and **D2** are also correct (D2 is Jensen applied to int e^{J_t} d nu^ = 1).
- **E.** (i) uses the uniform convergence J_t/t -> mu(d) under unique ergodicity, in both time directions. (iii) uses Gottschalk-Hedlund for minimal flows (cited). Correct.
- **F.** P(rho w) = rho Xw when X rho + d rho = 0. In the converse, the ergodic measures are a.c. with densities that are positive a.e., hence equivalent, hence equal. Correct.

## 2. New reductions (proved)

**Lemma 2.1 (bounded Cesaro averages give a solution).** Assume GH and let f be smooth. Put u_T = (1/T) int_0^T S_t f dt, which is a smooth function. Suppose that along some sequence T_n -> inf the u_{T_n} are bounded in D'(M). Then f - c lies in X(C^inf) for some constant c. In particular, for f = d, (V) holds.

*Proof.*
1. The cocycle identity gives, pointwise,
   u_T o g_r - u_T = -S_r f + (1/T)[int_T^{T+r} - int_0^r] S_t f dt.
   Differentiating at r = 0 gives Xu_T = -f + S_T f / T.
2. A weakly bounded sequence in D'(M) is equicontinuous (Banach-Steinhaus; C^inf(M) is Frechet), hence bounded in some (C^k)', hence in some H^{-s}. So a subsequence converges weakly in H^{-s}, and therefore in D', to some u.
3. m_n := S_{T_n} f / T_n is bounded by ||f||_inf. Pass to a further subsequence converging weak* in L^inf(nu) to some m.
4. We have m_n o g_r - m_n = (S_{T_n+r} f - S_r f - S_{T_n} f)/T_n, which is O(r/T_n). Composition with g_r is weak*-continuous on L^inf(nu): its predual is psi -> (psi o g_{-r}) e^{J_{-r}} on L^1(nu). So m o g_r = m a.e. for every r.
5. For any w in L^1 and any test function phi, int (w o g_r) phi dnu = int w (phi o g_{-r}) e^{J_{-r}} dnu. The difference quotient of (phi o g_{-r}) e^{J_{-r}} at r = 0 converges uniformly to -(X phi + d phi). Hence the D'-derivative at r = 0 of w o g_r is Xw. From step 4, Xm = 0. By L1, m is a constant c.
6. Letting n -> inf in step 1 (X is continuous on D') gives Xu = -f + c. By GH, u is smooth. So f - c = X(-u). For f = d, (O3) gives (V). ∎

**Lemma 2.2 (uniform bounds).** Assume GH and let f be smooth. If sup_{t>=0} ||S_t f||_{L^inf(nu)} < inf, or if {S_t f : t >= 0} is bounded in some H^{-s}, then f - c lies in X(C^inf) (and in fact c = 0 in the first case). So under GH, **(V) holds if and only if sup_{t >= 0, x} |J_t(x)| < inf.**
*Proof.* Under either hypothesis the averages u_T are bounded in D', so Lemma 2.1 applies. Conversely, (V) gives J_t = log rho - log rho o g_t, which is bounded. ∎
(Unlike Lemma E(iii), this needs neither unique ergodicity nor Gottschalk-Hedlund.)

**Theorem 2.3 (one scalar bound suffices).** Assume GH. Then (V) holds if and only if
  liminf_{T -> inf} (1/T) int_0^T F(t) dt < inf,  where F(t) := -int J_t dnu^ >= 0.
By D2, F(t) is the relative entropy KL(nu^ || (g_{-t})_* nu^). The same holds with t -> -t, by applying the result to -X. In particular (V) holds if and only if sup_{t >= 0} F(t) < inf.

*Proof.*
(=>) Under (V), J_t is bounded uniformly, so F is bounded.
(<=)
1. We have (g_{-t})_* nu^ = g_t^* nu^ = e^{J_t} nu^. So KL(nu^ || e^{J_t} nu^) = int log(e^{-J_t}) dnu^ = F(t).
2. Let mu_T = (1/T) int_0^T (g_{-t})_* nu^ dt. KL is jointly convex, so KL(nu^ || mu_T) <= (1/T) int_0^T F(t) dt, and this is <= B along a sequence T_n -> inf.
3. Take a weak* limit mu of mu_{T_n}. It is invariant: the total variation of (g_r)_* mu_T - mu_T is at most 2|r|/T (Krylov-Bogolyubov).
4. KL is weak* lower semicontinuous, being by the Donsker-Varadhan formula KL(P||Q) = sup_{phi in C(M)} [P(phi) - log Q(e^phi)] a supremum of continuous functions. Hence KL(nu^ || mu) <= B.
5. So nu^ << mu. Write mu = rho nu + mu_s (Lebesgue decomposition with respect to nu). Then nu^({rho = 0}) = 0, and KL(nu^||mu) = -int log(nu(M) rho) dnu^ <= B. So log^- rho is in L^1(nu). Also log^+ rho <= rho is in L^1. Hence log rho is in L^1(nu).
6. g_t is nonsingular, so (g_t)_* maps nu-a.c. measures to nu-a.c. measures and nu-singular ones to nu-singular ones. By uniqueness of the Lebesgue decomposition, rho nu is invariant.
7. Lemma B ([R3-q2]; its proof is the computation in step 5 of Lemma 2.1 with w = log rho, f = d) gives (V). ∎

*Meaning.* Under GH, (V) is equivalent to **bounded entropy production**: the relative entropy of nu with respect to its transports stays bounded. A positive asymptotic entropy production rate e_p = lim F(t)/t = -mu_+(d) (for Cesaro limits mu_+ of (g_s)_* nu^) is the main thing to exclude, but F = o(t) alone would not suffice.
Contrapositive: **if (V) fails, then (1/T) int_0^T F(t) dt -> +inf**, and by Lemma 2.1 ||u_T||_{H^{-s}} -> inf for every s, where u_T is the Cesaro average of J.

**Proposition 2.4 (one orbit suffices).** Assume GH. If some x in M has sup_{t >= 0} |J_t(x)| = B < inf, then (V) holds. So if (V) fails, then for every x both sup_{t>=0} |J_t(x)| and sup_{t<=0} |J_t(x)| are infinite (the second claim by applying the first to -X).

*Proof.*
1. Choose t_n -> inf with g_{t_n} x -> y. For fixed t and n large (so that t + t_n >= 0), the cocycle identity gives J_t(g_{t_n} x) = J_{t+t_n}(x) - J_{t_n}(x), which lies in [-2B, 2B]. By continuity of J_t in x, |J_t(y)| <= 2B for all real t.
2. So P(s) = int e^{J_t(y) - s|t|} dt is finite, with P(s) in [e^{-2B} 2/s, e^{2B} 2/s]. By Lemma D (checked in section 1), T_s -> nu^ as s -> 0.
3. Let A_s = (s/2) int e^{-s|t|} delta_{g_t y} dt be the Abel averages. Then T_s <= P(s)^{-1} e^{2B} (2/s) A_s <= e^{4B} A_s, and likewise T_s >= e^{-4B} A_s, as positive measures.
4. Take s_n -> 0 with A_{s_n} -> mu weak*. Then mu is invariant: the total variation of (g_r)_* A_s - A_s is at most (s/2) int |e^{-s|t-r|} - e^{-s|t|}| dt <= s|r|.
5. Inequalities between positive measures survive weak* limits, so e^{-4B} mu <= nu^ <= e^{4B} mu.
6. Hence mu = rho nu^ with e^{-4B} <= rho <= e^{4B}. So log rho is bounded, and Lemma B gives (V). ∎

**Proposition 2.5 (Busemann-type functions).** Put G(x) = sup_{t in R} J_t(x) in [0, inf] and H(x) = inf_{t in R} J_t(x) in [-inf, 0].
- G is lower semicontinuous and H is upper semicontinuous.
- G o g_r = G - J_r and H o g_r = H - J_r.
- Assume GH. If G is finite on a set of positive nu-measure and G is in L^1(nu), then (V) holds. If G - H is finite on a set of positive measure, then (V) holds.

*Proof.*
1. The cocycle identity gives sup_t J_t(g_r x) = sup_t (J_{t+r}(x) - J_r(x)) = G(x) - J_r(x), and likewise for H.
2. If G is in L^1, then a = G satisfies a o g_r - a = -J_r a.e. By the computation in step 5 of Lemma 2.1, Xa = -d in D'. By GH, a is smooth, and e^{a} nu is invariant by (O3).
3. G - H is a measurable invariant function with values in [0, inf]. By (N1) it is a.e. equal to a constant c. If c < inf, then a.e. orbit has bounded J, and Proposition 2.4 applies. ∎

So when (V) fails, nu-a.e. orbit has J unbounded above or unbounded below on R. Also, if G < inf a.e., then e^G nu is a sigma-finite invariant measure with density >= 1. This does not contradict anything I know, because it may have infinite mass and G need not be integrable.

**Proposition 2.6 (physical measures).** Assume GH and dim M >= 2. Let mu be an ergodic invariant probability, and let B+(mu) be its forward basin (the points x with (1/T) int_0^T delta_{g_t x} dt -> mu). If nu(B+(mu)) > 0, then mu(d) = 0 and supp mu = M. The same holds for backward basins.

*Proof.*
1. B+(mu) is an invariant Borel set, so by (N1) it is conull.
2. Suppose mu(d) < 0. For nu-a.e. x we have J_t(x)/t -> mu(d) < 0, so int_0^inf e^{J_t(x)} dt < inf a.e. Here e^{J_t} = d(nu o g_t)/d nu. By Hopf's criterion (cited: a nonsingular flow is conservative iff int_0^inf (dnu o g_t / dnu)(x) dt = inf for nu-a.e. x), the flow is not conservative. This contradicts (N2).
3. By dominated convergence, (1/T) int_0^T (g_t)_* nu^ dt -> mu. By D2, mu(d) <= 0.
4. So mu(d) = 0. Then Corollary D1 gives supp mu = M. ∎

Also, under unique ergodicity J_t/t -> 0 uniformly (Lemma E(i)), so F(t) = o(t). In that case the whole gap for (V) is the difference between F(t) = o(t), which is known, and a bounded Cesaro mean of F, which is needed (Theorem 2.3).

## 3. Check of the chain (steps 2-3 of the brief)
I re-checked the chain:
- (V) => H: (O2) gives unique ergodicity. Lemma A plus the duality in Text A give X(C^inf) = {omega-mean-zero}. Lemma 2 of Text B gives the tame estimate.
- Then the variational principle, Pesin's formula and Katok's horseshoe theorem for C^{1+alpha} flows (Lian-Young; cited from memory) give h_top = 0 whenever omega is hyperbolic. Note that a periodic orbit would give a second invariant measure, contradicting unique ergodicity.

I found no flaw. The chain still needs the Missing Lemma in dim >= 4.

## 4. Where the attempt stops, and dead ends
- **Approximate solutions.** Every dynamical approximate solution of Xa = -d that I could build (the Cesaro averages u_T, Busemann functions, Abel-weighted orbit measures) controls the error only in C^0 or in the weak* sense. The a priori estimate of Text B needs C^m control. So GH can be used only through compactness and uniqueness arguments, as in Lemma 2.1, Theorem 2.3 and Proposition 2.4. Those need a bound on u_T in D', which is equivalent to (V).
- **Conformal side versus invariant side.** Lemma D gives the conformal limit nu^ for every orbit with subexponential J, without any bound. Comparing it with the invariant (unweighted) averages needs J bounded along one orbit (Proposition 2.4), which is again equivalent to (V).
- **Conjugates of X.** The operators X + d - J_T/T are conjugate to X by e^{u_T}, so they are GH. Their kernels are spanned by e^{u_T}, and the normalised e^{u_T} nu are approximately invariant probability measures. But the GH constants of these operators are not uniform in T, so nothing passes to the limit.
- **Measure theory alone cannot close the gap.** Conservative, ergodic, type III_1 nonsingular flows, such as dissipative transitive Anosov flows with respect to Lebesgue, have every property of nu that I derived from GH except the smooth ones. So any proof must use smoothness in an essential way, beyond L1.

## 5. Summary
**I did not prove (V), and I did not find a counterexample.** The following are proved, under GH and with dim M >= 2 where needed:
1. Planner lemmas C, C1 (first sentence), D, D1, D2, E and F are correct (section 1).
2. **Lemma 2.1 / 2.2.** For smooth f, if the Cesaro averages u_T of S_t f are bounded in D' along a sequence, then f - c lies in X(C^inf). In particular (V) <=> sup_{t>=0, x} |J_t(x)| < inf. This needs neither unique ergodicity nor Gottschalk-Hedlund.
3. **Theorem 2.3.** (V) holds if and only if the Cesaro means of F(t) = KL(nu^ || (g_{-t})_* nu^) = -int J_t dnu^ stay bounded along a sequence (bounded entropy production). If (V) fails, these means tend to infinity.
4. **Proposition 2.4.** (V) holds if J_t(x) is bounded for t >= 0 at a single point x.
5. **Proposition 2.5.** (V) holds if G = sup_t J_t is integrable and finite on a set of positive measure, or if the oscillation of J along orbits is finite on a set of positive measure.
6. **Proposition 2.6.** An ergodic measure with a basin of positive volume has mu(d) = 0 and full support.
7. The chain's steps 2-3 contain no flaw that I could find.

**Open:**
- (V) itself, equivalently bounded entropy production under GH.
- Even F(t) = o(t), that is, mu_+(d) = 0 for every Cesaro limit of the transported volumes, is open without unique ergodicity.
- Unique ergodicity under GH.
- From memory and unverified: I believe the literature (Forni, around 2008, on the Greenfield-Wallach and Katok conjectures) asserts GH => unique ergodicity with a smooth invariant volume. I could not reconstruct that proof and do not rely on it.

=== END OF ANSWER round4_q1 ===

