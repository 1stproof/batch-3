# round13_q5 answer

## 0. Status (summary)

(PE0) is NOT proved here. What this answer establishes about the conformal-measure route:

- Sections 1-2 (proved): basic structure of nu-conformal finite measures. We may assume sigma >= 0 and sigma singular to nu. Sigma splits into a conservative part and a dissipative part, and both parts are again conformal.
- Section 3 (proved): the dissipative part is exactly Lemma C. It is nonzero iff some orbit has int_R e^{J_t(x)} dt < infinity. Points that are Birkhoff-generic for the hypothetical mu never qualify.
- Section 4 (proved): the absolutely-continuous-to-mu case. A conformal sigma << m, with m invariant and ergodic, exists iff J is a measurable coboundary with e^w in L^1(m). Under GH this happens iff m << nu (and then m ~ nu). This is a new necessary condition on the hypothetical mu of (PE0). It is not a contradiction.
- Section 5 (proved modulo cited thermodynamic formalism): Lemma S / Prop D of R12-d add nothing beyond Lemma C, Cor D1 and Section 4.
  - In the strict case (alpha < 0 < beta), the Lemma S measure is totally dissipative.
  - In the balanced case it is e^w times an invariant measure.
  - Prop D follows from Cor D1 alone.
- Section 6 (proved): in the volume case the route cannot be completed with a measure. Any GH-free version of it would prove that smooth volume-preserving uniquely ergodic flows have zero entropy, (UE-0), which I cannot settle.
- Section 7: exactly which suggested step fails, and the open questions.

## 1. Conventions and the transfer action on measures

As in the brief:
- nu is a smooth positive density and d = div_nu X.
- J_t(x) = int_0^t d(g_s x) ds, with the cocycle rule J_{t+s}(x) = J_s(x) + J_t(g_s x).
- Gamma_t phi := e^{J_t} (phi o g_t) and P phi := X phi + d phi.
- Gamma_{t+s} = Gamma_t Gamma_s = Gamma_s Gamma_t, and d/dt Gamma_t phi = Gamma_t P phi = P Gamma_t phi (R12-b notation).

For a finite signed Borel measure sigma put
 (Lambda_t sigma)(B) := int 1_B(g_t x) e^{J_t(x)} dsigma(x),
i.e. Lambda_t sigma = (g_t)_*(e^{J_t} sigma). Then:
- Lambda_t is linear, positive and invertible, with inverse Lambda_{-t}, by the cocycle rule.
- Lambda_t preserves mutual singularity, since g_t is a bijection and e^{J_t} > 0.
- Lambda_t nu = nu, by the change of variables formula (e^{J_t} is the nu-Jacobian of g_t).

**Lemma 1.1 (equivalent forms of conformality; proved).** For a finite signed Borel measure sigma, the following are equivalent:
(a) sigma(P phi) = 0 for every smooth phi (i.e. L_X sigma = d sigma; by Lemma A of R12-d this is the relation that GH restricts to sigma = c nu);
(b) sigma(Gamma_t phi) = sigma(phi) for all t and all bounded Borel phi;
(c) Lambda_t sigma = sigma for all t, i.e. sigma(g_t A) = int_A e^{J_t} dsigma for every Borel A (put A = g_{-t}B).
Such sigma are called *nu-conformal*.

*Proof.*
- (a) => (b): Let phi be smooth and F(t) := sigma(Gamma_t phi). The map t -> Gamma_t phi is C^1 into C^0 uniformly, so F'(t) = sigma(P Gamma_t phi). This vanishes by (a) applied to the smooth function Gamma_t phi. So F(t) = F(0).
  - Pass to continuous phi by uniform approximation, since Gamma_t is bounded on C^0.
  - Pass to bounded Borel phi by the monotone class theorem.
- (b) => (c): Take phi = 1_B. Then sigma(Gamma_t 1_B) = (Lambda_t sigma)(B).
- (c) => (a): (b) holds for smooth phi. Differentiate at t = 0 by dominated convergence: (Gamma_t phi - phi)/t -> P phi uniformly. ∎

**Lemma 1.2 (positive and singular parts; proved).** Let sigma be nu-conformal.
(i) The Jordan parts sigma^+, sigma^- and |sigma| are nu-conformal.
(ii) Write sigma = sigma_a + sigma_s for the Lebesgue decomposition with respect to nu (sigma_a << nu, sigma_s ⊥ nu). Both parts are nu-conformal.
(iii) sigma_a = f nu with f o g_t = f nu-a.e. for every t. So if nu is ergodic for the flow, sigma_a = c nu. Under GH, nu is ergodic (R7-d Lemma D), and in fact sigma = c nu outright (Lemma A).
(iv) If A is a flow-invariant Borel set, then 1_A sigma is nu-conformal.

*Proof.*
(i) Lambda_t sigma = Lambda_t sigma^+ - Lambda_t sigma^-, with mutually singular positive parts. By uniqueness of the Jordan decomposition, Lambda_t sigma^± = sigma^±.
(ii) Lambda_t preserves "<< nu", because nu(B) = 0 implies nu(g_{-t}B) = 0. It also preserves "⊥ nu": if sigma_s is carried by N with nu(N) = 0, then Lambda_t sigma_s is carried by g_t N, which is nu-null. Apply uniqueness of the Lebesgue decomposition.
(iii) Lambda_t(f nu) = (f o g_{-t}) nu. Indeed, for bounded Borel psi, int psi o g_t e^{J_t} f dnu = int psi (f o g_{-t}) dnu: this is Lambda_t nu = nu applied to the density psi (f o g_{-t}).
(iv) Lambda_t(1_A sigma) = 1_{g_t A} Lambda_t sigma = 1_A sigma. ∎

So for the route we may assume, without loss of generality, that **sigma is a positive finite measure with sigma ⊥ nu**. A signed measure gains nothing.

## 2. Hopf decomposition of a conformal measure

**Cited (Hopf decomposition; e.g. Aaronson, *An introduction to infinite ergodic theory*, §1.3, from memory).** Let T be an invertible nonsingular transformation of a sigma-finite measure space (Y, sigma), and let T^ be the transfer operator, the dual of f -> f o T, so that T^^n 1 = d(sigma o T^{-n})/dsigma. Then Y = C ⊔ D (mod sigma), with C, D T-invariant, where:
- T is conservative on C and D is a union of wandering sets;
- C = {sum_{n >= 0} T^^n 1 = infinity} mod sigma.
The decomposition is the same for T and T^{-1}, since wandering sets for T are wandering for T^{-1}.

**Proposition 2.1 (proved modulo the cited Hopf decomposition).** Let sigma be a finite positive nu-conformal measure. Put
 C := {x : sum_{n >= 0} e^{J_n(x)} = infinity  and  sum_{n >= 0} e^{J_{-n}(x)} = infinity}.
(a) C is exactly flow-invariant, and sigma|_C and sigma|_{M \ C} are nu-conformal.
(b) For sigma-a.e. x in M \ C, int_R e^{J_t(x)} dt < infinity.
(c) sigma|_C is conservative for g_1, and sigma|_{M \ C} is totally dissipative.

*Proof.*
- By Lemma 1.1(c), sigma o g_n has density e^{J_n} with respect to sigma. Apply the Hopf decomposition to T = g_{-1}, for which T^{-n} = g_n and T^^n 1 = e^{J_n}. Its conservative part is C_+ := {sum_n e^{J_n} = infinity}.
- Apply it to T = g_1 to get C_- := {sum_n e^{J_{-n}} = infinity}.
- The two decompositions coincide mod sigma, so C = C_+ = C_- mod sigma. This gives (c), and also (b): off C both sums converge, and |J_{n+s} - J_n| <= ||d||_inf for s in [0,1], so the integral is finite.
- (a): J_n(g_s x) = J_{n+s}(x) - J_s(x), and |J_{n+s} - J_n| <= |s| ||d||_inf. So each defining sum diverges at g_s x iff it diverges at x. Then apply Lemma 1.2(iv). ∎

**Consequence.** Every nonzero positive nu-conformal sigma ⊥ nu, which is what the route asks for, gives one of two objects:
- **(R-i)** a point x with int_R e^{J_t(x)} dt < infinity (if sigma(M \ C) > 0); or
- **(R-c)** a nonzero conservative nu-conformal measure singular to nu (if sigma(C) > 0).
Conversely, (R-i) gives a nu-conformal measure on a single orbit, by the construction in Lemma C of the brief (GH-free). Under GH, (R-i) is impossible by Lemma C itself.

## 3. The dissipative alternative (R-i) and the hypothetical mu

**Cited (Atkinson 1976, recurrence of cocycles, from memory).** Let T be an ergodic invertible transformation preserving a probability m, and let f be in L^1(m) with int f dm = 0. Then for m-a.e. x, liminf_{n -> inf} |S_n f(x)| = 0, where S_n f = sum_{k<n} f o T^k. The same holds for T^{-1}.

**Proposition 3.1 (proved modulo Atkinson).** Let mu be g_1-invariant and ergodic with int J_1 dmu = 0. For mu-a.e. x,
 sum_{n >= 0} e^{J_n(x)} = infinity  and  sum_{n >= 0} e^{J_{-n}(x)} = infinity.
So a sigma as in Proposition 2.1 has its dissipative part carried by a mu-null set, and in fact by a set that is null for every such mu. No point Birkhoff-generic for the (PE0)-measure lies on an (R-i) orbit.

*Proof.*
- J_n(x) = S_n J_1(x) for the map g_1, by the cocycle rule. Atkinson gives |J_n(x)| < 1 for infinitely many n, so the first sum diverges.
- For the second sum: J_{-n}(x) = -sum_{k=1}^{n} J_1(g_{-k}x), which is a Birkhoff sum of the mean-zero function -J_1 o g_{-1} for g_{-1}. Apply Atkinson to g_{-1}. ∎

*Remark.* In the volume case (d = 0 for the invariant density), J = 0 and (R-i) never occurs, for any flow. So (R-i) can contribute only outside the volume case, and only through non-generic points. Two such sources were considered earlier: su-intersections, which the centre direction prevents (Block R7-a "where it stops"), and asymptotic points of periodic orbits (Lemma K, Theorem B). Both need hyperbolic structure that the (PE0)-measure does not provide.

## 4. Conformal measures absolutely continuous with respect to an invariant measure

**Proposition 4.1 (no GH; proved).** Let m be a flow-invariant, flow-ergodic Borel probability, and let sigma != 0 be a finite positive measure with sigma << m. Then sigma is nu-conformal iff sigma = c e^w m, where w is a measurable function with
 J_t = w o g_t - w  m-a.e., for every t,  and  int e^w dm < infinity.
In particular, nu-conformal measures << m exist iff J is such an "L^1-exponential" measurable coboundary over m. In that case they are unique up to scaling, since w is unique up to an additive constant by ergodicity.

*Proof.*
- Write sigma = F m with F >= 0 in L^1(m). As in Lemma 1.2(iii), Lambda_t(F m) = ((e^{J_t} F) o g_{-t}) m, using invariance of m.
- So conformality means e^{J_t} F = F o g_t m-a.e. for each t.
- Then {F > 0} is invariant mod m, and by ergodicity it is conull. Put w := log F; this gives the coboundary relation, and e^w = F is in L^1.
- Conversely, if w is as stated, then F := e^w satisfies e^{J_t} F = F o g_t, so F m is conformal. ∎

**Theorem 4.2 (GH; proved).** Assume GH. Let mu be g_1-invariant and g_1-ergodic, and let mu-bar = int_0^1 (g_s)_* mu ds. Suppose that
 J_1 = w o g_1 - w  mu-a.e., with w measurable and int e^w dmu < infinity.
Then mu-bar is equivalent to nu (mu-bar << nu and nu << mu-bar). Equivalently, for a (PE0)-measure with mu-bar ⊥ nu, J_1 is NOT an L^1-exponential measurable coboundary over (g_1, mu).
Conversely, if mu-bar = h nu, then J_t = w o g_t - w with w = -log h (on {h > 0}, which is mu-bar-conull), and int e^w dmu-bar = nu{h > 0} < infinity.

*Proof.*
1. *A g_1-conformal measure.* Put sigma := e^w mu, a finite positive nonzero measure. For Borel B, sigma(g_1 B) = int 1_B o g_1^{-1} e^w dmu = int 1_B e^{w o g_1} dmu = int_B e^{J_1} dsigma, using invariance of mu. Applied to psi = phi o g_1, this gives sigma(Gamma_1 phi) = sigma(phi) for bounded Borel phi.
2. *Flow average.* Define sigma-bar(phi) := int_0^1 sigma(Gamma_s phi) ds, a finite positive measure with sigma-bar(1) >= e^{-||d||_inf} sigma(M) > 0. For smooth phi, d/ds sigma(Gamma_s phi) = sigma(Gamma_s P phi), so
 sigma-bar(P phi) = sigma(Gamma_1 phi) - sigma(phi) = 0.
 By Lemma A of R12-d (GH), sigma-bar = c nu with c > 0.
3. *sigma-bar << mu-bar.* If mu-bar(B) = 0, then mu(g_s^{-1} B) = 0 for a.e. s in [0,1], hence sigma(g_s^{-1} B) = 0 for a.e. s, hence sigma-bar(B) = int_0^1 int e^{J_s} 1_B o g_s dsigma ds = 0. So nu << mu-bar.
4. *Dichotomy.* mu-bar is flow-ergodic (R12-h Lemma 1). Its Lebesgue decomposition with respect to nu has two flow-invariant parts, because the flow preserves nu-null sets. An ergodic measure is extreme, so mu-bar << nu or mu-bar ⊥ nu. The second contradicts nu << mu-bar with nu != 0. So mu-bar << nu, and with step 3, mu-bar ~ nu.
5. *Converse.* Invariance of h nu gives h o g_t e^{J_t} = h nu-a.e., by Lemma 1.2(iii) with the roles reversed: (h nu) o g_t has density (h o g_t) e^{J_t}. So J_t = log h - log h o g_t = w o g_t - w, and int e^w dmu-bar = int_{h>0} h^{-1} h dnu. ∎

**What this gives for (PE0).** Under GH, the hypothetical mu either has mu-bar ~ nu, or J_1 is not an L^1-exponential measurable coboundary over mu.
- In the first case mu-bar = h nu with h > 0 a.e. Entry S8, as quoted in the brief (h^{-eps} in L^1 for some eps > 0 suffices), would make it a smooth volume. Without that integrability I cannot reduce to the volume case: X h = -d h has a non-smooth right-hand side, and GH says nothing about it.
- The second case is a genuine necessary condition, but it is not a contradiction. In general J_1 is not a coboundary, e.g. when J_1 has positive asymptotic variance. So **the route cannot take sigma << mu-bar**. It must produce sigma ⊥ mu-bar as well as sigma ⊥ nu.

## 5. Lemma S / Proposition D of R12-d are instances of Lemma C, Cor D1 and Section 4

Cited (thermodynamic formalism, from memory; Ruelle, Bowen, Parry-Pollicott): Let (Sigma, T) be an irreducible two-sided SFT and Phi Hölder.
- (T1) p(s) := P(s Phi) is C^1 (indeed real-analytic), with p'(s) = int Phi dm_s, where m_s is the unique equilibrium state of s Phi. m_s is ergodic and has full support in Sigma.
- (T2) If Phi is not cohomologous to a constant, p is strictly convex.
- (T3) Ruelle-Perron-Frobenius: for Hölder psi on a one-sided irreducible SFT, the eigenmeasure of L_psi^* is equivalent to the projection of the two-sided equilibrium state of the corresponding two-sided potential.
- (T4) Livsic: if every periodic orbit sum of Phi vanishes, then Phi = w o T - w with w Hölder.

**Proposition 5.1 (proved modulo T1-T4).** In the situation of Lemma S of R12-d:
(a) If alpha < 0 < beta, the measure sigma_0 constructed there is carried by points x such that, along the suspension, J_t(x) <= C_x - c|t| for all real t, for some c > 0. Hence the suspended measure sigma of Prop D is totally dissipative (Proposition 2.1), and sigma-a.e. orbit is an (R-i) orbit.
(b) If alpha = beta = 0, then sigma_0 = (const) e^{w} m for a T-invariant probability m and a Hölder w. This is the situation of Proposition 4.1.
(c) Proposition D follows from Cor D1 alone (plus T1), with no conformal-measure construction.

*Proof.*
(a)
- Here alpha < 0 < beta, so Phi is not cohomologous to a constant, and p is strictly convex by (T2).
- In Lemma S(b), G = s_0 Phi with p(s_0 + 1) = p(s_0). Strict convexity gives p'(s_0) < p(s_0+1) - p(s_0) = 0 < p'(s_0 + 1).
- sigma_0 = nu^- ⊗ nu^+, where nu^+ is the eigenmeasure for (a one-sided version of) G and nu^- the one for G + Phi on the past side. By (T3), nu^+ is equivalent to the future projection of m_{s_0}, and nu^- to the past projection of m_{s_0+1}.
- Phi is Hölder, so Phi(T^k z) depends on the past coordinates of z only up to an error O(theta^k) for k >= 0, and symmetrically for k <= 0. Hence for sigma_0-a.e. z:
  - (1/n) S_n Phi(z) -> m_{s_0}(Phi) = p'(s_0) < 0 as n -> +inf;
  - (1/n) sum_{k=1}^n Phi(T^{-k} z) -> m_{s_0+1}(Phi) = p'(s_0 + 1) > 0.
- Along the suspension with bounded roof, the first limit gives J_t <= C - ct for t >= 0. For t -> -inf, J_t is minus the sum of Phi over the past returns, so J_t <= C - c|t|.
(b) Lemma S's hypothesis alpha = beta = 0 gives int Phi dm = 0 for all invariant m, in particular for all periodic measures. By (T4), Phi = w o T - w. Then, by Lemma S(a) read backwards, e^{-w} sigma_0 satisfies (∗) with Phi = 0, i.e. it is T-invariant.
(c)
- Strict case alpha < 0 < beta: by (T1)-(T2), p' increases strictly and continuously from alpha to beta, so p'(s*) = 0 for some s*. Lift m_{s*} to the suspension and push it to K = pi(Sigma_r). The result m-bar is an ergodic flow-invariant probability with m-bar(d) = m_{s*}(Phi)/int r dm_{s*} = 0 and supp m-bar ⊂ K ≠ M. This contradicts Cor D1.
- Balanced case alpha = beta = 0: any ergodic invariant measure of the coding already contradicts Cor D1. ∎

**Moral.** The thermodynamic "pressure equation" device does not create new conformal measures for the purposes of GH. In the strict case it produces a family of Lemma-C orbits (dissipative). In the balanced case it produces e^w times an invariant measure (Section 4). Prop D's conclusion is already contained in Cor D1. So the "centre analogue of Lemma S" asked for in (Q3) must produce something of type (R-c) that is NOT of the form of Section 4. That is a genuinely new kind of object, not an extension of Lemma S.

## 6. The volume case: the route cannot be completed with a measure

**Proposition 6.1 (proved).** Assume GH and that X preserves a smooth positive density. Choose nu to be that density, so d = 0, J = 0, and "nu-conformal" means "flow-invariant". Then:
(a) every finite signed nu-conformal measure is c nu;
(b) the hypothetical (PE0)-measure has mu-bar = nu/nu(M);
(c) any sigma satisfying the route's requirements (L_X sigma = d sigma, sigma != c nu) must be a distribution that is not a measure, i.e. of positive order.

*Proof.*
- (O2) of the background: under GH with a smooth invariant volume, the flow is uniquely ergodic with invariant probability nu/nu(M).
- (a): by Lemma 1.2(i), sigma^+ and sigma^- are invariant positive measures, hence multiples of nu.
- (b): mu-bar is a flow-invariant probability, hence equal to nu/nu(M).
- (c) is (a) restated. ∎

**Corollary 6.2 (what a GH-free version of the route would prove).** Suppose steps (a)-(b) of the route were carried out GH-free. That is, from any smooth flow and any g_1-ergodic mu with h_mu(g_1) > 0 and int J_1 dmu = 0, together with the GH-free constraints listed in the brief (non-hyperbolic, full support of mu-bar), one could construct a nonzero positive nu-conformal measure singular to nu. Then the following statement would hold:
- **(UE-0)** No C^inf volume-preserving flow on a compact manifold that is uniquely ergodic has positive topological entropy.

*Proof.* Let such a flow be uniquely ergodic with h_top > 0. Its only invariant probability is the normalized volume nu-hat, so nu-hat has positive entropy (variational principle).
- Take mu a g_1-ergodic component of nu-hat with h_mu(g_1) = h_{nu-hat}(g_1) > 0 (R12-h Lemma 1, converse part). Then int J_1 dmu = 0, since J = 0.
- mu-bar = nu-hat has full support.
- nu-hat is non-hyperbolic: otherwise the Katok/Lian-Young horseshoe theorem gives a periodic orbit, whose invariant measure differs from nu-hat.
- The construction would give an invariant probability singular to nu-hat, contradicting unique ergodicity. ∎

Similarly, a GH-free construction of a non-measure invariant distribution would prove (DUE-0) of R7-b. That was already noted there.

I do not know whether (UE-0) is true. Constraints on a counterexample:
- it must be non-hyperbolic and minimal;
- it can have no horseshoes at all (a horseshoe carries invariant measures other than nu-hat);
- I recall Herman's construction of a minimal smooth diffeomorphism with positive topological entropy, but I do not reliably recall whether it is uniquely ergodic, so I do not use it.

In any case the route "build a conformal MEASURE from mu" is, in the volume case, at least as hard as (UE-0). To avoid this, the construction itself (not only the final appeal to Lemma A) must use the GH hypothesis beyond the derived properties listed above, or it must produce a distribution of positive order. The latter is an object for which no Pesin/thermodynamic template exists.

## 7. The suggested steps: where exactly the route fails

- **Step (a)** (leafwise measures on Pesin unstable plaques with Jacobian e^{h t}): available. These are the Ledrappier-Young conditionals.
- **Step (b)** (solve a pressure equation for the transverse factor). This is the step that fails, for two separate reasons.
  - (b1) With a centre direction there is no space carrying the "transverse factor" on which g_1 acts. In Lemma S the transverse factor lives on Sigma^- = Sigma/(local unstable sets), on which the one-sided shift acts. In the Pesin setting, the quotient by local unstable plaques xi is standard, but g_1 does not act on it: g_1 maps xi to the coarser g_1 xi. The quotient by global unstable leaves is not a standard Borel space, since the leaves are dense in supp mu-bar = M.
    - A transverse measure on global leaves with Jacobian e^{J - (unstable part)} is exactly a "transverse quasi-invariant measure" of the unstable lamination. In hyperbolic cases it is produced by stable holonomy (local product structure), which is absent here: dim W^s + dim W^u <= n - 2.
  - (b2) Even where the product construction works, it produces nothing new for GH (Section 5). In the strict case the measure is dissipative, i.e. Lemma C. In the balanced case it is e^w times an invariant measure, i.e. Section 4.
    - By Section 4, a balanced-type output for the (PE0)-measure would require J_1 to be an L^1-exponential coboundary over mu (only possible if mu-bar ~ nu).
    - By Proposition 3.1, a strict-type output cannot be carried by mu-generic points.
    - In the volume case (Section 6), both outputs are impossible GH-free, i.e. without first proving (UE-0).
- **Step (c)** ("singular to nu because carried by mu-generic points"). Such a sigma must also be singular to mu-bar (Section 4) and conservative (Proposition 3.1). In the volume case it cannot exist at all as a measure (Proposition 6.1). Lemma S's measure is NOT carried by generic points of a single invariant measure: in the strict case its points are forward-generic for m_{s_0} and backward-generic for m_{s_0+1}, which are different measures. So step (c) has no template.
- **Step (d)** (conclude by Lemma A): fine.
- **The a.c. alternative** ("if mu is not nu-singular, show mu is a smooth volume"). What is proved here: mu-bar = h nu with h > 0 nu-a.e. (Theorem 4.2 and its converse). The smooth-volume conclusion needs h^{-eps} in L^1 (entry S8). I could not obtain that integrability from GH.

## 8. Precise open questions left

- **(O1)** Construct, from a g_1-ergodic mu with h_mu > 0, int J_1 dmu = 0 and mu-bar ⊥ nu, a *conservative* positive nu-conformal measure that is singular to nu and to mu-bar. Equivalently, by Section 2, a sigma ⊥ nu with no (R-i) part. Or show that none exists in general (GH-free).
- **(O2)** Under GH, if mu-bar = h nu for the (PE0)-measure, is h^{-eps} in L^1 (so that S8 applies and mu-bar is a smooth volume)?
- **(O3)** (UE-0): does every C^inf volume-preserving uniquely ergodic flow have zero topological entropy? By Corollary 6.2, any GH-free measure-valued version of the route would prove it. A counterexample would show that the volume case of (PE0) needs GH beyond L1/K0 through the construction itself.
- (Q2) of R12-d (is K0 alone enough?) remains open. Everything in Sections 1-5 uses only K0, via Lemma A and Lemma C.
- (Q3) of R12-d: Remark B' (transverse-jet resonance conditions on periodic orbits) was not attempted here. By Section 5, a "centre analogue of Lemma S" in the sense of a pressure-equation product construction cannot help: it can only produce dissipative or coboundary-type conformal measures.
- **(PE0) itself remains open.**

=== END OF ANSWER round13_q5 ===

