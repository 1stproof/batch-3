Your work is not finished. Read and execute the below with ultrathink.

## Original Implementation Plan

**IMPORTANT**: Before proceeding, review the original plan you are implementing:
@plan.md

This plan contains the full scope of work and requirements. Ensure your work aligns with this plan.

---

## Round Re-anchor (REQUIRED FIRST STEP)

Before writing code:
- Re-read @plan.md
- Re-read @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Re-read the most recent round summaries/reviews that led to this round
- Write the current round contract to @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md

Your round contract must contain:
- Exactly one **mainline objective**
- The 1-2 target ACs for this round
- The **Capability Anchor**: relevant `Feature Map / Capability Map` node(s), or `N/A` if the plan has no capability map
- Which issues are truly **blocking** that mainline objective
- Which issues are **queued** and explicitly out of scope
- Concrete success criteria for this round

Do not start implementation until the round contract exists.

## Task Lane Rules

Use the Task system (TaskCreate, TaskUpdate, TaskList) with one required tag per task:
- `[mainline]` for plan-derived work that directly advances this round's objective
- `[blocking]` for issues that prevent the mainline objective from succeeding safely
- `[queued]` for non-blocking bugs, cleanup, or follow-up work

Rules:
- `[mainline]` work is the round's primary success condition
- `[blocking]` work is allowed only when it truly blocks the mainline objective
- `[queued]` work must be documented but must NOT replace the round objective
- If a new bug does not block the current objective, tag it `[queued]` and keep moving on mainline work

Before executing each task in this round:
1. Read @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each task/sub-task
3. Follow selected lesson IDs (or `NONE`) during implementation

---
Below is Codex's review result:
<!-- CODEX's REVIEW RESULT START -->
# Round 2 Review Result — prob-001

Reviewer: moonshotai/Kimi-k3 (max effort), reviewing Round 2 commit 38ee82a
(worker "Claude" per the RLCR loop). Scope checked against plan.md
AC-1..AC-5, problem.tex (verbatim), round-2-contract.md, the R1 SPINE
directive (Steps 0-3 + closeout), the full solution.tex (read line by line;
Section 4 audited at proof level), and the worker's round-2 summary.

Reviewer recompile: pdflatex twice, **0 errors, 0 undefined references,
15 pages** (limit 16); harmless hyperref PDF-string warnings only. Greps:
no `iffalse`, no `Stacks Tag`, no "same class", no TODO/hmm/wait. All 42
\ref's resolve to defined labels; tree is clean (round committed).

## Part 1 — Verification of the SPINE directive items

| Item | Directive | Status |
|---|---|---|
| Step 0 (B-7) | nerve-complex subsection with (0a)-(0f) | **DONE (0a)-(0e)**. ssec:nervetricks inserted: rem:normalize (0a), def:strand (0b), lem:constcx with the relocated front-insertion homotopy (0c), lem:subquot with signed transport (0d), lem:depth order-respecting via lem:nervemaps (0e), rem:transfer (0e'). (0f): lem:anchor **deleted**; lem:dead now states D is **initial** (q0-delta-terminal closed). Reviewer verified lem:constcx, lem:subquot, lem:depth line by line: all correct. |
| Step 1 (B-8) | generic filter lemma; sieve(i)/(ii) as corollaries | **PARTIAL**. lem:filter is a real, self-contained lemma and its proof is verifiable; the terrace induction is **deleted**. BUT the sieve re-derivations are **unsound in two places** (M-1 below), and sieve(i)'s single-dead-pin conclusion is **false** when rk(bar P) >= 2 (M-2 below). |
| Step 2 (B-9) | lem:sandwich repaired/replaced | **DONE**. lem:sandwich is now the correct common-refinement lemma (piecewise pushout of two covers covers and refines both, via the birhizomic pretopology) — exactly the weakened statement prop:vanish invokes. The flagged same-ray / GF-min / survival sub-claims are gone. Verified correct. |
| Step 3 (mainline) | prop:vanish Steps 1-3 rewritten as references | **NOT DONE** (worker honestly admits this). The old floating parentheticals remain ("all its components live at dead level", "dead or stricter-level overlap", "the sifted restricted cover is standard rigid...", "after one more pullback"); no new deduction was substituted. prop:vanish is still not line-by-line verifiable. |
| Closeout | q-b2-microtypo, Q-3(J'), q0 items | **DONE**: mu_Lambda / mu_E renames verified; def:square now says "rigid" (no J'); q0-lem-anchor deleted; q0-delta-terminal fixed. q-d-lemma: lem:dlemma proved (one line from ker chi^gp = 0 via prop:bp(c)) — correct, though it is not yet cited anywhere (it is material for the Round-3 Step-2/Step-3 citations). |

Sections 2-3 remain sound (no regressions detected on re-read).
Compile/page/AC-5 state verified: 15 pp, all limits fine.

## The main event: the claimed obstruction is of the WRONG map

The worker's summary claims the main theorem is "very likely FALSE as
stated" because "the unit F -> R pi_* pi^{-1} F splits" with complement
R pi_* M, M a complement-extended derived fiber. **This analysis is of
the wrong map, and the claimed obstruction does not exist in the
problem's actual form.** Dissection:

- What actually splits is the **site-extension** counit/unit for
  PSh(A) -> Sh(B) -> PSh(A): for a general presheaf H on A_P (NOT a
  sheaf), H -> j_* j^{-1} H with j: Sh(B) -> PSh(A) need not take values
  in sheaves, and an extension-by-zero gives a nontrivial kernel/cokernel
  pair. This phenomenon is real but **irrelevant**: j is not pi.
- The unit in problem.tex is eta_F: F -> R pi_* pi^{-1} F, where
  pi^{-1}: Sh(B_P) -> Sh(A_P) **lands in sheaves by definition**
  (left Kan extension FOLLOWED BY SHEAFIFICATION). There is one triangle
  (F, R pi_*, pi^{-1} F); pi^{-1} F is a single sheaf; **there is no
  complement term** to kill. The splitting the worker describes lives on
  the larger presheaf category and is exactly what sheafification
  annihilates.
- The worker's own Round-0/1 theorem: thm:descent (reviewer re-verified
  this round through Claims A/B and the endgame) proves **pi^{-1} F =
  G_F is a sheaf on the nose** with F(b) = G_F(i(b)) — so after
  thm:descent, the remaining question is purely
  H^{q>0}(i(b), G_F) = 0 (prop:vanish). No splitting arises: the object
  being derived is a sheaf, and the unit F -> pi_* G_F is already an
  isomorphism of sheaves (degree 0).
- The intuition that "R^{>0} pi_* probes triviality-on-A\\B" is also
  off-target: R^q pi_* is computed by sheaf cohomology along the
  B-slices i(b) (a slice of a full subcategory of A_P), which is
  precisely what prop:vanish computes. The claimed "idempotent F forces
  R^{>0} pi_* M != 0" was never exhibited (no example of a nonzero
  R pi_* M; the summary itself concedes the complement is informal).

**Consequence.** The path of record remains: prove prop:vanish
(H^{q>0}(i(b), G_F) = 0, H^0 = F(b)). The Sections 2-3 machinery is
intact, the G_F-sheaf theorem is proved, and the R2 Steps 0-1 support
lemmas are in place. The correct Round-3 action is to **restore and
complete the prop:vanish proof**, not to construct a counterexample.
The worker's own Step-2 two-fold displayed-equation comparison (which it
verified) ALREADY kills the D-level constant without any impossible
section-out-of-D — the "wrong-directed anchoring" objection was to a
straw-man route (the reviewed R1 directive never requested a section out
of D; it requested exactly the sieve-constancy + two-fold comparison that
the document already half-contains).

## Part 1 (cont.) — New findings in Section 4 (fractures in the R2 state)

### MAINLINE GAPS

**M-0 (AC-1; structural).** The deliverable currently carries
thm:main / thm:main-end / prop:vanish as PROVED statements while the
worker's own summary declares the theorem unproved and likely false.
Whatever the final mathematical outcome, solution.tex must not assert an
unproved theorem as proved — that is precisely what AC-4 exists to
police. Round 3 must either (a) close prop:vanish (directive below),
leaving the assertions intact, or (b) honestly re-state thm:main as an
open problem with the exact proved reductions. There is no third option.

**M-1 (lem:filter application fractures).** (i) lem:sieve(i)'s proof
hypothesizes "z vanishes at the diagonals (f, iB)" but prop:vanish Step 1
invokes lem:sieve(ii) at level P on a cocycle for which this hypothesis
is never established — the chain of instantiation is broken at its first
link. (ii) The phrase "at the remaining dead pieces by transport"
asserts without argument that vanishing at (f, iB) transports to ALL
dead pieces; it can only transport along dead overlaps, and the dead
sector is not connected under dead overlaps alone (see M-2).
(iii) lem:filter's (F2) requires the adjoined top piece to be a single
fold U factoring through H_top; all-dead tuples built from >= 2 folds
never arise by adjoining ONE fold to a lower tuple, so (F2)'s pattern
does not cover the deep dead sector (mitigated by M-2's alternate route —
the dead sector can be left arbitrary).

**M-2 (lem:sieve(i)'s conclusion is false as stated).** When
rk(bar P) >= 2 there exist nerve pieces dead "by exclusive or" — e.g.
(f, i(P/K_1), i(P/K_2)) with K_1, K_2 incomparable, or (f, g, i(P/K_2))
with f, g distinct-ray folds. Two such pieces can hold INDEPENDENT
elements of F(b_P) (no dead overlap joins them). Nothing in lem:filter
or lem:const pins them, and prop:vanish Step 2's pin of z_P needs only
the EQUALITY of the fold images, not the false single-constant claim.
The proof as written silently upgrades "z vanishes at diagonals" to "all
dead values are one constant", which the machinery does not give and
which is in general untrue.

**M-3 (closed items; no action).** q-b2-microtypo, Q-3(J'), q0-delta-terminal,
q0-lem-anchor, q-d-lemma, q-complex-foundations, B-7, B-9: closed —
recorded in the tracker. q-restriction-lemma and q-accounting remain open
(absorbed into mainline M-4).

**M-4 (R1-SPINE Step 3 not executed; q-restriction + q-accounting).**
prop:vanish Step 3's restriction to the slice over i(P/K), and the
floating "(the sifted restricted cover is standard rigid over
i(P/K); ...)" and "after one more pullback" clauses, were never replaced
by named references; the transport-forward from level K to level P in
that parenthetical is moreover stated with the WRONG direction
(Cech-class transport goes from fine covers to coarse, not from the
P-level down to the K-level).

### BLOCKING SIDE ISSUES

None separate from M-0..M-4: every defect sits directly on the mainline
objective (close prop:vanish).

### QUEUED SIDE ISSUES

- q-dead-sector: lem:filter (F2)'s single-anchor pattern does not cover
  deep dead pieces (>= 2 folds). Non-blocking: M-2's directive route
  never needs to touch the dead sector. Revisit only if the chosen
  route re-enters it.
- q-skippedcases: ensure rank-one (dim bar P <= 1) and P = {0} cases
  are treated by named references (lem:const + lem:dead base case), not
  a parenthetical.
- Q-3 (rest) and the final typography pass: still final-round.

## Part 2 — Goal Alignment Summary

AC-1: blocked on M-0..M-2, M-4 (Section 4 endgame unproved; deliverable
asserts it as proved). AC-2: OK (rem:verdier names SGA 4 Exp. V Thm
7.4.1 in words). AC-3: blocked on M-4 (floating parentheticals,
wrong-direction transport). AC-4: TRIGGERED — the worker's claim that
the theorem is likely false is not established (its "splitting" is of
the wrong map); the tracker now records the reviewer re-anchor.
AC-5: OK (15 pages, clean compile, package set compliant).

ACs: 2/5 addressed (AC-2, AC-5); AC-1/AC-3 blocked on the Section-4
endgame; AC-4 triggered and reconciled | Forgotten items: 0 |
Unjustified deferrals: 0 (the worker did not defer; it admitted and the
reviewer re-directed)

Tracker state reconciled by this reviewer: B-7 -> resolved (foundations);
B-8 -> partially resolved, REOPENED at the sieve(i)-conclusion level
(M-2); B-9 -> resolved; q-complex-foundations / q-d-lemma /
q0-lem-anchor / q0-delta-terminal / q-b2-microtypo -> closed;
q-restriction-lemma / q-accounting -> open (absorbed into mainline M-4);
q-dead-sector / q-skippedcases -> queued; Plan Evolution Log entry
added recording the wrong-map re-anchor. The worker's requested
"counterexample-required / likely-false reclassification" is REJECTED
(justification: the only exhibited obstruction is the site-extension
splitting, which sheafification removes; thm:descent already gives
pi^{-1} F a sheaf; no counterexample was produced; and the correct
contract for this job is a proof, with AC-4's honest-restatement branch
available only if the proof genuinely cannot be closed after a real
attempt at the directive).

## Part 3 — Capability Map Summary

Capability anchor: N/A (plan.md has no feature/capability map) |
Dependency gaps: 0 | Scope drift: no

## Part 4 — Directive implementation plan for Round 3 (restore prop:vanish; singular; execute as written)

Round 3's sole mainline objective: **close prop:vanish** so that
thm:main-end is a proved theorem again (or, only as a last resort after
the steps below are genuinely attempted, re-state thm:main as an open
problem with the proved reductions; the counterexample route is NOT
authorized). Execute Steps 3.1-3.4 in order. All required machinery
(lem:constcx, lem:subquot, lem:depth, rem:transfer, lem:filter,
lem:nerve, lem:mixed, lem:dlemma, lem:dead, lem:sandwich) is in place
and reviewer-verified.

**Step 3.1 (dispense the D-level constant — no section-out-of-D).**
In prop:vanish, DELETE the current Step 1 paragraph's claims that depend
on lem:sieve(ii)'s single pin. Replace Steps 1-2 by:
  (a) Step 1 (dead-sector hygiene): pull z back along the refinement
  S := {U tensor D} of {D} (a cover of D; cf. lem:sandwich for the
  common refinement bookkeeping). On S the RESTRICTED cocycle has all
  its nerve pieces dead, and G on the D-slice is the constant sheaf
  F(b_P) (lem:dead); by lem:constcx with H = D the restricted class
  vanishes after refinement. Conclude ONLY: after pulling z to a common
  refinement, the value at every nerve piece that maps to D is a
  coboundary value of elements of F(b_P); keep the notation z. Do NOT
  assert constancy of dead values.
  (b) Step 2 (kill the fold residues; keep the existing verified
  display): for kernel-J folds f, f' on distinct rays, the pairs
  (f, f'), (f, D), (f', D) are dead (lem:mixed(a), lem:nerve(i)). The
  cocycle equations at (f, D), (f', D), (f, f') read, with iota the
  terminal map to b_P and iota_D = id: the value z_{(f,D)} equals
  F(iota_f)(z_f) plus a dead coboundary term from (a); likewise for
  f' and for (f, f'). Substituting the (f,D)- and (f',D)-equations
  into the (f,f')-equation and using that all dead terms lie in the
  image of the same F(iota)-coboundary, conclude
      F(iota_f)(z_f) = F(iota_{f'})(z_{f'})   (equality in F(b_P)).
  State exactly this conclusion; cite lem:dlemma wherever a
  chi^gp((K/J)^gp) = dZ, d >= 1 identification is used. The existing
  displayed two-fold subtraction is retained; it DOES NOT require any
  single pin of the dead sector.

**Step 3.2 (re-prove lem:sieve(i) correctly; M-1/M-2).** Replace
lem:sieve(i)'s statement and proof by the level-strands filter:
  - Poset Xi: {below-fold levels} < {fold-ray strands indexed by rays
    rho} (top). Labels order-respecting by lem:depth.
  - For each fold-ray rho, the rho-fold strand {(f_rho, tau)} is
    differential-closed on tuples NOT containing a distinct-ray fold,
    and is contractible by lem:constcx with anchor H = f_rho (adjoining
    f_rho; every such tuple's face-omitting-f_rho lies one level lower;
    the transport is the identity since overlaps with f_rho have kernel
    J by lem:nerve(i) Case A, lem:mixed(C1)).
  - Apply lem:subquot successively over the finitely many rays: z is
    cohomologous to a cocycle vanishing on EVERY fold terrace. The dead
    sector is left arbitrary (it is not needed below).
  - Delete the clause "its dead positions are then pinned to a single
    element". Wherever prop:vanish used that clause, use Step 3.1(b)'s
    equality-of-fold-images instead.
  (This is the ONLY change to lem:sieve's statement; (ii) is retained
  with its proof unchanged — it was verified sound: the overlap of two
  K-exact pieces lies at levels >= K by lem:nerve(ii)/lem:mixed(C2), the
  >K values are already zero by hypothesis, so the K-exact cocycle
  relations pin ALL K-exact values to the value at i(P/K) along identity
  or canonical-quotient transitions.)

**Step 3.3 (Step 3 of prop:vanish — the K-induction; M-4).** Rewrite the
descending step as named references:
  (a) Assume values at levels strictly larger than K vanish. By
  lem:sieve(ii) all K-exact values are pinned to a single
  z_K-hat at B(i(P/K))-level.
  (b) The pair (f, i(P/K)) for a kernel-J fold is dead
  (lem:nerve(i)); its value lies in the already-killed or
  dead-coboundary sector; the cocycle equation at (f, i(P/K)) gives
  F(iota_{i(P/K)})(z_K-hat) = F(iota_f)(z_f); comparing two rays
  and using Step 3.1(b) gives F(pi_{K -> P})(z_K-hat) = 0 (keep the
  existing display; it is correct).
  (c) Kill z_K-hat itself: apply the induction hypothesis D(K)
  (strictly larger face) to the pullback of the cover along
  i(b) -> i(P/K): the pulled cocycle's class on i(P/K) vanishes after
  refinement; by lem:sieve(ii) applied at the K-level of the ORIGINAL
  cover the pinned constant z_K-hat is a transport of that pulled
  class, hence vanishes after one more pullback (rem:transfer). The
  sentence "after one more pullback" must cite rem:transfer; the
  sentence "the outward maps F(pi_{K->P}) of that constant are zero"
  must cite Step 3.3(b)'s display. DELETE every floating parenthetical.
  (Approved alternative to (c), choose ONE, do not write both: state a
  three-level filter lemma {levels < K} < {K-exact} < {levels > K}
  with the middle strand the constant one of lem:constcx anchored at
  i(P/K), whose kill is exactly D(K), and cite that instead.)
  (d) Rank-one and P={0} cases (q-skippedcases): replace the Step-2
  rank-one parenthetical by: "if dim(bar P) <= 1, the nerve of a
  standard rigid cover has at most one fold ray and the whole complex
  is the constant strand of lem:const (R_min = R_max = iB), so
  H^{q>=1} = 0 directly; P = {0} is lem:dead." Two sentences, named
  references.

**Step 3.4 (closeout).** Recompile twice; 0 errors / 0 undefined refs /
<= 16 pages. Update goal-tracker (B-8 -> resolved once M-2 closes; M-0
cleared). Commit with a message referencing this review; write the
round-3 summary. NO counterexample construction is permitted in this
round; if Steps 3.1-3.3 are genuinely blocked after an earnest attempt
(not an aesthetic preference), the only permitted fallback is the AC-4
honest-restatement branch: re-state thm:main as an open problem, keep
thm:descent/prop:adj/lem:* as proved propositions, and delete
thm:main-end's \qed claim — never leave an unproved theorem asserted.

Round 4 (review-driven): full line-by-line re-audit of the restored
Section 4 and the final Q-3 typography pass.

---

Mainline Progress Verdict: STALLED
(Steps 0-1 infrastructure landed and is verified — genuine progress on
B-7/B-9 — but the round's mainline objective was prop:vanish Steps 1-3,
which remain unclosed; Steps 1-2 introduced new fractures M-1/M-2; and
the worker's "likely false" verdict rested on an analysis of the wrong
map. Net: the deliverable is no closer to a valid proof of thm:main
than at the end of Round 1, though the support toolbox is now better.)

INCOMPLETE
<!-- CODEX's REVIEW RESULT  END  -->
---

## Goal Tracker Reference

Before starting work, **read** @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md to understand:
- The Ultimate Goal and Acceptance Criteria you're working toward
- Which Capability each Active Task belongs to, when the plan has a `Feature Map / Capability Map`
- Which tasks are Active, Completed, or Deferred
- Which side issues are blocking vs queued
- Any Plan Evolution that has occurred
- The latest side-issue state that needs attention

**IMPORTANT**: Keep the mutable section of `goal-tracker.md` up to date during the round.
Do NOT change the immutable section after Round 0.
If you cannot safely reconcile the tracker yourself, include an optional "Goal Tracker Update Request" section in your summary (see below).

## Mainline Guardrails

- Keep the mainline objective from @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md stable for this round
- Keep the Capability Anchor from @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md stable for this round
- Before implementing each mainline task, restate how it fits the anchored capability's business, design, and implementation context
- Do not let queued issues take over the round
- If Codex reported several findings, classify them into:
  - mainline gaps
  - blocking side issues
  - queued side issues
- Only mainline gaps and blocking side issues should drive the next code changes

---

Note: You MUST NOT try to exit by lying, editing loop state files, or executing `cancel-rlcr-loop`.

After completing the work, please:
0. If the `code-simplifier` plugin is installed, use it to review and optimize your code. Invoke via: `/code-simplifier`, `@agent-code-simplifier`, or `@code-simplifier:code-simplifier (agent)`
1. Commit your changes with a descriptive commit message
2. Write your work summary into @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-3-summary.md

## Task Tag Routing Reminder

Follow the plan's per-task routing tags strictly:
- `coding` task -> Claude executes directly
- `analyze` task -> execute via `/humanize:ask-codex`, then integrate the result
- Keep Goal Tracker Active Tasks columns `Tag` and `Owner` aligned with execution

## Capability Anchor Reminder

If the plan contains `## Feature Map / Capability Map`:
- The round contract must name the relevant Capability ID(s) or capability/feature name(s)
- Goal Tracker Active Tasks must keep their `Capability` column aligned with the round contract
- Mainline work must preserve the selected capability's business, design, and implementation context
- Do not let queued or future-scope capability work take over the current round

**Optional fallback**: if you could not safely update the mutable section of `goal-tracker.md` directly, include this section in your summary:
```markdown
## Goal Tracker Update Request

### Requested Changes:
- [E.g., "Mark Task X as completed with evidence: tests pass"]
- [E.g., "Add to Blocking Side Issues: bug Y blocks AC-2"]
- [E.g., "Add to Queued Side Issues: cleanup Z is non-blocking"]
- [E.g., "Plan Evolution: changed approach from A to B because..."]
- [E.g., "Defer Task Z because... (impact on AC: none/minimal)"]

### Justification:
[Explain why these changes are needed and how they serve the Ultimate Goal]
```

Codex will review your request and reconcile the Goal Tracker if justified.
