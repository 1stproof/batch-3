# round11_q9 — answer

## 0. Plan and statement attempted

**Target (ledger entry 68).** Assume X is GH on the compact connected manifold M. Fix a smooth positive density nu, put d = div_nu X and J_t(x) = int_0^t d(g_s x) ds. Let mu be a g_1-invariant, g_1-ergodic Borel probability with h_mu(g_1) > 0, and put lambda := mu(J_1) (this equals mu(d) when mu is flow-invariant). Claim: lambda = 0.

**Route.** This is the vanishing-moment argument of Prop. 6.2 (R6-a), done in full for unstable manifolds of any dimension. The plan:
- Cite precisely one normal-form theorem [NF] (Kalinin–Sadovskaya). It gives polynomial transition maps of bounded degree along Pesin unstable manifolds.
- Replace every "tempered bound" by a **good-times device**. All C^K estimates are made only at times n' when the backward orbit lies in a fixed Lusin set G_L, where the bounds are uniform. The gaps between such times are o(n) by Birkhoff. Polynomial maps of bounded degree are then controlled by their sup norm (equivalence of norms on a finite-dimensional space). From [NF] this needs only measurability, not temperedness.
- The same device proves that the Jacobian-holonomy function beta is C^inf along unstable leaves.
- Theorem J (R6-a §2) then gives the contradiction.

**Result.** lambda < 0 is impossible, and by applying it to -X so is lambda > 0. This is proved modulo the cited theorems [P] (Pesin), [LS] (Ledrappier–Strelcyn) and [NF] (non-stationary normal forms). The case lambda = 0 is not touched; it is (AP) at lambda = 0 and remains open.

## 1. Tools used

**Theorem J (R6-a §2; I re-checked steps 1–5 of its proof and they are correct).** Assume GH. Suppose S is a distribution density for which there are eps > 0, k and C with
|S(e^{J_t} phi∘g_t)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and all smooth phi.
Then S = 0.

**Notation.** f := g_1, a C^inf diffeomorphism. mu is f-ergodic with h_mu(f) > 0.
- By Ruelle's inequality mu has positive exponents. Let chi_1 > ... > chi_l > 0 be the distinct positive exponents, u the dimension of E^u, and d_0 := floor(chi_1/chi_l).
- Write x_n := f^{-n}x, and x_t := g_t x for real t.
- By Birkhoff (applied to f and f^{-1} with the function J_1, plus |J_t - J_{[t]}| <= ||d||_inf), J_t(x)/t -> lambda as t -> +inf and as t -> -inf, for a.e. x.

**[P] Pesin unstable manifolds (cited, standard).** For mu-a.e. x:
- W^u(x) = {y : limsup_n (1/n) log d(f^{-n}y, f^{-n}x) < 0} is an injectively immersed C^inf submanifold tangent at x to E^u_x (the sum of the Oseledets spaces of the positive exponents).
- f^{-1}W^u(x) = W^u(x_1).
- [P2] For every compact set Q ⊂ W^u(x) (compact in the intrinsic topology) and every delta > 0 there is C = C(x, Q, delta) with d^u(f^{-n}y, x_n) <= C e^{-(chi_l - delta)n} for all y in Q and n >= 0. Here d^u is the intrinsic leaf distance.

**[LS] Ledrappier–Strelcyn (cited).** There is a measurable partition xi subordinate to W^u, with xi(x) ⊂ W^u(x), such that h_mu(f) = H_mu(xi | f xi). Together with **Lemma 6.0** (R6-a; proof re-checked), h_mu(f) > 0 implies that the conditional measures mu^xi_x are non-atomic for a.e. x.

**[NF] Non-stationary normal forms on unstable manifolds (cited from memory).** Sources: Kalinin–Sadovskaya, "Normal forms for non-uniform contractions", J. Mod. Dyn. 11 (2017); Melnick, ETDS 2019, applied to f^{-1} restricted to W^u. The statement I use: there is a full-measure set on which, for each x, there is a C^inf diffeomorphism H_x : W^u(x) -> E^u_x with the following properties.
- (a) H_x(x) = 0 and D_x H_x = Id.
- (b) P_x := H_{x_1}∘f^{-1}∘H_x^{-1} : E^u_x -> E^u_{x_1} is a *sub-resonance polynomial map*. With respect to the Lyapunov splittings E^u = ⊕_j E_j, the E_i-component of P_x is a polynomial in which only monomials prod_j (coords in E_j)^{s_j} with sum_j s_j chi_j <= chi_i occur.
- (c) x -> H_x is measurable: for each K and r, the norms used in §2 below (C^{K+1} norms of H_x^{-1} on balls, Lipschitz constants of H_x on intrinsic balls) are measurable functions of x.

A global H_x also follows from a local one. If H^loc_x is defined on W^u_loc(x), put H_x := (P^{(n)})^{-1}∘H^loc_{x_n}∘f^{-n} on f^n(W^u_loc(x_n)). Here P^{(n)} is the composition of the local polynomial maps defined below, and the definitions agree on overlaps.

**Lemma 1.1 (closure and degree bound; proved).** For n >= 0 put P^{(n)}_x := P_{x_{n-1}}∘...∘P_x. Then H_{x_n}∘f^{-n} = P^{(n)}_x∘H_x on W^u(x), and P^{(n)}_x is a sub-resonance polynomial map of degree <= d_0.

*Proof.* The conjugacy follows by induction from (b). Give each coordinate of E_j the weight chi_j. A map is sub-resonance iff its E_i-component contains only monomials of weight <= chi_i. Let Q and P both be sub-resonance. Substituting P into a monomial of the E_i-component of Q of weight sum s_j chi_j <= chi_i replaces each E_j-coordinate by a polynomial whose monomials have weight <= chi_j. Weights add under multiplication, so every monomial obtained has weight <= chi_i. So the composition is sub-resonance. The exponents chi_j are the same for every fibre (mu is ergodic), so this applies to maps between different fibres. Degree: every weight is >= chi_l, so a monomial of total degree |s| allowed in some component has |s| chi_l <= chi_i <= chi_1, i.e. |s| <= d_0. ∎

**Lemma 1.2 (Markov-type bound; elementary).** Fix r_0 > 0. There are constants M_j = M_j(u, d_0, r_0) such that every polynomial map Q : E -> E' (Euclidean spaces of dimension u) of degree <= d_0 satisfies ||Q||_{C^j(B(0,r_0))} <= M_j sup_{B(0,r_0)} |Q|.

*Proof.* Both sides are norms on the finite-dimensional space of such maps (use orthonormal coordinates), and all norms on a finite-dimensional space are equivalent. ∎

**Lemma 1.3 (good times; elementary).** Let G be a measurable set with mu(G) > 0 and let delta > 0. For a.e. x there is C(x) such that for every real T >= 0 there is an integer n' >= T with x_{n'} in G and n' - T <= delta T + C(x).

*Proof.* By Birkhoff for f^{-1}, N(m) := #{0 <= j < m : x_j ∈ G} = m mu(G) + o(m). Suppose some interval [T, (1+delta)T] with T large contains no integer j with x_j ∈ G. Then N((1+delta)T) = N(T) + O(1). This contradicts (1+delta)T mu(G) + o(T) versus T mu(G) + o(T). ∎

## 2. The Jacobian holonomy beta is smooth along W^u

For w in M and z with d(g_s z, g_s w) -> 0 exponentially as s -> -inf, put
beta_w(z) := int_{-inf}^0 (d(g_s z) - d(g_s w)) ds
(absolutely convergent since d is Lipschitz). Directly from the definition:

(2.1) beta_{g_s w}(g_s z) = beta_w(z) + J_s(z) - J_s(w) for real s.

(2.2) beta_w(z) = sum_{n>=0} [b(f^{-n}z) - b(f^{-n}w)], where b := int_{-1}^0 d∘g_s ds is in C^inf(M).

Fix an integer K >= 1, and embed M in R^N, so that C^{K+1} norms of maps into M make sense. For an integer L >= 1, let G'_L be the set of points w in the full-measure set of [P] and [NF] such that:
- (G1) |H_w(y)| <= L d^u(y, w) for all y in W^u(w) with d^u(y, w) <= 1/L;
- (G2) ||H_w^{-1}||_{C^{K+1}(B(0,1/L))} <= L.

Every w in the full-measure set lies in G'_L for L large: H_w is a C^inf diffeomorphism with H_w(w) = 0. By [NF](c), G'_L is measurable, so mu(G'_L) > 0 for L large. Fix such an L.

**Lemma 2.1.** For a.e. w, beta_w∘H_w^{-1} is C^{K+1} on a neighbourhood of 0 in E^u_w. (K is arbitrary, so in fact beta_w is C^inf along W^u(w) near w.)

*Proof.* Fix r_0 > 0, put B_w := B(0, r_0) ⊂ E^u_w and Q := H_w^{-1}(closed B_w), a compact subset of W^u(w). Fix delta > 0 with delta(c_K + 2) < chi_l, where c_K is chosen so that ||b∘f^m||_{C^{K+1}} <= C e^{c_K m} for m >= 0.
1. By Lemma 1.3 (with G = G'_L), for each n there is n' >= n with w_{n'} ∈ G'_L and n' - n <= delta n + C.
2. By [P2], d^u(f^{-n'}y, w_{n'}) <= C e^{-(chi_l - delta)n'} for y in Q. So for n' >= n_1 this is < 1/L, and (G1) and Lemma 1.1 give sup_{B_w} |P^{(n')}_w| <= L C e^{-(chi_l - delta)n'}.
3. By Lemma 1.2, ||P^{(n')}_w||_{C^{K+1}(B_w)} <= C' e^{-(chi_l-delta)n'}.
4. By Lemma 1.1, H_{w_n}^{-1}∘P^{(n)}_w = f^{n'-n}∘H_{w_{n'}}^{-1}∘P^{(n')}_w. (Indeed P^{(n')} = P^{(n'-n)}_{w_n}∘P^{(n)}, and f^{-(n'-n)}∘H_{w_n}^{-1} = H_{w_{n'}}^{-1}∘P^{(n'-n)}_{w_n}.) Hence on B_w
 T_n(z) := b(f^{-n}H_w^{-1}z) - b(w_n) = Phi_n(P^{(n')}_w z) - Phi_n(0), with Phi_n := b∘f^{n'-n}∘H_{w_{n'}}^{-1}.
 By (G2) and the chain rule, ||Phi_n||_{C^{K+1}(B(0,1/L))} <= C L^{K+1} e^{c_K(n'-n)} <= C'' e^{c_K delta n}.
5. Faà di Bruno: every derivative of order 1..K+1 of Phi∘P is a sum of terms D^iPhi(P)·(product of i derivatives of P of order >= 1). Also |Phi(Pz) - Phi(0)| <= ||DPhi|| |Pz|. Together with step 3 (whose bound is <= 1 for large n'), this gives
 ||T_n||_{C^{K+1}(B_w)} <= C e^{c_K delta n} e^{-(chi_l - delta)n} for n >= n_1.
 This is summable by the choice of delta.
6. The finitely many terms with n < n_1 are C^inf on B_w, since f^{-n}∘H_w^{-1} is a smooth map into M.
By (2.2), beta_w∘H_w^{-1} = sum_n T_n converges in C^{K+1}(B_w). ∎

Now let G_L ⊂ G'_L be the set where, in addition,
- (G3) ||beta_w∘H_w^{-1}||_{C^{K+1}(B(0,1/L))} <= L.

By Lemma 2.1 and [NF](c) (measurability of the series), mu(G_L) > 0 for L large. Fix such an L.

## 3. Theorem (entry 68): lambda != 0 is impossible

**Theorem 3.1.** Assume GH. Let mu be an f-ergodic invariant probability (f = g_1) with h_mu(f) > 0 and lambda = mu(J_1). Then lambda = 0. This is proved modulo [P], [LS] and [NF].

*Proof for lambda < 0.*

**Choice of constants.**
- Choose K with (K+1)chi_l > |lambda| + 1.
- Let c'_K be such that, for s >= 0, ||J_s||_{C^{K+1}} and ||phi∘g_s||_{C^{K+1}}/||phi||_{C^{K+1}} are both <= C e^{c'_K s}.
- Choose delta > 0 so small that all of the following hold:
 - lambda + delta < 0;
 - delta(c_K + 2) < chi_l;
 - (K+1)(chi_l - delta) - |lambda| - delta - delta(c''_K) >= 1/2, where c''_K := (K+2)c'_K + 2||d||_inf (see step 4).
- Then fix L with mu(G_L) > 0, where G_L is defined with this K.

**Step 1 (base point and points).** Take x in the full-measure set where all of the following hold:
- [P], [NF] and Lemma 2.1 hold at x;
- J_t(x)/t -> lambda as t -> -inf;
- Lemma 1.3 holds for G = G_L;
- mu^xi_x is non-atomic (Lemma 6.0) and gives full measure to G_fwd := {y : J_t(y)/t -> lambda as t -> +inf}.

The last condition holds a.e. because mu(G_fwd) = 1 and conditionals of a full-measure set are full a.e.

Let D := K d_0, and let N_D be the dimension of the space of real polynomials of degree <= D on E^u_x. A non-atomic probability gives zero mass to every finite set, so xi(x) ∩ G_fwd is infinite. Choose N_D + 1 distinct points y_0, ..., y_{N_D} in xi(x) ∩ G_fwd ⊂ W^u(x), and put z_i := H_x(y_i). The z_i are distinct because H_x is injective.

**Step 2 (moments, and S).** The homogeneous linear system sum_i w_i Q(z_i) = 0, for Q in a basis of the polynomials of degree <= D, has N_D equations and N_D + 1 unknowns. So it has a solution w ≠ 0. Put
S := sum_i w_i e^{beta_x(y_i)} delta_{y_i}.
Then S ≠ 0: the y_i are distinct and some w_i ≠ 0. (This is item (4) of the task.) Write F_phi(t) := S(e^{J_t} phi∘g_t).

**Step 3 (forward estimate).** Each y_i lies in G_fwd, so J_t(y_i) <= C_i + (lambda + delta)t for t >= 0. Hence
|F_phi(t)| <= C e^{(lambda+delta)t} ||phi||_inf for t >= 0.

**Step 4 (backward estimate; items (1)–(3) of the task).** Let t <= 0. By Lemma 1.3, choose an integer n' >= |t| with x_{n'} ∈ G_L and s := n' - |t| ∈ [0, delta|t| + C]. Then g_t = g_s∘f^{-n'}. Put y_i' := f^{-n'}y_i ∈ W^u(x_{n'}).
- **Reduction to one leaf.** Using beta_x(y) + J_t(y) - J_t(x) = beta_{x_t}(g_t y) and (2.1),
 F_phi(t) = e^{J_t(x)} sum_i w_i Psi(y_i'),
 where Psi(y) := exp(beta_{x_{n'}}(y) + J_s(y) - J_s(x_{n'})) phi(g_s y) on W^u(x_{n'}).
- **The function in the chart.** Put Theta := Psi∘H_{x_{n'}}^{-1} on B(0,1/L). By (G2), (G3), |J_s| <= s||d||_inf, ||e^a||_{C^{K+1}} <= e^{sup|a|} C_K (1 + ||a||_{C^{K+1}})^{K+1} and the product rule,
 ||Theta||_{C^{K+1}(B(0,1/L))} <= C(L,K) e^{c''_K s} ||phi||_{C^{K+1}}.
- **The points in the chart.** zeta_i := H_{x_{n'}}(y_i') = P^{(n')}_x z_i, by Lemma 1.1. By [P2] (Q = {y_i}) and (G1), |zeta_i| <= L C e^{-(chi_l-delta)n'} for n' >= n_1. These points then lie in B(0,1/L).
- **Taylor and moments.** Write Theta = T_K Theta + R, with T_K Theta the Taylor polynomial of degree K at 0 and |R(zeta)| <= C_K ||Theta||_{C^{K+1}} |zeta|^{K+1}. The function (T_K Theta)∘P^{(n')}_x is a polynomial on E^u_x of degree <= K d_0 = D (Lemma 1.1). So sum_i w_i (T_K Theta)(zeta_i) = 0 by Step 2, and
 |sum_i w_i Psi(y_i')| = |sum_i w_i R(zeta_i)| <= C e^{c''_K s} e^{-(K+1)(chi_l - delta)n'} ||phi||_{C^{K+1}}.
- **The base weight.** J_t(x) <= C + (|lambda| + delta)|t|, since x is backward generic and lambda < 0.
- **Conclusion for t <= -n_1.** Since n' >= |t| and s <= delta|t| + C,
 |F_phi(t)| <= C exp([|lambda| + delta + c''_K delta - (K+1)(chi_l - delta)]|t|) ||phi||_{C^{K+1}} <= C e^{-|t|/2} ||phi||_{C^{K+1}}.
- **Bounded times.** For -n_1 < t <= 0, |F_phi(t)| <= C ||phi||_inf trivially.

**Step 5.** By Steps 3 and 4, S satisfies the hypothesis of Theorem J with k = K+1 and eps = min(|lambda + delta|, 1/2). So S = 0, which contradicts Step 2.

*Case lambda > 0.* -X is GH by (O4), and its time-1 map is g_{-1} = f^{-1}. mu is f^{-1}-ergodic with the same entropy. Since div_nu(-X) = -d, the log-Jacobian of -X is J^{-X}_t = J_{-t}, so its lambda equals -lambda < 0. The case already proved, applied to -X, gives a contradiction. ∎

**Corollary 3.2.** Assume GH. Every flow-ergodic invariant mu with h_mu(g_1) > 0 has mu(d) = 0, modulo [P], [LS] and [NF].

*Proof.* Take a g_1-ergodic component mu_0 of mu. Then mu = int_0^1 (g_s)_* mu_0 ds, so mu_0(J_1) = int_0^1 mu_0(d∘g_s) ds = mu(d), and h_{mu_0}(g_1) = h_mu(g_1) > 0. Apply Theorem 3.1 to mu_0. ∎

Consequence for the chain: (AP) is needed only for lambda = 0, exactly as entry 68 predicted.

## 4. Status: what is proved, what is cited, what is open

**Proved here, given the cited theorems:**
- Theorem 3.1 and Corollary 3.2 (entry 68).
- Lemma 1.1 (sub-resonance maps are closed under composition, degree <= d_0).
- Lemma 1.2 (polynomials of bounded degree are controlled by their sup norm).
- Lemma 1.3 (good times have o(n) gaps).
- Lemma 2.1 (beta is smooth along unstable leaves).

The four gaps listed in the task are handled as follows:
- (1) The normal-form input is stated exactly as [NF]. Only measurability of the charts is used; tempered bounds are not needed, thanks to the good-times device.
- (2) The points are chosen by Lemma 6.0 and [LS].
- (3) The backward estimate, including the Jacobian weights, is Step 4. The weights are carried by beta, which is smooth by Lemma 2.1.
- (4) Non-vanishing of S is Step 2.

**Cited, not re-proved:**
- [P]: Pesin's unstable manifold theorem, including the compact-uniform intrinsic contraction [P2].
- [LS]: the Ledrappier–Strelcyn subordinate partition and the entropy formula.
- [NF]: the Kalinin–Sadovskaya / Melnick non-stationary normal forms on Pesin unstable manifolds, including measurable dependence.
- Ruelle's inequality and Birkhoff's ergodic theorem.

[NF] is the one citation whose exact hypotheses I could not re-check from memory. As I recall it, it needs smoothness C^r with r large relative to chi_1/chi_l; C^inf suffices. If [NF] is available only for one-dimensional unstable manifolds, or only for u = 1 (where affine parameters are classical), the proof above is complete in that case without change: then d_0 = 1 and the polynomials are affine.

**Open:**
- (AP) at lambda = 0, i.e. (PE0): under GH, exclude an ergodic, non-hyperbolic mu with h_mu > 0 and mu(d) = 0.
- Hence the problem itself remains open in dimension >= 4 along this line.
- The method above cannot reach lambda = 0. Forward decay came for free from lambda < 0, and at lambda = 0 neither time direction gives decay.

=== END OF ANSWER round11_q9 ===
