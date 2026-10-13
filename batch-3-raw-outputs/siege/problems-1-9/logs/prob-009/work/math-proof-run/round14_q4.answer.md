# round14_q4 — attempt to refute (NRT_P)

**Plan/status line.** Outcome: **not refuted.** I found no counterexample, and no derivation of a known-false statement from (NRT_P). The ingredient that cannot be built with the tools available is the *global* one: a non-trivial admissible deformation of a smooth closed totally geodesic surface. Every chart-level ingredient (isotropy drop, rigid twin, detaching mirror) is already realised locally (round13_q3/q4/q6). This file proves some global necessary conditions that any such deformation must meet, and settles one candidate class of V_0 in part (§4).

What the file proves:
- (§1) a constant complex structure forces V_t = V_0 (cited rigidity theorem);
- (§2) stable translation lengths are monotone along the family;
- (§3) the Teichmüller curves inside V_0 are rigid: they cannot be deformed into V_t;
- (§4) the symmetric-locus candidates;
- (§5) a leading-term (normal-bundle) obstruction.

§6 says exactly what remains open.

Readings: (R1), (R2) with H_0 = id, coarse. I only use the global fact "V_t ≠ V_0 for some t", which any counterexample needs. If V_t = V_0 as sets for all t, then ∂V_t = ∂V_0 and Y_t = Y_0, so the problem's conclusion holds trivially.

Throughout, ℓ ≥ 3, M_g[ℓ] is the level-ℓ cover (a smooth variety, fine moduli space), and Γ_g[ℓ] ⊂ Mod_g is its group (torsion-free).

---

## 0. The reduction: a counterexample to (NRT_P) needs a non-rigid V_0

A counterexample to (NRT_P) needs t ↦ Y_t non-constant. Then ∂V_t ≠ ∂V_0 for some t, so V_t ≠ V_0. So:

**(0.1)** If V_0 is *rigid*, i.e. every family satisfying the problem's hypotheses has V_t = V_0 for all t, then (NRT_P) and the problem are vacuously true for that V_0.

The search for a counterexample is therefore the search for a smooth closed totally geodesic surface admitting a non-trivial deformation with fixed boundary combinatorics. The sections below collect the constraints on such a deformation.

---

## 1. Lemma 1 (a constant complex structure forces triviality)

**Lemma 1.** Suppose that for every t there is a biholomorphism φ_t : V_0 → V_t homotopic, as a map into M_g, to the inclusion. Here homotopic means: through H_s, s ∈ [0,t], then to φ_t. Then V_t = V_0 for all t.

*Proof (cited input).*
- **Imayoshi–Shiga rigidity (cited from memory).** Let B be a Riemann surface of finite type and f_1, f_2 : B → M_g[ℓ] holomorphic maps. If f_1 and f_2 are homotopic and their common monodromy π_1(B) → Γ_g[ℓ] has infinite image, then f_1 = f_2.
- Pass to a component V_0′ of the preimage of V_0 in M_g[ℓ]. Since H_t, φ_t are homotopies of maps into M_g, they lift to V_0′ on the complement of the finite branch data. This is a technical point that I do not check in detail.
- V_0′ is covered by algebraic curves B ⊂ V_0′ (for example generic hyperplane sections) whose monodromy is infinite. The reason: the monodromy of a totally geodesic V_0 contains pseudo-Anosov elements, and a generic hyperplane section surjects onto π_1 by Lefschetz.
- For each such B, the two maps f_0 = incl|_B and f_t = φ_t|_B are homotopic. So they are equal on B.
- These curves B cover a dense set, so φ_t = incl and V_t = V_0. ∎

So a counterexample needs the complex structure of V_t to vary. This agrees with the run's entry 33.

---

## 2. Lemma 2 (monotonicity of stable translation lengths) — proved

For a group element γ acting isometrically on a pseudo-metric space (Z, d), set ℓ_Z(γ) := lim_n d(z, γ^n z)/n. This limit exists by subadditivity and does not depend on z.

**Lemma 2.**
- (a) Let W be a connected complex space with a group Λ acting on it by biholomorphisms. Let F : W → T_g be a holomorphic map that is equivariant for a homomorphism ρ : Λ → Mod_g. Then, with k_W the Kobayashi pseudo-distance and d_T the Teichmüller metric, ℓ_{(W,k_W)}(γ) ≥ ℓ_{(T_g,d_T)}(ρ(γ)) for every γ ∈ Λ.
- (b) Let Ṽ_0 be a component of the preimage of V_0 in T_g, and Λ_0 its stabiliser. Then Ṽ_0 is contractible, k_{Ṽ_0} = d_T|_{Ṽ_0}, and ℓ_{Ṽ_0}(γ) = ℓ_T(γ) for every γ ∈ Λ_0.
- Consequently, if a component W_t of the preimage of V_t in T_g (or its normalisation) is invariant under γ ∈ Λ_0, then ℓ_{W_t}(γ) ≥ ℓ_{Ṽ_0}(γ). By Bers, the right-hand side equals log(dilatation of γ) for γ pseudo-Anosov.

*Proof.*
- (a) Holomorphic maps decrease Kobayashi pseudo-distances, and k_{T_g} = d_T (Royden, cited). So d_T(F z, ρ(γ)^n F z) = d_T(F z, F(γ^n z)) ≤ k_W(z, γ^n z). Divide by n and let n → ∞.
- (b) Ṽ_0 is a smooth complex surface, totally geodesic for d_T, which is uniquely geodesic (Teichmüller).
  - So Ṽ_0 is geodesically convex, and it contracts to a point along geodesics. Hence it is contractible.
  - For x ≠ y in Ṽ_0, the Teichmüller disc D containing the geodesic [x,y] is the union of the geodesics through x in the directions e^{iθ}v.
  - These directions are tangent to Ṽ_0, because T_xṼ_0 is a complex subspace. So D ⊂ Ṽ_0: the geodesics stay in Ṽ_0 by total geodesy, and analytic continuation does the rest.
  - D is a holomorphic isometric copy of the disc with its Kobayashi metric. So k_{Ṽ_0}(x,y) ≤ k_D(x,y) = d_T(x,y), and the reverse inequality is contraction.
  - Then ℓ_{Ṽ_0}(γ) = lim d_T(x, γ^n x)/n = ℓ_T(γ). ∎

**Meaning.** In the Kobayashi sense, every V_t is at least as "long" as V_0, in every direction the monodromy sees. For a curve in place of a surface, this plus Thurston's theorem forces rigidity (§3). For complex surfaces no analogue of Thurston's theorem is known to me. That is precisely the missing global tool.

---

## 3. Lemma 3 (Teichmüller curves of V_0 cannot be deformed into V_t) — proved modulo cited theorems

**Lemma 3.** Let C ⊂ V_0 be a Teichmüller curve, with normalisation C^ν, a hyperbolic Riemann surface of finite type. Let C′ ⊂ M_g be an algebraic curve with a homeomorphism ψ : C^ν → C′^ν that preserves punctures and such that incl_{C′}∘ψ ≃ incl_C as maps into M_g. Then C′ = C.

*Proof.*
- Lift to Teichmüller space. By Lemma 2(a) applied to the universal cover of C′^ν, ℓ_{C′}(γ) ≥ ℓ_T(ρ(γ)) = ℓ_C(γ) for every γ.
  - ℓ denotes hyperbolic length in the Kobayashi normalisation (curvature −4).
  - For C, the equality holds because C is an isometric Teichmüller disc quotient.
- Thurston's theorem (cited from memory, "Minimal stretch maps"): for marked finite-area hyperbolic surfaces X, X′ of the same type, if ℓ_{X′}(γ) ≥ ℓ_X(γ) for all simple closed γ, then X′ = X. Hence ψ is homotopic to an isometry, so C′^ν ≅ C^ν compatibly with the markings.
- The monodromy of a Teichmüller curve contains pseudo-Anosovs, so it is infinite. Imayoshi–Shiga (§1) then gives that the two maps coincide. ∎

(This is, as far as I remember, McMullen's argument for the rigidity of Teichmüller curves.)

**Corollary 3′.**
- If V_t ≠ V_0, then V_t ∩ V_0 contains only finitely many curves. In particular V_t contains at most finitely many of the Teichmüller curves of V_0.
- No holomorphic curve of V_t is a "deformation" of any other Teichmüller curve of V_0 in the sense of Lemma 3.
- So the Teichmüller curves of V_0 are not carried along the family. Their homotopy classes in V_t contain no holomorphic representative.

*Proof.*
- An analytic subset of the compact closure(V_0) ∩ closure(V_t) has finitely many components.
- If it had a 2-dimensional component, then V_t ⊃ V_0 (by irreducibility and smoothness), hence V_t = V_0, because V_t is closed in M_g and 2-dimensional and connected. ∎

This holds for every smooth closed totally geodesic V_0, so a counterexample needs a family V_t that "forgets" all the (infinitely many, when V_0 is a covering construction or one of the primitive examples) Teichmüller curves of V_0. That is not a contradiction: rigid curves (negative normal bundle in V_0) generally do not deform. But it rules out any construction of V_t that carries a Teichmüller-curve fibration or foliation of V_0 along.

---

## 4. The symmetric-locus candidates (the brief's suggested class)

Let h ∈ Mod_g have finite order. Let Z_h be the locus of curves with an automorphism conjugate to h; it is closed and algebraic (cited). Suppose V_0 is an **irreducible component** of Z_h. This is the case for Galois covering constructions over M_{0,5} or M_{1,2}, where the quotient orbifold has a 2-dimensional Teichmüller space.

**Lemma 4.**
- (a) If V_t ⊂ Z_h for all small t, then V_t = V_0. So any non-trivial admissible deformation has V_t ⊄ Z_h for t ≠ 0 small (t in a set accumulating at 0, hence for all t off a discrete set). Then V_t ∩ Z_h is an analytic subset of V_t of dimension ≤ 1.
- (b) Locally, such a deformation is possible as far as the coarse conditions go. At a generic z ∈ V_0 with Aut(z) = ⟨h⟩, h of order 2 acting by −1 on a normal coordinate w, the 3-fold 𝒱 = {W = t²} (coarse coordinate W = w²) satisfies:
  - 𝒱 is smooth;
  - t is a submersion on 𝒱;
  - the central fibre is reduced;
  - V_t = {w = ±t} carries no symmetry.
- (c) At the level of M_g[ℓ], the lift of such a deformation is a family of the h-fixed component V_0′ in which h does not act on the components X of the preimage (hX ≠ X). Its leading term is a section of the h-anti-invariant part N^− of the normal bundle N_{V_0′/M_g[ℓ]}. The invariant part is zero, because V_0′ is a full component of Fix(h).

*Proof.*
- (a) Z_h has finitely many irreducible components near closure(V_0), and V_0 is one of them, of dimension 2.
  - If V_t ⊂ Z_h, then V_t lies in a component of Z_h (V_t is irreducible).
  - By continuity of the family (R1), and since the components of Z_h meeting a neighbourhood of a generic point of V_0 are only V_0, that component is V_0. Generic points of V_0 lie on no other component.
  - So V_t ⊂ V_0, and V_t = V_0 by dimension and closedness.
  - The set of t with V_t ⊂ Z_h is analytic in Δ (closure(𝒱) ∩ (Z̄_h × Δ) is analytic), so it is either all of Δ or discrete.
- (b) Direct check, as in round13_q4 §1.
- (c) Write X near (z,0) as the graph of w = Σ_j a_j(s) t^{j/m}. The leading coefficient a_{j₀} is a local section of N. It is anti-invariant because hX ≠ X, and X has to be swapped with hX. This is the statement of §5 specialised. ∎

**Consequence for (NRT_P) in this class.**
- For V_0 ⊂ Z_h, every boundary point Q of V_0 has h (more precisely, a degeneration of h) in Aut(Q).
- A non-trivial deformation must break this symmetry at the generic points of V_t, by (a). The brief's isotropy drop at Q is then automatic for a = h, provided h survives as a label-moving automorphism at Q.
- So in this class, the isotropy-drop ingredient costs nothing. The whole difficulty is the existence of the deformation.
- I could not decide whether a covering-construction surface over M_{0,5} or M_{1,2} admits one. The question is equivalent (by §5) to the existence of a holomorphic section, with the boundary behaviour imposed by (R2), of Sym^k N^− on V_0′ that integrates to an actual family.

---

## 5. Leading-term obstruction (sketch, with stated hypotheses)

**Proposition 5 (sketch).** Let V_0′ be a component of the preimage of V_0 in M_g[ℓ], a smooth surface, with normal bundle N (rank 3g−5). Suppose V_t ≠ V_0. Then for some k ≥ 1, the bundle Sym^k N has a non-zero holomorphic section on V_0′.

*Sketch.*
- At a generic point z of V_0′, the preimage of 𝒱 is a finite union of 3-folds through V_0′ × {0}. In normal coordinates w ∈ C^{3g−5}, its fibre over t is a finite union of multivalued graphs w = a_b(s) t^{e/m} + o(t^{e/m}), for b in a finite index set. Here e/m is the smallest exponent that occurs, and some a_b ≢ 0. This uses Puiseux in t, uniformly in s on a dense open set.
- The leading coefficients {a_b(s)} form a local multisection of N. They are permuted by monodromy in t and by the deck group, and are well defined up to roots of unity.
- So the polynomial P(ξ) = ∏_b ⟨ξ, a_b⟩ on N^* is a well-defined local section of Sym^k N, with k the number of branches. It does not depend on the coordinates up to higher-order terms. It glues to a meromorphic section on the dense open set, and it extends holomorphically by Riemann extension across the analytic sets where it is locally bounded.
- It is non-zero because some a_b ≢ 0. ∎

Gaps in this sketch:
1. The behaviour at ∂V_0 (in closure(V_0′) ⊂ M̄_g[ℓ]): (R2) should give a log/zero condition, but I have not derived it.
2. The extension across the locus where the number of branches jumps.

**Why this matters.** The positivity theory of Teichmüller curves points towards vanishing of such sections. That theory is cited from memory and only in spirit: the Kobayashi/Teichmüller Finsler metric makes T M_g|_V "non-positive" in normal directions, and Möller-type maximal-Higgs results hold for Teichmüller curves. If H^0(V_0′, Sym^k N(−log-boundary)) = 0 for all k, then by Prop. 5 every smooth totally geodesic surface would be rigid, and the problem would be vacuously true. I could not prove this vanishing for surfaces.

---

## 6. Verdict, and what remains open

**Not refuted.**

What a counterexample to (NRT_P) (hence to the problem) needs, and the status of each ingredient:
1. Chart-level: rigid twin, isotropy drop, detaching mirror (FC2 / case II). Already realised in models (round13_q3 §1, round13_q4 §1, round13_q6 §3) consistent with (R1), (R2). **Buildable.**
2. Isotropy drop globally. For V_0 a component of a symmetric locus Z_h, it is *forced* by any non-trivial deformation (Lemma 4(a)). **Not an obstruction.**
3. **A non-trivial global deformation of a smooth closed totally geodesic surface satisfying (R1), (R2). Not buildable with present tools; this is the missing ingredient.** Any such deformation must meet all of the following:
   - vary the complex structure of V_t (Lemma 1);
   - have non-decreasing stable Kobayashi translation lengths for every monodromy element (Lemma 2);
   - carry along none of the Teichmüller curves of V_0, except finitely many fixed ones (Lemma 3, Cor. 3′);
   - for symmetric V_0, break the symmetry at generic points (Lemma 4);
   - come from a non-zero section of some Sym^k N on the level cover (Prop. 5, sketch).
   I know of no example of a totally geodesic surface meeting these, and I could not prove that none exists.

**Proved:** Lemma 2, Lemma 4(a)(b), Cor. 3′ (given Lemma 3). Proved modulo cited theorems (Imayoshi–Shiga rigidity, Thurston's stretch theorem, Royden's theorem, Bers' translation-length formula, all from memory): Lemmas 1 and 3. The lifting to M_g[ℓ] in Lemma 1 is not checked in detail.

**Sketched only:** Lemma 4(c) and Prop. 5. The boundary condition and the extension across the branch-jump locus are not derived.

**Open (named):**
- **(RigTG)** Is every smooth closed totally geodesic surface V_0 ⊂ M_g rigid under deformations satisfying (R1), (R2)? If yes, (NRT_P) and the problem hold vacuously. A natural route is a 2-dimensional analogue of Lemma 3: a Thurston-type theorem for Kobayashi translation lengths of families of complex surfaces, or the vanishing H^0(V_0′, Sym^k N(−∂)) = 0.
- (RigTG) for the covering-construction surfaces over M_{0,5} and M_{1,2}, and for the primitive examples (the flex locus and the gothic family; their exact identification is cited from memory): undecided.
- (NRT_P) itself and (Rig) (entry 82): unchanged, open.

=== END OF ANSWER round14_q4 ===
