kind: attempt
Open question attempted: the UPPER BOUND half of the goal (ledger entries #3 and #7; the goal #1 is: the minimax rate is n^{-2alpha/(2alpha+d+3)} up to logs; the lower bound is already proved). Your task: write a COMPLETE, SELF-CONTAINED, RIGOROUS proof that the estimator described below satisfies sup_{f in F(alpha,r)} E||hat f - f||_{L^2(D)}^2 <= C (log n)^K n^{-2alpha/(2alpha+d+3)} for every alpha > 1, d >= 2 and every sufficiently small fixed r. All the ingredients have been sketched by earlier rounds (spliced in below: a variance lemma, a bias lemma, and the planner's remainder argument). Your job is to turn them into one finished proof that a referee could check line by line: state every lemma precisely, prove it (or cite a precise standard theorem with its hypotheses checked), fix the smoother once and for all (extend-then-convolve, as in the bias file) and make sure the variance lemma's kernel hypotheses really hold for that smoother, check the source neighbourhood, the sphere, uniformity of all constants over F(alpha,r), the bad event, and the exact decomposition. Where an ingredient below is wrong or only sketched, repair it or replace it. In particular check: (1) the facts about V_J used everywhere (unique zero, C^1-closeness to x/d, ||D^2 V_J||_inf <~ 2^{J(2-alpha)_+}, outward transversality on the sphere so the backward flow stays in D) for the extend-then-convolve smoother; (2) the extension fact cited from memory in the bias file (G = div(F grad Eu) - 1 is C^{alpha-1} on R^d and vanishes to order alpha-1 at the sphere from outside) — prove it or avoid it (e.g. by another choice of E, or by bounding the boundary-layer term differently); (3) the gradient bound for the bias, sketched in Step 2 of the bias file; (4) the L^2 variance bounds for Z and grad Z, which the variance file argues at sketch level; (5) the remainder argument. End with a clear verdict: PROVED (with the exact rate and log power) or NOT PROVED (with the single precise remaining lemma).

=== BACKGROUND: notation, transport operator, exact identities, the proved lower bound ===

Notation. L_g w := div(g grad w) with Dirichlet condition on the unit sphere; u_g := the solution of L_g u = 1, u = 0 on the boundary; V_g := grad u_g. For g = 1: u_1 = (|x|^2-1)/(2d), V_1 = x/d. For g in F(alpha,r), r small, u_g is C^{alpha+1}-close to u_1 (Schauder), so V_g is C^alpha-close to x/d: it has exactly one zero x_g (a hyperbolic source, D V_g(x_g) close to I/d, div V_g close to 1 > 0), every flow line leaves the source and exits the sphere transversally (V_g . nu close to 1/d). White noise convention: <Y,phi> = <u_f,phi> + n^{-1/2} <W,phi>, <W,phi> ~ N(0, ||phi||_2^2).

Transport operator. For a C^1 vector field V of this type, T_V g := div(g V) = V.grad g + g div V. The equation T_V g = G has exactly one bounded solution (uniqueness: along a flow line a homogeneous solution grows like exp(int div V) when followed backwards into the source, so a bounded one vanishes), namely
   T_V^{-1}G(x) = int_0^infty G(Phi_{-s} x) exp( - int_0^s divV(Phi_{-sigma} x) d sigma ) ds,   Phi_t = flow of V.
For V = x/d this is T^{-1}G(x) = d int_0^1 t^{d-1} G(t x) dt, and ||T^{-1}G||_{L^2(D)} <= 2 ||G||_{L^2(D)}. T_V^{-1} integrates G along the backward ray from x to the source; it gains one derivative ALONG the flow and nothing across it.

Exact identities (elementary, checked):
 (I1) For f, g: u_g - u_f = -L_g^{-1} div((g-f) V_f).
 (I2) For f in F(alpha,r) (so f in C^1) and ANY C^2 function v whose gradient field V = grad v is of the above type: f = T_V^{-1}[ div(f grad v) ] = T_V^{-1}[ 1 + div(f grad(v - u_f)) ] pointwise on D (no boundary condition is involved).
 (I3) Plug-in estimator: if hat u is any C^2 estimate of u_f with hat V = grad hat u of the above type, and hat f := T_{hat V}^{-1}(1), then exactly
        hat f - f = - T_{hat V}^{-1}[ div(f grad e) ],   e := hat u - u_f.
 (I4) Resolvent identity: T_{V'}^{-1} - T_V^{-1} = - T_{V'}^{-1} (T_{V'} - T_V) T_V^{-1}, and (T_{V'} - T_V)Z = div(Z (V' - V)).

PROVED LOWER BOUND (round 1). For all alpha>1, d>=2, r in (0,1): inf_{hat f} sup_{f in F(alpha,r)} E||hat f - f||_2^2 >= c n^{-2alpha/(2alpha+d+3)}. Construction: Phi_k = 0-homogeneous extensions of disjoint angular bumps at scale 2^{-j} on the sphere (about 2^{j(d-1)} of them), h_k = kappa 2^{-j(alpha+2)} b(|x|) Delta Phi_k with b a fixed bump on (1/4,3/4); div(h_k x/d) = kappa 2^{-j(alpha+2)} c(|x|) Delta Phi_k with c = (r b' + (d-2) b)/d, so by duality ||Delta^{-1}-type response|| <= C 2^{-2j}||h_k||_2 (two integrations by parts move the Laplacian onto the test function); the non-radial drift of V_{f_theta} is O(2^{-j(alpha+1-eps)}) in sup norm and is absorbed; Assouad with 2^j ~ n^{1/(2alpha+d+3)} gives the bound. Also, for f = 1 and h = a(r) Y_l (spherical harmonic of degree l, radial profile of radial frequency mu), ||Dh||_2 ~ (1+mu) / (mu^2 + l^2) ||h||_2: the linearised forward symbol is ~ (1+|xi_radial|)/|xi|^2. Spectral count: variance n^{-1} int_{|xi|<=2^J} |xi|^4 (1+|xi_rad|)^{-2} dxi ~ n^{-1} 2^{J(d+3)}, bias^2 2^{-2J alpha}, balanced at the conjectured rate n^{-2alpha/(2alpha+d+3)}.


=== PLANNER'S REMAINDER ARGUMENT AND ASSEMBLY (round 3) ===
PLANNER'S REMAINDER ARGUMENT (round 3; to be checked, it is meant to remove the restriction alpha > 5/4 that an earlier attempt worried about).
Estimator: hat u := K_J Y with the extend-then-convolve smoother of the bias file below (K_J g = k_J * (E g)), 2^J ~ n^{1/(2alpha+d+3)}, hat V := grad hat u, hat f := T_{hat V}^{-1}(1) on the event A := {||D^m xi||_inf <= n^{-1/2} 2^{J(d/2+m)} J, m=1,2} (where xi := n^{-1/2} K_J W, so hat V = V_J + grad xi with V_J := grad K_J u), hat f := 1 off A; finally truncate to [1-r, 1+r] (this can only reduce |hat f - f| pointwise since f takes values in [1-r,1+r]).
Since n^{-1/2} 2^{J(d/2+2)} = 2^{-J(alpha - 1/2)} -> 0, on A the field hat V is C^1-close to x/d, so T_{hat V}^{-1} is bounded on L^2(D) uniformly (Jacobian argument of Step 0 in the bias file). P(A^c) <= exp(-c J^2) (Gaussian concentration / Borell-TIS from the sup bounds (iii) in the variance file), and off A the loss is <= 4r^2|D|, so A^c contributes O(exp(-cJ^2)) = o(n^{-1}).
Exact decomposition on A. Put b := K_J u - u, e := b + xi = hat u - u, Z := T_{V_J}^{-1} div(f grad e) = Z_b + Z_xi (bias part Z_b = -(f_0 - f) with f_0 := T_{V_J}^{-1}1, variance part Z_xi := T_{V_J}^{-1} div(f grad xi)). Since T_{hat V} Z = T_{V_J} Z + div(Z grad xi) and, by (I3), T_{hat V}(hat f - f) = -div(f grad e), we get T_{hat V}(hat f - f + Z) = div(Z grad xi), i.e. EXACTLY
     hat f - f = -Z_b - Z_xi + T_{hat V}^{-1} div(Z grad xi)
(uniqueness of bounded solutions; Z is bounded since V_J is smooth).
Remainder: ||T_{hat V}^{-1} div(Z grad xi)||_2 <= C(||grad Z||_2 ||grad xi||_inf + ||Z||_2 ||D^2 xi||_inf).
Inputs: (bias file) ||Z_b||_inf <~ J 2^{-J alpha}, ||grad Z_b||_inf <~ J 2^{-J(alpha-1)}; (variance file, with the noise factor n^{-1}) E||Z_xi||_2^2 <~ n^{-1} 2^{J(d+3)} = 2^{-2J alpha}, E||grad Z_xi||_2^2 <~ n^{-1} 2^{J(d+5)} = 2^{-2J(alpha-1)} (this direct bound already contains the cost ||D div V_J||_inf <~ 2^{J(2-alpha)_+}, absorbed because alpha > 1 — so no H^1-mapping bound for T_{V_J}^{-1} with an extra 2^{J(2-alpha)} is needed); (sup bounds) on A, ||grad xi||_inf <= 2^{-J(alpha+1/2)} J and ||D^2 xi||_inf <= 2^{-J(alpha - 1/2)} J.
Hence E[1_A ||remainder||_2^2] <~ J^4 (2^{-2J(alpha-1)} 2^{-J(2alpha+1)} + 2^{-2J alpha} 2^{-J(2alpha-1)}) = J^4 2^{-2J alpha} 2^{-J(2alpha-1)} = o(2^{-2J alpha}) for every alpha > 1/2 (the indicator lets one use the deterministic bounds on A, so no moment decoupling is needed).
Total: sup_{F(alpha,r)} E||hat f - f||_2^2 <~ J^2 2^{-2J alpha} ~ (log n)^2 n^{-2alpha/(2alpha+d+3)}.

=== VARIANCE FILE (earlier round's answer, verbatim) ===
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


=== BIAS FILE (earlier round's answer, verbatim) ===
# Bias lemma (round2_q3)

**Answer to the problem.** The conjectured minimax rate is n^{-2α/(2α+d+3)}, up to log factors. The lower bound is the one proved in round 1. This file proves the bias half of the upper-bound route, for a specific smoother: **extend first, then convolve**.

## Setup and choice of smoother
- E is a linear Seeley/Stein-type extension operator from D to R^d. It is bounded C^s(D) -> C^s(R^d) for 0<s<=S+2 (Hölder-Zygmund scale), and it is a finite sum of reflections across the sphere with smooth weights.
- k is a compactly supported kernel with ∫k = 1 and vanishing moments of orders 1..S, S > α+3. Set k_J = 2^{Jd} k(2^J ·) and K_J g := k_J * (E g).
- Applied to the data: K_J Y(x) = <Y, E^*k_J(x-·)>. Here E^* is a finite sum of weighted pullbacks, so E^*k_J(x-·) is in L^2(D). Hence this is a linear map of the data and does not depend on f.
- Notation: U := E u, F := E f, V^E := ∇U. Then F, V^E ∈ C^α(R^d), with norms ≲ 1, because u ∈ C^{α+1} by Schauder in the Zygmund scale.
- Define G := div(F V^E) - 1 on R^d. Then G ≡ 0 on D and G ∈ C^{α-1}(R^d). Hence |G(y)| ≲ dist(y,D)^{min(α-1,1)}, and in any case |G| ≲ 1.

## Step 0: T_{V_J}^{-1} is bounded on L^∞ and L^2, uniformly (including near the source)
- We have ||V_J - V||_{C^1} = ||∇(K_J u - u)||_{C^1} ≲ 2^{-J(α-1)} → 0. So for J large, V_J is C^1-close to x/d: div V_J ≥ 1-δ, and V_J·ν > 0 on the sphere. Therefore the backward flow Φ_{-s} maps D into D for all s ≥ 0.
- L^∞ bound: |T^{-1}H(x)| ≤ ||H||_∞ ∫_0^∞ e^{-(1-δ)s} ds.
- L^2 bound: substitute y = Φ_{-s}x, whose Jacobian is det DΦ_{-s} = exp(-∫_0^s div V_J). This gives
  ||H∘Φ_{-s} · e^{-∫div}||_{L^2(D)} ≤ e^{-(1-δ)s/2} ||H||_2,
  so ||T^{-1}||_{L^2→L^2} ≤ 2/(1-δ).
- Neither bound needs |V| bounded away from 0. The source therefore causes no difficulty.
- Localisation: if H is supported in the layer {1 - c2^{-J} < |x| < 1}, then every backward ray crosses that layer transversally (V_J·ν ≥ c) and spends time ≲ 2^{-J} in it. Hence ||T^{-1}H||_∞ ≲ 2^{-J} ||H||_∞.

## Step 1: exact identity on D
1. On D: div(f K_J V^E) = div(f ∇K_J u), since K_J commutes with ∇ on R^d.
2. On D: div(K_J(F V^E)) = K_J(div(F V^E)) = K_J(1+G) = 1 + K_J G, using K_J 1 = 1.
3. Hence, on D,
   L_f b = div(f ∇K_J u) - 1 = div R + V-term + K_J G,
   where f K_J V^E - K_J(F V^E) = V^E(x)(F - k_J*F)(x) + R(x), with
   R(x) := ∫ k_J(x-y)(F(x)-F(y))(V^E(y)-V^E(x)) dy.
4. By (I3), f_0 - f = -T_{V_J}^{-1}[L_f b]. So there are three contributions.

**(i) The term parallel to V.** Let g := F - k_J*F, so ||g||_∞ ≲ 2^{-Jα} and ||∇g||_∞ ≲ 2^{-J(α-1)}. Then
- div(gV) = T_{V_J} g - div(g ∇b), so T_{V_J}^{-1} div(gV) = g - T_{V_J}^{-1} div(g ∇b).
- ||div(g∇b)||_∞ ≲ 2^{-J(α-1)} · 2^{-Jα} + 2^{-Jα} · 2^{-J(α-1)}.
- Total contribution: O(2^{-Jα}).

**(ii) The commutator R.** Split F = F_L + F_H and V^E = V_L + V_H by a Littlewood–Paley cutoff at frequency 2^J. The pieces satisfy:
- ||F_H||_∞ ≲ 2^{-Jα} and ||∇F_H||_∞ ≲ 2^{-J(α-1)};
- ||D^m F_L||_∞ ≲ 1 for m < α, ≲ J for m = α, and ≲ 2^{J(m-α)} for m > α;
- the same bounds hold for V.

R is bilinear in (F, V^E). Bound each part:
- R(F_H, V^E) and R(F_L, V_H): one increment is at most 2^{-Jα}, the other is at most |x-y| ≲ 2^{-J}. So each is O(2^{-J(α+1)}). One x-derivative costs at most 2^J (on the kernel), or else hits an increment factor directly. So the divergence is O(2^{-Jα}).
- R(F_L, V_L): Taylor-expand both increments to total order S. Every monomial (y-x)^γ with 2 ≤ |γ| ≤ S integrates to 0 against k_J. The remainder has terms D^m F_L · D^{S+1-m} V_L · |x-y|^{S+1} with 1 ≤ m ≤ S. These are ≲ J 2^{J(m-α)_+} 2^{J(S+1-m-α)_+} 2^{-J(S+1)} ≲ J 2^{-J(α+1)}. The worst cases are m = 1 or S+1-m = 1. Derivatives are handled the same way.

So ||div R||_∞ ≲ J 2^{-Jα}, and by Step 0, ||T^{-1} div R||_∞ ≲ J 2^{-Jα}.

**(iii) The boundary term K_J G.** Since G vanishes on D, on D the term K_J G is supported in a layer of width ≲ 2^{-J}, and |K_J G| ≲ 2^{-J min(α-1,1)}.
- By the localisation in Step 0: ||T^{-1}K_J G||_∞ ≲ 2^{-J} 2^{-J min(α-1,1)}.
- For α ≤ 2 this is 2^{-Jα}.
- For α > 2 the crude bound is only 2^{-2J}. The fix is to choose E of order S, so that G is C^{α-1} and vanishes on D; then |G(y)| ≲ dist(y,D)^{α-1} near ∂D. This holds because all derivatives of G of order < α-1 vanish on ∂D (taken from the inside, where G ≡ 0) and G ∈ C^{α-1}. Hence |K_J G| ≲ 2^{-J(α-1)} in the layer, and ||T^{-1}K_J G||_∞ ≲ 2^{-Jα}.

**Conclusion of Step 1.** ||f_0 - f||_{L^∞(D)} ≲ J 2^{-Jα}, and therefore also in L^2.

## Step 2: gradient bound (sketch-level, but routine)
Let w := f_0 - f, which solves T_{V_J} w = H. Differentiating gives a transport system for ∇w:
V_J·∇(∂_i w) + Σ_j (∂_i V_j^J + δ_ij div V_J) ∂_j w = ∂_i H - w ∂_i div V_J.
- The zero-order matrix is close to (1+1/d)I and positive definite. So the same Duhamel argument as in Step 0 bounds the solution, in L^∞ and in the layer.
- Forcing terms: ||w ∂ div V_J||_∞ ≲ J 2^{-Jα} 2^{J(2-α)_+} ≲ J 2^{-J(α-1)} (using α ≥ 1).
- ∇ of the terms (i) and (ii) is ≲ J 2^{-J(α-1)}, by the same estimates with one more derivative.
- ∇K_J G is ≲ 2^{-J(α-2)} in the layer; after the layer gain it is ≲ 2^{-J(α-1)}.

Hence ||∇(f_0 - f)||_∞ ≲ J 2^{-J(α-1)}.

## Status
- **PROVED, with K = 1:** the bias lemma for the extend-then-convolve smoother. Step 1 is fully argued.
- **Not fully written out:**
  - the Step 2 gradient bound, which is only sketched;
  - the claim that E can be chosen so that G = div(F∇Eu) - 1 lies in C^{α-1}(R^d) with the boundary decay stated. Standard extension theory gives this, but I am citing it from memory.
- **Open, outside this task:** the variance part (a) and the remainder part (c) of the upper bound, so the minimax upper bound itself is still open in this file.

