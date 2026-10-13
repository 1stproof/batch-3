# Round 0 Contract

## Mainline objective

Produce a complete, rigorous, self-contained proof in `solution.tex` of the
statement in `problem.tex`: for a very general H-polarised Tyurin degeneration
X/Delta of K3 surfaces, construct the mirror elliptic fibration pi: Y -> P^1
with an allowable loop gamma for the quasipolar lattice N = H \oplus E8 \oplus
E8, verifying every item of Giovenzana--Thompson Definition 5.1
(lattice/checkerboard criterion, monodromy filtrations, Hodge-theoretic
data, and the correspondence of theorem (1) <=> (3)).

## Target ACs

- AC-1, AC-2

## Capability Anchor

N/A (the plan contains no `## Feature Map / Capability Map` section)

## Blocking side issues in scope

None known.

## Queued side issues out of scope

None.

## Round success criteria

- `solution.tex` is a standalone compilable article-class LaTeX document
  (<= 16 typeset pages) containing a full proof: explicit period-map
  computation of W(Y), the loop/monodromy construction verified at the
  I_{18} + I_1 + I_1 cusp (including the E8 \oplus E8 generators of
  the vanishing cycle filtration), checkerboard condition checked over an
  explicit 18-element integral basis, all four clauses of Definition 5.1
  verified with proof, and all invoked external results (Hasse principle,
  Nikulin embedding theorem, stackiness/Spider Lemma of Alexeev--Brunyate--
  Engel) stated precisely with hypotheses.
- `pdflatex` compiles `solution.tex` without errors.
