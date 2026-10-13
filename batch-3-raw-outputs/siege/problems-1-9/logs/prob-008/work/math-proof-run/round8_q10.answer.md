# round8_q10 — answer (work in progress)

## Plan
Target: statement (VC). Planned content:
1. Reformulation: (VC) is equivalent to "cohomology-free (CF) flows have zero topological entropy"; Katok's conjecture implies it.
2. New structural fact under (VC), in the spirit of Rodriguez Hertz–Rodriguez Hertz: M fibres smoothly over T^b, b = b_1(M), and the flow projects onto a linear flow.
3. New partial theorem: under (VC), positive entropy forces a zero Lyapunov exponent *inside the fibres*. The reason is that stable and unstable sets lie in fibres, so vertical hyperbolicity gives local product structure, hence su-quadrilaterals, which (VC) forbids. Corollary: (VC) holds when b_1(M) >= dim M - 2.
4. Status of mechanisms (a)–(d), and what remains open.

Standing conventions: omega is the smooth invariant positive density, normalised so that omega(M) = 1. Distributions u are identified with functionals phi -> <u, phi omega>. Since div_omega X = 0, we have <Xu, phi omega> = -<u, (X phi) omega>. "L1" denotes Text A, L1: every u in D' with Xu = 0 is constant.

## 1. Reformulation (proved)

Call X *cohomology-free* (CF) if every smooth f can be written f = c + Xu with c a constant and u smooth.

**Proposition 1.1.** For a smooth vector field X on a compact connected manifold M with dim M >= 1, the following are equivalent:
(i) X is GH and preserves a smooth positive density;
(ii) X is CF.
Hence (VC) is exactly the statement "the flow of a CF vector field has zero topological entropy". Katok's conjecture (from memory: every CF vector field is smoothly conjugate to a Diophantine linear flow on a torus) would imply (VC). I do not know whether (VC) is equivalent to Katok's conjecture. It looks strictly weaker, since it asks only for zero entropy.

*Proof.* (i) => (ii) is (O2) of the brief: constants plus X(C^inf) give C^inf.

(ii) => (i):
1. *No smooth u has Xu = 1*: at a maximum point q of u we have (Xu)(q) = 0. Hence the constant c in f = c + Xu is unique, and c(f) is a linear functional with kernel X(C^inf).
2. *c(f) = mu(f) for every invariant probability mu.* Indeed mu(Xu) = d/dt|_0 mu(u o g_t) = 0, and mu(1) = 1. So the flow is uniquely ergodic with measure mu, and X(C^inf) = ker mu is closed.
3. *mu is smooth.* Let nu be a smooth positive density and d = div_nu X. By CF, d = c + Xa with a smooth. By (O3) of the brief, e^{-a} nu is invariant, so (after normalising) mu = e^{-a} nu / (int e^{-a} d nu) =: omega.
4. *Invariant distribution densities.* Every invariant distribution density T annihilates X(C^inf) = ker omega. Hence T is a multiple of omega.
5. *GH.* Let u be in D' with Xu = f smooth. Pairing with omega gives omega(f) = <Xu, omega> = -<u, L_X omega> = 0. So f = Xv with v smooth. Then X(u - v) = 0, so the density (u - v) omega is invariant, hence equals c omega, and u = v + c is smooth. ∎

## 2. The torus fibration (proved; the idea is that of F. and J. Rodriguez Hertz, "Cohomology free systems and the first Betti number", quoted from memory — I reprove what I use)

Assume (VC). By (O2) the flow is minimal and uniquely ergodic, and every smooth f equals omega(f) + Xu with u smooth.

**Lemma 2.1 (invariant representatives).** Every class c in H^1(M; R) contains a smooth closed 1-form eta_c with L_X eta_c = 0 and with i_X eta_c equal to a constant rho(c). This eta_c is unique, and c -> rho(c) is linear.
*Proof.*
- Existence. Take any closed eta in c. Write i_X eta = rho + Xu with rho = omega(i_X eta) and u smooth. Put eta_c = eta - du. Then i_X eta_c = rho, and Cartan's formula gives L_X eta_c = d(i_X eta_c) + i_X d eta_c = 0.
- Uniqueness. Two such forms differ by dv with v smooth and Xv = i_X dv constant. The constant is 0 (look at a maximum of v). Then v is constant by L1, so dv = 0.
- Linearity follows from uniqueness. ∎

**Proposition 2.2 (fibration).** Let b = b_1(M) and suppose b >= 1. Choose classes c_1, ..., c_b in H^1(M; Z) whose images form a basis of H^1(M; R), put eta_i = eta_{c_i}, fix p in M, and define
 pi(x) = ( int_p^x eta_1, ..., int_p^x eta_b ) mod Z^b, a map M -> T^b = R^b / Z^b.
Then:
(a) pi is well defined and smooth, and pi(g_t x) = pi(x) + t alpha with alpha = (rho(c_1), ..., rho(c_b));
(b) pi is a surjective submersion, hence (Ehresmann) a locally trivial fibre bundle with compact fibres F_theta = pi^{-1}(theta) of dimension f := n - b;
(c) k . alpha != 0 for every k in Z^b \ {0}. In particular alpha != 0, and X is nowhere tangent to the fibres.
*Proof.*
(a) The periods of eta_i are integers, so pi is well defined. Also d pi = (eta_1, ..., eta_b), and d/dt pi(g_t x) = (eta_i(X))_i = alpha.
(b) L_X eta_i = 0 gives g_t^* eta_i = eta_i. So the rank r(x) of (eta_1(x), ..., eta_b(x)) is flow-invariant.
- Let r_0 = max r. The set {r = r_0} is open (lower semicontinuity of rank), nonempty and invariant. Its complement is closed and invariant; if it were nonempty it would contain an orbit closure, which is all of M by minimality. So r = r_0 everywhere.
- Then K(x) = {c in R^b : sum c_i eta_i(x) = 0} has constant dimension b - r_0 and depends continuously on x, as a map to a Grassmannian. It is flow-invariant, so it is constant on the dense orbits, hence constant: K(x) = K.
- For c in K, sum c_i eta_i = 0 identically, so sum c_i [eta_i] = 0 in H^1(M; R), and c = 0. Hence r_0 = b, and pi is a submersion.
- pi(M) is open (submersion) and compact, so pi(M) = T^b. Ehresmann's theorem (proper surjective submersion) gives the bundle structure.
(c) If k . alpha = 0, then e(x) = exp(2 pi i k . pi(x)) satisfies Xe = 0, so e is constant by L1. Then sum k_i eta_i = d(k . pi) = 0, contradicting the independence of the classes. Hence D pi(X) = alpha != 0. ∎

Note that b = 0 is allowed in (VC). Then Section 3 gives nothing, and the problem is untouched.

**Lemma 2.3 (asymptotic sets lie in fibres).** If d(g_{t_j} x, g_{t_j} y) -> 0 along some sequence |t_j| -> infinity, then pi(x) = pi(y).
*Proof.* Use a flat translation-invariant metric on T^b, and let L be the Lipschitz constant of pi. Then dist(pi x, pi y) = dist(pi(g_t x), pi(g_t y)) <= L d(g_t x, g_t y), because g_t acts on T^b as a translation. Let t = t_j -> infinity. ∎

**Lemma 2.4 (Lyapunov structure).** Put V = ker D pi (the vertical bundle, of rank f). Then:
(i) V is Dg_t-invariant, and on the quotient TM/V, identified with the trivial bundle T^b x R^b via D pi, Dg_t acts as the identity.
(ii) The product of the exponents of Dg_t|_V is trivial: the sum of the vertical Lyapunov exponents (with multiplicity) is 0 at omega-a.e. point.
(iii) Every vector with a negative forward exponent, and every vector with a positive exponent, lies in V. That is, E^s(x) + E^u(x) ⊂ V(x) for Oseledets-regular x.
*Proof.*
(i) This is D pi ∘ Dg_t = D pi, which follows from pi ∘ g_t = pi + t alpha.
(ii) Write omega = omega_V ⊗ pi^*(d theta), meaning that omega_V(x) is the density on V(x) for which omega(v_1, ..., v_f, w_1, ..., w_b) = omega_V(v_1, ..., v_f) dtheta(D pi w_1, ..., D pi w_b). This omega_V is a continuous positive fibre density. Since g_t preserves omega and acts trivially on the quotient, the Jacobian of Dg_t|_V with respect to omega_V is identically 1. Hence (1/t) log |det Dg_t|_V| -> 0, and by Oseledets this limit is the sum of the vertical exponents.
(iii) Suppose v is in E^s(x), so |Dg_t v| -> 0 as t -> +infinity. Then D pi(v) = D pi(Dg_t v) -> 0, so D pi(v) = 0. The case E^u uses t -> -infinity. ∎

## 3. Vertical hyperbolicity is incompatible with positive entropy (proved, modulo cited standard Pesin theory)

### 3.1 Theorem J in the volume case (self-contained re-proof)
**Lemma 3.1.** Assume (VC). Let S = sum_j w_j delta_{z_j} be a finite complex combination of point masses with sum_j w_j = 0. Put F_phi(t) = S(phi o g_t). Suppose there are C and eps > 0 with
 |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^1}   for all real t and all smooth phi.
Then S = 0.

*Proof.*
1. F_phi(t) = sum w_j phi(g_t z_j) is C^inf in t, and F_phi' = F_{X phi}.
2. Put m_j(phi) = int_R t^j F_phi(t) dt. Then |m_j(phi)| <= C ||phi||_{C^1} int |t|^j e^{-eps|t|} dt, so each m_j is a distribution density of order <= 1.
3. F_phi and F_{X phi} decay exponentially. Integrating by parts over R therefore gives m_0(X phi) = 0, and m_j(X phi) = -j m_{j-1}(phi) for j >= 1.
4. Since F_1 = S(1) = 0, we have m_j(1) = 0 for all j.
5. Induction: if m_{j-1} = 0 (or j = 0), then m_j(X phi) = 0 for all phi. Let u be the distribution with <u, phi omega> = m_j(phi). Then <Xu, phi omega> = -m_j(X phi) = 0, so u is a constant c by L1, i.e. m_j = c omega. Then c = m_j(1) = 0. Hence m_j = 0 for every j.
6. G(zeta) = int e^{-i zeta t} F_phi(t) dt is holomorphic on |Im zeta| < eps, and G^{(j)}(0) = (-i)^j m_j(phi) = 0 for all j. So G = 0, and by Fourier uniqueness (F_phi is continuous and in L^1) F_phi = 0. In particular S(phi) = F_phi(0) = 0 for all phi. ∎

(This is Theorem J of R6-a with nu = omega, d = 0. The only input from GH is L1.)

### 3.2 su-quadrilaterals are forbidden
**Lemma 3.2.** Assume (VC). There are no points x, y, z, w in M with x != y and x != z, together with constants C, theta > 0, such that
 d(g_t x, g_t y) <= C e^{-theta|t|} and d(g_t w, g_t z) <= C e^{-theta|t|} for t <= 0;
 d(g_t x, g_t z) <= C e^{-theta t} and d(g_t w, g_t y) <= C e^{-theta t} for t >= 0.
*Proof.*
1. Let S = delta_x - delta_y + delta_w - delta_z. Then S(1) = 0.
2. S != 0. If S = 0, the multisets {x, w} and {y, z} would coincide, which forces x in {y, z}. This is excluded.
3. For t <= 0, group the terms as F_phi(t) = [phi(g_t x) - phi(g_t y)] + [phi(g_t w) - phi(g_t z)]. For t >= 0, group them as [phi(g_t x) - phi(g_t z)] + [phi(g_t w) - phi(g_t y)].
4. Since |phi(a) - phi(b)| <= ||d phi||_inf d(a, b), we get |F_phi(t)| <= 2C e^{-theta|t|} ||phi||_{C^1} for all t.
5. Lemma 3.1 gives S = 0, contradicting step 2. ∎

(This is Corollary G2 of R7-a, which is proved there by the same argument. I include it so that the proof here is complete. No point needs to be generic; coincidences such as w = y are allowed.)

### 3.3 Cited Pesin theory (standard, quoted from memory)
Let T be a C^inf diffeomorphism of the compact manifold M preserving the ergodic Borel probability omega.
- [Os] Oseledets: there are constant exponents and a measurable splitting T_x M = E^s(x) ⊕ E^0(x) ⊕ E^u(x) into the sums of the Oseledets spaces with negative, zero and positive exponents.
- [Pe] Pesin's stable manifold theorem with Pesin sets. Fix theta > 0 smaller than every |nonzero exponent|. There are compact sets Lambda_1 ⊂ Lambda_2 ⊂ ... with omega(Lambda_l) -> 1 and constants r_l, C_l with the following property. For x in Lambda_l, the local stable manifold W^s_loc(x) is an embedded C^1 disc of radius r_l, tangent at x to E^s(x), with d(T^m y, T^m x) <= C_l e^{-theta m} for y in W^s_loc(x) and m >= 0. W^u_loc(x) has the same properties with T^{-1} and E^u. Moreover x -> W^{s}_loc(x) and x -> W^u_loc(x) are continuous on Lambda_l in the C^1 topology of embedded discs, and x -> E^s(x), E^u(x) are continuous on Lambda_l.
- [LY] Ledrappier–Strelcyn / Ledrappier–Young: there is a measurable partition xi^u subordinate to W^u. This means that xi^u(x) ⊂ W^u(x) and that xi^u(x) contains a neighbourhood of x in W^u(x), for the leaf topology. It satisfies h_omega(T) = H(xi^u | T xi^u). If h_omega(T) > 0, the conditional measures omega^u_x are non-atomic for a.e. x (Lemma 6.0 of R6-a, proved there from this formula). Applying the same to T^{-1} gives xi^s with non-atomic conditionals omega^s_x.

**Lemma 3.3 (density in the conditionals).** Let Lambda be a Borel set with omega(Lambda) > 0. For omega-a.e. x in Lambda, every leaf-neighbourhood of x in xi^u(x) has positive omega^u_x(Lambda ∩ ·)-measure.
*Proof.*
1. Let E be the set of x in Lambda for which this fails. Fix a plaque P = xi^u(x).
2. The set E ∩ P is contained in Lambda ∩ P minus the (leaf-topology) support of omega^u_x restricted to Lambda. That difference is omega^u_x-null, because the plaque is second countable.
3. So omega^u_x(E) = 0 for a.e. plaque, and omega(E) = int omega^u_x(E) d omega(x) = 0. ∎
(Measurability of E is standard and I do not check it.)

If moreover the conditionals are non-atomic, then for a.e. x in Lambda and every leaf-neighbourhood N of x there is y in Lambda ∩ N with y != x. Indeed omega^u_x(Lambda ∩ N) > 0 while omega^u_x({x}) = 0. The same holds for xi^s.

### 3.4 Main theorem of this answer
**Theorem 3.4.** Assume (VC) with b = b_1(M) >= 1, and let pi, V be as in Section 2. If h_top(g_1) > 0, then the vertical cocycle Dg_t|_V has a zero Lyapunov exponent with respect to omega (at omega-a.e. point).

*Proof.*
1. *Reduction to an ergodic time map.* For c > 0, the field cX again satisfies (VC) with the same omega and the same pi (now with frequency c alpha). Its time-1 map is g_c, and h_top(g_c) = c h_top(g_1). The L^2(omega) eigenvalues of the flow form a countable set, and g_c is ergodic unless c xi is in 2 pi Z \ {0} for some eigenvalue xi. So we may assume that T := g_1 is ergodic for omega. By unique ergodicity and the variational principle, h_omega(T) = h_top(T) > 0. Lyapunov exponents and the conclusion are unaffected by the rescaling.
2. *Hyperbolic splitting of V.* Suppose, for contradiction, that every exponent of Dg_t|_V is nonzero. Apply Oseledets to the restricted cocycle: V(x) = V^-(x) ⊕ V^+(x), where vectors of V^- have negative forward exponents and vectors of V^+ have negative backward exponents. Hence V^- ⊂ E^s and V^+ ⊂ E^u. With Lemma 2.4(iii) this gives E^s(x) ⊕ E^u(x) = V(x) = T_x F_{pi(x)}.
3. *Local manifolds lie in fibres.* By Lemma 2.3, W^s_loc(x) and W^u_loc(x) lie in F_{pi(x)}. Likewise W^u(x) lies in F_{pi(x)} for every point at which it is defined.
4. *Choice of x, y, z.* Fix l with omega(Lambda_l) > 0. By [LY] and Lemma 3.3 (for xi^u and xi^s), for a.e. x in Lambda_l and every delta > 0 there are
 - y in Lambda_l ∩ W^u_loc(x) with 0 < d(x, y) < delta, and
 - z in Lambda_l ∩ W^s_loc(x) with 0 < d(x, z) < delta.
 (The leaf-neighbourhoods of x of small leaf radius lie in the local discs and in B(x, delta).)
5. *Local product structure inside the fibre.* All of W^s_loc(x), W^u_loc(x), W^s_loc(y) and W^u_loc(z) lie in the single fibre F := F_{pi(x)}. Here pi(y) = pi(z) = pi(x) by step 3.
 - Inside the f-dimensional manifold F, W^s_loc(x) and W^u_loc(x) are C^1 discs of complementary dimensions dim E^s + dim E^u = f. They meet transversally at x, by step 2.
 - Take a local trivialisation chart of the bundle near x, with coordinates (theta, v) in R^b x R^f, F = {theta = pi(x)}. In it, W^s_loc(y) and W^u_loc(z) are C^1-close to W^s_loc(x) and W^u_loc(x) once delta is small, by the continuity in [Pe] on Lambda_l.
 - A transverse intersection of two discs of complementary dimension in R^f persists under C^1-small perturbations. Write both discs as graphs over E^s(x) and E^u(x) and apply the contraction mapping principle.
 - Hence for delta small enough (depending on l) there is a point w in W^s_loc(y) ∩ W^u_loc(z).
6. *Exponential asymptotics for real times.* With L = max_{s in [0,1]} Lip(g_s) and t = m + s:
 - d(g_t z, g_t x) <= L C_l e^{theta} e^{-theta t} and d(g_t w, g_t y) <= L C_l e^{theta} e^{-theta t} for t >= 0, since z is in W^s_loc(x), w is in W^s_loc(y), and x, y are in Lambda_l;
 - d(g_t y, g_t x) <= L C_l e^{theta} e^{-theta|t|} and d(g_t w, g_t z) <= L C_l e^{theta} e^{-theta|t|} for t <= 0, since y is in W^u_loc(x), w is in W^u_loc(z), and x, z are in Lambda_l.
7. The points x, y, z, w satisfy the hypotheses of Lemma 3.2 (x != y and x != z), which is a contradiction. ∎

**Corollary 3.5.** (VC) holds whenever b_1(M) >= dim M - 2. In particular, if dim M = 4 then (VC) holds unless b_1(M) <= 1, and if dim M = 5 it holds unless b_1(M) <= 2.
*Proof.* Let n = dim M and f = n - b <= 2. The case b = 0 forces n <= 2, and then the brief (Theorem 5.2 of R6-a) already gives h_top = 0, since dim M <= 3. So let b >= 1 and suppose h_top(g_1) > 0. After the rescaling of step 1 above, omega is ergodic for T = g_1 and h_omega(T) > 0.
- By Theorem 3.4 the vertical cocycle has a zero exponent. By Lemma 2.4(ii) the vertical exponents sum to 0. If f <= 2, this forces all vertical exponents to be 0.
- By Lemma 2.4(i) the quotient cocycle on TM/V is trivial, so its exponents are all 0.
- [cited, standard] For a cocycle with an invariant subbundle, the Lyapunov spectrum is the union, with multiplicities, of the spectra on the subbundle and on the quotient. Hence all exponents of omega vanish.
- Ruelle's inequality gives h_omega(T) <= 0. This is a contradiction. ∎

(For f = 1 and f = 0, Theorem 3.4 is not even needed: the single vertical exponent is 0 by Lemma 2.4(ii).)

**Remark 3.6 (how this fits the earlier obstruction).** Round 7 (R7-a, R7-f) isolated the obstruction for non-hyperbolic positive-entropy measures: su-cycles must close in the centre directions, which costs (c - 1) extra conditions, and Pesin leaves vary only measurably. Theorem 3.4 removes exactly the part of the centre that comes from H^1(M). Lemma 2.3 confines every stable or unstable set to one fibre of pi, so the b base directions are never a closing defect. What remains is the centre *inside* the fibres: zero exponents of Dg_t|_V. The remaining case of (VC) is therefore:
**(VC-rest)** omega has positive entropy, and either b_1(M) = 0, or the vertical cocycle Dg_t|_{ker D pi} has a zero exponent. Then f = n - b >= 3, so n >= 4 when b >= 1. When b = 0 the centre contains only the flow direction and at least one more zero exponent, as before.

## 4. Mechanisms (a)–(d) of the brief: what I found

**(d) Known conjecture.** By Proposition 1.1, (VC) is literally "CF flows have zero topological entropy". It is implied by Katok's conjecture on CF vector fields (quoted from memory). From memory, the following are known: Katok's conjecture in dimension 3 (Forni; Kocsard), and the factor onto a linear flow on T^{b_1} (Rodriguez Hertz–Rodriguez Hertz, of which Section 2 is a version). I do not recall any theorem giving zero entropy for CF flows in dimension >= 4, so I believe (VC) is open in the literature. I cannot confirm this from memory.

**(b) Singular spectrum: moving the control to other frequencies (partial, proved observation; does not conclude).** Assume b >= 2.
- By Proposition 2.2, e_k := exp(2 pi i k . pi) (k in Z^b) is a smooth unimodular eigenfunction: X e_k = i xi_k e_k with xi_k = 2 pi k . alpha.
- By 2.2(c) the xi_k are pairwise distinct, and Gamma = {xi_k} is dense in R (alpha has rationally independent coordinates and b >= 2).
- For smooth f, put f_k = f - <f, e_k> e_k. Then ē_k f_k has mean 0, so ē_k f_k = X v with v smooth. Hence f_k = (X - i xi_k)(e_k v), and iterating,
 (X - i xi_k)^{-N} f_k = e_k R^N(ē_k f_k), with ||(X - i xi_k)^{-N} f_k||_{L^2} <= C_N (1+|k|)^{m_N} ||f||_{C^{m_N}},
 where m_N is the derivative loss of R^N (tame estimate) and the factor |k|^{m_N} comes from multiplication by ē_k.
- Consequently the continuous part sigma^c_f of the spectral measure satisfies
 int |lambda - xi_k|^{-2N} d sigma^c_f(lambda) <= C_N^2 (1+|k|)^{2 m_N} ||f||^2_{C^{m_N}}
 for all k and N. So sigma^c_f is flat to infinite order at every point of the dense set Gamma.
- *Why this does not conclude.* To force sigma^c_f = 0 by covering a frequency window with neighbourhoods of the xi_k (|k| <= K, whose gaps are about K^{1-b}), one needs m_N <= rN + O(1) with r < b - 1. For a Diophantine linear flow on T^b the loss per inverse is tau >= b - 1, so the condition fails even in the model. Summing over k with polynomial weights instead gives an a.e.-finite function, so no contradiction either. I record this only as a limit of the method.

**(a) Algebra / variance.** I found no rigorous mechanism.
- What one needs, in L^2 terms, is a single smooth mean-zero f that is not an L^2-coboundary, i.e. int lambda^{-2} d sigma_f = infinity.
- The natural candidates are products a · (a o g_s) - mean. Their spectral behaviour at 0 is governed by fourth-order cumulants, and nothing in positive entropy controls these without mixing rates.
- Gordin-type martingale decompositions along the Pesin unstable partition control the "fine" side (Lipschitz f) but not the "coarse" side, where decay of E(f | T^n xi^u) towards E(f | Pinsker) is needed. So I could not settle (Q3).
- Theorem 3.4 is the substitute I found: it uses the algebra structure only through the existence of the eigenfunctions e_k, i.e. through cohomology classes. In other words it uses CF on the functions i_X eta, plus Theorem J on su-quadrilaterals.

**(c) Quasi-analytic vectors.** Nothing new. In the fibred case the finite linear combinations of the e_k (k != 0) are quasi-analytic vectors of R, since R e_k = e_k/(i xi_k). But they are functions of pi alone, so their span is not C^1-dense unless the fibre dimension n - b is 0. Theorem V therefore does not apply.

## 5. Summary: proved / sketched / open

**Proved** (modulo the standard cited facts: Ehresmann's theorem, Oseledets, Pesin's stable manifold theorem with Pesin sets and continuity on Pesin sets, the Ledrappier–Young subordinate partition with h = H(xi | T xi), Ruelle's inequality, and the union rule for exponents of cocycles with an invariant subbundle):
1. Proposition 1.1: (VC) is equivalent to "every CF flow has zero topological entropy"; Katok's conjecture implies (VC).
2. Proposition 2.2: under (VC) with b = b_1(M) >= 1, M is a smooth fibre bundle over T^b, and the flow projects to the linear flow with frequency alpha, where k . alpha != 0 for all k != 0. Lemma 2.3: stable and unstable sets lie in fibres. Lemma 2.4: the quotient cocycle is trivial and the vertical exponents sum to 0.
3. Lemmas 3.1–3.2: under (VC) no su-quadrilateral exists. This is a self-contained re-proof of Theorem J and Corollary G2 from earlier rounds.
4. **Theorem 3.4: under (VC) with b_1(M) >= 1, positive entropy forces a zero Lyapunov exponent of omega inside ker D pi.**
5. **Corollary 3.5: (VC) holds whenever b_1(M) >= dim M - 2.** For example, this covers dimension 4 with b_1 >= 2 and dimension 5 with b_1 >= 3.

**Sketched / partly checked:** in step 5 of Theorem 3.4, the persistence of transverse intersection uses the continuity of the local Pesin discs on Pesin sets. This is standard, and it is the same argument that gives local product structure for hyperbolic measures, but I give it only in outline. The measurability in Lemma 3.3 is not checked.

**Open (not settled here):**
- (VC) in general. In particular **(VC-rest)**: exclude, under (VC), an ergodic smooth volume of positive entropy with either b_1(M) = 0 or a zero exponent of the vertical cocycle Dg_t|_{ker D pi}. The first open configurations are dim M = 4 with b_1(M) <= 1, and dim M = 5 with b_1(M) <= 2.
- (Q2)/(Q3) of the brief (singular spectrum; the abstract algebra/variance statement) remain open. Section 4(b) shows that flatness on the dense frequency set 2 pi alpha . Z^b is available when b >= 2, but not with constants good enough to conclude.

=== END OF ANSWER round8_q10 ===

