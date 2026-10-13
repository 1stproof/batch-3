# Round 2 Contract (post audit #4)

## One mainline objective
Close audit #4's mainline gaps F-1, F-2, F-3 so the upper-bound risk
analysis (Prop. 5.1) is a complete proof: the inf-sup step must (i) use
a spectral projector $P_\delta$ whose cutoff matches the one-degree
smoothing ($u$-side frequencies $\lesssim\delta^{-1}$), with an explicit
off-shell/small-tail bound; (ii) replace `lem:origin`'s invented
two-sided interpolation by the proved radial endpoint + the one-sided
comparison actually used; (iii) insert the missing
$\|h\|_\infty\lesssim\sum_j\|h_j\|_\infty$ step in the absorption chain.

## Target ACs
- AC-1 (inf-sup + origin: every claimed bound now proved; no invented
  interpolation; no norm/energy conflation)
- AC-3 (quantifier/constant audit: constants $(\alpha,d,\psi)$-only,
  threshold $\delta_0$ explicit)

## Capability Anchor
N/A (plan has no capability map)

## Blocking side issues in scope (fix in same sweep)
- F-4: global source-sign sweep to `problem.tex`'s
  $\operatorname{div}(f\nabla u)=1$
  ($u_0=(|x|^2-1)/(2d)$, $\nabla u_0=x/d$, barrier signs flipped,
  invariance parenthetical dropped).

## Queued side issues out of scope
F-5 expository compression; Q-1 (exact log power), Q-2 (boundary
constants), Q-4 ($\alpha\le1$ wording), Q-5 (constant optimization);
page-economy polish beyond what F-1–F-4 edits need.

## Round success criteria
1. `lem:invert` rewritten: $P_\delta=P_{\le\Lambda}$,
   $\Lambda\asymp\delta^{-1}$
   ($\dim V_\delta\asymp\delta^{-d}$ by Weyl), tail either
   $\|(I-P_\delta)Tg\|_2\lesssim\Lambda^{-1}\|h\|_{H^1}\lesssim
   (\Lambda^{-1}\delta^{-1})\|h\|_2$ or the off-shell Schwartz decay of
   `scale2`'s `eq:Uupper`-tail; triangle (not norm-squared) subtraction;
   lower bound
   $\|P_\delta Th^{\rm bulk}\|_2\ge(c_1/2)\delta\|h^{\rm bulk}\|_2$.
2. `lem:origin` reformulated: radial endpoint proved (as-is), general
   claim replaced by the one-sided bound used downstream
   ($\|Th_\lambda\|_2\gtrsim\delta_\lambda^2\|h_\lambda\|_2$
   origin-near; never inverted), `rem:modewise` / `eq:infsupapp`
   adjusted.
3. Absorption chain (before `eq:absorb`) contains the explicit
   $\|h\|_\infty\le\sum_{2^{-j}\ge\delta}\|h_j\|_\infty$ line citing
   `lem:quad`.
4. Source-sign sweep applied globally (`problem.tex` source $=1$),
   barriers re-checked.
5. Two `pdflatex` passes clean, $\le16$ pages, no undefined refs, no
   hedges; tracker/summary updated; commit.
