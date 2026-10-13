# Round 0 Contract

## IMMUTABLE SECTION (set in Round 0 only)

### One mainline objective
Produce a complete, rigorous, self-contained `solution.tex` determining the
minimax $L^2$ rate (up to logarithmic factors) for estimating the conductivity
$f\in\mathcal F(\alpha,r)$, $\alpha>1$, from white-noise observations of the
Darcy solution $u_f$ on the unit ball, proving both a matching (up to logs)
lower bound (Fano) and upper bound (sieve least squares / smoothed scale
inversion).

### Target ACs
- AC-1 (every claimed bound proved; specialist-verifiable)
- AC-5 (standalone compilable LaTeX, standard packages, $\le 16$ typeset pages)

(AC-2, AC-3, AC-4 are also addressed but the round is anchored on AC-1/AC-5.)

### Capability Anchor
N/A (the plan has no `Feature Map / Capability Map` section)

### Blocking side issues in scope
- Whether $u_f\in H^1_0(D)$ from the PDE: resolved by using the integral
  (variational) formulation only; no $H^1$ membership is asserted.
- Sharp Crank--Nicolson-type estimate in Holder--Zygmund spaces for the ball:
  resolved by the dyadic-to-general extension of the scale inequality
  (valid with an extra constant, circumventing semigroup domain questions).
- Observation white noise on a bounded domain: handled by projecting onto the
  finite-dimensional sieve approximation space (finite-rank Gaussian noise).

### Queued side issues out of scope
- Determining exact logarithmic powers (only "up to logarithmic factors" is
  asked).
- Boundary-layer refinements of the degree-1 smoothing estimate.

### Round success criteria
1. `solution.tex` states the rate
   $n^{-2\alpha/(2\alpha+d+2)}$ up to logarithmic factors and proves both the
   lower and the upper bound with all constants' dependencies tracked.
2. The document compiles with `pdflatex` to at most 16 pages.
3. Every internal audit item (quantifiers, constants, small-$r$ usage,
   $\alpha>1$ usage, log losses) is resolved or explicitly removed.
