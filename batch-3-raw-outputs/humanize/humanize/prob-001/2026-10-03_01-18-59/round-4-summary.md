# Round 4 Summary

## Bottom line (read first)

I repaired M-5 (the lem:sieve proof is now sound and self-contained)
and I executed the review's Step B residuum approach — but the
residuum (M-8 / B3) is **unsound for arbitrary presheaves F**, so the
higher-direct-image vanishing cannot be honestly claimed. Per AC-4 I
took the only defensible branch: the deliverable now proves exactly the
sheaf property + degree-zero unit (verified) and records the two open
points. T2 is NOT complete; this summary includes a Goal Tracker Update
Request. The reviewer must adjudicate whether its B3 residuum has a
valid completion for all F that neither the review nor I could write
soundly.

## Work Completed

- **Step A (M-5) — DONE.** `lem:sieve` re-proved: the false `(ii)`
  single-`K` pin is deleted, and the `(i)` proof is now the explicit
  self-contained contraction `(w_r)_sigma := z_{(f_r,sigma)}` with the
  two-term identity displayed, identity transports cited to
  lem:nerve(i) Case A / lem:mixed(C1); the invalid `lem:constcx`
  citation is removed. Lemma renamed "Sieve: fold terraces".
- **Step B (M-6/M-8) — ATTEMPTED, found unsound.** prop:vanish Step 1
  (dead-sector hygiene) and Step 2 (fold terraces via lem:sieve) are
  sound and kept. Step 3 was restructured as the iB-contraction
  residuum kill, but the kill only closes `[z]=0` when the sheaf
  `\mathcal G` agrees on the base face and its quotient faces; for a
  **general** presheaf `F` the transitions `F(b) -> F(B(i(P/K)))` are
  quotient maps, not identities, and the dead/\ensuremath{iB}
  discrepancy at kernel-`J` tuples cannot be absorbed into Step 1's
  `w` (which lives only on the dead level). So the residuum does NOT
  give H^{q>0}=0 for all F. I did not fabricate it.
- **Step C (M-7, AC-4 honest closure) — DONE.** thm:main restated to
  exactly the proved content (sheaf property + degree-zero unit, for
  finitely generated P); prop:vanish downgraded to (a) H^0=F(b) and
  (b) the fold/dead reduction, with H^{q>0}=0 explicitly NOT claimed;
  a Closing remark records the two open points (higher direct images
  for arbitrary F; non-f.g. P via rem:nonfg's obstructions), with no
  counterexample claimed; the title and Overview were aligned so no
  unsupported quasi-isomorphism assertion remains anywhere (grep
  verified).
- **Step D — DONE.** Recompiled twice: 0 errors, 0 undefined
  references, 15 pages (limit 16). Greps: no iffalse / Stacks / same
  class / TODO / dangling lem:restrict / sieve(ii).

## Files Changed
- solution.tex (committed 030ed79): lem:sieve rewritten; prop:vanish
  downgraded with honest Step 3; lem:restrict deleted; thm:main +
  Closing remark + title + Overview aligned.
- goal-tracker.md: Round-4 plan-evolution row.

## Validation
- pdflatex x2: 0 errors, 0 undefined references, 15 pages.
- No unsupported `q>0` assertion: the only "R^{q>0}=0" string is in the
  Closing remark, saying it is NOT proved.

## Remaining Items
- MAINLINE OPEN: H^{q>0}(i(b),G_F)=0 for arbitrary F is unresolved and
  (per the above) does not follow from the residuum; I found no proof
  and no counterexample. If the intent is YES, it needs a genuinely
  different ingredient I could not locate.

## Goal Tracker Update Request

### Requested Changes:
- T2 (develop complete proof of quasi-isomorphism): keep
  `in_progress`; note = "degree-0 (R^0) proved via sheaf+descent;
  q>0 for arbitrary F OPEN — residuum contraction invalid for general
  F; no proof or counterexample found".
- B-8: mark RESOLVED (lem:sieve(i) repaired self-containedly; sieve(ii)
  retired/deleted as no longer needed).
- M-5: RESOLVED. M-6/M-8: mark "attempted; residuum unsound for
  arbitrary F; higher-images open". M-7 (AC-4): mark as the taken
  branch (sheaf + R^0 proved; q>0 and general P diagnosed open, no
  counterexample).
- New open item: "higher-direct-images for arbitrary F" on AC-1/AC-4.

### Justification:
AC-4 forbids asserting the unproved q>0; the residuum (the only route
offered) is unsound for general F. Honest restatement is the only
defensible closure, unless the reviewer supplies a valid completion of
the residuum for all F.

## BitLesson Delta
- Action: update
- Lesson ID(s): BL-20261003-check-splitting-before-cech
- Notes: extend — a "constant-strand / iB-contraction" residuum kill is
  valid ONLY when the sheaf's transition maps on the relevant face
  poset are identities; for a general presheaf the quotient maps are
  not, so the cocycle need not be a coboundary. Before driving a
  residuum contraction, verify the transitions on the residuum are
  identities (or the sheaf is constant there); otherwise the
  contraction leaves an unkillable discrepancy.
