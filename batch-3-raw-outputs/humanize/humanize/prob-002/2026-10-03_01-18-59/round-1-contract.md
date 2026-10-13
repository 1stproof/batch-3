# Round 1 Contract (post audit #3)

## One mainline objective
Close audit #3's mainline gaps G1–G7 and blocking issues B-5..B-9 so that
`solution.tex` rigorously proves both bounds of the minimax rate
$n^{-2\alpha/(2\alpha+d+2)}$ (up to logs). The rate itself is unchanged;
what is at stake is making the proofs correct (two-sided scale estimate,
inf-sup, and a non-vacuous risk analysis).

## Target ACs
- AC-1 (every claimed bound proved correctly; no false displays)
- AC-3 (constants/quantifiers audited; wrong powers/signs fixed)

## Capability Anchor
N/A (plan has no capability map)

## Blocking side issues in scope (fix in same sweep)
B-5 Cesàro constant $4d^2$/$2d$; B-6 source-sign convention; B-7
unbounded-$L$ phrasing; B-8 duplicate fragment; B-9 two "=" displays.

## Queued side issues out of scope
Q-1 exact log power; Q-2 boundary-layer constants; Q-4 alpha<=1 remark
wording; Q-5 constant optimization.

## Round success criteria
1. Mode-wise scale estimate $\|Th\|\asymp\delta(\delta+|x|)$ proved:
   annulus lower bound via shell diagonal dominance, origin exact radial
   sub-lemma, smooth-majorant AO, harmonic correction with second moment.
2. Exact radial origin computation displayed (gain $\delta^2$).
3. Risk analysis rebuilt: linearize about comparison point,
   multiplicative-r operator-difference bound, per-scale Nikolskii
   absorption valid for all $\alpha>1$, log-free basic inequality.
4. Sign/constant/fragment/display sweep (B-5..B-9) applied.
5. pdflatex two passes clean, $\le16$ pages, no undefined refs, no
   hedges.
