# Surgery on an L-space knot has at most two prime summands

## Answer

**Yes.** Here an "L-space knot" is a knot K in S^3 that has an L-space surgery S^3_r(K) at some slope r ∈ Q. The answer holds for every slope r ∈ Q ∪ {∞}.

**Theorem.** Let K ⊂ S^3 be an L-space knot and r ∈ Q ∪ {∞}. Then S^3_r(K) has at most two prime summands.

The bound is sharp. By Moser, S^3_6(T(2,3)) ≅ L(2,1) # L(3,2), which has two prime summands. More generally, if a cable C_{a,b}(J) is an L-space knot, its surgery at the cabling slope ab is L(a,b) # S^3_{b/a}(J).

The proof is complete, provided the published theorems listed in §0 hold. Those theorems are cited from memory. The Status section at the end gives the details.

---

## 0. Conventions and cited results

F = Z/2. M_K is the exterior of K, μ and λ are its meridian and Seifert longitude, and g = g(K).

**Mirroring.** S^3_r(mK) ≅ −S^3_{−r}(K), and reversing orientation does not change the number of prime summands. If K has a nontrivial L-space surgery at a negative slope, then mK has one at a positive slope. So we may assume K is a *positive* L-space knot, meaning it has an L-space surgery at some positive slope. The surgery slope p is then still an arbitrary integer of either sign, and both signs are treated below.

Cited theorems (from memory):

1. **Gabai (1987).** For a nontrivial knot K, S^3_0(K) is irreducible.
2. **Gordon–Luecke (1987).** If S^3_r(K) is reducible for a nontrivial K, then r is an integer.
3. **Howie (2002), the Scott–Wiegold conjecture.** A free product of three nontrivial cyclic groups is not the normal closure of a single element.
4. **Gordon–Luecke (1996), "Reducible manifolds and Dehn surgery".** If a surgery on a nontrivial knot in S^3 is reducible, one of its prime summands is a lens space other than S^3 and S^1×S^2. *We use only this weak consequence:* some prime summand L is an L-space with |H_1(L)| ≥ 2.
5. **Ni; Ghiggini (for g = 1).** An L-space knot is fibred. Its fibre is a minimal-genus Seifert surface F, of genus g, with one boundary component.
6. **Grushko–Neumann.** rank(G_1 * G_2) = rank G_1 + rank G_2 for finitely generated groups. Also van Kampen: π_1(M_1 # M_2) ≅ π_1(M_1) * π_1(M_2).
7. **Perelman.** A closed simply connected 3-manifold is S^3. This can be avoided; see Remark 3.4.
8. **Ozsváth–Szabó surgery package.** Let K be a positive L-space knot of genus g ≥ 1 and p ≠ 0 an integer.
   - (a) *Integers V_s.* There are integers V_s (s ∈ Z) with V_s ≥ 0, V_s − V_{s+1} ∈ {0,1}, V_s = 0 iff s ≥ g, and V_{−s} = V_s + s. Put H_s := V_{−s}, so H_s = 0 iff s ≤ −g.
   - (b) *Integer surgery mapping cone, plus version.*
     - Spin^c(S^3_p(K)) is labelled by Z/|p|. For each label i, HF^+(S^3_p(K), i) is isomorphic, as a relatively Z-graded F[U]-module, to the homology of the mapping cone of D = Σ(v_s + h_s): ⊕_{s≡i} A_s^+ → ⊕_{s≡i} B_s^+ (direct sums).
     - Here v_s: A_s^+ → B_s^+ and h_s: A_s^+ → B_{s+p}^+ are homogeneous chain maps.
     - For a positive L-space knot, H_*(A_s^+) ≅ H_*(B_s^+) ≅ T^+ := F[U,U^{−1}]/U·F[U]. On homology, v_s is U^{V_s} and h_s is U^{H_s}.
     - *Why homology-level maps suffice.* F[U] is a graded PID, hence hereditary. So every complex of graded F[U]-modules is quasi-isomorphic to its homology (it is formal), and in the derived category Hom(X, Z) = Hom(H(X), H(Z)) ⊕ Ext^1(H(X), H(Z)) with the appropriate degree shift. The target homology ⊕ T^+ is injective: T^+ is divisible, F[U] is Noetherian, and over a Noetherian ring direct sums of injectives are injective. So the Ext^1 term vanishes, and the morphism D is determined up to isomorphism in the derived category by its homology map. The mapping cone of a morphism is determined up to isomorphism by the morphism. Hence the homology of the cone, with its relative grading, can be computed from the homology-level maps U^{V_s} and U^{H_s}.
   - (c) *Affine labelling.* The labelling Spin^c(S^3_p(K)) ↔ Z/|p| is affine over H_1(S^3_p(K)) = Z/|p| = ⟨[μ]⟩, and [μ] acts by i ↦ i+1. The sign convention does not matter below.
   - (d) *Connected sums.*
     - Spin^c(Y_1 # Y_2) = Spin^c(Y_1) × Spin^c(Y_2), equivariantly for H_1(Y_1) ⊕ H_1(Y_2).
     - CF^−(Y_1#Y_2,(t_1,t_2)) ≃ CF^−(Y_1,t_1) ⊗_{F[U]} CF^−(Y_2,t_2).
     - If L is an L-space, then CF^−(L,t) ≃ F[U]. So HF^+(L#Y'',(t,t'')) ≅ HF^+(Y'',t'') as relatively graded F[U]-modules, up to a shift.
     - Lens spaces are L-spaces.

---

## 1. Reduction

Suppose S^3_r(K) has at least three prime summands. We derive a contradiction.

- If K is the unknot, its surgeries are S^3, S^1×S^2 and lens spaces, each with at most one prime summand.
- So K is nontrivial. Slope ∞ gives S^3, and slope 0 gives an irreducible manifold by Gabai.
- By Gordon–Luecke 1987, a non-integral slope also gives an irreducible manifold. An irreducible closed 3-manifold other than S^3 is prime.

So r = p is a nonzero integer. After mirroring (§0), K is a nontrivial positive L-space knot of genus g ≥ 1 and p ≠ 0 has either sign. Write

  Y = S^3_p(K) = P_1 # ⋯ # P_k, with every P_i prime and k ≥ 3.

H_1(Y) = Z/|p| is finite. So no P_i is S^1×S^2, and each H_1(P_i) is a direct summand of Z/|p|, hence finite cyclic.

## 2. Two topological consequences

**Lemma 2.1 (a homology-sphere summand).** Some P_i is an integer homology sphere B ≠ S^3.

*Proof.*
- π_1(M_K) is normally generated by μ, and π_1(Y) is a quotient of it, so π_1(Y) is normally generated by one element.
- Suppose three summands, say P_1, P_2, P_3, had nontrivial H_1. Then π_1(Y) = π_1(P_1) * ⋯ * π_1(P_k) maps onto π_1(P_1) * π_1(P_2) * π_1(P_3), by killing the other factors, and then onto H_1(P_1) * H_1(P_2) * H_1(P_3).
- That target is a free product of three nontrivial cyclic groups, and it is normally generated by the image of one element. This contradicts Howie's theorem.
- So at most two summands have nontrivial H_1. Since k ≥ 3, some P_i has H_1 = 0, and P_i ≠ S^3 because it is a prime summand. ∎

Write Y ≅ A # B, where B is this homology sphere and A is the sum of the other summands.

**Lemma 2.2 (an L-space summand).** Y ≅ L # Y'', where L is a lens space with a := |H_1(L)| ≥ 2. Hence a divides |p| and |p| ≥ 2.

*Proof.* By Gordon–Luecke 1996 (weak form), some prime summand is a lens space L ≠ S^3, S^1×S^2, so a ≥ 2. Also H_1(L) is a direct summand of Z/|p|. ∎

## 3. The cover bound

**Proposition 3.1 (cover bound).** Let K ⊂ S^3 be fibred with fibre F of genus g and one boundary component, and let p ≠ 0 be an integer. If S^3_p(K) ≅ A # B with B an integer homology sphere other than S^3, then

  |p|·rank π_1(B) + rank π_1(Ã) ≤ 2g, and hence |p| ≤ g.

Here N := |p| and Ã is the connected N-fold cyclic cover of A defined below.

*Setup.*
- Y = S^3_p(K) = M_K ∪_T V, where the meridian disc of the solid torus V is bounded by α = pμ + λ on T = ∂M_K.
- H_1(M_K) = Z⟨μ⟩. The class of a loop is its algebraic intersection number with F, and λ = 0 in H_1(M_K). So H_1(Y) = Z/N.
- Let φ: π_1(Y) → H_1(Y) = Z/N be the abelianisation, which is onto, and let q: Y_N → Y be the connected N-fold cyclic cover with group ker φ.

**3.2 Lower bound: Y_N ≅ Ã # (N copies of B).**
1. Let S be the splitting sphere, so Y = A° ∪_S B°, where ° means one open ball removed.
2. π_1(Y) = π_1(A) * π_1(B), and H_1(A) = H_1(Y) ≅ Z/N because H_1(B) = 0.
3. φ restricted to π_1(B°) = π_1(B) factors through H_1(B) = 0. So q^{−1}(B°) is N disjoint copies of B°, each mapped homeomorphically onto B°.
4. S is simply connected, so q^{−1}(S) is N spheres.
5. φ restricted to π_1(A°) = π_1(A) is the surjection π_1(A) → H_1(A) ≅ Z/N. So q^{−1}(A°) is connected: it is the induced N-fold cyclic cover Ã of A with N balls removed (the removed ball lifts to N balls).
6. Y_N is therefore Ã minus N balls, with a copy of B° glued to each boundary sphere. The gluing graph is a star, hence a tree, so Y_N ≅ Ã # B # ⋯ # B with N copies of B.
7. By van Kampen and Grushko–Neumann, rank π_1(Y_N) = rank π_1(Ã) + N·rank π_1(B).
8. π_1(B) is perfect (H_1(B) = 0) and nontrivial (Perelman, since B ≠ S^3). A nontrivial cyclic group has nontrivial abelianisation, so π_1(B) is not cyclic, and rank π_1(B) ≥ 2.

If N = 1 the cover is trivial and Ã = A. Nothing changes.

**3.3 Upper bound: rank π_1(Y_N) ≤ 2g.**
1. *The exterior lifts to a mapping torus.* On π_1(M_K), φ is the composite π_1(M_K) → H_1(M_K) = Z → Z/N with μ ↦ 1. So E := q^{−1}(M_K) is connected and is the N-fold cyclic cover dual to F. It is the mapping torus of h^N, where h is the monodromy, and it fibres over S^1 with fibre F̃, a homeomorphic lift of F. So π_1(E) = π_1(F̃) ⋊ ⟨t⟩, and the fibration map π: π_1(E) → Z has kernel π_1(F̃) and sends t ↦ 1.
2. *The boundary lifts to one torus.* μ ∈ π_1(T) maps onto a generator of Z/N. So T̃ := q^{−1}(T) is one torus, and q|: T̃ → T has degree N.
3. *The solid torus lifts to one solid torus.* μ meets α once, so μ is isotopic in V to the core of V. Hence π_1(V) maps onto Z/N, and Ṽ = q^{−1}(V) is one solid torus with ∂Ṽ = T̃.
4. *The filling curve.* The meridian disc of V lifts to N discs. Let β ⊂ T̃ be the boundary of one of them. Then q maps β homeomorphically onto α, so q_*[β] = [α]. Y_N = E ∪ Ṽ is the Dehn filling of E along β.
5. *Intersection numbers.* For a degree-N covering f: T̃ → T of tori, f_*x · f_*y = N(x·y). This follows from the transfer f^!: f_*x·z = x·f^!z and f^! f_* = N, since deck transformations of a torus act trivially on H_1.
   - F̃ ∩ T̃ = ∂F̃ is a single curve λ̃ with q_*[λ̃] = [λ].
   - Hence N(β·λ̃) = α·λ = (pμ+λ)·λ = ±p, so β·λ̃ = ±1. This holds for either sign of p.
6. *β goes once around.* On π_1(T̃), the map π is algebraic intersection with the fibre boundary λ̃. So π(β) = ±1, and β represents t^{±1}w for some w ∈ π_1(F̃), for any choice of basepoint path.
7. *Conclusion.* By van Kampen, π_1(Y_N) = π_1(E)/⟨⟨β⟩⟩. In this quotient t = w^{∓1} lies in the image of π_1(F̃). So π_1(Y_N) is generated by the image of π_1(F̃), which is free of rank 2g, and rank π_1(Y_N) ≤ 2g.

Combining 3.2 and 3.3: 2N ≤ N·rank π_1(B) ≤ rank π_1(Y_N) ≤ 2g, so |p| ≤ g. ∎

*Sanity checks.*
- T(2,3) with p = 1 gives the Poincaré sphere, and the bound is tight: 2 = 2.
- Take J fibred and nontrivial and p ≥ 2. The cable C_{p,1}(J) is fibred, and its p-surgery is L(p,1) # S^3_{1/p}(J). Its genus is p·g(J) ≥ p, which agrees with the bound. (This cable is not an L-space knot. The check only tests Proposition 3.1, which needs fibredness alone.)

**Remark 3.4 (avoiding Perelman).** Replace rank by Heegaard genus h.
- Since β·λ̃ = ±1, Y_N is the closed manifold of an open book with page F̃, so h(Y_N) ≤ 2g.
- By Haken's lemma, h(Y_N) = h(Ã) + N·h(B).
- h(B) ≥ 2, since closed manifolds of Heegaard genus ≤ 1 are S^3, S^1×S^2 and lens spaces.

## 4. Heegaard Floer input

In this section K is a nontrivial positive L-space knot of genus g, and p ≠ 0 is an integer with N := |p|.

### 4a. Coset invariance

Suppose S^3_p(K) ≅ L # Y'', where L is an L-space with a = |H_1(L)| ≥ 2 and Y'' is any closed oriented 3-manifold. If the homeomorphism reverses orientation, replace (L, Y'') by (−L, −Y''); −L is again an L-space of the same order. Put b := N/a. Then b is an integer and b ≢ 0 mod N.

**Lemma 4.1 (coset invariance).** For every label i, HF^+(S^3_p(K), i) ≅ HF^+(S^3_p(K), i+b) as relatively graded F[U]-modules, up to a degree shift.

*Proof.*
- H_1(L) is a subgroup of order a of Z/N = ⟨[μ]⟩, so it is ⟨b[μ]⟩.
- By 8(d), the spin^c structures with a fixed Y''-component t'' form one H_1(L)-orbit. All of them have HF^+ ≅ HF^+(Y'',t'') up to shift.
- By 8(c), the H_1(L)-orbits are exactly the cosets i + bZ of labels. ∎

### 4b. The invariant τ

Let M be a graded F[U]-module that is finite-dimensional in each degree. Record degrees by *level*, meaning half the grading, so U lowers the level by 1. Define τ(M) to be the multiset of levels k, where k appears with multiplicity dim(M_k / U·M_{k+1}).

τ is an isomorphism invariant, and shifting the grading translates τ. If M = T^+ ⊕ ⊕_l F[U]/U^{e_l}, then τ(M) is the multiset of the top levels of the finite summands, because U maps onto T^+. In particular |τ(M)| is the number of finite summands.

### 4c. The level model and the structure of each class

Fix a class c ∈ Z/N. Let s_1 < s_2 < ⋯ < s_m be the integers s ≡ c (mod N) with |s| ≤ g−1. Consecutive ones differ by N, and m = n_c := #{s ≡ c : |s| ≤ g−1}.

**Level model.** Use 8(b), which lets us compute with the homology-level maps U^{V_s} and U^{H_s} between copies of T^+.
- Record each tower T^+ by its *bottom level*.
- Regrade each B-tower so that the cone maps preserve levels. This is possible: in one class the A's and B's form a connected graph (each B is joined to its at most two adjacent A's), and the relative grading of the cone is homogeneous. A map U^e from a tower with bottom x then lands in a tower with bottom x+e.
- Under this regrading, an A-element at level k maps to the B-element at level k in each adjacent B that is "present at level k", meaning its bottom is ≤ k. All exponents are ≥ 0, so every present B has its adjacent A's present.
- So at level k the cone map is the coboundary δ_k: F^{vertices} → F^{edges} of a graph G_k. Its vertices are the A's with bottom ≤ k, and its edges are the B's with bottom ≤ k, each B joining its adjacent A's.
- U acts on cochains by restriction from G_{k+1} to G_k.
- The cone has two terms, and D commutes with U. So H(cone) = ker D ⊕ coker D as graded F[U]-modules.

The true relative grading is 2·level + constant on each side, because both satisfy the same constraints on a connected graph. So τ, computed in levels, is the invariant of §4b up to translation.

**Proposition 4.2 (structure of a class).**

(A) Let 0 < p ≤ 2g−2 and m ≥ 1. Then τ(HF^+(S^3_p(K), c)) = {y − 1 : y ∈ Y_c}. Here Y_c is the multiset of the m−1 "interior peak" levels
  y_j = (μ_j² − p²/4)/(2p), with μ_j = s_j + p/2 (1 ≤ j ≤ m−1).
In particular |τ| = m − 1.

(B) Let p = −N < 0 and m ≥ 1. Let Π_c be the multiset of the m+1 "peak" levels
  b(t) = −(u² − N²/4)/(2N), with u = t + N/2, for t ∈ {s_1 − N, s_1, s_2, …, s_m}.
Let M be its maximum. Then τ(HF^+(S^3_p(K), c)) = {y − 1 : y ∈ Π_c} with one copy of M − 1 removed. In particular |τ| = m.

Neither multiset depends on K.

*Proof of (A).*
- In class c, the A's and B's form one infinite path ⋯ A_{s−p} — B_s — A_s — B_{s+p} — ⋯. The bottoms must satisfy x(s+p) − x(s) = H_s − V_{s+p}, since B_{s+p} receives U^{H_s} from A_s and U^{V_{s+p}} from A_{s+p}.
- One solution is x(s) = s(s−p)/(2p) − V_s. Check: x(s+p) − x(s) = s − V_{s+p} + V_s = H_s − V_{s+p}, using H_s = V_s + s.
- The B between s and s+p has bottom y = x(s) + H_s = s(s+p)/(2p) = (μ² − p²/4)/(2p), where μ = s + p/2.
- x(s) → +∞ as |s| → ∞: for s ≥ g, V_s = 0, and for s < 0, V_s = V_{−s} + |s| ≤ g + |s|. So the quadratic term dominates, and G_k is a finite subforest of a path.
- The coboundary of a finite forest is onto. So D is surjective and HF^+ ≅ ker D. At level k, ker δ_k is the space of functions on the components of G_k, and U is restriction of functions.
- Hence dim(M_k / U·M_{k+1}) is the number of merges: the number of components of G_k minus the number of components of G_{k+1} that contain a vertex of G_k.
- *Edges with a zero exponent.* V_s = 0 iff s ≥ g, and H_s = 0 iff s ≤ −g. A B with both exponents 0 would be B_{s+p} with s ≤ −g and s+p ≥ g, so p ≥ 2g, which is excluded.
  - A B with exactly one exponent 0 appears at the same level as its endpoint on that side.
  - That endpoint A_e is new at that level. Its other edge has a positive exponent at A_e, since V_e = H_e = 0 would need e ≥ g and e ≤ −g. So that other edge appears strictly later.
  - The far endpoint of B is old, since B's exponent there is positive. So at this level B attaches the new vertex A_e to one old component, and merges no old components.
- *Edges with both exponents ≥ 1.* The edge B_{s+p} between A_s and A_{s+p} has exponents H_s ≥ 1 (iff s ≥ −(g−1)) and V_{s+p} ≥ 1 (iff s+p ≤ g−1). So these are exactly the m−1 edges between consecutive s_j, s_{j+1}: the interior peaks.
  - Each appears strictly after both of its endpoints.
  - G is a path, so each one joins two distinct components of the old graph.
- So the merges at level k are the interior peaks at level k+1. Hence τ = {y − 1 : y interior peak}, and |τ| = m − 1. ∎

*Proof of (B).* Here h_s: A_s → B_{s−N}. Let C be the class-c cone.
- *Truncation step 1.*
  - Let P = {A_s : s < g} ∪ {B_t : t < g}. It is a subcomplex: for s < g, A_s maps to B_s and B_{s−N}, and both indices are < g.
  - The quotient Q = C/P = {A_s, B_s : s ≥ g} has differential D_Q = (v_s, which is the identity since V_s = 0) + (h_s, which lowers the index by N and is present only while s−N ≥ g).
  - On finitely supported chains, the identity plus a part that lowers the index, with indices bounded below, is bijective: invert it by a finite Neumann series. So Q is acyclic and H(C) ≅ H(P).
- *Truncation step 2.*
  - Let P' = {A_s : |s| < g} ∪ {B_t : −g−N < t < g}. It is a subcomplex of P: for |s| < g we have s − N > −g − N.
  - The quotient R_0 = P/P' = {A_s : s ≤ −g} ∪ {B_t : t ≤ −g−N} has differential (h_s, the identity A_s → B_{s−N} since H_s = 0) + (v_s: A_s → B_s, present only while s ≤ −g−N).
  - Relative to the pairing A_s ↔ B_{s−N}, the second part raises the B-index by N, and indices are bounded above. So it is again identity plus nilpotent on finitely supported chains, and R_0 is acyclic. Hence H(C) ≅ H(P').
- *Shape of P'.* The class-c integers in (−g−N, g) are s_1 − N, s_1, …, s_m: s_1 − N ≤ −g < s_1 and s_m < g ≤ s_m + N. So P' is the zigzag
  B_{s_1−N} — A_{s_1} — B_{s_1} — A_{s_2} — ⋯ — A_{s_m} — B_{s_m}.
  Every exponent on it is ≥ 1: V_{s_j} ≥ 1 since s_j ≤ g−1, and H_{s_j} = V_{−s_j} ≥ 1 since −s_j ≤ g−1. The two end B's each have one A-neighbour. Treat them as edges to a "ground" vertex where cochains take the value 0. Then G ∪ {ground} is a single cycle with m+1 edges.
- *Levels.*
  - x(s) = −s(s+N)/(2N) − V_s, and b(t) = −t(t+N)/(2N) = −(u² − N²/4)/(2N), where u = t + N/2.
  - Check: b(s) = x(s) + V_s is immediate. Since H_s = V_s + s, x(s) + H_s = b(s) + s = (−s² − sN + 2sN)/(2N) = −s(s−N)/(2N) = b(s−N), as required.
- *coker part.* coker δ_k = H^1(G_k ∪ ground, ground), which is H^1(G_k ∪ ground) because the ground is one point. This is 0 until the cycle closes, at the maximal peak level M. From then on it is F, and U (restriction of cochains) is an isomorphism. So the coker part is a single tower and contributes nothing to τ.
- *ker part.* ker δ_k is the space of functions on the components of G_k that do not contain ground.
  - A vertex that is new at level k+1 has its edges strictly higher, since all exponents are ≥ 1. So it is isolated at level k+1, and the new edges at level k+1 join only old vertices or ground.
  - Hence dim(ker_k / U·ker_{k+1}) is the number of merges among old components, including merges into the ground component. That number is #(new edges at level k+1) − Δb_1, and b_1 increases (by 1) only at level M.
  - So τ = {y − 1 : y ∈ Π_c} with one copy of M − 1 removed, and |τ| = (m+1) − 1 = m. ∎

### 4d. Divisibility

**Proposition 4.3.** Suppose 2 ≤ |p| ≤ 2g−2 and S^3_p(K) ≅ L # Y'' with L an L-space of order a ≥ 2. Then |p| divides 2g−1.

*Proof.*
- Write 2g−1 = Q·N + r with 0 ≤ r < N. Then Q ≥ 1, since N ≤ 2g−2.
- The integers in [−(g−1), g−1] are 2g−1 consecutive integers. So n_i = Q+1 on a set S of r cyclically consecutive residues, and n_i = Q elsewhere. In particular every n_i ≥ 1.
- By Proposition 4.2, |τ(HF^+(S^3_p(K), i))| equals n_i − 1 if p > 0 and n_i if p < 0. Either way it is a strictly increasing function of n_i.
- By Lemma 4.1 and §4b, |τ| is invariant under i ↦ i+b with b ≢ 0. So S is invariant under translation by b.
- If 0 < r < N, then S is a proper nonempty cyclic interval. It has exactly one start point (x ∈ S with x−1 ∉ S), and a translation preserving S must fix that start point. That is impossible for b ≢ 0.
- So r = 0, i.e. N divides 2g−1. ∎

### 4e. The key contradiction

**Theorem 4.4.** Let K be a nontrivial positive L-space knot of genus g, and p a nonzero integer with |p| ≥ 2, |p| dividing 2g−1 and |p| < 2g−1. Then S^3_p(K) is not homeomorphic to L # Y'' for any L-space L with |H_1(L)| ≥ 2 and any closed oriented 3-manifold Y''.

*Proof.* Let N := |p| and n := (2g−1)/N. Both are odd, N ≥ 3 and n ≥ 3. In particular |p| ≤ (2g−1)/3 ≤ 2g−2, so Proposition 4.2 applies. Suppose such a splitting exists, and let b be as in §4a.

**(i) The comparison.** Let t be the representative of b with 0 < |t| ≤ (N−1)/2; it exists because N is odd and b ≢ 0. By Lemma 4.1 and §4b:

  (★) τ of class 0 and τ of class t agree up to a translation.

**(ii) Arithmetic.**
- For |c| ≤ (N−1)/2, the integers s ≡ c with |s| ≤ g−1 are exactly c + kN for |k| ≤ (n−1)/2. Indeed |c+kN| ≤ (N−1)/2 + (n−1)N/2 = g−1, while |k| = (n+1)/2 gives |c+kN| ≥ (nN+1)/2 > g−1. So m = n in every class.
- *Key fact.* Let u = c + (k+½)N and u' = c + (k'+½)N with k ≠ k'. If u² = u'², then u = −u', so 2c + (k+k'+1)N = 0. Hence N | 2c, so N | c because N is odd, and c = 0. So for c = t, distinct k give distinct values of u², hence distinct levels in both formulas of Proposition 4.2.

**(iii) Case p > 0.**
- *Class 0.* s_j = (j − (n+1)/2)N, so the interior peaks have μ_j = s_j + N/2 = (j − n/2)N for 1 ≤ j ≤ n−1. These are ±N/2, ±3N/2, …, ±(n−2)N/2: nonzero ± pairs. So every element of τ has even multiplicity, and τ is nonempty since n − 1 ≥ 2.
- *Class t.* μ_j = t + (j − (n+1)/2 + ½)N. By (ii) the n−1 levels are distinct.
- A translate of a nonempty multiset in which every multiplicity is even never has all multiplicities equal to 1. This contradicts (★).

**(iv) Case p < 0.**
- *Class 0.* The peaks are t' = kN for k = −(n+1)/2, …, (n−1)/2, so u = t' + N/2 runs over ±N/2, ±3N/2, …, ±nN/2, each value of |u| exactly twice. The maximal level M comes from |u| = N/2. Removing one copy of M − 1 leaves the levels for |u| = 3N/2, …, nN/2 still doubled, and these exist since n ≥ 3. So τ has a repeated element.
- *Class t.* By (ii) the n+1 peak levels are distinct, so the n elements of τ are distinct.
- This contradicts (★). ∎

*Computer checks (made while writing; not part of the proof).*
- For every admissible sequence V with g ≤ 5 (V_{g−1} = 1, steps 0/1, V_g = 0), every N with 2 ≤ N ≤ 2g−2, both signs and every class, an F_2 linear-algebra computation of the level-graded kernel and cokernel reproduced the counts |τ| = n_c − 1 (p > 0) and n_c (p < 0) of Proposition 4.2: 1520 cases, no exception. For p > 0 it used a long window of the untruncated path; for p < 0 it used the truncated zigzag.
- For g ∈ {2, 5, 8}, every such V, every odd N | 2g−1 with 3 ≤ N < 2g−1, both signs and every nonzero class t, the τ multisets of classes 0 and t differed up to translation: 1600 comparisons, no exception.

## 5. Proof of the Theorem

Assume, as in §1, that K is a nontrivial positive L-space knot of genus g, p ≠ 0, and Y = S^3_p(K) has k ≥ 3 prime summands.

1. By Lemma 2.1, Y ≅ A # B with B an integer homology sphere, B ≠ S^3.
2. By Lemma 2.2, Y ≅ L # Y'' with L a lens space (an L-space) of order a ≥ 2. So |p| ≥ 2.
3. K is fibred with fibre of genus g (§0, item 5). Proposition 3.1 gives |p| ≤ g.
   - If g = 1, this contradicts |p| ≥ 2.
   - So g ≥ 2, and 2 ≤ |p| ≤ g ≤ 2g−2.
4. By Proposition 4.3, applied to the splitting of step 2, |p| divides 2g−1. Also |p| < 2g−1.
5. By Theorem 4.4, the splitting of step 2 cannot exist. This is a contradiction.

So S^3_r(K) has at most two prime summands, for every L-space knot K and every slope r. ∎

## 6. By-products

- For a fibred knot, a reducible integral surgery with an integer-homology-sphere summand B ≠ S^3 requires |p| ≤ g (§3). This uses only fibredness.
- Given item 4 of §0, the argument of §5 shows more: a surgery on an L-space knot never has a prime summand that is an integer homology sphere other than S^3. Steps 2–5 use only the homology-sphere summand and the lens summand. This agrees with the known examples, cables at the cabling slope with summands L(a,b) and S^3_{b/a}(J).

---

## Status

**The main claim is proved: every surgery on an L-space knot has at most two prime summands.** The proof is complete *given the cited theorems of §0*. All of them are recalled from memory, and their exact published statements were not checked against the sources.

- The citation recalled with the least certainty is item 4, Gordon–Luecke 1996: a reducible surgery on a nontrivial knot in S^3 has a lens-space summand.
  - The proof needs only the weak form, that some prime summand is an L-space with |H_1| ≥ 2.
  - Without it, Lemma 2.2 would be unsupported, and steps 2–5 of §5 would need another source for such a summand.
  - I recall this as a standard theorem, but this is the dependency a reader should check first.
- The Ozsváth–Szabó surgery formula (item 8) is used as a relatively graded quasi-isomorphism, and is computed from homology-level maps. The justification is given in 8(b). The truncation for p < 0 is carried out explicitly in §4c and not cited.
- Two independent referee passes and a final verification pass during this attempt checked the chain in §§1–5 and found no logical gap. The final pass noted that an earlier draft's derivation of hat-version ranks was loosely justified. In this version that step is replaced: Proposition 4.3 now uses only the plus-version count |τ|, proved in Proposition 4.2. The final pass also noted that the 8(b) justification was terse; it has been expanded.
- Nothing else is open.

## Other routes

- **Chain A (shape theorem).** A different route cites a "shape theorem": a surgery with ≥ 3 summands is L_1 # L_2 # Y_3, with L_1 and L_2 lens spaces and Y_3 an integer homology sphere. Then:
  - for p < 2g−1, the HF^+ comparison of classes forbids an L-space summand of order |p|;
  - so p ≥ 2g−1, which contradicts |p| ≤ g from §3 when g ≥ 2.

  That shape theorem does **not** follow from Howie plus Gordon–Luecke 1996. The missing case is two summands with nontrivial H_1, only one of which is known to be a lens space. Its attribution could not be confirmed from memory. The case can be repaired with the coset-invariance argument of §4a for the lens summand alone, but then the route is essentially the proof above.
- **Perelman-free variant.** See Remark 3.4.
- **Invariants of Y alone cannot work (dead end).** In the configuration p = rs = 2g−1, Y = L_1 # L_2 # Y_3, the formal staircase V = V(T(r,s)) + 1 on [0, g−1] reproduces the following data of S^3_{rs}(T(r,s)) # S^3_{+1}(T(2,3)):
  - its d-invariants, and hence its HF^+;
  - its torsion and Casson–Walker data.

  So Floer or torsion invariants of S^3_p(K) alone cannot rule out three summands at p = 2g−1. The topological cover bound of §3 is what removes that slope range.
- **Lattice route.** Gluing the reversed surgery trace to sharp plumbings bounded by the lens summands gives d(Y_3) ≤ −2 in that configuration, but no contradiction. Routes through fractional Dehn twist coefficients and dual knots produced no closing argument either.
- **Literature.** As I recall, Hom–Lidman–Zufelt ("Reducible surgeries and Heegaard Floer homology", c. 2015) study reducible surgeries on L-space knots with the same conclusion. That recollection is unverified, and the proof above does not rely on it.
