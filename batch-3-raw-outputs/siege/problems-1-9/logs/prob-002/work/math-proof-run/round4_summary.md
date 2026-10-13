# Running summary after round 3 (written at round 4 plan)

## Problem
Minimax L^2-squared rate for recovering f in F(alpha,r) (C^alpha ball, radius r, around 1; r small; alpha>1) from Y = u_f + n^{-1/2}W, div(f grad u)=1 on the unit ball D in R^d (d>=2), u=0 on the sphere.

## Goal (ledger #1 OPEN; now entry 18 PROVED, awaiting two audits)
Minimax rate = n^{-2alpha/(2alpha+d+3)} up to logs. Answer to the question: n^{-2alpha/(2alpha+d+3)} (slower than the "degree-one" n^{-2alpha/(2alpha+d+2)}: the forward map smooths perturbations oscillating across the flow of grad u_f by two degrees).

## Standing results
1. LOWER BOUND (entry 4, round1_q1; independently checked, verdict PROVED, by round3_q4 = entry 15). For all alpha>1, d>=2, r in (0,1): inf sup E||hat f - f||^2 >= c n^{-2alpha/(2alpha+d+3)}. Assouad on h_k = kappa 2^{-j(alpha+2)} b(|x|) Delta Phi_k (Phi_k 0-homogeneous angular bumps, ~2^{j(d-1)} of them), ||u_theta - u_theta'||_2 <= C 2^{-2j}||h_k||_2 via the identity div(b Delta Phi_k x/d) = c(|x|) Delta Phi_k, H^2 duality, drift control by W^{2,p}+Gagliardo-Nirenberg (uses alpha>1). Text: round1_q1 lines 1-90.
2. UPPER BOUND (entry 12, round3_q1). For r <= r_0(d,alpha): the estimator f~ = clip_{[1-r,1+r]}(T_{V_hat}^{-1}1) on a good event A (f^ = 1 off A), V_hat = grad K_J Y, K_J g = (k_J * Eg)|_D (Seeley extension E, kernel with vanishing moments 1..S, S >= 2alpha+2), 2^J ~ n^{1/(2alpha+d+3)}, satisfies sup E||f~ - f||_2^2 <= C (log n)^4 n^{-2alpha/(2alpha+d+3)} (no log if alpha non-integer). Key device: linearise around the smooth f_0 = T_{V_J}^{-1}1 (V_J = grad K_J u): exact identity on A, f^ - f = (f_0 - f) - Z + T_{V_hat}^{-1}div(Z grad xi), Z = T_{V_J}^{-1}div(f_0 grad xi). Bias ||f_0 - f||_inf <= C J^2 2^{-J alpha} (commutator + moment cancellation + boundary layer gain 2^{-J}); variance E||Z||_2^2 <= C n^{-1}2^{J(d+3)} via ray measure mu_x and the energy bound int mu_x(B(z,delta))^2 dz, pointwise E Z(x)^2 <= C 2^{J(d+3)}|x-x_J|^{-1}, integrable for d>=2; remainder sup-norm O(J^4 2^{-J(2alpha-1)}) = o(2^{-J alpha}) iff alpha>1; P(A^c) <= 3 exp(-cJ^2). Cites from memory: Zygmund Seeley extension (C1), kernel approximation (C2), Zygmund Taylor (C3), Zygmund Schauder (C4), Gaussian facts (C5).
   Planner check (round 4): I re-derived the commutator algebra, the variance ray-measure computation (beta = d(1-d eps)/(1+d eps) > 1, (M), small-ball mass, integration) and the remainder exponents; all fine. One slip: Lemma 1 states ||D^m V_J|| <= CJ 2^{J(m+1-alpha)_+}, but the later steps use (and need, for alpha near 1, e.g. ||grad f_0|| <= 2^J in the variance step) the correct bound CJ 2^{J(m-alpha)_+}, which follows from V^E = grad Eu in C^alpha by (C2). Harmless typo-level; flagged to the auditors and to round4_q3.
3. VARIANCE LEMMA (entry 13, round3_q2): (V1) L^2 variance for Z built with f in C^1 (no log); noise sup bounds (V3) (= entry 9); grad Z bound only for f in C^2 or smoothed f_J; for unsmoothed f, 1<alpha<=2, conjectured false (heuristic). Not on the current line (round3_q1's proof avoids it), but gives an independent variance argument (Lemmas A, B there).
4. BIAS LEMMA (entry 14, round3_q3): ||f_0-f||_inf <= CJ^2 2^{-J alpha}, ||grad(f_0-f)||_inf <= CJ^3 2^{-J(alpha-1)}; Lemma A: G = div(F grad Eu) - 1 satisfies |G(y)| <= C dist(y,D)^{alpha-1} (finite-difference proof). Gradient half not on the current line.
5. Earlier: exact linearisation at f=1 with symbol (1+|xi_rad|)/|xi|^2 (round1_q3); isotropic stability ||T^{-1}G||_2 <= 2||G||_2 (round1_q4); noise sup bounds (entry 9, round2_q2).

## Chain (complete)
[GOAL] (entry 18) = entry 4 (lower, all r in (0,1)) + entry 12 (upper, r <= r_0) ; (log n)^4 is a log factor. Complete written proof: round1_q1 lines 1-90 + round3_q1 lines 1-222. Certification so far: lower half checked by round3_q4; full chain audits sent as round4_q1, round4_q2 (identical copies, independent engines).

## Dead ends (refuted statements)
- None refuted outright. Retracted: entry 5 (uniform pointwise variance sup bound; likely false near the source, round3_q2), entry 11 (remainder via grad Z with unsmoothed f; relies on a bound round3_q2 conjectures false for alpha<=2).
## Set aside, not refuted
- LSE/M-estimation + isotropic stability: only n^{-2(alpha-1)/(2alpha+d+2)} (round1_q4).
- Sample-split one-step route (round2_q4).

## Open gaps
- Only the audits of the full chain. Cited standard facts C1-C5 remain cited (acceptable for the final document; C4 Zygmund Schauder for small perturbations and C1 Seeley on Zygmund spaces are the least elementary).

## Next round should concentrate on
Audit wave (round4_q1, q2: full chain verify of entry 18) plus round4_q3 (rigorous write-up of Lemmas 1-3 with corrected exponents, for the final document). If both audits come back PROVED (or PROVED AFTER REPAIRS that are minor and stated), record two [AUDIT] lines citing entry 18 and conclude (the problem fixes the claim; nothing to raise). If an audit finds a gap: RETRACT entry 18, re-enter OPEN [GOAL], and aim the wave at the gap (likely candidates: Lemma 1/3 derivative exponents, Lemma 3(a) C^1 requirement, Dudley/Borell-TIS details).
