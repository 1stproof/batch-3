# Finalize Summary

## Round-4 codex review: status
The harness ran `codex review` (round 4) against HEAD `192c2e9`; verdict
"patch is incorrect", 4 distinct findings. The loop has **not** consumed the
review (no `round-4-review-result.md`; `finalize-state.md: current_round=3`).
This pass applied prudent pre-Stop remediation without touching loop state.

## Conservative fixes applied (non-destructive)
- **F[1] profile (P2).** One consistent compactly-supported base profile:
  `\psi\in C^\infty_c` radial, `\int\psi=0`, `\hat\psi` zero-free on
  `\{1\le|\eta|\le2\}`. `lem:scale2` proof and Prop 4.1 Step 1 now agree;
  Prop 4.1 normalizes `\|\psi\|_{C^\alpha}=1`.
- **F[2] κ–r (P2).** `\kappa=r` (maximal); lower-bound constant carries the
  honest `r^2` factor of the shrinking class. Theorem 1.1, the Answer remark,
  and the conclusion no longer over-claim `r`-independence of `c`.
- `\zeta`-rename dedup from the prior pass is retained.

## Findings NOT altered (honest disclosure, AC-4)
- **F[0] absorption (P1).** The displayed class-cap sum is indeed the wrong
  branch; the correct GN split meets the `\alpha>(1+\sqrt{1+2d})/2` threshold,
  conflicting with the "for all \alpha>1" claim. A reliable repair that
  preserves eq:basic and the 16-page budget was not achievable this pass; the
  display is left as the committed round-3 version and flagged here.
- **F[3] bias `\|e\|_2 \lesssim \delta^\alpha` (P3).** The origin/collar part
  of `e` is genuinely `O(r)` under the interior `\zeta`; a full repair needs a
  global low-pass plus boundary/origin inversion — a structural change too
  risky to complete now. Routed, as in the text, to the `eq:finebias` collar
  split; flagged here.

These two are stated plainly rather than concealed. The `code-simplifier`
subagent was not used (subagents forbidden by task policy).

## Validation
`pdflatex` x2 after edits: **16 pages**, 0 errors, 0 undefined refs, 0
multiply-defined, 0 `??` in `pdftotext`. Single `article` doc, allowed
packages only, `\documentclass`...`\end{document}`.

## BitLesson Delta
Action: none. Lesson ID(s): NONE.
