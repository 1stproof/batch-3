# Round 2 Contract

## Mainline objective
Attempt to prove Input (Mem) via the reviewer's complex-affine hull
construction (R2-1), and repair the remaining correctness issues
MG-A2 (premise inclusion), MG-A3 (component-identification),
MG-A4 ((g,n) scope of Thm 2.4(2)), B-1, B-2, plus cosmetics Q-5/Q-6.
If R2-1 cannot be completed honestly, package as a Reduction Theorem.

## Target ACs
- AC-1 (complete proof of every implication, or honestly-documented reduction)
- AC-2 (external results used within their hypotheses; no misquotes)

## Capability Anchor
N/A

## Blocking side issues in scope
- MG-A1 (Membership proof attempt - decisive)
- MG-A2 (premise inclusion), MG-A3 (derivative identification),
  MG-A4 ((g,n) scope), B-1 (properness), B-2 (near-circle)

## Queued side issues out of scope
- Q-3, Q-4, Q-5, Q-6 (cosmetics - fix only in final pass R2-7)
- B-3 (prop:regeneration black box - leave labelled)

## Round success criteria
- Either: Input (Mem) proved from hypotheses (i)-(ii) + quoted tools, or
  a precise record of exactly where the complex-analytic persistence
  argument fails.
- MG-A2/A3/A4 repaired in document; B-1/B-2 repaired.
- pdflatex clean, <= 16 pages.
