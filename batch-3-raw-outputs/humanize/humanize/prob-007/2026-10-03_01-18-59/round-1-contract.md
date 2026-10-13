# Round 1 Contract

## Mainline Objective

Repair the two blocking proof gaps identified in the Round-0 review
(Finding 1: the false Schreier/free-factor computation in Corollary
`cor:Hstruct`; Finding 2: the under-derived puncture census in Theorem
`thm:monodromy-full`), while keeping the manuscript's conclusions
correct — in particular re-deriving the actual monodromy at the
$v=p_0$ double zeros honestly (the local smoothing computation shows
the monodromy of the simple $\lambda$-loop is $x_0^{\circ2}$, not
$x_0$, so the two-component theorem must be replaced by the honest
statement $[\PMCG(B):H]\mid 8$ with $2\le[\PMCG(B):H]\le 8$, and all
downstream statements adjusted) — and deliver a `solution.tex` in
which every claim used on the load-bearing path is proved.

## Target ACs

- AC-1 (every claimed lemma/proposition fully proved; no sketches on
  the main path)
- AC-3 (audit: no confidence language, no false group-theoretic
  identity, correct monodromy census)

## Capability Anchor

N/A (the plan contains no `## Feature Map / Capability Map` section).

## Blocking side issues in scope

- BI-1 (Finding 1): `H∩K = ch^{-1}(2Z)` is unproved as written; the
  Schreier basis of `ch^{-1}(2Z)` has 5 generators, not 3, and the
  "either form" sentence is internally contradictory. Repair or weaken.
- BI-2 (Finding 2): Theorem `thm:monodromy-full`(i),(vii) assert
  monodromies without derivation; also the derivative parenthetical in
  items (ii)-(iv) is mis-stated. Replace with honest local computations.
  NOTE: own re-derivation shows the true monodromy at the double zero
  of `R` is `x_0^2` (the review's guess of `x_0` is incorrect; the
  honest local model gives the twist squared). Work with the true
  statement and adjust the index/component conclusions accordingly:
  `2 <= [PMCG(B):H] <= 8`, `T_gamma^2` fixes every component (still
  the AC-4 no-infinite-orbit conclusion), the exact count
  `# pi_0(D_f)` is stated as an open sharpening, not asserted.

## Queued side issues out of scope

- QI-1 (Finding 3): unused element `x_0'` — delete or repurpose
  (cleanup only). Will delete since unused.
- Numeric/illustrative remarks not on the load path.

## Round success criteria

1. Corollary `cor:Hstruct` and equation (6.1) contain only proved
   statements: either the full normal-closure argument for
   `H∩K = ch^{-1}(2Z)`, or the honest weakening
   `<x_0^2,x_1,x_2^2,x_3^2>^H <= H∩K` together with the exact usable
   memberships (`x_2^2 ∈ H`, `x_2 ∉ H`) and the index bounds.
2. Theorem `thm:monodromy-full` items (i) and (vii) are proved by
   explicit local computations in the smoothing/u^2 and w=1/lambda
   charts; the wrong derivative parenthetical is fixed; no undetermined
   exponents remain; unused named objects are removed.
3. All downstream statements (component count, twist action on
   `π_0`, Corollary `cor:answer`) are consistent with the proved
   monodromy set and the index bounds; the AC-4 no-infinite-orbit
   conclusion is retained and proved.
4. `pdflatex` runs cleanly twice: 0 errors, 0 undefined references,
   ≤ 16 pages.
5. Changes committed; goal tracker and round-1 summary updated.
