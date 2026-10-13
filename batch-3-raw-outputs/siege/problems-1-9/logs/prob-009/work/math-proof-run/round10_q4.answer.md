# round10_q4: attempt to refute MS10

**Status line.** I did not refute MS10, and I did not prove it either. The file contains:
- (§1) a proved statement about the logical status of MS10: given the chain, MS10 is *equivalent* to the problem's conclusion under (Rig). This answers the "vacuity" and "strength" questions of the brief, and it shows that any refutation must be a counterexample to the problem itself.
- (§2) a proved lemma (Lemma L) that makes the "level structure" mechanism B precise.
- (§3) a proved obstruction (Props. 3 and 4): mechanism B cannot work in the situation most likely to produce twins, namely covering-construction surfaces.
- (§4) the candidate-surface analysis, with the points where each attempt stopped.
- (§5) a summary of what is proved and what is open.

I re-checked only the statements of earlier rounds that I quote. The chain's PROVED entries are used as black boxes and are flagged where used.

---

## 1. MS10 is equivalent to the goal (under (Rig)); vacuity and strength

Write **Goal(Rig)** for the statement: *for every V_0, family V_t, stratum Δ_Γ and index i as in MS10's setting (smooth closed totally geodesic V_0; (R1), (R2), (Rig); dim ∂V_t = 1; π_i(∂V_t) = {Y_t}), t ↦ Y_t is constant.*

Write **MS10_w** for MS10 restricted to the pairs (β̃, b̃) and labels x that occur as a transition (β̃_m, β̃′_m, x_m) or as the endpoint (β̃, b̃, x) of a walk chain of Proposition K_w (entry 85), for the given family.

**Proposition 1.** Assume the PROVED entries 19, 24, 84–87 used in steps 2(a)–(d) of the chain. Then
 MS10 ⟺ MS10_w ⟺ Goal(Rig).

*Proof.*
- **MS10 ⇒ MS10_w.** MS10_w is a special case of MS10.
- **MS10_w ⇒ Goal(Rig).** This is chain step 2. Take a family with (Rig) and suppose Y is non-constant. Step 2(a) builds a walk chain. Step 2(b) is an induction along the chain:
  - at product-type transitions it uses entries 86/87;
  - at non-product transitions it uses MS10 only for the transition pair (β̃_m, β̃′_m, x_m), so MS10_w is enough.
 
 At the endpoint, step (c) (product type) or step (d) (MS10 at the endpoint pair, again covered by MS10_w) gives a contradiction. So Y is constant.
- **Goal(Rig) ⇒ MS10.** Every instance of MS10 has the hypothesis "t ↦ Y_t is non-constant" inside a setting to which Goal(Rig) applies. Under Goal(Rig) that hypothesis is never satisfied, so MS10 holds vacuously. ∎

**Consequences for the brief's test items.**
1. **Vacuity.** "MS10's hypotheses force Y constant" is *literally* Goal(Rig), i.e. the problem under (Rig). So a vacuity proof is a full solution under (Rig), and nothing weaker can come out of this route.
2. **Strength.** MS10 cannot fail "only at pairs no walk chain produces". Suppose MS10 fails for some family 𝔉. Then 𝔉 has Y non-constant, Goal(Rig) fails, and by the middle implication MS10_w fails *for 𝔉 itself*. The argument runs inside one family: the walk chain of 𝔉 must hit a non-product transition or endpoint where MS10 fails, unless a PROVED entry is wrong.
   - So no corrected, weaker missing statement of the form "MS10 at walk-chain pairs" changes the truth value. It can change only provability.
   - A genuinely weaker missing statement would have to replace "Y non-constant" by a *local* hypothesis. The brief already records that local hypotheses do not suffice (chart models: R7-3 §5, round9_q9 Lemma Loc).
3. **What a refutation needs.** A refutation of MS10 is exactly an admissible family satisfying (R1), (R2), (Rig) with Y non-constant. That is a counterexample to the problem under the run's readings, with the additional feature (forced by the chain) of a non-product twin point.
   - The problem is posed as a theorem. So a refutation is possible only if (a) the problem is false, or (b) the readings (R1)/(R2) are strictly weaker than the intended hypotheses. Reading (R2) is the coarse one: H_t need not preserve automorphism groups.
   - §3 shows that this coarseness is exactly where the twin mechanism lives.

---

## 2. Lemma L (positive-genus twins are separated by level structure)

**Set-up.** Let Q be a stable curve of genus g. Let c: S_g → Q be a collapse map that contracts disjoint simple closed curves γ_e (e ∈ E(G_Q)) to the nodes. For a component x of Q, let Σ_x ⊂ S_g be the closure of c^{-1}(x ∖ nodes). These are compact subsurfaces with pairwise disjoint interiors, and Σ_x has the genus of the normalisation of x.

**Lifts of automorphisms.** Every α ∈ Aut(Q) lifts to an orientation-preserving homeomorphism φ of S_g with c∘φ = α∘c, after isotopy. Construction:
- cut S_g along the γ_e;
- use α on the normalisations of the components, which is holomorphic and hence orientation preserving, and permutes the branch points of the nodes;
- extend across the collar annuli, compatibly with orientations.

The lift φ is unique up to isotopy and multitwists T_{γ_e}. A transvection T_{γ_e} fixes every homology class that has intersection 0 with all the γ_e. So the action of φ_* on classes supported in ⋃ int Σ_x is well defined.

**Lemma L.** Let m ≥ 2. Let α ∈ Aut(Q) have a lift φ with φ_* = id on H_1(S_g; Z/m). Then α(x) = x for every component x of Q of positive genus.

*Proof.*
1. Suppose α(x) = x′ ≠ x, where x has genus h ≥ 1. Then int Σ_x contains simple closed curves a, b with algebraic intersection a·b = 1.
2. φ maps Σ_x onto Σ_{x′} up to isotopy. So φ(a) can be isotoped into int Σ_{x′}, which is disjoint from int Σ_x ⊃ b. Hence φ_*[a]·[b] = 0.
3. But φ_*[a] ≡ [a] mod m, so φ_*[a]·[b] ≡ a·b = 1 mod m. This contradicts step 2 when m ≥ 2. ∎

**Remark.** Lemma L says nothing when g_i = 0, i.e. when Y_0 is an n_i-pointed rational curve with n_i ≥ 4. Mechanism B is therefore at best a positive-genus tool.

---

## 3. Where mechanism B stops: level covers do not trivialise the family when automorphism groups drop

**Cited facts (from memory).**
- **(Serre)** For m ≥ 3, an automorphism of a smooth curve of genus g ≥ 2 that acts trivially on H_1(X; Z/m) is the identity.
- **(Level cover)** The level-m cover M_g[m] → M_g (coarse) is the quotient map by Sp_{2g}(Z/m). It is a fine moduli space for m ≥ 3, and its fibre over [X] has exactly N/|Aut(X)| points, where N = |Sp_{2g}(Z/m)|. Indeed, Aut(X) acts freely on level structures by (Serre).
- Let M̄_g[m] be the normalisation of M̄_g in M_g[m]. It is finite over M̄_g.

**Proposition 3 (fibre-cardinality obstruction).** Let m ≥ 3. Suppose:
- a generic point of V_0 (outside a proper analytic subset) has automorphism group of order a_0;
- for some t, a generic point of V_t has automorphism group of order a_1 ≠ a_0.

Let 𝒱[m] be the preimage of 𝒱 in M_g[m] × Δ, and V_0[m] the preimage of V_0. Then no map H[m]: V_0[m] × Δ → 𝒱[m] over Δ is fibrewise bijective over H. Precisely, no map can satisfy both p∘H[m] = H∘(p × id) and "H[m]_t restricts to bijections p^{-1}(X) → p^{-1}(H_t X)". In particular the lifted family is not trivialised by any lift of H, and mechanism B ("topological triviality of 𝒱[m]") cannot be derived from (R2).

*Proof.*
- Let A_0 ⊂ V_0 and A_t ⊂ V_t be the proper analytic subsets outside which the automorphism order is a_0, resp. a_1.
- H_t is a homeomorphism V_0 → V_t, so V_0 ∖ (A_0 ∪ H_t^{-1}A_t) is non-empty (complement of a nowhere dense closed set).
- For X in that set, |p^{-1}(X)| = N/a_0 ≠ N/a_1 = |p^{-1}(H_t X)|. So no bijection exists. ∎

**Proposition 4 (covering constructions always fall under Prop. 3 or are trivial).** Let G be a nontrivial finite group, and let Z_G ⊂ M_g be the closed algebraic set of curves admitting a G-action of a fixed topological type. Suppose V_0 is an irreducible component of Z_G and Z_G has pure dimension 2. This is the situation of a covering construction whose image is a full component of its symmetric locus, as in the quintic example of PR-I, but the smoothness of V_0 is an extra assumption. Let
 T := {t ∈ Δ : V_t ⊂ Z_G}.
- If 0 is an accumulation point of T, then Y_t = Y_0 for all t.
- Otherwise, for all small t ≠ 0, V_t ⊄ Z_G, and the generic automorphism group of V_t does not contain the given G-action.

*Proof.*
1. V_t is homeomorphic to the connected manifold V_0, so V_t is irreducible. For t ∈ T, V_t is therefore an irreducible 2-dimensional analytic subset of Z_G, hence an irreducible component of Z_G (pure dimension 2). There are finitely many components.
2. By (R2), V_t → V_0 as t → 0, uniformly on compacts of V_0 via H_t. A component ≠ V_0 meets V_0 in a set of dimension ≤ 1, so it cannot contain H_t(K) for a fixed open K ⊂ V_0 and small t, because H_t(K) → K. Hence V_t = V_0 for t ∈ T near 0.
3. Then ∂V_t = ∂V_0 and Y_t = Y_0 on a set accumulating at 0. By the identity theorem for the holomorphic map Y (entry 19), Y ≡ Y_0.
4. Otherwise there is a punctured disc of t's with t ∉ T. ∎

**Conclusion of §3.**
- For covering-construction surfaces, which are the natural source of twins (the twins of PR-I are exchanged by the deck group), every non-trivial admissible family leaves the symmetric locus.
- If the generic automorphism order drops (a_1 < a_0), Prop. 3 forbids lifting H to level covers.
- So mechanism B, which in effect assumes that H transports the level structure, fails in exactly the case that matters. Lemma L stays true, but it applies only *after* a lift has been constructed, and that construction needs an automorphism-preserving transport (reading (R2+) below). That is not a hypothesis of the problem under the run's readings.

**Reading (R2+), recorded for the orchestrator.** Call (R2+) the reading in which H_t preserves the orbifold structure: Aut(H_t(P)) ≅ Aut(P) compatibly with the local charts. Under (R2+), the transport of labels in Def(Q) is Aut(Q)-equivariant. The twin ambiguity at non-product points then disappears: x persistent along β̃ and the joining paths transport the label through q^{-1}(V_0) ∩ B with a canonical identification at every time. I have not written out this deduction in full, so it is a sketch. If the intended meaning of "smoothly trivial" is an orbifold-smooth trivialisation, MS10 is presumably accessible under (R2+). Its failure mode lives only in the gap between (R2) and (R2+).

---

## 4. Candidate surfaces: where each refutation attempt stopped

**(a) Covering constructions over M_{0,5} (PR-I type).**
- *Twins.* Twins exchanged by the deck group occur at cusps, as in the quintic example.
- *Smoothness.* Smooth admissible V_0 of this type: not established. The quintic surface is singular (PR-I). I did not find a smooth one, nor prove that none exists.
- *Deformations.* By Prop. 4, any nontrivial deformation leaves Z_G. A counterexample needs V_t ⊄ Z_G satisfying (Rig). (Rig) means: every boundary piece of V_t has the *same* moving-image curve K as at t = 0, and only constant factors move.
- *Stopping point.* I found no mechanism producing a global algebraic family V_t, i.e. a family of algebraic surfaces in M̄_g (closure(V_t) is analytic in the projective M̄_g, hence algebraic by Chow), with all K's frozen and Y moving. Local models exist (round9_q9), but globalising them is the whole problem.

**(b) Pencil models.** Take a 3-fold Z̄ ⊃ V̄_0 in M̄_g and a pencil {s_0 + t s_1 = 0} that restricts on a boundary surface A × C ⊂ Δ_Γ to a pullback from the curve A ⊂ M_{g_i,n_i}. Such a pencil gives ∂V_t = {Y_t} × C with Y_t moving and no base points on A × C.
- *Why it fails as a counterexample to MS10.* By Prop. K (PR-H), V_0 has a MERGE/MOV branch somewhere in its boundary network. In a pencil model the piece carrying that branch is cut out by {s_0 + t s_1 = 0} on another boundary surface of Z̄. Its moving-image curve then varies with t unless s_0/s_1 is a pullback from the constant factors there too. So (Rig) fails generically.
- *What this shows.* These models are the natural candidate counterexamples to the *problem without (Rig)*. They are not counterexamples to MS10, because MS10 includes (Rig).
- *Stopping point.* I could not decide whether some (Z̄, pencil) has s_0/s_1 a pullback on *every* boundary surface while V̄_0 is totally geodesic and smooth. This is equivalent to Goal(Rig) failing in pencil form.

**(c) g = 3 and the hyperelliptic divisor (heuristic; the most promising arena for the "≥ 2-dimensional fixed component" requirement).**
- The failure mode needs, for every small τ ≠ 0, a curve Φ_τ ⊂ V_τ of α-symmetric curves accumulating at Q.
- If codim M_g^{[α]} ≥ 2, this is an excess intersection (expected dimension 2 − codim < 1), so it is non-generic.
- If codim M_g^{[α]} = 1, it is automatic as soon as V_τ ⊄ M_g^{[α]} and V_τ meets M_g^{[α]} near Q. By the dimension formula 3h − 3 + r for curves with an involution with quotient genus h and r branch points, the only codimension-1 involution loci occur for g ≤ 3. For g = 3 it is the hyperelliptic locus H_3 (dimension 5 = 6 − 1).
- Example of a totally geodesic surface inside H_3: the covering construction M_{0,5} → M_{0,8} (pull back by z ↦ z² branched at two of the five points) followed by the hyperelliptic double cover. This gives the curves y² = x(x² − a²)(x² − b²)(x² − c²).
- *Stopping points.* I did not check smoothness of this surface, nor the existence of non-product twin cusps exchanged by the hyperelliptic involution. I also could not produce a family satisfying (Rig).

**(d) EMMW flex and gothic loci** (cited from memory: Eskin–McMullen–Mukamel–Wright, primitive totally geodesic surfaces; I do not remember with certainty in which M_{g,n} each lives). I did not analyse their boundary for non-product twin points. Nothing is claimed.

---

## 5. Summary

**Proved here.**
- Prop. 1: MS10 ⟺ MS10_w ⟺ Goal(Rig), given the PROVED chain entries. So refuting MS10 = a counterexample to the problem with (Rig); proving MS10 by vacuity = proving the problem with (Rig); and weakening MS10 to walk-chain pairs changes nothing.
- Lemma L: automorphisms acting trivially on H_1(·; Z/m), m ≥ 2, fix every positive-genus component of a stable curve.
- Prop. 3: there is no fibre-bijective lift of H to level-m covers when the generic automorphism order of V_t differs from that of V_0.
- Prop. 4: for V_0 a component of a pure 2-dimensional symmetric locus Z_G, either Y is constant or V_t ⊄ Z_G for all small t ≠ 0.
- Together: mechanism B cannot be run under reading (R2) for covering-construction surfaces.

**Sketched only.** Under the orbifold reading (R2+), the twin ambiguity disappears (§3, last paragraph).

**Not achieved.**
- No counterexample to MS10.
- No contradiction derived from MS10.
- No proof of MS10.

**Open questions.**
1. (= Goal(Rig)) Does any admissible family with (Rig) have non-constant Y?
2. Does a smooth closed totally geodesic surface V_0 exist that has a non-product boundary point with twin Y_0-copies? Candidates: §4(a), (c), (d).
3. Is the intended reading of "smoothly trivial" (R2+)? If so, does MS10 follow from the chain data at non-product points? (§3, sketch.)
4. For g_i = 0 (rational Y_0), is there any replacement for Lemma L?

**Verdict: not proved, not refuted. Open.** Proposition 1 shows that the refutation task is equivalent to finding a counterexample to the problem itself under (Rig).

=== END OF ANSWER round10_q4 ===
