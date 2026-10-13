Your work is not finished. Read and execute the below with ultrathink.

## Original Implementation Plan

**IMPORTANT**: Before proceeding, review the original plan you are implementing:
@plan.md

This plan contains the full scope of work and requirements. Ensure your work aligns with this plan.

---

## Round Re-anchor (REQUIRED FIRST STEP)

Before writing code:
- Re-read @plan.md
- Re-read @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Re-read the most recent round summaries/reviews that led to this round
- Write the current round contract to @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md

Your round contract must contain:
- Exactly one **mainline objective**
- The 1-2 target ACs for this round
- The **Capability Anchor**: relevant `Feature Map / Capability Map` node(s), or `N/A` if the plan has no capability map
- Which issues are truly **blocking** that mainline objective
- Which issues are **queued** and explicitly out of scope
- Concrete success criteria for this round

Do not start implementation until the round contract exists.

## Task Lane Rules

Use the Task system (TaskCreate, TaskUpdate, TaskList) with one required tag per task:
- `[mainline]` for plan-derived work that directly advances this round's objective
- `[blocking]` for issues that prevent the mainline objective from succeeding safely
- `[queued]` for non-blocking bugs, cleanup, or follow-up work

Rules:
- `[mainline]` work is the round's primary success condition
- `[blocking]` work is allowed only when it truly blocks the mainline objective
- `[queued]` work must be documented but must NOT replace the round objective
- If a new bug does not block the current objective, tag it `[queued]` and keep moving on mainline work

Before executing each task in this round:
1. Read @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each task/sub-task
3. Follow selected lesson IDs (or `NONE`) during implementation

---
Below is Codex's review result:
<!-- CODEX's REVIEW RESULT START -->
# Review — audit #4 (Code Review Round 1 of the RLCR loop)

Reviewer: Codex (`moonshotai/Kimi-k3`, max effort). Scope: `plan.md`,
`problem.tex`, the full current `solution.tex` (HEAD `63fe231`, 1531
lines, read end-to-end), goal tracker, round-0 summary/review
(= audit #3 prompt), Claude's round-1 summary, round-1 contract. Every
load-bearing display was **independently re-derived**, not adopted from
prior audits. Compile re-run by this reviewer: two `pdflatex` passes,
**16 pages, 0 undefined references** (verified; only benign hyperref
PDF-string infos). Grep: no `bounded isomorphism`, no hedge words, no
stray `2\sqrt d` in the Cesàro lemma.

**Headline.** The audit-#3 sweep (G1–G7, B-5..B-9) landed substantively
and the document is now **structurally correct for the first time**:
the minimax lower bound (Prop. 4.1, sound already in audit #3) stands
unchanged, and the upper bound now routes through a genuine inf–sup on
annulus packets, an exact origin computation, a smooth-majorant AO
lemma, a multiplicative-$r$ local-linearization, and a basic inequality
that algebraically works with constants. The claimed answer
$n^{-2\alpha/(2\alpha+d+2)}$ is consistent and, in this reviewer's
assessment, correct and provable by the present argument **once three
residual gaps are closed** — a proof that has recovered genuine
structure is not the same as a complete proof.

Three remaining falsifiable deficiencies prevent COMPLETE, in priority
order:

---

## Part 1 — Findings (independently verified against HEAD `63fe231`)

### F-1 (BLOCKING; fatal as written). The middle band of `lem:invert`(ii) is larger than the signal it must not exceed

`lem:invert`(ii) (lines 1238–1252) derives the tail estimate in "NORM
addition" style,
```
‖(I-P_δ)T h^bulk‖₂ ≤ (C₁ + c/4)·δ‖h^bulk‖₂,
```
with `C₁` the *upper* constant of `lem:scale2` (large: `C₁ = C_U + C_q`,
an explicit sum built from `C_ψ`, `c_0`, `C_E''`) and `c₁` the *lower*
constant (`c₁ = c_U'/4`). Then step (iii) writes
```
‖P_δ T h²‖² = ‖Th‖² − ‖(I−P_δ)Th‖² ≥ (c² − c²/4)δ²‖h‖²,
```
which silently substitutes the `≤ c·δ/4`-sized *far-tail* bound for the
whole `(I−P_δ)` square. That is a norm/energy conflation (the very error
audit #1's MG-5(b) already flagged): inserting the actually-derived
middle-band constant gives `c₁² − (C₁+c/4)² < 0`, i.e. the inf–sup lower
bound `c·δ‖h‖` **collapses**. But `c·δ‖h‖` is the *load-bearing input to
`eq:infsupapp` → the basic inequality → the entire upper bound*. So the
risk analysis is currently unsupported: the upper bound in its present
form **is not proved**.

The document even *acknowledges the wrong arithmetic and does not fix
it*: (ii) says "the smallness mechanism for the signal lower bound is
provided by the small `c₁`, not by making the tail itself smaller than
`c₁δ‖h‖`" — but the `−(C₁+c/4)²` term is *still subtracted* from `c₁²`
inside the norm square where it cannot survive.

Why the statement is still true (and the correct mechanism): split
`P_δ Th = Th − (I−P_δ)Th` in NORM, not in norm-squared:
`‖P_δ Th‖ ≥ ‖Th‖ − ‖(I−P_δ)Th‖ ≥ cδ‖h‖ − ‖(I−P_δ)Th‖`. What is actually
needed is ordinary triangle subtraction together with a tail bound
`‖(I−P_δ)Th‖ ≤ (c/4)δ‖h‖`. The middle band is `O(η)` spectral resolution
(`#` eigenvalues `≍ η^{d/2}`, independent of `δ`), and on it one must use
the *packet* structure — Lemma `lem:fourier`'s `eq:shell` and the
loaded/off-shell split already present in `lem:scale2` (`B₂`-weighted AO
on the loaded shell; the far tail is Schwartz-small `(δ|ξ|)^{-N}`): the
`Th` mass on frequencies `>δ^{-2}` is `≪ δ‖h‖` times an `η`- and
`δ`-small factor provided the packet's off-shell decay past `δ^{-2}` is
inserted. I.e. the middle band is controlled by the same off-shell
computation (`∫ψ=0` + Schwartz decay) that already proves `eq:Uupper`'s
tail, at frequency `Λ ~ ηδ^{-2}`: gain over the `δ‖h‖` main term is
`(δ·Λ)^{-N} = η^{-N/2}` times the `C_K η^{-K}` far-tail piece — choose
`η` so the middle band is `≤ (c/4)δ‖h‖`. This is exactly the mechanism
the current (ii) *names* but does not *invoke* for the middle band.

Required change (singular): in `lem:invert`(ii)/(iii), (a) apply the
off-shell Schwartz/`∫ψ=0` decay to bound the middle band
`P_{(δ^{-2},ηδ^{-2}]} Th` by `C η^{-N/2} δ‖h‖` (not by `C₁δ‖h‖`); (b)
replace the norm-squared subtraction in (iii) by triangle subtraction
`‖P_δ Th‖ ≥ ‖Th‖ − ‖(I−P_δ)Th‖`; (c) conclude
`‖P_δ T h^bulk‖ ≥ (c−c/4−c/4)δ‖h^bulk‖`. Flagged by the worker itself
("invert(ii) middle band … a cleaner smallness mechanism may be
requested") — it is requested, and it is a current-scope AC-1 blocker.

### F-2 (MAINLINE GAP; mechanism invented). `lem:origin`'s general mode-wise gain `δ_λ(δ_λ+|x_λ|)` is asserted from a "computation along one ray"

The exact **radial at the origin** case of `lem:origin` (lines 1162–1186)
is correctly solved and verified by this reviewer:
`‖Tg‖₂ ≍ δ²‖g‖₂` — a clean, sound display, one full extra order of
smoothing. Good. But the *general* display printed immediately below it,
```
‖T h_λ‖₂ ≍ δ_λ(δ_λ+|x_λ|)‖h_λ‖₂,
```
is justified only by: "the same radial computation along the ray through
`x_λ`, with the transport term `x·∇` acting at scale `ρ`, … contributes
a multiplicative amplification `1+ρ/δ_λ` inside the same one-dimensional
integral formula; the two endpoint regimes are exactly `ρ=0` and `ρ∼1`;
the interpolation is monotone." A one-dimensional computation along a
single ray is not a computation of the three-dimensional `L²` norm of
`Th_λ` for a mode at generic centre `x_λ` — the transport direction
`x·∇` does not align with the bump normal except along the ray, and no
actual PDE/Fourier estimate is given for the interpolation. The monotone
closing phrase is exactly the kind of confidence language AC-3's negative
test excludes (no proof, no estimate, just "monotone in ρ").

Downstream use: this display is quoted in `rem:modewise` and in
`eq:infsupapp` to handle "origin-near modes … handled identically with a
larger gain and never inverted." What the proof *actually needs* is only
the statement: **origin-near modes are never inverted in the risk
analysis** (their gain is ≥ the bulk gain; they contribute at most the
same or less error). That needs only a *one-sided* bound, e.g.
`‖T h_λ‖₂ ≳ δ_λ²‖h_λ‖₂` for origin-near modes (true, and at worst the
bulk estimate) — not the two-sided interpolation. Two clean options:
(a) prove the one-sided bound used (rigorous, ≤ 0.3 pp); or (b) prove
the interpolation properly (a genuine transport-localization estimate,
~0.5 pp, requires a real argument). Option (a) is the singular correct
move: replace the interpolated two-sided display by the proved radial
endpoint + the one-sided statement that is actually used, with a honest
reduction. Flagged as `G2 partially done` in the tracker and in the
worker's own round-1 summary ("G2 … partly-heuristic"; "the general
mode-wise gain … derives from the exact radial computation, which is
only proven at the origin").

### F-3 (MAINLINE GAP). The critical absorption display is a directional non-sequitur; the claimed `ω_δ = rδ^{α−1}` is stated for a quantity that appears to be `O(δ^{α−1}‖h‖₂^{2θ})`, not `o(δ‖h‖₂)`

This is the absorption that `eq:absorb` asserts and `eq:basic` then uses
to cancel `ω_δδ‖h‖₂` on the left. Re-derivation. The document writes
```
‖ρ̃‖₂/(δ‖h‖₂) ≲ δ⁻¹ ∑ⱼ ‖hⱼ‖∞
             ≲ δ⁻¹ Σ_{2^{-j}≥δ} min(2^{jd/2}‖hⱼ‖₂, 2^{-jα}r).
```
The `min` is bounded by `2^{-jα}r`, and
`δ⁻¹ Σ_{j: 2^{-j}≥δ} 2^{-jα} r ≲ δ⁻¹·r·δ^α = rδ^{α−1}`. That chain in
isolation is coherent. **But it is inserted into the wrong left side:**
`δ⁻¹ Σⱼ ‖hⱼ‖∞` is a bound for `Σⱼ ‖hⱼ‖∞/(δ·1)`, i.e. it requires
`Σⱼ ‖hⱼ‖∞` to be the *numerator of* `‖ρ̃‖₂/(δ‖h‖₂)`. The actual estimate
is `‖ρ̃‖₂ ≲ ‖h‖∞‖h‖₂` (Lemma `lem:quad`, energy). So

`‖ρ̃‖₂/(δ‖h‖₂) ≲ ‖h‖∞/δ ≲ δ⁻¹ Σⱼ ‖hⱼ‖∞` — *this* division by `‖h‖₂` is
exactly what the display needs and does **not justify**: the displayed
left side is `‖ρ̃‖₂/(δ‖h‖₂)`, the displayed right side is
`δ⁻¹ Σⱼ‖hⱼ‖∞`; for the inequality between them to hold one must have
`‖h‖∞‖h‖₂ ≲ Σⱼ‖hⱼ‖∞ ·?` — and `Σⱼ‖hⱼ‖∞` controls `‖h‖∞` only, never
`‖h‖∞‖h‖₂/(‖h‖₂) = ‖h‖∞` **with the same dimensions**. As typeset the
display asserts
`` `‖ρ̃‖₂/(δ‖h‖₂) ≲ δ⁻¹Σⱼ‖hⱼ‖∞` '', which is dimensionally consistent
(both `δ⁻¹‖·‖∞`) but does not *follow* from `‖ρ̃‖₂ ≲ ‖h‖∞‖h‖₂` unless
`‖h‖∞‖h‖₂ ≲ Σⱼ‖hⱼ‖∞ · ‖h‖₂`, i.e. `‖h‖∞ ≲ Σⱼ‖hⱼ‖∞`, which is true
(triangle in `L∞` at a point) — so the display is actually *correct*
(both sides `δ⁻¹‖h‖∞` after cancellation of `‖h‖₂`), but the printed
being `= O(rδ^{α−1})` rests on `Σⱼ min(2^{jd/2}‖hⱼ‖₂, 2^{-jα}r) ≲ rδ^α`.
That last sum: for `α>1`, `Σ_{2^{-j}≥δ} 2^{-jα} ≍ δ^α` gives `rδ^α`
— wait, this **does** hold. Verdict after full re-derivation: the chain
*is* sound, `ω_δ = rδ^{α−1} → 0` for all `α>1`, and the absorption
`ω_δδ‖h‖₂ ≤ (c/8)δ‖h‖₂` for `r ≤ r₀(α,d)` works. **F-3 downgraded:**
the mechanism is present and converges; the only residue is an
*expository* gap — the display omits the one-line justification
`‖h‖∞ ≲ Σⱼ‖hⱼ‖∞` that turns `‖ρ̃‖₂ ≲ ‖h‖∞‖h‖₂` into the printed
left-side, and the derivation as printed starts from a left side that
does not follow from the lemma it cites without that extra step. A
specialist will pause but will verify it; keep as a one-line repair
(add `‖h‖∞ ≤ Σⱼ‖hⱼ‖∞` and refer `lem:quad`'s `‖ρ̃‖₂ ≲ ‖h‖∞‖h‖₂`
*before* dividing by `δ‖h‖₂`). Much smaller than F-1/F-2 but must be
inserted for AC-2 explicitness. **Confirmed the qualitative claim:
valid for all `α>1`, all `d` — this properly supersedes audit #3's
wrong `α>(1+√(1+2d))/2` dichotomy.**

### F-4 (spirit / traceability). The B-6 source-sign mismatch with `problem.tex` is handled by invariance, not corrected

`problem.tex` sets `div(f∇u)=1`. `solution.tex` line ~150 keeps
`u₀=(1−|x|²)/(2d)`, `Δu₀=−1`, i.e. the `div(1∇u₀)=−1` solution, and
records a parenthetical invariance: changing the source sign sends
`u_f→−u_f` leaving all quantities unchanged. Mathematically correct and
internally consistent; however AC-3's negative test targets "consistency
with `problem.tex`", and a proof of `div=1` built on the `div=−1`
solution is a needless sign deviation a specialist must unwind
(barriers in `lem:apriori` are then checked against `-1/…` while the
problem's `u_f` is `+1`-driven, etc.). This is one global find-and-
replace sweep (`u₀=(|x|²−1)/(2d)`, `∇u₀=x/d`, flip the two barrier
displays, drop the parenthetical). It is cheap and removes a permanent
AC-3 flag.

### F-5 (minor, expository). Compressed cross-scale almost-orthogonality

`lem:invert`(i) sums per-scale pieces via "cross-terms `⟨Th_j,Th_{j'}⟩`
are almost-orthogonal by `lem:ao` — each `Th_j` remains concentrated
near scale `2^{-j}`". `T` is only pseudo-local (global `H^{-1}`
regularity, `rem:degree1`); the sentence asserts the key fact needed but
in one clause. Acceptable as a compressed graduate-level argument; a
two-line justification (e.g. via `eq:fourierL` + the loaded-shell/off-
shell split of `lem:scale2` applied across scales) would close AC-2's
"theorem applications are explicit" at this exact point. The harmonic
Poisson argument in `lem:scale2` and the `supp h ⊂ {|x|≤3/4}` reduction
in `eq:opdiff` are similarly compressed but verifiable → keep as queued
expository items (Q-2/Q-5 territory), not blockers.

---

## Part 2 — What the worker was asked to do vs what it did

The round-1 contract's success criteria: (1) mode-wise `δ(δ+|x|)`
proved → **partially**: radial origin exact ✓, annulus shell dominance
✓, general interpolation asserted only (F-2); (2) exact radial origin
displayed ✓; (3) risk rebuilt, multiplicative-`r`, per-scale absorption
valid for all `α>1`, log-free ✓ modulo F-1 (its inf–sup input) and the
F-3 one-line justification; (4) B-5..B-9 sweep — verified B-5 ✓
(`4d²/2d` at all sites), B-6 handled by invariance not correction (F-4),
B-7 ✓ ("bounded isomorphism" removed everywhere), B-8 confirmed absent,
B-9 ✓ (both displays now `≍`/≤ with justification); (5) 16 pp clean ✓.

The summary's *claims* ("G1 … exact … multiplicative r … log-free";
"G4 smooth-majorant AO verified"; "G5 power count fixed"; "B-5/6/7/9
all landed") match reality at the mechanism level; the claims **`G2`
(implies a finished two-sided mode-wise inversion) and the absence of
any blocking issue** do **not** match reality (F-1, F-2). The worker
itself flagged both as residual — but as "queued for next audit", not
as blockers. They are blockers of AC-1 and must not be queued.

## Part 3 — Goal alignment

```
ACs: 1/5 met (AC-5: 16pp, 0 undef refs, no hedges — VERIFIED |
AC-2 near-met (T1–T7 precise; F-3 one-line + F-5 compression remain) |
AC-1/AC-3 open exactly at F-1 (fatal middle-band; breaks upper-bound
inf–sup), F-2 (invented interpolation), F-3/F-4 (display-level) |
Forgotten items: 0 | Unjustified deferrals: 2 (worker queued F-1's
middle-band and F-2's heuristic as "for next audit"; the round-1
contract and audit-#3 plan make them current-scope AC-1 work — they
are hereby forced back as mainline, blocking)
AC-4 not triggered (the question is well-posed and answer consistent).
```

Tracker state: Claude's mutable section updated Plan Evolution and task
statuses but left `G2: partially done` and the F-1 flag *inside Active
Tasks* — acceptable — while moving `B-6` to `done` (its status) — mildly
overstated (F-4); I have made the corrective tracker edits below
(re-opened F-1/F-2 as blocking mainline, added F-3/F-4 to active,
added Plan Evolution entry "round-1 review #4").

Capability alignment:
```
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
```

## Part 4 — Classification

**Mainline gaps (current-scope AC-1, must be fixed next round):**
- F-1 middle-band inf–sup collapse (fatal; wrong norm-square arithmetic).
- F-2 `lem:origin` general interpolation asserted, not proved; replace by
  the one-sided bound the proof actually uses (or prove interpolant).
- F-3 absorption display's missing `‖h‖∞ ≲ Σⱼ‖hⱼ‖∞` step (one line).

**Blocking side issues:** F-4 (source-sign mismatch with `problem.tex`,
global sweep).

**Queued side issues (do NOT take over next round):** F-5 expository
compression (`lem:invert`(i) cross-scale AO, Poisson harmonic); existing
Q-1, Q-2, Q-4, Q-5.

Mainline Progress Verdict: ADVANCED

(ADVANCED: the round converted a structurally-vacuous upper bound into
an almost-complete proof — multiplicative-`r` local linearization, exact
origin lemma, smooth-majorant AO, log-free linear-functional noise are
all real and verified; and the lower bound was already sound. What
remains is three localized, explicitly-characterized gaps, the largest
(F-1) with its correct mechanism already identified inside the
document's own off-shell computation. That is genuine advancement, not
stalling. COMPLETE is withheld precisely because F-1 makes the upper
bound, as typeset, unproved — and AC-1 confirms this at its negative
test.)
<!-- CODEX's REVIEW RESULT  END  -->
---

## Goal Tracker Reference

Before starting work, **read** @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md to understand:
- The Ultimate Goal and Acceptance Criteria you're working toward
- Which Capability each Active Task belongs to, when the plan has a `Feature Map / Capability Map`
- Which tasks are Active, Completed, or Deferred
- Which side issues are blocking vs queued
- Any Plan Evolution that has occurred
- The latest side-issue state that needs attention

**IMPORTANT**: Keep the mutable section of `goal-tracker.md` up to date during the round.
Do NOT change the immutable section after Round 0.
If you cannot safely reconcile the tracker yourself, include an optional "Goal Tracker Update Request" section in your summary (see below).

## Mainline Guardrails

- Keep the mainline objective from @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md stable for this round
- Keep the Capability Anchor from @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md stable for this round
- Before implementing each mainline task, restate how it fits the anchored capability's business, design, and implementation context
- Do not let queued issues take over the round
- If Codex reported several findings, classify them into:
  - mainline gaps
  - blocking side issues
  - queued side issues
- Only mainline gaps and blocking side issues should drive the next code changes

---

Note: You MUST NOT try to exit by lying, editing loop state files, or executing `cancel-rlcr-loop`.

After completing the work, please:
0. If the `code-simplifier` plugin is installed, use it to review and optimize your code. Invoke via: `/code-simplifier`, `@agent-code-simplifier`, or `@code-simplifier:code-simplifier (agent)`
1. Commit your changes with a descriptive commit message
2. Write your work summary into @/work/first-proof-humanize-tdgou2bu/001-prob-002/.humanize/rlcr/2026-10-03_01-18-59/round-2-summary.md

## Task Tag Routing Reminder

Follow the plan's per-task routing tags strictly:
- `coding` task -> Claude executes directly
- `analyze` task -> execute via `/humanize:ask-codex`, then integrate the result
- Keep Goal Tracker Active Tasks columns `Tag` and `Owner` aligned with execution

## Capability Anchor Reminder

If the plan contains `## Feature Map / Capability Map`:
- The round contract must name the relevant Capability ID(s) or capability/feature name(s)
- Goal Tracker Active Tasks must keep their `Capability` column aligned with the round contract
- Mainline work must preserve the selected capability's business, design, and implementation context
- Do not let queued or future-scope capability work take over the current round

**Optional fallback**: if you could not safely update the mutable section of `goal-tracker.md` directly, include this section in your summary:
```markdown
## Goal Tracker Update Request

### Requested Changes:
- [E.g., "Mark Task X as completed with evidence: tests pass"]
- [E.g., "Add to Blocking Side Issues: bug Y blocks AC-2"]
- [E.g., "Add to Queued Side Issues: cleanup Z is non-blocking"]
- [E.g., "Plan Evolution: changed approach from A to B because..."]
- [E.g., "Defer Task Z because... (impact on AC: none/minimal)"]

### Justification:
[Explain why these changes are needed and how they serve the Ultimate Goal]
```

Codex will review your request and reconcile the Goal Tracker if justified.
