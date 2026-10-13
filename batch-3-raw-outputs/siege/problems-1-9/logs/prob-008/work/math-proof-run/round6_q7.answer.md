# round6_q7 — answer

## 0. Status (read first)

**Target.** Under GH, lim_{t->inf} (1/t) log ∫ ||Λ Dg_t|| dν = 0. Equivalently (PE): h_top(g_1) = 0.

**Outcome.** NOT proved. The target is not reached, neither in general nor in the case of a smooth invariant volume (V). What this file proves is listed below.

- **§1.** A finite-regularity form of GH that needs no volume (Proposition 1).
- **§2.** In case (V), a list of consequences of GH; proofs complete (Proposition 2):
  - (a) every C^m function is cohomologous to a constant, with a C^1 transfer function and uniform bounds;
  - (b) endpoint rigidity of occupation measures;
  - (c) the derivative of the transfer function along unstable vectors;
  - (d) spectral measures of smooth functions vanish to infinite order at 0, so the asymptotic variance is 0;
  - (e) a functional identity for bi-asymptotic pairs.
- **§3.** In case (V), (PE) is equivalent to: all Lyapunov exponents of the invariant volume ω vanish. Equivalently λ* = 0. Positive entropy would need a NON-hyperbolic ω. (Proved, modulo the cited Pesin formula and Katok/Lian–Young closing.)
- **§4.** Why the three lines suggested in the brief stop. Each is stated precisely, with a counter-example to the "obvious next step" where I have one (a Cantor-gap cancellation).
- **§5.** The open questions, stated precisely.

Conventions are those of the brief: ν is a smooth positive density, d = div_ν X, J_t is the log ν-Jacobian, "L1" means ker(X on D') = constants, "Lemma 2" is the C^k a priori estimate of Text B, and (O2) is as in the background.

---

## 1. A finite-regularity form of GH (no volume needed)

For m ≥ 0 let Inv_m be the set of T in (C^m)' with T(Xv) = 0 for all v in C^∞. These are the X-invariant distribution densities of order ≤ m.

**Proposition 1.** Assume GH. For every k there are m and C with the following property. Let f be in C^m with T(f) = 0 for all T in Inv_m. Then there is u in C^k with ∫u dν = 0, Xu = f, and ||u||_{C^k} ≤ C||f||_{C^m}. In particular u(g_t x) − u(x) = ∫_0^t f(g_s x) ds for all x and t.

*Proof.*
1. Take m and C from Lemma 2 (Text B) for this k. Let E be the closure of X(C^∞) in the Banach space C^m.
2. By Hahn–Banach in C^m, E is the set of f in C^m annihilated by every T in (C^m)' that vanishes on X(C^∞). That set of T is exactly Inv_m. So f lies in E.
3. Write f = lim Xv_n in C^m, with v_n smooth and of ν-mean 0. By Lemma 2, ||v_n − v_p||_{C^k} ≤ C||Xv_n − Xv_p||_{C^m}. So (v_n) is Cauchy in C^k and converges to some u in C^k with ||u||_{C^k} ≤ C||f||_{C^m}.
4. Xv_n → Xu in D' and Xv_n → f in C^0. Hence Xu = f.
5. For k ≥ 1, u is C^1, and d/dt u(g_t x) = (Xu)(g_t x) = f(g_t x). ∎

---

## 2. The case of a smooth invariant volume

**Standing assumption in §2–3.** X is GH, dim M ≥ 2, and X preserves a smooth positive probability density ω, i.e. (V) holds.

Recall (O2): the invariant distribution densities are exactly the multiples cω. Hence:
- the flow is uniquely ergodic and minimal;
- it has no zeros and no periodic orbits;
- by the duality consequence in Text A, X(C^∞) = {f in C^∞ : ω(f) = 0};
- Inv_m = R·ω for every m.

**Proposition 2.** Under (V)+GH there are m and C such that the following hold.

(a) **Lipschitz transfer.** Every f in C^m can be written f = ω(f) + Xu_f, with u_f in C^1, ω(u_f) = 0, and ||u_f||_{C^1} ≤ C||f||_{C^m}. The map f ↦ u_f is linear.

(b) **Endpoint rigidity.** Put S_T f(x) = ∫_0^T f(g_s x) ds. For all f in C^m, all x, y in M and all real T,
 |S_T f(x) − S_T f(y)| ≤ C||f||_{C^m} (d(x,y) + d(g_T x, g_T y)).
 Equivalently, the occupation measures m_x^T = ∫_0^T δ_{g_s x} ds satisfy
 ||m_x^T − m_y^T||_{(C^m)'} ≤ C(d(x,y) + d(g_T x, g_T y)), uniformly in T.
 In particular:
 - if d(g_T x, x) < η, then ||m_x^T − Tω||_{(C^m)'} ≤ Cη;
 - for every T, the set {m_x^T : x in M} can be covered by (C'/ε)^{2n} balls of radius ε in (C^m)'. This bound does not depend on T.

(c) **Infinitesimal form.** For x in M, a vector e in T_xM, real T, and f in C^m:
 ∫_0^T df_{g_s x}(Dg_s e) ds = du_f(Dg_T e) − du_f(e).
 Hence |∫_0^T df(Dg_s e) ds| ≤ C||f||_{C^m}(|e| + |Dg_T e|). Suppose moreover |Dg_s e| → 0 as s → −∞ and ∫_{−∞}^0 |Dg_s e| ds < ∞ (for example, e a Pesin unstable vector). Then
 du_f(e) = ∫_{−∞}^0 df_{g_s x}(Dg_s e) ds,
 and this functional of f has norm ≤ C|e| on C^m, uniformly in x.

(d) **Spectral flatness at 0.** Let σ_f be the spectral measure of f in C^∞ with ω(f) = 0, for the unitary Koopman group U_t f = f∘g_t on L^2(ω). Then ∫ λ^{−2j} dσ_f(λ) < ∞ for every j ≥ 1. Hence σ_f([−ε, ε]) ≤ C_j(f) ε^{2j} for all j. Also sup_T ||S_T f||_{L^2(ω)} < ∞, so the asymptotic variance lim (1/T) Var_ω(S_T f) is 0.

(e) **Asymptotic pairs.** Suppose d(g_t x, g_t y) → 0 as t → +∞. Then for f in C^m, lim_{T→∞} ∫_0^T (f(g_s x) − f(g_s y)) ds exists and equals u_f(y) − u_f(x). Its absolute value is ≤ C||f||_{C^m} d(x,y). If the pair is asymptotic as t → +∞ and as t → −∞, then
 lim_{T,T'→∞} ∫_{−T'}^{T} (f(g_s x) − f(g_s y)) ds = 0 for every f in C^m.

*Proof.*
(a) By Proposition 1 with k = 1, using Inv_m = Rω, applied to f − ω(f). Note ||f − ω(f)||_{C^m} ≤ 2||f||_{C^m}.

(b) From (a), S_T f(x) = Tω(f) + u_f(g_T x) − u_f(x). Subtract the same identity at y; the term Tω(f) cancels. Then use Lip(u_f) ≤ ||u_f||_{C^1}.
- For the first bullet take y = x and compare with Tω, i.e. use S_T f(x) − Tω(f) = u_f(g_T x) − u_f(x).
- For the covering bound: m_x^T − Tω is the image of the pair (x, g_T x) under the map (p, q) ↦ [f ↦ u_f(q) − u_f(p)]. This map is C-Lipschitz from M×M to (C^m)'. Since M×M has dimension 2n, it can be covered by (C''/ε)^{2n} balls of radius ε/C.

(c) Differentiate the identity S_T f = Tω(f) + u_f∘g_T − u_f in the direction e, using that u_f is C^1. For the second statement: the function s ↦ d(u_f∘g_s)_x(e) = du_f(Dg_s e) has derivative df_{g_s x}(Dg_s e), because d/ds (u_f∘g_s) = (Xu_f)∘g_s = (f − ω(f))∘g_s. Integrate over [−R, 0]. The boundary term du_f(Dg_{−R} e) tends to 0 because |du_f| ≤ C||f||_{C^m} and Dg_{−R} e → 0.

(d)
1. C^∞ is a core for the generator of (U_t): it is U_t-invariant and dense. On C^∞ the generator is X, and X is skew-symmetric because L_X ω = 0.
2. Iterate (a): with u_0 = f and u_j = X^{−1}u_{j−1}, we get smooth mean-zero u_j with X^j u_j = f.
3. By the spectral theorem, σ_f = λ^{2j} σ_{u_j}. Hence ∫ λ^{−2j} dσ_f ≤ ||u_j||^2_{L^2}.
4. S_T f = u_1∘g_T − u_1, so ||S_T f||_{L^2} ≤ 2||u_1||_{L^2}.

(e) This is (b) with the limit taken: u_f(g_T x) − u_f(g_T y) → 0 by uniform continuity of u_f. In the two-sided case, add the forward and backward identities; the u_f(x) − u_f(y) terms cancel. ∎

**Remark 2.1 (what (b)–(e) would need to contradict positive entropy).** Each item is the statement "u_f exists with uniform bounds" in disguise. A contradiction needs one of the following.
- An f in C^m and orbit segments with arbitrarily close endpoints whose occupation measures differ by a fixed amount when tested on f.
- An f whose spectral measure does not vanish to infinite order at 0. A smooth observable with nondegenerate CLT variance would do.
- A bi-asymptotic pair (or su-cycle) whose cycle functional is not identically 0 on C^m.

In the uniformly or non-uniformly *hyperbolic* case such objects come from periodic or homoclinic structure, but under (V) that case is already excluded (§3). In the non-hyperbolic case I can produce none of them; see §4.3 for why the obvious "bump function" argument for (e) does not work.

---

## 3. (PE) in the volume case: reduction to the exponents of ω

**Proposition 3.** Assume (V)+GH and dim M ≥ 2. Then the following are equivalent:
 (i) h_top(g_1) = 0;
 (ii) h_ω(g_1) = 0;
 (iii) all Lyapunov exponents of ω for g_1 are 0;
 (iv) λ* := lim_t (1/t) log max_x ||Dg_t(x)|| = 0;
 (v) lim_t (1/t) log ∫ ||Λ Dg_t|| dω = 0.

Moreover, if h_top(g_1) > 0, then ω has positive entropy, has a positive and a negative exponent, and also has a zero exponent transverse to the flow direction. This forces dim M ≥ 4.

*Proof.*
- **(i)⇔(ii).** The flow is uniquely ergodic (O2), so g_1 has the unique invariant measure ω up to the averaging in Chain step 2. The variational principle gives h_top(g_1) = h_ω(g_1).
- **(ii)⇔(iii).** By Pesin's entropy formula for the smooth measure ω (cited from memory: h_ω(f) = ∫ Σ λ_i^+ dω for C^{1+α} f and ω absolutely continuous), h_ω = 0 iff there are no positive exponents. Since ω is invariant, the sum of the exponents is 0. So "no positive exponent" is the same as "all exponents 0".
- **(iii)⇔(iv).**
  - If λ* > 0, Lemma 1 of [R5-a] gives a flow-invariant m with ∫ χ dm ≥ λ*, where χ is the pointwise top exponent. By unique ergodicity m = ω, so ω has a positive exponent.
  - Conversely, a positive exponent of ω gives max_x ||Dg_t(x)|| ≥ e^{ct} along a sequence of t. Since log max_x ||Dg_t|| is subadditive in t, the limit λ* exists and is > 0.
- **(iv)⇒(v).** ||Λ A|| ≤ max(1, ||A||)^n.
- **(v)⇒(i).** By Przytycki's inequality (cited), h_top(g_1) ≤ limsup (1/N) log ∫ ||Λ Dg_N|| dω.

**The "moreover" part.**
1. Assume h_ω > 0. Then ω has a positive exponent (Ruelle's inequality), and also a negative one, since the sum is 0.
2. The flow direction has exponent 0, because X has no zeros.
3. Suppose all exponents other than the flow direction were nonzero. Then the flow version of Katok's closing/horseshoe theorem (Lian–Young, cited as [KLY] in the background) gives a horseshoe, hence periodic orbits. But periodic orbits are excluded by (O2): the orbit measure would be an invariant measure different from ω. So some transverse exponent is 0.
4. Counting the exponents (one positive, one negative, the flow direction, and one more zero) gives dim M ≥ 4. ∎

So in case (V) the problem is exactly the following.

> **(Q-V)** A GH flow with a smooth invariant volume is cohomology-free, with the tame estimates of Prop. 2(a). Can its volume have a non-hyperbolic positive-entropy Oseledets spectrum (E^u ≠ 0, E^c ⊋ RX, E^s ≠ 0)?

---

## 4. The three suggested lines and where each one stops

### 4.1 Line 1 (Grassmannian Jacobians)

**What is proved.** Fix a linear map A of R^n and k ≤ n, and let dE be the invariant probability on the Grassmannian G_k. Then
 ∫_{G_k} |det A|_E| dE ≥ c(n,k) ||Λ^k A||.
Proof: |det A|_E| = ||Λ^k A ξ_E||, where ξ_E is a unit decomposable k-vector. Hence |det A|_E| ≥ σ_top |⟨ξ_E, ξ_top⟩|, with ξ_top the top singular k-vector. The average of |⟨ξ_E, ξ⟩| over E does not depend on the unit decomposable vector ξ, and it is positive.

So with ν̂ the smooth measure on the Grassmann bundle and j_t(x, E) = |det Dg_t(x)|_E|:
 ∫_M ||Λ^k Dg_t|| dν ≍ ∫ j_t dν̂.
This is the total mass of L_t ν̂, where L_t = exp(t(X̂ + a_k))^T and a_k(x, E) = tr(∇X|_E) is smooth.

**Where it stops.** Every GH tool in the background concerns distributions on M. The weight j_t is a cocycle on the Grassmann bundle, and the lifted field X̂ is not GH: for a linear flow on a torus, functions of the fibre variable alone are X̂-invariant. A ν-measurable object on M can be extracted only by fibre-integration. That turns j_t into ∫ j_t dν̂_x, which is not a cocycle, so no transport identity of the type in Lemma 1 of [R5-b] or Lemma 0 of [R5-c] holds for it.

The only cocycle among these weights that pushes down to M is k = n (e^{J_t}). For it, ∫ e^{J_t} dν = ν(M) exactly, and Lemma C, Lemma D, Theorem K and Lemma H already use all it gives. I found no way to make GH act on the fibre directions.

### 4.2 Line 2 (pointwise exponents)

The pointwise exponent χ_ν is ν-a.e. constant ([R5-e] Cor. 4.2). The obstruction is the following.
- In case not-(V), ν is not invariant, so no Oseledets/Pesin relation ties χ_ν to entropy. By Theorem K, if (V) fails then D((g_t)_*ν || ν) → ∞ in Cesàro mean. So ν-typical behaviour is genuinely non-stationary.
- The rate of ∫ ||Λ Dg_t|| dν is governed by sets of exponentially small ν-measure. Examples are the points that stay near a horseshoe Λ for time t; by B3 the stable set of Λ is ν-null. Lemma 4.1, Lemma T, Theorem 1 and Lemma H all concern ν-a.e. or L^1 objects. They are blind to sets whose measure tends to 0 exponentially, unless an L^1-bounded object is built from them with a nonzero limit. I could not build one: the natural candidates (normalised restrictions of ν to the sets of slow escape, pushed forward) converge, by the computation of Lemma 5.1 of [R5-d], to conformal measures carried by W^u(Λ). Those are ν-singular, and Corollary 2 of [R5-b] already says that singular eigen-objects are not excluded by these tools.
- In case (V), Line 2 is §3: χ_ν = top exponent of ω, and (PE) ⇔ χ_ν = 0. That is exactly (Q-V), which remains open.

### 4.3 Line 3 (relative entropy / cycle functionals) and the bi-asymptotic test

Under (V) the analogue of Theorem K is automatic, so the content moves to Prop. 2.

The most promising concrete use is Prop. 2(e). A bi-asymptotic pair x ≠ y on different orbits, with ∫_R d(g_s x, g_s y) ds < ∞, satisfies Π(f) := ∫_R (f(g_s x) − f(g_s y)) ds = 0 for all f in C^m. One would like to contradict this by testing f = a bump of radius r at a point p = g_{s_0}x where the two orbits are δ ≫ r apart.

**Why this does not close.** Localise to a flow box B around p. Π restricted to B is the order-1 distribution Σ_k (δ_{a_k} − δ_{b_k}) ⊗ (Lebesgue measure along the flow) on transversal × time. Here a_k and b_k are the paired passages of the two orbits through the transversal, with Σ |a_k − b_k| < ∞. The a_k and b_k are pairwise distinct. Even so, such a sum can vanish identically.

*Example.* Take the standard Cantor set K in a circle, and let (b_k, a_k) be its complementary gaps. Then Σ (f(a_k) − f(b_k)) = ∫_{circle} f' − ∫_K f' = 0 for every C^1 function f, because K has measure 0.

So the bump test only works if a "generic position" property of the passages is known. For example: for some k and a sequence r → 0, the weighted passage measure W = Σ_j |a_j − b_j| (δ_{a_j} + δ_{b_j}), with the k-th pair removed, satisfies W(B(a_k, r)) = o(r). I cannot verify this from the dynamics.

Moreover, bi-asymptotic pairs are themselves known to exist only in the hyperbolic setting, which §3 has already excluded. In the non-hyperbolic case one would need Pesin su-cycles, and with zero centre exponents there is no local product structure.

---

## 5. Open questions (precise)

1. **(PE) in general.** Under GH, is lim (1/t) log ∫ ||Λ Dg_t|| dν = 0? Open here.
2. **(Q-V).** Let X be cohomology-free with tame estimates (GH + smooth invariant volume ω, hence uniquely ergodic and minimal). Must all Lyapunov exponents of ω vanish? By Prop. 3 this is equivalent to (PE) in case (V), and only the non-hyperbolic spectrum remains to be excluded.
3. **Smooth CLT obstruction.** Let a smooth flow preserve a smooth volume ω and have h_ω > 0. Is there some f in C^∞ (or C^m) whose spectral measure does not vanish to infinite order at 0? For instance, one with lim (1/T) Var(S_T f) > 0, or one with no L^2 transfer function. A yes answer, together with Prop. 2(d), settles (Q-V). I know this only under hyperbolicity with mixing rates, and that case is already excluded.
4. **Cycle functionals.** In the setting of (Q-V), does there exist a bi-asymptotic pair or a Pesin su-cycle whose functional (Prop. 2(e)) is nonzero on C^m? This needs the generic-position property of §4.3, which the Cantor-gap example shows is not automatic.
5. **(V) itself.** Does GH imply a smooth invariant volume? This was already open (Theorem K, Lemma F). In case not-(V), none of the above applies, and the questions listed in the brief's background (E1, (H3)) remain open.

Citations from memory: Pesin's entropy formula; Ruelle's inequality; Przytycki's inequality and Kozlovski's equality; Katok's closing/horseshoe theorem and the Lian–Young flow version; the spectral theorem and core theorem for unitary groups.

=== END OF ANSWER round6_q7 ===
