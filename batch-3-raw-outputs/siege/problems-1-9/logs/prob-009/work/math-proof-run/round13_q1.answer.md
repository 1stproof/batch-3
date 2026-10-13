# round13_q1 — attempt on MS11♭

## Status
**PARTIAL. MS11♭ is NOT proved here, and no counterexample is given.**

What this file adds:
1. **Model R (§2), a chart-level model of the reflection case (R-a)/(R-b).** It shows that step 3 of the planner's sketch ("rigid-twin exclusion by side-swap") cannot be completed by reasoning near the branch c̃. I name the inference in step 3 that fails. In the model:
   - the coarse V_t are smooth and t is a submersion;
   - H is smooth;
   - the coarse transported boundary curve is a single unibranch curve;
   - the automorphism a is a reflection of S fixing c̃ pointwise and swapping two Y_0-copies x and y;
   - x is Y-persistent on one anchored sheet T of c̃ and frozen on the other, aT.
2. **Reduction (§1)** of the endpoint failure to the frozen twin, phrased with "value functions" along lift-curves. This is a self-contained re-derivation of facts the run already knows (F2, the rigid twin, round11_q1 §4, round11_q4 §3). It is included only to fix the logic used in §2–§3. It is **not new**.
3. **Remarks on the chain (§3).** I found no new flaw. I record one point about its logical status and one about what a counterexample would require.

Readings: (R1) and (R2) with H_0 = id, exactly as in the task file. The orbifold reading (R2^orb) is **not** used. (Rig) is assumed wherever MS11♭ assumes it, and so is "t ↦ Y_t non-constant".

---

## 1. Value functions along lift-curves; where the failure sits (re-derivation, not new)

Notation is as in the task file. Q ∈ B_0, A = Aut(Q), and Λ is the set of lift-curves. By round12_q6 Lemma G1 (cited), Λ = {gL_1 : g ∈ A}.

**Definition.** For a lift-curve L and a label z that is intact along L near (0,0), put φ_z^L(t) := [F_z(L(t))] ∈ 𝔐 := M_{g_i,n_i}/S_{n_i}. Equivariance (K3) gives φ_z^{gL} = φ_{g^{-1}z}^{L}.

**Lemma 1.1 (dichotomy at generic time).** Let T be a boundary-type anchored sheet with a lift-curve L ⊂ T, and let z be intact along L with F_z(L(0)) ≅ Y_0. Then exactly one of the following holds:
- (a) φ_z^L is constant (z is *frozen* on L);
- (b) z is intact along T and F_z is constant on each T_t. Hence F_z ≡ φ_z^L(t) on T_t, and at t = 0, z is intact along the branch of T_0 with F_z ≡ Y_0.

*Proof.*
- **Generic time.** Fix a generic t and the branch T_t of the transported piece D_t through L(t), where L(t) is a puncture by the boundary-type assumption. Along T_t, one of three things happens to z:
  - (1) z is intact and F_z is constant;
  - (2) z is intact and F_z is non-constant;
  - (3) some edge at z is smoothed.
- **Cases (2) and (3).** Write the lifted piece as K × {c_t} with (G, M, K) ∈ 𝒦 ((Rig) together with Lemma S, cited).
  - In case (2), z is a moving vertex u ∈ M. Its value at the puncture is pr_u(κ) for some κ ∈ K ∩ ∂.
  - In case (3), z lies inside the degeneration of a vertex w of the piece. A constant vertex has value in the interior of M_w and cannot degenerate, so w ∈ M. The value of z is then the value of a component of pr_w(κ), with κ ∈ K ∩ ∂.
  - 𝒦 is finite and each K ∩ ∂ is finite. So in both cases φ_z^L(t) lies in a finite set F that does not depend on t.
- **Conclusion.** If φ_z^L is non-constant, then φ_z^L(t) ∉ F for t outside a discrete set, and case (1) holds for generic t. Intactness and the constancy of F_z on fibres are closed analytic conditions on T, so they hold on all of T. ∎

**Corollary 1.2 (the failure is a frozen twin; known: rigid twin of round11_q1 §4, G2 of round12_q6).** Suppose x is Y-persistent on an anchored sheet of β̃ containing L_1. Suppose further that MS11♭'s conclusion fails for b̃, so that x is not Y-persistent on any anchored sheet of b̃. Then for every lift-curve gL_1 lying in an anchored sheet of b̃:
- φ_x^{gL_1} ≠ Y;
- equivalently, y := g^{-1}x satisfies φ_y^{L_1} ≠ Y.

If x moreover merges or moves along b̃ at t = 0 (the endpoint case), then by Lemma 1.1, φ_y^{L_1} ≡ Y_0: y is a *frozen* Y_0-copy at Q_t for all t.

**Counting remark (coarse).** Fix a generic t. Every constant vertex with value Y_t of a piece D_t through the puncture Q_t gives a distinct component of Q_t isomorphic to Y_t. By Lemma 1.1, applied with φ = Y non-constant, every such component of Q_t is in turn a constant vertex along every branch of every piece with puncture Q_t. Consequently:
- the number n_Y(D) of constant Y_t-vertices of D_t is the same for all pieces D having Q as a puncture;
- the set 𝒩 of pieces with n_Y ≥ 1 is closed under puncture transitions. This is the coarse form of round11_q4 §3.

So "the Y-copy survives the transition" is automatic at the coarse level. The whole difficulty is *which label* carries it. That is exactly the twin issue.

---

## 2. Model R: the reflection case is consistent locally (new; refutes step 3 of the planner's sketch as a local argument)

**Setting of the model.** We work near a generic point p of a lifted branch c̃ ⊂ S, at which Stab_A(p) = ⟨a⟩ with a of order 2.
- The stratum of c has, among others, vertices x and y. Each carries one edge, e at x and e′ = ae at y, both joining it to the rest of the graph.
- To keep the bookkeeping minimal, take dim M_{g_i,n_i} = 1 (e.g. (g_i,n_i) = (0,4) or (1,1)). Let z_x, z_y be local coordinates of the moduli of the components x, y, centred at Y_0. Let s, s′ be the plumbing coordinates of e, e′, and let k be a coordinate along the moving part K of the piece. All other chart coordinates are set equal to fixed holomorphic functions of (k, w, t) below; they play no role.
- The automorphism a acts by (k, z_x, z_y, s, s′) ↦ (k, z_y, z_x, s′, s). This is a linear action of the shape a chart automorphism exchanging x ↔ y and e ↔ e′ has (taking the root-of-unity factors on the plumbing coordinates to be 1).
- Let φ be holomorphic on Δ with φ(0) = 0 and φ ≢ 0. φ(t) stands for the coordinate of Y_t, so Y is non-constant.

**The 3-fold.** Let X ⊂ Def × Δ be the image of the embedding
 (k, w, t) ↦ ( k, z_x = (w + φ(t))/2, z_y = (φ(t) − w)/2, s = s′ = w² − φ(t)², t ).
It is an embedding because w = z_x − z_y and t is a coordinate.

**Checks.**
1. *X is a smooth irreducible 3-fold and is a-invariant.* In the parameters, a acts by (k, w, t) ↦ (k, −w, t): it swaps z_x and z_y and fixes s = s′.
2. *Central fibre.* S := X ∩ {t = 0} = {(k, w/2, −w/2, w², w²)}. This is a smooth surface. Its boundary locus {s s′ = 0} is {w = 0}, which is the lifted branch c̃ = {(k, 0, 0, 0, 0)}. Along c̃, x and y are intact and both are ≅ Y_0. The element a acts on S by w ↦ −w: a **reflection of S fixing c̃ pointwise**. This is the configuration of (R-a)/(R-b) and of step 3 of the sketch.
3. *Fibre at t ≠ 0.* The boundary is {w = ±φ(t)}, which consists of two curves:
   - T_t = {(k, φ(t), 0, 0, 0)};
   - aT_t = {(k, 0, φ(t), 0, 0)}.

   On T_t, F_x ≅ Y_t and F_y ≡ Y_0: x is Y-persistent and y is frozen. On aT_t the roles are exchanged. The sets T := ⋃_t T_t and aT are irreducible (parametrised by (k, t)) and contain c̃ × {0}. So they are two distinct anchored sheets of c̃, with P(T) ∋ x, P(aT) ∋ y = ax, x ∉ P(aT). This is a (β)-twist by an element of Stab_pt(c̃) that is a reflection of S.
4. *Coarse picture.* Near q(p) the coarse space is the quotient by ⟨a⟩. The invariant W := w² gives coarse coordinates (k, W, t) on X/⟨a⟩.
   - The coarse 𝒳 is smooth and t is a submersion.
   - Each coarse V_t = {(k, W)} is a smooth surface.
   - The coarse boundary of V_t is the single smooth curve {W = φ(t)²}.
   - Hence H_t(k, W) := (k, W + φ(t)²) is a smooth stratum-preserving trivialisation, with H_0 = id. So (R1), (R2), (i), (ii) hold locally.
   - The transported piece has the (Rig) shape K × {c_t}, with constant values c_t[x] = φ(t), c_t[y] = 0.
5. *Total geodesy is not violated locally.* At t = 0 the smooth curves at (k, ±w) are identified by a. This is exactly the situation of V_0 near a boundary branch along which the boundary curves, but not the nearby smooth curves, carry the extra automorphism a. Nothing in the chart constrains the t-direction.

**Where step 3 of the planner's sketch fails.** Step 3 argues as follows:
- the two copies x, y "appear as limits of the same family of subsurfaces approached from the two sides of c̃";
- "the two sides of c̃ in S are glued by H_t continuously";
- "so the side-swap should force φ(t) and Y_0 to be values of the same constant vertex along a connected family", contradicting Theorem N at generic t.

Model R satisfies every premise, and the conclusion does not follow:
- H_t glues *coarse* points. Coarsely there is one side: the invariant W = w² is a single coordinate, and w and −w give the same coarse point. The coarse transported curve {W = φ(t)²} is a single unibranch curve with constant vertex values {φ(t), Y_0} as an unordered pair. That is perfectly consistent.
- In the chart, the label x takes the value φ(t) on T and Y_0 on aT. The only connected set containing both is T ∪ aT. Its two halves meet only in {t = 0}, where φ(0) = Y_0, so continuity of the value of x is not violated.
- For each fixed generic t, T_t and aT_t are disjoint curves near p. Theorem N, or the generic-time trichotomy, is applied at fixed t, so it sees two separate branches, each with constant vertices. There is no merge and no move.

So step 3 does not give a contradiction from data near c̃. Together with the earlier chart models at Q itself (round11_q7 §6, round11_q1 §5, round11_q2 §1.2, round12_q6 Model G3′, all cited, not re-checked), this shows the following. **The reflection mechanism must be combined with genuinely global information about the piece c, or about V_0, that is not visible near c̃.**

**What global information would be needed (not proved).** In the reflection case at t = 0:
- the generic curve of the piece c carries a, which swaps two constant Y_0-vertices;
- the lifted family Ê of c (an irreducible 2-dimensional analytic set proper over Δ, PR-D Lemma R0, cited) and its image αÊ under the induced graph automorphism α are distinct;
- Ê and αÊ meet along the α-invariant central fibre K × {c_0}.

A contradiction would need a global reason why Ê must be α-invariant, i.e. why the lifted piece family cannot split. One candidate would be that c_t must keep the automorphism a. Under the coarse reading (R2) I see no such reason. Under (R2^orb) it is automatic, which matches the run's result that MS11♭ holds under (R2^orb).

---

## 3. Remarks on the chain and on the logical status

- I re-read chain steps 1–2(d) as quoted in the task. I found no new flaw beyond what the run already records. I did not re-audit the cited entries.
- The derivation of the problem's claim needs **both** MS11♭ and (Rig) (entry 82). Since (Rig) is still open, a proof of MS11♭ alone would not prove the problem's claim. This is consistent with the task's wording; I record it only to keep the status clear.
- **On counterexamples.** A counterexample to MS11♭ would need an actual non-trivial holomorphic deformation V_t of a smooth, closed, totally geodesic surface V_0 ⊂ M_g that satisfies (R1), (R2). I know of no smooth totally geodesic surface admitting any non-trivial deformation as a subvariety of M_g (cited from memory, as an expectation rather than a theorem). If such surfaces are rigid as subvarieties, MS11♭ and the problem hold vacuously, and an explicit counterexample is out of reach. For this reason I did not pursue the counterexample route beyond chart-level models.

---

## 4. Proved / not proved / open

**Proved here** (under (R1), (R2), (Rig), Y non-constant, with the cited lemmas taken as inputs):
- Lemma 1.1 and Corollary 1.2, and the counting remark. These are re-derivations of known run facts in a uniform "value-function" form, **not new**.
- Model R: a chart-level model of the reflection case in which:
  - coarse V_t is smooth and H is smooth;
  - a reflection a of S fixes c̃ pointwise and swaps two Y_0-copies;
  - the anchored sheets T ≠ aT of c̃ carry a Y-persistent x and a frozen y, respectively.

  Consequently, step 3 of the planner's sketch fails as a local argument, at the inference "glued by H_t ⇒ same constant vertex along a connected family".

**Not proved:**
- MS11♭;
- (NRT);
- exclusion of (R-a), (R-b) or (γ°);
- MS8, and therefore the problem's claim.

**Open:**
- (O1) MS11♭ itself, or equivalently, under (Rig), the problem's claim under the coarse reading (R2).
- (O2) A global reason why the lifted piece family Ê of a piece whose generic curve has an automorphism swapping two constant Y_0-vertices must be α-invariant. This is the global input that step 3 of the sketch would need.
- (O3) (Rig) (entry 82).
- (O4) Whether smooth totally geodesic surfaces in M_g admit any non-trivial deformations as subvarieties (rigidity). A positive rigidity theorem would make the problem vacuous.

=== END OF ANSWER round13_q1 ===
