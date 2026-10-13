# round9_q7 — answer (MS8)

**Status: PARTIAL.** I do not prove MS8 in full and I do not give a counterexample. What I do:
- I prove three structural lemmas (T, S, J) from (R1), (R2) and (Rig).
- From them I get a reduction (Theorem R): MS8 holds unless the Prop K track meets one of two explicitly described configurations, (R-tw) "twin switch" and (R-cr) "interior MOV crossing".
- Both residual configurations stay OPEN. Inside the reduction they are the precise forms of the chain's "residual twins" and "residual crossings".

New compared with the round-8 material:
- **Lemma T.** H transports each piece into a single irreducible component of the boundary total space, both globally and locally at a point. The proof uses a non-separation argument from dimension theory. Before this, transport through crossings was not controlled.
- **Lemma S.** Under (Rig), a component of the boundary total space has the same non-constant vertex set M and the same curve K on *every* fibre, including t = 0.
- **Consequence.** A "crossing" can occur only at a twin switch or at the final branch of the track. It cannot occur in the middle of an aligned track.

Readings: (R1), (R2) as in the task, with H_0 = id. (Rig) as in MS8. Throughout, F denotes the finite set of pointed curves (with all orderings of special points) that occur as a smooth component of some coordinate of some point of K ∩ ∂(∏_{u∈M} M̄_u), for (G,M,K) ∈ 𝒦. It is finite because 𝒦 is finite and each K is an irreducible curve not contained in the boundary.

**Pinning principle (P).** If Y_t ∈ F for all t in a nonempty open set U ⊂ Δ, then Y ≡ Y_0.

*Proof.* Y is continuous and takes values in a finite set on a connected open subset of U, so it is constant there. By holomorphy (PR-A) and the identity theorem, which applies in an orbifold chart, Y is constant on Δ. ∎

## 1. Notation

- ℬ := closure(𝒱) ∩ (∂M̄_g × Δ). By (R1) it is analytic. By (R2) it is homeomorphic over Δ to B_0 × Δ, hence of pure dimension 2.
- Every irreducible component of ℬ dominates Δ, since fibres are 1-dimensional. So by Krull every fibre of every component is pure 1-dimensional.
- For a stratum Δ_G put ℬ_G := ℬ ∩ (Δ_G × Δ). This is an analytic subset of Δ_G × Δ.
- A *component of ℬ_G* means an irreducible component of ℬ_G. It has dimension 2, because H maps (B_0 ∩ Δ_G) × Δ onto it and B_0 ∩ Δ_G is 1-dimensional or empty.
- A *piece* at time 0 is an irreducible component E of B_0 ∩ Δ_G.

## 2. Lemma T (transport respects components)

**Lemma T.** Let E be a piece at time 0 in Δ_G.
(a) There is a unique component κ(E) of ℬ_G with H(E × Δ) ⊂ κ(E).
(b) Every component 𝒲 of ℬ_G satisfies 𝒲 = ∪_{κ(E)=𝒲} H(E × Δ). In particular 𝒲_0 = ∪_{κ(E)=𝒲} E, and a piece E lies in 𝒲_0 iff κ(E) = 𝒲.
(c) (Local version.) Let Q ∈ B_0 and let β be a branch at Q of a piece E. Let ℬ^{(1)}, …, ℬ^{(m)} be the local irreducible components at (Q,0) of the germ of ℬ_{G_β} ∪ {deeper strata}, i.e. of ℬ. For a small closed sub-branch β′ ∋ Q and a small disc D ∋ 0, H(β′ × D) lies in exactly one ℬ^{(k(β))}. Hence (H_t(Q), t) ∈ ℬ^{(k(β))} for t ∈ D. Moreover ℬ^{(k(β))} is a local component at (Q,0) of closure(κ(E)).

*Proof.*
1. Let E° be E minus the singular points of the analytic set B_0 ∩ Δ_G. This removes finitely many points of E. E° is a connected real 2-manifold, because E is irreducible and its regular locus minus a finite set is connected. So E° × Δ is a connected real 4-manifold.
2. Let Σ := Sing(ℬ_G). This includes all pairwise intersections of components. It is analytic of complex dimension ≤ 1, so its covering dimension is ≤ 2.
3. H^{-1}(Σ) ∩ (E° × Δ) is closed in E° × Δ and homeomorphic to a subset of Σ, so its dimension is ≤ 2 = 4 − 2.
4. Cited from memory (Hurewicz–Wallman, *Dimension Theory*, Thm IV 4): a closed subset of dimension ≤ n − 2 does not separate a connected n-manifold. So R := (E° × Δ) \ H^{-1}(Σ) is connected.
5. H(R) is a connected subset of Reg(ℬ_G). Each connected component of Reg(ℬ_G) lies in exactly one irreducible component. So H(R) lies in one component 𝒲 = κ(E).
6. R is dense in E × Δ, since a closed set of dimension ≤ 2 has empty interior in a 4-manifold, and E° is dense in E. Taking closures in Δ_G × Δ gives H(E × Δ) ⊂ 𝒲, because 𝒲 is closed there. Uniqueness: H(R) is not contained in Σ. This proves (a).
7. For (b), let x ∈ 𝒲 lie on no other component. By (R2), x = H(e,t) with e in some piece E′ of B_0 ∩ Δ_G. By (a), H(E′ × Δ) ⊂ κ(E′), and x is on no other component, so κ(E′) = 𝒲. So 𝒲 \ (other components) ⊂ ∪_{κ(E′)=𝒲} H(E′ × Δ).
8. The right-hand side is closed in Δ_G × Δ: it is a locally finite union of images of the relatively closed sets E′ × Δ under the homeomorphism H. The left-hand side is dense in 𝒲. This gives (b). If E ⊂ 𝒲_0 = ∪_{κ(E′)=𝒲} E′, then E = E′ for one of them, by irreducibility.
9. (c) is the same argument. Replace E° × Δ by β°′ × D, where β°′ = β′ \ {Q} is a punctured disc. Replace Σ by the singular locus of the germ union the pairwise intersections of the ℬ^{(k)}. Continuity of H at (Q,0) keeps H(β′ × D) inside a representative neighbourhood. Then (H_t(Q),t) ∈ closure(H(β°′ × {t})) ⊂ ℬ^{(k(β))}. The last claim holds because H(β′ × D) ⊂ κ(E). ∎

**Remark.** Lemma T is exactly what is needed to transport "which sheet" a branch lies on, using only the coarse homeomorphism H. It does not give vertex labels: H says nothing about the action of Aut(Q). That is where twins enter.

## 3. Lemma S (structure of components under (Rig))

Let 𝒲 be a component of ℬ_G. Let 𝒲̃ be an irreducible component of its preimage in ∏_{w∈V(G)} M_w × Δ; this is a finite map, and the preimage is permuted by Aut(G). Write f_u for the coordinate maps.

**Lemma S.**
(a) There are a set M = M(𝒲) ⊂ V(G) and an irreducible curve K = K(𝒲) with (G,M,K) ∈ 𝒦 such that:
- for every t, every 1-dimensional irreducible component E of 𝒲̃_t has M(E) = M and K(E) = K;
- t = 0 is included.
(b) For u ∉ M, the map (f_u, t): 𝒲̃ → M_u × Δ has 1-dimensional image 𝒞_u. So f_u is constant on each connected component of each fibre 𝒲̃_t, taking finitely many values c_u(t) that vary in t as a multivalued holomorphic function.
(c) Let x ∉ M. Suppose f_x ≅ Y_t (as pointed curves, some ordering) on a subset of 𝒲̃ of real dimension 4. Then it holds on all of 𝒲̃.

*Proof.*
1. Let M be the set of u such that f_u is non-constant on the components of the generic fibre. For u ∉ M, the image of (f_u,t) is 1-dimensional: its fibres over t are finite for generic t, and it is irreducible. So the image is a curve finite over Δ near generic points. Its closure meets each {t} in a discrete set, for every t, because the image is an irreducible curve that is not a vertical line. A vertical line would need f_u to be non-constant on fibre components. So f_u takes finitely many locally constant values on 𝒲̃_t for every t. This is (b).
2. By (Rig), for generic t the pieces of 𝒲̃_t carry curves from the finite set 𝒦. So by irreducibility and continuity one K works for all generic t, and 𝒲̃ maps into K × ∏_{u∉M} M_u × Δ (a closed condition), for all t.
3. Let E be any 1-dimensional component of a fibre, including t = 0. By (b), the vertices u ∉ M are constant on E. Since E is 1-dimensional, its image in K is not a point, hence it is dense in K. Each u ∈ M has non-constant projection on K, by the definition of M. So M(E) = M and K(E) = K. This is (a).
4. (c): {p ∈ 𝒲̃ : f_x(p) ≅ Y_{t(p)}} is analytic, since Y is holomorphic. An analytic subset of an irreducible 2-dimensional space that has real dimension 4 is the whole space. ∎

**Definition (persistent).** Call 𝒲 *persistent* if its generic points have a Y_t-copy. Equivalently, by S(c) and the Lemma D(1) argument, some vertex x ∉ M(𝒲) has f_x ≡ Y_t on 𝒲̃. Such an x is a *persistent vertex*.
- Every component κ(E), with E a component of ∂V_0, is persistent with persistent vertex i: H_t(E) ⊂ ∂V_t, and vertex i of ∂V_t is Y_t.
- Locally at a point (Q,0) with Q ∈ Δ_{G_Q}: let 𝒲̃^a be a germ component of the preimage of closure(𝒲) in Def(Q) × Δ. If 𝒲 is persistent, there is a vertex y_a of G_Q such that all edges at y_a are identically 0 on 𝒲̃^a and z_{y_a} ≅ Y_t on 𝒲̃^a.
  - Proof: limits of smooth Y_t-copies at nearby points are smooth, so as in Lemma D(1) the copy comes from a single intact vertex. Finitely many vertices cover the irreducible germ, so one vertex works everywhere on it.

## 4. Lemma J (junction trichotomy)

**Setting.**
- Q ∈ B_0 lies in Δ_{G_Q}.
- β is a branch at Q of a piece E. Let 𝒲̃^a be a germ component at (0,0) ∈ Def(Q) × Δ of the preimage of ℬ^{(k(β))}, containing a lift β̃ of β. Assume 𝒲̃^a has persistent vertex x.
- b is another branch at Q, of a piece E″ in stratum Δ_{G″}. Let 𝒲̃″ be a germ component of the preimage of ℬ^{(k(b))} containing a lift b̃ of b.
- U_b := the edges of G_Q that are not identically 0 on b̃. Then G″ = G_Q / U_b.
- Write [y] for the vertex of G″ containing y.

**Lemma J.** There are g′ ∈ Aut(Q) and a nonempty open set U ⊂ Δ \ {0} near 0 such that, with x̂ := g′^{-1}x, exactly one of the following holds.
- **(J1) pinned:** Y_t ∈ F for t ∈ U. Hence Y ≡ Y_0 by (P). This happens whenever, along b̃ (equivalently, generically on 𝒲̃″), x̂ is merged, i.e. [x̂] ≠ {x̂}. It also happens whenever [x̂] = {x̂} ∈ M(κ(E″)) and U_b ≠ ∅ (puncture-move).
- **(J2) persistent:** [x̂] = {x̂} ∉ M(κ(E″)). Then x̂ is a persistent vertex of 𝒲̃″, so κ(E″) is persistent.
- **(J3) crossing:** U_b = ∅, so b lies in the stratum of Q and Q is an interior point of E″, and x̂ ∈ M(κ(E″)).

*Proof.*
1. **Finding g′ and U.** Put Q_t := H_t(Q). By Lemma T(c), (Q_t,t) ∈ ℬ^{(k(β))} ∩ ℬ^{(k(b))} for t ∈ D. The preimage of ℬ^{(k(β))} is ∪_g g𝒲̃^a, because Aut(Q) permutes the preimage components of an irreducible germ transitively, and similarly for ℬ^{(k(b))}.
   - For g, h ∈ Aut(Q), let T_{g,h} := {t ∈ D* : some lift of Q_t lies in g𝒲̃^a ∩ h𝒲̃″}. These are finitely many sets covering D*.
   - Each is closed in D*: lifts of Q_t stay in a compact neighbourhood of 0, since the preimage of Q is {0}.
   - By Baire, some T_{g,h} has interior. Put g′ := g^{-1}h. Then for t in an open set U there is q_t ∈ 𝒲̃^a ∩ g′𝒲̃″ over (Q_t,t).
   - Shrink U to avoid the discrete set of t over which some germ component has a fibre component inside a deeper stratum. Then for t ∈ U, q_t is a limit of points of the fibre at t of g′𝒲̃″ that lie in the generic stratum Δ_{G″} (relabelled by g′).
2. **At q_t.** Since q_t ∈ 𝒲̃^a, vertex x is intact at q_t and z_x(q_t) ≅ Y_t. On g′𝒲̃″ the role of x is played by the vertex x̂ = g′^{-1}x of 𝒲̃″. So in what follows, "x on g′𝒲̃″" is "x̂ on 𝒲̃″".
3. **Merged.** Suppose [x̂] ≠ {x̂}.
   - (i) [x̂] ∈ M″. If not, the [x̂]-coordinate is constant, equal to c, a smooth curve, on fibre components at t. Its limit at q_t is the curve assembled from the components in [x̂]. That curve contains an edge at x̂, which is pinched at q_t because x is intact there, so it is nodal and differs from c. Contradiction.
   - (ii) So the limit at q_t of the M″-coordinates is a point of K(κ(E″)) whose [x̂]-coordinate is nodal. That is a point of K ∩ ∂, and z_x(q_t) ≅ Y_t is a smooth component of it. Hence Y_t ∈ F. This is (J1).
4. **Puncture-move.** Suppose [x̂] = {x̂} ∈ M″ and U_b ≠ ∅. Some edge e ∈ U_b lies inside some vertex group [w] of G″. As in step 3(i), [w] ∈ M″. So the limit point of K at q_t lies in K ∩ ∂, and its x̂-coordinate is z_x(q_t) ≅ Y_t. Hence Y_t ∈ F. This is (J1).
5. **Constant.** Suppose [x̂] = {x̂} ∉ M″. By Lemma S(b), z_x is constant on the fibre components of g′𝒲̃″ through q_t, and q_t lies in the closure of their generic part. So the constant is z_x(q_t) ≅ Y_t, for every t ∈ U. The union of these fibre components over t ∈ U has real dimension 4. By S(c), applied to the germ and then to the global irreducible component, x̂ is persistent on 𝒲̃″ and κ(E″) is persistent. This is (J2).
6. **The remaining case** is [x̂] = {x̂} ∈ M″ with U_b = ∅, which is (J3).
7. **Generic behaviour equals behaviour along b̃.** The generic points of b̃ and of 𝒲̃″ lie in the same stratum Δ_{G″}, because E″ ⊂ κ(E″)_0 ∩ Δ_{G″}. So U_b is the set of edges not identically 0 on 𝒲̃″. By Lemma S(a), the piece E″ has M(E″) = M(κ(E″)). So "x̂ merged / moving / constant along b at t = 0" coincides with the generic behaviour on 𝒲̃″. ∎

**Corollary J′ (aligned junctions).** In Lemma J, suppose x̂ = x, i.e. g′ fixes the vertex x. Suppose also that x is intact and constant along b at t = 0, as happens in the middle of a Prop K track. Then (J2) holds with persistent vertex x on 𝒲̃″ ⊃ b̃.
- (J3) cannot occur: x constant along b implies x ∉ M(κ(E″)), by Lemma J step 7.
- (J1) cannot occur either: under the hypothesis x is neither merged nor moving along b.

So **in an aligned track, crossings never occur in the middle**. They can occur only at a non-aligned junction (g′x ≠ x) or at the terminal branch.

## 5. Theorem R (reduction of MS8)

**Input from Prop K (PR-H §3), used as stated there, "modulo routine marking details".**
- There is a compact connected K_0 ⊂ B_0 containing a generic point P of ∂V_0, and a point Q_0 ∈ K_0 with a terminal branch b_* of type MERGE or MOV.
- The labeled Σ_i-vertex x is intact and ≅ Y_0 along K_0, consistently with the path marking.
- A closed connected subset of the finite topological graph B_0 is path-connected through finitely many vertices. So there is an embedded arc in K_0 from P to Q_0, passing through finitely many junction points Q_1, …, Q_r. At each Q_k the arc arrives along a branch β_k and leaves along a branch b_k. Lifts β̃_k, b̃_k carry the *same* labeled track vertex x; this is the marking consistency.
- Inside a piece the persistent vertex does not change. By Lemma S(c) it is a global property of the lifted component κ(E) with the labeling of E.

**Definitions.**
- A junction (including the terminal point Q_0 with b = b_*) is *aligned* if, in Lemma J applied with x the track vertex, some admissible g′ fixes x.
- Otherwise it is *non-aligned*. Then g′x ≠ x for every admissible g′, so x and x̂ = g′^{-1}x are two distinct components of Q exchanged by an automorphism of Q. These are twins in the sense of PR-I.

**Theorem R.** Assume (R1), (R2), (Rig) and the conclusion of Prop K. Suppose every junction Q_1, …, Q_r is aligned, Q_0 is aligned, and the terminal branch b_* is MERGE or MOV with b_* not contained in the stratum of Q_0 (puncture-MOV). Then Y_t = Y_0 for all t.

*Proof.*
1. **Base.** The arc starts in a component of ∂V_0, whose κ is persistent with persistent vertex i = x (§3).
2. **Induction.** Inside a piece the persistent vertex is unchanged. At an aligned junction Q_k, Corollary J′ either pins Y (and we are done by (P)) or makes x persistent on the germ containing b̃_k, hence on κ of the next piece.
3. **Terminal point.** At Q_0, alignment gives x̂ = x.
   - If b_* is MERGE for x, then x is merged along b_*, which is case (J1) step 3.
   - If b_* is puncture-MOV, then x ∈ M with U_b ≠ ∅, which is case (J1) step 4.
   - Either way Y_t ∈ F for t in an open set, and (P) gives Y ≡ Y_0. ∎

**What Theorem R does not cover: the residual configurations (OPEN).**
- **(R-tw) Twin switch.** Some junction Q (possibly Q_0) is non-aligned. Then Q has a nontrivial automorphism g′ with g′x ≠ x. Along the outgoing branch, the persistent copy is x̂ = g′^{-1}x, whose value is ≡ Y_t on its component, while the track copy x is not persistent there. Its constant c(t) satisfies c(0) = Y_0 and c ≢ Y_t, or x is merged/moving generically but not at t = 0.
  - Lemma J still gives (J1), (J2) or (J3) for x̂. In case (J2) the network of *persistent* pieces continues, but on a different copy than the track. Prop K says nothing about where x̂ eventually merges or moves.
  - Restarting Prop K from the piece with the copy x̂ (Lemma PA applies to any piece, PR-H Remark) produces a new track that can switch again. I found no well-founded quantity that rules out infinitely many switches or cycles.
- **(R-cr) Interior MOV / crossing.** Either the terminal branch b_* (aligned) lies in the stratum of Q_0 and x moves along it, or a non-aligned junction falls into (J3). Then Y_t ∈ pr_x(K) for a fixed K ∈ 𝒦 and t near 0. This is a curve condition, not a finiteness condition, so no pinning follows. Excluding it would need more: either that a Prop K track can be continued past an interior MOV point, or a further geometric property of totally geodesic V_0. Theorem X (R8-1) covers only crossings inside a common Q-factorial sheet.

**Relation to the chain.**
- Lemma T shows that the coarse homeomorphism H always respects irreducible components, globally and locally. So "crossings" in the sense of H mixing sheets do not occur.
- Lemmas S and J then show that the only crossings that matter are (J3)-crossings, and Corollary J′ shows these occur only at non-aligned junctions or at the terminal branch.
- So the open part of MS8 is exactly (R-tw) together with the terminal (R-cr). This matches the chain's list of "residual twins and residual crossings", in a sharper form.
- I found no flaw in the chain's derivation of the problem's claim from MS8 in the part I used: holomorphy of Y_t (PR-A) and the finiteness of F under (Rig). I did not audit the rest of the chain.

## 6. Summary

**Proved here** (from (R1), (R2), (Rig); dimension-theory and analytic-geometry facts cited from memory as indicated):
- Lemma T: H maps each piece into a unique global, and local, irreducible component.
- Lemma S: M and K are constant on all fibres of each component, including t = 0. Constant vertices vary along a curve 𝒞_u finite over Δ. Persistence of a Y-copy is a property of the whole component.
- Lemma J: the junction trichotomy pinned / persistent / crossing, for the transported vertex x̂ = g′^{-1}x.
- Corollary J′: there are no crossings inside an aligned track.
- Theorem R: MS8 holds whenever the Prop K track is aligned at all its junctions and its terminal branch is a MERGE or a puncture-MOV.

**Not proved: MS8 in full.** The open cases are (R-tw), a non-aligned (twin) junction, and (R-cr), a terminal interior MOV or a (J3) crossing after a twin switch. Theorem R depends on these extra conditions, so by the task's rules it is a partial result, not a proof of MS8.

**No counterexample** was constructed.

=== END OF ANSWER round9_q7 ===

