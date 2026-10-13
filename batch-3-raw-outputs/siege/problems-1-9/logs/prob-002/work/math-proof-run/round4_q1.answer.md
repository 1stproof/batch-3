# round4_q1: referee check of the chain for the minimax rate n^{-2α/(2α+d+3)}

**Verdict: PROVED AFTER THE REPAIRS GIVEN.** The repairs are R1–R4 in Part B, plus one cosmetic fix in Part A. None of them changes the rate. All of them are local and are carried out below.

**Answer to the problem.** For every α>1, d≥2 and every fixed r∈(0,r_0(d,α)], the minimax rate is n^{-2α/(2α+d+3)} up to logarithmic factors. Precisely:
- c n^{-2α/(2α+d+3)} ≤ inf sup E||f̂−f||²_2 ≤ C (log n)^4 n^{-2α/(2α+d+3)};
- the log factor can be dropped for non-integer α.

Standard facts are cited from memory, as in the chain: Schauder and W^{2,p} theory, Seeley extension on Zygmund spaces, Littlewood–Paley approximation bounds, Dudley, Borell–TIS, Assouad and Gagliardo–Nirenberg. I checked that each is stated correctly in the form used. The (C2) bounds in particular follow from a Littlewood–Paley splitting: blocks l≤J use the vanishing of 1−k̂(2^{-J}·) to order S+1>s, and blocks l>J use ||D^m k_J||_1 ≤ C2^{Jm}.

---

## PART A (lower bound): checked, correct

1. **Hypercube and membership.** The Φ_k have disjoint supports (radius 2^{-j}/2, centres 2^{-j+1} apart). Since φ_0 is constant near 0, Φ_k is smooth. Each χ_k = 2^{-2j}Δ_SΦ_k satisfies ||∂^mχ_k|| ≤ C2^{jm} and ||χ_k||²_{L²(S)} ≍ 2^{-j(d-1)}. The usual splitting of the difference quotient (|x−y| below or above 2^{-j}) gives ||2^{-jα}Σθ_kχ_k||_{C^α} ≤ C uniformly. So f_θ∈F(α,r) for κ=κ(r) small. Correct.

2. **Sizes.** ||h_k||²_2 = κ²2^{-2jα}∫b²ρ^{d-5}dρ ||χ_k||² ≍ 2^{-j(2α+d-1)}. Correct.

3. **Exact identity.** div(g∇(u_g−u_f)) = 1 − div(g∇u_f) = −div(h∇u_f). Correct.

4. **Duality.** L_g is self-adjoint, and (E1) gives ||L_g^{-1}φ||_{H²} ≤ C||φ||_2. Correct.
   - Cosmetic fix: in (E1) the hypothesis g≥1/2 should read g≥1−r, since the constant depends on the ellipticity bound 1−r>0. With that change (E1) holds for every r<1.

5. **Homogeneity identity.** Write G = bΔΦ_k. Then div(Gx) = r∂_rG + dG. Since ΔΦ_k is (−2)-homogeneous, r∂_r(bΔΦ_k) = (rb' − 2b)ΔΦ_k. This gives c = (rb' + (d−2)b)/d. Integrating by parts twice is legitimate because cψ is compactly supported in the annulus, where Φ_k is smooth. The resulting bound is C2^{-j(α+2)}2^{-j(d-1)/2}||ψ||_{H²} = C2^{-2j}||h_k||_2||ψ||_{H²}. Correct.

6. **Drift.** Put w = u_f − u_1. Then div(f∇w) = −div((f−1)x/d) = −q, and termwise q = κ2^{-j(α+2)}cΔΦ_{θ'}. Correct.
   - **W^{2,p} bound:** ||q||_p ≤ C2^{-jα}, and (E2) applies with a uniform constant because F(α,r) is compact in C¹.
   - **L^p bound by duality:** ∫wφ = −∫qψ is justified by two integrations by parts, with w∈W^{2,p}, p>d, and ψ∈W^{2,p'}∩W^{1,p'}_0. Then |∫Φ_{θ'}Δ(cψ)| ≤ ||Φ||_∞||cψ||_{W^{2,1}} ≤ C. So ||w||_p ≤ C2^{-j(α+2)}.
   - **Gagliardo–Nirenberg:** with t = (1+d/p)/2 the scaling is correct. On the ball the lower-order term C||w||_p is dominated by ||w||^t_{W^{2,p}}||w||^{1-t}_p, so the stated form holds.
   - Result: ||W||_∞ ≤ C2^{-j(α+1-d/p)} ≤ C2^{-2j} once d/p ≤ α−1. This is where α>1 is used.

7. **KL and Assouad.** In the white-noise model KL = (n/2)||u_θ−u_θ'||² ≤ Cn2^{-j(2α+d+3)}. Pinsker then gives TV ≤ 1/4.
   - Because the supports are disjoint, ||f̂−f_θ||² ≥ (1/4)Σ_k 1{θ̂_k≠θ_k}||h_k||², where θ̂_k is the nearer-vertex choice on each support.
   - Assouad then gives at least (M/8)(3/4)min||h_k||² ≍ 2^{-2jα} = n^{-2α/(2α+d+3)}. Correct.

**Part A: PROVED** for every α>1, d≥2, r∈(0,1).

---

## PART B (upper bound): checked, with repairs

### Kernel properties (K1)–(K3)
E* is the identity on D plus the pullbacks z ↦ a_iχ(|R_i^{-1}z|)φ(R_i^{-1}z)|det DR_i^{-1}(z)| on the shells {1−λ_iη<|z|<1}.
- (K1) holds: x enters only through k_J(x−t).
- (K2) holds: if t = R_i^{-1}z with |t|>1 and |x−t| ≤ C2^{-J}, x∈D, then |t|−1 ≤ C2^{-J}. Hence |z−t| = (1+λ_i)(|t|−1) ≤ C2^{-J}.
- (K3) holds: sup² times support volume gives the L² bound, and (K1) with |a|+1 ≤ 4 gives the Lipschitz bound.

### Event A and its consequences
The arithmetic is correct. Since n^{-1/2} ≤ 2^{-J(α+(d+3)/2)}, on A we have ||D^mξ|| ≤ J2^{-J(α+3/2-m)}.

### R2 (gap, repaired): A is not observable
ξ = K_JY − K_Ju depends on the unknown f. Therefore "f̂ := T_{V̂}^{-1}1 on A, 1 off A" is not a statistic.

**Repair.** Let ε_0 be the threshold of Lemma 2. Define the observable event B := {||V̂ − x/d||_{C¹(D)} ≤ ε_0}, and set
- f̂ := T_{V̂}^{-1}1 on B, and f̂ := 1 off B;
- f̃ := truncation of f̂ to [1−r,1+r].

Lemma 1, with ε = ε_0 and r ≤ r_0, J ≥ J_0, gives A ⊂ B. So on A the estimator is exactly the one analysed. On A^c we still have |f̃−f| ≤ 2r, so the assembly is unchanged.

For n with J < J_0, the risk is bounded by 4r²|D|, which is absorbed into the constant.

### Lemma 1 and R1 (the exponent)
The first two bullets are correct:
- ||V_J−V||_{C¹} ≤ C2^{-J(α-1)} follows from (C2) with s=α and m=0,1<α.
- ||V−x/d||_{C¹} ≤ C||u−u_1||_{C^{α+1}} ≤ Cr, using C^{α+1} ⊂ C² for α>1.
- ||∇ξ||_{C¹} is small on A.

**R1.** The third bullet is misstated. Applying (C2) with g = V^E ∈ C^α actually gives the stronger bound

  ||D^mV_J||_∞ ≤ CJ 2^{J(m-α)_+}.

To see this, split k_J*g = Σ_l k_J*Δ_lg:
- for l ≤ J, ||D^mΔ_lg|| ≤ 2^{l(m-α)};
- for l > J, ||D^mk_J*Δ_lg|| ≤ C2^{Jm}2^{-lα}.

Summing gives 2^{J(m-α)} if m>α, J if m=α, and C if m<α. This corrected bound is exactly what §3 and §6 use. The proof line "by (C2)" proves it, so only the displayed statement must be changed.

The weaker exponent (m+1−α)_+ would not suffice. It would give ||∇f_0|| ≤ CJ2^{J(3-α)_+}, which for α<2 is larger than 2^J. That would break the kernel bound |D_yk_J| ≤ C2^{J(d+2)} in §5, and the remainder bound in §6 for α near 1. With R1 every later exponent checks; see below.

### Lemma 2 (geometry): correct
- **Item 1.** Ψ(x) = x − dX(x) = −d(X − x/d) satisfies |Ψ| ≤ dε and Lip Ψ ≤ dε. So there is a fixed point in B(0,1/2), which is a zero of X. It is unique by item 2.
- **Item 2.** Follows from X(y) = A(y)(y−x_X) with ||A−I/d|| ≤ ε.
- **Item 3.** On the sphere, γ·X ≥ 1/d − ε.
- **Item 4.** rr' = −(γ−x_X)·X(γ).
- **Item 5.** d/ds|Mv|² = −2Mv·DX Mv ≤ −2(1/d−ε)|Mv|².
- **Item 6.** tr DX ≥ 1 − dε.

### Lemma 3 (transport inverse): correct, plus R3
- **(a)** Correct. It needs g∈C¹(D̄) and X∈C¹.
- **(b)** Correct.
- **(c)** Correct. On |γ| ≥ 1/2, d/ds|γ|² ≤ −2(1/(4d) − ε) < 0. So |γ| cannot increase across |γ| = 1/2, and the layer is crossed at most once, in time ≤ C2^{-J}.
- **(d), (e)** Correct. |∇_xw| ≤ Cw||D div X||, the variational equation gives ||D²Φ_{-s}|| ≤ C||D²X||, and |D²w| ≤ Cw(||D div X||² + ||D²div X|| + s||D²X|| ||D div X||), which is integrable.

**R3 (missing fact, added).** (★) uses T_X(T_X^{-1}H) = H, both for f̂ = T_{V̂}^{-1}1 and for T_{V_J}Z = div(f_0∇ξ). Lemma 3(a) only gives the converse direction, T_X^{-1}T_X = id. The chain's remark "Lemma 3(a) is not even needed" misattributes the fact used.

> **Lemma 3(a').** Let H∈C(D̄), and suppose g := T_X^{-1}H is C¹. Then T_Xg = H.
>
> *Proof.* By the flow property, w(s,Φ_{-t}x) = w(s+t,x)/w(t,x). Hence
>   g(Φ_{-t}x)w(t,x) = ∫_t^∞ H(Φ_{-s}x)w(s,x)ds.
> Differentiate at t=0+ (one-sided at ∂D, where the backward flow points inward):
>   −X·∇g(x) − g(x)div X(x) = −H(x). ∎

The C¹ property holds in both uses:
- f̂ is C¹ by Lemma 3(e), since V̂ is smooth.
- Z is C¹ by Lemma 3(d), since f_0 ∈ C² by (e) and so div(f_0∇ξ) ∈ C¹.

### §3: bounds on f_0, and identity (★): correct with R1, R3
With R1, ||∇f_0|| ≤ C||D²V_J|| ≤ CJ2^{J(2-α)_+}. Also

  ||D²f_0|| ≤ C(J2^{J(3-α)_+} + J²2^{2J(2-α)_+}) ≤ CJ²2^{J(3-α)_+},

because 2(2−α) ≤ 3−α for α ≥ 1.

The algebra of (★) is correct:
- T_{V̂}(f̂−f_0) = 1 − 1 − div(f_0∇ξ);
- T_{V̂}Z = div(f_0∇ξ) + div(Z∇ξ).

Lemma 3(a) is applied to f̂ − f_0 + Z, which is C¹ (f̂ by (e), f_0 smooth, Z by (d)). So every function to which (a) is applied is C¹.

### §4: bias: correct
- **Identity.** f_0 − f ∈ C¹ because C^α ⊂ C¹ for α>1, and div(fV) = 1 classically.
- **Commutator algebra.** Writing F(x)−F(x−h) = −Δ_{-h}F(x) and V^E(x−h) = V^E(x) + Δ_{-h}V^E(x), then substituting h → −h, gives exactly F(k_J*V^E) = k_J*(FV^E) + (F − k_J*F)V^E + R. Correct.
- **G.** div k_J*(FV^E) = k_J*div(FV^E), since FV^E ∈ C¹(R^d). G ∈ C^{α-1}(R^d) by the algebra property, and G=0 on D̄.
- **(i)** Correct, with total C2^{-Jα} + C2^{-J(2α-1)}.
- **(ii)** Correct. The pairs are (a,b) = (α−1,α) or (α,α−1).
  - When a ≤ 1, P_A is empty. The remainder exponents are 1+a, 1+b and a+b, whose minimum is α since 2α−1 ≥ α.
  - Polynomial terms have degree between 2 and less than 2α−1, so they integrate to zero against k_J (S ≥ 2α+2).
  - The remainder gives CJ²2^{-Jα}.
- **(iii)** Correct. Here k_J*G = k_J*G − G on D, has size ≤ C2^{-J(α-1)}, and is supported within C2^{-J} of ∂D. Lemma 3(c) then gives C2^{-Jα}.

Total bias: CJ²2^{-Jα}.

### §5: variance: correct
- **Kernel bound.** |D_yk_J| ≤ C2^{J(d+2)}1{|y−z| ≤ δ}. This uses ||∇f_0|| ≤ CJ2^{J(2-α)_+} ≤ 2^J, valid because (2−α)_+ < 1; this needs R1.
- **Energy bound.** ∫μ(B(z,δ))²dz ≤ Cδ^d∫μ(B(y,2δ))μ(dy). Correct.
- **Change of variables (M).** Since w ≤ e^{-(1-dε)s} and r(s) ≥ ρ_xe^{-(1/d+ε)s}, we get w ≤ (r/ρ_x)^β. Also ds ≤ dr/((1/d−ε)r). Correct.
- **Small-ball masses.** Correct. For y on the ray, ρ(y) ≤ ρ_x.
- **Integration.** Correct. In fact β > 1/2 suffices: 2β−1 > 0 for the outer part, and min(1,(δ/ρ_x)^{2β}) ≤ min(1,δ/ρ_x) for the inner part. So the claim β > 1 is true but stronger than needed.
- **Conclusion.** Since ∫_D|x−x_J|^{-1}dx ≤ C for d ≥ 2, E||Z||² ≤ Cn^{-1}2^{J(d+3)} ≤ C2^{-2Jα}.

### §6: remainder and bad event: correct, with R1 and minor J-powers
- **||G_ξ||.** The second term is CJ²2^{-J(α+1/2-(2-α)_+)}. Since (2−α)_+ < 1, this is ≤ CJ2^{-J(α-1/2)} after absorbing a power of J. Harmless.
- **||∇G_ξ||.** Both cross terms have exponent −(2α−5/2) ≤ −(α−3/2) for α ≥ 1.
- **||∇Z||.** ||G_ξ|| ||D div V_J|| ≤ CJ²2^{-J(α-1/2-(2-α)_+)} ≤ CJ²2^{-J(α-3/2)}.
- **div(Z∇ξ).** Bounded by CJ⁴2^{-J(2α-1)}, and 2α−1 > α exactly when α > 1. Correct.
- **Bad event.** σ_m ≤ Cn^{-1/2}2^{J(d/2+m)}, the canonical metric is Lipschitz with constant ≤ Cσ_m2^J, and Dudley gives E sup ≤ Cσ_m√J. Borell–TIS with t = Jn^{-1/2}2^{J(d/2+m)}/2 then gives P(A^c) ≤ Ce^{-cJ²}, which is smaller than any power of n. Uniform in f.

### Assembly: correct
E||f̃−f||² ≤ C(J⁴2^{-2Jα} + 2^{-2Jα} + J⁸2^{-2J(2α-1)} + e^{-cJ²}) ≤ C(log n)⁴n^{-2α/(2α+d+3)}.

### R4 (cosmetic)
- The reference "(I1)" in (C4) is dangling. (C4) follows directly from Zygmund-scale Schauder theory: w = u_f − u_1 solves div(f∇w) = −div((f−1)x/d), whose right side has C^{α-1} norm ≤ Cr.
- The estimator uses the known α and r_0, which is legitimate for a minimax statement.

---

## Final status

- **Part A: PROVED** (one cosmetic fix: the ellipticity bound in (E1)).
- **Part B: PROVED AFTER REPAIRS:**
  - R1: correct the exponent in Lemma 1 to (m−α)_+;
  - R2: replace the unobservable event A by the observable event B ⊇ A in the definition of the estimator;
  - R3: add Lemma 3(a') (T_XT_X^{-1}H = H for C¹ outputs);
  - R4: minor bookkeeping (J-powers, β > 1/2 suffices, the dangling (I1)).
- **Claim:** for every α>1, d≥2 and r ≤ r_0(d,α), the minimax L²-risk is n^{-2α/(2α+d+3)} up to logarithmic factors (log power ≤ 4, and 0 for non-integer α). **PROVED AFTER THE REPAIRS GIVEN**, modulo the standard cited facts, which are stated correctly.
- **Open (not needed for the claim):**
  - the sharp log power for integer α;
  - whether the rate changes for large r, where Lemma 1's smallness fails and ∇u_f may have several critical points.

=== END OF ANSWER round4_q1 ===
