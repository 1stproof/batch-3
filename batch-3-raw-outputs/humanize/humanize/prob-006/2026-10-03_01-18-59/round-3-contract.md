# Round 3 Contract

## Mainline Objective

Fix the single P1 blocking accuracy finding from the Round-2 review: the
closing Remark (rem:glcabling) falsely attributes to Gordon--Luecke a proof
of the cabling conjecture and asserts Theorem 1.1's conclusion holds for
arbitrary knots. Replace it with a correct statement of Gordon--Luecke's
actual results, without touching the (final, reviewer-verified) proof chain
or Section 4 mechanism sketch.

## Target ACs

- AC-2 (precise, supported statements; no false theorem attribution)
- AC-4 (never present conjecture as fact)

## Capability Anchor

N/A (plan has no Feature Map / Capability Map).

## Blocking Issues In Scope

- P1: Remark rem:glcabling (lines ~494-503) claims Gordon--Luecke proved the
  cabling conjecture for knots in S^3 (open: Gonzalez-Acuna--Short) and that
  "the conclusion of Theorem 1.1 holds for arbitrary knots." Both are wrong as
  stated. Fix by restating Gordon--Luecke's actual theorem: a reducible
  surgery on a knot in S^3 has exactly two prime summands and (with the
  reducing-slope integrality, Theorem thm:gl) the slope is integral; the
  full cabling conjecture remains open; our result for L-space knots uses the
  stronger Ni--Wu conclusion (cabling at the cabling slope) to additionally
  identify the summands and prove primality.

## Queued Issues Out Of Scope

None; no new features, no restructuring. Section 4 sketch untouched.

## Round Success Criteria

1. Remark rem:glcabling no longer asserts that the cabling conjecture is
   proved, nor that the conclusion holds for arbitrary knots; it states
   Gordon--Luecke's true result accurately and notes the conjecture's open
   status and the role of Ni--Wu's stronger conclusion.
2. `pdflatex` compiles clean; PDF remains <= 16 pages; mathematics unchanged.
3. Commit + Round-3 summary; goal tracker updated.

## Immutability Note

Original plan's Ultimate Goal/ACs unchanged. Review-phase fix only.
