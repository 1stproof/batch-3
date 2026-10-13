# Answer to round4_q3: rigorous proofs of Lemmas 1–3 and the Section 3 consequences

Plan: §0 conventions; §1 Lemma 1 (with the corrected exponent (m−α)_+, and exactly when the factor J is needed); §2 Lemma 2; §3 Lemma 3 (a), (a′) (a right-inverse property that (★) uses but the excerpt never states), (b)–(e); §4 consequences for f_0; §5 what is proved and what was corrected.

## 0. Conventions

* B is the open unit ball and D = B̄. For vectors |·| is the Euclidean norm. For matrices and multilinear maps ‖·‖ is the operator norm. ‖·‖_∞ means the sup over D.
* **Fields.** "X is a C^k field on D" (k ≥ 1) means that X is the restriction to D of a C^k field on some open set U ⊃ D, still written X. This covers every field the proof uses. V_J = (k_J * V^E)|_D is the restriction of a C^∞ field on R^d. V̂ = V_J + ∇ξ is one too, because x ↦ k_J(x,·) is defined and smooth for all x ∈ R^d, so ξ has a smooth version on R^d by (C5). (Any field that is C^1 up to the boundary of the closed ball has a C^1 extension by Whitney's theorem, cited from memory. This is not needed.)
* **Functions.** g ∈ C^k(D) means g ∈ C^k(B) and all derivatives of order ≤ k extend continuously to D.
* ‖X − x/d‖_{C^1(D)} := max( sup_D |X(x) − x/d| , sup_D ‖DX(x) − I/d‖ ). If one uses the sum of the two terms instead, only the value of ε changes.
* Throughout, **ε ≤ ε_0 := 1/(8d)**. Put a := 1/d − ε ≥ 7/(8d). Then 1 − dε ≥ 7/8.
* Pointwise, |∇ div X| ≤ d‖D^2X‖ and ‖D^2 div X‖ ≤ d‖D^3X‖, because div X = tr DX.
* **Flow.** Φ_t is the flow of X on U, and Φ_{−s}x for s ≥ 0 solves γ' = −X(γ), γ(0) = x. Standard ODE theory, cited from memory (e.g. Hartman, *ODE*, Ch. V): if X ∈ C^k(U), the flow is defined on an open set Ω ⊂ R×U. On Ω it is C^k in x, and the x-derivatives up to order k are continuous in (t,x) and satisfy the variational equations obtained by formally differentiating the ODE.
* w(s,x) := exp(−∫_0^s div X(Φ_{−σ}x) dσ).

## 1. Lemma 1 (fields)

**Cited facts (from memory, standard; Triebel, *Theory of Function Spaces*).** Let (Δ_j)_{j≥0} be a Littlewood–Paley decomposition. For s > 0, the space C^s = B^s_{∞∞}(R^d) is characterised by ‖g‖_{C^s} ≍ sup_j 2^{js}‖Δ_j g‖_∞, and g = Σ_j Δ_j g converges uniformly. The Bernstein inequality gives ‖D^m Δ_j g‖_∞ ≤ C_m 2^{jm}‖Δ_j g‖_∞. Embedding: for s > 1, C^s ⊂ C^{1,β} with β := min(s−1, 1/2), and ‖g‖_{C^1} + [Dg]_β ≤ C‖g‖_{C^s}. Also C^{α+1} ⊂ C^2 with continuous inclusion, since α + 1 > 2.

**Lemma 1.1 (corrected derivative bound).** Let g ∈ C^s(R^d), s > 0, and m ≥ 1 an integer. Then, with C depending only on k, m, s, d:

‖D^m(k_J * g)‖_∞ ≤ C 2^{J(m−s)} ‖g‖_{C^s} if m > s;  ≤ C (J+1) ‖g‖_{C^s} if m = s;  ≤ C ‖g‖_{C^s} if m < s.

In particular ‖D^m(k_J * g)‖_∞ ≤ C J 2^{J(m−s)_+}‖g‖_{C^s} for J ≥ 1. **The factor J is needed only when m = s**, i.e. only when α is an integer equal to m (α = 2 for m = 2, α = 3 for m = 3). For every other α the bound holds without the factor J. (When m = s the logarithm cannot be removed in general; one example is g(x) = x_1^m log|x_1| cut off near 0. This sharpness remark is stated without proof, and nothing below uses it.)

*Proof.*
1. The sum Σ_j (D^m k_J) * Δ_j g converges uniformly: ‖(D^m k_J) * Δ_j g‖ ≤ ‖D^m k_J‖_{L^1}‖Δ_j g‖ ≤ C 2^{Jm}2^{−js}‖g‖_{C^s}. Hence D^m(k_J * g) = Σ_j (D^m k_J) * Δ_j g.
2. Terms with j ≤ J. Write (D^m k_J) * Δ_j g = k_J * D^mΔ_j g. Its norm is at most ‖k‖_{L^1} C 2^{jm}‖Δ_j g‖ ≤ C 2^{j(m−s)}‖g‖_{C^s}.
3. Terms with j > J. By step 1 each term is at most C 2^{Jm}2^{−js}‖g‖_{C^s}.
4. Summing step 3 over j > J gives C 2^{J(m−s)}‖g‖_{C^s} ≤ C 2^{J(m−s)_+}‖g‖_{C^s}.
5. Summing step 2 over 0 ≤ j ≤ J gives Σ_{j≤J} 2^{j(m−s)}. This is ≤ C 2^{J(m−s)} if m > s, equal to J + 1 if m = s, and ≤ C if m < s. ∎

(Lemma 1.1 is the second bullet of (C2), proved here. It needs no moment conditions on k.)

**Lemma 1 (corrected and complete).** Let ε ∈ (0, ε_0]. There are r_0 > 0 and J_0, depending only on d, α, ε and the fixed kernels, such that for r ≤ r_0 and J ≥ J_0:
1. ‖V_J − x/d‖_{C^1(D)} ≤ ε/2;
2. on A, ‖V̂ − x/d‖_{C^1(D)} ≤ ε;
3. ‖D^m V_J‖_∞ ≤ C 2^{J(m−α)_+} for m = 2, 3 when α ≠ m, and ‖D^m V_J‖_∞ ≤ C J when α = m. In all cases ‖D^m V_J‖_∞ ≤ C J 2^{J(m−α)_+}.

The excerpt's exponent (m+1−α)_+ is correct but weaker. The stronger (m−α)_+ is the one Section 3 uses.

*Proof.*
1. **Item 3.** On D, D^m V_J = D^m(k_J * V^E), and ‖V^E‖_{C^α} ≤ C. Apply Lemma 1.1 with s = α.
2. **Item 1.** On D, V = ∇u = V^E and ∇u_1 = x/d, where u_1 = (|x|^2 − 1)/(2d). So V_J − x/d = (k_J*V^E − V^E) + ∇(u − u_1) on D.
3. By the embedding with s = α > 1, D^iV^E is β-Hölder for i = 0, 1, with seminorm ≤ C. Since ∫k = 1 and k has compact support, for i = 0, 1:
   |D^i(k_J*V^E − V^E)(x)| = |∫ k_J(y)(D^iV^E(x−y) − D^iV^E(x)) dy| ≤ C ∫|k_J(y)||y|^β dy = C 2^{−Jβ}∫|k||z|^β dz.
4. By (C4) and the embedding C^{α+1} ⊂ C^2: ‖∇(u−u_1)‖_{C^1(D)} ≤ C‖u − u_1‖_{C^{α+1}} ≤ C r.
5. Hence ‖V_J − x/d‖_{C^1(D)} ≤ C_1(2^{−Jβ} + r). This is ≤ ε/2 once r ≤ r_0 := ε/(4C_1) and 2^{−J_0β} ≤ ε/(4C_1).
6. **Item 2.** By the choice of J, 2^{J(2α+d+3)} ≤ n, so n^{−1/2} ≤ 2^{−J(α+(d+3)/2)}. On A, for m = 1, 2, 3:
   ‖D^mξ‖_∞ ≤ J n^{−1/2}2^{J(d/2+m)} ≤ J 2^{−J(α+3/2−m)}.
   These are the three displayed bounds of the excerpt.
7. Hence ‖∇ξ‖_{C^1(D)} = max(‖∇ξ‖_∞, ‖D^2ξ‖_∞) ≤ J 2^{−J(α−1/2)}. Since α > 1/2, this tends to 0, so it is ≤ ε/2 for J ≥ J_0 (enlarging J_0). Then item 2 follows from item 1 and the triangle inequality. ∎

## 2. Lemma 2 (geometry)

**Lemma 2.** Let X be a C^1 field on D (in the sense of §0) with ‖X − x/d‖_{C^1(D)} ≤ ε ≤ ε_0. Then:
1. X has exactly one zero x_X in D, and |x_X| ≤ dε (better than the stated 2dε).
2. For y ∈ D, with ρ(y) := |y − x_X|: (1/d − ε)ρ^2 ≤ (y − x_X)·X(y) and |X(y)| ≤ (1/d + ε)ρ.
3. For x ∈ D, γ(s) = Φ_{−s}x is defined for all s ≥ 0 and lies in D. If x ∈ B, then γ(s) ∈ B for all s ≥ 0. If x ∈ ∂D, then γ(s) ∈ B for all s > 0.
4. r(s) := ρ(γ(s)) satisfies r(0)e^{−(1/d+ε)s} ≤ r(s) ≤ r(0)e^{−(1/d−ε)s}. If r(0) > 0, then r > 0 and −(1/d+ε)r ≤ r' ≤ −(1/d−ε)r. If r(0) = 0, then r ≡ 0.
5. For x ∈ D and s ≥ 0: ‖DΦ_{−s}(x)‖ ≤ e^{−as}, a = 1/d − ε. More generally, the propagator P(s,σ) of y' = −DX(γ(s))y satisfies ‖P(s,σ)‖ ≤ e^{−a(s−σ)} for s ≥ σ ≥ 0.
6. 1 − dε ≤ div X ≤ 1 + dε on D, so e^{−(1+dε)s} ≤ w(s,x) ≤ e^{−(1−dε)s}.

*Proof.*

1. **Zero of X.** Let G(x) := x − dX(x) = −d(X(x) − x/d).
   1. For x ∈ D, |G(x)| ≤ dε ≤ 1/8, so G maps D into B(0, dε) ⊂ D.
   2. D is convex and ‖DG‖ = d‖DX − I/d‖ ≤ dε ≤ 1/8 on D, so G is a contraction on the complete space D.
   3. By the Banach fixed-point theorem G has exactly one fixed point, and it lies in B(0, dε).
   4. G(x) = x if and only if X(x) = 0. So X has exactly one zero x_X in D, and |x_X| ≤ dε.

2. **Linearisation at the zero.** Fix y ∈ D. The segment from x_X to y lies in D because D is convex.
   1. X(y) = X(y) − X(x_X) = A(y)(y − x_X), with A(y) := ∫_0^1 DX(x_X + t(y − x_X)) dt.
   2. ‖A(y) − I/d‖ ≤ sup_D‖DX − I/d‖ ≤ ε.
   3. Hence (y − x_X)·X(y) = ρ^2/d + (y−x_X)·(A − I/d)(y−x_X) ≥ (1/d − ε)ρ^2.
   4. Also |X(y)| ≤ ‖A‖ρ ≤ (1/d + ε)ρ.

3. **Invariance of D and of B.** Let γ be the maximal solution of γ' = −X(γ) in U, on [0, s_+), and put φ(s) := |γ(s)|^2.
   1. For z ∈ ∂D, z·X(z) = 1/d + z·(X(z) − z/d) ≥ 1/d − ε > 0. So whenever |γ(t)| = 1, φ'(t) = −2γ·X(γ) ≤ −2(1/d − ε) < 0. (†)
   2. *D is invariant.* Let x ∈ D and suppose γ leaves D. Put t_1 := inf{t : φ(t) > 1}. Then φ(t_1) = 1 by continuity. By (†) and continuity of φ', φ < 1 on (t_1, t_1 + δ) for some δ > 0. This contradicts the definition of t_1. So γ ⊂ D on [0, s_+).
   3. *Global existence.* A maximal solution of an ODE with continuous field on an open set leaves every compact subset of the set. D ⊂ U is compact, so s_+ = ∞.
   4. *B is invariant.* Let γ(t_0) ∈ B and suppose t_1 := inf{t > t_0 : φ(t) ≥ 1} < ∞. Then φ(t_1) = 1 and φ < 1 on [t_0, t_1), so φ'(t_1) ≥ 0, contradicting (†).
   5. *Boundary starts.* If x ∈ ∂D, then φ(0) = 1 and φ'(0) < 0 by (†). So γ(s) ∈ B for small s > 0, and then for all s > 0 by step 4.
   6. Since γ stays in D, Φ_{−s}x is just the flow of −X inside D. The values of X outside D play no role.

4. **Radial rates.** Since X(x_X) = 0, the constant curve x_X is the solution starting at x_X, so r(0) = 0 forces r ≡ 0 by uniqueness. In general:
   1. (r^2)' = −2(γ − x_X)·X(γ).
   2. By item 2 and Cauchy–Schwarz, −2(1/d+ε)r^2 ≤ (r^2)' ≤ −2(1/d−ε)r^2.
   3. Gronwall applied to r^2 gives r(0)^2e^{−2(1/d+ε)s} ≤ r(s)^2 ≤ r(0)^2e^{−2(1/d−ε)s}.
   4. If r(0) > 0, then r > 0, r is C^1 and r' = (r^2)'/(2r), which gives the differential inequalities.

5. **Contraction of the linearised flow.** Fix σ ≥ 0 and y_0, and let y(s) = P(s,σ)y_0, i.e. y' = −DX(γ(s))y with y(σ) = y_0.
   1. Since γ(s) ∈ D, v·DX(γ)v = |v|^2/d + v·(DX − I/d)v ≥ a|v|^2.
   2. Hence (|y|^2)' = −2y·DX(γ)y ≤ −2a|y|^2, so |y(s)| ≤ e^{−a(s−σ)}|y_0|.
   3. By the variational equation, M(s) := DΦ_{−s}(x) solves M' = −DX(γ)M with M(0) = I. So M(s) = P(s,0) and ‖M(s)‖ ≤ e^{−as}.

6. **Divergence and weight.** div X = 1 + tr(DX − I/d), and |tr B| ≤ d‖B‖. Integrating along γ ⊂ D gives the bounds on w. ∎

## 3. Lemma 3 (transport inverse)

The hypotheses of Lemma 2 hold throughout. For H ∈ C(D) put T_X^{-1}H(x) := ∫_0^∞ H(Φ_{−s}x) w(s,x) ds for x ∈ D.
- By Lemma 2.6, |H(Φ_{−s}x)w| ≤ ‖H‖_∞e^{−(1−dε)s}. So the integral converges absolutely, uniformly in x.
- The integrand (s,x) ↦ H(Φ_{−s}x)w(s,x) is continuous on [0,∞)×D. By dominated convergence, T_X^{-1}H ∈ C(D).

**Semigroup identity.** By Lemma 2.3, the flow property Φ_{−s}Φ_{−t} = Φ_{−s−t} (s, t ≥ 0) holds on D. Hence w(s,Φ_{−t}x) = w(s+t,x)/w(t,x), and for t ≥ 0

 (SG)  w(t,x) · T_X^{-1}H(Φ_{−t}x) = ∫_t^∞ H(Φ_{−s}x) w(s,x) ds.

**(a) Uniqueness.** If g ∈ C^1(D) and div(gX) = H on B, then g = T_X^{-1}H on D.

*Proof.*
1. Fix x ∈ D and put γ(s) = Φ_{−s}x and ψ(s) := g(γ(s))w(s,x). Then ψ is continuous on [0,∞).
2. For s > 0 we have γ(s) ∈ B (Lemma 2.3), so ψ is differentiable there, with
   ψ'(s) = [−∇g(γ)·X(γ) − g(γ)div X(γ)]w = −div(gX)(γ)w = −H(γ(s))w(s,x).
3. Hence ψ(S) − ψ(δ) = −∫_δ^S H(γ)w ds for 0 < δ < S.
4. Let δ → 0, using continuity of ψ. Let S → ∞, using |ψ(S)| ≤ ‖g‖_∞e^{−(1−dε)S} → 0.
5. This gives g(x) = ψ(0) = ∫_0^∞ H(γ)w ds. ∎

**(a′) Right inverse.** (This is used in (★) but is not stated in the excerpt.) Let H ∈ C(D) and suppose g := T_X^{-1}H ∈ C^1(D); by (d) below this holds when X ∈ C^2 and H ∈ C^1(D). Then div(gX) = H on D.

*Proof.*
1. Fix x ∈ B and differentiate (SG) at t = 0^+.
2. The right side has derivative −H(x), by continuity of the integrand.
3. On the left, g is C^1 near x, t ↦ Φ_{−t}x is C^1 with derivative −X(x) at t = 0, w(0) = 1 and ∂_t w(0) = −div X(x). So the left side has derivative −∇g(x)·X(x) − g(x)div X(x) = −div(gX)(x).
4. Hence div(gX) = H on B, and on D by continuity of both sides. ∎

How (★) uses (a) and (a′):
- T_{V̂}f̂ = 1 and T_{V_J}f_0 = 1 are (a′) with H = 1.
- T_{V_J}Z = div(f_0∇ξ) is (a′) with H = div(f_0∇ξ) ∈ C^1(D). This needs f_0 ∈ C^2(D) (proved in (e)) and ξ ∈ C^3.
- The final step uses (a) with the C^1 function f̂ − f_0 + Z.

**(b)** ‖T_X^{-1}H‖_∞ ≤ ‖H‖_∞∫_0^∞e^{−(1−dε)s}ds = ‖H‖_∞/(1−dε) ≤ (8/7)‖H‖_∞ ≤ 2‖H‖_∞. ∎

**(c) Boundary layer.** Let 0 < δ ≤ 1 and H ∈ C(D) with H = 0 on {|x| ≤ 1−δ}. Then ‖T_X^{-1}H‖_∞ ≤ 6dδ‖H‖_∞. With δ = C2^{−J} this is the excerpt's (c).

*Proof.*
1. If δ > 1/2, then (b) gives ‖T^{-1}H‖ ≤ 2‖H‖ ≤ 4δ‖H‖ ≤ 6dδ‖H‖. So assume δ ≤ 1/2.
2. Put c := (1−δ)^2 ≥ 1/4, fix x ∈ D, and let φ(s) := |Φ_{−s}x|^2.
3. Whenever φ(s) ≥ 1/4, i.e. |γ| ≥ 1/2:
   γ·X(γ) = |γ|^2/d + γ·(X(γ) − γ/d) ≥ |γ|(|γ|/d − ε) ≥ (1/2)(1/(2d) − 1/(8d)) = 3/(16d).
   So φ' = −2γ·X(γ) ≤ −3/(8d).
4. Let s_1 := inf{s ≥ 0 : φ(s) ≤ c}. On [0, s_1) we have φ > c ≥ 1/4, so φ decreases at rate at least 3/(8d), starting from φ(0) ≤ 1. Hence s_1 ≤ (1 − c)·8d/3 ≤ 2δ·8d/3 ≤ 6dδ.
5. For s ≥ s_1, φ(s) ≤ c. Otherwise put t_1 := inf{t > s_1 : φ(t) > c}. Then φ(t_1) = c, and φ'(t_1) < 0 forces φ < c just after t_1, contradicting the definition of t_1.
6. So for s ≥ s_1 the ray lies in {|y| ≤ 1−δ}, where H(Φ_{−s}x) = 0. Since w ≤ 1,
   |T^{-1}H(x)| ≤ ∫_0^{s_1}|H(γ)| ds ≤ 6dδ‖H‖_∞. ∎

**Notation for (d) and (e).** For x ∈ D: γ(s) = Φ_{−s}x, M(s) := DΦ_{−s}(x), N(s) := D^2Φ_{−s}(x) (a symmetric bilinear map), and ℓ(s,x) := log w(s,x) = −∫_0^s div X(Φ_{−σ}x)dσ.

**Lemma 3.1 (derivatives of the flow and the weight; no polynomial factors in s).** Let a = 1/d − ε ≥ 7/(8d).
1. If X ∈ C^1: ‖M(s)‖ ≤ e^{−as}. (This is Lemma 2.5.)
2. If X ∈ C^2: ‖N(s)‖ ≤ (‖D^2X‖_∞/a) e^{−as}.
3. If X ∈ C^2: ℓ(s,·) is C^1, and |D_xℓ(s,x)| ≤ ‖D div X‖_∞/a for all s ≥ 0.
4. If X ∈ C^3: ℓ(s,·) is C^2, and ‖D_x^2ℓ(s,x)‖ ≤ ‖D^2 div X‖_∞/(2a) + ‖D div X‖_∞‖D^2X‖_∞/a^2.
5. Consequently D_xw = wD_xℓ and D_x^2w = w(D_x^2ℓ + D_xℓ⊗D_xℓ). So |D_xw| ≤ w‖D div X‖/a and
   ‖D_x^2w‖ ≤ w[‖D^2 div X‖/(2a) + ‖D div X‖‖D^2X‖/a^2 + ‖D div X‖^2/a^2],
   with w ≤ e^{−(1−dε)s} ≤ e^{−7s/8}.

*Proof.*
- **Item 2.** For X ∈ C^2 the flow is C^2 on Ω, so we may differentiate M' = −DX(γ)M in x. This gives N'[v,u] = −DX(γ)N[v,u] − D^2X(γ)[Mv, Mu] with N(0) = 0.
  - By variation of constants (checked by differentiating), N(s)[v,u] = −∫_0^s P(s,σ)D^2X(γ(σ))[M(σ)v, M(σ)u]dσ.
  - By Lemma 2.5 (γ ⊂ D):
    ‖N(s)‖ ≤ ∫_0^s e^{−a(s−σ)}‖D^2X‖_∞e^{−2aσ}dσ = ‖D^2X‖_∞e^{−as}(1 − e^{−as})/a ≤ ‖D^2X‖_∞e^{−as}/a.
- **Item 3.** Fix s. The integrand σ ↦ div X(Φ_{−σ}x) has x-derivative D(div X)(γ(σ))M(σ), which is jointly continuous in (σ,x) on compact subsets of the flow domain. Differentiating under the finite integral,
  D_xℓ(s,x)[v] = −∫_0^s D(div X)(γ(σ))[M(σ)v]dσ,
  so |D_xℓ| ≤ ‖D div X‖_∞∫_0^se^{−aσ}dσ ≤ ‖D div X‖_∞/a.
- **Item 4.** In the same way, D_x^2ℓ(s,x)[v,u] = −∫_0^s (D^2 div X(γ)[Mv,Mu] + D div X(γ)[N[v,u]])dσ. By items 1–2 this is bounded by ‖D^2 div X‖∫_0^∞e^{−2aσ}dσ + ‖D div X‖(‖D^2X‖/a)∫_0^∞e^{−aσ}dσ.
- **Item 5.** Chain rule for w = e^ℓ. ∎

So the derivatives of Φ_{−s} decay like e^{−as}, and the derivatives of log w are bounded uniformly in s. The factor (1+s)^2 in the excerpt's sketch is an overestimate. It is harmless, since (1+s)^2e^{−7s/8} is integrable. The only s-dependence left to integrate is w ≤ e^{−7s/8}.

**Differentiation under ∫_0^∞ (justification for (d) and (e)).** Let F(s,x) be the integrand: F = H(Φ_{−s}x)w(s,x) for (d), F = w(s,x) for (e). Let k = 1 for (d) and k = 2 for (e).
1. Fix x_0 ∈ B and S > 0. B is open and Φ_{−s}B ⊂ B (Lemma 2.3), and [0,S]×{x_0} is a compact subset of the open set Ω. So there is a ball B(x_0,η) ⊂ B with [0,S]×B(x_0,η) ⊂ Ω.
2. On that set F is C^k in x, and its x-derivatives are jointly continuous in (s,x). So g_S(x) := ∫_0^S F(s,x)ds is C^k on B, with D^jg_S = ∫_0^S D_x^jF ds.
3. By Lemma 3.1, |D_x^jF(s,x)| ≤ K e^{−7s/8} uniformly in x ∈ D. Hence, for j ≤ k, g_S → g and D^jg_S → G_j := ∫_0^∞ D_x^jF ds uniformly on B.
4. B is convex and open, so uniform convergence of the derivatives gives g ∈ C^k(B) with D^jg = G_j.
5. The flow derivatives are continuous on Ω ⊃ [0,∞)×D, and DH and D^j div X are continuous on D. So (s,x) ↦ D_x^jF(s,x) is continuous on [0,∞)×D and dominated by Ke^{−7s/8}. Hence G_j is continuous on D, and g ∈ C^k(D).

**(d)** If X ∈ C^2 and H ∈ C^1(D), then g = T_X^{-1}H ∈ C^1(D) and
 ‖∇T_X^{-1}H‖_∞ ≤ (8/7)‖∇H‖_∞ + (8/(7a))‖H‖_∞‖D div X‖_∞ ≤ C_d(‖∇H‖_∞ + ‖H‖_∞‖D div X‖_∞).

*Proof.* By the justification above,
 Dg(x)[v] = ∫_0^∞[DH(γ)[M v] w + H(γ) w D_xℓ[v]]ds.
By Lemma 3.1,
 |∇g(x)| ≤ ∫_0^∞e^{−7s/8}(‖∇H‖e^{−as} + ‖H‖‖D div X‖/a)ds ≤ (8/7)(‖∇H‖ + ‖H‖‖D div X‖/a). ∎

**(e)** If X ∈ C^3, then T_X^{-1}1 ∈ C^2(D), and with C_d depending only on d (recall a ≥ 7/(8d)):
 ‖∇T_X^{-1}1‖_∞ ≤ (8/(7a))‖D div X‖_∞,
 ‖D^2T_X^{-1}1‖_∞ ≤ (8/7)[‖D^2 div X‖_∞/(2a) + ‖D div X‖_∞‖D^2X‖_∞/a^2 + ‖D div X‖_∞^2/a^2]
  ≤ C_d(‖D^2 div X‖_∞ + ‖D div X‖_∞^2 + ‖D div X‖_∞‖D^2X‖_∞).

*Proof.* T^{-1}1 = ∫_0^∞w(s,·)ds. Apply the justification with F = w, use Lemma 3.1(5), and integrate against e^{−7s/8}. ∎

All constants depend only on d, given ε ≤ 1/(8d). They are uniform over all fields X with ‖X − x/d‖_{C^1(D)} ≤ ε. X ∈ C^3 is used only qualitatively; quantitatively only the displayed norms enter.

*Remark (smoothness of f_0; sketch).* Only f_0 ∈ C^2 is needed in Section 3, and the cases j ≤ 2 below are fully proved above. For higher j, argue by induction on j. If X ∈ C^k, the j-th variational equation has the form N_j' = −DX N_j + R_j, where R_j is a sum of terms D^iX[N_{j_1},…,N_{j_i}] with i ≥ 2. So |R_j| ≤ Ce^{−2as}, and Duhamel gives ‖D^jΦ_{−s}‖ ≤ C_j e^{−as} for j ≤ k. Likewise D^jℓ is bounded uniformly in s. Hence T_X^{-1}1 ∈ C^{k−1}(D), and for X = V_J (which is C^∞) f_0 ∈ C^∞(D).

## 4. Consequences used in Section 3

Assume r ≤ r_0 and J ≥ J_0 (Lemma 1). Then X = V_J satisfies the hypotheses of Lemmas 2 and 3 and is C^∞ on R^d. Let f_0 := T_{V_J}^{-1}1. We use ‖D div V_J‖ ≤ d‖D^2V_J‖, ‖D^2 div V_J‖ ≤ d‖D^3V_J‖ and Lemma 1(3).
1. **Sup bound.** ‖f_0‖_∞ ≤ 2 by (b), in fact ≤ 8/7. Also f_0 ≥ ∫e^{−(1+dε)s}ds = 1/(1+dε) > 0.
2. **Gradient.** By (e), ‖∇f_0‖_∞ ≤ C‖D div V_J‖ ≤ C‖D^2V_J‖ ≤ C J 2^{J(2−α)_+}. The factor J is needed only if α = 2.
3. **Second derivatives.** By (e),
   ‖D^2f_0‖_∞ ≤ C(‖D^3V_J‖ + ‖D^2V_J‖^2) ≤ C(J2^{J(3−α)_+} + J^2 2^{2J(2−α)_+}) ≤ C J^2 2^{J(3−α)_+}.
   The last step uses 2(2−α)_+ ≤ (3−α)_+ for α ≥ 1: if α ≥ 2 the left side is 0, and if 1 ≤ α < 2 then 4 − 2α ≤ 3 − α ⇔ α ≥ 1. More precisely, J^2 is needed only when α = 2, J only when α = 3, and no logarithm otherwise.
4. **Regularity and the equation.** f_0 ∈ C^2(D) (indeed C^∞), and div(f_0V_J) = 1 by (a′).

## 5. Summary: what was proved, what was corrected

**Proved in full**, apart from the cited standard facts (Littlewood–Paley characterisation, Bernstein inequality and Hölder embeddings for Zygmund spaces; the Schauder fact (C4); C^k dependence of ODE flows on initial data, with variational equations):
- **Lemma 1.1:** ‖D^m(k_J*g)‖_∞ ≤ C2^{J(m−s)_+}‖g‖_{C^s} for m ≠ s, and ≤ C(J+1)‖g‖_{C^s} for m = s.
- **Lemma 1:**
  - ‖V_J − x/d‖_{C^1} ≤ ε/2, and on A, ‖V̂ − x/d‖_{C^1} ≤ ε.
  - ‖D^mV_J‖ ≤ CJ2^{J(m−α)_+} for m = 2, 3; the factor J is needed only when α = m.
- **Lemma 2, items 1–6:**
  - item 1 with the sharper bound |x_X| ≤ dε;
  - item 3 strengthened: B is invariant and boundary points enter B immediately;
  - item 5 including the propagator bound.
- **Lemma 3:**
  - (a) uniqueness;
  - (a′) the right-inverse property, which (★) needs and the excerpt lacks;
  - (b) with constant 8/7;
  - (c) with the explicit constant 6dδ, for all δ ∈ (0,1];
  - Lemma 3.1: ‖D^2Φ_{−s}‖ ≤ ‖D^2X‖e^{−as}/a, and the derivatives of log w are bounded uniformly in s;
  - (d) and (e) with explicit constants depending only on d, uniform over ‖X − x/d‖_{C^1} ≤ ε ≤ 1/(8d), including rigorous differentiation under the integral up to the boundary.
- **Section 3 consequences:** ‖f_0‖ ≤ 2, ‖∇f_0‖ ≤ CJ2^{J(2−α)_+}, ‖D^2f_0‖ ≤ CJ^2 2^{J(3−α)_+}.

**Corrections and clarifications to the excerpt.** None of its statements is false.
- Lemma 1(3) as written, with (m+1−α)_+, is true but too weak for Section 3. The correct exponent, proved here, is (m−α)_+.
- "C^k field on D" must be read as the restriction of a C^k field on a neighbourhood of D; V_J and V̂ satisfy this. Otherwise the flow and its derivatives at boundary points need an extension argument.
- (★) uses the right-inverse property (a′), which is now proved.
- The (1+s)^2 factor in the excerpt's proof of (d) and (e) is unnecessary: all the relevant derivative bounds are uniform in s.

**Not fully proved.**
- C^∞ smoothness of f_0 is only sketched. C^2, which is what Section 3 uses, is fully proved.
- The sharpness of the factor J when α = m is not proved.

=== END OF ANSWER round4_q3 ===
