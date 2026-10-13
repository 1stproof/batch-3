# round13_q1 — answer (final; partial result: (PE0) NOT proved, no counterexample)

**Summary.** (PE0) remains open. New, fully proved: *infinite su-chains with summable leg lengths* give exact distributions
with two-sided exponential decay, so Theorem J applies to them (Theorem IC; general case with a holonomy condition). In the
volume case flow shifts are killed for such chains and the infinite-chain accessible sets are null and disjoint along orbits
(Theorem IC-T, Corollary IC-N); in the general case two such chains from one point, ending anywhere in its weak-stable set,
already contradict GH, with no holonomy or flow-shift condition (Theorem IC2). Consequently (PE0) (resp. its volume case)
follows from GH-free statements (IC-gen) (resp. (IC-vol)) that are weaker than all earlier closing targets: only the genuine
centre must be steered, only in the limit, with summable cost (Corollaries R1, R2, Proposition CP). The planner's Mechanism
C(b) cannot work from the form of its identity (Lemma D) and is superseded by Theorem IC2. Section 7 lists what is open.

## Plan (written first, updated as I go)
I read the brief (all 5200 lines). (PE0) is, as the brief says, at least as hard as the volume case of the
problem, which itself sits inside the Greenfield–Wallach / Katok circle. I do not expect to settle it outright.
Plan:
1. Look for a NEW exact object with two-sided decay that avoids the two known walls:
   (a) exact closing of su-chains is a codimension-(c-1) condition (centre defect);
   (b) approximate closing degenerates in the limit (Lemma G / Prop W / Lemma O1-O3 of R12-b).
   Candidate found: **infinite su-chains with summable leg lengths ("chains closing at infinity")**. They give an
   EXACT distribution (an infinite, conditionally convergent Dirac sum, convergent in (C^1)') with two-sided
   decay, without any limit procedure on configurations. State and prove the criterion (volume case first,
   then the weighted general case), then see what geometric input it needs.
2. Analyse the planner's Mechanism C (weighted chains + L1): prove or kill step (b).
3. Record what remains open.

Statement currently attempted (Section 1 below): *Theorem IC (infinite chains).* Under GH, there is no infinite
su-chain in a Pesin block with summable leg lengths whose limit point lies on the local stable leaf of its
starting point (or equals it), and which has one "isolated" vertex; weighted version in the non-volume case
with a single real holonomy condition.

---

## 0. Conventions (as in the brief)
nu smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, Gamma_t phi = e^{J_t}(phi o g_t),
P phi = X phi + d phi. Fix a Riemannian distance on M (M connected), so |phi(a) - phi(b)| <= ||dphi||_inf d(a,b);
||phi||_{C^1} := max(||phi||_inf, ||dphi||_inf). Lip(d) is the Lipschitz constant of d.
**Theorem J** (R6-a, proved there from GH via (F1),(F2)): if S is a distribution density and
|S(Gamma_t phi)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and smooth phi, then S = 0.

## 1. Theorem IC: infinite su-chains with summable legs (new; fully proved)

**Definition (summable chain).** Let C >= 1, theta > 0. A *summable chain with constants (C, theta)* is a
sequence (x_i)_{i >= 0} of points of M such that, for every i >= 0,
- (L1) d(g_t x_{2i}, g_t x_{2i+1}) <= C e^{-theta|t|} d(x_{2i}, x_{2i+1}) for all t <= 0 ("u-leg");
- (L2) d(g_t x_{2i+1}, g_t x_{2i+2}) <= C e^{-theta t} d(x_{2i+1}, x_{2i+2}) for all t >= 0 ("s-leg");
- (L3) ell := sum_{i >= 0} d(x_i, x_{i+1}) < infinity.
By (L3) the sequence is Cauchy; p := lim x_i is its *limit point*. Legs of length 0 are allowed, so every
finite chain in the sense of Theorem T / Corollary G1 (padded by constant legs) is a summable chain.

(Availability, cited Pesin theory, as in [PB] of R9-i: on a Pesin block K of g_1 for an ergodic mu there are
C_K, theta, r_K such that for z in K and y, y' in W^u_loc(z): d(g_{-n} y, g_{-n} y') <= C_K e^{-theta n} d(y, y'),
and symmetrically on W^s_loc(z); interpolation to real t changes only the constant. So any sequence with
x_{2i} in K, x_{2i+1} in W^u_loc(x_{2i}), x_{2i+2} in K with x_{2i+1} in W^s_loc(x_{2i+2}), and summable
lengths, is a summable chain. Note that only every other vertex has to lie in K.)

**Jacobian constants.** For a pair (a, b) as in (L1) put beta^u(a,b) := lim_{t -> -inf} (J_t(a) - J_t(b)); for a
pair as in (L2) put beta^s(a,b) := lim_{t -> +inf} (J_t(a) - J_t(b)). With K_d := Lip(d) C / theta:
 |J_t(a) - J_t(b) - beta^u(a,b)| <= K_d d(a,b) e^{-theta|t|} (t <= 0),  |beta^u(a,b)| <= K_d d(a,b),
and the same for beta^s with t >= 0.
*Proof.* For t <= 0, J_t(a) - J_t(b) = -int_t^0 (d(g_s a) - d(g_s b)) ds, and the integrand is bounded by
Lip(d) C d(a,b) e^{-theta|s|}, which is integrable on (-inf, 0]; the limit exists and the tail beyond t is at
most Lip(d) C d(a,b) e^{-theta|t|}/theta. The bound on beta^u is the case t = 0. Same for beta^s. ∎

**Weights.** Put w_0 := 1, w_{2i+1} := -w_{2i} e^{beta^u(x_{2i}, x_{2i+1})}, w_{2i+2} := -w_{2i+1} e^{beta^s(x_{2i+1}, x_{2i+2})}.
Then w_{2i} > 0 > w_{2i+1}, e^{-K_d ell} <= |w_i| <= e^{K_d ell}, and w_{2N} = exp(sum_{j < 2N} beta_j) -> w_inf :=
exp(sum_j beta_j) > 0, where beta_j is the beta^u or beta^s of the j-th leg (absolutely summable by (L3)).
In the volume case (nu = omega invariant, d = 0) all beta vanish and w_i = (-1)^i.

**Theorem IC.** Assume GH. Let (x_i) be a summable chain with constants (C, theta), limit point p, and suppose:
- (L4) there are eta in [0, theta) and C' with J_t(x_{2i}) <= C' + eta|t| for t <= 0 and
  J_t(x_{2i+1}) <= C' + eta t for t >= 0 (all i), and J_t(x_0) <= C' + eta t for t >= 0;
- (L5) d(g_t x_0, g_t p) <= C e^{-theta t} for all t >= 0 (i.e. p lies on the strong stable set of x_0;
  p = x_0 is allowed);
- (HC) (holonomy condition) w_inf = e^{beta^s(x_0, p)}, i.e. sum_j beta_j = beta^s(x_0, p).
Then the distribution
  S := sum_{i >= 0} ( w_{2i} delta_{x_{2i}} + w_{2i+1} delta_{x_{2i+1}} )   (convergent in (C^1)')
is zero. Consequently, **no vertex x_j is distinct from p and from all x_i, i != j** (an "isolated vertex").
In the volume case (L4) and (HC) hold automatically (d = 0), and the theorem says: no summable chain whose
limit lies in the strong stable set of its first point has an isolated vertex.

*Proof.*
1. *Convergence.* For a u-leg (a, b) = (x_{2i}, x_{2i+1}) and ||phi||_{C^1} <= 1:
   |w_a phi(a) + w_b phi(b)| = |w_a| |phi(a) - e^{beta^u(a,b)} phi(b)| <= |w_a|(d(a,b) + |1 - e^{beta^u}|)
   <= e^{K_d ell}(1 + K_d e^{K_d ell}) d(a,b), using |1 - e^r| <= |r| e^{|r|}. By (L3) the series defining S
   converges absolutely in (C^1)'. Likewise S' := sum_i (w_{2i+1} delta_{x_{2i+1}} + w_{2i+2} delta_{x_{2i+2}}) converges.
2. *The two groupings.* The difference of the N-th partial sums of S and S' is w_0 delta_{x_0} - w_{2N} delta_{x_{2N}}.
   Since ||w_{2N} delta_{x_{2N}} - w_inf delta_p||_{(C^1)'} <= |w_{2N} - w_inf| + w_inf d(x_{2N}, p) -> 0,
   S - S' = delta_{x_0} - w_inf delta_p.
3. *A leg estimate.* Let (a,b) be a u-leg. For t <= 0 put r_t := J_t(a) - J_t(b) - beta^u(a,b), |r_t| <= K_d d(a,b) e^{-theta|t|} <= K_d ell. Then
   w_a e^{J_t(a)} phi(g_t a) + w_b e^{J_t(b)} phi(g_t b) = w_a e^{J_t(a)} [ (phi(g_t a) - phi(g_t b)) + (1 - e^{-r_t}) phi(g_t b) ],
   whose modulus is <= e^{K_d ell} e^{J_t(a)} (C + K_d e^{K_d ell}) d(a,b) e^{-theta|t|} ||phi||_{C^1}. The same holds for an
   s-leg (b, c) = (x_{2i+1}, x_{2i+2}) and t >= 0 with e^{J_t(b)}.
4. *Backward decay.* For each t, Gamma_t phi is smooth, so S(Gamma_t phi) is the sum of the u-leg terms. For t <= 0, by step 3 and (L4),
   |S(Gamma_t phi)| <= e^{K_d ell}(C + K_d e^{K_d ell}) e^{C'} ell e^{-(theta - eta)|t|} ||phi||_{C^1}.
5. *Forward decay.* For t >= 0, by step 2, S(Gamma_t phi) = S'(Gamma_t phi) + e^{J_t(x_0)} phi(g_t x_0) - w_inf e^{J_t(p)} phi(g_t p).
   The first term is bounded as in step 4 with the s-legs. By (HC) and (L5), the last two terms equal
   e^{J_t(x_0)}[ (phi(g_t x_0) - phi(g_t p)) + (1 - e^{-r''_t}) phi(g_t p) ], r''_t := J_t(x_0) - J_t(p) - beta^s(x_0, p),
   with |r''_t| <= Lip(d) C e^{-theta t}/theta (same computation as for the Jacobian constants, with d(x_0,p) replaced by 1 since
   (L5) carries no length factor). By (L4) this is <= C'' e^{-(theta - eta)t} ||phi||_{C^1}.
6. Steps 4-5 give (*) of Theorem J with k = 1, eps = theta - eta (S is real). Hence S = 0.
7. *Isolated vertex.* Suppose x_j != p and x_j != x_i for all i != j. The set F := {x_i : i != j} ∪ {p} is closed (its only
   possible accumulation point is p) and does not contain x_j. Take phi smooth with phi(x_j) = 1 and phi = 0 near F. Every term of
   the series for S(phi) vanishes except w_j phi(x_j) = w_j != 0. So S != 0, contradicting step 6. ∎

**Remarks.** (i) Corollary G1 of R7-a (single closed cycle with zero holonomy) is the special case of an eventually constant
chain. (ii) The new feature is that S is an EXACT distribution (a conditionally convergent infinite Dirac sum, absolutely
convergent only after grouping into legs) with two-sided decay. No limit of configurations is taken, so the degeneration
phenomena of R12-b (Lemmas O1-O3, Proposition W, Lemma G) do not arise: the corrections that bring the chain back to the stable
set of x_0 are part of S, at all scales simultaneously. (iii) Only the leg lengths need to be summable; the number of legs is
infinite. (iv) The proof uses GH only through Theorem J.

## 2. Volume case: flow shifts are killed for infinite chains too, and infinite-chain classes are null (new; proved)

Setting: GH, dim M >= 2, X preserves a smooth positive probability density omega; nu = omega, d = 0, J = 0. By (O2) the flow is
uniquely ergodic, has no zeros, and every smooth phi has phi - omega(phi) = Xu with u smooth. I use Lemma I and Corollary I'
(integrality lemma) and the flow-box set-up of Theorem T (Block R12-a, quoted in the brief).

**Theorem IC-T.** In this setting let (x_i) be a summable chain with constants (C, theta) and limit p, and suppose there is a
real tau with d(g_t p, g_{t+tau} x_0) <= C e^{-theta t} for all t >= 0. Then tau = 0. Hence (Theorem IC, volume case) the
distribution S = sum_i (delta_{x_{2i}} - delta_{x_{2i+1}}) vanishes, and the chain has no isolated vertex.

*Proof.* (Theorem T, with infinitely many legs.) Legs: the u-legs (x_{2i}, x_{2i+1}; H = (-inf, 0]), the s-legs
(x_{2i+2}, x_{2i+1}; H = [0, inf)), and the final leg (g_tau x_0, p; [0, inf)). Each leg (a, b; H) satisfies
d(g_t a, g_t b) <= c_leg e^{-theta|t|} on H, with c_leg = C d(a,b) for chain legs and c_leg = C for the final leg; so
sum over legs of c_leg <= C(ell + 1) < inf.
1. *Cycle functional.* For Lipschitz phi, l(phi) := sum_legs int_H (phi(g_t a) - phi(g_t b)) dt; each term is bounded by
   Lip(phi) c_leg/theta, so the series converges absolutely. seg(phi) := int_0^tau phi(g_s x_0) ds.
2. *Telescoping.* For smooth u: a u-leg gives u(a) - u(b) (the boundary term at -inf vanishes since d(g_t a, g_t b) -> 0 and u
   is uniformly continuous); an s-leg (x_{2i+2}, x_{2i+1}) gives u(x_{2i+1}) - u(x_{2i+2}). The partial sum over the first N
   u-legs and N s-legs is u(x_0) - u(x_{2N}) -> u(x_0) - u(p). The final leg gives u(p) - u(g_tau x_0). So
   l(Xu) = u(x_0) - u(g_tau x_0) = -seg(Xu).
3. *GH identity.* For smooth phi, phi - omega(phi) = Xu, and l(1) = 0, so l(phi) = tau omega(phi) - seg(phi). This extends to
   Lipschitz phi: mollify to phi_j -> phi uniformly with sup Lip(phi_j) < inf; each leg term converges by dominated
   convergence, and the series over legs converges by dominated convergence for series (bound sup_j Lip(phi_j) c_leg/theta,
   summable).
4. *Flow box.* K_* := {x_i : i >= 0} ∪ {p} ∪ {g_s x_0 : s between 0 and tau} is compact (a convergent sequence with its limit,
   plus an arc) with empty interior (dim M >= 2). Choose the flow box Psi, the radii R, delta and the constants C_1, c_2 exactly
   as in Step 4 of Theorem T, with U' disjoint from K_*. Test functions phi = (chi ⊗ eta) o Psi^{-1}: then seg(phi) = 0 and
   omega(phi) = int eta w_0 dz.
5. *Crossings, leg by leg.* For each leg, Step 5 of Theorem T gives
   int_H (phi(g_t a) - phi(g_t b)) dt = sum_{j in F_leg} e_j eta(zeta_j) + sum_k (eta(alpha_k) - eta(beta_k)),
   F_leg finite, e_j = ±1, with sum_k |alpha_k - beta_k| <= C_1 c_leg sum_k e^{-theta|t_k|} <= C_1 A_delta c_leg, where
   A_delta := 2 sum_{m >= 1} e^{-2 theta delta m} (the crossing times t_k are 2delta-separated and |t_k| >= 2delta).
   *Short legs have no unmatched part.* If C_1 c_leg e^{theta delta} < min(delta/2, R/4, c_2), then T_1 = 0 is admissible in
   Step 5 of Theorem T, every crossing of a in H is matched, and every crossing t' of b in H with z(t') in B(5R/4) is a partner:
   indeed |t'| >= 2delta (b is not in U'), g_{t'} a is within c_leg e^{-theta|t'|} < delta/2 of g_{t'} b = Psi(0, z'), so
   g_{t'} a = Psi(s'', z'') with |s''| + |z'' - z'| < delta/2; then t' - s'' is a crossing of a, in H (|s''| < 2delta <= |t'|),
   with z'' in B(3R/2), and its partner is t' (g_{t'-s''} b = Psi(-s'', z')). So F_leg = ∅ for all but finitely many legs.
6. *Summing.* Since sum over legs of sum_k |eta(alpha_k) - eta(beta_k)| <= Lip(eta) C_1 A_delta sum c_leg < inf, the
   leg-by-leg representations add up to l(phi) = Lambda(eta) in the notation of Lemma I, with finite F = union of the F_leg and
   a summable family of pairs. By Step 3, Lambda(eta) = tau int eta w_0 dz for all Lipschitz eta supported in B(R). Corollary I'
   gives tau = 0. The final claim is Theorem IC with p in the strong stable set of x_0. ∎

**Definition.** For theta > 0 and x in M let Ahat_theta(x) be the set of limit points of summable chains with x_0 = x, rate
theta and arbitrary constant C. (It contains the su-class A(x) of R12-a §4.1 restricted to rate theta.)

**Corollary IC-N.** In the setting of Theorem IC-T, for every x and theta > 0:
 (i) Ahat_theta(g_tau x) = g_tau Ahat_theta(x) for all tau;
 (ii) Ahat_theta(x) ∩ Ahat_theta(g_tau x) = ∅ for every tau != 0;
 (iii) Ahat_theta(x) is an analytic (hence universally measurable) set and omega(Ahat_theta(x)) = 0;
 (iv) no summable chain from x whose limit lies in the strong stable set of x has an isolated vertex.
*Proof.* (i) g_tau maps a summable chain with constants (C, theta) to one with constants (C L_tau e^{theta|tau|}, theta),
L_tau := max_{|s| <= |tau|} Lip(g_s)^2: for t + tau and t of the same sign this is the estimate with e^{-theta|t+tau|} <=
e^{theta|tau|} e^{-theta|t|} and d(a,b) <= Lip(g_{-tau}) d(g_tau a, g_tau b); for t between -tau and 0 (or 0 and -tau) use
d(g_{t+tau} a, g_{t+tau} b) <= Lip(g_{t+tau}) d(a,b) and e^{-theta|t|} >= e^{-theta|tau|}. Lengths change by a bounded factor,
and limits are mapped to limits. Apply this to tau and -tau.
(ii) Let y = lim of a chain (a_i) from x and of a chain (b_i) from g_tau x. Run the proof of Theorem IC-T with the functional
l := l_A - l_B, where l_A, l_B are the cycle functionals of the two chains (legs as in Step 1, without a final leg). By Step 2,
l(Xu) = (u(x) - u(y)) - (u(g_tau x) - u(y)) = -seg(Xu). Steps 3-6 apply verbatim (the legs of B enter with the opposite sign,
which only exchanges alpha_k and beta_k and the signs e_j). So tau = 0.
(iii) For rational C, L > 0 the set Ch_{C,L}(x) of sequences (x_i) in M^N with x_0 = x satisfying (L1), (L2) (constants C,
theta) and sum d(x_i, x_{i+1}) <= L is closed in the compact metrizable space M^N (each condition is closed). The map
(x_i) -> lim x_i is Borel on it (a pointwise limit of the continuous coordinate maps). So Ahat_theta(x) is a countable union
of Borel images of compact sets, i.e. analytic, hence universally measurable. By (i), (ii) and invariance of omega, the sets
g_s Ahat_theta(x), s in [0, 1), are pairwise disjoint and of equal measure; so the measure is 0.
(iv) is Theorem IC-T with tau = 0 combined with Theorem IC. ∎

So under GH + volume the "infinite-chain accessible sets" are thin, cross each local weak-stable leaf of their base point only
in the strong stable leaf (Theorem IC-T), and carry no non-degenerate infinite cycle (Theorem IC). This strictly contains
Corollary T2 of R12-a (finite chains).

## 3. General (non-volume) case: two infinite chains absorb both the flow shift and the holonomy (new; proved)

Without a smooth invariant volume, Theorem IC-T (integrality) is unavailable, and Theorem IC needs the exact strong-stable
ending (L5) plus the real equation (HC). Both can be removed at the price of a second chain, by the group-ring device of
Theorem G of R7-f.

Notation: for psi = sum_j c_j [s_j] in the group algebra C[R] (finite sums, [a][b] = [a+b]) and a distribution density S put
(psi ⋆ S)(phi) := sum_j c_j S(Gamma_{s_j} phi). Then (psi ⋆ S)(Gamma_t phi) = sum_j c_j S(Gamma_{t + s_j} phi), and
(psi psi') ⋆ S = psi ⋆ (psi' ⋆ S). For a function F on R, (psi ⋆ F)(t) := sum_j c_j F(t + s_j).

**Theorem IC2.** Assume GH. Let x_0 be a point and let (a_i), (b_i) be two summable chains with a_0 = b_0 = x_0, constants
(C, theta), limits p_1, p_2, and assume (L4) (with the same eta < theta) for both chains. Assume the *weak-stable endings*:
there are real tau_1, tau_2 with
 d(g_t p_k, g_{t + tau_k} x_0) <= C e^{-theta t} for all t >= 0 (k = 1, 2).
Assume finally that each chain has an *orbit-isolated vertex*: a vertex v_k != x_0 of the k-th chain, occurring exactly once
in the combined list of vertices of both chains, which is neither a zero of X nor periodic, and whose orbit contains no other
vertex of either chain and neither p_1 nor p_2. Then we have a contradiction.
No holonomy condition and no condition on tau_1, tau_2 is needed.

*Proof.* Let S_k, S'_k be the u- and s-groupings of chain k (Section 1, weights w^{(k)}_i, limits w^{(k)}_inf), so that
S_k - S'_k = delta_{x_0} - w^{(k)}_inf delta_{p_k}, S_k(Gamma_t phi) = O(e^{-(theta-eta)|t|}) ||phi||_{C^1} for t <= 0 and
S'_k(Gamma_t phi) = O(e^{-(theta-eta)t}) ||phi||_{C^1} for t >= 0 (steps 1-4 of Theorem IC; (L5),(HC) are not used there).
1. *The endpoint terms.* Put F(t) := e^{J_t(x_0)} phi(g_t x_0) and q_k := g_{tau_k} x_0. Since p_k and q_k are forward
   asymptotic at rate theta, beta_k := lim_{t -> +inf} (J_t(q_k) - J_t(p_k)) exists and |J_t(q_k) - J_t(p_k) - beta_k| <=
   Lip(d) C e^{-theta t}/theta. Also e^{J_t(q_k)} phi(g_t q_k) = e^{-J_{tau_k}(x_0)} F(t + tau_k) (cocycle identity). Hence, for t >= 0,
   (delta_{x_0} - w^{(k)}_inf delta_{p_k})(Gamma_t phi) = ((1 - c_k [tau_k]) ⋆ F)(t) + E_k(t),
   c_k := w^{(k)}_inf e^{-beta_k} e^{-J_{tau_k}(x_0)} > 0, |E_k(t)| <= C_k e^{J_t(q_k)} e^{-theta t} ||phi||_{C^1} <= C'_k e^{-(theta-eta)t} ||phi||_{C^1}
   (by (L4) at x_0: J_t(q_k) = J_{t+tau_k}(x_0) - J_{tau_k}(x_0) <= const + eta t).
2. *Case psi_1 := 1 - c_2[tau_2] = 0*, i.e. tau_2 = 0 and c_2 = 1. Then p_2 is in the strong stable set of x_0 and
   w^{(2)}_inf = e^{beta^s(x_0, p_2)}, which is (L5) + (HC) for chain 2. Theorem IC applied to chain 2, whose vertex v_2 is
   isolated (orbit-isolation implies isolation), gives a contradiction. The case 1 - c_1[tau_1] = 0 is symmetric.
3. *Case psi_1 != 0 and psi_2 := -(1 - c_1[tau_1]) != 0.* Put S := psi_1 ⋆ S_1 + psi_2 ⋆ S_2, an element of (C^1)'.
   - t <= -T_0, T_0 := |tau_1| + |tau_2|: all shifted times t + s_j are <= 0, so |S(Gamma_t phi)| <= C'' e^{-(theta-eta)|t|} ||phi||_{C^1}.
   - t >= T_0: S_k = S'_k + (delta_{x_0} - w^{(k)}_inf delta_{p_k}) and step 1 give
     S(Gamma_t phi) = [psi_1 ⋆ (S'_1(Gamma_. phi) + E_1) + psi_2 ⋆ (S'_2(Gamma_. phi) + E_2)](t) + ((psi_1(1 - c_1[tau_1]) + psi_2(1 - c_2[tau_2])) ⋆ F)(t).
     The last ring element is (1 - c_2[tau_2])(1 - c_1[tau_1]) - (1 - c_1[tau_1])(1 - c_2[tau_2]) = 0 (C[R] is commutative), so
     |S(Gamma_t phi)| <= C'' e^{-(theta-eta)t} ||phi||_{C^1}.
   - |t| <= T_0: |S(Gamma_t phi)| <= C''' ||phi||_{C^1}, since Gamma_s is bounded on C^1 uniformly for |s| <= 2T_0.
   By Theorem J (k = 1, S real), S = 0.
4. *S != 0.* S is a convergent (after grouping) combination of Dirac masses at the points g_s y, y a vertex of chain 1 and
   s in supp psi_1 ⊂ {0, tau_2}, or y a vertex of chain 2 and s in supp psi_2 ⊂ {0, tau_1}; these points accumulate only at
   the finitely many points g_s p_k. Consider v = v_1. If g_s y = v for one of these (y, s), then y lies on the orbit of v, so
   y = v (orbit isolation) and s = 0 (v is not periodic). The points g_s p_k are not v (p_k is not on the orbit of v). So a
   bump phi at v vanishing near all other points and accumulation points gives S(phi) = w^{(1)}_{v} · (coefficient of [0] in
   psi_1) = w^{(1)}_v · (1 if tau_2 != 0, 1 - c_2 if tau_2 = 0), which is nonzero (in case 3 with tau_2 = 0 we have c_2 != 1).
   This contradicts step 3. ∎

**Remarks.** (i) For finite chains this is Theorem G of R7-f for a graph made of two cycles through x_0 (cyclomatic number 2,
so N > p + q), with weak classes. The new point, as in Section 1, is that the chains may be infinite with summable legs, so
"closing" is replaced by "converging into the weak-stable set of x_0". (ii) The flow direction and the Jacobian holonomy are
both absorbed; only the genuine centre (the E^c_0 directions, dimension c - 1 >= 1) still has to be "closed", and only in the
limit. (iii) In the volume case one chain suffices (Section 2).

## 4. What Sections 1-3 reduce (PE0) to (GH-free statements; proved reductions)

**Corollary R1 (volume case).** Suppose the following GH-free statement holds:
(IC-vol) *For every C^inf flow on a compact connected manifold of dimension >= 2 preserving a smooth probability density omega
with h_omega(g_1) > 0, there are theta > 0 and x in M such that (alpha) omega(Ahat_theta(x)) > 0, or (beta)
Ahat_theta(x) ∩ Ahat_theta(g_tau x) != ∅ for some tau != 0, or (gamma) some summable chain (rate theta) from x whose limit
lies in the strong stable set of x has S = sum_i (delta_{x_{2i}} - delta_{x_{2i+1}}) != 0 (e.g. it has an isolated vertex).*
Then every GH vector field preserving a smooth volume has zero topological entropy.
*Proof.* Under GH + volume the flow is uniquely ergodic with invariant measure omega (O2), so h_top(g_1) > 0 gives
h_omega(g_1) > 0 by the variational principle. (alpha), (beta) contradict Corollary IC-N (iii), (ii); (gamma) contradicts
Theorem IC (volume case). dim M = 1 is trivial. ∎

**Corollary R2 (general case).** Suppose the following GH-free statement holds:
(IC-gen) *For every C^inf vector field and every g_1-invariant, g_1-ergodic Borel probability mu with h_mu(g_1) > 0 and
int J_1 dmu = 0, there are a point x_0 and two summable chains from x_0 satisfying (L4) for some 0 <= eta < theta, with
weak-stable endings and orbit-isolated vertices (Theorem IC2).*
Then (PE0) holds, and with the chain of the brief (steps 1-2) every GH field has zero topological entropy.
*Proof.* Theorem IC2. ∎

*How R1, R2 compare with the earlier targets.* (Q-vol) of R12-a (an exact non-degenerate closed su-chain, or a chain from x to
g_t x with t != 0) implies (IC-vol): a finite chain padded with zero-length legs is a summable chain; for a closed one, S is
the alternating sum of R12-a (non-degenerate means S != 0, which is (gamma)); a chain from x to g_t x, t != 0, gives
g_t x in Ahat_theta(x) ∩ Ahat_theta(g_t x), which is (beta). (EG), (AC), (CH) of earlier rounds ask for exact finite configurations, obtained if at all by
compactness from approximate ones, which loses non-degeneracy (R12-b). (IC-vol)/(IC-gen) only ask that su-paths can be steered
back into the weak-stable set of the base point **in the limit, with summable cost**, and the flow direction and (in the
general case) the Jacobian holonomy need not be controlled at all. Only the genuine centre E^c_0 (dimension c - 1 >= 1) must be
steered.

**Proposition CP (a sufficient local "steering" property; proved).** Let K be a compact set on which the local leaves have
uniform constants as in the availability remark of Section 1, and x_0 in K. Put Delta(q) := dist(q, W^s_loc(x_0)). Suppose
there are r_0 > 0, kappa in (0,1), A, alpha > 0 with:
 (i) there is x_1 in K ∩ W^u_loc(x_0), x_1 != x_0, with Delta(x_1) <= r_0;
 (ii) for every q in K with Delta(q) <= r_0 and every finite set F ⊂ M there is a finite su-path q = y_0, y_1, ..., y_m = q' with
     all y_j in K, consecutive points on a common local leaf (u and s alternately, starting with u) of one of them, total length
     <= A Delta(q)^alpha, Delta(q') <= kappa Delta(q), and y_j not in F for j >= 1.
Then (gamma) of (IC-vol) holds at x_0 (with the same theta), and in the general case one obtains a summable chain from x_0 with
limit in W^s_loc(x_0); if (L4) holds on K and (ii) can be run twice with disjoint vertex sets (including orbits) one obtains
the data of Theorem IC2.
*Proof.* Put q_0 := x_1 and choose q_{k+1} := q'_k by (ii) applied to q_k with F := all vertices chosen so far together with
x_0, x_1. Then Delta(q_k) <= kappa^k r_0, the k-th path has length <= A kappa^{k alpha} r_0^alpha, so the concatenated path
(padded by zero-length legs where two legs of the same type meet) is a summable chain; its limit p lies in K (closed) with
Delta(p) = 0, i.e. p in W^s_loc(x_0). The vertex x_1 is distinct from all later vertices (by the choice of F) and from p
(W^u_loc(x_0) ∩ W^s_loc(x_0) = {x_0} for Pesin local manifolds, and x_1 != x_0). So x_1 is isolated. ∎

**Why (ii) is not proved here (the remaining gap, precise).** In a Lyapunov chart at q, a u-leg and an s-leg change the u- and
s-coordinates freely but change the E^c_0-coordinate only through the "bracket" (holonomy defect) of su-quadrilaterals. (ii)
needs: at every small scale r and near every point of K, the E^c_0-defects of su-loops in K of cost <= A r^alpha contain a
positively spanning family of vectors of size comparable to r^{1+alpha'} (then a greedy choice gives the factor kappa). In the
uniformly partially hyperbolic C^1 setting this follows from non-integrability (Brin's quadrilateral argument); if instead all
small quadrilaterals close, (gamma) holds with a finite chain. In the Pesin setting the leaves through points of K depend only
Hölder-continuously on the base point and K ∩ leaf is a fractal set of positive leaf measure, so the defect map is only a
continuous map on a fractal parameter set; I could not show that its values are directionally rich at all scales, nor that
failure of richness forces exact closing. Note that one-sidedness of the defects is NOT an obstruction (u-first and s-first
quadrilaterals have defects of opposite orientation, and a correction may concatenate one of each), and non-degeneracy needs
only one isolated vertex (x_1), so retracing portions of the path is harmless. The gap is therefore a purely geometric,
GH-free statement about non-uniform partial hyperbolicity with a zero exponent: **"steerability in the centre at all scales,
or exact closing"**.

*Model check (sketch, not a proof about flows).* In the Heisenberg lamination model of Example 2.3 of R12-e (u-leaves = lines in
x, s-leaves = curves tau -> (x, y + tau, z + x tau), centre = z), a u-first quadrilateral with sides (a, b) based at (x,y,z) ends at
(x, y, z + ab), and one with sides (a, -b) ends at (x, y, z - ab); so two quadrilaterals close exactly (a non-degenerate 8-cycle).
If all vertices are required to lie in a fractal set K = A_1 x A_2 x A_3 of positive measure (fat Cantor sets), exact closing
may fail (the parameter set of admissible (a, b) is fractal, so the intermediate value argument is unavailable), but steering
works: at a Lebesgue density point, the admissible (a, b) at scale r have almost full measure in [-r, r]^2, so the product ab
can be chosen within a factor 1 ± 1/2 of any prescribed value of size <= r^2/4, with all vertices in K near density points;
iterating gives a summable chain converging back into W^s_loc of the base point, with cost O(|defect|^{1/2}) per step. This is
exactly the situation Proposition CP is designed for: **infinite chains replace the intermediate value theorem by Lebesgue
density.** For an actual non-uniformly partially hyperbolic flow the missing ingredient is a first-order expansion of the
quadrilateral defect, D_q(a, b) = kappa(q)(a, b) + o(|a||b|) with kappa non-degenerate near the points visited (C^1 dependence
of the stable leaves along unstable leaves on Pesin blocks, i.e. (SR) of R12-b, plus a non-vanishing bracket), or else a proof
that its failure forces exact closing.

## 5. The planner's Mechanism C(b) cannot work as stated (proved), and is superseded by Theorem IC2

Mechanism C turns a weighted chain closing up to a flow shift into the identity l^w + seg^w = c nu (by L1), and in a flow box
into "a summable weighted transversal dipole sum equals c w_0 dz"; step (b) hoped to exclude c != 0 from the form of this
identity. The form alone excludes nothing:

**Lemma D (every finite measure is a positive-weight dipole sum).** Let m >= 1, mu a finite positive Borel measure on R^m with
support in a cube Q_0, and q_inf a point outside Q_0. There are pairs (alpha_k, beta_k) and weights c_k > 0 with
sum_k c_k |alpha_k - beta_k| < inf such that mu(eta) = sum_k c_k (eta(alpha_k) - eta(beta_k)) for every Lipschitz eta on R^m
with eta(q_inf) = 0 (in particular for every Lipschitz eta supported in a ball disjoint from q_inf).
*Proof.* Let D_j be the dyadic subcubes of Q_0 of level j (side s_0 2^{-j}), c(Q) the centre of Q, and
mu_j := sum_{Q in D_j} mu(Q) delta_{c(Q)} (assign boundary points to one cube). Then
mu_{j+1} - mu_j = sum_{Q in D_j} sum_{Q' child of Q} mu(Q') (delta_{c(Q')} - delta_{c(Q)}), a sum of dipoles with weights
mu(Q') >= 0 and lengths |c(Q') - c(Q)| <= sqrt(m) s_0 2^{-j-2}; the total weighted length at level j is <= sqrt(m) s_0 2^{-j-2} mu(Q_0),
summable in j. Also mu_0 = mu(Q_0)(delta_{c(Q_0)} - delta_{q_inf}) on functions vanishing at q_inf. Summing,
the partial sums equal mu_J(eta) -> mu(eta) for continuous eta (mu_J -> mu weak*, the cubes shrinking). Dipoles with weight 0
are discarded. ∎

So the transversal identity is consistent with any c (for c < 0 exchange alpha_k and beta_k); a proof of (b) would have to use
the specific dynamical origin of the weights (e^{J_t} along finitely many orbits) and of the positions of the crossings, and I
see no mechanism for that. **But Mechanism C is not needed:** Theorem IC2 removes both the flow shift and the holonomy condition
at the cost of a second chain, using only Theorem J (no integrality, no L1 at the level of the cycle functional).

## 6. Mechanism E (second conformal density): not advanced
I did not find a construction of a finite measure (or distribution) sigma != c nu with L_X sigma = d sigma from a
non-hyperbolic mu. The only remark I can add: by Corollary IC-N and Theorem IC2 a counterexample's su-structure is "acyclic even
in the limit", so a product-type (local product structure) construction of sigma as in Lemma S / Proposition D of R12-d is
unavailable for exactly the same geometric reason as the chains; Mechanism E does not seem to bypass the centre-steering gap.

## 7. Status

**Answer to the task.** I could neither prove (PE0) nor construct a counterexample. (A counterexample would be a GH field with
positive entropy, hence not smoothly conjugate to a Diophantine linear flow, i.e. a counterexample to the Greenfield–Wallach
conjecture; see R11-d.) I did not find any flaw in the chain "variational step + entry 113 + (PE0) => h_top = 0" as quoted in the
brief; I did not re-verify entry 113 (R11-a) myself.

**Proved here (new, complete proofs above; GH used only through Theorem J and, in Section 2, through the volume-case identity
(3.1)/Lemma I of Theorem T):**
1. Theorem IC: no summable infinite su-chain whose limit is in the strong stable set of its first point, with Jacobian holonomy
   condition (HC) and growth condition (L4), has S != 0 (e.g. an isolated vertex). Volume case: (L4), (HC) automatic.
2. Theorem IC-T (volume case): a summable chain cannot end in W^s(g_tau x_0) with tau != 0.
3. Corollary IC-N (volume case): the infinite-chain accessible sets Ahat_theta(x) are analytic, omega-null, pairwise disjoint
   along each orbit; this strictly extends Corollary T2 of R12-a.
4. Theorem IC2 (general case): two summable chains from a common point, ending anywhere in its weak stable set (arbitrary flow
   shifts, no holonomy condition), with orbit-isolated vertices, contradict GH.
5. Lemma D: any finite measure is a positive-weight summable dipole sum; hence step (b) of the planner's Mechanism C cannot follow
   from the form of the transversal identity (and Mechanism C is superseded by item 4).
6. Proposition CP: a local "centre-steering" property on a Pesin block implies the hypothesis of item 1 (and, run twice, of
   item 4).

**Reductions (proved):** the volume case of the problem follows from the GH-free statement (IC-vol) (Corollary R1); (PE0), hence
the whole problem via the brief's chain, follows from the GH-free statement (IC-gen) (Corollary R2). Both are weaker than the
earlier targets (Q-vol), (EG), (AC), (CH): no exact closing, no compactness, no control of the flow direction, and (general
case) no control of the Jacobian holonomy; only the genuine centre E^c_0 must be steered, and only in the limit with summable
cost.

**Open (explicitly):**
- (PE0) itself.
- (IC-vol) and (IC-gen): steerability of su-paths in the genuine centre at all scales on Pesin blocks of a non-hyperbolic
  positive-entropy measure, or else exact closing ("centre-steering or closing" dichotomy for non-uniform partial
  hyperbolicity with zero exponents). The precise missing local input is (ii) of Proposition CP; the difficulty is that Pesin
  leaves depend only Hölder-continuously on fractal sets of base points, so the quadrilateral defect map has no first-order
  (bracket) expansion. With C^1 stable holonomies along unstable leaves on a Pesin block (the regularity (SR) of R12-b) and a
  nonvanishing bracket, the greedy steering of Proposition CP would go through (sketch only, not written out).
- Whether GH itself forces any accessibility-type property (no GH consequence beyond Theorem J, Lemma I and L1 is used above).

=== END OF ANSWER round13_q1 ===

