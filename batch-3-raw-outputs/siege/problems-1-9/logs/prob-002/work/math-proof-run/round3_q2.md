kind: attempt
Open question attempted: the VARIANCE LEMMA (ledger entry #5, in the L^2 form that the upper bound needs), stated precisely here for one fixed smoother, to be PROVED IN FULL RIGOUR (an earlier round gave the sketch spliced below; your job is a complete proof, or a precise counterexample/correction).

Setting. D unit ball in R^d, d >= 2; alpha > 1; r small; f in F(alpha,r); u = u_f; W Gaussian white noise on L^2(D). Smoother ("extend then convolve"): E a fixed linear Seeley-type extension operator (finite sum of reflections across the sphere with smooth weights; bounded C^s(D) -> C^s(R^d) for 0 < s <= S+2), k in C_c^infty(R^d) with int k = 1 and vanishing moments of orders 1..S, S > alpha+3, k_J = 2^{Jd}k(2^J .), K_J g := k_J * (E g) restricted to D. So K_J g(x) = int_D k_J(x,y) g(y) dy with k_J(x,y) := (E^* k_J(x - .))(y); xi := K_J W is the smooth Gaussian field xi(x) = <W, k_J(x,.)>. V_J := grad K_J u. Transport operator T_V g := div(gV), inverted by T_V^{-1}G(x) = int_0^infty G(Phi_{-s}x) exp(-int_0^s divV(Phi_{-sigma}x) dsigma) ds (Phi = flow of V). Set Z := T_{V_J}^{-1} div(f grad xi).

Claim to prove (constants depending only on alpha, d, r, k, E):
 (V1) E||Z||_{L^2(D)}^2 <= C 2^{J(d+3)};
 (V2) E||grad Z||_{L^2(D)}^2 <= C 2^{J(d+5)};
 (V3) E||D^m xi||_{L^infty(D)}^2 <= C J 2^{J(d+2m)}, m = 1,2,3, and P(||D^m xi||_inf > t 2^{J(d/2+m)}) <= C exp(-c t^2) for t >= C sqrt J.
Prove also every property of V_J you use (unique zero x_J in D, ||DV_J - I/d||_inf <= eps, ||D^2 V_J||_inf <= C 2^{J(2-alpha)_+}, V_J . nu >= c > 0 on the sphere so the backward flow maps D into D, the flow estimates (F1)-(F4) below), from Schauder theory for u_f (u_f in C^{alpha+1}(D) close to (|x|^2-1)/(2d)) and the properties of E and k. Check carefully: the kernel bounds |d_x^b d_y^a k_J(x,y)| <= C 2^{J(d+|a|+|b|)}, supp in |x-y| <~ 2^{-J}, for this E (reflected pieces); differentiation under the integral; the shell decomposition near the source x_J (where |V_J| -> 0 and the ray measure concentrates); that only an L^2 bound, not a sup bound, is claimed. If you find (V1) or (V2) false, give the correct power and say what fails.

=== EARLIER ROUND'S SKETCH (verbatim) ===
# Variance lemma: answer (round2_q2)

## Setting and assumptions on K_J
K_J f(x) = ∫ k_J(x,y) f(y) dy with: supp k_J(x,·) ⊂ B(x, C2^{-J}); |∂_y^a k_J(x,y)| ≤ C 2^{J(d+|a|)} for |a| ≤ 3, and the same for ∂_x^b ∂_y^a with 2^{J(d+|a|+|b|)} (true for interior convolution with a C^∞ compactly supported kernel, and for standard boundary-corrected local-polynomial kernels / boundary wavelets of the corresponding regularity). Only these size/support bounds are used, so the sphere costs nothing extra. Write x_J for the zero of V_J, ρ(y) = |y - x_J|.

Facts on V_J (from Schauder, α>1, r small, J large): ||DV_J - I/d||_∞ ≤ ε, div V_J ∈ [1-ε, 1+ε], ||D²V_J||_∞ ≤ C 2^{J(2-α)_+}, x_J the unique zero. Hence along the backward flow γ(s) = Φ_{-s}x:
 (F1) ρ(γ(s)) ∈ [e^{-(1/d+ε)s}, e^{-(1/d-ε)s}] ρ(x) (since (d/ds)ρ = -(γ-x_J)·V_J/ρ and V_J(y) = DV_J(·)(y-x_J));
 (F2) weight w(s) = exp(-∫_0^s div V_J) ≤ e^{-(1-ε)s};
 (F3) ||DΦ_{-s}|| ≤ e^{-(1/d-ε)s} (from d/ds DΦ_{-s} = -DV_J DΦ_{-s});
 (F4) the ray is radially monotone with radial speed ≥ c|γ'|, so the arclength of the ray inside any ball of radius δ is ≤ Cδ.
Consequently the measure μ_x := ∫_0^∞ w(s) δ_{γ(s)} ds has, on the piece of ray in the shell ρ ∈ [2^{-k-1}, 2^{-k}] ∩ (0, ρ(x)], arclength length ≲ 2^{-k} and arclength density ≲ (2^{-k}/ρ(x))^{d-1-Cε} / ρ(x) (by F1, F2: ds/dℓ ~ 1/ρ, w ~ (ρ/ρ(x))^{d(1±ε)}).

## (i) — PROVED in L^2 form; uniform sup form as stated is NOT proved (and the near-source loss is real)
Z(x) = ∫ div(f∇ξ)(γ(s)) w(s) ds = <W, K_J^* div(f∇μ_x)> (ξ smooth, differentiation under the integral; for the n-scaled noise multiply by n^{-1}). Using f∂_iμ = ∂_i(fμ) - (∂_i f)μ (f ∈ C^1), K_J^* div(f∇μ_x)(z) = Σ_i ∫ [∂²_{y_i} k_J(y... )] terms: it is a sum of ∫ ∂_y^a k_J(y,z) g_a(y) dμ_x(y), |a| ∈ {1,2}, |g_a| ≤ C.
Lemma (tube). For a piece P of the ray of length L ≥ 2^{-J} with arclength density ≤ m, the function F_P(z) = ∫_P ∂^a k_J(y,z) g(y) dμ is supported in the 2^{-J}-tube around P (volume ≲ L 2^{-J(d-1)}) and |F_P| ≤ C 2^{J(d+|a|)} · m · 2^{-J} by (F4). So ||F_P||_2^2 ≤ C m² L 2^{J(d+3)} (|a|=2 dominates). For a piece inside a ball of radius 2^{-J} with total mass M: ||F_P||_2 ≤ M ||∂^a k_J||_2 ≤ C M 2^{J(d/2+2)}.
Summing over shells (triangle inequality, geometric sums since 2d-1-Cε > 0): for ρ(x) ≥ 2^{-J},
 E Z(x)^2 = ||K_J^* div(f∇μ_x)||_2^2 ≤ C [Σ_k (2^{-k}/ρ(x))^{d-1/2-Cε} ρ(x)^{-1/2}]² 2^{J(d+3)} + C(2^{-J}/ρ(x))^{2d-Cε} 2^{J(d+4)} ≤ C 2^{J(d+3)} / ρ(x),
and for ρ(x) ≤ 2^{-J} (mass ≤ 1 in a 2^{-J}-ball): E Z(x)^2 ≤ C 2^{J(d+4)}. So
 **E Z(x)^2 ≤ C 2^{J(d+3)} min(ρ(x)^{-1}, 2^J)**, and since ∫_D ρ^{-1} dx < ∞ for d ≥ 2,
 **E||Z||_{L^2(D)}^2 ≤ C 2^{J(d+3)}** (no log). This is what the upper-bound route needs.
The sup bound sup_x E Z(x)^2 ≤ C J^K 2^{J(d+3)} is NOT proved: the tube bound near x is the dominant term and scales like 2^{J(d+3)}/ρ(x) (the ray from x has length ρ(x) and density ~1/ρ(x)); I expect this to be sharp, i.e. the pointwise variance genuinely blows up to order 2^{J(d+4)} within 2^{-J} of the source (a polynomial, not logarithmic, loss), but it is harmless in L^2 because d ≥ 2.

## (ii) — PROVED (sketch-level rigour, same method), in the form E||∇Z||_2^2 ≤ C 2^{J(d+5)}
∂_e Z(x) = ∫ [∇G(γ(s))·DΦ_{-s}(x)e] w ds + ∫ G(γ(s)) ∂_e w(s) ds, G = div(f∇ξ). First term: a measure of first derivatives along the ray with extra factor ||DΦ_{-s}|| ≤ (ρ(γ)/ρ(x))^{1-Cε} (F1, F3); tube lemma with |a| ≤ 3 gives ≤ C 2^{J(d+5)} min(ρ(x)^{-1}, 2^J). Second term: |∂_e w(s)| ≤ w(s) ∫_0^s |D div V_J| ||DΦ_{-σ}|| dσ ≤ C 2^{J(2-α)_+} w(s), giving ≤ C 2^{J(d+3)+2J(2-α)_+} min(ρ^{-1},2^J) ≤ C 2^{J(d+5)} min(...) since α > 1. (f∈C^1 suffices; ∇f only enters through the |a|=1 terms.) Integrating: E||∇Z||_2^2 ≤ C 2^{J(d+5)}. The sup form again only with the min(ρ^{-1},2^J) factor. No failure for α<2.

## (iii) — PROVED
D^mξ(x) = <W, ∂_x^m k_J(x,·)> is centered Gaussian with variance ≤ ||∂^m_x k_J(x,·)||_2^2 ≤ C 2^{J(d+2m)}, and x ↦ D^mξ(x) has Lipschitz-in-L^2(Ω) constant ≤ C 2^{J(d/2+m+1)}. On a grid of mesh 2^{-2J} (≤ C 2^{2Jd} points) the Gaussian maximal inequality gives E max² ≤ C J 2^{J(d+2m)}; the grid-to-continuum oscillation is controlled by Dudley's entropy bound (or by the same argument for D^{m+1}ξ with sup bound C 2^{J(d+2m+2)}J, times mesh² 2^{-4J}), giving E||D^mξ||_∞^2 ≤ C J 2^{J(d+2m)}, m=1,2,3.

## Summary
(i) L^2 version PROVED (E||Z||_2^2 ≤ C 2^{J(d+3)}); uniform pointwise version NOT PROVED, replaced by E Z(x)^2 ≤ C 2^{J(d+3)} min(|x-x_J|^{-1}, 2^J) (source costs a power 2^J pointwise but is integrable for d ≥ 2; sphere costs nothing). (ii) PROVED in L^2 form, same caveat pointwise. (iii) PROVED. Open: sharpness of the pointwise near-source blow-up; whether the remainder step (c) only needs L^2 bounds (it appears to, as written).

Context answer to the main problem (conjectured route, lower bound proved earlier): minimax rate n^{-2α/(2α+d+3)} up to logs.

