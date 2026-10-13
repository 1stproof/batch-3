# Round 1 Contract

## Mainline Objective

Resolve all six blocking review findings B-1..B-6 of the Round 0 review
in `solution.tex`, in the review's directive order (f.g. scope,
Lemma 2.4 Step 2 clause, finite presentation subsection, Cech nerve
definition plus named comparison theorem, Lemma 4.3(b) restatement,
iffalse block deletion), then recompile and commit.

## Target ACs

- AC-1 (every claim proved; no substantive case left unproved)
- AC-3 (audit: quantifiers, degeneracies, consistency with problem.tex)

## Capability Anchor

N/A (plan.md has no Feature Map / Capability Map).

## Blocking Side Issues in Scope

- B-1 f.g. scope breach at solution.tex line 43: resolve via Branch B
  (honest scoping: monoids as in the problem, with the running f.g.
  hypothesis isolated in one explicit paragraph) plus the STAR remark
  that all verifications only ever meet finitely presented data.
- B-2 Lemma 2.4 Step 2 false "same class" clause (delete + repair).
- B-3 finite presentation never treated (add subsection; verify all
  structure/refinement/test maps).
- B-4 Cech nerve never defined; cofinality cited by website tag number.
- B-5 Lemma 4.3(b) ambiguous/false as written (restate as C1/C2).
- B-6 iffalse block deletion (already done in the working file; verify)
  and residual AC-5 cleanup.

## Queued Side Issues out of Scope

- Q-1 global re-verification of nerve kernel claims over arbitrary
  parents (Round 2 audit, per the review).
- Q-2 grep for other "same class" usages (after B-2 repair; tiny).
- Q-3 typography pass (final round).

## Round Success Criteria

1. Each of B-1..B-6 has an explicit, checkable repair in solution.tex
   at the place the review indicated.
2. pdflatex twice: 0 errors, 0 undefined references, at most 16 pages.
3. No Markdown or workflow commentary inside solution.tex (including
   no \\iffalse blocks).
4. Goal tracker updated, commit with a message referencing the review,
   round-1-summary.md written by the worker.
