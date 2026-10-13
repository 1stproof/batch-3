# Answer to round4_q6 (MS4 via rigidity of maps into M_g plus rigidity of the base)

## 0. Status (summary)
- **Proved, citing Imayoshi–Shiga (from memory).** Theorem A: rigidity of holomorphic maps into a level cover M' of M_g over a fixed quasi-projective base of any dimension. The base may be singular.
- **Proved.** Corollary B, a countability statement: up to composing with M' → M_g, holomorphic maps B → M' that are nonconstant on curves come in at most countably many, so they have at most countably many images. No topological hypothesis on the family is needed.
- **Proved.** Theorem C, a conditional resolution. Let V'_t be an irreducible component of the preimage of V_t in a level cover. If the isomorphism class of the analytic space V'_t takes only countably many values as t ranges over Δ, then t ↦ Y_t is constant, which is the claim. In particular this holds if the V'_t are all biholomorphic to V'_0.
- **Not proved: the missing lemma (ML).** The claim is reduced to ML: the complex structure of V'_t does not move, or at least takes only countably many isomorphism classes. Section 5 gives a sufficient condition (log-rigidity together with a log-smooth extension of the family). I could not verify that condition for totally geodesic surfaces. The question stays **open**.
- **Important caveat (Section 6).** The suggested Step 2 compares V_0 and V_t through homotopy classes. That breaks down when V_0 lies in the locus of curves with nontrivial automorphisms, which is the case for the known covering-construction examples. In that case the level covers of V_0 and V_t need not be homeomorphic. Theorem C is formulated so that it does not need this comparison.

## 1. Conventions
- Fix m ≥ 3. Let Γ' = ker(Mod_g → Sp(2g, Z/m)). This group is torsion-free (Serre) and normal of finite index.
- Let M' = T_g/Γ' = M_g[m]. Cited from memory: M' is a smooth quasi-projective fine moduli space with a universal family, and the quotient map p: M' → M_g = M'/G, G = Sp(2g, Z/m), is finite.
- M' is aspherical with π_1 = Γ', because T_g is contractible and Γ' acts freely.
- Fact (Bers, from memory): T_g is biholomorphic to a bounded domain in C^{3g-3}.
- For each t, V_t is irreducible: V_t ≅ V_0 topologically, and V_0 is a connected smooth surface.
- V'_t denotes an irreducible component of p^{-1}(V_t). It is closed in M', hence quasi-projective.
- p(V'_t) = V_t. Proof: G acts transitively on the components of p^{-1}(V_t). These components all have the same image, which is closed because p is finite, and the images together cover V_t.
- Lemma 1 of P-a gives that Y: Δ → M_{g_i,n_i}, t ↦ Y_t, is holomorphic. Continuity comes from (i); holomorphy comes from analyticity of closure(𝒱) ∩ (Δ_Γ × Δ). I re-checked the argument in outline only and use it as given.

## 2. Theorem A (rigidity over a fixed base)
**Lemma A0.** Let C be a finite-type Riemann surface and u: C → M' a holomorphic map whose monodromy u_*: π_1(C) → Γ' has finite image. Then u is constant.

*Proof.*
1. Γ' is torsion-free, so the image of u_* is trivial.
2. By the lifting criterion for the unramified covering T_g → M', u lifts to a holomorphic map ũ: C → T_g ⊂ C^N, with bounded image.
3. C is a compact Riemann surface minus finitely many points. Bounded holomorphic functions extend across punctures (Riemann), so ũ extends to the compact surface.
4. A holomorphic map from a compact Riemann surface into C^N is constant by the maximum principle. ∎

**Cited theorem (Imayoshi–Shiga 1988, the rigidity half of the Parshin–Arakelov finiteness theorem; stated from memory).** Let C be a Riemann surface of finite type. Let two locally non-trivial holomorphic families of compact genus-g Riemann surfaces over C have the same monodromy up to conjugation in Mod_g. Then they are isomorphic over C.

For u_1, u_2: C → M' this gives the following. If the u_j are nonconstant and homotopic, then the pulled-back universal families have conjugate monodromy, and the theorem says they are isomorphic over C. Hence p∘u_1 = p∘u_2.

**Theorem A.** Let B be an irreducible quasi-projective variety (possibly singular) and f_1, f_2: B → M' homotopic holomorphic maps. Suppose that for every b ∈ B there is an irreducible curve C ⊂ B through b such that f_1|_C is nonconstant. Then p∘f_1 = p∘f_2.

*Proof.*
1. Fix b and such a curve C. Let ν: C̃ → C be its normalization, a finite-type Riemann surface.
2. f_1∘ν and f_2∘ν are homotopic (restrict the homotopy), so they have conjugate monodromy.
3. f_1∘ν is nonconstant, so by Lemma A0 its monodromy is infinite. Hence f_2∘ν also has infinite monodromy and is nonconstant.
4. By Imayoshi–Shiga, p∘f_1∘ν = p∘f_2∘ν. Evaluating at a preimage of b gives p f_1(b) = p f_2(b). ∎

**Hypothesis check.** The required curves exist whenever f_1 is injective, for instance the inclusion of a subvariety. Then any curve through b works; take a component through b of a general linear section of B through b. One does not need Teichmüller discs for this.

## 3. Corollary B (countability)
Let B be an irreducible quasi-projective variety. Let 𝓗(B) be the set of holomorphic maps f: B → M' that are injective, or more generally satisfy the curve hypothesis of Theorem A. Then {p∘f : f ∈ 𝓗(B)} is countable, and so is {p(f(B)) : f ∈ 𝓗(B)}.

*Proof.*
1. M' is a K(Γ',1), so free homotopy classes of maps B → M' correspond to conjugacy classes of homomorphisms π_1(B) → Γ'.
2. π_1(B) is finitely generated, because B has the homotopy type of a finite CW complex. Γ' is countable. So there are countably many such classes.
3. By Theorem A, p∘f depends only on the homotopy class of f. ∎

## 4. Theorem C (conditional resolution of the claim)
**Theorem C.** Suppose the set {isomorphism class of the analytic space V'_t : t ∈ Δ} is countable. This holds, for example, if every V'_t is biholomorphic to V'_0. Then π_i(∂V_t) = {Y_0} for all t.

*Proof.*
1. Δ is uncountable, so there is an uncountable S ⊂ Δ such that all V'_t, t ∈ S, are biholomorphic to one fixed B := V'_{t_1}.
2. For t ∈ S choose a biholomorphism h_t: B → V'_t. Let ι_t: V'_t → M' be the inclusion. Then f_t := ι_t∘h_t: B → M' is holomorphic and injective, so f_t ∈ 𝓗(B).
3. Its image satisfies p(f_t(B)) = p(V'_t) = V_t.
4. By Corollary B, {V_t : t ∈ S} is countable. Each V_t determines ∂V_t and hence Y_t, so {Y_t : t ∈ S} is countable.
5. Hence some value y is taken on an uncountable set S_y ⊂ S. Write Δ as a countable union of compact sets; one of them contains infinitely many points of S_y, so S_y has an accumulation point in Δ.
6. Y is holomorphic (P-a, Lemma 1). Y^{-1}(y) is an analytic subset of Δ with an accumulation point in Δ, so it is all of Δ. Hence Y_t = y = Y_0 for all t. ∎

**Remark.** Suppose in addition that the V'_t form a topologically trivial family and that h_t can be chosen homotopic to the transport map. Then Theorem A gives directly V_t = p(V'_t) = V_0 for that t. This is Step 2 of the suggested approach. Theorem C needs strictly less: it needs no homotopy compatibility and no topological triviality of the level covers.

## 5. The missing lemma, and what would prove it
**ML (missing lemma; unproved).** For the family in the problem, with V_0 totally geodesic of dimension 2 and hypotheses (i), (ii), (R1), (R2), the isomorphism class of the analytic space V'_t takes only countably many values for t ∈ Δ. For instance, V'_t ≅ V'_0 for all t.

By Theorem C, ML implies the problem's claim.

**A sufficient condition (standard deformation theory, cited from memory).** Suppose the following hold:
- (a) The family 𝒱' := (a component of (p × id)^{-1}(𝒱)) → Δ admits a relative log-smooth compactification (𝒳, 𝒟) → Δ. That is, 𝒳 → Δ is smooth and proper, 𝒟 is a relative SNC divisor, and 𝒳 \ 𝒟 = 𝒱'.
- (b) H^1(X_0, T_{X_0}(−log D_0)) = 0.

Then the family of log pairs is locally trivial near t = 0. This is the Kodaira–Spencer–Kuranishi rigidity theorem for log pairs, cited from memory. So V'_t ≅ V'_0 for t in a neighbourhood of 0. That is an uncountable set, so the argument of Theorem C, run on that set, gives Y constant.

Neither (a) nor (b) is established:
- **(b) is unknown to me.** For ball quotients it would follow from Calabi–Vesentini-type vanishing, but the known totally geodesic surfaces are not ball quotients or Shimura varieties, as far as I recall. These are the flex locus in M_{1,3} and the gothic locus in M_4 (McMullen–Mukamel–Wright; Eskin–McMullen–Mukamel–Wright). I know of no vanishing theorem for H^1(T(−log D)) that uses the Teichmüller-totally-geodesic structure.
- **(a) is not implied by (i) and (ii).** Hypothesis (i) gives smooth triviality stratum by stratum in M̄_g, not a log-smooth compactification of the level cover. Moreover, the fibre of 𝒱' over 0 can be non-reduced or singular when V_0 meets the branch locus of p.

**Why the other suggested routes were not completed.**
- **Retraction route (b).** This would need a Stab(Ṽ_0)-equivariant holomorphic retraction of T_g onto the lift Ṽ_0. I do not know whether one exists, even for Teichmüller discs together with equivariance. Even given one, r∘F_t: Ṽ_t → Ṽ_0 descends to a holomorphic map V_t → V_0. Its properness and degree one would still have to be proved, using cusp behaviour that (i) controls only topologically. This route is unproved.
- **Hodge-theoretic route (Möller-type).**
  - Background, from memory: Möller proved rigidity of Teichmüller curves. The rank-2 maximal-Higgs sub-VHS persists under deformation, because Arakelov equality is a degree condition and degrees are constant in flat families. Maximal Higgs then characterizes Teichmüller curves, and these are countable.
  - Analogue for surfaces: one would need (1) persistence of the rank-4 sub-local system W (Wright/Filip) as a sub-VHS over V_t, which follows from Deligne semisimplicity if W occurs with multiplicity one in H^1; and (2) a Hodge-theoretic, numerically detectable characterization of totally geodesic surfaces.
  - Given both, V_t would be totally geodesic, and countability (P-a, Lemma 3) would finish. Neither (1) in general nor (2) is known to me. This is a second form of the missing lemma.
- **Local hypotheses.** (i) and (ii) cannot replace ML. P-b and P-a Observation 4 show that every local condition along Δ_Γ is satisfied by an arbitrary holomorphic arc Y_t.

## 6. Caveat about homotopy comparison and level covers
The suggested Step 2 assumes f_t∘Φ_t ≃ f_0 as maps into M'. In the coarse space M_g that homotopy carries no information. To lift it to M' one needs V'_t to be a topologically trivial deformation of V'_0.

That fails if V_0 lies in the locus of curves with a nontrivial automorphism (as covering constructions do) while V_t does not, or more generally if V_t meets that branch locus in a way that varies with t. Then p^{-1}(V_0) and p^{-1}(V_t) can have different numbers of components and different topology.

Theorem C and Corollary B avoid this problem, because they use only abstract isomorphism classes and count homotopy classes. ML is accordingly formulated for the V'_t, not for the V_t.

## 7. Open questions (explicit)
1. **(ML)** Is the complex structure of V'_t locally constant, or does it at least take countably many values, in a family satisfying (i) and (ii) with V_0 totally geodesic of dimension 2?
2. Is H^1(X, T_X(−log D)) = 0 for a log-smooth compactification of (a level cover of) a totally geodesic surface in M_g?
3. Is there a Hodge-theoretic characterization of totally geodesic surfaces that is stable under deformation (an analogue of Möller's maximal-Higgs characterization)?

A positive answer to 1 proves the claim by Theorem C. Positive answers to 2 (together with a log-smooth extension of the family, Section 5(a)) or to 3 (together with persistence of W) would imply 1. The problem's claim itself remains **unproved** here.

=== END OF ANSWER round4_q6 ===
