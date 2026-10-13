# Task: hostile referee report on four self-contained proofs (Theorem 7.5, Corollary C.5, Lemmas F0/F1, Proposition Ψ)

You are an independent referee. Below are excerpts of a long document about the problem stated after this query. The excerpts are self-contained for the four results to be checked; other sections of the document are referred to by name only, and you may take the *statements* of those referred results as given (they are not under review here), but you must check every step of the four proofs below.

**What to do.** For each of the four results — (1) Theorem 7.5 (with Lemma 7.1, Lemma 2.5 and Proposition 5.1 as used there), (2) Corollary C.5, (3) Lemmas F0 and F1 (including Lemmas F1.1, F1.2), (4) Proposition Ψ with Lemma S — go through the proof step by step as a hostile referee. For each step say whether it is correct; for each error or gap say precisely what is wrong, whether it is fatal or repairable, and give the repair in full if you can. Check that each cited classical fact is stated correctly (to the best of your knowledge) and is used within its scope; flag any citation you believe is misstated. Check every explicit formula (hyperbolic trigonometry in Lemma S, Riemann–Hurwitz in F0 and F1) yourself. Pay particular attention to:
- Theorem 7.5: is the path-lifting at constant isotropy order correct (existence, uniqueness, constancy of stabilisers), and is the joint-continuity argument (step 3) complete? Is it true that P = ξ_G∘p is open with fibres the Mod_G-orbits, and that the slice facts (P2)(i)–(v) hold? Does anything require (Loc) or more than (AP)?
- Corollary C.5: closedness of the locus of curves with non-trivial automorphisms; uniformity in step 2.
- Lemma F1: the pairs construction in Steps 2c–2d (the document deliberately avoids the Birman–Hilden property — check that nothing still uses it), torsion-freeness of Γ_1, the finiteness of fibres of Υ, Step 6.
- Proposition Ψ: the hexagon maps of Lemma S (Cases 1 and 2), the gluing into a pants map, the marking identification, and the use of Thurston's theorem (Th) and properness (Prop) in (c).

**Output format.** Start with a summary table: result | verdict (correct / correct with minor repairs / gap / false) | one-line reason. Then a section per result with the step-by-step check and full repairs. End with a list of any cited classical facts you consider misstated.

---

## Excerpt 1: the setting (document §1)

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

## Excerpt 2: Part II §1.1 (stable graphs, strata, Teichmüller spaces), §1.3 (readings), §1.4 (Kuranishi charts)

### 1.1 Stable graphs, strata, Teichmüller spaces

**C1 (stable graphs).**
- A stable graph G of genus g consists of:
  - a vertex set V(G) with genera g_w;
  - a set H(G) of half-edges with an attaching map to V(G);
  - a fixed-point-free involution on H(G), whose orbits are the edges E(G).
- n_w denotes the number of half-edges at w. Stability means 2g_w − 2 + n_w > 0.
- Aut(G) is the group of pairs of bijections of V(G) and H(G) that respect attachment, the involution and the genera. **Such an automorphism may exchange the two half-edges of an edge.**
- Contraction: for a subset U ⊂ E(G), G/U is the graph obtained by contracting the edges of U. Its vertices are the connected subgraphs spanned by U; for y ∈ V(G), [y] denotes the vertex of G/U containing y.

**C2 (strata).**
- For a stable graph G, Δ_G ⊂ M̄_g is the locally closed algebraic subset of stable curves whose dual graph is isomorphic to G.
- It is a boundary stratum iff E(G) ≠ ∅.
- closure(Δ_G) ∖ Δ_G is a union of strata Δ_{G′} with G ≅ G′/U for some U ≠ ∅ ("deeper" strata), and it is closed.

**C3 (vertex moduli and Teichmüller spaces).**
- For each w ∈ V(G), fix a reference surface Σ_w of genus g_w with n_w distinct points labelled by the half-edges at w.
- M_w denotes the moduli space of genus-g_w curves with n_w distinct points labelled by these half-edges, M̄_w its Deligne–Mumford compactification, and ∂M̄_w := M̄_w ∖ M_w.
- T_w is the Teichmüller space of (Σ_w, labelled points), and Mod_w the pure mapping class group (isotopy classes of orientation-preserving homeomorphisms of Σ_w fixing each labelled point).
- T_G := ∏_w T_w, Mod_Π := ∏_w Mod_w, and p : T_G → ∏_w M_w = T_G/Mod_Π is the quotient map.
- pr_w denotes the w-th coordinate. For W ⊂ V(G), pr_W denotes the projection to ∏_{w∈W}.

**C4 (the stratum group Mod_G).**
- Mod_G is the group of pairs g = (σ, (φ_w)_w), where:
  - σ ∈ Aut(G);
  - φ_w is an isotopy class of orientation-preserving homeomorphisms Σ_w → Σ_{σ(w)} carrying the point labelled h to the point labelled σ(h).
- It acts on T_G by sending (C_w, f_w)_w to the point whose σ(w)-coordinate is C_w, with marking f_w∘φ_w^{-1} and with the point f_w(h) relabelled σ(h).
- ξ_G : ∏_w M_w → Δ_G is the gluing map: for every edge {h, h′}, glue the point labelled h to the point labelled h′.
- We use the following standard facts (St), cited at the end:
  - (St1) Mod_G acts properly discontinuously by biholomorphisms on T_G. Every point x̂ has a Stab(x̂)-invariant open neighbourhood U ("slice neighbourhood") with gU ∩ U ≠ ∅ ⇒ g ∈ Stab(x̂), and these form a neighbourhood basis.
  - (St2) ξ_G∘p : T_G → Δ_G is surjective, and its fibres are exactly the Mod_G-orbits.
  - (St3) Mod_Π is the kernel of Mod_G → Aut(G), (σ, φ) ↦ σ; this map is onto. So Aut(G) = Mod_G/Mod_Π acts on ∏_w M_w by permuting factors and relabelling points, and ξ_G is the quotient map by this finite group.
  - (St4) ξ_G is a finite (hence proper) morphism of quasi-projective varieties. It extends to the finite gluing morphism ξ̄_G : ∏_w M̄_w → closure(Δ_G).
- (Mod_G is the stack-theoretic stratum group: [T_G/Mod_G] = Δ_G as a substack of M̄_g. See Lemma 2.4 for its stabilisers.)

**C5 (time-t objects).** For a boundary stratum G and t ∈ Δ put:
- A_t = A^G_t := closure(V_t) ∩ Δ_G;
- Â_t := ξ_G^{-1}(A_t) ⊂ ∏_w M_w;
- Ã_t := p^{-1}(Â_t) ⊂ T_G, which is Mod_G-invariant;
- B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g.

A **piece** (at time t, in the stratum G) is a 1-dimensional irreducible component E of the analytic set Â_t. For a piece E:
- ν : Ê → E is its normalisation;
- M(E) := {w ∈ V(G) : pr_w|_E is non-constant} (the moving vertices);
- K(E) := closure of pr_{M(E)}(E) in ∏_{u∈M(E)} M̄_u;
- for a vertex c ∉ M(E), φ_c(E) ∈ M_c denotes the constant value of pr_c on E.

**C6 (classes).**
- For a type (h, m), 𝔐_{h,m} := M_{h,m}/S_m (unordered marked points), with finite quotient map Z ↦ [Z].
- Let C be a smooth irreducible component of a stable pointed curve. "C with its special points" means the normalisation of C, with the preimages of nodes and the marked points lying on C as an unordered set of special points. Its class is taken in the appropriate 𝔐.

### 1.3 The readings

**(R1)** closure(𝒱) is a closed analytic subset of M̄_g × Δ, and its fibre over t is closure(V_t).

**(R2)** (coarse reading of the smooth triviality and of (i), (ii)). There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ (write H_t := H(·, t)) such that:
- H_0 = id;
- H is smooth on V_0 × Δ (never used below);
- for every stratum G, including the open one, H((closure(V_0) ∩ Δ_G) × Δ) = closure(𝒱) ∩ (Δ_G × Δ).

Consequently H_t(A^G_0) = A^G_t for all G, H_t(B_0) = B_t, and H_t(∂V_0) = ∂V_t.

*Standing-reading caveat.* (R1) and (R2) are themselves readings of the problem. In particular (R2) encodes (i) and (ii) by **one** stratum-preserving homeomorphism that trivialises all strata simultaneously. Everything below is conditional on them.

**(R2^orb)** (embedded orbifold reading). (R2) holds, and for every boundary stratum G there is a continuous map H̃ = H̃^G : Ã_0 × Δ → T_G (write H̃_t := H̃(·, t)) such that for all t ∈ Δ:
- (a) ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
- (b) H̃_t(g x) = g H̃_t(x) for all g ∈ Mod_G and x ∈ Ã_0;
- (c) Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x) for all x ∈ Ã_0;
- (d) H̃_0 = id.

**(Loc)** (chart-level local reading). For every boundary stratum G, every x̂ ∈ Ã_0 and every t_0 ∈ Δ there are:
- an open neighbourhood W of x̂ in T_G;
- an open disc I ∋ t_0;
- a continuous h : (W ∩ Ã_0) × I → T_G,

such that:
- (L1) ξ_G∘p∘h_s = H_s∘ξ_G∘p on W ∩ Ã_0, for s ∈ I;
- (L2) for each u ∈ W ∩ Ã_0, Stab_{Mod_G}(h_s(u)) does not depend on s ∈ I.

By Theorem 7.2, (R2) + (Loc) ⇔ (R2^orb). The direction ⇒ is the content of the theorem; ⇐ holds with h := H̃, by (a) and (c).

**The two orbifold readings.** "Regard M̄_g and its strata as orbifolds" admits two inequivalent precise forms.
- **(O-emb), embedded/substack reading.** A_t is the reduced closed substack of the stack Δ_G = [T_G/Mod_G]; its isotropy at z is the full Aut(z) (Lemma 2.4). The trivialisation is an isomorphism of substacks over Δ. That is, its local lifts are equivariant through isomorphisms of the **ambient** local groups Aut(z) → Aut(H_t z), these isomorphisms being locally constant in s (this constancy is part of the reading, not a consequence; see Remark 7.3).
  - (O-emb) gives (Loc) (Remark 7.3), hence (R2^orb) by Theorem 7.2. Conversely, (R2^orb) gives (O-emb) by definition.
  - So **(R2^orb) formalises (O-emb).**
- **(O-int), intrinsic reading.** Each A_t carries its own effective orbifold structure, and H_t is an orbifold diffeomorphism of these intrinsic structures. The local homomorphisms need not be onto, or injective, on the ambient groups.
  - (O-int) is strictly weaker: the chart-level model of §8.2 satisfies (O-int) but violates (c).
- Locally, **(R2^orb) ⇔ (O-emb) ⊊ (O-int) ⊆ (R2)**. Theorem A is proved under (O-emb) only. The wording of the problem ("smooth subvariety of M_g", "complex submanifold", "smoothly trivial") does not decide between these readings, and arguably leans towards the coarse one.

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


## Excerpt 3: Part II Lemma 2.5 and Proposition 5.1

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

## II.5. Isotropy is transported; the lift of Q_t is unique [orb]

For Q ∈ B_0 put Q_t := H_t(Q). By (R2), Q_t ∈ Δ_{G_Q}.

**Proposition 5.1 (isotropy) [orb: (a), (c)].** For every Q ∈ B_0 and t ∈ Δ, |Aut(Q_t)| = |Aut(Q)|.

*Proof.*
- Let G := G_Q. Then Q ∈ A^G_0, so there is x̂ ∈ Ã_0 with ξ_G p(x̂) = Q.
- By (a), ŷ := H̃_t(x̂) satisfies ξ_G p(ŷ) = Q_t.
- By Lemma 2.5 and (c): Aut(Q_t) ≅ Stab_{Mod_G}(ŷ) = Stab_{Mod_G}(x̂) ≅ Aut(Q). ∎


## Excerpt 4: Part II §7 — Lemma 7.1, Theorem 7.2 (Theorem LG; for context), Theorem 7.5 (UNDER REVIEW), Remark 7.6

**Lemma 7.1 (unique continuation of stabiliser-constant lifts) [none].** Let I ⊂ ℝ be an interval, and let γ_1, γ_2 : I → T_G be continuous with ξ_G p γ_1 = ξ_G p γ_2. Suppose s ↦ Stab_{Mod_G}(γ_1(s)) is locally constant and γ_1(s_0) = γ_2(s_0) for some s_0. Then γ_1 = γ_2.

*Proof.*
- E := {s : γ_1(s) = γ_2(s)} is closed, since T_G is Hausdorff.
- **E is open.** Let s_1 ∈ E, y := γ_1(s_1), and U a slice neighbourhood of y (St1).
  - For s near s_1, both γ_i(s) lie in U. By (St2), γ_2(s) = g_sγ_1(s) for some g_s ∈ Mod_G. Then g_sU ∩ U ≠ ∅, so g_s ∈ Stab(y).
  - By local constancy, Stab(γ_1(s)) = Stab(y) for s near s_1. So g_s fixes γ_1(s), and γ_2(s) = γ_1(s).
- I is connected, so E = I. ∎

**Theorem 7.2 (Theorem LG) [coarse (R2) + (Loc)].** Assume (R2) and (Loc). Then for every boundary stratum G there is a continuous H̃ : Ã_0 × Δ → T_G satisfying (a)–(d). It is unique even among continuous maps satisfying only (a), (c) and (d).

*Proof.*

**1. Construction.** For x ∈ Ã_0 and t ∈ Δ, let γ_{x,t} : [0,1] → T_G be a continuous lift of r ↦ H_{rt}(ξ_G p x) with γ_{x,t}(0) = x and with r ↦ Stab(γ_{x,t}(r)) locally constant. Put H̃_t(x) := γ_{x,t}(1).

**2. Existence of γ_{x,t}.**
- For each τ in the segment {rt : 0 ≤ r ≤ 1}, (Loc) at (x, τ) gives W_τ, I_τ and h^τ. By compactness and a Lebesgue number, there are τ_1, …, τ_k and 0 = r_0 < ⋯ < r_k = 1 with {rt : r ∈ [r_{j−1}, r_j]} ⊂ I_j := I_{τ_j}. Write h^j := h^{τ_j}.
- 0 ∈ I_1. By (L1) and H_0 = id, h^1_0(x) lies over ξ_G p(x), so h^1_0(x) = a x for some a ∈ Mod_G (St2). Replace h^1 by a^{-1}h^1; (L1) and (L2) are preserved, since Stab(a^{-1}y) = a^{-1}Stab(y)a. Now h^1_0(x) = x.
- Put γ(r) := h^1_{rt}(x) on [r_0, r_1].
- Inductively, γ(r_j) and h^{j+1}_{r_j t}(x) lie over the same point, so γ(r_j) = g h^{j+1}_{r_j t}(x) with g ∈ Mod_G. Put γ(r) := g h^{j+1}_{rt}(x) on [r_j, r_{j+1}].
- γ is continuous. By (L2), Stab(γ(r)) is constant on each [r_{j−1}, r_j], and these constants agree at the junctions. So Stab(γ(r)) = Stab(x) for all r.

**3. Uniqueness of γ_{x,t}.** This is Lemma 7.1. In particular:
- H̃ is well defined;
- H̃_{rt}(x) = γ_{x,t}(r), by uniqueness applied to the reparametrised path.

**4. Properties.**
- (a) holds by construction.
- (d): for t = 0 the constant path is the lift.
- (c): Stab(H̃_t x) = Stab(γ_{x,t}(1)) = Stab(x).
- (b): for g ∈ Mod_G, g∘γ_{x,t} lifts the same path (since ξ_G p g = ξ_G p), starts at gx, and has constant stabiliser g Stab(x) g^{-1}. By Lemma 7.1 it equals γ_{gx,t}.
- **Uniqueness of H̃.** Let H̃′ be continuous with (a), (c), (d). Then r ↦ H̃′_{rt}(x) is a lift starting at x, by (d), with constant stabiliser Stab(x), by (c). By Lemma 7.1 it equals γ_{x,t}, so H̃′ = H̃.

**5. Joint continuity at (x_0, t_1).**
- Take the data of step 2 for (x_0, t_1). Absorb the elements g into the h^j, so that γ_{x_0,t_1}(r) = h^j_{rt_1}(x_0) on [r_{j−1}, r_j].
- Each h^j is defined on (W_j ∩ Ã_0) × I_j, with W_j a neighbourhood of x_0. Put W := ⋂_j W_j.
- By compactness there is δ > 0 with rt ∈ I_j for r ∈ [r_{j−1}, r_j] and |t − t_1| < δ.
- Let K := Stab(x_0). By step 2, K = Stab(γ_{x_0,t_1}(r)) for all r. It is finite.

**Claim.** For (x, t) ∈ (W ∩ Ã_0) × Δ close enough to (x_0, t_1) and each j, there is k_j ∈ K with γ_{x,t}(r) = k_j h^j_{rt}(x) on [r_{j−1}, r_j].

*Proof of the claim.*
- **j = 1.** h^1_0(x) = a_x x with a_x ∈ Mod_G. As x → x_0, both x and a_x x = h^1_0(x) tend to h^1_0(x_0) = x_0. So, for x close to x_0, both lie in a slice neighbourhood of x_0, and a_x ∈ K.
  - The path r ↦ a_x^{-1}h^1_{rt}(x) lifts the path, starts at x, and has constant stabiliser. By Lemma 7.1 it equals γ_{x,t} on [0, r_1]. Take k_1 := a_x^{-1}.
- **j → j + 1.** Put y_0 := γ_{x_0,t_1}(r_j) = h^j_{r_jt_1}(x_0) = h^{j+1}_{r_jt_1}(x_0); then Stab(y_0) = K.
  - For (x, t) close to (x_0, t_1), both k_j h^j_{r_jt}(x) and h^{j+1}_{r_jt}(x) lie in a K-invariant slice neighbourhood U of y_0 and over the same point.
  - So they differ by some k′ ∈ Stab(y_0) = K.
  - By Lemma 7.1 on [r_j, r_{j+1}], γ_{x,t} = k′h^{j+1}_{rt}(x) there. Take k_{j+1} := k′.

**Continuity.** H̃_t(x) = k_k h^k_t(x) with k_k ∈ K. As (x, t) → (x_0, t_1), h^k_t(x) → h^k_{t_1}(x_0) = H̃_{t_1}(x_0) =: y_1, and every element of K fixes y_1. Since K is finite, H̃_t(x) → y_1. ∎

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


## Excerpt 5: Corollary C.5 (UNDER REVIEW) and Remark C.6. Here B_0 = closure(V_0) ∖ V_0, H is the trivialisation of (R2), and "Theorem A" is the theorem: under (R1) and (R2^orb), Y_t = Y_0 for all t (take it as given).

**Corollary C.5 (trivial automorphisms on the boundary).** Assume (R1) and (R2). If Aut(z) = {1} for every z ∈ B_0 = closure(V_0) ∖ V_0, then Y_t = Y_0 for all t ∈ Δ. (This rests on Theorem A and its cited classical facts.)

*Proof.*
1. **The set Z := {w ∈ M̄_g : Aut(w) ≠ {1}} is closed.** Near any J ∈ M̄_g take the chart q : B → q(B) ≅ B/Aut(J) of (Kur). For p ∈ B, Aut(X_p) ≅ Stab_{Aut(J)}(p), so Z ∩ q(B) = q(⋃_{a ≠ 1} Fix(a)). Each Fix(a) is closed in B, there are finitely many a, and q is closed (a finite-group quotient map). So Z ∩ q(B) is closed in q(B), for every J; hence Z is closed.
2. **(AP) on a small disc.** B_0 is compact (closed in the compact M̄_g) and disjoint from Z, so it has positive distance from Z for a metric on M̄_g. H is uniformly continuous on B_0 × {|t| ≤ 1/2} and H_0 = id, so there is r > 0 with H_t(B_0) ∩ Z = ∅ for |t| < r. Then |Aut(H_t z)| = 1 = |Aut z| for z ∈ B_0 and |t| < r.
3. **Conclusion.** Part II Remark 7.6 (rescale to t ↦ V_{rt}, apply Theorem 7.5 and Theorem A, extend by Lemma 2.3). ∎

*Remark C.6.* The hypothesis of C.5 fails whenever B_0 contains a curve with an elliptic tail, or more generally a component with an automorphism fixing its special points, so C.5 is far from the general case. Upper semicontinuity of |Aut| gives |Aut(H_t z)| ≤ |Aut z| for |t| small depending on z, but not the reverse inequality, and not uniformly in z; this is why the general case is open.

---


## Excerpt 6: Lemmas F0 and F1 (UNDER REVIEW), with their cited inputs

- **(dF)** Generalised de Franchis theorem (Imayoshi 1983; from memory): if R and Y are Riemann surfaces of finite type and Y is hyperbolic, there are only finitely many non-constant holomorphic maps R → Y.

**Lemma F0 (finiteness for genus-0 targets; proved here, no citation beyond big Picard and Riemann–Hurwitz).** Let R be a Riemann surface of finite type, i.e. R = R̄ ∖ P with R̄ compact of genus h and P finite, |P| = k. Then:
- (a) there are only finitely many non-constant holomorphic maps R → P¹ ∖ {0,1,∞};
- (b) for every n ≥ 4 there are only finitely many non-constant holomorphic maps R → M_{0,n} (points labelled).

*Proof.*
- (a) Let f : R → P¹ ∖ {0,1,∞} be holomorphic and non-constant. By the big Picard theorem f has no essential singularity at a point of P (near such a point it would take the value 0 or 1), so f extends to a non-constant holomorphic map f̄ : R̄ → P¹ of some degree d ≥ 1, with f̄^{-1}{0,1,∞} ⊂ P.
  - **Degree bound.** Over the three points 0, 1, ∞ the ramification satisfies Σ_{p ∈ f̄^{-1}{0,1,∞}} (e_p − 1) = 3d − #f̄^{-1}{0,1,∞} ≥ 3d − k. Riemann–Hurwitz gives 2h − 2 = −2d + Σ_{p ∈ R̄}(e_p − 1) ≥ −2d + 3d − k, i.e. d ≤ 2h − 2 + k.
  - **Divisors.** div(f̄) is supported in P, and its positive and negative parts have degree d ≤ 2h − 2 + k. So div(f̄) lies in a finite set of divisors.
  - **Constants.** Two meromorphic functions with the same divisor differ by a constant factor (their quotient is holomorphic and zero-free on the compact R̄). Fix f_0 with div(f_0) = div(f̄), so f̄ = c f_0 with c ∈ ℂ^*. f̄ is surjective, so it takes the value 1 at some point, which lies in P; at that point p, f_0(p) ∈ ℂ^* and c = 1/f_0(p). So c lies in the finite set {1/f_0(p) : p ∈ P, f_0(p) ∈ ℂ^*}.
  - Hence there are finitely many f.
- (b) Normalising the points labelled 1, 2, 3 to 0, 1, ∞ identifies M_{0,n} with {(x_4, …, x_n) ∈ (P¹ ∖ {0,1,∞})^{n−3} : x_l ≠ x_m for l ≠ m}. A holomorphic map g = (x_4, …, x_n) : R → M_{0,n} has coordinates x_m : R → P¹ ∖ {0,1,∞}, each constant or, by (a), one of finitely many non-constant maps.
  - If g is non-constant, some x_l is non-constant. Its extension x̄_l : R̄ → P¹ is surjective, so P¹ ∖ x_l(R) ⊂ x̄_l(P), a finite set.
  - A constant coordinate x_m ≡ c_m must satisfy c_m ≠ x_l(z) for all z ∈ R, so c_m ∈ x̄_l(P).
  - So g is determined by finitely many choices: which coordinates are constant, the non-constant ones from the finite set of (a), and the constants from the finite sets x̄_l(P). ∎

(Sanity check: for R = P¹ ∖ {0,1,∞}, (a) gives d ≤ 1, and the maps are the six Möbius maps permuting {0,1,∞}, as expected.)

**Lemma F1 (finiteness for targets of genus ≥ 1 with marked points; proved here from closed-surface finiteness).** Let h ≥ 1, m ≥ 1, N ≥ 3, and let Mod_{h,m}[N] be the kernel of PMod_{h,m} → Sp(2h, ℤ/N) (so Mod_u[N] of Theorem 4.4 for g_u ≥ 1). Put M_{h,m}[N] := T_{h,m}/Mod_{h,m}[N]. For every Riemann surface R of finite type, the set of **all** non-constant holomorphic maps R → M_{h,m}[N] is finite.

(In particular each free homotopy class contains finitely many such maps, which is all that Theorem 4.4(b) needs. The case (1,1) is included; it is also covered by (dF). The proof uses no finiteness statement for families of punctured surfaces: it reduces to closed fibres by a characteristic branched covering. Notation inside this proof is local: Φ, Π, Λ, G, L, K, Q, M, Υ have the meanings given here, unrelated to their uses elsewhere in Part II.)

*Cited inputs (from memory).*
- **(IS_c) Imayoshi–Shiga finiteness, closed fibres** (Imayoshi–Shiga 1988; for compact bases this is the Parshin–Arakelov theorem). Let B be a Riemann surface of finite type and g ≥ 2. There are only finitely many isomorphism classes, over B, of locally non-trivial holomorphic families of closed Riemann surfaces of genus g over B. (A holomorphic family is a proper holomorphic submersion from a complex surface onto B with fibres of genus g; locally non-trivial means that over no non-empty open subset of B are all fibres isomorphic.)
- **(BC) Branched covers and Teichmüller spaces** (MacLachlan–Harvey 1975; Birman–Hilden; Bers–Greenberg; Nag's book). For a finite regular branched covering of the kind constructed in Step 2c below, the induced map Φ : T_{h,m} → T_{h′} is holomorphic and injective. *Sketch:* uniformise the orbifold (Σ_0, cone order n_j at x_j) by a cocompact Fuchsian group Γ_0, and let Γ_Y = ker(Γ_0 → G); by Bers–Greenberg T(Γ_0) ≅ T_{h,m}, and T(Γ_Y) ≅ T_{h′}, compatibly with markings; in Bers' model (Γ-compatible Beltrami coefficients modulo w^μ = w^ν on ℝ) Φ is the inclusion [μ] ↦ [μ], injective because the equivalence relation is the same, and holomorphic because in the Bers embedding it is the restriction of the linear inclusion B_2(Γ_0) ⊂ B_2(Γ_Y).
- **(TF)** (Serre's lemma for closed surfaces): Mod_g[N′] is torsion-free for N′ ≥ 3.

*F1 §0.* Trivial case and conventions

If R is not hyperbolic, its universal cover is C or P^1. By the Bers embedding, T_{h,m} is biholomorphic to a bounded domain in C^{3h-3+m}. A lift of a holomorphic map R → M_{h,m}[N] to universal covers is therefore constant (Liouville, or compactness for P^1). So every holomorphic map R → M_{h,m}[N] is constant, and the set in question is empty.

From now on R = D/Π, where D is the unit disc and Π ≅ π_1(R) is a Fuchsian group. Π is finitely generated because R has finite type.

Write T = T_{h,m}, PMod = PMod_{h,m}, and M = M_{h,m}[N] = T/Mod_{h,m}[N]. Mapping classes act on T by [X, φ] ↦ [X, φ∘ϑ^{-1}], where φ: (Σ_0, P) → (X, P_X) is a marking. Here Σ_0 is a closed genus-h surface, P ⊂ Σ_0 is a set of m labelled points, and S_0 = Σ_0 \ P.

*F1 §1.* The closed case

**Lemma F1.1.** Let B be of finite type, g ≥ 2 and N' ≥ 3. Then there are only finitely many non-constant holomorphic maps B → M_g[N'].

*Proof.*

1. **M_g[N'] is a fine moduli space.** Mod_g[N'] acts freely on T_g by (TF). It therefore acts freely on the Teichmüller curve, and the quotient is a universal curve C → M_g[N']; this is a proper holomorphic submersion. As a set, M_g[N'] = {(X, α)}/iso, where α is a symplectic isomorphism (Z/N')^{2g} → H_1(X, Z/N'). Indeed, two markings of X inducing the same α differ by an element of Mod_g[N'].

2. **Non-constant maps give locally non-trivial families.** Let F: B → M_g[N'] be holomorphic and non-constant. Then the composite B → M_g is non-constant, because M_g[N'] → M_g has finite fibres and B is connected. By the identity theorem it is non-constant on every open set. Hence F^*C is locally non-trivial.

3. **Isomorphic families give maps differing by Sp(2g, Z/N').** Suppose F_1^*C ≅ F_2^*C over B via Θ. Each F_i comes with a continuous level structure α_i(b) on the fibre over b, that is, a section of the finite covering space of symplectic frames of H_1(X_b, Z/N'). Then σ(b) := α_1(b)^{-1} ∘ Θ_b^{-1} ∘ α_2(b) is a continuous map into the finite group Sp(2g, Z/N'). It is therefore constant, say σ, and F_2 = σ·F_1, where σ acts by (X, α) ↦ (X, α∘σ).

4. **Count.** By (IS_c) there are finitely many families, and each family arises from at most |Sp(2g, Z/N')| maps. ∎

*F1 §2.* The branched-cover construction

**Step 2a (a characteristic subgroup).** Let π = π_1(S_0). It is free of rank 2h+m-1 ≥ 2. Let c_1, ..., c_m be loops around the punctures; each is non-trivial in π.

- π is residually finite, so for each j there is a normal subgroup K_j of finite index with c_j ∉ K_j. Let d be the largest of these indices.
- Let K be the intersection of all subgroups of π of index ≤ d. There are finitely many such subgroups, since π is finitely generated.
- K is characteristic in π, has finite index, and no c_j lies in K.

Let G = π/K, and let n_j ≥ 2 be the order of the image of c_j in G.

**Step 2b (the covering of a pointed curve).** For a pointed curve (X, P_X) of type (h,m), let Y° → X \ P_X be the regular G-cover corresponding to K. It is canonical because K is characteristic, and it is unique up to deck transformations. Fill in the ends to get a compact Riemann surface Y_X with a branched G-cover Y_X → X. This cover is branched exactly over P_X, with order n_j over x_j.

By Riemann–Hurwitz, 2h'-2 = |G|·(2h-2 + Σ_j (1 - 1/n_j)) > 0, because h ≥ 1 and m ≥ 1. So the genus h' of Y_X satisfies h' ≥ 2. In particular Aut(Y_X) is finite (Hurwitz).

**Step 2c (the map Φ and lifts of mapping classes).** Fix Y_0 → Σ_0 for the base point. Define Φ: T_{h,m} → T_{h'} by [X, φ] ↦ [Y_X, φ̃], where φ̃ is any lift of φ.

- Lifts exist because φ_*(K) = K (K is characteristic).
- Two lifts differ by a deck transformation, which is conformal on Y_X, so they define the same point of T_{h'}.
- An isotopy rel P lifts to an isotopy.

Every ϑ ∈ PMod lifts to Y_0: a representing homeomorphism of (Σ_0, P) acts on π by an automorphism defined up to inner automorphisms, which preserves the characteristic subgroup K, so it lifts to the regular cover Y_0° and extends over the filled-in points. The isotopy classes of the lifts of ϑ form a coset ϑ̃G in Mod(Y_0), where G ⊂ Mod(Y_0) is the group of deck classes: lifts of one homeomorphism differ by deck transformations, and an isotopy rel P downstairs lifts to an isotopy upstairs. G injects into Mod(Y_0), because a non-trivial conformal automorphism of a surface of genus ≥ 2 is not isotopic to the identity.

To avoid any appeal to the Birman–Hilden property (whether a lift isotopic to the identity upstairs forces the downstairs class to be trivial), we work with **pairs**. Let L be the set of pairs (ϑ, ϑ̃) with ϑ ∈ PMod and ϑ̃ ∈ Mod(Y_0) the isotopy class of a lift of a representative of ϑ. Under componentwise composition L is a group. The projection L → PMod, (ϑ, ϑ̃) ↦ ϑ, is a surjective homomorphism, and its kernel is {(1, g) : g ∈ G}, which is isomorphic to G. The second projection L → Mod(Y_0), (ϑ, ϑ̃) ↦ ϑ̃, is also a homomorphism (it need not be injective, and we never use injectivity). Directly from the definitions, **Φ(ϑ·p) = ϑ̃·Φ(p)** for every (ϑ, ϑ̃) ∈ L.

By (BC), Φ is holomorphic and injective.

**Step 2d (choosing levels).** Fix N' ≥ 3. Let Λ := {(ϑ, ϑ̃) ∈ L : ϑ̃ ∈ Mod(Y_0)[N']}, the preimage of the finite-index subgroup Mod(Y_0)[N'] under the second projection; it has finite index in L. The intersection of Λ with the kernel of the first projection is {(1, g) : g ∈ G ∩ Mod(Y_0)[N']}. Since Mod(Y_0)[N'] is torsion-free (TF), G is finite and G injects into Mod(Y_0), this intersection is trivial. So the first projection maps Λ isomorphically onto a subgroup Γ'' ⊂ PMod, of finite index because L → PMod is onto and [L : Λ] < ∞. Let λ: Γ'' → Mod_{h'}[N'] be the inverse isomorphism followed by the second projection, ϑ ↦ ϑ̃; it is a homomorphism, and Φ(ϑp) = λ(ϑ)Φ(p) for ϑ ∈ Γ''.

Let Γ_1 be the normal core in PMod of Γ'' ∩ Mod_{h,m}[N]. Then Γ_1 is normal in PMod, of finite index, and contained in Mod_{h,m}[N]. It is torsion-free, because Mod_{h,m}[N] is: a finite-order element of PMod_{h,m} is represented by a conformal automorphism f of some pointed curve (X, P_X) fixing each marked point (Nielsen realisation for finite cyclic groups); if it lies in Mod_{h,m}[N], then f acts trivially on H_1(X; ℤ/N) with N ≥ 3 and h ≥ 1, so f = id by Serre's lemma (the genus-≥1 form of (TF): an automorphism of a compact Riemann surface of genus ≥ 1 that fixes a point and acts trivially on H_1(·; ℤ/N), N ≥ 3, is the identity), and the mapping class is trivial. Put M_1 := T/Γ_1. This is a complex manifold and a finite unramified cover q: M_1 → M.

Define Υ: M_1 → M_{h'}[N'] by Γ_1 p ↦ Mod_{h'}[N']·Φ(p). It is well defined by the equivariance in Step 2d, and holomorphic because locally it is Φ read in covering charts.

**Lemma F1.2.** (a) Υ is locally injective. (b) Υ has finite fibres.

*Proof.*

(a) Let x = Γ_1 p.
- Choose a neighbourhood W of Φ(p) on which the covering T_{h'} → M_{h'}[N'] is injective.
- Choose a neighbourhood U of p on which T → M_1 is injective and with Φ(U) ⊂ W.
- On U, Υ∘(projection) = (projection)∘Φ, and the right-hand side is injective on U because Φ is injective (BC).
- Hence Υ is injective on the open set image(U) ∋ x.

(b) Suppose Υ(Γ_1 q) = Υ(Γ_1 p).
- Then Y_q ≅ Y_p via some conformal c. Hence Σ_q ≅ Y_p / (c G_q c^{-1}), and the iso carries the labelled points x_j(q) to branch points of this quotient.
- Aut(Y_p) is finite and has finitely many subgroups, and there are finitely many labellings. So the pointed curve [Σ_q, x(q)] ∈ M_{h,m} lies in a finite set.
- The map M_1 → M_{h,m} has fibres of size at most [PMod : Γ_1] < ∞. ∎

*F1 §3.* Proof of Lemma F1

Let f: R → M be holomorphic and non-constant.

**Step 1 (the homomorphism ρ_f).** Choose a lift f̃: D → T. Since Mod_{h,m}[N] acts freely as the deck group, there is a homomorphism ρ_f: Π → Mod_{h,m}[N] with f̃∘γ = ρ_f(γ)∘f̃. Changing the lift conjugates ρ_f.

**Step 2 (finitely many intermediate covers).** Since Γ_1 is normal, H_f := ρ_f^{-1}(Γ_1) is the kernel of the induced map Π → Q := Mod_{h,m}[N]/Γ_1. Q is a finite group and Π is finitely generated, so there are finitely many homomorphisms Π → Q. Hence H_f ranges over a finite set {H_1, ..., H_s} of finite-index subgroups.

It therefore suffices to fix H = H_k and to show that the set 𝓕_H of non-constant f with H_f = H is finite.

**Step 3 (lifting f to R').** Let R' = D/H. It is a connected finite unramified cover p_H: R' → R, so it has finite type and is hyperbolic.

For f ∈ 𝓕_H, fix one lift f̃. It descends to a holomorphic f': R' → M_1 with q∘f' = f∘p_H. Since p_H is surjective, f' determines f. So f ↦ f' is injective on 𝓕_H.

**Step 4 (the composite F' is non-constant).** Let F' := Υ∘f': R' → M_{h'}[N']. If F' were constant, then Φ∘f̃ would take values in a single Mod_{h'}[N']-orbit. That orbit is discrete, because the action is properly discontinuous, and D is connected, so Φ∘f̃ would be constant. Since Φ is injective, f̃ would be constant, and so would f, a contradiction.

**Step 5 (finitely many values of F').** By Lemma F1.1 applied to B = R' and g = h', there are only finitely many possible F'.

**Step 6 (finitely many f' over each F').** Fix F', and let f'_a, f'_b: R' → M_1 be continuous maps with Υ∘f'_a = Υ∘f'_b = F'. Let E = {r : f'_a(r) = f'_b(r)}.
- E is closed, since M_1 is Hausdorff.
- E is open by Lemma F1.2(a): near a point of E both maps take values in a neighbourhood on which Υ is injective.
- R' is connected, so either f'_a = f'_b or the two maps disagree at every point.

Fix r_0 ∈ R'. Distinct lifts then take distinct values in Υ^{-1}(F'(r_0)), which is finite by Lemma F1.2(b). So there are finitely many f' over each F'.

**Conclusion.** Combining Steps 3–6, 𝓕_H is finite. Hence the set of all non-constant holomorphic maps R → M_{h,m}[N] is finite. ∎

(This is the argument suggested as a "possible repair" in an earlier version of II.11; it is now carried out.)



## Excerpt 7: Proposition Ψ (UNDER REVIEW) and the list of classical facts cited in Part I. (§0.4 and (CD) refer to the canonical plumbing-chart description of augmented Teichmüller space near a stable curve J: U ⊂ T̄_g a neighbourhood of a lift J̃, Tw the group generated by Dehn twists about the node curves α_e of J, B = U/Tw a Kuranishi chart with smoothing parameters s_e, p_U : U → B, L_y the locus where label y is intact, and F_y(p) the component of the fibre labelled y.)

## I.6A. Proposition Ψ (the subsurface restriction map) — proved here

This section proves the properties of the function ψ used in §5 and in Lemma L.1 of the Bridge. (Earlier versions of this document cited them as a classical fact "(Ψ)" whose exact scope was unchecked.) The only inputs are classical facts listed in §I.7: Fenchel–Nielsen coordinates (FN), (GC1), the collar lemma (Coll), Mumford compactness (Mum), properness of filling length functions (Prop), Thurston's stretch-map rigidity (Th) and elementary hyperbolic trigonometry (Hex).

**Conventions.**
- S is the closed reference surface of genus g. Σ′ ⊂ S is an essential subsurface: a component of S cut open along a multicurve, with boundary curves γ_1, …, γ_r. If both sides of one curve of S belong to Σ′, they count as two distinct boundary components. Σ′° is Σ′ with each γ_j replaced by a puncture, labelled by γ_j. T(Σ′°) is its Teichmüller space, M(Σ′°) the moduli space with labelled punctures, M̄(Σ′°) its Deligne–Mumford compactification with a fixed metric d, and [Y] the class of Y ∈ T(Σ′°).
- A curve β ⊂ Σ′ is *non-peripheral* if it is an essential closed curve in int Σ′ not freely homotopic into a boundary curve.
- If Σ′ is a pair of pants, T(Σ′°) is a point and everything below is trivial. So assume it is not.
- **FN data.** Let P′ be a pants decomposition of Σ′ (interior curves only), with fixed seams in every pair of pants: three disjoint arcs joining the cuffs in pairs. For b ∈ [0,∞)^r and c = (ℓ_α, τ_α)_{α∈P′} ∈ (ℝ_{>0}×ℝ)^{P′}, Φ_{P′}(b,c) is the marked surface obtained as follows. Each pair of pants with cuff lengths given by c and b is the double H ∪ H̄ of a right-angled hexagon H across its seams; a side on γ_j of length b_j/2 = 0 is replaced by an ideal vertex (a cusp). The pants are glued along each α ∈ P′ with twist τ_α. By (FN), c ↦ Φ_{P′}(0,c) is a homeomorphism (ℝ_{>0}×ℝ)^{P′} → T(Σ′°).
- For X ∈ T_g let c(X) be the P′-coordinates of X and b(X) = (ℓ_{γ_j}(X))_j. Then the bordered surface X|Σ′ obtained by cutting X along the geodesics γ_j is Φ_{P′}(b(X), c(X)), and **ψ_{Σ′,P′}(X) := Φ_{P′}(0, c(X))**. For every non-peripheral β ⊂ Σ′, ℓ_β(X|Σ′) = ℓ_β(X), since π_1(Σ′) ⊂ π_1(S) and the holonomy of X|Σ′ is the restriction.
- A *vertex subsurface* of z̃ ∈ T̄_g is a component Σ′ of S cut along the node curves of z̃. Then every boundary curve of Σ′ is a node curve of z̃, no node curve of z̃ lies in int Σ′, and the component of z̃ on Σ′ is a marked point W_{Σ′}(z̃) ∈ T(Σ′°), with cusps at the nodes on ∂Σ′.

**Proposition Ψ.**
- **(a) Continuity and naturality.** ψ_{Σ′,P′} : T_g → T(Σ′°) is continuous. For h ∈ Mod_g, ψ_{hΣ′,hP′}(hX) = h_*ψ_{Σ′,P′}(X), where h_* : T(Σ′°) → T(hΣ′°) is the change of marking. In particular [ψ_{hΣ′,hP′}(hX)] = [ψ_{Σ′,P′}(X)], with the punctures of hΣ′ labelled by the h-images of the γ_j. If h is a product of Dehn twists about curves that are disjoint from int Σ′ (for example boundary curves of Σ′), then ψ_{Σ′,P′}(hX) = ψ_{Σ′,P′}(X).
- **(b) Shrinking.** For every X ∈ T_g, every P′ and every non-peripheral closed curve β ⊂ Σ′, ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X). Consequently, for every η′ > 0 there is ε > 0, depending only on the type of Σ′°, such that: if some non-peripheral simple closed curve of Σ′ has ℓ_X < ε (for instance Ext_X < ε/π), then d([ψ_{Σ′,P′}(X)], ∂M̄(Σ′°)) < η′, for every P′.
- **(c) Convergence, uniformly in the pants decomposition.** Let X_k ∈ T_g with X_k → z̃ in T̄_g, and let Σ′ be a vertex subsurface of z̃. Let P′_k be **any** sequence of pants decompositions of Σ′. Then ψ_{Σ′,P′_k}(X_k) → W_{Σ′}(z̃) in T(Σ′°), and hence [ψ_{Σ′,P′_k}(X_k)] → [W_{Σ′}(z̃)] in M(Σ′°).
- **(d) Chart form.** Let J, a lift J̃, U, Tw, B = U/Tw and p_U be as in (CD) (§0.4), let y be a label of J, and Σ_y its marked vertex subsurface. Let w_k ∈ U ∩ T_g with p_U(w_k) → p ∈ L_y, and let P_k be any pants decompositions of Σ_y. Then [ψ_{Σ_y,P_k}(w_k)] → [F_y(p)].

The uniformity in (c) and (d) matters: in the applications the subsurface is fixed only up to a mapping class that varies with the sequence (h_k in Lemma TI(3), the twists τ_k in Lemma L.1, the chart translates in §5.8), and transporting by it replaces a fixed pants decomposition by a varying one.

### Proof of (a)
Extend P′ to a pants decomposition P of S by adding the curves γ_j and a pants decomposition of S ∖ Σ′, and extend the seams. By (FN), the P-coordinates are a homeomorphism T_g → (ℝ_{>0}×ℝ)^P. The P′-coordinates depend only on the pants inside Σ′. So ψ_{Σ′,P′} is the composite of the projection to the P′-coordinates with the homeomorphism Φ_{P′}(0,·), hence continuous.

Naturality: the geodesic representative of hα on hX is that of α on X, and h carries seams to seams. So the (hP′, h(seams))-coordinates of hX are the (P′, seams)-coordinates of X, and ψ_{hΣ′,hP′}(hX) = h_*ψ_{Σ′,P′}(X). If h is a product of twists about curves disjoint from int Σ′, h can be supported in annuli outside int Σ′; then hΣ′ = Σ′, hP′ = P′ with the same seams, the marking of X|Σ′ is unchanged, and the P′-coordinates of hX and X agree. ∎

### Proof of (b): the shrinking lemma

**Lemma S.** Let b ∈ ℝ_{>0}^r and c ∈ (ℝ_{>0}×ℝ)^{P′}. There is a continuous map F : Φ_{P′}(b,c) → Φ_{P′}(0,c) that does not increase the length of any rectifiable path and induces the marking identification on π_1(Σ′). Consequently ℓ_β(Φ_{P′}(0,c)) ≤ ℓ_β(Φ_{P′}(b,c)) for every non-peripheral closed curve β ⊂ Σ′; in particular ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X) for X ∈ T_g.

**Reduction to hexagons.** The idea is to build F pants by pants, and each pants map from a map of one hexagon H_a (boundary sides of length a = b_j/2 > 0) to the corresponding hexagon H_0 (those sides replaced by ideal vertices). The hexagon map f must have these properties:

- (H1) f is 1-Lipschitz for the hyperbolic metrics. Both hexagons are convex in ℍ², so this is the same as for their intrinsic metrics.
- (H2) f maps each "interior half-cuff" side (half of a curve of P′) isometrically onto the corresponding side, matching endpoints.
- (H3) f maps each seam side into the same seam side (or its closure through ideal vertices).
- No condition is imposed on the sides lying on the γ_j.


**Why such hexagon maps suffice.**
- Each pants is Y = H ∪ H̄, where H̄ is the mirror image across the seams. The pants map is f on H and σ_0 f σ_a on H̄, where σ is the reflection. Because f maps seams into seams, which σ fixes pointwise, the two definitions agree on the seams.
- On each interior cuff α, the pants map is the isometry fixing the seam feet. So two pants glued along α with twist τ_α, in both surfaces, give a well-defined continuous F. Pants not touching ∂Σ′ are mapped by the identity.
- F is locally 1-Lipschitz. Near any point, a geodesic segment between two nearby points crosses the hexagon sides (geodesic arcs) at finitely many points z_1, …, z_m, and each subsegment lies in one hexagon, where F is 1-Lipschitz; the triangle inequality gives d(Fx,Fy) ≤ Σ d(Fz_l, Fz_{l+1}) ≤ d(x,y). A locally 1-Lipschitz map does not increase lengths of paths.
- **F induces the marking identification.** F maps each hexagon into the corresponding hexagon (closed up through its ideal vertices), each seam into the same seam, and each interior half-cuff onto itself fixing the seam feet. Homotope a loop in Σ′ off the boundary sides so that it crosses seams and half-cuffs transversally finitely often; it becomes a concatenation of arcs, each inside one hexagon with endpoints on seams or half-cuffs. F carries each arc to an arc in the corresponding hexagon with endpoints on the same seams/half-cuffs; since hexagons are contractible and seams and half-cuffs are connected, the image loop is freely homotopic to the corresponding loop of Φ_{P′}(0,c) under the standard (marking) identification.
- Hence for the closed geodesic β of Φ(b,c), F∘β is freely homotopic to β in Φ(0,c) and has length ≤ ℓ_β(Φ(b,c)). Since β is non-peripheral, it has a geodesic representative in Φ(0,c), whose length minimises length in the free homotopy class. This gives the inequality.
- For X ∈ T_g: X|Σ′ = Φ(b(X), c(X)), ψ(X) = Φ(0, c(X)), and ℓ_β(X|Σ′) = ℓ_β(X).

Each pants of P′ has 1 or 2 cuffs among the γ_j; 3 cuffs would make Σ′ a pair of pants. If some γ_j coincide as curves of S they are still distinct boundary components of Σ′, so no pants has the same γ_j twice. This leaves two hexagon cases.

**Case 1: one boundary side.** Write H_a for the hexagon with alternate sides a (on γ), x, y. Here x and y are halves of interior cuffs, possibly two halves of the same curve. Its seams are s_{ax}, s_{xy}, s_{ya}, with V = x ∩ s_{xy} and W = y ∩ s_{xy}. H_0 is the hexagon with sides x, y and an ideal vertex ξ in place of a.

Write s_a = |s_{xy}(H_a)| and s_0 = |s_{xy}(H_0)|. By (Hex), cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0, so s_a > s_0. Put d = (s_a − s_0)/2 > 0.

*Fermi picture.* Use Fermi coordinates (τ, h) about the line of s_{xy}: τ is the position of the foot (τ = 0 at V), and h ≥ 0 is the distance on the side of the hexagon.
- The lines of x and y are the fibres τ = 0 and τ = s (s = s_a or s_0).
- By convexity, each fibre τ = τ_0 with 0 ≤ τ_0 ≤ s meets the hexagon in a segment {0 ≤ h ≤ top(τ_0)}.
- The τ-projections of the top sides s_{ax}, a, s_{ya} are consecutive intervals [0, τ_C], [τ_C, τ_D], [τ_D, s_a]. Here C = s_{ax} ∩ a and D = a ∩ s_{ya}; monotonicity comes from (Hex). A side line cannot be perpendicular to s_{xy}: e.g. s_{ax} and s_{xy} are both perpendicular to the x-line, hence ultraparallel.
- In H_0, the ideal vertex ξ projects to a point B′ at τ = u_1′ ∈ (0, s_0); write u_2′ = s_0 − u_1′. The perpendicular ray ω′ from B′ to ξ lies in H_0. In H_0, s_{ax} projects onto [0, u_1′) and s_{ya} onto (u_1′, s_0].

*x-placement.* Put H_a and H_0 in ℍ² so that they share V, the x-side and the direction of s_{xy}. Then they also share the full line of s_{ax}: it is the perpendicular to the x-side at its other endpoint, on the same side. H_a's seam s_{ax} is the segment of this line from the top of x to C, and C lies on H_0's ray from the top of x to ξ. By monotonicity of the projection along that ray, τ_C < u_1′.

*y-placement.* Symmetrically, sharing W, the y-side and s_{ya}, one gets s_a − τ_D < u_2′.

*Cut.* Let u := u_1′ + d. Then:
- τ_C < u_1′ < u;
- τ_D > s_a − u_2′ = u_1′ + 2d > u, using s_a = s_0 + 2d.

So the fibre τ = u in H_a is a segment c from B ∈ s_{xy} up to a point of the side a. Cut H_a = P_1 ∪ P_2 along c, with P_1 = H_a ∩ {τ ≤ u} and P_2 = H_a ∩ {τ ≥ u}, both convex. Likewise cut H_0 = Q_1 ∪ Q_2 along ω′, with Q_1 = H_0 ∩ {τ ≤ u_1′}, both convex.

*The map.* In the x-placement, set f := π_{Q_1} on P_1 (nearest-point projection, 1-Lipschitz by (Hex)). In the y-placement, set f := π_{Q_2} on P_2. Check P_1; P_2 is symmetric.
- The x-side and the seam segment s_{ax} of P_1 lie in Q_1 (on its boundary), so they are fixed. This gives (H2) and (H3) for them.
- Points of s_{xy} with τ ≤ u_1′ are fixed. A point with u_1′ < τ ≤ u projects to the half-plane {τ ≤ u_1′} at B′ (s_{xy} ⟂ ω′ at B′), and B′ ∈ Q_1. So the base goes into s_{xy}.
- A point q ∈ c at height h projects to the half-plane {τ ≤ u_1′} at its foot q′ on the line of ω′. This is the orthogonal projection between two lines perpendicular to s_{xy} at distance d, so q′ is on the upper half-line, i.e. on the ray ω′ ⊂ Q_1, at a height p(h, d) depending only on (h, d). Hence π_{Q_1}(q) = q′.
- The side a goes somewhere into Q_1, which is allowed.
- From P_2 the cut c also lies at distance d beyond ω′: in the y-placement its foot is at distance s_a − u = u_2′ + d from W. So π_{Q_2}(q) is the point of ω′ at height p(h, d) too. Both definitions agree on c, and f is continuous on H_a.
- f is 1-Lipschitz on H_a: a geodesic of H_a crosses c at most once, and each piece is mapped 1-Lipschitz.
- (H2) holds for both x and y, and (H3) holds: s_{ax} → s_{ax}, s_{xy} → s_{xy}, s_{ya} → s_{ya}.

**Case 2: two boundary sides.** Write H_a for the hexagon with alternate sides a_1, a_2 (on γ's), x (an interior half-cuff), and seams σ_1 = s_{a_1 x}, σ_2 = s_{x a_2}, s_{12}. H_0 has sides x and two ideal vertices ξ_1, ξ_2. Its seams are:
- the ray L_1 from the endpoint A_1 of x to ξ_1, perpendicular to x;
- the ray L_2 from the endpoint A_2 of x to ξ_2, perpendicular to x;
- the full geodesic M = ξ_1ξ_2.

Place H_a so that it shares x, L_1 and L_2. Then σ_i = [A_i, C_i] ⊂ L_i, and f := π_{H_0}|_{H_a} is 1-Lipschitz.
- x is fixed, giving (H2). No point of H_a projects into the interior of x, because H_a lies on the inner side of the x-line.
- σ_i is fixed.
- It remains to show that s_{12}(H_a) lies in the closed half-plane beyond M (the side not containing H_0). Then each of its points projects to its foot on M, and M lies entirely in ∂H_0, so (H3) holds.

s_{12}(H_a) is the segment D_1D_2, with D_i = a_i ∩ s_{12}. By convexity of half-planes it suffices that D_1 and D_2 are beyond M. By symmetry, treat D_1.

Use the upper half-plane with ξ_1 = ∞ and A_1 = iα. Then:
- L_1 = {i t : t ≥ α};
- x is the arc of |z| = α from iα to A_2 = α e^{iφ}, with cot(φ/2) = e^{x}, so sin φ = 1/cosh x and cos φ = tanh x;
- L_2 is the circle orthogonal to |z| = α at A_2, with centre α/cos φ and radius α tan φ; its outer endpoint is ξ_2 = α(1 + sin φ)/cos φ = α coth(x/2);
- M = {Re z = α coth(x/2)}, and H_0 ⊂ {Re z ≤ α coth(x/2)};
- C_1 = i α e^{σ_1};
- the a_1-line is the circle |z| = α e^{σ_1}, and D_1 = α e^{σ_1} e^{iθ}, where arclength a_1 from the top means cot(θ/2) = e^{a_1}, i.e. cos θ = tanh a_1.

So D_1 is beyond M iff e^{σ_1} tanh a_1 ≥ coth(x/2), i.e. e^{σ_1} ≥ R := cosh a_1 (cosh x + 1)/(sinh a_1 sinh x).

By (Hex), cosh σ_1 = (cosh a_2 + cosh a_1 cosh x)/(sinh a_1 sinh x). Hence R − cosh σ_1 = (cosh a_1 − cosh a_2)/(sinh a_1 sinh x).
- If a_1 ≤ a_2 this is ≤ 0, and we are done.
- Otherwise we need sinh σ_1 ≥ (cosh a_1 − cosh a_2)/(sinh a_1 sinh x). With Nn = cosh a_1 cosh x + cosh a_2 and Dd = sinh a_1 sinh x, this means Nn² − Dd² ≥ (cosh a_1 − cosh a_2)². Factoring:

  Nn² − (cosh a_1 − cosh a_2)² = cosh a_1 (cosh x + 1)(cosh a_1 (cosh x − 1) + 2 cosh a_2),

  while Dd² = sinh² a_1 (cosh x − 1)(cosh x + 1). The required inequality reduces to

  cosh² a_1 (cosh x − 1) + 2 cosh a_1 cosh a_2 ≥ sinh² a_1 (cosh x − 1),

  which is obvious.


(The two inequalities used — cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0 in Case 1, and e^{σ_1} ≥ R in Case 2 together with the factorisation displayed there — were also checked numerically on 2·10^5 random hexagons.)

*Consequence (the second sentence of (b)).* The set K := {[Y] ∈ M̄(Σ′°) : d([Y], ∂M̄(Σ′°)) ≥ η′} is a compact subset of M(Σ′°). The systole is continuous and positive on M(Σ′°), so it is ≥ some ε > 0 on K. If ℓ_β(X) < ε for a non-peripheral simple β, then sys(ψ_{Σ′,P′}(X)) ≤ ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X) < ε by Lemma S, so [ψ_{Σ′,P′}(X)] ∉ K. Maskit's comparison ℓ ≤ π Ext gives the parenthetical form. ∎

### Proof of (c)
Write Y_k := ψ_{Σ′,P′_k}(X_k) and W := W_{Σ′}(z̃).
1. **Bounded lengths of a filling set.** Fix finitely many non-peripheral simple closed curves β_1, …, β_p of Σ′ that fill Σ′° (every non-peripheral simple closed curve of Σ′ meets some β_j essentially; e.g. a pants decomposition of Σ′ together with one dual curve for each of its curves). Since Σ′ is a vertex subsurface of z̃, (GC1) gives ℓ_β(X_k) → ℓ_β(W) for every non-peripheral closed curve β ⊂ Σ′. By Lemma S, ℓ_{β_j}(Y_k) ≤ ℓ_{β_j}(X_k), which is bounded in k. This bound does not depend on the P′_k.
2. **Precompactness.** By (Prop), {Y ∈ T(Σ′°) : ℓ_{β_j}(Y) ≤ C for all j} is compact. So every subsequence of (Y_k) has a further subsequence converging to some W′ ∈ T(Σ′°).
3. **Identification of the limit.** Length functions are continuous on T(Σ′°). So for every non-peripheral closed curve β ⊂ Σ′, ℓ_β(W′) = lim ℓ_β(Y_k) ≤ lim ℓ_β(X_k) = ℓ_β(W), by Lemma S and (GC1). Peripheral curves are cusps on both surfaces. By Thurston's theorem (Th), applied to the identity marking W → W′ (all closed geodesics of W are non-peripheral, and lengths do not increase), the identity is homotopic to an isometry, i.e. W′ = W in T(Σ′°).
4. Every subsequence has a further subsequence converging to W, so Y_k → W. The map T(Σ′°) → M(Σ′°) is continuous. ∎

### Proof of (d)
The quotient map U → U/Tw = B is open. Fix w′ ∈ U over p and a neighbourhood basis O_1 ⊃ O_2 ⊃ … of w′ in U. For each j, p_U(O_j) is a neighbourhood of p, so for k ≥ k_j there is τ ∈ Tw with τw_k ∈ O_j. Choosing τ_k accordingly gives τ_kw_k → w′ in T̄_g.
- The node curves of w′ are the α_e with s_e(p) = 0. Since p ∈ L_y, all boundary curves of Σ_y are nodes of w′, and no α_e lies in int Σ_y (Σ_y is a component of S ∖ ∪_e α_e). So Σ_y is a vertex subsurface of w′, and by (CD) its component is F_y(p): [W_{Σ_y}(w′)] = [F_y(p)].
- τ_k is a product of twists about the α_e, which are disjoint from int Σ_y. By (a), ψ_{Σ_y,P_k}(w_k) = ψ_{Σ_y,P_k}(τ_kw_k).
- By (c), applied to τ_kw_k → w′ and the pants decompositions P_k, [ψ_{Σ_y,P_k}(τ_kw_k)] → [F_y(p)]. ∎

*Remark (what is not claimed).* For a fixed point X, ψ_{Σ′,P′}(X) depends on P′; only limits at vertex subsurfaces are intrinsic. Convergence when node curves of z̃ lie inside Σ′ (and cross P′) is neither proved nor used: every use is at a vertex subsurface, which is guaranteed in §5 by (b0) and Lemma TI(2), and in Lemma L.1 by the pattern S.


## I.7 Cited classical facts (Part I) (all cited from memory; stated in the form used)

- **(Pl) Plumbing / Kuranishi charts** (Masur 1976; Bers; Wolpert). Near P ∈ Δ_G there is an orbifold chart Def(P)/Aut(P) of M̄_g with coordinates (z,(t_e)) as described in §1. The component deformations come from smooth Beltrami differentials supported in fixed compacts K_w, so that h_z → id in C^∞ on compacts. Plumbing z_ew_e = t_e is done in fixed coordinate discs. The fibres carry a labelling of components by V(G). Openness of versality: near any of its points p, Def(P) is a Kuranishi chart for the fibre over p.
- **(Dual) Teichmüller duality** (Teichmüller, Hamilton, Krushkal, Royden). For a tangent vector v at X ∈ T_{g,n} represented by μ: ‖v‖_T = sup{Re∫μφ : φ ∈ Q(X), ‖φ‖_1 = 1}. The supremum is attained at a unique norming φ = q_v, the extremal Beltrami differential is ‖v‖ q̄_v/|q_v|, and the Teichmüller disc tangent to v is the one generated by q_v.
- **(Bun)** For a plumbing family, π_*(ω^{⊗2}) is locally free of rank 3g−3. Its fibre at a stable curve consists of differentials on the components with at most double poles at node branches and equal quadratic residues a_e on the two branches. The a_e(φ) = (2πi)^{-1}∮_{|z_e|=r_0} z_eφ/dz_e are holomorphic and linearly independent at P, with common kernel ⊕_w Q(Y_w).
- **(GC1)–(GC3) Augmented Teichmüller space** (Abikoff; Bers; Fenchel–Nielsen).
  - (GC1) If (X_n,f_n) → P̃ in the γ-stratum, then ℓ(γ_e) → 0, and suitably conjugated holonomies restricted to Γ_w converge to type-preserving holonomies of P̃_w, with ℓ_{X_n}(c) → ℓ_{P̃_w}(c) for non-peripheral c ⊂ Σ_w.
  - (GC2) Conversely, if ℓ(γ_e) → 0 and conjugates of ρ_n|_{Γ_w} converge to discrete faithful type-preserving R_w with finite-area quotient, then (X_n,f_n) converges to the γ-stratum point with components H/R_w.
  - (GC3) If X_n → P in M̄_g, then after a subsequence there are markings with (X_n,f_n) convergent in T̄ to a lift of P.
- **(CD) Canonical chart description** (Abikoff, Bers, Hubbard–Koch, Wolpert): as stated in §0.4. Also: hyperbolic metrics of plumbing fibres vary continuously off the collars, and ℓ(α_e) → 0 (equivalently Ext(α_e) → 0) iff s_e → 0, uniformly on compact parts of the chart.
- **(Thin)** (collar lemma; Abikoff topology). If X_k → z̃ in T̄_g and ℓ_1 is less than half the systole of every component of z̃, then for large k the curves of hyperbolic length < ℓ_1 on X_k are exactly the node curves of z̃ (in the marking), and their lengths tend to 0.
- **(FN) Fenchel–Nielsen coordinates** (Fenchel–Nielsen; Wolpert for analyticity). For a pants decomposition P of S (with seams), the coordinates (ℓ_α, τ_α)_{α∈P} give a real-analytic diffeomorphism T_g → (ℝ_{>0}×ℝ)^P. For a finite-type surface F° with cusps and a pants decomposition P of F, c ↦ Φ_P(0,c) (gluing of hexagons with ideal vertices, §I.6A) is a homeomorphism (ℝ_{>0}×ℝ)^P → T(F°). The coordinates of α ∈ P depend only on the (one or two) pants adjacent to α.
- **(Hex) Hyperbolic plane geometry.** Nearest-point projection onto a closed convex subset of ℍ² is 1-Lipschitz. The fibres of nearest-point projection onto a geodesic line L are the geodesics perpendicular to L; so its restriction to a geodesic disjoint from L and not perpendicular to it is injective and continuous, hence monotone. In a right-angled hexagon with alternate sides a, x, y, the side opposite to a has cosh s = (cosh a + cosh x cosh y)/(sinh x sinh y); this stays valid for a = 0 (ideal vertex).
- **(Coll) Collar lemma.** If α is a simple closed geodesic of length ℓ and β a closed geodesic, then ℓ_β ≥ i(α,β)·2 arcsinh(1/sinh(ℓ/2)).
- **(Mum) Mumford compactness.** For a finite-type F° and ε > 0, {[Y] ∈ M(F°) : sys(Y) ≥ ε} is compact.
- **(Prop) Properness of filling length functions** (Kerckhoff, *The Nielsen realization problem*, 1983, Lemma 3.1, and its standard extension to finite-area surfaces with cusps). If β_1, …, β_p fill F° (every essential non-peripheral simple closed curve meets some β_j essentially), then {Y ∈ T(F°) : ℓ_{β_j}(Y) ≤ C ∀j} is compact. *Sketch:* by (Coll) the systole is ≥ ε(C) > 0 on this set; by (Mum) there are mapping classes φ_k with φ_kY_k in a fixed compact set K; by Wolpert's inequality ℓ_c(Y′) ≤ e^{2d_T(Y,Y′)}ℓ_c(Y) only finitely many curves have length ≤ C somewhere on K, so the φ_k(β_j) range over a finite set; the subgroup of the pure mapping class group fixing every β_j is finite (Alexander method), so the φ_k range over a finite set, and the Y_k lie in finitely many translates of K.
- **(Th) Thurston's stretch-map rigidity** (Thurston, "Minimal stretch maps between hyperbolic surfaces", 1986 preprint, cited from memory; the same fact is (Th) of Part II §10). Let X, Y be complete hyperbolic surfaces of finite area and ψ : Y → X a homeomorphism (cusps to cusps). If ℓ_X(ψ(c)) ≤ ℓ_Y(c) for every closed geodesic c of Y, then ψ is homotopic to an isometry.
- **(Ext) Maskit's comparison.** ℓ_X(γ)/π ≤ Ext_X(γ) ≤ (ℓ_X(γ)/2)e^{ℓ_X(γ)/2}.
- **Kerckhoff's formula.** d_T(X,Y) = ½ log sup_γ Ext_Y(γ)/Ext_X(γ). In particular Ext_Y(γ) ≤ e^{2d_T(X,Y)}Ext_X(γ), and Ext is K-quasi-invariant.
- **(QC1)** (Lehto–Virtanen II.5). Normalised K-qc maps of Ĉ form a sequentially compact family with K-qc limits. K-qc embeddings of a domain omitting two values form a normal family whose limits are constant or K-qc embeddings.
- **(QC2)** (Lehto–Virtanen V.5.3; Ahlfors V). If μ_n → μ a.e. with ‖μ_n‖_∞ ≤ k < 1, then the normalised solutions w^{μ_n} → w^μ uniformly on Ĉ.
- **(QC3)** A qc map with μ = 0 a.e. is conformal (Weyl). If μ_f = μ_h a.e., then f∘h^{-1} is conformal.
- **Royden's theorem.** The Kobayashi metric of T_{g,n} equals the Teichmüller metric. Hence a Teichmüller disc is a holomorphic isometric embedding of (H, d_H), and holomorphic maps are contractions.
- **Bers embedding.** T_{g,n} is biholomorphic to a bounded domain in C^{3g−3+n}.
- **Masur.** Cylinder directions of a finite-area quadratic differential are dense in RP¹. The q-geodesic representative of a curve realises its intersection numbers with the horizontal and vertical measured foliations.
- **Veech.** The Veech group of a Teichmüller curve is a non-cocompact lattice. A cylinder direction of a lattice surface is parabolic (Veech dichotomy), so Teichmüller curves are never compact.
- **Selberg's lemma.** A finitely generated linear group has a torsion-free normal subgroup of finite index.
- **Chow; Remmert.** Closed analytic subsets of projective varieties are algebraic. The image of an irreducible analytic set under a proper (finite) holomorphic map is an irreducible analytic set.
- **Krull / active lemma.** If S is a pure 2-dimensional analytic set and f is holomorphic and not identically 0 on any local component at a zero z, then {f = 0} ∩ S is pure 1-dimensional at z.
- **Milnor conic structure.** For an analytic germ (X,0) and small round balls B_ε, X ∩ B_ε is homeomorphic to the cone over its link. The irreducible components of X ∩ B_ε represent the germ components, and the branches of a curve germ meet only at 0 in B_ε.
- **Cartan.** For a properly discontinuous action of a countable group by biholomorphisms, T/Γ is a normal complex space. Near a point with stabiliser A there is an A-invariant ball with linear action, precisely invariant, and B/A → T/Γ is an open embedding. Invariant polynomials of a finite group separate orbits.
- **Normalisation.** The normalisation of an irreducible germ is an irreducible normal germ (one point over 0). A holomorphic map from a normal (for example 1-dimensional smooth) space whose image is not contained in the non-normal locus lifts uniquely to the normalisation. Normal surfaces have isolated singularities.
- **(Res)** (resolution of normal surface germs; Zariski's main theorem). There is a resolution π: W̃ → W, biholomorphic off ŝ_0, with compact connected exceptional curve Exc = ∪E_k. (Str): the strict transform of an irreducible curve germ meets Exc in exactly one point.
- **(Neg)** (Du Val, Mumford, Grauert). The intersection matrix (E_k·E_j) is negative definite.
- **(RA)** (Grauert; Cartan's Theorem A). A line bundle of positive degree on every E_k becomes, after shrinking W and passing to a power, globally generated on W̃.
- **Strict Schwarz–Pick.** A proper simply connected subdomain Ω ⊊ H has hyperbolic metric strictly larger than that of H at every point.
- **Elementary analysis:** Montel, Riemann extension, the identity theorem, the maximum principle, Baire, and Gauss–Bonnet for flat surfaces with conical singularities.

