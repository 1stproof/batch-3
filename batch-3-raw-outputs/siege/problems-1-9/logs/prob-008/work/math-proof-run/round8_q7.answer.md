# round8_q7 answer

## Plan
Target: (PE-NH) via the named approach (invariance principle / accessibility dichotomy for the zero-exponent centre).
Steps: (1) turn the "rigid" branch into a precise, checkable criterion that feeds Theorem G (R7-f) and prove it;
(2) check whether any invariance principle in the literature delivers the dichotomy for a general non-hyperbolic
positive-entropy measure; (3) isolate exactly what the "twisting" branch would need.

## 0. Status (summary)
- **Proved (modulo standard Pesin block facts, cited, and Theorem G of R7-f):** Proposition B, a *bracket criterion*:
  under GH, for an ergodic mu with h_mu(g_1) > 0 and mu(d) = 0, the local weak-stable plaques and local strong-unstable
  plaques of mu-good points meet only on a set of pairs of measure zero. This holds for mu x mu, and also for every
  relative product m x_zeta m along any measurable "slicing" zeta whose conditionals do not charge asymptotic classes.
  This is the rigorous form of the "rigid" branch: any rigidity conclusion that yields positive-measure bracket
  closing, even only inside centre slices, contradicts GH. As a by-product it gives a horseshoe-free proof that
  hyperbolic measures with mu(d) = 0 cannot have positive entropy under GH.
- **Not obtained:** the dichotomy itself. No invariance principle I know (cited below from memory) applies to a
  general non-hyperbolic positive-entropy measure of a flow. All of them need a uniform or skew-product centre
  fibration and a base with local product structure. The "twisting" branch (bracket set null for every admissible
  slicing) is left exactly where R7-f left it. A measure-theoretic version of Theorem G (Section 5) shows that
  inside one box the twisting branch is not contradicted by measure theory alone.
- **Open:** (PE-NH) itself; precisely, the twisting branch (TW) of Section 6, and the large-|lambda| cases.

## 1. Setting and standard inputs

Let mu be ergodic and flow-invariant, with h_mu(g_1) > 0 and lambda = mu(d) = 0, where d = div_nu X and
J_t(z) = int_0^t d(g_s z) ds as in the background. Let chi^+_min > 0 > chi^-_max be the exponents closest to 0 (they
exist by Ruelle's inequality for g_1 and g_{-1}). Fix 0 < eta < theta < min(chi^+_min, |chi^-_max|).

**[PB] Pesin blocks (standard, cited from memory; Pesin, Fathi–Herman–Yoccoz, Barreira–Pesin).** For the C^inf
diffeomorphism g_1 there are compact sets K_l, increasing in l, with mu(union K_l) = 1, and constants r_l > 0, C_l,
with the following properties. For z in K_l there are C^1 embedded closed discs W^{ss}_loc(z) and W^{uu}_loc(z)
through z (local strong stable and strong unstable manifolds, tangent to the sums of the Oseledets spaces with
negative, resp. positive, exponents). They have inner radius >= r_l and depend continuously on z in K_l (in the C^1
topology), and
 d(g_t y, g_t z) <= C_l e^{-theta t} for t >= 0 and y in W^{ss}_loc(z);
 d(g_t y, g_t z) <= C_l e^{-theta|t|} for t <= 0 and y in W^{uu}_loc(z).
(Real times are obtained from integer times by interpolation, as in R5-a Lemma 2.)

Since J_t(z)/t -> 0 as t -> +-inf for mu-a.e. z, the function z -> sup_t (J_t(z) - eta|t|) is finite a.e. Also, for
mu-a.e. z the forward and backward orbits of z are dense in supp mu. Intersecting, we may and do assume that every
z in K_l satisfies J_t(z) <= l + eta|t| for all real t and has forward and backward orbit dense in supp mu.

Put W^{s0}_loc(z) := union over |tau| <= r_l of g_tau(W^{ss}_loc(z)) (the local weak-stable plaque).

**Asymptotic relations.** Write z ≈_s z' if there is sigma in R with d(g_t z', g_{t+sigma} z) -> 0 as t -> +inf, and
z ≈_u z' if the same holds as t -> -inf. These are equivalence relations (the shifts add, as in R7-f Remark (5)).

## 2. Lemma 1 (proved): asymptotic classes are mu-null

**Lemma 1.** If mu is ergodic, flow-invariant and not carried by a single orbit (in particular if h_mu(g_1) > 0),
then mu({z' : z' ≈_s z}) = 0 for every z, and likewise for ≈_u.

*Proof.*
1. A_z := {z' : z' ≈_s z} is flow-invariant, because z' ≈_s z implies g_r z' ≈_s z (with shift sigma + r). It is
   also universally measurable: it is the projection of a Borel subset of M x R, i.e. an analytic set. By
   ergodicity, mu(A_z) is 0 or 1. Suppose it is 1.
2. *Uniformization.* For z' in A_z choose a shift sigma(z'). For S, T > 0 and eps > 0, the set
   B(S, T, eps) := {z' : |sigma(z')| <= S and d(g_t z', g_{t+sigma(z')} z) < eps for all t >= T}
   increases to A_z as S, T -> inf (for fixed eps). (Measurability: replace "some sigma" by "some sigma in
   [-S, S]"; the condition is then closed in sigma and the set is analytic.) Fix S with
   mu(union_T B(S, T, eps)) >= 1/2 for every eps, which is possible since these sets increase as eps grows.
3. For z' in B(S, T, eps) we have g_T z' in N_eps(gamma_T), where gamma_T := g_{[T-S, T+S]} z is an orbit segment of
   time length 2S. Hence mu(B) = mu(g_T B) <= mu(N_eps(gamma_T)) <= s(eps) := sup over orbit segments gamma of time
   length 2S of mu(N_eps(gamma)).
4. *s(eps) -> 0 as eps -> 0.* If not, take segments gamma_k = g_{[0,2S]} w_k and eps_k -> 0 with
   mu(N_{eps_k}(gamma_k)) >= c > 0. Pass to a subsequence with w_k -> w. Then gamma_k -> gamma = g_{[0,2S]} w
   uniformly. So for every delta > 0, mu(closed N_delta(gamma)) >= c, and therefore mu(gamma) >= c. An ergodic
   flow-invariant probability giving positive mass to a compact orbit segment is carried by that orbit, and that
   orbit is then periodic or a zero (a non-periodic orbit has infinite measure under invariance). This is excluded.
5. Choose eps with s(eps) < 1/4 and then T with mu(B(S, T, eps)) > 1/4. This contradicts step 3.
The case of ≈_u is the same with t -> -inf. ∎

## 3. Proposition B (proved modulo [PB] and Theorem G of R7-f): the bracket criterion

Fix l and a ball U of radius much smaller than r_l. Put m := mu restricted to K_l ∩ U and
 E := {(z, z') in (K_l ∩ U)^2 : W^{s0}_loc(z) ∩ W^{uu}_loc(z') is nonempty}.
E is closed in K_l x K_l, since the plaques are compact and vary continuously on K_l, hence Borel.

**Proposition B.** Assume GH, and let mu be ergodic with h_mu(g_1) > 0 and mu(d) = 0. Let zeta be any measurable
partition of K_l ∩ U, with conditional measures m_y (y in the quotient, with quotient measure m-hat), such that for
m-hat-a.e. y the measure m_y gives zero mass to every ≈_s-class and every ≈_u-class. Then
 ∫ (m_y x m_y)(E) dm-hat(y) = 0.
In particular (zeta = trivial partition; its hypothesis holds by Lemma 1): (m x m)(E) = 0.

*Proof.* Suppose the integral is positive. Fix y with δ := (m_y x m_y)(E) > 0 for which m_y does not charge
asymptotic classes, and normalize m_y to a probability.
1. *A 3 x 2 grid of pairs (Cauchy–Schwarz).* Write E^{z'} := {z : (z, z') in E} and f(z) := m_y({z' : (z, z') in E}).
   Then ∫∫ m_y(E^{z'_1} ∩ E^{z'_2}) dm_y(z'_1) dm_y(z'_2) = ∫ f^2 dm_y >= (∫ f dm_y)^2 = δ^2 > 0.
   So the set Q of pairs (z'_1, z'_2) with m_y(E^{z'_1} ∩ E^{z'_2}) > 0 has positive m_y x m_y-measure. The set of
   pairs with z'_1 ≈_u z'_2 has measure ∫ m_y([z'_1]_u) dm_y(z'_1) = 0 (Fubini for the universally measurable
   relation). Choose (z'_1, z'_2) in Q with z'_1 not ≈_u z'_2. The set F := E^{z'_1} ∩ E^{z'_2} has positive
   m_y-measure, and each ≈_s-class is m_y-null. So we can choose z_1, z_2, z_3 in F, pairwise not ≈_s.
2. *The configuration.* For i = 1, 2, 3 and j = 1, 2, pick y_{ij} in W^{s0}_loc(z_i) ∩ W^{uu}_loc(z'_j). Write
   y_{ij} = g_{tau_{ij}} v_{ij} with v_{ij} in W^{ss}_loc(z_i) and |tau_{ij}| <= r_l.
3. *Distinct, non-periodic orbits ((G1) of R7-f).*
   - If y_{ij} were periodic or a zero, z_i would be forward asymptotic to that orbit O, so the omega-limit of z_i
     would be O. But the forward orbit of z_i is dense in supp mu, which is not a single orbit. Contradiction.
   - If y_{kl} = g_s y_{ij} with i != k: since y_{ij} ≈_s z_i (via v_{ij}) and y_{kl} ≈_s z_k, transitivity gives
     z_i ≈_s z_k, which is excluded.
   - If i = k and j != l, the same argument backward gives z'_j ≈_u z'_l, which is excluded.
4. *Classes ((G2), (G3)).* The forward classes are C_i = {y_{i1}, y_{i2}} with representative y_{i1}. For t >= 0,
   d(g_t y_{i2}, g_{t + tau_{i2} - tau_{i1}} y_{i1})
   <= d(g_{t+tau_{i2}} v_{i2}, g_{t+tau_{i2}} z_i) + d(g_{t+tau_{i2}} z_i, g_{t+tau_{i2}} v_{i1})
   <= C' e^{-theta t},
   by [PB] (the finitely many times with t + tau < 0 are absorbed into the constant). The backward classes are
   D_j = {y_{1j}, y_{2j}, y_{3j}}, all in W^{uu}_loc(z'_j), with representative y_{1j} and shift 0. By [PB] and the
   triangle inequality, d(g_t y_{kj}, g_t y_{1j}) <= 2 C_l e^{-theta|t|} for t <= 0.
5. *Growth ((G4)).* For t >= 0, J_t(y_{ij}) = J_{t+tau}(v) - J_tau(v) with v = v_{ij}, tau = tau_{ij}, and
   |J_s(v) - J_s(z_i)| <= Lip(d) C_l/theta for s >= 0. Since J_s(z_i) <= l + eta|s|, this gives
   J_t(y_{ij}) <= C'' + eta t. For t <= 0, |J_t(y_{ij}) - J_t(z'_j)| <= Lip(d) C_l/theta and
   J_t(z'_j) <= l + eta|t|. Here eta < theta.
6. So N = 6 points, p = 3 forward classes and q = 2 backward classes form grid data in the sense of R7-f, with
   N > p + q. Theorem G of R7-f (which rests on Theorem J) says this is impossible under GH. ∎

**Remarks.**
1. *(Hyperbolic measures, horseshoe-free.)* If mu is hyperbolic with mu(d) = 0, local product structure of Pesin
   plaques says W^{s0}_loc(z) and W^{uu}_loc(z') meet whenever z, z' in K_l ∩ U and U is small (cited, standard).
   So E = (K_l ∩ U)^2 and (m x m)(E) = m(U ∩ K_l)^2 > 0 for a ball U around a density point. Proposition B then
   recovers Theorem 5.1 (for mu(d) = 0) without the Katok / Lian–Young horseshoe theorem.
2. *(Sanity check.)* N × T^q with g_t = (Anosov flow h_t) × (Diophantine translation) and mu = m × Haar, m Gibbs
   (not GH, by (O2)). Take zeta to be the partition by the T^q-coordinate. Then m_y is (m restricted to a base box)
   × delta_theta. It does not charge asymptotic classes (Lemma 1 for the base). Base local product structure gives
   (m_y x m_y)(E) > 0. So Proposition B correctly detects non-GH, although (m x m)(E) = 0 there: the brackets close
   only within T^q-slices. This is why the relative form is needed.
3. Proposition B is exactly the form the "rigid" branch must deliver. It suffices to show that, for some good box,
   some measurable slicing zeta whose conditionals do not charge asymptotic classes, and a positive measure of
   slices, strong-unstable and weak-stable plaques of good points close up (meet) for a positive-measure set of
   pairs. An invariance-principle conclusion of the classical type gives this. Suppose mu sits on a fibration over a
   hyperbolic base measure with local product structure, and its centre disintegration is su-holonomy invariant.
   Then slicing by holonomy-transported centre coordinates gives the sanity-check situation.

## 4. The invariance principle: what it says and why it does not apply here

Cited from memory; hypotheses as I recall them.
- **Ledrappier (1986, LNM 1186, "Positivity of the exponent for stationary sequences of matrices").** Let A be a
  measurable linear cocycle over (X, mu, f), and let B be a sub-sigma-algebra with f^{-1}B ⊂ B (or the reverse
  inclusion, depending on the version) such that A is B-measurable. If lambda_min(A) = lambda_max(A), then every
  invariant measure on the projective bundle that projects to mu has a B-measurable disintegration. Problem here:
  (i) it concerns projective measures of a *linear* cocycle, whereas Proposition B needs information about mu
  itself along a nonlinear centre; (ii) for the natural cocycle Dg_t|E^c_0 with B = the sigma-algebra of the
  unstable partition, A is not B-measurable (Dg depends on the point, not only on its W^{uu}-plaque). Avila–Viana's
  holonomies are the substitute for (ii).
- **Avila–Viana (Invent. Math. 181 (2010), "Extremal Lyapunov exponents: an invariance principle and
  applications"), Theorem B/D type.** Let F be a smooth cocycle on a fibre bundle with compact fibres over a
  hyperbolic homeomorphism (or a partially hyperbolic map) whose invariant base measure has local product
  structure, and suppose F admits stable and unstable holonomies (fibre bunching). If the fibre exponents of an
  F-invariant measure m vanish, then m has a disintegration that is s- and u-holonomy invariant, and continuous on
  the support when the base measure has local product structure.
- **Avila–Santamaria–Viana (Astérisque 358, 2013)** and **Tahzibi–Yang (Trans. AMS 2019, "Invariance principle and
  rigidity of high entropy measures")**: these are versions for uniformly partially hyperbolic diffeomorphisms
  (Tahzibi–Yang: one-dimensional centre, with an entropy hypothesis).

**Hypothesis check for a general non-hyperbolic positive-entropy mu of a GH flow.** None of these frameworks is
available.
- (a) There is no invariant centre fibration or foliation: Pesin centre manifolds are neither unique nor invariant
  as a lamination.
- (b) There is no hyperbolic base factor carrying mu with local product structure: the quotient of the dynamics by
  the centre does not exist as a dynamical system.
- (c) The flow is not assumed partially hyperbolic (no dominated splitting).
A non-uniform version for the *linear* centre cocycle is plausible. Centre holonomies along W^{uu} exist on Pesin
blocks, because uu-distances contract at rate e^{-theta|t|} while ||Dg_t|E^c|| = e^{o(|t|)}, so the holonomy
products converge. I expect a Ledrappier/Avila–Viana argument would give su-invariance of projective centre measures
(not checked). But that is information about Dg on E^c, not about the bracket set E of Proposition B, and I see no
way to pass from one to the other. **So the dichotomy cannot currently be established through the invariance
principle.** The missing property is that the measure-level centre disintegration be holonomy invariant. Even
granting it, a further step is needed: holonomy invariance must produce positive relative measure of bracket
closing (Proposition B's hypothesis). That step uses product structure of the base, which is absent in general.

## 5. Measured form of Theorem G and what it shows about the twisting branch (proof sketched)

**Proposition G_mu (sketch; same proof as Theorem G).** Assume GH and the setting of Section 3. Let psi be a bounded
nonzero function on K_l ∩ U. Then it is impossible that both:
- for m-a.e. strong-stable plaque A (atoms of the partition of K_l ∩ U into sets W^{ss}_loc(z) ∩ K_l ∩ U, which is
  a measurable partition after shrinking U; cited standard), ∫_A psi e^{beta^s} dm_A = 0; and
- for m-a.e. strong-unstable plaque B, ∫_B psi e^{beta^u} dm_B = 0.
Here beta^s(z) = lim_{t->+inf} (J_t(z) - J_t(a_A)) and beta^u(z) = lim_{t->-inf} (J_t(z) - J_t(b_B)) for measurably
chosen plaque representatives.

*Sketch.* For S = psi m, split S(e^{J_t} phi ∘ g_t) over the A-plaques for t >= 0 and over the B-plaques for
t <= 0. Expand as in Theorem G (R7-a): the leading terms vanish by the balance conditions, and the errors are
<= C e^{-(theta - eta)|t|} ||psi||_inf ||phi||_{C^1}, uniformly by [PB]. Theorem J then gives S = 0.

In the unweighted case, nonzero balanced psi exist iff the image of m under z -> (A(z), B(z)) is *not an extreme
point* of the set of couplings of its two marginals. This is the Douglas (1964) / Lindenstrauss (1965) criterion,
cited from memory: a coupling is extreme iff L^1(first marginal) + L^1(second marginal) is dense in L^1 of the
coupling. So under GH all such local couplings are (weighted-)extreme. In the hyperbolic or rigid case this fails,
consistently with Section 3. In the twisting case the incidence structure of A- and B-plaques looks like a forest.
Couplings carried by acyclic supports are extreme (Beneš–Štěpán 1987, cited from memory; and I recall Losert (1982)
constructed extreme couplings with non-atomic conditionals). So **no measure-theoretic argument confined to one box
can contradict the twisting branch**: dynamics (long su-paths, recurrence) must enter.

## 6. The exact missing property

By Proposition B and Lemma 1, (PE-NH) with mu(d) = 0 would follow from:

**(TW)** Let mu be ergodic, non-hyperbolic, with h_mu(g_1) > 0 and mu(d) = 0, under GH. Suppose that for every
good box and every admissible slicing zeta the bracket set E has relative measure 0. Then there are finitely many
good orbits whose weak su-graph (R7-f Remark (5)) has a component with two independent cycles. Such orbits would
come from long, global su-paths that close modulo the flow.

I could not prove (TW).
- The closing condition has codimension c - 1 >= 1 in the genuine centre, and the Frobenius bracket form
  omega: E^u x E^s -> E^c_0 (R7-f §3(a)) prevents local closing whenever omega != 0.
- GH has so far been used only through L1/F1/F2, Theorem J and its consequences, and Lemmas D/B3/B4. None of these
  says anything about intersections of Pesin leaves.
- The one place GH might supply (TW) is global: Lemma D (Patterson equidistribution of weighted orbits to nu) and
  Corollary D1 (supp mu = M) give recurrence of leaves everywhere. But turning recurrence into exact closing again
  needs c - 1 real conditions, with no transversality mechanism for measurable leaves.
So whether GH can supply (TW) remains open; I see no route.

Also outside this attempt: the cases mu(d) <= -chi^+_min (or >= |chi^-_max|) of (PE-NH). There forward (resp.
backward) classes are exempt, but the other side needs cancellation faster than |lambda| >= chi_min. First-order
brackets (Proposition B) give only rate theta < chi_min, so Proposition B does not apply. Proposition N of R7-c
covers part of this; the rest needs higher-order cancellation (normal forms), which is unchecked.

## 7. What is proved, what is not

- **Proved:** Lemma 1. Proposition B (modulo the cited Pesin block facts [PB] and Theorem G of R7-f), including the
  relative form and the horseshoe-free reproof of Theorem 5.1 for hyperbolic mu with mu(d) = 0 (modulo the cited
  local product structure of Pesin plaques).
- **Sketched:** Proposition G_mu and its extremality interpretation (Douglas–Lindenstrauss, Beneš–Štěpán, Losert,
  all cited from memory).
- **Not established:** the invariance-principle dichotomy. No cited theorem applies, because of hypotheses (a)–(c)
  of Section 4.
- **Open:** (TW); hence (PE-NH) and the problem in dimension >= 4. Also the large-|lambda| non-hyperbolic cases not
  covered by Proposition N.

=== END OF ANSWER round8_q7 ===
