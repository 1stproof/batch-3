# Running summary after round 6 (written at round 7 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After six rounds (39 queries) there is no proof and no counterexample.
- Round 6 showed that the round-6 missing statement MS5 (entry 40) is false in spirit. The cyclic quintic-cover surface V = {y^5 = quintic} ⊂ M_6 meets every hypothesis of MS5 except smoothness, and MS5 fails for it. So does its smooth locus V°, which is locally closed but not closed.
- In that same example the problem's conclusion still holds, under (O), by a "twin"/Krull mechanism.
- Round 6 also proved (PA) in general (Lemma PA) and proved (O) under pointwise conditions (Theorem L).
- This round re-decomposes the chain around a time-t, twin-free missing statement MS6 (below). It uses two new chain lemmas: L1 (constancy persists) and L2 (rigidity of every non-constant vertex).

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3). By Chow's theorem, closure(V_t) is algebraic.
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, carrying (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G (round2_q1, round3_q1).
  - (R2) is a Thom–Mather-type strengthening of the literal (i)/(ii) (round5_q6 §1.2, round5_q3 §6). The final document must say so openly.
- Fixed index i: recovered by a Baire argument (round4_q5 §1).
- "Smooth" for V_0: the round-6 example is singular both in the coarse sense (an A_1 point) and in the orbifold sense (a crossing at the Fermat quintic) (round6_q3 Prop. 2). Its smooth locus V° is smooth but not closed (round6_q2). The problem says "smooth subvariety". Whether a locally closed V_0 is admissible is a reading question to flag in the final document.

## Standing results
All hold under (R1)/(R2). Facts marked [mem] are cited from memory by the workers. Never drop an entry from this list.

- **S1 (entries 2, 19; round4_q3).** t ↦ Y_t is holomorphic Δ → M_{g_i,n_i}. So the goal is equivalent to local constancy, or to Y_t lying in a countable set for t in a set with an accumulation point.
- **S1′ (entry 34; round5_q7).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t in a set accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No local argument near ∂V_t can work.
  - The forgetful-fibre family in M_{0,7} meets every hypothesis except total geodesy, and has Y_t non-constant (round5_q6).
  - So total geodesy must be used globally.
- **S4 (entries 8, 9).** Topological data (monodromy, self-intersections) are blind to Y_t.
- **S5 (entry 5).** If every V_t is totally geodesic, the claim holds (countability).
- **S6/S6′ (entries 14, 24).** Pinning lemma, and incidence transport P_t = H_t(P_0) (Lemma B′, round4_q7).
- **S7 (entry 15).** Royden domination: d_T ≤ Kobayashi on the lift of V_t.
- **S8 (entry 25; round4_q7 C1/C2).** Two facts at a cusp of ∂V_t:
  - Krull gives a second boundary branch;
  - a merge branch has a non-constant merged vertex whose limit contains Y_t.
- **S9 (entry 20).** A Douady germ that is a reduced point implies the claim.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning. Log vector fields are tangent to V_0, so a counterexample needs the complex structure of V_t to vary.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t imply the claim.
- **S12 (entry 26).** Log-flow converse; never applies (not on the current line).
- **S13 (entry 29; round5_q4 Lemma R\*).** Under (H_0) (π_v∘ν lifts to an equivariant isometry onto a Teichmüller disc, for an orbifold structure on Ẽ_0) and (O) (orbifold transport), the conclusion is f_t∘A_t = f_0 for an orbifold biholomorphism A_t: Ẽ_0 → Ẽ_t homotopic to Ĥ_t. In particular π_v(E_t) = π_v(E_0).
  - Proof: Royden, Bers [mem], Thurston minimal stretch [mem], Selberg, plus an axis argument.
- **S13′ (new; round6_q7 Theorem L).** (O) holds, hence Lemma R for all t, if:
  - (★) at each c ∈ Ẽ_0, every automorphism of f_0(c) comes, modulo generic automorphisms, from the local group of O_0 at c;
  - (★∞) at each puncture, the limit stable curve has no extra automorphisms.
  - In particular there is no creation of cone points at curves without extra automorphisms. Lemma N: the normalized total space has reduced, unibranch zero fibre.
  - Three explicit local models (cross / fix / ram) show that (O) cannot be derived locally when (★) fails.
  - Lemma D: negative normal degree confines the family to a divisor.
- **S14 (entry 30; round5_q1 Theorem P).** Pinning under (T0) in all-lifts form. Lemma R0: the lifted family of pieces 𝓦^{(a)} ⊂ ∏M̄_w × Δ is an irreducible 2-dimensional analytic set, proper over Δ, with fibre over 0 inside the lifted closure of E_0.
- **S14′ (new; round6_q8 Theorems P′, P″).** Pinning needs (T0) only for ONE branch β″ of ONE piece at P_0, and only at the vertices that can carry the genuine Y_0-component (patterns), for product-type G and G′.
  - Germ argument: limits of lifts along transported branches converge to the lift along the original branch.
- **S14″ (new; round6_q6 Lemma D, Pinning Lemma, Theorem 4; round6_q1 Theorem P_S).** Krull applied at each time t.
  - At a point P of closure(∂V_t) \ ∂V_t, every node of P is kept along some boundary branch of closure(V_t) (Krull in the Kuranishi chart).
  - A branch over ∂V_t has a clean i-vertex j with P_j ≅ Y_t (Lemma D(1)).
  - A merge branch is either a genuinely new boundary curve (D1) or ∂V_t again with a twin copy of Y_t (D2).
  - Theorem 4 (Tw) / Theorem P_S (S): if near P_0 the only boundary is ∂V_0 ∪ {P_0}, and a combinatorial condition holds, then Y_t ≡ Y_0, given Lemma R for one Teichmüller vertex. This needs no transport of branch identities.
- **S15 (entries 31, 32; round5_q5).** Two lemmas, depending on (F2), which is only sketched.
  - Lemma T′: positive area at a vertex v at one point of a piece E implies π_v|_E is an orbifold-unramified Teichmüller curve, and E is non-compact.
  - Lemma V: the constant vertex i carries no area.
- **S15′ (new; round6_q9 Lemma PA, also round6_q5 Prop. 3).** At a generic point of any 1-dimensional boundary piece E (product stratum), the norming differentials of the tangent vectors of V_0 along E have limits of full area, supported on the vertices of maximal Teichmüller speed along E.
  - Hence (PA) holds, and with T′, **every piece has a Teichmüller vertex**.
  - Collar estimate: ‖b∂_{t_e}‖_T ≤ |b|/(2|t_e| log(1/|t_e|)).
- **S16 (new; round6_q9 Lemma NH, Prop. K).** Flowing generating pairs from a generic point of ∂V_0 in a direction where a top-level cylinder is horizontal and some Γ-curve at i is not:
  - one gets a compact connected set K_0 ⊂ closure(V_0) \ V_0 (the "Y_0-network") containing a point of ∂V_0, along which the path-marked Σ_i-component stays intact and ≅ Y_0;
  - and a point Q_0 ∈ K_0 with a boundary branch of type MERGE (some ∂Σ_i curve unpinched) or MOV (Σ_i-component non-constant).
  - Q_0 need not lie in closure(∂V_0).
- **S17 (round5_q5 Prop. 5.1, round5_q8 Cor. N / Theorem M; entries 36, 37).** Covering-construction special cases: marked covering loci over M_{0,5}, and cyclic M_{0,5} constructions with a bubble constant factor.
- **S18 (new; round6_q1, q2, q3, q5, q6).** The quintic surface V ⊂ M_6, Γ = (genus 2)–(genus 4), Y_0 = (y^5 = x(x−1), ∞).
  - closure(V) \ V = ∂V ⊔ {P_*}, where P_* is a chain Y_0 – B – Y_0 with an end-swapping automorphism.
  - Every 1-dimensional boundary piece lies in Δ_Γ, so MS5 fails. G = Γ never works in MS5 (Lemma A, round6_q3).
  - V is singular (round6_q3 Prop. 2).
  - Problem conclusion for deformations of V: holds under (R1), (R2) and (O) for the genus-4 vertex (round6_q6 Prop. 3; round6_q1 Cor. 3.4).
- **S19 (round6_q4, round6_q3 R-b).** The Picard surface y^3 = ∏(x−a_j)·(x−a_5)^2 in M_3.
  - Its only merges occur in a non-product stratum (three parallel edges). So MS5 restricted to product strata fails there.
  - It is possibly singular (unverified).
  - Lesson: any missing statement must allow non-product strata (work with lifts to ∏M̄_w).
- **Not on the current line:** round3_q2 (persistence of (M)); round3_q3 Lemma 2; round5_q6 Prop. B; S12; Theorem M.

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness and closedness hypotheses is false.** It fails for the closed singular quintic-cover surface V ⊂ M_6 and for its smooth, locally closed smooth locus V° (round6_q2 Prop. 2.4 and 3.3; also round6_q1, q3, q5, q6; new REFUTED entry).
  - MS5 as stated (smooth AND closed) is not strictly refuted. But any proof would have to derive a boundary statement from interior smoothness, which every worker judged implausible.
  - MS5 is therefore abandoned as the missing statement (RETRACT 40).
- Closed candidates, not refuted routes:
  - Kobayashi "domination ⇒ equality" in dimension 2 (round5_q7);
  - persistence of a Teichmüller curve inside V_t (round5_q7);
  - the multi-scale route to MS5 as stated (round6_q6 §5 shows that route cannot give MS5 in the quintic example).

## Open gaps (routes set aside, not refuted)
- A. MS6 (below), the current missing statement.
- B. (O) for the Teichmüller vertex of the pieces used (entry 41). Settled under (★), (★∞) (Theorem L). Open for curves meeting the orbifold locus badly or with automorphic cusps.
- B′. (F2) of round5_q5, the limit statement behind Lemma T′. Only sketched.
- C. Twin-robust transport of the Y-network (round6_q2 §4.2 shows the σ-splitting worry; round6_q6 Prop. 3 circumvents it by applying Krull at each t).
- D. MOV branches and branches leaving closure(∂V_0) (round6_q9 B1, B2).
- E. Rigidity of V_0 (H^0(N) = 0, Douady), Arakelov/Möller characterisation, Kobayashi metric, Hodge transport. Not pursued since round 4.
- F. Counterexample. It needs varying complex structure (S10′), and a V_0 in which no copy of Y_t ever merges or appears in a rigid puncture value.

## The chain and the missing statement

**Two new chain lemmas (my derivations this round; each needs one written check).**

- **L1 (constancy persists).** Let E_0 be a 1-dimensional irreducible piece of closure(V_0) ∩ Δ_G, let 𝓦 be the lifted family of S14 (Lemma R0), and let u be a vertex with pr_u constant (= Z_0 ∈ M_u) on the lift of E_0. Then pr_u is constant on (each irreducible component of) the lift of E_t, for every t.
  - *Proof.* Take an affine open U ∋ Z_0 of the quasi-projective coarse space M_u. 𝓦 → Δ is proper and pr_u(𝓦_0) = {Z_0}, so pr_u(𝓦_t) ⊂ U for |t| < ε. A holomorphic map from a compact connected analytic curve to an affine variety is constant. Hence the map (pr_u, t) on the irreducible 2-dimensional 𝓦 has rank ≤ 1 on an open set, hence everywhere, and pr_u is constant on the fibre components for all t.
  - *Contrapositive.* A vertex that is non-constant along E_t for some t is non-constant along E_0.
- **L2 (rigidity of all non-constant vertices).** Let E_0 have a Teichmüller vertex v in the orbifold sense, with (O) for (E_0, v). By S13 there is an orbifold biholomorphism A_t: Ẽ_0 → Ẽ_t, homotopic to the transported marking.
  - For every vertex u with π_u non-constant on E_0, the map g_t := π_u∘ν_t∘A_t is holomorphic and homotopic to g_0.
  - g_0 has infinite monodromy: finite monodromy would lift a finite cover to the bounded domain T_u, and then extend over the punctures, so g_0 would be constant. So g_t is non-constant.
  - By Imayoshi–Shiga [mem; as in round5_q1 Lemma R Step 5], g_t lies in a finite set of maps independent of t.
  - Consequently: closure(π_u(E_t)) ∈ a finite set of curves (equal to closure(π_u(E_0)) by the closed-set argument of round5_q1 Step 6), and **the limit values of π_u at the punctures of Ẽ_t lie in a finite set F(E_0,u) ⊂ M̄_u independent of t.**

**Chain.**
1. By entry 19, Y is holomorphic. If Y_t ∈ F for t in a set T accumulating in Δ, with F finite, then some Y^{-1}(y) is non-discrete, and Y ≡ y = Y_0.
2. By entry 45 (Lemma PA) and entry 31 (Lemma T′, modulo (F2)), every 1-dimensional boundary piece E_0 of closure(V_0) has a Teichmüller vertex. For non-product strata, work on an irreducible component of the lift to ∏M_w.
3. Assume (O) for these vertices (entry 41). Then L2 applies to every piece. Let F be the finite set of n_i-pointed smooth curves isomorphic, after relabelling, to a component of a point of F(E_0,u), over all pieces E_0 and all vertices u non-constant on E_0.
4. **MS6** gives, for t ∈ T, a piece E_t = H_t(E_0), a vertex u non-constant on E_t, and a puncture p with the limit of π_u at p having a component ≅ Y_t.
   - By L1, u is non-constant on E_0.
   - By L2, that limit lies in F(E_0,u).
   - So Y_t ∈ F for t ∈ T, and step 1 concludes.
5. What remains after MS6: (O) for the pieces used (entry 41), (F2) behind Lemma T′, and the written checks of L1 and L2.

**Missing statement (MS6).** Setting: g ≥ 2; V_0 ⊂ M_g a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric. V_t is a family as in the problem, satisfying (i), (ii) under readings (R1) and (R2) (stated in full in the query), with Δ_Γ ≅ ∏ M_{g_j,n_j} of product type, dim ∂V_t = 1, π_i(∂V_t) = {Y_t} for all t, and dim M_{g_i,n_i} > 0.

Definitions:
- A *piece at time t* is a 1-dimensional irreducible component E of the lift ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w, for some stable graph G (product type not required).
- Ē → closure(E) is the normalization of its closure in ∏M̄_w. A *puncture* of E is a point p ∈ Ē lying over closure(E) \ E.
- For a vertex u, write f_u := pr_u ∘ ν : Ē → M̄_u.

**Statement.** There is a set T ⊂ Δ with an accumulation point in Δ such that for every t ∈ T there exist:
- a piece E at time t,
- a vertex u of its graph G with f_u non-constant,
- and a puncture p of E,

such that the stable curve f_u(p) ∈ M̄_u has an irreducible component which, with its special points (node branches and marked points, in some order), is isomorphic to Y_t as an n_i-pointed curve.

(Examples of how it can hold: a boundary branch at a point Q merging a component Q_x ≅ Y_t (Lemma C2 gives a nodal limit containing Q_x), including merges along ∂V_t itself where Q_x is a twin; or a MOV-type branch whose moving vertex has limit Y_t at a puncture.)

Entered as an OPEN line (locator round7_plan). It replaces entry 40 (retracted).

**Why it should hold (my sketch).**
1. At t = 0, Prop. K (S16) produces, from ∂V_0, a connected Y_0-network K_0 ending at Q_0 with a MERGE or MOV branch b.
   - MERGE gives a nodal puncture value containing a component ≅ Y_0 (Lemma C2). So MS6 holds at t = 0 there.
   - MOV at a puncture of b's piece also gives it. MOV at an interior point needs handling: there Q_0 is simultaneously a cusp of the previous STAY piece, which constrains it.
2. Transport to t. The network is a finite chain of STAY pieces D (Σ_i-vertex constant). By L1 each stays constant along D_t, with a holomorphic value z_D(t). At a junction J, the components of H_t(J) are given in two ways, by the constants and fixed puncture values of each branch. Matching these multisets as holomorphic functions of t (finitely many bijections, identity theorem) forces z_D ≡ z_{D′} or ≡ a fixed value. In the latter case Y is constant and we are done.
3. Twins break the naive matching. Krull at each t (S14″) says every node of H_t(J) is kept by some branch, and a count of the components ≅ Y_t (generic t) should keep one copy on the network.
4. At Q_t = H_t(Q_0) the transported branch b_t has the same stratum. Its merged or moving vertex is non-constant (L1). The same count at Q_t places a Y_t-copy inside its puncture value.

The hard step is the twin-robust count in steps 2–4. A cleaner alternative is an argument entirely at time t: at a cusp P_t of ∂V_t all components other than Y_t are fixed puncture values (L2) or holomorphic constants (L1). Then show, from Krull and the connectedness of closure(V_t) \ V_t, that no "Y_t-copy stays isolated everywhere" configuration can exist.

**Tried so far** (on MS6 and its earlier wordings MS5 (entry 40), (T0) (entry 28), (C-merge)/(H1)):
- round3_q1: (H1) isolated as missing.
- round4_q7 §C: (C-merge) not derivable locally.
- round5_q1, q2, q3, q4, q9: conditional pinning theorems assuming (T0); heuristics only.
- round5_q4 §4: obstructions N1–N3.
- round5_q5: analytic half (T′, V); marked covering loci; Jenkins–Strebel sketch.
- round5_q8: cyclic M_{0,5} constructions; the twin gap.
- round6_q1, q2, q3, q8 (closing task on MS5): MS5 fails for the singular quintic surface. Krull/twin pinning (Theorem P_S). Single-branch form (T0_β) and merge branches from Wright's cylinder deformations under (H-cyl).
- round6_q4 (refute MS5): the Picard surface (non-product merges).
- round6_q5 ((H) via the residue count): proved (PA) at generic points; (H) fails for the quintic surface.
- round6_q6 (multi-scale route): the route cannot give MS5; Lemma D merge-or-twin; Theorem 4 (Tw).
- round6_q9 (Jenkins–Strebel route continued): Lemma PA, Lemma NH, Prop. K (MERGE or MOV on the Y_0-network); obstructions B1–B5.
- MS6 itself: not yet attacked.

## Target for round 7

**Progress test.** Rounds 5 and 6 produced no proof of the missing statement (MS4, then MS5) and no proof of the goal. MS5 turned out false in spirit. Round 6 did prove general results: Lemma PA, Theorem L, Prop. K, and the Krull pinning theorems. But these settle sub-gaps or special classes; they do not shorten the chain as it stood. **Main line stalled — no universal progress.**

**What differs from last round's sketch and decomposition.**
- The missing statement is now at time t, not t = 0. It is twin-free (any component ≅ Y_t counts) and stratum-free (G = Γ and non-product strata allowed).
- The merged vertex need not be Teichmüller: rigidity of all non-constant vertices comes from L2, and constancy of constant vertices from L1.
- The pinned objects are puncture values, which covers MERGE, twins and MOV-at-cusp uniformly.
- The mechanism is: Prop. K at t = 0, then L1/L2 transport, plus Krull at time t.

**Wave (escalation rule), 9 attempt queries:**
- q1, q2, q3, q8: the closing task on MS6, byte-identical. Spliced in:
  - holomorphy, Lemma B′, C1/C2, Lemma R/R0, Lemma R\*;
  - PR-F §0–3 (T′);
  - Lemma PA and Prop. K (round6_q9 §1, §3);
  - Lemma D, the Pinning Lemma, Theorem 4 and the quintic example (round6_q6 §2–4);
  - Theorem P′/P″ (round6_q8 §1);
  - plus the chain with L1/L2 and the sketch.
- q4: refute MS6 exactly as stated. New wording, so this is required.
- q5: hardest step, cut out: the twin-robust transport along the Y-network (steps 2–4 of the sketch), as a self-contained claim with L1/L2 given.
- q6: named approach not yet tried. A purely time-t argument at the cusps of ∂V_t, using Krull + L1 + L2 + connectedness of the boundary curve closure(V_t) \ V_t and the clean-vertex structure, with no transport of branch identities. Includes the "no isolated Y_t-copy anywhere" contradiction.
- q7 (elsewhere 1): (O) beyond Theorem L, continuing round6_q7 (mechanisms cross/fix/ram and (★∞)).
- q9 (elsewhere 2, the chain check): verify L1 and L2 as written, including the non-product lift, Imayoshi–Shiga's hypotheses, and puncture-value finiteness.
