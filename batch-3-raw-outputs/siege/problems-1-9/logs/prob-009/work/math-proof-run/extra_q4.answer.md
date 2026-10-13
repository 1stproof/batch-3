# Answer to extra_q4: finiteness of holomorphic maps R -> M_{h,m}[N]

## What is proved

**Theorem (stronger than (IS_marked)).** Let (h,m) satisfy h >= 1, m >= 1, 2h-2+m > 0, let N >= 3, and let R be a Riemann surface of finite type. Then the set of *all* non-constant holomorphic maps R -> M_{h,m}[N] is finite.

So for every free homotopy class 𝔥 the set of non-constant holomorphic maps in 𝔥 is finite. That is (IS_marked), and (IS_count) follows. **(IS_rig) is not proved and not claimed.**

The proof uses only the following.
- **(C1)** The Imayoshi–Shiga finiteness theorem for families of **closed** surfaces (cited from memory, stated in §1).
- **(C2)** The standard fact that a finite regular branched covering induces a holomorphic injective map of Teichmüller spaces (cited, stated in §2, with a proof sketch).
- **(C3)** Serre's lemma: Mod_g[N], N >= 3, is torsion-free.

No statement about families of punctured surfaces is used. The proof also works for (h,m) = (1,1), and for any hyperbolic (h,m) once the ramification orders are chosen large enough. It does not use the homotopy class at all.

On the scope of Imayoshi–Shiga: I believe, with moderate confidence (about 65%), that the MSRI Publ. 11 (1988) paper is itself stated for "holomorphic families of Riemann surfaces of type (g,n)". If so it would give the theorem directly. The argument below avoids that question and reduces everything to the closed case.

---

## 0. Trivial case and conventions

If R is not hyperbolic, its universal cover is C or P^1. By the Bers embedding, T_{h,m} is biholomorphic to a bounded domain in C^{3h-3+m}. A lift of a holomorphic map R -> M_{h,m}[N] to universal covers is therefore constant (Liouville, or compactness for P^1). So every holomorphic map R -> M_{h,m}[N] is constant, and the set in question is empty.

From now on R = D/Π, where D is the unit disc and Π ≅ π_1(R) is a Fuchsian group. Π is finitely generated because R has finite type.

Write T = T_{h,m}, PMod = PMod_{h,m}, and M = M_{h,m}[N] = T/Mod_{h,m}[N]. Mapping classes act on T by [X, φ] ↦ [X, φ∘ψ^{-1}], where φ: (Σ_0, P) -> (X, P_X) is a marking. Here Σ_0 is a closed genus-h surface, P ⊂ Σ_0 is a set of m labelled points, and S_0 = Σ_0 \ P.

## 1. The closed case

**Cited theorem (C1) (Imayoshi–Shiga 1988; cited from memory; the closed-fibre version is certainly covered).** Let B be a Riemann surface of finite type and g >= 2. Then there are only finitely many isomorphism classes, over B, of locally non-trivial holomorphic families of closed Riemann surfaces of genus g over B.

- A holomorphic family is a proper holomorphic submersion π: 𝓜 -> B from a complex surface, with fibres of genus g.
- Locally non-trivial means that over no non-empty open subset of B are all the fibres biholomorphic to each other.

The same finiteness also follows from the Parshin–Arakelov theorem, once one knows that the families are algebraic. I do not need that route.

**Lemma 1.** Let B be of finite type, g >= 2 and N' >= 3. Then there are only finitely many non-constant holomorphic maps B -> M_g[N'].

*Proof.*

1. **M_g[N'] is a fine moduli space.** Mod_g[N'] acts freely on T_g by (C3). It therefore acts freely on the Teichmüller curve, and the quotient is a universal curve C -> M_g[N']; this is a proper holomorphic submersion. As a set, M_g[N'] = {(X, α)}/iso, where α is a symplectic isomorphism (Z/N')^{2g} -> H_1(X, Z/N'). Indeed, two markings of X inducing the same α differ by an element of Mod_g[N'].

2. **Non-constant maps give locally non-trivial families.** Let F: B -> M_g[N'] be holomorphic and non-constant. Then the composite B -> M_g is non-constant, because M_g[N'] -> M_g has finite fibres and B is connected. By the identity theorem it is non-constant on every open set. Hence F^*C is locally non-trivial.

3. **Isomorphic families give maps differing by Sp(2g, Z/N').** Suppose F_1^*C ≅ F_2^*C over B via Θ. Each F_i comes with a continuous level structure α_i(b) on the fibre over b, that is, a section of the finite covering space of symplectic frames of H_1(X_b, Z/N'). Then σ(b) := α_1(b)^{-1} ∘ Θ_b^{-1} ∘ α_2(b) is a continuous map into the finite group Sp(2g, Z/N'). It is therefore constant, say σ, and F_2 = σ·F_1, where σ acts by (X, α) ↦ (X, α∘σ).

4. **Count.** By (C1) there are finitely many families, and each family arises from at most |Sp(2g, Z/N')| maps. ∎

## 2. The branched-cover construction

**Step 2a (a characteristic subgroup).** Let π = π_1(S_0). It is free of rank 2h+m-1 >= 2. Let c_1, ..., c_m be loops around the punctures; each is non-trivial in π.

- π is residually finite, so for each j there is a normal subgroup K_j of finite index with c_j ∉ K_j. Let d be the largest of these indices.
- Let K be the intersection of all subgroups of π of index <= d. There are finitely many such subgroups, since π is finitely generated.
- K is characteristic in π, has finite index, and no c_j lies in K.

Let G = π/K, and let n_j >= 2 be the order of the image of c_j in G.

**Step 2b (the covering of a pointed curve).** For a pointed curve (X, P_X) of type (h,m), let Y° -> X \ P_X be the regular G-cover corresponding to K. It is canonical because K is characteristic, and it is unique up to deck transformations. Fill in the ends to get a compact Riemann surface Y_X with a branched G-cover Y_X -> X. This cover is branched exactly over P_X, with order n_j over x_j.

By Riemann–Hurwitz, 2h'-2 = |G|·(2h-2 + Σ_j (1 - 1/n_j)) > 0, because h >= 1 and m >= 1. So the genus h' of Y_X satisfies h' >= 2. In particular Aut(Y_X) is finite (Hurwitz).

**Step 2c (the map Φ and lifts of mapping classes).** Fix Y_0 -> Σ_0 for the base point. Define Φ: T_{h,m} -> T_{h'} by [X, φ] ↦ [Y_X, φ̃], where φ̃ is any lift of φ.

- Lifts exist because φ_*(K) = K (K is characteristic).
- Two lifts differ by a deck transformation, which is conformal on Y_X, so they define the same point of T_{h'}.
- An isotopy rel P lifts to an isotopy.

Every ψ ∈ PMod lifts to Y_0. Its lifts form a coset ψ̃G in Mod(Y_0), where G ⊂ Mod(Y_0) is the group of deck classes. G injects into Mod(Y_0), because a non-trivial conformal automorphism of a surface of genus >= 2 is not isotopic to the identity.

The set L of all lifts is a subgroup, and L -> PMod is surjective with kernel G. Directly from the definitions, **Φ(ψ·p) = ψ̃·Φ(p)** for every lift ψ̃ of ψ.

**Cited fact (C2) (standard; e.g. MacLachlan–Harvey 1975, Birman–Hilden; also Nag's book, Bers–Greenberg).** Φ is holomorphic and injective. In fact it is a Teichmüller-isometric embedding onto Fix(G).

*Sketch of proof.*
- Uniformize the orbifold (Σ_0, cone order n_j at x_j) by a cocompact Fuchsian group Γ_0. The orbifold is hyperbolic, since 2h-2+Σ(1-1/n_j) > 0. Then Y_0 = H/Γ_Y, where Γ_Y = ker(Γ_0 -> G).
- In Bers' model, T(Γ) is the space of Γ-compatible Beltrami coefficients modulo the relation "w^μ = w^ν on R". By Bers–Greenberg, T(Γ_0) ≅ T_{h,m}; also T(Γ_Y) ≅ T_{h'}. Both identifications are compatible with markings.
- Under these identifications Φ is the inclusion [μ] ↦ [μ]. This inclusion is injective because the equivalence relation is the same in both spaces.
- It is holomorphic because in the Bers embedding it is the restriction of the linear inclusion B_2(Γ_0) ⊂ B_2(Γ_Y).

I am confident in this fact.

**Step 2d (choosing levels).** Fix N' >= 3. Let Λ := L ∩ Mod(Y_0)[N']; it has finite index in L. Since Mod(Y_0)[N'] is torsion-free (C3) and G is finite, Λ ∩ G = 1. So Λ maps isomorphically onto a finite-index subgroup Γ'' ⊂ PMod. Let λ: Γ'' -> Λ ⊂ Mod_{h'}[N'] be the inverse isomorphism; then Φ(ψp) = λ(ψ)Φ(p) for ψ ∈ Γ''.

Let Γ_1 be the normal core in PMod of Γ'' ∩ Mod_{h,m}[N]. Then Γ_1 is normal in PMod, of finite index, torsion-free, and contained in Mod_{h,m}[N]. Put M_1 := T/Γ_1. This is a complex manifold and a finite unramified cover q: M_1 -> M.

Define Ψ: M_1 -> M_{h'}[N'] by Γ_1 p ↦ Mod_{h'}[N']·Φ(p). It is well defined by the equivariance in Step 2d, and holomorphic because locally it is Φ read in covering charts.

**Lemma 2.** (a) Ψ is locally injective. (b) Ψ has finite fibres.

*Proof.*

(a) Let x = Γ_1 p.
- Choose a neighbourhood W of Φ(p) on which the covering T_{h'} -> M_{h'}[N'] is injective.
- Choose a neighbourhood U of p on which T -> M_1 is injective and with Φ(U) ⊂ W.
- On U, Ψ∘(projection) = (projection)∘Φ, and the right-hand side is injective on U because Φ is injective (C2).
- Hence Ψ is injective on the open set image(U) ∋ x.

(b) Suppose Ψ(Γ_1 q) = Ψ(Γ_1 p).
- Then Y_q ≅ Y_p via some conformal c. Hence Σ_q ≅ Y_p / (c G_q c^{-1}), and the iso carries the labelled points x_j(q) to branch points of this quotient.
- Aut(Y_p) is finite and has finitely many subgroups, and there are finitely many labellings. So the pointed curve [Σ_q, x(q)] ∈ M_{h,m} lies in a finite set.
- The map M_1 -> M_{h,m} has fibres of size at most [PMod : Γ_1] < ∞. ∎

## 3. Proof of the Theorem

Let f: R -> M be holomorphic and non-constant.

**Step 1 (the homomorphism ρ_f).** Choose a lift f̃: D -> T. Since Mod_{h,m}[N] acts freely as the deck group, there is a homomorphism ρ_f: Π -> Mod_{h,m}[N] with f̃∘γ = ρ_f(γ)∘f̃. Changing the lift conjugates ρ_f.

**Step 2 (finitely many intermediate covers).** Since Γ_1 is normal, H_f := ρ_f^{-1}(Γ_1) is the kernel of the induced map Π -> Q := Mod_{h,m}[N]/Γ_1. Q is a finite group and Π is finitely generated, so there are finitely many homomorphisms Π -> Q. Hence H_f ranges over a finite set {H_1, ..., H_s} of finite-index subgroups.

It therefore suffices to fix H = H_k and to show that the set 𝓕_H of non-constant f with H_f = H is finite.

**Step 3 (lifting f to R').** Let R' = D/H. It is a connected finite unramified cover p_H: R' -> R, so it has finite type and is hyperbolic.

For f ∈ 𝓕_H, fix one lift f̃. It descends to a holomorphic f': R' -> M_1 with q∘f' = f∘p_H. Since p_H is surjective, f' determines f. So f ↦ f' is injective on 𝓕_H.

**Step 4 (the composite F' is non-constant).** Let F' := Ψ∘f': R' -> M_{h'}[N']. If F' were constant, then Φ∘f̃ would take values in a single Mod_{h'}[N']-orbit. That orbit is discrete, because the action is properly discontinuous, and D is connected, so Φ∘f̃ would be constant. Since Φ is injective, f̃ would be constant, and so would f, a contradiction.

**Step 5 (finitely many values of F').** By Lemma 1 applied to B = R' and g = h', there are only finitely many possible F'.

**Step 6 (finitely many f' over each F').** Fix F', and let f'_a, f'_b: R' -> M_1 be continuous maps with Ψ∘f'_a = Ψ∘f'_b = F'. Let E = {r : f'_a(r) = f'_b(r)}.
- E is closed, since M_1 is Hausdorff.
- E is open by Lemma 2(a): near a point of E both maps take values in a neighbourhood on which Ψ is injective.
- R' is connected, so either f'_a = f'_b or the two maps disagree at every point.

Fix r_0 ∈ R'. Distinct lifts then take distinct values in Ψ^{-1}(F'(r_0)), which is finite by Lemma 2(b). So there are finitely many f' over each F'.

**Conclusion.** Combining Steps 3–6, 𝓕_H is finite. Hence the set of all non-constant holomorphic maps R -> M_{h,m}[N] is finite. ∎

## 4. Status and remarks

**Proved.** The Theorem: absolute finiteness, hence (IS_marked) and (IS_count). This is modulo the cited results (C1) (closed-fibre Imayoshi–Shiga), (C2) (branched covers induce holomorphic injections of Teichmüller spaces; Bers–Greenberg and the Bers model) and (C3) (Serre). All three are cited from memory as stated above.

**Notes on the steps.**
- The restriction to a homotopy class is not needed.
- The "constant coordinate" danger flagged in the task (a continuous family with one constant coordinate) cannot occur. Any such continuum of non-constant maps would give infinitely many maps, which contradicts the finiteness.
- The forgetful-map route was not needed.

**Not proved / open here.**
- (IS_rig), that is, uniqueness within a homotopy class.
- Whether the original Imayoshi–Shiga paper covers type (g,n) directly. I believe it does (moderate confidence), but nothing above depends on it.

=== END OF ANSWER extra_q4 ===
