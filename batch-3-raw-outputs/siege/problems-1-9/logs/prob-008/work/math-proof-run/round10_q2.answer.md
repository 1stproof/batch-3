# round10_q2 — answer

## 0. Status

- **(JC) is not proved here, and no counterexample is given.** Nor are (NJ) or the zero-entropy goal proved.
- **Step 3 of the chain (Theorem A) was checked independently, line by line, and is correct (§1).** It delivers exactly what (JC) needs. The definitions match: functionals on C^1 are the same as order-<=1 distribution densities. The remarks in the statement of (JC) are also correct: c = 0 works for strips containing 0, and the statement does not depend on nu. I also re-checked the composition of the chain (steps 1-4). It is sound, so (JC) would finish the problem.
- §2 gives some small new facts, with proofs:
  - the time-change behaviour of chains;
  - a two-point form of the chain obstruction;
  - a remark on Banach perturbation, explaining why GH at 0 cannot be moved to c != 0 by semi-Fredholm stability (that would need a loss-free estimate);
  - the inheritance of chains under complex conjugation.
- §3 records the approaches I tried and exactly where each one fails.
- §4 lists the open questions.

---

## 1. Independent check of Theorem A (step 3 of the chain)

**Setting.** nu is a smooth positive density, d = div_nu X, P phi = X phi + d phi, and Gamma_t phi := e^{J_t} (phi o g_t), so that d/dt Gamma_t phi = Gamma_t P phi = P Gamma_t phi. This uses that (t, x) -> e^{J_t(x)} phi(g_t x) is jointly C^inf; the commutation P Gamma_t = Gamma_t P follows from Gamma_{t+s} = Gamma_t Gamma_s, by differentiating in s at s = 0.

**Theorem A (restated with k = 1).** Let Omega = {a < Re z < b}. Let T_z (z in Omega) be continuous linear functionals on C^1(M) such that:
- (i) z -> T_z(phi) is holomorphic for smooth phi;
- (ii) sup{|T_z(phi)| : a_1 <= Re z <= b_1, ||phi||_{C^1} <= 1} < inf on closed substrips;
- (iii) T_z(P phi) = z T_z(phi).

If some c in Omega carries no order-1 Jordan chain, then T_z = 0 for all z.

**Proof, re-derived.**

1. *Transport identity.* Fix z and smooth phi, and put h(t) = T_z(Gamma_t phi).
   - The map t -> Gamma_t phi is C^1 into C^1(M), indeed into C^inf, and T_z is continuous on C^1. So h is C^1 with h'(t) = T_z(P Gamma_t phi) = z h(t).
   - Hence T_z(Gamma_t phi) = e^{zt} T_z(phi).

2. *Gaussian superposition.* Put sigma = Re c and choose rho > 0 with [sigma - rho, sigma + rho] inside (a, b). Define
   S(phi) := (1/2 pi i) ∫_{Re z = sigma} e^{(z - sigma)^2 + omega (z - sigma)} T_z(phi) dz.
   - On the line z = sigma + iy, the weight has modulus e^{-y^2}. With (ii), S is a continuous functional on C^1.
   - F_phi(t) := S(Gamma_t phi) = (1/2 pi i) ∫ rho_omega(z) e^{zt} T_z(phi) dz, by step 1. Exchanging S with Gamma_t is legitimate: Gamma_t phi is smooth, and the integral is absolutely convergent for each fixed test function.
   - The integrand is holomorphic on the closed strip [sigma - rho, sigma + rho]. For fixed t it is bounded there by C e^{rho^2 + |omega| rho + |t|(|sigma| + rho)} e^{-y^2} ||phi||_{C^1}. So the horizontal connecting segments at |y| = Y contribute O(e^{-Y^2}) -> 0, and Cauchy's theorem moves the line to Re z = sigma ± rho.
   - This gives |F_phi(t)| <= K e^{(sigma + rho)t} ||phi||_{C^1} for t <= 0 (line sigma + rho), and |F_phi(t)| <= K e^{(sigma - rho)t} ||phi||_{C^1} for t >= 0 (line sigma - rho).
   - Hence H_phi(t) := e^{-ct} F_phi(t) satisfies |H_phi(t)| <= K e^{-rho|t|} ||phi||_{C^1}, because |e^{-ct}| = e^{-sigma t}.

3. *S != 0 for some omega.* If T is not identically 0, pick phi_0 and z_0 with T_{z_0}(phi_0) != 0. Then y -> T_{sigma+iy}(phi_0) is not identically 0, by the identity theorem on the connected strip. It is continuous and bounded by (ii). S_omega(phi_0) is, up to a constant, the Fourier transform at -omega of the nonzero L^1 function e^{-y^2} T_{sigma+iy}(phi_0). By Fourier uniqueness it is nonzero for some omega.

4. *Moments.* m_j(phi) := ∫ t^j H_phi(t) dt is continuous on C^1, with |m_j(phi)| <= K ||phi||_{C^1} ∫ |t|^j e^{-rho|t|} dt.
   - H_phi' = H_{(P-c)phi}, since F_phi' = F_{P phi}.
   - Integration by parts on [-R, R] is justified: the boundary terms R^j e^{-rho R} -> 0, and both integrals converge absolutely, using the bound of step 2 for phi and for (P - c)phi.
   - This gives m_0 o (P - c) = 0 and m_j o (P - c) = -j m_{j-1}.

5. *Using the hypothesis at c.*
   - If m_0 != 0, then (A, B) = (-m_1, m_0) is an order-1 Jordan chain at c: B o (P - c) = 0 and A o (P - c) = m_0 = B.
   - So m_0 = 0. Inductively, if m_{j-1} = 0 then m_j o (P - c) = 0 and (-m_{j+1}/(j+1)) o (P - c) = m_j. So m_j = 0 by the same argument.

6. *Conclusion.* G(xi) := ∫ e^{-i xi t} H_phi(t) dt is holomorphic on |Im xi| < rho, with all Taylor coefficients at 0 equal to (-i)^j m_j(phi) = 0. So G = 0, hence H_phi = 0 (continuous L^1 function with zero Fourier transform), hence S(phi) = H_phi(0) = 0 for every phi. This contradicts step 3. ∎

**Verdict: Theorem A is correct.** Three points needed care, and all three hold.
- (a) The chain (A, B) = (-m_1, m_0) consists of functionals continuous for the C^1 norm. This is exactly the class in the definition of (JC), "continuous linear functionals on C^1(M)". Distribution densities of order <= 1 extend uniquely to C^1, since C^inf is dense in C^1, so the two readings of (JC) coincide.
- (b) The chain relations are needed only on smooth phi. That is how (JC) is stated.
- (c) c may be non-real. Nothing in the proof uses Im c = 0.

**Matching Theorem R'.** The family of Theorem R' is continuous on C^1, holomorphic, bounded on closed substrips uniformly in Im z, satisfies T_z o P = z T_z on smooth phi, and is nonzero. So Theorem A applies with k = 1.

**Remarks in (JC).**
- *c = 0 under GH.* B o P = 0 gives B = C nu by (K0). Then A o P = C nu means Xu = -C for u = A/nu. By (K1) this forces C = 0, so B = 0. Correct.
- *nu-independence.* If nu' = e^w nu, then d' = d + Xw and P' = e^{-w} P e^{w}. The map (A, B) -> (A(e^w ·), B(e^w ·)) sends chains for P to chains for P', preserves order, and preserves B != 0. Correct.

**The whole chain.** Steps 1 and 2 were checked in R9-a. Step 3 is checked above. Step 4 is then a correct deduction. **Hence (JC) => [GOAL] is a valid implication.**

---

## 2. Small new facts (proved)

### 2.1 Chains under time change: an equivalent "weighted" form

**Lemma 2.1.** Let h > 0 be smooth and X' = hX. With the same nu, d' = h d + Xh and P' = P o M_h, where M_h is multiplication by h. A pair (A', B') is an order-k Jordan chain at c for P' if and only if, with A := A' o M_{1/h} and B := B' o M_{1/h},

  B o P = c B o M_{1/h},  A o P = c A o M_{1/h} + B o M_{1/h},  B != 0.

*Proof.*
- div_nu(hX) = h div_nu X + Xh, so P'phi = hX phi + (hd + Xh)phi = X(h phi) + d h phi = P(h phi).
- Substitute psi = h phi in B'(P'phi) = c B'(phi): this gives B(P psi) = c B(psi/h). The same substitution handles the A-relation.
- M_h is a C^k-automorphism, so orders are preserved. ∎

**Consequence.** GH is invariant under time change (O4), and positive entropy is preserved by time changes (Abramov). So (JC) for all GH fields is equivalent to the following: for every GH field X, every smooth positive h, and every strip of Theorem R for hX, some c in it admits no solution of the *generalized* chain problem with weight 1/h.

The strip for hX is the strip for X rescaled: lambda' = lambda / ∫h^{-1} dmu, and the exponents are scaled by the same factor. So nothing about the position of the strip relative to 0 can be changed this way. The ratio lambda/chi is a time-change invariant.

This rules out the hope, for instance, that a suitable time change moves the strip of a lambda != 0 measure onto 0. **Dead end, recorded with proof.**

### 2.2 Why GH at 0 does not propagate to c != 0 by perturbation (precise form of Remark 3.3 of R8-b)

**Lemma 2.2.** Let E, F be Banach spaces with E ⊂ F continuously, and L : E -> F bounded with an estimate ||u||_E <= C ||Lu||_F on a closed complement of ker L. Then for |c| < 1/(C ||i||) the operator L - c (where i : E -> F is the inclusion) satisfies the same type of estimate, with dim ker(L - c) <= dim ker L. This is standard (semi-Fredholm stability).

What GH gives is: for every k there are m = m(k) > k and C with ||u - mean||_{C^k} <= C ||Xu||_{C^m}.

**Remark (this is a diagnosis, not a theorem).** The natural Banach setting is:
- E = completion of C^inf under ||u||_{C^k} + ||Xu||_{C^m};
- F = C^m.

Then X : E -> F has kernel = constants and the estimate of Lemma 2.2. But the perturbation c·i : E -> F is bounded only if

  ||u||_{C^m} <= C' (||u||_{C^k} + ||Xu||_{C^m}),

which is a *loss-free* estimate. GH (via the closed graph theorem) does not provide it. It fails for Diophantine linear flows with tau > 0: for u = e_k with |k.alpha| ~ |k|^{-tau}, the left side is |k|^m and the right side is |k|^k + |k|^{m - tau}, so it fails whenever k < m - tau.

So the perturbative route from 0 to c != 0 is closed, even for fields where (JC) is true: Diophantine flows have no chains at all, as shown by Fourier series. Any transfer of GH from 0 to c != 0 must therefore use something non-perturbative, or a loss-free / quantitatively tame estimate ("quantitative tameness", open question 4 of R9-b). This only sharpens Remark 3.3 of R8-b and Remark D of R9-e; it is a barrier observation, not a contribution to (JC). (An earlier draft of this section claimed a general impossibility; that claim is withdrawn, because I have no proof that the loss-free estimate fails for every GH field.)

### 2.3 Complex conjugation and real structure

P has real coefficients. So if (A, B) is a chain at c, then (A-bar, B-bar), with A-bar(phi) := conj(A(conj phi)), is a chain at c-bar. Hence the set of chain-carrying points is symmetric about R.

Consequently, (JC) for the strip {a < Re z < b} may be checked at points with Im c >= 0. In particular it suffices to test real c, or any single vertical half-line. This is elementary but removes one degree of freedom from future searches.

### 2.4 A two-point form of the obstruction

Let (A, B) be a chain at c and fix phi with B(phi) != 0. As in Prop 7.3 of R9-b, A(Gamma_t phi) = e^{ct}(A(phi) + t B(phi)).

Hence the functional-valued map t -> e^{-ct} A o Gamma_t equals A + tB. It is affine in t, with nonzero slope B.

Under GH at c = 0 the slope is killed: by (K0) the slope B is a multiple of nu. Then A o P = (const) nu says that w = A/nu solves Xw = -const, so the constant is 0 by (K1). At c != 0 the slope B is an eigen-density at c, and no smooth object enters.

**Observation.** A chain at c gives, for every smooth phi with B(phi) != 0, a "time function along the transport":

  tau_phi(t) := A(Gamma_t phi) / B(Gamma_t phi) = A(phi)/B(phi) + t.

So the ratio A/B increases at unit speed along the weighted transport. This is the precise form of the formal identity X(alpha/b) = -1 for alpha = A/nu, b = B/nu.

For order-0 chains this ratio is realised as a Borel function (the r of Lemma 1.1, R9-c). This gives total dissipativity, and (K1) would follow if the ratio were a distribution. **For order 1 the ratio has no pointwise meaning, and I could not realise it.** This is where the order-1 case stops; see §3.2.

---

## 3. Approaches attempted for (JC) and where each stops

### 3.1 Volume case, iterated inverse plus Pinsker structure (new attempt; stops at the centre direction)

Setting: GH plus a smooth invariant volume omega, nu = omega, R = X^{-1} on mean-zero functions.

**Step (proved).** By Prop 3.1(c) of R8-e, for every N, R^N phi_0 has oscillation <= C theta^{-N} ||phi||_{C^1} along local strong unstable plaques of a Pesin block. By Cor 3.2 of R8-e, the same holds along local strong stable plaques, since the inverse for -X is -R.

**Step (proved).**
- Let sigma_phi be the spectral measure of phi in L^2(omega).
- The set of smooth phi such that 0 lies in the support of the spectral measure of the projection of phi onto the Pinsker complement H_P^perp is a dense G_delta in C^inf. Proof:
  - each set {phi : ||E(-1/n, 1/n) P^perp phi|| > 0} is open, being the complement of a closed subspace;
  - it is nonempty, since H_P^perp has Lebesgue spectrum when h_omega > 0 and C^inf is dense in L^2;
  - an open set whose complement is a proper closed subspace is dense;
  - Baire's theorem in the Fréchet space C^inf finishes.
- For such phi, put u_N := R^N phi_0 / ||R^N phi_0||_{L^2}. Then:
  - u_N has L^2 norm 1 and mean 0;
  - ||X u_N||_{L^2} -> 0, because ||R^{N-1} phi_0|| / ||R^N phi_0|| -> 0 when 0 is in the support of sigma_phi;
  - u_N has oscillation -> 0 along local s- and u-plaques of the Pesin block. Indeed ||R^N phi_0||_{L^2} >= (theta')^{-N} sigma_phi(|xi| < theta')^{1/2} for every theta' > 0, and sigma_phi(|xi| < theta') > 0 because 0 is in the support. Take theta' < theta. (This uses that the constants of Prop 3.1(c) of R8-e are uniform over a Pesin block, which is standard Pesin theory, cited.)
  - The ratio claim: write ∫ xi^{-2N+2} dsigma <= eps^2 ∫_{|xi|<eps} xi^{-2N} dsigma + eps^{-2N+2} sigma(M), and ∫ xi^{-2N} dsigma >= (eps/2)^{-2N} sigma(|xi| < eps/2). So the ratio has limsup <= eps^2 for every eps. (Countable Lebesgue spectrum on the Pinsker complement for positive-entropy flows is cited from memory: Rokhlin–Sinai / Gurevich.)

**Where it stops.** A Hopf-type argument would turn "almost invariant along X, s and u" into L^2-precompactness, then into a nonzero invariant mean-zero limit, contradicting ergodicity. That needs local product structure in which s, u and X span TM. With zero exponents transverse to X, the centre directions are uncontrolled. In the model "Anosov × Diophantine rotation" (not GH) such sequences exist: functions of the torus coordinate. **This is the same centre obstruction as in R7-a §4 and R7-f §3, now in spectral form.**

### 3.2 Order-1 chains via the 1-jet lift (suggestion (b) of the planner)

- An order-1 functional is a measure pair (m_0, m_1) on M ⊔ SM, by Hahn–Banach and Riesz.
- The set of representing pairs of norm <= r is weak*-compact and convex.
- The lifted transport e^{-ct} Gamma-hat_t maps representations of B to representations of B. But it multiplies norms by up to e^{-Re c t} G-hat_1(t), which is unbounded for Re c inside the band (Lemma 1.1 of R9-b).
- So Markov–Kakutani / Følner averaging yields an *equivariant* representation only at the band edges (Re c >= gamma_1^+ or <= -gamma_1^-), where Prop 7.3 / Lemma 1 already exclude chains.

**Conclusion (proved in the sense of this mechanism):** no equivariant representation can be obtained by averaging inside the band. Choosing c anywhere inside the strip does not change this, since the strips of Theorem R lie inside the band (Cor 1.2(b) of R9-b). **Dead end.**

### 3.3 Products of eigen-distributions (wavefront calculus)

- Suppose u, v are generalized functions with Xu = -cu, Xv = cv, and WF(u) ∩ (-WF(v)) = ∅. Then the product uv is defined and X(uv) = 0, so uv = K is constant by (K0).
- With a chain (u, alpha) at c: X(alpha v) = -uv = -K, so K = 0 by (K1).
- So under GH, **every** such WF-admissible product of an eigen-distribution at c with one at -c vanishes, and alpha v is constant.
- With a chain at -c as well, the same computation gives only further vanishing relations.

There is no contradiction without a non-degeneracy input "uv != 0". For the Theorem-R families, u and v are carried by the orbit closures of different pairs (unstable pair for c, stable pair for -c, available exactly when lambda = 0 and 0 < c < min(theta, theta')). I could neither verify the WF condition nor get uv != 0. **Recorded as a mechanism that makes GH act at 0 starting from c and -c, but stops at non-degeneracy.** It is new relative to the ledger, as far as I can tell; it is the diagonal restriction of the (X, X) tensor of R9-d, which is legitimate exactly under the WF condition.

### 3.4 The statement (SO)

(SO): under GH, for every x and every real kappa != 0, ∫_R e^{J_t(x) - kappa t} dt = inf.

If the integral is finite with kappa > 0, the backward weak* limit measures m of x have m(d) >= kappa and the forward ones have m(d) <= kappa. This follows from the Lipschitz property of t -> J_t(x) - kappa t, which forces it to -inf at both ends.

To use GH at 0 one needs forward cancellation at a rate > kappa, i.e. forward-asymptotic partners or exact self-similarity as in Lemma K. Neither is available at a general point. Lemma K's backward jet cancellation only produces strips not containing 0, of right edge < gamma_K^+ (the band grows quadratically in K, the cancellation rate only linearly). So (SO) is the single-orbit case of (JC) and is equally open.

---

## 4. Summary: proved, not proved, open

**Proved here (new, modest):**
- §1: independent full check of Theorem A (step 3), and of the match with Theorem R' and with the definitions in (JC). Correct.
- §2.1: chains under time change (equivalent weighted form). The ratio lambda/chi is time-change invariant, so time changes cannot move strips.
- §2.2: barrier remark. Semi-Fredholm perturbation from 0 to c needs a loss-free estimate, which GH does not supply. This is a diagnosis, not a theorem.
- §2.3: conjugation symmetry of the chain-carrying set.
- §2.4 and §3.3: Leibniz/WF consequences. Under GH, every WF-admissible product of eigen-distributions at c and -c vanishes.
- §3.1 (spectral part): density of smooth functions whose Pinsker-complement spectral measure has 0 in its support, and the resulting almost-invariant sequences in the volume case.

**Not proved (open):**
1. **(JC)** itself, and the stronger (NJ). Hence the [GOAL] in dimensions >= 4.
2. (SO), the order-0 single-orbit sub-case.
3. Non-degeneracy for the product mechanism of §3.3: for lambda = 0, find an unstable-pair eigen-distribution at c and a stable-pair one at -c with WF-admissible, nonzero product.
4. The centre-direction step of §3.1 in the volume case: show that almost-invariant L^2 sequences that are almost constant on Pesin s/u plaques cannot have norm bounded below, under GH.
5. (V), quantitative tameness, and (J1-0), as listed in R9-b §5.

=== END OF ANSWER round10_q2 ===
