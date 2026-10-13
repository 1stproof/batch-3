# Round 2 Contract

## Mainline Objective

Eliminate the round-1 repair residue flagged in the review (Findings
R1-F1 (a)-(d) and R1-F2): make every internal statement of
`solution.tex` consistent with the corrected round-1 mathematics, in
particular (a) align the component-count bound to `2 ≤ # ≤ 4`
everywhere, (b) replace the impossible generating set `H = <...>` with
an honest subgroup `H_0 ≤ H` and realign the index chain, (c) give
`def:descend` a non-circular definition, (d) fix the dangling/broken
fragments and the four value-table sign errors and hoist the `u_3`
definition, and delete the unproved conjugation clause in
`cor:Hstruct`(iii)/(iv) replacing it by the uniform parity argument on
all ten puncture loops.

## Target ACs

- AC-1 (internal logical consistency of the manuscript; every display
  a true statement)
- AC-3 (audit: no stale contradictions, no impossible generating set,
  no unproved clauses)

## Capability Anchor

N/A (the plan contains no `## Feature Map / Capability Map` section).

## Blocking side issues in scope

- R1-F1(a): stale "between 2 and 8" in cor:answer (must read 2..4).
- R1-F1(b): impossible `H = <7 gens>` equality; replace by
  `H_0 := <u_0,u_2,x_1,x_0^2,x_2^2,x_3^2> ≤ H` and use
  `[PMCG(B):H] ≤ [K:H_0∩K] ≤ 4`.
- R1-F1(c): `def:descend` circular; rewrite non-circular with the
  peripheral ambiguity remarked invisible on A.
- R1-F1(d): fragments and four s_i value signs; hoist `u_3` notation.
- R1-F2: cor:Hstruct (iii) conjugation clause replaced by parity on
  the ten puncture loops; H∩K ⊆ F proved.

## Queued side issues out of scope

- The exact component count `#π0(D_f) ∈ {2,4}` (unused).
- The `{p_1,v}` descended class (unstated, unused).

## Round success criteria

1. `solution.tex` contains no display `H = <...>` equality; uses
   `H_0 ≤ H` consistently; the index display reads
   `[PMCG(B):H] ≤ [K:H_0∩K] ≤ 4` with `2 ≤ [PMCG(B):H]` from `x_2 ∉ H`.
2. No "between 2 and 8" remnant; no "fix the v-strand" conj. clause;
   `def:descend` non-circular; no fragments; the four s_i values are
   `s_0(1/2)=-1/4`, `s_2(1/2)=+1/4`, `s_2(1)=-1`, `s_2(-1)=+1`; `u_3`
   defined in sec:setup.
3. `pdflatex` twice: 0 errors, 0 undefined references, ≤16 pages.
4. Changes committed; round-2 summary written; goal tracker updated.
