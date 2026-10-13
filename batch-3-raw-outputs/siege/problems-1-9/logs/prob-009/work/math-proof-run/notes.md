# Notes (after finalize)

## State
- Protocol finished. [GOAL] (ledger entry 1) OPEN; no PROVED goal line anywhere in the ledger, so main claim = the problem's claim, NOT PROVED.
- Incoming draft saved as judge/finalize_previous_proof.md. Final proof.md (~393 KB) written.

## Commit wave (r3) results
- r3_verify: whole draft refereed. No fatal error. S1 (serious, repairable): Part I §5.7 single-label step used Lemma TI(4) (approximate) for an exact identity. Minor M1–M7 (L.2 Step 4 dim ≤ 2; A.1(1) open/closed disc; §0 item 3 labelling; Lemma PA τ_n generic; A.6 Step 1 clause; U.8 sketch label; U.6 step 1 wording). Verdicts: Thm 7.5, C.5, C.7, C.8, C.10, Sect. U, Part I (except S1), Bridge, Thm B OK; Thm A OK modulo citations once S1 repaired.
- r3_q1: PROVED (checked by me): intrinsic condition (NGD) on closure(𝒱) (finite special sets Σ_t = top-special ⊔ isotropy-special; continue as disjoint sections; |Aut| locally constant on and off them) ⇔ some boundary trivialisation has (AP) on a disc; under (NGD), H′ = H∘Ψ (point-pushes in discs) has (AP), H′_0 = id. Conditional on Theorem A using H only on boundary points — I verified this by inspecting Part II (Lemma 2.3, 3.1, §5, Setting 6.0/6.1, §9, Thm 7.5; §1.2 open-stratum use not needed). Folded in as Section C: Lemma C.12.0–C.12.6, Theorems C.12, C.13, Cor C.13.1, Lemma C.14, Cor C.15, Remarks C.16. Push map checked numerically.
- r3_q2: Lemma CP (topological cone-point lemma), Lemma NJ/BAL, Props A2*/B2* — partial on (Rig); recorded only in "Other routes".
- r3_q3: Prop H (psh Hodge determinant of isotropic lattices; constancy on compact curves with invariant lattice), Cor H4 under unverified (Mon_t) — partial on (NRT-Z); recorded only in "Other routes".

## Repairs made in finalize
- S1: new Lemma 5.7A in §5.7 = Bridge L.1 Steps 1–3; L.1 Step 1 rewritten to use only "A = node curves" + TI(2) (Σ_i = Σ_w, ι(w) = c_m), new L.1 Step 4 derives the label; constancy argument now uses discreteness of the simple length spectrum of Y_0; N ≥ n_2 in §5.10.
- M1–M7 all applied.
- Title now states the answer; §0 renamed "Summary"; final-revision note added; end sections "Status" and "Other routes" (old Section R moved/renamed); Section G retitled "Detailed list of open points"; Section G item 1, item 5, C.3(e) updated for (NGD).

## Honest status
- Claim proved under (R1)+(R2)+(NGD) (most general), (R1)+(R2^orb) (Thm A), (R1)+(R2)+(Rig)+(NRT_P) (Thm B), plus Section U cases. Open: (NGD) failure case; (Rig), (NRT_P); readings (R1),(R2) not derived from literal hypotheses.
- Not independently refereed: Lemma 5.7A repair, Section C.12–C.16.
