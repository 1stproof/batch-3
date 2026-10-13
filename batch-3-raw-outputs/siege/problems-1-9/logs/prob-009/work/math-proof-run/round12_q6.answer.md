# round12_q6 — Mechanism G (lift-curves in a 3-fold component X and their stabilisers)

## Status (final)
**MS11♭ is NOT proved here and NOT refuted.** What this file does:
- It describes the lift-curves exactly (Lemma G1).
- It gives an exact criterion for MS11♭ in terms of lift-curves (Lemma G2).
- It corrects the planner's observation: (1L_X) gives MS11♭ only when the initial twist τ satisfies an extra condition (Lemma G2(c)). So (1L_X) alone is not sufficient.
- It determines the local structure of 𝒳 at generic points of S × {0} (Lemma G3). The planner's three cases are not exhaustive. In particular "t = b², a single lift-curve" is false in general: an irreducible X can contain two lift-curves exchanged by an element of K_S, the pointwise stabiliser of S (Model G3′).
- It shows that such K_S-multiplicities are harmless (Proposition G4).
- It isolates what remains (§4): an element of A_X that acts non-trivially on S or moves S, or a twist τ ∉ Stab(b̃)·Stab(x).

Global input (total geodesy, Lemma TG) would be needed exactly for the residual case of §4. I could not make it work.

Conventions. I use the run's readings (R1), (R2) with H_0 = id, (Rig), and the notation of the task: A := Aut(Q) acting on the ball B ⊂ Def(Q); q : B → B/A; 𝒳 := q^{-1}(closure 𝒱) ∩ (B × Δ_ε); Λ := {(p,t) : q(p) = Q_t}; L_0 is a lift-curve. A acts on B × Δ_ε by g(p,t) = (gp,t).

The following facts are taken from the run as given (spliced in the task file). I did not re-prove them.
- (F1) Every anchored sheet contains a lift-curve (round11_q4 L2.1).
- (F2) If T is a boundary-type sheet and L ⊂ T is a lift-curve, then P(T) = C(L) (round11_q4 L2.2, round11_q1 L2.3).
- (F3) Equivariance (K3): F_{gy}(gp) ≅ F_y(p). Hence C(gL) = g·C(L), P(gT) = g·P(T), and g maps anchored sheets of c̃ to anchored sheets of gc̃.
- (F4) By (P), every anchored sheet of β̃ or of b̃ is of boundary type.
- (F5) Mechanism D: D = X ∩ {∏ s_e = 0} has a connected sheet graph. Its vertices are anchored boundary-type sheets, including anchored sheets of β̃ and of b̃. Moreover τT_x ⊂ X with τ ∈ Stab_pt(β̃) (round11_q7 D1(d)).

## 1. Lemma G1 (lift-curves) — proved
Assume, as in the run's definition, that Λ is a closed analytic subset of B × Δ_ε. Let L_0 be one irreducible component of its germ at (0,0), and put A_L := Stab_A(L_0).
- (a) Near (0,0), Λ = ⋃_{g∈A} gL_0. The lift-curves are exactly the distinct gL_0, and they correspond bijectively to A/A_L.
- (b) Put A_X := {g ∈ A : gL_0 ⊂ X}. Then G_X·A_X·A_L = A_X, where G_X := Stab_A(X). Moreover A_X = ⋃_{X′} {g : gX′ = X}, the union taken over the components X′ of 𝒳 that contain L_0. Each set {g : gX′ = X} is either empty or a coset G_X h. The number of lift-curves in X is |A_X|/|A_L|. If g ∈ A_X ∖ G_X, then L_0 ⊂ X ∩ g^{-1}X with g^{-1}X ≠ X.

*Proof.*
- (a) We have q^{-1}(Q) = A·0 = {0}, since 0 is A-fixed. So Λ ∩ {t = 0} = {(0,0)}. Hence t|_{L_0} is non-constant, and it is a finite map of an irreducible curve germ, so t(L_0) contains a neighbourhood of 0.
- Let (p,t) ∈ Λ with |t| small. Choose (p′,t) ∈ L_0. Then q(p′) = Q_t = q(p), so p = gp′ for some g ∈ A, and (p,t) ∈ gL_0.
- Each gL_0 is an irreducible curve germ, so the components of Λ are the distinct gL_0. Their stabiliser structure is the standard orbit–stabiliser count.
- (b) gL_0 ⊂ X ⟺ L_0 ⊂ g^{-1}X. Since g^{-1}X is a component of 𝒳 (𝒳 is A-invariant), this proves the union formula. The coset statement holds because gX′ = X = hX′ ⟺ gh^{-1} ∈ G_X. The rest is immediate. ∎

## 2. Lemma G2 (exact criterion; the role of τ) — proved from (F1)–(F5)
Fix a lift-curve L_1 ⊂ T_x (one exists by (F1)). Then x ∈ P(T_x) = C(L_1) by (F2) and (F4). Call a lift-curve L *x-good* if x ∈ C(L). Let Λ_b be the set of lift-curves that lie in some anchored sheet of b̃.
- (a) MS11♭ ⟺ Λ_b contains an x-good lift-curve.
- (b) gL_1 is x-good ⟺ g^{-1}x ∈ C(L_1); in particular this holds for g ∈ Stab_A(x). Λ_b is invariant under Stab_A(b̃), the setwise stabiliser of b̃. Hence MS11♭ holds as soon as Λ_b ∩ Stab_A(b̃)·Stab_A(x)·L_1 ≠ ∅.
- (c) **Correction to the planner's observation.** Assume (1L_X), i.e. X contains exactly one lift-curve L_X. Then τx ∈ P(T) for every D-sheet T of X, and in particular for every anchored sheet T_b of b̃ in X. MS11♭ follows if τ ∈ Stab_A(b̃)·Stab_A(x), e.g. if τx = x or τb̃ = b̃. Without this condition, (1L_X) only gives "x is persistent on an anchored sheet of τ^{-1}b̃". That is a different lifted branch of b, lying in τ^{-1}S.

*Proof.*
- (a) "⇐": an x-good L ⊂ T_b gives x ∈ C(L) = P(T_b) by (F2) and (F4). "⇒": x ∈ P(T_b) = C(L) for any L ⊂ T_b, and such an L exists by (F1).
- (b) C(gL_1) = gC(L_1) by (F3). If k ∈ Stab_A(b̃) and L ⊂ T_b, then kL ⊂ kT_b, which is an anchored sheet of kb̃ = b̃.
- (c) Every D-sheet T is anchored (F5), so it contains a lift-curve (F1). That lift-curve lies in X, so it is L_X, and P(T) = C(L_X).
  - τT_x ⊂ X is 2-dimensional and lies in {∏ s_e = 0}, so it is a D-sheet. Hence C(L_X) = P(τT_x) = τP(T_x) ∋ τx.
  - Write τ = k s with k ∈ Stab(b̃) and s ∈ Stab(x). Then k^{-1}T_b is an anchored sheet of b̃, and P(k^{-1}T_b) = k^{-1}P(T_b) ∋ k^{-1}τx = sx = x. ∎

Remark. In the chain's endpoint use, (τ^{-1}b̃, x) and (b̃, τx) are A-equivalent pairs. So the twisted conclusion contradicts MERGE/MOV of x along b̃ only if τ ∈ Stab(b̃)Stab(x). The twist is therefore a genuine part of the problem and is not just bookkeeping.

## 3. Local structure along S × {0} — proved
Let K_S ⊂ A be the pointwise stabiliser of S. Let p ∈ S × {0} be generic: off {∏ s_e = 0}, off the singular set, with Stab_A(p) = K_S, and S smooth at p.

**Lemma G3.** Read Lemma Red as "the central fibre of the coarse 𝒱 → Δ is reduced" (ledger entry 80), and assume 𝒱 is smooth in the coarse space near q(p).
- (a) Near p, 𝒳 = S × Λ_p, where Λ_p is the K_S-invariant lift, to the normal slice N × Δ, of a smooth coarse curve t ↦ (c(t), t). Its components are Puiseux curves, permuted transitively by K_S. So K_S permutes transitively the components of 𝒳 that contain S × {0}. In particular K_S ⊂ G_X if 𝒳 has a single component through S × {0}, for instance under the orbifold reading (Orb), in which q^{-1}(𝒱) is smooth.
- (b) Under (Orb): X is smooth at p, with coordinates (s_1, s_2, y), S = {y = 0}, and t = unit·y^m. Here m = |image of K_S in Aut(X,p)|, and K_S acts by y ↦ ζy, ζ ∈ μ_m. In particular m = 1 (t is a coordinate) iff K_S acts trivially on X.
- (c) (Tool (a)(1) of the task.) Let X be smooth at p with dt|_X ≠ 0, and let g ∈ G_X have finite order, fix S × {0} pointwise, and preserve t. Then g = id on X.

*Proof.*
- (c) By Cartan, g is linearisable at p. dg_p is the identity on ker dt_p = T_pS, and dt∘dg_p = dt. So dg_p = I + N with N(T_pX) ⊂ ker dt_p and N|_{ker dt_p} = 0. Then N² = 0. A unipotent matrix of finite order is the identity, so g = id near p. Fix(g) ∩ X is analytic and contains an open subset of the irreducible germ X, so it is all of X.
- (b) Here X = q^{-1}(𝒱) is smooth of dimension 3 near p, and X ∩ {t = 0} = q^{-1}(V_0) = K_S·S = S near p.
  - K_S fixes the smooth hypersurface S of X pointwise. After linearisation its image acts on the normal line through a faithful character group μ_{m′}. So X/K_S has coordinates (s, Y = y^{m′}).
  - t is K_S-invariant and vanishes exactly on S, so t = unit·Y^k with m = km′.
  - The coarse fibre {t = 0} is reduced, which forces k = 1.
- (a) In coarse coordinates near q(p), B/K_S ≅ S × (N/K_S), and coarse 𝒱 ⊃ V_0 = S × {0}. Coarse 𝒱 is smooth with reduced central fibre, so t|_{coarse 𝒱} is a submersion at generic points. So coarse 𝒱 is, generically over S, a family of smooth curves t ↦ (s, c_s(t), t) depending holomorphically on s.
  - The preimage of each such curve in N × Δ is a union of Puiseux curves, permuted transitively by K_S (the argument of Lemma G1(a)). For generic s the combinatorics is locally constant in s, which gives the product description.
  - A component of the germ of 𝒳 at (0,0) that contains S × {0} is, near p, a union of local components. Transitivity at p therefore gives transitivity on the global components. ∎

**The planner's three cases are not exhaustive.**
- Under (Orb) only "t = y^m, K_S ≅ μ_m on X" occurs, for every m ≥ 1. The case "X ≠ gX, t = ±b" cannot occur.
- Under the coarse reading, more general K_S-orbits of Puiseux curves occur, for example a non-reflection K_S acting on a normal plane.
- More importantly, the generic structure along S × {0} says nothing about the lift-curves. Those curves meet {t = 0} only at the origin, where X need not be a product.

**Model G3′ (proved, chart-level): an irreducible X with two lift-curves exchanged by k ∈ K_S.**
- Take chart coordinates (a, b, y, …) with k : y ↦ −y, and S = {y = 0} (coordinates a, b). Let Q_t lie on {a = b = 0}.
- Let X := {y² = t² + t a} (other coordinates 0).
  - X is irreducible, because t(t+a) is not a square.
  - X is k-invariant, and its central fibre is supported on S.
  - At generic points (a ≠ 0), X is smooth with t = y²/a·unit, which is case (b) with m = 2.
  - Its coarse image {Y = t² + ta} (Y = y²) is smooth, with reduced central fibre.
- X ∩ {a = b = 0} = {y = ±t}. These are two lift-curves L, kL ≠ L, both in X, and Q_t loses k.

So (1L_X) fails here, contrary to the planner's local evidence for the case "t = b²". The failure is harmless, by the next proposition.

**Proposition G4 (proved from (F1)–(F5)).** Put L_1′ := τL_1 ⊂ τT_x ⊂ X. Suppose:
- (i) every lift-curve of X that lies in an anchored sheet of b̃ inside X has the form kL_1′ with k ∈ Stab_A(b̃) (for instance, all lift-curves of X are K_S-translates of L_1′; note that K_S ⊂ Stab_A(b̃) because b̃ ⊂ S); and
- (ii) τ ∈ Stab_A(b̃)·Stab_A(x).

Then MS11♭ holds.

*Proof.* By (F5) there is an anchored sheet T_b of b̃ in X. It contains a lift-curve (F1), which lies in X, so by (i) it is kτL_1. Then kτ ∈ Stab(b̃)Stab(x) by (ii), and Lemma G2(b) applies to the curve kτL_1 ∈ Λ_b. ∎

So the K_S-part of A_X never matters, even under the coarse reading. In that reading the components kX (k ∈ K_S) through S × {0} are just as good as X, since k fixes β̃ and b̃ pointwise.

## 4. What remains (residual configuration) — not proved
By G2 and G4, a failure of MS11♭ needs at least one of the following.
- **(R-a)** A lift-curve gτL_1 ⊂ X lying in an anchored sheet of b̃, with g ∉ Stab(b̃)·K_S. This needs one of:
  - g ∈ G_X acting non-trivially on S (g ∈ Stab(S) ∖ K_S, a "reflection" of S); by Lemma TG, Fix(g) ∩ S is then a Teichmüller disc or consists of boundary curves;
  - g ∉ G_X, with X ∩ g^{-1}X ⊃ L_0, i.e. two 3-fold components meeting along a lift-curve, where g^{-1}X ⊃ g^{-1}S × {0} and g^{-1}S ≠ S.

  In either case g ∉ Aut(Q_t) for generic t: Q_t loses g.
- **(R-b)** The initial twist τ ∈ Stab_pt(β̃) does not lie in Stab(b̃)·Stab(x). Since τ fixes β̃ pointwise, either τS ≠ S, or τ is a reflection of S whose fixed set contains β̃.

**Where global input must enter.** All the constraints used in G1–G4 are chart-local. The run already has chart-level models realising (R-a)/(R-b) failures (round11_q7 §6, round11_q1 §5, round11_q2 §1.2). So no chart-local argument can exclude them.
- The candidate global input is total geodesy: Lemma TG applied to g on S, together with Lemma PA (constant vertices carry no area).
- One would need: a reflection g of S that fixes the boundary curve β̃ (or a Teichmüller disc), and is lost by Q_t, cannot exchange a Y-persistent copy with a non-persistent one.
- I could not derive this. In particular, I found no mechanism linking the action of g on S at t = 0 to which labels are persistent at t ≠ 0. Persistence is read off the lift-curves, which see S only at the origin.

## Summary
**Proved** (modulo the run's facts F1–F5, cited not re-proved):
- Lemma G1: lift-curves form one A-orbit; the lift-curves in X form a union of cosets G_X h.
- Lemma G2: an exact criterion for MS11♭; (1L_X) implies MS11♭ only under τ ∈ Stab(b̃)Stab(x). The planner's observation needed this correction.
- Lemma G3: the local structure along S × {0}. The three-case list is not exhaustive. Tool (a)(1) is proved.
- Model G3′: (1L_X) can fail through K_S even for irreducible X.
- Proposition G4: K_S-multiplicity is harmless.

**Not proved:** MS11♭. Steps 2 and 3 of the task are not achieved; (1L_X) is false in general, as Model G3′ shows.

**Open:**
- (O-G1) Exclude (R-a): an element of A acting non-trivially on S, or moving S, that relates the x-good lift-curve to the lift-curves of the anchored b̃-sheets.
- (O-G2) Exclude (R-b), or show that τ can always be chosen in Stab(b̃)Stab(x).
- (O-G3) The run's open (Rig) (entry 82).

No counterexample was constructed.

=== END OF ANSWER round12_q6 ===
