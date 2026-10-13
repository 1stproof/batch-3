# Part II — a self-contained proof of Theorem A under the embedded orbifold reading

**Status line.**
- **Main result.** This text gives a complete proof of Theorem A, using only:
  - the Part I statements I.2, I.3, I.5 and I.6, in the precise forms stated in §1.6;
  - classical theorems, listed with precise statements at the end.
  The proof does not use I.1, I.4 or Lemma PT directly; I.1 enters only through I.2/I.3.
- **One flagged citation.** There is a single citation whose scope I cannot check from memory: the Imayoshi–Shiga finiteness theorem for targets with marked points (GAP G1). It is used once, in Theorem 4.4(b), and only through the endpoint step §9.3.
  - It is resolved for vertex types (1,1) and (0,4) by the generalised de Franchis theorem.
- **A shorter route.** Under (R2^orb) the original "anchored sheet / Theorem N / walk-chain induction" machinery collapses:
  - at every boundary point Q the lift locus of the transported point Q_t is a single Aut(Q)-fixed point p(t) (Prop. 5.2);
  - the descended transport Π_t carries constant vertex values along pieces (Theorem 4.4(a) together with Lemma 6.1).
  So the value of the tracked copy at p(t) can be read from both sides of every transition. The induction along the walk chain becomes a chain of equalities [φ_{c_m}(t)] = [φ_{c_{m+1}}(t)] (§9).
  - This route needs neither Theorem N, nor Lemma U (of the original), nor anchored sheets, nor Lemmas T, S, J, Theorem R, nor the holomorphy of t ↦ Q_t, nor Theorem X*_all, nor Lemma PT.
- **Appendix A.** As requested, Appendix A proves the coarse-valid lemmas of the original route under the weakest hypotheses their proofs allow, labelled accordingly. They are not used in the proof of Theorem A.
- **Labels.** Every lemma is labelled [coarse] (uses at most (R1), (R2)), [coarse+Rig], [orb] (uses (R2^orb), with the items (a)–(d) used listed), or [none] (no hypothesis on the family).

---

## 1. Conventions, readings, and the Part I input

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

### 1.2 The data of the problem

- V_0 ⊂ M_g is a smooth totally geodesic complex surface. 𝒱 ⊂ M_g × Δ is the family, V_t its fibres, and closures are taken in M̄_g, respectively M̄_g × Δ.
- Γ is the fixed stable graph. By the problem's assumption, Δ_Γ is of product type: ξ_Γ : ∏_{j} M_{g_j,n_j} → Δ_Γ is an isomorphism, and π_j = pr_j∘ξ_Γ^{-1}.
- ∂V_t := closure(V_t) ∩ Δ_Γ = A^Γ_t. It has dimension 1, and π_i(∂V_t) = {Y_t} with Y_t ∈ M_{g_i,n_i}.
- **Dimension of B_t (used tacitly).** Under (R1), B_t is a closed analytic subset of dimension ≤ 1.
  - Every irreducible component Z of the analytic set closure(V_t) contains points of V_t: the points of Z on no other component form a non-empty open subset of closure(V_t), and V_t is dense.
  - So Z meets the 2-dimensional manifold V_t in a non-empty open set, and dim Z = 2.
  - B_t = closure(V_t) ∩ ∂M̄_g is analytic and contains no open subset of any Z. Hence dim B_t ≤ 1.
  - Consequently every Â_t has dimension ≤ 1.

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

**The two orbifold readings (qualification (Rep-6)).** "Regard M̄_g and its strata as orbifolds" admits two inequivalent precise forms.
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
- **J0** (with repair R3′, valid in every boundary stratum). In the situation of I.2, there is a holomorphic F_0 : H → T_G with:
  - (i) p∘F_0 = ν∘u_0;
  - (ii) f_0 := pr_j∘F_0 : H → T_j is an isometric holomorphic embedding. Here H carries the Poincaré metric of curvature −4, T_j the Teichmüller metric, and the image is a Teichmüller disc;
  - (iii) for every λ ∈ Λ, the set R(λ) := {g ∈ Mod_Π : F_0∘λ = g∘F_0} is a coset gS of the finite group S := {s ∈ Mod_Π : s∘F_0 = F_0}. Moreover R(λ) ⊂ N(S), the normaliser, and R(λμ) = R(λ)R(μ).
  - Consequently λ ↦ R(λ) is a homomorphism Λ → N(S)/S.

**I.5 (Proposition K_w, walk chain, with its repairs; a statement about V_0 only).** There are the following data.
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

## 2. Preliminaries that use at most (R1), (R2)

**Lemma 2.1 (algebraicity and finite type) [coarse: (R1) only].** For every t ∈ Δ and every boundary stratum G:
1. Â_t is a closed algebraic subset of dimension ≤ 1 of the quasi-projective variety ∏_w M_w. It has finitely many pieces and finitely many isolated points, and its singular set Sing(Â_t) is finite.
2. For a piece E, the normalisation Ê is a compact Riemann surface minus finitely many points, and ν : Ê → E is finite (hence proper).
3. For a piece E, M(E) ≠ ∅. K(E) is an irreducible projective curve in ∏_{u∈M(E)} M̄_u, not contained in the boundary ∂ := ∏_{u∈M(E)} M̄_u ∖ ∏_{u∈M(E)} M_u. The set K(E) ∩ ∂ is finite.

*Proof.*
1. By (R1), closure(V_t) is a closed analytic subset of the projective variety M̄_g, hence algebraic (Chow).
   - Δ_G is locally closed algebraic, so A_t is locally closed algebraic. ξ_G is a morphism (St4), so Â_t is a closed algebraic subset of ∏_w M_w, of dimension ≤ 1 by §1.2.
   - The analytic irreducible components of an algebraic set are its algebraic irreducible components (fact (Irr)). There are finitely many of them.
   - The singular set of a ≤1-dimensional algebraic set is a closed algebraic subset of dimension 0, hence finite.
2. E is an irreducible quasi-projective curve. Its (analytic = algebraic) normalisation is a smooth irreducible quasi-projective curve, i.e. a compact Riemann surface minus finitely many points, and ν is finite.
3. **M(E) ≠ ∅**, since E is not a point.
   - The closure Ē of E in the projective variety ∏_w M̄_w is an irreducible projective curve.
   - pr_{M(E)}(Ē) is compact, contains pr_{M(E)}(E), and lies in its closure. So K(E) = pr_{M(E)}(Ē) is an irreducible projective curve. It is not a point, because each u ∈ M(E) is non-constant on E.
   - K(E) ⊄ ∂, because pr_{M(E)}(E) ⊂ ∏ M_u. So K(E) ∩ ∂ is a proper closed algebraic subset of an irreducible curve, hence finite. ∎

**Definition 2.1′ (finite set of a piece).** For a piece E put M := M(E). F′(E) is the set of classes (C6) of all smooth irreducible components, with their special points, of all coordinates κ_u (u ∈ M) of all points κ ∈ K(E) ∩ ∂. By Lemma 2.1(3) it is finite.

**Lemma 2.2 (ends of pieces) [none].** Let E be a piece, z_n ∈ E, and z_n → κ in ∏_w M̄_w.
1. If κ_w ∈ ∂M̄_w, then w ∈ M(E).
2. If some coordinate of κ lies in the boundary, then pr_{M(E)}(κ) ∈ K(E) ∩ ∂.

*Proof.*
1. If w ∉ M(E), then pr_w(z_n) = φ_w(E) ∈ M_w for all n, so κ_w = φ_w(E) ∈ M_w.
2. pr_{M(E)}(z_n) ∈ pr_{M(E)}(E), so the limit lies in the closed set K(E). By (1), the boundary coordinate is indexed by an element of M(E), so pr_{M(E)}(κ) ∈ ∂. ∎

**Lemma 2.3 (holomorphy of t ↦ Y_t) [coarse: (R1), (R2)].** The map Δ → M_{g_i,n_i}, t ↦ Y_t, is holomorphic. Consequently, if Y_t = Y_0 for all t in a non-empty open subset of Δ, then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Continuity.** Fix z_0 ∈ ∂V_0. By (R2), H_t(z_0) ∈ ∂V_t, so Y_t = π_i(H_t(z_0)). This is continuous in t.
2. **Setting up a proper map.**
   - Put 𝒜′ := closure(𝒱) ∩ (closure(Δ_Γ) × Δ), which is analytic by (R1).
   - Let 𝒵 ⊂ 𝒜′ be the closed analytic subset lying over closure(Δ_Γ) ∖ Δ_Γ. Then 𝒜′ ∖ 𝒵 = ⋃_t ∂V_t × {t}.
   - Let 𝒜̂′ := (ξ̄_Γ × id)^{-1}(𝒜′) ⊂ ∏_j M̄_{g_j,n_j} × Δ, and let 𝒜̂ be the union of its irreducible components not contained in 𝒵̂ := (ξ̄_Γ × id)^{-1}(𝒵).
   - Then 𝒜̂ is the closure of 𝒜̂′ ∖ 𝒵̂ (fact (Cl)). Since ∏_j M̄_{g_j,n_j} is compact, the map φ := (pr_i, t) : 𝒜̂ → M̄_{g_i,n_i} × Δ is proper.
3. **The image is the graph.**
   - By Remmert's proper mapping theorem, Σ := φ(𝒜̂) is analytic.
   - Since φ is proper, hence closed, Σ = closure(φ(𝒜̂′ ∖ 𝒵̂)). By the product-type assumption, φ(𝒜̂′ ∖ 𝒵̂) = {(Y_t, t) : t ∈ Δ}.
   - This graph is already closed in M̄_{g_i,n_i} × Δ: if (Y_{t_n}, t_n) → (y, t), then y = Y_t by continuity. So Σ is the graph of Y.
4. **Holomorphy.**
   - The projection t : Σ → Δ is a homeomorphism, with inverse t ↦ (Y_t, t). So Σ is a 1-dimensional analytic set (topological dimension 2).
   - Σ is locally irreducible at every point: a curve germ with r ≥ 2 branches has punctured neighbourhoods with ≥ 2 components, whereas a disc does not.
   - So the normalisation ν_Σ : Σ̂ → Σ is a homeomorphism, and t∘ν_Σ : Σ̂ → Δ is a bijective holomorphic map of Riemann surfaces, hence biholomorphic.
   - Thus Y = pr_1∘ν_Σ∘(t∘ν_Σ)^{-1} is holomorphic.
5. **Identity theorem.** The set {t : Y_t = Y_0} is the preimage of a point under a holomorphic map, hence a closed analytic subset of the connected disc Δ. If it has interior, it is Δ. ∎

**Lemma 2.4 (topological characterisation of pieces) [none].** Let X be a closed analytic set of dimension ≤ 1 in a complex space, and let X^disc be the set of points of X having a neighbourhood in X homeomorphic to an open disc of ℝ². Then:
- the 1-dimensional irreducible components of X are exactly the closures of the connected components of X^disc;
- consequently, a homeomorphism X → X′ between two such sets maps the 1-dimensional irreducible components of X bijectively onto those of X′.

*Proof.* We use the local structure of curve germs (fact (CG)). If z ∈ X lies on a 1-dimensional component and the germ (X, z) has r ≥ 1 branches, then:
- z has arbitrarily small neighbourhoods U for which U ∖ {z} is a disjoint union of r punctured discs, one in each branch;
- each branch is homeomorphic to a disc.

1. **X^disc = the non-isolated points with r(z) = 1.**
   - If r(z) = 1, the branch is a disc neighbourhood.
   - Isolated points are not in X^disc.
   - Suppose r(z) ≥ 2 and z had a disc neighbourhood V. Choose U as above inside V, and a closed topological disc D ∋ z, a neighbourhood of z, with D ⊂ U. Then D ∖ {z} is connected, so it lies in one of the punctured discs of U ∖ {z}. But D is a neighbourhood of z, so it meets every branch. Contradiction.
2. **Points of X^disc lie on exactly one component.** A point on two distinct components has at least two branches, since distinct components share no open subset. For a component E, put X^disc_E := X^disc ∩ E. It is E minus a closed discrete subset of E: the points of E on other components, together with the multi-branch points of E.
3. **X^disc_E is connected and dense in E.** It equals ν(Ê ∖ D) with D closed and discrete in the connected Riemann surface Ê. So it is connected and dense in E.
4. **X^disc_E is a connected component of X^disc.**
   - It is open in X^disc, since it is the complement of the closed, locally finite union of the other components.
   - It is closed in X^disc, since E is closed.
   - X^disc = ⊔_E X^disc_E, so these are exactly the components.
5. **Homeomorphisms.** A homeomorphism maps X^disc onto X′^disc. It maps components to components and closures to closures. ∎

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

*Remark (repair Rep-1).* Let K_G be the kernel of the action of Mod_G on T_G. Then K_G ⊂ Stab(x̂) for every x̂. Correct examples of non-trivial elements of K_G:
- the elliptic involution of a (1,1)-vertex, extended by the identity;
- for a (1,2)-vertex whose two special points are the half-edges of a self-loop, the half-edge swap together with z ↦ p_1 + p_2 − z.

There are no (2,0)-vertices in boundary strata. Since every stabiliser contains K_G, condition (c) "modulo K_G" is equivalent to (c). None of this is used below.

---

## 3. The descended transport Π_t [orb]

Fix a boundary stratum G and use the notation of C5. Put Â := ⋃_t Â_t × {t} = (ξ_G × id)^{-1}(closure(𝒱) ∩ (Δ_G × Δ)), a closed subset of ∏_w M_w × Δ.

**Lemma 3.1 (descended transport) [orb: (a); (b) for all g ∈ Mod_G (descent uses only g ∈ Mod_Π; injectivity and surjectivity use general g); the inclusion "⊂" of (c); (d)].** There is a map Π : Â_0 × Δ → ∏_w M_w, Π_t := Π(·, t), with the following properties.
1. p∘H̃_t = Π_t∘p on Ã_0.
2. Π_t is a homeomorphism Â_0 → Â_t, ξ_G∘Π_t = H_t∘ξ_G, and Π_0 = id.
3. Θ : Â_0 × Δ → Â, (z, t) ↦ (Π_t z, t), is a homeomorphism.
4. For every y ∈ A_0 and t ∈ Δ: ξ_G^{-1}(H_t(y)) = Π_t(ξ_G^{-1}(y)).
5. For each piece E of Â_0, E_t := Π_t(E) is a piece of Â_t, and E ↦ E_t is a bijection between the pieces at times 0 and t.
6. For each piece E there is a homeomorphism Ĥ_t : Ê → Ê_t with ν_t∘Ĥ_t = Π_t∘ν. It maps the punctures (ends) of Ê bijectively to those of Ê_t.

*Proof.*
1. **Descent.** If p(x) = p(y) with x, y ∈ Ã_0, then y = gx with g ∈ Mod_Π, and H̃_t y = gH̃_t x by (b). So Π_t(p x) := p(H̃_t x) is well defined, and (1) holds.
   - By (a), ξ_G(Π_t(px)) = H_t(ξ_G p x) ∈ H_t(A_0) = A_t (R2). So Π_t maps into Â_t and ξ_G∘Π_t = H_t∘ξ_G.
   - By (d), Π_0 = id.
2. **H̃_t is injective on Ã_0.**
   - Let H̃_t x = H̃_t y. By (a), H_t(ξ_G p x) = H_t(ξ_G p y), and H_t is injective, so ξ_G p x = ξ_G p y.
   - By (St2), y = gx for some g ∈ Mod_G. Then g H̃_t x = H̃_t(gx) = H̃_t x by (b), so g ∈ Stab(H̃_t x) = Stab(x), using the inclusion "⊂" of (c). Hence y = x.
3. **H̃_t is onto Ã_t.**
   - Let y ∈ Ã_t. Then ξ_G p y ∈ A_t = H_t(A_0), so ξ_G p y = H_t(ξ_G p x) = ξ_G p H̃_t x for some x ∈ Ã_0.
   - By (St2), y = gH̃_t x = H̃_t(gx), and gx ∈ Ã_0 because Ã_0 is Mod_G-invariant.
4. **Π_t is bijective onto Â_t.**
   - Injective: if Π_t(px) = Π_t(py), then H̃_t y = gH̃_t x = H̃_t(gx) with g ∈ Mod_Π. By step 2, y = gx, so py = px.
   - Surjective by step 3.
5. **Joint continuity of Π.** p is the quotient map of a group action, hence open. Its restriction to the saturated set Ã_0 is open onto Â_0, so p × id : Ã_0 × Δ → Â_0 × Δ is a quotient map. The map (x, t) ↦ p(H̃_t x) is continuous and constant on its fibres, so Π is continuous.
6. **Continuity of Θ^{-1}, hence (2) and (3).**
   - Let (w_n, t_n) → (w, t) in Â, and z_n := Π_{t_n}^{-1}(w_n). Then ξ_G(z_n) = H_{t_n}^{-1}(ξ_G w_n) → H_t^{-1}(ξ_G w), by continuity of H^{-1}.
   - ξ_G is proper (St4), so the z_n lie in a compact set.
   - Every limit point z of (z_n) lies in the closed set Â_0 and satisfies Π_t z = w, by joint continuity. By injectivity z = Π_t^{-1} w, so z_n → Π_t^{-1}w.
   - Thus Θ is a continuous bijection with continuous inverse. Restricting to a fixed t gives (2).
7. **(4).** "⊇" follows from ξ_G Π_t = H_t ξ_G. For "⊆": if ξ_G(w) = H_t(y) with w ∈ Â_t, write w = Π_t(z). Then H_t(ξ_G z) = H_t(y), so ξ_G z = y.
8. **(5)** follows from (2) and Lemma 2.4, applied to Â_0 and Â_t; both have dimension ≤ 1 by §1.2.
9. **(6).**
   - Let F ⊂ E be the finite set (Lemma 2.1) of multi-branch points of E together with Π_t^{-1}(multi-branch points of E_t).
   - ν and ν_t are homeomorphisms over the complements of the multi-branch points (continuous, bijective, proper). So Ĥ_t := ν_t^{-1}∘Π_t∘ν is a homeomorphism Ê ∖ ν^{-1}(F) → Ê_t ∖ ν_t^{-1}(Π_t F).
   - Let ẑ ∈ ν^{-1}(F) and let D be a small closed disc around ẑ. As points of D ∖ ẑ approach ẑ, their images approach the finite set ν_t^{-1}(Π_t ν ẑ), because ν_t is proper.
   - Ĥ_t(D ∖ ẑ) is connected. For D small it therefore lies in a small neighbourhood of a single point of that finite set; define Ĥ_t(ẑ) to be that point.
   - Doing the same for Ĥ_t^{-1} gives a continuous inverse. So Ĥ_t is a homeomorphism Ê → Ê_t, and it maps ends to ends.
   - By Lemma 2.1(2), the ends are the punctures. ∎

**Remark 3.2 (where (R2^orb) enters).** Under (R2) alone, (1)–(6) are available for product-type strata, with Π_t := H_t. In non-product strata a continuous, bijective choice of lifts of H_t to ∏_w M_w is exactly what may fail: it is the "twin" problem of the original route.

---

## 4. Rigidity of transported pieces (Theorem RO) [orb]

Fix a boundary stratum G and a piece E of Â_0. Take j, Λ, u_0 : H → Ê and O_0 = H/Λ from I.2, and F_0, f_0, R(λ), S from J0 (I.3). For t ∈ Δ let E_t := Π_t(E), with ν_t : Ê_t → E_t and Ĥ_t : Ê → Ê_t from Lemma 3.1.

Throughout this section:
- H carries the Poincaré metric of curvature −4, with distance d_H. For hyperbolic γ ∈ PSL_2(ℝ), α_γ is its axis and ℓ(γ) := d_H(x, γx) for x ∈ α_γ is its translation length.
- T_j carries the Teichmüller metric d_T. For a mapping class g, τ(g) := inf_X d_T(X, gX).

**Lemma 4.1 (transported orbifold) [orb, through Lemma 3.1].** For every t ∈ Δ there are:
- a lattice Λ_t ⊂ PSL_2(ℝ) and a holomorphic map u_t : H → Ê_t inducing a biholomorphism H/Λ_t ≅ Ê_t. Its elliptic fixed points lie exactly over the points Ĥ_t(c), c a cone point of O_0, with order e_c, and its cusps correspond to the punctures of Ê_t;
- a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0;
- an isomorphism θ_t : Λ_t → Λ, θ_t(λ) := h̃_t^{-1}λh̃_t, which maps elliptic, parabolic and hyperbolic elements to elements of the same type.

For t = 0 we take Λ_0 = Λ, u_0 and h̃_0 = id.

*Proof.*
1. **The lattice Λ_t.** Let O_t be the orbifold with underlying Riemann surface Ê_t, cone points Ĥ_t(c) of order e_c, and the punctures of Ê_t as cusps.
   - Ĥ_t is a homeomorphism mapping punctures to punctures (Lemma 3.1(6)). So Ê and Ê_t have the same genus and number of punctures, and χ^orb(O_t) = χ^orb(O_0) < 0.
   - By the uniformisation theorem for hyperbolic 2-orbifolds (Unif), there is a lattice Λ_t with a holomorphic quotient map u_t : H → H/Λ_t = Ê_t, branched exactly over the cone points with the given orders, whose cusps correspond to the punctures.
2. **Lifting Ĥ_t.** Let H^♮_t := H ∖ u_t^{-1}(cone points) and O_t^♮ := Ê_t ∖ (cone points).
   - u_t : H^♮_t → O_t^♮ is a regular covering with deck group Λ_t. It corresponds to the normal subgroup N_t ⊂ π_1(O_t^♮) normally generated by the e_c-th powers of small loops around the cone points.
   - Ĥ_t maps a small disc around a cone point c onto a disc around Ĥ_t(c) containing no other cone point. So it maps a small loop around c to a loop freely homotopic to a small loop around Ĥ_t(c), or to its inverse. Hence (Ĥ_t)_* N_0 = N_t.
   - By the lifting criterion, Ĥ_t lifts to a homeomorphism H^♮_0 → H^♮_t; the same applies to Ĥ_t^{-1}.
   - Near a preimage of a cone point, u is locally z ↦ z^{e}. A homeomorphism of punctured discs commuting with z ↦ z^e extends continuously over 0.
   - So the lift extends to a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0.
3. **The isomorphism θ_t.** For λ ∈ Λ_t,
   u_0∘h̃_t^{-1}λh̃_t = Ĥ_t^{-1}∘u_t∘λ∘h̃_t = Ĥ_t^{-1}∘u_t∘h̃_t = u_0.
   - So h̃_t^{-1}λh̃_t is a deck transformation of u_0 : H^♮_0 → O_0^♮, i.e. an element of Λ.
   - θ_t is an injective homomorphism, and the symmetric argument gives its inverse.
4. **Types.**
   - θ_t preserves orders, and in a Fuchsian group the non-trivial elements of finite order are exactly the elliptic ones.
   - For an infinite-order element λ: λ is parabolic iff it stabilises a component of u^{-1}(P), where P is a punctured-disc neighbourhood of a puncture containing no cone point.
     - Such a component C covers P with infinite cyclic deck group, generated by the image of the peripheral loop, which is parabolic.
     - Conversely, a parabolic λ fixes the cusp point at which C sits, so λC = C.
     - In a Fuchsian group, an element fixing a parabolic fixed point is parabolic or trivial.
   - h̃_t maps the components of u_0^{-1}(P) onto the components of u_t^{-1}(Ĥ_t P). So θ_t preserves parabolicity, and hence also hyperbolicity. ∎

**Proposition 4.2 (transport of the joint lift) [orb: (a), (b) for g ∈ Mod_Π, and via Lemma 3.1 also (c), (d)].** Put F_t := H̃_t∘F_0∘h̃_t^{-1} : H → T_G. Then:
1. F_t is holomorphic and p∘F_t = ν_t∘u_t;
2. F_t∘λ = g∘F_t for every λ ∈ Λ_t and every g ∈ R(θ_t λ).

*Proof.*
1. **Lifting.** F_0(H) ⊂ Ã_0, since p F_0 = ν u_0 takes values in Â_0. So F_t is defined and continuous. By Lemma 3.1(1) and (6) and Lemma 4.1,
   p∘F_t = Π_t∘p∘F_0∘h̃_t^{-1} = Π_t∘ν∘u_0∘h̃_t^{-1} = Π_t∘ν∘Ĥ_t^{-1}∘u_t = ν_t∘u_t.
   ν_t∘u_t is holomorphic, so F_t is holomorphic by CL (I.3), applied with Γ = Mod_Π acting on T = T_G.
2. **Equivariance.** We have h̃_t^{-1}λ = θ_t(λ)h̃_t^{-1}. For g ∈ R(θ_tλ),
   F_t(λy) = H̃_t F_0(θ_t(λ)h̃_t^{-1}y) = H̃_t(g F_0(h̃_t^{-1}y)) = g F_t(y),
   using (b). ∎

**Lemma 4.3 (rigidity of the Teichmüller coordinate) [orb, through Prop. 4.2].** There is A_t ∈ PSL_2(ℝ) with A_tλA_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ. In particular A_tΛA_t^{-1} = Λ_t. Moreover f_t∘A_t = f_0, where f_t := pr_j∘F_t.

*Proof.* For μ ∈ Λ put R_j(μ) := pr_j(R(μ)), a set of mapping classes of the vertex j. Every g ∈ R_j(μ) satisfies g∘f_0 = f_0∘μ.

1. **Step 1.** Let μ ∈ Λ be hyperbolic and g ∈ R_j(μ). Then g is pseudo-Anosov, τ(g) = ℓ(μ), and the set Min(g) where d_T(X, gX) = τ(g) is the geodesic f_0(α_μ).
   - By J0(ii), f_0 is an isometry onto the Teichmüller disc 𝔇 = f_0(H). So g preserves 𝔇, acts on it as f_0μf_0^{-1}, and translates the Teichmüller geodesic f_0(α_μ) by ℓ(μ) > 0.
   - A mapping class preserving a Teichmüller disc and acting on it as a hyperbolic isometry is pseudo-Anosov (fact (VT)).
   - By Bers' theorem (Bers), a pseudo-Anosov g has a unique invariant Teichmüller geodesic, its axis. Min(g) is exactly the axis, and τ(g) is the translation along it. So the axis is f_0(α_μ) and τ(g) = ℓ(μ).
2. **Step 2: ℓ_t(γ) ≥ ℓ(θ_tγ) for hyperbolic γ ∈ Λ_t.** Here ℓ_t denotes translation length for Λ_t.
   - θ_tγ is hyperbolic (Lemma 4.1). Take x ∈ α_γ and g ∈ R_j(θ_tγ).
   - By Prop. 4.2(2), f_t(γx) = g f_t(x). f_t is holomorphic, so it is 1-Lipschitz by Royden's theorem (Roy). Hence
     τ(g) ≤ d_T(f_t x, g f_t x) = d_T(f_t x, f_t γx) ≤ d_H(x, γx) = ℓ_t(γ).
   - By Step 1, τ(g) = ℓ(θ_tγ).
3. **Step 3: Thurston.**
   - By Selberg's lemma (Sel), Λ has a torsion-free normal subgroup Λ′ of finite index. Put Λ′_t := θ_t^{-1}(Λ′) = h̃_tΛ′h̃_t^{-1}.
   - X := H/Λ′ and X_t := H/Λ′_t are complete hyperbolic surfaces of finite area. h̃_t descends to a homeomorphism φ : X → X_t, mapping cusps to cusps, which induces θ_t^{-1} on deck groups.
   - For every closed geodesic class of X, represented by a hyperbolic λ′ ∈ Λ′, Step 2 with γ := θ_t^{-1}(λ′) gives ℓ_{X_t}(φ(λ′)) ≥ ℓ_X(λ′). Thus ψ := φ^{-1} : X_t → X does not increase lengths of closed curves.
   - If φ reverses orientation, replace X_t by its complex conjugate. This changes no lengths.
   - By Thurston's theorem (Th), ψ is homotopic to an isometry. Lifting the homotopy equivariantly gives an isometry A_t of H with A_tλ′A_t^{-1} = θ_t^{-1}(λ′) for λ′ ∈ Λ′. The conjugation is constant along the lifted homotopy, because Λ′_t is discrete.
   - A_t is a priori possibly orientation-reversing.
4. **Extension to Λ.**
   - For λ ∈ Λ put ψ(λ) := A_t^{-1}θ_t^{-1}(λ)A_t and c := λ^{-1}ψ(λ).
   - For λ′ ∈ Λ′, normality of Λ′ gives ψ(λλ′λ^{-1}) = λλ′λ^{-1}, i.e. cλ′c^{-1} = λ′.
   - The centraliser of a lattice in Isom(H) is trivial (Cent), so c = 1. Hence A_tλA_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ.
5. **Step 4: k_t := f_t∘A_t equals f_0.**
   - For μ ∈ Λ and g ∈ R_j(μ): k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x), by Prop. 4.2(2) with λ = θ_t^{-1}(μ), since R_j(θ_tλ) = R_j(μ).
   - k_t is 1-Lipschitz (Roy). For hyperbolic μ and x ∈ α_μ,
     d_T(k_t x, g k_t x) = d_T(k_t x, k_t μx) ≤ ℓ(μ) = τ(g).
     So k_t(x) ∈ Min(g) = f_0(α_μ).
   - At a transverse intersection point x of two distinct axes α_μ, α_ν we get k_t(x) ∈ f_0(α_μ) ∩ f_0(α_ν) = {f_0(x)}, by injectivity of f_0.
   - Such points are dense in H (Dens). By continuity, k_t = f_0.
6. **Orientation.** If A_t reversed orientation, k_t would be anti-holomorphic and equal to the non-constant holomorphic f_0, which is impossible. So A_t ∈ PSL_2(ℝ). ∎

**Consequence.** A_t descends to a biholomorphism ā_t : Ê = H/Λ → H/Λ_t = Ê_t with u_t∘A_t = ā_t∘u_0.

**Theorem 4.4 (Theorem RO) [orb: everything used in Lemma 3.1, Prop. 4.2, Lemma 4.3; part (b) also uses (IS), see GAP G1].** For all t ∈ Δ:
- (a) M(E_t) = M(E);
- (b) K(E_t) = K(E).

*Proof.*
1. **Step 1 (an honest homomorphism into a torsion-free group).**
   - Fix N ≥ 3. For each w, Mod_w[N] is defined as the kernel of Mod_w → Sp(2g_w, ℤ/N) if g_w ≥ 1, and as Mod_w if g_w = 0 (repair R2′). Each Mod_w[N] is torsion-free and normal of finite index in Mod_w (fact (TF)). Put Mod[N] := ∏_w Mod_w[N].
   - S is finite, so S ∩ Mod[N] = {1}.
   - By J0(iii), λ ↦ R(λ) is a homomorphism Λ → N(S)/S. Let Λ^N be the preimage of the subgroup (N(S) ∩ Mod[N]S)/S. This is a subgroup because Mod[N] is normal in Mod_Π, and its index is at most [Mod_Π : Mod[N]] < ∞. So Λ^N has finite index in Λ.
   - By Selberg's lemma and passing to the normal core, there is a torsion-free normal subgroup Λ″ ⊂ Λ^N of finite index in Λ.
   - For μ ∈ Λ″, R(μ) ∩ Mod[N] consists of exactly one element r(μ). It is non-empty by the definition of Λ^N, and two such elements differ by an element of S ∩ Mod[N] = {1}.
   - r : Λ″ → Mod[N] is a homomorphism, because r(μ)r(ν) ∈ R(μν) ∩ Mod[N].
2. **Step 2 (normalised maps with t-independent equivariance).** Put g_t := F_t∘A_t : H → T_G, which is holomorphic. For μ ∈ Λ″, by Lemma 4.3 and Prop. 4.2(2) with r(μ) ∈ R(μ) = R(θ_t(θ_t^{-1}μ)),
   g_t(μx) = F_t(θ_t^{-1}(μ)A_t x) = r(μ) g_t(x).
   - Mod[N] acts freely and properly discontinuously on T_G (finite stabilisers in a torsion-free group are trivial). So M[N] := T_G/Mod[N] = ∏_w M_w[N] is a complex manifold, and each M_w[N] = T_w/Mod_w[N] is a K(Mod_w[N], 1), since T_w is contractible.
   - R := H/Λ″ is a Riemann surface of finite type with π_1(R) = Λ″, a finite cover of the finite-area orbifold H/Λ.
   - g_t descends to a holomorphic ḡ_t = (ḡ^w_t)_w : R → M[N]. Moreover p∘g_t = ν_t∘u_t∘A_t = ν_t∘ā_t∘u_0.
3. **Step 3 (fixed homotopy classes).**
   - The coordinate g^w_t := pr_w∘g_t is a lift of ḡ^w_t that is r_w-equivariant, with r_w := pr_w∘r.
   - So ḡ^w_t induces r_w on fundamental groups, up to conjugation (base-point changes).
   - By (KP1), free homotopy classes of maps from R into a K(π,1) correspond to homomorphisms π_1(R) → π modulo conjugation. Hence, for each w, the maps ḡ^w_t (t ∈ Δ) are all freely homotopic.
4. **Step 4 (part (a)).** We show: ḡ^w_t is constant ⟺ r_w = 1. The right-hand side does not depend on t.
   - (⇒) If ḡ^w_t is constant, then g^w_t takes values in one discrete Mod_w[N]-orbit, so it is constant (H is connected), say ≡ y. Then r_w(Λ″) ⊂ Stab(y), which is finite and hence trivial.
   - (⇐) If r_w = 1, then g^w_t descends to a holomorphic map R → T_w. T_w is biholomorphic to a bounded domain (Bers embedding, (BE)). Bounded holomorphic functions extend over the punctures of R to its compactification R̄, and are then constant. So ḡ^w_t is constant.
   - Next, pr_w∘ν_t∘ā_t∘u_0 = π_w∘g^w_t, where π_w : T_w → M_w factors through the finite-to-one map M_w[N] → M_w. Since ā_t∘u_0 is onto Ê_t and H is connected:
     pr_w is constant on E_t ⟺ ḡ^w_t is constant ⟺ r_w = 1.
   - Hence M(E_t) = {w : r_w ≠ 1} for every t, and (a) follows.
5. **Step 5 (finitely many candidates).** Put M := M(E). For u ∈ M, the maps ḡ^u_t (t ∈ Δ) are non-constant, holomorphic, and freely homotopic (Step 3).
   - By (IS) (GAP G1; for u of type (1,1) or (0,4) by (dF) instead), they lie in a finite set Φ_u independent of t.
   - pr_M(E_t) = pr_M ν_t ā_t u_0(H) is the image of R under (ρ_u∘ḡ^u_t)_{u∈M}, where ρ_u : M_u[N] → M_u.
   - Hence K(E_t) lies in a finite set 𝒦_E of curves, independent of t.
6. **Step 6 (constancy).** For K ∈ 𝒦_E put T_K := {t ∈ Δ : K(E_t) = K}.
   - **T_K is closed.** Let t_n → t* with t_n ∈ T_K. Every point of E_{t*} is Π_{t*}(z) = lim_n Π_{t_n}(z) for some z ∈ E, by joint continuity (Lemma 3.1). So pr_M(E_{t*}) ⊂ K, hence K(E_{t*}) ⊂ K.
   - By (a) and Lemma 2.1(3), K(E_{t*}) is an irreducible curve. So it equals the irreducible curve K.
   - The T_K are finitely many, pairwise disjoint, closed, and cover the connected Δ. So one of them is Δ, and by Π_0 = id it is T_{K(E)}. ∎

*Remarks.*
- Only (a) is used for the transitions in §9. (b) is used only at the endpoint, in §9.3, and only through Corollary 4.5 below.
- Part (a) does not use (IS).

**Corollary 4.5 (ends of transported pieces) [orb, (IS) through 4.4(b)].** Let z_n ∈ E_t with z_n → κ ∈ ∏_w M̄_w, and suppose some coordinate of κ lies in the boundary. Then:
- every boundary coordinate of κ is indexed by an element of M(E);
- pr_{M(E)}(κ) ∈ K(E) ∩ ∂;
- every smooth component, with its special points, of every coordinate κ_u (u ∈ M(E)) has its class in the finite, t-independent set F′(E) of Definition 2.1′.

*Proof.* Lemma 2.2 applied to the piece E_t, together with M(E_t) = M(E) and K(E_t) = K(E) from Theorem 4.4. ∎

---

## 5. Isotropy is transported; the lift of Q_t is unique [orb]

For Q ∈ B_0 put Q_t := H_t(Q). By (R2), Q_t ∈ Δ_{G_Q}.

**Proposition 5.1 (isotropy) [orb: (a), (c)].** For every Q ∈ B_0 and t ∈ Δ, |Aut(Q_t)| = |Aut(Q)|.

*Proof.*
- Let G := G_Q. Then Q ∈ A^G_0, so there is x̂ ∈ Ã_0 with ξ_G p(x̂) = Q.
- By (a), ŷ := H̃_t(x̂) satisfies ξ_G p(ŷ) = Q_t.
- By Lemma 2.5 and (c): Aut(Q_t) ≅ Stab_{Mod_G}(ŷ) = Stab_{Mod_G}(x̂) ≅ Aut(Q). ∎

**Proposition 5.2 (one fixed lift) [orb: (a), (c)].** Let J ∈ B_0, and let B′ ⋐ B be Aut(J)-invariant balls in Def(J), both small enough for (Kur). Then there is ε > 0 such that for |t| < ε:
- J_t ∈ q(B′);
- q^{-1}(J_t) ∩ B = {p(t)} is a single point, fixed by Aut(J), and p(t) ∈ B′;
- t ↦ p(t) is continuous, with p(0) = 0;
- p(t) lies in the deepest locus {s_e = 0 for all e ∈ E(G_J)}.

*Proof.*
1. **Choice of ε.** t ↦ J_t is continuous and J_0 = J ∈ q(B′), which is open. Choose ε with J_t ∈ q(B′) for |t| < ε.
2. **One point.**
   - By (Kur), q^{-1}(J_t) ∩ B is one Aut(J)-orbit Aut(J)·p. It has |Aut(J)|/|Stab_{Aut(J)}(p)| elements.
   - Again by (Kur), Stab_{Aut(J)}(p) ≅ Aut(X_p) ≅ Aut(J_t), which by Prop. 5.1 has order |Aut(J)|.
   - So the orbit is a single point p(t), fixed by Aut(J). Since q^{-1}(J_t) ∩ B′ ≠ ∅, we have p(t) ∈ B′. Also p(0) = 0, because q^{-1}(J) ∩ B = {0}.
3. **Continuity.** Let t_n → t. The p(t_n) lie in the compact set closure(B′) ⊂ B. Any limit point p* satisfies q(p*) = J_t, so p* = p(t). Hence p(t_n) → p(t).
4. **Deepest locus.** J_t ∈ Δ_{G_J}, so X_{p(t)} has |E(G_J)| nodes. By (Kur), all s_e(p(t)) vanish. ∎

*Remark 5.3.*
- Under (R2) alone, q^{-1}(J_t) ∩ B may consist of several points: the "lift-curves" permuted by Aut(J). This happens when the isotropy drops at t ≠ 0 (§8.2), and it is the source of all the twin configurations of the original route.
- Prop. 5.2 removes them. Holomorphy of p (which holds when (P) holds for some branch at J, by Lemma A.1(2) and CL) is not needed.

---

## 6. Transport of lifted branches [items 1–2 coarse; items 3–5 orb]

**Setting 6.0.** Let J ∈ B_0 and choose balls B′ ⋐ B ⊂ Def(J) as in Prop. 5.2. Let β be a branch of B_0 at J, with stratum G := G_β of β ∖ J, β̃ a lift, S := S_β̃, and ι : G_S → G an isomorphism (Lemma 1.1). We shrink the neighbourhood of J and ε > 0 so that the following hold.
- (i) β is a closed disc around J with β ∖ J ⊂ Δ_G, and H(β × Δ_ε) ⊂ q(B′) × Δ_ε. This is possible by continuity of H at (J, 0), since H(J, 0) = (J, 0).
- (ii) β ∖ J avoids the finite set ξ_G(Sing Â_0 ∪ {isolated points of Â_0}) (Lemma 2.1(1)).
- (iii) Prop. 5.2 holds on Δ_ε.
- (iv) Near J, B_0 is the union of its branches at J, and these meet only at J.

Since (i)–(iv) involve finitely many conditions, they can be imposed simultaneously for finitely many branches at finitely many points.

Define:
- N := H((β ∖ J) × Δ_ε);
- Ñ := the connected component of q^{-1}(N) ∩ (B × Δ_ε) containing (β̃ ∖ 0) × {0}, which is connected;
- Ñ_t := {p : (p, t) ∈ Ñ}.

By (Kur), q^{-1}(q(B′)) ∩ B = B′, so Ñ ⊂ B′ × Δ_ε.

Let E be the piece of Â_0 containing Π_{S,ι}(β̃ ∖ 0). It exists and is unique: Π_{S,ι}(β̃ ∖ 0) is a connected subset of ξ_G^{-1}(β ∖ J), which by (ii) lies in the 1-manifold of regular 1-dimensional points of Â_0, and each component of that manifold lies in a single piece.

**Lemma 6.1 (transported lifts).** In Setting 6.0:
1. [coarse: (R1), (R2)] q(Ñ) = N. In particular Ñ_t ≠ ∅ and q(Ñ_t) = H_t(β ∖ J) for every t ∈ Δ_ε.
2. [coarse: (R2)] Every (p, t) ∈ Ñ has pattern S(p) = S.
3. [orb: through Lemma 3.1] Π_{S,ι}(Ñ_t) ⊂ E_t = Π_t(E) for every t ∈ Δ_ε.
4. [orb: through Prop. 5.2] For every t ∈ Δ_ε there are points (p_n, t) ∈ Ñ with p_n → p(t). For every such sequence, Π_{S,ι}(p_n) → κ̂(t) := Π_{S,ι}(p(t)) ∈ ∏_w M̄_w.
5. If (P) holds for β, then κ̂(t) has a coordinate in the boundary.

*Proof.*
1. **q(Ñ) = N.**
   - N is homeomorphic to (β ∖ J) × Δ_ε, hence connected.
   - N is open in ℬ_G := closure(𝒱) ∩ (Δ_G × Δ_ε). Indeed, H is a homeomorphism (A^G_0 × Δ_ε) → ℬ_G by (R2), and β ∖ J is open in A^G_0 by (iv).
   - q^{-1}(ℬ_G) ∩ (B × Δ_ε) is an analytic subset of the locally closed analytic set q^{-1}(Δ_G) × Δ_ε, hence locally connected. Its open subset q^{-1}(N) is locally connected too, so its components are open.
   - Aut(J) permutes these components. The union of the translates of Ñ is open, closed and Aut(J)-invariant in q^{-1}(N).
   - q restricted to the saturated set q^{-1}(N) is an open and closed map onto N, being a quotient by a finite group. So q(Ñ) = q(Aut(J)·Ñ) is non-empty, open and closed in N, hence equal to N.
2. **Pattern.** For (p, t) ∈ Ñ we have q(p) ∈ H_t(β ∖ J) ⊂ Δ_G, by (R2). By Lemma 1.1, S(p) is locally constant on Ñ, which is connected. At t = 0 it equals S on β̃ ∖ 0.
3. **Π_{S,ι}(Ñ_t) ⊂ E_t.**
   - By (2) and (PN1), ξ_G(Π_{S,ι}(p)) = q(p) ∈ H_t(β ∖ J) for (p, t) ∈ Ñ. By Lemma 3.1(4), Π_{S,ι}(p) ∈ Π_t(ξ_G^{-1}(β ∖ J)).
   - So Ψ : Ñ → ∏_w M_w × Δ_ε, (p, t) ↦ (Π_{S,ι}(p), t), maps the connected set Ñ into Θ(ξ_G^{-1}(β ∖ J) × Δ_ε) (Θ as in Lemma 3.1(3)).
   - ξ_G^{-1}(β ∖ J) is an open subset of the analytic set Â_0, hence locally connected. Let γ̂ be its connected component containing the connected set Π_{S,ι}(β̃ ∖ 0). Then γ̂ is open and closed in ξ_G^{-1}(β ∖ J).
   - By (ii), γ̂ is a connected subset of the regular 1-dimensional locus of Â_0, so it lies in a single piece, namely E.
   - Since Θ is a homeomorphism, Θ(γ̂ × Δ_ε) is open and closed in Θ(ξ_G^{-1}(β ∖ J) × Δ_ε). It meets Ψ(Ñ), because Θ(γ̂ × {0}) = γ̂ × {0} ⊃ Ψ((β̃ ∖ 0) × {0}), using Π_0 = id.
   - Hence Ψ(Ñ) ⊂ Θ(γ̂ × Δ_ε). That is, Π_{S,ι}(Ñ_t) ⊂ Π_t(γ̂) ⊂ Π_t(E) = E_t.
4. **Convergence to p(t).**
   - Fix t. Take y_n ∈ β ∖ J with y_n → J. By (1) there are (p_n, t) ∈ Ñ with q(p_n) = H_t(y_n) → H_t(J) = J_t.
   - Let (p_n, t) ∈ Ñ be any sequence with q(p_n) → J_t. The p_n lie in the compact set closure(B′) ⊂ B, and every limit point p* satisfies q(p*) = J_t, so p* = p(t) by Prop. 5.2. Hence p_n → p(t).
   - In particular the sequence just constructed converges to p(t), which proves the existence claim.
   - The p_n lie in L_S ∩ B by (2), p(t) lies in the deepest locus ⊂ L_S, and Π_{S,ι} is continuous on L_S ∩ B. Hence Π_{S,ι}(p_n) → Π_{S,ι}(p(t)).
5. **A boundary coordinate under (P).**
   - If S = E(G_J), then G_β ≅ G_S = G_J and J ∈ Δ_{G_β}, contrary to (P). So there is an edge e ∈ E(G_J) ∖ S.
   - e is contracted into a vertex w of G_S. By (PN2), the ι(w)-coordinate of κ̂(t) is glued along the node e, so it is nodal, i.e. lies in ∂M̄_{ι(w)}. ∎

**Proposition 6.2 (value of a constant label at the fixed lift) [orb: Lemma 6.1(3),(4) and Theorem 4.4(a)].** In Setting 6.0, assume (β̃, x) is labelled by (E, c) with c ∉ M(E) (Definition 1.2, with the ι of the setting). Then for |t| < ε:
- c ∉ M(E_t);
- comp_x(p(t)) = ι^*(φ_c(E_t)), where φ_c(E_t) is the constant value of pr_c on E_t;
- in particular [comp_x(p(t))] = [φ_c(E_t)].

*Proof.*
- By Theorem 4.4(a), c ∉ M(E_t).
- Take (p_n, t) ∈ Ñ with p_n → p(t) (Lemma 6.1(4)). By Definition 1.2, (PN3) and Lemma 6.1(2),(3):
  comp_x(p_n) = ι^*(pr_c Π_{S,ι}(p_n)) = ι^*(φ_c(E_t)).
- comp_x is continuous on L_x ∩ B ⊃ L_S ∩ B, and p(t) ∈ L_S. So comp_x(p(t)) = ι^*(φ_c(E_t)). ∎

**Proposition 6.3 (merge or move at a puncture lands in a finite set) [orb, with (IS) through Cor. 4.5].** In Setting 6.0, assume (P) for β. Let x ∈ V(G_J) satisfy one of:
- (MERGE) x is not intact for S;
- (MOV) x is intact for S and [comp_x] is non-constant along β̃.

Then [comp_x(p(t))] ∈ F′(E) for all |t| < ε.

*Proof.*
- By Lemma 6.1(4),(5), κ̂(t) is a limit of points Π_{S,ι}(p_n) ∈ E_t and has a boundary coordinate. By Corollary 4.5, pr_M(κ̂(t)) ∈ K(E) ∩ ∂, with M := M(E).
- Let [x] be the vertex of G_S containing x and u := ι([x]). By (PN2), κ̂(t)_u is the stable curve glued from the comp_y(p(t)), y ∈ [x]. So comp_x(p(t)), with the half-edges at x as special points, is one of its smooth components with its special points.
- **u ∈ M.**
  - (MERGE): some edge at x lies in E(G_J) ∖ S and is contracted into [x]. So κ̂(t)_u is nodal, and u ∈ M by Corollary 4.5.
  - (MOV): [x] = {x}. By (PN3), pr_u∘Π_{S,ι} = (ι^{-1})^* comp_x is non-constant on β̃ ∖ 0, whose image lies in E. So u ∈ M(E).
- By Corollary 4.5, [comp_x(p(t))] ∈ F′(E). ∎

**Remark 6.4 (robustness of the labelling under Aut(G)) [orb: (b)].** Suppose Part I supplies the labelled identification of I.5 only up to relabelling by Aut(G). That is, (β̃, x) is labelled by (σE, σ(c)) for some σ ∈ Aut(G), instead of by (E, c). Then the conclusions of §9 are unchanged.
- Choose g ∈ Mod_G lifting σ (St3). By (b), H̃_t∘g = g∘H̃_t, which descends to Π_t∘σ = σ∘Π_t on Â_0.
- Hence (σE)_t = σ(E_t), and σ(c) is constant on (σE)_t with value the relabelling of φ_c(E_t).
- So [φ_{σ(c)}((σE)_t)] = [φ_c(E_t)].

---

## 7. The local reading (Loc) implies (R2^orb) (Theorem LG)

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

**Remark 7.3 ((O-emb) ⇒ (Loc); repair Rep-5).** Under (O-emb), at x̂ ∈ Ã_0 and t_0 there are:
- a slice neighbourhood W of x̂;
- injective continuous local lifts h_s : W ∩ Ã_0 → T_G of H_s (s ∈ I);
- an isomorphism φ : Stab(x̂) → Stab(h_{t_0}x̂), **independent of s by the reading**, with h_s(au) = φ(a)h_s(u).

Shrinking W and I, we may assume h((W ∩ Ã_0) × I) ⊂ W′, a slice neighbourhood of h_{t_0}x̂. Then Stab(h_s u) = φ(Stab u) for all s:
- If b ∈ Mod_G fixes h_s(u) ∈ W′, then b ∈ Stab(h_{t_0}x̂), so b = φ(a) with a ∈ Stab(x̂). Then h_s(au) = h_s(u), and au ∈ W, so au = u by injectivity.
- Conversely, if au = u with u ∈ W, then a ∈ Stab(x̂), and φ(a)h_s(u) = h_s(u).

This gives (L2); (L1) is the lifting property.

The independence of φ from s cannot be *deduced* from equivariance: equivariance determines φ_s(a) only modulo the pointwise stabiliser of h_s(W ∩ Ã_0), which may be non-trivial on the 1-dimensional set Ã_0. So it is part of the reading (O-emb).

**Remark 7.4 ((Loc) only near t_0 = 0; repair Rep-4).**
- The radius of the disc I given by (Loc) at (x̂, 0) may depend on x̂, and Ã_0 is not compact modulo Mod_G. So (Loc) at t_0 = 0 alone does **not** give (a)–(d) on any Ã_0 × Δ_r, and is not known to suffice. This is open.
- If (Loc) holds at all (x̂, t_0) with |t_0| < r for a fixed r > 0, then:
  - Theorem 7.2 gives (a)–(d) over Δ_r;
  - the rescaled family t ↦ V_{rt} satisfies (R1) and (R2^orb) over Δ;
  - Theorem A then gives Y_t = Y_0 for |t| < r, and Lemma 2.3 extends this to Δ.

---

## 8. Discussion: what (R2^orb) buys, and the coarse reading

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
| Theorem 4.4(b), Cor. 4.5 | via 4.4(a) | **(IS) — GAP G1**; (dF) for (1,1), (0,4) |
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

Both obstructions are exactly the isotropy drop of §8.2. The coarse-valid lemmas of the original route, which reduce the coarse problem to "(Rig) + MS11♭", are proved in Appendix A.

---

## Appendix A. Coarse-valid lemmas of the original route (not used in the proof of Theorem A)

These are proved under the weakest hypotheses their proofs allow. Labels:
- [coarse] = (R1), (R2);
- [coarse+P] = in addition (P) for the branch considered;
- [coarse+Rig] = in addition (Rig);
- [+Ync] = in addition "t ↦ [Y_t] is non-constant".

**(Rig)** means: there is a finite set 𝒦 of triples (G, M, K) — G a boundary stratum, M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible curve — such that every piece E at every time t, in every stratum, has (G, M(E), K(E)) ∈ 𝒦 up to relabelling by Aut(G). Under (R2^orb), (Rig) holds by Theorem 4.4, with 𝒦 := {(G, M(E), K(E)) : E a piece at time 0}.

**Setting A.0.**
- J ∈ B_0, b a branch at J with lift b̃, Ñ := Ñ_b̃ as in Setting 6.0. Only items (i), (ii) and (iv) of Setting 6.0 are used; item (iii) (Prop. 5.2) is not.
- Γ_J := {(J_t, t) : |t| < ε}.
- 𝒥 := {(p, t) ∈ B × Δ_ε : q(p) = J_t}, the lift locus. A **lift-curve** is an irreducible component of the germ of 𝒥 at (0,0).
- An **anchored sheet** (= b̃-sheet) is an irreducible component T of closure(Ñ) (closure in B × Δ_ε) with b̃ × {0} ⊂ T.
- For a vertex y of G_J and an analytic set T ⊂ B × Δ_ε, put A_y(T) := {(p, t) ∈ T : p ∈ L_y, [comp_y(p)] = [Y_t]}. Then:
  - y is **Y-persistent on T** (y ∈ P(T)) if A_y(T) = T;
  - for a lift-curve L, C(L) := {y : A_y(L) = L}.
- Ω denotes a small open neighbourhood of (J, 0) in M̄_g × Δ_ε with Ω ∩ ℬ ⊂ H((B_0 ∩ U) × Δ_ε), where U is as in Setting 6.0(iv). It exists by continuity of H^{-1} at (J, 0).

**Fact (Cl′) [none].** Let X be an analytic set, Z ⊂ X a closed analytic subset, and C a union of connected components of X ∖ Z. Then closure(C) is the union of those irreducible components X_l of X, not contained in Z, for which X_l ∖ Z ⊂ C. In particular closure(C) is analytic.

*Proof.*
- For X_l ⊄ Z, the set X_l° := X_l ∖ (Z ∪ Sing X ∪ ⋃_{l′≠l} X_{l′}) is connected and dense in X_l. (Fact (Reg): the regular locus of an irreducible analytic set is a connected manifold, and a proper analytic subset does not disconnect it.)
- X_l ∖ Z lies between X_l° and its closure, so it is connected. Hence each X_l ∖ Z lies in a single component of X ∖ Z.
- X ∖ Z = ⋃_l (X_l ∖ Z), so C is the union of the X_l ∖ Z that it contains. Their closures are the X_l. ∎

**Fact (TrQ) [none].** Let a finite group A act on a complex manifold germ, with quotient map π, and let X be an irreducible germ in the quotient. Then A permutes the irreducible components of π^{-1}(X) transitively.

*Proof.* Let Y be one component. A·Y is analytic and A-invariant. π(A·Y) is analytic (Remmert), of dimension dim X and contained in X, hence equal to X. So π^{-1}(X) = π^{-1}(π(A·Y)) = A·Y. ∎

**Lemma A.1 (transport families) [coarse+P].** Assume (P) for b. Then, inside Ω:
1. H(b × Δ_ε) = N ⊔ Γ_J is a closed analytic set of pure dimension 2. It is irreducible after shrinking Ω.
2. Γ_J is a closed analytic curve, and t ↦ J_t is holomorphic on Δ_ε. 𝒥 is a closed analytic subset of B × Δ_ε, of dimension ≤ 1, with 𝒥 ∩ {t = 0} = {(0,0)}.
3. closure(Ñ) is analytic of pure dimension 2, and closure(Ñ) ⊂ Ñ ∪ 𝒥.

*Proof.*
1. **Analyticity and dimension.**
   - Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ_ε), which is analytic by (R1). Let 𝒵 ⊂ 𝒜 be its closed analytic part over closure(Δ_{G_b}) ∖ Δ_{G_b}.
   - In Ω, 𝒜 ∖ 𝒵 = ⊔_k N_k, where N_k := H((b_k ∖ J) × Δ_ε) and b_k runs over the branches at J with b_k ∖ J ⊂ Δ_{G_b}. (J ∉ Δ_{G_b} by (P).)
   - Each N_k is open in 𝒜 ∖ 𝒵, because H is a homeomorphism. So N = N_1 is open and closed there.
   - By (Cl′), closure(N) ∩ Ω is a union of irreducible components of 𝒜 ∩ Ω. Each contains a non-empty open subset of the topological 4-manifold N, so each has dimension 2.
   - Since b × Δ_ε is closed and H is a homeomorphism onto the closed set closure(𝒱), closure(N) ∩ Ω = H(b × Δ_ε) ∩ Ω = (N ∪ Γ_J) ∩ Ω.
   - **Irreducibility.** N ∖ Sing(closure N) is connected, since Sing has real dimension ≤ 2 in the 4-manifold N (Hurewicz–Wallman, (HW)). So it lies in the regular part of a single component, and is dense.
2. **Γ_J.**
   - N ⊂ Δ_{G_b} × Δ, and Δ_{G_b} ∩ closure(Δ_{G_J}) = ∅, because G_b is a proper contraction of G_J.
   - So Γ_J = closure(N) ∩ (closure(Δ_{G_J}) × Δ_ε) ∩ Ω is analytic. The projection t : Γ_J → Δ_ε is a homeomorphism, and as in Lemma 2.3(4), t ↦ J_t is holomorphic.
   - 𝒥 = (q × id)^{-1}(Γ_J) is analytic and finite over Γ_J, so dim 𝒥 ≤ 1. Also 𝒥 ∩ {t = 0} = q^{-1}(J) × {0} = {(0,0)}.
3. **closure(Ñ).**
   - q is open, so closure(q^{-1}(N)) = q^{-1}(closure N) = q^{-1}(N) ∪ 𝒥.
   - Ñ is a component of the locally connected space q^{-1}(N) (proof of Lemma 6.1(1)), so it is open and closed there. Hence closure(Ñ) ⊂ Ñ ∪ 𝒥.
   - Apply (Cl′) with X := q^{-1}(closure N), Z := 𝒥 and C := Ñ: closure(Ñ) is a union of components X_l of X.
   - **Pure dimension 2.** For each such X_l, the set X_l ∖ (𝒥 ∪ other components) is open in Ñ. Its image under the open map q|_{q^{-1}(N)} is open in the 4-manifold N. So dim q(X_l) = 2, hence dim X_l = 2. ∎

**Lemma A.2 (Lemma B1♭) [coarse+P].** Assume (P) for b, and let T be an irreducible component of closure(Ñ).
- (a′) q(T) = H(b × Δ_ε) ∩ Ω, (0,0) ∈ T, and t is non-constant on T. Moreover T ∩ {t = 0} is a union of lifts a b̃ (a ∈ Aut(J)), each satisfying (a b̃ ∖ 0) × {0} ⊂ Ñ and aS_b̃ = S_b̃.
- (a″) Anchored sheets exist. For every p̃ ∈ b̃ ∖ 0, every irreducible component of the germ of closure(Ñ) at (p̃, 0) lies in an anchored sheet, and every anchored sheet contains such a germ component.
- (b′) The pointwise stabiliser Stab_pt(b̃) := {a ∈ Aut(J) : a|_b̃ = id} permutes the anchored sheets transitively.

*Proof.*
1. **(a′).**
   - q is finite on B × Δ_ε, so q(T) is an irreducible 2-dimensional analytic subset (Remmert) of the irreducible H(b × Δ_ε) (Lemma A.1(1)), hence equal to it.
   - (J, 0) ∈ q(T) and q^{-1}(J) = {0}, so (0,0) ∈ T.
   - If t were constant on T, T would lie in closure(Ñ) ∩ {t = 0} ⊂ q^{-1}(b) × {0}, which has dimension 1. So t is non-constant on T, and by Krull, T ∩ {t = 0} is of pure dimension 1 at each of its points.
   - T ∩ {t = 0} ⊂ q^{-1}(b) ∩ B = ⋃_a a b̃, and each a b̃ ∩ B is irreducible. So T ∩ {t = 0} is a union of some of the a b̃.
   - Since 𝒥 ∩ {t = 0} = {(0,0)} and T ⊂ Ñ ∪ 𝒥, we get (a b̃ ∖ 0) × {0} ⊂ Ñ. The pattern is constant (= S_b̃) on Ñ (Lemma 6.1(2)), and equals aS_b̃ on a b̃ ∖ 0. So aS_b̃ = S_b̃.
2. **(a″).**
   - b̃ × {0} ⊂ closure(Ñ) is an irreducible curve, so it lies in a component: an anchored sheet exists.
   - A germ component at (p̃, 0) of closure(Ñ) lies in exactly one global component T, because two distinct components meet in dimension ≤ 1. By (a′), T ∩ {t = 0} is a union of lifts containing p̃. For B small, distinct lifts meet only at 0, so this union contains b̃, and T is anchored.
   - Conversely, an anchored sheet contains (p̃, 0), so its germ there contains a germ component.
3. **(b′).**
   - Choose p̃ ∈ b̃ ∖ 0 with Stab_{Aut(J)}(p̃) = Stab_pt(b̃). This excludes, for each a ∉ Stab_pt(b̃), the discrete set of its fixed points on b̃.
   - Near p̃, q is the quotient by Stab(p̃) (Kur). Near (q(p̃), 0), the set H(b × Δ_ε) is the topological 4-manifold N. Its germ is irreducible: otherwise removing the ≤ 1-dimensional intersection of two components would disconnect a punctured neighbourhood, contradicting (HW).
   - By (TrQ), Stab(p̃) permutes the germ components of closure(Ñ) at (p̃, 0) transitively. Near (p̃, 0), closure(Ñ) coincides with q^{-1}(N).
   - Every a ∈ Stab_pt(b̃) maps Ñ to the component of q^{-1}(N) containing a(b̃ ∖ 0) = b̃ ∖ 0, i.e. to Ñ. So it maps anchored sheets to anchored sheets.
   - If T and T′ are anchored sheets with germ components g ⊂ T and g′ ⊂ T′ at (p̃, 0), choose a with ag = g′. Then aT ⊃ g′, so aT = T′. ∎

**Lemma A.3 (Lemma 4.1: anchored sheets contain a lift-curve) [coarse+P].** Assume (P) for b. Then every anchored sheet T contains a lift-curve.

*Proof.*
1. **Points of T away from 𝒥 and {t = 0}.** T is of pure dimension 2 at (0,0), and T ∩ (𝒥 ∪ {t = 0}) has dimension ≤ 1. So there are (p_n, t_n) ∈ T ∖ (𝒥 ∪ {t = 0}) converging to (0,0).
   - By Lemma A.1(3), (p_n, t_n) ∈ Ñ, so q(p_n) ∈ H_{t_n}(b ∖ J).
   - Put z_n := H_{t_n}^{-1}(q(p_n)) ∈ b ∖ J. Then z_n → J by continuity of H^{-1}.
2. **Arcs.** Parametrise b by a closed disc centred at J, and let α_n be the radial segment from z_n to J.
   - By uniform continuity of H on b × closure(Δ_{ε′}), H_{t_n}(α_n) → {J}.
   - So for large n, H_{t_n}(α_n) ⊂ q(B″), where B″ ⋐ B is a smaller invariant ball with p_n ∈ B″.
3. **The image of a component reaches J_{t_n}.**
   - Let C be an irreducible component through p_n of the analytic curve T_{t_n} ∩ B″ (pure 1-dimensional by Krull). Then q(C) is an irreducible analytic curve, closed in q(B″) (Remmert, q|_{B″} proper).
   - q(C) lies in Z := H_{t_n}(b) ∩ q(B″), which is analytic (the t_n-slice of Lemma A.1(1)). Indeed q(T_{t_n}) ⊂ H_{t_n}(b ∖ J) ∪ {J_{t_n}}, since T ⊂ Ñ ∪ 𝒥.
   - At each w ∈ H_{t_n}(α_n ∖ J), Z is homeomorphic to a disc near w, hence locally irreducible.
   - Let O be the set of such w near which q(C) contains a neighbourhood of w in Z.
     - O ∋ q(p_n): the 1-dimensional germ of q(C) at q(p_n) lies in the irreducible germ of Z there, hence equals it.
     - O is open in the arc.
     - O is closed in the arc: a limit point w lies in the closed set q(C), and the same germ argument applies.
   - So O is the whole connected arc. Since J_{t_n} lies in its closure and q(C) is closed in q(B″), J_{t_n} ∈ q(C).
4. **Conclusion.**
   - There is p′_n ∈ C with q(p′_n) = J_{t_n}, i.e. (p′_n, t_n) ∈ T ∩ 𝒥. By properness and q^{-1}(J) = {0}, p′_n → 0.
   - So (0,0) is not isolated in the analytic set T ∩ 𝒥, and this set contains an irreducible curve germ at (0,0).
   - That germ is a component of the germ of 𝒥, since dim 𝒥 ≤ 1. ∎

*Complement to Lemma A.2(b′).* The claim "near (p̃, 0), closure(Ñ) coincides with q^{-1}(N)" holds for the following reasons.
- 𝒥 is closed and meets {t = 0} only at (0,0).
- By the local conic structure of analytic sets, every point of q^{-1}(N) close to (p̃, 0) is joined to (p̃, 0) ∈ Ñ inside q^{-1}(N). Hence it lies in Ñ.

**Global objects for the remaining lemmas.**
- ℬ := closure(𝒱) ∩ (∂M̄_g × Δ). It is analytic by (R1) and equals H(B_0 × Δ) by (R2). It has dimension ≤ 2.
- For a stratum G, ℬ_G := ℬ ∩ (Δ_G × Δ).
- A **coarse piece** is a 1-dimensional irreducible component D of B_0 ∩ Δ_G, for some G; we put D_t := H_t(D). By the argument of Lemma 2.1, applied in M̄_g, the analytic set B_0 is algebraic, has finitely many coarse pieces, and has a finite singular set.

**Lemma A.4 (Lemma T: transport respects components) [coarse].** Let D be a coarse piece in Δ_G.
- (a) There is a unique irreducible component κ(D) of ℬ_G with H(D × Δ) ⊂ κ(D).
- (b) Every irreducible component 𝒲 of ℬ_G satisfies 𝒲 = ⋃_{κ(D)=𝒲} H(D × Δ).

*Proof.*
1. Let D° be D minus the finitely many singular points of B_0 ∩ Δ_G. D° is connected, being the image of the connected normalisation of D minus a finite set, and it is a real 2-manifold. So D° × Δ is a connected 4-manifold.
2. Σ := Sing(ℬ_G) has covering dimension ≤ 2, and so does H^{-1}(Σ) ∩ (D° × Δ).
3. By (HW), R := (D° × Δ) ∖ H^{-1}(Σ) is connected. H(R) is a connected subset of Reg(ℬ_G), so it lies in one component κ(D).
4. R is dense in D × Δ, and κ(D) is closed. So H(D × Δ) ⊂ κ(D). Uniqueness: H(R) ⊄ Σ.
5. For (b), let x ∈ 𝒲 lie on no other component. Then x = H(e, t) with e in some coarse piece D′, or e an isolated point of B_0 ∩ Δ_G.
   - In the second case, H({e} × Δ) is a curve of real dimension 2. The points of 𝒲 on no other component form a set of real dimension 4, so the first case occurs on a dense subset.
   - By (a), κ(D′) = 𝒲. So a dense subset of 𝒲 lies in the set ⋃_{κ(D′)=𝒲} H(D′ × Δ), which is closed because it is a finite union of images of closed sets under the homeomorphism H. ∎

**Lemma A.5 (fibres of the lifted families) [coarse].** For a boundary stratum G, let 𝓦_G be the union of those irreducible components of (ξ̄_G × id)^{-1}(closure(𝒱) ∩ (closure(Δ_G) × Δ)) ⊂ ∏_w M̄_w × Δ that are not contained in the preimage of the deeper strata. Then:
- 𝓦_G is closed analytic and proper over Δ;
- 𝓦_G ∩ (∏_w M_w × Δ) = Â;
- for every 2-dimensional irreducible component W of 𝓦_G and every t ∈ Δ, the fibre W_t is non-empty and of pure dimension 1, and each irreducible component of W_t is the closure in ∏_w M̄_w of a piece at time t.

*Proof.*
1. **Closedness, properness, and the open part.** By (Cl′), 𝓦_G = closure(Â), and Â is closed in ∏_w M_w × Δ. Properness follows from compactness of ∏_w M̄_w.
2. **The deeper part of each fibre is finite.**
   - (ξ̄_G × id)(𝓦_G) ⊂ closure(ℬ_G) = H(closure(A_0) × Δ), using that H is a closed embedding.
   - closure(A_0) ∖ A_0 is finite: it consists of the finitely many points added to the closures of the finitely many curves of A_0 (Lemma 2.1).
   - So the part of W_t over deeper strata is finite, since ξ̄_G is finite.
3. **Fibres.** dim W_t ≤ 1, so t is non-constant on W. t|_W is proper, so its image is a closed analytic subset of Δ of dimension 1, i.e. Δ. By Krull, each W_t is of pure dimension 1.
4. **Components.** Let D be a component of W_t. Then D ∩ ∏_w M_w is D minus a finite set, hence an irreducible curve in Â_t. It lies in a piece E, and since it is closed and 1-dimensional, it equals E. So D = closure(E). ∎

**Lemma A.6 (Lemma U; contains Lemma S) [coarse+Rig].** Let W be a 2-dimensional irreducible component of some 𝓦_G. Then there are M_W ⊂ V(G) and an irreducible curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, such that for every t and every component D = closure(E) of W_t:
- M(E) = M_W and K(E) = K_W;
- every u ∉ M_W is constant on E;
- D = K_W × {c_D} for some c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*
1. **Step 1 (generic moving set).**
   - Let n : W^ν → W be the normalisation, a normal surface. Let W^ν →^a T →^{b′} Δ be the Stein factorisation (SF) of t∘n, which is proper. Then T is a normal curve, hence smooth, and b′ is finite.
   - The critical values of a are discrete. Critical curves of a on Reg W^ν are contracted by a, and Sing W^ν is discrete (normal surfaces have isolated singularities).
   - So for τ outside a discrete set, a^{-1}(τ) is a smooth compact connected curve, hence irreducible.
   - For every t, W_t = ⋃_{τ ∈ b′^{-1}(t)} n(a^{-1}(τ)). For t outside a discrete set the components of W_t are exactly the curves n(a^{-1}(τ)).
   - For a vertex u let Φ_u := (pr_u∘n, a) and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert (CR).
     - If R_u = W^ν, then pr_u is constant on every component of every fibre of a, hence on every component of every W_t.
     - Otherwise dim R_u ≤ 1. Fibre components on which pr_u is constant lie in R_u, so this happens only for τ in a discrete set.
   - Put M_W := {u : R_u ≠ W^ν}. There is a discrete Z_W ⊂ Δ such that for t ∉ Z_W every component of W_t has moving set exactly M_W. For every t, every u ∉ M_W is constant on every component.
2. **Step 2 (one curve; uses (Rig)).**
   - Σ := (pr_{M_W}, t)(W) is closed, analytic and irreducible (Remmert), and has dimension 2.
   - For t ∉ Z_W, Σ_t is the union of the curves K(E), and by (Rig) these lie in the finite list K_1, …, K_N (relabellings included). So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
   - Σ is irreducible of dimension 2, so Σ = K_j × Δ for one j. Put K_W := K_j.
   - Each pr_u (u ∈ M_W) is non-constant on K_W.
3. **Step 3 (all times).** Let D = closure(E) be a component of W_t.
   - The u ∉ M_W are constant on D.
   - pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, and it is not a point (else D would be a point). So pr_{M_W}(D) = K_W.
   - Hence M(E) = M_W, K(E) = K_W, and D = K_W × {c_D}, with c_D ∈ ∏ M_u since the constant values on E lie in M_u. ∎

*Lemma S, parts (b) and (c), as consequences.*
- For u ∉ M_W, (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the finite set of values of u on the components of W_t.
- If, for a vertex x ∉ M_W, the analytic set {[pr_x] = [Y_t]} ⊂ W has real dimension 4, then it is all of W.

**Lemma A.7 (the Y-locus is analytic) [coarse].** Ŷ := {(Q, t) ∈ M̄_g × Δ : Q has a smooth component which, with its special points, has class [Y_t]} is a closed analytic subset of M̄_g × Δ.

*Proof.*
- For a stable graph G and a vertex v of type (g_i, n_i), put A_{G,v} := {(z, t) ∈ ∏_w M̄_w × Δ : [z_v] = [Y_t]}. This is the preimage of the graph of the holomorphic map t ↦ [Y_t] (Lemma 2.3), so it is closed analytic. It forces z_v ∈ M_v.
- (ξ̄_G × id)(A_{G,v}) is closed analytic, since ξ̄_G is finite (Remmert).
- Ŷ is the finite union of these images.
  - ⊆: take G := G_Q and z the normalised components of Q.
  - ⊇: the smooth factor z_v is an irreducible component of ξ̄_G(z), and its special points there are its n_v marked points. ∎

**Lemma A.8 (dichotomy for coarse pieces) [coarse].** Let D be a coarse piece. Exactly one of the following holds.
- (N) For every t, every point of H_t(closure D) has a component of class [Y_t].
- (F) There is a countable Z_D ⊂ Δ such that, for t ∉ Z_D, only finitely many points of H_t(closure D) have such a component.

*Proof.*
1. Let D° be D minus the finitely many singular points of B_0. D° is connected and open in B_0. So M_D := H(D° × Δ) is open in ℬ and is a connected 4-manifold.
2. By (HW), M_D ∖ Sing(ℬ) is connected. So M_D lies in one irreducible component W of ℬ.
3. 𝓝 := Ŷ ∩ ℬ is analytic (Lemma A.7).
4. If W ⊂ 𝓝, then (N) holds, because 𝓝 is closed and H_t(closure D) = closure(H_t D°).
5. Otherwise dim(W ∩ 𝓝) ≤ 1. Its components form a countable, locally finite family. Let Z_D be the set of t such that some component lies in the fibre over t.
   - For t ∉ Z_D, (W ∩ 𝓝)_t is discrete and compact, hence finite.
   - Together with the finite set H_t(closure D ∖ D°), this gives (F).
6. (N) and (F) exclude each other, since H_t(closure D) is infinite. ∎

Let 𝒩 be the set of coarse pieces with (N).

**Theorem A.9 (Theorem N) [coarse+Rig+Ync].** Define:
- 𝒫 := ⋃_{(G,M,K)∈𝒦} (K ∩ ∂), over all relabellings, which is finite;
- F′_𝒦 := the set of classes of the smooth components, with special points, of the coordinates of points of 𝒫;
- Z := ⋃_{D∉𝒩} Z_D ∪ {t : [Y_t] ∈ F′_𝒦}, which is countable (the second set is discrete, because [Y] is holomorphic and non-constant).

Let t ∉ Z, Q ∈ B_t, and let y be a vertex of G_Q with [comp_y(0)] = [Y_t] in a chart Def(Q). Let b be a branch of B_t at Q, with lift b̃ and pattern S. Then y is intact for S, and exactly one of the following holds.
- **(STAY)** comp_y is constant along b̃, and the coarse piece D′ with H_t^{-1}(b ∖ Q) ⊂ D′ lies in 𝒩.
- **(IMOV)** S = E(G_Q), and [comp_y] is non-constant along b̃.

*Proof.*
1. **Setting up.** Choose ι : G_S → G_b. Shrinking b̃, the set Π_{S,ι}(b̃ ∖ 0) lies in a single piece E at time t (Lemma 2.1 at time t). Put κ := Π_{S,ι}(0), which is the limit of Π_{S,ι} along b̃ (PN). Let u := ι([y]).
2. **Merge is impossible.** Suppose an edge at y is not in S.
   - By (PN2), κ_u is nodal, so by Lemma 2.2, u ∈ M(E) and pr_{M(E)}κ ∈ K(E) ∩ ∂ ⊂ 𝒫.
   - comp_y(0), with its special points, is a component of κ_u. So [Y_t] ∈ F′_𝒦, contradicting t ∉ Z.
3. **Puncture-move is impossible.** Suppose y is intact, S ≠ E(G_Q), and [comp_y] is non-constant along b̃.
   - Then u = {y} ∈ M(E).
   - κ has a nodal coordinate, coming from an edge outside S. So pr_{M(E)}κ ∈ 𝒫 and κ_u = comp_y(0). Again [Y_t] ∈ F′_𝒦, a contradiction.
4. **The constant case.** If y is intact and comp_y is constant along b̃, then every point of b near Q has a component of class [Y_t].
   - Since b ∖ Q ⊂ H_t(D′), H_t(closure D′) has infinitely many such points. As t ∉ Z_{D′}, Lemma A.8 gives D′ ∈ 𝒩.
5. **Otherwise** y is intact, comp_y is non-constant, and S = E(G_Q): this is (IMOV). ∎

**Lemma A.10 (Lemma 4.2: persistence is read off a lift-curve) [coarse+Rig+Ync+P].** In Setting A.0 with (P) for b, let T be an anchored sheet and L ⊂ T a lift-curve. Then P(T) = C(L).

*Proof.*
1. **⊆.** Immediate, since L ⊂ T.
2. **⊇: curves in slices.** Let y ∈ C(L). t is non-constant on L, since 𝒥 ∩ {t = 0} = {(0,0)}. So L_t ≠ ∅ for small t ≠ 0.
   - Take such a t ∉ Z (Theorem A.9) and (p, t) ∈ L.
   - T_t has pure dimension 1 at p (Krull), so it contains a curve germ γ at p.
   - Since T ⊂ Ñ ∪ 𝒥 and 𝒥_t is finite, γ ∖ p ⊂ Ñ_t. So q(γ) is the germ at J_t of the branch H_t(b) of B_t, which is locally irreducible since it is a disc.
   - By (Kur′), the germ (B, p) is a universal deformation of X_p ≅ J_t. Since p lies in the deepest locus, its vertex labels are those of G_J.
   - Theorem A.9 at (J_t, p, y, H_t(b), γ) applies, because [comp_y(p)] = [Y_t] (y ∈ C(L)). (IMOV) would require H_t(b) ∖ J_t ⊂ Δ_{G_J}, which contradicts (P) and stratum preservation. So (STAY) holds: comp_y ≡ const of class [Y_t] along γ, i.e. γ ⊂ A_y(T).
3. **⊇: conclusion.**
   - A_y(T) = T ∩ (L_y × Δ) ∩ {([comp_y], [Y_t]) ∈ diagonal} is analytic.
   - It contains a curve in the slice {t} for uncountably many t.
   - An analytic set of dimension ≤ 1 has only countably many irreducible components, so it contains curves in only countably many slices.
   - Hence dim A_y(T) = 2, and A_y(T) = T by irreducibility. ∎

**Not reproduced here.** The following results of the original route are **not** proved in this text:
- the generic-time trichotomy (Theorem 1), which is a variant of Theorem A.9 using Lemma A.6 in place of Lemma A.8;
- Lemma J and Theorem R (junction trichotomy and the aligned-track reduction);
- Lemma 4.1(b)'s consequence "L ⊂ T for the unique lift-curve" (Prop. 3.3 of the original), which is Prop. 5.2 here;
- the original MS11♭/Prop. 4.3 bookkeeping.

They are not needed for Theorem A (see GAP G3).

---

## 9. Proof of Theorem A

**Theorem A.** Assume the hypotheses of the problem, read as (R1) and (R2^orb) — equivalently, by Theorem 7.2, as (R1), (R2) and (Loc) — and the Part I results I.2, I.3, I.5, I.6 in the forms of §1.6. Then Y_t = Y_0 for all t ∈ Δ, i.e. π_i(∂V_t) = {Y_0}.

*Proof.*

### 9.1 Set-up
- Take the data of I.5: pieces E^m with constant vertices c_m (m = 1, …, k); transitions J_m with labelled lifts (β̃_m, x_m) and (β̃′_m, x_m); the endpoint Q_0 with the labelled lift (β̃, x) and the terminal lift b̃.
- At each of the finitely many points J_1, …, J_{k−1}, Q_0, fix balls B′ ⋐ B as in Prop. 5.2. Impose Setting 6.0 for each of the finitely many lifts β̃_m, β̃′_m (at J_m) and β̃, b̃ (at Q_0), with one common ε > 0.
- Shrinking a lift to a smaller ball preserves "labelled by" (Definition 1.2). For each labelled lift, use in Setting 6.0 the isomorphism ι supplied by Definition 1.2. The piece of Setting 6.0 is then the piece named in I.5, since it is the piece containing Π_{S,ι}(lift ∖ 0). (If I.5 gives the labels only up to Aut(G), use Remark 6.4.)
- For b̃ choose any ι_b : G_{S_b} → G_b, and let E_b be the piece of Setting 6.0.
- Let p_m(t) (respectively p_0(t)) be the unique lift of H_t(J_m) (respectively H_t(Q_0)) given by Prop. 5.2.
- Put φ_m(t) := φ_{c_m}(E^m_t), where E^m_t = Π_t(E^m). This is well defined, since c_m ∉ M(E^m_t) by Theorem 4.4(a).

### 9.2 The value of the tracked copy is carried along the chain
**Claim.** [φ_m(t)] = [Y_t] for m = 1, …, k and |t| < ε.

1. **Base, m = 1.**
   - E^1 ⊂ ∂V_0 (via ξ_Γ), and E^1_t = Π_t(E^1) ⊂ Â^Γ_t = ∂V_t, by Lemma 3.1(2) and (R2).
   - On ∂V_t, pr_i = π_i ≡ Y_t, and c_1 = i. So φ_1(t) = Y_t, in fact for all t ∈ Δ.
2. **Step m → m + 1.** Apply Prop. 6.2 at J_m twice:
   - to (β̃_m, x_m), labelled by (E^m, c_m): [comp_{x_m}(p_m(t))] = [φ_m(t)];
   - to (β̃′_m, x_m), labelled by (E^{m+1}, c_{m+1}): [comp_{x_m}(p_m(t))] = [φ_{m+1}(t)].

   Both statements concern the **same point** p_m(t), the unique, Aut(J_m)-fixed lift of H_t(J_m) in B (Prop. 5.2). Hence [φ_{m+1}(t)] = [φ_m(t)].
   - No case distinction is needed: J_m may be a puncture of either adjacent piece or lie in its stratum (interior and R(D)-transitions), and the strata may or may not be of product type.

### 9.3 The endpoint
1. Prop. 6.2 at Q_0, applied to (β̃, x) labelled by (E^k, c_k), together with 9.2, gives
   [comp_x(p_0(t))] = [φ_k(t)] = [Y_t] for |t| < ε.
2. By I.6, (P) holds for b. By (K-c), x is in case MERGE or MOV for S_b. Prop. 6.3, applied to b̃ at the same point p_0(t), gives
   [comp_x(p_0(t))] ∈ F′(E_b).
3. Hence [Y_t] ∈ F′(E_b) for |t| < ε, and F′(E_b) is a finite set independent of t (Definition 2.1′).

### 9.4 Conclusion (incorporating Rep-3)
- The preimage of the finite set F′(E_b) under M_{g_i,n_i} → 𝔐_{g_i,n_i} is finite.
- t ↦ Y_t is continuous (Lemma 2.3) and Δ_ε is connected, so Y_t = Y_0 for |t| < ε.
- By Lemma 2.3 (holomorphy of t ↦ Y_t and the identity theorem), Y_t = Y_0 for all t ∈ Δ. ∎

**Remarks on the proof.**
- **No contradiction argument is needed.** We never assume that Y is non-constant. The generic-time machinery of the original route (Theorem N, the trichotomy) and the anchored sheets are replaced by three facts:
  - one fixed lift p(t) (Prop. 5.2);
  - constancy of the constant vertices of every transported piece (Theorem 4.4(a));
  - continuity of comp_x.
- **(IS) enters only through Theorem 4.4(b), used once, in step 9.3(2),** and only for the moving vertices of the single piece E_b. Theorem 4.4(a), which carries the value along the chain, does not use it.
- **Uses of (R2^orb).**
  - (a), (b), the inclusion "⊂" of (c), and (d) enter through Lemma 3.1, and through it Prop. 4.2, Lemma 4.3, Theorem 4.4 and Lemma 6.1(3).
  - (a) and both inclusions of (c) enter through Props. 5.1 and 5.2. The inclusion "⊃" is the one giving |Aut(J_t)| ≥ |Aut(J)|.
- **Part I used:** I.2 and I.3 (through Theorem 4.4), I.5 (the chain), I.6 (only (P) at Q_0). I.1 enters only through I.2/I.3. I.4 and Lemma PT are not used.

---

## Cited classical facts (from memory; precise statements as used)

**Moduli and Kuranishi theory**
- **(St)** For a stable graph G, with the notation of C4:
  - Mod_G acts properly discontinuously by biholomorphisms on T_G = ∏ T_w, with slice neighbourhoods;
  - ξ_G∘p is surjective onto Δ_G, with fibres the Mod_G-orbits;
  - Mod_Π = ker(Mod_G → Aut(G)), and this map is onto;
  - ξ_G : ∏ M_w → Δ_G is the quotient by Aut(G), a finite morphism of quasi-projective varieties, extending to the finite gluing morphism ξ̄_G : ∏ M̄_w → closure(Δ_G);
  - M̄_g and the M̄_w are projective.

  (Deligne–Mumford, Knudsen; Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, Ch. XI–XII.)
- **(Kur), (K2), (PN)** As stated in §1.4 (ACG II, Ch. XI).
- **(Kur′)** For p ∈ B, the germ (B, p) with the restricted family is a universal deformation of X_p, and q near p is the quotient by Stab_{Aut(J)}(p).
- **(Iso)** A biholomorphism of a stable pointed Riemann surface that is isotopic to the identity rel marked points is the identity.
- **(TF)** For N ≥ 3, Mod_w[N] (C4/Step 1 of Theorem 4.4) is torsion-free and normal of finite index. Ingredients:
  - Nielsen realisation (Kerckhoff): a finite-order class is realised by an automorphism;
  - g = 0: a Möbius map fixing ≥ 3 points is the identity;
  - g = 1: a group automorphism of an elliptic curve trivial on H_1(·, ℤ/N), N ≥ 3, is the identity;
  - g ≥ 2: Serre's lemma.
- **(BE)** Bers embedding: T_{h,m} is biholomorphic to a bounded domain in ℂ^{3h−3+m}.

**Teichmüller and hyperbolic geometry**
- **(Roy)** Royden; Earle–Kra, Gardiner for punctured surfaces: on T_{h,m} the Teichmüller metric equals the Kobayashi metric. Hence every holomorphic map from H, with the Poincaré metric of curvature −4, to T_{h,m} is 1-Lipschitz.
- **(VT)** Thurston, Veech: a mapping class preserving a Teichmüller disc and acting on it as a hyperbolic isometry is pseudo-Anosov. Equivalently, an affine automorphism of a half-translation surface with hyperbolic derivative is pseudo-Anosov.
- **(Bers)** For a pseudo-Anosov class g, τ(g) = inf_X d_T(X, gX) > 0. It is attained exactly on the unique g-invariant Teichmüller geodesic (the axis), along which g translates by τ(g).
- **(Th)** Thurston, "Minimal stretch maps between hyperbolic surfaces": let X, Y be complete hyperbolic surfaces of finite area and ψ : Y → X a homeomorphism (cusps to cusps). If ℓ_X(ψ(c)) ≤ ℓ_Y(c) for every closed geodesic c of Y, then ψ is homotopic to an isometry.
- **(Sel)** Selberg's lemma: finitely generated linear groups are virtually torsion-free. Lattices in PSL_2(ℝ) are finitely generated.
- **(Cent)** The centraliser of a lattice of PSL_2(ℝ) in the full isometry group of H is trivial.
- **(Dens)** For a lattice, the pairs of fixed points of hyperbolic elements are dense in ∂H × ∂H. Hence transverse intersection points of axes are dense in H.
- **(Unif)** Uniformisation of hyperbolic 2-orbifolds of finite type: given a compact Riemann surface minus finitely many points, with finitely many points c_k of assigned orders e_k ≥ 2 and χ^orb < 0, there is a lattice Λ and a holomorphic Galois branched covering H → H/Λ ≅ the surface. It is branched of order e_k exactly over c_k, and its cusps correspond to the punctures.
- **Lifting criterion** for coverings; local model z ↦ z^e at cone points.
- **(IS)** Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces" (1988), in the form used: if R is a Riemann surface of finite type and Y = T_{h,m}/Γ with Γ ⊂ PMod_{h,m} torsion-free of finite index, then each free homotopy class of maps R → Y contains only finitely many non-constant holomorphic maps. **Scope uncertain for m > 0: GAP G1.**
- **(dF)** Generalised de Franchis theorem (Imayoshi 1983; from memory): if R and Y are Riemann surfaces of finite type and Y is hyperbolic, there are only finitely many non-constant holomorphic maps R → Y.

**Topology and analytic geometry**
- **(KP1)** For a connected CW complex X and Y = K(π, 1), free homotopy classes [X, Y] correspond to Hom(π_1 X, π) modulo conjugation.
- **(Chow)** Closed analytic subsets of projective varieties are algebraic.
- **(Irr)** For a complex algebraic variety:
  - analytic irreducible components are the algebraic ones;
  - the analytic normalisation is the algebraic one;
  - the Euclidean closure of a constructible set equals its Zariski closure;
  - smooth irreducible quasi-projective curves are compact Riemann surfaces minus finitely many points.
- **(Remmert)** The image of an analytic set under a proper holomorphic map is analytic. Finite maps preserve dimension and map irreducible sets to irreducible sets.
- **(Krull)** If T is an irreducible analytic set of dimension d and f is holomorphic and non-constant on T, then every non-empty fibre of f has pure dimension d − 1.
- **(Cl)** For analytic X and a closed analytic Z ⊂ X, closure(X ∖ Z) is the union of the irreducible components of X not contained in Z.
- **(Reg)** The regular locus of an irreducible analytic set is a connected manifold. A proper analytic subset does not disconnect a connected complex manifold.
- **(CG)** Local structure of curve germs:
  - a 1-dimensional germ with r branches has arbitrarily small neighbourhoods U with U ∖ {z} a disjoint union of r punctured discs;
  - branches are homeomorphic to discs;
  - normalisation separates branches.
- **(Con)** Analytic sets are locally connected and locally conic, in particular locally contractible.
- **(HW)** Hurewicz–Wallman, *Dimension Theory*, Thm. IV.4:
  - a closed subset of covering dimension ≤ n − 2 does not separate a connected n-manifold;
  - analytic sets of complex dimension k have covering dimension 2k;
  - covering dimension is monotone on subsets of separable metric spaces.
- **(SF)** Stein factorisation of proper holomorphic maps (Grauert–Remmert).
- **(CR)** Cartan–Remmert: {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
- **Riemann extension theorem; identity theorem.**
- **CL (Part I, I.3)** is quoted, not classical; see §1.6.

---

## GAPs

- **G1 (citation scope; affects Theorem 4.4(b), hence Cor. 4.5, Prop. 6.3 and step 9.3(2)).** The Imayoshi–Shiga finiteness theorem is cited from memory, in the form (IS) above, for targets M_u[N] = T_u/Mod_u[N]. Vertices of boundary strata always carry marked points (n_u ≥ 1), so the marked case is the relevant one.
  - I recall the published theorem being formulated for holomorphic families of Riemann surfaces of type (g, n), but I cannot confirm that it covers all n ≥ 1, and in particular g = 0.
  - **Resolved** for vertices u of type (1,1) or (0,4): there M_u[N] is a hyperbolic Riemann surface of finite type, and (dF) gives finiteness of all non-constant holomorphic maps R → M_u[N].
  - **Narrowed.** (IS) is needed only for the moving vertices of the single piece E_b at the endpoint.
  - **Possible repair, not carried out.** Compose with a canonical finite-to-one holomorphic map M_{h,m}[N′] → M_{h′}[N] given by a level-structure-determined branched covering. Its lift T_{h,m} → T_{h′} is a holomorphic isometric embedding. Then apply the closed-surface finiteness theorem, and recover finiteness upstairs by a Lemma-CS-type argument.
- **G2 (the precise form of Part I).** I.5 is used in the form (K-a)–(K-c) with Definition 1.2. This is my precise reading of "common chart label x_m", "marking identification x_m ↔ c ↔ x_{m+1}", and of the Gap A repair ("the marking lift stays on one lifted curve with a fixed factor c"). Remark 6.4 shows that the argument tolerates relabelling by Aut(G). If Part I's statement were weaker than (K-b) in some other respect (for instance, if the label correspondence held only along some lift a·β̃ rather than β̃), that would have to be checked against Part I.
  - I.2/I.3 are used as stated in §1.6. In particular this includes J0 in every boundary stratum, with repair R3′.
- **G3 (not reproduced; not needed for Theorem A).** In Appendix A the following are not proved here:
  - the generic-time trichotomy (Theorem 1);
  - Lemma J;
  - Theorem R;
  - the original MS11♭/Prop. 4.3 bookkeeping.
- **Readings (not gaps in the proof, but conditions of the result).**
  - Theorem A is proved under (R1) and (R2^orb) = (O-emb), equivalently (R1), (R2) and (Loc).
  - **Open:**
    - the problem under the coarse reading (R2), and under the intrinsic reading (O-int);
    - whether a global admissible family with isotropy drop at the boundary exists (§8.2);
    - whether (Loc) at t_0 = 0 alone suffices (Remark 7.4).

=== END OF ANSWER extra_q2 ===

