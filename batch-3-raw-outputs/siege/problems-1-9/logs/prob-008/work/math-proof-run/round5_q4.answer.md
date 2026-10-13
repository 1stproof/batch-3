# round5_q4: attempt to refute (Lambda)

## Plan and status
Plan: (1) see what a counterexample to (Lambda) would have to look like, and what (Lambda) forces beyond the problem's claim; (2) go through the candidate classes (homogeneous flows, products and skew products, dimension 1) and either show GH fails or show lambda* = 0; (3) say what is left.

Outcome in brief: I found no counterexample, and I argue that none is realistically available (Section 1). I did not find a general proof of (Lambda) either. I prove that (Lambda) is strictly stronger than anything established so far: it implies that GH fields have no zeros and no periodic orbits (Section 2). For each candidate class I give a proved obstruction or a reduction (Sections 3-6).

## Section 1. Why a refutation is not realistic (meta-remark; literature cited from memory)
The Greenfield-Wallach conjecture says: a GH vector field lives on a torus and is smoothly conjugate to a Diophantine linear flow, possibly after a smooth time change. I recall it as proved in dimension <= 3 (Forni, about 2008, using F. and J. Rodriguez Hertz's theorem on cohomology-free systems and the first Betti number, and Kocsard's work). I cite this from memory and do not use it below.

For a Diophantine linear flow, Dg_t = Id. A smooth time change hX of it is again smoothly conjugate to a linear flow, since 1/h minus its mean is a smooth coboundary. Smooth conjugacy keeps ||Dg_t|| bounded. So every flow allowed by the conjecture has lambda* = 0. A counterexample to (Lambda) would therefore disprove the Greenfield-Wallach conjecture, and it would have to live in dimension >= 4 if my recollection about dimension 3 is right. Below I check that the natural candidate classes all fail.

## Section 2. What (Lambda) implies: it is strictly stronger than the problem (proved)
Write lambda*(X) for the quantity in (Lambda). By (O4), -X is GH whenever X is, so (Lambda) applies to both X and -X.

**Proposition 2.1.** Assume GH, dim M >= 2, and (Lambda) for X and for -X. Then:
(a) X has no zeros;
(b) X has no periodic orbits;
(c) every invariant probability mu has all its Lyapunov exponents equal to 0, and mu(d) = 0;
(d) the flow is minimal.

*Proof.*
(a) Let X(p) = 0 and A = DX(p). Then Dg_t(p) = e^{tA}. The norm dominates the spectral radius, so ||e^{tA}|| >= e^{t max Re spec A}, which gives lambda*(X) >= max Re spec A. In the same way, lambda*(-X) >= max Re spec(-A) = -min Re spec A. At a zero, div_nu X(p) = tr A, because div_{rho dx} X = sum_i d_i X^i + X^i d_i log rho. By P1, tr A = d(p) != 0. Since tr A is the sum of the Re lambda_i, either max Re spec A > 0 or min Re spec A < 0. So lambda*(X) > 0 or lambda*(-X) > 0, which contradicts (Lambda).
(b) Let gamma be periodic with period T through p. Let m_1, ..., m_{n-1} be the eigenvalues of Dg_T(p) other than the eigenvalue 1 in the flow direction. Since ||Dg_{kT}(p)|| >= (spectral radius of Dg_T(p))^k, (Lambda) for X gives |m_i| <= 1. Since Dg_{-T}(p) = Dg_T(p)^{-1}, (Lambda) for -X gives |m_i| >= 1. So |det Dg_T(p)| = 1. Also det Dg_T(p) = e^{J_T(p)} > 0, so J_T(p) = int_gamma d = 0. That is, the return map has Jacobian 1, which Observation P (R-b) excludes.
(c) Let mu be ergodic. Its top exponent is at most lambda*(X) = 0, and its bottom exponent is at least -lambda*(-X) = 0. So all its exponents vanish. By Birkhoff and Oseledets, mu(d) = lim J_t/t = lim (1/t) log det Dg_t is the sum of the exponents, which is 0. Non-ergodic mu follow by ergodic decomposition.
(d) By (c) and Corollary D1, every ergodic measure has full support. Every orbit closure carries an ergodic measure, so every orbit closure is M. ∎

**Consequence for the chain.** The problem only asks for zero entropy, and a flow with a hyperbolic zero or a dissipative hyperbolic periodic orbit can have zero entropy. (Lambda) excludes all of these, and the earlier rounds could not exclude them from GH without a smooth invariant volume (V). So (Lambda) is at least as hard as "GH implies no zeros and no periodic orbits". That statement is open in this chain, and it follows from (V) by (O2).

Under (V), (Lambda) is equivalent to the problem's claim. Indeed, (V) and GH give unique ergodicity with invariant measure omega (O2). Then h_top = h_omega by the variational principle. lambda* is the top exponent of omega, since the sup over ergodic measures of the top exponent equals lambda* for a continuous linear cocycle (standard, cited). Pesin's formula (cited) gives h_omega = sum of the positive exponents of omega. Since omega is invariant, the exponents sum to 0, so h_omega = 0 iff all exponents vanish iff lambda* = 0.

So (Lambda) is the right target only when combined with (V). Without (V) it is a harder statement than the problem.

## Section 3. Two general tools (proved)

**Lemma 3.1 (factors).** Let pi: M -> B be a smooth surjective submersion onto a compact connected manifold, with dpi(X) = X_B o pi for a vector field X_B on B. If X is GH, then X_B is GH.
*Proof.* Pull-back of distributions along a submersion is well defined and continuous. Locally pi is (x,y) -> x and pi^*u = u ⊗ 1. Also X(pi^*u) = pi^*(X_B u), which is checked on smooth u and extended by density. If X_B u is smooth, then X(pi^*u) is smooth, so u ⊗ 1 is smooth locally. Hence u is smooth: restrict to a slice y = const. ∎

**Lemma 3.2 (invariant submanifolds; generalises Observation P).** Let Sigma ⊂ M be a closed embedded X-invariant submanifold of positive codimension. Suppose X|_Sigma preserves a smooth positive density sigma on Sigma, and that d|_Sigma = X_Sigma(a) for some smooth function a on Sigma (here d = div_nu X). Then X is not GH.
*Proof.* Extend a to a smooth function ã on M and put nu' = e^{-ã} nu. Then d' := div_{nu'} X = d - Xã vanishes on Sigma, because Sigma is invariant, so (Xã)|_Sigma = X_Sigma a. The measure T = sigma, viewed on M, satisfies L_X T = 0. Let u = T/nu'. By Observation 0, <Xu, phi nu'> = -T(X phi + d' phi) = -T(d' phi) = 0, since T(X phi) = 0 and d' = 0 on supp T. So Xu = 0. But u ≠ 0 is carried by the nu'-null set Sigma, so u is not a smooth function. This contradicts GH (equivalently L1). ∎

*Remark.* If (Sigma, X|_Sigma) is itself GH, then by (O2) sigma is its only invariant density. By the duality consequence of Text A applied on Sigma, d|_Sigma is then a coboundary iff int_Sigma d sigma = 0, i.e. iff the sum of the sigma-normal Lyapunov exponents is 0. Examples are a Diophantine invariant torus whose normal Jacobian is 1 on average, and (Observation P) a periodic orbit whose return map has Jacobian 1.

If (V) holds, Lemma 3.2 is superseded: by (O2), any proper closed invariant set at all contradicts GH.

## Section 4. Homogeneous flows (class analysis)
Setting. G is a connected Lie group and Gamma a lattice with M = Gamma\G compact; G is then unimodular. Take X ∈ g and the flow g_t(Gamma h) = Gamma h exp(tX). Haar measure descends to a smooth invariant volume omega, so (V) holds. By (O2), GH therefore implies that the flow is uniquely ergodic and minimal.

**Lemma 4.0 (derivative).** Use the metric coming from an inner product on g (left-invariant metrics descend to Gamma\G). Then ||Dg_t(x)|| = ||e^{-t ad X}|| for every x. Hence lambda* = -min Re spec(ad X). Since tr ad X = 0, lambda* = 0 iff spec(ad X) ⊂ iR, and in that case ||Dg_t|| grows polynomially.
*Proof.* Right translation by a = exp(tX) maps the curve s -> h exp(sY) to h a exp(s Ad(a^{-1})Y). In the left-invariant frame its differential is therefore Ad(exp(-tX)) = e^{-t ad X}, independently of the point. Since the trace is 0, if some eigenvalue has nonzero real part then some eigenvalue has negative real part. ∎

So for homogeneous flows, (Lambda) amounts to: "GH implies spec(ad X) ⊂ iR".

**Proposition 4.1 (nilmanifolds).** If G is nilpotent, then ad X is nilpotent and lambda* = 0 for every X, whether or not X is GH. No counterexample is possible in this class. These flows have zero entropy: ||Dg_t|| grows polynomially, so h_top = 0 by step 2 of the chain.

**Lemma 4.2 (closed-orbit criterion).** Suppose that for some T ≠ 0 and some g ∈ G, g exp(TX) g^{-1} ∈ Gamma. Then the orbit of Gamma g is periodic, so for dim M >= 2 the field X is not GH.
*Proof.* Put gamma = g exp(TX) g^{-1}. Then Gamma g exp(TX) = Gamma gamma g = Gamma g. If X ≠ 0 the field has no zeros, so this is a genuine periodic orbit. Its orbit measure is invariant and differs from omega, which contradicts the unique ergodicity forced by GH and (V) (O2). If X = 0, then GH fails trivially. ∎

**Proposition 4.3 (Sol).** Let G = Sol = R^2 ⋊ R, where s acts by e^{sA} with A = diag(1,-1), and let Gamma be any cocompact lattice. If X has lambda* > 0, then X is not GH. Hence GH implies lambda* = 0 on Gamma\Sol.
*Proof.* Write g = n ⊕ R·A with n = R^2 abelian, and X = aA + Y with Y ∈ n.
- If a = 0, then ad X is nilpotent and lambda* = 0. So a ≠ 0.
- Since ad A is invertible on n and [n,n] = 0, Ad(exp Z)A = A - [A,Z] for Z ∈ n. Choosing Z = -(ad A)^{-1}(Y/a) gives Ad(exp Z)(aA) = X.
- Gamma is not contained in N. Otherwise the continuous surjection Gamma\G -> N\G ≅ R would have compact image. So some gamma_0 = (v, s_0) ∈ Gamma has s_0 ≠ 0.
- Conjugating by (w,0) gives (w + v - e^{s_0 A}w, s_0). Since e^{s_0 A} - I is invertible, we can choose w with w + v - e^{s_0 A}w = 0. So gamma_0 is G-conjugate to (0, s_0) = exp(s_0 A) = exp(T X') with X' = aA and T = s_0/a.
- Since X = Ad(exp Z)X', the element exp(TX) is G-conjugate to exp(TX'), and hence to gamma_0.
- Lemma 4.2 applies. ∎

**Proposition 4.4 (Gamma\PSL(2,R), Gamma cocompact).**
- If X is elliptic or parabolic, then spec ad X ⊂ iR and lambda* = 0.
- If X is hyperbolic, X is conjugate to aH with a ≠ 0, so ad X has eigenvalues 0 and ±2a, and lambda* > 0. A cocompact Fuchsian group contains hyperbolic elements (cited, standard). Each hyperbolic element is conjugate to exp(sH) for some s, so Lemma 4.2 shows that X is not GH.
So GH implies lambda* = 0 here as well.

**General G (sketch only, uses citations).** Suppose spec ad X ⊄ iR. Then X has a nontrivial "hyperbolic part". To refute GH it suffices to find any proper closed invariant set, by minimality (O2). For semisimple G with cocompact Gamma, I expect such sets to come from compact orbits of a Cartan subgroup containing the hyperbolic part of X. Their existence is the Prasad-Raghunathan theorem, cited from memory, and the subgroup orbits would also need to be invariant under the elliptic and unipotent parts. I have not carried this out. The mixed (Levi times radical) case is also not done. **Open:** a complete proof that a homogeneous GH flow has spec ad X ⊂ iR.

## Section 5. Products and skew products over Diophantine flows

**Proposition 5.1 (products).** Let X = X_1 ⊕ X_2 on M_1 × M_2. If X is GH, then X_1 and X_2 are GH. With the product metric, ||Dg_t|| = max(||Dg^1_t||, ||Dg^2_t||), so lambda*(X) = max(lambda*(X_1), lambda*(X_2)).
*Proof.* GH of the factors follows from Lemma 3.1 applied to the two projections. The derivative is block diagonal. ∎
So a counterexample built as a product already contains a counterexample in lower dimension.

**Proposition 5.2 (skew products with a fixed fibre field).** Let M = T^k × F, with F compact and connected, and let X = alpha·d_theta + c(theta) W, where W is a vector field on F and c > 0 is smooth. If X is GH, then:
- alpha is GH on T^k, i.e. alpha is Diophantine (Lemma 3.1 and the classical Fourier criterion);
- W is GH on F.
Moreover lambda*(X) >= (min c) lambda*(W).
*Proof.*
- GH of W: let v ∈ D'(F) with Wv smooth, and put u = 1 ⊗ v. Then Xu = c(theta) ⊗ Wv is smooth. By GH, u is smooth, hence v is smooth.
- The exponent bound: the flow is g_t(theta, y) = (theta + t alpha, phi^W_{tau(t,theta)}(y)) with tau(t,theta) = int_0^t c(theta + s alpha) ds >= t min c. The fibre block of Dg_t is Dphi^W_{tau}(y). ∎
So this class also reduces to lower dimension, namely to the fibre field W.

**General skew products X = alpha·d_theta + V(theta, y), V vertical.**
- If the fibre fields V(theta,·) preserve a common smooth fibre density m, then dtheta ⊗ m is invariant, because div_{dtheta⊗m} X = div_m V(theta,·) = 0. So (V) holds, and by (O2) any proper closed invariant set, for example an invariant graph, refutes GH.
- Without a common fibre volume, Lemma 3.2 refutes GH whenever there is a smooth invariant graph Sigma = {y = s(theta)} whose normal Jacobian averages to 0 over the Diophantine base. On Sigma the flow is conjugate to the Diophantine linear flow, which is GH and preserves Lebesgue measure; then use the Remark after Lemma 3.2.
- Dissipative invariant graphs (nonzero average normal Jacobian) are not excluded by any result I have, and neither are skew products whose fibre dynamics has no invariant graph. This is the same gap as dissipative periodic orbits (R-b), and I cannot close it. It is exactly where (V) is missing.

**Conjugates and time changes (O4).** These preserve GH. Under a smooth conjugacy, lambda* is unchanged, since ||DΦ|| and ||DΦ^{-1}|| are bounded. Under a time change hX with h > 0, lambda* need not be preserved in general, but in the presence of (V) the classes above are closed under time change for the purposes of (Lambda). Indeed, the time change hX preserves the smooth volume omega/h, the time-changed flow is still uniquely ergodic, and Abramov's formula (cited) gives h_{omega/h}(hX) = h_omega(X) / int (1/h) dω̂, where ω̂ is the normalised volume. By Section 2 the time-changed flow therefore has zero exponents iff X does. So these operations produce no new candidates.

## Section 6. Dimension 1 (proved), and a remark on dimension 2

**Proposition 6.1.** On M = S^1, a GH field has no zeros. Hence the flow is smoothly conjugate to a rotation flow, ||Dg_t|| is bounded, lambda* = 0, and h_top = 0.
*Proof.*
- Suppose X(p) = 0. Let u be the sawtooth function θ - p on (p, p + 2π), with a jump at p. Then u' = 1 - 2π δ_p in D', so Xu = X·u' = X - 2π X(p) δ_p = X, which is smooth. But u is discontinuous, contradicting GH.
- So X ≠ 0 everywhere. In the coordinate s = int dθ/X we have X = c d_s with c constant, and the flow is a rotation. ∎

Dimension 2: every continuous flow on a compact surface has zero topological entropy (Young, 1977, cited from memory). So the problem's claim holds for dim M <= 2 without GH. (Lambda) in dimension 2 is not settled here, because hyperbolic zeros are not excluded (cf. Section 2).

## Section 7. Attempts at a general proof under (V), and why they stall
Assume GH and (V). The case "(V) fails" is not covered by anything below. Then omega is the unique invariant measure, and every smooth f with omega(f) = 0 equals Xu with ||u||_{C^k} <= C ||f||_{C^m} (Text B). By Section 2, (Lambda) is then equivalent to h_omega = 0.

(a) Spectral route.
- Iterating X^{-1} on mean-zero smooth functions shows: for every j, the spectral measure of each smooth f satisfies sigma_f((-eps, eps)) <= C_j eps^{2j} ||f||^2_{C^{m_j}}.
- If h_omega > 0, the Koopman flow has a Lebesgue-spectrum component of infinite multiplicity on the orthocomplement of the Pinsker factor (Rokhlin-Sinai type theorem for flows, cited).
- To get a contradiction one needs a smooth f, or an f in H^s with s large compared to the derivative loss m_j/j, whose projection to that component has spectral density bounded below near 0.
- Soft arguments do not produce such an f. In L^2(R, l^2) with multiplication by iλ, the vectors whose Fourier transform vanishes to infinite order at 0 form a dense subspace. So some input from Pesin theory, such as regularity of the unstable foliation, would be needed. **Dead end as it stands.**

(b) Bounded-deviation counting.
- The integrals int_0^t f(g_s x) ds are bounded by C ||f||_{C^m}, uniformly in x and t.
- Counting (T, eps)-separated orbits against bounded Lipschitz Birkhoff paths gives only exponential bounds, so it yields no contradiction with h > 0. **Dead end.**

(c) Eigen-distribution route.
- This is (E1) of R4-q10 together with Lemma C there.
- Not resolved. Note that resolvents (s - X)^{-1} = int_0^∞ e^{-st} (·) o g_t dt are bounded on C^k only for s > k lambda*. This is consistent with lambda* > 0 and gives no contradiction by itself.

## Summary
**Proved:**
1. (Lambda), applied to X and -X, implies that a GH field has no zeros, no periodic orbits, only invariant measures with zero exponents and mu(d) = 0, and that the flow is minimal (Prop. 2.1). So without (V), (Lambda) is strictly harder than the problem.
2. Under (V), (Lambda) is equivalent to zero entropy (Section 2, using Pesin's formula, cited).
3. Lemma 3.1 (GH passes to smooth factors) and Lemma 3.2 (an invariant submanifold carrying an invariant density with coboundary normal divergence refutes GH).
4. No counterexample to (Lambda) exists among: nilmanifold flows (lambda* = 0 always); flows on compact Gamma\Sol and Gamma\PSL(2,R) (lambda* > 0 implies a periodic orbit, which refutes GH); products, and skew products alpha + c(theta)W over a torus (these reduce to lower dimension); volume-preserving skew products with an invariant graph; conservative invariant graphs in general; and dimension 1 (GH implies no zeros, hence a rotation).

**Sketched or cited:**
- The general homogeneous case (Prasad-Raghunathan).
- The dimension 2 entropy statement (Young).
- The meta-remark that a counterexample would disprove the Greenfield-Wallach conjecture, which I recall as proved in dimension 3 (Forni; Kocsard; F. and J. Rodriguez Hertz).

**Open:**
- (Lambda) in general.
- Whether GH excludes dissipative invariant tori, dissipative periodic orbits and hyperbolic zeros without (V).
- (V) itself.
- Under (V), whether cohomology-freeness with tame estimates forces h_omega = 0.
- The problem's claim in dimension >= 4 (in dimension <= 2 it holds for all flows; in dimension 3 it follows from the cited Greenfield-Wallach result).

Recommendation to the planner: (Lambda) without (V) is the wrong target. Prove (V) first. Then (Lambda) is equivalent to h_omega = 0, and that is where work should concentrate.

=== END OF ANSWER round5_q4 ===
