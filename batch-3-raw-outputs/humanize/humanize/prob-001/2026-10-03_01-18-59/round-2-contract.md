# Round 2 Contract

## Mainline Objective

Make `prop:vanish` and its supporting lemmas (`lem:sieve`, `lem:sandwich`,
the complex foundations) line-by-line verifiable by implementing the
generic nerve-complex support machinery ONCE (the SPINE of the Round-1
review) and re-deriving every later sentence as a named reference to it.
Execute the review's Steps 0-3 in order; Step 4 (optional reorder) only
after Steps 0-3 land.

## Target ACs

- AC-1 (every claim proved; Section 4 auditable line by line)
- AC-3 (`prop:vanish` references definite lemmas, never a floating
  parenthesis; audit of quantifiers and support bookkeeping)

## Capability Anchor

N/A (plan.md has no Feature Map / Capability Map).

## Blocking Side Issues in Scope

- B-7 (foundations; SPINE Step 0): insert a "The nerve complex"
  subsection before `def:square` containing (0a) nerve/alternating =
  normalized quotient; (0b) DEPTH = face-poset depth of Phi_U + sieve
  S(K); (0c) constant-complex acyclicity lemma (relocate `lem:const`'s
  homotopy); (0d) exact-subquotient / signed-transport lemma with its
  six-line check; (0e) homotopy-transfer along refinements; (0f) delete
  `lem:anchor` (or derive as terminal case of (0c)) and fix the wrong
  "terminal" parenthetical at `lem:dead`.
- B-8 (generic filter lemma; SPINE Step 1): formal statement and proof
  (finite level poset, order-respecting labels, top-level values zero =>
  cohomologous one level lower after label-preserving refinement);
  re-derive `lem:sieve`(i),(ii) as two corollaries each; DELETE the
  terrace induction.
- B-9 (sandwich isolation; SPINE Step 2): inline (2a) the sifted-cover
  family S = {U otimes D} refining the singleton {D} in `prop:vanish`
  Step 1, and (2b) the explicit restriction/pullback along i(b) ->
  i(P/K) in Step 3 (state+prove the q-restriction lemma there); repair
  `lem:sandwich` only if still needed elsewhere (precise index set,
  GF-min computation, survival clause).

## Queued Side Issues (implement only inside Steps 0-3, never replacing them)

- q-d-lemma: standalone proven lemma (chi((K/J)gp) = dZ, d>=1 for tight
  chi), cited in `lem:nerve` Case B and the Step-3 computations.
- q-restriction-lemma: pullback of standard rigid covers to the slice
  over i(P/K); strata via (C2).
- q-accounting: replace floating "(dead or stricter-level overlap)"
  clauses by named references after the generic lemma exists.
- q0-delta-terminal: D is the INITIAL object of the B-slice (B(D)=b_P);
  fix wording.
- q0-lem-anchor: delete (absorbed into (0c)).
- q-b2-microtypo: rename the embedding Lambda -> R from phi to mu in
  `lem:N` Step 2.
- Q-3 typography pass: "J-prime-rigid" slip in `def:square` (no J'
  defined -> write "rigid"); "leaves the kernel" phrasing.

## Round Success Criteria

1. The "nerve complex" subsection exists with (0a)-(0f) as stated, and
   every later use of filtration/sieve/exactness/transfer references it.
2. The generic filter lemma is stated and proved once; `lem:sieve`(i),(ii)
   are each re-derived by exactly two references; the terrace induction is
   gone.
3. `prop:vanish` Steps 1-3 are rewritten as reference-based deductions:
   Step 1 <= 2 sentences citing (0c)+(0e)+filter lemma concluding
   z_P-terminal = 0; Step 2 keeps the displayed two-fold subtraction
   (verified correct) and cites the promoted q-d-lemma; Step 3 = induction
   hypothesis D(K) + q-restriction-lemma + filter lemma, with "after one
   more pullback" citing (0e) and "outward maps zero" referencing Step 2;
   Step 4 + consistency note preserved.
4. Closeout items: q-b2-microtypo, Q-3 typography, q0-delta-terminal all
   applied.
5. pdflatex twice: 0 errors, 0 undefined references, at most 16 typeset
   pages (currently 14; Steps 0-2 add roughly 1.5 pages).
6. Goal tracker updated (B-7/B-8/B-9 -> resolved; queue items closed), a
   commit whose message references this review, and round-2-summary.md.
