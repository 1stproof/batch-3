# Round 4 Contract

## Mainline Objective

Make `prop:vanish` a proof by REPLACING the face-induction fragment
(which has the fatal element-vs-image gap M-6) with the review's
degree-inductive residuum calculation (M-8 / Step B: after sieve(i)
kills fold terraces, the residuum is constant on the face poset with
minimum iB, and every cocycle on it is a coboundary via the displayed
contraction — so [z]=0 within one cover). Repair the lem:sieve(i)
citation fracture (M-5 / Step A: expand to the self-contained
contraction display, drop the lem:constcx citation). Close the document
at AC-4's f.g. branch (M-7 / Step C: Closing Remark for arbitrary P
naming the two obstructions; no counterexample claimed). Then Step D
closeout.

## Target ACs

- AC-1 (prop:vanish proved line by line; thm:main-end proved for f.g. P)
- AC-4 (honest closure: f.g. theorem proved + general case diagnosed as
  open with named obstructions; the counterexample route stays rejected)

## Capability Anchor

N/A (plan.md has no Feature Map / Capability Map).

## Blocking Side Issues in Scope

- M-5: lem:sieve(i) cites lem:constcx through a failing hypothesis
  (anchor f_r not a minimum of the strand); expand to the explicit
  contraction (two-line display), cite lem:mixed(C1)/lem:nerve(i)
  Case A for identity transports, drop the lem:constcx citation.
- M-6/M-8: prop:vanish Step 3's final kill is unsound
  (image-annihilation does not give element-annihilation); replace the
  whole K-induction by the degree-inductive residuum (Steps B1-B5).
- M-7: AC-4 closure for the arbitrary-P outer question.

## Queued Side Issues (out of scope)

- q-accounting (lem:filter becomes uncited — leave in place, queue
  cosmetic deletion if page budget tightens).
- q-dead-sector: close as WONTFIX/superseded once M-8 lands.
- q-restriction-lemma / sieve(ii): consumed/retired by B4 (delete
  lem:restrict and sieve(ii); rename lem:sieve to "Sieve: fold
  terraces").
- Q-3 (rest) + final typography pass; q-scope-lifting explicitly out.

## Round Success Criteria

1. Step A: lem:sieve(i)'s proof uses the written-out contraction
   (w_r)_sigma := z_{(f_r,sigma)} with the two-term identity
   displayed; no lem:constcx citation in that proof.
2. Steps B1-B5: prop:vanish restructured as an explicit induction on
   the degree q; B1 dead-hygiene kept (cite the contraction/lem:dead);
   B2 keep sieve(i) through "replace z by this representative",
   deleting the now-moot 0=0 tail; B3 residuum = transport of the
   single z_{iB} value (value-level equalities only, no
   higher-vanishing invoked) then contraction-h coboundary with
   dead-sector discrepancy absorbed into w; B4 deletions (sieve(ii),
   lem:restrict, (dagger), old Steps 3-4) done; B5 degree-0 stays
   thm:descent+prop:adj with the no-circularity sentence and the q=1
   base stated.
3. Step C: Closing Remark (<=12 lines) after thm:main-end records the
   f.g. theorem + the two obstructions for arbitrary P + verdict open.
4. Step D: recompile twice 0 errors / 0 undefined refs / <=16 pages;
   greps clean (no dangling lem:restrict/sieve(ii), no orphan
   "i(P/K))", rem:transfer cited at every pullback); tracker updated
   (T2-R3 completed iff A-C all landed; B-8 resolved; M-5/M-6/M-7
   resolved); commit referencing this review; round-4-summary.
