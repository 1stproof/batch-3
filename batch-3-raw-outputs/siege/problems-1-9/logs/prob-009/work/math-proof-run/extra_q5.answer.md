# Answer to extra_q5: statement (Ψ)

**Status.** Work in progress. Plan:
- §0 conventions and the classical facts I cite (from memory);
- §1 proof of (i);
- §2 a new "shrinking lemma" (Lemma S): if you set the boundary lengths to 0 while keeping the interior FN coordinates fixed, no closed geodesic gets longer. The proof uses explicit 1-Lipschitz maps of right-angled hexagons;
- §3 proof of (ii):
  - (ii-a) in full when every node curve of z̃ inside Σ′ belongs to P′ (in particular when there are none);
  - (ii-b) the "limit lies in ∂M̄" part in full, for all P′;
  - (ii-c) the general case, conditional on Thurston's theorem (cited) and a standard twist-control estimate (sketched);
- §4 proof of (iii).

## §0. Conventions and cited facts

**Fenchel–Nielsen (FN) conventions.** Let F be a compact surface, possibly with boundary curves γ_1,…,γ_r, and let P be a pants decomposition of F (interior curves only). Fix seams in every pair of pants: three disjoint arcs joining the three cuffs in pairs. For a marked hyperbolic structure in which each γ_j is a geodesic boundary of length b_j > 0, or a cusp (b_j = 0):
- each pair of pants of P is cut by its seams (realised as orthogeodesics, or as geodesics running out to the cusp) into two isometric right-angled hexagons. When some b_j = 0, the corresponding side of each hexagon degenerates to an ideal vertex.
- the twist τ_α ∈ ℝ of α ∈ P is the signed displacement along α between the feet of the seams coming from the two sides. As usual it is lifted to ℝ using the marking.
- conversely, the surface Φ_P(b, c) with c = (ℓ_α, τ_α)_{α∈P} is obtained by gluing the hexagons: pants Y(ℓ's) = H ∪ H̄ (mirror copies glued along the seams), and pants are glued along α with twist τ_α.

So two surfaces with the same interior coordinates c are glued by literally the same combinatorial rule; only the pants shapes differ.

**Facts cited from memory.**

- **(F1) FN theorem.** Wolpert proved the analytic part; the rest is classical. For S closed and P a pants decomposition of S, the map T_g → (ℝ_{>0}×ℝ)^P is a real-analytic diffeomorphism. For a surface with cusps (b = 0), c ↦ Φ_P(0, c) is a homeomorphism (ℝ_{>0}×ℝ)^P → T(F°). The coordinates (ℓ_α, τ_α) of α ∈ P depend only on the hyperbolic structure of the union of the (one or two) pants adjacent to α.
- **(F2) Abikoff's description of T̄.** Let N be a multicurve and P ⊇ N any pants decomposition. Points w of T̄ whose node set N(w) is contained in P have coordinates:
  - (ℓ_α(w), τ_α(w)) for α ∈ P ∖ N(w), computed in the component of w containing α (pants adjacent to a node are cusped);
  - ℓ_α(w) = 0 for α ∈ N(w).

  For z̃ with node set N ⊆ P, a neighbourhood basis of z̃ in T̄ consists of the sets of w with: N(w) ⊆ N, ℓ_α(w) < ε for α ∈ N, and |ℓ_α(w) − ℓ_α(z̃)| < ε, |τ_α(w) − τ_α(z̃)| < ε for α ∈ P ∖ N. This holds for **every** such P, and the same description applies to T̄(F°) for any F°. The quotient map T̄(F°) → M̄(F°) (by the pure mapping class group) is continuous. This is the description recalled in the task statement.
- **(F3) Mumford compactness.** For ε > 0, {[Y] ∈ M(F°) : sys(Y) ≥ ε} is compact. Conversely, sys is continuous and positive on M(F°), so it is bounded below on every compact set. Hence [Y_k] leaves every compact subset of M(F°) iff sys(Y_k) → 0.
- **(F4) Collar lemma.** If α is a simple closed geodesic of length ℓ and β is a closed geodesic, then ℓ_β ≥ i(α,β) · 2 arcsinh(1/sinh(ℓ/2)).
- **(F5) Hyperbolic plane geometry.**
  - Nearest-point projection onto a closed convex subset of ℍ² is 1-Lipschitz.
  - The fibres of nearest-point projection onto a geodesic line L are the geodesics perpendicular to L. Hence the projection, restricted to a geodesic disjoint from L and not perpendicular to L, is injective and continuous, so monotone.
  - Right-angled hexagon with alternate sides a, x, y: the side s_{xy} opposite to a satisfies cosh s_{xy} = (cosh a + cosh x cosh y)/(sinh x sinh y), and similarly for the other sides. These formulas stay valid for a = 0 (ideal vertex).
- **(F6) Thurston's rigidity**, from "Minimal stretch maps between hyperbolic surfaces" (1986 preprint), cited from memory. Let Y, Z be complete finite-area hyperbolic structures on the same surface (cusps allowed). If ℓ_β(Y) ≤ ℓ_β(Z) for every simple closed curve β, then Y = Z in Teichmüller space. (Thurston shows the best Lipschitz constant L(Z,Y) equals sup_β ℓ_β(Y)/ℓ_β(Z), that L ≥ 1, and that L = 1 only if Y = Z.) **Only §3(ii-c) uses this.**

**Notation.** For X ∈ T_g and Σ′ ⊂ S as in the task, X|Σ′ is the bordered surface obtained by cutting X along the geodesics γ_j. If c(X) are the P′-FN coordinates of X and b(X) = (ℓ_{γ_j}(X))_j, then:
- X|Σ′ = Φ_{P′}(b(X), c(X));
- ψ_{Σ′,P′}(X) = Φ_{P′}(0, c(X));
- ℓ_β(X|Σ′) = ℓ_β(X) for every essential closed curve β ⊂ Σ′, since π_1Σ′ ⊂ π_1S and the holonomy of X|Σ′ is the restriction.

Throughout, Σ′ is not a pair of pants. If it were, T(Σ′°) would be a point and everything is trivial.

## §1. Proof of (i)

Extend P′ to a pants decomposition P of S by adding ∂Σ′ and a pants decomposition of S ∖ Σ′; extend the seams arbitrarily. By (F1), FN_P : T_g → (ℝ_{>0}×ℝ)^P is a homeomorphism.

Let pr be the projection to the P′-coordinates. These coordinates depend only on the pants inside Σ′, so they do not depend on the extension. Then ψ_{Σ′,P′} = Φ_{P′}(0, ·) ∘ pr ∘ FN_P is a composition of continuous maps (indeed of real-analytic maps).

**Naturality.** Let h ∈ Mod_g, acting by change of marking. The geodesic representative of hα in hX is the geodesic representative of α in X, and the h-image of a seam is a seam. Hence the FN coordinates of hX with respect to (hP′, h(seams)) equal those of X with respect to (P′, seams). Setting the boundary lengths to 0 commutes with relabelling, so ψ_{hΣ′,hP′}(hX) = h_*ψ_{Σ′,P′}(X), where h_* : T(Σ′°) → T(hΣ′°) is the change of marking. ∎

## §2. The shrinking lemma

**Lemma S.** Let b ∈ ℝ_{>0}^r and c ∈ (ℝ_{>0}×ℝ)^{P′}. There is a continuous map F : Φ_{P′}(b,c) → Φ_{P′}(0,c) with two properties:
- F does not increase the length of any rectifiable path;
- F induces the marking-identification on π_1(Σ′).

Consequently ℓ_β(Φ_{P′}(0,c)) ≤ ℓ_β(Φ_{P′}(b,c)) for every essential non-peripheral closed curve β ⊂ Σ′. In particular, for X ∈ T_g:

  ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X).

**Reduction to hexagons.** The idea is to build F pants by pants, and each pants map from a map of one hexagon H_a (boundary sides of length a = b_j/2 > 0) to the corresponding hexagon H_0 (those sides replaced by ideal vertices). The hexagon map f must have these properties:

- (H1) f is 1-Lipschitz for the hyperbolic metrics. Both hexagons are convex in ℍ², so this is the same as for their intrinsic metrics.
- (H2) f maps each "interior half-cuff" side (half of a curve of P′) isometrically onto the corresponding side, matching endpoints.
- (H3) f maps each seam side into the same seam side (or its closure through ideal vertices).
- No condition is imposed on the sides lying on the γ_j.

**Why such hexagon maps suffice.**
- Each pants is Y = H ∪ H̄, where H̄ is the mirror image across the seams. The pants map is f on H and σ_0 f σ_a on H̄, where σ is the reflection. Because f maps seams into seams, which σ fixes pointwise, the two definitions agree on the seams.
- On each interior cuff α, the pants map is the isometry fixing the seam feet. So two pants glued along α with twist τ_α, in both surfaces, give a well-defined continuous F. Pants not touching ∂Σ′ are mapped by the identity.
- F is 1-Lipschitz on a small ball around each point. At a seam or cuff point, a geodesic between points of different hexagons crosses the common side at some z, so d(Fx,Fy) ≤ d(Fx,Fz) + d(Fz,Fy) ≤ d(x,z) + d(z,y) = d(x,y). A locally 1-Lipschitz map does not increase lengths of paths.
- Let f_std : H_a → H_0 be the standard homeomorphism, defined away from the ideal vertices. It has the same side-to-side behaviour, and gluing it gives a map in the marking class. The straight-line homotopy (inside the convex H_0) between f and f_std keeps seam points on the same seam geodesic and fixes the half-cuffs. Therefore it is compatible with the mirror symmetry and the gluings, and F is homotopic to the marking map.
- Hence for the closed geodesic β of Φ(b,c), F∘β is freely homotopic to β in Φ(0,c) and has length ≤ ℓ_β(Φ(b,c)). Since β is non-peripheral, it has a geodesic representative in Φ(0,c), whose length minimises length in the free homotopy class. This gives the inequality.
- For X ∈ T_g: X|Σ′ = Φ(b(X), c(X)), ψ(X) = Φ(0, c(X)), and ℓ_β(X|Σ′) = ℓ_β(X).

Each pants of P′ has 1 or 2 cuffs among the γ_j; 3 cuffs would make Σ′ a pair of pants. If some γ_j coincide as curves of S they are still distinct boundary components of Σ′, so no pants has the same γ_j twice. This leaves two hexagon cases.

**Case 1: one boundary side.** Write H_a for the hexagon with alternate sides a (on γ), x, y. Here x and y are halves of interior cuffs, possibly two halves of the same curve. Its seams are s_{ax}, s_{xy}, s_{ya}, with V = x ∩ s_{xy} and W = y ∩ s_{xy}. H_0 is the hexagon with sides x, y and an ideal vertex ξ in place of a.

Write s_a = |s_{xy}(H_a)| and s_0 = |s_{xy}(H_0)|. By (F5), cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0, so s_a > s_0. Put d = (s_a − s_0)/2 > 0.

*Fermi picture.* Use Fermi coordinates (τ, h) about the line of s_{xy}: τ is the position of the foot (τ = 0 at V), and h ≥ 0 is the distance on the side of the hexagon.
- The lines of x and y are the fibres τ = 0 and τ = s (s = s_a or s_0).
- By convexity, each fibre τ = τ_0 with 0 ≤ τ_0 ≤ s meets the hexagon in a segment {0 ≤ h ≤ top(τ_0)}.
- The τ-projections of the top sides s_{ax}, a, s_{ya} are consecutive intervals [0, τ_C], [τ_C, τ_D], [τ_D, s_a]. Here C = s_{ax} ∩ a and D = a ∩ s_{ya}; monotonicity comes from (F5). A side line cannot be perpendicular to s_{xy}: e.g. s_{ax} and s_{xy} are both perpendicular to the x-line, hence ultraparallel.
- In H_0, the ideal vertex ξ projects to a point B′ at τ = u_1′ ∈ (0, s_0); write u_2′ = s_0 − u_1′. The perpendicular ray ω′ from B′ to ξ lies in H_0. In H_0, s_{ax} projects onto [0, u_1′) and s_{ya} onto (u_1′, s_0].

*x-placement.* Put H_a and H_0 in ℍ² so that they share V, the x-side and the direction of s_{xy}. Then they also share the full line of s_{ax}: it is the perpendicular to the x-side at its other endpoint, on the same side. H_a's seam s_{ax} is the segment of this line from the top of x to C, and C lies on H_0's ray from the top of x to ξ. By monotonicity of the projection along that ray, τ_C < u_1′.

*y-placement.* Symmetrically, sharing W, the y-side and s_{ya}, one gets s_a − τ_D < u_2′.

*Cut.* Let u := u_1′ + d. Then:
- τ_C < u_1′ < u;
- τ_D > s_a − u_2′ = u_1′ + 2d > u, using s_a = s_0 + 2d.

So the fibre τ = u in H_a is a segment c from B ∈ s_{xy} up to a point of the side a. Cut H_a = P_1 ∪ P_2 along c, with P_1 = H_a ∩ {τ ≤ u} and P_2 = H_a ∩ {τ ≥ u}, both convex. Likewise cut H_0 = Q_1 ∪ Q_2 along ω′, with Q_1 = H_0 ∩ {τ ≤ u_1′}, both convex.

*The map.* In the x-placement, set f := π_{Q_1} on P_1 (nearest-point projection, 1-Lipschitz by F5). In the y-placement, set f := π_{Q_2} on P_2. Check P_1; P_2 is symmetric.
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

By (F5), cosh σ_1 = (cosh a_2 + cosh a_1 cosh x)/(sinh a_1 sinh x). Hence R − cosh σ_1 = (cosh a_1 − cosh a_2)/(sinh a_1 sinh x).
- If a_1 ≤ a_2 this is ≤ 0, and we are done.
- Otherwise we need sinh σ_1 ≥ (cosh a_1 − cosh a_2)/(sinh a_1 sinh x). With Nn = cosh a_1 cosh x + cosh a_2 and Dd = sinh a_1 sinh x, this means Nn² − Dd² ≥ (cosh a_1 − cosh a_2)². Factoring:

  Nn² − (cosh a_1 − cosh a_2)² = cosh a_1 (cosh x + 1)(cosh a_1 (cosh x − 1) + 2 cosh a_2),

  while Dd² = sinh² a_1 (cosh x − 1)(cosh x + 1). The required inequality reduces to

  cosh² a_1 (cosh x − 1) + 2 cosh a_1 cosh a_2 ≥ sinh² a_1 (cosh x − 1),

  which is obvious.

So D_1 (and likewise D_2) is beyond M, and Case 2 is done. This completes the proof of Lemma S. ∎

*Remark.* Lemma S holds for every P′ and every b, with no smallness assumption. It is a pure monotonicity statement: shrinking the boundary to cusps at fixed interior FN coordinates shortens every closed geodesic (weakly).

## §3. Proof of (ii)

**Setting.** X_k ∈ T_g and X_k → z̃ in T̄_g. Let N be the node set of z̃, with ∂Σ′ ⊆ N. Since N is a multicurve containing ∂Σ′, each other node curve either lies in int Σ′ or is disjoint from Σ′. Write N_in for the node curves in int Σ′ (non-peripheral in Σ′). Let W̃ ∈ T̄(Σ′°) be the **Σ′-side of z̃**:
- its components are the components of z̃ lying in Σ′, with nodes on ∂Σ′ turned into labelled punctures;
- its node set is N_in;
- it is marked by the marking of z̃.

W̃ is defined from z̃ alone.

### (ii-a) Convergence and independence when N_in ⊆ P′ (in particular when N_in = ∅)

**Proposition A.** If every node curve of z̃ in int Σ′ belongs to P′, then ψ_{Σ′,P′}(X_k) → W̃ in T̄(Σ′°), hence [ψ_{Σ′,P′}(X_k)] → [W̃] in M̄(Σ′°). The limit does not depend on P′ among the pants decompositions containing N_in, which when N_in = ∅ means all of them. If N_in ≠ ∅, the limit lies in ∂M̄(Σ′°).

*Proof.*
1. Let P := P′ ∪ ∂Σ′ ∪ P_out, where P_out is a pants decomposition of S ∖ Σ′ containing the node curves outside Σ′. Then P ⊇ N.
2. By (F2) applied to P: ℓ_α(X_k) → 0 for α ∈ N_in. For α ∈ P′ ∖ N_in, (ℓ_α, τ_α)(X_k) → (ℓ_α, τ_α)(z̃), computed in the component of z̃ containing α.
3. By definition, ψ(X_k) ∈ T(Σ′°) has exactly these P′-coordinates (c(X_k)).
4. The coordinates (ℓ_α, τ_α)(z̃) for α ∈ P′ ∖ N_in are, by definition, the FN coordinates of W̃: same component, same cusped pants, same seams.
5. By (F2) in T̄(Σ′°) with the pants decomposition P′ ⊇ N_in = N(W̃), ψ(X_k) → W̃. Project to M̄(Σ′°) by the continuous quotient map.
6. Independence holds because W̃ does not involve P′. If N_in ≠ ∅, W̃ has nodes, so [W̃] ∈ ∂M̄(Σ′°). ∎

*Remark.* For finite k, ψ_{Σ′,P′}(X_k) does depend on P′. Changing P′ changes which coordinates are held fixed while the boundary is shrunk. Only the limit is intrinsic.

### (ii-b) The boundary part, for every P′

**Proposition B.** Let X_k ∈ T_g be any sequence (convergence is not needed). Suppose some essential non-peripheral simple closed curve β ⊂ Σ′ has ℓ_β(X_k) → 0. Then for every pants decomposition P′ of Σ′:
- sys(ψ_{Σ′,P′}(X_k)) → 0;
- [ψ_{Σ′,P′}(X_k)] leaves every compact subset of M(Σ′°);
- every limit point in M̄(Σ′°) lies in ∂M̄(Σ′°).

*Proof.* By Lemma S, ℓ_β(ψ_{Σ′,P′}(X_k)) ≤ ℓ_β(X_k) → 0, and (F3) gives the rest. ∎

In the situation of (ii), the hypothesis "some essential non-peripheral curve of Σ′ has length → 0" holds iff N_in ≠ ∅:
- if β ∈ N_in, then ℓ_β → 0;
- if β is not a node curve, either β crosses a node curve and ℓ_β(X_k) → ∞ by (F4), or β is disjoint from N, and then (F2) with a pants decomposition containing N ∪ {β} gives ℓ_β(X_k) → ℓ_β(z̃) > 0.

So Proposition B gives "the limit lies in ∂M̄(Σ′°)" whenever that hypothesis holds, with no restriction on P′.

### (ii-c) Convergence for general P′ — conditional on Thurston's rigidity (F6)

**Proposition C.** Assume (F6). Then for every pants decomposition P′ of Σ′, ψ_{Σ′,P′}(X_k) → W̃ in T̄(Σ′°), and hence [ψ_{Σ′,P′}(X_k)] → [W̃] in M̄(Σ′°).

*Proof.* Write Y_k = ψ_{Σ′,P′}(X_k). Fix a pants decomposition P″ of Σ′ containing N_in. It suffices to show that every subsequence has a further subsequence along which Y_k → W̃. We use (F2) in T̄(Σ′°) with P″.

(1) *Upper bounds.* Let β ⊂ Σ′ be simple and disjoint from N_in (so disjoint from N). By Lemma S, ℓ_β(Y_k) ≤ ℓ_β(X_k). By (F2) with a pants decomposition containing N ∪ {β}, ℓ_β(X_k) → ℓ_β(W̃) < ∞ (or → 0 if β ∈ N_in). So:
- ℓ_α(Y_k) → 0 for α ∈ N_in;
- every such β has bounded length along Y_k.

(2) *Lower bounds.* Let α ∈ P″ ∖ N_in, lying in the component C of Σ′ ∖ N_in. α is non-peripheral in C, so C is not a pair of pants and there is a simple β ⊂ C with i(α,β) > 0. By (1), ℓ_β(Y_k) is bounded. By the collar lemma (F4), ℓ_α(Y_k) is bounded below. Also ℓ_α(Y_k) is bounded above by (1).

(3) *Twists — standard estimate, sketched here and not written out in full.* Let α ∈ P″ ∖ N_in and let β_α be a dual curve inside the union X_α of the two P″-pants adjacent to α. It crosses α once (X_α a one-holed torus) or twice (X_α a four-holed sphere), and it is disjoint from N_in.

Lift to ℍ²: consecutive lifts L_0, L_1, L_2 of α met by a lift of β_α span at most two periods of β_α. Let d_0, d_2 be the lengths of the orthogeodesics from L_1 to L_0 and L_2, and t the distance along L_1 between their feet. Then 2ℓ_{β_α} ≥ d(L_0, L_2), and by the right-angled hexagon formula

  cosh d(L_0, L_2) = cosh d_0 cosh d_2 + sinh d_0 sinh d_2 cosh t.

- d_0 and d_2 are lengths of orthogeodesics from α to itself in the adjacent pants. They are continuous positive functions of the cuff lengths on {ℓ_α ∈ [m, M], other cuffs ∈ [0, M]} (cusps allowed), so they are bounded below.
- |t − τ_α| ≤ ℓ_α, because the feet differ from the seam feet by at most ℓ_α.

Hence |τ_α(Y_k)| ≤ arccosh(cosh(2ℓ_{β_α}(Y_k))/(sinh d_0 sinh d_2)) + ℓ_α, which is bounded by (1) and (2).

(4) *Limit.* By (2) and (3), along a subsequence the P″-coordinates (ℓ_α, τ_α)(Y_k), α ∈ P″ ∖ N_in, converge to (ℓ_α^∞, τ_α^∞) with ℓ_α^∞ > 0. With (1) and (F2) this gives Y_k → W̃′, where W̃′ ∈ T̄(Σ′°) has node set exactly N_in and these coordinates.

(5) *Identification.* Let C be any component of Σ′ ∖ N_in that is not a pair of pants. Let W′_C, W_C ∈ T(C°) be the corresponding cusped components of W̃′ and W̃. For simple non-peripheral β ⊂ C, (F2) with a pants decomposition containing N_in ∪ {β} gives ℓ_β(W′_C) = lim ℓ_β(Y_k). By (1), this is ≤ lim ℓ_β(X_k) = ℓ_β(W_C). By (F6), W′_C = W_C. Pants components carry no moduli.

A point of T̄(Σ′°) with node set N_in is determined by its marked components, since twists at nodes are forgotten. So W̃′ = W̃. ∎

**What is proved for (ii).**
- The convergence and independence statements of (ii) are fully proved under "every node curve of z̃ in int Σ′ lies in P′". This contains the extra hypothesis of the task: no node curve of z̃ in int Σ′.
- The "limit lies in ∂M̄(Σ′°)" part is fully proved for all P′ (Proposition B).
- The general convergence statement is proved modulo (F6) and the twist estimate (3), which is only sketched.

## §4. Proof of (iii) (chart form)

**Setting.** Let N_J = {α_e} be the node curves of J̃ and U a precisely invariant neighbourhood. Assume, as in the task, that U/Tw ≅ B, with the quotient topology induced from T̄_g (Kuranishi/plumbing chart; taken as given).

Shrinking U if necessary, take U inside a basic neighbourhood of (F2) for J̃ and some pants decomposition P ⊇ N_J. Then every w ∈ U has N(w) ⊆ N_J. In the plumbing description, the nodes of the fibre over p are the α_e with s_e(p) = 0.

Let y be a vertex and Σ_y the corresponding component of S ∖ ∪α_e; a loop edge contributes two punctures. If Σ_y is a pair of pants, everything is trivial. Otherwise fix a pants decomposition P_y of Σ_y with seams, and take P := N_J ∪ ⋃_v P_v.

**Extension of ψ to U.** For w ∈ U, no curve of P_y is a node of w. So the coordinates (ℓ_α(w), τ_α(w)), α ∈ P_y, are defined, with the boundary curves of Σ_y possibly nodes, i.e. cusps. Define

  ψ_y(w) := Φ_{P_y}(0, (ℓ_α(w), τ_α(w))_{α∈P_y}) ∈ T(Σ_y°).

On U ∩ T_g this is ψ_{Σ_y,P_y}.

**Claim 1: ψ_y is continuous on U.** By (F2), the coordinates (ℓ_α, τ_α), α ∈ P_y ⊆ P ∖ N_J, are continuous on U: at any w_0 ∈ U, α is not a node of w_0. Then use (F1) for Φ_{P_y}(0, ·).

**Claim 2: ψ_y is Tw-invariant, already in T(Σ_y°).** A Dehn twist about α_e changes the FN coordinates with respect to P only in τ_{α_e} (by ±ℓ_{α_e}). For a node, the twist parameter is not a coordinate, and the twist fixes the point. The coordinates of P_y are unchanged.

So ψ_y, and hence [ψ_y], descends to a continuous function on U/Tw ≅ B. In particular [ψ_{Σ_y}] extends continuously from the image of U ∩ T_g (the locus where all s_e ≠ 0) to all of B, which is stronger than "a neighbourhood of L_y". Equivalently, along any sequence in U converging in T̄_g to a point over L_y, [ψ_{Σ_y}] converges; this is also Proposition A, since there are no nodes inside Σ_y.

**Claim 3: on L_y the extension equals [F_y].** If w ∈ U lies over p ∈ L_y, then every boundary curve of Σ_y is a node of w (s_e(p) = 0 for all edges e at y). So the component of w lying in Σ_y is the cusped surface whose P_y-FN coordinates are those of w. That is exactly ψ_y(w), marked.

Its class in M(Σ_y°), with punctures labelled by the half-edges at y, is the component labelled y of the fibre over p with its special points: [ψ_y(w)] = [F_y(p)].

On L_y this value does not depend on P_y. Off L_y, the extension does depend on P_y; the statement only claims independence on L_y. ∎

## Summary: what is proved, conditional, and open

**Proved** (using only the classical facts F1–F5):
- (i): continuity and naturality.
- Lemma S (new, with complete proof): ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X) for all non-peripheral β ⊂ Σ′. This holds for every P′ and every X ∈ T_g, via explicit 1-Lipschitz hexagon maps (nearest-point projections).
- (ii) convergence to the Σ′-side of z̃, and independence of P′, whenever every node curve of z̃ in int Σ′ lies in P′. This includes the task's extra hypothesis that no node curve lies in int Σ′.
- (ii) "limit lies in ∂M̄(Σ′°)": for every P′ and every sequence, short interior curves of X_k force sys(ψ(X_k)) → 0 (Proposition B).
- (iii) in full. In fact [ψ_{Σ_y}] extends continuously to all of B, and equals [F_y] on L_y. This uses only (F2) and the chart description U/Tw ≅ B, which the task supplies as given.

**Conditional:** (ii) convergence for arbitrary P′, when some node curves of z̃ in int Σ′ cross curves of P′ (Proposition C). This rests on two things:
- Thurston's rigidity theorem (F6), cited from memory: a finite-area hyperbolic structure whose simple length spectrum is dominated by another's equals it;
- a standard twist-control estimate, sketched in §3(ii-c)(3) but not written out in full.

**Open (in this answer):** a self-contained proof of Proposition C that avoids (F6). I see no reason for it to be false; Lemma S plus (F6) give a proof. The application never needs this case.

**Citations made from memory:**
- (F1) Fenchel–Nielsen theorem and Wolpert's analyticity;
- (F2) Abikoff's description of augmented Teichmüller space, valid for any pants decomposition containing the nodes;
- (F3) Mumford compactness;
- (F4) the collar lemma;
- (F6) Thurston's minimal-stretch rigidity;
- the right-angled hexagon formulas in (F5).

=== END OF ANSWER extra_q5 ===
