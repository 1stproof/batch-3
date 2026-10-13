# Answer to round4_q3 (MS4: is t -> Y_t constant?)

## Status summary
I could not prove MS4 in full, and I could not build a counterexample. Below:
- **(A) Proved.** Holomorphy of t -> Y_t, from (R1) and (R2) only. This is a cleaner proof than P-a's, which relied on a properness claim that was not justified.
- **(B) Proved (pinning theorem).** MS4 holds whenever the closure of dV_0 has one "pinning incidence" with a boundary piece whose closure does not move. This makes P-d Lemma B fully rigorous, and it shows that local continuity suffices.
- **(C) Proved modulo one cited theorem.** MS4 holds if every V_t is totally geodesic. The proof uses countability of totally geodesic subvarieties (cited from memory) and Sierpinski's theorem, so it needs no "continuous + countable" heuristic.
- **(D) Sketch only.** For covering constructions, (B) reduces MS4 to the rigidity of the boundary Teichmuller curve. That rigidity is cited from memory (Moller) and is not checked.
- **(E) Open.** The general statement remains open. I explain why the natural attempts at a counterexample are blocked (in fact they confirm the mechanism of (B)), and what a general proof would need.

Notation: dV_t = {Y_t} x C_t with C_t a curve in the other factors. Phi : closure(V_0) x Delta -> closure(calV) is the stratified homeomorphism of (R2), and Phi_t = Phi(., t).

---

## (A) Lemma 1 (holomorphy of Y_t), proved from (R1) and (R2)

**Lemma 1.** t -> Y_t is a holomorphic map Delta -> M_{g_i,n_i}.

*Proof.*
1. **Continuity.** Fix p in dV_0. By (R2), Phi(p,t) lies in dV_t for every t, so Y_t = pi_i(Phi(p,t)). This is continuous in t because Phi is continuous.
2. **The analytic set A.** Let A = closure(calV) cap (Delta_Gamma x Delta). By (R1), A is a closed analytic subset of the complex manifold Delta_Gamma x Delta. By (R2), A is homeomorphic to dV_0 x Delta. The set dV_0 is a 1-dimensional analytic set, so every nonempty open subset of A has real topological dimension 4. Hence A has pure complex dimension 2.
3. **The projection to Delta.** Each fibre A_t = dV_t has dimension 1. So no irreducible component of A lies in a fibre of phi : A -> Delta.
4. **The bad set.** Let B be the union of Sing(A) and the critical set of phi restricted to Reg(A). Then B is a closed analytic subset of dimension at most 1.
   - It is a proper subset in each component. Otherwise phi would be locally constant on an open subset of Reg(A), and that would force a component into a fibre.
   - The 1-dimensional irreducible components of B form a locally finite family. Those contained in fibres of phi lie over a discrete set D in Delta.
   - For t not in D, the fibre A_t (dimension 1) is not contained in B. Indeed, the intersection of A_t with B is a union of fibre-contained components of B, which do not occur over such t, and of finitely many points locally.
5. **Local sections.** For t_0 not in D, pick a in A_{t_0} \ B. Near a, A is a manifold and phi is a submersion. So there is a holomorphic local section s of phi with s(t_0) = a, and Y_t = pi_i(s(t)) is holomorphic near t_0.
6. **Conclusion.** Y is continuous on Delta and holomorphic on Delta \ D with D discrete. By the removable singularity theorem (in local coordinates of M_{g_i,n_i}, which is an orbifold, so work in a local manifold chart / finite cover near Y_{t_0}), Y is holomorphic on Delta. ∎

**Corollary.** MS4 is equivalent to "Y_t = Y_0 for all t in some neighbourhood of 0", by the identity theorem.

---

## (B) Pinning theorem (rigorous)

**Theorem B.** Suppose there exist:
- a stratum Delta_{G'} contained in closure(Delta_Gamma);
- a point P_0 in closure(dV_0) cap Delta_{G'};
- a stratum Delta_G with Delta_{G'} contained in closure(Delta_G);

such that:
- (a) P_0 is an isolated point of closure(V_0) cap Delta_{G'};
- (b) P_0 lies in closure(E_0), where E_t := closure(V_t) cap Delta_G and dim E_0 = 1;
- (c) the family E_t is "closure-constant" near t = 0, i.e. closure(E_t) = closure(E_0) for t small.

Then Y_t = Y_0 for all t in Delta.

*Proof.*
1. **Definition of P_t.** Put P_t = Phi(P_0, t).
   - Phi_t is a homeomorphism from closure(V_0) onto closure(V_t) mapping the Delta_Gamma-part onto the Delta_Gamma-part. So it maps closure(dV_0) onto closure(dV_t), and P_t lies in closure(dV_t) cap Delta_{G'}.
   - P_t is continuous in t.
2. **The i-th component of P_t is Y_t.**
   - The gluing map from (product of the closures of M_{g_j,n_j}) to the closure of M_g is proper and continuous. So the closure of {Y_t} x C_t equals the image of {Y_t} x closure(C_t).
   - Every point of it is a stable curve having the smooth pointed curve Y_t as the component at vertex i.
   - In particular, P_t determines Y_t: it is the vertex-i component of P_t.
3. **Applying (ii).** Choose a neighbourhood U of P_0 such that closure(V_0) cap Delta_{G'} cap U = {P_0}, which is possible by (a).
   - Then closure(E_0) cap Delta_{G'} cap U is contained in {P_0} and contains P_0, by (b).
   - So the hypothesis of (ii) holds for (Delta_G, Delta_{G'}, U), and (ii) yields, for all t, closure(E_t) cap Delta_{G'} cap U = closure(V_t) cap Delta_{G'} cap U.
   - For t small, P_t lies in U and in closure(V_t) cap Delta_{G'}, hence P_t lies in closure(E_t) = closure(E_0), by (c).
4. **Finiteness.** closure(E_0) cap Delta_{G'} is finite.
   - closure(V_0) cap closure(Delta_G) is a compact analytic set. closure(E_0) is the union of those of its irreducible components that meet Delta_G. These have dimension 1, since E_0 is dense open in them and dim E_0 = 1.
   - Delta_{G'} is disjoint from Delta_G. So closure(E_0) cap Delta_{G'} lies in closure(E_0) \ E_0, which is a proper closed analytic subset of a compact 1-dimensional analytic set, hence finite.
5. **Conclusion.** t -> P_t is continuous with values in a finite set for small t, so it is constant there. By step 2, Y_t = Y_0 for small t, and by the Corollary of Lemma 1, for all t. ∎

**Remarks.**
- (c) is the only non-formal input. It holds, for example, if the boundary curve E_0 is *rigid*: every deformation of it as a 1-dimensional subvariety of Delta_G, with fixed topological type, is trivial.
- Isolatedness (a) holds automatically when dim Delta_{G'} cap closure(V_0) = 0 near P_0. For a 2-dimensional V_0 this is the generic situation for codimension-3 or deeper strata, but it is not guaranteed.
- If (a) fails, the same proof works whenever the hypothesis of (ii) can be verified on some U.

---

## (C) Sub-case: every V_t totally geodesic (proved modulo citation)

**Cited (from memory).**
- Every totally geodesic subvariety of M_g of dimension at least 2 is (the projection of) a GL(2,R)-orbit closure of quadratic differentials (Wright; Filip's algebraicity).
- By Eskin–Mirzakhani–Mohammadi (plus the quadratic-differential version via the canonical double cover), there are only countably many orbit closures.
- Hence there are only countably many totally geodesic subvarieties of M_g.

**Proposition C.** If V_t is totally geodesic for every t, then V_t = V_0 for all t, and in particular Y_t = Y_0.

*Proof.*
1. Each V_t is irreducible, because it is homeomorphic to V_0 (connected, smooth). For each of the countably many totally geodesic surfaces W, let F_W = {t : V_t = W}.
2. **F_W is closed.** Let t_n -> t with V_{t_n} = W.
   - Every point of V_t is Phi(p,t) = lim Phi(p,t_n), a limit of points of W. It lies in M_g, and W is closed in M_g, so V_t is contained in W.
   - Both are irreducible closed 2-dimensional analytic subsets of M_g, so V_t = W.
3. **Conclusion.** The F_W are pairwise disjoint, closed, countably many, and cover the connected space Delta. By Sierpinski's theorem (a connected compact Hausdorff space is not a countable union of at least 2 pairwise disjoint nonempty closed sets; apply it to closed subdiscs, which are compact connected), only one F_W is nonempty. Hence V_t = V_0. ∎

This sub-case does not answer the question, since V_t is not assumed totally geodesic.

---

## (D) Covering constructions: reduction to rigidity of a boundary Teichmuller curve (sketch)

**Model example (worked in M_{0,n}).** In the problem's setting one transports it to M_g by a further covering construction; that step is not checked.
- Take the base (P^1; 0, inf, 1, x, y) in M_{0,5} and the cover z -> z^d. Let S be the configurations (0, inf, mu_d, xi mu_d, eta mu_d) with xi^d = x and eta^d = y. This is the fixed locus of a relabelling permutation, so it is smooth. It is totally geodesic, being the image of a covering construction: lifted Teichmuller maps are Teichmuller maps for the integrable pulled-back differential.
- **The stratum Gamma.** As x, y -> 1 together, we reach the stratum Gamma: a central vertex (0, inf, d nodes) with d leaves of type M_{0,4}.
  - dS = {Y_0} x (curve), where Y_0 = (P^1; 0, inf, mu_d) lies in M_{0,d+2}. This factor has positive dimension for d >= 2, so this is a genuine instance of the problem's situation.
- **The pinning curve.** E_0 is the boundary piece of S in the stratum where x -> 1 only: configurations (0, inf, mu_d, eta mu_d) in M_{0,2d+2}. Its closure contains the corner point P_0 (eta -> 1), whose central component is Y_0. Here P_0 is isolated in its (codimension-2) stratum, and (ii) transports the incidence.
- **Conclusion of the sketch.** E_0 is itself a Teichmuller curve (the covering construction of M_{0,4}). So Theorem B gives MS4 for this S provided Teichmuller curves are rigid under deformations of the curve inside the stratum, with the base curve allowed to vary. I recall (from memory, **not verified**) that Moller (JAMS 2006) proves "Teichmuller curves are rigid", via the maximal-Higgs sub-VHS; it is unclear to me whether his statement covers deformations with varying base. If it does, MS4 holds for this example and, by the same pattern, for covering constructions whose constant factor lies over an M_{0,3} base component adjacent to such a Teichmuller boundary curve.

**Why the naive counterexample fails in this model (proved for the ansatz).**
- Try deforming S by moving only the A-points: A_j = zeta^j a_j(xi, eta), with B, C unchanged.
- Hypothesis (i) at the stratum x = 1 forces all d collisions B_k = A_{k+m} to happen simultaneously along one curve. On that curve this forces a_j to be independent of j, i.e. the A-points form a regular d-gon.
- At the corner, which lies on both collision curves, the central component is therefore (0, inf, regular d-gon) = Y_0.
- So Y_t = Y_0 within this ansatz. Constant perturbations A_j = zeta^j + t c_j are excluded altogether: they change the topology of the parameter domain (d^2 instead of d excluded values), violating smooth triviality.

---

## (E) What remains open
1. **MS4 in general.** In general, a constant factor Y_0 of a 1-dimensional boundary piece of a totally geodesic surface need not be shown to admit a pinning incidence as in Theorem B. A general proof would need either of:
   - (E1) a structure theorem: every constant factor of a boundary piece of closure(V_0) appears, at an isolated deeper point, in the closure of a boundary piece E_0 that is rigid. Such E_0 should be a product of Teichmuller curves / orbit closures in the factors where the limiting quadratic differential is nonzero; this would use WYSIWYG / Mirzakhani–Wright boundary theory and rigidity of orbit-closure boundary pieces. **Unproved.**
   - (E2) rigidity of V_0 itself: H^0 of the log normal sheaf of (closure(V_0), boundary) in closure(M_g) vanishes. Then every family is trivial. **Unproved; I know no such theorem for totally geodesic surfaces.**
2. **No counterexample found.** Every attempt I examined is either forced back to Y_0 by (i), or violates smooth triviality.
3. **The derivation problem -> MS4 is sound under (R1) and (R2).** (R1) is needed for analyticity; without it, only continuity of Y_t follows, and Lemma 1's identity-theorem step is lost. Theorem B, however, uses only continuity plus (ii), so it does not need (R1) beyond the analyticity of closure(V_0) and of the closures of the E_t.

=== END OF ANSWER round4_q3 ===
