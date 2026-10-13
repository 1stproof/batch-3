# Round 3, q3: bias lemma for the extend-then-convolve smoother

**Answer to the problem (unchanged conjecture).** The minimax rate is n^{-2α/(2α+d+3)}, up to log factors. The lower bound comes from earlier rounds. This file proves only the bias lemma (B1) and (B2).

**Conventions.**
- For a function g on R^d, write k_J*g for plain convolution, and K_J u := k_J*(Eu).
- The kernel k has compact support in B(0,c₀), ∫k = 1, and ∫k(z)z^γ dz = 0 for 1 ≤ |γ| ≤ S, with S > α+3.
- E is a Seeley/Stein extension, bounded C^s(D̄) → C^s(R^d) for 0 < s ≤ α+1 in the Hölder–Zygmund scale. This boundedness is cited from memory, as standard.
- Schauder theory in the Zygmund scale gives u ∈ C^{α+1}(D̄) with norm ≲ 1. This is also cited from memory; for integer α it is the Zygmund-scale version.
- Set U = Eu, F = Ef, V := ∇U, b := K_J u − u on D, and V_J = ∇K_J u = V + ∇b on D.

## (a) The extension fact: proved, for every α > 1, integer values included

**Lemma A.** Let G := div(F∇U) − 1 on R^d. Then G ∈ C^{α−1}(R^d), G ≡ 0 on D̄, and |G(y)| ≤ C dist(y,D)^{α−1} for dist(y,D) ≤ 1/4.

*Proof.*
1. F ∈ C^α and ∇U ∈ C^α. Hölder–Zygmund spaces of positive order are algebras, so F∇U ∈ C^α. Taking the divergence gives G ∈ C^{α−1}.
2. G = 0 in the interior of D by the PDE, and on D̄ by continuity.
3. Let s = α−1 > 0 and m = ⌊s⌋+1. We use the standard equivalent norm sup_{x,h} |Δ_h^m G(x)| / |h|^s (cited from memory). It is valid for integer s too (Zygmund case).
4. Take y outside D with t = dist(y,D) small. Let x₀ = y/|y| ∈ ∂D, ν = x₀, h = tν. The points x₀ + (j−m+1)h for j = 0..m−1 lie on the inward normal segment of length (m−1)t, which is inside D̄ for t small. So G vanishes at all of them.
5. Hence G(y) = G(x₀+h) = Δ_h^m G(x₀ − (m−1)h), and therefore |G(y)| ≤ C t^s. ∎

This step needs no Taylor expansion and produces no log loss, even for integer α.

**Consequence.**
- For x ∈ D, (k_J*G)(x) = 0 unless dist(x,∂D) < c₀2^{−J}.
- In that layer, |k_J*G| ≤ C 2^{−J(α−1)}.
- Also |∇(k_J*G)| = |(∇k_J)*G| ≤ C 2^{−J(α−2)}.

## The identity (checked)

1. On D, div(f_0 V_J) = 1 and div(fV_J) − 1 = div(f∇b). So T_{V_J}(f_0 − f) = −div(f∇b).
2. On D, ∇K_J u = k_J*V. A direct computation gives
   f(k_J*V) − k_J*(FV) = V(x)·g(x) + R(x),
   where g := F − k_J*F and R(x) := ∫k_J(x−y)(F(x)−F(y))(V(y)−V(x)) dy.
3. Also div(k_J*(FV)) = k_J*(1+G) = 1 + k_J*G.
4. Hence

   **f_0 − f = −T^{-1}div(gV) − T^{-1}div R − T^{-1}(k_J*G).**

## (d) Step 0: checked

**Flow and boundary behaviour.**
- ‖V_J − V‖_{C^1(D)} ≲ 2^{−J(α−1)}, with an extra factor J if α = 2. V = ∇u is C^1-close to x/d because f is C^α-close to 1 (r small).
- Hence div V_J ≥ 1−δ, and V_J·x/|x| ≥ c > 0 on {|x| > 1/2}.
- So the backward flow Φ_{−s} keeps D invariant, and |Φ_{−s}x| is strictly decreasing while |Φ_{−s}x| > 1/2.

**Duhamel formula.** The unique bounded solution is
  w(x) = ∫_0^∞ H(Φ_{−s}x) e^{−∫_0^s div V_J(Φ_{−σ}x) dσ} ds.

**Bounds on T^{-1}.**
- L^∞: ‖T^{-1}‖_{L^∞→L^∞} ≤ 1/(1−δ).
- L^2: change variables using the Jacobian e^{−∫div}, as in the earlier answer.
- Neither bound uses a lower bound on |V_J|, so the source (the zero of V_J) causes no difficulty.

**Localisation.** Suppose H is supported in the layer L_J = {1 − c₀2^{−J} < |x| < 1}.
- A backward ray started at x is radially monotone there, so it meets L_J in a single time interval.
- That interval has length ≤ c₀2^{−J}/c.
- Hence ‖T^{-1}H‖_∞ ≤ C 2^{−J}‖H‖_∞.

## (B1): proved

**(i) The term from g.**
- Since T_{V_J}g = div(gV) + div(g∇b), we have T^{-1}div(gV) = g − T^{-1}div(g∇b).
- Bounds on g: ‖g‖_∞ ≲ 2^{−Jα} and ‖∇g‖_∞ ≲ 2^{−J(α−1)}. Bounds on b: ‖∇b‖_∞ ≲ 2^{−Jα} and ‖D²b‖_∞ ≲ 2^{−J(α−1)}.
- Hence ‖div(g∇b)‖_∞ ≲ 2^{−J(2α−1)}, and this term contributes O(2^{−Jα}).

**(ii) The commutator R: bookkeeping checked.** Write F = F_L + F_H and V = V_L + V_H by a Littlewood–Paley cut at frequency 2^J.

*High-frequency parts.*
- In R(F_H,V) and R(F_L,V_H), one increment is ≲ 2^{−Jα} and the other is ≲ |x−y| ≲ 2^{−J}. Here we use ‖∇V‖_∞ = ‖D²U‖_∞ ≲ 1 and ‖∇F_L‖_∞ ≲ 1, which need α > 1.
- So each of these terms is O(2^{−J(α+1)}).

*Low-frequency part R(F_L,V_L).*
- Taylor-expand each increment to order S with remainder.
- Products of monomials of total degree between 2 and S integrate to zero against k_J.
- The surviving terms have the form D^βF_L·D^γV_L·|h|^{|β|+|γ|}, with |β|, |γ| ≥ 1 and |β|+|γ| > S, or are remainder terms.
- Use ‖D^mF_L‖_∞ ≲ 2^{J(m−α)_+}, with a factor J when m = α. The exponent is then −J(|β|+|γ|) + J(|β|−α)_+ + J(|γ|−α)_+ ≤ −J(α+1) in every case.
- So R(F_L,V_L) = O(J² 2^{−J(α+1)}). The factor J² occurs only for integer α.

*Derivatives.*
- One x-derivative costs at most 2^J, whether it falls on k_J or on an increment. So ‖div R‖_∞ ≲ J² 2^{−Jα}.
- Two x-derivatives give ‖∇div R‖_∞ ≲ J² 2^{−J(α−1)}.

**(iii) The boundary term.** By Lemma A and the localisation in Step 0, ‖T^{-1}(k_J*G)‖_∞ ≲ 2^{−J}·2^{−J(α−1)} = 2^{−Jα}.

**Total.** ‖f_0 − f‖_∞ ≲ J² 2^{−Jα}. This is J² rather than J, which is harmless up to logs; it is J⁰ for non-integer α.

## (B2) / (b): proved

Let w = f_0 − f and T_{V_J}w = H. Differentiate the Duhamel formula; V_J is smooth for fixed J, so the flow is C^1. Then p = ∇w solves

  V_J·∇p + A p = ∇H − w∇div V_J,   with A = (DV_J)^T + (div V_J)I,

and p is given by the matching matrix Duhamel formula.

**Duhamel bound for the system.**
- We have |DΦ_{−s}| ≤ e^{(1/d+δ)s}, against the weight e^{−(1−δ)s}.
- Since d ≥ 2, the net rate is e^{−(1−1/d−2δ)s}, which is integrable, uniformly near the source.
- So the system has L^∞ bound ≲ ‖forcing‖_∞, and the same 2^{−J} gain for forcing supported in L_J.

**Forcing terms.**
- ‖D³K_J u‖_∞ ≲ 2^{J(2−α)_+} (times J if α = 2). Hence ‖w∇div V_J‖_∞ ≲ J² 2^{−Jα}·J 2^{J(2−α)_+}, which is ≲ J³ 2^{−J(α−1)} since α > 1.
- Term (i): ∇g ≲ 2^{−J(α−1)}. Also ∇div(g∇b) ≲ (D²g·∇b + ∇g·D²b + g·D³b) ≲ 2^{−J(α−1)}.
- Term (ii): ∇div R ≲ J² 2^{−J(α−1)}.
- Term (iii): ∇(k_J*G) ≲ 2^{−J(α−2)} on L_J. After the layer gain this is 2^{−J(α−1)}.

**Conclusion.** ‖∇(f_0 − f)‖_{L^∞(D)} ≲ J³ 2^{−J(α−1)}, which is (B2) up to a power of J. For non-integer α ≠ 2 the J factors disappear.

## Status

**Proved here**, citing from memory only:
- E bounded on the Hölder–Zygmund scale;
- Schauder estimates in the Zygmund scale;
- Hölder–Zygmund spaces are algebras;
- the difference-norm characterisation.

**What is proved:**
- (B1) with J² in place of J. The extra factor occurs only for integer α.
- (B2) with J³ in place of J.
- The extension fact, Lemma A, which had been cited from memory in round 2. It is now proved by a finite-difference argument, with no log loss.

**Corrections to the earlier answer:**
- The log powers are J² and J³, not J.
- K_J acting on R^d functions must be read as plain convolution k_J*.

**Still open:**
- the variance and remainder parts of the upper bound;
- uniqueness of the bounded transport solution, which is asserted, not reproved;
- so the minimax upper bound n^{−2α/(2α+d+3)} remains conjectural.

=== END OF ANSWER round3_q3 ===
