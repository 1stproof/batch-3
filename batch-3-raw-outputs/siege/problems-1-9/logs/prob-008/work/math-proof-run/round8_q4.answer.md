# round8_q4 answer

## 0. Outcome

I did **not** prove (PE-NH), and I did not find a counterexample. The problem's claim is therefore still established only for dim M <= 3 and for hyperbolic positive-entropy measures; the core case (PE0) remains open.

This file records:
- (§1) a re-check of the chain, in which I found no flaw;
- (§2) two small new lemmas, both proved:
  - Lemma 2.1 (GH-free): divergence of the one-sided weighted orbit integrals when mu(d) >= 0, with an exact identity when they converge;
  - Lemma 2.2 (GH): a one-sided Patterson lemma;
- (§2) their consequence, Corollary 2.3, which says precisely what the strip transforms T_z of (PE0) look like as z -> 0+ and why they give no contradiction;
- (§3) an analysis of the planner's (J1): it is an "absence of continuous spectrum" statement that (K0) and (K1) cannot give;
- (§4) the volume case restated as "cohomology-free implies zero entropy", with a literature pointer cited from uncertain memory;
- (§5) the open questions.

Notation is as in the brief: nu, d = div_nu X, J_t, P phi = X phi + d phi, F_phi(t) = S(e^{J_t} phi o g_t), and nu-hat = nu/nu(M).

## 1. Check of the chain

- **Step 2 (entry 60 / Theorem 5.1).** I re-read the proof in R6-a §§3-5 and agree with it.
  - Lemma K is correct: Cayley-Hamilton on the jets at p, then backward decay at rate K log(1/kappa) - max(0, -I).
  - Corollary 4.2 combines Lemma K/K' with P1 and Observation P.
  - The appeal to [KLY] needs mu(Zero X) = 0 and h_mu > 0. Both hold: if mu(Zero X) > 0 then, by ergodicity, mu is a point mass at a zero and its entropy is 0.
- **Step 4.** The reduction to flow-ergodic measures through mu-bar and Jacobs' formula is standard and correct.
- **Step 3.** Steps 1 and 2 give step 3 trivially.

So the chain is sound. Its only gap is step 1 (PE-NH).

A remark on the case lambda != 0 (sub-case R1). This case is closed under one condition. Suppose one grants tempered C^K non-stationary normal forms along Pesin unstable manifolds of a non-uniform contraction. I recall this as Kalinin-Sadovskaya, "Normal forms for non-uniform contractions", J. Mod. Dyn. 2017; I am citing from memory and have **not** checked the hypotheses, in particular the C^r regularity and tempered-bound statements. Granting it, the vanishing-moment argument of R6-a Prop. 6.2, step 4, goes through with polynomials of degree < rK in place of affine parameters. Then every lambda != 0 is excluded. I add nothing here beyond flagging the citation. The case lambda = 0 (PE0) is untouched by it.

## 2. New small results (proved)

**Lemma 2.1 (no GH needed).** Let mu be ergodic and flow-invariant. Put A^+(x) := int_0^inf e^{J_t(x)} dt, which lies in (0, inf].
(i) Either A^+ < inf mu-a.e., or A^+ = inf mu-a.e.
(ii) If A^+ < inf a.e., then mu(1/A^+) = -mu(d). In particular mu(d) < 0.
Hence, if mu(d) >= 0, then int_0^inf e^{J_t(x)} dt = inf for mu-a.e. x. Symmetrically, if mu(d) <= 0, then int_{-inf}^0 e^{J_t(x)} dt = inf for mu-a.e. x. So in case (PE0) both one-sided integrals diverge at mu-a.e. point.

*Proof.*
1. *Cocycle identity.* Since J_t(g_s x) = J_{t+s}(x) - J_s(x), we have
 A^+(g_s x) = e^{-J_s(x)} int_s^inf e^{J_t(x)} dt.
 So {A^+ < inf} is invariant, and (i) follows from ergodicity.
2. *A lower bound.* A^+ >= int_0^1 e^{J_t} dt >= e^{-||d||_inf}. So 0 < 1/A^+ <= e^{||d||_inf}, and 1/A^+ is bounded and measurable.
3. *The derivative of a = log A^+ along orbits.* Assume A^+ < inf a.e. On {A^+ < inf}, step 1 gives
 a(g_s x) = -J_s(x) + log( A^+(x) - int_0^s e^{J_t(x)} dt ).
 This is C^1 in s, and differentiating gives
 d/ds a(g_s x) = -d(g_s x) - e^{J_s(x)} / (e^{J_s(x)} A^+(g_s x)) = -(d + 1/A^+)(g_s x).
4. *Integrated form.* Hence a(g_s x) - a(x) = -int_0^s (d + 1/A^+)(g_r x) dr.
5. *Birkhoff.* Divide by s. By Birkhoff's theorem the right side tends to -(mu(d) + mu(1/A^+)) for a.e. x.
6. *Recurrence.* Choose K with mu{|a| <= K} > 0. By Poincaré recurrence for g_1, a.e. x in {|a| <= K} has g_n x in {|a| <= K} for infinitely many integers n. Along those times the left side, divided by s, tends to 0.
7. Hence mu(d) + mu(1/A^+) = 0. Since 1/A^+ > 0, this gives mu(d) < 0.
8. *Time reversal.* For the backward statement apply the result to -X. Its log-Jacobian is J_{-t}, its divergence is -d, and mu(-d) >= 0 when mu(d) <= 0. ∎

**Lemma 2.2 (one-sided Patterson lemma; GH).** Let x satisfy J_t(x) = o(t) as t -> +inf and int_0^inf e^{J_t(x)} dt = inf. For s > 0 put
 N(s) := int_0^inf e^{J_t(x) - st} dt,
 T_s^+(phi) := N(s)^{-1} int_0^inf e^{J_t(x) - st} phi(g_t x) dt.
Then T_s^+ -> nu-hat weak* as s -> 0+. The same holds backward.

*Proof.*
1. *Finiteness and divergence.* N(s) < inf because J_t = o(t). By monotone convergence, N(s) -> inf as s -> 0+.
2. *An identity.* d/dt [e^{J_t(x) - st} phi(g_t x)] = e^{J_t(x) - st} (P phi - s phi)(g_t x). Integrate over [0, R] and let R -> inf; the boundary term at R tends to 0 because J_t = o(t). This gives
 T_s^+(P phi) = s T_s^+(phi) - phi(x)/N(s).
3. *The limit.* Every weak* limit point T of T_s^+ as s -> 0+ is a probability measure with T(P phi) = 0 for all phi.
4. By (F1) (that is, GH through L1), T = nu-hat. Compactness then gives convergence of the whole family. ∎

**Corollary 2.3 (what the strip transforms of (PE0) look like at z = 0).**
Setting: mu is ergodic with mu(d) = 0 and h_mu > 0. Points x and y are mu-generic and backward exponentially asymptotic at rate theta (as in Prop. 6.1). Put S = delta_x - e^b delta_y, so that T_z = B_z + Phi_z on 0 < Re z < theta.

Facts:
- B_z is holomorphic on Re z < theta, hence across z = 0.
- For real s -> 0+, we have Phi_s = N_x(s)(nu-hat + o(1)) - e^b N_y(s)(nu-hat + o(1)) weak*, and N_x(s), N_y(s) -> inf.

*Proof.* Apply Lemmas 2.1 and 2.2 to x and to y; the hypothesis J_t = o(t) holds by genericity. ∎

Consequences:
- For every phi with nu(phi) = 0, |T_s(phi)| = o(N_x(s) + N_y(s)).
- T_s(phi) / (N_x(s) + N_y(s)) converges to a multiple of nu(phi) along subsequences.

These are exactly the asymptotics that F1 and F2 permit. So no contradiction can come from the leading term at z = 0. This makes rigorous the "Patterson behaviour" remark of R6-d (R2): the singularity of T_z at 0 is of divergent-normalisation type, and it is aligned with nu.

## 3. On the planner's statement (J1)

(J1) says: under GH there is no nonzero S with
- |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for t <= 0, and
- |F_phi(t)| <= C e^{a t} ||phi||_{C^k} for t >= 0,
for some 0 <= a < eps.

*Finite-dimensional model.* Replace the transport by e^{tA} on C^N and S by a covector.
- Backward decay at rate eps forces S into the sum of generalised eigenspaces with Re(eigenvalue) >= eps.
- Forward growth <= e^{at} forces S into those with Re <= a.
- So S = 0 automatically, with no use of (K0) or (K1).

In infinite dimensions the analogue fails as soon as there is continuous spectrum. The shift on L^2(R) has functionals with one-sided (indeed two-sided) decay. So (J1) is precisely a statement that, near the imaginary axis, the transport has no "continuous spectrum" seen by finite-order distributions.

*What (K0) and (K1) can and cannot see.* (K0) and (K1) constrain the transposed operator only at the single spectral point z = 0. They enter Theorem J through the moments int t^j F_phi(t) dt, and these moments are not defined under one-sided decay. The backward moments m_j^- = int_{-inf}^0 t^j F_phi dt do exist. They satisfy
- m_0^-(P phi) = S(phi), and
- m_j^-(P phi) = -j m_{j-1}^-(phi) for j >= 1.
This is a Jordan chain that starts at S instead of 0, so F1 and F2 never apply. Hence any proof of (J1) must use GH away from z = 0, or the closed-range half of GH, and I found no way to do either. This agrees with R7-b.

## 4. The volume-preserving case: an exact reformulation and a literature pointer

**Lemma 4.1 (proved, elementary).** Let X preserve a smooth positive density omega. Then
 GH <=> (CF): every smooth f equals omega-hat(f) + Xu with u smooth.
Moreover, in this case h_top(g_1) = h_omega(g_1).

*Proof.*
- *GH => CF.* This is (O2) together with the duality consequence of Text A: the invariant distribution densities are the multiples c·omega, and X(C^inf) is their annihilator.
- *CF => GH.*
  - Let u be in D' with Xu = f smooth. Pairing with omega gives omega(f) = 0.
  - CF then gives f = Xv with v smooth, so X(u - v) = 0.
  - Under CF, the annihilator of X(C^inf) = {omega-hat(f) = 0} is one-dimensional. So the invariant distribution densities are the multiples of omega.
  - Since d = 0, (u - v)omega is invariant; hence u - v is constant and u is smooth.
- *Entropy.* GH gives unique ergodicity (O2), and the variational principle gives h_top = h_omega. ∎

So the volume case of the problem is exactly the statement "a cohomology-free C^inf flow has zero (metric = topological) entropy".

*Literature pointer (uncertain, from memory).* I recall a paper of Flaminio and Paternain, "Linearization of cohomology-free vector fields" (Discrete Contin. Dyn. Syst., about 2011), whose abstract says that a cohomology-free vector field "can be embedded continuously in a linear flow on an Abelian group". If that statement is correct as recalled, it would settle the volume case:
- a continuous injective equivariant map into a translation flow (which is isometric for an invariant metric), from a compact space, makes {g_t} equicontinuous;
- equicontinuity forces h_top = 0.

I could not reconstruct their proof, and I am not certain of the exact statement. The general (non-volume) case would in any event still need "GH implies a smooth invariant volume" (the open statement (V)), or a separate argument for non-volume GH fields. I therefore list this only as a pointer, not as a result.

## 5. Status

**Proved here (new):**
- Lemma 2.1 (GH-free): in (PE0) both one-sided weighted orbit integrals diverge; when A^+ < inf, mu(1/A^+) = -mu(d).
- Lemma 2.2: the one-sided Patterson lemma.
- Corollary 2.3: the leading asymptotics of the strip transforms at z = 0+ are multiples of nu-hat, consistent with GH.
- Lemma 4.1: in the volume case, GH <=> CF and h_top = h_omega.

**Proved earlier (re-checked here):**
- under GH, every positive-entropy ergodic measure is non-hyperbolic (modulo [Ru], [KLY]);
- zero topological entropy for dim M <= 3;
- the band restrictions on mu(d) (Prop. 6.1, Prop. N).

**Conditional:**
- lambda != 0 (sub-case R1) is closed, given the unchecked citation of non-uniform normal forms (§1).
- The volume case is closed, given the uncertain Flaminio–Paternain citation (§4).

**Open (named explicitly):**
1. (PE0): under GH, no ergodic non-hyperbolic mu with h_mu(g_1) > 0 and mu(d) = 0. This is the core, and hence the problem in dimension >= 4.
2. (J1), equivalently a resonance-type continuation of the forward pair transforms across Re z = 0; both are stronger than (PE0).
3. (V): GH implies a smooth invariant volume.
4. CF implies zero entropy (in the volume case, equivalent to the problem), unless the Flaminio–Paternain result is as recalled.

=== END OF ANSWER round8_q4 ===
