# Round 2 Summary

## Work Completed
Round-2 contract (post audit #4) executed: the three mainline gaps (F-1,
F-2, F-3) and the blocking side issue (F-4) are all fixed at the mechanism
level.

- **F-1 (fatal / mainline — `lem:invert`(ii)/(iii)).** The old middle-band
  used the crude `C_1 δ‖h‖` bound inside a *norm-squared* subtraction,
  which collapses (`c_1²-(C_1+c/4)²<0`). Fixed by: (a) changing the sieve
  projector `P_δ` to cut at Dirichlet eigenvalue `≤ C_W δ^{-2}` (i.e.
  physical scale `≳ δ`, matching the one-degree smoothing; `dim V_δ ≍
  δ^{-d}` preserved by Weyl — `T:weyl` and §(A) updated); (b) bounding the
  spectral tail by `lem:scale2`'s own off-shell Schwartz decay
  (`eq:Uupper` tails, `∫ψ=0`), giving the new `eq:spectail`
  `‖(I-P_δ)Thᵇᵘˡᵏ‖ ≤ C̃ C_W^{-N/4} δ‖hᵇᵘˡᵏ‖`, with the fixed constant
  `C_W` chosen so the tail `≤ (c/4)δ‖h‖`; (c) step (iii) now uses
  *ordinary norm (triangle) subtraction*
  `‖P_δTh‖ ≥ ‖Th‖ - ‖(I-P_δ)Th‖ = (3c/4)δ‖h‖`, replacing the impossible
  norm-square line. The inf–sup input to `eq:infsupapp` → the basic
  inequality is now sound.
- **F-2 (mainline — `lem:origin`).** The invented two-sided interpolation
  `‖Th_λ‖ ≍ δ_λ(δ_λ+|x_λ|)‖h_λ‖` (justified only by a "one-ray"
  computation + "monotone" rhetoric) is **deleted**. Replaced by the
  one-sided bound actually used downstream, `eq:origingain`
  `‖Th_λ‖ ≳ δ_λ²‖h_λ‖` for origin-near modes, proved by re-running
  `lem:scale2`'s loaded-shell power count with the single change
  `|x_m|² ≲ δ_λ²` (one full extra power of `δ_λ`), harmonic `q` absorbed
  into `δ_0`. `rem:modewise` updated (Γ_λ phrase gone; "never inverted, no
  two-sided estimate needed"). The radial endpoint's exterior step
  (`w≡0` on `[δ,1]`) was made rigorous (`w'=0` there + `w(1)=0` instead
  of quoting scale2's annulus support fact).
- **F-3 (mainline — absorption).** The chain now cites `lem:quad`'s
  `‖ρ̃‖₂ ≲ ‖h‖_∞‖h‖₂` and the pointwise `‖h‖_∞ ≤ Σ_j‖h_j‖_∞` (L^∞
  summability since `‖h_j‖_∞ ≲ 2^{-jα}r`, `α>0`) *before* dividing by
  `δ‖h‖₂`, closing the explicitness gap; conclusion `ω_δ = rδ^{α-1} → 0`
  (`α>1`) unchanged.
- **F-4 (blocking — source sign).** Global sweep to `problem.tex`'s
  `div(f∇u)=1`: `u_0=(|x|²-1)/(2d)`, `∇u_0=x/d`, `Δu_0=1`; sign-invariance
  parenthetical deleted; `eq:u0prop` sign flipped; `lem:lin` defines `Tg`
  by `-Δw = -div(g∇u_0)` so `Δ(Tg)=+Lg` is preserved (all uses of `T`
  are norm-valued, hence sign-agnostic under `T↦-T`); `lem:apriori`
  barriers recomputed (sub `u_0/(1+r)`, super `u_0/(1-r)`); `(f-1)∇u_0
  =(f-1)x/d`; opdiff `u_m-u_0=+Δ^{-1}div((m-1)∇u_0)`;
  `div(m∇(u_m-u_0))=+div((m-1)∇u_0)`; fine-scale `div(f_0∇w)=+div(e∇u_m)`.

**Incident note.** Mid-pass a `git stash`/`pop` cycle briefly reverted the
uncommitted edits (and a dangling recovery stash was dropped). The exact
patch sequence was replayed and the work committed immediately
(`ccec7ee`, final build `d80b673`).

## Files Changed
- `solution.tex`: F-1 (`T:weyl`, §(A) `V_δ`/`P_δ`, `lem:invert` + proof
  (ii)/(iii), `eq:spectail`), F-2 (`lem:origin` statement + proof,
  `eq:origingain`, `rem:modewise`), F-3 (absorption chain), F-4 (u₀
  display, `eq:u0prop`, `lem:lin`, `lem:apriori`, `∇u₀`/opdiff/fine-scale
  sign sites); page-economy `geometry margin=0.93in`.
- Audit artifacts (`solution.pdf/.aux/.log/.out`) regenerated.

## Validation
- `pdflatex -interaction=nonstopmode` ×2: **16 pages**, 0 errors, 0
  undefined references, `pdftotext` shows 0 `??`.
- Sign-consistency grep: no residual `div(f∇u_f)=-1`, no `1-|x|²`,
  no `\Delta u_0=-1`, no `\nabla u_0(x)=-`, no "immaterial" parenthetical.
- PDF text inspection of §5.2 (Lemmas 5.2/5.3, (ii)/(iii), Remark 5.4)
  and the absorption display confirms all four fixes render correctly.
- No `\linespread`/`\setlength` hacks; article class + standard packages.
- Overfull hboxes: 7, all pre-existing in un-edited regions (non-fatal).

## Remaining Items
- Awaits independent audit #5. Within round scope: none. Out-of-scope
  (contract "queued side issues"): F-5 expository compression
  (`lem:invert`(i) cross-scale AO), Q-1/Q-2/Q-4/Q-5. The AC-3 note
  "reduce to ≤15pp for safety" is superseded: geometry `margin=0.93in`
  gives 16pp without content cuts.

## BitLesson Delta
- Action: add
- Lesson ID(s): BL-20261003-no-git-stash-mid-round
- Notes: Never run `git stash`/`git pop` while holding uncommitted
  deliverable edits in this loop — a stash conflict silently reverted an
  entire round's work; commit to a branch (or a WIP commit) before any
  compile-vs-baseline comparison. Reversible-by-commit beats stash.
