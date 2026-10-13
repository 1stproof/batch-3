# Round 3 Contract (drift recovery)

## Recovered mainline objective (exactly one)
Resolve the single three-round defect at `prop:EF`: the printed `(SK)` first channel is
`-delta th q^{-2} cK_s^{(-)-1}` (NOT `-delta th cK_s^{(-)-1}`), so the `(EF)->(EF')`
conversion that (M2), Part-1 well-definedness, and Part-2's quotient stand on is,
as a literal stated implication, unproved. This round makes the exact mathematical
status of that step fully proved one way or the other and rebuilds the arc layer on
the result, so that `S_n(B*) ~ D` and `S_n(B*)/I ~ H = U_q^{ext}(sl(n))` are proved.

## Target ACs (proof of mainline movement)
- AC-1: the (EF)/(EF') step and the cross commutator made rigorous; thm:mixed(e)=(M2),
  thm:one (Part 1) and lem:diag (Part 2) re-derived on the corrected basis.
- AC-3: verification rebuilt so it FAILS loudly on a wrong EF coefficient; no engine
  asserts (EF') as a step rule.

## Capability anchor
N/A (plan.md has no capability map).

## Root cause of the drift/stagnation
Across rounds 0-2 the pairing/cross layer kept being repaired at the convention level
(kernel slot, (PA) line order) while the decisive scalar - the first (SK)
`<x_1,S^{-1}(y_1)>` channel with a two-letter second argument `S^{-1}(E_r)=-E_r cK_r^{-1}`
- was never confronted honestly. The round-2 review pinned its true value `-th q^{-2}`
and showed the "two (PA) variants agree on single letters => cross calculus insensitive"
claim false. The prior worker left three uncommitted patches that restore the `q^{-2}`
but did not resolve the downstream `(EF)->(EF')` gap.

## Blocking issues (in scope)
- B1 (FATAL, reviewer A1): decide the status of `(EF)->(EF')` in D. Two-live-options:
  (a) a q^2-cancelling grouplike channel (engine: `cross(E,F.cK)` picks up a `q^{+2}`
      on the `F E cK` channel) may make the derivation valid WITHOUT rescaling E; or
  (b) D1(a) of the review: accept the twist, rescale `E'_r=q^{-1}E_r`, re-derive
      def:phi / minors / M-relations / Part-2 from the rescaled map.
  Whichever is mathematically forced - execute it completely; do NOT leave the
  "sensitive to (PA) variant" sentence false; do NOT keep a derivation that only
  "reduces both to the same normal form" by assertion.
- B2: every downstream display re-derived in the final world (arc images, minors, M0-M3,
  M2/bigon face, Omega centrality, lem:diag). No transposed stale expectations.

## Queued (out of scope this round)
- Q2 scratch tidying; Q3 the (SK) "exhaustive enumeration" prose trim;
  label hygiene ((conj)/(CJ),(MXg)).

## Success criteria (verdict -> ADVANCED)
- `prop:EF`/cross commutator correct AND every use of `(EF')` justified by an explicit,
  hand-checkable derivation (not an asserted engine equivalence);
- (M2), thm:one, lem:diag re-established in the corrected world with the arc minors
  recomputed;
- one engine with full two-letter `<x_1,S^{-1}(y_1)>` support deriving (EF); the
  (EF)->(M2-raw) step checked by rewrite; the battery fails on a wrong coefficient;
- `rem:verify`, goal-tracker, bitlesson updated; clean compile <=16 pp; committed.
