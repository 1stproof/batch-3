kind: writeup
Task: complete, fully rigorous proofs of the deterministic flow and transport lemmas on which an upper-bound proof for this problem rests (the proof is otherwise complete; these lemmas were written tersely). The excerpt below (Sections 0-3 of that proof, verbatim) defines the estimator and states Lemmas 1-3 with short proofs. Please:
1. Lemma 1: prove the field bounds with the correct exponents. Since V^E = grad Eu is in C^alpha (Hölder-Zygmund) with norm <= C, show ||D^m V_J||_inf <= C J 2^{J(m-alpha)_+} for m = 2, 3 (the excerpt states the weaker exponent (m+1-alpha)_+, but later uses ||D div V_J||_inf <= C J 2^{J(2-alpha)_+} and ||D^2 div V_J||_inf <= C J 2^{J(3-alpha)_+}); say exactly when the factor J is needed. Also prove ||V_J - x/d||_{C^1(D)} <= eps for r <= r_0, J >= J_0, and the same for V_hat on the event A.
2. Lemma 2: give full proofs of items 1-6 (existence and uniqueness of the zero, forward invariance of D under the backward flow, the radial rate bounds, ||DPhi_{-s}|| <= e^{-(1/d - eps)s}, the weight bound).
3. Lemma 3: prove (a) (uniqueness of C^1 solutions of div(gX) = H via the backward-flow representation), (b), (c) (the boundary-layer gain: a backward ray spends time <= C 2^{-J} in {|x| > 1 - C 2^{-J}}), and in full detail (d) and (e): differentiability of x -> T_X^{-1}H(x) under the integral, the bound on ||D^2 Phi_{-s}|| from the variational equation, the bounds on the first and second derivatives of the weight w(s,x), and the resulting estimates ||grad T_X^{-1}H||_inf <= C(||grad H||_inf + ||H||_inf ||D div X||_inf) and ||D^2 T_X^{-1}1||_inf <= C(||D^2 div X||_inf + ||D div X||_inf^2 + ||D div X||_inf ||D^2 X||_inf), with constants uniform over fields X with ||X - x/d||_{C^1} <= eps. Track the polynomial-in-s factors against the exponential decay explicitly.
4. Derive the consequences used in Section 3: ||f_0||_inf <= 2, ||grad f_0||_inf <= C J 2^{J(2-alpha)_+}, ||D^2 f_0||_inf <= C J^2 2^{J(3-alpha)_+}.
If any statement is false as written, say so and give the corrected statement with proof. End with a list of exactly what was proved.

=== EXCERPT (Sections 0-3 of the upper-bound proof, verbatim) ===
## 0. Conventions and cited facts (C)

C^s denotes the Hölder–Zygmund space B^s_{∞∞}. Constants C, c depend only on d, α, r_0 and the fixed kernels, never on f ∈ F(α,r) or on n. Choose J := ⌊log_2 n/(2α+d+3)⌋, so that 2^J ≤ n^{1/(2α+d+3)} < 2^{J+1}. In particular n^{-1/2} ≤ 2^{-J(α+(d+3)/2)} and n^{-1} 2^{J(d+3)} ≤ 2^{-2Jα}.

Facts cited from memory:
- **(C1) Extension.** There is a linear E with Eg = g on D, bounded C^s(D) → C^s(R^d) for 0 < s ≤ S_0 (take S_0 > α+2). It has Seeley form: for |t| > 1, Eg(t) = χ(|t|) Σ_i a_i g(R_i t), where R_i t = (1 − λ_i(|t|−1)) t/|t|, λ_i > 0, and χ is a smooth cutoff equal to 0 for |t| ≥ 1 + η. Boundedness on Zygmund spaces follows from boundedness on C^k for k ≤ S_0 + 1, by real interpolation.
- **(C2) Approximation.** Let k ∈ C_c^∞ with ∫k = 1 and vanishing moments of orders 1..S, S ≥ 2α + 2, and put k_J = 2^{Jd} k(2^J·). Then for g ∈ C^s(R^d):
  - ||D^m(k_J*g − g)||_∞ ≤ C 2^{-J(s−m)} ||g||_{C^s} for 0 ≤ m < s;
  - ||D^m(k_J*g)||_∞ ≤ C J 2^{J(m−s)_+} ||g||_{C^s};
  - if ψ ∈ C_c^∞ has vanishing moments of orders 0..S, then ||ψ_J*g||_∞ ≤ C 2^{-Js} ||g||_{C^s}.
- **(C3) Taylor in Zygmund spaces.** For A ∈ C^a, a > 0: Δ_h A(x) := A(x+h) − A(x) = Σ_{1≤|γ|<a} ∂^γA(x) h^γ/γ! + r_A(x,h), with |r_A| ≤ C |h|^a (1 + log(1/|h|)) for |h| ≤ 1. The log appears only when a is an integer. C^a is an algebra for a > 0.
- **(C4) Schauder.** For f ∈ F(α,r) and r ≤ r_0: ||u_f||_{C^{α+1}} ≤ C and ||u_f − u_1||_{C^{α+1}} ≤ C r. This is the Zygmund-scale Schauder estimate for div(f∇u) = 1 with Dirichlet data on the ball, combined with (I1).
- **(C5) Gaussian facts.**
  - A centred Gaussian process y ↦ W(φ_y), with y ↦ φ_y ∈ L^2 smooth, has a smooth version with D^m W(φ_y) = W(∂^m_y φ_y).
  - Bochner integrals of continuous L^2-valued maps commute with W.
  - Dudley's entropy bound and the Borell–TIS inequality.

## 1. Estimator

Put K_J g := (k_J * Eg)|_D. On data this is K_J Y(x) = ⟨Y, k_J(x,·)⟩, with k_J(x,z) := (E^* k_J(x−·))(z), z ∈ D.

**Kernel properties.** By (C1), E^* is the identity plus finitely many weighted pullbacks under the diffeomorphisms R_i^{-1}, with bounded Jacobians. Hence:
- (K1) |∂_x^a k_J(x,z)| ≤ C 2^{J(d+|a|)} for |a| ≤ 4.
- (K2) k_J(x,z) = 0 unless |x−z| ≤ C_0 2^{-J}. Indeed, if |x − R_i^{-1}z| ≤ C2^{-J} with x ∈ D, then 1 − |z| ≤ Cλ_i 2^{-J}, so |z − R_i^{-1}z| ≤ C'2^{-J}.
- (K3) ||∂^a_x k_J(x,·)||_2^2 ≤ C 2^{J(d+2|a|)}, and x ↦ ∂^a_x k_J(x,·) is Lipschitz into L^2 with constant C 2^{J(d/2+|a|+1)}.

**Notation.**
- U := Eu, F := Ef, V := ∇u, V^E := ∇U. By (C1) and (C4), ||F||_{C^α} + ||V^E||_{C^α} ≤ C.
- V_J := ∇K_J u = (k_J * V^E)|_D, and b := K_J u − u.
- ξ := n^{-1/2} K_J W. This is a smooth Gaussian field by (C5), and it does not depend on f.
- û := K_J Y = K_J u + ξ and V̂ := ∇û = V_J + ∇ξ.

**Event.** A := {||D^m ξ||_∞ ≤ J n^{-1/2} 2^{J(d/2+m)} for m = 1, 2, 3}. On A:

  ||∇ξ||_∞ ≤ J 2^{-J(α+1/2)},  ||D^2ξ||_∞ ≤ J 2^{-J(α−1/2)},  ||D^3ξ||_∞ ≤ J 2^{-J(α−3/2)}.

**Definition of the estimator.**
- f̂ := T_{V̂}^{-1} 1 on A, and f̂ := 1 off A.
- f̃ := min(max(f̂, 1−r), 1+r).
- Since 1−r ≤ f ≤ 1+r, truncation can only decrease |f̃ − f| pointwise.

## 2. Vector-field and transport lemmas

**Lemma 1 (fields).** For r ≤ r_0 and J ≥ J_0, with ε small:
- ||V_J − x/d||_{C^1(D)} ≤ ε;
- on A also ||V̂ − x/d||_{C^1(D)} ≤ ε;
- ||D^m V_J||_∞ ≤ C J 2^{J(m+1−α)_+} for m = 2, 3.

Proof.
- ||V_J − V||_{C^1} ≤ C 2^{-J(α−1)} by (C2), and ||V − x/d||_{C^1} ≤ Cr by (C4).
- ||D^2ξ||_∞ ≤ J 2^{-J(α−1/2)} on A.
- The bound on D^m V_J = D^m(k_J * V^E) is (C2). ∎

**Lemma 2 (geometry).** Let X be a C^1 field on D with ||X − x/d||_{C^1} ≤ ε, ε small. Then:
1. X has exactly one zero x_X, and |x_X| ≤ 2dε.
2. With ρ(y) := |y − x_X|: (1/d − ε)ρ^2 ≤ (y − x_X)·X(y) and |X(y)| ≤ (1/d + ε)ρ.
3. The backward flow Φ_{-s} maps D into D for all s ≥ 0.
4. Along γ(s) = Φ_{-s}x, r(s) := ρ(γ(s)) satisfies −(1/d+ε)r ≤ r' ≤ −(1/d−ε)r.
5. ||DΦ_{-s}|| ≤ e^{-(1/d−ε)s}.
6. w(s) := exp(−∫_0^s div X(γ)) ≤ e^{-(1−dε)s}.

Proof.
1. The map x ↦ x − dX(x) has Lipschitz constant ≤ dε < 1 and maps B(0,1/2) into itself, so it has a fixed point there. That fixed point is a zero of X. The zero is unique by item 2.
2. Write X(y) = A(y)(y − x_X) with A := ∫_0^1 DX(x_X + t(y−x_X)) dt. D is convex, so the segment lies in D, and ||A − I/d|| ≤ ε.
3. On the sphere, d/ds |γ|^2 = −2γ·X(γ) ≤ −2(1/d − ε) < 0.
4. This follows from item 2.
5. We have d/ds DΦ_{-s} = −DX(γ) DΦ_{-s}, and DX ≥ (1/d − ε)I in the symmetric sense up to ε.
6. div X ≥ 1 − dε. ∎

**Lemma 3 (transport inverse).** Under the hypotheses of Lemma 2, put T_X g := div(gX) and T_X^{-1}H(x) := ∫_0^∞ H(Φ_{-s}x) w(s) ds for H ∈ C(D).
- (a) If g ∈ C^1(D) and T_X g = H, then g = T_X^{-1}H.
- (b) ||T_X^{-1}H||_∞ ≤ 2||H||_∞.
- (c) If supp H ⊂ {|x| > 1 − C2^{-J}}, then ||T_X^{-1}H||_∞ ≤ C 2^{-J} ||H||_∞.
- (d) If X ∈ C^2 and H ∈ C^1, then T_X^{-1}H ∈ C^1 and ||∇T_X^{-1}H||_∞ ≤ C(||∇H||_∞ + ||H||_∞ ||D div X||_∞).
- (e) If X ∈ C^3, then ||D^2 T_X^{-1}1||_∞ ≤ C(||D^2 div X|| + ||D div X||^2 + ||D div X|| ||D^2X||). Similarly, ||∇T_X^{-1}1||_∞ ≤ C ||D div X||_∞.

Proof.
- (a) We have d/ds [g(γ(s)) w(s)] = −(X·∇g + g div X)(γ) w = −H(γ) w. Integrate over [0,S] and let S → ∞, using that g is bounded and w → 0.
- (b) Immediate from Lemma 2.6.
- (c) On |γ| ≥ 1/2 we have d/ds |γ|^2 ≤ −c. So the backward ray spends time ≤ C2^{-J} in the layer.
- (d), (e) Differentiate under the integral. We have |∂ w(s)| ≤ w(s) ∫_0^s ||D div X|| ||DΦ_{-σ}|| dσ ≤ C ||D div X|| w(s). The flow satisfies ||DΦ_{-s}|| ≤ e^{-cs} and ||D^2Φ_{-s}|| ≤ C||D^2X||: the variational equation d/ds D^2Φ = −DX D^2Φ − D^2X(DΦ, DΦ) has contracting linear part. The second derivative of w is bounded by w(s)(1+s)^2 times the stated products. Everything is integrable against e^{-(1−dε)s}. ∎

## 3. Exact decomposition

Let f_0 := T_{V_J}^{-1} 1. By Lemma 1 and Lemma 3(d,e), using ||D^m div V_J|| ≤ ||D^{m+1}V_J||:
- ||f_0||_∞ ≤ 2;
- ||∇f_0||_∞ ≤ C J 2^{J(2−α)_+};
- ||D^2 f_0||_∞ ≤ C J^2 2^{J(3−α)_+}.

Here (2(2−α))_+ ≤ (3−α)_+ because α ≥ 1. f_0 is smooth.

Define the variance term

  Z := T_{V_J}^{-1} div(f_0 ∇ξ).

Z is defined for every ω because V_J is deterministic, and Z ∈ C^1 by Lemma 3(d).

**Identity.** On A:

  f̂ − f = (f_0 − f) − Z + T_{V̂}^{-1} div(Z∇ξ).    (★)

Proof.
1. Since f̂ = T_{V̂}^{-1}1 and f_0 is C^1, Lemma 3(a) is not even needed for the following. We have T_{V̂}(f̂ − f_0) = 1 − div(f_0 V_J) − div(f_0 ∇ξ) = −div(f_0∇ξ).
2. Also T_{V̂} Z = T_{V_J} Z + div(Z∇ξ) = div(f_0∇ξ) + div(Z∇ξ).
3. Hence T_{V̂}(f̂ − f_0 + Z) = div(Z∇ξ). The left side is applied to a C^1 function, so Lemma 3(a) gives f̂ − f_0 + Z = T_{V̂}^{-1} div(Z∇ξ). ∎

