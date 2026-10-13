# Round 2 Contract

## Mainline Objective

Resolve the two P3 expository findings from the Round-1 code review of
`solution.tex` --- (P3-a) the muddled primality inference in Case 2
($0$-surgery) that leans on $b_1=1$ instead of excluding $S^1\times S^2$ via
the nonseparating-sphere argument, and (P3-b) the unsourced/unhedged
generalization claim in the closing remark (Remark 5.4) --- without altering
the (final, reviewer-verified) proof chain or adding content.

## Target ACs

- AC-3 (audit of logical direction / clean inference)
- AC-2 (all stated claims supported or hedged)

## Capability Anchor

N/A (plan has no Feature Map / Capability Map).

## Blocking Issues In Scope

- P3-a: Case 2 sentence "It is not $S^3$ (indeed $b_1=1$), hence it is prime"
  mis-attributes the exclusion of the non-prime possibility $S^1\times S^2$.
  Treat as blocking for safe acceptance of the round (the fix is a one-line
  rewrite the reviewer supplied verbatim).
- P3-b: Remark 5.4 closing claim "...the statement that generalizes to knots
  in arbitrary $L$-space homology spheres, where Theorem 1.2 is unavailable"
  is unsubstantiated in that generality. Fix by hedging/sourcing.

## Queued Issues Out Of Scope

None beyond the two findings; no new features, no restructuring.

## Round Success Criteria

1. Case 2 rewritten so the primality inference reads: $S^3_0(K)$ is not
   $S^1\times S^2$ (which contains a nonseparating essential sphere,
   contradicting irreducibility) and not $S^3$ (since $b_1=1$), hence prime.
2. Remark 5.4 closing sentence replaced by a hedged formulation (analogues of
   the cabling statement have been pursued for knots in $L$-space homology
   spheres), or removed, so no unsupported general claim remains.
3. `pdflatex` compiles clean; PDF remains <= 16 pages; mathematics unchanged.
4. Commit + Round-2 summary; goal tracker updated.

## Immutability Note

Original plan's Ultimate Goal/ACs unchanged. Review-phase fixes only.
