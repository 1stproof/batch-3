# round13_q7 — answer

## 0. Status (read first)
- **(PE0) is NOT proved here, and no counterexample is given.** The problem's claim (zero topological entropy under GH)
  therefore stays proved only in the cases already in the ledger (dim M <= 3; all hyperbolic measures; etc.).
- I checked the chain (Section 1). It correctly derives the claim from (PE0) + Block R11-a, modulo the cited theorems.
- New material (Section 2): a self-contained Laplace/Liouville form of the pair obstruction, Theorem R. It proves that a
  counterexample to (PE0) yields holomorphic families of eigen-distributions X w_z = -z w_z on a strip 0 < Re z < eps,
  vanishing only on a discrete set; and the same with -X. Hence (PE0) follows from a "local E1" statement: for every
  eps > 0, X + kappa is injective on D' for uncountably many kappa in (0, eps). **Honest overlap note:** after
  deriving it I found that this is essentially Theorem B of block R5-a (stated there under "every invariant mu has mu(d)=0";
  here only the single measure mu is needed), together with remark (iv) after Theorem J. So it is a sharpening and
  re-proof, not a new mechanism. I add the volume-case observation that the family is flat at z = 0 in every sector
  (Prop. 2.3). That matches the ledger's "spectral flatness" dead end and shows exactly where it gets stuck.
- Dead end recorded (Section 3): a global route (pigeonhole approximate closing + the dual estimate (O1)) gives only
  approximate configurations. Rearranged orbit segments satisfy those, so the route yields no contradiction.

## 1. Check of the chain
Step 1 (variational step) is correct. Two details I checked:
(a) If mu is g_1-invariant and g_1-ergodic, then mu-bar = int_0^1 (g_s)_* mu ds is flow-invariant and flow-ergodic. Proof:
for a flow-invariant Borel set A, mu-bar(A) = int_0^1 mu(g_{-s}A) ds = mu(A), and A is g_1-invariant, so mu(A) is 0 or 1.
(b) Entropy: h_{(g_s)_*mu}(g_1) = h_mu(g_1), since g_s conjugates g_1 to itself. Jacobs' integral formula then gives
h_{mu-bar}(g_1) = h_mu(g_1). Also mu-bar(d) = int_0^1 int d o g_s dmu ds = int J_1 dmu.
So a counterexample to (PE0) may be taken flow-invariant and flow-ergodic with mu(d) = 0. This is used below.
Step 2 is Block R11-a; I did not re-check it. Step 3 is logic. h_top(g_t) = |t| h_top(g_1) is standard (Abramov).
So the chain is sound modulo (PE0) and the cited inputs.

## 2. Theorem R (Laplace/Liouville form of the pair obstruction) — proved, modulo Pesin theory as cited in Prop. 6.1
Conventions as in the brief: P phi = X phi + d phi, and e^{tP} phi := e^{J_t} (phi o g_t). Then d/dt e^{tP}phi = e^{tP} P phi.
A distribution density H with H(P phi) = z H(phi) for all phi gives w = H/nu with X w = -z w (Observation 0).

**Lemma 2.1 (abstract).** Assume GH (in fact only the definitions are used here). Let S be a distribution density and
F_phi(t) := S(e^{tP} phi). Assume there are eps > 0 and C with
(i) |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^1} for t <= 0;
(ii) for every delta > 0 there is C_delta with |F_phi(t)| <= C_delta e^{delta t} ||phi||_{C^0} for t >= 0.
For Re z > 0 put G_+(z)(phi) = int_0^inf e^{-zt} F_phi(t) dt. For Re z < eps put G_-(z)(phi) = int_{-inf}^0 e^{-zt} F_phi(t) dt.
On the strip Sigma = {0 < Re z < eps} put H(z) = G_+(z) + G_-(z). Then:
(a) H(z) is a distribution density of order <= 1, holomorphic in z, and H(z)(P phi) = z H(z)(phi).
(b) If H vanishes on a subset of Sigma with an accumulation point in Sigma, then S = 0.

*Proof.* F_phi is C^1 with F_phi' = F_{P phi} (Theorem J step 1). Bounds (i), (ii) also hold for P phi, with C^2 norms of phi.
G_+(z) converges absolutely for Re z > 0 (take delta < Re z). G_-(z) converges absolutely for Re z < eps. Both are
holomorphic, by dominated differentiation on compact sets. Explicitly,
|G_+(z)(phi)| <= C_delta ||phi||_{C^0} / (Re z - delta) and |G_-(z)(phi)| <= C ||phi||_{C^1} / (eps - Re z).
Integration by parts uses e^{-zt}F_phi(t) -> 0 at +inf when Re z > delta, and at -inf when Re z < eps. It gives
 G_+(z)(P phi) = -S(phi) + z G_+(z)(phi),  G_-(z)(P phi) = S(phi) + z G_-(z)(phi).
Adding these on Sigma gives (a).
(b) By the identity theorem, H(z)(phi) = 0 on all of Sigma for every phi, so G_+ = -G_- on Sigma. Define E(z) := G_+(z)(phi)
for Re z > 0 and E(z) := -G_-(z)(phi) for Re z < eps. This is an entire function. For Re z >= eps/2 (take delta = eps/4),
|E| <= 4 C_{eps/4} ||phi||_{C^0} / eps. For Re z <= eps/2, |E| <= 2C ||phi||_{C^1} / eps. So E is bounded and, by Liouville,
constant. As Re z -> +inf, G_+(z)(phi) -> 0 by the first bound, so E = 0. Hence the Laplace transform of the continuous,
sub-exponentially growing function F_phi on [0, inf) vanishes for all z > 0. By Lerch's uniqueness theorem F_phi = 0 on
[0, inf), and S(phi) = F_phi(0) = 0. Since phi was arbitrary, S = 0. ∎

**Theorem R.** Assume GH and let mu be a counterexample to (PE0). By Section 1 we may take mu flow-ergodic with mu(d) = 0
and h_mu(g_1) > 0. Let chi_min^+ > 0 be its smallest positive exponent and chi_max^- < 0 its largest negative exponent.
Then for every eps in (0, chi_min^+) there is a holomorphic family z -> H(z), 0 < Re z < eps, of distribution densities
of order <= 1. Each H(z) gives w_z = H(z)/nu with X w_z = -z w_z, and w_z != 0 outside a discrete subset of the strip.
The same holds for -X: there are w'_z != 0 with X w'_z = +z w'_z, 0 < Re z < eps' < |chi_max^-|, outside a discrete set.
*Proof.* Take x, y exactly as in Prop. 6.1 (block R6-a; this cites [P] and [LY], with Lemma 6.0). Thus x != y,
y lies in W^u_loc(x), both are two-sided Birkhoff-generic for d, and d(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0, where
theta = chi_min^+ - delta'. Put b = lim_{t->-inf} (J_t(x) - J_t(y)) and S = delta_x - e^b delta_y != 0.
Since mu(d) = 0 we have J_t(x), J_t(y) = o(|t|) in both time directions. Hence:
- (ii) holds with the C^0 norm;
- (i) holds with rate theta - delta'', by the estimate of Prop. 6.1 / R5-a Theorem B(c): the factor e^{J_t(x)} = e^{o(|t|)}
  times the backward cancellation C e^{-theta|t|} ||phi||_{C^1}.
Apply Lemma 2.1. For -X use (O4). ∎

**Corollary 2.2 (a sufficient condition for (PE0)).** (PE0) holds if, for every eps > 0, X + kappa is injective on
distributions of order <= 1 for uncountably many real kappa in (0, eps). (An uncountable subset of (0, eps) has an
accumulation point in (0, eps); apply Lemma 2.1(b) on the real segment.) The condition in the other sign is equally
sufficient, via -X. So a counterexample to the problem must have real point spectrum of X on D' filling (-eps, 0) and
(0, eps') up to countable sets. Real eigen-*measures* never exist: if m is a finite signed measure with
L_X m = kappa m, kappa != 0, then |m| satisfies the same relation, because transport with positive weights preserves
|.|; pairing with 1 gives kappa |m|(M) = 0. So the eigen-distributions must have infinite variation, as H(z) does.
(H(z) is a convergent dipole series along the backward orbits.)

**Proposition 2.3 (volume case: flatness at 0; proved).** Suppose in addition that nu is X-invariant (d = 0). Under GH
every mean-zero smooth f equals Xh with h smooth (O2). Then for each phi and each N, |H(z)(phi)| <= C_{N,phi} |z|^N / Re z
as z -> 0 in the strip. In particular H(z) = O(|z|^{N-1}) for every N in every sector |arg z| <= pi/2 - delta.
*Proof.* S(1) = 0. Write phi = c + X h_1, h_1 = c_1 + X h_2, and so on, with h_j smooth (O2). Integration by parts as in
Lemma 2.1 gives G_+(z)(Xh) = -S(h) + z G_+(z)(h) and G_-(z)(Xh) = S(h) + z G_-(z)(h). Since S kills constants, iterating gives
 H(z)(phi) = z H(z)(h_1) = ... = z^N H(z)(h_N),
and |H(z)(h_N)| <= ||h_N||_{C^1}(C'/Re z + C''/eps). ∎
So H is a nonzero holomorphic family that is flat at 0 in sectors, like e^{-1/z}. This is not contradictory. A
contradiction would need a holomorphic continuation of G_+ across Re z = 0 near 0, i.e. a forward decay rate for
F_phi. GH gives no such rate (the h_N lose derivatives without control). This is the same obstruction as the ledger's
"GH acts only at the spectral point 0" and the closed Mechanism B.

## 3. Dead end: global approximate closing
Fix k = 1 in Lemma 2 of Text B. Then for every smooth u, Lip(u) <= C ||Xu||_{C^m}. Hence for orbit-segment measures
gamma_{x,T}, the functional gamma_{x,T} - gamma_{y,T} equals an invariant distribution plus an error S with
||S||_{(C^m)'} <= C(d(x,y) + d(g_T x, g_T y)). In the volume case the invariant part is forced to be small, so
|int_0^T phi(g_t x) dt - int_0^T phi(g_t y) dt| <= C ||phi||_{C^m} (d(x,y) + d(g_T x, g_T y)).
Positive entropy gives e^{hT} (T, eps)-separated points. Pigeonhole in M x M then gives separated x, y with
d(x,y), d(g_T x, g_T y) <= delta = e^{-hT/(3n)}.
**Why it is dead:** the conclusion only says that the two occupation measures agree in (C^m)' up to delta. Two orbit
segments that traverse the same nearly self-returning pieces in a different order (as in any horseshoe) have occupation
measures differing only near the junctions, by about the junction gap. Junction gaps of size delta are compatible with
all the above. So approximate configurations carry no contradiction; only exact closing can (the ledger's #123 and
Theorem A0). I found no way to get exact closing from GH in the presence of zero exponents.

## 4. Context (from memory; please verify)
The dim <= 3 case also follows from Katok's horseshoe theorem (as in Theorem 5.2), and I believe this is how the
three-dimensional results on the Katok and Greenfield–Wallach conjectures (Kocsard; Forni, around 2008–2009) exclude
positive entropy. I know of no published proof of zero entropy for GH (or even cohomology-free) flows in dimension >= 4.
The general claim is implied by the Greenfield–Wallach conjecture. I recall it as open in that generality, but this
recollection is uncertain.

## 5. Open questions (explicit)
1. (PE0) itself.
2. Local E1: under GH, is X + kappa injective on D' (order <= 1 suffices) for uncountably many kappa in (0, eps), for
   every eps > 0? By Corollary 2.2 this implies (PE0).
3. Equivalent analytic form: for the pair S of Theorem R, does z -> S((z - P)^{-1}) continue holomorphically from
   Re z > 0 to a neighbourhood of 0? This needs a forward decay rate, which GH has not been shown to give.
4. Exact su-cycles (closing up to a flow shift) for positive-entropy measures with zero exponents. In the volume
   case Theorem T would then finish.

=== END OF ANSWER round13_q7 ===
