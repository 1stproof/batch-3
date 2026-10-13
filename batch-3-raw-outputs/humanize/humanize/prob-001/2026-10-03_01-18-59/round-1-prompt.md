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
- Write the current round contract to @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md

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
# Round 0 Review Result — prob-001

Reviewer: moonshotai/Kimi-k3 (max effort), reviewing Round 0 commit 9a5ab43.
Scope checked against plan.md (AC-1..AC-5), problem.tex (verbatim, twice),
round-0-contract.md, full solution.tex (all 1144 lines, read line by line),
solution.log (recompiled by reviewer: 11 pages, 0 errors, 0 undefined refs).

## Verification of Claudes claims

| Claim in summary | Reality |
|---|---|
| pdflatex 0 errors / 0 undefined refs / 11 pages | TRUE (reviewer recompiled; three harmless hyperref PDF-string warnings only) |
| solution.tex is the only mathematical deliverable, article class, standard packages | TRUE |
| Standalone and structural audit line by line | FALSE: the document contains a leftover iffalse/fi editorial block (~lines 657-690) with workflow commentary, and the audit missed five substantive gaps (B-1..B-5 below) |
| no reusable tooling/workflow lesson | accepted |
| Bidirectional universality of P -> P/K vs P[-c]^sharp (Prop. 2.1(a)); pushout-kernel criterion (Lem. 2.13) | Verified correct on the stated domain (f.g. monoids); sharpness used correctly |
| Valuative collapse Lem. 2.4 | Steps 1 and 3 verified correct; Step 2's final contradiction is INVALID (B-2) but the statement remains true and repairable in one clause |
| Descent Thm. 3.4 (Claims A and B) | Verified correct modulo B-1/B-3; the endgame argument is correct: composite bijective implies both maps bijective |

---

## Part 1 — Findings

### MAINLINE GAPS (plan-derived; block AC-1/AC-3/AC-5)

**G-1 (= tracker B-1). Silent change of the problems hypotheses.**
problem.tex: "a monoid is an integral, saturated, sharp, commutative, unital
semigroup." solution.tex line 43 adds **finitely generated**. The whole
proof then uses f.g. at: Prop. 2.1(b) (finitely many faces, Gordan),
Lem. 2.4 Steps 1-3 (f.g. Gamma; rational polyhedral cone), Cor. 2.5 (tight
functionals on pointed f.g. cones), and cover constructions producing only
f.g. monoids. This is not a normalization choice; it changes the class of
objects, and the answer can change with it: for non-f.g. P even the
affirmative answers mechanism (cofinal family of f.p. covers built from
folds and CFA pieces) is no longer available, because P -> N and P -> P/K
may fail to be of finite presentation, and "finitely many faces" is false.
AC-1 negative test ("leaves a substantive case unproved": the non-f.g. case)
and AC-3 (consistency with problem.tex) are violated.

**G-2 (= B-2). Lemma 2.4, Step 2: the contradiction is mathematically false as written.**
Lines ~179-183: after fixing a generator summand g outside H_1 with
delta-g >= n*gamma, the text concludes "but delta-g in H_1 (same class)".
This is wrong: delta-g is NOT in H_1 because g is not in H_1 and the
H_1-classes in the totally ordered Gamma/H_1 satisfy
class(delta-g) = max(class(delta), class(g)) = class(delta), which is 2.
Repair is one deletion: the clause before it already yields the
contradiction: g in H_1 and delta-g in H_1 (both lie in the convex submonoid
V cap H_1 since 0 <= g <= delta and 0 < n*gamma <= delta-g), and
delta = (delta-g) + g >= n*gamma for infinitely many (all large) n
contradicts H_1 archimedean. Delete the false clause; do not keep it in any
form.

**G-3 (= B-3). Finite presentation — a hypothesis of the problems central
definition — is never treated anywhere.**
(a) Birhizomicity of f REQUIRES f.p.; no structure map of any cover used
(P -> N, P -> P/K, the piece maps of an arbitrary given cover R) is ever
checked or assumption-verified to be f.p. Lem. 2.10 states f.p. as a
hypothesis and never uses it; Cor. 2.11 and 2.20 assert birhizomicity (hence
f.p.) silently; Cor. 2.19 invokes the defining property of "R is a cover"
(which includes f.p. of the slice map) without comment.
(b) Covers are treated as families of OBJECTS of A_P, with arbitrary
alpha: P -> Q (Thm. 2.12's N(S) refinement; Prop. 2.15's U; Lem. 4.3's
sub-configurations). Over non-surjective alpha the pushout arguments detour
through Z_U, L_U; the review verified the descent theorem works under the
weaker standing assumption "alpha surjective" (then Z_U = P + J^gp and
L_U = J^gp for all pieces, and every kernel-J piece receives a map from
iB(T)), but the paper never says covers may be assumed of this form, and
some claims are materially harder without it (Lemmas 4.2/4.3 are only ever
computed over i(b); see B-4).
(c) The refinement maps used in Lem. 4.5 (fold-vs-fold products U tensor V,
"with birhizomicity from Lem. 2.10") need f.p. and atomicity jointly; only
atomicity is mentioned.

**G-4 (= B-4). The Cech object never exists.**
Section 4 computes colim_R H-cech^q(R;G) but never defines the simplicial
object whose nerve is being computed: the "nerve" of a cover (iterated
pushouts, degeneracies from identities, face maps from structure maps
between pieces) is used throughout (Lem. 4.2 "in the nerve", Lem. 4.6
"terraces", Step 1 "all its components live at dead level") but constructed
nowhere, and the lemma that these multi-pushouts exist as f.p. monoids and
form a simplicial semicosheaf is absent. Consequently no cofinality
statement is available: the Verdier step "sheaf cohomology on i(b) equals
colim over Cech complexes of covers" (cited as "Stacks Tag 03F9/01GY") must
be replaced by (i) a definition of the nerve in the sliced site (degenerate
tuples included, alternating quotient), (ii) the statement and proof that a
structure map between nerve pieces over i(b) exists iff the kernel face
refines (true when the structure maps alpha are surjective; cite the
universal property of P/K), and (iii) the comparison theorem used, named
with its hypotheses in words rather than website tag numbers.

**G-5 (= B-5). Lemma 4.3(b) is false as stated in general and ambiguously stated.**
The parenthetical "adding a tight fold to a kernel-K configuration leaves
the kernel K" needs "tight" to mean different things in its two uses: for
the base piece it means tight on P-bar (valid only when the configuration
has Z = P + J^gp); for a kernel-K configuration it must mean ker phi = K
(with Z = P + K^gp). Written over an arbitrary U (non-surjective alpha_U)
both readings can fail. Restate as the two exact claims (implementation
plan item 5), each following from Lem. 2.13 as in the Lem. 4.2 Case A
computation.

Also within mainline: the iffalse/fi block (~lines 657-690) is leftover
workflow commentary inside the deliverable, an AC-5 breach, and it shows the
endgame of Thm. 3.4 was patched rather than audited. Delete it.

### BLOCKING SIDE ISSUES

None separate from B-1..B-6 above (all sit directly on the Ultimate Goal and
are classified as mainline gaps).

### QUEUED SIDE ISSUES (documented; must NOT take over Round 1)

- Q-1: after B-3/B-4, re-verify Lem. 4.2/4.3 kernel claims at the level of
  generality actually used (nerve pieces over common parents U, not only
  over i(b)).
- Q-2: after the B-2 repair, grep for any other implicit use of the removed
  "same class" shortcut (none found outside Lem. 2.4 / Ex. 2.17; Ex. 2.17
  verified OK).
- Q-3: typography pass ("leaves the kernel" wording; Def. 4.1 mentions
  J-prime-rigid without defining a J-prime; rank-one parentheticals).

---

## Part 2 — Goal Alignment Summary

ACs: 1/5 addressed cleanly (AC-1 and AC-3 have blocking gaps B-1..B-5; AC-2
has the tag-number citation; AC-5 has the iffalse block; AC-4 not
triggered) | Forgotten items: 0 | Unjustified deferrals: 0

The tracker marked T1/T3/T4 "completed", which this review contradicts
(f.g. normalization breach; iffalse block; audit missed B-1..B-5).
The reviewer has corrected the tracker: B-1..B-6 added as Blocking Side
Issues; T1/T3/T4 returned to in_progress with notes. Plan-evolution entries
are fine. No scope drift.

## Part 3 — Capability Map Summary

Capability anchor: N/A (plan.md has no feature/capability map) | Dependency
gaps: 0 | Scope drift: no

---

## Part 4 — Directive implementation plan for Round 1 (singular; execute as written)

Execute items 1-6 in order; recompile and commit after items 2 and 6.

**1. (Fix B-1, the f.g. scope breach).** Decide the scope via the following
test, carried out first:
   (STAR) prove that the sheaf condition and the acyclicity of G_F on i(b)
   need only be tested on covers of T whose pieces are f.p. under P, because
   the birhizomic topology on A_P^op (or on the f.p. part, with sheaves
   extended by the comparison lemma) is generated by such covers.
   The natural attempt: observe P -> P/K is f.p. only when K is the face
   generated by a single element, which for non-f.g. P need not cover all
   faces; hence the CFA family can genuinely fail to consist of f.p. maps.
   If (STAR) closes (Branch A: state exactly the comparison-lemma hypotheses
   used — every object of the site admits a cover by f.p. objects; continuous
   and cocontinuous inclusion of the f.p. part; cite SGA 4 III by name),
   rewrite section 1 to say all verification is reduced to covers by f.p.
   pieces, and apply the section 2 machinery only to f.p. data (with the
   sentence that all auxiliary monoids in section 2 lemma proofs are f.g.
   because they arise as f.p. data when P is f.g., which imposes the check
   in item 3). If (STAR) cannot be closed with bounded effort, take Branch B
   (honest restriction): state at the start of section 1, verbatim, that
   "monoid" is used exactly as in the problem but the theorem is proved for
   finitely generated P, with a closing remark describing precisely what
   obstructs the general case (f.p. of P -> P/K; finiteness of the face
   poset). Under no circumstances keep the current silent redefinition at
   line 43.

**2. (Fix B-2).** In Lem. 2.4 Step 2, delete the false clause (exact string:
"but $\delta-g\in H_1$ (same class) and $H_1$ archimedean bounds $n$:
contradiction.") and finish the step with: "then $g,\delta-g\in V\cap H_1$
(as $0\le g\le\delta$ and $0\le n\gamma\le\delta-g$), and
$\delta=(\delta-g)+g\ge n\gamma$ for infinitely many $n$ contradicts $H_1$
archimedean." Recompile; commit.

**3. (Fix B-3).** Add a subsection "Finite presentation" to section 2
immediately after Construction 2.2 containing exactly:
   (i) the definition of f.p. used (colimit-preservation, equivalently a
   quotient of a free f.g. monoid by a f.g. congruence); one line noting it
   is standard;
   (ii) proof that P -> N (surjective) is f.p. exactly when the graph of
   ker phi is a f.g. congruence, and P -> P/K is f.p. exactly when K is
   generated as a face by a finite set (equivalently one element); both
   automatic when P is f.g. (Prop. 2.1(b));
   (iii) a standing w.l.o.g. lemma: every cover admits a refinement whose
   piece maps are surjective (apply Cor. 2.11(b) at each piece, then
   Thm. 2.12, keeping f.p. members);
   (iv) one sentence each in Cor. 2.19 and Lem. 4.5 noting the slice and
   refinement maps are f.p. by (ii) and Thm. 2.12, and in Lem. 2.10 noting
   the necessity test maps v/d and d-times-id are f.p. by (ii).

**4. (Fix B-4).** At the start of section 4 add the definition of the Cech
nerve of a cover R = {T -> U_i} of i(b): its degree-q part is the closure of
R under iterated pushouts over i(b) (existing and f.p. by Construction 2.2
plus item 3(ii)), with degeneracies from identities and face maps from the
structure maps; prove (short lemma) that a structure map between nerve
pieces over i(b) exists iff the kernel face refines (surjective structure
maps; universal property of P/K), hence the nerve is a simplicial
semicosheaf for G_F (dead pieces: their G-value sits at the terminal
B-level; verify all face maps into a dead piece lie under the top level, one
sentence via the Phi-computation). Replace the "Stacks Tag 03F9/01GY"
citation by naming Verdiers hypercovering theorem and stating in words that
for a site with fiber products it computes sheaf cohomology as the colimit
over covers of Cech cohomology of the cover nerves as defined.

**5. (Fix B-5).** Replace Lem. 4.3(b)s parenthetical by the two exact
claims, each with its pushout-criterion proof modeled on Lem. 4.2 Case A:
   (C1) Phi_U = J and Z_U = P + J^gp imply Phi of (U tensor f_phi) = J for
   phi tight on P-bar = P/J.
   (C2) Phi_U = K and Z_U = P + K^gp imply Phi of (U tensor f_phi) = K for
   phi with ker phi = K, tight on P/K.
   Add one sentence noting that under the standing w.l.o.g. of item 3(iii)
   all nerve pieces used satisfy the respective Z-hypotheses.

**6. (Fix B-6 + closeout).** Delete the entire iffalse/fi block
(lines ~657-690). Run the queued Q-1/Q-2 checks. Recompile twice; verify 0
errors, 0 undefined references, at most 16 pages. Update the goal tracker
(B-1..B-6 out of Blocking as resolved; T1-T5 statuses per reality). Commit
with a message referencing this review; write the round-1 summary.

Round 2 (review-driven): a full line-by-line re-audit of the repaired
document, especially section 4 Steps 2-3 (the two-fold subtraction and the
descending face loop), whose strategy the review verified but whose written
justifications depend on B-3/B-4/B-5 having been repaired in the exact
places indicated.

---

Mainline Progress Verdict: ADVANCED
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

- Keep the mainline objective from @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md stable for this round
- Keep the Capability Anchor from @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md stable for this round
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
2. Write your work summary into @/work/first-proof-humanize-tdgou2bu/000-prob-001/.humanize/rlcr/2026-10-03_01-18-59/round-1-summary.md

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
