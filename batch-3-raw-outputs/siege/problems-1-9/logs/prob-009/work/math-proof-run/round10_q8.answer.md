# round10_q8 — MS10: derivation of the claim, and a structural finding

**Status / plan.** (1) Derive the problem's claim from MS10 + cited statements (done below, with two flagged points). (2) Name of first move on MS10: **arithmetic (fields of definition)**. It is a dead end; §2.1 says why. (3) The main finding, a **symmetry argument**, is in §2.2. In the swap-symmetric twin case MS10 is *equivalent* to the problem's own conclusion for that V_0, and MS10 is false for local germs. So MS10 is genuinely global and is no easier than the problem in exactly the twin case it was meant to handle. Final: **not proved** (MS10 remains open; no refutation).

## 1. MS10 + cited statements ⇒ the problem's claim

Assume, for a contradiction, that t ↦ Y_t is non-constant. By entry 19 it is holomorphic. We work under (R1), (R2), (Rig) with H_0 = id.

**Step 0 (start).** Take a generic point of ∂V_0, and let D^1 ⊂ ∂V_0 be the piece containing it. Let x be the vertex-i label.
- By (R2), H maps (closure(V_0) ∩ Δ_Γ) × Δ onto closure(𝒱) ∩ (Δ_Γ × Δ).
- So every point of the transport family of a lifted branch of D^1 lies over ∂V_t.
- Since Δ_Γ is of product type and π_i(∂V_t) = {Y_t}, vertex x is intact there with F_x ≅ Y_t.
- Hence x is Y-persistent along every lifted branch of D^1. Entry 24 gives the same at limit points.

**Step 1 (walk chain).** Proposition K_w (entry 85) gives:
- a chain of pieces D^1, …, D^k;
- transition points J_1, …, J_{k−1}, each with a chart label x_m that is the constant region ≅ Y_0 on both sides;
- an incoming lifted branch and an outgoing lifted branch at each J_m, joined by lifted interior paths inside a small chart ball — exactly the "joined inside the chart" hypothesis of MS10;
- an endpoint Q_0 with a terminal lifted branch along which x MERGES or MOVES at t = 0.

**Step 2 (propagating persistence).** Induct along the chain. Suppose x_m is Y-persistent along the incoming branch at J_m.
- *J_m in a non-product stratum.* MS10, applied to (β̃ = incoming, b̃ = outgoing, x = x_m), gives Y-persistence along the outgoing branch.
- *J_m in a product-type stratum.* By Lemma PT (entry 86), no automorphism moves a positive-dimensional vertex, so the alignment element g′ of entry 87 fixes the label. Lemma T/S (entry 87) says persistence is constant on whole components of the boundary total space, and both branches transport into one component. So persistence transfers.
- *Flag A:* this product-type step relies on the cited statements in the exact form quoted; I cannot check their proofs.
- In either case, persistence then spreads along the whole next piece D^{m+1} (entry 87: constant on components).

**Step 3 (endpoint).** At Q_0, persistence passes in the same way from the incoming branch to the terminal branch:
- by MS10 if Q_0 is non-product;
- by Lemma PT + entry 87 if Q_0 is of product type. In that case Theorem R (entry 87), for terminal MERGE or puncture-MOV, also applies directly. Entry 86 says an interior-MOV endpoint never lies in a product stratum.

**Flag B:** the terminal lifted branch must be joined inside the chart to the incoming one. I read entry 85 as providing this (the ray's lifted path continues inside the chart ball), but the quoted statement says it explicitly only for transitions.

Persistence at t = 0 along the terminal branch says x is intact and F_x ≡ Y_0 along it. This contradicts MERGE (an edge at x is unpinched, so x is not intact) and MOV (F_x is non-constant). Hence Y is constant, i.e. π_i(∂V_t) = {Y_0}. ∎ (modulo Flags A and B, MS10, and (Rig))

The hypothesis "Y non-constant" of MS10 is in force throughout, since the argument is by contradiction. So the derivation goes through.

## 2. Attack on MS10

### 2.1 First move: arithmetic (fields of definition)

Totally geodesic subvarieties of M_g are defined over Q̄. (Cited from memory: this follows from the Eskin–Mirzakhani–Mohammadi / Filip results that orbit closures are algebraic and defined over Q̄. Teichmüller curves: McMullen.)

So closure(V_0), its boundary strata and Y_0 are defined over Q̄. This constrains only t = 0. V_t for t ≠ 0 is an arbitrary holomorphic deformation, and nothing arithmetic singles out Y_t. A countability argument works only if every V_t is totally geodesic, which entry 93 already uses.

**Dead end:** arithmetic sees only t = 0, and MS10 is a statement coupling t = 0 data with the deformation. (§2.2 shows its t = 0 content is itself global.)

### 2.2 The symmetric-sheet reduction (main finding)

**Lemma E (equivariance of transport).**
- *Claim.* For σ ∈ Aut(Q) and a lifted branch β̃: σ(Ñ_β̃) = Ñ_{σβ̃} (σ acting on the Def(Q) factor). Also F_y(σp) ≅ F_{σ^{-1}y}(p) for every label y.
- *Consequence.* x is Y-persistent along σβ̃ iff σ^{-1}x is Y-persistent along β̃.
- *Proof.* B is Aut(Q)-invariant and q∘σ = q. So the set q^{-1}(H((β∖Q)×Δ_ε)) ∩ (B×Δ_ε) is σ-invariant, and σ maps its component containing β̃∖0 to the one containing σβ̃∖0. The label statement is the definition of the induced relabelling. ∎

**Lemma J (σ-stable sheets give joined pairs).**
- *Claim.* Let S ⊂ B be a locally irreducible germ (a sheet of q^{-1}(closure(V_0))) with σS = S, and let β̃ be a boundary branch of S. Then β̃ and σβ̃ are joined inside the chart in the sense of MS10.
- *Proof.* S ∩ q^{-1}(B_0) is a proper analytic subset of the irreducible germ S. The complement of a proper analytic subset in a locally irreducible germ is connected (after shrinking to a good representative). That complement lies in q^{-1}(V_0) and accumulates on both β̃∖0 and σβ̃∖0. ∎

**Proposition T (MS10 in the twin case is the problem itself).**
- *Setting.* Let Q be non-product and σ ∈ Aut(Q) with σS = S as in Lemma J. Suppose x is Y-persistent along β̃, and the twin label x' := σ^{-1}x is *not* intact-and-constant along β̃ at t = 0. (The natural twin picture: x frozen ≅ Y_0, its isomorphic twin x' moving or merging.)
- *Claim.* Then MS10 (whose hypotheses hold by Lemma J) forces the contradiction "Y non-constant is impossible", i.e. Y ≡ Y_0.
- *Proof.* MS10 for the pair (β̃, σβ̃) gives that x is persistent along σβ̃. By Lemma E, x' is then persistent along β̃, so at t = 0 x' is frozen along β̃, contradicting the assumption. ∎

So for any V_0 that has such a σ-stable twin configuration, MS10 is *equivalent* to the problem's conclusion for that V_0. MS10 is no easier than the original problem in the twin case.

**Remark (MS10 is not local).** The local deformations of Lemma Loc (entry 93) can be expected to extend σ-equivariantly at a twin point Q: deform S to σ-stable germs S_t in which x is frozen at Y_t along β̃_t and x' at Y_t along σβ̃_t, with Y_t moving. Such germs would violate MS10's conclusion. I have not checked that the automorphism hypothesis of Lemma Loc holds at non-product points, so this is plausible rather than proved. If it holds, any proof of MS10 must use global information about V_0: the Teichmüller-disc structure of pieces (entry 70), or compactness / intersection theory of closure(V_t). It cannot come from chart analysis.

**Plausibility.** This does not make MS10 implausible: it may hold because such configurations force Y constant globally. But it shows MS10 should be attacked as "global twin rigidity", not as a local lemma.

### 2.3 What remains open
- **MS10 itself.** Equivalently, in the twin case, the claim for V_0 admitting a σ-stable sheet whose two branches have swapped frozen/moving twins.
- **(Rig)** (entry 82).
- **Flags A and B** of §1.
- **Whether σ-stable twin sheets occur at all** in closure(V_0) for some totally geodesic surface V_0. If they provably cannot, MS10's twin case is vacuous and only non-symmetric joined pairs remain.

**Outcome: not proved** (derivation of the claim from MS10 done modulo Flags A/B; MS10 open, shown to be global and, in the twin case, equivalent to the problem).

=== END OF ANSWER round10_q8 ===
