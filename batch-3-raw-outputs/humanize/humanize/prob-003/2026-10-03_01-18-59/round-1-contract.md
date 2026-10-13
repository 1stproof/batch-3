# Round 1 Contract

## Mainline objective
Repair Part 1 of solution.tex so the isomorphism S_n(B*) ≅ D = U_q(b−) ⋈ U_q(b+)
is true and proved: fix the cross-relation convention (antipode S, not S^{−1}),
recompute all mixed relations channel-wise, prove well-definedness, then deduce
Part 2 (S_n(B*)/I ≅ U_q(sl(n))) rigorously.

## Target ACs
- AC-1 (both parts proved)
- AC-2 (no unstated external input; all constants derived)

## Capability Anchor
N/A (no capability map in plan).

## Blocking side issues (must fix)
- A1: Prop 3.3 cross-computation false/unproved (S vs S^{−1}, Δ²(E), S(F)).
- A2: Lemma 1.2 (grouplikes commute) false → cross-conjugation instead.
- A3: Definition 2.1/well-definedness gaps.
- A4: Thm 4.2 circularity / Lemma 4.2 contradiction.

## Queued (out of scope)
- Q1 scratch tidying; Q4 label hygiene (folded into edits).

## Success criteria
- solution.tex: consistent conventions, (SK-S) cross product verified by exact
  symbolic computation, Lemma 1.1/Prop cross-computation redone and machine-checked,
  Part 1 well-definedness+isomorphism proved, Part 2 deduced; compiles ≤16 pages.
