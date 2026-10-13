# Answer to round5_q1: Statement (Lambda)

## Status and plan
I first tried to prove (Lambda), then looked at what it implies. Outcome:

- **(Lambda) is NOT proved, and neither is zero entropy.** No counterexample was found either.
- **Proposition 1 (proved).** Under GH with dim M >= 2, (Lambda) implies four things: mu(div_nu X) = 0 for every invariant probability mu; X has no zeros; X has no periodic orbits; and the flow is minimal. So (Lambda) contains "GH implies minimality and no zeros", which is a large part of the Greenfield–Wallach conjecture. Zero entropy does not visibly imply any of these. My judgment is that (Lambda) is a strictly harder target than the problem.
- **Lemma 2 (proved; a new GH consequence).** This is a resolvent/correlation lemma: under GH, a smooth f whose correlations against smooth densities are improperly integrable in forward time is minus a smooth coboundary.
- **Corollary 3 (proved).** It applies Lemma 2: GH flows (dim >= 2) whose pushed-forward smooth densities converge at an integrable rate are uniquely ergodic and minimal. In particular such flows have no periodic orbits or zeros.
- The last section records where each attempted mechanism stops.

Conventions are those of the brief. nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (log of the nu-Jacobian of g_t at x). For smooth u and a smooth density sigma, int (Xu) sigma = - int u L_X sigma. Distributions u act on smooth densities, and <Xu, sigma> := -<u, L_X sigma>.

## 0. Step 2 of the chain is correct
- For a Lipschitz self-map f of a compact n-dimensional Riemannian manifold, h_top(f) <= n max(0, log Lip f). This is classical (Kushnirenko/Ito; cited from memory).
- For a flow, h_top(g_T) = |T| h_top(g_1) (Abramov-type formula for topological entropy; cited).

Together these give h_top(g_1) <= (n/T) log^+ max ||Dg_T||, which tends to n max(0, lambda*) as T -> infinity. So (Lambda) would suffice. The difficulty is that (Lambda) is much stronger than needed (Section 1).

## 1. Proposition 1: what (Lambda) implies under GH (proved)

**Proposition 1.** Assume GH and dim M >= 2. Suppose (Lambda) holds for X. Then:
- (a) J_t(x)/t -> 0 uniformly in x as |t| -> infinity, and mu(d) = 0 for every invariant probability mu.
- (b) X has no zeros.
- (c) X has no periodic orbits.
- (d) Every ergodic invariant probability has support M, and the flow is minimal.

*Proof.* By (O4), -X is GH, so (Lambda) applies to -X as well. Write a(t) = max_y ||Dg_t(y)|| and b(t) = max_y ||Dg_{-t}(y)||. Both are e^{o(t)} as t -> +infinity.

(a) The nu-Jacobian e^{J_t(x)} equals |det Dg_t(x)| (determinant with respect to the Riemannian volume) times a ratio of smooth positive densities at x and g_t x. That ratio is bounded above and below by constants. For an invertible linear map A of n-dimensional Euclidean spaces,
||A^{-1}||^{-n} <= |det A| <= ||A||^n.
For t > 0, Dg_t(x)^{-1} = Dg_{-t}(g_t x), so ||Dg_t(x)^{-1}|| <= b(t). Hence |J_t(x)| <= n log max(a(t), b(t)) + C = o(t) uniformly in x. The case t < 0 follows by symmetry.

For an invariant probability mu, int J_t dmu = int_0^t mu(d o g_s) ds = t mu(d). So mu(d) = (1/t) int J_t dmu -> 0, and mu(d) = 0.

(b) If X(p) = 0, then delta_p is invariant, so by (a) d(p) = 0. This contradicts P1.

(c) If gamma is a periodic orbit of period T, the normalised orbit measure is invariant. By (a), int_0^T d(gamma(t)) dt = 0. This contradicts Observation P (dim >= 2).

(d) Let mu be ergodic. Take x in supp mu that is Birkhoff-generic for d in both time directions; mu-a.e. point qualifies. Then J_t(x)/t -> mu(d) = 0 as t -> +-infinity, so Lemma D applies.
- The measures T_s are carried by the closure of the orbit of x. That closure is contained in supp mu, a closed invariant set.
- Weak* limits of measures supported in a closed set stay supported in it. The limit nu/nu(M) has full support, so supp mu = M.
- Every orbit closure carries an ergodic invariant probability, whose support is M. So every orbit closure is M, and the flow is minimal. ∎

**Consequence for the chain.** To prove (Lambda) one must in particular prove, from GH alone, that GH vector fields have no zeros and are minimal. These are central unsolved points of the whole program (compare the remark after Lemma H: zeros are not excluded by any known argument).

Zero topological entropy implies none of (a)–(d). For example, north–south-type flows have zero entropy, zeros, and mu(d) != 0. So (Lambda) is strictly harder than the problem. A proof of the problem should not route through (Lambda) unless it also proves minimality.

## 2. Lemma 2: resolvent/correlation lemma (proved)

**Lemma 2.** Assume GH. Let f be in C^infinity(M). Suppose that for every smooth density sigma the improper integral
U(sigma) := lim_{R->infinity} int_0^R < f o g_t , sigma > dt
exists, where <h, sigma> = int h sigma. Then there is u in C^infinity with Xu = -f and U(sigma) = int u sigma. Consequently:
- mu(f) = 0 for every invariant probability mu;
- sup_{x,t} |int_0^t f(g_s x) ds| <= 2||u||_inf.

*Proof.*
1. **U is a distribution.** U_R(sigma) = int_0^R <f o g_t, sigma> dt satisfies |U_R(sigma)| <= R ||f||_inf ||sigma||_{L^1}, so each U_R is a continuous linear functional on the Fréchet space of smooth densities. By hypothesis U_R converges pointwise to U. By Banach–Steinhaus (a pointwise limit of continuous linear functionals on a Fréchet space is continuous), U is continuous, i.e. a distribution u.
2. **The correlation tends to 0.** Put a(t) = <f o g_t, sigma>. Since d/dt (f o g_t) = X(f o g_t),
a(R) - a(0) = int_0^R int X(f o g_t) sigma dt = - int_0^R <f o g_t, L_X sigma> dt = -U_R(L_X sigma).
The right side converges to -U(L_X sigma), because L_X sigma is a smooth density. So a(R) has a limit A. Since int_0^R a(t) dt converges, A = 0.
3. **Xu = -f.** Letting R -> infinity in step 2 gives U(L_X sigma) = a(0) = <f, sigma>. Hence <Xu, sigma> = -<u, L_X sigma> = -<f, sigma> for every sigma, i.e. Xu = -f.
4. **Consequences.** By GH, u is smooth. For an invariant probability mu, mu(Xu) = d/dt mu(u o g_t)|_{t=0} = 0, so mu(f) = 0. Finally, int_0^t f(g_s x) ds = u(x) - u(g_t x). ∎

**Corollary 3.** Assume GH and dim M >= 2. Suppose there is a Borel probability m such that, for every smooth phi and every smooth density sigma, the improper integral
int_0^infinity ( <phi o g_t, sigma> - m(phi) sigma(M) ) dt
converges. (For example, int |...| dt < infinity, as with exponential or integrable decay of correlations of pushed-forward smooth densities toward a limit measure m.) Then:
- the flow is uniquely ergodic with invariant measure m;
- m(d) = 0, and the flow is minimal;
- in particular it has no zeros and no periodic orbits.

The same conclusion holds with t -> -infinity, by applying it to -X.

*Proof.*
1. Apply Lemma 2 to f = phi - m(phi). The hypothesis holds because <f o g_t, sigma> = <phi o g_t, sigma> - m(phi) sigma(M). So mu(phi) = m(phi) for every invariant probability mu and every smooth phi, hence mu = m.
2. Invariant probabilities exist, so the flow is uniquely ergodic with invariant measure m.
3. Lemma E (established background) then gives m(d) = 0, supp m = M and minimality. A zero would give the invariant measure delta_p, and a periodic orbit (dim >= 2) its orbit measure; either would differ from the fully supported m. ∎

What this excludes: every GH flow with a periodic orbit or zero, together with integrable-rate convergence of smooth densities. For example, it excludes dissipative or conservative Anosov flows that are exponentially mixing for smooth densities; this uses the GH hypothesis only, with no volume needed. It is a partial result for a subclass and does NOT answer the problem. General positive-entropy flows need not have any decay of correlations.

## 3. Where the attempts stop (honest record)

1. **Krein–Rutman eigen-objects.** Let lambda* > 0. Consider the positive operators P_t Psi(v) = |Dg_t v|^2 Psi(g^_t v) on C(SM). Using the resolvent and normalised maximisers, one obtains a probability S on SM with P_t^* S = e^{2 lambda* t} S. The squared weight avoids the v -> -v cancellation.
   - Then Q(B) = int B(v,v) dS(v) is a nonzero positive symmetric-2-tensor current with Q(g_t^* B) = e^{2 lambda* t} Q(B).
   - Any passage from Q to a distribution u on M with Xu smooth requires either an equivariant linear functional of functions or closedness. Bilinear pairings only give an eigen-distribution of X ⊕ X on M x M, and the product field is never GH (it has invariant distributions supported on the diagonal), so no contradiction follows.
   - With the 1-current version C_S, the sign cancellation (N) remains unresolved.
2. **(E1)** (no real eigen-distributions X W = kappa W, kappa != 0) is not accessible by local means:
   - Multiplying a measure eigen-distribution supported on a compact invariant K by a smooth psi requires psi o g_t = e^{-kappa t} psi on K, which forces psi = 0 on K.
   - Jet distributions along periodic orbits or at zeros give only non-resonance conditions (Lemma H type).
   - Moreover (E1) implies mu(d) = 0 for all mu (tilted conformal measures), hence, by Proposition 1's argument, no zeros or periodic orbits and minimality. So it is equally hard.
3. **Dual and transfer arguments** (O1, pushing forward the solutions S_{x,y}) are conjugation-invariant reformulations. Since X commutes with g_t, the growth of g_t on D'/I equals its growth on (C^infinity_0)'. They yield no new inequality.
4. **Horseshoe route** (dim 3, where positive entropy gives a hyperbolic measure and hence horseshoes, by Lian–Young; cited). By Lemma D/Prop 2.2, all invariant measures on the horseshoe Lambda have mu(d) of one strict sign, bounded away from 0. This is consistent with Lemma C and with B3, because W^s(Lambda) is volume-null for non-attractors. A contradiction would need global information on orbits leaving a neighbourhood of Lambda, which GH does not visibly give.

## Summary of what is proved / open
- **Proved:** Proposition 1 ((Lambda) implies mu(div X) = 0 for all mu, no zeros, no periodic orbits, minimality); Lemma 2; Corollary 3; the validity of chain step 2 (cited classical bounds).
- **Not proved (open here):**
  - (Lambda) itself;
  - zero topological entropy for GH flows in general (only dim <= 2 is automatic, since flows on surfaces have zero entropy, a cited theorem of Young);
  - (E1);
  - GH implies no zeros;
  - GH implies minimality / unique ergodicity;
  - (V).
- **Recommendation:** abandon (Lambda) as the target. By Proposition 1 it is at least as hard as "GH implies no zeros + minimality".

=== END OF ANSWER round5_q1 ===
