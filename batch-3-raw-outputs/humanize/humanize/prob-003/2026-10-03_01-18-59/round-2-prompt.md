Your work is not finished. Read and execute the below with ultrathink.

## Drift Recovery Mode

Codex judged the recent implementation rounds as failing to advance the mainline.

- Consecutive stalled/regressed rounds: 2
- Last mainline verdict: stalled

This round is a **drift recovery round**. Do not continue with normal issue-clearing behavior.

## Original Implementation Plan

**IMPORTANT**: Re-anchor on the original plan first:
@plan.md

## Required Recovery Re-anchor

Before changing code:
- Re-read @plan.md
- Re-read @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Re-read the recent round summaries and review results that led here
- Rewrite the round contract at @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md

Your recovery contract must contain:
- Exactly one recovered **mainline objective**
- The 1-2 target ACs that prove mainline progress this round
- The recovered **Capability Anchor**: relevant `Feature Map / Capability Map` node(s), or `N/A` if the plan has no capability map
- The root cause of recent drift or stagnation
- Which issues are truly **blocking** the recovered mainline objective
- Which issues remain **queued** and explicitly out of scope
- Concrete success criteria that would change the verdict back to `ADVANCED`

Do not start implementation until the recovery contract exists.

## Task Lane Rules

Use the Task system (TaskCreate, TaskUpdate, TaskList) with one required tag per task:
- `[mainline]` for plan-derived work that directly advances the recovered objective
- `[blocking]` for issues that prevent the recovered mainline objective from succeeding safely
- `[queued]` for non-blocking bugs, cleanup, or follow-up work

Rules:
- This round must prove mainline movement, not just reduce noise
- `[blocking]` work is allowed only when it directly unblocks the recovered mainline objective
- `[queued]` work must stay documented but must NOT replace the recovered objective
- If a new issue does not block the recovered objective, tag it `[queued]` and keep moving on mainline work

---
Below is Codex's review result:
<!-- CODEX's REVIEW RESULT START -->
# Round 1 Review Result - prob-003 (bigon algebra = generalized quantum double)

Reviewer: independent audit of `solution.tex` (commit 952d32c), the round-1
summary, the goal tracker, and the worker scratch. Build state: pdflatex
compiles, 12 pages, 0 undefined refs (AC-5 fine). The pairing calculus
(lem:T, lem:compat) and the three-channel commutator (prop:EF) are NOW
CORRECT - I re-derived them from (PA),(P),(C),(S),(SK) in two exact engines
built for this review (rational functions in t, q=t^12) and by hand.
But the keystone cross-conjugation Lemma (lem:cross) is proved with TWO
CANCELLING SIGN SLIPS whose net effect is the fatal one: its statements
(a),(b) carry the INVERSE scalar of what the paper's own (SK) gives.
Everything routed through (a)/(b) as statements (centrality lem:loops, the
diagonal quotient's consistency with internal (H1), the def:A families
(M0)b and (M1), and all "machine verification" of the cross rules) is
unsound. The mainline is NOT established.

## Mainline Progress Verdict: STALLED

Genuine round-1 progress (verified by the reviewer from the axioms, not by
trusting the worker's scripts): the pairing table lem:T and the
compatibility lem:compat are right; prop:EF
$F_sE_r-E_rF_s=\delta_{rs}\theta(\cK_r^{(+)}-\cK_s^{(-)-1})$ is right
(three channels, two engines, hand check - all agree); (M2) holds exactly
as printed; thm:mixed(b),(c),(d) hold exactly as printed; the minor images
of prop:t are right; the external inputs are now honestly stated. But the
"quantum double" object as presented is internally inconsistent, Part 1's
map is well-defined only onto the wrong algebra, and Part 2's quotient
$D/J$ is mathematically wrong (it collapses to the Cartan torus).

```
ACs: 1/5 fully met (AC-5 only) | Forgotten items: 0 | Unjustified deferrals: 0
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
```

=====================================================================
## A. BLOCKING SIDE ISSUES (on the mainline path; must be fixed)
=====================================================================

### A1R (FATAL). lem:cross(a),(b) are false as stated; their proofs contain the same sign error twice

Reviewer recomputed the one-channel (SK) evaluations from (DE),(P),(PA)
(after re-verifying the pairing table and the grouplike pairing
$\la\hK^u,\hK^v\ra=q^{u\cdot v}$, $u\cdot v=\frac1n(\sum u)(\sum v)-\sum
u_kv_k$, on a full weight grid). Facts, all machine-confirmed:

- Channel value in (a): $E_r\hK^{u(-)}=\la\hK^u,\cK_r\ra\,\hK^{u(-)}E_r
  =q^{\,u\cdot\kappa_r}\hK^{u(-)}E_r$, where $\kappa_r=e_r-e_{r+1}$ is the
  weight of $\cK_r$. The paper's display reads $q^{\,u\cdot\alpha_r}$ -
  SIGN SLIP #1, since $\kappa_r=-\alpha_r$ and
  $u\cdot\kappa_r=\alpha_r(u)$. So the truth is
      $$E_r\hK^{u(-)}=q^{+\alpha_r(u)}\hK^{u(-)}E_r .$$
- The next line "using $u\cdot\alpha_r=-\alpha_r(u)$" then misapplies
  $(\ast)$ to the wrong-side expression - SIGN SLIP #2. The two slips
  cancel inside the proof, and the statement (a) inherits slip #1:
  printed (a) says the cross-conjugation by $\hK_i^{(-)}$ on $E_r$ is
  $q^{+\alpha_r(i)}$; the (SK)-true value is $q^{-\alpha_r(i)}$.
  Numerically (n=2, r=1): true $E_1\hK_1^{(-)}=q^{-1}\hK_1^{(-)}E_1$
  (engine output `1*t^-12`), but (a) asserts the $q^{+1}$-conjugation.
- Same phenomenon in (b)(c): in (b) the channel scalar
  $\la\cK_s^{-1},g^{-1}\ra=q^{\kappa_s\cdot\mu}$ is displayed as
  $q^{(-\alpha_s)\cdot(-\mu)}$ and evaluated by $(\ast)$, producing the
  inverse of the true exponent in the conclusion; the (SK)-true value of
  the cross-conjugation by $\hK_i^{(+)}$ on $F_s$ is $q^{+\alpha_s(i)}$
  (engine: $\hK_1^{(+)}F_1=q^{+1}F_1\hK_1^{(+)}$ at n=2), while printed
  (b) gives $q^{-\alpha_s(i)}$. In (c), the grouplike channel scalar is
  $\la g,g'\ra$, not $\la g,g'\ra\la g,g'^{-1}\ra$ (there is exactly one
  pairing factor, not two); the conclusion "commute" is true but the
  displayed computation is wrong.

Consequences (each independently fatal unless fixed):

1. **lem:diag is physically false for the true $D$.** With the true
   cross rules, setting $\hK^{(+)}=\hK^{(-)}=\hK$ makes the cross
   relations read: conjugation by $\hK_i$ on $E_r$ is $q^{-\alpha_r(i)}$
   and on $F_s$ is $q^{+\alpha_s(i)}$, while the internal (H1) relations
   give the opposite powers. Hence
   $(q^{\alpha_r(i)}-q^{-\alpha_r(i)})E_r=0$ for $i\in\{r,r+1\}$ and the
   $F$-analogue, so at generic $q$ every $E_r,F_s$ vanishes: $D/J$ is
   the Cartan torus, not $H$. lem:diag's conclusion "exactly
   Definition def:H" is only sustained by the wrong-signed (a),(b).
2. **$D$ as presented is not associative under the wrong signs.**
   lem:loops's proof computes conj of $\Omega_i=\hK_i^{(+)}\hK_i^{(-)-1}$
   on $E_r$ as (H1) $\times$ (a$^{-1}$) $=q^{+\alpha_r(i)-\alpha_r(i)}
   =1$. But (a$^{-1}$) there is the paper's inverse rule; under the
   statement (a) that the same paper asserts, the cross factor flips and
   the total is $q^{2\alpha_r(i)}\neq1$. Both computations are quotable
   from the paper's own rules, so the presented word algebra violates
   associativity. (This is the algebraic shadow of consequence 1:
   centrality of $\Omega$ in an associative double is EQUIVALENT to the
   consistency of the diagonal quotient.) The worker's vtest.py
   Omega-centrality checks ("om1..om4") FAIL at n=2,3,4 and were
   dismissed as stale; eng2.py avoided the check. No correct script has
   ever verified centrality in a derived-from-(SK) model.
3. **thm:mixed(b),(c),(d) survive; def:A's (M0)b and (M1) families are
   wrong for a genuine double.** Because the paper derived them from the
   wrong-signed (a)/(b), the (M0)b scalar $q^{\alpha_j(i)}$ and the (M1)
   family $q^{-\alpha_i(j)}$ are not what a consistent double gives.
   Note (M1$'$) as printed in thm:mixed(c) coincidentally equals what
   the TRUE (a$^{-1}$) gives, i.e. the arc-relation (M1) is compatible
   with the true cross rules - but any salvage must re-derive the
   presentation, not re-quote (a)/(b).
4. **The round-1 "machine verification" of lem:cross is void.** Both
   vtest.py and eng2.py IMPLEMENT the paper's rule table (their
   docstrings say so) and re-check it against itself; the only battery
   that derives values from (PA),(P),(C) is pair2.py (which passes and
   is sound, and which this reviewer used). The worker summary's claims
   "cross-conjugation lemma ... one-channel (SK) evaluations ...
   machine-verified" and "Omega-centrality all generator pairs PASS" are
   not supported by any script that derives the cross rules from (SK).

### A2R (BLOCKING). The round-1 repair direction (the reviewer's directive)

The problem statement (and the round-0 review's D1) both allow rebuilding
the object rather than patching signs. The diagonal computation that MUST
be repaired has the following structure (all pieces verified by the
reviewer): the cross commutator lands on
$\delta_{rs}\theta(\cK_r^{(+)}-\cK_r^{(-)-1})$, i.e. the two Cartan
lattices enter with OPPOSITE exponents. Consequently a consistent nonzero
double with internal (H1) on both Borels exists only if the cross
conjugations match, which forces the antipodal-loop
$\Omega_i^{anti}=\hK_i^{(+)}\hK_i^{(-)}$ (NOT $\hK_i^{(-)-1}$) to be
central, and turns the quotient kernel into
$\cK_i^{(+)}-\cK_i^{(-)}$ IN DIFFERENCE-PAIR FORM
$(\hK_i\hK_{i+1}^{-1})^{(+)}-(\hK_i\hK_{i+1}^{-1})^{(-)}$. There are two
coherent implementations; round 2 must implement exactly one, with every
rule derived from a single sign convention:

*(i) Preferred, fully elementary.* Keep def:A's $\Sn(\B^*)$ EXACTLY as
  printed (it is the declared presentation of the problem's surface
  algebra), keep the correct (M2), thm:mixed(b),(c),(d), prop:t, and
  REDEFINE the target as the UNIVERSAL algebra
  $\widetilde D$ on generators $\hK_i^{(\pm)\pm1},E_r,F_s$ with (H1),
  (H3)$_E$, (H3)$_F$, and the three cross families
  $\hK_i^{(-)}E_r=q^{-\alpha_r(i)}E_r\hK_i^{(-)}$,
  $F_s\hK_i^{(+)}=q^{-\alpha_s(i)}\hK_i^{(+)}F_s$,
  $[E_r,F_s]=\delta_{rs}\theta(\cK_s^{(-)-1}-\cK_r^{(+)})$ -
  where the cross exponents are chosen MINUS-internal precisely so that
  the anti-identification $\hK_i^{(+)}=\hK_i^{(-)-1}=:\hK_i'$
  consistently yields (H1) in the quotient. Prove:
  (1) $\Omega_i^{anti}=\hK_i^{(+)}\hK_i^{(-)}$ is central in
  $\widetilde D$ (both cross conjugations now agree with the internal
  ones after inversion);
  (2) the PBW basis exists (the cross rules are confluent); THEN the
  presentation is associative and coincides with the standard
  $U_q^{ext}(\mathfrak{gl}(n))$: the map
  $\gK_i\mapsto\hK_i^{(+)}$, $\gK_i'\mapsto\hK_i^{(-)-1}$ identifies
  the cross commutator with the difference-pair relation;
  (3) $\Phi:\Sn(\B^*)\to\widetilde D$,
  $b_{ii}\mapsto\hK_i^{(+)}=\gK_i$,
  $c_{ii}\mapsto\hK_i^{(-)-1}=\gK_i'$,
  $b_{i,i+1}\mapsto E_i\hK_{i+1}^{(+)}$,
  $c_{i+1,i}\mapsto\hK_{i+1}^{(-)-1}F_i=(\gK_{i+1}')F_i$
  is well-defined - the (M0)b family must be RE-DERIVED and will come
  out with the corrected scalar $q^{-\alpha_j(i)}$?? - derive it
  mechanically from (2)'s rules, do not transpose from the round-1
  paper; (M1) similarly; (M2) and (M3) are already correct;
  (4) Part 2: $I=(\omega_i-1)$, $\Phi(\omega_i)=\gK_i\gK_i'$; the
  quotient $\widetilde D/(\gK_i\gK_i'-1)$ has presentation (H1),(H2),
  (H3) in $E_r,F_r$ and the difference-pair Cartans
  $\cK_r=\gK_r\gK_{r+1}^{-1}=(\cK_r^{+})=(\cK_r^{-})$-identified,
  with residual Cartan lattice of rank $n-1$: this is the adjoint-form
  $U_q(\mathfrak{sl}(n))$, with $\Omega=\prod\hK_i=1$ automatic. State
  precisely which Cartan form survives (adjoint vs simply connected)
  and reconcile with the problem's $U_q^{ext}$: if the problem's
  algebra is strictly the simply-connected one, the isomorphism of
  Part 2 holds only after adjoining the free central rank-1 lattice;
  this must be stated honestly, since the skein ideal forces
  $\prod(\hK_i^{(+)}\hK_i^{(-)-1})=1$ relationships only through the
  $\omega_i$.

*(ii) Alternative.* Declare $D:=U_q^{ext}(\mathfrak{gl}(n))$ directly
  (standard presentation, no skew-pairing axiomatization), cite the
  Drinfel'd-Tanisaki theorem that it is the generalized double of the
  two Borels w.r.t. the stated pairing (under the anti-diagonal
  Cartan identification), and do Parts 1-2 entirely in the
  $U_q^{ext}(\mathfrak{gl}(n))$ presentation. This keeps every
  existing correct computation (lem:T is used only through (P) values;
  prop:EF, M2, thm:mixed(b),(c),(d), minor images) and removes the
  need to re-derive (SK)-channel Tables with correct signs. Risk: the
  double identification must be stated exactly; the (M0)b,(M1)
  scalars still must be recomputed in the new presentation.

In BOTH options the following round-1 content may be reused verbatim:
lem:T, lem:compat, prop:EF and its proof, the (M2) display and proof
(except the two intermediate crossing scalars, which are each inverted
in the round-1 text; with the repaired rules recompute both crossings
and print the true pair - their product must remain 1), thm:mixed(b),(c),(d) proofs, prop:t,
lem:split as a Laurent-monomial argument (re-targeted at
$\Omega_i^{anti}$), the PBW-bijection strategy of thm:one, and the
ideal-equality skeleton of thm:two.

### A3R (BLOCKING, AC-3). Verification claims outrun what the scripts do

- vtest.py and eng2.py hard-code the paper's rule table; they cannot
  detect sign errors in lem:cross and they did not (their M3/M1
  "machine-derived exponents" are derived WITHIN the wrong rule world,
  here coinciding with correct values because those relations route
  through (a$^{-1}$)/(b) in the directions the paper uses).
- vtest.py as committed prints 24 FAILURES (stale 'A' literals, wrong-
  signed 'M2' and 'om' expectations); the summary's "stale literals
  superseded" line understates that the om-checks that WOULD have caught
  the centrality contradiction are among them.
- Round-2 rule: every machine-supported claim must come from a script
  that implements (PA),(P),(C),(S),(SK) directly (or the option-(ii)
  presentation relations, stated as such in the docstring) and asserts
  only differences computed by the engine, never hand-entered
  expectations labelled by the relation being "verified".

=====================================================================
## B. MAINLINE GAPS (vs plan ACs)
=====================================================================

- G1 (AC-1): Part 1 not established: the map $\Phi$ is proved well-
  defined only against the wrongly-presented $D$; a consistent double
  satisfying internal (H1)+(H1)-matched cross rules+prop:EF forces
  (M0)b,(M1) families different from at least one of {def:A,(a),(b)} -
  the conflict must be resolved by A2R. Part 2 not established:
  lem:diag collapses under true rules (torus, not H), and
  thm:two inherits it.
- G2 (AC-2): OK - external inputs are now precisely stated (skein
  presentation = def:A via Lê's triangular decomposition; existence of
  the skew pairing / double construction).
- G3 (AC-3): FAILED at the cross-conjugation lemma (two cancelling
  slips); the "83 PASS" battery is sound but covers only the pairing
  layer; the cross-rule battery tests hard-coded rules; see A3R.
- G4 (AC-4): currently asserts (and "verifies") sign-wrong statements;
  the honest repair exists (A2R) and most computations are already
  correct.
- G5 (AC-5): OK (12 pages, standard packages, compiles clean).

=====================================================================
## C. QUEUED SIDE ISSUES (do NOT take over next round)
=====================================================================

- Q1. scratch/ tidying remains deferred to final submission.
- Q2. vtest.py stale literals must be deleted/replaced when the battery
  is rebuilt (fold into A3R, no separate effort).
- Q3. BitLesson BL-20261003-skew-pairing-bookkeeping must be UPDATED
  AGAIN: the round-1 text enshrined "machine-derived exponents" but the
  real lesson is now: derive cross rules from the pairing axioms in the
  verifier itself; a passing battery over a hand-entered rule table is
  evidence of nothing; cancelling sign slips inside one lemma pass every
  consequence routed through pairwise-cancelling uses (M2, thm:mixed(b))
  while destroying single-use consequences (centrality, quotient).
- Q4. When touching thm:one, add the one-sentence triangularity
  argument for why images of ordered arc monomials are independent in
  the PBW basis (minor images are two-term combinations, so "exponent
  data preserved" is not literally true as written).

=====================================================================
## D. DIRECTIVE FOR ROUND 2 (execute in order)
=====================================================================

Objective: a consistent target algebra, a well-defined isomorphism for
Part 1, a correct quotient for Part 2. Est. 3-4 pages net change.

D1. Implement A2R option (i) or (ii) - pick (ii) if the double
    identification can be stated exactly within the page budget,
    otherwise (i). Whichever is chosen, the cross rules must be written
    once, from one sign convention, and the omega-family must be the
    anti-podal one ($\hK_i^{(+)}\hK_i^{(-)}$-type). Prove associativity
    (PBW/confluence) of the presented target BEFORE using it.
D2. Re-derive the mixed relations of def:A mechanically from the
    repaired rules: (M2),(M3),(M0)a are correct; recompute (M0)b and
    the (M1) family and update def:A / thm:mixed accordingly. Fix the
    two inverted intermediate scalars in the (M2) proof display.
D3. Redo Part 2: centrality of the arc loops in $\Sn(\B^*)$ follows
    from the presentation + Phi-injectivity; the quotient identifies
    the difference-pair Cartans; state exactly which Cartan lattice
    survives and reconcile with the problem's $U_q^{ext}(\sl(n))$
    (adjoint vs simply connected; add the free rank-1 factor if
    needed, stated as such).
D4. Rebuild the verification battery per A3R (derived-from-axioms
    engine only; assert engine-vs-engine differences); update
    rem:verify to describe exactly what is checked. Fix Q4's
    triangularity sentence in thm:one.
D5. Recompile; <= 16 pages; update tracker; BitLesson per Q3; commit.

=====================================================================
## E. GOAL-TRACKER ACTIONS (already applied by reviewer)
=====================================================================

- Plan Evolution Log: added "1 (review) CORRECTION" row recording the
  lem:cross sign slips, the void verification of the cross rules, and
  the collapse of D/J.
- Active Tasks: the five falsely-DONE mainline rows replaced by the
  round-2 tasks (one-sign-convention cross rules; re-derived (M0)b/(M1);
  Part 1 with triangularity; Part 2 with the honest Cartan bookkeeping;
  verification-honesty task).
- Blocking table: A1/A2 re-opened with the precise defect descriptions.
- Completed-and-Verified: AC-1/AC-2 rows removed; added a "(partial)"
  row for the reviewer-verified fragments (lem:T, lem:compat, prop:EF,
  M2/M0a/M3, minor images) and kept AC-2/AC-5.

Reviewer verdict: NOT complete. The round-1 summary's claims "all proved
and machine-verified" for thm:mixed (a)-(e) and "Omega_i central ...
PASS" do not survive audit; Part 1 and Part 2 remain open. Round 2 must
execute Part D.
<!-- CODEX's REVIEW RESULT  END  -->
---

## Goal Tracker Reference

Before starting work, **read and update** @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md as needed:
- Keep the immutable section unchanged
- Re-anchor Active Tasks on the recovered Capability Anchor when the plan has a `Feature Map / Capability Map`
- Record the drift/stagnation cause in the mutable section if it changed planning
- Keep blocking vs queued issue classification accurate
- Ensure the tracker and contract now describe the same recovered mainline objective

## Recovery Guardrails

- Do not spend this round mostly on queued cleanup
- Do not broaden scope to compensate for previous stalls
- Do not jump to unrelated or future-scope capability nodes to compensate for previous stalls
- If the original approach was flawed, log the plan evolution explicitly instead of silently changing direction
- If you cannot produce a credible recovered mainline objective, say so in the summary with concrete blockers

## BitLesson Selection (REQUIRED FOR EACH TASK)

Before executing each task or sub-task, you MUST:

1. Read @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each task/sub-task to select relevant lesson IDs
3. Follow the selected lesson IDs (or `NONE`) during implementation

Reference: @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/bitlesson.md

---

Note: You MUST NOT try to exit by lying, editing loop state files, or executing `cancel-rlcr-loop`.

After completing the work, please:
0. If the `code-simplifier` plugin is installed, use it to review and optimize your code. Invoke via: `/code-simplifier`, `@agent-code-simplifier`, or `@code-simplifier:code-simplifier (agent)`
1. Commit your changes with a descriptive commit message
2. Write your work summary into @/work/first-proof-humanize-tdgou2bu/002-prob-003/.humanize/rlcr/2026-10-03_01-18-59/round-2-summary.md

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
