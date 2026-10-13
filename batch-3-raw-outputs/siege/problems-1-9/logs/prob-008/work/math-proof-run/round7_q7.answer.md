# round7_q7: answer (final; partial result. PE-NH not proved; Theorem J+, Lemma H, Theorem V and Proposition O proved)

## Plan
Target: (PE-NH). Approach as directed:
(1) prove a "Theorem J+" (weakest decay under which the moment / Jordan-chain argument still forces S = 0);
(2) examine continuation of the pair transform across Re z = 0 (Pesin-block transfer operators), and record exactly where it fails.
Expected outcome: PE-NH itself stays open. The rigorous new results are Theorem J+ (quasi-analytic decay), Lemma H (a horodisc / Carleman uniqueness lemma for eigen-families defined only on a strip), Theorem V (the volume case reduced to a density statement about quasi-analytic vectors of X^{-1}), and Proposition O (a proved obstruction to the Hennion route when there is a zero exponent).

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t the log-Jacobian, P phi = X phi + d phi, and F_phi(t) = S(e^{J_t} phi o g_t) for a distribution density S. Facts (F1) and (F2) of R6-a §1 are used. Cited theorems are quoted from memory and marked [cited].

## 1. Theorem J+ (proved): quasi-analytic two-sided decay suffices

**Theorem J+.** Assume GH. Let S be a distribution density. Suppose:
(i) (rapid decay, continuous in phi) for every j >= 0 there are C_j, k_j with int_R |t|^j |F_phi(t)| dt <= C_j ||phi||_{C^{k_j}} for all smooth phi;
(ii) (quasi-analyticity) for every smooth phi the numbers N_j(phi) := int_R |t|^j |F_phi(t)| dt satisfy sum_{j>=1} N_j(phi)^{-1/j} = infinity (read 0^{-1/j} as +infinity).
Then S = 0.

In particular S = 0 whenever |F_phi(t)| <= C ||phi||_{C^k} e^{-|t|/log(e+|t|)} for all t and phi (Example 1.2 below). Theorem J (decay e^{-eps|t|}) is a special case.

*Proof.*
1. As in Theorem J step 1, F_phi is C^1 with F_phi' = F_{P phi}.
2. Put m_j(phi) := int t^j F_phi(t) dt. By (i), m_j is well defined and |m_j(phi)| <= C_j ||phi||_{C^{k_j}}, so m_j is a distribution density.
3. *Jordan relations without pointwise decay.* Fix j and phi. By (i), both t^j F_phi and t^j F_phi' = t^j F_{P phi} are in L^1, and so is |t|^{j+1} |F_phi|. Hence liminf_{R -> inf} R^{j+1}(|F_phi(R)| + |F_phi(-R)|) = 0: otherwise this quantity is >= c > 0 for all large R, and int^inf R^j(|F_phi(R)| + |F_phi(-R)|) dR >= int^inf c R^{-1} dR = infinity. Choose R_n -> infinity with R_n^j(|F_phi(R_n)| + |F_phi(-R_n)|) -> 0. Integrating by parts on [-R_n, R_n] and letting n -> infinity (dominated convergence for the integrals):
 m_0(P phi) = 0, and m_j(P phi) = -j m_{j-1}(phi) for j >= 1.
4. Exactly as in Theorem J step 4, (F1) and (F2) give m_j = 0 for every j.
5. *Denjoy-Carleman.* Fix phi and write N_j = N_j(phi). If N_0 = 0 then F_phi = 0 a.e., hence everywhere by continuity. Otherwise put G(xi) := int e^{-i xi t} F_phi(t) dt. By (i), G is C^infinity on R, G^{(j)}(xi) = int (-it)^j e^{-i xi t} F_phi(t) dt, so sup |G^{(j)}| <= N_j, and G^{(j)}(0) = (-i)^j m_j(phi) = 0 for all j. The sequence (N_j) is log-convex, since by Cauchy-Schwarz N_j^2 = (int |t|^{(j-1)/2}|F|^{1/2} |t|^{(j+1)/2}|F|^{1/2})^2 <= N_{j-1} N_{j+1}. Put M_j := N_j/N_0, so M_0 = 1, M_j is log-convex, and M_j^{1/j} is nondecreasing. Then sum M_j^{-1/j} = sum N_0^{1/j} N_j^{-1/j}. Since N_0^{1/j} -> 1, this diverges by (ii).
 [cited: Denjoy-Carleman theorem, e.g. Rudin, Real and Complex Analysis, Thm 19.11] If M_0 = 1, (M_j) is log-convex and sum_j M_j^{-1/j} = infinity, then the class C{M_j} = {f in C^inf(R) : ||f^{(j)}||_inf <= beta_f B_f^j M_j for all j} is quasi-analytic: f in the class with f^{(j)}(0) = 0 for all j implies f = 0.
 Here ||G^{(j)}||_inf <= N_0 M_j, so G is in C{M_j} with all derivatives zero at 0. Hence G = 0. By Fourier uniqueness on L^1 and continuity, F_phi = 0, so S(phi) = F_phi(0) = 0. ∎

**Example 1.2 (decay e^{-|t|/log(e+|t|)} is enough).** Let |F_phi(t)| <= C ||phi||_{C^k} e^{-w(|t|)} with w(t) = t/log(e+t). Then (i) holds (with k_j = k). For (ii) put E_m := sup_{t >= 0} t^m e^{-w(t)}. Then N_j <= C||phi||(int_0^1 dt + int_1^inf t^{-2} t^{j+2} e^{-w(t)} dt) <= C||phi||(1 + E_{j+2}). To bound E_m (m >= 3):
- for 0 < t <= m^2: log(e+t) <= L_m := log(e+m^2), so m log t - w(t) <= m log t - t/L_m <= m log(m L_m) - m (the maximum over t > 0 is at t = m L_m);
- for t > m^2: m <= sqrt t, and sqrt t >= (log(e+t))^2 once t >= t_0 (an absolute constant), so m log t <= sqrt t log(e+t) <= t/log(e+t) = w(t), i.e. t^m e^{-w(t)} <= 1, provided m^2 >= t_0.
Hence E_m <= max(1, (m L_m/e)^m) for large m, and L_m <= 3 log m for m >= 3. So N_j^{1/j} <= C' j log j for large j, and sum_j 1/(j log j) = infinity. ∎

**Remark 1.3 (the moment method cannot go further).** Steps 1-4 use only (i). Step 5 is the only place where (ii) enters, and (ii) cannot be weakened to a non-quasi-analytic condition within this method. [cited: Paley-Wiener / Beurling] If W is even, nondecreasing on [0, inf) and int_0^inf W(t)/(1+t^2) dt < infinity, then there is a nonzero continuous F in L^1(R) with |F(t)| <= e^{-W(t)} and Fourier transform supported in [1, 2]. Such an F has all moments zero. So vanishing moments plus decay e^{-|t|^a} (a < 1) do not force F = 0, and a proof under weaker decay would need more input from the dynamics than the Jordan chain.

**Remark 1.4 (what J+ does not give).** Theorem J+ still needs decay in BOTH time directions, faster than every power of |t|. At mu(d) = 0 the forward factor e^{J_t(x)} at a mu-generic point is e^{o(t)} and typically fluctuates like e^{±c sqrt t}. So point masses on a single unstable leaf give no forward decay at all, and Theorem J+ does not apply to them. Theorem J+ helps only if a forward cancellation of super-polynomial (quasi-analytic) quality is produced. Mechanism (iii) of the sketch therefore still needs mechanism (i) (forward cancellation); see §4.

## 2. Lemma H (proved): uniqueness for eigen-families known only on a strip, under Carleman-flatness at 0

Lemma M needs a continuation of T_z to a punctured neighbourhood of 0. The following purely complex-analytic lemma replaces the continuation by quantitative flatness on the half-disc.

**Lemma H.** Let r > 0, U := {z : Re z > 0, |z| < r}, and let f be holomorphic on U. Suppose there are C and numbers K_N in [0, inf) (N = 0, 1, 2, ...) with
 |f(z)| <= C K_N |z|^N / Re z for all z in U and all N,
and put Lambda(y) := inf_N K_N y^{-N} for y >= 1. If int_1^inf log Lambda(y) dy/y^2 = -infinity, then f = 0 on U.

*Proof.* Fix a with 1/(2a) < r and let H := {z : Re(1/z) > 2a}. This is the open disc with centre 1/(4a) and radius 1/(4a). Every z in closure(H) \ {0} has Re z > 0 and |z| <= 1/(2a) < r, so closure(H) \ {0} ⊂ U. Put g(w) := f(1/w), which is holomorphic on a neighbourhood of the closed half-plane {Re w >= 2a}. Since Re z = Re w/|w|^2 and |z| = 1/|w|,
 |g(w)| <= C K_N |w|^{2-N} / Re w.
- With N = 2: |g| <= C K_2/(2a) on {Re w >= 2a}, so g is bounded there.
- On the line w = 2a + iy with |y| >= 1: |w| >= |y|, so |w|^{-N} <= |y|^{-N}, and |g(2a+iy)| <= (C/2a) |w|^2 Lambda(|y|).
Hence log|g(2a+iy)| <= c + 2 log(|y| + 2a) + log Lambda(|y|), and int log|g(2a+iy)| dy/(1+y^2) = -infinity (the positive part is bounded, because g is bounded).
[cited: Hardy-space fact, e.g. Garnett, Bounded Analytic Functions, Ch. II] If g is bounded and holomorphic on an open half-plane, continuous on its closure, and not identically 0, then the integral of log|g| over the boundary line against dy/(1+y^2) is > -infinity.
So g = 0. Hence f = 0 on H, and so on U by the identity theorem. ∎

Remark. [cited: Mandelbrojt / Ostrowski] For log-convex K_N the condition int log Lambda(y) dy/y^2 = -inf is equivalent to sum K_N^{-1/N} = inf, i.e. to the Carleman condition. If K_N <= A B^N, then Lambda(y) = 0 for y > B and the condition holds trivially.
Lemma H is sharp for the same reason as Remark 1.3. f(z) = e^{-1/sqrt z} (principal branch) is holomorphic and nonzero on U and satisfies |f(z)| <= e^{-|z|^{-1/2}/sqrt 2} <= C_N |z|^N on U. Here C_N ~ (2N)! 2^N is a Gevrey-2, non-quasi-analytic sequence. So flatness at the boundary point 0 alone never suffices; a quasi-analytic rate is needed.

## 3. Theorem V (proved): the volume-preserving case reduced to quasi-analytic vectors of X^{-1}

Setting: GH, and X preserves a smooth positive density omega. Take nu = omega, so d = 0, J_t = 0 and P = X. Write omega-hat = omega/omega(M). By (O2), the invariant distribution densities are the multiples of omega. By the duality consequence of Text A, X(C^inf) = {f : omega-hat(f) = 0} =: C^inf_0. By Corollary 3 of Text B, X: C^inf_0 -> C^inf_0 is a topological isomorphism. Let R := (X|_{C^inf_0})^{-1}. For smooth phi put phi_0 := phi - omega-hat(phi),
 K_N(phi) := ||R^N phi_0||_{C^1},  Lambda_phi(y) := inf_N K_N(phi) y^{-N},
and let Q be the set of smooth (complex-valued) phi with int_1^inf log Lambda_phi(y) dy/y^2 = -infinity ("quasi-analytic vectors of R").

**Theorem V.** In this setting, suppose lambda* > 0 (lambda* := lim (1/n) max_x log||Dg_n(x)||; by Ruelle's inequality and the variational principle, h_top(g_1) > 0 implies lambda* > 0). Then Q is not dense in C^inf(M) for the C^1 norm.
Equivalently: if Q is C^1-dense, then lambda* = 0 and h_top(g_1) = 0.

*Proof.*
1. By R5-a Lemma 2 (which uses only lambda* > 0 and the cited Pesin-Ruelle theorem), there are x != y and C0, theta > 0 with d(g_{-t}x, g_{-t}y) <= C0 e^{-theta t} for t >= 0. Let S := delta_x - delta_y and F_phi(t) := phi(g_t x) - phi(g_t y). Then
 |F_phi(t)| <= C0 e^{-theta|t|} ||phi||_{C^1} for t <= 0,  |F_phi(t)| <= 2||phi||_inf for t >= 0.
(In the volume case no hypothesis on J is needed, because J = 0.)
2. For z in the strip Sigma := {0 < Re z < theta} put T_z(phi) := int_R e^{-zt} F_phi(t) dt. This is holomorphic in z, and |T_z(psi)| <= (2/Re z + C0/(theta - Re z)) ||psi||_{C^1}. Since F_{X psi} = F_psi', and the boundary terms vanish at both ends (Re z > 0 handles +inf; the backward bound with Re z < theta handles -inf), integration by parts gives T_z(X psi) = z T_z(psi). Also F_1 = 0, so T_z(1) = 0.
3. Hence, for any smooth phi and any N: T_z(phi) = T_z(phi_0) = T_z(X^N R^N phi_0) = z^N T_z(R^N phi_0). On U := {Re z > 0, |z| < theta/2} this gives
 |T_z(phi)| <= (2 + C0) K_N(phi) |z|^N / Re z.
4. If phi is in Q, Lemma H gives T_z(phi) = 0 on U, hence on Sigma by the identity theorem.
5. Each T_z (z in Sigma) is continuous for the C^1 norm. So if Q were C^1-dense, T_z = 0 for every z in Sigma. But take phi_* smooth with phi_*(x) = 1 and phi_*(y) = 0. Then G(t) := e^{-theta t/2} F_{phi_*}(t) is continuous and in L^1 with G(0) = 1, and its Fourier transform is omega' -> T_{theta/2 + i omega'}(phi_*). So that transform is not identically 0 (R5-a step (f)), a contradiction. ∎

**Corollary V.1 (sanity check).** In the setting of Theorem V with lambda* > 0, the constants together with the smooth eigenfunctions of X (X phi = i eta phi, eta real and nonzero) do not span a C^1-dense subspace.
(Proof: a finite combination phi of eigenfunctions with |eta_i| >= delta has mean zero, R phi_i = phi_i/(i eta_i), and K_N(phi) <= A delta^{-N}. So Lambda_phi = 0 for large y, and phi is in Q.) This is consistent with the classical fact that discrete spectrum forces zero entropy; it is not new.

**Where Theorem V stops (precise).** The models show what is missing.
- Diophantine linear flows on T^n: the trigonometric polynomials lie in Q (geometric K_N), so Q is dense.
- For real-analytic phi on T^n with |phi-hat_k| <= e^{-a|k|} and |k.alpha| >= c|k|^{-tau}: ||R^N phi||_{C^1} grows like (N!)^tau, with tau >= n-1. This is non-quasi-analytic for n >= 3, so analyticity of phi is not the right notion.
Thus a GH volume-preserving flow with lambda* > 0 would have to be one in which no C^1-dense set of smooth functions has iterated inverses R^N of quasi-analytic growth. GH, through the closed graph theorem, gives the existence of the tame bounds ||R psi||_{C^k} <= C_k ||psi||_{C^{m_k}} and nothing about the growth of C_k, m_k, or of ||R^N phi||. I could not produce quasi-analytic vectors from GH alone. L^2 spectral theory (X is skew-adjoint on L^2(omega)) gives L^2-analytic vectors (spectral subspaces E(|eta| > delta)), but T_z is not L^2-continuous: it has order 1, because of the point masses.
Remark on removing the point masses. One can make S absolutely continuous, S = sigma omega with sigma in L^1, by smearing the pair along unstable leaves over a Pesin block, using the absolute continuity of the unstable foliation for omega. If sigma is in L^2, then for Re z > 0 the forward part equals <(z - X)^{-1} phi, sigma>, and the backward part is the continuation of -<(z - X)^{-1} phi, sigma> from Re z < 0. Then T_z is the jump of the L^2 resolvent across iR, i.e. 2 pi times the density of the cross spectral measure of (phi, sigma), continued into the strip. GH (step 3) makes this density flat at 0 to all orders. Positive entropy (countable Lebesgue spectrum off the Pinsker factor) does not contradict flatness for individual phi, and I could not get a contradiction for a dense set of phi. So the gap is the same: smooth phi whose spectral data near 0 is controlled quantitatively.
**Non-volume case.** Step 3 needs a tame inverse of P = X + d on its range. Without a smooth invariant volume, P is injective on C^inf, and its range is dense in ker(nu-hat), since the annihilator of the range of P is span(nu) by (F1). I could not show that this range is closed. By the closed range theorem for Fréchet spaces [cited], this is equivalent to weak*-closedness of the range of the transpose of P, i.e. of L_X on distribution densities. Even granting it, the iteration breaks: P^{-1} maps ker(nu-hat) into C^inf but not into ker(nu-hat).

## 4. Approach (2): continuation via Pesin-block transfer operators, and why it stops

### 4.1 The continuation is needed only for the forward part
Let mu be ergodic with h_mu > 0 and mu(d) = 0. Let x be mu-generic and y != x a mu-generic point of xi(x) ⊂ W^u_loc(x) (Lemma 6.0). Let b, theta be as in Prop 6.1, S = delta_x - e^b delta_y, and T_z = B_z + F_z with
 B_z(phi) = int_{-inf}^0 e^{-zt} F_phi(t) dt,  F_z(phi) = int_0^inf e^{-zt} F_phi(t) dt.
- For t <= 0: |F_phi(t)| <= C e^{J_t(x)} e^{-theta|t|} ||phi||_{C^1} and J_t(x) = o(|t|). So B_z is holomorphic on the half-plane Re z < theta, which contains Re z = 0 and everything to its left.
- So the transfer operator on unstable discs proposed in the brief serves the backward part, and the backward part needs no continuation. Theorem B used that operator only because its points were not generic.
- The obstruction is entirely in F_z. This is the difference of the two single-orbit forward transforms int_0^inf e^{-zt} e^{J_t(w)} phi(g_t w) dt, for w = x and for w = y (weight e^b). The forward orbits of x and y separate, since y is on the unstable leaf of x.
- In Theorem B, F_z continued because the forward orbit of y entered a contracting forward disc at a periodic point and stayed there. Then one autonomous operator L' f = e^{j'} f o g_{P'} on C^K(disc) represents the whole forward tail, and the resolvent (I - e^{-zP'} L')^{-1} continues it.

### 4.2 What a Pesin-block version would need, and what fails
For a mu-generic w, the forward returns to a Pesin block K occur at times n_1 < n_2 < ..., with return maps g_{n_{i+1} - n_i} between different local stable discs W^s_loc(g_{n_i} w). The forward transform becomes sum_i e^{-z n_i} (L_i ... L_1 Phi_i)(w), a non-autonomous product with no resolvent identity, so Hennion + Riesz-Schauder (facts (H), (F) of R6-c) do not apply.
To get one autonomous operator, it must act on functions on the whole family of discs {W^s_loc(v) : v in K}, as the induced (first-return) weighted Koopman operator. That space contains functions that are constant along the discs, and on them the operator is the Koopman operator of the induced base dynamics, including the centre (zero-exponent) directions, which are neither contracted nor expanded. The following shows that this kills quasi-compactness.

**Proposition O (proved).** Let L be a bounded operator on a Banach space B with infinitely many distinct eigenvalues of modulus >= 1. Then r_ess(L) >= 1, so (H)+(F) cannot give a meromorphic resolvent on any disc {|s| > r} with r < 1.
*Proof.* If r_ess(L) = r < 1, then by (F) the spectrum in {|s| > r} consists of isolated eigenvalues. The infinitely many eigenvalues in the compact set sigma(L) ∩ {|s| >= 1} would accumulate at a point s* with |s*| >= 1 > r, and s* lies in sigma(L) since the spectrum is closed. Then s* is not isolated, a contradiction. ∎

*Application (model with a zero exponent).* Let N carry a flow h_t with an ergodic positive-entropy measure m (e.g. an Anosov flow). On N × T^q take g_t(n, theta) = (h_t n, theta + t alpha) with alpha Diophantine and mu = m × Haar. Then mu has q additional zero exponents, and its local stable and unstable discs are W^{s/u}_h(n) × {theta}.
- Let L f = e^{j} f o g_P be the fixed-time weighted Koopman operator on any Banach space B of functions on a family of such discs (or on N × T^q) that contains the functions e_k(n, theta) = e^{i k.theta}, with product volume so that j = 0.
- Then L e_k = e^{i P k.alpha} e_k. For all but countably many P these eigenvalues are pairwise distinct for infinitely many k, so r_ess(L) >= 1 by Proposition O.
- Directly: ||L^n e_k||_{C^K} ~ |k|^K while |e_k|_{C^{K-1}} ~ |k|^{K-1}. So no Lasota-Yorke inequality ||L^n f||_K <= R_n ||f||_K + C_n |f|_{K-1} with R_n < 1 can hold on all e_k.
The continuation step of Theorem B is GH-free. So any GH-free continuation theorem for non-hyperbolic positive-entropy mu would have to work in such product models, and there the Hennion mechanism provably has no spectral gap.
This does not prove that the pair transform has a natural boundary at Re z = 0 in the model. Heuristically it does: for phi = sum_k a_k(n) e^{ik.theta}, F_z(phi) = sum_k e^{ik.theta} A_k(z - i k.alpha), where A_k is the forward pair transform of the base flow. A singularity of A_k at 0 (expected, of size zeta^{-1/2}, from CLT behaviour of a(h_t n) - a(h_t n')) is then copied to the dense set {i k.alpha}. That is a heuristic, not a proof.

### 4.3 Mechanisms (i) and (iii) of the sketch
- (iii) is settled in §1. Quasi-analytic two-sided decay suffices and non-quasi-analytic decay does not (for the moment method). Two-sided decay is still required, so (iii) does not remove the need for forward cancellation.
- (i), smearing along the centre: for S = int rho(c) delta_{x(c)} dc along a centre curve, F_phi(t) for t >= 0 is int rho(c) e^{J_t(x(c))} phi(g_t x(c)) dc. With a zero exponent, the curve g_t(x(c)) has length e^{o(t)}, so averaging over c gives no exponential gain. In the product model, the integral of e^{i k.(theta(c) + t alpha)} rho(c) dc does not decay in t at all. So centre-smearing cannot replace the missing su-intersections. In the model, dim W^{ws} + dim W^{uu} = n - q < n, so forward and backward clusters cannot be matched by holonomy.

## 5. Final status

**Proved here.**
1. *Theorem J+ (§1).* Under GH, no nonzero distribution density S has two-sided decay of F_phi(t) = S(e^{J_t} phi o g_t) of quasi-analytic (Denjoy-Carleman) quality, continuously in phi. For example e^{-|t|/log(e+|t|)} suffices. Non-quasi-analytic decay cannot be handled by the moment method (Remark 1.3, cited Paley-Wiener).
2. *Lemma H (§2).* An eigen-family holomorphic only on a half-disc at 0 vanishes if it is flat at 0 with Carleman-quasi-analytic constants. This is sharp (e^{-1/sqrt z}).
3. *Theorem V (§3).* If GH holds, X preserves a smooth volume, and lambda* > 0 (in particular if h_top > 0), then the quasi-analytic vectors Q of R = X^{-1} are not C^1-dense in C^inf. Equivalently, C^1-density of Q forces zero entropy.
4. *Proposition O (§4).* With a zero exponent, the weighted Koopman / transfer operators used in Theorem B have essential spectral radius >= 1 in product models, so the Hennion route to continuing the forward transform across Re z = 0 cannot work GH-free.

**Not proved: (PE-NH) remains open**, and with it (PE) and the problem in dimension >= 4 (in dimension 4 modulo the Pesin estimates of Prop 6.2). Precisely, any one of the following would close it:
(Q1) a nonzero S with two-sided quasi-analytic decay (Theorem J+) for a non-hyperbolic positive-entropy mu with mu(d) = 0. This needs forward cancellation, i.e. points or densities that are pairwise forward-asymptotic across distinct unstable classes, which the zero exponent obstructs;
(Q2) a continuation of the forward single-orbit transforms across Re z = 0 (meromorphic with bounded pole order: Lemma M), which Proposition O shows cannot come from Hennion-type quasi-compactness;
(Q3) in the volume case, quantitative control of the iterated tame inverses ||R^N phi||_{C^1} (Carleman growth on a C^1-dense set), which GH via the closed graph theorem does not provide;
(Q4) for mu(d) <= -chi^+_min (resp. >= |chi^-_max|) with higher-dimensional unstable (resp. stable) directions: the non-stationary normal-form citation of Prop 6.2, which I did not check.
The chain itself (steps 2-4) I re-checked and found no flaw. Step 1 is exactly (PE-NH), and it is not established.

=== END OF ANSWER round7_q7 ===

