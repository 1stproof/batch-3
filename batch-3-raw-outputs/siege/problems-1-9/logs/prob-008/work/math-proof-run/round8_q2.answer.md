# round8_q2: answer

## 0. Status (read this first)
- **(PE-NH) is not proved here, and I found no counterexample.** So the problem's claim is still proved only in the cases listed in the brief: dim M <= 3, hyperbolic measures, and the mu(d)-bands of Prop. 6.1 / Prop. N.
- **Chain check.** I re-checked step 2 (Theorem 5.1, modulo [Ru] and [KLY]) and step 4 (variational principle, reduction to flow-ergodic measures, Jacobs' formula). I see no flaw in either. The chain is sound: (PE-NH) would finish the problem.
- **New rigorous results (Sections 1-2).** They locate exactly where the closed-range half of GH can and cannot enter.
  - **Proposition A (proved).** Under GH, a smooth invariant volume exists, i.e. (V) holds, iff the weighted operator P = X + d has closed range in C^inf(M).
  - **Proposition B (proved).** Under GH, (V) holds iff the space I of X-invariant distribution densities is one-dimensional.
  - **Corollary C (dichotomy).** Outside the volume case, neither operator has both properties that a Jordan-chain-plus-tame-inverse argument needs (uniqueness at eigenvalue 0, and a tame inverse on the range):
    - the weighted operator P (Theorem J's operator) has the uniqueness (K0), but no closed range;
    - the unweighted X has the tame inverse, but not the uniqueness.
    - Inside the volume case the two operators coincide. What remains there is only the growth of the iterated inverses (Theorem V of R7-e).
- Section 3 records the routes I tried and the exact points where they stop.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, and P phi = X phi + d phi, so that L_X(phi nu) = (P phi) nu. A distribution u corresponds to the density T = u nu, with <Xu, phi nu> = -T(P phi). We write nu-hat(phi) = int phi dnu / nu(M) and ker nu-hat = {psi in C^inf : int psi dnu = 0}. I is the space of distribution densities T with T(X phi) = 0 for all phi; these are the X-invariant ones.

## 1. Proposition A: (V) iff P has closed range

**Proposition A.** Assume GH. The following are equivalent.
(i) X preserves a smooth positive density (V).
(ii) P(C^inf(M)) is closed in C^inf(M).
When they hold, P(C^inf) = ker nu-hat.

*Proof.*

**(i) => (ii).** Let rho nu be a smooth positive invariant density, so L_X(rho nu) = 0. For smooth phi,
 L_X(rho phi nu) = (X phi) rho nu + phi L_X(rho nu) = rho (X phi) nu.
So P(rho phi) = rho X phi, i.e. P = M_rho X M_rho^{-1}, where M_rho (multiplication by rho) is a topological automorphism of C^inf. Hence P(C^inf) = rho X(C^inf). This is closed, because X(C^inf) is closed (Corollary 3 of Text B).

**(ii) => (i).** Four steps.

*Step 1: P(C^inf) is dense in ker nu-hat, hence equal to it.*
- P(C^inf) lies in ker nu-hat, because int (P phi) dnu = int_M L_X(phi nu) = int_M d(i_X phi nu) = 0.
- Let T be a continuous functional on C^inf vanishing on P(C^inf). Then T(P phi) = 0 for all phi, so T = c nu by (F1). Such a T vanishes on ker nu-hat.
- By Hahn-Banach, P(C^inf) is therefore dense in ker nu-hat. Under (ii) it is closed, so P(C^inf) = ker nu-hat.

*Step 2: ker P != 0.*
- Suppose P is injective. Then P : C^inf -> ker nu-hat is a continuous linear bijection between Fréchet spaces (ker nu-hat is a closed subspace). By the open mapping theorem, P^{-1} is continuous.
- Put S_0(psi) := -nu(P^{-1} psi) on ker nu-hat. This functional is continuous. Extend it to S in (C^inf)' by Hahn-Banach (locally convex form).
- Then S(P phi) = -int phi dnu for all phi. So u := S/nu satisfies <Xu, phi nu> = -S(P phi) = int phi dnu, i.e. Xu = 1.
- This contradicts (K1). (By GH u is smooth, and at a maximum point of u we have Xu = 0.)

*Step 3: a non-negative smooth invariant density.*
- P has real coefficients, so ker P contains a real rho != 0. Then Pρ = 0, i.e. X rho = -d rho.
- Along orbits, d/dt rho(g_t x) = -d(g_t x) rho(g_t x), so rho(g_t x) = rho(x) e^{-J_t(x)}. Hence U_+ = {rho > 0} and U_- = {rho < 0} are open and invariant.
- A nonempty open invariant set is nu-conull (Lemma D of R7-d). Proof: for an invariant Borel set B, X 1_B = 0 in D', so 1_B is a.e. constant by L1.
- U_+ and U_- are disjoint, so they cannot both be nonempty. Replacing rho by -rho, we may assume rho >= 0 and U_+ != ∅.
- Then U_+ is conull, hence dense, and Z := {rho = 0} is a closed invariant nu-null set.

*Step 4: Z is empty.*
- For eps > 0 put v_eps := log(rho + eps), which is smooth. Then
 X v_eps = f_eps := -d rho/(rho + eps).
 We have |f_eps| <= ||d||_inf, and f_eps -> -d · 1_{U_+} = -d nu-a.e. So f_eps -> -d in L^1(nu), hence in D'.
- Take smooth phi with int phi dnu = 0. By Step 1, phi = P psi with psi smooth. Then
 <v_eps, phi nu> = <v_eps, (P psi) nu> = -<X v_eps, psi nu> = -int f_eps psi dnu -> int d psi dnu.
- Put w_n := v_{1/n} - c_n, where c_n := nu-hat(v_{1/n}). For every smooth phi,
 <w_n, phi nu> = <v_{1/n}, (phi - nu-hat(phi)) nu>,
 which converges by the previous item.
- C^inf(M) is Fréchet, hence barrelled. By the Banach-Steinhaus theorem, the pointwise limit w is a distribution and w_n -> w weak*. Hence Xw = lim X w_n = lim f_{1/n} = -d, which is smooth. By GH, w is smooth.
- Take smooth chi >= 0 supported in U_+ with int chi dnu = 1. On U_+, v_{1/n} -> log rho in C^inf_loc. So int v_{1/n} chi dnu converges, and therefore c_n = int v_{1/n} chi dnu - <w_n, chi nu> converges to some c.
- Hence w = log rho - c on U_+, so log rho >= min_M w + c on U_+.
- If Z contained a point z, density of U_+ and continuity of rho would give points of U_+ where rho is arbitrarily small, i.e. log rho -> -inf. This is a contradiction. So Z = ∅.

So rho > 0 everywhere and rho nu is a smooth positive invariant density: (V) holds. The final claim of the proposition is Step 1. ∎

*Remarks.*
1. Proposition A only rewrites (V). It does not prove it. Its use is diagnostic: R7-e (end of §3) and the planner's sketch (2) both asked for a tame inverse of P on its range. Proposition A shows that this tame inverse exists exactly in the volume case, where P is conjugate to X and nothing new is gained.
2. In particular the iteration T_z(phi) = z^N T_z(P^{-N} phi) (Theorem V of R7-e) cannot be run in the non-volume case without first proving (V).
3. Cited only: the open mapping theorem, Hahn-Banach and Banach-Steinhaus for Fréchet spaces. GH enters through L1, (F1), (K1), and in Step 4 through GH itself applied to Xw = -d.

## 2. Proposition B and the dichotomy

**Proposition B.** Assume GH. Then (V) holds iff dim I = 1.

*Proof.*
- (V) => dim I = 1. Take nu = omega invariant. Then T in I iff u = T/omega satisfies Xu = 0 (by (O2)), iff u is constant (L1).
- dim I = 1 => (V). I contains every invariant probability, so I = R mu for the unique invariant probability mu. By the duality consequence of Text A, X(C^inf) = {f : mu(f) = 0}. Hence d - mu(d) = Xa with a smooth, and (O3) gives (V). ∎

**Corollary C (dichotomy for Jordan-chain arguments).** Assume GH and not (V).

*Weighted operator P (the operator of Theorems J, J*, G, Lemma M).*
- Uniqueness holds: T∘P = 0 implies T = c nu (F1), and the Jordan chain at 0 terminates (F2).
- But P(C^inf) is not closed (Proposition A).
- So no estimate |T(phi)| <= C ||P^{-1} phi||_{C^k}-type can be iterated, and the tame "divisibility" of Theorem V is unavailable.

*Unweighted operator X (functions transported without Jacobian weight).*
- The tame inverse exists (Lemma B of R7-d).
- But dim I >= 2 (Proposition B), so the unweighted Jordan chain does not terminate. Its moments are m_j(phi) = int t^j S(phi o g_t) dt.
  - From m_0∘X = 0 and m_1∘X = -m_0 one gets only m_0 in I and m_0(1) = 0.
  - That forces m_0 = 0 iff I ∩ {T : T(1) = 0} = 0, i.e. iff dim I <= 1, i.e. (V).
- So the unweighted analogue of Theorem J (no S != 0 with |S(phi o g_t)| <= C e^{-eps|t|} ||phi||_{C^k}) holds under GH iff (V) holds, as far as this proof goes.

*Consequence.* Any proof of (PE-NH) along the round-6/7 lines (moments at z = 0 + continuation or quantitative flatness near 0) must either
- (a) first prove (V), and then handle the volume case, where everything reduces to quantitative growth of ||R^N phi|| (Theorem V); or
- (b) use a mechanism that does not rest on a single operator having both uniqueness and a tame inverse.

Two checks:
- The unweighted moment claim is verified directly. Integration by parts as in Theorem J gives m_j(X phi) = -j m_{j-1}(phi).
- The weighted claim is Proposition A.

## 3. Routes attempted for (PE-NH) and where each stops

**3.1 Stable pairs, unweighted.** In the volume-free setting, take x != y on one Pesin stable leaf and S' = delta_x - delta_y. Then G_f(t) = S'(f o g_t) decays like e^{-theta t} forward and is bounded backward. This holds with no condition on d: the J_t-growth issue of the weighted picture disappears.
- The Laplace transforms give eigen-densities T_z∘X = z T_z on -theta < Re z < 0, and T_z is not identically 0 (Fourier uniqueness).
- The forward half A_z = int_0^inf e^{-zt} G dt is holomorphic on Re z > -theta, a neighbourhood of 0. Its Taylor coefficients form an infinite chain A_j∘X = -A_{j-1}, with A_0∘X = -S' and geometric bounds |A_j(f)| <= C theta^{-j-1} ||f||_{C^1}.
- The tame inverse R of X does exist here, but the chain lands in I, which is not one-dimensional unless (V) (Corollary C). So this route stops at the same point, with the roles of the two halves of GH exchanged.

**3.2 Real eigen-distributions (E1).** Assume all invariant measures have mu(d) = 0 and lambda* > 0. Then R5-a Theorem B gives a holomorphic family T_z (0 < Re z < theta) with T_z∘P = z T_z, splitting as B_z + F_z, where B_z is holomorphic on Re z < theta.
- If GH excluded nonzero real eigen-distributions for kappa in some interval (0, kappa_0), then B_z = -F_z there. So T_z = 0, and S = 0 by Fourier uniqueness.
- So (J1) would follow from "E1 near 0". I could not prove E1 near 0.
- The dual tame solvability (Lemma B(iii) of R7-d) gives only mixed-norm bounds ||T_z||_{(C^{m_j})'} <= C_j |z|^j ||T_z||_{(C^k)'}. These are the same non-quasi-analytic data as Theorem V.

**3.3 Bounded Birkhoff integrals (volume case).** Lemma F(3) of R7-d gives sup_{p,T} |int_0^T f(g_s p) ds - T omega(f)| <= C ||f||_{C^m}.
- I checked whether uniformly bounded discrepancy for all smooth f can by itself contradict positive entropy, via counting (T, eps)-separated segments. It cannot, at the level of generality where only the discrepancy bound is used.
- Encoding orbits by u = R(Phi), with Phi an embedding, gives bounded curves in R^N whose velocities are Phi(g_s x). Such curves can be exponentially many (bounded random-walk-type counts), so no contradiction follows.
- The k-point statistics of every segment are fixed up to errors e^{m Lambda tau}/T, which is consistent with typicality for omega, not with zero entropy.

**3.4 Spectral form (volume case).** By the nuclear spectral theorem (Gelfand-Kostyuchenko; cited from memory), applied to the skew-adjoint X on L^2(omega) with the rigging C^inf ⊂ L^2 ⊂ D', generalized eigenvectors u in H^{-s} with Xu = i xi u exist for sigma-a.e. xi. Here sigma is the maximal spectral type of X on L^2(omega).
- Hence, in the volume case, (E1-i) of R7-g (for each s, only countably many xi admit nonzero H^{-s} eigen-distributions) would force pure point spectrum.
- Pure point spectrum gives h_omega = 0, and by unique ergodicity (O2) h_top = 0.
- This is a sharper target in the volume case, but I could not prove (E1-i).

## 4. Summary of what is proved and what is open

**Proved here (complete proofs above).**
- Proposition A: under GH, (V) iff P(C^inf) is closed (and then P(C^inf) = ker nu-hat).
- Proposition B: under GH, (V) iff dim I = 1.
- Corollary C: outside (V), the weighted operator has uniqueness but no closed range, and the unweighted operator has a tame inverse but no uniqueness. Inside (V) the remaining difficulty is purely quantitative, via Theorem V.

**Not proved / open.**
- (PE-NH) itself, in particular its core case (PE0): mu(d) = 0, non-hyperbolic, positive entropy. This includes the volume-preserving case.
- The intermediate statements that would each suffice, by the arguments recalled above:
  - (J1);
  - E1 near 0 (no real eigen-distributions Xu = kappa u for small kappa > 0);
  - in the volume case, (E1-i) or a C^1-dense set of quasi-analytic vectors of R (Theorem V);
  - outside the volume case, (V) together with one of these.
- No counterexample was found. Any counterexample would have to be a GH flow with a non-hyperbolic positive-entropy ergodic measure. By Theorem 5.1 and Prop. N, its exponent sum would have to be 0 or large compared with the smallest exponent on the relevant side.

=== END OF ANSWER round8_q2 ===
