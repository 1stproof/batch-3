# round12_q9 — check of Proof A (ledger entry 113)

## 0. Plan and statement checked
Statement (entry 113 = Theorem 3.1 of Proof A): assume GH. Let mu be a g_1-invariant, g_1-ergodic Borel probability with h_mu(g_1) > 0. Then lambda := mu(J_1) = 0.
Plan: check every step of Proof A in order (§1). Then discuss the cited normal-form input [NF] (§2), and record the cases that are complete without the full [NF] (§3). The verdict is in §4.

## Summary verdict
Every step of Proof A that does not depend on [NF] is correct. Only minor clarifications are needed, and they are supplied below. The exponent bookkeeping in Lemma 2.1 and Step 4 is right, including the growth constant c''_K and the gap s. Proof A therefore proves Theorem 3.1 and Corollary 3.2 exactly as stated, modulo:
- [P] (Pesin unstable manifolds, including [P2]);
- [LS] (Ledrappier–Strelcyn);
- Ruelle's inequality and Birkhoff's theorem;
- Theorem J and Lemma 6.0 (both re-checked);
- one normal-form statement [NF'] (§2), weaker than Proof A's [NF]: measurable LOCAL charts are enough.

To my recollection, [NF'] is what Kalinin–Sadovskaya (JMD 2017) and Melnick (ETDS 2019) provide. I cannot verify their exact hypotheses from memory (§2).

Without [NF], the proof is complete (modulo classical 1-dimensional facts) in these cases:
- (i) u = 1;
- (ii) more generally, the fastest positive exponent chi_1 is simple and the Ledrappier–Young partial entropy h_1(mu) along the fast unstable foliation is positive.

When lambda > 0, read these conditions on the negative exponents. See §3.

---

## 1. Step-by-step check of Proof A

### 1.1 Tools section
- **Theorem J.** I re-checked it.
  - Step 3: integrating by parts gives m_j(P phi) = -j m_{j-1}(phi).
  - Step 4 (induction via F1 and F2) and Step 5 (holomorphic Fourier transform on the strip |Im xi| < eps, all derivatives vanishing at 0) are correct.
  - The constant C in (*) must not depend on phi. In Proof A it never does: it depends on x, the points, K, delta and L.
- **Notation.**
  - Birkhoff for f and for f^{-1}, applied to J_1, gives J_n/n -> lambda. Interpolation, using |J_t - J_{[t]}| <= ||d||_inf, gives real t.
  - Ruelle's inequality for f gives u >= 1.
  - d_0 = floor(chi_1/chi_l). Correct.
- **[P], [P2].** These are standard.
  - W^u(x) = {limsup < 0} coincides with the Pesin unstable manifold of the positive exponents. Indeed, limsup <= -eps for some eps in (0, chi_l) is the same set for all such eps.
  - [P2] holds for compact Q ⊂ W^u(x) because Q ⊂ f^m W^u_loc(x_m) for some m.
  - Zero exponents of mu play no role.
- **[LS] + Lemma 6.0.** Correct. I re-checked the monotonicity w(fx) >= w(x) and the conclusion w = 0 a.e.
- **[NF].** Discussed in §2. Two clarifications:
  - Sub-resonance maps must have P(0) = 0, i.e. no monomial with s = 0. The condition "weight <= chi_i" written in Proof A would formally allow constant terms. This is harmless here, because P_x(0) = H_{x_1}(f^{-1}x) = H_{x_1}(x_1) = 0 by (a).
  - The global extension H_x := (P^{(n)})^{-1}∘H^loc_{x_n}∘f^{-n} uses two facts. First, sub-resonance maps with invertible linear part form a group, since they are triangular with respect to the weights. Second, the local relations H^loc_{x_{k+1}}∘f^{-1} = P_{x_k}∘H^loc_{x_k} hold wherever both sides are defined. Both facts are available.
  - The extended H_x need not be onto E^u_x, and nothing requires that. Every later use (the sets B_w, B(0,1/L), the points zeta_i) only needs a fixed ball around 0 inside the image. Repair: choose r_0 <= the radius of H_w(W^u_loc(w)), and L large.
- **Lemma 1.1 (closure, degree bound).** Correct.
  - Substitute into a monomial of weight Σ s_j chi_j <= chi_i, replacing each E_j-coordinate by a polynomial whose monomials have weight <= chi_j. Every monomial produced has weight <= Σ s_j chi_j <= chi_i.
  - The weights are the same at every fibre, because mu is ergodic.
  - The class "E_i-component has weight <= chi_i" does not depend on the choice of linear coordinates inside each E_j.
  - Degree bound: |s| chi_l <= Σ s_j chi_j <= chi_1, so |s| <= d_0.
- **Lemma 1.2.** Correct. All norms on a finite-dimensional space are equivalent, and isometries identify each (E^u_x, Riemannian inner product) with R^u, so the constants depend only on (u, d_0, r_0, j).
- **Lemma 1.3.** Correct.
  - For T >= T_0(x), the count N(floor((1+delta)T)) - N(ceil(T)) equals delta T mu(G) + o(T), which is > 0. So the interval [T, (1+delta)T] contains a visit.
  - For T < T_0, take C(x) := (first visit time >= T_0). Visits are infinite by Birkhoff.

### 1.2 Section 2 (beta smooth along leaves)
- **(2.1).** beta_{g_s w}(g_s z) = ∫_{-inf}^{s}(d(g_r z) - d(g_r w)) dr = beta_w(z) + J_s(z) - J_s(w). Correct for all real s.
- **(2.2).** Correct, since Σ_{n>=0} ∫_{-1}^0 d(g_{r-n} ·) dr = ∫_{-inf}^0. Convergence is absolute: backward distances decay exponentially at integer times, and g_r is Lipschitz for r in [0,1].
- **Exponential growth constant.** The constant c_K with ||b∘f^m||_{C^{K+1}} <= C e^{c_K m} exists. Iterate Faà di Bruno on the compact manifold M.
- **G'_L.** The sets are increasing in L, and every point of the full-measure set lies in some G'_L, because H_w is C^1 near w. Measurability is [NF](c).
  - If one wants (G1) without measurability issues about the intrinsic distance d^u, replace it by a Lipschitz bound for H_w on H_w^{-1}(B(0,1/L)) relative to d^u. Nothing changes.
- **Lemma 2.1.** All steps are correct.
  - Step 2: [P2] at w gives the bound on d^u(f^{-n'}y, w_{n'}); (G1) at w_{n'} then gives sup_{B_w}|P^{(n')}_w| <= LC e^{-(chi_l-delta)n'}.
  - Step 4 identity: f^{n'-n}∘(H_{w_{n'}}^{-1}∘P^{(n')}_w) = f^{n'-n}∘f^{-n'}∘H_w^{-1} = f^{-n}∘H_w^{-1}, and Phi_n(0) = b(w_n).
  - Phi_n bound: ||Phi_n||_{C^{K+1}(B(0,1/L))} <= C ||b∘f^{n'-n}||_{C^{K+1}} (1+L)^{K+1} <= C e^{c_K(delta n + C)}. This is the chain rule applied to F∘G with ||G||_{C^{K+1}} <= L.
  - Step 5 (Faà di Bruno): each derivative of order 1..K+1 of Phi∘P is a sum of D^iPhi(P)·(i factors D^{a}P), with i >= 1. Each factor is <= C'e^{-(chi_l-delta)n'} <= 1. Hence ||T_n||_{C^{K+1}} <= C||Phi_n||_{C^{K+1}} e^{-(chi_l-delta)n'} <= C e^{(c_K delta - chi_l + delta)n}.
  - This is summable because delta(c_K+2) < chi_l. It uses n' >= n and the convexity of B(0,1/L), the latter for the C^0 term.
  - Conclusion: beta_w∘H_w^{-1} is C^{K+1} on B(0,r_0) for any admissible r_0.
- **(G3).** Measurable. Each T_n is a measurable C^{K+1}(B(0,1/L))-valued function of w: it is built from H_w^{-1}, using a measurable orthonormal frame of E^u_w. The series converges in that Banach space for a.e. w (Lemma 2.1, taking r_0 >= 1/L inside the image), and limits of measurable maps are measurable. The sets G_L increase to a full-measure set, so mu(G_L) > 0 for L large.

### 1.3 Theorem 3.1
- **Order of constants.** The order K -> c'_K, c''_K, c_K -> delta -> L is consistent. As delta -> 0, the left side of the third condition tends to (K+1)chi_l - |lambda| > 1, so a suitable delta exists.
- **Step 1.** Correct.
  - mu(G_fwd) = 1 by Birkhoff for the f-ergodic mu.
  - Since mu(G_fwd) = ∫ mu^xi_x(G_fwd) dmu, a.e. conditional gives G_fwd full mass.
  - A non-atomic probability makes xi(x) ∩ G_fwd infinite.
- **Step 2.** Correct. There are N_D homogeneous equations in N_D + 1 unknowns, so a solution w != 0 exists. Then S != 0: the y_i are distinct, beta_x(y_i) is finite, and S has coefficients w_i e^{beta_x(y_i)}, not all zero. This answers item (f).
  - Compared with Proof B: B's beta equals minus A's beta_x (B uses a = J_{-1} = -b), so both proofs use the same weights.
- **Step 3.** Correct.
- **Step 4.**
  - *Reduction.* By (2.1) with s = t: beta_x(y_i) + J_t(y_i) = beta_{g_t x}(g_t y_i) + J_t(x). Write g_t = g_s∘f^{-n'}, where s = n' + t >= 0. Then (2.1) at x_{n'} with time s gives beta_{g_s x_{n'}}(g_s y_i') = beta_{x_{n'}}(y_i') + J_s(y_i') - J_s(x_{n'}). So F_phi(t) = e^{J_t(x)} Σ w_i Psi(y_i'). This is item (e), and it is correct.
  - *Theta.* Put a := beta_{x_{n'}}∘H^{-1} + J_s∘H^{-1} - J_s(x_{n'}). Then sup|a| <= L + 2s||d||_inf, by (G3) and |J_s| <= s||d||_inf. Also ||a||_{C^{K+1}} <= C(L) e^{c'_K s}, by (G2) and the chain rule.
    - Hence ||e^a||_{C^{K+1}} <= C e^{L + 2s||d||_inf} (1 + C e^{c'_K s})^{K+1}.
    - The factor phi∘g_s∘H^{-1} contributes C e^{c'_K s}||phi||_{C^{K+1}}.
    - The total exponent is (K+2)c'_K + 2||d||_inf = c''_K. This matches Proof A.
  - *Points and moments.* zeta_i = P^{(n')}_x z_i, by Lemma 1.1. The bound |zeta_i| <= LC e^{-(chi_l-delta)n'} follows from [P2] with Q = {y_i}, together with (G1).
    - (T_K Theta)∘P^{(n')}_x is a polynomial on E^u_x of degree <= K d_0 = D, constant term included. So Σ w_i (T_K Theta)(zeta_i) = 0.
    - The Taylor remainder on the convex ball is <= C_K ||Theta||_{C^{K+1}} |zeta|^{K+1}.
  - *Exponents.* The total is (|lambda|+delta)|t| + c''_K s - (K+1)(chi_l-delta)n'. Use s <= delta|t| + C and n' >= |t| (the right direction, since the remainder exponent is negative). This gives the bound C exp([|lambda| + delta + c''_K delta - (K+1)(chi_l-delta)]|t|) <= C e^{-|t|/2}. The bookkeeping (item (c)) is correct.
  - The requirement n' >= n_1 holds for t <= -n_1. For bounded t the bound is trivial.
- **Step 5.** Theorem J applies with k = K+1 and eps = min(|lambda+delta|, 1/2), so S = 0. This is a contradiction.
- **Case lambda > 0.** -X is GH. Its time-1 map is f^{-1}, and mu is f^{-1}-ergodic with the same entropy. Since J^{-X}_1 = J_{-1} and J_{-1}(y) = -J_1(f^{-1}y), invariance gives mu(J^{-X}_1) = -lambda. Correct.

### 1.4 Corollary 3.2 (item (g))
Correct. Proof A takes for granted the identity mu = ∫_0^1 (g_s)_*mu_0 ds. Here is a justification.
- Let mu = ∫ m dP(m) be the g_1-ergodic decomposition. Each g_s commutes with g_1, so it maps g_1-ergodic measures to g_1-ergodic measures, and g_1 itself fixes each component. So the circle R/Z acts on the space of components, and P is invariant under this action.
- Because mu is flow-ergodic, P is ergodic for the circle action. The action of the compact group R/Z has smooth orbit structure, so P is carried by a single orbit and equals the image of Haar measure on that orbit.
- Hence mu = ∫_0^1 (g_s)_*mu_0 ds.
- Next, h_{(g_s)_*mu_0}(g_1) = h_{mu_0}(g_1), since g_s conjugates g_1 to itself. Jacobs' formula then gives h_mu = h_{mu_0}.
- Finally mu_0(J_1) = ∫_0^1 mu_0(d∘g_s) ds = mu(d).

---

## 2. The normal-form input (item (a))

### 2.1 What the papers prove (cited from memory, with stated uncertainty)
**Kalinin–Sadovskaya, "Normal forms for non-uniform contractions", JMD 11 (2017).** As I recall it:
- *Setting.* An ergodic invertible measure-preserving system (X, mu, f). A measurable vector bundle E. Fibre maps F_x : E_x -> E_{fx} that are C^r diffeomorphisms, or are defined on neighbourhoods of 0, with F_x(0) = 0. The derivative cocycle D_0F_x has only negative Lyapunov exponents, chi_1 < ... < chi_l < 0, with arbitrary multiplicities and any number of them.
- *Hypotheses.* A regularity hypothesis on x -> ||F_x||_{C^r}: bounded or tempered, in Lyapunov norms. I do not remember which. Also r large compared with the ratio chi_1/chi_l of the extreme exponents, so that every sub-resonance is a polynomial term of order <= r. C^inf certainly suffices.
- *Conclusion.* A measurable family of C^r diffeomorphisms H_x with H_x(0) = 0 and D_0H_x = Id, such that P_x = H_{fx}∘F_x∘H_x^{-1} lies in the finite-dimensional group of sub-resonance polynomial maps. These are taken with respect to the Lyapunov splitting, with the condition Σ s_j chi_j <= chi_i written for the positive rates. H is unique up to composition with sub-resonance maps.
- *Further features.* A local version (fibre maps defined on balls of tempered radius) is included or follows by cut-off. The authors apply it to the restriction of a diffeomorphism to Pesin stable manifolds; applied to f^{-1}, this covers Pesin unstable manifolds.
- *No narrow-band condition.* None is needed in this measurable (Oseledets) setting. Narrow-band conditions belong to the uniform/continuous versions (Guysinsky–Katok; Kalinin–Sadovskaya, Geom. Dedicata 2016), where only bounds on the rates are known.

**Melnick, ETDS 2019.** Same type of result (non-stationary sub-resonance normal forms for measurable contracting cocycles, C^inf version), with measurable dependence of the charts. This is the form used by Brown–Eskin–Filip–Rodriguez Hertz.

**Where I am unsure.**
- The exact regularity and temperedness hypotheses.
- Whether the papers state the Pesin-manifold corollary for measures that also have zero exponents.

Mathematically, zero exponents in the complementary directions are irrelevant. Only the family of C^inf contractions f^{-1} : W^u(x) -> W^u(x_1) enters. Through Pesin's graph charts, which have tempered C^r norms, this family is a non-uniform contraction with exponents -chi_1, ..., -chi_l. Pesin's unstable-manifold theorem for an arbitrary ergodic measure with some positive exponents provides exactly such charts.

### 2.2 What Proof A actually needs: [NF']
For mu-a.e. x there are:
- an open neighbourhood U_x of x in W^u(x) with f^{-1}(U_x) ⊂ U_{x_1}, and with the f^n(U_{x_n}) increasing and exhausting W^u(x) (standard when U_x is a Pesin local leaf of tempered size in Lyapunov charts);
- a C^{K+2} embedding H_x : U_x -> E^u_x, with H_x(x) = 0, for each fixed K needed;

such that:
- H_{x_1}∘f^{-1} = P_x∘H_x on U_x, with P_x sub-resonance;
- x -> H_x is measurable as a C^{K+2}-valued map, after a measurable trivialisation of E^u.

The global H_x of Proof A then follows from Proof A's extension formula. The definitions agree because of the inclusions f^{-1}U_x ⊂ U_{x_1} and the group property. Properties (a)–(c) as used follow. Two points to note:
- D_xH_x = Id and surjectivity onto E^u_x are never used. Only (G1), (G2) and balls of radius 1/L inside the image are used.
- No tempered bound on H_x is used. The good-times device (Lemma 1.3), applied to the Lusin sets G_L, replaces it, and I checked that this device is correct.

So **Proof A is complete modulo [NF']**. As far as I can recall, [NF'] is the content of KS 2017 / Melnick 2019 applied to f^{-1}|W^u, and it requires neither narrow band nor hyperbolicity of mu.

## 3. Cases complete without the general normal-form theorem

**(A) u = 1** (one positive exponent, simple). Then d_0 = 1 and the P_x are linear maps of R. The H_x are the classical affine parameters on 1-dimensional Pesin unstable curves, given by H_x(y) = ∫_x^y Π_{k>=0} [|Df^{-1}|_{TW^u}(f^{-k}z)| / |Df^{-1}|_{TW^u}(f^{-k}x)|] dz, a classical 1-dimensional distortion construction (cited).
- They are C^inf along leaves, depend measurably on x, and satisfy H_{x_1}∘f^{-1} = A(x)H_x.
- Proof A then runs verbatim, with polynomials of degree <= K in one variable and K+2 points.
- This is Proposition 6.2 of R6-a, now with complete estimates: the good-times device replaces the tempered bounds that were only sketched there.

**(B) Fast leaf.** Suppose lambda < 0, the fastest positive exponent chi_1 is simple, and the Ledrappier–Young partial entropy h_1(mu) along the fast unstable foliation W^1 is positive. Here W^1 is the Pesin strong unstable curve tangent to E_1, which exists for every ergodic mu (Pesin; Ledrappier–Young II, cited).
- *Non-atomic conditionals.* Ledrappier–Young II give an increasing measurable partition xi_1 subordinate to W^1 with H(xi_1 | f xi_1) = h_1. The proof of Lemma 6.0 uses only that the partition is increasing, that mu is f-invariant and ergodic, and that H(xi|f xi) > 0. Applied to xi_1 it gives non-atomic conditionals on W^1-plaques.
- *Rerunning Proof A.* Run Proof A with W^1 in place of W^u, chi_1 in place of chi_l, d_0 = 1, and affine parameters on the curves W^1(x) as in (A).
  - [P2] holds on W^1 with rate chi_1 - delta.
  - Lemma 2.1 holds for beta along W^1 with the same proof.
  - Steps 1–5 are unchanged, with K chosen so that (K+1)chi_1 > |lambda| + 1.
- So Theorem 3.1 holds in case (B), modulo classical 1-dimensional facts and Ledrappier–Young.
- If lambda > 0, apply (B) to -X. The condition then concerns the most negative exponent of mu (simple) and the partial entropy of g_{-1} along the fast stable curves.

**(C) Not covered without [NF'].** Two situations are left:
- E_1 has dimension > 1;
- h_1 = 0 while h_mu > 0, so that the entropy lives only in slower unstable directions.

Example of the second: a positive-entropy measure times a Dirac mass at a strongly expanding fixed point. In these situations the backward transports in smooth charts are not confined to a finite-dimensional space of maps. A finite family of moment conditions then cannot annihilate the Taylor polynomials at all good times. Supplying that finite-dimensionality is exactly what [NF'] does, and I see no way around it.
- Restricting to the slowest direction does not help: there is no invariant smooth slow foliation.
- Quotienting a W^{(i)} leaf by the faster sub-foliation does not help either: the holonomies are only Hölder, and the test functions are not constant along the fast leaves.
- One sub-case is easier: all positive exponents equal, of any multiplicity. Then d_0 = 1, and only non-stationary linearisation is needed. This is a special case of [NF'], so it is still a citation.

## 4. Verdict
1. Every inference of Proof A outside [NF] is correct. Only minor clarifications are needed, and they are supplied in §1:
   - P(0) = 0 for sub-resonance maps;
   - the image balls need only be local;
   - (G3) is measurable;
   - Lemma 1.3 holds for small T;
   - the g_1-ergodic decomposition used in Corollary 3.2.

   The items flagged in the task check out: Lemma 1.1, Lemma 1.2, Lemma 1.3, Lemma 2.1 and (G3), Step 4's reduction and its exponent bookkeeping (gap s, constant c''_K), S != 0, and the reduction of Corollary 3.2.
2. Proof A proves Theorem 3.1 (entry 113) exactly as stated, and Corollary 3.2, modulo:
   - Pesin theory [P], [P2];
   - Ledrappier–Strelcyn;
   - Ruelle and Birkhoff;
   - the local measurable normal-form statement [NF'] of §2.2.

   [NF'] is weaker than Proof A's [NF]: it needs only local charts, measurability and no temperedness. To my recollection it is what Kalinin–Sadovskaya 2017 and Melnick 2019 provide for f^{-1} restricted to W^u, with no narrow-band or hyperbolicity hypothesis. The exact hypotheses of those papers are not re-verified here.
3. Without [NF'], the theorem is proved:
   - in case (A), u = 1;
   - in case (B), fastest exponent simple with positive fast partial entropy;
   - in the corresponding cases on the stable side when lambda > 0.

**Open.**
- (PE0): exclude lambda = 0, which this method cannot reach. Hence the original problem (zero topological entropy) remains open along this chain in dimension >= 4.
- An independent verification of the exact hypotheses of [NF'] in the cited papers.

=== END OF ANSWER round12_q9 ===
