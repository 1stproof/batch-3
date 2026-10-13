# Round 0 Summary

## What Was Implemented

Decided and proved the answer to prob-004: **NO, not in general**.

Main result written in `solution.tex` (5 typeset pages, standalone, article class):

1. **Theorem (obstruction).** If $(M,\omega)$ is symplectic, $D$ a symplectic SNC
   divisor, and $J$ an almost complex structure that is SNC-adapted (every point has
   coordinates with $D=\{z_1\cdots z_r=0\}$ and $z_1,\ldots,z_r$ $J$-holomorphic),
   then for every compact connected component $D_\alpha$:
   - strata $D_A$ are $J$-invariant (Lemma: pointwise algebra from the CR equation);
   - the normal bundle $\nu_\alpha$ becomes a complex line bundle via $J$;
   - locally $J$-holomorphic defining functions yield local frames
     $e_i=\dd z_1^{(i)}|_{D_\alpha}$ of the complex conormal bundle $\nu_\alpha^*$;
     on overlaps the ratios $h_{ij}=z_1^{(j)}/z_1^{(i)}$ are $J$-holomorphic (ratio
     lemma: $h$ satisfies the CR identity on the dense open complement and the CR
     identity extends across $D$ by continuity), hence constant on the compact
     connected component (maximum principle via Nijenhuis–Woolf discs);
   - constant transition functions => $\nu_\alpha^*$ has a flat connection =>
     $c_1(\nu_\alpha^*)=0$ in $H^2(D_\alpha;\mathbb{R})$ =>
     $e(\nu_\alpha)=0$ => $D_\alpha\cdot D_\alpha=0$.
2. **Corollary (counterexample).** $(\CP^2,\omega_{FS}, L\cong\CP^1)$: a line is a
   symplectic SNC divisor (single smooth component) with $L\cdot L=1$, so no tame
   SNC-adapted $J$ exists. The obstruction $L\cdot L=1$ is topological in the pair
   $(M,L)$, hence unchanged by any cohomologous symplectic deformation keeping $L$
   symplectic SNC — the deformation clause of the question cannot help.
   Same conclusion for two lines (each component self-intersection +1).
3. Sharpness discussion (product cases with trivial normal bundle do admit adapted
   tame $J$, e.g. $J_X\oplus i$ on $X\times\mathbb{C}$).

Additional key insight recorded: taming of $J$ is not even used in the obstruction;
adaptedness alone already forces $D_\alpha\cdot D_\alpha=0$. This makes the answer
robust (no dependence on $\omega$'s deformation at all).

## Files Changed

- `solution.tex` — the full disproof (only deliverable; compiled to 5 pages).

## Validation

- `pdflatex solution.tex` run twice: compiles cleanly, no LaTeX errors, all
  cross-references resolved, 5 pages (limit 16).
- Line-by-line audit of the delicate steps:
  * strata preservation uses only the pointwise CR equation (no integrability);
  * the CR identity for `h` at divisor points is justified by continuity from the
    dense open set, not by division at the point;
  * quotient of $J$-holomorphic functions is $J$-holomorphic where denominator != 0;
  * maximum principle needs only local existence of $J$-holomorphic discs
    (Nijenhuis–Woolf) and the classical maximum modulus principle, both stated
    explicitly as the only external inputs;
  * flat connection from locally constant transition functions; Chern–Weil gives
    $c_1=0$ in real cohomology; Euler/Chern sign conventions stated;
  * $L\cdot L=1$ from $\nu_L=\mathcal{O}(1)$; deformation-invariance because the
    self-intersection is a property of the oriented smooth pair $(\CP^2,L)$;
  * question-consistency: $(\CP^2,\omega_{FS})$ closed; single component trivially
    SNC; two-line case transverse hence SNC in the Darboux-model sense used by
    the question.

## Remaining Items

- None blocking. Open side question recorded in tracker (sharpness when all
  self-intersections vanish) — out of scope for the asked question.

## BitLesson Delta

Action: add
Lesson ID(s): BL-20261003-ratio-cocycle-obstruction
Notes: Beforehand I iterated on a YES-construction and repeatedly hit overlap
incoherence; the decisive check is the local CR computation for the ratio of two
$J$-holomorphic defining functions, which flips the anticipated "antiholomorphic
ratio" intuition into genuine holomorphicity (continuity across the divisor), and
then the maximum principle forces a constant cocycle and a flat conormal bundle.
Lesson: when a YES-construction for adapted objects keeps resisting overlap
gluing, compute the transition ratio's $\bar\partial_J$ on the dense open set and
extend by density: if the transition data become rigid (constant), the problem is
usually NO with a characteristic-class obstruction; test against
$(\CP^2, \text{line})$ first. (bitlesson.md entry appended below in the round;
no selector tool installed in this environment.)
