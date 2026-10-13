# Round 1 Review Result (Reviewer: Kimi-k3, max effort)

## Scope of review

Read in full: `plan.md`, `problem.tex`, the round-1 prompt, the round-1
contract, the goal tracker, the round-0 review result, and all 800 lines
of `solution.tex` at commit d0ad78a. Re-ran `pdflatex solution.tex` twice:
exit code 0, no LaTeX errors, no undefined references/citations, 11
typeset pages (AC-5 still satisfied: begins with
`\documentclass[11pt]{article}`, ends with `\end{document}`, only allowed
packages, no Markdown/commentary). Build artifacts present are
git-ignored; the commit history matches the claimed trajectory
(4bc6512, 84c0d90, d0ad78a).

## Part 2: Goal Alignment Summary

```
ACs: 5/5 addressed; AC-1/AC-2 still gated by the mainline gaps below | Forgotten items: 0 | Unjustified deferrals: 0
```

The immutable section is untouched and correct. The mutable section is
aligned: the Round-1 repair task is listed and honestly marked done, and
the stale "Round 1 repairs ... active" row has been superseded by the
"Round 1 executed ... done" row directly beneath it (mild duplication, but
not misleading, since Rows read together reflect Round 0 completed,
Round-1 repairs completed). Q-1 was queued for opportunistic fixing and
Claude folded it in; most of Q-1 is indeed fixed, but one sub-item
(`H^{perp-ish}`) was *recorded as fixed while never having existed in the
tex source* --- see Q-2. I have updated the tracker per Part 5 below.

## Part 3: Capability Alignment Summary

```
Capability anchor: N/A (plan has no Feature Map / Capability Map) | Dependency gaps: 0 | Scope drift: no
```

## Part 4: Round-1 contract cross-check (success criteria 1--7)

Verified item by item against the contract:

1. **Prop 4(a) generality sentence** --- FIXED (lines 471-483): now "for
   very general t in the punctured disc ... (this is the assumed
   very-generality hypothesis)". The old conflation and the
   "imprimitive-cusp-free" terminology are gone. PASS.
2. **Prop 4(c) minimal cell structure + subdivision** --- FIXED
   (lines 448-457, 492-505): $(V,E,F)=(1,1,2)$ with $\chi=2$ stated and
   recomputed in-line (both in the statement at line 453 and in the proof
   at line 498); the 4-fold subdivision into the pillowcase is stated in
   both places; Thm 4(b) (lines 599-606) gives the quadrangulated
   pillowcase $\chi=4-4+2=2$, the homeomorphism, and the subdivision
   relation; "matching Proposition 4(c)" is gone. PASS.
3. **Thm 4(d) explicit filtration model** --- PARTIALLY FIXED
   (lines 649-683): the rank-19 model $\cE=N\oplus\bZ f'$, the two
   embeddings, $\Phi$ = identity-on-$N$ plus $v\mapsto f$, and the four
   itemised checks are all present. However the checks (iii) and (iv) are
   still one level too gestural for AC-2 line-by-line verifiability (see
   M-8), and the display has two defects (see M-9). PARTIAL.
4. **Checkerboard as vertex bipartition** --- FIXED (lines 719-728):
   vertex bipartition of the equatorial 4-cycle, evenness of 4, and a
   light-leaf disposal (both leaf branches carry $II^*$-fibres only, same
   leaf type) are now stated; the wrong face-2-colouring is gone. The
   light-leaf phrase is a plausible paraphrase of [GT, 4.13]; acceptable.
   PASS.
5. **Prop 4(d) honest external quote** --- FIXED (lines 507-527): the
   isomorphisms $E_m(\X)/W_2(\X)\simeq N$ and
   $E_m'(\X)/E_m(\X)\simeq(-1)U$ are now quoted from [GT, Example~1.2]
   with hypotheses and the displayed Clemens--Schmid fragment, parallel
   to the Theorem C treatment, retaining $\rk E_m=18$, $\rk E_m'=20$.
   PASS (with a consistency caveat, item M-9).
6. **Lemma 3 statement + Lemma 1 section sentence** --- FIXED:
   Lemma 3 (lines 382-391) now contracts exactly $\sigma$ and the two
   $II^*$-components with Du Val $E_8+E_8$ image; the proof (393-421) is
   the advertised horizontal/vertical case split; Saint-Donat applied.
   The section argument in Lemma 1 (lines 284-295) is the clean
   Riemann--Roch + $E_8$-Weyl + $p_a=0$ argument. M-7 punctuation fixed
   (line 340-341 ends `$...27\,\beta(t)^2 + 4 c^3 t^2 = 0$. Conversely`).
   PASS.
7. **Compile + page count + commit + summary** --- VERIFIED independently:
   two clean runs, 11 pages $\le 16$, commit d0ad78a exists, round-1
   summary present. PASS.

## Findings

### Mainline Gaps

**M-8 ($E_m'/E_m$ quadratic-form mismatch; checks (iii)/(iv) of Def
5.1(4) incomplete).** Two form-level defects remain in the Definition
5.1(4) verification, and they feed the ranks listed under M-9.

(a) On the fibration side, Thm 4(d) asserts
$E_m'(Y,\gamma)/E_m(Y,\gamma)\simeq U(-1)$ (line 544) and the strategy
overview (line 113) asserts the same on the degeneration side. But under
the summary's own convention ($E_m'$ of rank 20, an *extension of $E_m$
by one class*), $E_m'/E_m$ has rank $20-18=2$, whereas $U(-1)$ has rank
2 but is not what the quoted degeneration-side computation says: Prop
4(d) (line 525) quotes from [GT, Example 1.2] that
$E_m'(\X)/E_m(\X)\simeq (-1)U$ **whose intersection form is negative
definite of rank 2**. Meanwhile the explicit rank-19 model
$\cE=N\oplus\bZ f'$ of lines 649-655 is built with $(f')^2=0$,
$f'\cdot f=1$, so in that model the direction quotienting out $N$
together with $W_2=\bZ f$ gives the unimodular hyperbolic form
$(\begin{smallmatrix}0&1\\1&0\end{smallmatrix})=U$, **not** $(-1)U$.
Line 671 even says "the unimodular pairing of $H=U$". Fix the lattice
model so that it actually exhibits $E_m'/E_m\simeq U(-1)$ on both sides:
i.e.\ state that $E_m'$ contains $\cE$ as the sublattice where the
$U(-1)$-partner of $f$ pairs as $\langle -1\rangle$ (or, equivalently,
change the model to $N\oplus\bZ f'\oplus\bZ g$ of rank 20 with
$f\cdot g=1$, $g^2=-2$, $f'\cdot g=0$, $(f')^2=0$, and identify
$E_m'/\bZ f$ with $N\oplus U(-1)$), and then recompute check (iii) in
that corrected model: the pairing between $E_m/W_2=N$ and
$E_m'/E_m=U(-1)$ must be shown to be the **same bilinear form** on both
sides under $\Phi$, not merely asserted to be unimodular.

(b) Check (iv) is not a verification at present: line 678-680 says the
degeneration-side $H$-polarisation restricted to $E_m(\X)$ "maps to the
same class $\sigma+2f$ in the $H$-summand". Since $\sigma+2f$ has
$\sigma\cdot f=1$, and on the degeneration side $W_2(\X)=\bZ v$ is the
kernel of the quotient map $E_m(\X)\to N$, a section-type polarisation
vector is pinned only modulo $W_2$; the claim that its image is exactly
$\sigma+2f$ (not $\sigma+2f+nv$) needs one sentence: the polarisation on
the degeneration side is the class $h\in H\subset N$ pulled back along
the DN-duality of Prop 4(d) (i.e.\ its image under
$E_m(\X)/W_2(\X)\xrightarrow{\sim}N$ is the generator $h=\sigma+2f$ of
the ample ray fixed by the $H$-polarised family hypothesis), and
the indeterminacy by a multiple of $v$ is absorbed by $v\mapsto f$
because $f$ also maps to $0$ in $E_m/W_2$. Add this one sentence.

**M-9 (rank numerology is now internally inconsistent).** The document
states all three of: $E_m'/E_m\simeq U(-1)$ (rank 2) at lines 114,
466, 525, 544, 644; $E_m'/E_m$ "is a rank $16$ lattice" at line 113
(strategy overview) and by implication "rank $16$" via line 309's
unrelated $E_8$-rank ($\operatorname{rk}(E_8^{\oplus2})=16$ is fine);
$\rk W_2=\ker N$ "of rank $21$" at line 444 while the display above it
says $\rk N=2$ on a 22-dimensional $H^2(\X_t)$ ($\ker N$ has rank
$22-2=20$, not 21). These three cannot all hold. Repair: line 444
change "rank $21$" to "rank $20$"; line 113 change "a rank $16$ lattice
isomorphic to $(-1)L_E$ where $L_E=U$, i.e.\ to $U$" to "a rank $2$
lattice isomorphic to $U(-1)$"; audit lines 108-115, 441-446, 525-527,
541-547, 643-645 so that exactly one statement of each rank survives:
$\rk E_m=18$, $\rk E_m'=20$, $\rk(E_m'/E_m)=2$, $E_m'/E_m\simeq U(-1)$,
$\rk W_2$ (deg side) $=1$ inside $E_m$ and $20$ inside $H^2(\X_t)$.

### Blocking Side Issues

None beyond M-8/M-9 (they are mainline correctness gaps, not side
issues).

### Queued Side Issues

- **Q-2.** Line 655: "a lattice of rank $19$ containing $N$ of index
  $\infty$-codimension $1$" is garbled English (should be "an overlattice
  of rank 19, i.e.\ containing $N$ as a corank-1 sublattice"). Also the
  strategy overview line 114's "$(-1)L_E$ where $L_E=U$, i.e.\ to $U$"
  should read "$U(-1)$" once corrected to rank 2 (see M-9). Fix in the
  same editing pass; not separately scheduled. Note for the record: the
  Round-1 summary's `"H^{perp-ish}" replaced by ...` claim describes a
  string that never existed in the tex source (it appeared only in the
  round-0 review's shorthand); the actual tex already had acceptable
  wording, so no harm, but summary claims should describe real diffs.
- **Q-3 (pre-existing, from round 0, not a regression).** Prop 1's proof
  (lines 162-197) silently writes $\Lambda_{\mathrm{K3}}\simeq
  U^{\oplus3}\oplus E_8^{\oplus2}$ with $E_8$ **negative** definite (per
  line 51-52's convention) and then in line 188-190 rewrites
  $E_8^{\oplus2}=E_8\oplus E_8$ as summands of $U\oplus N$. Since the K3
  lattice is $U^{\oplus3}\oplus E_8(-1)^{\oplus2}$, and Prop 1 needs the
  embedding of the *negative* $E_8$'s of $N$ into those summands, one
  clarifying sentence should be added: either adopt the convention that
  in this document $E_8$ denotes the negative-definite lattice throughout
  and the K3 lattice is written $U^{\oplus3}\oplus E_8^{\oplus2}$ in that
  convention, or insert the minus signs. One line; opportunistic.

The round-0 Q-1 items ("1-bounds are standard" grammar at line 488-489,
italic `$nef$`) were checked and are genuinely fixed.

## Directive implementation plan for Round 2 (all edits local to solution.tex)

1. **Fix the numerology first (M-9), 4 one-line edits:**
   - line 444: "of rank $21$" $\to$ "of rank $20$".
   - line 113-115: replace `$E_m'/E_m$ is a rank $16$ lattice isomorphic
     to $(-1)L_E$ where $L_E=U$, i.e.\ to $U$.' by `$E_m'/E_m$ is a rank
     $2$ lattice isomorphic to $U(-1)$.'
   - verify line 309's "rank $16$" is clearly about
     $E_8^{\oplus2}$ (it is; leave it).
   - after these edits, grep for `rank $2` / `U(-1)` / `rank $20$` to
     confirm uniqueness of each statement.
2. **Repair the Filtration model (M-8(a)), lines 649-683:** replace the
   single line putting $\cE$ by a two-generator extension: put
   $\cE\coloneqq N\oplus(\bZ f'\oplus\bZ g)$ of **rank 20**, with
   $(f')^2=0$, $g^2=-2$, $f'\cdot g=0$, $f\cdot g=1$,
   $f'\cdot f=1$, both $\perp\bZ\sigma+E_8^{\oplus2}$; state
   $\cE/\bZ f = N\oplus U(-1)$ (the $U(-1)$ spanned by the images of
   $f',g$ with form
   $\bigl(\begin{smallmatrix}0&-1\\-1&-2\end{smallmatrix}\bigr)$
   up to basis change --- state explicitly that this is $U(-1)$, e.g.\
   via $e_1=f',e_2=g-f'$ to get
   $\bigl(\begin{smallmatrix}0&-1\\-1&0\end{smallmatrix}\bigr)$);
   then on both sides $E_m'=\cE$, $E_m=N$, $W_2=\bZ f$, so
   $E_m'/E_m=U(-1)$ matches the quoted degeneration-side result. This
   simultaneously discharges M-8(a) and the rank arithmetic of M-9
   ($18+2=20$).
3. **Complete checks (iii) and (iv) (M-8):**
   - (iii): add one display: in $\cE$, the pairing
     $E_m/W_2\times E_m'/E_m\to\bZ$ is induced by the intersection form;
     compute on generators ($f\cdot g=1$, $f\cdot f'=1$, and
     orthogonality to $\sigma+E_8^{\oplus2}$) and state that under $\Phi$
     (identity on $N$, $v\mapsto f$) the same Gram matrix results on the
     degeneration side because the quoted [GT, Example 1.2] data has the
     identical form.
   - (iv): add the one missing sentence that the quasi-polarisation on
     the degeneration side is the pullback of $h=\sigma+2f$ along
     $E_m(\X)/W_2(\X)\simeq N$ (the indeterminacy by $\bZ v$ being
     exactly $W_2$, killed in the quotient, with $v\mapsto f$ mapping to
     $0$ in $E_m/W_2$), so $\Phi$ sends it to the fibration-side
     semiample class.
4. **Q-2 cosmetic:** line 655 rewrite the index-$\infty$ clause; make
   line 114 say "$U(-1)$" (already covered by step 1).
5. **Q-3 opportunistic:** in Section 1 (line 57-60) or at Prop 1, add
   one sentence fixing the $E_8$ sign convention in
   $\Lambda_{\mathrm{K3}}$.
6. Re-run `pdflatex` twice; expect 11--12 pages; commit; update summary.

All repairs are strictly local (one display replaced, ~8 lines added, ~4
one-word edits). No change to the proof architecture or to the statements
of external theorems used.

## Verdict

Round 1 genuinely advanced the mainline: five of the seven round-0 gaps
(M-1, M-3, M-4, M-5, M-7) are fully and correctly repaired, M-6 is
repaired, and the filtration display now exists in the form the contract
required. But the Definition 5.1(4) verification introduced a
quadratic-form mismatch ($U$ vs $U(-1)$) and the document now carries
three mutually inconsistent rank statements ($U(-1)$ of rank 2 vs
"rank 16"; $\ker N$ of rank 21 vs $\rk N=2$), so AC-2's "no unstated or
incorrect form carries the argument" is not yet met. These are small,
concretely repairable defects; the correct verdict is progress with
remaining mainline gaps, not a stall and not a regression.

Mainline Progress Verdict: ADVANCED
