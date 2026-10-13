# round14_q9 answer

## Plan / statement attempted
Target: local E1 under GH. I do not prove it. What I do prove is an exact reformulation of it in Case B (every invariant
probability mu has mu(d) = 0), and this includes the volume-preserving case. In Case B, local E1 is equivalent to a purely
dynamical statement, lambda*(X) = 0, i.e. uniformly subexponential growth of ||Dg_t||. GH plays no part in the
equivalence. So the local-E1 route is at least as hard as proving "GH => uniform subexponential derivative growth", and
that statement is strictly stronger than the volume case of the problem. I also check that local E1 (indeed full E1) holds
in every known GH example. Finally I record the dead ends for ideas (a)-(c).

Conventions are those of the brief: nu, d = div_nu X, J_t, P phi = X phi + d phi. A distribution density T gives
u = T/nu, and T(P phi) = kappa T(phi) for all phi iff Xu = -kappa u. Also
lambda*(X) := lim_n (1/n) max_x log ||Dg_n(x)||. The limit exists by subadditivity, and lambda* >= 0.

## 1. The transfer group (elementary, proved)
For smooth phi put L_t phi := e^{J_t} (phi o g_t). By the cocycle identity J_{t+s}(x) = J_s(x) + J_t(g_s x) we have
L_{t+s} = L_s L_t, so (L_t) is a group. As in Theorem J step 1, t -> L_t phi is C^1 into C^inf(M), and
d/dt L_t phi = L_t(P phi). Differentiating L_{s} L_t phi at s = 0 also gives d/dt L_t phi = P L_t phi, so P L_t = L_t P.

**Lemma 1.1.** If T is a distribution density with T(P psi) = kappa T(psi) for all smooth psi, then
T(L_t phi) = e^{kappa t} T(phi) for all real t and all smooth phi.
*Proof.* Put F(t) = T(L_t phi). By continuity and linearity of T, F'(t) = T(P L_t phi) = kappa F(t). Hence F(t) = e^{kappa t} F(0). QED

## 2. Subexponential growth excludes eigen-distributions of order <= 1 (proved, no GH)
Put beta := lim_{t->+inf} (1/t) max_x J_t(x). The limit exists by subadditivity. It equals max_mu mu(d) over invariant
probabilities (fact 1 of Prop 2.1), and it is >= 0.

**Proposition 2.1.** Let kappa > beta + lambda*(X). Then no nonzero distribution density T of order <= 1 satisfies
T(P phi) = kappa T(phi) for all phi.

*Proof.* Fix delta > 0. For large |t| we have ||Dg_s(x)|| <= C_delta e^{(lambda*+delta) s} for 0 <= s <= t, and
J_t <= C_delta + (beta+delta) t. Also d(J_t) = int_0^t d(d o g_s) ds, so
|dJ_t| <= ||dd||_inf int_0^t ||Dg_s|| ds <= C'_delta e^{(lambda*+delta)t}. Then

||L_t phi||_{C^1} <= e^{max J_t} ( ||phi||_inf (1 + ||dJ_t||_inf) + ||dphi||_inf ||Dg_t||_inf )
                  <= C''_delta e^{(beta+lambda*+2delta) t} ||phi||_{C^1}.

Since T has order <= 1, Lemma 1.1 gives e^{kappa t}|T(phi)| = |T(L_t phi)| <= C ||L_t phi||_{C^1}. Choose delta with
kappa > beta + lambda* + 2 delta and let t -> +inf. This gives T(phi) = 0. QED

**Corollary 2.2.** If beta = 0 and lambda*(X) = 0, then X + kappa is injective on distributions of order <= 1 for every
real kappa > 0. The same argument with t -> -inf, i.e. for -X, gives the case kappa < 0 when the backward quantities
vanish.

## 3. The equivalence in Case B (proved, modulo Theorem B of the brief, which needs no GH)
Case B: every invariant probability mu has mu(d) = 0. Then beta = 0 by fact 1 of Prop 2.1 (and in fact J_t = o(|t|)
uniformly, by Lemma 3 of R5-a).

**Theorem 3.1.** Assume Case B; GH is not needed. The following are equivalent:
 (i) local E1: for every eps > 0, uncountably many kappa in (0, eps) admit no nonzero u of order <= 1 with Xu = -kappa u;
 (ii) for every kappa > 0 there is no nonzero u of order <= 1 with Xu = -kappa u;
 (iii) lambda*(X) = 0;
 (iv) lambda*(-X) = 0.

*Proof.*
- (iii) => (ii) is Corollary 2.2, using beta = 0.
- (ii) => (i) is trivial.
- (i) => (iii): suppose lambda*(X) > 0. Theorem B of R5-a (no GH needed; it uses Lemma 1, the cited Pesin-Ruelle theorem
  (R) and Lemma 3) gives theta > 0 and, for every kappa in (0, theta) outside a discrete subset of (0, theta), a nonzero
  T_kappa of order <= 1 with Xu_kappa = -kappa u_kappa. A discrete subset of (0, theta) is countable. So for eps < theta,
  all but countably many kappa in (0, eps) carry a nonzero eigen-distribution. This contradicts (i).
- (iii) <=> (iv): suppose lambda*(X) > 0. By Lemma 1 of R5-a there is an invariant m with int chi dm > 0, so some ergodic
  component mu has a positive top Lyapunov exponent for g_1. The sum of its exponents is mu(d) = 0 (the nu-Jacobian of g_1
  is e^{J_1}, and Birkhoff applies). So mu also has a negative exponent, and at mu-generic x, ||Dg_{-n}(x)|| grows
  exponentially. Hence lambda*(-X) > 0. The converse is symmetric. QED

**Consequences.**
1. In the volume-preserving case, take nu = omega, so d = 0 and Case B holds. There, local E1 under GH is literally the
   statement "GH + smooth invariant volume => ||Dg_t|| = e^{o(|t|)} uniformly". By Ruelle's inequality that statement
   gives zero entropy for every invariant measure at once. It is strictly stronger than the volume case of the problem,
   since zero entropy does not by itself give lambda* = 0. So local E1 contains, as a special case, a statement at
   least as hard as the core open case #16 / (PE0) in the volume setting. It does not circumvent the dynamical core.
2. GH must be used to prove local E1. For example, the geodesic flow of a negatively curved surface on its unit tangent
   bundle preserves volume and has lambda* > 0, so by Theorem 3.1 local E1 fails for it; consistently, it is not GH.
3. This settles the alternative the task offered. Eigen-distributions do fill an interval minus a discrete set
   (Theorem B) exactly when lambda* > 0 in Case B. Whether GH excludes this is exactly the question whether GH forces
   lambda* = 0. That question is open here.

## 4. Case A (some invariant mu has mu(d) != 0): partial remarks
- If some ergodic mu has kappa := mu(d) > 0, then [R4-q7] Prop 2.2 gives an order-0 eigen-distribution with Xu = -kappa u.
  So local E1 implies that the set {mu(d) : mu ergodic} ∩ (0, eps) misses uncountably many points of (0, eps) for every
  eps. This is automatic if that set is countable.
- Proposition 2.1 still applies: there are no order-<=1 eigen-distributions with kappa > beta + lambda*. So any failure
  of local E1 must live at kappa <= beta + lambda*.
- I have no equivalence in Case A. Theorem B needs J_t = o(|t|) along the pair, and that is not available in general.

## 5. Known GH examples satisfy full E1 (proved)
Let X be a Diophantine linear field alpha on T^n, and X' = hX with h > 0 smooth. Write 1/h = c + Xb with
c = int 1/h > 0 and b smooth. This is possible because, for Diophantine alpha, every smooth function of mean zero is
X of a smooth function (Fourier series). Suppose X'u = -kappa u with kappa real and nonzero, and u in D'. Then
Xu = -(kappa/h) u. Put w = e^{kappa b} u. Then
Xw = kappa (Xb) w - kappa (c + Xb) w = -kappa c w.
In Fourier coefficients, (i<k, alpha> + kappa c) w_k = 0 for every k. The factor is never 0, so w = 0 and u = 0.
Hence every currently known GH example (smooth time changes of Diophantine linear flows, which by the
Greenfield-Wallach/Katok conjecture should be all of them up to smooth conjugacy) satisfies E1 for all real kappa != 0
and all orders. So no counterexample to local E1 under GH can come from known examples. Such a counterexample would
disprove the Katok conjecture.

## 6. Dead ends for the suggested ideas
(a) Jordan chains. Excluding an order-1 Jordan chain at a single kappa means showing ker(X+kappa) = 0 or
ker (X+kappa)^2 = ker(X+kappa). The argument of Theorem J at z = 0 used two facts: L1 (the kernel of X) and the maximum
principle "Xw = const => const = 0". Neither has an analogue for X + kappa, since X + kappa is not known to be GH. By
Section 3, in Case B any successful argument would prove lambda* = 0, so it must contain genuinely dynamical input.
(b) Tame estimate. T(R phi) = T(phi)/kappa gives |T(phi)| <= |T| (C kappa)^j ||phi||_{C^{1+j l}}, where l is the loss of
derivatives. This tends to 0 only when the C^{1+jl} norms grow at most geometrically. Real-analytic phi have factorial
growth, and R does not preserve spectral bands, so the iteration fails. Uncountably many kappa give no extra
structure: the u_kappa need not form a family. (In the setting of Theorem B they do form a holomorphic family, and that
is Theorem 3.1 again.)
(c) Microlocal criterion. The criterion needs a classical Q, elliptic on WF(u), with [X,Q] - cQ smoothing near WF(u). At
the principal level this asks for a continuous nonvanishing q on the compact set S(WF(u)) in the sphere bundle with
|Phi_t xi|^m q(hat Phi_t xi) = e^{ct} q(xi). This requires the cocycle m log|Phi_t xi| to be cohomologous to the constant
ct on WF(u). That holds only in rigid, uniformly conformal situations, and the full-symbol requirement is stronger
still. So it does not apply in general.

## Summary
Proved:
- Lemma 1.1 and Proposition 2.1 (no GH needed): there is no order-<=1 eigen-distribution with Xu = -kappa u when
  kappa > beta + lambda*.
- Theorem 3.1: in Case B, which includes the volume case, local E1 <=> (for all kappa > 0, X + kappa is injective on
  order <= 1) <=> lambda*(X) = 0 <=> lambda*(-X) = 0. GH is not needed for the equivalence. The step (i) => (iii) uses
  Theorem B of the brief, which relies on the cited Pesin-Ruelle theorem.
- Section 5: full E1 holds for smooth time changes of Diophantine linear flows.

Open:
- Local E1 under GH is not proved.
- In Case B it is equivalent to "GH => lambda* = 0", i.e. uniform subexponential derivative growth. This is open and
  stronger than the volume case of the problem.
- Case A (some mu(d) != 0) is not reduced.
- Consequently, the route "local E1 => (PE0)" does not bypass the dynamical core. In the volume case it requires proving
  more than (PE0).

=== END OF ANSWER round14_q9 ===
