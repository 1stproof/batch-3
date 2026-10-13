# Task: can an admissible deformation change the automorphism groups of boundary curves? (the last open case of the problem)

**Background.** A long document attacks the problem stated after this query. It fixes readings (R1), (R2) of the hypotheses (Excerpt 1). Its main results, which you may use as black boxes, are:

- **Theorem A′ (proved there; take as given).** Assume (R1), (R2) and
  **(AP)** |Aut(H_t(z))| = |Aut(z)| for every z ∈ B_0 := closure(V_0) ∖ V_0 and every t with |t| < r (some r > 0),
  where H is the trivialisation of (R2) and Aut(z) is the automorphism group of the stable curve z. Then Y_t = Y_0 for all t ∈ Δ.
  (The proof: (R2) + (AP) is equivalent, by a path-lifting argument at constant isotropy order, to an "orbifold" form (R2^orb) of the trivialisation, in which H lifts on every boundary stratum to a continuous, mapping-class-equivariant, stabiliser-preserving map of Teichmüller spaces; under (R2^orb) a long argument using total geodesy of V_0 gives the claim.)
- **Corollary C.5 (consequence).** Under (R1), (R2), if no point of B_0 has a non-trivial automorphism, the claim holds (because the locus of curves with non-trivial automorphisms is closed in M̄_g, so (AP) holds for small |t| by compactness).
- **Theorem B (proved there; take as given).** Under (R1), (R2) and a rigidity hypothesis (Rig), the claim holds unless the statement (NRT_P) fails; and a failure of (NRT_P) forces an *isotropy drop* |Aut(H_t(Q))| < |Aut(Q)| for all small t ≠ 0, at a "puncture point" Q ∈ B_0 that has two distinct components isomorphic (with special points) to Y_0, exchanged by an automorphism of Q, lying in a stratum not of product type. (Definitions in Excerpt 4.)
- A chart-level model (Excerpt 3) shows that, *locally*, a stratum-preserving trivialisation can drop isotropy: a curve of symmetric boundary points can be moved off the symmetric locus. So any proof that (AP) holds must be global and must use total geodesy of V_0 (local arguments near the boundary are known not to suffice).

So the problem is open exactly in the situation where the trivialisation changes the automorphism order of boundary points arbitrarily close to t = 0.

**Your task.** Settle as much as you can of the following, in decreasing order of value. Give complete proofs of anything you claim; mark clearly anything you only sketch.
1. **Prove (AP) on a small disc**, for every family satisfying the problem's hypotheses (V_0 smooth, closed, 2-dimensional, totally geodesic; (R1), (R2); the dimension and constant-factor hypotheses may be used if helpful). Or prove a weaker statement that still feeds Theorem A′: for example, that the trivialisation H can be *replaced* by another trivialisation H′ satisfying (R2) and (AP) (the problem only asserts existence of some trivialisation, so changing H is allowed as long as (R2) holds for H′). Note: (AP) concerns the family of sets closure(V_t) ∩ Δ_G only through H; think about whether the *sets* B_t (with their isotropy stratifications {z : |Aut z| ≥ k} ∩ B_t) form an isotropy-equisingular family, and whether a trivialisation respecting the isotropy stratification can then be chosen.
   - Useful structure: B_0 is a compact complex curve (union of finitely many irreducible components, "pieces", each a curve in some stratum, plus finitely many points); by the Part I results (Excerpt 2), the normalisation of every piece of B_0 is H/Λ for a lattice Λ, and on it one vertex (the "Teichmüller vertex") traces a Teichmüller curve. The isotropy locus {|Aut| ≥ k} ∩ closure(V_t) is a closed analytic subset for every t, and {(z,t) : z ∈ closure(V_t), |Aut z| ≥ k} is closed analytic in M̄_g × Δ by (R1).
   - Two distinct mechanisms must be excluded (or shown harmless): (α) a whole piece of B_0 lies in a locus {|Aut| ≥ k} that the transported piece leaves for t ≠ 0 ("curve drop"); (β) an isolated point of B_0 (a puncture point / node of B_0) has more automorphisms than its transport ("point drop"); and the reverse (isotropy rise). For each, decide whether total geodesy excludes it, whether it can be removed by re-choosing H, or whether it can genuinely occur.
2. If (AP) cannot be proved in general, **prove the claim directly in the presence of isotropy change**, or reduce it further, using Theorem A′, Corollary C.5 and Theorem B as black boxes.
3. If you believe isotropy change can occur for an admissible deformation of a totally geodesic surface (with or without the constant-factor hypothesis), **construct an example** or give strong evidence; say whether it yields a counterexample to the problem.

**Output format.** Start with a short summary of what you proved (precise statements), then full proofs, then sketches and evidence clearly marked as such.

---

## Excerpt 1: setting and readings (document §1)

## 1. Setting and readings

- **Spaces.**
  - M̄_g is the coarse Deligne–Mumford space, a normal projective variety.
  - Δ_G is the stratum of stable curves with dual graph G.
  - ξ_G : ∏_{w∈V(G)} M_w → Δ_G is the finite gluing map, with M_w = M_{g_w,n_w} and the special points labelled by the half-edges at w.
  - Δ_G is *of product type* if ξ_G is injective. By hypothesis Δ_Γ is of product type, and Δ_Γ ≅ ∏_j M_{g_j,n_j}.
- **V_0 and the family.** V_0 ⊂ M_g is smooth, 2-dimensional and totally geodesic. We read "subvariety" as closed and irreducible, so V_0 is closed in M_g and connected. 𝒱 ⊂ M_g × Δ is the total space of the family, and V_t its fibres.
- **Closures and boundaries.** All closures are taken in M̄_g or M̄_g × Δ. B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g, and ∂V_t := closure(V_t) ∩ Δ_Γ.
- **Classes.** 𝔐 := M_{g_i,n_i}/S_{n_i} (marked points unordered), and [Z] ∈ 𝔐 denotes the class of an n_i-pointed curve Z of type (g_i,n_i).
- **The hypothesis.** dim ∂V_t = 1 and π_i(∂V_t) = {Y_t}. If dim M_{g_i,n_i} = 0 there is nothing to prove, so we assume dim M_{g_i,n_i} ≥ 1 throughout.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- **(R2)** (the coarse reading). There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ, written H(z,t) = (H_t(z), t), such that:
  - H is smooth on V_0 × Δ;
  - H_0 = id;
  - for every stratum G, including the open stratum M_g, H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ).

  (R2) encodes "smoothly trivial" together with (i) and (ii) as one stratum-preserving trivialisation. This is a reading: literally, (i) and (ii) give trivialisations stratum by stratum together with the compatibility (ii). Under (R2), H_t need not preserve automorphism groups of boundary points.
- **(R2^orb)** (the embedded orbifold reading) strengthens (R2). It is defined in Part II §1.3 and used only for Theorem A.
- **(AP)** (automorphism orders preserved): |Aut(H_t(z))| = |Aut(z)| for all z ∈ B_0 and all t ∈ Δ. By Part II Theorem 7.5, (R2) + (AP) ⇔ (R2^orb).
- **Algebraicity.** By (R1) and Chow's theorem, closure(V_t) is a projective algebraic subset of M̄_g.

---

## Excerpt 2: Part I input in the forms used (document Part II §1.6), with the Kuranishi chart facts (Part II §1.4) and Lemma 2.5

### 1.4 Kuranishi charts (classical facts, cited as (Kur), (K2), (PN); precise statements at the end)

Let J be a stable curve with dual graph G_J.
- **(Kur)** There is a universal deformation over a smooth germ Def(J), on which Aut(J) acts.
  - Part of the coordinates are smoothing parameters s_e, e ∈ E(G_J). The node e persists in the fibre X_p iff s_e(p) = 0.
  - The dual graph of X_p is canonically G_J/{e : s_e(p) ≠ 0}.
  - For a sufficiently small Aut(J)-invariant ball B ⊂ Def(J), the map q : B → M̄_g, p ↦ [X_p], induces an isomorphism of analytic spaces from B/Aut(J) onto an open set q(B). Moreover, for every p ∈ B, restriction gives an isomorphism Stab_{Aut(J)}(p) ≅ Aut(X_p).
  - In particular q^{-1}(q(p)) ∩ B = Aut(J)·p, and q^{-1}(J) ∩ B = {0}.
- **(K2)** For a vertex x of G_J, put L_x := {s_e = 0 for every edge e at x}. Over L_x ∩ B the fibres have a smooth component labelled x, whose special points are labelled by the half-edges at x. This gives a holomorphic map comp_x : L_x ∩ B → M_{g_x,n_x}.
- **(PN)** For S ⊂ E(G_J), put L_S := {s_e = 0 for all e ∈ S} and G_S := G_J/(E(G_J) ∖ S). Partial normalisation of the fibres along the nodes in S gives a holomorphic map Π_S : L_S ∩ B → ∏_{w∈V(G_S)} M̄_w with the following properties.
  - (PN1) If p has pattern exactly S, i.e. {e : s_e(p) = 0} = S, then Π_S(p) ∈ ∏_w M_w and ξ_{G_S}(Π_S(p)) = q(p).
  - (PN2) If p ∈ L_S lies in the deepest locus {s_e = 0 for all e}, then the w-coordinate of Π_S(p) is the stable curve glued from the comp_y(p), y ∈ w, along the edges of E(G_J) ∖ S inside w.
  - (PN3) If x is **intact** for S (every edge at x lies in S), then {x} is a vertex of G_S, and pr_{{x}}∘Π_S = comp_x on L_S ∩ B.
  - Given an isomorphism ι : G_S → G onto a reference graph, write Π_{S,ι} for Π_S followed by the induced relabelling ∏_{w∈V(G_S)} M̄_w → ∏_{w∈V(G)} M̄_w. Then (PN1) reads ξ_G∘Π_{S,ι} = q on the pattern-S locus.

### 1.5 Branches, lifts, patterns, labels

Let J ∈ B_0.
- **Branch.** A branch of B_0 at J is a local irreducible component β of the germ of B_0 at J. In a small neighbourhood:
  - β ∖ J is a punctured disc lying in a single stratum Δ_{G_β} (the strata meet β∖J in analytic subsets, one of which is open and dense; shrink);
  - distinct branches meet only at J.
- **(P).** We say **(P) holds for β** if J ∉ Δ_{G_β}, i.e. J is a puncture of the piece containing β∖J.
- **Lift.** A lift β̃ of β is an irreducible component at 0 of q^{-1}(β) in Def(J). For B small, β̃ ∩ B is irreducible and β̃ ∖ 0 is connected.

**Lemma 1.1 (patterns) [none].** For p ∈ B put S(p) := {e : s_e(p) = 0}. Then on q^{-1}(Δ_{G′}) ∩ B, for any stratum G′, S(·) is locally constant. Hence:
- every lift β̃ has a constant pattern S_β̃ on β̃ ∖ 0;
- G_{S_β̃} ≅ G_β.

*Proof.*
- Near p_0, s_e ≠ 0 for every e ∉ S(p_0), so S(p) ⊆ S(p_0).
- If q(p), q(p_0) ∈ Δ_{G′}, then |S(p)| = |E(G′)| = |S(p_0)|, because the number of nodes of X_p is |S(p)|.
- Hence S(p) = S(p_0). Since β̃ ∖ 0 is connected and lies in q^{-1}(Δ_{G_β}), the rest follows from (Kur). ∎

**Definition 1.2 (labelled lifts).** Let β̃ be a lift of a branch β at J, S := S_β̃, and x ∈ V(G_J). Let E be a piece at time 0 in the stratum G of β ∖ J, and c ∈ V(G). We say **(β̃, x) is labelled by (E, c)** if there is an isomorphism ι : G_S → G such that:
- x is intact for S and ι({x}) = c;
- Π_{S,ι}(β̃ ∖ 0) ⊂ E.

In that case, by (PN3), comp_x = ι^*(pr_c∘Π_{S,ι}) on L_S ∩ B, where ι^* is the relabelling of special points induced by ι on the half-edges at x. In particular [comp_x(p)] = [pr_c Π_{S,ι}(p)].

### 1.6 Part I input, in the precise forms used

The following are taken as given (proved in Part I). I.1, I.4 and Lemma PT are not used here.

**I.2 (Theorem TV, the part used).** Let G be a boundary stratum and E a piece of Â_0. Then there are a vertex j of G and a lattice Λ = Λ_E ⊂ PSL_2(ℝ) (of finite index in the Veech group Γ′ of a Teichmüller curve in M_j), such that Ê ≅ H/Λ as Riemann surfaces. We write u_0 : H → Ê for the quotient map.
- O_0 := H/Λ is regarded as a hyperbolic 2-orbifold. Its cone points c have orders e_c, its cusps are the punctures of Ê, and χ^orb(O_0) < 0.
- Ê is a compact Riemann surface minus finitely many points.

**I.3 (Lemmas CS, CL, J0).**
- **CL.** Let Γ be a countable group acting properly discontinuously by biholomorphisms on a complex manifold T, X := T/Γ with Cartan's quotient structure, and p : T → X the quotient map. Let Q be a connected Riemann surface, h : Q → X holomorphic, and L : Q → T continuous with p∘L = h. Then L is holomorphic.
- **J0** (valid in every boundary stratum, by Part I Supplement R3′). In the situation of I.2, there is a holomorphic F_0 : H → T_G with:
  - (i) p∘F_0 = ν∘u_0;
  - (ii) f_0 := pr_j∘F_0 : H → T_j is an isometric holomorphic embedding. Here H carries the Poincaré metric of curvature −4, T_j the Teichmüller metric, and the image is a Teichmüller disc;
  - (iii) for every λ ∈ Λ, the set R(λ) := {g ∈ Mod_Π : F_0∘λ = g∘F_0} is a coset gS of the finite group S := {s ∈ Mod_Π : s∘F_0 = F_0}. Moreover R(λ) ⊂ N(S), the normaliser, and R(λμ) = R(λ)R(μ).
  - Consequently λ ↦ R(λ) is a homomorphism Λ → N(S)/S.

**I.5 (Proposition K_w, walk chain; a statement about V_0 only; Part I §I.5 with Lemma L.1 of the Bridge section).** There are the following data.
- **(K-a) Pieces and constant vertices.** For m = 1, …, k: a boundary stratum G_m, a piece E^m of Â_0^{G_m}, and a vertex c_m ∉ M(E^m). Moreover G_1 = Γ, E^1 ⊂ Â_0^Γ = ∂V_0 (identified via ξ_Γ), and c_1 = i.
- **(K-b) Transitions.** For m = 1, …, k−1: a point J_m ∈ B_0, lifts β̃_m, β̃′_m at 0 ∈ Def(J_m) of branches of B_0 at J_m, and a vertex x_m of G_{J_m}, such that:
  - (β̃_m, x_m) is labelled by (E^m, c_m);
  - (β̃′_m, x_m) is labelled by (E^{m+1}, c_{m+1}).
- **(K-c) Endpoint.** A point Q_0 ∈ B_0, a lift β̃ at 0 ∈ Def(Q_0) and a vertex x of G_{Q_0} with (β̃, x) labelled by (E^k, c_k). Also a lift b̃ at 0 ∈ Def(Q_0) of a branch b of B_0 at Q_0 such that, with S_b := S_b̃, one of the following holds:
  - **MERGE:** x is not intact for S_b;
  - **MOV:** x is intact for S_b and [comp_x] is non-constant along b̃.

(This is the chain's "common chart label x_m" with the "marking identification x_m ↔ c ↔ x_{m+1}", made precise through Definition 1.2. The interior transitions coming from the finite sets R(D) are among the J_m. The requirement that both lifts at a transition lie in one irreducible component of q^{-1}(closure V_0) is part of I.5 but is not used here.)

**I.6 (Corollary IMOV_all, the part used).** In (K-c), (P) holds for b: Q_0 ∉ Δ_{G_b}.

---

**Lemma 2.5 (stabilisers are automorphism groups) [none].** Let x̂ ∈ T_G and Z := ξ_G p(x̂). Then Stab_{Mod_G}(x̂) ≅ Aut(Z), canonically.

*Proof.* Write x̂ = (C_w, f_w)_w.
1. **The homomorphism.**
   - g = (σ, (φ_w)) fixes x̂ iff for each w there is a biholomorphism α_w : C_w → C_{σ(w)}, isotopic to f_{σ(w)}∘φ_w∘f_w^{-1} and carrying the point labelled h to the point labelled σ(h).
   - α_w is unique, because a biholomorphism of a stable pointed curve isotopic to the identity is the identity (fact (Iso)).
   - Since σ respects the pairing of half-edges, ⊔_w α_w descends to an automorphism α(g) of Z. Then g ↦ α(g) is a homomorphism.
2. **Injective.** If α(g) = id, its lift to the normalisation ⊔_w C_w is the identity. It fixes each component and each preimage of each node, so σ = id on V(G) and H(G). Then each α_w = id, so φ_w is trivial.
3. **Surjective.** Let α ∈ Aut(Z).
   - α lifts to the normalisation. It permutes components and node preimages compatibly with the pairing, which defines σ ∈ Aut(G), with its action on half-edges, and biholomorphisms α_w : C_w → C_{σ(w)}.
   - Put φ_w := [f_{σ(w)}^{-1}∘α_w∘f_w]. Then g := (σ, (φ_w)) ∈ Mod_G fixes x̂, and α(g) = α. ∎

*Remark.* Let K_G be the kernel of the action of Mod_G on T_G. Then K_G ⊂ Stab(x̂) for every x̂. Correct examples of non-trivial elements of K_G:
- the elliptic involution of a (1,1)-vertex, extended by the identity;
- for a (1,2)-vertex whose two special points are the half-edges of a self-loop, the half-edge swap together with z ↦ p_1 + p_2 − z.

There are no (2,0)-vertices in boundary strata. Since every stabiliser contains K_G, condition (c) "modulo K_G" is equivalent to (c). None of this is used below.

---


## Excerpt 3: Theorem 7.5 and Remark 7.6, the chart-level isotropy-drop model and where the orbifold argument breaks (Part II §7–§8)

**Theorem 7.5 (preservation of automorphism orders implies (R2^orb)) [coarse (R2) + (AP); no use of (Loc)].** Assume (R2) and

- **(AP)** |Aut(H_t(z))| = |Aut(z)| for every boundary point z ∈ B_0 and every t ∈ Δ.

Then for every boundary stratum G there is a continuous H̃ : Ã_0 × Δ → T_G satisfying (a)–(d) of §1.3. Conversely, (R2^orb) implies (AP) (Prop. 5.1). Hence, under (R2), **(R2^orb) ⇔ (AP) ⇔ (Loc)**, and Theorem A holds under (R1) + (R2) + (AP).

*Proof.* Fix a boundary stratum G and write P := ξ_G∘p : T_G → Δ_G.

**0. Two facts about P.**
- (P1) P is continuous, surjective and open, and its fibres are the Mod_G-orbits. Indeed p is the quotient map of a group action, hence open; ξ_G is a finite, hence closed, surjective morphism whose fibres are the Aut(G)-orbits (St3, St4), so it is a quotient map whose fibres are orbits of a finite group, hence open; fibres by (St2).
- (P2) Let y ∈ T_G, A := Stab_{Mod_G}(y) (finite), and U a slice neighbourhood of y (St1). Then: (i) P(U) is open and P^{-1}(P(U)) = ⊔_{gA ∈ Mod_G/A} gU, a disjoint union; (ii) every u ∈ U has Stab(u) ⊂ A; (iii) U → P(U) is the quotient by A and is proper (preimages of compact sets are compact); (iv) if |Stab(u)| = |A| for some u ∈ U, then Stab(u) = A, i.e. u ∈ Fix(A); (v) P restricted to Fix(A) ∩ U is a homeomorphism onto P(Fix(A) ∩ U) = {z ∈ P(U) : |Aut(z)| = |A|}.
  - (i): P(U) is open by (P1). If gU ∩ g′U ≠ ∅ then g^{-1}g′ ∈ A, so the translates are disjoint or equal; a point over P(U) is h·u with u ∈ U, so lies in hU.
  - (ii): gu = u ∈ U gives gU ∩ U ≠ ∅, so g ∈ A.
  - (iii): two points of U with the same image are related by some g with gU ∩ U ≠ ∅, so g ∈ A. Properness: a finite group quotient map is proper.
  - (iv) follows from (ii), since the groups are finite.
  - (v): P is injective on Fix(A) ∩ U, because two points of U with the same image differ by an element of A, which fixes both. Fix(A) ∩ U is closed in U and A-saturated, and the quotient map U → U/A ≅ P(U) is closed, so its restriction to Fix(A) ∩ U is a closed continuous injection, i.e. a homeomorphism onto its image. By Lemma 2.5, |Aut(P(u))| = |Stab(u)|; so by (ii) and (iv) a point z ∈ P(U) has |Aut(z)| = |A| iff its lift in U lies in Fix(A).

**1. Path lifting at constant automorphism order.** Let c : [0,1] → Δ_G be continuous with |Aut(c(r))| = k for all r, and let x ∈ P^{-1}(c(0)). Then there is exactly one continuous γ : [0,1] → T_G with P∘γ = c and γ(0) = x. Moreover Stab(γ(r)) = Stab(x) for all r.
- *Local sections.* For r_* ∈ [0,1], pick y ∈ P^{-1}(c(r_*)), its stabiliser A (|A| = k by Lemma 2.5) and a slice U. By (P2)(v), σ := (P|_{Fix(A)∩U})^{-1} is a continuous section of P over the set {z ∈ P(U) : |Aut z| = k}, which contains c(r) for all r in an open interval J_{r_*} ∋ r_*. Replacing y by gy replaces U by gU and σ by gσ, with the same domain; so J_{r_*} depends only on r_*, and through every point over c(r_*) passes one of these sections.
- *Existence.* Choose 0 = r_0 < ⋯ < r_m = 1 such that each [r_{l−1}, r_l] lies in some J_{r_*} (Lebesgue number). Lift successively: on [r_{l−1}, r_l] use the translate of the section passing through the already constructed point over c(r_{l−1}).
- *Constant stabiliser.* Near any r_1, γ(r) lies in a slice U of γ(r_1) and has stabiliser of order k = |Stab(γ(r_1))|, hence equal to Stab(γ(r_1)) by (P2)(iv). So r ↦ Stab(γ(r)) is locally constant, hence constant.
- *Uniqueness* is Lemma 7.1, whose hypothesis (locally constant stabiliser) has just been checked for any such lift.

**2. Definition of H̃.** For x ∈ Ã_0 and t ∈ Δ, the path c_{x,t}(r) := H_{rt}(P(x)), r ∈ [0,1], is continuous, lies in Δ_G because H preserves strata (R2), and has constant automorphism order |Aut(P(x))| by (AP). Let γ_{x,t} be its lift from step 1 with γ_{x,t}(0) = x, and put H̃_t(x) := γ_{x,t}(1). Since c_{x,t} lies in A^G_{rt}, γ_{x,t}(1) ∈ Ã_t.
- (a): P(H̃_t x) = c_{x,t}(1) = H_t(P x).
- (d): for t = 0 the path is constant, and so is its lift.
- (c): Stab(H̃_t x) = Stab(γ_{x,t}(1)) = Stab(x) by step 1.
- (b): for g ∈ Mod_G, g∘γ_{x,t} is a lift of the same path c_{x,t} = c_{gx,t} (as P(gx) = P(x)), starting at gx. By uniqueness it is γ_{gx,t}, so H̃_t(gx) = gH̃_t(x).

**3. Joint continuity at (x_0, t_1).** Let γ_0 := γ_{x_0,t_1} and K := Stab(x_0) = Stab(γ_0(r)) for all r (step 1).
- For each r, choose a slice neighbourhood of γ_0(r); its stabiliser is K. By compactness of [0,1] and continuity of γ_0, there are 0 = r_0 < ⋯ < r_m = 1 and slice neighbourhoods U_j of γ_0(r_j) (j = 0, …, m−1) with γ_0([r_j, r_{j+1}]) ⊂ U_j; also let U_m be a slice neighbourhood of γ_0(1).
- The map (z, s) ↦ H_s(z) is continuous, so c_{x,t} → c_{x_0,t_1} uniformly on [0,1] as (x, t) → (x_0, t_1). Since c_{x_0,t_1}([r_j, r_{j+1}]) is a compact subset of the open set P(U_j), for (x, t) close to (x_0, t_1) we have c_{x,t}([r_j, r_{j+1}]) ⊂ P(U_j) for all j.
- **Induction.** Let (x_n, t_n) → (x_0, t_1) with x_n ∈ Ã_0, and γ_n := γ_{x_n,t_n}. We show γ_n(r_j) → γ_0(r_j) for j = 0, …, m. For j = 0 this is x_n → x_0. Assume it for j < m. For large n, γ_n(r_j) ∈ U_j, and γ_n([r_j, r_{j+1}]) is a connected subset of P^{-1}(P(U_j)) = ⊔ gU_j (disjoint open sets, (P2)(i)) meeting U_j; hence γ_n([r_j, r_{j+1}]) ⊂ U_j. The points γ_n(r_{j+1}) ∈ U_j lie over c_{x_n,t_n}(r_{j+1}) → c_{x_0,t_1}(r_{j+1}) = P(γ_0(r_{j+1})). By properness of U_j → P(U_j) ((P2)(iii)), every subsequence has a further subsequence converging to a point of U_j over P(γ_0(r_{j+1})), i.e. to a point of the K-orbit of γ_0(r_{j+1}); since K fixes γ_0(r_{j+1}), that point is γ_0(r_{j+1}). So γ_n(r_{j+1}) → γ_0(r_{j+1}).
- For j = m this gives H̃_{t_n}(x_n) → H̃_{t_1}(x_0). T_G is metrisable, so H̃ is continuous.

**4. The equivalences.** (R2^orb) ⇒ (AP) is Prop. 5.1 (which uses only (a), (c) and Lemma 2.5). (R2) + (AP) ⇒ (R2^orb) is steps 0–3. (R2) + (Loc) ⇒ (R2^orb) is Theorem 7.2, and (R2^orb) ⇒ (Loc) with h := H̃. Theorem A (§9) uses only (R1) and (a)–(d). ∎

*Remark 7.6 (what Theorem 7.5 changes).*
- The orbifold reading is now a single, checkable condition on the coarse trivialisation: H_t must not change the order of the automorphism group of any boundary point. The difference between the coarse reading (R2) and (R2^orb) is exactly the possibility of **isotropy change** at boundary points along the family (drop, as in the chart model of §8.2, or rise).
- (AP) is only needed on a disc: if (AP) holds for |t| < r, apply Theorem 7.5 and Theorem A to the rescaled family t ↦ V_{rt}, and extend by Lemma 2.3.
- In particular, by Corollary C.5 below, the claim holds under (R1) + (R2) whenever no point of B_0 has a non-trivial automorphism.

---

## II.8. Discussion: what (R2^orb) buys, and the coarse reading

### 8.1 Dependency table

| Result | Hypotheses on the family | Other inputs |
|---|---|---|
| Lemma 1.1, Def. 1.2 | none | (Kur) |
| Lemma 2.1 | (R1) | Chow, (Irr) |
| Lemma 2.2 | none | — |
| Lemma 2.3 | (R1), (R2) | Remmert, (Cl), normalisation |
| Lemma 2.4 | none | (CG) |
| Lemma 2.5 | none | (Iso) |
| Lemma 3.1 | (R2^orb): (a), (b), (c) "⊂", (d) | (St), Lemmas 2.1, 2.4 |
| Lemma 4.1 | via Lemma 3.1 | (Unif), lifting criterion |
| Prop. 4.2 | (a), (b) for Mod_Π, via Lemma 3.1 | I.2, J0, CL |
| Lemma 4.3 | via Prop. 4.2 | (Roy), (VT), (Bers), (Sel), (Th), (Cent), (Dens) |
| Theorem 4.4(a) | via Lemma 4.3 | (TF), (KP1), (BE) |
| Theorem 4.4(b), Cor. 4.5 | via 4.4(a) | Lemma F0 for genus 0; Lemma F1 (from (IS_c), (BC), (TF)) for genus ≥ 1 |
| Prop. 5.1, 5.2 | (a), (c) | Lemma 2.5, (Kur) |
| Lemma 6.1(1),(2) | (R1), (R2) | (Kur), Lemma 1.1 |
| Lemma 6.1(3)–(5) | via Lemma 3.1, Prop. 5.2 | (PN) |
| Prop. 6.2 | via 6.1, 4.4(a) | (PN3), (K2) |
| Prop. 6.3 | via 6.1, Cor. 4.5 | (PN2) |
| Theorem A | (R1), (R2^orb) | I.2, I.3, I.5, I.6 |
| Lemma 7.1 | none | (St) |
| Theorem 7.2 | (R2), (Loc) | (St) |

### 8.2 The coarse reading admits isotropy drop (chart-level model)
This model shows that (R2^orb) is strictly stronger than (R2), and that (O-int) does not imply (c).
- At a boundary point Q, take stratum coordinates (u, v) on Def(Q)^{G_Q}. Let σ ∈ Aut(Q) act by u ↦ −u, fixing v.
- The coarse coordinates are (U, v) with U = u², so the coarse chart is smooth.
- Let B_0 contain, near Q, the curve {u = 0}. Each of its points carries the extra automorphism σ.
- H_t(U, v) := (U + t², v) is a holomorphically varying, stratum-preserving trivialisation. So (R2) holds at chart level.
- For t ≠ 0, the transported curve is {u = ±t}, on which σ acts freely. So |Aut(H_t z)| < |Aut(z)|, and (c) fails.
- No continuous lift with (a) and (c) exists, by counting stabiliser orders.
- (O-int) holds: σ fixes {u = 0} pointwise, so the intrinsic (effective) isotropy is trivial both before and after transport.
- Whether a **global** family satisfying (i), (ii) and such an isotropy drop at the boundary exists is open.

### 8.3 Where the proof breaks under (R2) alone
1. **Prop. 5.2.** q^{-1}(J_t) ∩ B may consist of several points (the lift-curves), permuted by Aut(J) and not individually Aut(J)-fixed. Then the two applications of Prop. 6.2 at J_m in §9.2 may concern **different** lifts p(t) ≠ p′(t) = a·p(t). One only gets [φ_{m+1}(t)] = [comp_{a^{-1}x_m}(p(t))]: the twin problem.
2. **Lemma 3.1 in non-product strata.** Without a continuous bijective lift Π_t, a constant vertex of a piece cannot be followed to a well-defined piece at time t, and (Rig) is not available.

Both obstructions are exactly the isotropy change of §8.2. This is now a theorem: by Theorem 7.5, under (R2) the failure of (R2^orb) is equivalent to the failure of (AP). The coarse-valid lemmas used for the coarse reading (Part III) are proved in Appendix A.

---


## Excerpt 4: Part III §0 (definitions of pieces, (Rig), transport families, lift-curves, (NRT_P), Theorem B)

## III.0. Conventions, definitions, statement

**0.1 Setting and readings.** g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric. 𝒱 ⊂ M_g × Δ is the family of the problem, V_t its fibres. The hypotheses (i), (ii) and "smoothly trivial" are read as follows.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set. Its fibre over t is closure(V_t) (closures in M̄_g).
- **(R2)** There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ, i.e. H(z,t) = (H_t(z), t). It is smooth on V_0 × Δ, and H_0 = id. For every stratum Δ_G (including the open stratum M_g), H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ).

  This is the *coarse* reading: H_t need not preserve automorphism groups of points.

Δ_Γ is a boundary stratum of *product type*: the gluing map ξ_Γ : ∏_{w∈V(Γ)} M_w → Δ_Γ is bijective on coarse spaces. Here M_w = M_{g_w,n_w}, with the half-edges at w as the marked points. So Δ_Γ ≅ ∏_j M_{g_j,n_j}, and π_i = pr_i ∘ ξ_Γ^{-1}. We put ∂V_t := closure(V_t) ∩ Δ_Γ and assume dim ∂V_t = 1 and π_i(∂V_t) = {Y_t} for all t, with dim M_{g_i,n_i} > 0.

**0.2 Notation.**
- B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g.
- By (R2), H_t(B_0) = B_t, and H_t maps closure(V_0) ∩ Δ_G onto closure(V_t) ∩ Δ_G for every stratum.
- 𝔐 := M_{g_i,n_i}/S_{n_i}, a normal complex space. For an n_i-pointed curve Z of genus g_i, [Z] ∈ 𝔐 is its class with the marked points unordered.
- A *component of type (g_i,n_i)* of a nodal curve is an irreducible component whose normalisation has genus g_i and carries n_i special points (preimages of nodes and marked points).
- Y : Δ → M_{g_i,n_i} denotes t ↦ Y_t. Since M_{g_i,n_i} → 𝔐 has finite fibres and Δ is connected, Y is constant iff [Y] is constant.
- *Germs.* "Germ" always means a germ of a complex-analytic set. Inclusions and equalities of germs are inclusions and equalities of germs.

**0.3 Charts (classical; see facts K1–K5 at the end).** For Q ∈ M̄_g, Def(Q) is the base of the Kuranishi family of the stable curve C_Q. B ⊂ Def(Q) is a small Aut(Q)-invariant ball centred at the point 0 representing C_Q. The map q : B → M̄_g is the quotient by Aut(Q) onto an open neighbourhood q(B) of Q.
- For every edge e of the dual graph G_Q there is a plumbing coordinate s_e on B. For p ∈ B, the nodes of the fibre C_p correspond bijectively to the edges e with s_e(p) = 0.
- The *labels* are the vertices of G_Q.
- A label y is *intact at p* if s_e(p) = 0 for every edge e at y. Then C_p has a distinguished irreducible component deforming the component y of C_Q; with its special points, this is F_y(p).
- Put L_y := {p : y intact at p}. Then p ↦ F_y(p) is holomorphic on L_y (fact PN below), with values in M_{g_y,n_y} for a chosen ordering of the half-edges at y.
- The *pattern* at p is S(p) := {e : s_e(p) = 0}.
- An element a ∈ Aut(Q) acts on B, on the labels and on the edges.

**0.4 Pieces, lifted families, (Rig).**
- A *lifted piece at time t* in a stratum Δ_G is a 1-dimensional irreducible component E of the analytic set ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w. Its image ξ_G(E) is a *piece* (at time t).
- M(E) is the set of vertices w for which pr_w is non-constant on E. K(E) is the closure of pr_{M(E)}(E) in ∏_{u∈M(E)} M̄_u.
- **(Rig)** There is a finite set 𝒦 of triples (G, M, K) with the following properties:
  - M ⊂ V(G);
  - K ⊂ ∏_{u∈M} M̄_u is an irreducible closed curve not contained in the boundary;
  - for every t and every lifted piece E at time t in Δ_G, the triple (G, M(E), K(E)) lies in 𝒦 up to the action of Aut(G).
- The *lifted family* 𝒲_G is the closure in ∏_w M̄_w × Δ_* of (ξ_G × id)^{-1}(closure(𝒱) ∩ (Δ_G × Δ_*)). Here Δ_* ⊂ Δ is the disc fixed in 0.6.
- For a 2-dimensional irreducible component W of 𝒲_G, write W_t for its fibre over t, and M_W, K_W, F_W for the data of BB3 (§1).

**0.5 Remark (dimensions).** dim B_0 ≤ 1. Indeed, B_0 is an analytic subset of the 2-dimensional analytic set closure(V_0). Every point of B_0 is a limit of points of V_0, so B_0 contains no 2-dimensional component of closure(V_0).

By (R2), closure(𝒱) ∩ (∂M̄_g × Δ) = H(B_0 × Δ). This set has topological dimension ≤ 4, so as an analytic set it has dimension ≤ 2. Since ξ_G is finite, 𝒲_G^∘ := 𝒲_G ∩ (∏M_w × Δ_*) = (ξ_G × id)^{-1}(closure 𝒱 ∩ (Δ_G × Δ_*)) has dimension ≤ 2. (𝒲_G^∘ is closed in ∏M_w × Δ_*, being the preimage of a set closed in Δ_G × Δ_*.)

Let C be an irreducible component of 𝒲_G. Pick x ∈ C on no other component, and a neighbourhood U of x with 𝒲_G ∩ U = C ∩ U. Since x lies in the closure of 𝒲_G^∘, C ∩ U meets 𝒲_G^∘. So C ∩ (∏M_w × Δ_*) is a non-empty open subset of C. It is contained in 𝒲_G^∘, hence dim C ≤ 2.

**0.6 The disc Δ_*, the finite set 𝔉, the value curves, and Φ.**
- Fix a closed disc Δ̄_* ⊂ Δ centred at 0, with interior Δ_*. All lifted families are taken over Δ_*.
- 𝒲_G is proper over Δ_* (BB3). Each 2-dimensional component W surjects onto Δ_* (BB3: every fibre W_t is non-empty). Components are locally finite, and all of them meet the compact set 𝒲_G ∩ {t = 0}. Hence there are only finitely many components, and there are finitely many stable graphs G of genus g. So **the set 𝒲 of all 2-dimensional components W of all 𝒲_G is finite.**
- For W ∈ 𝒲, let 𝔉_W ⊂ 𝔐 be the set of classes of components of type (g_i,n_i), with their special points, of the coordinates κ[w] (w ∈ M_W) of points κ ∈ F_W. A coordinate that is a smooth curve counts as its own unique component. 𝔉_W is finite because F_W is finite (BB3). Put 𝔉 := ⋃_{W∈𝒲} 𝔉_W, a finite set.
- For W ∈ 𝒲 and a vertex u ∉ M_W of type (g_i,n_i), let Γ̄_{W,u} ⊂ 𝔐 × Δ_* be the image of Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ_* under M_u × Δ_* → 𝔐 × Δ_*.
  - Γ_{W,u} is an irreducible closed curve, finite over Δ_* (BB3; it is closed by Remmert, since (pr_u,t) is proper on W).
  - M_u → 𝔐 is finite, so Γ̄_{W,u} is again an irreducible closed analytic curve, finite over Δ_*.
  - Put Γ̄_all := ⋃_{W,u} Γ̄_{W,u}, a finite union of closed curves.
- **Definition (Φ).** Φ is the set of irreducible germs φ at (Y_0, 0) ∈ 𝔐 × Δ_* that are local branches at (Y_0,0) of some Γ̄_{W,u} (W ∈ 𝒲, u ∉ M_W of type (g_i,n_i)) and are *non-constant*, i.e. φ ≠ germ of {Y_0} × Δ_*. Φ is finite.
- A branch φ may be a Puiseux branch of degree > 1 over Δ_*. So "the value of φ over t" is the finite set φ_t := φ̂ ∩ (𝔐 × {t}), where φ̂ is a fixed small closed representative. All statements involving φ_t are statements about this set.

**0.7 Transport families, anchored sheets, lift-curves.** Let Q ∈ B_0, with chart q : B → q(B), and let c be a local branch of B_0 at Q, i.e. an irreducible component of the germ of B_0 at Q.
- Since B_0 is a curve, after shrinking B we may represent c by a closed subset of q(B) that is homeomorphic to a closed disc with centre Q. After a further shrinking, c ∖ Q lies in a single stratum Δ_{G_c}. Reason: each stratum meets c ∖ Q in a locally closed analytic subset, and c ∖ Q is a connected punctured disc, so only the stratum containing the generic points of c meets c ∖ Q near Q. Possibly G_c = G_Q; then c ⊂ Δ_{G_Q} near Q.
- Choose ε > 0 with H(c × Δ̄_ε) ⊂ q(B) × Δ_ε. Put N_c := H((c° ∖ Q) × Δ_ε), where c° is the interior of the disc c. N_c is homeomorphic to a punctured disc times a disc, hence connected.
- A *lifted branch* (lift) c̃ of c is an irreducible component at 0 of the germ q^{-1}(c). Its pattern S(c̃) := {e : s_e ≡ 0 on c̃}. After shrinking B, s_e ≠ 0 on c̃ ∖ 0 for e ∉ S(c̃), so S(p) = S(c̃) on c̃ ∖ 0.
- The **transport family** Ñ_c̃ is the connected component, containing (c̃ ∖ 0) × {0}, of (q × id)^{-1}(N_c) ⊂ B × Δ_ε.
- An **anchored sheet** of c̃ is an irreducible component T of the germ at (0,0) of closure(Ñ_c̃) (closure in B × Δ_ε) with c̃ × {0} ⊂ T. Anchored sheets exist: the irreducible germ c̃ × {0} lies in the germ of closure(Ñ_c̃), hence in one of its components.
- c̃ (and any anchored sheet of c̃) is **of boundary type** if Q ∉ Δ_{G_c}. Q is a **puncture point** if it has a branch c of boundary type, i.e. a branch with c ∖ Q in a stratum other than Δ_{G_Q}. Being of boundary type depends only on the coarse branch c, not on the lift.
- Put Q_t := H_t(Q), 𝒬 := {(Q_t, t) : t ∈ Δ_ε}, and the *lift locus* Λ := (q × id)^{-1}(𝒬) ⊂ B × Δ_ε.
- A **lift-curve** is an irreducible component of the germ of Λ at (0,0). (§2 shows that, at a puncture point, Λ is analytic near (0,0) and that its germ is a finite union of curve germs.)

**0.8 Persistence.** Let T be an irreducible 2-dimensional germ at (0,0) in B × Δ_ε, L an irreducible curve germ at (0,0), and z a label. For a germ X on which z is intact, write v_z : X → 𝔐 × Δ_ε, (p,t) ↦ ([F_z(p)], t).
- z is **Y-persistent** on T if z is intact on T (T ⊂ L_z × Δ_ε) and [F_z(p)] = [Y_t] for all (p,t) in a representative of T.
- z is **Φ-persistent on T with function φ** (φ ∈ Φ) if z is intact on T and the image germ v_z(T) is contained in φ. Then P_Φ(T) := the set of labels Φ-persistent on T with some φ ∈ Φ. The function is unique: if v_z(T) ⊂ φ ∩ φ′, then since t|_T is non-constant (Lemma 2.1(c)), v_z(T) is a 1-dimensional germ in both irreducible 1-dimensional germs, so φ = v_z(T) = φ′.
- For a lift-curve L (on which every label is intact, Lemma 2.3(c)): C_Φ(L) := the set of labels z for which the image germ v_z(L) is a branch in Φ.
- z is a **rigid Y_0-copy along L** if v_z(L) is the germ of {Y_0} × Δ_ε.
- **Y ∈ Φ** means: the germ of the graph of [Y] at (Y_0,0) belongs to Φ (proved in Lemma 2.7, assuming Y non-constant).

**0.9 Statement (NRT_P).** *Setting:* that of 0.1, together with (R1), (R2), (Rig), and "t ↦ Y_t is non-constant". *Claim:* there do not exist a puncture point Q ∈ B_0, an automorphism a ∈ Aut(Q), a lift-curve L at Q and a label x of G_Q such that
- x ∈ C_Φ(L), and
- a^{-1}x is a rigid Y_0-copy along L.

In words: along L, for all small t ≠ 0, the component x is intact with class on a branch φ ∈ Φ, while the component a^{-1}x is intact with class ≡ Y_0. (Necessarily a^{-1}x ≠ x: a label cannot be both.)

**0.10 Theorem B.** *Assume the setting of 0.1 with (R1), (R2), Δ_Γ of product type, dim M_{g_i,n_i} > 0, (Rig) and (NRT_P). Then Y_t = Y_0 for all t ∈ Δ.* Moreover:
- (NRT_P) is implied by the problem's conclusion, and a counterexample to (NRT_P) is a counterexample to the problem;
- any configuration violating (NRT_P) forces an isotropy drop |Aut(Q_t)| < |Aut(Q)| for small t ≠ 0.

---


## Excerpt 5: Section C (corollaries)

# Section C — Corollaries

Throughout this section assume (R1), (R2), that Δ_Γ is of product type, and that dim M_{g_i,n_i} ≥ 1. A **puncture point** is a point Q ∈ B_0 having a branch c of B_0 with c ∖ Q contained in a stratum other than Δ_{G_Q} (Part III §0.7).

**Corollary C.1 (no moving Y_0-copies).** Assume (Rig). Suppose that for every puncture point Q ∈ B_0, no automorphism of Q maps an irreducible component C of Q with [C] = [Y_0] (with its special points) onto a different component. Then Y_t = Y_0 for all t ∈ Δ. In particular this holds in each of the following cases:
- (a) 2g_i − 2 + n_i > g − 1;
- (b) every puncture point of B_0 lies in a stratum of product type;
- (c) every puncture point Q of B_0 has Aut(Q) = {1}.

*Proof.*
- By Theorem B (Part III), it suffices to verify (NRT_P), in the setting where Y is non-constant.
- Suppose (Q, a, L, x) violates (NRT_P), so Q is a puncture point.
- Since x ∈ C_Φ(L), the germ v_x(L) passes through (Y_0, 0), so the component of Q labelled x has class [Y_0].
- a^{-1}x ≠ x, because a label cannot be both in C_Φ(L) and a rigid Y_0-copy along L (Part III §0.9).
- By Part III fact K3 (at p = 0), the automorphism a of Q maps the component labelled a^{-1}x onto the component labelled x. These are distinct components of class [Y_0], contradicting the hypothesis.

The special cases:
- (a) Two distinct components of type (g_i, n_i) would give 2(2g_i − 2 + n_i) ≤ 2g − 2 by Lemma U.4.
- (b) By Part I Lemma PT, in a product-type stratum every automorphism maps each component of positive-dimensional type to itself, and M_{g_i,n_i} has positive dimension.
- (c) is clear. ∎

**Corollary C.2 (no isotropy drop).** Assume (Rig). Suppose that for every puncture point Q ∈ B_0 there are t_n → 0 with t_n ≠ 0 and |Aut(H_{t_n}(Q))| = |Aut(Q)|. Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
- By Part III §6.2, a configuration (Q, a, L, x) violating (NRT_P) satisfies ap ≠ p for every (p,t) ∈ L with small t ≠ 0, hence |Aut(Q_t)| < |Aut(Q)| for such t.
- t(L) contains a neighbourhood of 0 (Part III Lemma 2.3(a)). So the isotropy drops for every small t ≠ 0, contrary to the hypothesis.
- Hence (NRT_P) holds, and Theorem B applies. ∎

**Corollary C.3 (shape of a counterexample).** Let a family satisfying the problem's hypotheses, read as (R1) and (R2), have Y non-constant. Then:
- (a) g ≥ 3 (Theorem U.3);
- (b) V_t is totally geodesic for at most countably many t (Theorem U.5);
- (c) the level-cover complex structures V′_t take uncountably many isomorphism classes (Theorem U.6), and closure(V_0) is not an isolated point of the Douady space (Proposition U.7);
- (d) either (Rig) fails, or there is a puncture point Q ∈ B_0 with the following properties:
  - Q lies in a non-product stratum;
  - Q has two distinct components of class [Y_0] exchanged by an automorphism, so 2g_i − 2 + n_i ≤ g − 1;
  - |Aut(H_t(Q))| < |Aut(Q)| for all small t ≠ 0;

  (Corollaries C.1, C.2 and Theorem B);
- (e) the family does not satisfy (R2^orb), nor (Loc) on any disc |t_0| < r (Theorem A and Part II Remark 7.4); equivalently (Part II Theorem 7.5), on every disc |t| < r some boundary point z ∈ B_0 has |Aut(H_t(z))| ≠ |Aut(z)| for some t. In particular some point of B_0 has a non-trivial automorphism (Corollary C.5). This rests on the cited facts of Theorem A.

*Remark C.4 (the readings genuinely differ).* Part II §8.2 gives a chart-level model of a smooth, stratum-preserving trivialisation satisfying (R2) under which isotropy drops at the boundary, so that (R2^orb) fails. Whether a *global* admissible family with such an isotropy change exists is unknown. If none exists, i.e. if (AP) holds for every admissible family on some disc around 0, then the coarse problem is solved outright by Theorem 7.5 and Theorem A (no (Rig) needed).

**Corollary C.5 (trivial automorphisms on the boundary).** Assume (R1) and (R2). If Aut(z) = {1} for every z ∈ B_0 = closure(V_0) ∖ V_0, then Y_t = Y_0 for all t ∈ Δ. (This rests on Theorem A and its cited classical facts.)

*Proof.*
1. **The set Z := {w ∈ M̄_g : Aut(w) ≠ {1}} is closed.** Near any J ∈ M̄_g take the chart q : B → q(B) ≅ B/Aut(J) of (Kur). For p ∈ B, Aut(X_p) ≅ Stab_{Aut(J)}(p), so Z ∩ q(B) = q(⋃_{a ≠ 1} Fix(a)). Each Fix(a) is closed in B, there are finitely many a, and q is closed (a finite-group quotient map). So Z ∩ q(B) is closed in q(B), for every J; hence Z is closed.
2. **(AP) on a small disc.** B_0 is compact (closed in the compact M̄_g) and disjoint from Z, so it has positive distance from Z for a metric on M̄_g. H is uniformly continuous on B_0 × {|t| ≤ 1/2} and H_0 = id, so there is r > 0 with H_t(B_0) ∩ Z = ∅ for |t| < r. Then |Aut(H_t z)| = 1 = |Aut z| for z ∈ B_0 and |t| < r.
3. **Conclusion.** Part II Remark 7.6 (rescale to t ↦ V_{rt}, apply Theorem 7.5 and Theorem A, extend by Lemma 2.3). ∎

*Remark C.6.* The hypothesis of C.5 fails whenever B_0 contains a curve with an elliptic tail, or more generally a component with an automorphism fixing its special points, so C.5 is far from the general case. Upper semicontinuity of |Aut| gives |Aut(H_t z)| ≤ |Aut z| for |t| small depending on z, but not the reverse inequality, and not uniformly in z; this is why the general case is open.

---

