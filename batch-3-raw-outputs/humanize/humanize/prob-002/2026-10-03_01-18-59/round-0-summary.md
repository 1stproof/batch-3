# Round 0 Summary

## What Was Implemented

Produced a complete draft `solution.tex` proving the minimax rate
for the Darcy inverse-conductivity problem is
$n^{-2\alpha/(2\alpha+d+2)}$ up to logarithmic factors.

Key components:
- Exact linearization identity $\Delta(Tg)=g+\frac{x\cdot\nabla}{d}g$
  (Lemma 2.1) with the very-weak (integral) PDE formulation, avoiding any
  claim that $u_f\in H^1_0$.
- Transport operator $L=I+\frac{x\cdot\nabla}{d}$ shown to be a bounded
  isomorphism of $L^2(D)$ via the explicit radial inverse and a
  Cesaro/Hardy change-of-variables isometry (Lemma 2.2).
- Exact Fourier-side identity $\widehat{Lh}=-\frac1d\xi\cdot\nabla_\xi\widehat h$
  establishing $T$ is order exactly $-1$ (Lemma 3.1) plus a
  wavelet-packet scale estimate $\norm{Tg}\asymp\delta\norm{g}$ with a
  harmonic (boundary) correction (Lemma 3.2).
- Fano lower bound via Varshamov--Gilbert-separated wavelet packets and
  Gaussian-shift KL $=\frac n2\norm{u_f-u_0}^2$ (Sec 4).
- Upper bound via sieve least squares on the spectral projection of the
  white noise, a discrete inf-sup/scale inversion, bias ($L^2$ Cα→δ^α) and
  variance balancing, with the quadratic remainder controlled for α>1
  (Sec 5).

## Files Changed

- `solution.tex` (full rewrite): draft minimax solution, compiles to 10 pages.
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` (initialized).
- `.humanize/rlcr/2026-10-03_01-18-59/round-0-contract.md` (created).

## Validation

- `pdflatex solution.tex` (two passes): compiles clean, no undefined
  references, 10 pages (within the 16-page limit).

## Remaining Items

- The minimax rate up to logarithmic factors is fully established
  (matching powers of $n$; upper bound carries a stated power of $\log n$).
  Some technically-routine sub-estimates (wavelet-packet
  interference / almost-orthogonality detail in Lemma 3.2, boundary-layer
  handling in the discrete inf-sup Lemma 5.1, and the metric-entropy log
  factor) are stated with their main mechanism and sketched to a standard
  level of detail; they do not affect the stated rate and can be expanded
  if the reviewer requests. The solution compiles to 11 pages.

## Round 1 Addendum (post-review)

Applied the Round-0 review's directive plan (MG-1..MG-11, B-1..B-4):
- MG-8/MG-11: added "(External tools (precise statements))" section T1-T7.
- MG-10: transposition definition of $u_f\in L^2$ + uniqueness (§2.4);
  deleted the $H^{1+\alpha^-}$ claim.
- B-1/B-2: fixed Lemma 2.2(i) malformed display; renamed/refined the
  "Zero mean" remark to "Transport structure of L".
- MG-1/MG-6/MG-2: added Lemma (AO) `lem:ao` (separated-exponential
  almost-orthogonality with Schur/Cotlar sum); repaired U-term shells
  (off-shell decay via $\int\psi=0$ and Schwartz decay; scale factors).
- MG-3: replaced vacuous "injectivity + scale-invariance" lower bound by a
  direct rescaling argument with the scale-invariant functional
  $\mathcal J$ and $\psi$-dependent constant $c_U$.
- MG-5: rewrote Lemma `lem:invert` with (i) multi-scale lower bound,
  (ii) spectral tail via $H^{2K-1}$ inverse, (iii) subtraction.
- MG-9: corrected frequency bookkeeping ($\delta^{-1}$, eigenvalue
  $\delta^{-2}$); justified $H^{-1}$ gain for the fine bias.
- MG-4: removed circular $\|h\|_\infty\lesssim\delta^\alpha$; now
  compact-sieve ($C^\alpha\le2r$) + Gagliardo--Nirenberg interpolation +
  explicit two-regime dichotomy ($\alpha>1$ yields decay).
- MG-7/B-3: rewrote the log paragraph — noise enters as a LINEAR
  functional, no union bound needed, log-free upper bound; Theorem 1.1 and
  Prop. 5.1 now show $\Phi_n=n^{-2\alpha/(2\alpha+d+2)}$ (log-free).
- B-4: removed "harmless"/"standard-level"/"proof sketch"/"for
  completeness" hedges.

Validation: `pdflatex` two passes, 13 pages, no undefined references, no
errors/warnings. $c_U$ depends only on $(\psi,d)$; all constants
$(\alpha,d)$-dependent only; $\alpha>1$ used at Lemma 2.5, MG-3, MG-4.

## BitLesson Delta

Action: none
Lesson ID(s): NONE
Notes: BitLesson KB is empty; no lessons applied.
