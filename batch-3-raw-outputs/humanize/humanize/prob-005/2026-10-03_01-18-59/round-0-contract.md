# Round 0 Contract

## IMMUTABLE SECTION (modifiable only in Round 0)

### Mainline Objective

Decide the truth value of the statement in problem.tex and produce a complete,
rigorous proof in solution.tex: namely, prove that for every hyperfield H and
all x, y, z with 0 ∈ x ⊞ y ⊞ z, one also has
0 ∈ x³ ⊞ y³ ⊞ z³ ⊞ -xyz ⊞ -xyz ⊞ -xyz.

### Target ACs

- AC-1 (complete proved answer), AC-4 (honest verdict; expected positive
  resolution with full proof)

### Capability Anchor

N/A (plan has no Feature Map / Capability Map section)

### Blocking side issues in scope

None currently.

### Queued side issues out of scope

- bitlesson-selector binary absent (informational only).

### Round success criteria

- Truth value decided with proof strategy covering: degenerate cases
  (xyz = 0), the collapse case (x ⊞ y = {-z} for some pair), and the free
  case (no pair-sum collapses).
- solution.tex compiles standalone with pdflatex, ≤ 16 pages, standard
  packages only, begins with \documentclass and ends with \end{document}.
- Goal tracker initialized and updated; round committed; round-0 summary
  written.
