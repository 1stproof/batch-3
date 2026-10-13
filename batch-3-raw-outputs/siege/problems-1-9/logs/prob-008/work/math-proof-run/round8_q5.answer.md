# round8_q5 — answer (statement (J1))

## Plan (written first)
Target: (J1). Approach: compute exactly what (J1) says in Laplace form. Result obtained (Section 2): (J1) is
*equivalent*, for any smooth vector field (GH not used in the equivalence), to the absence of nonzero holomorphic
eigen-families T_z (T_z∘P = z T_z) on vertical strips a < Re z < b with 0 <= a < b. Then (Sections 3-4) sufficient
spectral conditions, model checks, a check of the "why it matters" derivation, and the precise open statement.
I did NOT prove (J1) and did not find a counterexample; Section 5 explains why a counterexample would have to be a
GH flow with a whole strip of non-imaginary eigen-distributions, which no known GH flow has.

Conventions as in the brief: Gamma_t phi := e^{J_t} (phi∘g_t), so F_phi(t) = S(Gamma_t phi), P phi = X phi + d phi.
Facts used (no GH): (t,x) -> e^{J_t(x)} phi(g_t x) is C^inf, so t -> Gamma_t phi is C^1 into C^inf(M) with derivative
Gamma_t P phi (Theorem J step 1, R6-a); and P Gamma_t phi = Gamma_t P phi. (Proof of the latter: by the cocycle
identity Gamma_s Gamma_t = Gamma_{s+t}; differentiate in s at s = 0: P Gamma_t phi = d/ds Gamma_{t+s} phi |_{s=0}
= Gamma_t P phi.)

## 1. Definitions

**Eigen-family (EF) on a strip.** Let a < b. An EF on Sigma(a,b) = {a < Re z < b} is a family of distribution densities
T_z, z in Sigma(a,b), such that
 (E1) z -> T_z(phi) is holomorphic on Sigma(a,b) for every smooth phi;
 (E2) T_z(P phi) = z T_z(phi) for all phi, z;
 (E3) for every closed substrip a < a1 <= Re z <= b1 < b there are k, N, C with |T_z(phi)| <= C (1+|z|)^N ||phi||_{C^k}.
It is *nonzero* if T_z != 0 for some z.

Lemma 1.1 (no GH). If T_z is a distribution density with T_z∘P = z T_z, then T_z(Gamma_t phi) = e^{zt} T_z(phi)
for all real t.
Proof. h(t) := T_z(Gamma_t phi) is C^1 with h'(t) = T_z(Gamma_t P phi) = T_z(P Gamma_t phi) = z h(t). ∎

In terms of generalized functions (Observation 0), t_z := T_z/nu satisfies X t_z = -z t_z: an EF is a holomorphic
family of eigen-distributions of X with eigenvalues -z filling a strip.

## 2. Theorem 2.1 (equivalence; proved; no GH needed)

Let X be any smooth vector field on a compact manifold.
(A) Let S be a distribution density, k, C, and real a < eps with |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} (t <= 0),
 |F_phi(t)| <= C e^{a t} ||phi||_{C^k} (t >= 0) [the hypothesis of (J1), here without requiring a >= 0].
 Then T_z(phi) := int_R e^{-zt} F_phi(t) dt is an EF on Sigma(a, eps), and if this EF is zero then S = 0.
(B) Conversely, if T is a nonzero EF on Sigma(a,b) and a < a' < b' < b, there is a nonzero distribution density S
 (complex; its real or imaginary part is a nonzero real one) satisfying the hypothesis of (A) with (a, eps) = (a', b').
Consequently:
 **(J1) holds for X  <=>  X has no nonzero EF on any strip Sigma(a,b) with 0 <= a < b.**
(=>: an EF on Sigma(a,b), a >= 0, gives by (B) a nonzero S with 0 <= a < a' < b' = eps, contradicting (J1).
 <=: given S as in (J1), (A) gives an EF on Sigma(a,eps), a >= 0, which must be zero, so S = 0.)

*Proof of (A).*
1. Holomorphy and bounds. For t <= 0, |e^{-zt}F_phi(t)| <= C e^{-(eps - Re z)|t|}||phi||_k; for t >= 0,
 <= C e^{-(Re z - a)t}||phi||_k. So the integral converges absolutely, locally uniformly on Sigma(a,eps), T_z(phi) is
 holomorphic and |T_z(phi)| <= C(1/(eps - Re z) + 1/(Re z - a))||phi||_k: (E1), (E3) (with N = 0) hold.
2. Eigen-relation. F_phi is C^1 with F_phi' = F_{P phi}. On [-R,R]: int e^{-zt}F_{P phi} dt = [e^{-zt}F_phi]_{-R}^{R}
 + z int e^{-zt}F_phi dt. The bounds of step 1 (applied to phi and P phi) make the boundary terms -> 0 and the integrals
 converge; so T_z(P phi) = z T_z(phi): (E2).
3. Split T_z = B_z + G_z, B_z(phi) := int_{-inf}^0 e^{-zt}F_phi dt (holomorphic on Re z < eps, |B_z(phi)| <=
 C||phi||_k/(eps - Re z)), G_z(phi) := int_0^inf e^{-zt}F_phi dt (holomorphic on Re z > a, |G_z(phi)| <=
 C||phi||_k/(Re z - a)). Suppose T = 0. Fix phi. Then E(z) := B_z(phi) on Re z < eps and E(z) := -G_z(phi) on
 Re z > a agree on the strip, so E is entire. With m = (a+eps)/2: |E| <= C||phi||_k/(eps - m) on Re z <= m and
 |E| <= C||phi||_k/(m - a) on Re z >= m. By Liouville E is constant; and E(x) = B_x(phi) -> 0 as x -> -inf along the
 reals (dominated convergence on t <= 0: for real x <= m, |e^{-xt}F_phi(t)| = e^{x|t|}|F_phi(t)| <=
 e^{m|t|}C e^{-eps|t|}||phi||_k, integrable, and e^{x|t|} -> 0 for t < 0 as x -> -inf). So E = 0.
4. In particular y -> B_{iy}(phi) = int_{-inf}^0 e^{-iyt} F_phi(t) dt vanishes identically: the L^1 function
 F_phi·1_{(-inf,0]} has zero Fourier transform, hence is 0 a.e.; F_phi is continuous, so S(phi) = F_phi(0) = 0. ∎

*Proof of (B).* Choose c in (a', b'). For real omega let rho_omega(z) := exp((z-c)^2 + omega(z-c)) (entire; on
z = sigma + iy, |rho_omega(z)| = exp((sigma-c)^2 - y^2 + omega(sigma-c)): Gaussian decay in y, uniformly on vertical
strips). Define
 S_omega(phi) := (1/2 pi i) int_{Re z = c} rho_omega(z) T_z(phi) dz.
By (E3) on the closed strip a' <= Re z <= b' (constants k, N, C), S_omega is a distribution density of order k.
1. Transport. By Lemma 1.1, F_phi(t) := S_omega(Gamma_t phi) = (1/2 pi i) int_{Re z = c} rho_omega(z) e^{zt} T_z(phi) dz.
2. Contour shift. The integrand is holomorphic on the closed strip [a', b'] and, by (E3) and the Gaussian factor, it
 is O(e^{-y^2/2}) on horizontal segments uniformly in sigma in [a',b'] (for fixed t). By Cauchy's theorem the line
 Re z = c can be moved to Re z = b' (use for t <= 0) or to Re z = a' (use for t >= 0). Hence
 |F_phi(t)| <= e^{b' t} K ||phi||_k for t <= 0 and |F_phi(t)| <= e^{a' t} K ||phi||_k for t >= 0, with
 K = (1/2pi) sup_{sigma in{a',b'}} int |rho_omega(sigma+iy)| C(1+|sigma+iy|)^N dy < inf.
 This is the hypothesis of (A) with eps = b', a = a'.
3. Nonvanishing. Since T != 0, pick z0, phi with T_{z0}(phi) != 0. If T_z(phi) vanished on the whole line Re z = c it
 would vanish on Sigma(a,b) (identity theorem), so h(y) := T_{c+iy}(phi) is a continuous, polynomially bounded function,
 not identically 0. Now S_omega(phi) = (1/2pi) int e^{-y^2} e^{i omega y} h(y) dy, the Fourier transform (at -omega) of
 the nonzero continuous L^1 function e^{-y^2}h; it is not identically 0 in omega. So S_omega != 0 for some omega.
4. Real form. For real phi set (Re S)(phi) := Re S(phi), extended complex-linearly; Re S and Im S satisfy the same
 bounds, and one of them is nonzero. ∎

**Corollary 2.2 (complete picture of "strip statements"; under GH).**
- Strips containing 0 (a < 0 < b): no nonzero EF. (Lemma M of R6-b on a small disc around 0, plus the identity
 theorem; equivalently Theorem J via Theorem 2.1(B) with a' < 0 < b'.)
- Strips with 0 <= a: no nonzero EF  <=> (J1) for X.
- Strips with b <= 0: no nonzero EF <=> (J1) for -X. (For -X: P_{-X} = -P, Gamma^{-X}_t = Gamma_{-t}; so T_z is an EF
 of X on Sigma(a,b) iff T_{-z} is an EF of -X on Sigma(-b,-a).)
So **(J1) for X and for -X together is equivalent to: a GH vector field has no nonzero holomorphic eigen-family
T_z∘P = zT_z (with (E3)) on any open vertical strip.** Equivalently, in terms of generalized functions: no
holomorphic, locally polynomially bounded family of eigen-distributions X t_z = -z t_z over a strip.

Remark 2.3 (what (J1) is NOT). A single eigen-distribution with real part kappa > 0 gives F_phi(t) = e^{zt}S(phi),
rate kappa on both sides, outside (J1) (as the brief notes). Theorem 2.1 shows that (J1) is precisely the statement
that eigenvalues off the imaginary axis cannot occur *holomorphically on an open set*; isolated eigenvalues are
irrelevant.

Remark 2.4 (the families that the problem actually produces). In the case lambda = mu(d) = 0 of the pair construction
(x != y, mu-generic, on one Pesin local unstable leaf), (A) gives a nonzero EF on Sigma(0, theta) (union over delta of
the strips (delta, theta - delta)) with |T_z(phi)| <= C_delta ||phi||_{C^1} for delta <= Re z <= theta - delta; it is
nonzero by R5-a step (f). So for the problem's purposes the needed statement is: **under GH no nonzero EF on
Sigma(0, theta)** (with blow-up of the bounds at Re z -> 0+ allowed). For lambda > 0 (stable pairs), the strip is
(max(0, lambda + delta - theta'), lambda - delta), which in the surviving range lambda >= |chi^-_max| (Prop 6.1)
does not touch 0; so for that case the full (J1), with a > 0, is needed.

## 3. Sufficient spectral conditions for (J1) (proved reductions)

For k >= 0 let Sigma_k := {z in C : there is a nonzero distribution density B of order <= k with B∘P = zB}
(the order-k point spectrum of the transpose of P; equivalently -Sigma_k is the set of eigenvalues of X on
generalized functions of order k). Sigma_k does not depend on nu: if nu' = e^{c}nu then P' phi = e^{-c}P(e^{c}phi),
and B -> B(e^{-c}·) is an order-preserving bijection between eigen-densities for P and P'.

**Proposition 3.1.** If for every k the set Sigma_k ∩ {Re z > 0} has empty interior, then (J1) holds.
Proof. Let S be as in (J1) (0 <= a < eps) and T the EF of Theorem 2.1(A); on Sigma(a,eps) ⊂ {Re z > 0} it has fixed
order k. If S != 0, T is nonzero, so T_{z}(phi) ≢ 0 for some phi; its zeros are discrete, so T_z != 0 and z in Sigma_k
for all z off a discrete set of the strip: Sigma_k contains an open set. ∎

**Proposition 3.2 (Jordan-chain form).** Say that z admits an order-k Jordan chain if there are distribution densities
A, B of order <= k, B != 0, with B∘P = zB and A∘P = zA + B. If for every k the set of z with Re z > 0 admitting an
order-k Jordan chain has empty interior, then (J1) holds. In fact a nonzero EF of order k on a strip produces an
order-k Jordan chain at every point of the strip off a discrete set.
Proof. Let T be a nonzero EF of order k on a closed substrip. T'_z(phi) := d/dz T_z(phi) = (1/2 pi i) oint T_w(phi)
(w-z)^{-2} dw over a small circle, so T'_z is a distribution density of order k. Differentiating (E2) in z:
T'_z(P phi) = zT'_z(phi) + T_z(phi). At every z with T_z != 0, (A,B) = (T'_z, T_z) is a Jordan chain. ∎

Remark 3.3 (why this is the natural generalisation of (K1), and where GH stops). At z = 0, GH excludes Jordan chains:
B∘P = 0 gives B = c nu (F1), and A∘P = c nu forces c = 0 (F2 = (K1)). The proof of (F2) is "u = A/nu satisfies
Xu = -c smooth, so u is smooth by GH, and Xu = 0 at a maximum of u". At z != 0 the analogous equations are
X b = -z b, X alpha = -z alpha - b (b = B/nu, alpha = A/nu): the right-hand sides are not smooth, so GH gives nothing.
If b and alpha were smooth, then: Re z != 0 => b = 0 (at a maximum of |b|^2, 0 = X|b|^2 = -2 Re z |b|^2);
Re z = 0 => |b| is a nonzero constant (X|b|^2 = 0, L1) and w := alpha/b is smooth with Xw = -1, contradicting (K1).
So smooth eigen-families and smooth Jordan chains are excluded for every z; the whole difficulty is that GH
(a statement about X = P - 0 only) does not make P - z hypoelliptic for z != 0. Note that P - z hypoelliptic for small
real z > 0 would by itself be a very strong statement: the continuous solution u_0 = int_{-inf}^0 e^{zs} f∘g_s ds of
(X + z)u = f (in the generalized-function form) would have to be smooth for every smooth f, which essentially says
that derivatives of f∘g_s grow subexponentially, i.e. it already contains the zero-entropy conclusion. So I see no
way to obtain hypoellipticity of P - z from GH that is not circular.

Remark 3.4 (one-sided divisibility, recorded; no GH). Under the hypothesis of (J1), with B_z, G_z as in the proof of
Theorem 2.1(A): Taylor expansion of B at 0 (radius eps) gives B_j(phi) := int_{-inf}^0 ((-t)^j/j!) F_phi dt (order k,
||B_j|| <= C eps^{-j-1}) with B_0∘P = S, B_j∘P = B_{j-1}; expansion of G at any z0 > a (radius z0 - a) gives G_j of
order k, ||G_j|| <= C (z0-a)^{-j-1}, with G_0∘(P - z0) = -S, G_j∘(P - z0) = G_{j-1}. So S is geometrically divisible
by P and by P - z0, with two "inverses" that may differ by an element of ker(·∘(P - z)); by Theorem 2.1 they agree
(on the strip) iff S = 0. This is the precise content of the brief's point (ii): divisibility alone carries no
contradiction unless ker(·∘(P - z)) is controlled for z in the strip.

## 4. Checks

**4.1 Models (proved).** Let Y be a Diophantine linear field on T^n (|k.alpha| >= c|k|^{-tau} for k != 0), nu = Lebesgue,
so d = 0, P = Y. If B∘Y = zB then with e_k = e^{2 pi i k.x}: (2 pi i k.alpha) B(e_k) = z B(e_k), so B(e_k) = 0 unless
z = 2 pi i k.alpha; since B is determined by its values on trigonometric polynomials, Sigma_k ⊂ 2 pi i{k.alpha}, a
countable subset of iR. By Proposition 3.1 (J1) holds for Y and for -Y; by invariance of Sigma_k under smooth
conjugacy (and under the change of nu) the same holds for every vector field smoothly conjugate to a Diophantine linear
field. (This is the only class of GH fields I know, so it is consistent with (J1).)
For a flow with an ergodic mu of positive entropy and mu(d) = 0 (not GH), R5-a Theorem B shows that (0, theta) minus a
discrete set lies in Sigma_1: an EF on Sigma(0, theta) exists. So (J1) is exactly the statement that GH removes this
continuum of non-imaginary eigenvalues.

**4.2 The "why it matters" derivation (checked; correct).**
- lambda = 0: x != y in G on one local unstable leaf (Lemma 6.0, conditionals non-atomic and carried by G).
 t <= 0: |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|}||phi||_{C^1} (R5-a step 4(c)), and J_t(x) <= C_delta + delta|t|,
 giving rate theta - delta; t >= 0: e^{J_t(x)}, e^{b + J_t(y)} <= C e^{delta t}. So a = delta < eps = theta - delta for
 small delta. Correct; constants depend on x, y, which is allowed.
- lambda > 0: x != y in G on one local stable leaf (Lemma 6.0 for g_{-1}); b' exists since d(g_t x, g_t y) <= C e^{-theta' t},
 t >= 0. t <= 0: no cancellation needed, e^{J_t(x)}, e^{b'+J_t(y)} <= C e^{-(lambda - delta)|t|}. t >= 0: cancellation
 gives C e^{J_t(x)} e^{-theta' t}||phi||_{C^1} <= C e^{(lambda + delta - theta')t}||phi||_{C^1}. Then
 a := max(0, lambda + delta - theta') < lambda - delta = eps as soon as 2 delta < theta' and delta < lambda. Correct.
- lambda < 0: -X is GH (O4), mu is (-X)-ergodic with the same entropy, divergence -d, mean -lambda > 0. Correct.
- S != 0 since x != y. And (J1) => h_mu = 0 for all ergodic mu, then the variational step. Correct, modulo the cited
 Pesin theory, Ruelle inequality and Ledrappier-Strelcyn/Lemma 6.0 as in R6-a.
So the chain "(J1) => problem" is sound. By Theorem 2.1 it can be restated: **the problem follows from: under GH,
X has no nonzero EF on any strip Sigma(a,b) with 0 <= a < b, nor (for -X) on any strip with a < b <= 0** — i.e. GH
forbids holomorphic families of non-imaginary eigen-distributions. (For the lambda = 0 case alone, strips Sigma(0,theta)
suffice, Remark 2.4.)

## 5. Can (J1) fail?
A counterexample needs a GH field X with a nonzero EF on a strip in {Re z > 0} (Theorem 2.1). By 4.1 such an X is not
smoothly conjugate to a Diophantine linear flow, so it would in particular be a counterexample to the
Greenfield-Wallach / Katok conjecture (cited from memory: the conjecture that every GH vector field is smoothly
conjugate to a Diophantine linear flow on a torus, up to the known time-change normalisations; proved, as I recall, only
in low dimensions, by Forni and Kocsard in dimension 3, under assumptions I cannot reconstruct reliably). Conversely, if
that conjecture were known in all dimensions, (J1) would follow from 4.1 (and the problem would follow trivially anyway).
So neither a proof via the conjecture nor a counterexample is within reach here.

## 6. Status / summary

PROVED (no GH needed unless stated):
1. Theorem 2.1: (J1) for X <=> no nonzero holomorphic, locally polynomially bounded eigen-family T_z∘P = zT_z on a
 vertical strip a < Re z < b with 0 <= a < b. Under GH (Corollary 2.2): (J1) for X and -X <=> no such family on any
 strip (strips through 0 are already excluded by Lemma M / Theorem J).
2. Propositions 3.1, 3.2: (J1) follows if, for each order k, the non-imaginary order-k point spectrum Sigma_k of the
 transpose of P has empty interior in {Re z > 0}, or if order-k Jordan chains (the z != 0 analogue of (K1)) occur only on
 a set with empty interior there. Smooth eigen-functions/Jordan chains are excluded at every z (Remark 3.3).
3. (J1) holds for every field smoothly conjugate to a Diophantine linear flow (4.1).
4. The derivation "(J1) => zero entropy" in the brief is correct (4.2); for the case mu(d) = 0 only strips Sigma(0, theta)
 are needed (Remark 2.4).

NOT PROVED / OPEN:
- (J1) itself. Equivalent open question (by Theorem 2.1): **(EF) Does GH exclude a nonzero holomorphic family of
 distributional eigen-solutions X t_z = -z t_z, of bounded order, for z in an open vertical strip in {Re z > 0}?**
 Sufficient: (E1-strip) for each k, {z : Re z > 0, X t = -z t has a nonzero solution of order k} has empty interior;
 or (K1_z) no order-k Jordan chain at z for z in an open set of {Re z > 0}.
- Why the available tools stop: GH (L1, F1, F2, tame estimate, closed range, dual solvability) concerns X = P - 0 only;
 all of them control the kernel/Jordan structure of P at z = 0 (Lemma M), and nothing transfers this to P - z, z != 0
 (Remark 3.3); one-sided divisibility (Remark 3.4) is equivalent to the hypothesis and carries no extra information.
- No counterexample: it would contradict the Greenfield-Wallach/Katok conjecture (Section 5).

=== END OF ANSWER round8_q5 ===
