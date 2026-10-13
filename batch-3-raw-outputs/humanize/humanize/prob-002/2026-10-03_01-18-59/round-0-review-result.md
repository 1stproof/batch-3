# Review — audit #3 (current round): Independent Verification of the Round-2 Task Set

Reviewer: Codex (`moonshotai/Kimi-k3`, max effort). Scope: `plan.md`,
`problem.tex`, the full current `solution.tex` (HEAD `13876cd`, 1184
lines), goal tracker, round-1 contract, Claude's Round-0/Round-1 summary,
and the previous audit ("audit #2", G1–G7 / B-5..B-8). This review
**independently re-derived the load-bearing steps** rather than adopting
audit #2's conclusions. Compile re-run by this reviewer: two `pdflatex`
passes, **13 pages, no undefined references** (only benign hyperref
PDF-string info warnings) — AC-5 currently met.

**Headline.** No commits have occurred since audit #2; every finding
G1–G7 and B-5..B-8 was re-verified by hand **and is present verbatim in
the current document**. The Round-2 task set in the goal tracker is
therefore exactly right and is confirmed as the directive plan, with two
refinements added by this review (new item **B-9**; an explicit threshold
computation for the false step inside G1(c); and a sharper statement of
the correct r-smallness mechanism for the G1 repair). The final answer
$n^{-2\alpha/(2\alpha+d+2)}$ remains *consistent* (the Fano lower bound
is sound; the origin-region degeneracy can only improve the gain), but the
document does **not** currently prove it. COMPLETE is not warranted.

---

## Part 1 — Independent verification of audit #2's findings (all CONFIRMED in current document)

### V1 (G1 CONFIRMED, with sharpened detail). §5(C) risk analysis is vacuous as written

Re-derivation. With $e=\Pi_\delta f_0-f_0$, $h=\widehat f-\Pi_\delta f_0$,
the document's chain writes, linearizing about $\one$,
$\|\rho_g\|_2\lesssim r(\|g-\one\|_2+r)\lesssim r(\|h\|_2+r)$ and arrives at
$$c\,\delta\|h\|_2\ \lesssim\ n^{-1/2}\|\xi_\delta\|_2+\delta^{\alpha}+r\bigl(\|h\|_2+r\bigr).$$
For **fixed** $r>0$ and $\delta\to0$ this display is compatible with
*any* $\|h\|_2$ (the $r\|h\|_2$ term strictly dominates $c\delta\|h\|_2$),
so the very next display, in which the $r(\|h\|_2+r)$ term has silently
disappeared, does not follow. The intervening "two regimes" paragraph
substitutes a *different* remainder estimate
$\|\rho_{g_1}-\rho_{g_2}\|_2\lesssim\|h\|_\infty\|h\|_2$ that is never
connected back to the display (which contains the non-vanishing
$r^2$-order pieces $\|f_0-\one\|_\infty\|f_0-\one\|_2$ — these do not
tend to $0$ as $h\to0$). Confirmed verbatim at lines 1056–1087.

**Sharpened detail (new).** The correct mechanism behind
"$r$ small" is *multiplicative*, not additive: linearizing about the
comparison point (or an $r$-close smooth surrogate $m$), one has
$T=T_{m}+(T-T_m)$ with the operator-difference satisfying
$\|(T-T_m)h\|_2\lesssim r\,\delta\|h\|_2$ on the sieve, restoring the
gain $\frac c2\delta\|h\|_2$ once $r\le r_0(\alpha,d)$; the quadratic
remainder about $m$ is then $O(\|h\|_\infty\|h\|_2)$ and absorbs via
$\alpha>1$ at the minimax scale. The document's additive
$r(\|h\|_2+r)$ can never serve this role. This is the form the G1 repair
must take (it was implicit in audit #2's repair sketch (i)–(ii); it is
now stated as a requirement).

**Threshold computation (new).** The dichotomy's absorption uses
$\|h\|_\infty\lesssim\|h\|_2^{\theta}(4r)^{1-\theta}$; the optimal
Gagliardo–Nirenberg exponent between $L^2$ and $C^\alpha$ in dimension
$d$ is $\theta=\frac{\alpha}{\alpha+d/2}$. At $\|h\|_2\asymp\delta_*^\alpha$
the ratio is $\delta_*^{\alpha\theta-1}$, which tends to $0$ **iff**
$\alpha\theta>1\iff\alpha^2>\alpha+d/2\iff\alpha>\frac{1+\sqrt{1+2d}}{2}$
(e.g. $\alpha>1.62$ for $d=2$; $\alpha>2$ for $d=3$). The document's
sentence "the required condition reduces to $\alpha>1$" is therefore
false for $1<\alpha\le\frac{1+\sqrt{1+2d}}{2}$ — which includes all of
$(1,2]$ in dimension $d=3$ and more in higher $d$. (Audit #2 quoted the
weaker necessary threshold $\alpha>d/2$; the exact threshold from the
document's own interpolation is the one above. Both refute the printed
claim.) The repair must use the per-scale (Nikolskii-with-class-cap)
summation, which at the minimax scale needs only $\alpha>1$.

### V2 (G2/G3 CONFIRMED, by an exact computation). The two-sided scale/inversion claims fail at the origin

Take a radial bump $g(x)=\varphi(|x|/\delta)$ supported in $B_\delta$
about the origin, $\|g\|_2=1$. Solving $\Delta w=Lg=\frac1d\diver(xg)$
radially with $w=0$ on $\partial D$: $r^{d-1}w'(r)=\frac1d r^d g(r)$
(regularity at $0$ kills the constant), and $g\equiv0$ on $[\delta,1]$
forces $w'\equiv0$ then $w\equiv0$ there (from $w(1)=0$ and continuity
of the flux, since $g(\delta)=0$). Hence
$$w(x)=-\frac1d\int_{|x|}^{\delta}s\,g(s)\,ds\ \ \ (|x|\le\delta),\qquad w\equiv0\ \ (|x|\ge\delta),$$
in agreement with the formula $\frac1d J$-transport along radial rays, and
$$\|w\|_2^2=\int_0^\delta\Bigl|\frac1d\int_r^\delta s\,g(s)\,ds\Bigr|^2 r^{d-1}dr\,|\mathbb S^{d-1}|
\ \asymp\ \delta^4\|g\|_2^2$$
(by Cauchy–Schwarz in the inner integral;
upper and lower are both $\asymp\delta^4$ for non-trivial profiles).
So $\|Tg\|_2\asymp\delta^2\|g\|_2$ — **one full extra order of smoothing
versus the claimed $\delta\|g\|_2$**. This single example simultaneously
falsifies:
- `lem:scale2`'s lower bound as stated (its centres satisfy only
  $|x_m|\le\tfrac12$, origin included), and
- `lem:invert` part (i)'s per-scale claim $\|Th_j\|_2\gtrsim2^{-j}\|h_j\|_2$
  for origin-near coarse pieces, hence the lower bound of
  `eq:infsup` for general sieve differences (a single origin-centred
  scale-$\delta$ bump $h$ gives $\|P_\delta Th\|_2\asymp\delta^2\|h\|_2
  \ll c\delta\|h\|_2$).

The cause is visible in the Fourier identity itself:
$\widehat{L\tilde h}=-\frac1d\xi\cdot\nabla_\xi\widehat{\tilde h}$
vanishes at $\xi=0$ for *any* $\tilde h$; equivalently $\diver(xg)$
has total integral controlled by the boundary flux $\int_{\partial D}g$.
For boundary-distance-$1$ packets the gain is exactly $\delta$; for
centre-distance $\rho$ the mode-wise gain interpolates
$\delta(\delta+\rho)$. Note the direction of the failure: the truth is
*stronger* smoothing, so the true minimax rate is unaffected (origin
modes are easier to estimate), but the **proof as written** uses the
false lower bound in the upper-bound risk analysis, and that use is
fatal (G1 needs inf-sup for *all* sieve differences, including
origin-near ones).

Also CONFIRMED: the spectral-tail part (ii) of `lem:invert` derives
$\|(I-P_\delta)Th\|_2\lesssim C_K\delta\|h\|_2$ (powers
$\delta^{2K}\cdot\delta^{-(2K-1)}=\delta$) and then says "choose $K$
large enough that $C_K\delta^{K-1}\le c/2$" — a condition involving a
$\delta^K$ that never appears in the derived bound; since $C_K$ grows
with $K$, no such choice yields $\le\frac c2\delta\|h\|_2$. The correct
mechanism is the audit's threshold $\eta\delta^{-2}$ with $\eta$ large.

### V3 (G4/G5/G6 CONFIRMED). AO proof's decay step is false; U-term chain off by one power; `eq:shell` mis-stated as a general identity

- **G4.** The ball-indicator transform is a jinc/Bessel profile,
  $\widehat{\one_{B_\rho}}(y)=(2\pi)^{d/2}\rho^{d/2}|y|^{-d/2}J_{d/2}(\rho|y|)
  \sim|y|^{-(d+1)/2}$ oscillatory — **not** $O((1+\rho|y|)^{-N})$ for all
  $N$ as the proof asserts. With the true decay, the displayed Schur sum
  $\sum_{k\ge1}k^{d-1}(1+4k)^{-(d+1)/2}\sim\sum_k k^{(d-3)/2}$ diverges
  for every $d\ge2$. The *statement* of `lem:ao`(i) is true and provable
  (smooth majorant $\varphi_0(\xi/\rho)\ge\one_{B_\rho}$,
  $\varphi_0\in C_c^\infty$, whose transform is Schwartz — the audit's fix),
  but the *proof given* is defective: AC-1 fails at this step.
  Also confirmed: `lem:ao`'s second bound is stated for fixed-$v$ weights
  $(x_m{\cdot}v)b_m$ but *applied* in `lem:scale2` to the
  $\xi$-dependent weight $(x_m\cdot\xi)$, a statement/usage mismatch.
  (The correct fixed-coordinate version —
  $|\sum_m a_m(x_m\cdot\xi)e^{ix_m\xi}|^2\le
  |\xi|^2\sum_j|\sum_m a_mx_{m,j}e^{ix_m\xi}|^2$ pointwise, then apply
  (i) with $b_m=a_mx_{m,j}$ — gives exactly the needed
  $\lesssim\rho^2\cdot\frac14\sum a_m^2\asymp\delta^{-2}\sum a_m^2$;
  one line of repair, currently absent.)
- **G5.** The U-term display (lines 602–606) carries the spurious factor
  $\cdot\delta^{-1}$: as typeset the middle expression has order
  $\delta^{d+1}\sum a_m^2$ while the right side claims
  $\delta^{d+2}\sum a_m^2$. The intermediate power-count parenthetical
  ($\delta^{2d}\delta^{-d}\delta^{4}\delta^{-2}=\delta^{d+2}$) omits the
  same $\delta^{-1}$; neither reading of the display is correct as
  written.
- **G6.** `eq:shell` is stated for **every** $h\in C^\alpha$ as a
  two-sided shell equivalence, then proved only "in the model case of a
  scale-$\delta$ wavelet packet". As a general identity it is false
  ($\xi\cdot\nabla_\xi$ radially differentiates across shells; profiles
  homogeneous of degree $0$ along rays give exact cancellation). The
  statement must be restricted to the packet usage.

### V4 (G7/B-5/B-6/B-7/B-8 CONFIRMED). Precise list with line anchors

- G7(i): line 943 "$\widehat f$ is computed by linear least squares over
  the sieve coefficients" — false (objective is nonlinear in $g$).
- G7(ii): Theorem 1.1 + §6 print the log-free $\Phi_n$; justified only
  *after* G1 is repaired (the linear-functional observation is correct
  but currently sits downstream of a vacuous inequality).
- B-5: lines 298–302 print "$=4d\|g\|^2$" and "$\|L^{-1}g\|_2\le
  2\sqrt d\|g\|_2$"; the preceding display ($d^2\cdot4$) gives
  $4d^2\|g\|^2$, i.e. $\|L^{-1}\|\le2d$. The $2\sqrt d$ also appears at
  line 219 and in the lemma header.
- B-6: line 156 $u_0=(1-|x|^2)/(2d)$, $\Delta u_0=-1$: this is the
  solution for source $-1$, contradicting `problem.tex`'s source $=1$.
  (Internally consistent throughout; the global sign swap
  $u_0=(|x|^2-1)/(2d)$, $\nabla u_0=x/d$ fixes it with all estimates
  unchanged.)
- B-7: `$L$ extends to a bounded isomorphism of $L^2(D)$'
  (lem:Linv(iii)) plus the same phrase in §1's mechanism sentence and in
  `rem:crux` — false for the unbounded operator $L$ (coefficients
  bounded but $\nabla$ not); the true statements are:
  $J=L^{-1}\in\mathcal B(L^2)$ ($\|J\|\le2d$), $\|Lg\|_2\ge(2d)^{-1}\|g\|_2$,
  $L\in\mathcal B(H^1,L^2)$, and $T\in\mathcal B(L^2,H^1_0)
  \cap\mathcal B(H^{-1},L^2)$.
- B-8: the garbled fragment "...annihilated by $P_\delta$ and does not
  worsen the bound) by $P_\delta$ and does not worsen the estimate)"
  (§5(C) fine-bias paragraph) is present as described.

### V5 (NEW finding — B-9). Two literal "=" displays in Prop. 4.1 Steps 1–2 that are false as equalities

1. Step 1: "$\|\psi_m\|_{C^\alpha}=\delta^{-\alpha}\|\psi\|_{C^\alpha}$".
   Dilation scales $\nabla^j\psi_m$ by $\delta^{-j}$; only the *top*
   Hölder/Zygmund seminorm scales as $\delta^{-\alpha}$. The full norm
   is $\sum_{j\le a}\delta^{-j}\|\nabla^j\psi\|_\infty+
   \delta^{-\alpha}[\psi]_{\dot C^\alpha}\asymp\delta^{-\alpha}$ for
   $\delta\le1$ — comparable, not equal.
2. Step 2: "$\|\Psi_S\|_{C^\alpha}=\max_m\|\psi_m\|_{C^\alpha}$" with an
   "(equality …)" parenthetical. For separated disjoint supports the
   cross-support difference quotients do not vanish:
   $|\nabla^a\psi_m(x)-\nabla^a\psi_{m'}(y)|/|x-y|^t
   \le 2^{\,1-t}\delta^{-\alpha}\|\nabla^a\psi\|_\infty$, same order as
   single-bump quotients; hence $\|\Psi_S\|_{C^\alpha}\asymp\max_m
   \|\psi_m\|_{C^\alpha}$ with a constant $\le 2^{1-t}+1$, not equality.

Both are harmless to the rate ($\kappa$ absorbs the factor) but are
false displays a specialist will flag; fix alongside B-5..B-8 (replace
"=" by "$\le C$"/"$\asymp$" with one-line justification).

### V6 (re-verified sound — do NOT touch). Lower bound pipeline

Prop. 4.1 Steps 1–5, `lem:fano`, and the remainder-ratio argument
(`rem:alpha>1`): the only operator input used downstream is the *upper*
scale bound $\|Tg_S\|_2\lesssim\delta\|g_S\|_2$ (KL smallness) plus
Lemma 2.5 ($\|R(g_S)\|_2\lesssim\kappa^2\delta^{2\alpha}\ll
\kappa\delta^{\alpha+1}$, the true use of $\alpha>1$). The upper scale
bound survives all origin issues (extra smoothing only helps) modulo the
AO repair of V3/G4. The balance
$\delta=cn^{-1/(2\alpha+d+2)}$, $n\delta^{2\alpha+2}=c^{2\alpha+2}
\delta^{-d}$, Fano constants — all verified. **The minimax lower bound
at $n^{-2\alpha/(2\alpha+d+2)}$ stands in the current document.**
The two "$\asymp$" displays in Step 4 that quote the (defective) lower
side are used only in one direction downstream; when G3 lands their
quantifiers should be restricted to annulus centres (cosmetic at that
point).

Consistency check (this reviewer, agreeing with audit #2): the true
mode-wise gain $\delta(\delta+\rho)$ makes origin-near modes strictly
*easier*, and the annulus bulk ($M\asymp\delta^{-d}$ centres with
$|x_m|\ge c_0$, gain $\asymp\delta$) reproduces exactly
$n^{-2\alpha/(2\alpha+d+2)}$ on both sides. **The printed answer is not
in doubt; the proof obligations are.**

---

## Part 2 — Directive Round-2 implementation plan (singular; in commit order)

This is audit #2's plan, confirmed, with the V1/V3/V5 refinements. All
items are current-scope AC-1/AC-2/AC-3 obligations; none may be deferred.

1. **[mainline | B-5, B-6, B-7, B-8, B-9]** Text/constant sweep:
   (a) global sign convention to source $+1$: $u_0=(|x|^2-1)/(2d)$,
   $\nabla u_0=x/d$, replace $-\diver(\phi\nabla u_0)$ signs
   consistently (displays in Lemmas 2.1, 2.4, 2.5 and the barrier in
   `lem:apriori`);
   (b) Cesàro constant: $4d^2$ in the display, $\|L^{-1}\|\le2d$ at all
   five sites (lemma header, line 219, lines 298–302, §1, conclusion);
   (c) restate $L$-invertibility precisely (B-7 wording; delete
   "bounded isomorphism of $L^2$" everywhere);
   (d) delete the duplicated $P_\delta$ fragment;
   (e) B-9: replace both "$=$" by $\asymp$/≤ with one-line reasons.
2. **[mainline | G4, G5, G6]** Rewrite `lem:ao` proof with the smooth
   majorant $\varphi_0(\xi/\rho)\ge\one_{B_\rho}$ (Schwartz transform,
   legitimate rapid decay; $\rho^d\asymp|B_\rho|$ bookkeeping unchanged);
   delete part (ii); add the fixed-coordinate weighted corollary
   $\frac1{|B_\rho|}\int_{B_\rho}|\sum_m a_m(x_m\cdot\xi)e^{ix_m\xi}|^2d\xi
   \le|\xi|^2\sum_j\mathcal M_\rho(ax_{\cdot,j})\le\frac{\rho^2}{4}
   \sum a_m^2$; rewrite the U-term display as the two-line computation
   ($\mathbf a$-terms integrated first, multiplier $\delta^{2d+4}$,
   total $\le C\delta^2\|g\|_2^2/\|\psi\|_2^2$, clean powers); restrict
   `lem:fourier`'s conclusion to the exact identity + packet expansion
   (delete the general `eq:shell`).
3. **[mainline | G3]** Restrict all packet constructions (statement of
   `lem:scale2`, Prop 4.1 Step 1) to centres $\{c_0\le|x_m|\le\tfrac12\}$
   ($c_0=c_0(d)$ fixed small; $M\asymp\delta^{-d}$ persists). Take
   $\psi=\phi-\beta\phi(\cdot/2)$ with $\widehat\phi=\rho(|\cdot|)$
   supported on $\{1\le|\eta|\le2\}$, $\rho>0$ inside (jinc-type; $0$th
   and 1st moments vanish). Prove the lower bound by shell diagonal
   dominance: drop all shells $\ne$ the loaded shell (non-negative
   terms); on it, the per-mode phase-gradient factor satisfies
   $|x_m\cdot\xi|\asymp|\xi||x_m|\ge c_0\delta^{-1}/2$ in the diagonal,
   with off-diagonals Schur-summable via step-2 AO — final display
   $\|Ug\|_2^2\ge c_U\delta^4\cdot\delta^{-d}\cdot\delta^{-2}
   \cdot\delta^{2d}\sum a_m^2=c_U\delta^2\|g\|_2^2$, explicit powers,
   no $\mathcal J$-rhetoric (delete that paragraph). Harmonic
   correction: vanishing second moment upgrades the trace bound to
   $\|q\|_2\le C_q\delta^2\|g\|_2$ (sources at distance $\ge1/8$ from
   $\partial D$; second-moment vanishing gives one extra $\delta$), so
   $c_1=c_U$ without constant comparison.
4. **[mainline | G2]** Replace `lem:invert` by mode-wise inversion: for
   $h=\sum_\lambda h_\lambda$ (centres $x_\lambda$, scales
   $\delta_\lambda\ge\delta$),
   $\|Th\|_2^2\gtrsim\sum_\lambda\Gamma_\lambda^2\|h_\lambda\|_2^2$,
   $\Gamma_\lambda=\delta_\lambda(\delta_\lambda+|x_\lambda|)$: bulk
   modes by step 3 (per scale), origin modes by the exact $J$-map
   computation (V2; give it as a displayed sub-lemma), and the
   cross-mode/scale AO for $\{Th_\lambda\}$ (Schur on far centres;
   each $Th_\lambda$ is concentrated near $B(x_\lambda,C\delta_\lambda)$
   up to the harmonic tail on the boundary-adjacent part). Spectral
   tail: threshold $\eta\delta^{-2}$,
   $\|(-\Delta)^{-K}\|_{\text{tail}}\le\delta^{2K}\eta^{-K}$, then the
   $H^{2K-1}$ inverse inequality on the sieve — choose $K$ with
   $C_K\eta^{-K/2}\le c/2$, one explicit line. Conclude the two regimes:
   annulus-supported sieve differences: $\frac c2\delta\|h\|_2\le
   \|P_\delta Th\|_2\le C\delta\|h\|_2$; origin-near: stronger gain
   (used monotonically, never inverted in risk terms).
5. **[mainline | G1, G7]** Rebuild §5(C) around the comparison point:
   (i) delete the $r(\|h\|_2+r)$ display and the dichotomy paragraph;
   (ii) define $m=\Pi_\delta f_0$ (or an $r$-close smooth surrogate with
   $1-2r\le m\le1+2r$) and linearize there:
   $u_{\widehat f}-u_m=T_mh+\widetilde\rho$ with
   $\|\widetilde\rho\|_2\lesssim\|h\|_\infty\|h\|_2$ (same energy proof
   as Lemma 2.5 with $\nabla u_m$ in place of $\nabla u_0$);
   (iii) uniform inf-sup:
   $\|P_\delta T_mh\|_2\ge\|P_\delta Th\|_2-\|(T_m-T)h\|_2\ge
   \frac c2\delta\|h\|_2$, using $\|(T_m-T)h\|_2\le C r\delta\|h\|_2$
   on the sieve (the operator-difference bound; r-smallness enters
   **multiplicatively** — V1) for the annulus part, and the stronger
   origin gain for the rest;
   (iv) absorption: per-scale Nikolskii with class cap,
   $\|h_j\|_\infty\lesssim\min\{2^{jd/2}\|h_j\|_2,\,2^{-j\alpha}r\}$,
   summed over $\le C\log(1/\delta)$ scales and started from the
   bootstrap $\|h\|_2\le2r$ — at the target scale this is
   $\delta_*^{\alpha-1}\cdot$(class factor)$\to0$ using **only**
   $\alpha>1$ (state it quantitatively; no unspecified $\theta'$);
   (v) basic inequality in the clean form
   $\frac c2\delta\|h\|_2\le n^{-1/2}\|\xi_\delta\|_2+
   \delta_*^{1+\alpha}+o(\delta_*\|h\|_2)$, take expectations
   ($\E\|\xi_\delta\|_2^2=\dim V_{\delta_*}\asymp\delta_*^{-d}$; the
   noise enters as a linear functional — no union bound; log-free),
   balance at $\delta_*=n^{-1/(2\alpha+d+2)}$;
   (vi) fix the "linear least squares" sentence (estimator = measurable
   minimizer over the closed sieve; only risk properties used);
   (vii) keep Theorem 1.1 log-free only if (v) delivers it (it does,
   per the linear-functional argument); otherwise print the log on the
   upper side.
6. **[mainline | AC-3/AC-5]** Final audit pass: quantifier list
   ($\exists r_0(\alpha,d,\psi)$; constants independent of
   $n,\delta,f$); the complete $\alpha>1$ usage list (Step 4 of
   Prop 4.1; step 5(iv) above; nowhere else); page budget (13pp +
   ~2pp of repairs ≤ 16pp; the deleted $\mathcal J$-rescaling paragraph
   and dichotomy paragraph buy back ~1pp). Grep harness: no
   "sketch|harmless|standard|for completeness" hedges; every display
   power-counted.

---

## Part 3 — Claimed-vs-actual (Claude's Round-1 summary)

Reaffirmed from audit #2 and re-verified this round: of the Round-1
addendum items, T1–T7 + transposition (§2.4), the B-1/B-2 display fixes,
MG-9's bookkeeping, B-4 hedge removal, and compilation are **met**; the
AO lemma, scale2 lower bound, `lem:invert`, the §5(C) absorption
argument, and the log-free claim are **not met in substance** (V1–V4).
The claims "no errors/warnings", "13 pages", "constants
$(\alpha,d)$-dependent only" are accurate; the claim "applied the
directive plan (MG-1..MG-11)" is accurate only for the
statement/display-level items, not for the analytic load-bearing ones.

---

## Part 4 — Goal alignment summary

```
ACs: 1/5 met (AC-5: 13pp, compiles clean) | AC-2 near-met (T1–T7 precise;
transposition definition of u_f; B-5/B-6/B-7/B-9 imprecisions remain) |
AC-1/AC-3 open exactly at G1–G7 (+B-5..B-9 cosmetic-but-false displays) |
Forgotten items: 0 | Unjustified deferrals: 0 (none requested; the
"sketched to a standard level of detail" language from Round 0 was
already converted into mainline tasks in earlier audits)
```

Capability alignment:

```
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
```

(The plan has no Feature/Capability Map; round contracts correctly
use N/A.)

Tracker state: aligned with this review (Round-2 task set G1–G7,
B-5..B-8 active); this review added B-9 and the G1 threshold/mechanism
annotations to the tracker itself, plus Plan Evolution entry
"2 (review #3)".

## Part 5 — Mainline gap / side-issue classification

**Mainline gaps (block AC-1/AC-3; directive plan in Part 2):**
G1 (vacuous risk analysis; multiplicative-r repair; GN threshold
$\alpha>(1+\sqrt{1+2d})/2$ not "$\alpha>1$" as written), G2 (mode-wise
inversion; spectral tail threshold), G3 (annulus restriction + shell
diagonal dominance), G4 (smooth-majorant AO + weighted corollary),
G5 (U-term chain power fix), G6 (restrict `eq:shell` to packets),
G7 (estimator sentence; log-free only after G1).

**Blocking side issues (fix in the same sweep):** B-5 ($4d^2$/$2d$),
B-6 (source-sign convention), B-7 (unbounded-$L$ phrasing, all
sites), B-8 (duplicate fragment), B-9 (two "=" displays that are
only $\asymp$).

**Queued side issues (documented; not this round):** Q-1 (exact log
power), Q-2 (boundary-layer constants), Q-4 ($\alpha\le1$ conjectural
remark wording), Q-5 (optimize $\eta,c_0$ constants).

Mainline Progress Verdict: ADVANCED

(ADVANCED, not STALLED: the last commit round landed real
statement-level repairs (T1–T7, transposition, MG-9 bookkeeping, hedge
removal) and the surviving gaps are precisely identified with the
corrected mathematics in hand — the rate's lower bound is proved and
the upper bound's failure modes are local (origin degeneracy) and
structural (linearization point), each with an explicit sound repair.
COMPLETE is deliberately not output: G1–G7 remain open current-scope
AC-1/AC-3 work.)
