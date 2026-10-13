# Running summary after round 7 (written at round 8 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After seven rounds (48 queries) there is no proof and no counterexample. Round 7 attacked MS6 (entry 52) with 9 queries. It produced:
- MS6 under no-twin hypotheses (several independent versions);
- written checks of the chain lemmas, which found real flaws (L1 only for product strata; L2 needs (O_G));
- the observation that MS6 is not easier than the goal and contains an open t = 0 statement (MS6_0);
- a global family of maps showing that Lemma R*'s map-level conclusion fails without (O).

The two obstacles left in MS6 are the same in every file:
- **twins**: an automorphism of a junction or terminal point moves the tracked Y_0-copy, and the copies separate for t ≠ 0;
- **interior-MOV ("crossing")**: the network ends at an interior point of a piece whose Y-vertex moves.

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, preserving every stratum, with H_0 = id (round2_q1, round3_q1).
  - (R2) is a Thom–Mather-type strengthening of the literal (i)/(ii); the final document must say so (round5_q6 §1.2).
- The fixed index i is recovered by a Baire argument (round4_q5 §1).
- "Smooth" V_0: the quintic test surface is singular (round6_q3). Whether a locally closed V_0 is admissible is a reading question to flag.

## Standing results (never drop; [mem] = cited from memory by the workers)
- **S1 (entries 2, 19; round4_q3).** t ↦ Y_t is holomorphic. So the goal ⇔ Y_t lies in a finite (or countable) set for t in a set accumulating in Δ.
- **S1′ (entry 34; round5_q7).** The goal holds iff ∂V_t ∩ ∂V_0 ≠ ∅ for t in a set accumulating in Δ.
- **S2 (entries 3, 23).** (ii) is tautological along Γ and for coarser strata.
- **S3 (entries 4, 35).** No local argument near ∂V_t can work. The forgetful-fibre family in M_{0,7} satisfies every hypothesis except total geodesy and has Y_t non-constant (round5_q6).
- **S4 (entries 8, 9).** Topological data are blind to Y_t.
- **S5 (entry 5).** If every V_t is totally geodesic, the claim holds.
- **S6/S6′ (entries 14, 24).** Pinning lemma; incidence transport P_t = H_t(P_0).
- **S7 (entry 15).** Royden domination.
- **S8 (entry 25; round4_q7 C1/C2).** Krull gives a second branch at a cusp; a merged vertex is non-constant (Lemma C2).
- **S9 (entry 20).** Douady germ a reduced point ⇒ claim.
- **S10/S10′ (entries 21, 33).** Imayoshi–Shiga pinning; a counterexample needs the complex structure of V_t to vary.
- **S11 (entry 22).** Countably many isomorphism classes of V′_t ⇒ claim.
- **S12 (entry 26).** Log-flow converse (not on the current line).
- **S13 (entry 29; round5_q4).** Lemma R*: under (H_0) and (O), f_t ∘ A_t = f_0 for orbifold biholomorphisms A_t.
- **S13′ (entry 46; round6_q7).** Theorem L: (O) holds under the pointwise conditions (★), (★∞).
- **S13″ (new; round7_q7).**
  - Lemma G (careful sketch): (O) holds between any two times outside a closed discrete D ⊂ Δ.
  - Cor. G1/G2: Lemma R fails only if 0 is a type-jump time and no generic member is Teichmüller.
  - Prop. X: the explicit family ι∘(w² + t) into the double-pentagon Teichmüller curve has image constant, (O) failing, and no A_t. So the map-level Lemma R* fails without (O). Realisability as boundary pieces is unchecked.
- **S14/S14′/S14″ (entries 30, 47, 48).** Theorem P, Theorems P′/P″, and Krull/twin pinning (Theorem 4).
- **S15/S15′ (entries 31, 32, 45).** Lemma T′ (modulo (F2)), Lemma V, Lemma PA. Every piece has a vertex of positive area, hence (modulo F2) a Teichmüller vertex.
- **S16 (entry 50; round6_q9).** Proposition K: from ∂V_0 a compact connected Y_0-network reaches Q_0 with a MERGE or MOV branch ("modulo routine marking details").
- **S17 (entries 36, 37).** Covering-construction special cases.
- **S17′ (new; round7_q4).**
  - Theorem C: for every Galois covering construction over M_{0,5} or M_{1,2}, MS6_0 holds via an explicit merge at a cusp of ∂V_0.
  - Theorem A (q4): the t = 0 merge condition (M_β) gives MS6 near t = 0 for every admissible family, with no Teichmüller or (O) hypothesis.
- **S18 (entries 43, 44, 49).** The quintic surface (singular). MS5 fails there; the problem's conclusion holds under (O) by the twin mechanism.
- **S19.** The Picard surface: merges only in non-product strata.
- **S20 (new; L1, L1′; round7_q9 §1, round7_q1 §1, round7_q3 §1, round7_q8 Lemma 2.1).**
  - L1 holds for product-type strata, and for Aut(G)-fixed vertices.
  - L1′ holds for all G: constancy on all components of the 0-fibre of an irreducible lifted family W propagates to every fibre. Constancy is t-independent.
  - Lemma 2.1: non-constancy persists off a discrete set of t.
  - For non-product strata, L1 as first worded is unjustified: a local model has the 0-fibre containing several Aut(G)-translates (round7_q1 §1.2, round7_q9 §1.4). "E_t is the transport of some E_0" fails there.
- **S21 (new; L2; round7_q9 §2).** For product G, under (H_0) for a Teichmüller vertex and **(O_G)** ((O) for the whole map to ∏M_w):
  - every non-constant vertex u has its maps f_u^t ∘ A_t in a finite set;
  - its puncture values lie in a finite set F(E_0,u);
  - its image curve lies in a finite set.
  - (O) for v alone does NOT suffice: coarse homotopy carries no orbifold monodromy (q2, q3, q9).
  - L2′ for non-product G is only a sketch (q9 §2.6).
- **S22 (new; time-t lemmas; round7_q6 §1, round7_q2 Lemmas 1, 2, 4).**
  - Lemma 1: at any t, a merge of ANY Y_t-copy along any boundary branch, or an intact moving copy along a branch whose piece has the point as a puncture, gives the MS6 configuration at t.
  - Lemma 2: the set N_t of boundary points with a Y_t-copy is closed, also in families.
  - Lemma 3: if MS6 fails at t, every copy along every branch is STAY or IMOV. Without IMOV, N_t is a union of connected components of B_t.
  - Pattern transport (q2 Lemma 2): lifted branch patterns transport as a·S, a ∈ Aut(J).
- **S23 (new; no-twin transport theorems).** Under (R1), (R2), Prop K, and a MERGE or puncture-MOV endpoint, MS6 holds on a punctured neighbourhood of 0 in each of these cases:
  - (NT*): no boundary point has two Y_0-components, product strata (round7_q8 Thm A);
  - (NT): no automorphism of junction or terminal points moves the tracked copy (round7_q5 Thm A, round7_q2 Thm 5, round7_q3 Thm A);
  - (Lock) at finitely many chain points (round7_q6 Thm T).
  - Also: total-merge transport (round7_q2 Thm 3).
- **S24 (new; structure of the obstruction).**
  - Under the chain inputs, MS6 ⇔ [goal and MS6_0] (round7_q2 Prop 6), so MS6 is not easier than the goal. MS6_0 (a t = 0 statement) is open because of crossings.
  - Twin dichotomy: if Y is non-constant and there is no IMOV, the network fails only by a twin jump (round7_q5 Thm B). Chart-local arguments cannot exclude twin jumps (round7_q5 §5 local model).
  - Crossings are locally consistent (round7_q8 §4.2).
  - Transporting marked Teichmüller rays to time t meets orbifold points of V_τ, which sweep real hypersurfaces. Their monodromy is an automorphism that can swap twins (round7_q8 §4.3).
  - So round7_q1's "continuity principle" (Thm A, which claims to remove twins via interior paths) has a gap: its Steps 4–5 assume the τ-transported markings are coherent in s, which fails across such points. It is also non-uniform near junctions (planner's check).
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; Theorem M; Theorems P/P′/P″ (superseded by S23).

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness and closedness hypotheses is false** (entry 43; round6_q2). MS5 itself was abandoned (RETRACT 40).
- **Lemma R*'s map-level conclusion without (O), as a statement about families of maps with a Teichmüller anchor**, is false (round7_q7 Prop X). Whether such families arise as boundary pieces of an admissible V_t is unchecked. So this is a dead end for proofs of L2 that avoid (O), not a refutation of Lemma R.
- Closed candidates, not refuted routes:
  - Kobayashi domination ⇒ equality;
  - persistence of a Teichmüller curve inside V_t;
  - the multi-scale route to MS5;
  - length/area/Arakelov inequalities for (O) (round7_q7 §4: all one-sided in the wrong direction).

## Open gaps (routes set aside, not refuted)
- A. **MS6** (entry 52): retracted this round as the missing statement. It is no easier than the goal and contains the open t = 0 statement MS6_0. Replaced by the weaker MS8 below.
- B. **(O_G)** for every piece, or directly (Rig) without (O). Lemma G gives (O) generically. Conjecture FAC (factorisation through a fixed curve) is open.
- B′. (F2) of round5_q5 (behind Lemma T′).
- C. Twins: Lock / twin jumps.
- D. Interior-MOV (crossings).
- E. Rigidity of V_0 (H^0(N) = 0, Douady), Arakelov/Möller, Kobayashi, Hodge transport. Not pursued since round 4.
- F. Counterexample: needs varying complex structure, and a V_0 whose Y_0-networks reach only twin-locked-out or crossing exits.
- G. Non-product strata: L1/L2 need L1′/L2′ (L2′ sketched).
- H. Proposition K is proved only "modulo routine marking details", and those details touch the twin issue.

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No. No round-7 file proves MS6 (entry 52) as stated. Each proves it only under a no-twin or (Lock) hypothesis together with a MERGE or puncture-MOV endpoint (S23). Round 7 also showed that MS6 is no easier than the goal (S24).

**Re-decomposition this round.** The chain now argues by contradiction, as q8 §1.4 recommended. The rigidity output of L2 becomes a hypothesis (Rig) of the missing statement. This removes the open t = 0 content of MS6 (MS6_0): MS8 is vacuous for constant families. It also lets the image-level rigidity handle part of the IMOV case.

**Definitions used below.**
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w, for some stable graph G (any G, product type not required).
- ν: Ē → ∏M̄_w is the normalization of its closure. A *puncture* is a point p ∈ Ē with ν(p) ∉ ∏M_w. Put f_u = pr_u∘ν.
- M(E) := {u ∈ V(G) : f_u non-constant}. K(E) := the closure of the image of E in ∏_{u∈M(E)} M̄_u.

**Chain.**
1. Entry 19 (S1): t ↦ Y_t is holomorphic. So if Y_t lies in a finite set for t in a set accumulating in Δ, then Y ≡ Y_0. Equivalently, if Y is non-constant, Y_t avoids any prescribed countable set of values for all t outside a countable set Z ("generic t").
2. Entries 45 (Lemma PA) and 31 (Lemma T′, modulo (F2)): every piece at time 0 has a Teichmüller vertex in the orbifold sense (on the lift, for non-product G).
3. Entry 56 (L2 for product G, under (O_G)), the L2′ sketch (non-product G), and entry 54 (L1′): the maps (f_u^t ∘ A_t)_{u∈M(E)} lie in a t-independent finite set. Hence:
   - **(Rig)**: there is a finite set 𝒦 of triples (G, M, K), up to Aut(G), with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in its boundary, such that every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦.
   - This is ledger entry 69 (OPEN): it still needs (O_G) for every piece, (F2), and L2′.
   - Consequence of (Rig) used below: at a puncture p of E, some non-constant vertex hits the boundary (constant vertices take values in M_w), so pr_{M(E)}ν(p) ∈ K ∩ ∂(∏M̄_u), a finite set. Hence all puncture values of non-constant vertices lie in a finite set F, independent of t.
4. **MS8** (below; ledger entry 68): (Rig) ⇒ Y_t = Y_0 for all t.

Steps 1–4 give the goal from MS8 together with entry 69. MS8 is the strongest intermediate claim the main line needs next. It is the geometric core, containing the twin and crossing problems. After MS8, only entry 69 remains: the analytic input (O_G), (F2), and L2′.

MS8 is an implication quantified over all admissible V_0 and families. It is not a restriction to a sub-class. Its hypothesis (Rig) is exactly what step 3 supplies.

**Missing statement (MS8).**
- *Setting.* g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2), with H_0 = id.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type. ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - V_t is not assumed totally geodesic for t ≠ 0.
- *Hypothesis (Rig)*, as in chain step 3: there is a finite set 𝒦 of triples (G, M, K), M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that for every t ∈ Δ and every piece E at time t, (G, M(E), K(E)) ∈ 𝒦 up to the action of Aut(G).
- *Conclusion.* Y_t = Y_0 for all t ∈ Δ.

(Entered as OPEN entry 68, locator round8_plan. It replaces MS6, entry 52, which is retracted.)

**Why it should hold (my sketch).**
1. Suppose Y is non-constant. Generic t avoids the countable set Z of times at which:
   - Y_t is a component of an element of F;
   - Y_t lies in a 0-dimensional intersection of two curves of 𝒦 (projected to factors of type (g_i,n_i));
   - Y_t = φ_c(t) for a constant-vertex value function φ_c ≢ Y (these are holomorphic, round7_q5 Lemma 1).
2. At generic t no Y_t-copy merges or moves at a puncture (entry 57 + F). So every copy along every branch is STAY or IMOV.
3. **IMOV at generic t, at Q_t ∈ E_t, moving vertex x.**
   - Suppose some other y ∈ M(E) has its Q_t-component inside a merged or puncture-moving vertex of an adjacent piece. Then pr_{M(E)}(Q_t) ∈ K(E) ∩ {y-coordinate ∈ finite set}, which is finite. So Y_t is in a finite set: impossible at generic t.
   - Otherwise H_t^{-1}(Q_t) = Q_0 is a *pure crossing* of V_0: every moving vertex of E is intact and constant along the adjacent STAY piece D.
   - Exclude pure crossings by total geodesy. Near Q_0, Minsky's product-region theorem makes V_0 coarsely a product (Teichmüller disc in M_x) × (cusp of the D-plumbing). Total geodesy forces the Teichmüller discs in mixed directions to stay in V_0. The aim is to contradict uniqueness of Teichmüller geodesics, the non-existence of isometric bidiscs (Antonakoudis), or Lemma PA's area localisation in mixed directions.
4. **Without IMOV.** N_t ⊇ C_t = H_t(C_0), and ALL Y_t-copies of every point of C_t stay along all branches.
5. **Twin step.** Let J be a junction of Prop K's network, and σ ∈ Aut(J) move the tracked copy x.
   - (a) If x and σx stay isomorphic for t near 0 (Lock), the merged copy at the end is a Y_t-copy, contradicting step 2.
   - (b) If not, the twin jump needed to escape requires orbifold points of V_τ near J with automorphism ≈ σ (round7_q8 §4.3). These are σ-fixed points of the Aut(J)-invariant lifted family 𝓛 ⊂ Def(J) × Δ. Their absence makes the interior-path continuity principle (round7_q1 §2) valid near J. Their presence should force a σ-symmetric boundary point near J_t, i.e. Lock again.
6. So the Prop K track stays among the copies of type Y, and its MERGE or puncture-MOV terminal contradicts step 2.

**Tried so far** (on MS8 and its earlier wordings MS6, MS5 = entry 40, (T0) = entry 28, (C-merge)/(H1)):

| Locator | Approach | Yield |
|---|---|---|
| round3_q1 | — | (H1) isolated as missing |
| round4_q7 §C | local analysis | (C-merge) not derivable locally |
| round5_q1, q2, q3, q4, q9 | conditional pinning assuming (T0) | heuristics only |
| round5_q5 | analytic half | T′, V; covering loci |
| round5_q8 | cyclic constructions | twin gap found |
| round6_q1, q2, q3, q8 (closing on MS5) | — | MS5 fails for the singular quintic; Krull/twin pinning |
| round6_q4 (refute MS5) | — | Picard surface |
| round6_q5 | residue count | (PA) at generic points |
| round6_q6 | multi-scale route | Lemma D, Theorem 4 |
| round6_q9 | Jenkins–Strebel rays | Lemma PA, Prop K |
| round7_q1, q2, q3, q8 (closing on MS6) | no-twin transport | MS6 under (NT*)/(NT)/(P′) with MERGE or puncture-MOV endpoint; continuity principle (gap); MS6 ⇔ goal + MS6_0; L1/L2 flaws found |
| round7_q4 (refute MS6) | — | no counterexample; Theorem C (covering constructions); MS6′ (two-curve intersection) proposed for IMOV |
| round7_q5 (twin-robust transport (TR)) | — | proved under (NT); twin dichotomy; chart-local model of a twin jump; MS7 (Aut-closed sets) — the planner notes MS7 is violated by the quintic configuration, so it is too strong |
| round7_q6 (time-t open/closed) | — | time-t lemmas; Theorem T under (Lock); "purely time-t" contradiction argued impossible (heuristic) |
| round7_q7 ((O) without (★)) | — | Lemma G, Prop X, FAC conjecture |
| round7_q9 (check L1/L2) | — | L1′, L2 needs (O_G), L2′ sketch |

MS8 itself has not yet been attacked.

## Target for round 8

**Progress test.** Rounds 6 and 7 produced:
- no proof of the missing statement (MS5, then MS6);
- no proof of the goal;
- no new universal PROVED result that shortens the chain. L1′ and L2-under-(O_G) are corrections, and the no-twin theorems settle sub-classes.

**Main line stalled — no universal progress.**

**What differs from last round.**
- The missing statement is now the contradiction form MS8, "(Rig) ⇒ Y constant". It is strictly weaker than MS6 and has no t = 0 content for constant families.
- The sketch handles IMOV through joint image rigidity plus a "pure crossing" exclusion at t = 0, and twins through a fixed-point analysis of Aut(J) on the Aut-invariant lifted family. This replaces "count copies along the network".

**Wave (escalation rule), 10 attempt queries.**
- q1, q2, q3: the closing task on MS8, byte-identical. Spliced in:
  - PR-A/B/C, PR-H (Lemma PA, Prop K), PR-I (quintic/Krull);
  - round7_q6 §1–3, round7_q8 §2–4, round7_q5 §1–5, round7_q2 §0–4, round7_q9 §1, round7_q1 §2;
  - the chain and the sketch.
- q4: refute MS8 exactly as stated (new wording).
- q5: the twin step cut out as a self-contained claim. Named approach: fixed points of Aut(J) on the invariant lifted family, plus repair of round7_q1's continuity principle (its gap posed as the thing to overcome).
- q6: the pure-crossing exclusion at t = 0 for totally geodesic V_0, plus the IMOV reduction. Named approach: Minsky product regions / bidisc non-existence / area localisation.
- q7: fresh lens. The statement and cited statements only. Derive the goal from MS8 + (Rig), then attack by a first move none of the listed attempts used.
- q8: a fourth byte-identical copy of the closing task.
- q9 (elsewhere 1; attacks entry 69, a remaining chain input): (Rig) without (O_G). Continues round7_q7 (Lemma G, FAC, image-cycle rigidity) and round7_q9 (L2, L2′).
- q10 (elsewhere 2; the one chain check): Lemma T′ (entry 31) with its fact (F2), checked and completed.
