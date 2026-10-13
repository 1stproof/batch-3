# round14_q1: attempt on (NRT_P)

**Plan/status line.** I re-check the derivation (NRT_P) ⇒ MS8 (round13_q5), then look for a global argument for (NRT_P), starting with case (A) of the planner's split. **Outcome: NOT PROVED, no counterexample.**

This file contains:
- §1: a re-check of round13_q5. I found no flaw. There is one genericity point in Lemma 1, step 2, and it is harmless; I repair it.
- §2: a proved structural lemma (Lemma A). At t = 0, a "split lifted family" through a generic point of a lifted piece can only come from a graph automorphism that fixes that lifted piece pointwise.
- §3: what Lemma A gives for case (A), and why it does not close case (A). The planner's claim "a failure in case (A) needs W ≠ σW" depends on how vertices are named. With the a-transported naming, W′ = W always, and no contradiction appears.
- §4: open items.

Readings: (R1) and (R2) with H_0 = id, in the coarse reading. (R2^orb) is not used. Standard facts are cited from memory and named where they are used.

---

## 1. Re-check of the derivation (NRT_P) ⇒ MS8

**Lemma 1, step 2 (genericity).** The step needs points p_n ∈ T_t, near p_* and off Λ_t, such that Π(p_n) ∈ W. By (I4), Π maps only a *dense open* subset T° ⊂ T into W.
- T ∖ T° is analytic of dimension ≤ 1.
- So its t-slices are finite for all t outside a discrete set Z′.
- For t ∉ Z′, the points of T_t ∖ Λ_t near p_* can be taken in T°, and the argument goes through as written.
- For t ∈ Z′: the conclusion "the image of λ_y lies in the closed analytic curve 𝒢" holds on L ∖ (Z′-fibres). Since 𝒢 is closed, it holds on all of L.

So Lemma 1 stands.

**Lemmas 2 and 3, Prop. 4, Lemma 5.** I re-read them and found no gap beyond what depends on the cited inputs (I1)–(I6), which I did not re-derive. In particular:
- In Prop. 4 the last clause is correct. x is intact on T′ ⊃ c̃′ × {0}, and its value lies on a branch ψ of a curve that is finite over Δ, whose t = 0 slice is the single point Y_0.
- In Lemma 5 the irreducibility argument is correct. It excludes a constant branch of an irreducible Γ that contains a non-constant branch.

So the derivation holds, modulo (I1)–(I6) and (Rig).

---

## 2. Lemma A (split lifted families come from pointwise stabilisers)

**Setting.**
- c is a piece of B_0 in a stratum Δ_{G_c}.
- ξ: ∏_{w∈V(G_c)} M_w → Δ_{G_c} is the finite quotient by Aut(G_c) on coarse spaces (cited from memory: the stratum is the quotient of the product by the graph automorphisms).
- 𝒞 := H((c ∖ punctures) × Δ_ε) ⊂ Δ_{G_c} × Δ_ε is the coarse piece family. It is analytic of dimension 2, by (R1), (R2) and (i).
- E is an irreducible component of ξ^{-1}(c_0), and e ∈ E is a generic point.

**Lemma A.** Let W and W′ be irreducible components of (ξ × id)^{-1}(𝒞) that both contain (e, 0). Then W′ = kW for some k ∈ Aut(G_c) that fixes E pointwise. Moreover, if W′ ≠ W, then every curve of c_0 near ξ(e) has a non-trivial automorphism induced by k. This automorphism permutes components according to k, and in particular it swaps two vertices whose value curves differ: Γ_{W,w} ≠ Γ_{W,kw} for some w.

*Proof.*
1. *𝒞 is locally irreducible at (ξ(e), 0).*
   - c is an irreducible curve, so it is smooth at the generic point ξ(e). H is a homeomorphism from c × Δ_ε onto 𝒞 near this point, so 𝒞 is a topological 4-manifold there.
   - Suppose the germ were reducible: 𝒞 = 𝒞_1 ∪ 𝒞_2, with no inclusion between the two.
   - Then Z := 𝒞_1 ∩ 𝒞_2 has complex dimension ≤ 1, hence covering dimension ≤ 2 in a 4-manifold.
   - The complement of such a closed set in a connected open subset of the manifold is connected (standard: a set of codimension ≥ 2 does not separate).
   - But that complement is the disjoint union of the non-empty open sets 𝒞_1 ∖ Z and 𝒞_2 ∖ Z. This is a contradiction.
2. *Local form of ξ.* Near e, ξ × id is the quotient by the finite group Stab(e) ⊂ Aut(G_c).
3. *Components above an irreducible germ.*
   - Each irreducible component of the preimage maps onto the germ: the map is finite and open, the image has the same dimension, and the germ is irreducible.
   - The group acts transitively on fibres.
   - Take a generic point of the germ. Its preimages are smooth points of the preimage, each lying on exactly one component.
   - Hence the components through (e, 0) form one Stab(e)-orbit, and W′ = kW with k ∈ Stab(e).
4. *k fixes E pointwise.* For each k ∈ Aut(G_c), the fixed set {e : ke = e} is analytic. For generic e ∈ E, ke = e therefore holds iff k fixes E pointwise.
5. *The automorphism of the curves of c_0.* If k fixes e = (pointed curves C_w)_w, then C_{kw} ≅ C_w as pointed curves, compatibly with the node pairing. So k induces an automorphism of the glued stable curve ξ(e).
   - If W′ = kW ≠ W, then k acts non-trivially on vertices with different value curves. Otherwise kW and W would agree in every coordinate's value curve, and kW = W would follow from the product structure K_W × {c_t} of (I4).
   - In that case the automorphism of ξ(e) is non-trivial. ∎

**Remark (the coarse phenomenon behind it).** In case W′ = kW ≠ W, the automorphism induced by k on the curves of c_0 is lost along c_t for generic t ≠ 0, because Γ_{W,w}(t) ≠ Γ_{W,kw}(t). This is the "lost automorphism" of rounds 12 and 13, now spread along the whole boundary piece rather than sitting at an isolated point. It is allowed by the coarse reading (R2) and excluded by (R2^orb).

---

## 3. Case (A): what Lemma A gives, and why it does not settle the case

**Setting.** Case (A) of the planner's split:
- along L ⊂ T, with T a boundary-type anchored sheet whose lifted family component is W, the label x is a constant vertex u of W, with Γ_{W,u} ⊇ φ non-constant;
- y = a^{-1}x is a constant vertex v of W, with Γ_{W,v} ≡ {Y_0} × Δ.

**Observation 1 (naming).**
- Use for ac̃ the vertex naming obtained from that of c̃ by transport under a. By (K3), for p ∈ T the curves at p and at ap are isomorphic, and the transported names of the components agree.
- So Π(ap) = Π(p), and aT has the **same** lifted component W.
- Under this naming, along aL ⊂ aT the label x corresponds to v, with value ≡ Y_0, and the label ax corresponds to u, with value φ(t). This is fully consistent and contains no contradiction.
- With a *fixed* naming one gets instead σW, with σ ∈ Aut(G_c) the change of naming. Whether σW = W depends on that bookkeeping, not on geometry.

So the planner's sketch item 2 ("a failure in case (A) needs W ≠ σW") is not an invariant statement. As written it does not yield a contradiction in the case σW = W either: the vertices u, v of W simply have different value curves, and a does not act on W.

**Observation 2 (what would be needed).** A contradiction in case (A) would need a *global* identification of u with v. For example: some k ∈ Aut(G_c) fixing the lifted piece E pointwise with kW = W and ku = v. That would give Γ_{W,u} = Γ_{W,v}, which is impossible because one branch is non-constant and the other is ≡ Y_0.
- At Q we only know that a ∈ Aut(Q) exchanges the labels. Aut(Q) can be strictly larger than the image of Stab_pt(E) at Q: Q is a puncture, a deeper point.
- Nothing proved so far forces the swap at Q to extend to an automorphism of the generic curve of c_0.
- Lemma A shows that *if* it extends, i.e. if a is induced near Q by some k ∈ Stab_pt(E), then either kW = W, which gives the contradiction above, or kW ≠ W, which is the split-family situation with the automorphism lost along all of c_t.
- Excluding the split family globally (using total geodesy of V_0, smoothness of V_0, (Rig), and Y non-constant) is the remaining question for this sub-case. I could not do it.

**Case (B)** (y is a component of a cusp of K_W, with Y_0 ∈ 𝔉_W). Not treated beyond the round-13 record. By Lemma NG (round13_q7), any argument has to combine t = 0 data with a t ≠ 0 input.

---

## 4. Summary

**Proved:**
- The derivation (NRT_P) ⇒ MS8 of round13_q5 re-checked: no flaw found. One harmless genericity point in Lemma 1, step 2 is repaired (§1).
- Lemma A (§2): components of the lifted piece family that pass through a generic point of a lifted t = 0 piece form one orbit under the pointwise stabiliser of that lifted piece. A genuine split forces an automorphism of every curve of c_0 that is lost at generic t ≠ 0.
- Observation 1 (§3): the "W ≠ σW" criterion of the planner's sketch depends on the naming. With the a-transported naming, the anchored sheets T and aT carry the same W, and case (A) gives no contradiction by itself.

**Not proved:** (NRT_P), in either case (A) or case (B). No counterexample is given.

**Open questions (named):**
1. (A-ext) In case (A): must the label swap a at the puncture Q be induced by an automorphism of the generic curve of the piece c_0, i.e. by some k ∈ Stab_pt(E)? If it is, and if moreover kW = W, then case (A) is excluded.
2. (Split) Can a smooth closed totally geodesic V_0 admit a deformation satisfying (R1) and (R2) in which a boundary piece's lifted family splits (kW ≠ W, Lemma A), i.e. the curves of c_0 have an automorphism that is lost along c_t?
3. Case (B), as in the planner's sketch item 3.
4. (Rig) (entry 82), unchanged.

Verdict: **not proved** (open).

=== END OF ANSWER round14_q1 ===
