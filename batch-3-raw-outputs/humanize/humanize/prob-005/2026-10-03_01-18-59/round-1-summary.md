# Round 1 Summary

## Work Completed

The round-0 document was rejected by review (correctly) for proving the
free case "granting" an unproved lemma supported by enumeration, and for
asserting a false structural claim (|H×/⟨g³⟩| ∈ {1,3}) attributed to
Massouros/Baker–Bowler. This round's mainline objective (per the round-1
contract) was to close the free case from (H1)–(H4) alone, or — if that
proved impossible after genuine effort — to implement review Option B.

**Option A (close the free case) was attempted exhaustively and did not
succeed.** Six distinct proof calculi were tried, all failing:
1. Saturated set-level S1-replacement closure (only produces
   supersets; never pins the needed value).
2. Multidegree-decorated binomial towers with cancellation bookkeeping
   (the "missing" terms cancel only at value level, unreachable by
   valid moves).
3. The value-swap step 1∈g⊞m, m∈M ⟹ 0∈g⊞(−1)⊞(ab)³ — numerically
   FALSE for the canonical (F3-produced) witnesses in ~7% of instances
   (a concrete counter-instance in F₁₉/{±1} was isolated, so the
   reviewer's suggested chain in Option A does NOT close either).
4. The general cancellation lemma 0∈X⊞S ∧ 0∈(−S)⊞T ⟹ 0∈X⊞T — false
   in arbitrary hyperfields (random counterexamples found), though it
   happens to hold in the specific structured instance.
5. Explicit witness-family constructions (v∈{1}, v∈u³, v∈ab·u², ...):
   families cover only 82.6% of instances; no finite union of provable
   families is complete.
6. Quotient-by-cubes / Massouros-type structural reductions: the needed
   general lemma |G|≤3 is false over Q (reviewer's counterexample), and
   the route found no replacement.

**Option B was then implemented**, exactly as the reviewer's binding
instruction prescribes: `solution.tex` was rewritten to
- keep and correct Section 1 (preliminaries) including the clean fix of
  the garbled step in lem:basic(iv) (erratum B3.2) and the typo in
  prop:degen (B3.3);
- prove the degenerate case (Prop 2.3) and the collapse case (Lemma 3.1,
  Corollary 3.2) fully from (H1)–(H4);
- isolate the remaining free case in the precisely stated Elevation
  Problem (Remark 4.4), proven equivalent to the unconditional statement
  in the free case;
- prove Theorem 2.1 only in its conditional form (Elevation Problem ⇒
  full theorem);
- contain NO assertion of "yes" for the original question, and no use of
  enumeration, computation, external structural theorems, or unproved
  lemmas as proof steps anywhere.

## Files Changed

- `solution.tex` — rewritten (Option B); 5 pages, article class, only
  amsmath/amssymb/amsthm/mathtools/geometry/enumitem/hyperref.
- `.gitignore` — ignore pdflatex artifacts (carried from round 0).
- `.humanize/rlcr/2026-10-03_01-18-59/round-1-contract.md` — round
  contract (mainline objective + success criteria).
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` — mutable section:
  Plan Evolution entry for the downgrade; active tasks updated; the
  false-claim issue marked resolved; the open Elevation Problem recorded
  as the remaining item.

## Validation

- `pdflatex -interaction=nonstopmode -halt-on-error solution.tex`
  two passes: exit 0, no errors, no undefined references, 5 pages (≤ 16).
- Forbidden-content check on the rendered PDF text: no occurrences of
  "hmm/wait/rather", "enumeration", "verified", "Massouros",
  "Baker–Bowler", "cube subgroup", "exchange lemma", "descent",
  "disagreement", "99.6%", "137 403", "618 867", "154".
- Every proof step in Sections 1–4 was reread in the PDF and audited
  against (H1)–(H4) or a lemma proved in the document.

## Remaining Items (the honest state)

- AC-1 is NOT met for the original question: the free case remains open
  as the Elevation Problem (Remark 4.4 of solution.tex):
  1∈a⊞b ⟹ 0∈a³⊞b³⊞(−1)⊞(ab)⊞(ab)⊞(ab), proven equivalent there to the
  original problem in the free case. Any future proof of it immediately
  completes the theorem. The empirical evidence (round 0: 137 403
  instances, 0 failures) makes the affirmative answer very likely true,
  but the present document does not assert it as proved.
- The reviewer may judge AC-1 unmet; per Option B the summary marks this
  explicitly rather than assert "yes".

## Goal Tracker Update Request (only if direct edits are read
    conservatively; the mutable section WAS updated)

- Plan Evolution: round-1 entry added (verdict downgraded per Option B).
- Queued: false cube-subgroup claim marked RESOLVED; open Elevation
  Problem recorded as the remaining item.

## BitLesson Delta

- Action: none
- Lesson ID(s): NONE
- Notes: bitlesson-selector binary not present in the environment; the
  KB was read directly and contains no entries. No new lessons added.
