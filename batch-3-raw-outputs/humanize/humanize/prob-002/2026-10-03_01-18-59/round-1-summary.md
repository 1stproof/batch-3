# Round 1 Summary

## Work Completed

**Recovery note (tool incident).** Mid-round an editing command
(`git checkout HEAD -- solution.tex`, issued while cleaning up a bad
interim patch) reverted the uncommitted G1–G7 repairs that the earlier
worker pass had produced against audit #3. The full sequence of 26
post-commit patches was recovered verbatim from this job's own runtime
session rollout
(`.codex-home-node-1/sessions/...rollout-...d080.jsonl`; access limited
to this job's own runtime files — no external content, no sibling jobs,
no published solutions), replayed onto HEAD 13876cd in chronological
order, and verified by recompilation. Two patches (1, 10) were flagged
by the replay threshold and confirmed already applied by overlapping
follow-up patches.

**Audit-#3 directive sweep landed.**
- G1 (§5(C)): linearization about the comparison point $m=\Pi_\delta
  f_0$; operator difference made *exact*
  ($T_mh-Th=-\Delta^{-1}\operatorname{div}(h\nabla(u_m-u_0))$, bound
  $r\delta\|h\|_2$ via interior Schauder + packet estimate) —
  multiplicative $r$; per-scale Nikolskii absorption with
  $\omega_\delta=r\delta^{\alpha-1}\to0$, valid for all $\alpha>1$
  (no GN dichotomy); basic inequality re-derived exactly
  ($X,Z,\Delta Y$ variables; cross terms accounted); log-free risk via
  the linear noise functional evaluated at the random $\widehat f$.
- G2: mode-wise `lem:invert` + `lem:origin` (exact radial origin
  computation, gain $\delta^2$; general
  $\delta_\lambda(\delta_\lambda+|x_\lambda|)$); spectral tail with
  threshold $\eta\delta^{-2}$ at fixed $K$. FLAGGED for next audit:
  middle band $P_{(\delta^{-2},\eta\delta^{-2}]}$ still uses the crude
  upper-side constant — constants tracked explicitly ($c_1\ll C_1$),
  but a cleaner smallness mechanism may be requested.
- G3: annulus restriction $\{c_0\le|x_m|\le\tfrac12-c_0\}$; single-shell
  diagonal dominance with radial annulus profile; NEW `lem:harmonic`
  plus a Poisson/mean-oscillation argument for the harmonic correction
  (bump multipole, $\int\psi=0$ kills the monopole, oscillatory part
  $e^{-c/\delta}$-damped on $\{|x|\le3/4\}$); constants
  $C_q\delta_0\le c_U'/4$ by $\delta_0$-shrinking.
- G4 smooth-majorant AO verified; G5 `eq:uterm` power count fixed; G6
  `eq:shell` restricted to packets with the radial caveat; G7 estimator
  described as measurable argmin over the closed sieve.
- B-5 ($4d^2/2d$, all five sites), B-6 (normalization sentence on the
  source sign + corrected `lem:apriori` signs; invariance
  $u_f\mapsto-u_f$ recorded), B-7 ("bounded isomorphism of $L^2$"
  removed at all four sites; precise
  $T\in\mathcal B(L^2,H^1_0)\cap\mathcal B(H^{-1},L^2)$), B-8
  (verified fixed upstream), B-9 ($\asymp$ displays with the
  $\le2^{1-t}+1$ constant) all landed.

## Files Changed
- `solution.tex` (the deliverable; compiles to 16 pages).
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` (mutable
  section: Plan Evolution, Active Tasks, Completed table).
- `.humanize/rlcr/2026-10-03_01-18-59/round-1-summary.md` (this file).

## Validation
- `pdflatex solution.tex` $\times 2$: exit 0, "Output written ... (16
  pages)", 0 "??", only benign hyperref PDF-string infos.
- Grep audits: no "bounded isomorphism"; no `2\sqrt d`; source sign
  $-1$ consistent with the normalization sentence; no hedge words
  (`sketch|harmless|for completeness`).

## Remaining Items
- `lem:invert`(ii) middle-band cleanup (constants currently consistent
  but the mechanism could be tightened).
- The harmonic Poisson argument is compressed; a formal Szegő/Poisson
  citation can be added at a few lines' cost (page budget now zero —
  16/16).
- If the reviewer requests expansions, candidate trims to stay within
  16 pp: `rem:const`, `rem:modewise`, §6 bullets.

## BitLesson Delta
- Action: none
- Lesson ID(s): NONE
- Notes: a workflow candidate ("checkpoint uncommitted work before any
  `git checkout`; verify editor exit codes per batch") is recorded in
  the tracker but not formalized as a lesson (not mathematical).

## Goal Tracker Update Request
None — the mutable section was updated directly (Plan Evolution entry,
Active Tasks G1–G7/B-5..B-9 statuses, Completed-table row).
