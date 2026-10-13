# round3_q1: upper bound n^{-2α/(2α+d+3)} (log n)^4

**Answer.** The minimax rate is n^{-2α/(2α+d+3)}, up to log factors. The lower bound was proved in round 1 and is not redone here. This file proves the matching upper bound, with log power K ≤ 4 (K = 0 for non-integer α). The proof is fully argued except for standard function-space facts, which I cite from memory (list C below).

I changed the planner's decomposition in one place. I linearise around f_0 := T_{V_J}^{-1}1, which is smooth, instead of around f. This removes every need for a bound on ∇(f_0 − f) (the bias file's sketched Step 2). It also removes every need for ∇Z with Z built from f, which is not C^1 when α < 2. The remainder is then controlled by crude sup-norm bounds, and these suffice for every α > 1.

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

## 4. Bias: ||f_0 − f||_{L^∞(D)} ≤ C J 2^{-Jα}

**Exact identity for the bias.** Since f ∈ C^1 and div(f∇u) = 1 with u ∈ C^2:

  T_{V_J}(f_0 − f) = 1 − div(fV_J) = −div(f∇b).

So f_0 − f = −T_{V_J}^{-1} div(f∇b) by Lemma 3(a).

**Decomposition of div(f∇b).** On D, where F = f:
1. f ∇K_J u = F (k_J * V^E) = k_J*(FV^E) + gV^E + R, where
   - g := F − k_J*F,
   - R(x) := −∫ k_J(−h) Δ_hF(x) Δ_hV^E(x) dh.
2. Also div(k_J*(FV^E)) = k_J*(1 + G) = 1 + k_J*G, where G := div(FV^E) − 1. Here G ∈ C^{α−1}(R^d) with norm ≤ C by (C3), and G = 0 on D.
3. Therefore div(f∇b) = div(gV) + div R + k_J*G on D.

**(i) The term div(gV).**
- We have V = V_J − ∇b, so div(gV) = T_{V_J} g − div(g∇b). Hence T^{-1}div(gV) = g − T^{-1}div(g∇b), by Lemma 3(a) since g ∈ C^1.
- The ingredients satisfy ||g||_∞ ≤ C2^{-Jα}, ||∇g||_∞ ≤ C2^{-J(α−1)}, ||∇b||_∞ ≤ C2^{-Jα} and ||D^2b||_∞ ≤ C2^{-J(α−1)}.
- So this contribution is ≤ C2^{-Jα} + C2^{-J(2α−1)}.

**(ii) The term div R.**
- R(x) = −∫k_J(−h) Δ_hF(x) Δ_hV^E(x) dh. So ∂_x R = −∫ k_J(−h)[Δ_h∂F · Δ_hV^E + Δ_hF · Δ_h∂V^E] dh.
- Each bracket is Δ_hA · Δ_hB with (a,b) = (α−1, α) or (α, α−1), and A, B have C^a, C^b norms ≤ C.
- By (C3), the product is a polynomial in h whose monomials all have degree ≥ 2, plus a remainder ≤ C|h|^{min(1+a, 1+b, a+b)} (1 + log(1/|h|))^2. Here min(1+a, 1+b, a+b) = α.
- The polynomial terms integrate to zero against k_J(−h) by the vanishing moments (orders 2..2α+1 ≤ S).
- The remainder integrates to ≤ CJ^2 2^{-Jα}.
- So ||div R||_∞ ≤ CJ^2 2^{-Jα}, and by Lemma 3(b) the contribution is ≤ CJ^2 2^{-Jα}.
- (The J^2 is present only when a or b is an integer; otherwise there is no log.)

**(iii) The term k_J*G.**
- Since G = 0 on D, for x ∈ D we have k_J*G(x) = k_J*G(x) − G(x). By (C2), its size is ≤ C2^{-J(α−1)}.
- It vanishes when dist(x, ∂D) > C2^{-J}.
- Lemma 3(c) then gives a contribution ≤ C 2^{-J} 2^{-J(α−1)} = C2^{-Jα}.
- This replaces the bias file's claim about the vanishing order of G at the sphere, which is no longer needed.

**Total bias.** ||f_0 − f||_∞ ≤ CJ^2 2^{-Jα}, uniformly over F(α,r). This also closes item (2) of the brief.

## 5. Variance: E||Z||_2^2 ≤ C n^{-1} 2^{J(d+3)} ≤ C 2^{-2Jα}

**Representation.**
- Write D_y := f_0(y)Δ_y + ∇f_0(y)·∇_y. Then div(f_0∇ξ)(y) = n^{-1/2} W(D_y k_J(y,·)).
- By (C5), Z(x) = n^{-1/2} W(h_x) with h_x(z) = ∫_0^∞ w(s) D_y k_J(y,z)|_{y=γ_x(s)} ds, where γ_x is the backward V_J-ray from x.
- Hence E Z(x)^2 = n^{-1}||h_x||_2^2.

**Pointwise kernel bound.**
- By (K1), (K2) and ||∇f_0|| ≤ CJ2^{J(2−α)_+} ≤ 2^J (for J large, as α > 1): |D_y k_J(y,z)| ≤ C 2^{J(d+2)} 1{|y−z| ≤ δ}, with δ := C_0 2^{-J}.
- With μ_x := ∫_0^∞ w(s) δ_{γ_x(s)} ds, this gives |h_x(z)| ≤ C2^{J(d+2)} μ_x(B(z,δ)).
- Therefore ||h_x||_2^2 ≤ C 2^{2J(d+2)} ∫ μ_x(B(z,δ))^2 dz ≤ C 2^{2J(d+2)} δ^d ∫ μ_x(dy) μ_x(B(y,2δ)).

**Measure along the ray.**
- Let ρ := |· − x_J| and ρ_x := ρ(x). By Lemma 2.4, r(s) decreases strictly, and e^{-s} ≤ (r(s)/ρ_x)^{d/(1+dε)}.
- So w(s) ≤ (r/ρ_x)^β with β := d(1−dε)/(1+dε) > 1, since d ≥ 2 and ε is small.
- Changing variables s → r' = r(s), with |dr/ds| ≥ c r', gives for any φ ≥ 0:

  ∫ φ dμ_x ≤ C ∫_0^{ρ_x} φ(γ at radius r') (r'/ρ_x)^β dr'/r'.    (M)

**Mass of μ_x in a small ball.** The set of s with |γ(s) − y| ≤ 2δ has r(s) ∈ [ρ(y) − 2δ, ρ(y) + 2δ]. So by (M), m(y) := μ_x(B(y,2δ)) satisfies:
- if ρ(y) ≥ 4δ: m(y) ≤ C δ (ρ(y)/ρ_x)^β / ρ(y);
- if ρ(y) < 4δ: m(y) ≤ C min(1, (6δ/ρ_x)^β).

**Integration.** Apply (M) again to ∫ m dμ_x:
- the part with r' ≥ 4δ is ≤ C δ ρ_x^{-2β} ∫_0^{ρ_x} r'^{2β−2} dr' ≤ Cδ/ρ_x, since 2β − 1 > 0;
- the part with r' < 4δ is ≤ C min(1, (δ/ρ_x)^β)^2 ≤ C min(1, δ/ρ_x).

Hence ||h_x||_2^2 ≤ C 2^{J(d+4)} min(1, 2^{-J}/ρ_x) ≤ C 2^{J(d+3)} |x − x_J|^{-1}.

**Conclusion.** Since ∫_D |x − x_J|^{-1} dx ≤ C for d ≥ 2, Tonelli gives E||Z||_2^2 ≤ C n^{-1} 2^{J(d+3)} ≤ C 2^{-2Jα}. This is a self-contained proof of item (4) for Z. The variance file's "tube lemma" is replaced by the energy bound ∫μ(B(z,δ))^2 dz above. No ∇Z variance bound is needed.

## 6. Remainder and the bad event

**Remainder on A.** Let G_ξ := div(f_0∇ξ) = f_0Δξ + ∇f_0·∇ξ. On A, using §3 and α > 1:
- ||G_ξ||_∞ ≤ CJ2^{-J(α−1/2)} + CJ^2 2^{J(2−α)_+} 2^{-J(α+1/2)} ≤ CJ 2^{-J(α−1/2)}.
- ||∇G_ξ||_∞ ≤ C(||D^3ξ|| + ||∇f_0|| ||D^2ξ|| + ||D^2f_0|| ||∇ξ||) ≤ CJ^3 (2^{-J(α−3/2)} + 2^{-J(2α−5/2)}) ≤ CJ^3 2^{-J(α−3/2)}.
- By Lemma 3(b,d) with ||D div V_J|| ≤ CJ2^{J(2−α)_+}: ||Z||_∞ ≤ CJ2^{-J(α−1/2)} and ||∇Z||_∞ ≤ CJ^3 2^{-J(α−3/2)}.
- Hence ||div(Z∇ξ)||_∞ ≤ ||∇Z|| ||∇ξ|| + ||Z|| ||Δξ|| ≤ CJ^4 2^{-J(2α−1)}.
- By Lemma 3(b) for V̂ (Lemma 1 applies on A), ||T_{V̂}^{-1}div(Z∇ξ)||_∞ ≤ CJ^4 2^{-J(2α−1)}.
- This is o(2^{-Jα}) exactly because α > 1. This closes item (5) of the brief.

**Bad event.**
- D^mξ(x) = n^{-1/2} W(∂^m_x k_J(x,·)) has standard deviation σ_m ≤ C n^{-1/2} 2^{J(d/2+m)}, by (K3).
- Using the Lipschitz bound in (K3), Dudley's bound over D gives E sup_D |D^mξ| ≤ C σ_m √J.
- Borell–TIS then gives P(A^c) ≤ 3 exp(−cJ^2) for J ≥ J_0. This holds uniformly in f, since ξ does not depend on f.

## 7. Assembly

**THEOREM (PROVED, modulo the cited standard facts C1–C5).** Let d ≥ 2, α > 1 and r ≤ r_0(d,α). Then

  sup_{f∈F(α,r)} E||f̃ − f||_{L^2(D)}^2 ≤ C (log n)^4 n^{-2α/(2α+d+3)}.

Proof.
- On A, by (★) and |f̃ − f| ≤ |f̂ − f|:
  ||f̃ − f||_2^2 ≤ 3|D|(CJ^2 2^{-Jα})^2 + 3||Z||_2^2 + 3|D|(CJ^4 2^{-J(2α−1)})^2.
- Off A: ||f̃ − f||_2^2 ≤ 4r^2|D|.
- Taking expectations: E||f̃ − f||_2^2 ≤ C J^4 2^{-2Jα} + C2^{-2Jα} + C J^8 2^{-2J(2α−1)} + C e^{-cJ^2} ≤ C J^4 2^{-2Jα}.
- Finally 2^{-2Jα} ≤ 4^α n^{-2α/(2α+d+3)} and J ≤ log_2 n. ∎

**Log power.** As written the bound carries (log n)^4. The factor J^4 comes from squaring the J^2 in the bias. For non-integer α (no Zygmund logs) the bias has no log, and the bound is C n^{-2α/(2α+d+3)} with K = 0.

**Conclusion.** Combined with the round-1 lower bound c n^{-2α/(2α+d+3)}, the minimax rate is

  n^{-2α/(2α+d+3)}, up to logarithmic factors.

**Verdict: PROVED.** The rate is n^{-2α/(2α+d+3)}, with log power K ≤ 4 in general, and K = 0 for non-integer α. This rests on facts C1–C5 cited from memory: the Zygmund-scale Seeley extension, the kernel approximation bounds, Zygmund Taylor remainders, Zygmund Schauder estimates, and standard Gaussian process facts.

**Not needed / open.**
- The bias gradient bound (the bias file's Step 2) is not needed.
- The vanishing order of G at the sphere is not needed.
- The variance bound for ∇Z is not needed.
- Still open (not needed): whether the pointwise variance genuinely blows up near the source.

=== END OF ANSWER round3_q1 ===
