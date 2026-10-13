# Running summary after round 5 (written at round 6 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After five rounds (30 queries) there is no proof and no counterexample. Round 5 moved the difficulty off the family and onto V_0 alone, plus one technical orbifold condition:
- the pinning theorem, Theorem P of round5_q1, reduces the goal to a structural statement (T0) about closure(V_0) at t = 0;
- the length-rigidity Lemma R (round5_q1, q2, q3, q4, q9) is proved, but only under an orbifold-transport hypothesis (O) on the family.

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3). By Chow, closure(V_t) is algebraic.
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, carrying (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G (round2_q1, round3_q1).
  - round5_q6 §1.2 and round5_q3 §6 point out that (R2) is a Thom–Mather-type strengthening of the literal hypotheses (i) and (ii), which give a separate trivialisation for each stratum.
  - A proof under (R2) proves the claim for families satisfying (R2). The final document must state this reading openly.
- Fixed index i. A Baire argument recovers a fixed i (round4_q5 §1).

## Standing results
All hold under (R1)/(R2). Theorems marked [mem] are cited from memory by the workers. None of these finishes the goal.

- **S1 (entries 2, 19; round4_q3 (A); also round5_q6 §1.3 from (R1) alone).** t ↦ Y_t is holomorphic Δ → M_{g_i,n_i}. So the goal is equivalent to local constancy of Y near 0.
- **S1′ (round5_q7 Lemma 1; new entry).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t in a set accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for every coarser G. It has content only at isolated deeper points.
- **S3 (entry 4).** No local or semi-local argument near ∂V_t works.
  - Sharpened by round5_q6 Prop A: an explicit family in M_{0,7} (fibres of a forgetful map) satisfies smooth triviality, (i), (ii) in fixed-U form, (R1), (R2), dim ∂V_t = 1, constancy on a factor of a product stratum, and still has Y_t non-constant.
  - Only total geodesy fails there (and the ambient space is M_{0,7}, not M_g).
  - round5_q9 §4 sketches the M_g analogue.
  - So total geodesy of V_0 must enter globally.
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5).** If every V_t is totally geodesic, the claim holds.
- **S6 / S6′ (entries 14, 24).**
  - Pinning lemma.
  - Incidence transport: P_t := H(P_0,t) ∈ closure(E_t) ∩ closure(∂V_t), continuous in t, with vertex-i component Y_t (round4_q7 Lemma B′).
- **S7 (entry 15).** Royden domination d_T ≤ k_{Ṽ_t}.
- **S8 (entry 25; round4_q7 C1, C2).** Two facts at every cusp:
  - there is an extra boundary branch at every cusp;
  - a merge branch has non-constant merged projection, whose limit has vertex-i component Y_t.
  - (C-merge) cannot follow from local analysis.
- **S9 (entry 20).** Douady germ reduced point ⇒ claim.
- **S10 (entry 21).** Holomorphically trivial families are trivial, and a fixed test curve pins Y_t. Imayoshi–Shiga [mem].
- **S10′ (round5_q7 Cor. 3′; new entry).** Every holomorphic logarithmic vector field near closure(V_0) is tangent to V_0. So the conditional counterexample mechanism of entry 26 never applies. A counterexample needs the abstract complex structure of V_t to vary.
- **S11 (entry 22).** Countably many isomorphism classes of V'_t ⇒ claim.
- **S12 (entry 26).** Log-flow converse. By S10′ its hypothesis is never met. Not on the current line.
- **S13 (new; round5_q4 Lemma R\*; also round5_q1, q2, q3, q9 versions). Lemma R, length rigidity of Teichmüller boundary curves.**
  - Let E_0 be a 1-dim irreducible piece of closure(V_0) ∩ Δ_G (product stratum), and E_t = H_t(E_0).
  - Assume (H_0): with respect to an orbifold structure O_0 on the normalization Ẽ_0, π_v∘ν lifts to a ρ_0-equivariant isometric embedding of the disc onto a Teichmüller disc.
  - Assume (O): the orbifold data transport, i.e. f_t lifts equivariantly for an orbifold structure on Ẽ_t of the same type, with ρ_t = ρ_0∘θ_t.
  - Then π_v(E_t) = π_v(E_0) for all t.
  - Proof: Royden + Bers [mem] give equality τ_T(ρ_0γ) = ℓ_0(γ); Royden gives ℓ_t ≥ ℓ_0; Thurston's minimal-stretch theorem [mem, finite-area case] plus a Selberg cover gives E_t ≅ E_0; then an axis-intersection argument (round5_q4) or Imayoshi–Shiga finiteness (q1, q2, q9) finishes.
  - Lemma O1 (round5_q4): (O) survives disappearance or order-drop of cone points. Splitting or creation of cone points is NOT excluded. I constructed a local model of splitting, (ℤ/2)² acting by reflections, and one of creation, a curve tangent to a pseudo-reflection divisor. Both need a divisorial orbifold locus or a singular lifted surface.
  - (O) is automatic when the factor M_{h,m} has no orbifold points: genus 0 with ordered points, or m ≥ 2h+3 (round5_q8 (M4)).
  - Without (O) the cited form is not proved. round5_q1 and q9 tacitly assumed the level lift; round5_q2 states it as (Lev), round5_q3 as (Lift_t).
- **S14 (new; round5_q1 Theorem P, with Lemma R0). Pinning under (T0).**
  - Assume (R1), (R2) and (T0) in the "all-lifts" form, written out as MS5 below.
  - Assume Lemma R's conclusion holds for every Teichmüller pair (a,u) used.
  - Then Y_t ≡ Y_0.
  - The proof quantifies over all lifts R of P_0 and all vertices u carrying a twin of Y_0. This repairs the automorphism ("twin") gap that round5_q8 §3 found in round4_q7 Theorem E and in the simpler versions (round5_q2 Thm 1, q3 Thm 3.1, q4 Thm E\*, q9 Thm P), which track one lift only.
  - Lemma R0: the lifted family of boundary curves is analytic, with fibre over 0 inside the lifted closure of E_0.
- **S15 (new; round5_q5 Lemmas G, G′, T′, V, Prop C, Prop 4.1).** Proved modulo [mem] facts and the limit statement (F2), which is only sketched.
  - (G) GL₂(ℝ)-moves of generating pairs keep boundary limits in the same stratum.
  - (T′) Suppose that at one point of a boundary piece E, some sequence of generating pairs gives vertex v positive area. Then π_v|_E is orbifold-unramified onto a Teichmüller curve, so (H_0) holds, and E is non-compact.
  - (V) Along ∂V_0, the constant vertex i never carries positive area.
  - (C) Under (PA), cusps of ∂V_0 exist.
  - (4.1) (T0\*) — cusp + merge + positive area at the merged vertex — gives the "exists" form of (T0).
- **S16 (special cases of (T0)).**
  - round5_q5 Prop 5.1: covering loci over M_{0,5} with all branch preimages marked satisfy (T0\*) at every cusp.
  - round5_q8 Cor. N: cyclic covering constructions in M_g from M_{0,5} with a bubble-type constant factor have a merge branch and a thrice-punctured merged curve. Theorem M (round5_q8) then pins Y_t, given (M2) automorphisms, (M4) fine target and (M5) product stratum.
- **Not on the current line:** round3_q2 (persistence of (M)); round3_q3 Lemma 2; round5_q6 Prop B (affine-linear deformations of a ℤ/3 locus are rigid).

## Conditional results (not standing)
- round4_q7 Theorem E: superseded by S14. It also has the twin gap.
- round5_q8 Theorem M: (M1)–(M5) ⇒ claim, via Imayoshi–Shiga on a thrice-punctured sphere. It has no orbifold problem when M4 holds.

## Dead ends
- No route is dead by a REFUTED precise statement; no ledger entry is REFUTED.
- Negative standing results: S2, S3, S4, and S10′ (no ambient-flow counterexamples).
- Two candidate mechanisms are closed (closed candidates, not refuted routes):
  - Kobayashi "domination ⇒ equality" for surfaces (round5_q7 §4): no Thurston-type theorem in dimension 2;
  - persistence of a Teichmüller curve inside V_t (round5_q7 §2): it is equivalent to T ⊂ V_t.

## Open gaps (routes set aside, not refuted)
- A. **(T0) for every V_0** — now the missing statement (MS5 below).
  - Sub-gaps:
    - (PA) positive area somewhere on ∂V_0;
    - merge with positive area at a point of closure(∂V_0);
    - the twin condition for all lifts;
    - compact C_0 (round5_q2 §3.1: then P_0 must lie on ∂V_0 itself, with G coarser than Γ, which MS5 allows).
  - Heuristic doubt: round5_q4 (N3) suggests that boundary curves "transverse" to GL₂(ℝ) could fail (T0). round5_q5 Lemma V and T′ indicate this happens only if (PA) fails.
  - Unmarked covering loci: contracted bridges may pinch the vertex-i edges on both branches at a cusp (round5_q5 caveat). round5_q8 Cor. N shows some cusp still merges in cyclic M_{0,5} constructions.
- B. **(O) orbifold transport for the Teichmüller pieces used** (the second input of the chain). Set aside, not refuted.
- C. Rigidity of V_0 (H^0(N) = 0, Douady, log-rigidity, constancy of complex structure).
- D. Arakelov/Möller characterisation.
- E. Kobayashi metric for surfaces.
- F. Hodge transport.
- G. Counterexample.
  - S10′ kills ambient flows.
  - A counterexample needs varying complex structure, a V_0 failing (T0) or (O), and (round5_q8 §3) possibly symmetry breaking at a cusp.
  - round5_q6 Prop A / round5_q9 §4 give non-totally-geodesic models. Whether some forgetful fibre is totally geodesic is open; it is expected not.

## The chain and the missing statement

**Chain.** Entry numbers refer to the ledger after this round's block.
1. By entries 2/19 (S1), t ↦ Y_t is holomorphic. The goal is therefore equivalent to Y being constant for t near 0.
2. Fix V_0, Γ, i. Assume MS5 (below) holds for V_0. It provides:
   - a product stratum Δ_G;
   - a point P_0;
   - for every relevant pair (a,u), a Teichmüller-curve projection π_u(E^{(a)}) in the orbifold sense (H_0).
3. For each such pair, by entry 29 (Lemma R\*, round5_q4), (O) for E^{(a)} at vertex u gives closure(π_u(E_t^{(a)})) = closure(π_u(E^{(a)})) for all small t.
4. With that conclusion for every pair of step 2, entry 30 (Theorem P, round5_q1) gives Y_t ∈ F for |t| small, where F is a finite set. Its steps:
   - transport P_t = H_t(P_0) (entry 24);
   - lift R^n over P_{t_n};
   - pass to the limit R over P_0 (Lemma R0);
   - MS5(a) puts the vertex u carrying Y_{t_n} in the boundary of M̄_u;
   - MS5(b) with Lemma R puts R^n_u in the finite set closure(π_u(E^{(a)})) ∩ ∂M̄_u.
5. Y_t is continuous, so it is constant near 0. By step 1 it is constant on Δ.
6. **What still remains after MS5: (O) (entry 41)** for the pairs of step 2. It is automatic when the factor M_u has no orbifold points (S13). So MS5 is the strongest intermediate claim the main line needs next. With MS5 and (O), steps 1–5 are a complete proof under (R1)/(R2).

**Missing statement (MS5, ledger entry 40).** Setting:
- Let g ≥ 2 and let V_0 ⊂ M_g be a smooth closed 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric (every Teichmüller disc tangent to V_0 at a point of V_0 lies in V_0).
- Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product-type boundary stratum of M̄_g. Assume ∂V_0 := closure(V_0) ∩ Δ_Γ has dimension 1 and π_i(∂V_0) = {Y_0} for an index i with dim M_{g_i,n_i} > 0.

Definitions:
- A stratum Δ_G is of product type if the gluing map ξ_G: ∏_{w∈V(G)} M_w → Δ_G is bijective. Here M_w = M_{g_w,n_w}, and ξ̄_G: ∏ M̄_w → M̄_g is its extension.
- Let E^{(1)}, …, E^{(s)} be the 1-dimensional irreducible components of closure(V_0) ∩ Δ_G, and let 𝐂^{(a)} be the closure of ξ_G^{-1}(E^{(a)}) in ∏_w M̄_w.
- For a vertex u, "π_u(E^{(a)}) is a Teichmüller curve in the orbifold sense" means: f = π_u∘ν: Ẽ^{(a)} → M_u (ν the normalization) is non-constant, and there are
  - an orbifold structure on Ẽ^{(a)} with orbifold uniformization D → Ẽ^{(a)} and group Λ,
  - a homomorphism ρ: Λ → Mod_u,
  - and a ρ-equivariant holomorphic lift F: D → T_u of f that is an isometry from the Poincaré (Kobayashi) distance onto its image for the Teichmüller distance.

**Statement.** There exist a product-type stratum Δ_G and a point P_0 ∈ closure(∂V_0) with P_0 ∈ closure(E^{(a)}) \ E^{(a)} for some a, such that the following holds. For every a with P_0 ∈ closure(E^{(a)}), every R ∈ 𝐂^{(a)} with ξ̄_G(R) = P_0, and every vertex u of G such that some irreducible component of the stable curve R_u, with its special points in some order, is isomorphic to Y_0:
- (a) R_u ∈ ∂M̄_u (the Y_0-component is merged with other components at u);
- (b) π_u(E^{(a)}) is a Teichmüller curve in the orbifold sense.

(P_0 may lie on ∂V_0 itself when G is a proper contraction of Γ; it need not be a cusp.)

**Why it should hold (my sketch).**
1. **(PA) by a residue count.** At P ∈ ∂V_0, take generating pairs X_n → P. The 2-dimensional spaces Q_V(X_n) converge to a 2-dimensional space L of stable quadratic differentials on P. The quadratic-residue map L → ℂ^{E(Γ)} should have rank 1, because ∂V_0 has codimension 1 in closure(V_0) and only one direction leaves Δ_Γ. Its kernel gives a finite-area limit q_∂ ≠ 0. By Lemma V, q_∂|_{Y_0} = 0, so some vertex j ≠ i carries positive area, provided area does not leak into the collars.
2. **A Teichmüller curve at j.** Lemma T′ makes π_j(∂V_0-piece) an orbifold-unramified Teichmüller curve C_j, which is non-compact.
3. **A cusp and a merge branch.** Flow along a periodic direction of η_j (Veech dichotomy) to a cusp P_∞ of ∂V_0. Flowing nearby smooth generating pairs (X_n,q_n) in the same direction should pinch the horizontal cylinders of q_n but not the Γ-curves, since q_∂ has zero residue there and they are not cylinder cores. The resulting branch then has the merge property at i.
4. **Positive area on the merged vertex.** The merged vertex v absorbs part of the positive-area region of j, so Lemma T′ gives (b), and (a) holds by construction.
5. **Twins.** Twins of Y_0 are permuted by Aut(P_∞) and are treated symmetrically.

The hard steps are the rank-1 residue count with no area leakage, and the interchange of the limits n → ∞ and flow time → ∞.

**Tried so far** (on MS5 and its earlier wording (T0), entry 28; and on (C-merge)/(H1)):
- round3_q1: (H1) isolated as missing; conditional on Möller-type data.
- round4_q7 §C: (C-merge) cannot follow from local analysis.
- round5_q1, q2, q3, q4, q9: conditional pinning theorems assuming (T0). Heuristics only for (T0) itself.
- round5_q4 §4: obstructions (N1)–(N3). Cusps may be absent; merge is unproved; Teichmüller property heuristically doubtful for "transverse" boundary curves.
- round5_q5: analytic half done (Lemma T′, V, Prop C). Reduction to (T0\*) (positive-area merge). Proved for marked covering loci. Jenkins–Strebel route sketched with gaps (a)–(d).
- round5_q8: merge and (M3) proved for cyclic M_{0,5} constructions in M_g with a bubble-type constant factor; twin gap identified.

## Target for round 6

**Progress test.** Neither round 4 nor round 5 produced a proof of MS4 or of the goal. Round 5 did produce new general PROVED results:
- Lemma R\* under (O);
- Theorem P in all-lifts form;
- Lemmas T′ and V.

Together they re-decompose the chain. The family-dependent difficulty, MS4, is replaced by a statement about V_0 alone (MS5) plus a technical statement about the family (O). This is a different decomposition, but the chain now needs two unproved statements. MS5 may also fail for some V_0, so it is not a strictly simpler statement that the goal reduces to. Counted strictly: **main line stalled — no universal progress.**

**What differs from last round.**
- The missing statement is now MS5, which concerns only the totally geodesic V_0 at t = 0, where Wright/Mirzakhani–Wright structure and generating differentials are available. It is no longer the family statement MS4.
- My mechanism is new: a residue-rank count giving (PA), Lemma T′, a periodic-direction cusp, and a merge branch with positive area.
- The second input (O) is isolated explicitly. I found local models of cone-point splitting and creation, so it is a genuine gap.

**Wave (escalation rule), 9 attempt queries:**
- q1, q2, q3: the closing task on MS5 (identical copies). Spliced in:
  - PR-1 (holomorphy);
  - Lemma B′;
  - round4_q7 §C (C1, C2, the merge definition);
  - round5_q1 Lemma R, R0 and Theorem P;
  - round5_q4 Lemma R\* and (O);
  - round5_q5 Lemmas G, T′, V and (T0\*);
  - the chain and the sketch.
- q4: refute MS5 exactly as stated. This is the first round MS5 is posed. Candidates:
  - compact C_0 with no merge at any point;
  - a twin of Y_0 that stays unmerged;
  - a boundary curve with no positive-area vertex (failure of (PA));
  - unmarked covering loci with contracted bridges.
- q5: the hardest step of the sketch, cut out: (PA) and positive-area merge (T0\*) via limits of the 2-plane Q_V(X_n) and the residue-rank count, with Lemma T′/V spliced.
- q6: named approach not yet tried, the multi-scale differentials / level graph boundary of the rank-2 orbit closure. Use the Bainbridge–Chen–Gendron–Grushevsky–Möller compactification and the Chen–Wright / Mirzakhani–Wright WYSIWYG boundary to produce the MS5 configuration at a codimension-2 point of the boundary.
- q7: (O). This is the second input of the chain; settling it reduces the goal to MS5 alone. Prove Lemma R without (O): either show that cone points of the pulled-back orbifold cannot split or be created along the family (using smoothness of the normalized total space and the Teichmüller property at t = 0), or find a cone-type-robust replacement for Thurston's theorem.
- q8: a fourth copy of the closing task (one more independent attempt).
- q9: listed approach continued from its partial result. round5_q5 §6 (Jenkins–Strebel rays from a periodic direction of the positive-area limit η_j) is spliced in with its gaps (a)–(d). The task is to close those gaps and produce the MS5 configuration.
