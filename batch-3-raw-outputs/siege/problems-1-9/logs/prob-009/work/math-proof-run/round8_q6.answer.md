# round8_q6 — the crossing step (CR) of MS8

**Plan / status line.** (CR) is **not proved**, and **no counterexample** is given. This file proves the following:
- **(A) Proposition 1**, a corrected (CR1). At all but countably many t, every IMOV event belongs to one of three residual types:
  - pure crossing;
  - "shared crossing" — this type only occurs when D is in the same stratum as E, a case the planner's (CR1) misses;
  - "same-branch twin" — only if one reads "crossing" loosely.
- **(B) Proposition 2**, a persistence dichotomy. Assume (Rig) and that Y is non-constant. Then either the IMOV times are countable, or a residual IMOV configuration persists along an analytic sheet that is finite and surjective over Δ.
- **(C) Corollary 3.** (CR) follows from a statement **(PC) about V_0 alone**: there is no "persistent residual crossing" at t = 0. (PC) is open.
- **Section 4** explains why the named approach (Minsky product regions, Antonakoudis, uniqueness of Teichmüller discs, area localisation) does not prove (PC) as it stands. The asymptotic metric at a pure crossing is a sup-product. Sup-products of the factor Teichmüller spaces contain isometric bidiscs, so the contradiction cannot come from the limit object. It would need quantitative (second-order) control.

Readings (R1), (R2) and the definitions of the task (pieces, M(E), K(E), puncture, F, (Rig)) are used throughout. H_0 = id.

**Conventions.**
- "Countable" sets of times are the exceptional sets.
- PR-A gives that t ↦ Y_t is holomorphic. If it is non-constant, then for any finite (or countable) set Ψ of classes in M_{g_i,n_i}/S_{n_i}, the set {t : [Y_t] ∈ Ψ} is countable. Indeed, each fibre of the non-constant holomorphic map t ↦ [Y_t] into the analytic space M_{g_i,n_i}/S_{n_i} is discrete.
- Results cited from the run (L1′, Lemma C2, R7-1 Lemma 1, R7-4 Lemma 2) are used as stated there. I re-checked only the parts I use, as indicated.

---

## 1. The finite sets supplied by (Rig)

Let 𝒦 be the finite set of (Rig).
- For (G, M, K) ∈ 𝒦, put ∂K := K ∩ ∂(∏_{u∈M} M̄_u). The curve K is irreducible, compact and not contained in the closed analytic set ∂(∏M̄_u), so ∂K is finite.
- Let 𝔉 be the finite set of all pairs (smooth irreducible component of some coordinate f_u of a point of ∂K, together with its special points). This ranges over all triples in 𝒦, all u ∈ M, and all Aut(G)-relabellings, and is taken modulo relabelling of special points.

**Lemma 1.1 (puncture values).** Let E be a piece at time t, p ∈ Ē a puncture, and v ∈ M(E). Every irreducible component of f_v(p), with the special points it has as a component of f_v(p), lies in 𝔉.

*Proof.*
- Constant vertices take values in M_w, so pr_{M(E)}ν(p) ∈ ∂(∏_{u∈M(E)} M̄_u).
- pr_{M(E)}ν(p) also lies in K(E), so it lies in ∂K(E).
- (G, M(E), K(E)) ∈ 𝒦 up to Aut(G). ∎

**Lemma 1.2 (a coordinate pinned ⇒ Y_t pinned).** Let E be a piece at time t and x, y ∈ M(E). Suppose e ∈ E satisfies [pr_y(e)] ∈ Ψ for a finite set Ψ. Then [pr_x(e)] lies in a finite set Ψ′ that depends only on Ψ and 𝒦, not on t or E.

*Proof.*
- pr_{M(E)}(e) ∈ K(E), and pr_y is non-constant on the irreducible compact curve K(E), because y ∈ M(E).
- So pr_y^{-1}(Ψ) ∩ K(E) is finite. Take Ψ′ to be the union of its x-projections over the finitely many triples of 𝒦 and their relabellings. ∎

---

## 2. Proposition 1 (corrected CR1)

Fix t and an IMOV event (Q, E, x, D) as in the task. Choose a lift q ∈ Def(Q) and lifted branches ẽ, d̃ through q of ξ(E) and of ξ(D) (compare R7-4 Lemma 2(b) at fixed t). Vertices of G′ = G_Q are the chart labels. For y ∈ V(G′), comp_y(q) is the y-component of Q, a smooth curve with special points labelled by the half-edges at y. Along ẽ every label is intact. Since Q is an interior point of E, the M(E)-coordinates of the point of E over q are (comp_y(q))_{y∈M(E)}.

**Proposition 1.** Assume (Rig) and Y non-constant. There is a countable set Z_1 ⊂ Δ with the following property. For t ∉ Z_1, every IMOV event (Q, E, x, D) at time t is of one of the following types.
- **(P) pure crossing.** Every y ∈ M(E) is intact along d̃ and comp_y is constant along d̃. (D is either coarser, with Q a puncture of D, or in the same stratum on a different coarse branch.)
- **(S) shared crossing.** D is in the same stratum G′ on a different coarse branch. The set M_∩ := M(E) ∩ M(D) is nonempty, and the curves pr_{M_∩}(K(E)) and pr_{M_∩}(K(D)) coincide. Every y ∈ M(E) \ M_∩ (including x) is intact and constant along D.
- **(T) same-branch twin.** ξ(D) and ξ(E) have the same coarse branch b at Q, and d̃ = a^{-1}ẽ for some a ∈ Aut(Q) with ax ≠ x. Then along ẽ the label x moves and the label ax is constant, and comp_{ax}(q) ≅ comp_x(q) ≅ Y_t.
  - This type only arises if "crossing E at Q" in the task's definition is read to allow the same coarse branch. Under the literal reading ("crossing" = different branch) it does not occur.

*Proof.*

**Case 1: D is coarser** (U := unpinched set of d̃ ≠ ∅; Q is a puncture p of D). Let y ∈ M(E) \ {x}.
- *y is merged along d̃* (some edge at y lies in U).
  - The vertex v of G = G′/U containing y is non-constant on D (PR-C Lemma C2).
  - comp_y(q), with its special points, is an irreducible component of f_v(p) (R7-1 Lemma 1(a), R7-4 Lemma 1 step 3). So [comp_y(q)] ∈ 𝔉 by Lemma 1.1.
- *y is intact and non-constant along d̃.* Then f_y(p) = comp_y(q) (R7-1 Lemma 1(b)), which lies in 𝔉.
- In both sub-cases, Lemma 1.2 with Ψ = 𝔉 gives [Y_t] = [comp_x(q)] ∈ 𝔉′, a finite set. This happens only for t in the countable set Z_1^a := {t : [Y_t] ∈ 𝔉′}.
- Otherwise every y ∈ M(E) is intact and constant along d̃ (for y = x this is part of the definition). This is (P).

**Case 2: D is in the same stratum, on a different coarse branch.** All labels are intact along both branches. Let y ∈ M(E) \ {x} be non-constant along D, so y ∈ M_∩ := M(E) ∩ M(D).
- The point c := (comp_y(q))_{y∈M_∩} lies on both C_E := pr_{M_∩}K(E) and C_D := pr_{M_∩}K(D). Both are irreducible compact curves, because y is non-constant on both K's.
- If C_E ≠ C_D, then C_E ∩ C_D is finite. There are only finitely many such pairs (𝒦 is finite; include relabellings). Lemma 1.2, applied with y ∈ M_∩, gives [Y_t] in a finite set 𝔊′. This happens only for t in the countable set Z_1^b.
- Otherwise we are in (S), or in (P) if M_∩ = ∅.

**Case 3: same coarse branch.**
- The lifts of the irreducible germ b at q are permuted transitively by Stab(q) = Aut(Q) (R7-1 §3, Step 3). So d̃ = a^{-1}ẽ for some a ∈ Aut(Q).
- For p ∈ d̃ we have ap ∈ ẽ and comp_y(p) ≅ comp_{ay}(ap) (K3 of R7-3). So comp_x constant along d̃ is equivalent to comp_{ax} constant along ẽ. Since comp_x is non-constant along ẽ, ax ≠ x.
- At q = aq (a ∈ Stab(q)): comp_{ax}(q) ≅ comp_x(q). This is (T).

Put Z_1 := Z_1^a ∪ Z_1^b. ∎

**Correction to the planner's (CR1).** In the same-stratum case the reduction does not give "every vertex of M(E) constant along D". A vertex y ∈ M(E) that also moves along D is pinned only if its two image curves differ. Type (S) is the residue.

---

## 3. Proposition 2 (persistence) and Corollary 3 (reduction to t = 0)

### 3.1 The potential IMOV points form finitely many holomorphic sheets

Let F_0 ⊂ B_0 be the set of points Q_0 that satisfy at least one of the following:
- (a) Q_0 lies on ≥ 2 local branches of B_0;
- (b) Q_0 ∈ closure(ξ(D_0)) \ ξ(D_0) for some 1-dimensional piece D_0;
- (c) Q_0 is an isolated point of B_0 ∩ Δ_{G}, where Δ_G is its stratum.

F_0 is finite: B_0 is a compact 1-dimensional analytic set (R7-1 Lemma 4), and each condition singles out finitely many points.

**Lemma 3.1.** Let Q_0 ∈ F_0. Then the following hold.
- (i) For every t the conditions (a), (b), (c) hold at Q_t := H_t(Q_0) for B_t exactly when they hold at Q_0. Conversely, every point of B_t satisfying (a), (b) or (c) is of the form H_t(Q_0) with Q_0 ∈ F_0.
- (ii) t ↦ Q_t is a holomorphic map Δ → M̄_g.

*Proof.*
- **(i).**
  - H_t is a stratum-preserving homeomorphism B_0 → B_t ((R2)).
  - The number of local branches of a curve germ is a topological invariant: it is the number of components of the link.
  - Closures are preserved, and isolatedness within a stratum is preserved.
- **(ii), the curve Λ_{Q_0}.** Let G′ be the stratum of Q_0. Put Λ_{Q_0} := {(Q_t, t)} ⊂ A_{G′} := closure(𝒱) ∩ (Δ_{G′} × Δ).
  - The set Λ_{F_0} := ∪_{Q_0∈F_0∩Δ_{G′}} Λ_{Q_0} is closed in A_{G′}, and it is contained in a closed analytic subset Σ of A_{G′} of dimension ≤ 1. Take Σ to be the union of three sets:
    - Sing(A_{G′}) ∪ Crit(t|_{Reg A_{G′}}), which contains every point where the fibre of t has ≥ 2 branches or is 0-dimensional. At a regular point where t is a submersion, the fibre is a smooth curve.
    - The sets closure(A_{G}) ∩ (Δ_{G′} × Δ) for strata G strictly coarser than G′ other than M_g. These are analytic by (R1). By (R2) they equal H((closure(C_G) ∩ Δ_{G′}) × Δ), with C_G = closure(V_0) ∩ Δ_G of dimension ≤ 1. So they are finite over each t.
    - The 0-dimensional parts of the fibres, which are already contained in the first set.
  - Σ has dimension ≤ 1. It is a proper analytic subset of the pure 2-dimensional A_{G′}, because A_{G′} ≅ C × Δ is 4-dimensional at points of 1-dimensional pieces.
  - Λ_{Q_0} is closed in Σ and homeomorphic to Δ. At a regular point of Σ, a real 2-dimensional topological manifold inside the real 2-manifold Reg Σ is open, by invariance of domain. So Λ_{Q_0} ∩ Reg Σ is open and closed in Reg Σ. Hence Λ_{Q_0} is a finite union of irreducible components of Σ. Being homeomorphic to Δ, it is a single irreducible analytic curve, and t restricted to it is a homeomorphism onto Δ.
- **(ii), holomorphy.** Let n : Λ̃ → Λ_{Q_0} be the normalization. Then t ∘ n is a holomorphic bijection of Riemann surfaces onto Δ, hence biholomorphic. So t ↦ Q_t = n((t∘n)^{-1}(t)) is holomorphic. ∎

**Consequence.**
- In cases (P) with D coarser, (P)/(S) with D in the same stratum on a different branch, and Case 1 generally: Q satisfies (a) or (b). So Q = Q_t = H_t(Q_0) with Q_0 ∈ F_0, and Q_t moves holomorphically.
- For type (T) see §3.3.

### 3.2 The dichotomy (crossing types)

**Combinatorial data.** Fix Q_0 ∈ F_0 with stratum G′, and branches β_E, β_D of B_0 at Q_0. Then H_t(β_E) and H_t(β_D) are branches at Q_t, in the same strata as β_E, β_D. Fix also a 2-dimensional irreducible component W of the lifted family 𝓦_{G′} (R7-5 (P2), (P4)), and a vertex x ∈ V(G′). Call such a choice a datum δ. There are finitely many data.

Let Λ_δ := {(e, t) ∈ W : ξ(e) = Q_t}, the preimage of the holomorphic sheet of Lemma 3.1.
- Λ_δ is analytic, because it is the preimage under the finite map ξ × id of an analytic curve.
- Every point of Λ_δ has a neighbourhood in which Λ_δ is finite over Δ.
- Every irreducible component λ of Λ_δ is a curve, proper over Δ (W → Δ is proper), and it is not contained in a fibre of t (fibres of Λ_δ are finite). So t(λ) = Δ: the image is open by the open mapping theorem and closed by properness.

**Proposition 2.** Assume (Rig) and Y non-constant. Let T_{cr} be the set of t ∉ Z_1 at which an IMOV event of type (P) or (S) occurs. Then either T_{cr} is countable, or there are a datum δ and a component λ of Λ_δ with the following properties.
- **(Pers 1)** [pr_x(e)] = [Y_t] for every (e, t) ∈ λ.
- **(Pers 2)** For all t outside a countable set, the point (e, t) ∈ λ is the lift, on a piece E_t ⊂ W_t, of an IMOV event of type (P) or (S) at Q_t, with x moving on E_t and D_t := the piece of H_t(β_D). The type and the set of intact / constant / moving labels do not depend on t.
- **(Pers 3)** At t = 0, Q_0 itself carries a configuration of the same type, with value Y_0: a "persistent residual crossing" of V_0.

*Proof.*
- **Countably many t per component.** For a component λ of Λ_δ, the set {(e, t) ∈ λ : [pr_x(e)] = [Y_t]} is analytic in λ. Either it is all of λ, which is (Pers 1), or it is discrete in λ. In the latter case its t-image is countable.
- **Reduction to (Pers 1).** Every event in T_{cr} has a lift point of the form above for some datum, by §3.1. Data and components are finite in number. So if T_{cr} is uncountable, (Pers 1) holds for some (δ, λ), and uncountably many event times have their lift on λ.
- **(Pers 2): constancy and non-constancy.** For each label w, the set of t at which w is constant on the piece of W_t through the lift point is either countable or everything. This follows from the rank argument of R7-2 Lemma 2.1 / R7-3 Lemma 1(b) (Cartan–Remmert applied to (pr_w, t) on the relevant 2-dimensional family). The same argument applies to the lifted family of D, and to whether f_w is constant along it.
- **(Pers 2): patterns.** Pinched/unpinched patterns of the lifted branches H_t(β_D) are independent of t (R7-4 Lemma 2(a), (b)).
- **(Pers 2): the value of D's x-vertex.** The constant value of D's x-vertex is a holomorphic function φ(t) (R7-3 Lemma 1(a)). It equals Y_t at uncountably many t, hence identically.
- **(Pers 3).** Constancy at uncountably many t forces constancy at t = 0 (same rank argument). Non-constancy of x on E_t at some t forces non-constancy at t = 0 on a piece of W_0 (L1′, contrapositive). Values pass to t = 0 by continuity. The lift point e_0 over Q_0 lies on a piece of W_0 through Q_0. ∎

**Caveat on (Pers 3).** For a non-product stratum, the piece of W_0 on which x is non-constant may be a translate σE_0 rather than E_0 (R7-5 §1.4). Then (Pers 3) holds with the label x replaced by the appropriate σ-translate. I have not written this out.

### 3.3 Type (T)

For a fixed W and labels x ≠ x′, put Θ_{x,x′} := {(e, t) ∈ W : [pr_x(e)] = [pr_{x′}(e)]}. This is analytic.
- Θ_{x,x′} ≠ W. Otherwise x and x′ would be twins everywhere on W, which contradicts "x moves, x′ = ax constant" on E_t.
- Its 1-dimensional components contained in fibres t = t_1 are whole pieces of W_{t_1} along which x and x′ are twins. They do not contain E_{t_1}. So a type-(T) event at a point of E_t that is not on another piece (otherwise it is a point of F_0-type (a)) lies on a non-vertical component θ of Θ_{x,x′}. Such a θ is proper and surjective over Δ, as in §3.2.
- The argument of Proposition 2, with λ replaced by θ, gives the same dichotomy:
  - either the type-(T) times are countable;
  - or [pr_x] = [Y_t] = [pr_{x′}] identically along θ, i.e. a twin coincidence that persists to t = 0. Here, at the point e_0 ∈ θ_0, the moving label x passes through Y_0 at a point where the constant twin label x′ ≅ Y_0, and Q(e_0) has an automorphism exchanging x and x′.

  I have **not** checked whether the automorphism a_t persists along θ. If it does not, the event is only a coincidence of values and not a type-(T) event at generic t, in which case type (T) contributes only countably many times.

### 3.4 Corollary 3 (reduction of (CR) to V_0)

**Corollary 3.** Assume (Rig) and Y non-constant. Then (CR) holds unless V_0 has a **persistent residual configuration**: (Pers 1)–(Pers 3) for some datum, or the persistent twin coincidence of §3.3. In particular (CR) follows from:

**(PC) [open].** For every smooth closed 2-dimensional totally geodesic V_0 ⊂ M_g, B_0 has no point Q_0 carrying either of the following:
- a pure crossing (piece E ∋ Q_0 in Q_0's stratum, another branch D at Q_0, every label of M(E) intact and constant along D);
- a shared crossing with equal projected curves.

(A persistent twin coincidence of type (T) must also be excluded, unless the caveat in §3.3 disposes of it.)

*Proof.* Combine Proposition 1, Proposition 2 and §3.3. The countable exceptional sets add up to a countable set. ∎

Note that (PC) is only a sufficient condition. Corollary 3 really needs the weaker statement "no persistent such configuration". Persistence also carries information about the family: Q_t moves holomorphically along K(E), with x-coordinate Y_t. However, at a fixed t ≠ 0 nothing in (R1), (R2), (i), (ii) or (Rig) contradicts persistence.
- **Local consistency (cf. R7-2 §4.2).** The germ (σ, ρ) ↦ s_e = ρσ (edges at M(E)-vertices), s_f = ρ (f ∈ U), x-coordinate σ + c(t) can be used at every t. Here c(t) is chosen so that the x-value at the crossing is Y_t.
- **Compatibility with (Rig).** K(E) is fixed. The crossing point slides along it, and the pinned coordinates of Proposition 1 are not involved.

So any proof of (CR) must use total geodesy at t = 0, as the planner said.

---

## 4. On (CR2) / (PC): why the named approach does not close it (analysis, not proofs)

Setting: a pure crossing at Q_0 ∈ B_0 with D coarser (U ≠ ∅). This is the main case.

**1. Asymptotic norm.** By the computation of Lemma PA (PR-H §1, Steps 2–5), near Q_0 the Teichmüller norm on T_X V_0 is a sup over vertex factors in the limit X → Q_0.
- A tangent vector of V_0 decomposes into Beltrami pieces on the thick parts of the vertex components and on the U-collars. The collar part is controlled by estimate (C).
- Normal families and the Fatou argument of Steps 3–4 give lim ‖v‖_T = max_w ‖a_w‖_{T(Y_w)} for vectors with bounded collar part (one also needs the plumbing-direction contributions). So the limit norm is a sup-norm.
- In a pure crossing, the E-direction is supported on M(E) and the D-direction on M(D) ∪ (U-collars). These two sets are disjoint, so the limiting norm on T_X V_0 is the bidisc norm max(|a|‖v_E‖, |b|‖v_D‖).

**2. Antonakoudis.** The cited theorem is S. Antonakoudis, "Teichmüller spaces and bounded symmetric domains do not mix isometrically", GAFA 2017 (cited from memory). It says: for dim_ℂ T_{g,n} ≥ 2 and a bounded symmetric domain B with dim_ℂ B ≥ 2, there is no holomorphic map B → T_{g,n} or T_{g,n} → B that is an isometry for the Kobayashi metrics.
- It forbids an exact isometric bidisc in T_g.
- What a pure crossing gives is only an asymptotic bidisc structure. Rescaled limits of V_0 at Q_0 live in the product of the Teichmüller spaces of the components (times horoball factors for U), with the sup metric. Such a product does contain holomorphic isometric bidiscs.
- So a limiting argument cannot contradict Antonakoudis. One would need a quantitative version: an estimate of the deviation from the sup-norm at distance ε from the boundary, which beats the rate at which V_0 approaches the bidisc structure. I do not have one.

**3. Uniqueness of Teichmüller discs and total geodesy in mixed directions.**
- For w = a v_E + b v_D with |a|‖v_E‖ > |b|‖v_D‖, the norming differential q_w is close to q_{v_E}: its area concentrates on the maximal-speed vertex of M(E), by Lemma PA, Step 5.
- The disc generated by q_w nevertheless has tangent w, which has a nonzero D-component. The tangent of the disc of q is [q̄/|q|], which is non-trivial on the low-area D-region. So area concentration does NOT mean the disc ignores D. Both the disc of q_w and the disc of q_{v_E} lie in V_0, and there is no contradiction at first order.
- In the limiting bidisc, complex geodesics in such directions are non-unique (graphs z ↦ (z, f(z)), with f any holomorphic self-map of Δ with f(0) = 0 and f′(0) = b/a). In T_g they are unique. Exploiting this needs control of second-order terms of the Teichmüller metric near the boundary. Minsky's theorem only gives coarse (additive-error) control, which is useless infinitesimally.
- I could not find a contradiction.

**4. Wright / orbit closures.** V_0 is the image of an affine invariant manifold (Eskin–McMullen–Mukamel–Wright: totally geodesic subvarieties come from GL⁺(2,ℝ)-orbit closures; cited from memory). A pure crossing would mean that the boundary of that orbit closure (in the multi-scale / WYSIWYG compactification) has a point at which two boundary components with "independent" cylinder-type degenerations meet: M(E)-thick parts deform along E, while U-collars and M(D) deform along D.
- Wright's cylinder deformation theorem would say that the M(E)-cylinders and the U-cylinders lie in different equivalence classes of the 2-dimensional (projectivised, complex) tangent space.
- A rank-2, dimension-2 manifold is a locus of torus covers (rank 2 implies full rank of the projection, which for dimension 2 is only possible in genus 2 / torus-cover situations). A rank-1 dimension-2 manifold has a 1-dimensional rel or a 2-dimensional twist space.
- Pursuing this would require a classification-type input that I cannot supply or verify from memory. Open.

**5. Local reducibility.** If closure(V_0) is locally reducible at Q_0 with E and D in different local sheets, then the norm argument above concerns two separate sheets. Each sheet is a 2-dimensional germ with only one of the two boundary curves, and no bidisc-type structure arises at all.
- Such a point could in principle exist even for smooth V_0: V_0 is smooth in M_g, but its closure need not be locally irreducible at boundary points.
- Proposition K's network can pass from E to D at such a point, since it passes through Q_0 ∈ closure(D) ∩ E regardless of sheets. So local reducibility does not help (PC); it makes (PC) harder, because then even an exact local product structure would not be forced.
- Hence (PC) as stated might be false for some V_0. I have no example. A covering construction from M̄_{0,5} would need Φ̄ to identify a point of the open boundary divisor with a corner point of another divisor (possible only after stabilization contracts rational components). I did not check any case.

---

## 5. Summary: proved / not proved / open

**Proved** (modulo the cited run lemmas L1′, C2, R7-1 Lemma 1, R7-4 Lemma 2, and R7-2 Lemma 2.1 / R7-3 Lemma 1 rank arguments, and standard analytic geometry):
1. Lemmas 1.1, 1.2: under (Rig), puncture values are finite, and pinning one moving coordinate on a piece pins Y_t.
2. Proposition 1 (corrected CR1): at all but countably many t, every IMOV event is a pure crossing (P), a shared crossing with equal projected curves (S), or a same-branch twin (T). Type (S) is a gap in the planner's (CR1) for same-stratum D.
3. Lemma 3.1: the possible crossing points move on finitely many holomorphic sheets t ↦ H_t(Q_0), Q_0 ∈ F_0.
4. Proposition 2 and Corollary 3: assuming (Rig) and non-constant Y, either the IMOV times are countable, or a residual configuration persists analytically and is present at t = 0. Hence (CR) ⇐ (PC). The non-product-stratum relabelling caveat in (Pers 3) and the automorphism-persistence caveat in §3.3 are noted but not written out.

**Not proved:** (CR) itself, and (CR2) in the planner's form.

**Open questions:**
- **(PC)**: does a smooth closed totally geodesic surface V_0 ⊂ M_g admit a pure crossing, or a shared crossing with equal projected curves, at a point of B_0? More weakly: does it admit one that persists in a family satisfying (R1), (R2) and (Rig)?
- **Quantitative Antonakoudis.** Is there a quantitative "no asymptotic isometric bidisc" statement near the boundary of M̄_g that would rule out pure crossings in which E and D lie in one local sheet?
- **Locally reducible closures.** Can closure(V_0) be locally reducible at a boundary point that is interior to one boundary piece and a puncture of another? If so, (PC) must be weakened, and (CR) would have to be proved by another mechanism, if at all.

=== END OF ANSWER round8_q6 ===
