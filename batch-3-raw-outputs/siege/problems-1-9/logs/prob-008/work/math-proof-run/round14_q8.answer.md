# round14_q8: verification of Blocks R13-a and R13-b

Scope: I checked items 1-5 of the task step by step against the material quoted in the task file. That material is Blocks R13-a and R13-b, Theorem J and (F1)/(F2) (R6-a), Theorem T as given in R12-a and corrected in R13-f, Lemma I and Corollary I' (R12-a §2), and Theorem G (R7-f). As instructed, I take Theorem J, (F1), (F2), Theorem T, Lemma I and Corollary I' as proved. I did not re-derive anything else, and I did not try to prove (SC), (IC-gen), (IC-vol) or (PE0).

Notation as in the blocks: Gamma_t phi = e^{J_t}(phi o g_t), P = X + d, ||phi||_{C^1} = max(||phi||_inf, ||dphi||_inf), and |phi(a) - phi(b)| <= ||dphi||_inf d(a,b) for the Riemannian distance on the connected manifold M.

**Summary of verdicts**
1. Theorem IC (with the definitions, the Jacobian constants and the weights): proves the statement exactly as stated.
2. Theorem IC-T: proves the statement exactly as stated. One phrase should be reworded (2.1); no statement changes. Corollary IC-N (i)-(iv): proves the statements exactly as stated.
3. **Theorem IC2: proves the statement exactly as stated. No hidden hypothesis is used** (details in 3.6).
4. Corollaries R1 and R2: the reduction logic is correct, with two wording points for R1. **Proposition CP: does not prove its claim as written.** The zero-length padding forced at x_1 cancels the mass at x_1, so x_1 is never isolated. A one-word change in hypothesis (ii) repairs it (4.3). Its claim about the data of Theorem IC2 is only sketched.
5. Leg functional, (1.2), (1.3), Theorem L, Corollary L1: correct exactly as stated. Corollary L2: the identity is correct; the "in particular" sentence needs the extra condition that the point has nonzero net coefficient (for example, it occurs once in L_1). Corollary L3: correct as stated, but its parenthetical remark about different terminal weights is false when y != x_0.

---

## 1. Block R13-a, Section 1: Theorem IC

**1.1 Definitions.** (L1)-(L3) are as stated. By (L3) the sequence (x_i) is Cauchy, so the limit p exists because M is compact, hence complete. Zero-length legs are harmless.

**1.2 Jacobian constants.** Let (a, b) be a u-leg and t <= 0. Then J_t(a) - J_t(b) = -int_t^0 (d(g_s a) - d(g_s b)) ds. By (L1) the integrand is bounded by Lip(d) C d(a,b) e^{-theta|s|}, which is integrable on (-inf, 0]. So the limit beta^u exists. The tail beyond t is at most Lip(d) C d(a,b) e^{-theta|t|}/theta = K_d d(a,b) e^{-theta|t|}. At t = 0 (J_0 = 0) this gives |beta^u| <= K_d d(a,b). The s-leg case is the same. Correct.

**1.3 Weights.** |w_j| = exp(sum_{i<j} beta_i), and sum_i |beta_i| <= K_d ell, which gives the two-sided bound e^{-K_d ell} <= |w_j| <= e^{K_d ell}. The signs alternate and w_{2N} = exp(sum_{j<2N} beta_j) -> w_inf > 0.

The weights produce cancellation in the asymptotic direction. For a u-leg, w_b = -w_a e^{beta^u(a,b)}, so w_b e^{J_t(b)} = -w_a e^{J_t(a)} e^{-r_t}, where r_t := J_t(a) - J_t(b) - beta^u -> 0 as t -> -inf. The s-legs work the same way. In the volume case w_i = (-1)^i. Correct.

**1.4 Step 1 (convergence).** For a u-leg and ||phi||_{C^1} <= 1:
|w_a phi(a) + w_b phi(b)| = |w_a| |phi(a) - e^{beta^u} phi(b)| <= |w_a| (d(a,b) + |beta^u| e^{|beta^u|}) <= e^{K_d ell} (1 + K_d e^{K_d ell}) d(a,b).
By (L3) the leg-grouped series converges absolutely in (C^1)', and S' converges in the same way. Note that S is defined as the limit of leg-grouped partial sums. The ungrouped Dirac series does not converge absolutely, since |w_i| is bounded below. The block says this in Remark (ii), so the definition is consistent. For smooth psi, S(psi) is the sum of the u-leg terms. Correct.

**1.5 Step 2 (two groupings).** The N-th partial sums differ by w_0 delta_{x_0} - w_{2N} delta_{x_{2N}}. Since ||delta_x||_{(C^1)'} <= 1 and ||delta_x - delta_y||_{(C^1)'} <= d(x,y), the stated bound holds. It tends to 0, so S - S' = delta_{x_0} - w_inf delta_p in (C^1)'. Correct.

**1.6 Step 3 (leg estimate).** The algebraic identity holds with r_t as in 1.3. The modulus is at most
|w_a| e^{J_t(a)} [ ||dphi|| C d(a,b) e^{-theta|t|} + |r_t| e^{|r_t|} ||phi|| ],
and |r_t| <= K_d d(a,b) e^{-theta|t|} <= K_d ell. This gives the stated bound. The s-leg case for t >= 0 is the same. Correct.

**1.7 Step 4 (backward decay).** Sum Step 3 over the u-legs and use (L4) at the even vertices: e^{J_t(x_{2i})} <= e^{C'} e^{eta|t|} for t <= 0. Since sum d(x_{2i}, x_{2i+1}) <= ell, the stated bound follows. Correct.

**1.8 Step 5 (forward decay).** By Step 2, S(Gamma_t phi) = S'(Gamma_t phi) + (delta_{x_0} - w_inf delta_p)(Gamma_t phi). This is legitimate because Gamma_t phi is smooth and the identity holds in (C^1)'.
- S' is bounded by the s-leg version of Step 4, using (L4) at the odd vertices.
- For the endpoint term, (L5) gives the existence of beta^s(x_0, p) and |r''_t| <= Lip(d) C e^{-theta t}/theta. With (HC), w_inf e^{J_t(p)} = e^{J_t(x_0)} e^{-r''_t}, which gives the displayed identity. (L4) at x_0 forward then gives the bound e^{C'+eta t} · O(e^{-theta t}) ||phi||_{C^1}.
Correct.

**1.9 Step 6.** S lies in (C^1)', so it is a distribution density. The two bounds give (*) of Theorem J with k = 1 and eps = theta - eta > 0. Theorem J gives S = 0. Correct. Theorem J does not even need S to be real.

**1.10 Step 7 (isolated vertex).** F := {x_i : i != j} ∪ {p} is closed: it is a convergent sequence together with its limit, plus possibly finitely many repetitions. Also x_j ∉ F. A smooth phi with phi(x_j) = 1 and phi = 0 on a neighbourhood of F kills every leg-grouped partial sum except the term w_j phi(x_j). So S(phi) = w_j != 0. Correct. This step uses no GH, a fact that matters for Proposition CP below.

**1.11 Volume case.** Take nu = omega. Then d = 0 and J = 0, so (L4) holds with C' = 0, eta = 0, and (HC) reads 1 = e^0. Correct.

**Verdict, item 1: Theorem IC proves the statement exactly as stated.** GH enters only through Theorem J.

---

## 2. Block R13-a, Section 2: Theorem IC-T and Corollary IC-N

**2.1 Theorem IC-T.**
- *Legs and constants.* The final leg (g_tau x_0, p; [0, inf)) satisfies d(g_t g_tau x_0, g_t p) <= C e^{-theta t} by hypothesis. Chain legs have c_leg = C d(a,b). So sum c_leg <= C(ell + 1). Correct.
- *Step 1.* Each leg integral is at most Lip(phi) c_leg/theta, so the series over legs converges absolutely. Correct.
- *Step 2 (telescoping).* A u-leg gives u(x_{2i}) - u(x_{2i+1}), and an s-leg (x_{2i+2}, x_{2i+1}) gives u(x_{2i+1}) - u(x_{2i+2}). The partial sums equal u(x_0) - u(x_{2N}) -> u(x_0) - u(p). The final leg gives -(u(g_tau x_0) - u(p)). So l(Xu) = u(x_0) - u(g_tau x_0) = -seg(Xu). Absolute convergence makes the order of summation irrelevant. Correct.
- *Step 3.* (O2) gives phi - omega(phi) = Xu, with l(1) = 0 and seg(1) = tau. The extension to Lipschitz phi uses dominated convergence inside each leg integral and then for the series over legs, with the summable majorant sup_j Lip(phi_j) c_leg/theta. Correct.
- *Step 4.* K_* is a convergent sequence with its limit, plus a C^1 arc. It is compact and nu-null, so it has empty interior when dim M >= 2. X has no zeros (O2). Every leg endpoint (the x_i, g_tau x_0 and p) lies in K_*, hence outside U', which is what Step D of Theorem T needs. The test functions give seg(phi) = 0 and omega(phi) = int eta w_0 dz. Correct.
- *Step 5.* Step D of the corrected Theorem T applies leg by leg, with C_0 replaced by c_leg. The flow-box constants C_1 >= 1, c_2, delta and R do not depend on the leg, and T_1 may depend on it. On a half-line, crossing times that are 2delta-separated with |t_k| >= 2delta give sum_k e^{-theta|t_k|} <= sum_{m>=1} e^{-2 theta delta m} <= A_delta. So sum_k |alpha_k - beta_k| <= C_1 A_delta c_leg.
  - *Short legs.* The corrected Step D says "choose T_1 > delta", so the phrase "T_1 = 0 is admissible" does not literally fit it. The claim itself is right, and the block's own argument proves it directly. I re-checked it as follows. Assume C_1 c_leg < min(delta/2, R/4, c_2).
    - Every crossing t_c of a in H with z(t_c) in B(3R/2) is matched. The partner time t_c - s' has |s'| < delta/2 <= |t_c|/4, so it has the same sign as t_c and lies in H. Its transversal coordinate lies in B(7R/4), inside B(2R).
    - Every crossing t' of b in H with z(t') in B(5R/4) is a partner. The point g_{t'} a = Psi(s'', z'') has |s''| + |z'' - z'| < delta/2. So t' - s'' is a crossing of a in H with z'' in B(3R/2). Since g_{t'-s''} b = Psi(-s'', z') and Psi is injective, its partner is exactly t'.
    - The matching is injective, by 2delta-separation.
    - All remaining crossings have transversal coordinate outside B(R) and contribute 0.
    So F_leg is empty. Since c_leg = C d(x_i, x_{i+1}) -> 0, all but finitely many legs are short. Correct.
- *Step 6.* F = ∪ F_leg is finite. The union of the pair families is summable, with total at most C_1 A_delta sum c_leg. The data do not depend on chi or eta. Rearrangement is allowed because l(phi) converges absolutely over legs and each leg representation converges absolutely. So l(phi) = Lambda(eta) in the form of Lemma I, with e_j in {±1}. Step 3 gives Lambda(eta) = int eta (tau w_0) dz, and Corollary I' gives tau = 0. Then (L5) holds with the same C, and Theorem IC (volume case) gives S = 0 and no isolated vertex. Correct.

**Verdict on Theorem IC-T: proves the statement exactly as stated.** It inherits repairs (R1) and (R2) of R13-f, which are already built into the corrected Step D that it cites. The only change needed is to replace "T_1 = 0 is admissible in Step 5 of Theorem T" by the direct short-leg argument above.

**2.2 Corollary IC-N.**
- **(i)** For a u-leg and t <= 0 there are two cases.
  - If t + tau <= 0: d(g_{t+tau} a, g_{t+tau} b) <= C e^{-theta|t+tau|} d(a,b) <= C e^{theta|tau|} e^{-theta|t|} Lip(g_{-tau}) d(g_tau a, g_tau b).
  - If 0 < t + tau (so t lies in (-tau, 0]): |t + tau| <= |tau|. Then d(g_{t+tau} a, g_{t+tau} b) <= Lip(g_{t+tau}) Lip(g_{-tau}) d(g_tau a, g_tau b), and e^{-theta|t|} >= e^{-theta|tau|}.
  So the constant C L_tau e^{theta|tau|} works, and s-legs are symmetric. Lengths are multiplied by at most Lip(g_tau), and limits map to limits. Applying this with tau and -tau gives equality. Correct.
- **(ii)** l_A(Xu) = u(x) - u(y) and l_B(Xu) = u(g_tau x) - u(y), so l(Xu) = u(x) - u(g_tau x) = -seg(Xu). Steps 3-6 apply with K_* containing both chains, y and the arc. The legs of B enter with the opposite sign, so their unmatched crossings carry e_j in {±1}, still integers, and their pairs are reversed. Corollary I' gives tau = 0. Correct.
  (If x were periodic with period tau, the same argument would give a contradiction. That is consistent, since there are no periodic orbits in the volume case.)
- **(iii)**
  - Each condition (L1), (L2) at fixed t, and each partial-sum bound, is closed in M^N. So Ch_{C,L}(x) is compact metrizable.
  - The limit map is a pointwise limit of continuous maps, hence Borel. A Borel image of a compact set is analytic.
  - A chain with constant C is also a chain with any larger constant, so the countable union over rational C and L exhausts Ahat_theta(x).
  - Analytic sets are universally measurable.
  - By (i) and (ii), the sets g_s Ahat_theta(x) = Ahat_theta(g_s x), s in [0,1), are pairwise disjoint. They have equal omega-measure, so the measure is 0.
  Correct.
- **(iv)** Theorem IC-T gives tau = 0 if the limit lies in the strong stable set at rate theta; enlarge C if needed. Then Theorem IC (volume case) applies. Correct.

**Verdict on Corollary IC-N: (i)-(iv) prove the statements exactly as stated.** "Strong stable set" means at rate theta throughout.

---

## 3. Block R13-a, Section 3: Theorem IC2 (checked in full)

**3.1 Preliminaries.** The bounds S_k(Gamma_t phi) = O(e^{-(theta-eta)|t|}) for t <= 0 and S'_k(Gamma_t phi) = O(e^{-(theta-eta)t}) for t >= 0 use only Steps 1-4 of Theorem IC and the s-leg half of Step 5. Those use (L1)-(L4) and not (L5) or (HC). Correct.

S_k - S'_k = delta_{x_0} - w^{(k)}_inf delta_{p_k} is Step 2 of Theorem IC. Correct.

psi ⋆ S is in (C^1)', because Gamma_s is bounded on C^1 (e^{J_s} is smooth and g_s is a diffeomorphism). The identity (psi ⋆ S)(Gamma_t phi) = sum_j c_j S(Gamma_{t+s_j} phi) holds because Gamma_s Gamma_t = Gamma_{s+t}, by the cocycle rule. The identity (psi psi') ⋆ F = psi ⋆ (psi' ⋆ F) follows by expanding the double sum. Correct.

**3.2 Step 1 (endpoint identity).**
- The ending hypothesis gives d(g_t q_k, g_t p_k) = d(g_{t+tau_k} x_0, g_t p_k) <= C e^{-theta t}. So beta_k exists, with |r_t| <= Lip(d) C e^{-theta t}/theta, where r_t := J_t(q_k) - J_t(p_k) - beta_k.
- The cocycle rule gives J_t(g_tau x_0) = J_{t+tau}(x_0) - J_tau(x_0), hence e^{J_t(q_k)} phi(g_t q_k) = e^{-J_{tau_k}(x_0)} F(t + tau_k).
- Then w_inf e^{J_t(p_k)} phi(g_t p_k) = c_k F(t + tau_k) - E_k(t), with
  E_k(t) = -w_inf e^{-beta_k} e^{J_t(q_k)} [e^{-r_t} phi(g_t p_k) - phi(g_t q_k)].
- So (delta_{x_0} - w_inf delta_{p_k})(Gamma_t phi) = F(t) - c_k F(t + tau_k) + E_k(t) = ((1 - c_k[tau_k]) ⋆ F)(t) + E_k(t), as claimed.
- The bracket is at most (C + K e^K) e^{-theta t} ||phi||_{C^1}, with K = Lip(d) C/theta.
- For t >= 0 with t + tau_k >= 0, (L4) at x_0 gives J_t(q_k) <= C' + eta(t + tau_k) - J_{tau_k}(x_0). If tau_k < 0 and 0 <= t < |tau_k|, then J_t(q_k) is bounded by 2||d||_inf |tau_k|; this case is not mentioned in the block but is harmless.
- Hence |E_k(t)| <= C'_k e^{-(theta-eta)t} ||phi||_{C^1} for all t >= 0. c_k > 0 is clear.
Correct.

**3.3 Step 2 (degenerate case).**
- In C[R], 1 - c[tau] = 0 iff tau = 0 and c = 1. If tau != 0 the coefficient of [0] is 1.
- With tau_2 = 0: q_2 = x_0, so the ending hypothesis is exactly (L5) for chain 2 with the same C. Then beta_2 = beta^s(x_0, p_2) and c_2 = w^{(2)}_inf e^{-beta^s(x_0,p_2)}, so c_2 = 1 is exactly (HC).
- (L4) is assumed for chain 2.
- The vertex v_2 is isolated in the sense of Theorem IC:
  - it occurs once in the combined list, so it differs from every other vertex of chain 2;
  - p_2 is not on its orbit, so v_2 != p_2.
- Theorem IC then gives a contradiction. The case 1 - c_1[tau_1] = 0 is symmetric and uses v_1.
Correct.

**3.4 Step 3 (main case).** The three time ranges check out.
- For t <= -T_0, every shifted time t + s_j (s_j in {0, tau_2} or {0, tau_1}) is <= 0, and e^{-(theta-eta)|t+s_j|} <= e^{(theta-eta)T_0} e^{-(theta-eta)|t|}.
- For t >= T_0, every t + s_j >= 0. Step 1 applies at u = t + s_j, and the F-terms collect into ((psi_1(1 - c_1[tau_1]) + psi_2(1 - c_2[tau_2])) ⋆ F)(t). The ring element is 0 because C[R] is commutative. The remaining terms are psi_k ⋆ (S'_k(Gamma. phi) + E_k), which are O(e^{-(theta-eta)t}) ||phi||_{C^1}.
- For |t| <= T_0, |S(Gamma_t phi)| <= ||S||_{(C^1)'} sup_{|t| <= T_0} ||Gamma_t||_{C^1 -> C^1} ||phi||_{C^1}.
So (*) of Theorem J holds with k = 1 and eps = theta - eta, and S = 0. Correct.

**3.5 Step 4 (S != 0) in all sub-cases.**
- S is a leg-grouped convergent combination of Dirac masses at the points g_s y, where either y is a vertex of chain 1 and s ∈ supp psi_1 ⊂ {0, tau_2}, or y is a vertex of chain 2 and s ∈ supp psi_2 ⊂ {0, tau_1}. Its accumulation points are the finitely many points g_s p_k.
- Suppose g_s y = v_1. Then y lies on the orbit of v_1, so y = v_1 as a point, by orbit isolation. Since v_1 occurs exactly once in the combined list and v_1 != x_0, y is the vertex at v_1's index in chain 1. Then g_s v_1 = v_1 with v_1 neither periodic nor a zero, so s = 0. In particular:
  - no chain-2 term and no shifted term (s = tau_2 != 0) sits at v_1;
  - no accumulation point g_s p_k equals v_1, since p_k is not on its orbit.
- The closure of the support minus {v_1} is therefore closed and does not contain v_1, so a bump phi exists.
- Every leg-grouped partial sum, evaluated at phi, reduces to (coefficient of [0] in psi_1) · w^{(1)}_{v_1}.
- If tau_2 != 0 that coefficient is 1.
- If tau_2 = 0 it is 1 - c_2. This is nonzero in Step 3 because psi_1 != 0 there, which covers the sub-case "tau_2 = 0 with c_2 != 1".
- In every case S(phi) != 0, which contradicts Step 3. The case split (psi_1 = 0; psi_2 = 0; both nonzero) is exhaustive. Correct.

**3.6 Hidden hypotheses (as the task asks).**
- *Uniformity of constants.* Both chains and both endings use one (C, theta), and (L4) uses one (eta, C') for both chains. This is part of the statement. It costs nothing: take the larger C and C', and the smaller theta, keeping eta below it. All constants in the proof depend only on the configuration, never on phi, as Theorem J requires. Nothing else needs to be uniform.
- *Zeros and periodicity.* Only v_1 and v_2 must be neither zeros nor periodic, and this is assumed. Other vertices, x_0 and the p_k may be zeros or periodic without affecting any step. Step 1 is pure cocycle algebra, and Step 4 only concerns the point v_1.
- *Measurability.* None is used. The theorem concerns one fixed countable configuration.
- *Real values.* The weights and the c_k are real, so S is real. Theorem J does not need this anyway.
- *Dimension, volume, Pesin theory.* None is used. GH enters only through Theorem J (via (F1), (F2)), including inside the application of Theorem IC in Step 2.
- The two hypotheses actually used in Step 4 are "occurs exactly once in the combined list" and "orbit contains no other vertex of either chain and neither p_1 nor p_2". Both are stated.
- Unused hypothesis: in Step 3 only v_1 is used. v_2 is needed only in the degenerate case of Step 2.

**Verdict, item 3: Theorem IC2 proves the statement exactly as stated, under exactly the stated hypotheses ((L1)-(L4) for both chains with common constants, weak-stable endings with constant C, orbit-isolated vertices). No hidden hypothesis is used.**

---

## 4. Block R13-a, Section 4: reductions

**4.1 Corollary R1.** The logic is correct, with two implicit points.
- "h_top(g_1) > 0 gives h_omega(g_1) > 0 by the variational principle" needs the variational principle for flows: the supremum may be taken over flow-invariant measures. This is standard and is the reduction recorded in R12-h / R6-a §5: mu-bar = int_0^1 (g_s)_* mu ds has the same g_1-entropy. Unique ergodicity of the flow (O2) then forces mu-bar = omega.
- In (gamma), "strong stable set" must mean at the same rate theta, so that (L5) holds and Theorem IC (volume case) applies.
Then (alpha) contradicts IC-N(iii), (beta) contradicts IC-N(ii), and (gamma) contradicts Theorem IC. The case dim M = 1 is trivial. **Verdict: correct (reduction logic).**

**4.2 Corollary R2.** (IC-gen) is quantified over all fields. Applied to a GH field and a hypothetical (PE0)-measure, it yields data that contradict Theorem IC2. So (PE0) holds, and steps 1-2 of the chain finish. **Verdict: correct (reduction logic).**

**4.3 Proposition CP: gap.**
The chain starts with the u-leg x_0 -> x_1. Hypothesis (ii) applied at q_0 = x_1 produces a path that starts with a u-leg. So two u-legs meet at x_1, and the proof pads with a zero-length s-leg (x_1, x_1). The padded chain therefore contains x_1 at two consecutive indices, with weights w_2 = -w_1 e^{beta^s(x_1,x_1)} = -w_1. The total mass of S at x_1 is w_1 + w_2 = 0. So x_1 is not isolated in the sense of Theorem IC (it occurs twice), and S may well vanish.

The proof's sentence "x_1 is distinct from all later vertices ... So x_1 is isolated" is false for the padded chain. No other vertex is guaranteed to be isolated, because hypothesis (ii) does not require the vertices inside one path to be distinct.

*Repair.* In (ii), replace "starting with u" by "starting with s". Then:
- x_0 ->u x_1 ->s y_1 needs no padding at x_1.
- Later paddings duplicate only junction points q_k with k >= 1. Each q_k is some y_j with j >= 1 of an earlier path, so it lies outside F, which contains x_1.
- All later vertices avoid F.
- p != x_1 because W^u_loc(x_0) ∩ W^s_loc(x_0) = {x_0}.
So x_1 occurs exactly once and is isolated. Theorem IC Step 7, which is GH-free, gives S != 0, which is (gamma) (volume case). With the repair:
- in the general case the chain has limit in W^s_loc(x_0), so it has a strong-stable ending (tau = 0);
- the rest of the proof is correct: Delta is 1-Lipschitz, Delta(q_k) <= kappa^k r_0, the path lengths are summable, and the legs satisfy (L1)/(L2) with the length factor by the availability remark (cited Pesin theory);
- p ∈ W^s_loc(x_0) needs the local leaf to be taken closed.

Alternatively, keep (ii) as stated and also require the vertices within each path to be pairwise distinct and different from p. Then y_1 of the first path can serve as the isolated vertex: it is entered by a u-leg and left by an s-leg, so it is never padded.

*The IC2 clause.* "If (L4) holds on K and (ii) can be run twice with disjoint vertex sets (including orbits), one obtains the data of Theorem IC2" is only a sketch. To make it exact it needs:
- the same padding repair for both chains;
- two points x_1, x'_1 as in (i) on distinct orbits, neither periodic nor a zero of X;
- their orbits avoiding all other vertices of both chains and the limits p_1, p_2.

**Verdict on Proposition CP: does not prove its claim as written (the isolated vertex is cancelled by the forced padding). It proves it after the repair above. The IC2 clause is a sketch.** This does not affect Theorem IC, IC-T, IC2, R1 or R2, which do not use CP.

---

## 5. Block R13-b, Sections 1-2

**5.1 Leg functional.**
- For a type-u leg, J_t(b) - J_t(a) = -int_t^0 (d(g_r b) - d(g_r a)) dr -> -beta. So beta = lim_{t -> -inf} (J_t(a) - J_t(b)), the same constant as beta^u in R13-a. The error is at most (Lip(d) C/theta) e^{-theta|t|}. Type s is analogous.
- The split of Delta(t)(phi) is an identity, and (1.1) follows.
- Under (G), |Delta(t)(phi)| <= C'' e^{-theta'|t|} ||phi||_{C^1} in the asymptotic direction. So l has order <= 1.
- (G) transfers from a to b because the difference converges.
Correct.

**5.2 Identity (1.2).** d/dt [e^{J_t(a)} phi(g_t a)] = e^{J_t(a)} (P phi)(g_t a), so Delta(t)(P phi) = d/dt Delta(t)(phi).
- Type u: int_{-inf}^0 d/dt Delta(t)(phi) dt = Delta(0)(phi) - lim_{-inf} Delta(t)(phi) = Delta(0)(phi).
- Type s: -int_0^inf d/dt Delta(t)(phi) dt = Delta(0)(phi).
- Delta(0)(phi) = alpha phi(a) - alpha e^beta phi(b).
The vanishing at the asymptotic end uses (G). Correct.

**5.3 Transport rule (1.3).** alpha e^{J_s(a)} (Gamma_t phi)(g_s a) = alpha e^{J_{s+t}(a)} phi(g_{s+t} a), so Delta(s)(Gamma_t phi) = Delta(s+t)(phi). The two integral formulas follow by substitution. Correct.

**5.4 Chain identity and the value of c (Section 1).** Telescoping with w_{k+1} = w_k e^{beta_k} and seg^w(P phi) = e^{J_tau(x_0)} phi(g_tau x_0) - phi(x_0) are correct. In the volume case (l + seg)(1) = tau, so c = tau/nu(M). Correct.

**5.5 Theorem L.**
- *Step 1.* D∘P = m = 0, so D = c nu by (F1). Correct.
- *Step 2.* By (1.3), G_phi(t) = sum_u int_{-inf}^t Delta_k(r)(phi) dr. Its derivative is sum_u Delta_k(t)(phi), which equals G_{P phi}(t) by (1.2)-type integration.
  - The t <= 0 bound is clear.
  - For t >= 0, nu(Gamma_t phi) = nu(phi) because e^{J_t} is the nu-Jacobian of g_t. So G_phi(t) = c nu(phi) - F(Gamma_t phi), and F(Gamma_t phi) is a sum of forward tails, O(e^{-theta' t}).
  Correct.
- *Step 3.* The integral converges absolutely for 0 < Re z < theta': backward the integrand decays like e^{-(theta' - Re z)|t|}, forward G is bounded and e^{-Re z t} decays. The integration by parts has vanishing boundary terms; the same bounds hold for P phi with C^2 norms. The splitting T_z = H_1 + c nu(phi)/z - H_2 is an identity, with H_1 holomorphic on Re z < theta' and H_2 on Re z > -theta'. So T_z(phi) continues meromorphically to |Re z| < theta' with at most a simple pole at 0, and the eigen-relation extends by the identity theorem on the connected punctured strip. Correct.
- *Step 4.* On |z| = r < theta', |T_z(phi)| <= C_r ||phi||_{C^2}. This uses the C^1 bound for phi, and for the relation with P phi the C^2 norm. So the A_n are distribution densities.
  - A_n = 0 for n < -1, and A_{-1} = c nu (the residue).
  - The eigen-relation gives A_n∘P = A_{n-1}.
  - A_0∘P = c nu, so c = 0 by (F2).
  - The induction with (F1) and (F2) gives A_n = 0 for all n.
  - The disc |z| < theta' lies in the strip, so the Laurent series represents T_z on 0 < |z| < theta'. Hence T_z = 0 there, and on the whole punctured strip by the identity theorem.
  Correct. (The block says "order <= 1" for A_n. With the C^1 bounds of Step 2 this is right for A_n itself; only the relation A_n∘P uses ||P phi||_{C^1}. Immaterial.)
- *Step 5.* For sigma ∈ (0, theta'), e^{-sigma t} G_phi(t) is continuous and in L^1, and its Fourier transform is y -> T_{sigma+iy}(phi) = 0. So G_phi = 0 and B(phi) = G_phi(0) = 0. Correct.
- *Step 6.* m_u(phi) = sum_u l_k(P phi) = B(P phi) = 0. Then c = 0 gives D = 0, F = 0 and m_s = F∘P = 0. Correct.

**Verdict on Theorem L: proves the statement exactly as stated.** GH enters only through (F1) and (F2).

**5.6 Corollary L1.** With alpha_k = w_k, leg k contributes w_k delta_{x_k} - w_{k+1} delta_{x_{k+1}}, so m = (1 - w_N) delta_{x_0} = 0. Because the leg types alternate, each x_k (0 <= k <= N-1) is an endpoint of exactly one u-leg. Since the points are distinct, m_u has mass ±w_k != 0 at x_k. So m_u != 0, contradicting Theorem L. **Proves exactly as stated.**

**5.7 Corollary L2.** The combined family has boundary (a(1 - h_1) + b(1 - h_2)) delta_{x_0} = 0, and its u-part is a m_u(L_1) + b m_u(L_2). Theorem L allows zero coefficients. The identity is correct. If h_1, h_2 != 1, then a = 0 would force b = 0, so both are nonzero. Correct.

*Gap in the "in particular" sentence.* L2 does not assume the points of a loop are distinct. A u-point y of L_1 that does not occur in L_2 could occur several times in L_1, with cancelling net coefficient in m_u(L_1). *Repair:* require that m_u(L_1) has nonzero mass at y, for instance that y occurs exactly once in L_1. Then a · (±w) != 0 when a != 0.

**Verdict: the identity of L2 proves exactly as stated; the "in particular" holds after this repair.**

**5.8 Corollary L3.** Take the legs of C_1 with coefficients w^{(1)} and those of C_2 with coefficients -w^{(2)}. The total boundary is (delta_{x_0} - W delta_y) - (delta_{x_0} - W delta_y) = 0, and Theorem L gives m_u(C_1) = m_u(C_2). No reversal and no alternation is needed. **The statement is proved exactly as stated.**

*Error in the remark.* The parenthetical "If the two terminal weights differ, combine as in L2" is false when y != x_0. For a m(C_1) + b m(C_2) = (a + b) delta_{x_0} - (a W_1 + b W_2) delta_y to vanish we need b = -a and a(W_1 - W_2) = 0. With W_1 != W_2 this forces a = b = 0, so nothing follows. (When y = x_0 the remark is Corollary L2.) The remark should be deleted. This does not affect the statement of L3.

---

## 6. Overall verdict

- **Theorem IC2 holds exactly as stated.** I checked every step: the endpoint identity and its error bound (including the range 0 <= t < |tau_k| when tau_k < 0), the case split, the cancellation in C[R], the three time ranges, the application of Theorem J, and the non-vanishing at the orbit-isolated vertex in all sub-cases, including tau_2 = 0 with c_2 != 1. Its hypotheses suffice as stated, with no hidden uniformity, measurability or zero-avoidance assumption beyond what the statement already says. **Step 4 of the chain may apply it verbatim.**
- The other results the chain uses are also proved exactly as stated: Theorem IC; Theorem IC-T (with a wording fix); Corollary IC-N; Corollaries R1 and R2 (logic); Theorem L; Corollary L1; the identities of L2 and L3.
- Defects found, none on the path of the chain:
  - (a) Proposition CP: the padding at x_1 cancels the mass there, so its isolated-vertex conclusion fails as written. It holds after the repair "paths in (ii) start with an s-leg" (or distinct vertices within each path). Its IC2 clause is only a sketch.
  - (b) Corollary L2: the "in particular" needs a nonzero net coefficient at the chosen point.
  - (c) Corollary L3: the parenthetical remark about different terminal weights is false for y != x_0.
- Not checked here (outside the brief): entry 113 (R11-a), the variational step, and the open statement (SC). Theorem J, (F1), (F2), Theorem T, Lemma I and Corollary I' were taken as proved, as instructed.

**Open (unchanged):** (SC), equivalently (IC-gen) / (IC-vol), equivalently the centre-steering property (ii) of Proposition CP (in repaired form), and hence (PE0) and the problem in dimension >= 4.

=== END OF ANSWER round14_q8 ===
