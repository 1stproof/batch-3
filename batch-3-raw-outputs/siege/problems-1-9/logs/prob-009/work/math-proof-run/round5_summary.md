# Running summary after round 4 (written at round 5 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t. After four rounds (21 queries) there is no proof and no counterexample. Every round-4 worker (9 deep queries) reports MS4 open; all lean towards it being true, but by a global rigidity mechanism that nobody has established.

## Readings adopted by all workers (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3). By Chow's theorem, closure(V_t) is then algebraic.
- (R2) Smooth triviality together with (i),(ii) is read as a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, carrying (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G (round2_q1, round3_q1).
- Fixed index i: if i were allowed to depend on t, a Baire argument recovers a fixed i on an open set (round4_q5 §1). Proofs take i fixed, which is the natural reading of "that factor".

## Standing results
(Each holds under (R1)/(R2). None finishes the goal. Statements cited "from memory" by workers are marked as such.)
- **S1 (entry 2; repaired proof entry 19; round4_q3 (A), also round4_q1 §0, round4_q8 §0).** t ↦ Y_t is holomorphic Δ → M_{g_i,n_i}.
  - The original properness argument (round1_q4) had a gap: points of ∂V_{t_n} can escape into deeper strata.
  - round4_q3 (A) gives a clean proof. A = closure(𝒱) ∩ (Δ_Γ × Δ) has pure dimension 2. Away from a discrete set of t there are local holomorphic sections of A → Δ, and Y_t = π_i(section) there. Continuity comes from (R2), and the removable-singularity theorem finishes.
  - round4_q8 §0 gives an alternative: the closure in ∏ M̄_{g_j,n_j} × Δ, then Remmert, then normalization.
  - Consequence: the goal is equivalent to Y being constant on some nonempty open set of t.
- **S2 (entry 3; round1_q1).** (ii) for Γ and the strata in its closure is tautological. round4_q2 Obs. 0.1 adds (entry 23) that (ii) is vacuous or tautological for every pair (Δ_G, Δ_Γ) with G coarser than Γ. So (ii) has content only at isolated points of deeper strata.
- **S3 (entry 4; round1_q3; sharpened round4_q8 §B.3).** No argument local or semi-local to ∂V_t can work. In particular "constancy of H^1(Y_t) in the LMHS" is a restatement of the goal, not a reduction (round4_q8 §B.1).
- **S4 (entries 8, 9).** Monodromy, local monodromies, weight filtrations and intersection numbers are t-independent and blind to Y_t.
- **S5 (entry 5; round4_q3 (C) gives a clean Sierpiński-based proof).** If every V_t is totally geodesic, the claim holds (countability, cited from memory).
- **S6 (entry 14; round3_q1 Lemma B; rigorous version round4_q3 (B)).** Pinning theorem: an isolated deeper point P_0 ∈ closure(∂V_0) lying on closure(E_0) for a 1-dimensional boundary piece E_t with closure(E_t) = closure(E_0) forces Y_t = Y_0.
- **S6′ (entry 24; round4_q7 Lemma B′, round4_q2 Obs. 0.2).** Under (R2), incidences are transported automatically: P_t := H(P_0,t) ∈ closure(E_t) ∩ closure(∂V_t) ∩ Δ_{G'}, continuous in t, with E_t := H(E_0 × {t}). Neither (ii) nor isolatedness is needed. The vertex-i component of P_t is Y_t.
- **S7 (entry 15; round3_q4).** d_T ≤ k_{Ṽ_t}, with equality at t = 0 when V_0 is filled by Teichmüller discs. Royden is cited.
- **S8 (entry 25; round4_q7 Lemmas C1, C2).** Lemma C1: at every cusp P ∈ closure(∂V_t) \ ∂V_t there is a 1-dimensional boundary branch b ≠ β of closure(V_t) along which some extra edge e is pinched. Lemma C2: if b has the *merge property* (some edge of G' at vertex i is unpinched along b, so vertex i lies in a bigger vertex v of G_b), then F = π_v(E) is a curve, and its limit at P is a boundary point Q of M̄_{h,m} whose vertex-i component is Y_t.
- **S9 (entry 20; round4_q8 Prop. A, round4_q1 Thm A; Douady theory cited).** If the germ of the Douady space of the level cover M̂ at the flat limit Ẑ_0 of closure(V_0) is a reduced point (e.g. Hom(I/I², O) = 0, which is H^0(N) = 0 when Ẑ_0 is reduced), the claim holds. Only t = 0 data are needed.
- **S10 (entry 21; round4_q9 Lemma 0 and Thms A, B; round4_q5 Prop B; round4_q4 Thm 1; Imayoshi–Shiga cited).**
  - (a) A continuous family of holomorphic maps F_t: S → M_g from a fixed finite-type Riemann surface, with F_0 nonconstant, is constant.
  - (b) If there are biholomorphisms Φ_t: V_0 → V_t, continuous in t with Φ_0 = id, then V_t = V_0.
  - (c) (Theorem A of round4_q9) If a fixed finite-type curve maps holomorphically into V_t, continuously in t, and reaches ∂V_t at a puncture, then Y_t is constant.
  - Hence any counterexample must have abstract complex structure of V_t varying in t. Entry 18 is half settled.
- **S11 (entry 22; round4_q6 Thm C).** If the isomorphism classes of the level-cover components V'_t take only countably many values, the claim holds. Proof: countably many homotopy classes, plus Imayoshi–Shiga, plus the identity theorem.
- **S12 (entry 26; round4_q1 Thm B; the fixed-U form of (ii) is only sketched).** Converse criterion. A holomorphic logarithmic vector field ξ near closure(V_0), of product form (v(y), w(y,z)) near ∂V_0 with v(Y_0) ≠ 0, yields via its flow a family satisfying all hypotheses with Y_t nonconstant. So the claim for a given V_0 is a global rigidity property of closure(V_0) ⊂ M̄_g.
- **Not on the current line:** round3_q2 (persistence of (M)); round3_q3 Lemma 2.

## Conditional results (not standing)
- **round4_q7 Theorem E.** Assume (C-merge): at some cusp P_0 of ∂V_0 there is a boundary branch b with the merge property. Assume (H2′): F_0 = π_v(E_0) carries a maximal-Higgs rank-2 sub-VHS. Assume the cited results (K) (holomorphic isometric discs are Teichmüller discs, McMullen) and (Ct) (Teichmüller curves are countable). Then the claim holds.
  - Steps 1, 2, 4 of Prop D (Fuchsian monodromy, Deligne isotypic argument, Kobayashi isometry through the L-block period map) are argued in the file.
  - Step 3 cites Toledo = 2 deg.
  - Lemma F gives a second pinning: two rigid curves through Y in factor i.
- **round4_q3 (D) (sketch).** In the covering-construction model (configurations (0,∞,μ_d, ξμ_d, ημ_d)), C-merge holds and E_0 is a Teichmüller curve. So the claim holds there if Teichmüller curves are rigid allowing the base to vary.
- **round4_q9 heuristics.** In M_{0,7} involution-locus examples, naive deformations violate (i) (ψ_7 is nef and big, so the log normal section vanishes).
- **round3_q1 Prop A** is superseded by Theorem E.

## Dead ends
No route is dead by a REFUTED precise statement. No ledger entry is REFUTED. The negative standing results S2, S3, S4 show the following data cannot pin Y_t on their own: (ii) along Γ; local or semi-local analysis near ∂V_t, including LMHS data; topological data.

## Open gaps (routes set aside, not refuted)
- A. MS4 itself (entry 17), the goal in reduced form.
- B. Incidence route. (C-merge) is open; it cannot follow from local analysis (round4_q7 C). So are (H2′) or another rigidity of F_t, and the recursive case where π_i(E_0) is a point.
- C. Rigidity of V_0. This is strictly stronger than the goal. Variants:
  - H^0(N^log) = 0 (entry 13);
  - the Douady germ is a point (S9);
  - log-rigidity H^1(T(−log D)) = 0 plus a log-smooth family (round4_q5 §3, round4_q6 §5, round4_q9 B′);
  - constancy or countability of the complex structure of V_t (S10, S11; entry 18 second half, "ML").
  None has been attempted concretely with a mechanism. Restricting normal sections to Teichmüller curves stalls on an H^1(N_{C/V_0}) obstruction (round4_q1 §1, round4_q4).
- D. Arakelov/numerical (entry 11) and a Möller-type characterization of totally geodesic surfaces ((α)–(γ), round4_q8 §D). Set aside.
- E. Kobayashi metric (round3_q4). Only a one-sided inequality; no "domination ⇒ equality" theorem in dimension 2.
- F. Hodge transport (entry 10). The LMHS step is a restatement (round4_q8 §B).
- G. Counterexample. It would need a log vector field as in S12, or at least a deformation with varying complex structure (S10). Two naive constructions fail:
  - level-set deformations change the boundary combinatorics (round4_q5 §4, round4_q9 Ex. 1);
  - symmetric covering-locus deformations become branched double covers (round4_q1).
  Genus 2 gives nothing (round4_q1, round4_q8). Set aside, not refuted.

## The chain and the missing statement
**Chain.**
- (1) By entry 2, with the repaired proof of entry 19, t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}.
- (2) So the goal, π_i(∂V_t) = {Y_0} for all t, is literally the statement that this map is constant. By the identity theorem it suffices that Y is constant on some nonempty open set of t.
- (3) The missing statement below is exactly that. Nothing remains after it except stating the readings (R1) and (R2).
- (4) No proved reduction to a strictly simpler single statement exists. Every reduction in hand either needs two or more unproved statements, or a strictly stronger one. The two-or-more case is the new pinning chain in the sketch: Lemma R plus (T0). The strictly stronger options are rigidity of V_0 (S9, S10, S11) and total geodesy of V_t (S5).

**Missing statement (MS4, entry 17, wording unchanged).** Let g ≥ 2. Let V_0 ⊂ M_g be a smooth 2-dimensional complex subvariety, totally geodesic for the Teichmüller metric. Let 𝒱 ⊂ M_g × Δ be a complex submanifold with V_t = ψ(φ^{-1}(t)), satisfying hypotheses (i) and (ii) of the problem, and read as follows:
- (R1) closure(𝒱) ⊂ M̄_g × Δ is analytic, with fibre closure(V_t) over t;
- (R2) there is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, smooth on V_0 × Δ, mapping (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G.

Let Δ_Γ ≅ ∏_j M_{g_j,n_j} be a product boundary stratum. Suppose that for every t the set ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1 and π_i(∂V_t) = {Y_t} for one fixed index i. Then the holomorphic map Δ → M_{g_i,n_i}, t ↦ Y_t, is constant.

**Why it should hold (sketch; new mechanism this round: McMullen–Thurston length rigidity of boundary curves plus pinning).**
1. **Lemma R (rigidity of Teichmüller boundary curves under the family).**
   - Let E_0 be a 1-dimensional boundary piece of closure(V_0) in Δ_G, and E_t = H(E_0 × {t}) its transport (S6′). Let v be a vertex of G such that f_0 = π_v|_{E_0}, lifted to universal covers, is an isometry of the Poincaré disc onto a Teichmüller disc in T_{h,m}, i.e. π_v(E_0) is (covered by) a Teichmüller curve.
   - Then π_v(E_t) = π_v(E_0) for all t.
   - Proof idea (McMullen's rigidity argument):
     - The normalizations Ẽ_t are marked finite-area hyperbolic surfaces of one fixed topological type (by R2), and f_t has fixed monodromy ρ.
     - Royden/Schwarz–Pick give τ_T(ρ(γ)) ≤ ℓ_{E_t}(γ) for every γ. At t = 0 equality holds, since ρ(γ) is affine pseudo-Anosov on the disc or parabolic.
     - So ℓ_{E_t} ≥ ℓ_{E_0} on all curves. Thurston's theorem ("minimal stretch maps": sup_γ ℓ_Y/ℓ_X ≥ 1 with equality only for X = Y) forces E_t ≅ E_0 as marked surfaces.
     - Then S10(a) (Imayoshi–Shiga) gives f_t = f_0 ∘ (that biholomorphism).
   - This bypasses Möller's zero condition and the Hodge step (H2′) of round4_q7.
2. **(T0), the t = 0 structure.** At some cusp P_0 of closure(∂V_0) there is a boundary branch b with the merge property (S8), such that the merged projection π_v(E_0) is a Teichmüller curve. Alternatively, Lemma F of round4_q7 applies: two Teichmüller-curve projections through Y_0 in factor i with no common component. Heuristic support:
   - boundary pieces of a Teichmüller-totally-geodesic surface should be complex geodesics for the sup-product Kobayashi metric of Δ_G (limits of Teichmüller discs);
   - so some factor projection is a Teichmüller disc;
   - Mirzakhani–Wright / Chen–Wright boundary theory locates the vertices with nonzero limit differential;
   - the covering-construction model satisfies (T0) (round4_q3 (D)).
3. **Pinning.** Given 1 and 2, S6′ and S8 give Q_t ∈ closure(π_v(E_0)) ∩ ∂M̄_{h,m}, which is a finite set. Q_t is continuous in t, hence constant, and its vertex-i component is Y_t (round4_q7 Thm E). Also needed: cusps of ∂V_0 exist. Teichmüller-curve projections of C_0 are never compact, and if every projection of C_0 is constant, ∂V_0 would be 0-dimensional.

**Tried so far** (MS4 and earlier wordings: the goal itself, entry 6):
- round1_q1–q4: direct attempts and plumbing → S1–S3, no mechanism.
- round2_q1: Hodge transport/LMHS → S4, missing lemma (M).
- round2_q2: rigidity/Arakelov/normal sheaf survey → conditional reductions.
- round2_q3: structure at t = 0 and topology → S4.
- round2_q4: counterexample search → none.
- round3_q1: incidence, Milnor–Wood, Möller → S6, conditional (H1)–(H3).
- round3_q2: Arakelov-equality transport → reduction to persistence of (M).
- round3_q3: infinitesimal rigidity H^0(N^log) = 0 → reduction only.
- round3_q4: Kobayashi metric → S7, one-sided.
- round4_q1, q2, q3, q9 (closing task, identical copies) → repaired S1, Douady criterion, pinning theorem made rigorous, S10, S12 converse criterion; no proof.
- round4_q4: refutation → none; conditional rigidity (S10(b)).
- round4_q5: statement-only fresh move (Imayoshi–Shiga over a fixed base) → reduction to base rigidity (BR′).
- round4_q6: Imayoshi–Shiga plus base rigidity → S11, missing lemma ML (complex structure of V_t countable) open.
- round4_q7: incidence route continued → S6′, S8, Thm E conditional on (C-merge), (H2′), (K), (Ct).
- round4_q8: Torelli/LMHS at the boundary → restatement of the goal (dead as a reduction), Douady criterion S9.

## Target for round 5
**Progress test.** Rounds 3 and 4 produced no proof of MS4 or of the goal. They produced no universal PROVED result that shortens the chain, and no strictly simpler replacement statement. S6′, S8, S9, S10, S11 and S12 are general and are recorded under Standing results, but each is either a sufficient condition strictly stronger than MS4 or a lemma that still needs two unproved inputs. **Main line stalled — no universal progress.**

**What differs from last round's sketch.** Last round's mechanisms were (a) Imayoshi–Shiga plus base rigidity, (b) Möller's Hodge characterization for incidences, and (c) Torelli at the boundary. The new mechanism replaces the Hodge rigidity of boundary curves by McMullen's length-spectrum argument: Royden, then Thurston's minimal-stretch theorem, then Imayoshi–Shiga. That argument needs only that a boundary projection be a Teichmüller curve at t = 0, and it lets the base complex structure vary, which S10 cannot. The open input is moved to the t = 0 structural statement (T0), which concerns V_0 alone, where total geodesy is available.

**Wave (escalation rule), 9 attempt queries, all on MS4:**
- q1, q2, q3, q9: the closing task (identical copies), carrying the spliced standing results and the new sketch.
- q4: the named approach "McMullen–Thurston length rigidity plus pinning". Prove Lemma R in full, then (T0) or a substitute.
- q5: the hardest step (T0) cut out as a self-contained claim about V_0 only, using Mirzakhani–Wright / Chen–Wright boundary theory and Kobayashi limits of Teichmüller discs; or exhibit a V_0 where it fails.
- q6: statement-only. MS4 or its earlier wordings have been attacked in four rounds. The worker must derive the completion itself and choose a first move not on the list.
- q7: rigidity of V_0 through Kobayashi-extremality. Run a length-spectrum or Kobayashi-domination argument on the surfaces themselves, using the dense family of Teichmüller curves or discs in V_0 and the closed geodesics they carry, to show the complex structure of V_t is locally constant (ML / S11). This is new: earlier attempts used H^1 or Hodge vanishing.
- q8: sharpen the S12 obstruction into a counterexample. Find a totally geodesic V_0 and a stratum-preserving flow, or a non-flow deformation with varying complex structure, that moves Y_0. Otherwise identify exactly what forbids it.
