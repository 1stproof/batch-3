# round13_q3: attempt on MS11♭ (rigid-twin / reflection case)

**Status line.** PARTIAL. I do not prove MS11♭ and I do not give a global counterexample. I read only the task part of the brief, the chain, and the round-12 file round12_q7 (Φ-persistence, Lemma 1.2, Prop. 2.1, Lemma 4.1). I did not re-read the rest of the 5000-line prior-results file.

What this file contains:
- (§1) Step 3 of the planner's sketch ("the two sides of c̃ are swapped by the reflection, so φ(t) and Y_0 are forced onto one constant vertex") does not work. In a complex surface a complex curve has no two sides. More importantly, there is an explicit **local model near a generic point of the piece c**, not only near Q. In it the reflection case with a rigid twin occurs, and it is compatible with (R1) and (R2) in the chart. So step 3 cannot be proved by any argument that is local along c.
- (§2) A new proved necessary condition (Lemma FC), under a smoothness hypothesis on the 3-fold component. In a reflection-type failure, one of two things happens. Either there is a third anchored sheet of c̃ fixed pointwise by σ, on which x and y have equal value functions. Or, for every small t ≠ 0, V_t contains a holomorphic curve of smooth curves admitting the automorphism σ, and these curves converge to c as t → 0. In words: the automorphism that is "lost" on the boundary reappears on interior curves of V_t.
- (§3) Chain check. I found no new flaw. I re-state the dependence on (Rig).
- (§4) Proved / not proved / open.

Readings (R1), (R2), and all the definitions (pieces, Def(Q), labels, anchored sheets, Φ, rigid copies), are those of the task file.

---

## 1. The planner's step 3 fails: a local model of a reflection with a rigid twin near a generic point of c

### 1.1 Two corrections to the picture in step 3
- c̃ is a complex curve in the complex surface germ S, so S ∖ c̃ is connected near any point of c̃: a punctured disc bundle has no "two sides".
  - A finite-order σ ∈ Stab_pt(c̃) acting non-trivially on a smooth local branch S_1 ⊃ c̃ is linearised (Cartan) as (u, w) ↦ (u, ζw), with ζ ≠ 1 a root of unity. Here c̃ = {w = 0}.
  - "Approaching from the two sides" should therefore read: the subsurface Σ_x of the curve at (u, w) is carried by σ to the subsurface Σ_y of the curve at (u, ζw), which is the same coarse point.
- Hence the right question is: does the monodromy "x ↦ y" of the small coarse loop around c in V_0 survive in V_t? The model below shows that it need not survive near c_t. What it does force is an interior orbifold point (§2).

### 1.2 The model
Setting at a generic point p ∈ c̃, p ≠ 0. Assumptions on the curve P at p:
- P has two components x, y ≅ Y_0 (dim M_{g_i,n_i} = d > 0). Each is attached by one node, e = (x, r_1) and σe = (y, r_2), to a component R.
- There is an automorphism σ of P of order 2. It swaps x and y, preserves R, and swaps r_1 and r_2.
- The moving part of c lies in the remaining coordinates and keeps σ. That is, the curves of c all admit σ, as they must for σ ∈ Stab_pt(c̃).

Coordinates on Def(P):
- z_x, z_y ∈ C^d: local moduli coordinates of the two components, chosen σ-equivariantly, so that σ*z_y = z_x.
- s_e, s_{σe}: plumbing parameters, with node coordinates chosen σ-equivariantly (possible because σ² = id), so that s_{σe}∘σ = s_e.
- u: the remaining coordinates (the moving part; σ acts trivially on the u-locus used).
- All further edges are treated like e, σe below; I suppress them.

Define X ⊂ Def(P) × Δ as the image of (u, w, t) ↦ point with
- s_e = s_{σe} = w(w − t);
- z_x = Y_0 + a(t − w), z_y = Y_0 + a·w, where a ∈ C^d ∖ {0} is fixed;
- remaining coordinates K(u).

Checks:
1. **σ-invariance.** σ(u, w, t) = (u, t − w, t). Indeed, s_e and s_{σe} are both invariant under w ↦ t − w, and z_x(u, t − w, t) = Y_0 + a·w = z_y(u, w, t). So σ(X_t) = X_t for each t.
2. **t = 0.** S := X_0 is given by s_e = s_{σe} = w², z_x = Y_0 − a w, z_y = Y_0 + a w. Along c̃ = {w = 0}, both x and y are intact, constant, ≅ Y_0. σ fixes c̃ pointwise and acts on S by w ↦ −w. This is the **reflection case (R-a)**.
3. **Boundary at time t.** N = 0 on X_t exactly on T_t = {w = 0} and σT_t = {w = t}.
   - T := {w = 0}: x is intact with value φ(t) = Y_0 + a t (non-constant), and y is intact with value ≡ Y_0.
   - σT = {w = t}: x is intact with value ≡ Y_0, so x is **rigid** there.
   - Both T and σT contain c̃ × {0}, so both are anchored sheets of c̃. This is exactly the rigid-twin (β)-edge of round12_q7 Prop. 2.1(3), second alternative.
4. **(R1), (R2) in the chart.** Assume Aut(P) = ⟨σ⟩. Then the coarse germ of closure(V_t) at c_t is X_t/⟨σ⟩, with coordinates (u, v), v = (w − t/2)².
   - The coarse boundary is {v = t²/4}. At t = 0, the coarse V_0 is {(u, v)}, v = w², with boundary {v = 0}.
   - H_t(u, v) := (u, v + t²/4) is a homeomorphism, smooth (indeed holomorphic) in (u, v, t). It preserves the open stratum and the boundary stratum, and H_0 = id.
   - The coarse 𝒱 is the smooth 3-fold {(u, v, t)}. So the chart-level content of (R1), (R2) holds.
5. **Where the swap went.** For t ≠ 0, σ fixes the interior curve {w = t/2} of X_t. There N = s_e s_{σe} ≠ 0, s_e = −t²/4, and z_x = z_y = Y_0 + a t/2. These are smooth curves of V_t with the extra automorphism σ. They converge to c as t → 0.
   - The coarse loop around c in V_0 has monodromy x ↦ y. At time t, a small loop around c_t has no swap. A loop of the original size encloses the orbifold point v = 0 and does have the swap.
   - Nothing forces φ(t) = Y_0: the values agree only at the σ-fixed interior curve, where both equal Y_0 + a t/2.

**Conclusion of §1.** The mechanism proposed in step 3 does not hold in this model. The reflection σ, a non-constant Φ-copy x on T and a rigid copy on σT all coexist, near a generic point of c, with (R1) and (R2) satisfied in the chart. Any proof of (R-a) must therefore use information that is global along c or global on V_0: total geodesy, the global walk, or the behaviour at the punctures of c.
- Total geodesy of S at t = 0 is not tested by the model. I give no argument that this S can be totally geodesic, nor that it cannot. A proof of (R-a) through total geodesy would have to exclude an S of exactly this shape: the reflection w ↦ −w, with z_x − z_y vanishing to first order along c̃.

## 2. Lemma FC: the lost automorphism reappears on interior curves of V_t

**Lemma FC (fixed-curve dichotomy).** Let c̃ be a lifted branch of a piece c, p ∈ c̃ ∖ {0} a point, and σ ∈ Stab_pt(c̃). Let X be an irreducible component of q^{-1}(closure 𝒱) ∩ (B × Δ_ε) through (p, 0). Assume:
- (a) near (p, 0), X is a complex manifold, t|_X is a submersion, and X ∩ {t = 0} = S_1 is a smooth local branch at p of the t = 0 sheet;
- (b) σ(X) = X and σ|_{S_1} ≠ id (the reflection case).

Then Fix(σ) ∩ X =: Ψ is, near (p, 0), a 2-dimensional complex submanifold with Ψ ∩ {t = 0} = c̃ and t|_Ψ a submersion. Moreover exactly one of the following holds:
- (FC1) Ψ ⊂ {N = 0}. Then Ψ is a 2-dimensional germ of X ∩ {N = 0} containing c̃ × {0}, fixed pointwise by σ. At every point of Ψ, F_y ≅ F_{σy} for every label y. In particular, if σ swaps x and y, then x and y have the same value function on Ψ.
- (FC2) For every small t ≠ 0, the curve Ψ_t := Ψ ∩ {t} contains points r with N(r) ≠ 0. Each such r is a smooth curve of V_t (after applying q) admitting the automorphism induced by σ. As t → 0 these curves converge to c.

*Proof.*
1. σ ∈ Aut(Q) acts on B × Δ_ε as σ_B × id, so t∘σ = t, and σ preserves X and each X_t. Since X is a manifold and σ has finite order, Cartan's linearisation theorem applies at the fixed point (p, 0). So Fix(σ|_X) is a submanifold whose tangent space is the eigenvalue-1 space E of dσ on T := T_{(p,0)}X (dim 3).
2. σ preserves X_0 = S_1, so dσ preserves T S_1 = ker(dt|_T). This is 2-dimensional, because t|_X is a submersion and X_0 = S_1 is smooth. On T S_1:
   - dσ fixes T c̃, since σ fixes c̃ pointwise;
   - dσ ≠ id, since σ|_{S_1} has finite order and is not the identity, and by Cartan a finite-order map with identity differential at a fixed point is the identity near it. So the eigenvalues on T S_1 are 1 and ζ ≠ 1.
3. On T/T S_1 ≅ C (via dt), σ acts trivially, because t∘σ = t. As dσ is diagonalisable (finite order), its eigenvalues on T are 1, ζ, 1. So dim E = 2, and E ⊄ T S_1, i.e. dt|_E ≠ 0.
4. Hence Ψ is a 2-dimensional submanifold and t|_Ψ is a submersion. Ψ_0 = Fix(σ|_{S_1}) is a 1-dimensional submanifold of S_1 containing c̃, so it equals c̃ near p.
5. Ψ is a connected manifold germ, hence irreducible. So either Ψ ⊂ {N = 0}, which is (FC1), or Ψ ∩ {N = 0} is a proper analytic subset of dimension ≤ 1.
6. In the second case, the components of the 1-dimensional germ (Ψ ∩ {N = 0}, (p, 0)) are c̃ × {0} and curves on which t is non-constant: a curve inside {t = 0} lies in Ψ_0 = c̃. So for small t ≠ 0, Ψ_t ∩ {N = 0} is finite while Ψ_t is a curve. The other points r of Ψ_t lie in q^{-1}(V_t), because H preserves the open stratum and X ∩ {N ≠ 0} lies over 𝒱. Since σ(r) = r with σ ∈ Aut(Q), σ induces an automorphism of the curve at r.
7. As t → 0, Ψ_t → Ψ_0 = c̃, so q(r) → c.
8. In case (FC1), σ fixes each point r of Ψ. Then σ induces an automorphism of the curve at r that maps the component labelled y to the one labelled σy, by (K3) of the brief. So F_y(r) ≅ F_{σy}(r). ∎

**Consequences for MS11♭.**
- In a reflection-type rigid-twin failure that satisfies (a) and (b), alternative (FC1) produces a third anchored sheet Ψ of c̃. On Ψ the Φ-copy and the rigid copy have the **same** value function, so it is either in Φ or ≡ Y_0.
  - If it is in Φ, then x is Φ-persistent on Ψ, by round12_q7 Lemma 1.2 applied on Ψ. Then x survives the twist at c̃ in the Φ-sense, *provided* Ψ is reachable in the sheet graph from the x-carrying sheet. I could not prove that reachability.
- Alternative (FC2) is what happens in the model of §1. It gives a new **necessary condition** for a counterexample:
  - *(NC-Fix) V_t (t ≠ 0 small) contains a holomorphic curve of smooth curves with an automorphism exchanging the Y_0-subsurfaces Σ_x and Σ_y, and this curve tends to the boundary piece c as t → 0. On these curves F_x ≅ F_y.*
  - (NC-Fix) is not contradictory by itself. V_t is not totally geodesic, and nothing in (R1) and (R2) forbids V_t from meeting the σ-symmetric locus of M_g in a curve that degenerates into c. By the upper semicontinuity of fibre dimension, the analytic set closure(𝒱) ∩ (closure(M_g^σ) × Δ) may have fibre c at t = 0 and an interior curve at t ≠ 0.
- Hypothesis (a) is a genuine restriction. It fails, for example, if X_0 is non-reduced or contains S_1 together with other sheets at p. So Lemma FC covers only part of (R-a), and **this section is partial by the task's own criteria**.

## 3. Chain check
- I re-read the chain steps 1, 2(a)–(d) as stated in the brief. Within the scope of what I read I found no new flaw.
- The logical dependence is unchanged.
  - Step 1 uses (Rig) (entry 82), which is open and does not follow from MS11♭. So even a full proof of MS11♭ would leave (Rig) open, and the problem would still not be settled.
  - The Φ-version of the chain (round12_q7 §3) still has the unchecked substitutions: Lemma PT, Lemma J / Cor. J′, and the transfer along D^{m+1}. I did not check them.
- The model of §1 is local at a generic point of a piece. So it is **not** a counterexample to MS11♭: MS11♭ concerns a puncture Q with conditions (P) and (S), and the global hypotheses (total geodesy, smoothness of V_0, Y non-constant). It shows only that the rigid-twin twist can occur in the middle of a piece, and so must be excluded by global arguments if it is to be excluded at all.
- Remark (orientation only, not proved). The monodromy picture of §1.1 explains why the orbifold reading (R2^orb) helps. A failure needs the swap monodromy of a coarse loop around c to be realised, at time t, by an interior orbifold point, i.e. alternative (FC2). Under the coarse reading (R2) nothing forbids this. That is consistent with the brief's record that MS11♭ holds under (R2^orb) but is open under (R2).

## 4. Proved / not proved / open

**Proved:**
- §1: an explicit chart-level model in which the reflection case (R-a) and the rigid-twin (β)-edge occur near a generic point of c, compatible with (R1) and (R2) in the chart.
  - Hence step 3 of the planner's sketch, as a local mechanism, is false.
  - The model leaves open whether its t = 0 sheet can be totally geodesic.
- §2, Lemma FC (under hypotheses (a), (b)): the dichotomy (FC1) / (FC2), and the necessary condition (NC-Fix) for reflection-type failures in case (FC2).

**Not proved:**
- MS11♭ in general, or even in the reflection case (R-a).
- The reachability in the sheet graph of the σ-fixed sheet Ψ in case (FC1).
- The Φ-chain substitutions (unchanged from round12_q7).

**Open (named):**
- (R-a) as a global statement. One must exclude, using total geodesy of V_0 or the global walk, a reflection σ ∈ Stab_pt(c̃) together with a rigid twin. By §1, no argument local along c can do this.
- Whether a totally geodesic S can have the shape of §1 at t = 0: a reflection w ↦ −w with z_x − z_y vanishing to first order on c̃.
- (NC-Fix): can a smooth totally geodesic V_0 admit a deformation satisfying (R1) and (R2) in which interior σ-symmetric curves of V_t degenerate onto c? A negative answer, or exclusion of (FC2) by any means, together with the reachability needed in (FC1), would settle (R-a) under hypothesis (a).
- (Rig) (entry 82), as before.

=== END OF ANSWER round13_q3 ===
