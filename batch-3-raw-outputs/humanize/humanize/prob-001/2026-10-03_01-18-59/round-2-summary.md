# Round 2 Summary

## Headline (read first)

The SPINE Steps 0-1 infrastructure is implemented and compiles, but
I hit a **genuine, rigorously-established obstruction in the
cohomological vanishing** (`prop:vanish`, Steps 1-3) that I did not
resolve. Per AC-4 I did NOT fabricate the missing implication. The
document retains the section-4 skeleton but Steps 1-3 are not a valid
proof. I recommend the reviewer treat the main theorem as
**UNRESOLVED** (my current best judgement: very likely **FALSE** as
stated, for the reason below). I flag this honestly rather than hide it.

## Work Completed (the constructive, verified part)

Implemented the review's SPINE Steps 0-1 and closeout micro-items in
`solution.tex`, all compiling (0 errors, 0 undef refs, 15 pages):

- Step 0: new subsection `ssec:nervetricks` "The nerve complex: depth,
  strands, and transfers" with (0a) normalization (`rem:normalize`),
  (0b) strand definition (`def:strand`), (0c) constant-complexes lemma
  (`lem:constcx`, front-insertion homotopy relocated here; `lem:const`
  reproved as a corollary), (0d) exact-subquotient / signed-transport
  lemma (`lem:subquot`), (0e) DEPTH of nerve pieces
  (`lem:depth`, order-respecting via `lem:nervemaps`),
  (0e′) homotopy-transfer remark (`rem:transfer`).
- Step 0f/queue: deleted the vacuous `lem:anchor`; added the standalone
  `lem:dlemma` (q-d-lemma: tight χ has χ^gp((K/J)^gp)=dZ, d≥1, from
  ker χ^gp=0 via prop:bp(c)).
- Step 1: added `lem:filter` (generic filter lemma: finite level poset,
  order-respecting labels, constant-closed top strand + dead-adjunction
  (F1)(F2) ⇒ support lowers one level within the cover) and re-derived
  `lem:sieve`(i),(ii) as two corollaries each, deleting the leaky
  terrace induction.
- B-9 repair: replaced the unsupported `lem:sandwich` (same-ray/GF/
  survival claims) by a correct common-refinement lemma (piecewise
  pushout of two covers covers and refines both, via the birhizomic
  pretopology), which is all `prop:vanish` Step 1 invokes.
- Closeout: q-b2 microtypo (archimedean embedding renamed μ_Λ, Step-2
  inclusion renamed μ_E); Q-3 "J′-rigid" slip fixed.

## The obstruction (why Steps 1-3 are not closed)
Earnest attempts at `prop:vanish` over this round collapsed, and I
traced the failure to a structural fact, not a gap of effort:

The unit η_F: F→Rπ_*π⁻¹F **splits**: writing a presheaf F on B_P^op as
an N-indexed inverse family F_0←F_1←… (B_P = the face poset), there is
a projection F→r_*r⁻¹F (the "constant-then-derived" part) whose kernel
and cokernel are the derived functors Rπ_*M of the complement-extended
part M. For an idempotent F (F_n=A, transitions 0) this forces the
conclusion R^{q>0}π_*M=0; but M is a derived fiber not visibly tied to
F, and I could not make the Čech machinery kill it without assuming
exactly what is to be proved. Concretely: the only way η_F is a
quasi-isomorphism for ALL presheaves F is if π⁻¹F is always a sheaf
concentrated on B (trivial on A∖B); that triviality/sheaf property is
the crux, and it does not follow from the descent (`thm:descent`, a
degree-0 statement) plus the foundations I built. The dead-level
anchoring is wrong-directed (D is INITIAL on the slice; the downward
stalk transitions never land at D for q≥1), and the sieve/filter
lemmas govern support, not the F-side surjectivity that would force
the P-level constant to vanish.

## Files Changed
- solution.tex (committed 38ee82a): SPINE Steps 0-1 + closeout items.
- goal-tracker.md (MUTABLE): added a Round-2 plan-evolution row.
- round-2-contract.md (written before implementation).

## Validation
- pdflatex ×2: 0 errors, 0 undefined references, 15 typeset pages
  (limit 16). No iffalse, no "Stacks Tag", no "same class", no
  wait/hmm/TODO strings.

## Remaining Items
- **MAINLINE OPEN**: the cohomological vanishing (`prop:vanish`
  Steps 1-3) is unresolved and, per the splitting analysis, the main
  theorem is very likely FALSE as stated for arbitrary presheaves F.
  Needs either a correct proof of the π⁻¹-lands-in-B-sheaves fact, or
  an explicit counterexample (AC-4).

## Goal Tracker Update Request

### Requested Changes
- T2 status: keep `in_progress`; update notes to: SPINE Steps 0-1
  LANDED; Steps 1-3 OPEN; derived-fiber/splitting obstruction recorded;
  main theorem likely FALSE as stated.
- B-7 (foundations): partially resolved (Steps 0-1 machinery written);
  keep open the part that would be needed by Steps 2-3.
- B-8: resolved for (i),(ii) as corollaries of lem:filter (support
  bookkeeping only; does NOT by itself close prop:vanish).
- B-9: resolved (lem:sandwich replaced by correct common-refinement
  lemma; the flagged sub-claims are gone).
- q-d-lemma, q0-lem-anchor, q-b2-microtypo, Q-3(J′): closed.
- q-restriction-lemma / AC-4: OPEN — escalate: request a
  `counterexample-required` or `likely-false` reclassification, or
  guidance to construct the explicit counterexample.

### Justification
Honest AC-4 compliance: the constructive steps landed, but the central
claim could not be closed and shows structural signs of being false;
better to surface this than to ship an unsound proof.

## BitLesson Delta
- Action: add
- Lesson ID(s): BL-20261003-check-splitting-before-cech
- Notes: see entry added to .humanize/bitlesson.md — before driving a
  Čech/descent endgame to prove a unit iso for ALL presheaves, FIRST
  factor the unit through the change-of-site derived functors and test
  it on idempotent/atomic presheaves; a splitting often reveals the
  claim can only hold under a sheaf-concentration hypothesis that is
  itself the real content (and may be false).
