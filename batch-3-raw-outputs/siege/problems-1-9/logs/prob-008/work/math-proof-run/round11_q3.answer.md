# round11_q3: attempt on (AP)

## Plan / status (written first)
Target: (AP), or zero entropy for GH flows by any route.
Outcome: **(AP) is NOT proved and NOT refuted.** I found no counterexample. Below are (1) a check of the chain, (2) some rigorous observations about the volume case lambda = 0 (where (AP) has its simplest form), which reduce it to a statement about cohomology-free flows, and (3) the exact point where every attempt stopped.

## 1. Check of the chain (steps 1-4)
- Step 1 (variational principle for the homeomorphism g_1, then Jacobs' formula / ergodic decomposition of entropy): correct.
- Step 2: Rec = {z : z in alpha(z) and z in omega(z)} is Borel. Poincare recurrence for g_1 and for g_{-1} gives nu'(Rec) = 1. Intersecting the full-measure set G with Rec does not affect Steps 3-4: for nu'-a.e. x, the conditional measure nu'^xi_x gives full mass to G ∩ Rec and has no atoms, so a y != x in G ∩ Rec ∩ xi(x) exists. The backward exponential estimate is first obtained at integer times for g_{-n}. It extends to all real t <= 0 because the flow is uniformly Lipschitz on [0,1]. I find no flaw.
- Step 3: the reduction X -> -X is correct. -X is GH. The log-Jacobian of -X is J^{-X}_t = J_{-t}, so its Birkhoff average is -lambda. The entropy of nu' is the same for g_{-1} as for g_1.
- So the chain is sound, and the problem reduces to (AP) with lambda <= 0. By Theorem J only lambda = 0 and lambda <= -theta remain. Proposition N (entropy lies in exponents <= |lambda| when lambda < 0) shows the case lambda <= -theta is exactly the case where the pair cannot be pushed into faster unstable leaves.

## 2. The volume case: rigorous observations (all proved)
Assume GH, dim M >= 2, and a smooth positive invariant density omega. Take nu = omega, so d = 0 and J = 0. Write omega-hat = omega/omega(M).

**Lemma V1 (GH + volume gives CF with a tame inverse).** Every X-invariant distribution density is c·omega. Hence X(C^inf) = {f : omega(f) = 0}. The inverse X^{-1}: C^inf_0 -> C^inf_0 (inverse onto the mean-zero functions) is continuous. Concretely, for every k there are m and C with ||X^{-1} f||_{C^k} <= C ||f||_{C^m}.
*Proof.* Let T be an invariant density and write T = v·omega with v a distribution. Then 0 = L_X(v omega) = (Xv) omega because div_omega X = 0. So Xv = 0, and v is constant by L1. The closed-range statement (Text A, duality consequence) then gives X(C^inf) = ann(c·omega) = {omega(f) = 0}. The bound is Lemma 2 of Text B. ∎

**Lemma V2 (uniformly bounded discrepancy).** For all x, all t and all smooth f, |∫_0^t f(g_s x) ds − t·omega-hat(f)| <= 2C ||f||_{C^m}. Here m and C are those of V1 with k = 0.
*Proof.* Let u = X^{-1}(f − omega-hat(f)). The integral in question equals u(g_t x) − u(x). ∎

**Lemma V3 (pair identity).** Let x != y satisfy (a) of (AP). Define B(psi) = ∫_{-inf}^0 [psi(g_s x) − psi(g_s y)] ds. This is a distribution of order 1, since |B(psi)| <= ||psi||_{C^1} C/theta. For every smooth psi and every real t,
  ∫_{-inf}^t [psi(g_s x) − psi(g_s y)] ds = u_psi(g_t x) − u_psi(g_t y), where u_psi = X^{-1}(psi − omega-hat(psi)).
Consequently, with m and C from V1 for k = 1,
  |∫_{-inf}^t [psi(g_s x) − psi(g_s y)] ds| <= C ||psi||_{C^m} dist(g_t x, g_t y) for all real t.
B is nonzero, because B(X phi) = phi(x) − phi(y).
*Proof.* Both sides are linear in psi and vanish at psi = 1. By V1, C^inf = R·1 + X(C^inf), so it suffices to check psi = X phi. For that psi, the left side is lim_{R->inf} [phi(g_t x) − phi(g_t y) − phi(g_{-R} x) + phi(g_{-R} y)], which equals phi(g_t x) − phi(g_t y) by (a). On the right side, u_{X phi} = phi − omega-hat(phi), so the right side is the same quantity. ∎

**Remark V4 (where entropy must live in the volume case).** Under GH + volume, omega is the only invariant probability (O2), so positive entropy means h_omega > 0. The flow is minimal, so it has no periodic orbit when dim M >= 2. Katok's horseshoe/closing theorem (cited from memory: a C^{1+alpha} flow with a hyperbolic ergodic measure of positive entropy has hyperbolic periodic orbits) then forces omega to be non-hyperbolic: it has a zero exponent transverse to X. Theorem J gives the same conclusion inside this program. In this case (AP) says: in a minimal, uniquely ergodic, cohomology-free volume-preserving flow, there is no bi-recurrent pair that is exponentially asymptotic in backward time.

**What V3 does and does not give.** V3 says the two orbits of an (AP)-pair spend equal time in every smooth "bump", up to an error C ||psi||_{C^m} dist(g_t x, g_t y), at every time t. If the pair were proximal along a sequence t_n -> +inf, i.e. dist(g_{t_n} x, g_{t_n} y) -> 0, the occupation-time differences would tend to 0 along t_n. Neither recurrence of x and y separately nor V2 yields a contradiction from this. V2 already bounds each orbit's discrepancy by O(1), so independent excursions after the orbits separate do not produce growing differences. This is exactly the approximate-coincidence problem (AC) of round9_q9 in its plainest form.

## 3. Dead ends checked this round (with reasons)
- **Counting separated orbits against the tame estimate.** Take e^{hT} (T, eps)-separated orbit segments. Bowen-ball test functions of length L have C^m norms of order e^{m·Lip·L}, while the frequencies to be distinguished are of order e^{-hL}. The tame bound ||X^{-1} f||_{C^0} <= C ||f||_{C^m} therefore gives discrepancy bounds e^{m·Lip·L}, which are far too weak. Derivative growth always beats entropy here. The same happens with u = ∫ rho(s) psi∘g_s ds, or with comparing ||u∘g_t||_{C^k} and ||(Xu)∘g_t||_{C^m}: the loss m > k destroys any comparison of exponents.
- **Spectral/CLT route (volume case).** V1 gives ∫ xi^{-2} dsigma_f(xi) < inf for every smooth mean-zero f, so every smooth f has zero asymptotic variance. A positive-entropy factor has Lebesgue spectrum, but that does not prevent a dense subspace (the smooth functions) from having spectral densities that vanish at 0. No contradiction is obtained without a C^m-bounded family whose spectral density at 0 stays away from 0. Constructing such a family is the same difficulty as above.
- **Time changes / choosing faster leaves for lambda < 0.** A time change rescales all exponents and lambda by the same factor, so |lambda|/chi does not change. Proposition N says the entropy sits in exponents <= |lambda|, so the pair cannot be taken in a leaf with rate > |lambda|. The vanishing-moment idea (planner's (1)) needs a smooth 1-dimensional sub-leaf on which the backward dynamics is affine up to tempered errors. I could not extract such a sub-leaf from the data (a)-(c), nor in general from Pesin theory when the slow exponents are not simple.

## 4. Summary: what is proved, what is open
- **Proved here:** the chain (steps 1-4) is sound (Section 1). In the volume case, GH is equivalent to CF with a tame inverse (V1). This gives uniformly bounded discrepancy (V2) and the pair identity and bound (V3). In that case the only possible positive-entropy measure is the volume, and it must be non-hyperbolic (V4; uses Katok's theorem, cited from memory).
- **Open:** (AP) for lambda = 0, even under a smooth invariant volume (minimal, uniquely ergodic, cohomology-free flows). Also open: (AP) for lambda <= -theta. Hence zero topological entropy for GH flows in dimension >= 4 remains unproved by this attempt.
- **Precise stopping point:** we need a mechanism that converts the two-sided-in-time pair data into forward cancellation, that is, forward decay of the transported pair density at a quasi-analytic or exponential rate. V3 shows the forward transport is bounded by dist(g_t x, g_t y), but nothing forces that distance to become small along t -> +inf.

=== END OF ANSWER round11_q3 ===
