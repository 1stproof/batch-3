# round7_q2: answer

## Plan
Target: (PE-NH). The hard case is mu(d) = 0 (PE0). Plan: (1) re-check the chain; (2) look for new mechanisms at lambda = 0 (directional weights through currents, decay weaker than exponential, single-orbit Patterson behaviour); (3) write down rigorously whatever new lemmas come out, and say exactly where the argument stops.

Outcome, stated up front: **I could not prove (PE-NH) and found no counterexample.** What follows is a set of rigorous auxiliary results, plus proofs that three further routes are dead ends.

## 0. The chain
Steps 2 and 4 look correct to me, granted the cited theorems: Ruelle's inequality, Katok/Lian–Young for flows, the stable manifold theorem, Jacobs' formula, and the variational principle. One remark on step 2: [KLY] needs mu(Zero X) = 0. This holds because mu(Zero X) is 0 or 1 by ergodicity, and if it were 1 then g_1 = id on supp mu, which forces h_mu = 0. With that, the chain reduces the problem exactly to (PE-NH). All the difficulty is in step 1.

## 1. Theorem J under quasi-analytic decay (proved)
**Theorem J_w.** Assume GH. Let S be a distribution density and F_phi(t) = S(e^{J_t} phi o g_t). Suppose |F_phi(t)| <= C ||phi||_{C^k} e^{-w(|t|)} for all t and all phi, where w >= 0 is continuous and nondecreasing, w(t)/log t -> infinity, and the moment sequence M_j := int |t|^j e^{-w(|t|)} dt satisfies sum_j M_j^{-1/j} = infinity (for example w(t) = t/log(e+t)). Then S = 0.

*Proof.* Steps 1–4 of Theorem J use only that t^j F_phi(t) and t^j F_{P phi}(t) are integrable and tend to 0 at both infinities. Both hold here, since w(t)/log t -> infinity. So all moments m_j(phi) = int t^j F_phi dt vanish. Fix phi and let G(xi) = int e^{-i xi t} F_phi(t) dt. Then G is C^infinity, |G^{(j)}(xi)| <= C' M_j for all real xi, and G^{(j)}(0) = (-i)^j m_j(phi) = 0 for all j. M_j is log-convex (Hölder), and sum M_j^{-1/j} = infinity. By the Denjoy–Carleman theorem (cited from memory: the class C{M_j} on R is quasi-analytic iff sum M_j^{-1/j} = infinity for log-convex M_j), G = 0 on R. By Fourier uniqueness in L^1 and continuity, F_phi = 0, so S(phi) = F_phi(0) = 0. ∎

This is the precise form of planner suggestion (iii). It does not by itself reach lambda = 0. At mu-generic points J_t = o(|t|) with no rate, so no single point or leaf cluster gives such decay in the forward direction (see §3).

## 2. Theorem J with mean-zero test functions; closed 1-currents give nothing new (proved)
**Lemma 2.1.** Assume GH. Let S be a distribution density such that the bound (*) of Theorem J holds only for phi with int phi dnu = 0. Then S vanishes on such phi.
*Proof.* Note int P phi dnu = int L_X(phi nu) = 0 for every phi, so P maps C^infinity into C^infinity_0(nu). The moments m_j are defined on C^infinity_0(nu). For phi in C^infinity_0(nu) we have m_0(P phi) = 0 and m_j(P phi) = -j m_{j-1}(phi). For any phi, P phi is mean-zero and m_j(P phi) is defined.

Extend each m_j by mt_j(phi) := m_j(phi - nu-hat(phi)).
- For every phi: mt_j(P phi) = m_j(P(phi - nu-hat(phi))) + nu-hat(phi) m_j(d). Here P 1 = d, and d is mean-zero.
- j = 0: m_0(P psi) = 0 for all psi. So mt_0(P phi) = 0, hence mt_0 = c nu by F1, and m_0 = mt_0 restricted to mean-zero phi, which is 0.
- Induction: if m_{j-1} = 0, then m_j(P psi) = 0 for mean-zero psi. So mt_j(P phi) = nu-hat(phi) m_j(d) = (m_j(d)/nu(M)) int phi dnu. F2 gives m_j(d) = 0, then mt_j = c nu by F1, hence m_j = 0.

The Fourier step is then the same as in Theorem J. ∎

**Corollary 2.2 (dead end: directional weights).** One might hope to replace the Jacobian weight e^{J_t} (the sum of the exponents) by a single exponent, by transporting closed 1-currents. GH does extend to closed 1-currents (Lemma B), and the Jordan-chain argument does run for them. But it gives nothing beyond Lemma 2.1.
*Proof.* Let C be a closed 1-current with |<(g_t)_* C, gamma>| <= C' e^{-eps|t|} ||gamma||_{C^k} for all t and all (n-1)-forms gamma. If gamma is closed, then <(g_t)_* C, gamma> = <[C],[gamma]> does not depend on t, because g_t is isotopic to the identity. Decay therefore forces [C] = 0, so C = dU with U a 0-current (de Rham for currents). Then <(g_t)_* dU, gamma> = ±<U o g_{-t}, d gamma>. Every mean-zero smooth density phi nu has the form d gamma, and gamma can be chosen with ||gamma||_{C^k} <= C'' ||phi||_{C^{k'}} (Hodge theory). So the hypothesis is exactly Lemma 2.1's hypothesis for S = U nu. ∎
Consequence: closed 1-currents carry no directional weight. Weights of the form |Dg_t v| come only from non-closed currents, and GH says nothing about those. So "use a single stable exponent in place of the sum" does not work with the tools at hand.

## 3. Single orbits at lambda = 0: forced Patterson divergence (proved modulo Atkinson's theorem)
**Lemma 3.1.** Let mu be ergodic with mu(d) = 0 and not carried by Zero(X). For mu-a.e. x, int_0^infinity e^{J_t(x)} dt = infinity and int_{-infinity}^0 e^{J_t(x)} dt = infinity. (No GH needed.)
*Proof.* Apply Atkinson's recurrence theorem (cited from memory: for an ergodic measure-preserving map T and an integrable f with zero mean, for a.e. x and every eps > 0, |sum_{i<n} f(T^i x)| < eps for infinitely many n) to T = g_1 and f = J_1, which has mean mu(d) = 0. g_1 need not be ergodic, but the theorem holds for non-ergodic T as long as f has zero conditional mean on the ergodic components of T. That holds here: the ergodic components of g_1 are g_s-images of each other, and J_1 o g_s - J_1 = J_s o g_1 - J_s is a g_1-coboundary of a bounded function. So |J_n(x)| < 1 for infinitely many integers n, and |J_t(x)| <= 1 + ||d||_inf for t in [n, n+1]. This gives infinitely many disjoint unit intervals on which e^{J_t(x)} >= e^{-1-||d||}. The backward statement is the same with g_{-1}. ∎
Consequence: when lambda = 0, any combination of point masses needs genuine cancellation in both time directions. Weights alone never give integrability. This confirms the obstruction recorded in R6-d and R6-e.

## 4. Where the argument stops
I could not construct, for a non-hyperbolic ergodic mu with h_mu > 0 and mu(d) = 0, a nonzero distribution density S whose transport decays in both time directions, even in the weak sense of Theorem J_w. Without such an S I also found no other way to contradict GH. The case mu(d) = 0 of (PE-NH), i.e. (PE0), therefore remains **open**. Specifically, the following are still unproved:
- (O-a) the GH-free Conjecture (C) at lambda = 0. Two-sided cancellation needs su-cycles, and for non-hyperbolic mu, W^s and W^u of nearby points generically do not meet. Smearing along center/flow transversals does not help: a fixed center displacement between transported densities does not shrink, because the center exponent is 0.
- (O-b) a resonance-type continuation of one-orbit Laplace transforms across Re z = 0, which Lemma M would need.
- (O-c) the case mu(d) != 0 with neither a 1-dimensional unstable nor a 1-dimensional stable direction, outside the band of Prop. 6.1. This is reducible to Prop. 6.2's argument modulo non-stationary sub-resonance normal forms along Pesin unstable manifolds; I have not checked that citation.

**Proved overall (with the earlier rounds):** zero entropy when dim M <= 3; exclusion of hyperbolic positive-entropy measures; the band of Prop. 6.1; and, new here, Theorem J_w, Lemma 2.1 / Corollary 2.2 and Lemma 3.1. **Open:** (PE0), hence the problem for dim M >= 4.

=== END OF ANSWER round7_q2 ===

