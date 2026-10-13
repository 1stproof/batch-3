# Running summary after round 8 (written at round 9 plan)

## Goal
Ledger entry 1, OPEN [GOAL]: the claim exactly as posed. For the holomorphic, smoothly trivial family V_t deforming the smooth 2-dimensional totally geodesic V_0 ⊂ M_g, under (i) and (ii): if ∂V_t = closure(V_t) ∩ Δ_Γ is 1-dimensional and π_i(∂V_t) = {Y_t} for all t, then Y_t = Y_0 for all t.

After eight rounds (58 queries) there is no proof and no counterexample. Round 8 attacked MS8 (entry 68) with 10 queries. It produced:
- (F2) proved in full and Lemma T′ repaired: every boundary piece in every stratum has a Teichmüller vertex (Theorem TV, round8_q10). This removes (F2) from the inputs of (Rig).
- Under (Rig): uniformity of lifted families (Lemma U) and a generic-time trichotomy (no Y_t-copy merges or moves at a puncture at generic t; every IMOV is a pure crossing). Proved independently in round8_q2, q3, q4, q1, q8.
- Conditional resolutions of the twin step (under (U_J), (SC)/(IP), (NB)+(NB_∂)) and a structural description of what a twin jump needs.
- Theorem X (t = 0, total geodesy): no crossing inside a common Q-factorial sheet.
- round8_q9: (Rig), even in weak form, cannot be derived from piece-level data (Examples Z, Z′); global input is required.

## Readings adopted (must be stated in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (round2_q3).
- (R2) There is a stratified homeomorphism H: closure(V_0) × Δ ≅ closure(𝒱) over Δ, smooth on V_0 × Δ, preserving every stratum, with H_0 = id (round2_q1, round3_q1).
  - (R2) is a Thom–Mather-type strengthening of the literal (i)/(ii); the final document must say so (round5_q6 §1.2).
- The fixed index i is recovered by a Baire argument (round4_q5 §1).
- "Smooth" V_0: the quintic test surface is singular (round6_q3). Whether a locally closed V_0 is admissible is a reading question to flag.
- (R2^orb), optional and NOT adopted: "smoothly trivial" read in the orbifold category, so that H_t preserves isotropy groups |Aut| of boundary points. Under it the twin obstruction disappears (round8_q8 Cor. 2). If ever used, it must be flagged as a further strengthening.

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
- **S25 (entry 70; round8_q10).** (F2) proved in a general form (Theorem F2*: any scale, any phase, no integrability), with Lemmas B, Conv, Conj, Lim, TR. Lemma G′ is completed. Lemma T′ Steps 2 and 4 are repaired.
  - **Theorem TV.** Every 1-dimensional irreducible component E of the (lifted) boundary of closure(V_0) in any stratum has a vertex j such that:
    - closure(π_j(E)) is a Teichmüller curve;
    - π_j∘ν: E^ν → C^ν is proper, E^ν = H/Λ_E with Λ_E of finite index in the Veech group;
    - the lift to universal covers is the Teichmüller disc;
    - E is non-compact, and every end maps to a cusp.
  - Corollary Φ̂: a continuous marked limiting-disc map φ̂: H → Â for every stratum.
  - Corollary AR: affine rigidity of the constant vertex.
  - Lemma PA itself is still quoted, not re-proved.
- **S26 (entry 71; round8_q2 Lemma U; also round8_q7 Lemma S).** Under (R1), (R2), (Rig): each 2-dimensional component W of each lifted boundary family has a single moving set M_W and a single image curve K_W for all components of all fibres at all t; every piece is K_W × {point}. This removes the non-product L1 pathology under (Rig).
- **S27 (entry 72; round8_q2 Thm 1, round8_q3 Thm N, round8_q4 Lemma G, round8_q1 Lemmas A–B, round8_q8 Lemma 4).** Generic-time trichotomy. Assume (Rig) and Y non-constant. Outside a discrete set of t:
  - no Y_t-copy anywhere merges, or moves at a puncture;
  - every copy along every branch STAYs or IMOVs;
  - every IMOV is a pure crossing (all moving vertices of the crossing piece frozen along the other branches) or a shared crossing with equal projected curves (round8_q6 Prop 1);
  - the boundary points carrying Y_t-copies, minus a finite set, form the twin-free network C_t (round8_q3).
- **S28 (entry 73; round8_q1 Theorem X, Lemma S, Cor. X′).** At an interior point Q_0 of a piece E (product stratum), no sheet of closure(V_0) containing a branch of E carries a nonzero effective Q-Cartier divisor supported on boundary curves not over E's branch.
  - Monomial form: no integers n_e with Σ n_e ord_{Ê_l}(s_e) = 0 for all l, Σ n_e ord_{C_i}(s_e) ≥ 0 for all i, and > 0 for some i.
  - Sheets are topological, so H_t transports them.
  - Hence crossings inside a common Q-factorial sheet (or where the monomial criterion applies) never occur at any t.
  - [mem]: the flat-convergence fact (Fl).
- **S29 (entry 74; round8_q4 Theorem 2V, round8_q3 Cor. T).** Under (Rig), MS8 holds if some cusp P_0 of ∂V_0 satisfies:
  - (Tw1): near P_0 the boundary of closure(V_0) is ∂V_0 ∪ {P_0};
  - (C1) and (C2), or (Mg).
  - In particular this holds when |V(Γ)| = 2 and (Tw1) holds at one cusp. There is no hypothesis on automorphisms.
  - Corollary G1: a merged copy has a frozen class, so every counterexample needs twins at every t = 0 merge point.
- **S30 (entries 75–77; conditional twin theorems).** MS8 holds when Prop K ends in MERGE or puncture-MOV and any one of the following holds:
  - (a) (U_J) or (Lock) at every junction and (U_{Q_0}) at the end (round8_q5 Thm A, B, Cor. C; this repairs the R7-6 continuity principle under (U));
  - (b) star coherence (SC) or (NT) at every chain point, with a product-type chain (round8_q8 Thm 1). (SC) follows from isotropy preservation (IP), hence from (R2^orb);
  - (c) (NB) and (NB_∂): no new orbifold points of V_τ accumulating on Prop K's continuum, and no constant/moving coincidence (round8_q2 Thm S).
- **S31 (entry 78; round8_q8 Prop 3, round8_q5 Prop D).** A twin jump at a junction J forces:
  - failure of (IP), (NT), (Lock) and (U_J);
  - either a "persistent twin" (the next piece carries two constant Y_0-vertices with different value functions, one ≡ Y), or a junction crossing;
  - at the endpoint, a twin of the merging copy, exchanged by an automorphism of Q_0, that STAYs along the merge branch;
  - an α ∈ Aut(J) moving x whose fixed locus in the lifted 3-fold 𝒞° accumulates at (J,0) in one of three configurations: (A) curves of V_0 near J; (B) a boundary branch fixed pointwise; (C) a holomorphic arc of α-symmetric curves of V_τ reaching J only at τ = 0.
  - Chart-local analysis cannot exclude any of these.
- **S32 (entry 79; round8_q6 Props 1–2, round8_q2 Prop 7).** Under (Rig) with Y non-constant, either IMOV times are countable, or:
  - Y(Δ) lies in a fixed curve pr_y(K_W);
  - a residual crossing (pure, shared, or same-branch twin) persists analytically to t = 0.
  - So crossings reduce to a t = 0 statement (PC), which is open.
- **S33 (entry 80; round8_q9).** Results on (Rig):
  - Lemma Red (the central fibre is reduced);
  - Lemma Deg;
  - Lemma P0: which vertices degenerate at a puncture is a deformation invariant;
  - Cor. B / Theorem B: (Rig) for a piece in the birational case under (Σ-fixed);
  - **Examples Z, Z′:** families of pieces with a fixed Teichmüller vertex, trivial source and fixed punctures, but a varying joint image or a varying interior puncture value. So (Rig) and (Rig-w) cannot follow from piece data. Realisability by an admissible V_t is unchecked.
- **Not on the current line:** round3_q2; round3_q3 Lemma 2; round5_q6 Prop B; S12; Theorem M; Theorems P/P′/P″; S23 (superseded by S30); round7_q1 continuity principle (entry 66, repaired only under (U), S30(a)).

## Dead ends (REFUTED precise statements only)
- **MS5 without the smoothness and closedness hypotheses is false** (entry 43; round6_q2). MS5 itself was abandoned (RETRACT 40).
- **Lemma R*'s map-level conclusion without (O), as a statement about families of maps with a Teichmüller anchor**, is false (round7_q7 Prop X). Whether such families arise as boundary pieces of an admissible V_t is unchecked. So this is a dead end for proofs of L2 that avoid (O), not a refutation of Lemma R.
- Closed candidates, not refuted routes:
  - Kobayashi domination ⇒ equality;
  - persistence of a Teichmüller curve inside V_t;
  - the multi-scale route to MS5;
  - length/area/Arakelov inequalities for (O) (round7_q7 §4: all one-sided in the wrong direction).
- **Piece-level (Rig) is false** (entry 81; round8_q9 Examples Z, Z′). The statement refuted is this: "for a holomorphic family of maps of a piece with a fixed Teichmüller vertex, trivial source family, fixed punctures and (O) for v, the joint image curve (or the puncture values of all non-constant vertices) is t-independent". So no proof of (Rig) may use piece data alone. This is a dead end for that proof method, not a refutation of (Rig).

## Open gaps (routes set aside, not refuted)
- A. **MS8** (entry 68): the current missing statement (below). What remains inside it, given S27, is twins and crossings.
- B. **(Rig)** (entry 69, reworded as entry 82 this round). F2 is now done. It still needs:
  - (O_G) for every piece, and L2′;
  - by S33, global input (the 2-dimensional family V_t, or t = 0 structure that persists).
  - Untried approach: persistence of the Arakelov equality / maximal Higgs sub-VHS (Möller's characterisation of Teichmüller curves) under deformation, plus the multi-scale affine-disc description of all vertex coordinates (F2* at lower scales).
- C. Twins: S30 settles them under (U)/(SC)/(NB); S31 describes the residue.
- D. Crossings: S28 excludes common Q-factorial sheets; residue = two-sheet crossings (Cr1) and non-Q-Cartier crossings (Cr2) (round8_q1 §4.3), or (PC) (round8_q6).
- E. Rigidity of V_0 itself (H^0(N) = 0, Douady, Hodge/Arakelov characterisation of total geodesy, entries 10, 11, 13). Not pursued since round 4.
- F. Counterexample. It would need:
  - a varying complex structure;
  - twins at every t = 0 merge point (S29 Cor. G1);
  - failure of (Tw1)/(C1)/(C2) at every cusp;
  - a twin jump in configuration (A), (B) or (C), or a non-Q-factorial or two-sheet crossing.
  - Realising Examples Z/Z′ by an admissible family is open (round8_q9 Q1).
- G. Inherited inputs:
  - Prop K "modulo routine marking details" (entry 50), in the forms (K′), (K*+), (TD_J), (TD_Q). The fixed-witness form (TD_Q) is only sketched (round8_q5 §5).
  - Lemma PA is quoted.
  - (PT_chain), product-type strata along Prop K's chain: needed by round8_q8 Thm 1. Probably removable by Lemma U under (Rig) — unchecked.

## The chain and the missing statement

**Is a complete proof or refutation in hand?** No.
- No round-8 file proves MS8 (entry 68) as stated. Each proves it only under an extra hypothesis on twins ((U_J), (SC)/(IP), (NB)+(NB_∂), (Tw1)+(C1)+(C2)), and with a MERGE or puncture-MOV endpoint (S29, S30).
- No file refutes MS8. round8_q4 tried and found nothing false following from it.

**Definitions used below** (unchanged from round 8).
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w, for some stable graph G (any G).
- ν: Ē → ∏M̄_w is the normalization of its closure.
- A *puncture* is a point p ∈ Ē with ν(p) ∉ ∏M_w. Put f_u = pr_u∘ν.
- M(E) := {u : f_u non-constant}.
- K(E) := the closure of the image of E in ∏_{u∈M(E)} M̄_u.

**Chain.**
1. Entry 19: t ↦ Y_t is holomorphic. So if Y_t lies in a finite (or countable) set for t in a set accumulating in Δ, then Y ≡ Y_0.
2. Entry 70 (Theorem TV, with (F2) now proved) together with entry 45 (Lemma PA): every piece at time 0, in every stratum, has a Teichmüller vertex. Its π_j∘ν is a proper orbifold covering of a Teichmüller curve whose lift is the Teichmüller disc.
3. Entry 56 (L2 under (O_G), product strata), the L2′ sketch (non-product strata), entry 54 (L1′) and entry 71 (Lemma U) give **(Rig)**:
   - there is a finite set 𝒦 of triples (G, M, K), up to Aut(G), with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in its boundary;
   - every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦.
   - This is entry 82 (OPEN; replaces entry 69). It still needs (O_G) for every piece and L2′. By S33, it needs global input.
   - Consequence: all puncture values of non-constant vertices lie in a t-independent finite set F.
4. **MS8** (entry 68, wording unchanged): (Rig) ⇒ Y_t = Y_0 for all t.

Steps 1–4 give the goal from MS8 together with entry 82.
- MS8 is the strongest intermediate claim the main line needs next. After MS8, only entry 82 remains.
- MS8 is quantified over all admissible V_0 and families; it is not a sub-class.
- Inside MS8, entry 72 (S27) already settles the generic-time analysis. What MS8 still needs is to connect the t = 0 track of Prop K (entry 50) to generic t across twins and crossings.

**Missing statement (MS8)** (unchanged; OPEN entry 68, locator round8_plan).
- *Setting.* g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2), with H_0 = id.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type. ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - V_t is not assumed totally geodesic for t ≠ 0.
- *Hypothesis (Rig)*, as in chain step 3: there is a finite set 𝒦 of triples (G, M, K), M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that for every t ∈ Δ and every piece E at time t, (G, M(E), K(E)) ∈ 𝒦 up to the action of Aut(G).
- *Conclusion.* Y_t = Y_0 for all t ∈ Δ.

**Why it should hold (my sketch; revised).**
1. Suppose Y is non-constant. At generic t, S27 holds: no Y_t-copy merges or puncture-moves; IMOVs are pure or shared crossings.
2. **Crossings: the same-sheet lemma (new).** V_0 is smooth, so near a boundary point Q the sheets of closure(V_0) are the closures of the components of V_0 ∩ U. Prop K's track is a connected interior path inside V_0 ∩ U ((TD_J), (TD_Q)). Hence it lies in ONE component, so the STAY branch along which it arrives and the next (or terminal) branch are boundary curves of a COMMON sheet S at Q.
3. Theorem X's monomial criterion (S28) then applies with G = s_f^a / s_e^b: take e unpinched along the STAY branch, f pinched along it, and a·ord_Ê(s_f) = b·ord_Ê(s_e) on the crossing branch. This excludes IMOV endpoints and junction crossings, unless a further boundary curve of S through Q blocks the sign condition.
4. In that residual case use Q-factoriality. Conjecture: the normalized sheets of closure(V_0) at boundary points have quotient (toric) singularities. Reason: the closure of the orbit closure in the multi-scale compactification is cut out by linear equations in log-period coordinates (Benirschke–Dozier–Grushevsky), and 2-dimensional toric singularities are cyclic quotients, hence Q-factorial. Whether this survives the map to M̄_g must be checked.
5. **Twins.** With crossings gone, S30(a)/(b) need (U_J) or (SC) at the chain points. By S31, a failure needs α ∈ Aut(J) moving x, with fixed points in the lifted 3-fold accumulating at (J,0).
   - Case (A): the intersection of the lift of V_0 with Fix(α) is totally geodesic. Both contain every Teichmüller disc tangent to them, and complex geodesics are unique. So it is a union of Teichmüller curves through J's neighbourhood, whose boundary branches at J carry α. This should force (Lock) of x, αx along a network piece.
   - Case (B) gives (Lock) on the fixed branch directly.
   - Case (C) is invisible at t = 0. It must be excluded by the time-t same-lift Krull argument of round8_q3 Cor. T, applied in the sheet X_t at the lift q_t through which the transported terminal branch passes.
6. Then Prop K's MERGE/puncture-MOV endpoint, transported, contradicts step 1.

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
| round7_q4 (refute MS6) | — | no counterexample; Theorem C |
| round7_q5 (twin-robust transport) | — | proved under (NT); twin dichotomy; chart-local twin-jump model |
| round7_q6 (time-t open/closed) | — | time-t lemmas; Theorem T under (Lock) |
| round7_q7 ((O) without (★)) | — | Lemma G, Prop X, FAC conjecture |
| round7_q9 (check L1/L2) | — | L1′, L2 needs (O_G), L2′ sketch |
| round8_q1 (closing on MS8) | generic-time analysis + Hurwitz/Teichmüller-disc limits | Lemma B (pure crossings); Theorem X (no crossing in a Q-factorial common sheet); MS7* reformulation of the twin residue |
| round8_q2 (closing on MS8) | Stein factorisation; square lifting | Lemma U; Theorem 1 (trichotomy); Theorem S under (NB)+(NB_∂); Prop 7 (crossing ⇒ Y(Δ) in a fixed curve) |
| round8_q3 (closing on MS8) | analytic Y-locus; twin-free network | Theorem N; Cor. T (Krull pair at one lift, any automorphisms) |
| round8_q8 (closing on MS8) | transport families; isotropy | Theorem 1 under (SC); (SC) ⇐ (IP) ⇐ (R2^orb); Prop 3 (persistent twins) |
| round8_q4 (refute MS8) | local models, criteria | no counterexample; Theorem 2V; Cor. G1 (frozen merged classes); twin-jump and crossing models survive (Rig) |
| round8_q5 (twin step, fixed points of Aut(J)) | covering lemma modulo Γ_x | Theorems A/B under (U_J); Prop D, cases (A), (B), (C) |
| round8_q6 (crossing step, Minsky/Antonakoudis) | persistence | Prop 1 (pure/shared/same-branch types); Prop 2; (CR) ⇐ (PC); the bidisc route fails at first order (sup-products contain bidiscs) |
| round8_q7 (fresh lens, statements only) | Lemma S; junction lemma; Abel–Jacobi | only escape = sliding crossings (J5) and twins; Abel constraint pins genus ≥ 1 sliding crossings with one moving point |

## Target for round 9

**Progress test.** Rounds 7 and 8 produced progress on the chain:
- Round 8 proved (F2) and repaired Lemma T′, giving Theorem TV (entry 70). This holds for every admissible V_0 and every stratum, and it shortens the chain: (F2) is removed from the inputs of (Rig).
- Round 8 also proved, under MS8's own hypothesis (Rig) and for every admissible family, the generic-time trichotomy (entry 72) and Lemma U (entry 71). These are steps 1–2 of last round's sketch for MS8, now theorems.
- So the main line is not stalled. MS8 stays the missing statement with unchanged wording.

What changed in the sketch:
- Crossings: the same-sheet lemma plus Theorem X's monomial criterion, with a Q-factoriality conjecture for the residue.
- Twins: the α-fixed-locus case analysis (A)/(B)/(C), plus the observation that (SC) holds whenever the Γ-orbit of lifts of J_t in the track's lifted 3-fold component 𝒳 = closure(𝒞°) is a single point. Here Γ is the stabiliser of 𝒳 in Aut(J), and lifts of J_t in 𝒳_t form one Γ-orbit.

**Wave (escalation rule), 10 attempt queries.**
- q1, q2, q3, q7 — the closing task on MS8, byte-identical. Spliced in:
  - the older prior results (PR-A, B, C, H, I; R7-1 §1–2; R7-2 §2, §4; R7-3; R7-4; R7-5);
  - the round-8 results: round8_q2 §1–5, round8_q1 §2–4, round8_q3 §2–4.1, round8_q4 §3, round8_q5 §1–6, round8_q8 §0–5, round8_q6 §1–3;
  - Theorem TV;
  - the chain and the revised sketch.
- q4 — the crossing step cut out: no pure or shared crossing at a junction or endpoint of Prop K's chain. Approach: same-sheet lemma + Theorem X monomial criterion + Q-factoriality of normalized sheets (multi-scale / linear-equations lens).
- q5 — the twin step cut out. Approach: α-fixed loci, cases (A), (B), (C) of round8_q5 Prop D, with total geodesy (Fix(α) ∩ V_0 is totally geodesic) and the same-lift Krull argument (round8_q3 Cor. T).
- q6 — the twin step by a different first move: the lifted 3-fold component 𝒳 of the track, its stabiliser Γ, and the Γ-orbit of the lifts of J_t (prove (SC) or reduce to an isotropy statement about Γ).
- q8 — the obstruction posed as the thing to overcome or to sharpen into a counterexample: the persistent-twin / endpoint-twin configuration of round8_q8 Prop 3 (with round8_q4 §5 constraints (T1)–(T3)).
- q9 (elsewhere 1; attacks entry 82, the chain's other open input) — (Rig) by global input. Approach: persistence of the Arakelov equality / maximal-Higgs rank-2 sub-VHS under the deformation (Möller's characterisation), and the multi-scale affine-disc description of all vertex coordinates (F2* at lower scales, Cor. Φ̂). Examples Z/Z′ are posed as the test.
- q10 (elsewhere 2; gap E, set aside) — rigidity of V_0 itself: show that a smooth closed totally geodesic surface has no non-trivial deformation satisfying (R1)/(R2), or that every V_t is totally geodesic, via a Hodge-theoretic characterisation (rank-4 (2,2) sub-VHS, Arakelov-type equality, persistence of integers in the family). Either gives the goal at once (entry 5 / countability).
- Next round (10): MS8 will then have been attacked in rounds 8 and 9, so one query must be statements-only with a new first move.
