# Answer to round10_q6: the tilted Lemma C (SO)

## Plan (written first, updated as I go)
Target: (SO) — under GH, for every x in M and every real kappa != 0, int_R e^{J_t(x) - kappa t} dt = +infinity.
Steps:
1. Reduce it to the eigen-distribution form: if the integral is finite, u = m/nu is a nonnegative measure-distribution with Xu = -kappa u.
2. Check what the exponential-margin case is equivalent to (Jordan chains).
3. Look for special cases (asymptotics to hyperbolic periodic orbits or zeros) that can be settled with the known lemmas.
4. Look for a general mechanism; if none is found, state precisely where the argument stops.

## Summary of outcome
I do not prove (SO) in general, and I have no counterexample. What I prove:
- (Lemma 1) An elementary pointwise bound: if I(x,kappa) := int_R e^{J_t(x)-kappa t} dt < inf, then J_t(x) <= C + kappa t for ALL real t. In particular, for kappa > 0 the orbit has volume decay at linear rate backward (J_t <= C - kappa|t|, t <= 0), and for kappa < 0 it has it forward (J_t <= C - |kappa| t, t >= 0).
- (Theorem 2, the main partial result) Under GH, (SO) holds at (x, kappa) whenever kappa > 0 and x is forward-exponentially asymptotic to a point p with g_P p = p (a zero of X or a periodic point, hyperbolic or not), and whenever kappa < 0 and x is backward-exponentially asymptotic to such a p. It also holds when x is itself periodic or a zero. The proof combines Lemma 1 with Lemma K / Lemma K' (block R6-a §3).
- (Corollary 3) Under GH, (SO) holds for every x whose omega-limit (when kappa > 0) or alpha-limit (when kappa < 0) is a hyperbolic periodic orbit or a hyperbolic zero. In particular it holds for every orbit connecting two hyperbolic periodic orbits or zeros, for every kappa != 0.
- (Proposition 4) The "exponential margins" case of (SO) is EQUIVALENT in difficulty to order-0 Jordan chains. An orbit that violates (SO) with margins a < b produces a holomorphic eigen-family together with an order-0 Jordan chain at every real c in (a,b). With Lemma 1.1 of R9-c, this gives: (SO) at the real point kappa holds for all x (with margins) iff there is no order-0 chain at Re c = kappa (made precise below). So no margin-restricted shortcut exists: the margin case IS the order-0 half of (NJ).
- §5 is a precise account of where the general argument stops, and why (K0) and (K1) alone do not visibly suffice.

## 1. Elementary facts

Notation as in the brief: c_x(t) := e^{J_t(x) - kappa t}, I(x,kappa) := int_R c_x(t) dt.

**Lemma 1.** Let kappa be real and I(x,kappa) < inf. Then c_x(t) -> 0 as |t| -> inf, and with C := log sup_t c_x(t) < inf we have J_t(x) <= C + kappa t for all t in R.
*Proof.* c_x' (t) = (d(g_t x) - kappa) c_x(t), so |(log c_x)'| <= L := ||d||_inf + |kappa|, hence c_x(t) >= c_x(s) e^{-L|t-s|}. If c_x(s) >= eps for some s, then c_x >= eps e^{-L} on [s-1, s+1]. Infinitely many such s with pairwise distance >= 2 would contradict integrability. So c_x -> 0 at +-inf. c_x is continuous, so it is bounded on R; take C = log sup c_x. Then J_t(x) - kappa t <= C. ∎

**Lemma 1' (trivial orbits).** If x is a zero of X or periodic, then I(x,kappa) = inf for every real kappa (no GH needed).
*Proof.* At a zero, J_t(x) = t d(x), and int_R e^{(d(x)-kappa)t} dt = inf. If x has period P, then J_{t+P}(x) = J_t(x) + I with I = J_P(x), so c_x(t+P) = e^{I - kappa P} c_x(t). Hence int over [nP,(n+1)P] equals q^n int_0^P c_x, with q = e^{I-kappa P} > 0 and the last integral > 0. The sum over n in Z diverges for every q > 0. ∎

**Remark 1'' (convexity).** kappa -> log I(x,kappa) is convex (Hölder), so K_x := {kappa : I(x,kappa) < inf} is an interval. Lemma C (GH, dim >= 2) says 0 is not in K_x. So (SO) says K_x is empty. A failure of (SO) at x gives an interval K_x lying entirely on one side of 0.

**Remark (asymptotic meaning).** By Lemma 1, if kappa in K_x, every weak* limit mu of backward empirical measures (1/T) int_{-T}^0 delta_{g_s x} ds satisfies mu(d) >= kappa. Indeed (1/T) int_{-T}^0 d(g_s x) ds = -J_{-T}(x)/T >= kappa - C/T. Symmetrically, every forward limit satisfies mu(d) <= kappa.

## 2. Main partial result: orbits exponentially asymptotic to a fixed point of some g_P

I use Lemma K and Lemma K' of block R6-a §3 exactly as quoted in the brief:
- Lemma K: under GH there are no p, P > 0 with g_P p = p and no y != p such that (a) d(g_{-mP} y, p) <= C theta^m for all integers m >= 0 (some theta in (0,1)) and (b) J_t(y) <= C - eps t for all t >= 0 (some eps > 0).
- Lemma K': the same with time reversed: no y != p with d(g_{mP} y, p) <= C theta^m (m >= 0) and J_t(y) <= C - eps|t| for all t <= 0.
Their proofs use GH only through Theorem J, and Theorem J uses only (F1) and (F2), i.e. (K0) and (K1) (Remark (i) after Theorem J).

**Theorem 2.** Assume GH (in fact (K0) and (K1) suffice). Let x in M and kappa != 0. Suppose that one of the following holds:
 (i) kappa > 0, and there are p in M, P > 0 with g_P p = p, and C, theta in (0,1), such that d(g_{mP} x, p) <= C theta^m for all integers m >= 0 (x is forward-exponentially asymptotic to p along the times mP);
 (ii) kappa < 0, and the same holds with g_{-mP} x in place of g_{mP} x (backward-exponentially asymptotic);
 (iii) x is a zero of X or a periodic point.
Then int_R e^{J_t(x) - kappa t} dt = +infinity.
*Proof.* (iii) is Lemma 1'. In (i) and (ii), if x = p then g_P x = x, so x is a zero or periodic, and (iii) applies. So assume x != p, and suppose for contradiction that I(x,kappa) < inf. By Lemma 1, J_t(x) <= C_1 + kappa t for all real t.
 (i) kappa > 0. For t <= 0 this reads J_t(x) <= C_1 - kappa|t|. With y = x, eps = kappa and the constant max(C, C_1), the hypotheses of Lemma K' hold, which is a contradiction.
 (ii) kappa < 0. For t >= 0 this reads J_t(x) <= C_1 - |kappa| t. That is (b) of Lemma K with eps = |kappa|, and (a) is the hypothesis. Lemma K gives a contradiction. ∎

Note what Theorem 2 does NOT need: hyperbolicity of p, any information on the other end of the orbit, or margins. The tilt is absorbed because Lemma 1 turns the finiteness at kappa into linear volume decay on exactly the side opposite to the asymptotic one. On that side, Lemma K / K' need decay of the UNtilted Jacobian, and they recover arbitrary decay on the asymptotic side from the jets of p (Cayley-Hamilton).

**Corollary 3.** Assume GH. Let gamma be a hyperbolic periodic orbit or a hyperbolic zero.
 (a) If kappa > 0 and omega(x) = gamma (equivalently x in W^s(gamma)), then I(x,kappa) = inf.
 (b) If kappa < 0 and alpha(x) = gamma (x in W^u(gamma)), then I(x,kappa) = inf.
 (c) In particular, (SO) holds for every kappa != 0 at every point of W^u(gamma_1) ∩ W^s(gamma_2), for hyperbolic periodic orbits or zeros gamma_1, gamma_2.
*Proof.* (a) By the stable manifold theorem [SM], as quoted in R6-a §4, x lies in W^{ss}(q) for some q in gamma, and d(g_t x, g_t q) <= C_x e^{-ct} for t >= 0. Let P be the period of gamma (P = 1 for a zero). Then g_{mP} q = q, so d(g_{mP} x, q) <= C_x (e^{-cP})^m, and Theorem 2(i) applies. (b) The same with W^{uu} and Theorem 2(ii). (c) For kappa > 0 use (a) with gamma_2; for kappa < 0 use (b) with gamma_1. ∎
(Part (c) can also be read off from Corollary 4.1 of R6-a. That corollary gives I(gamma_1) <= 0 <= I(gamma_2). The Remark in §1 gives I(gamma_2)/P_2 <= kappa <= I(gamma_1)/P_1, which forces kappa = 0. Theorem 2 is stronger, because it needs only ONE end.)

## 3. The margin case is exactly the order-0 half of (NJ)

**Proposition 4.** Let x satisfy J_t(x) <= C + a t for t >= 0 and J_t(x) <= C + b t for t <= 0, with a < b. (No GH is needed for (i)-(ii).)
 (i) For a < Re s < b, put B_s(phi) := int_R e^{J_t(x) - s t} phi(g_t x) dt and A_s(phi) := d/ds B_s(phi) = -int_R t e^{J_t(x) - s t} phi(g_t x) dt. Both are complex measures of finite mass (order 0), holomorphic in s, and they satisfy
 B_s(P phi) = s B_s(phi),  A_s(P phi) = s A_s(phi) + B_s(phi)  for all smooth phi.
 (ii) For real s in (a,b), B_s is a positive measure of positive mass. Hence every real c in (a,b) carries an order-0 Jordan chain (and so does every complex c in the strip outside a discrete set).
 (iii) Under GH, 0 is not in [a,b]. If 0 were in (a,b), I(x,0) < inf would contradict Lemma C. If 0 = a, every s in (0,b) is still covered by (ii). So a failure of (SO) with margins yields order-0 chains at real points c != 0.
*Proof.* |e^{J_t - s t}| <= e^{C - (Re s - a)t} for t >= 0, and <= e^{C + (b - Re s) t} for t <= 0. Both decay exponentially, locally uniformly in s, so the integrals (including those with the factor t) converge absolutely and can be differentiated under the integral sign. Next, d/dt [e^{J_t - st} phi(g_t x)] = e^{J_t - st} ((P phi)(g_t x) - s phi(g_t x)). Integrating over [-R,R] and letting R -> inf (the boundary terms tend to 0) gives B_s(P phi) = s B_s(phi). Differentiating this identity in s gives B_s'(P phi) = B_s(phi) + s B_s'(phi), i.e. the stated relation for A_s = B_s'. (ii): B_s(1) = int e^{J_t - st} dt > 0. For fixed phi with B_sigma(phi) != 0 (sigma real), s -> B_s(phi) is holomorphic and not identically 0, so its zeros are discrete. ∎

Combined with Lemma 1.1 / Cor. 1.2 of R9-c (quoted in the brief: an order-0 chain at c forces |B| to be carried by {x : I(x, Re c) < inf}), this gives:
- (SO) at kappa for all x  ==>  no order-0 chain at any c with Re c = kappa;
- an order-0 chain-free real point in every interval (a,b) not containing 0 (i.e. order-0 (NJ) on the real axis)  ==>  (SO) for every orbit with exponential margins.
So the margin-restricted version of (SO) carries no simplification: it is essentially equivalent to the real-axis part of order-0 (NJ). Without margins, a failure of (SO) at kappa gives only the eigen-measure B_kappa (Observation 0: u = B_kappa/nu, Xu = -kappa u, nonnegative, carried by one orbit). A chain also needs int |t| c_x(t) dt < inf, which may fail.

## 4. Where the general argument stops

Take kappa > 0; the case kappa < 0 follows by reversing time. After Theorem 2, a counterexample to (SO) must have all of the following:
 - J_t(x) <= C + kappa t for all t (Lemma 1). So the orbit contracts volume at rate >= kappa in backward time, and every backward empirical limit has mu(d) >= kappa > 0.
 - x is NOT forward-exponentially asymptotic to any fixed point of any g_P. In particular omega(x) is not a hyperbolic periodic orbit or a hyperbolic zero.
 - x may well be backward asymptotic to a periodic orbit gamma, necessarily with I(gamma)/P >= kappa > 0, i.e. a volume-expanding periodic orbit, which Corollary 4.1 of R6-a allows as an alpha-limit only if the orbit does not end on a hyperbolic periodic orbit.
Concretely, the simplest case left open is: x in W^u(gamma), gamma hyperbolic periodic with I(gamma)/P > kappa > 0, and the forward orbit of x accumulating on a non-periodic set (e.g. a horseshoe, or a non-hyperbolic set) with forward growth J_t(x) <= C + kappa t.

Why the available tools fail there.
1. *Theorem J needs untilted two-sided decay.* With S supported on the orbit of x, the failure of (SO) gives two-sided decay of e^{-kappa t} F_phi(t), where F_phi(t) = S(e^{J_t} phi o g_t), and not of F_phi itself. The tilted moments m_j(phi) = int t^j e^{-kappa t} F_phi(t) dt satisfy m_0((P - kappa)phi) = 0 and m_j((P - kappa)phi) = -j m_{j-1}(phi). The induction of Theorem J then needs (F1)/(F2) for P - kappa in place of P, i.e. "no eigen-density at kappa", which is (E1), stronger than (SO). GH visibly acts only through (F1), (F2), at the spectral point 0.
2. *Jets fix only the asymptotic side.* Cayley-Hamilton (Lemma K) or vanishing moments in a leaf parameter (Prop. 6.2 of R6-a) produce a combination S = sum w_j delta_{y_j} whose transport decays at ANY prescribed rate on the side where the y_j are mutually exponentially asymptotic. On the other side, F_phi = Q(shift) f with f(t) = e^{J_t(x)} phi(g_t x) (for points on one orbit), or a sum of such terms over partner points. A finite difference operator cannot turn growth of order e^{kappa t} into decay unless f has matching (quasi-)periodic structure on that side. In Theorem 2 the free side is exactly the side where Lemma 1 already gives decay; the open case is the one where the asymptotic structure is on the same side as the decay.
3. *Pairs off the orbit need information on the partner.* A pair S = delta_x - e^b delta_y with y in the strong unstable set of x (as in Prop. 6.1 of R6-a) gives backward decay only if the backward contraction rate between x and y beats the backward growth of e^{J_t(x)}. In the case kappa > 0 the backward side already decays; the forward side needs J_t(y) <= C - eps t. For an arbitrary partner y nothing is known about that, while for x itself only J_t(x) <= C + kappa t is known.
4. *Symmetries of GH do not move kappa to 0.* Time changes Y = hX (h > 0 smooth) keep GH (O4). They change J along an orbit only by the bounded term log h(g_t x) - log h(x), as a function of the old time t, and they rescale time by tau(t) = int_0^t ds / h(g_s x). The kappa = 0 integral becomes int e^{J_t(x)} dt / h(g_t x) up to bounded factors, so its finiteness is invariant. Hence no time change maps a kappa != 0 violation to a kappa = 0 violation (and so to Lemma C). Reversal X -> -X maps kappa to -kappa. Changing nu, or conjugating by e^a, changes J by bounded amounts. So all known GH-preserving operations preserve the class of orbits with 0 not in K_x.
5. *(K0) + (K1) only.* Theorem 2 needs only (K0) and (K1). I do not know whether (SO) itself follows from (K0) + (K1). I have no example of a field satisfying (K0) and (K1) with K_x nonempty for some x. Note that (K0) applied to bounded invariant functions already forces nu-ergodicity, so such an example would need a nu-null orbit running from a volume-contracting (backward) region to a slower one inside a nu-ergodic flow. I could neither build one nor rule it out.

## 5. Status

Proved:
- Lemma 1, Lemma 1', the convexity remark (elementary, no GH).
- Theorem 2: (SO) at (x, kappa) for kappa > 0 when x is forward-exponentially asymptotic to a fixed point of some g_P (zero or periodic point, hyperbolic or not), for kappa < 0 in the backward case, and for x periodic or a zero. It uses only (K0) and (K1), via Lemma K / K' of R6-a.
- Corollary 3: (SO) for kappa > 0 on all of W^s(gamma), and for kappa < 0 on all of W^u(gamma), gamma a hyperbolic periodic orbit or zero (cites the classical stable manifold theorem). Hence (SO) holds for all kappa != 0 on every heteroclinic or homoclinic orbit of hyperbolic periodic orbits or zeros.
- Proposition 4 (no GH): an orbit violating (SO) with exponential margins a < b produces order-0 Jordan chains at all real c in (a,b), and these c are != 0 under GH. With Lemma 1.1 of R9-c, the margin version of (SO) is equivalent in strength to excluding order-0 chains on the real axis. So no margin-restricted partial result is easier than the order-0 half of (NJ).
Open:
- (SO) in general. The first open case: kappa > 0 and x backward-asymptotic to a volume-expanding periodic orbit (I/P >= kappa), with the forward orbit not exponentially asymptotic to any periodic point or zero (and symmetrically for kappa < 0).
- Whether (SO) follows from (K0) + (K1) alone.
- (E1) (no real eigen-distribution at kappa != 0), which would imply (SO) at once.

=== END OF ANSWER round10_q6 ===

