# Running summary after round 4 (written at round 5 plan) — CONCLUDED

## Problem
Minimax L^2-squared rate for recovering f in F(alpha,r) (C^alpha ball of radius r around 1; r small; alpha>1) from Y = u_f + n^{-1/2}W, div(f grad u)=1 on the unit ball D in R^d (d>=2), u=0 on the sphere.

## Answer
Minimax rate = n^{-2alpha/(2alpha+d+3)} up to log factors (precisely c n^{-2alpha/(2alpha+d+3)} <= minimax risk <= C (log n)^4 n^{-2alpha/(2alpha+d+3)}, no log for non-integer alpha). Interpretation: the forward map smooths perturbations oscillating across the (near-radial) flow lines of grad u_f by two degrees, along the flow by one; the effective ill-posedness is "degree 2 in d-1 directions plus degree 1 radially", giving d+3 in the denominator rather than d+4 (isotropic degree 2) or d+2.

## Goal status
Ledger entry 18: PROVED [GOAL] (lower entry 4 + upper entry 12). Certified by two independent full-chain audits: round4_q1 (entry 19) and round4_q2 (entry 20), both "PROVED AFTER THE REPAIRS GIVEN", repairs change no rate. Run concludes at round 5 (round5_DONE.md). Problem fixes the claim, so there is nothing to raise.

## Standing results
1. LOWER BOUND (entry 4, round1_q1 lines 1-90; checked by round3_q4 = entry 15, and by Part A of round4_q1, round4_q2). All alpha>1, d>=2, r in (0,1). Assouad over h_k = kappa 2^{-j(alpha+2)} b(|x|) Delta Phi_k, Phi_k 0-homogeneous angular bumps (~2^{j(d-1)} of them); ||u_theta-u_theta'||_2 <= C 2^{-2j}||h_k||_2 via div(b Delta Phi_k x/d) = c(|x|) Delta Phi_k and H^2 duality; drift term controlled by W^{2,p} + L^p duality + Gagliardo-Nirenberg (uses alpha>1). Cosmetic fixes: ellipticity constant g>=1-r in (E1); bounded-domain GN carries a harmless lower-order term.
2. UPPER BOUND (entry 12, round3_q1). r<=r_0(d,alpha). Estimator: V_hat = grad K_J Y (extend-then-convolve smoother, kernel with vanishing moments up to S>=2alpha+2), 2^J ~ n^{1/(2alpha+d+3)}; f^ = T_{V_hat}^{-1}1 (transport inverse along backward flow of V_hat from its unique zero, T_X g = div(gX)) on the OBSERVABLE event B = {||V_hat - x/d||_{C^1} <= eps_0}, f^=1 off B; f~ = clip to [1-r,1+r]. Analysis on good event A (subset of B): exact identity f^-f = (f_0-f) - Z + T_{V_hat}^{-1}div(Z grad xi), f_0 = T_{V_J}^{-1}1, Z = T_{V_J}^{-1}div(f_0 grad xi). Bias ||f_0-f||_inf <= CJ^2 2^{-J alpha}; variance E||Z||^2 <= C n^{-1}2^{J(d+3)} (ray measure, pointwise E Z(x)^2 <= C2^{J(d+3)}|x-x_J|^{-1}); remainder O(J^4 2^{-J(2alpha-1)}) = o(2^{-J alpha}) iff alpha>1; P(A^c) <= Ce^{-cJ^2}.
   Repairs required for the final document (from round4_q1/q2): R1 Lemma 1 exponent (m-alpha)_+ instead of (m+1-alpha)_+; R2 observable event B in place of A (round4_q1); R3 right-inverse Lemma 3(a'): if g = T_X^{-1}H is C^1 then div(gX)=H (proof by differentiating the semigroup identity w(t,x) g(Phi_{-t}x) = int_t^inf H(Phi_{-s}x)w(s,x)ds at t=0); R4 (C4) proved by Neumann series: L_f = Delta + div((f-1)grad), ||div((f-1)grad v)||_{C^{alpha-1}} <= C r ||v||_{C^{alpha+1}}, Delta_D^{-1}: C^{alpha-1} -> C^{alpha+1} (Zygmund Schauder, cited) — this is where r small enters; R5 J-power bookkeeping (bias header CJ^2; ||G_xi|| carries J^2), beta>1/2 suffices in the variance integration.
3. LEMMA DETAILS (entry 21, round4_q3): full proofs of Lemma 1.1 (||D^m(k_J*g)|| <= C 2^{J(m-s)_+} for m != s, C(J+1) for m=s, via Littlewood-Paley), Lemma 1, Lemma 2 (unique zero |x_X|<=d eps, invariance of D and B, radial rates, contraction of linearised flow, div bounds), Lemma 3 (a),(a'),(b) const 8/7,(c) boundary layer 6d delta,(d),(e) with s-uniform bounds on derivatives of log w; f_0 bounds. Use for the final write-up.
4. VARIANCE LEMMA (entry 13, round3_q2), BIAS LEMMA (entry 14, round3_q3): supporting, not on the current line (alternative arguments).
5. Earlier: exact linearisation at f=1 with symbol (1+|xi_rad|)/|xi|^2 (round1_q3); isotropic stability (round1_q4); noise sup bounds (entry 9, round2_q2).

## Dead ends
None refuted. Retracted: entries 5, 11 (superseded). Set aside, not refuted: LSE + isotropic stability (only n^{-2(alpha-1)/(2alpha+d+2)}, round1_q4); sample-split one-step (round2_q4).

## Open (outside the claim)
Sharp log power for integer alpha; behaviour for large r (several critical points of u_f possible).

## Next
Concluded. Final proof assembly: lower bound from round1_q1 lines 1-90 (with cosmetic fixes); upper bound from round3_q1 with repairs R1-R5 and lemma proofs from round4_q3; cited standard facts: Seeley extension on Zygmund spaces, Littlewood-Paley/kernel approximation, Zygmund Taylor/algebra property, Zygmund Schauder for Dirichlet Laplacian, GT H^2/W^{2,p}, Gagliardo-Nirenberg, Dudley, Borell-TIS, Assouad, ODE flow differentiability.
