# round3_q1: assessment of the "rigid other boundary curves + incidence" mechanism

**Summary.** The mechanism proves the claim only conditionally, under three explicit hypotheses (H1)–(H3) below. A complete unconditional proof is not obtained. The single missing lemma is (H1), which is about the boundary configuration of V_0. Literature results are cited from memory.

## Interpretations adopted
- (I1) As in context item 1: t -> Y_t is holomorphic, so it is enough to show that Y_t ranges over a countable or discrete set for t near 0.
- (I2) Smooth triviality together with (i) and (ii) is read as a stratified homeomorphism closure(V_0) x Δ ≅ closure(𝒱) over Δ. It carries each boundary piece E_0 ⊂ Δ_G to a continuous family E_t ⊂ Δ_G. In particular the monodromy of the H^1 local system restricted to E_t, and to each factor projection π_j(E_t), is independent of t up to conjugacy.

## Step B is rigorous once Step A holds (pinning lemma)
**Lemma B.** Suppose:
- G' is a degeneration of Γ in which the vertex carrying Y stays intact;
- P_t ∈ closure(∂V_t) ∩ Δ_{G'} depends continuously on t;
- E_t is a 1-dimensional boundary piece in a stratum Δ_G with Δ_{G'} ⊂ closure(Δ_G);
- P_t ∈ closure(E_t) for all t;
- closure(E_t) = closure(E_0) for all t.

Then Y_t = Y_0.

*Proof.* E_0 is a quasi-projective curve. So closure(E_0) \ E_0 is finite, and in particular closure(E_0) ∩ Δ_{G'} is finite. The continuous map t -> P_t takes values in this finite set and Δ is connected, so P_t = P_0 for all t. The factor of P_t at the vertex carrying Y is Y_t, by context item 2. Hence Y_t = Y_0. ∎

How the incidence P_t ∈ closure(E_t) persists:
- Hypothesis (ii), applied with the pair (Δ_G, Δ_{G'}) and a neighbourhood U of P_0, says: if near P_0 the set closure(V_0) ∩ Δ_{G'} is locally contained in the closure of the Δ_G-piece, then the same holds for every t.
- So the persistence is legitimate exactly when, locally at P_0, the deeper boundary of V_0 comes out of E_0. This holds when P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} that lies in closure(E_0).
- Continuity of P_t in t then comes from (i) applied to Δ_{G'}.

## Step A: conditional rigidity of a non-constant factor
**Proposition A.** Let F_t := π_j(E_t) ⊂ M_{h,m} be a non-constant factor of E_t. Assume:
- (H2) F_0 is a Teichmüller curve, and its maximal-Higgs rank-2 summand L is a multiplicity-one isotypic component of the local system R^1 over F_0. More generally: L is the unique rank-2 sub-local system with its monodromy representation, up to isomorphism.
- (H3) Möller's characterization applies in M_{h,m}. From memory (Möller, "Variations of Hodge structures of a Teichmüller curve", JAMS 19 (2006)): a curve C -> M_g is a Teichmüller curve iff its VHS contains a rank-2 sub-VHS with maximal Higgs field. I am not certain whether the statement needs an extra condition, namely that the zeros of a generating section of L^{1,0} form sections, i.e. lie at marked points in the M_{h,m} setting.
  - If it does, that condition is NOT obviously preserved by the topological transport. This must be checked against the source.

Then F_t = F_0 for all t.

*Proof sketch.*
1. By (I2) the local system over F_t is the transport of the one over F_0, so it contains a sub-local system L_t with the same representation ρ_L.
2. By Deligne's semisimplicity theorem, the isotypic decomposition of a polarizable ℤ-VHS is a decomposition into sub-VHS. With multiplicity one this makes L_t a sub-VHS of weight 1, rank 2.
3. For a rank-2 weight-1 real VHS on a punctured curve, 2 deg L^{1,0} (Deligne extension) equals the Euler/Toledo number of ρ_L, up to sign. The Euler/Toledo number is a topological invariant of the representation.
4. At t = 0 it equals |χ(F_0)|; that is Arakelov equality, i.e. maximal Higgs field. Hence it equals |χ(F_t)| as well: the punctured curves F_t are homeomorphic by (I2). So L_t has maximal Higgs field.
5. By (H3), F_t is a Teichmüller curve.
6. Teichmüller curves are countable: each is the image of a closed SL(2,ℝ)-orbit, and there are only countably many by Eskin–Mirzakhani–Mohammadi (or already because Veech groups are finitely generated lattices defined over number fields).
7. The family t -> F_t is continuous, takes values in a countable set and is non-constant only if it jumps, so it is constant. ∎

If every factor of E_t is either constant or of this rigid type, Step A applies to each non-constant factor.
- Induction on the number of constant factors would still need each constant factor of E_t to be pinned by an incidence with yet another boundary piece. This is the same problem again, in a stratum of higher codimension.
- An induction on codimension terminates in the 0-dimensional strata of closure(V_t). These are finite and continuous in t, hence constant. But it only closes up if the incidence structure (H1) is available at every level.

## Conditional theorem
**Theorem (conditional).** Assume:
- **(H1)** There exist G', P_0 and E_0 as in Lemma B such that:
  - P_0 is an isolated point of closure(V_0) ∩ Δ_{G'} lying in closure(E_0);
  - the vertex carrying Y in G' lies, in G, inside a component on which E_0 has a non-constant projection F_0;
  - and the needed P_t ∈ closure(E_t) follows from (ii).
- (H2) and (H3) hold for that F_0.
- Pinning works through that factor: the finitely many points of closure(F_0) at the relevant boundary stratum of M_{h,m} have their Y-component determined. This is true because the boundary point of closure(F_0) restricts to Y_t on the subsurface.

Then π_i(∂V_t) = {Y_0} for all t.

*Proof.*
1. By Proposition A, closure(F_t) = closure(F_0).
2. Project P_t to the component of G that contains Y. The projection is a point of closure(F_t) in a deeper boundary stratum, so it lies in a finite set and is continuous in t, hence constant.
3. Its factor at the vertex of Y is Y_t. Hence Y_t = Y_0.

Note that this only needs the single factor F_t to be constant, not all of E_t. ∎

## What fails or remains open
1. **(H1), the missing lemma.** I cannot prove that some boundary piece of V_0 has a varying component that degenerates to a curve containing Y_0 as a component.
   - In the multi-scale picture (heuristic 7), Y_0 is a lower-level component at ∂V_0. A boundary curve E_0 where Y's subsurface is top-level and varies would have to be found, e.g. at cusps of C_0 where the level structure rearranges. Its existence is not established.
   - Configurations where the mechanism fails: every boundary piece of V_0 whose closure contains a point with Y_0 as a component has a constant projection there, or an isolated-incidence point P_0 does not exist. In those cases Step B gives nothing.
2. **(H2), multiplicity.** For arithmetic (square-tiled) Teichmüller curves, L may occur with multiplicity greater than 1 in R^1. Then L_t need not be a sub-VHS; only the isotypic component is. Maximality of some rank-2 sub-VHS inside it can fail.
3. **(H3).** The exact form of Möller's characterization (extra condition on zeros; versions for marked points and for quadratic differentials) has to be checked against the source. Preservation of the extra condition under topological transport is open.
4. The whole argument uses the strong reading (I2) of "smoothly trivial" together with (i) and (ii).

**Status.**
- Proved: Lemma B (rigorous, given (I2)).
- Proved conditionally: Proposition A and the conditional Theorem, under (H1)–(H3), with (H3) cited from memory.
- Open: the claim as posed, specifically (H1).

=== END OF ANSWER round3_q1 ===
