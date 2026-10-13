# round11_q1 — answer (worker draft, written incrementally)

## Plan
Target: the missing statement (AP), or zero entropy for GH flows by any route.
Steps: (1) check the chain (Theorem R' Steps 1-4 with G ∩ Rec; the reduction X -> -X);
(2) look for a new mechanism, mainly in the core case lambda = 0 with a smooth invariant volume (d = 0);
(3) write down rigorously whatever partial results come out, and the exact point where the argument stops.

## Summary of outcome (filled in at the end)
I do NOT prove (AP), and I do NOT prove zero entropy for GH flows. I give no counterexample either. What follows:
(A) a check of the chain: I find no flaw in it;
(B) two proved observations in the volume case. They are new as far as I can tell from the brief, and both are only partial:
 - B1 (spectral thinness at 0);
 - B2 (every one-pair consequence of the tame inverse is automatically consistent), which explains why pair-only arguments that use GH only through the inverse of X cannot close the case lambda = 0;
(C) the exact point where the argument stops, plus literature recalled from memory with stated uncertainty.

## (A) Check of the chain
Step 1. The variational principle for the homeomorphism g_1 gives a g_1-invariant measure with positive entropy. The ergodic decomposition together with Jacobs' formula gives a g_1-ergodic one. Correct.

Step 2. Let nu' be g_1-ergodic with h > 0. By Ruelle's inequality, (g_1, nu') has a positive exponent; the flow direction contributes exponent 0. Pesin local unstable manifolds exist a.e. for the positive part of the spectrum: these are strong unstable discs, transverse to X. For y in W^u_loc(x) we have dist(g_{-n}x, g_{-n}y) <= C_0 e^{-theta n} for integers n >= 0. Since sup_{|s|<=1} ||Dg_s|| < infinity, the same bound holds for real t <= 0 with a larger C.

G: since nu' is g_1-ergodic, J_n(z)/n -> nu'(J_1) a.e. as n -> +-infinity (Birkhoff for g_1 and g_{-1}). Since |J_t - J_{[t]}| <= ||d||_inf, the limit along real t follows. So nu'(G) = 1.

Rec: Poincare recurrence for g_1 (resp. g_{-1}) gives a.e. z with g_{n_k} z -> z along n_k -> +infinity (resp. -infinity). Hence z lies in omega(z) and in alpha(z) for the flow.

Existence of y: the conditional measures of nu' on the elements of xi are non-atomic a.e., because h > 0 (Ledrappier-Young: h_nu'(g_1, xi) = h > 0 forces non-atomic conditionals). A full-measure set has full conditional measure on a.e. element. So for a.e. x in G ∩ Rec there is y != x in xi(x) ∩ G ∩ Rec.

Hence (a), (b), (c) hold with lambda = nu'(d). One remark: y is not of the form g_tau x with tau != 0. Indeed x is not a zero of X (a zero would be an atom of nu', impossible for an ergodic non-atomic measure with positive entropy). Along backward returns of x, the distance dist(g_t x, g_{t+tau} x) stays bounded below, so it does not tend to 0. This is not needed for (AP), which only asks x != y.

Step 3. Under X -> -X: div_nu(-X) = -d, and the flow of -X is g_{-t}. So J^{-X}_t(z) = int_0^t (-d)(g_{-s} z) ds = J_{-t}(z). Also nu' is ergodic for g_{-1} with the same entropy, and (O4) gives GH for -X. The new lambda is -lambda. Correct.

Conclusion of (A): the chain (AP) => [GOAL] is sound. All of the difficulty sits in (AP).

## (B) Partial results in the volume case
Standing assumption for this section: GH, and X preserves a smooth positive probability density omega (so d = 0 and every J_t = 0 when nu = omega). By (O2) the flow is uniquely ergodic and minimal, and omega-mean-zero smooth functions are exactly X(C^inf). By Text B Lemma 2, the solution u_f in C^inf_0 of Xu = f satisfies ||u_f||_{C^k} <= C_k ||f||_{C^{m(k)}}.

### B1 (proved). Spectral thinness at 0
Let U_t f = f o g_t be the unitary group on L^2(omega). Let A be its generator, so A f = Xf on C^inf. For f in L^2 let sigma_f be its spectral measure: <U_t f, f> = int e^{i t s} d sigma_f(s).
Claim: for every smooth f with omega(f) = 0 and every k >= 1,
 int s^{-2k} d sigma_f(s) < infinity, sigma_f({0}) = 0, and sigma_f((-eps, eps)) <= eps^{2k} ||u^{(k)}||_{L^2}^2.
Here u^{(k)} is the smooth mean-zero function with X^k u^{(k)} = f.
Quantitatively, sigma_f((-eps, eps)) <= C eps^2 ||f||^2_{C^{m(0)}}.

Proof. Iterating the solvability gives u^{(1)} = u_f, then u^{(j+1)} = u_{u^{(j)}} (each u^{(j)} is mean zero and smooth), so X^k u^{(k)} = f. Since C^inf is invariant under U_t and dense, Nelson's core theorem (cited) shows it is a core for A, and A = X there. Hence f = A^k u^{(k)}. By the spectral theorem, sigma_f(ds) = s^{2k} sigma_{u^{(k)}}(ds), which gives all the claims. For the quantitative form take k = 1 and use ||u_f||_{L^2} <= ||u_f||_{C^0} <= C ||f||_{C^{m(0)}}. QED

Consequence and limitation. Suppose h_omega(g_1) > 0. Then h_top > 0 forces h_omega > 0, by unique ergodicity and the variational principle. By Rokhlin-Sinai (cited: a flow with positive entropy has countable Lebesgue spectrum on the orthocomplement H_L of L^2 of the Pinsker factor), the projections P_L f of smooth f are dense in H_L. B1 says each such projection has a spectral density that vanishes to infinite order at s = 0.
This is NOT a contradiction by itself: inside a Lebesgue-spectrum space, the vectors with spectral density vanishing to infinite order at 0 form a dense subspace. A contradiction would need a smooth f whose projection P_L f has spectral density positive at 0, i.e. a non-zero "asymptotic variance" int_R <U_t P_L f, P_L f> dt. I could not produce such an f. In the hyperbolic case it comes from periodic orbits (the Livsic obstruction), which are already excluded in the volume case.

### B2 (proved). The pair functional is the normalised transfer solution and stays bounded under the flow
Let x != y satisfy (a) of (AP) (d = 0, so (b) holds with lambda = 0). Put
 Phi(f) = int_{-inf}^0 ( f(g_s x) - f(g_s y) ) ds.
Then:
(i) Phi is a distribution of order 1. Phi(1) = 0, and Phi(Xu) = u(x) - u(y) for all smooth u.
(ii) Phi is the unique distribution with the properties in (i).
(iii) For all real t, the functional (g_t)_* Phi : f -> Phi(f o g_t) = int_{-inf}^t (f(g_s x) - f(g_s y)) ds is the unique such solution for the pair (g_t x, g_t y). There are m and C, independent of x, y and t, with
 | int_{-inf}^t ( f(g_s x) - f(g_s y) ) ds | <= C ||f||_{C^m} dist(g_t x, g_t y) for all smooth f.

Proof.
(i) By (a), |f(g_s x) - f(g_s y)| <= ||df||_inf C e^{theta s}, so the integral converges. Also
 Phi(Xu) = lim_{R -> inf} [u(g_s x) - u(g_s y)]_{s=-R}^{0} = u(x) - u(y).
(ii) The difference D of two solutions vanishes on X(C^inf) + R·1 = C^inf (by (O2), X(C^inf) has codimension 1 and does not contain 1). So D = 0.
(iii) The identity follows from the change of variables s -> s + t. For the bound, (O1) gives S with S(Xu) = u(x') - u(y') and ||S||_{(C^m)'} <= C dist(x', y'). Then S' = S - S(1) omega is also a solution, with S'(1) = 0 and ||S'|| <= C'' dist(x', y'). Indeed |S(1)| <= ||S|| ||1||_{C^m}, and omega has norm <= 1 on (C^m)'. By (ii), S' is the transported Phi. QED

Why B2 cannot close (AP) at lambda = 0. Statement (iii) holds for every pair (x', y') along the orbit pair; it is the full content of the tame inverse at the pair level. The two-sided weighted-decay argument (Theorem J) needs (g_t)_* S -> 0 in both time directions. Here (iii) gives only boundedness in the forward direction, and boundedness is exactly what any smooth transfer function u_f produces. To exclude the pair, a proof must use input beyond the inverse of X restricted to the pair: for example the multiplicative structure of C^inf, or genuinely many orbits (recurrence used quantitatively). The suggestion's four-point recurrence scheme is one attempt at this. It fails because recurrence of x only brings g_{-s}x near x. It does not make g_{t-s}x track g_t x for t >= 0, which is what forward cancellation needs (that would be the stable-manifold relation, i.e. the forward-asymptotic case already handled by Theorem G).

## (C) Where the argument stops; literature (from memory); open questions
1. Proved here: (A), the chain check (no flaw found); B1; B2.
   Not proved: (AP) in the cases lambda = 0 and lambda <= -theta. The case -theta < lambda < 0 holds by Theorem J, as the brief states.
   Hence the [GOAL] (zero topological entropy for GH flows) remains unproved in this answer.

2. The exact obstruction, in the volume case. The flow is uniquely ergodic, so positive topological entropy means h_omega > 0. If omega is hyperbolic (no zero exponents besides the flow direction), Katok's closing/horseshoe theorem for flows (cited) produces periodic orbits, and (O2) forbids them. What remains is the case where omega has positive entropy and also zero exponents transverse to the flow.
   For such a flow, B1 and B2 show that the consequences of GH that I could extract through the inverse of X — spectral thinness at 0 and bounded transfer integrals along unstable pairs — are formally compatible with positive entropy. Two things are missing:
   (Q1) a smooth f whose Pinsker-orthogonal part has positive spectral density at 0;
   (Q2) a pair-level mechanism that produces two-sided decay.

3. Literature, recalled from memory and NOT verified; please treat it as a pointer only.
   - Flaminio and Paternain ("Linearization of cohomology-free vector fields", around 2011): I recall the statement that a cohomology-free vector field (every smooth f is cohomologous to a constant via a smooth transfer function) embeds continuously in a linear flow on an abelian group. If "embeds" means injectively and equivariantly into a compact abelian group with a translation flow, this would give equicontinuity and hence zero entropy in the volume case, since GH plus a smooth invariant volume implies cohomology-free by (O2). I cannot reconstruct their proof. The obvious construction (circle-valued v with Xv constant, one per class in H^1(M; Z)) only gives a torus factor of dimension b_1(M), which need not be injective.
   - Forni (Greenfield-Wallach and Katok conjectures in dimension 3) and Kocsard (Katok conjecture for cohomology-free vector fields in dimension 3): these treat dimension 3. The brief records that dim M <= 3 is already settled here (Theorem J).
   I am not aware, with confidence, of a published proof that GH alone, without an invariant volume, implies zero entropy.

Open questions, explicitly:
 (AP0) (AP) with lambda = 0, including the volume case d = 0.
 (AP-) (AP) with lambda <= -theta.
 (Q1) and (Q2) above.
 (V) Does GH imply a smooth invariant volume? This would reduce everything to the volume case.
 (FP) Does the Flaminio-Paternain embedding, if correctly recalled, give injectivity? If so, the volume case would follow.

4. Checked and dead here: the "eigenfunction" route to an embedding in the volume case. Take a smooth phi: M -> S^1 and write X(log phi) = i f. Solving f = c + Xw gives a smooth eigenfunction psi = phi e^{-iw} with X psi = i c psi.
   But if phi is null-homotopic, then psi is constant: phi = e^{iv}, X(v - w) = c, and integrating against omega forces c = 0, so v - w is constant by L1.
   So smooth eigenfunctions modulo constants correspond exactly to H^1(M; Z). They give only a torus factor of dimension at most b_1(M), which cannot separate points in general (for example, when M is simply connected).
   Equicontinuity therefore cannot be obtained this way. The only remaining candidate source is the uniform boundedness of all smooth cocycles, sup_{t,x} |int_0^t (f - omega(f))(g_s x) ds| <= C ||f||_{C^m}, and I could not derive equicontinuity from it.

=== END OF ANSWER round11_q1 ===

