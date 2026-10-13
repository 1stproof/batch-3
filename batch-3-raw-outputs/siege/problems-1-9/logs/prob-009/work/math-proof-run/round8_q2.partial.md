# round8_q2 — answer (MS8)

**Status / plan (written first, updated as I go).**
Plan: (1) extract everything (Rig) gives at a *generic* time t (proved, §1); (2) reduce MS8 to precise
statements about the two known obstacles (twins, crossings) (§2); (3) attack the twin case through the
fixed loci of automorphisms in the lifted family (§3). Current target of §1: "Generic-time structure
theorem" below.

Readings (R1), (R2) and the notation of the task file are used throughout. "Generic" is defined in §1.

## 1. Generic-time structure under (Rig) (proved)

### 1.1 Fixed finite sets and the value curves

Let 𝒦 be the finite set of (Rig). All pointed curves are compared in the coarse space
𝔐 := M_{g_i,n_i}/S_{n_i} ("≅ Y" means equal image in 𝔐).

**(F) the fixed finite set 𝔉 ⊂ 𝔐.** It consists of the classes of all smooth components (with their special
points) of the coordinates of the following finitely many points:
- (F1) the points of K ∩ ∂(∏_{u∈M} M̄_u), for (G,M,K) ∈ 𝒦 (finite: K is an irreducible compact curve not
  contained in the closed analytic set ∂(∏ M̄_u));
- (F2) for each (G,M,K) ∈ 𝒦, each y ∈ M and each point a of the finite set A_1 of curves occurring as
  components in (F1) (more precisely: each y and each pointed curve c in the finite set of classes from (F1)),
  the points of K ∩ {pr_y = some curve whose class is c, up to relabelling}. Since pr_y|_K is non-constant
  (y ∈ M means f_y is non-constant, and K is the closure of the image of the piece), this is a finite set.

𝔉 is independent of t.

**(Γ) value curves.** For each stable graph G (finitely many), each 2-dimensional irreducible component W of
the lifted family 𝓦_G (R7-5, (P2)–(P4)), and each vertex u of G such that pr_u is constant on every
1-dimensional component of W_0 (equivalently, by L1′, of every W_t), put
Γ_{W,u} := (pr_u, t)(W) ⊂ M̄_u × Δ. W → Δ is proper, so Γ_{W,u} is an irreducible analytic set (Remmert),
and by L1′ every fibre is finite; t is non-constant on it; so Γ_{W,u} is an irreducible curve, finite over Δ.
When M_u is of type (g_i,n_i), let Γ'_{W,u} be its image in 𝔐 × Δ (still an irreducible curve finite
over Δ). Call (W,u) a **Y-vertex** if Γ'_{W,u} = graph(Y) (Y: Δ → 𝔐 is holomorphic by PR-A; its graph is an
irreducible curve).

**Definition (generic).** Assume Y is non-constant. Z ⊂ Δ is the set of t such that either Y_t ∈ 𝔉, or
(Y_t, t) ∈ Γ'_{W,u} for some (W,u) that is not a Y-vertex. For each of the finitely many non-Y-vertices,
Γ'_{W,u} ∩ graph(Y) is an intersection of two distinct irreducible curves, hence discrete; Y^{-1}(𝔉) is
discrete because Y is non-constant. So **Z is discrete in Δ**, in particular countable and closed.
(This improves the "countable" of the chain to "discrete", and covers non-product strata via L1′.)

### 1.2 The structure theorem

Fix t ∉ Z, Q ∈ B_t, a lift q ∈ Def(Q), a Y_t-copy y of q (a label with comp_y(q) ≅ Y_t), and a boundary or
interior branch b of B_t at Q with a lift b̃ through q (pattern S_b̃, piece E at time t, graph G_b,
point p ∈ Ē over Q).

**Theorem 1 (generic-time trichotomy).** Exactly one of:
- (STAY) every edge at y is in S_b̃, the vertex {y} of G_b is constant on E, and the pair (W,{y}) with
  E ⊂ W_t is a Y-vertex;
- (IMOV) Q ∈ Δ_{G_b} (Q is an interior point of the piece; S_b̃ = E(G_Q)), y ∈ M(E), and the point
  pr_{M(E)}(Q) ∈ K(E) satisfies: for every z ∈ M(E) and every other branch b' at Q through q, the label z is
  STAY or IMOV along b' (never merged, never moving at a puncture).
Moreover MERGE (some edge at y unpinched along b̃) and puncture-MOV are impossible.

*Proof.*
1. *Merge excluded.* If some edge at y is unpinched, then by R7-4 Lemma 1 (proof, items 3–4) p is a puncture,
   the vertex u ∋ y of G_b is non-constant, and comp_y(q) is a component of f_u(p). By (Rig) and chain step 3,
   pr_{M(E)}ν(p) ∈ K ∩ ∂, so f_u(p) is a coordinate of a point of (F1) and Y_t ∈ 𝔉: excluded.
2. *Puncture-move excluded.* If y is intact, u = {y} non-constant and Q ∉ Δ_{G_b}, then p is a puncture
   (R7-4 Lemma 1 (b)) and f_y(p) = comp_y(q) ≅ Y_t is a coordinate of a point of (F1): Y_t ∈ 𝔉, excluded.
3. *Constant case.* If y is intact and {y} constant on E, its value is comp_y(q) ≅ Y_t, so
   (Y_t,t) ∈ Γ'_{W,{y}}; as t ∉ Z, (W,{y}) is a Y-vertex: STAY.
4. *Remaining case.* y intact, {y} non-constant, Q ∈ Δ_{G_b}. Let z ∈ M(E) and b' another branch at Q.
   If z were merged or puncture-moving along b', then as in 1–2 comp_z(q) has class in the (F1)-set, so
   pr_{M(E)}(Q) lies in the finite (F2)-set of K(E), and its y-coordinate Y_t lies in 𝔉: excluded. ∎

**Corollary 2 (closure of the network).** For t ∉ Z let N_t := {Q ∈ B_t : Q has a Y_t-copy}. N_t is closed
(R7-1 Lemma 2). If no IMOV occurs at points of N_t, N_t is open in B_t, hence contains the connected
component C_t ∋ ∂V_t of B_t, and every Y_t-copy of every point of C_t is STAY along every branch.
(Proof: Theorem 1 + R7-1 Lemma 3; the Y_t-copy y is STAY along every branch, so nearby points of every
branch carry the constant Y_t-component.) ∎

**Remark (twins are harmless at fixed generic t).** Theorem 1 and Corollary 2 never compare different
copies: at generic t *every* Y_t-copy behaves as stated, whatever the automorphisms. The twin problem lives
only in the passage t → 0, where Prop K's merging copy must be shown to be a limit of Y_t-copies.

**Remark (a small clarification of 𝔉).** In (F2) read: for each (G,M,K) ∈ 𝒦, each y ∈ M and each class c in
the finite set of classes of coordinates-components arising in (F1), the (finitely many) points of K at
which the class of pr_y equals c; here finiteness holds because pr_y|_K is non-constant for y ∈ M. 𝔉 is the
set of classes of smooth components of all coordinates of all points of (F1) and (F2).

## 2. What Theorem 1 gives for MS8, and the exact residue (proved reduction)

Assume throughout §2: the hypotheses of MS8, and **Y non-constant** (to be contradicted).

### 2.1 The two surviving configurations

By Theorem 1, for each generic t (t ∉ Z, Z discrete) and each Y_t-copy y of each Q ∈ B_t and each branch b
at Q: y STAYs (with value function ≡ Y) or is in an IMOV (crossing) configuration. So:

**Proposition 3 (dichotomy at generic times).** One of the following holds.
- (I) For some generic t, some Q ∈ B_t, some lift q, some Y_t-copy y of q and some branch, the IMOV case of
  Theorem 1 occurs. Then, with E the piece and M = M(E), K = K(E) as in (Rig): Y_t = pr_y(pr_{M}(Q)) lies in
  the fixed irreducible algebraic curve T := pr_y(K) ⊂ M̄_{g_i,n_i} (image under a finite morphism of
  projective varieties, hence an irreducible curve), and T is not a point since y ∈ M.
- (II) For every generic t, every Y_t-copy of every point of B_t STAYs along every branch at that point. Then
  for every generic t: N_t is open and closed in B_t (Corollary 2), so C_t ⊂ N_t, and every coarse piece D of
  C_t has a lift with a vertex constant of value ≅ Y_t (R7-4 Lemma 4 and Corollary 4′, whose hypotheses hold
  because by Theorem 1 no MS6 configuration exists at generic t and no piece is MOV-blocked at a point of
  N_t: MOV-blockedness at P ∈ D ∩ N_t would be an IMOV, excluded in case (II)). By Theorem 1 each such
  constant vertex is a Y-vertex, i.e. its value function is ≡ Y; specialising to t = 0 (Y-vertices are
  defined by curves Γ_{W,u} over all of Δ, and L1′ gives the constancy at t = 0 as well), **every piece of
  C_0 carries a vertex constant of value ≅ Y_0, and every point of C_0 has a component ≅ Y_0.**

*Proof.* Immediate from Theorem 1 and the quoted prior results; in (I), T is an algebraic curve because K is
a closed irreducible curve in the projective variety ∏_{u∈M} M̄_u and pr_y is a morphism non-constant on K. ∎

### 2.2 Case (II): the residue is exactly the twin/label problem

In case (II) we have, at t = 0, a "network" 𝒩 := {(D,c) : D a piece of C_0 (in any stratum, lifted), c a
vertex of D with (W_D,c) a Y-vertex}, containing (each component of ∂V_0, i), and with the property that
every piece of C_0 occurs in it.

What is still missing is a *contradiction*: Proposition K (PR-H §3, total geodesy at t = 0) produces a point
Q_0 ∈ B_0 and a branch b at Q_0 at which a **path-marked** copy of Y_0 merges (MERGE) or moves
(puncture-MOV or interior-MOV). To contradict (II) one needs the merging copy to be, at generic t, a
Y_t-copy. The following is the precise transport statement that is available, and the precise gap.

**Lemma 4 (transport of a merge to generic times; proved).** Let Q ∈ B_0, let q_0 = 0 ∈ Def(Q), let b̃ be a
lifted branch at 0 with pattern S := S_b̃, and let x be a label merged along b̃ (some edge at x not in S).
Then for all small t there are a lift q_t of Q_t := H_t(Q) and a lifted branch at q_t with pattern exactly S
(so x is merged along it), and q_t → 0 as t → 0. Consequently, by Theorem 1, for generic small t,
comp_x(q_t) ≇ Y_t.

*Proof.* Let Ñ be the component of q^{-1}(H((b \ {Q}) × Δ)) containing b̃ \ {0} (R7-4 Lemma 2(a)); the
pattern is constant = S on Ñ, and closure(Ñ) is a finite union of irreducible 2-dimensional germs (Lemma
2(c)), on each of which t is non-constant, so each slice Ñ_t is 1-dimensional and nonempty for small t.
Ñ_t → H_t(b) \ {Q_t} is finite and proper, so points of Ñ_t tending to Q_t accumulate at a lift q_t of Q_t,
and the branch of Ñ_t at q_t has pattern S. Since Def(Q) → Def(Q)/Aut(Q) is proper and Q_t → Q, every lift
of Q_t tends to 0. The last sentence is case 1 of Theorem 1 (merge excluded for Y_t-copies). ∎

**The gap, stated exactly.** Lemma 4 shows the merged label x is *not* a Y_t-copy for generic t; since
comp_x(q_t) → comp_x(0) ≅ Y_0 and Y_t → Y_0, this is consistent: the splitting of twins. To contradict (II)
one needs a label identification: that the Y-vertex label furnished by (II) at the pieces adjacent to Q_0
**is**, in the chart Def(Q_0) and at the same lift q_t, the label that merges along the transported branch.
Two lifted branches at the *same* lift differ by an element σ ∈ Aut(Q_0) (R7-3 Lemma 3), and
comp_x(σq) ≅ comp_{σ^{-1}x}(q); so the argument yields only "some Aut(Q_0)-translate of x is a Y_t-copy".
This is precisely the twin obstruction of R7-2 §4.1, R7-3 §4–5, realised (for a singular V_0) by the quintic
example PR-I. Therefore:

**Theorem 5 (reduction; proved).** Assume the hypotheses of MS8. Then Y_t = Y_0 for all t, provided at least
one of the following holds.
- (a) *Orbit-merge form of Proposition K:* there are Q ∈ B_0, a lifted branch b̃ at 0 ∈ Def(Q) and a label x
  with comp_x(0) ≅ Y_0 such that **every** label in Aut(Q)·x is merged along b̃, or is intact along b̃ with
  comp non-constant along b̃ and Q ∉ Δ_{G_b}; and Q is in the same connected component C_0 of B_0 as ∂V_0
  with every Y_0-copy at Q being in Aut(Q)·x — more economically, it suffices that Aut(Q)·x ⊇ {labels of
  Y_0-copies of Q} and Q ∈ C_0 (hypothesis (TM) of R7-4 Theorem 3 together with (Y)).
- (b) *(NT\*)* no point of B_0 has two distinct components ≅ Y_0 (then Aut(Q) fixes the unique Y_0-copy
  label, and (a) reduces to Proposition K itself, in the MERGE or puncture-MOV case), **together with** the
  exclusion of the interior-MOV endpoint.
- (c) *(Lock)* at the finitely many junction points of Proposition K's network, in the MERGE or puncture-MOV
  case (R7-1 Theorem T).

*Proof.* (a): By Proposition 3 we may assume case (II) (in case (I) see §3). By (II), Q ∈ C_0 ⊂ N_0 has a
component ≅ Y_0, and for generic t the point Q_t has a Y_t-copy: indeed by (II) the piece D of C_0 through
(or ending at) Q has a Y-vertex c, whose value at the puncture/point over Q_t is Y_t and is the component at
some label ℓ of some lift of Q_t (R7-1 Lemma 5(ii),(iii)); by (II) applied at generic t, ℓ is a label of a
Y_t-copy. Pulling back by the automorphism identifying that lift with the lift q_t of Lemma 4, we obtain a
label ℓ' ∈ Aut(Q)·ℓ with comp_{ℓ'}(q_t) ≅ Y_t, and by R7-1 Lemma 5(iii) (limits of labels of copies lie in
Λ(Q)) ℓ' ∈ Λ(Q). If Λ(Q) ⊆ Aut(Q)·x, then ℓ' = a^{-1}x for some a ∈ Aut(Q), and by hypothesis a^{-1}x is
merged (resp. intact and moving) along b̃, hence x is merged along a b̃ and ℓ' = a^{-1}x is merged along b̃;
applying Theorem 1 at q_t to the Y_t-copy ℓ' and the lifted branch at q_t of pattern S_b̃ (Lemma 4 provides
one at q_t itself) contradicts the merge/puncture-move exclusion. Hence Y is constant, i.e. Y_t ≡ Y_0.
(This is R7-4 Theorem 3 re-proved inside the present generic-time framework; the exclusion is now at *every*
generic t, not just along a sequence.)
(b), (c) are R7-2 Theorem A and R7-1 Theorem T, quoted; they are the already-known partial results. ∎

*Caveat.* In the proof of (a) I used R7-1 Lemma 5(ii),(iii) (constant vertices give, at every lift of the
transported point, a label whose component is the constant value, and these labels converge into Λ(Q)).
Lemma 5 is proved there for product-type strata and asserted ("checked routinely") in general; I re-checked
(ii) and (iii) and they use only (Def1)-continuity of the chart components plus L1 in the form L1′, so they
are available for all strata once L1′ is used in place of L1 — which is legitimate here since
(II) furnishes Y-vertices through the components W of the lifted families, exactly the objects L1′ speaks
about.

## 3. Case (I): the crossing (interior-MOV) case

### 3.1 The image curve is t-independent (proved from (Rig))

**Lemma 6.** Let W be a 2-dimensional irreducible component of a lifted family 𝓦_G (R7-5 (P2)), and let
M ⊂ V(G) be the set of vertices non-constant on the 1-dimensional components of the fibres W_t (by L1′ this
set is the same for all t). Assume (Rig). Then the closure Σ := (pr_M × id)(W) ⊂ ∏_{u∈M} M̄_u × Δ satisfies
Σ = K × Δ for a single irreducible curve K; consequently K(E) = K for every piece E ⊂ W_t and every t: the
image curve of a transported piece does not depend on t.

*Proof.* W is proper over Δ, so Σ is a closed irreducible analytic set (Remmert); t is non-constant on it,
and each fibre Σ_t = pr_M(W_t) is a finite union of the curves K(E), E a 1-dimensional component of W_t
(these are curves, not points, since M is the non-constant set). So dim Σ = 2. By (Rig) the K(E) belong to
a fixed finite list K_1, …, K_N of irreducible curves in ∏_{u∈M} M̄_u (up to the finite group Aut(G), which
we may absorb by enlarging the list). Hence Σ ⊂ ⋃_j (K_j × Δ), a finite union of irreducible
2-dimensional sets. Since Σ is irreducible and 2-dimensional, Σ = K_j × Δ for one j. Finally
K(E) ⊂ Σ_t = K_j, and both are irreducible curves, so K(E) = K_j. ∎

### 3.2 What case (I) forces (proved)

**Proposition 7.** Assume MS8's hypotheses and Y non-constant, and suppose case (I) of Proposition 3 occurs
(an IMOV/crossing at some generic time). Then there is a fixed irreducible algebraic curve T ⊂ M̄_{g_i,n_i}
(independent of t, by Lemma 6), namely T = pr_y(K) for a piece E with y ∈ M(E), such that **Y_t ∈ T for all
t ∈ Δ**, and moreover:
1. at t = 0 the corresponding piece E_0 ⊂ B_0 has the non-constant vertex y with closure(π_y(E_0)) = T and
   T ∋ Y_0;
2. for generic t, the point Q_t ∈ E_t realising the crossing satisfies pr_y(pr_{M(E)}(Q_t)) = Y_t, so Q_t
   lies in the finite fibre (pr_y|_K)^{-1}(Y_t); in particular t ↦ pr_{M(E)}(Q_t) is a non-constant path in
   the fixed curve K;
3. the adjacent STAY piece D (for which Q_t is a puncture) has a Y-vertex, i.e. a vertex constant with
   value Y_t for all t.

*Proof.* Proposition 3(I) gives Y_t ∈ pr_y(K(E)) at the generic time in question; Lemma 6 makes K and hence
T t-independent, and Theorem 1 gives, at every generic t and at the point Q_t = H_t(Q_0), the same
alternative (the configuration transports: strata, branches and pieces are transported by (R2), and the
merge/puncture-move alternatives remain excluded at every generic t). Thus Y_t ∈ T for all generic t, hence
for all t by continuity of Y and closedness of T. Items 1–3 are read off from the IMOV clause of Theorem 1
and from case (II)'s argument applied to the branch of D at Q_t (that branch cannot be a merge or a
puncture-move for the Y_t-copy y, so it is a STAY, whose constant value is Y_t and hence whose vertex is a
Y-vertex). ∎

**Why this does not yet close case (I).** T is only known to be *some* algebraic curve. If (and only if) the
vertex y of E_0 can be shown to be a "Teichmüller vertex" (positive area in the sense of PR-F, Lemma PA —
which locates positive area at a vertex of *maximal speed*, not necessarily at y), then T is a Teichmüller
curve; but even then a non-constant holomorphic Y : Δ → T is not absurd (T is uniformised by ℍ). To
contradict case (I) one needs genuinely new input at t = 0, excluding crossings: that is Open question 2 of
R7-2 §4.2. The local model recorded there (s_e = ρσ at the edges of x, s_f = ρ elsewhere, x-coordinate σ)
shows a crossing is consistent with (R1), (R2), (i), (ii) and with (Rig), so no local analytic (Krull-type)
argument at a single point can exclude it; and the planner's suggested route (Minsky product regions plus
non-existence of isometric bidiscs, Antonakoudis) is a statement about the interior geometry of V_0 near the
crossing that I was not able to make precise: the two directions at the crossing are a "Teichmüller-disc"
direction in the moving factor and a plumbing (cusp) direction, and total geodesy does force Teichmüller
discs in all mixed directions to lie in V_0 — but a Teichmüller disc in a mixed direction is not a product
direction, and the known rigidity theorems (no holomorphic isometric embedding of a bidisc into
Teichmüller space, Antonakoudis, cited from memory) apply to isometric *embeddings of the bidisc*, which is
not what the configuration produces. I record this as a dead end, not as a result.
