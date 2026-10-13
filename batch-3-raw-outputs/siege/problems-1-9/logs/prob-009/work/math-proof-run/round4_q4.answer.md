# round4_q4 — attempt to refute MS4

## Outcome
I found **no counterexample**. Every route to one runs into a rigidity phenomenon. What I prove is a conditional rigidity theorem (Theorem 1): if the abstract complex structure of V_t does not move, the whole family is trivial and the claim holds. I also give a first-order criterion (Proposition 2), and I explain why a counterexample would need a totally geodesic surface whose complex structure has non-trivial deformations. Whether such a V_0 exists remains open here.

Statements from the literature are cited from memory and marked as such.

## Cited result
**Rigidity theorem (Imayoshi–Shiga 1988, extending Arakelov–Parshin; cited from memory).** Let R be a Riemann surface of finite type. Let F_0, F_1 : R → M_g be holomorphic maps that are non-constant. "Map" is meant in the orbifold sense: a holomorphic family of genus-g curves, or equivalently an equivariant holomorphic lift R̃ → T_g. Suppose F_0 and F_1 are homotopic, in the sense that their lifts are equivariant for the same monodromy π_1(R) → Mod_g and are equivariantly homotopic. Then F_0 = F_1.

To avoid orbifold issues one can pass to a finite-index torsion-free level structure. Then M_g^{(ℓ)} is a fine moduli space and all of the above is literal. The coarse statement follows by taking the image.

## Theorem 1 (rigidity when the complex structure of V_t is fixed)
**Hypotheses.** Assume the setting of MS4. Assume also that there are biholomorphisms Φ_t : V_0 → V_t, depending continuously on t, with Φ_0 = id. Continuity is in the compact-open topology; only continuity on [0, t] for each t is needed.

**Conclusion.** Then V_t = V_0 for all t, and in particular Y_t = Y_0.

**Proof.**
1. V_0 is algebraic. Totally geodesic subvarieties of M_g are quasi-projective: their closures are algebraic by Eskin–Mirzakhani–Mohammadi and Filip, cited from memory.
2. Choose a projective embedding of closure(V_0). Let C range over the smooth loci of the irreducible curve sections. Each C is a Riemann surface of finite type, and these curves cover a dense subset of V_0.
3. Let ι : V_0 → M_g be the inclusion. Put F_s = ι_s ∘ Φ_s|_C, where ι_s : V_s → M_g is the inclusion. Each F_s is holomorphic.
4. F_0 is injective, so it is non-constant.
5. The family s ↦ F_s, for s ∈ [0, t], is a continuous path of maps C → M_g. Lift it to the level cover (after passing to a finite cover of C if needed). The lifts to T_g then form an equivariant homotopy with constant monodromy, because the monodromy is discrete and varies continuously.
6. By the Rigidity theorem, F_t = F_0 on C.
7. So Φ_t = id as maps into M_g on a dense set of V_0, hence everywhere. Therefore V_t = V_0, and ∂V_t = ∂V_0. ∎

**Corollary 1a.** The claim holds whenever the family of abstract complex manifolds V_t is locally trivial in t near 0. By the identity theorem (P-a, Lemma 1) it is enough to have this near t = 0.

This holds, for example, if both of the following are true:
- the log pair (resolution of closure(V_0), boundary) is rigid, i.e. H^1(T(−log D)) = 0;
- the family of closures is a locally trivial deformation of that pair.

## Proposition 2 (first-order criterion)
**Claim.** If the family is non-trivial, then V_0 carries a non-zero holomorphic section of its normal bundle N_{V_0/M_g}.

**Proof.** Suppose V_t ≠ V_0 for some t near 0. Write the family locally as a graph over V_0 in normal coordinates. Let k be the first order in t at which the graph function is non-zero. Its t^k-coefficient is a non-zero holomorphic section of N_{V_0/M_g}. This section is independent of the choice of coordinates, by the usual argument. ∎

So H^0(V_0, N_{V_0}) = 0 forces rigidity. For the claim it would even suffice to have this vanishing only for sections whose behaviour near ∂V_0 is the one compatible with (i) and (ii).

## Why a counterexample would have to be unusual
Theorem 1 shows that any counterexample needs all of the following:
- (a) a smooth 2-dimensional totally geodesic V_0 whose complex structure deforms non-trivially (as a quasi-projective surface, compatibly with the stratification);
- (b) an accompanying holomorphic deformation of the map into M_g;
- (c) Y_t moving along the way.

For the concrete V_0 listed in the task, I could not verify (a):
- **Loci built from M_{0,5}.** Covering constructions over genus-0 bases with 5 branch points are, up to finite maps, quotients or covers of M_{0,5}. The pair (M̄_{0,5} = dP_5, its 10 boundary lines) is rigid, since 4 points of P^2 in general position are projectively unique. So V_0 = M_{0,5} itself is rigid as a log pair. For finite covers V_0 → M_{0,5}, the group H^1(T(−log D)) picks up extra summands from π_*O. I did not prove that these summands vanish, so log rigidity of such covers is unproved here.
- **Flex and gothic loci.** I did not determine the deformation theory of these loci.

## Teichmüller curves inside V_0
I tried to deduce rigidity of V_0 from the density of Teichmüller curves in it, using Möller's rigidity of Teichmüller curves (cited from memory). This fails: a Teichmüller curve C ⊂ V_0 need not deform to a holomorphic curve in V_t.

The same obstruction blocks the normal-bundle route. A section of N_{V_0}|_C lifts to N_{C/M_g} only modulo an H^1 obstruction, which I could not control.

## Status
- **Proved:** Theorem 1 and Corollary 1a, which use the cited Imayoshi–Shiga rigidity; Proposition 2.
- **Refutation:** not achieved. No counterexample was found, and every hypothesis of a candidate example would need verifying.
- **Open:**
  - (Q1) Is every smooth 2-dimensional totally geodesic V_0 rigid as a quasi-projective complex surface, compatibly with its boundary stratification? Equivalently, can one construct biholomorphisms Φ_t as in Theorem 1? A positive answer would prove MS4 in full via Theorem 1.
  - (Q2) Is H^0(V_0, N_{V_0/M_g}) = 0 for totally geodesic surfaces? This would be an analogue for surfaces of Möller's rigidity of Teichmüller curves. A positive answer would also prove MS4, via Proposition 2.
- **Assessment:** the evidence points to the claim being true. A rigidity statement of this kind is the missing ingredient.

=== END OF ANSWER round4_q4 ===
