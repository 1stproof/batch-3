# round12_q4 answer

## Plan and status
Target: (PE0), to be refuted or proved. I did not settle it either way. This file gives:
(1) a factor lemma, proved in full: GH passes to smooth submersive factors;
(2) consequences of (1) for a hypothetical counterexample to (PE0), with proofs;
(3) a test of the natural candidate "suspension of (rotation x Anosov)", which has no periodic orbits; (1) rules it out;
(4) a dead end in the volume / cohomology-free case (spectral argument), with the reason it fails.
Everything that rests on the background (Theorem 5.2 of R6-a and the citations it uses) is marked as such.

## 1. Factor lemma (proved)
**Lemma F1.** Let M, N be compact connected manifolds and pi : M -> N a surjective submersion. Let X be a smooth field on M and Y a smooth field on N with d pi (X) = Y o pi. If X is GH, then Y is GH.

*Proof.*
1. Fix a smooth positive density nu_M on M. Fibre integration pi_* maps smooth densities on M to smooth densities on N, and it is continuous. (Locally pi is a projection by the submersion theorem, and fibre integration with a partition of unity preserves smoothness.) Put rho := pi_* nu_M. It is a smooth density, positive because pi is surjective.
2. *Pullback.* For a distribution v on N (a generalised function, paired with densities), define pi^* v by
 <pi^* v, psi nu_M> := <v, pi_*(psi nu_M)>.
 This is continuous from D'(N) to D'(M). For smooth v it gives v o pi (Fubini).
3. *Intertwining.* For smooth v, X(v o pi) = (Yv) o pi by the chain rule. Both maps X o pi^* and pi^* o Y are continuous from D'(N) to D'(M), and C^inf(N) is dense in D'(N). So X(pi^* v) = pi^*(Yv) for every v in D'(N).
4. *Smoothness descends.* Suppose pi^* v = w with w in C^inf(M). Take psi = phi o pi with phi in C^inf(N). Then pi_*((phi o pi) nu_M) = phi rho, so
 <v, phi rho> = int_M w (phi o pi) nu_M = int_N phi pi_*(w nu_M).
 Hence v = pi_*(w nu_M)/rho, which is smooth.
5. Now let v be in D'(N) with Yv = f in C^inf(N). By step 3, X(pi^* v) = f o pi, which is smooth. By GH, pi^* v is smooth, so v is smooth by step 4. ∎

**Corollary F2 (proved, modulo the background).**
Let X be GH on M and pi : M -> N a submersive factor as in F1.
(a) Y is GH. Hence Y satisfies every GH consequence in the background. In particular:
 - Y has no Jacobian-1 periodic orbits;
 - no hyperbolic periodic orbit or zero of Y has a homoclinic point (R6-a, Cor. 4.2);
 - if dim N <= 3, then h_top(Y) = 0 (R6-a, Thm 5.2; this uses Ruelle's inequality and Katok / Lian–Young, as cited there).
(b) So if X were a counterexample to the problem with a submersive factor of dimension <= 3, all of its entropy would have to sit in the fibres. By Bowen's inequality (cited from memory: h(X) <= h(Y) + sup_{q in N} h(g_1, pi^{-1}(q))), we would need sup_q h(g_1, pi^{-1} q) > 0. For the measure mu of (PE0), the Abramov–Rokhlin formula (cited from memory) gives h_mu(g_1) = h_{pi_* mu}(Y_1) + h_mu(g_1 | pi^{-1} B_N). When dim N <= 3 the first term is 0, so the conditional fibre entropy is positive.
(c) Any open set of fields with a positive-entropy GH-violating factor is excluded. Examples:
 - Skew products over (suspensions of) Anosov systems. These have an Anosov factor, which has periodic orbits with homoclinic points, so (a) is violated.
 - More generally, any field with a submersive factor carrying a hyperbolic periodic orbit together with one of its homoclinic points.

## 2. A natural candidate, and why it fails (proved)
**Candidate.** Take A in SL(2,Z) hyperbolic and alpha irrational (Diophantine, say). Let F(theta, x) = (theta + alpha, A x) on T^1 x T^2. Let M = M_F be the mapping torus (dim 4) and X = d/ds its suspension field.
Properties:
- X preserves the smooth volume.
- X has positive entropy: h = log of the spectral radius of A.
- X has no periodic orbits and no zeros, since F^n(theta, x) = (theta, x) would force n alpha in Z. So Observation P, Lemma K and the homoclinic obstructions do not apply directly.
- In dimension 4 the exponents of the volume are (log|ev|, 0, 0, -log|ev|): non-hyperbolic with mu(d) = 0. This is exactly the shape that Corollary 6.3 of R6-a predicts for a dimension-4 counterexample.

So it passes every pointwise test in the brief. Nevertheless it is **not** GH.

*Proof.* The map (theta, x, s) -> (x, s) defines a submersion M_F -> M_A (the mapping torus of A on T^2), and it sends X to the suspension field X_A of A.
- X_A has a periodic orbit gamma (fixed points of A exist, e.g. x = 0).
- X_A preserves volume, so its Poincaré map along gamma has Jacobian 1.
- By Observation P (background), X_A is not GH.
- By Lemma F1, X is not GH. ∎

The same argument kills every skew product (theta, x) -> (theta + alpha, B_theta(x)) whose fibre maps do not depend on theta, and more generally any extension of a non-GH field. Removing periodic orbits by taking a product with an irrational rotation never helps: the factor keeps them. Any counterexample to (PE0) must therefore be "factor-irreducible" in the following sense: every submersive factor is again GH.

## 3. Dead end: spectral approach in the volume (cohomology-free) case
Setting: X preserves omega and is GH. So it is cohomology-free with tame inverse R: for smooth f of mean 0, f = X(Rf) and ||Rf||_{C^k} <= C ||f||_{C^{m_k}} (background).
- For smooth mean-zero f and every j, the Koopman spectral measure satisfies sigma_f((-eps, eps)) <= eps^{2j} ||R^j f||_{L^2}^2. This holds because sigma_f = |xi|^{2j} sigma_{R^j f}.
- Positive entropy gives a Lebesgue spectral component (Rokhlin–Sinai, cited from memory).
- **No contradiction:** density of such f in L^2 controls spectral measures only in total variation, with an error independent of eps. A dense subspace of vectors whose spectral measures vanish to infinite order at 0 exists for Lebesgue spectrum as well.
So size and spectral estimates alone cannot work. This matches Remarks C and D of R9-e.

## 4. Summary
**Proved:**
- Lemma F1: GH descends to submersive factors.
- Corollary F2(a), modulo the background.
- Section 2: the natural candidate with no periodic orbits — a suspension of (irrational rotation x hyperbolic toral automorphism), 4-dimensional, volume preserving, with exponents (chi, 0, 0, -chi) — is not GH.

**New necessary conditions for a counterexample to (PE0) or to the problem:**
- every smooth submersive factor is GH;
- every factor of dimension <= 3 has zero entropy (modulo R6-a), so the entropy is carried by the fibres (Abramov–Rokhlin / Bowen, cited);
- no submersive factor has a periodic orbit with Jacobian-1 return map, or a hyperbolic periodic orbit with a homoclinic point.

**Open:** (PE0) itself, already in the volume-preserving (cohomology-free) case. There it reads: a cohomology-free flow has zero entropy. I neither refuted nor proved it. The exact point where things stop is the same as in R11-b: no finite Dirac or leaf-moment configuration gives two-sided exponential decay when lambda = 0, and spectral bounds give no contradiction (Section 3).

=== END OF ANSWER round12_q4 ===
