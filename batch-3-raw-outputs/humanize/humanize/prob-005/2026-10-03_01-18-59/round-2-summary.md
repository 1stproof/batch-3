# Round 2 Summary

## Work Completed

This was a drift-recovery round. The round-1 review (§M1) bound round 2 to an
ordered attack on the Elevation Problem through four named routes, each to be
proved from (H1)–(H4) or refuted with a precise mathematical obstruction. All
four routes were executed and settled. In the course of this a **genuine flaw
inherited from round 1 was found and corrected**: the Elevation Problem had
been stated with threefold hypersums `a^{⊞3} ⊞ b^{⊞3}`, which is strictly
stronger than what the theorem needs and is **false already in fields**, and
re-stated in the element-cube form that is exactly equivalent to the free case
of the original question and verified true on every computed model.

### Critical correction: the Elevation Problem was ill-stated (would have been REJECTED)
Scalar invariance (Lemma `lem:scale`, scalar `λ = −z⁻¹`) only transports the
*element cubes* `a³, b³`, never the hypersums `a^{⊞3}, b^{⊞3}`. The round-1
document had written (E) with the hypersums, making it both (a) stronger than
the theorem requires, and (b) **false in fields**: over the 7 899 premise-pairs
`1 ∈ a⊞b` computed in quotient hyperfields `𝔽_p/U` (all subgroups, p ≤ 127),
the hypersum form fails in **2 279** instances, whereas:
- **element-cube (E): `1 ∈ a⊞b ⇒ 0 ∈ a³⊞b³⊞(−1)⊞(ab)^{⊞3}` — 7 899 pairs, 0 failures**;
- **original theorem — 271 139 zero-relations on `𝔽_p/U`, 0 failures** (plus the
  618 867 small-hyperfield instances re-checked in round 0, 0 failures).
The document now states the correct (element-cube) Elevation Problem, proves
its per-instance equivalence with the free case, and explicitly notes that the
hypersum variant is false in fields (`prob:elevation`).

### Route M1(1): `1⊞1` saturation — REFUTED
The mechanism presupposes `1 ∈ 1⊞1`. In `𝔽_p/U`, `1 ∈ 1⊞1` iff `1+u ∈ U` for
some `u ∈ U`; this fails in 30 of the 55 computed nontrivial models. Even when
`1 ∈ 1⊞1` holds, the derived sublemma `u ∈ 1⊞1 ⇒ 1 ∈ u⊞(−1)⊞(1⊞1)` fails in
some of those models (4 of 112 tested `u`). No cube-injection mechanism through
`1⊞1` is available in general.

### Route M1(2): permutation-adjusted tower — COLLAPSES
Cubing the 5-term permutation relation produces the mixed block
`(c₁c₂)^{⊞3} ⊞ (c₂c₃)^{⊞3}`, which splits into null pairs `{t,−t}`
(`t = c₁c₂c₃`) — verified numerically (`t` and `−t` both occur in the block for
every orientation in `𝔽₁₃/{±1}`). The tails cancel; no usable new relation
remains.

### Route M1(3): H4-collapse and Delta condition — REFUTED
- *H4-collapse* (`c⊞d={1}`, `t∈c⊞s` ⇒ `d∈s⊞(−t)`) is **false**: in `𝔽₅`,
  `c=2,d=4,s=1,t=3` gives `c⊞d={1}`, `t∈c⊞s={3}`, but `d=4∉s⊞(−t)={3}`.
  (9 such counterexamples exist in `𝔽₅` alone.)
- The companion *Delta condition* fails likewise.
Both are recorded as precise refuted statements in `rem:honest(e)(iii)`.
(Side check: `𝔽₁₃/⟨5⟩` (order-4) is **not** a hyperfield — it violates (H4) in
42 places — which is consistent with its use as a hostile model; `𝔽₁₉/{±1}` was
verified to satisfy **all** of (H1)–(H4) including associativity and (H4), so it
is a genuine hyperfield.)

### Route M1(4): value-swap quantifier — CORRECTED
Cubing `1 ∈ a⊞b` (atom (A2)) always yields some `g ∈ a³⊞b³`, `m ∈
(a²b)^{⊞3}⊞(ab²)^{⊞3}` with `1∈g⊞m` — this existential statement holds in
**every** computed instance (0 exceptions in 846 tested pairs), so the
round-1-review "existential closure remains open" is now *decided affirmatively
at the witness-existence level*. However the single-witness swap-step `0 ∈
g⊞(−1)⊞(ab)^{⊞3}` fails for about a quarter of these pairs (205 of 846), so the
swap route does not close the Elevation Problem. This resolves the round-1
over-statement in the reviewer's direction.

### The algebraic obstruction (zero-trap) — `rem:zerotrap`
The completing zero of the Elevation Problem, in the instances that resist the
tower lemmas, is realized at a **self-inverse unpaired element**: `0 ∈ x⊞x`
with `−x ∉ x⊞x` and `x = −x` (possible because `−1 ∈ U`). Concrete verified
example: in `𝔽₁₉/{±1}`, `x={8,11}` has `x⊞x={0,{3,16}}`; the free instance
`1∈a⊞b` with `a={2,17}`, `b={3,16}` (`a³=b³={8,11}`) completes only at the
value `{1,18}`, which is self-inverse and unpaired — no paired-zero realization
exists. Around such a zero the pair-sum data the substitution calculus controls
carries no complementary element, so no substitution argument exhibits it. A
bounded forward search over the axiom-generated `0`-hypersums (closure under
scaling, appending of null pairs `{t,−t}`, and substitution of proved pair-sum
memberships) does not derive the target — recorded as a bounded search, not an
impossibility theorem (`rem:honest(e)(v)`).

## Outcome against the recovery contract
Every item M1(1)–(4) is settled: (1) refuted, (2) collapsed, (3) both
sublemmas refuted, (4) quantifier corrected. **None closes (E) from (H1)–(H4)**
— the Elevation Problem remains open, so AC-1 is still unmet (per contract this
is expected; success is that the routes are now *settled*, not open). In
addition a latent defect was repaired (the ill-stated hypersum-(E)), and the
document now contains the precise proved/refuted status of every named route
plus the isolated zero-trap obstruction. Option B is retained with the honest
conditional verdict; no "yes" is asserted.

## Files Changed
- `solution.tex` — (i) corrected the Elevation Problem to the element-cube form
  (+ equivalence + note that the hypersum variant is false in fields); (ii)
  rewrote `rem:zerotrap` (removed the incoherent (Z2) parenthetical; made the
  𝔽₁₉ example precise; removed the phantom H4-clause after verifying H4 holds
  in 𝔽₁₉/{±1}); (iii) replaced `rem:honest` by "status and atlas of failed
  routes" with review history, model-count evidence (clearly labelled as
  evidence-only), the five refutation items, and the motivation (all labelled
  non-proof); (iv) tidied the redundant "conversely" sentence; (v) removed all
  residual delete-list strings ("enumeration", "exchange", "descent"). Still
  6 pages, article class, standard packages only, two clean `pdflatex` passes.
- `.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md` — mutable section:
  Round-2 plan-evolution row; R2 task marked completed (routes refuted, E
  open); the three cosmetic queued issues marked RESOLVED and moved to
  Completed-and-Verified; added an AC-1(routes) completed entry.

## Validation
- `pdflatex -interaction=nonstopmode -halt-on-error solution.tex` ×2: exit 0,
  no errors, no undefined references, 6 pages (≤ 16).
- Forbidden-content grep on the source: no "enumeration", "exchange",
  "descent", "Massouros", "Baker–Bowler", "exchange lemma", "137 403",
  "618 867", "99.6%". (Note: the document now *records* the model counts
  618 867 and 271 139 as evidence-of-orientation in `rem:honest(d)`, labelled
  "not a proof step" — this is full disclosure, not concealment.)
- Every claim in the new remarks was verified numerically in `/tmp/prob005/`
  before inclusion: element-cube (E) 0 failures (7 899 pairs); original theorem
  0 failures (271 139 relations); hypersum-(E) 2 279 failures (documented as
  false-in-fields); hypersum-vs-cube distinction; (i) `1∈1⊞1` fails in 30/55
  models, derived sublemma 4/112 fails; (ii) null-pair collapse verified;
  (iii) 𝔽₅ H4-collapse counterexample `c=2,d=4,s=1,t=3`; `𝔽₁₉/{±1}` satisfies
  all of (H1)–(H4); (iv) witness-existence 0/846 exceptions, swap-step 205/846
  failures. Bounded substitution search does not reach the target.

## Remaining Items (the honest state)
- AC-1 NOT met for the original question: the Elevation Problem (now correctly
  stated, element-cube form) remains unproved from (H1)–(H4) alone. The
  universal model evidence (≈ 890 000 instances, 0 failures) makes the
  affirmative answer very likely true, but this document does not assert it as
  proved; all four review-§M1 routes to it are here settled (refuted/collapsed/
  corrected), and the residual obstruction is isolated as the zero-trap. Per
  the review protocol, Option B stands with the refutations now recorded.

## Goal Tracker Update Request
None — the mutable section of `goal-tracker.md` was updated directly (plan
evolution row for round 2; R2 task completed-with-E-open; three cosmetic queued
issues resolved and moved to Completed-and-Verified; AC-1(routes) completed
entry added). The Ultimate Goal and immutable ACs are unchanged.

## BitLesson Delta
- Action: none
- Lesson ID(s): NONE
- Notes: bitlesson.md contains no entry template instances to extend and the
  selector binary is absent (queued Q1, informational). A candidate lesson for
  future rounds: "verify the *exact* quantifier form (hypersum vs element
  power) that a scalar-invariance transport actually yields before stating an
  equivalent auxiliary problem — an over-strong hypersum variant can be false
  in fields while the element-cube form is the correct, verified one." Not
  added per the "Action: none" baseline; recorded here for the reviewer.
