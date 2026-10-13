# Running summary after round 1 (written at round 2 plan)

## Problem
Minimax L^2-squared rate for recovering f in F(alpha,r) (C^alpha ball of radius r around 1, r small, alpha>1) from Y = u_f + n^{-1/2}W, div(f grad u)=1 on the unit ball D in R^d (d>=2), u=0 on the boundary.

## Goal (ledger #1, OPEN)
Minimax rate = n^{-2alpha/(2alpha+d+3)} up to logs (lower bound + matching upper bound). Note: this is slower than the "degree-one" rate n^{-2alpha/(2alpha+d+2)} one might naively expect; the reason is that perturbations oscillating across the flow of grad u_f are smoothed by two degrees, those along it by one.

## Established
1. LOWER BOUND, PROVED (round1_q1; ledger entry 4, planner re-checked). For all alpha>1, d>=2, r in (0,1): inf sup E||hat f - f||^2 >= c n^{-2alpha/(2alpha+d+3)}. Construction: choose ~2^{j(d-1)} 2^{-j}-separated points on S^{d-1}, angular bumps Phi_k (0-homogeneous extensions), h_k = kappa 2^{-j(alpha+2)} b(|x|) Delta Phi_k = kappa 2^{-j alpha} b|x|^{-2} chi_k(x/|x|), chi_k = 2^{-2j} Delta_S Phi_k; f_theta = 1 + sum theta_k h_k in F(alpha,r) for kappa small. Key identity: div(b Delta Phi_k x/d) = c(|x|) Delta Phi_k with c = (r b' + (d-2) b)/d (Delta Phi_k is (-2)-homogeneous). Key estimate ||u_theta - u_theta'||_2 <= C 2^{-2j}||h_k||_2 via: exact identity u_g-u_f = -L_g^{-1}div(h V_f); duality with psi = L_g^{-1}phi, ||psi||_{H^2}<=C; radial part integrated by parts twice onto Phi_k (||Phi_k||_{L^2(annulus)} ~ 2^{-j(d-1)/2}); drift W = grad(u_f - u_1) has ||W||_inf <= C 2^{-j(alpha+1-eps)} (W^{2,p} bound 2^{-j alpha}, L^p bound 2^{-j(alpha+2)} by duality, Gagliardo-Nirenberg), absorbed because alpha>1. KL = n/2 ||u-u'||^2 <= C n 2^{-j(2alpha+d+3)}; Assouad with 2^j ~ n^{1/(2alpha+d+3)}. Cited from memory: GT 8.12/8.13 (H^2), GT 9.15/9.17 (W^{2,p}), Assouad (Tsybakov 2.12), GN. Section 4 of round1_q1: bumps at the source, isotropic wavelets, radial oscillation all give faster (weaker) lower bounds. Planner's shell analysis: perturbations at distance rho from the source contribute less (rho^d (n rho)^{-2alpha/(...)}), so no log loss from the source.
2. Exact linearisation at f=1 (round1_q3): h = a(r)Y_l: div(h x/d) = (1/d) r^{1-d}(r^d a)' Y_l; ||Dh|| ~ l^{-2}||h|| for fixed profile, ~ mu/(mu^2+l^2) for radial frequency mu. Symbol (1+|xi_rad|)/|xi|^2; spectral variance n^{-1}2^{J(d+3)} (round1_q2 checked this integral; near the source the factor rho^{-1} is integrable for d>=2).
3. Isotropic stability for V = x/d (round1_q4, Lemma 1): T^{-1}G(x) = d int_0^1 t^{d-1}G(tx)dt, ||h||_2 <= 2||G||_2; consequently ||f1-f2||_2 <~ ||u1-u2||_{H^2} (general V only sketched).
4. Flux identity (round1_q2): int_{T_A cap {u=t}} f|grad u| dS = |Omega_t| over flow tubes.

## Dead ends
- LSE / M-estimation + isotropic stability + interpolation: only n^{-2(alpha-1)/(2alpha+d+2)} (round1_q4), strictly slower; isotropic arguments cannot reach the target. Conditional-stability/interpolation arguments generally use the worst direction and will not give the mixed rate.
- One-step correction with an H^1-type remainder bound needs alpha >= 2 (planner's computation) unless the anisotropic smallness of grad(u_{tilde f} - u_f) is used.

## Planner's upper-bound route (round 2 plan; heuristic, ledger entries 5-7 OPEN)
Notation: T_V g := div(gV), inverted (unique bounded solution) by integrating along the backward flow into the source: T_V^{-1}G(x) = int_0^inf G(Phi_{-s}x) exp(-int_0^s divV(Phi_{-sigma}x)dsigma) ds.
Exact identities: (I2) f = T_{grad v}^{-1}[1 + div(f grad(v - u_f))] for any suitable v; (I3) plug-in hat f = T_{grad hat u}^{-1}(1) satisfies hat f - f = -T_{grad hat u}^{-1} div(f grad(hat u - u_f)); (I4) resolvent identity, (T_{V'} - T_V)Z = div(Z(V'-V)).
Plug-in with hat u = K_J Y, 2^J ~ n^{1/(2alpha+d+3)}; reference field V_J = grad K_J u (deterministic, smooth):
  hat f - f = -T_{V_J}^{-1}div(f grad b) [bias] - T_{V_J}^{-1}div(f grad xi) [variance] + T_{hat V}^{-1}div(Z grad xi) [remainder], b = K_J u - u, xi = n^{-1/2}K_J W, Z = T_{V_J}^{-1}div(f grad(b+xi)).
  Variance: pointwise representer = smoothed weighted line measure along the backward ray; tube radius 2^{-J}, two transverse derivatives: 2^{J(d+3)}.
  Bias: interior L_f b = div([f,K_J]V), [f,K_J]V = V(f - K_J f) + int k_J(x-y)(f(x)-f(y))(V(y)-V(x))dy; first term parallel to V (T^{-1}div(gV) = g), second O(2^{-J(alpha+1)}) after moment cancellation. Boundary layer and source need care.
  Remainder: o(2^{-J alpha}) if ||grad Z||_2 <~ 2^{J(1-alpha)}, given sup bounds on D xi, D^2 xi (needs alpha > 1/2).
Alternative route (round2_q4): sample splitting, pilot tilde f, tilde u = u_{tilde f}, one-step via (I2), iterate; remainder div((tilde f - f) grad(u_{tilde f} - u_f)) small by anisotropic smallness of grad(u_{tilde f}-u_f) (Gagliardo-Nirenberg between W^{-1} and C^1 rates of the pilot). Representer psi for a fixed phi is 0-homogeneous near the source, so div(f grad psi) not in L^2 for d<=4: needs regularisation near the source.

## Open gaps
1. Variance lemma (entry 5). 2. Bias lemma (entry 6), especially at the boundary and near the source, and for alpha in (1,2). 3. Remainder/assembly (entry 7), in particular grad Z control when V_J is only C^{1,alpha-1} uniformly. 4. Upper bound #3 overall.
5. (For final audit) the lower bound of round1_q1 will need a verify query as part of the full chain.

## Round 2 wave (4 attempt queries)
q1 full plug-in upper-bound proof; q2 variance lemma; q3 bias lemma; q4 alternative sample-split one-step route.

## Next round should concentrate on
Read q1/q4 for a complete upper-bound proof; if one exists, the goal (lower bound round1_q1 + that upper bound) becomes provable and needs two verify queries of the complete chain (lower + upper). Otherwise attack whichever of the variance/bias/remainder lemmas remains open, using q2/q3.
