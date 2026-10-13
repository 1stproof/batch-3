kind: attempt
Open question attempted: the BIAS LEMMA (ledger entry #6), to be PROVED IN FULL RIGOUR for the extend-then-convolve smoother (an earlier round's answer, spliced below, proved the sup-norm half modulo one extension fact cited from memory, and only sketched the gradient half).

Claim to prove (constants depending only on alpha, d, r, the kernel k and the extension E; J large): for every f in F(alpha,r), with u = u_f, V_J := grad K_J u, f_0 := T_{V_J}^{-1}(1) (unique bounded solution of div(f_0 V_J) = 1 on D),
 (B1) ||f_0 - f||_{L^infty(D)} <= C J 2^{-J alpha};
 (B2) ||grad(f_0 - f)||_{L^infty(D)} <= C J 2^{-J(alpha-1)}   (an L^2(D) version of (B2) suffices for the application if L^infty is hard).
Specific tasks: (a) the extension fact used in part (iii): with U = Eu, F = Ef, G := div(F grad U) - 1, prove G in C^{alpha-1}(R^d) and |G(y)| <= C dist(y,D)^{alpha-1} near the sphere (for all alpha > 1, including integer alpha in the Zygmund scale and alpha > 2) — or replace this step by an argument that does not need it (e.g. a different extension, or extending f and u jointly so that the equation holds to high order outside D, or bounding the boundary-layer term in L^2 using that backward rays cross the layer of width 2^{-J} transversally); (b) a complete proof of (B2), including the zero-order matrix of the differentiated transport system, the source (where V_J vanishes), the boundary layer, and the cost ||D^2 V_J||_inf <~ 2^{J(2-alpha)_+} for alpha < 2; (c) check the Littlewood-Paley/Taylor bookkeeping in part (ii) of the commutator, including the x-derivative needed for div R and integer alpha (Zygmund, where log factors J appear); (d) check Step 0 (L^infty and L^2 boundedness of T_{V_J}^{-1}, the localisation gain 2^{-J} for forcing supported in the boundary layer). If something fails, give the correct bound and say exactly what it costs.

=== EARLIER ROUND'S ANSWER (verbatim) ===
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

