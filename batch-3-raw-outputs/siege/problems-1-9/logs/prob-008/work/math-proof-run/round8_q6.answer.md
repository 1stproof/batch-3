# round8_q6 — answer

## 0. Status (summary)

The named approach is "tame closed range and duality". Results, in order of strength:

1. **Proposition C1 (proved; answers lead (c)).** Assume GH. Then the following are equivalent:
   - (V): X preserves a smooth positive density;
   - P = X + d has closed range in C^inf(M);
   - there is a distribution u with Xu = -d.
   
   So closedness of the range of P (equivalently, by the closed range theorem, weak*-closedness of the range of X on D'(M)) is not a weaker substitute for (V). It is (V). Once it holds, the flow is uniquely ergodic and minimal, and a positive-entropy measure would have to be the smooth volume itself. Without (V), X(D') is a proper subspace of D' that is not weak*-closed: it misses both 1 and d, and d lies in its weak* closure.
2. **Structural dichotomy (proved; explains leads (a) and (b) outside the volume case).** The weighted transport S(e^{J_t} phi o g_t), used by Theorem J, Lemma K, Theorem G and the B_j chain, is governed by the transpose of P. Under GH its kernel is trivial ((K0)), but by item 1 its range is closed only if (V) holds. The closed-range half of GH (Lemma A/B) concerns the transpose of X, i.e. the unweighted transport S(phi o g_t). That operator has closed range, but its kernel I (the invariant distribution densities) may be large. The unweighted analogue of Theorem J holds as soon as dim I = 1, and under GH that is again (V). So outside (V) the closed-range half cannot enter the Jordan-chain mechanism. The approach therefore reduces to the volume case.
3. **Volume case: divisor identity and leafwise geometric bounds (proved).** Assume GH and a smooth invariant volume omega. Let R be the tame inverse of X on mean-zero functions. For any pair x != y that is exponentially backward-asymptotic, the backward divisors B_j of lead (a) are exactly B_j = S o R^{j+1}, with S = delta_x - delta_y. They coincide with the Hahn–Banach pair functionals of lead (b), which are unique here. Consequently
   |(R^N phi_0)(g_t x) - (R^N phi_0)(g_t y)| <= C theta^{-N} e^{-theta|t|} ||phi||_{C^1}  for all t <= 0 and N >= 1.
   The global norms of R^N phi_0 are only tamely controlled. The leafwise oscillations, however, are geometrically controlled, along unstable leaves and (by -X) along stable leaves. This is exactly the quasi-analytic control that Theorem V asks for, but only along strong leaves, not along the centre or the flow.
4. **Why the approach stops (precise; partly heuristic).** In the volume case every object produced by tame duality from point-pair data has a forward half that the closed-range data does not control. The only output is infinite-order flatness at z = 0 of the eigen-family T_z. Flatness without quasi-analytic rates is consistent with T_z != 0: e^{-z^{-1/2}} is the standard example. In a translation (Lax–Phillips) model of the Pinsker complement, smoothness gives exponential decay of the "fine" tail, and GH gives infinite divisibility by the generator. Nonzero vectors with both properties exist, so a contradiction needs control of the "coarse" tail (rates of convergence to the Pinsker factor). Neither GH nor positive entropy is known to supply that.

**Not proved:** (PE-NH), and the problem in dim M >= 4. Open questions are listed in §6.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, P phi = X phi + d phi, J_t(x) = int_0^t d(g_s x) ds. A distribution density T corresponds to the distribution function u = T/nu, with <Xu, phi nu> = -T(P phi) (Observation 0).

---

## 1. Proposition C1: under GH, closed range of P is equivalent to (V)

**Lemma 1.1 (elementary closed range duality).** Let E, F be Fréchet spaces and A: E -> F continuous and linear with A(E) closed. Then every continuous linear functional l on E that vanishes on ker A is of the form l = lambda o A for some continuous linear functional lambda on F.

*Proof.*
1. A(E) is a closed subspace of a Fréchet space, so it is Fréchet.
2. A: E -> A(E) is continuous and onto. By the open mapping theorem it is open, so the induced map E/ker A -> A(E) is a topological isomorphism.
3. Define lambda_0(Ae) := l(e). This is well defined because l vanishes on ker A. It is continuous on A(E) by step 2.
4. Hahn–Banach (locally convex form) extends lambda_0 to some lambda in F'. Then lambda(Ae) = l(e) for all e. ∎

**Lemma 1.2 (smooth invariant signed densities have zero mean divergence).** Let rho be smooth with P rho = 0, i.e. L_X(rho nu) = 0. Then int d rho dnu = 0. No GH is needed here.

*Proof.*
1. Along orbits, d/dt rho(g_t x) = (X rho)(g_t x) = -d(g_t x) rho(g_t x). Hence rho(g_t x) = rho(x) e^{-J_t(x)}.
2. Consequently |rho| o g_t · e^{J_t} = |rho|. This is the invariance criterion for |rho| nu: J_t is the log nu-Jacobian of g_t, so int phi o g_t · h dnu = int phi · (h o g_{-t}) e^{J_{-t}} dnu, and the right side equals int phi h dnu when h o g_s e^{J_s} = h for all s.
3. The set A = {rho > 0} is invariant by step 1. If rho = 0 identically there is nothing to prove. Otherwise m := |rho| nu / int|rho| dnu is an invariant probability.
4. Claim: for m-a.e. x, J_t(x)/t -> 0 as t -> +inf.
   - By Birkhoff the limit exists m-a.e.
   - By Poincaré recurrence (compact metric space, invariant probability), m-a.e. x satisfies g_{t_k} x -> x for some t_k -> inf.
   - For m-a.e. x we have rho(x) != 0. Step 1 gives J_{t_k}(x) = log|rho(x)| - log|rho(g_{t_k} x)|, which tends to 0 by continuity of rho. So the limit is 0.
5. By Birkhoff, E_m(d | invariant sets) = 0 m-a.e. Hence int_A d dm = 0 and int_{A^c} d dm = 0, since A is invariant.
6. int d rho dnu = (int |rho| dnu)(int_A d dm - int_{A^c} d dm) = 0. ∎

**Proposition C1.** Assume GH. The following are equivalent:
(i) (V): there is a smooth rho_0 > 0 with L_X(rho_0 nu) = 0;
(ii) P(C^inf) is closed in C^inf(M);
(iii) there is u in D'(M) with Xu = -d.

*Proof.*
- (i) => (ii). With rho_0 as in (i) we have X rho_0 = -d rho_0. Hence P(rho_0 w) = rho_0 Xw + w(X rho_0 + d rho_0) = rho_0 Xw. So P(C^inf) = rho_0 · X(C^inf). This set is closed because X(C^inf) is closed (Text B, Corollary 3) and multiplication by rho_0 is a topological automorphism of C^inf.
- (ii) => (iii). Apply Lemma 1.1 with E = F = C^inf(M), A = P and l(phi) := int d phi dnu. By Lemma 1.2, l vanishes on ker P. So there is a distribution density T with T(P phi) = int d phi dnu for all phi. Then u := T/nu satisfies <Xu, phi nu> = -T(P phi) = <-d, phi nu>, i.e. Xu = -d.
- (iii) => (i). By GH, u is smooth. Put rho_0 := e^u > 0. Then X rho_0 = -d rho_0, so P rho_0 = 0 and L_X(rho_0 nu) = 0. ∎

**Remarks.**
1. The proof of (ii) => (i) uses GH only once, for the right-hand side -d. It does not use (K0).
2. In terms of the transpose: P^T T = T o P corresponds to -X on distribution functions. So (ii) says that X(D') is weak*-closed. (That reformulation needs the standard closed range theorem for Fréchet spaces, cited from memory, e.g. Trèves, *Topological Vector Spaces, Distributions and Kernels*, Thm 37.2. The proof above does not need it.)
3. Suppose (V) fails under GH. By (iii), -d is not in X(D'), and by (K1) neither is 1. By the bipolar theorem, the weak* closure of the range of P^T (= -X on distribution functions) is (ker P)^perp, and -d lies in (ker P)^perp by Lemma 1.2. So **without (V), X(D') is a proper subspace of D' that is not weak*-closed: -d is in its weak* closure but not in X(D').** If moreover ker P = 0, then X(D') is weak*-dense. I have *not* shown that ker P != 0 alone forces (V): one would need log|rho| to be a distribution solution of Xu = -d.
4. Consequence for lead (c). If the range of P were closed, then (V) would hold. (O2) would then give unique ergodicity and minimality, and a positive-entropy ergodic measure would have to be omega itself. (PE-NH) then reduces to statement (*) of block R7-d (the volume case). Closedness of P(C^inf) is, however, *equivalent* to (V) under GH, i.e. to the Greenfield–Wallach-type assertion that is itself open. So lead (c) does not give (V) for free.

---

## 2. Weighted versus unweighted transport: where each half of GH lives

Two transports are attached to a distribution density S:
- weighted: F_phi(t) = S(e^{J_t} phi o g_t), with d/dt F_phi(t) = F_{P phi}(t);
- unweighted: G_phi(t) = S(phi o g_t), with d/dt G_phi(t) = G_{X phi}(t).

The Jordan-chain proof of Theorem J (moments m_j, m_j o P = -j m_{j-1}) works for a transport exactly when the transpose of the governing operator has
(a) a one-dimensional kernel spanned by an element that does not lie in its own range.

| | operator | kernel of transpose | range |
|---|---|---|---|
| weighted | P | R·nu by (K0) | contains nu? No, by (K1) |
| unweighted | X | I (invariant densities) | closed, = {T : T(1) = 0} (GH, Lemma B) |

**Observation 2.1 (proved).** Assume GH.
(a) For the weighted transport, (a) holds by (K0) and (K1). This is Theorem J.
(b) For the unweighted transport, (a) holds iff dim I = 1. Under GH, dim I = 1 implies (V).

*Proof of (b).*
- Run Theorem J's steps 2–4 with X in place of P. Then m_0 o X = 0, so m_0 lies in I. Also m_0 = -m_1 o X lies in the range of the transpose of X, which is {T : T(1) = 0} (Lemma B(iii) of R7-d, together with the fact that ker X on C^inf is the constants).
- If I = R·mu with mu(1) = 1, then m_0 = c mu with c = m_0(1) = 0. Inducting as in Theorem J gives all m_j = 0, and Fourier uniqueness gives S = 0. If dim I >= 2, the chain argument does not close.
- If dim I = 1, then I = R·mu, where mu is the unique invariant probability. The condition of (O3), "T(d) = c T(1) for all T in I", holds with c = mu(d). So d lies in R + X(C^inf), and (O3) gives (V). ∎

**What this means for leads (a) and (b) in general.**
- Lemma B(iii) (tame Hahn–Banach division: T = S o X) is division in the *unweighted* picture.
- The divisors B_j of lead (a) satisfy B_j o P = B_{j-1}. This is division in the *weighted* picture, i.e. by P^T, which is -X on distribution functions.
- Outside (V) these are different operators. By Proposition C1, the weighted division has closed range only under (V).
- So the tame bounds of Lemma B(iii) give no information on the B_j unless (V) holds. The same applies to the Hahn–Banach pair functionals S_{pq} of lead (b): they live in the unweighted picture, where the uniqueness needed for a Jordan chain holds only if dim I = 1, which again gives (V).
- **Conclusion: the closed-range half of GH can enter a Theorem-J-type argument only in the volume case.** §3 treats that case.

---

## 3. Volume case: divisors = iterated tame inverses; leafwise geometric bounds

Setting: GH, and X preserves a smooth positive density omega. Take nu = omega, so d = 0, J = 0 and P = X. By (O2) the flow is uniquely ergodic, and I = R·omega. By Text B Corollary 3, X: C^inf_0 -> C^inf_0 is a topological isomorphism, where C^inf_0 is the space of omega-mean-zero functions. Let R be its inverse and phi_0 := phi - omega-hat(phi). R commutes with composition by g_t: if Xv = f, then X(v o g_t) = f o g_t, and v o g_t is again mean zero.

Let x != y satisfy d(g_t x, g_t y) <= C0 e^{-theta|t|} for t <= 0. Such pairs exist whenever lambda* > 0 (R5-a, Lemma 2), for example on a Pesin unstable leaf. Put S = delta_x - delta_y and G_phi(t) := phi(g_t x) - phi(g_t y). Then |G_phi(t)| <= C0 e^{-theta|t|} ||phi||_{C^1} for t <= 0.

**Definition.** B_j(phi) := int_{-inf}^0 ((-t)^j / j!) G_phi(t) dt for j >= 0. Then |B_j(phi)| <= C0 theta^{-j-1} ||phi||_{C^1}.

**Proposition 3.1 (proved).**
(a) B_0(X phi) = S(phi), B_j(X phi) = B_{j-1}(phi) for j >= 1, and B_j(1) = 0.
(b) B_j(phi) = S(R^{j+1} phi_0) for all smooth phi and all j >= 0.
(c) Hence, for every N >= 1, every smooth phi and every t <= 0:
 |(R^N phi_0)(g_t x) - (R^N phi_0)(g_t y)| <= C0 theta^{-N} e^{-theta|t|} ||phi||_{C^1}.
(d) Every Hahn–Banach solution S' of S'(X phi) = phi(x) - phi(y) with S'(1) = 0 equals B_0. In particular such S' are unique, and S' = S o R.

*Proof.*
(a) G_{X phi} = G_phi'. Integrate by parts on [-L, 0] and let L -> inf. The boundary term at -L vanishes by the exponential decay. At 0 it equals G_phi(0) = S(phi) for j = 0, and 0 for j >= 1. Also G_1 = 0.
(b) Put D_j(phi) := S(R^{j+1} phi_0), a continuous functional with D_j(1) = 0. For psi smooth, R^{j+1}(X psi) = R^j psi_0, so D_0(X psi) = S(psi_0) = S(psi) (S(1) = 0) and D_j(X psi) = D_{j-1}(psi). Let E_j := B_j - D_j. Then E_0 o X = 0, so E_0 is an invariant distribution density, hence E_0 = c omega. Since E_0(1) = 0, c = 0. Inductively, E_j o X = E_{j-1} = 0 gives E_j = 0 in the same way.
(c) R^N phi_0 o g_t = R^N((phi o g_t)_0). So the left side equals |B_{N-1}(phi o g_t)| by (b). Now
 B_{N-1}(phi o g_t) = int_{-inf}^0 ((-s)^{N-1} / (N-1)!) G_phi(s + t) ds.
 For t <= 0 the integrand is bounded by C0 ||phi||_{C^1} (|s|^{N-1} / (N-1)!) e^{-theta(|s| + |t|)}, and the integral of that is C0 theta^{-N} e^{-theta|t|} ||phi||_{C^1}.
(d) S' - B_0 vanishes on X(C^inf) = C^inf_0 and on 1, so S' - B_0 = 0. ∎

**Corollary 3.2 (stable side).** The same holds for x, y exponentially forward-asymptotic, with R replaced by -R. Apply Proposition 3.1 to -X, which is GH by (O4) and preserves omega; its tame inverse is -R. So on Pesin blocks of an ergodic measure with positive entropy, the iterated inverses R^N phi_0 have geometrically bounded oscillation (C theta^{-N} ||phi||_{C^1}) along local strong unstable and local strong stable leaves. The constants depend only on the Pesin block. By contrast, ||R^N phi_0||_{C^0} is controlled only tamely (C_N ||phi||_{C^{m_N}}), and along the flow direction R^N phi_0(g_s x) - R^N phi_0(x) = int_0^s R^{N-1} phi_0(g_r x) dr, which carries no geometric bound.

**What this gives, and why it is not enough (precise).**
1. Theorem V (R7-e) asks for quasi-analytic growth of K_N(phi) = ||R^N phi_0||_{C^1}. Proposition 3.1 gives geometric growth of the strong-leaf oscillations of R^N phi_0. That is the right size, but in the wrong directions: the eigen-family T_z(phi) = z^N T_z(R^N phi_0) needs S(R^N phi_0 o g_t) for t >= 0, where x and y separate.
2. For t >= 0, Proposition 3.1(b) gives
 |S(R^N phi_0 o g_t)| = |B_{N-1}(phi o g_t)| <= C0 ||phi||_{C^1} sum_{k=0}^{N} t^k theta^{-(N-k)} / k! + 2||phi||_inf t^N/N!,
 which is <= C ||phi||_{C^1} theta^{-N} e^{theta t}. Combined with the trivial bound 2||R^N phi_0||_inf =: 2K'_N, this gives
 |T_z(phi)| <= C |z|^N K'_N^{1 - sigma/theta} theta^{-N sigma/theta} / sigma,  sigma = Re z in (0, theta),
 for N with K'_N >= theta^{-N}. This is an improvement over Theorem V's bound |z|^N K'_N / sigma. But as sigma -> 0 it degenerates to the same bound, so Lemma H still needs quasi-analytic K'_N. Lead (a)'s hoped-for contradiction "geometric growth of the B_j + eigen-relation + tame bounds" does not materialise: the geometric bounds on the B_j are exactly the Taylor coefficients at 0 of the backward transform B_z, which is already holomorphic on Re z < theta. The forward transform remains uncontrolled.

---

## 4. Why the volume-case approach stops: the coarse tail (partly heuristic)

**Lemma 4.1 (proved, complex analysis).** Put F(z) = e^{-z^{-1/2}}/(1+z) (principal branch) on Re z > 0.
- F is in the Hardy space H^2 of the right half-plane. Indeed, for Re z >= 0, z != 0, one has Re(z^{-1/2}) >= |z|^{-1/2} cos(pi/4) > 0, so |F(z)| <= 1/|1+z|.
- For every N, z^{-N} F(z) is also in H^2. Indeed, |z^{-N} e^{-z^{-1/2}}| <= |z|^{-N} e^{-|z|^{-1/2}/sqrt 2} is bounded near 0.
- By Paley–Wiener, F and z^{-N}F are Laplace transforms of L^2 functions k_0 and k_N supported in [0, inf), with d^N k_N / dt^N = k_0 in the distributional sense. Their Fourier transforms are F(i xi) and (i xi)^{-N} F(i xi) up to normalisation.

**Heuristic model (sketch, not proved for a general positive-entropy omega).** Assume an exhaustive filtration by unstable partitions for the flow (Pesin / Ledrappier–Young). Then the Pinsker complement H carries a translation (Lax–Phillips) representation: H ≅ L^2(R; K), with U_t = translation and the subspaces "measurable w.r.t. g_T xi, orthogonal to Pinsker" corresponding to functions supported in [T, inf). In that model:
- smooth phi have exponentially decaying *left* (fine) tails: ||1_{s<T} k_phi|| <= C e^{theta T} ||phi||_{C^1}. This is the smoothness of phi at small unstable scales, the L^2 shadow of Proposition 3.1(c).
- GH gives that k_phi is infinitely divisible by d/ds in L^2, tamely (Proposition 3.1 of R7-b).
- Nothing constrains the *right* (coarse) tail: there is no rate for E(phi | g_T xi) -> E(phi | Pinsker) as T -> inf.

Lemma 4.1 shows that nonzero k satisfying the first two properties exist; it can even have support in [0, inf). So any contradiction must use coarse-scale information. In the hyperbolic case the coarse unstable scale is linked to the fine stable scale by local product structure (this is where Theorem G and Lemma K succeed). With a zero centre exponent there is no such link (R7-a §4, R7-f §3). That is the same obstruction as in the weighted picture, seen spectrally.

---

## 5. Lead (d): other routes from tame solvability to zero entropy (remarks)

- **Gottschalk–Hedlund / eigenfunction route.** If f takes values in Z and f - c = h o T - h with h bounded, then e^{2 pi i h} is an eigenfunction. For smooth flows the integer structure is available only through closed 1-forms with integral periods: f = eta(X), eta = d theta, gives eigenfunctions e^{2 pi i (theta - u)}. This yields the Rodriguez Hertz torus factor of dimension b_1(M) (cited from memory). It says nothing about entropy in the fibres, and nothing at all when b_1 = 0.
- **Spectral route.** The spectral measures of smooth functions are flat at 0 (R7-b, Proposition 3.1). This is compatible with Lebesgue spectrum, as in §4.
- **Tame-estimate counting.** Bounded discrepancy (Lemma F(4) of R7-d) holds for all smooth "cylinder" functions prod_i phi_i o g_{s_i}. The errors grow like e^{m Lambda s_max}, which is compatible with uniquely ergodic positive-entropy symbolic behaviour. No contradiction found.

---

## 6. What is proved, what is open

**Proved here.**
- Proposition C1: under GH, (V) <=> P(C^inf) closed <=> there is u in D' with Xu = -d. Also Lemma 1.2 (no GH needed) and Remark 3 (without (V), X(D') is proper and not weak*-closed).
- Observation 2.1: the weighted/unweighted dichotomy. The closed-range half of GH supports a Jordan chain only if dim I = 1, which under GH gives (V).
- Proposition 3.1 and Corollary 3.2 (volume case): B_j = S o R^{j+1}; Hahn–Banach pair functionals are unique and equal B_0; geometric leafwise oscillation bounds for R^N phi_0 along strong stable and unstable leaves; the improved but still non-closing bound on T_z.
- Lemma 4.1: an explicit nonzero, infinitely divisible, one-sided L^2 profile, flat at 0.

**Sketched / heuristic.** §4: the translation-representation model, and the claim that no argument using only fine-tail decay and divisibility can conclude. §5.

**Open.**
1. (PE-NH) itself, hence the problem in dim M >= 4, in both the volume and the non-volume case.
2. (V) under GH, equivalently closedness of P(C^inf) (Proposition C1). This is a Greenfield–Wallach-type statement.
3. Volume case (*) of R7-d. A sharper sub-question suggested by Corollary 3.2: if R^N phi_0 has geometrically bounded oscillation along the strong stable and unstable leaves of omega, must ||R^N phi_0||_{C^0} grow quasi-analytically for a C^1-dense set of phi? If so, Theorem V would finish the volume case. Equivalently, one would need coarse-tail (rate-of-Pinsker-convergence) control for smooth functions, which neither GH nor positive entropy is known to give.

=== END OF ANSWER round8_q6 ===
