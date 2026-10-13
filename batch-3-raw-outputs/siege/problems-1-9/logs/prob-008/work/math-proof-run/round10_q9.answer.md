# round10_q9 answer

## 0. Plan and verdict

**Plan.** (a) Find out exactly how (J2-prod) and (J2) relate to the open statement (EF): "under GH there is no nonzero holomorphic order-k eigen-family of P^T on a vertical strip". (b) Run the moment argument of Theorem J on M x M for D = S (x) S and find what each moment says. (c) Look for a way to kill m_0 using GH of X.

**Verdict (proved below).**
1. (J2-prod) implies (EF) (Proposition A). So the tensor statements (J2) => (J2-prod) are at least as strong as the open statement (EF).
2. Call S *tilted-decaying* if N_S(t) <= C e^{ct - eps|t|} for some real c. The distributions S produced by Theorem R' are tilted-decaying. For such S, (J2-prod) for S is equivalent to the vanishing of the eigen-family T_z = Laplace transform of S on the strip |Re z - c| < eps (Proposition B). So the tensor route reaches the [GOAL] exactly when (EF) does. It gives no reduction, and its extra generality (oscillating log N_S) is irrelevant to the problem.
3. On M x M, for tilted-decaying S the moments are m_j(phi (x) psi) = (1/2 pi i) int_{Re z = c} (-d/dz)^j T_z(phi) T_z(psi) dz (Proposition C). Moreover **m_0 = 0 already forces S = 0** (Proposition D). So the Jordan-chain induction on M x M has no content beyond its first step. Any proof along the "kill m_0 using GH of X" line is literally a proof that T is identically 0, i.e. of (EF) for T. This is the exact point where the tensor route stops. I could not prove (J2-prod), (J2) or (EF), and I found no counterexample.

Throughout: nu is a smooth positive density, d = div_nu X, J_t is the log nu-Jacobian, Gamma_t phi = e^{J_t}(phi o g_t), P = X + d. Facts used: Gamma_{t+s} = Gamma_t Gamma_s (cocycle identity); t -> Gamma_t phi is C^1 into C^inf(M) with derivative Gamma_t P phi = P Gamma_t phi (Theorem J, step 1); int Gamma_s psi dnu = int psi dnu (change of variables).

**Basic Lemma 0.** If T is a distribution density with T(P phi) = z T(phi) for all smooth phi, then T(Gamma_t phi) = e^{zt} T(phi) for all real t.
*Proof.* Put h(t) = T(Gamma_t phi). Then h is C^1 and h'(t) = T(P Gamma_t phi) = z h(t). ∎

## 1. Proposition A: (J2-prod) implies (EF)

**(EF_k), the form used here.** Let Omega = {a < Re z < b}. A *strip family of order k* is a family (T_z), z in Omega, of linear functionals on C^inf(M) with:
- (i) z -> T_z(phi) is holomorphic for each smooth phi;
- (ii) for every closed substrip K there is C_K with |T_z(phi)| <= C_K ||phi||_{C^k} for z in K;
- (iii) T_z(P phi) = z T_z(phi).

(EF_k) says: under GH every such family vanishes identically. (Theorem R' produces such a family with k = 1.)

**Proposition A.** Fix k. Suppose (J2-prod) holds for distributions of order <= k. Then (EF_k) holds.

*Proof.* Let (T_z) be a strip family of order k on {a < Re z < b}. Fix a < a' < b' < b, put c = (a'+b')/2 and C' := C_{[a',b']}. For smooth phi define
 S(phi) := (1/2 pi) int_R e^{(c+iy)^2} T_{c+iy}(phi) dy.
Since |e^{(c+iy)^2}| = e^{c^2 - y^2}, the integral converges and |S(phi)| <= C' e^{c^2} pi^{-1/2} ||phi||_{C^k}. So S is a distribution density of order <= k.

*Step 1 (contour shift).* By Lemma 0, T_z(Gamma_t phi) = e^{zt} T_z(phi). Hence
 S(Gamma_t phi) = (1/2 pi i) int_{Re z = c} e^{z^2 + zt} T_z(phi) dz.
The integrand is holomorphic on the strip. On the horizontal segments Im z = +-Y, a' <= Re z <= b', it is bounded by e^{b'^2 + max(|a'|,|b'|)|t| - Y^2} C' ||phi||_{C^k}, which tends to 0 as Y -> inf. So by Cauchy's theorem the line Re z = c can be replaced by Re z = c' for any c' in [a', b']:
 |S(Gamma_t phi)| <= (1/2 pi) int_R e^{c'^2 - y^2 + c' t} C' ||phi||_{C^k} dy = C'' e^{c' t} ||phi||_{C^k}.
For t >= 0 take c' = a'; for t <= 0 take c' = b'. With N_S defined by the C^k unit ball:
 N_S(t) <= C'' e^{a' t} (t >= 0),  N_S(t) <= C'' e^{-b'|t|} (t <= 0).
Hence N_S(t) N_S(-t) <= C''^2 e^{-(b'-a')|t|} for all real t.

*Step 2 (S is nonzero unless T vanishes).* By (J2-prod), S = 0. Then S(Gamma_{-s} phi) = 0 for every real s and every smooth phi, because Gamma_{-s} phi is smooth. By Lemma 0,
 0 = S(Gamma_{-s} phi) = (e^{-cs}/2 pi) int_R e^{-iys} G_phi(y) dy,  with G_phi(y) := e^{(c+iy)^2} T_{c+iy}(phi).
G_phi is continuous and integrable, and its Fourier transform vanishes identically. By Fourier uniqueness on L^1, G_phi = 0, so T_{c+iy}(phi) = 0 for all real y. By the identity theorem, T_z(phi) = 0 on the whole strip. Since phi is arbitrary, T vanishes identically. ∎

## 2. Proposition B: for the S that matter, (J2-prod) is the same as (EF)

**Definition.** A distribution density S of order <= k is *tilted-decaying (at c, rate eps)* if N_S(t) <= C e^{ct - eps|t|} for all real t.

**Proposition B.** Let S be tilted-decaying at c with rate eps. For |Re z - c| < eps and smooth phi put
 T_z(phi) := int_R e^{-zt} S(Gamma_t phi) dt.
Then:
- (T_z) is a strip family of order k on {c - eps < Re z < c + eps};
- T vanishes identically iff S = 0.

Consequently (EF_k) implies the conclusion of (J2-prod) for every tilted-decaying S. The S of Theorem R' is tilted-decaying, with k = 1, c = lambda + theta/2 and rate theta/2 - delta > 0. Indeed, for t >= 0, e^{-ct} N_S(t) <= C_3 e^{(delta - theta/2)t}; for t <= 0, e^{-ct} N_S(t) <= C_2 e^{(lambda + theta/2 - theta - lambda + delta)|t|} = C_2 e^{-(theta/2 - delta)|t|}. So, as far as the [GOAL] is concerned, (J2-prod) is used only on tilted-decaying S, where it is equivalent to (EF). Its extra generality concerns S whose log N_S oscillates with no supporting line of positive margin (caveat (iii) of the task), and the [GOAL] never needs such S.

*Proof.*
- *Convergence.* |e^{-zt} S(Gamma_t phi)| <= C e^{(c - Re z)t - eps|t|} ||phi||_{C^k}. On a closed substrip |Re z - c| <= eps - eta this is at most C e^{-eta|t|} ||phi||_{C^k}. This gives (ii) with C_K = 2C/eta.
- *Holomorphy (i).* The convergence is locally uniform in z, so (i) follows by Morera's theorem and Fubini.
- *(iii).* t -> S(Gamma_t phi) is C^1 with derivative S(Gamma_t P phi). Integrate by parts on [-R, R]:
 int_{-R}^R e^{-zt} S(Gamma_t P phi) dt = [e^{-zt} S(Gamma_t phi)]_{-R}^{R} + z int_{-R}^R e^{-zt} S(Gamma_t phi) dt.
 The boundary term tends to 0. So T_z(P phi) = z T_z(phi).
- *Nonvanishing.* T_{c+iy}(phi) is the Fourier transform at y of the continuous L^1 function t -> e^{-ct} S(Gamma_t phi). If T vanishes identically, this function is 0, and at t = 0 this gives S(phi) = 0. Conversely S = 0 gives T = 0 trivially. ∎

*Consequence of A and B.* (J2) => (J2-prod) (Prop. T' of block R9-d) => (EF_k). Neither tensor statement is weaker than (EF). Since (EF) is exactly the statement round 9 could not prove, the tensor route is not a reduction; at best it is a different formulation.

## 3. Proposition C: the M x M moments of S (x) S, explicitly

Let S be tilted-decaying at c with rate eps, of order k, and let T_z be its strip family (Proposition B). For smooth phi, psi put a(t) = S(Gamma_t phi) and b(t) = S(Gamma_t psi). Then
 (S (x) S)((Gamma_t (x) Gamma_{-t})(phi (x) psi)) = a(t) b(-t),  |a(t) b(-t)| <= C^2 e^{-2 eps|t|} ||phi||_{C^k} ||psi||_{C^k}.
(The tilt e^{ct} e^{-ct} cancels; this is the point of the tensor trick.) The moments m_j(phi (x) psi) = int t^j a(t) b(-t) dt determine the m_j: each m_j is a distribution on M x M, and the span of products is dense in C^inf(M x M).

**Proposition C.** For all smooth phi, psi and every j >= 0:
 m_j(phi (x) psi) = (1/2 pi) int_R [(-d/dz)^j T_z(phi)]_{z = c+iy} T_{c+iy}(psi) dy.
In particular m_0 = (1/2 pi i) int_{Re z = c} T_z (x) T_z dz (Parseval).

*Proof.*
1. *Decay of B(z) := T_z(psi) on the line.* By (iii) twice, z^2 T_z(psi) = T_z(P^2 psi). So |B(c+iy)| <= C_K min(||psi||_{C^k}, ||P^2 psi||_{C^k} / |c+iy|^2), which is integrable in y.
2. *Fourier inversion.* The function e^{-ct} b(t) is continuous and in L^1, and its Fourier transform y -> B(c+iy) is integrable. So inversion holds pointwise: b(-t) = (1/2 pi) int e^{-(c+iy)t} B(c+iy) dy.
3. *Fubini.* t^j a(t) e^{-ct} is in L^1, because |a(t) e^{-ct}| <= C e^{-eps|t|}. Hence
 m_j(phi (x) psi) = (1/2 pi) int B(c+iy) [int t^j a(t) e^{-(c+iy)t} dt] dy,
 and the inner integral is (-d/dz)^j T_z(phi) at z = c + iy, by differentiation under the integral sign inside the strip. ∎

## 4. Proposition D: m_0 = 0 already forces S = 0

**Proposition D.** Let S be tilted-decaying. If the zeroth moment m_0 of S (x) S vanishes, then S = 0.

*Proof.* By Lemma 0, T_z(Gamma_s psi) = e^{zs} T_z(psi). So Proposition C applied to psi' = Gamma_s psi gives
 0 = m_0(phi (x) Gamma_s psi) = (e^{cs}/2 pi) int_R e^{iys} T_{c+iy}(phi) T_{c+iy}(psi) dy  for every real s.
The function y -> T_{c+iy}(phi) T_{c+iy}(psi) is continuous and integrable (the first factor is bounded, the second integrable by step 1 above). By Fourier uniqueness it vanishes. Take psi = phi: then T_{c+iy}(phi)^2 = 0, so T_z(phi) = 0 on the line and hence on the whole strip. By Proposition B, S = 0. ∎

(Equivalently, m_0(phi (x) Gamma_s psi) = (a_phi * a_psi)(s) is the convolution of the two orbit functions. The vanishing of m_0 is the vanishing of all these convolutions, and in the tilted case that is equivalent to S = 0.)

**What this means for the planned line "run Theorem J's moment argument for S (x) S on M x M".**
- In Theorem J the induction m_0 = 0 => m_1 = 0 => ... and then Fourier uniqueness are the substantive steps. On M x M, for tilted-decaying S, Proposition D makes every step after the first redundant: m_0 = 0 is equivalent to S = 0, and so equivalent to T = 0.
- Any argument that kills m_0 using the chain m_0 o P_Y = 0, m_1 o P_Y = -m_0 is therefore a proof of (EF) for the family T. It cannot be easier than (EF).
- By Proposition C, the M x M chain (m_1, m_0) is the superposition along the line Re z = c of the factor objects (-T_z') (x) T_z and T_z (x) T_z. Here T_z' := dT_z/dz satisfies T_z'(P phi) = z T_z'(phi) + T_z(phi): it is an order-k Jordan chain (T_z', T_z) of P^T at every point z of the line where T_z != 0. So the M x M Jordan chain at 0 is literally the integral over the line of factor Jordan chains at the points z = c + iy, tensored with eigen-densities. This makes caveat (ii) of the task precise. Excluding it requires excluding those chains (or their superposition), which is (JC)/(EF) again.
- *Partial pairings.* K_0(psi) := m_0(. (x) psi) = (1/2 pi) int T_{c+iy}(psi) T_{c+iy} dy is a superposition of eigen-densities of P^T at points with real part c, and it satisfies K_0(psi) o P = K_0(P psi). GH of X, through (K0) and (K1), constrains only the spectral point 0 of P^T. To act on K_0(psi) it needs a statement about P^T near Re z = c, which is (JC) again. When c = 0 is allowed (strips containing 0), the whole question is already settled by Theorem J / Lemma M.

So the tensor route, applied to the distributions the [GOAL] needs, is equivalent to (EF) on the strip of Theorem R'. **(J2-prod) and (J2) remain unproved and unrefuted; by Proposition A, each is at least as strong as (EF).**

## 5. Side observations (checked as far as stated; I do not claim they are new)

(a) *Sanity check on the model.* For a Diophantine linear flow (d = 0), Gamma_t is a translation and so an isometry of C^k. Hence N_S(t) = ||S||_{(C^k)'} for all t, and (J2-prod) holds trivially. This is consistent, and gives no information.

(b) *The strip of Theorem R' is really (lambda, lambda + theta).* The pair x, y can be chosen once, generic in both time directions, independently of delta. Then for every delta > 0 the forward bound N_S(t) <= C(delta) e^{(lambda+delta)t} holds, while the backward bound does not depend on delta. So T_z is one family on lambda < Re z < lambda + theta, with bounds on closed substrips; delta is only a margin. In the volume-preserving case, lambda = 0 and the strip touches 0. This is the known boundary situation, where Lemma M does not apply.

(c) *Volume case: reduction to analytic vectors of R = X^{-1} (sketch; presumably the content of round7_q7, Theorem V).* Assume GH and a smooth invariant volume nu (d = 0, P = X). Then X : C^inf_0 -> C^inf_0 has a continuous inverse R ((O2), Text B). Let T_z be the family of (b) on 0 < Re z < theta.
- T_z(1) = 0, because z T_z(1) = T_z(X 1) = 0.
- For mean-zero phi, T_z(phi) = z^j T_z(R^j phi), hence |T_z(phi)| <= |z|^j ||T_z||_{(C^1)'} ||R^j phi||_{C^1}.
- If ||R^j phi||_{C^1} <= C_phi A_phi^j, then T_z(phi) = 0 on the nonempty open set {|z| < 1/A_phi} ∩ strip, hence on the whole strip.

So T = 0, and with it the [GOAL] in the volume case, follows if such "R-analytic" vectors (plus constants) are dense in C^1. For Diophantine flows they are: trigonometric polynomials. In general I see no way to produce them. Flow-mollifiers int k(s) psi o g_s ds with k-hat supported away from 0 are R-analytic but are not even C^1 when the flow has positive exponents, because k is Schwartz but not exponentially decaying (k-hat is compactly supported, so k cannot decay exponentially), while ||psi o g_s||_{C^1} grows exponentially in |s|. And the tame estimate ||R psi||_{C^k} <= C ||psi||_{C^{k+m}} loses m derivatives at each step, so it gives only Gevrey-type bounds, which are not enough.

## 6. Status summary

**Proved here:**
- Lemma 0.
- Proposition A: (J2-prod) => (EF_k), and hence (J2) => (J2-prod) => (EF).
- Proposition B: for tilted-decaying S, which include the S of Theorem R', (J2-prod) for S <=> vanishing of its strip family. So for the [GOAL] the tensor route is equivalent to (EF) on the strip of Theorem R'.
- Proposition C: the explicit Parseval form of all M x M moments.
- Proposition D: m_0 = 0 alone forces S = 0, for tilted-decaying S.

**Consequence.** The suggested line (kill m_0 on M x M using GH of X on each factor) cannot be easier than (EF). The M x M Jordan chain at 0 is the superposition along a vertical line of the factor Jordan chains (T_z', T_z) at Re z = c, tensored with eigen-densities.

**Sketched:** §5(b), §5(c).

**Open (not settled here):**
- (J2-prod), (J2), (EF), (JC), and so the problem's claim in dimension >= 4 with non-hyperbolic positive-entropy measures.
- Two concrete open sub-questions:
  - (Q1) In the volume-preserving GH case, are the R-analytic vectors dense in C^1? An affirmative answer settles that case by §5(c).
  - (Q2) Can GH of X be made to act at a spectral point c with Re c != 0 at all? For example, does GH of X imply that X - c is injective on D'(M) for small real c != 0?

No counterexample to any of these statements is known to me.

=== END OF ANSWER round10_q9 ===

