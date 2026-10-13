# round12_q2 — answer

## 0. Status
I did **not** prove (PE0), and I did **not** find a counterexample. (PE0) stays open, and so does the problem in dimension >= 4. Below are:
(i) a check of the chain;
(ii) a short new analysis of the strongest existing tool, Proposition MG (R8-f), in the volume case. It shows that MG gives a contradiction exactly when a certain "su-coupling" measure is **not an extreme coupling**. The criterion that comes for free (an absolutely continuous part, via Lindenstrauss) holds exactly in the hyperbolic case. A smooth twisted model (Heisenberg) shows that non-extremality does not need local product structure. The remaining gap is the low regularity of Pesin laminations, which is stated precisely below;
(iii) the routes I tried and why each stops;
(iv) a list of the open questions.
Items marked "proved" have complete proofs here. Items marked "cited" are quoted from memory.

## 1. Check of the chain
Step 1 (variational principle + Jacobs) and step 2 (entry 113: for g_1-ergodic mu with h_mu(g_1) > 0, GH forces int J_1 dmu = 0) give a g_1-ergodic mu with h_mu > 0 and int J_1 dmu = 0. (PE0) excludes exactly such mu. So (PE0) + step 1 + step 2 implies h_top(g_1) = 0, and I found no gap in this logic. It relies on the citations in step 2 (Pesin, Ledrappier-Strelcyn, non-stationary normal forms), which I did not re-check. As stated, the chain does derive the problem's claim from (PE0).

## 2. Proposition MG in the volume case is a statement about extreme couplings (proved; uses only MG of R8-f)
Setting: GH, and X preserves a smooth positive density omega. Take nu = omega, so d = 0, J = 0 and every beta = 0. Let (K, m, xi^s, xi^u) be data as in Proposition MG, with uniform constants (S), (U) and (R) with eta = 0. Assume the partitions are measurable, so that the quotients Y := K/xi^s and Z := K/xi^u are standard. Let pi_s : K -> Y and pi_u : K -> Z be the quotient maps. Let m^_s, m^_u be the quotient measures, and put m~ := (pi_s, pi_u)_* m on Y x Z. Then m~ is a coupling of m^_s and m^_u.

**Lemma 2.1 (proved).** The following are equivalent:
(a) there is a nonzero w in L^inf(m) with E_m[w | xi^s] = 0 and E_m[w | xi^u] = 0, i.e. the hypothesis of MG holds with w != 0;
(b) m~ is not an extreme point of the convex set of couplings of (m^_s, m^_u).
Consequently, **under GH + volume, m~ is an extreme coupling for every such data set.**

*Proof.*
(b) => (a):
- If m~ = (m_1 + m_2)/2 with m_1 != m_2 two couplings, then eta := (m_1 - m_2)/2 satisfies |eta| <= m~ and has zero marginals.
- Let h = d eta / d m~, so |h| <= 1, and put w(z) := h(pi_s z, pi_u z). Then w is bounded and nonzero on a set of positive m-measure.
- Disintegrate m over xi^s: m = int m_A dm^_s(A). For m^_s-a.e. y, int_{pi_s^{-1}(y)} w dm_{A_y} = int h(y, .) d m~(. | y), and this is 0 because the Y-marginal of eta vanishes.
- Symmetrically, w has zero conditional means on xi^u-cells.

(a) => (b):
- Given w, normalise so that ||w||_inf <= 1. Put eta := (pi_s, pi_u)_*(w m), so |eta| <= m~.
- eta has zero marginals, because the conditional means vanish.
- eta != 0: otherwise E_m[w | sigma(pi_s, pi_u)] = 0. But w is sigma(pi_s, pi_u)-measurable mod m, because xi^s ∨ xi^u is the point partition on K (locally W^s_loc(x) ∩ W^u_loc(x) = {x}; this holds for Pesin local manifolds through points of a Pesin block). So w = 0, a contradiction.
- Hence m~ ± eta are couplings, and m~ is their midpoint.

The final sentence of the lemma is MG. ∎

**Corollary 2.2 (cited input: Lindenstrauss, "A remark on extreme doubly stochastic measures", Amer. Math. Monthly 1965, from memory: an extreme coupling is singular with respect to the product of its marginals).** Under GH + volume, for every MG data set the coupling m~ is singular w.r.t. m^_s ⊗ m^_u.

**Why this does not settle (PE0) (analysis; the dimension count is a sketch).**
- In the hyperbolic case, local product structure with absolutely continuous conditionals makes m~ ≈ product measure, so Corollary 2.2 is violated. This is another view of Theorem 5.1 and of MG's remark.
- In the non-hyperbolic case (genuine centre of dimension c - 1 >= 1), the s-index space Y has "dimension" n - s and Z has n - u. So Y x Z has dimension 2n - u - s = n + c, while m~ lives on the n-dimensional incidence set {(y, z) : the plaques meet}. Hence m~ is automatically singular, and Corollary 2.2 gives nothing.
- So the a.c. criterion fails exactly in the case (PE0) needs. One needs non-extremality of a singular coupling. For finite or countable supports this is the existence of cycles (Theorem G (b), (c)). In general it is "aperiodicity"-type structure of the support (I recall Hestir-Williams, but I cannot state their criterion reliably).

**Example 2.3 (proved; smooth twisted model, no local product structure, yet non-extreme).** On R^3 take u-leaves = lines in the x-direction (field U = ∂_x) and s-leaves = curves τ -> (x, y + τ, z + xτ) (field V = ∂_y + x∂_z), both with Lebesgue leaf measure. Lebesgue measure disintegrates along both families with these leaf measures; for the s-family, at fixed x the map is a translation of the (y,z)-plane.
- [U, V] = ∂_z, which commutes with U and V. So u- and s-plaques are not jointly integrable, and no small su-quadrilateral closes.
- For H in C_c^inf(R^3), H != 0, put w := ∂_x V^2 H. Then int w dx = 0 on every u-line.
- Also w = (V ∂_x + ∂_z) V H = V(∂_x V H + ∂_z H), a V-derivative of a compactly supported function, so int w dτ = 0 on every s-curve.
- w != 0: if ∂_x(V^2 H) = 0 with compact support, then V^2 H = 0, hence VH = 0, hence H = 0.

So for smooth (twisted) laminations the coupling is non-extreme. Consistently, Theorem U (R8-f) rules out uniform partial hyperbolicity. The obstruction in (PE0) is therefore **not** the twisting itself. It is that Pesin laminations live on fractal Pesin blocks and depend only Hölder-continuously on the base point. The constructions above (derivatives along leaves, or cycles produced by dimension counting with invariance of domain / Hurewicz / coarea) need either open parameter sets or Lipschitz walk maps with nondegenerate Jacobian.

## 3. Routes tried in this round, and why each stops
- **Cycles from absolutely continuous conditionals (volume case).** Walks x -> y_1 (in W^u_loc ∩ K) -> y_2 (in W^s_loc ∩ K) -> ... have parameter sets of positive Lebesgue measure in R^{k(u+s)} (absolute continuity of Pesin laminations, cited). Two walks with a common end give a cycle, hence a contradiction (Theorem G, volume case). But the end map is only Hölder in the earlier parameters. Non-injectivity would need the coarea formula with positive Jacobian. Lipschitz injective maps from positive-measure sets of R^2 to R exist (g(x) = int_0^x 1_{C^c}, which is injective on a fat Cantor set C, plus a second coordinate), and Hurewicz fails because fat Cantor sets have covering dimension 0. **Stops.**
- **Weak leaves of complementary dimension.** If c = 2, then dim W^{ws} + dim W^{wu} = n, but both contain the flow direction. So E^{ws} + E^{wu} has dimension n - 1, there is no transversality, and intersection theory does not apply. **Stops.**
- **Spectral / variance route (volume case).** GH gives sup_{x,T} |int_0^T f∘g_t dt| <= C||f||_{C^m} for mean-zero f. A contradiction would need a smooth f that is not an L^2-coboundary. Measurable coboundaries are dense, and small-ball local times have variance ~ T r^{n+1} only in the few-visit regime T << r^{-(n-1)}, which is too short against r^{-2m}. Without mixing rates there is no conclusion. **Stops** (same as R7-b, R8-e).
- **Conditional-independence criterion (proved, but no useful class found).** Let P = sigma(xi^u), F = sigma(xi^s), G = P ∩ F, and suppose P and F are conditionally independent given G. Take a in L^inf(P) and b in L^inf(F) with E[a|G] = E[b|G] = 0, both supported, via G-measurable cut-offs, on a common G-set where they are nonzero. Then w = ab satisfies E[w|P] = a E[b|G] = 0 and E[w|F] = b E[a|G] = 0, and w != 0. So under GH + volume such conditional independence (with P != G and F != G on a common G-set) is impossible. It holds in products (Anosov x rotation), which are already non-GH; I could not verify it for any twisted class.
- **Smooth discs (Yomdin-Newhouse volume growth).** These lead to real eigen-currents, hence to (E1)/(E1-int), which is already known to be equivalent to the goal. **Stops.**

## 4. What is proved / open
Proved here:
- Lemma 2.1 (MG in the volume case is equivalent to extremality of the su-coupling).
- Example 2.3 (smooth twisted laminations give non-extreme couplings).
- The conditional-independence criterion in §3.

Cited: Corollary 2.2 (via Lindenstrauss).

None of these proves (PE0), even in the volume case.

Open:
- **(PE0) itself.**
- In the volume case, it would follow from **(EXT)**: for a smooth volume-preserving flow with h_omega(g_1) > 0 and a zero centre exponent, some Pesin data set (K, m, xi^s, xi^u) has a non-extreme su-coupling. Equivalently: some nonzero bounded w on a Pesin block has zero conditional means on both local stable and local unstable plaques.
- A sufficient form of (EXT): a finite su-cycle (closing exactly, or modulo the flow with more edges than vertices) through points of a Pesin block. Producing it needs regularity of Pesin laminations, or a coarea-type argument for Hölder walk maps, that I do not have.

=== END OF ANSWER round12_q2 ===
