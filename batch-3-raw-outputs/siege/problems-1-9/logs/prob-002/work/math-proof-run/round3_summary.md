# Running summary after round 2 (written at round 3 plan)

## Problem
Minimax L^2-squared rate for recovering f in F(alpha,r) (C^alpha ball of radius r around 1, r small, alpha>1) from Y = u_f + n^{-1/2}W, div(f grad u)=1 on the unit ball D in R^d (d>=2), u=0 on the sphere.

## Goal (ledger #1, OPEN)
Minimax rate = n^{-2alpha/(2alpha+d+3)} up to logs (lower bound + matching upper bound). This is slower than the naive "degree-one" rate n^{-2alpha/(2alpha+d+2)}: perturbations oscillating across the flow of grad u_f are smoothed by two degrees, those along it by one.

## Established
1. LOWER BOUND, PROVED (round1_q1; ledger #4; planner re-checked key steps; formal verify query sent in round 3 as round3_q4). For all alpha>1, d>=2, r in (0,1): inf sup E||hat f - f||^2 >= c n^{-2alpha/(2alpha+d+3)}. Construction: ~2^{j(d-1)} 2^{-j}-separated points on S^{d-1}, 0-homogeneous angular bumps Phi_k, h_k = kappa 2^{-j(alpha+2)} b(|x|) Delta Phi_k; key identity div(b Delta Phi_k x/d) = c(|x|) Delta Phi_k, c = (r b' + (d-2) b)/d; ||u_theta - u_theta'||_2 <= C 2^{-2j}||h_k||_2 via the exact identity u_g-u_f = -L_g^{-1}div(h V_f), H^2 duality, two integrations by parts onto Phi_k, drift W = grad(u_f-u_1) with ||W||_inf <= C 2^{-j(alpha+1-eps)} (W^{2,p} + L^p duality + Gagliardo-Nirenberg), absorbed since alpha>1; Assouad with 2^j ~ n^{1/(2alpha+d+3)}. The full text is in round1_q1.answer.md (lines 1-90) and is spliced verbatim in round3_q4.md.
2. Exact linearisation at f=1 (round1_q3): symbol (1+|xi_rad|)/|xi|^2; spectral variance n^{-1}2^{J(d+3)} (round1_q2).
3. Isotropic stability for V=x/d (round1_q4): ||T^{-1}G||_2 <= 2||G||_2.
4. Noise sup bounds (round2_q2 (iii), ledger new): E||D^m xi||_inf^2 <= C J 2^{J(d+2m)}.

## Upper-bound route (plug-in transport estimator) — status after round 2
Notation: T_V g := div(gV), inverted along the backward flow into the source: T_V^{-1}G(x) = int_0^inf G(Phi_{-s}x) exp(-int_0^s divV(Phi_{-sigma}x)dsigma) ds. Identities (checked by round2_q1): (I2) f = T_{grad v}^{-1}[1 + div(f grad(v-u_f))]; (I3) plug-in hat f = T_{grad hat u}^{-1}(1) satisfies hat f - f = -T_{grad hat u}^{-1}div(f grad(hat u - u_f)); (I4) (T_{V'}-T_V)Z = div(Z(V'-V)).
Smoother fixed by round2_q3: extend-then-convolve, K_J g = k_J*(Eg), E Seeley extension, k with vanishing moments 1..S, S>alpha+3. Estimator hat u = K_J Y, 2^J ~ n^{1/(2alpha+d+3)}, hat f = T_{grad hat u}^{-1}(1) on a good event, truncated to [1-r,1+r].
- Step 0 (round2_q3): T_{V_J}^{-1} bounded on L^inf and L^2 uniformly (L^2 via substitution y = Phi_{-s}x, Jacobian exp(-int div V)); no difficulty at the source; forcing supported in the boundary layer of width 2^{-J} gains a factor 2^{-J} (rays cross transversally).
- Variance (round2_q2, sketch level): E||Z_xi||_2^2 <= C 2^{J(d+3)} (times n^{-1}), E||grad Z_xi||_2^2 <= C 2^{J(d+5)}, pointwise E Z(x)^2 <= C 2^{J(d+3)} min(rho^{-1}, 2^J), rho = distance to the source x_J; the pointwise sup bound fails near the source but the L^2 bound holds since rho^{-1} is integrable for d>=2. Method: line measure mu_x on backward ray, flow facts (F1)-(F4), tube lemma, shell decomposition. Kernel hypotheses: |d^a k_J| <= C 2^{J(d+|a|)}, support 2^{-J}.
- Bias (round2_q3): exact identity on D: L_f b = div(V^E(F - k_J*F)) + div R + K_J G, R the bilinear commutator, G = div(F grad Eu) - 1 (zero on D). Parallel term gives O(2^{-J alpha}); div R = O(J 2^{-J alpha}) by Littlewood-Paley split and moment cancellation; K_J G supported in boundary layer, gains 2^{-J}. Result ||f_0 - f||_inf <~ J 2^{-J alpha}, modulo the cited extension fact (G in C^{alpha-1}, vanishing to order alpha-1 at the sphere; needed for alpha>2). Gradient bound ||grad(f_0-f)||_inf <~ J 2^{-J(alpha-1)} only sketched (differentiated transport system, zero-order matrix ~ (1+1/d)I).
- Remainder (planner, round 3, unverified; resolves round2_q1's alpha>5/4 worry): exact identity on the good event hat f - f = (f_0 - f) - Z_xi + T_{hat V}^{-1}div(Z grad xi), Z = T_{V_J}^{-1}div(f grad(b+xi)); remainder <~ ||grad Z||_2||grad xi||_inf + ||Z||_2||D^2 xi||_inf = O(J^2 2^{-J alpha}2^{-J(alpha-1/2)}). round2_q1 worried that T_{V_J}^{-1} on H^1 costs 2^{J(2-alpha)}; but round2_q2(ii)'s direct estimate of grad Z_xi already includes the D div V_J cost and still gives 2^{J(d+5)} since alpha>1. Bad event probability exp(-cJ^2), loss bounded by truncation.
So the upper bound is assembled at sketch level; what is missing is a single rigorous write-up.

## Dead ends
- LSE / M-estimation + isotropic stability + interpolation: only n^{-2(alpha-1)/(2alpha+d+2)} (round1_q4).
- Sample-split one-step route (round2_q4): pilot rates too weak for alpha near 1, iteration needs rate-preserving projection; abandoned in favour of the plug-in route.
- Pointwise uniform variance bound near the source (round2_q2): likely false, unnecessary.

## Open gaps
1. Rigorous variance lemma (L^2) for the extension smoother (new ledger line; round3_q2).
2. Extension fact and gradient bias bound (round3_q3).
3. Full assembly incl. remainder, V_J facts, uniformity (round3_q1).
4. Formal verify of the lower bound (round3_q4).

## Round 3 wave
q1 complete assembled upper-bound proof (attempt); q2 rigorous variance lemma (attempt); q3 rigorous bias lemma (attempt); q4 verify of lower bound round1_q1 (verify, not attempt).

## Next round should concentrate on
If round3_q1 (with q2, q3) yields a complete written upper-bound proof: write PROVED [GOAL] line citing round1_q1 (lower) and the upper-bound file, and send two verify queries carrying the complete chain (lower proof from round1_q1 plus the upper proof) verbatim. If q1 leaves a gap, aim the wave at that single lemma, reusing q2/q3 rigorous pieces.
