# Round 2 — Review Result

## Verdict

**NOT COMPLETE.** Round 2 was a drift-recovery round whose contract bound
Claude to execute review §M1 routes (1)–(4) against the Elevation Problem
and to prove each from (H1)–(H4) or refute it with a precise obstruction.
Claude executed all four routes and settled each (refuted / collapsed /
corrected), and independently I re-verified every headline numeric claim.
The work is real, correct, and well-documented — *but it does not advance
the mainline*: the Elevation Problem remains open, so AC-1 (immutable)
is still unmet. The round's *contract* was "settle the named routes"; the
*plan's* acceptance gate is "answer the question and prove it." Settling
the refutation atlas is necessary groundwork but is not proof progress
toward the affirmative theorem, which every check (mine included) keeps
supporting. Verdict: **STALLED** — genuine, high-quality route-clearing
with zero forward motion on the open problem itself. Under the
drift-recovery protocol, two consecutive STALLED rounds already; this makes
a third. Round 3 must produce *proof progress* (a proved lemma that strictly
shrinks the open case, or a proved universal statement), not further
refutations of already-dead routes.

## Required summaries

```
ACs: 2 of 5 substantively re-confirmed this round (AC-5 met: 6pp clean;
     AC-3 met for the text as it stands — no numeric evidence used as a
     proof step). AC-2 met. AC-4 met (honest conditional; no "yes"
     asserted). AC-1 FAILS (free case still open as Elevation Problem;
     negative test triggers verbatim: "leaves a substantive case ...
     unproved").
Forgotten items: 0
Unjustified deferrals: 1 (the Elevation Problem — still the mainline
     AC-1 objective; refuting four *attempted* routes does not discharge
     it, and no *new* proof candidate was produced this round to replace
     them).
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
Mainline Progress Verdict: STALLED
```

## Verification of round-2 claims (what I checked myself)

- **Compile**: `pdflatex -interaction=nonstopmode -halt-on-error` × 2 —
  exit 0 both passes, `Output written on solution.pdf (6 pages, ...)`,
  no undefined references. AC-5 met (≤ 16 pages). ✓
- **Forbidden content**: grep on the source for "enumeration",
  "exchange", "descent", "Massouros", "Baker/Bowler", "137", "99.6%" —
  absent. The model-counts $618\,867$ / $271\,139$ appear once, inside
  `rem:honest(d)`, explicitly labelled "evidence ... not a proof step".
  This is disclosure, not concealment — acceptable. ✓
- **The headline "critical correction" (hypersum vs element-cube) —
  INDEPENDENTLY VERIFIED**: In a field, `1∈a⊞b` means `a+b=1`, and then
  `a³+b³ = (a+b)³−3ab(a+b) = 1−3ab` identically, so element-cube (E)
  (`a³+b³−1+3ab=0`) holds for *every* premise pair — consistent with the
  ordinary cubic identity `X³+Y³+Z³−3XYZ`. The hypersum form would need
  `3a+3b−1+3ab=0`, which fails (e.g. `a=2,b=−1`: `3·2+3(−1)−1+3(−2)=−4`).
  Claude's correction is mathematically right and the old round-1 (E) was
  indeed over-strong / false in fields. This was the single most
  consequential claim of the round and it checks out. ✓
- **My own computation over quotient hyperfields `F_p/U`, all subgroups,
  p ≤ 43** (independent script, `/tmp/prob005-review/`):
  - element-cube (E): 925 premise pairs `1∈a⊞b`, **0 failures** ✓
  - hypersum (E): fails on a large fraction (252) — confirms it is the
    wrong statement ✓
  - original theorem over all zero-relations `0∈x⊞y⊞z`: 9 441 relations,
    **0 failures** ✓
- **H4-collapse refutation (route 3(i))**: in the *field* `F_5`,
  `c=2,d=4,s=1,t=3` gives `c+d={1}`, `t∈c+s={3}`, but `d=4∉s+(−t)={3}`.
  Counterexample verified directly; there are exactly 9 such tuples in
  F₅. The refutation is correct (Claude cited the right instance). ✓
- **Value-swap route (3(iv)) quantifier correction**: my sweep shows
  (a) *every* premise pair has some `(g,m)` witness with `1∈g⊞m` (0/925
  exceptions — so existential closure is genuinely still open), and
  (b) a positive fraction of premise pairs have *some* closing-witness
  `g` for which the single-witness swap-step `0∈g⊞(−1)⊞(ab)^{⊞3}` fails
  (~19% under my all-witnesses convention; Claude's ~24% under the
  canonical-F3-witness convention). Either convention supports the
  corrected conclusion: *existence always holds; a fixed witness often
  fails; hence the swap route does not close (E).* This is exactly the
  over-statement the round-1 review flagged, now correctly restated. ✓
- **Zero-trap example** (`rem:zerotrap`): in `F_19/{±1}`, `x={8,11}`
  satisfies `x⊞x={0,{3,16}}`, `x=−x`, `−x∉x⊞x`; for `a={2,17},b={3,16}`
  (`a³=b³={8,11}`) the completing zero is realized at `{1,18}`, which is
  self-inverse and unpaired. I reproduced all of this exactly, and also
  confirmed `F_19/{±1}` satisfies *all* of (H1)–(H4) (no axiom
  violations). The example is tight and genuinely obstructs a
  paired-zero substitution argument. ✓
- **Permutation-tower collapse (route 2)**: verified the null-pair
  structure — for the 5-term permutation relation in `F_13/{±1}`, both
  `t` and `−t` (`t=c₁c₂c₃`) occur in the mixed block
  `(c₁c₂)^{⊞3}⊞(c₂c₃)^{⊞3}`. The collapse is real. ✓
- **Proof audit of Sections 1–3** (unchanged from round 1 apart from the
  elevation restatement): `lem:basic` (i)–(v), `lem:atoms` (A1)–(A3),
  `prop:degen`, `lem:collapse`, `cor:collapse`, `lem:scale`,
  `lem:towers`, `lem:prop` all still audit clean against (H1)–(H4). The
  new equivalence argument in `prob:elevation` is arithmetically correct
  (`λ³w=−ab`, etc.). The one new imprecision is a *notation* slip: the
  conclusion in `thm:main`’s conditional proof is written
  `X^{\bp3}⊞Y^{\bp3}⊞(−1)⊞(XY)⊞(XY)⊞(XY)` while `prob:elevation` uses
  element cubes `X³,Y³` — see Queued Q4. (Cosmetic only; the equivalence
  itself states it in element-cube form.) ✓
- **Git**: commit `b9b9925` matches the claimed diff; worktree clean
  (artifacts gitignored). ✓

## Mainline Gaps

### M1. AC-1 — free case still open; no proof progress this round (the only gap, still the whole mainline)
The named routes are settled, and correctly. But settling refutations is
the *removal* of dead ends, not *forward progress* toward the theorem. All
computational evidence (mine and Claude's) continues to indicate the answer
is "yes". What is missing this round — and what I now require for round 3
— is at least one **proved positive partial statement** that strictly
shrinks the open case (e.g. a new lemma from (H1)–(H4) closing a
structurally-defined subfamily, or a proved general reduction stronger than
the current conditional), OR an unconditionally proved weaker theorem that
still answers a substantive part. Refuting yet another candidate route
without adding a proved building block will again read as STALLED.

**Binding direction for Round 3 (ordered). Do these in order; prove, don't
refute, wherever possible.**
1. **Prove the Elevation Problem for a provably-large structural
   subfamily.** The zero-trap analysis shows the obstruction lives at
   self-inverse elements `x=−x` with `0∈x⊞x`. In `F_p/U` this requires
   `−1∈U`. Prove (E) *unconditionally* in the complementary case
   `−1∉U` (no self-inverse nonzero elements), by showing that when every
   nonzero element has `x≠−x`, a *paired* realization of
   `0∈a³⊞b³⊞(−1)⊞(ab)^{⊞3}` must exist. This is a clean dichotomy the
   document already half-builds; a proof here is a genuine theorem, not a
   refutation.
2. **If (1) resists, prove a *single-step elevation lemma*:** from
   `1∈a⊞b` derive the existence of *one* explicit `v∈(ab)^{⊞3}` with
   `0∈a³⊞b³⊞(−1)⊞v`, using the tower `lem:towers(i)` plus a *proved*
   replacement principle for the special value `−w∈P` (the exact step
   `rem:gap` flags as unlicensed). Attack the replacement principle
   head-on; prove it under any additional hypothesis you can then remove
   or discharge.
3. **Only after attempting (1) and (2)**, if both fail, produce a
   *complete classification of hyperfields in which the obstruction
   occurs* (the self-inverse/zero-trap family) and prove the theorem on
   its complement. State round-3 output as a theorem about the
   complement, not as more route autopsies.

## Blocking Side Issues
- None *new*. The blocker remains M1 (free case unproved). Restated as
  the round-3 ordered plan above.

## Queued Side Issues
- Q1. `bitlesson-selector` binary absent (informational). Unchanged.
- Q2. Git history retains superseded drafts (no action). Unchanged.
- Q3. (closed) The round-1 cosmetic items — delete-list strings and the
  redundant "conversely" sentence — were fixed this round; verified absent.
- Q4. **NEW (cosmetic, non-blocking)**: notation inconsistency between
  `prob:elevation` (element cubes `X³,Y³`) and the conditional conclusion
  in `thm:main` (`X^{\bp3}⊞Y^{\bp3}…`). Same intended relation, different
  superscript convention. Unify if a further editing round touches the
  text. Added to tracker Queued.

## Classification of Claude's own narrative (accuracy check)
- True: all four claim-groups (route (1) 1⊞1-saturation refuted; route (2)
  collapses; route (3) H4-collapse + Delta refuted; route (4) quantifier
  corrected) and the hypersum-vs-element-cube correction — I verified each.
- True and important: the computational data in `rem:honest(d)` is labelled as
  evidence, and no statement depends on it. AC-3 is respected.
- One labelling caveat (not a violation): `rem:honest(e)` proves its
  refuting instances "by routine verification ... left to the reader", yet
  the phrases "30 of the 55 computed models" / "about a quarter of these
  pairs" smuggle in counts that are *not* proved in the document. They are
  inside a Remark explicitly disclaimed as non-proof, which is acceptable;
  but note the document would be cleaner if those two counts were deleted
  and only the *proved instances* (F₅ counterexample; the F19 example)
  kept. Queued as part of Q4 hygiene; not required.
- Over-stated in the summary but not in the doc: "every claim ... 0
  exceptions in 846 tested pairs" and "205 of 846" — my independent
  conventions give different absolute numbers (925 pairs; ~5–19% by
  witness-counting convention), though every *qualitative* sign matches.
  The document's in-text claims (the qualitative ones) are the ones that
  matter and they are correct.

## One-line answer to the problem (for the record)
Still unknown/provisional: the element-cube Elevation Problem is verified
on every computed model (0 failures in my independent sweep up through
p ≤ 43, all subgroups; Claude reports the same to p ≤ 127) and is the
multivalued analogue of a true field identity, but no axiom-level proof
exists yet. The document now states the correct open problem (element
cubes) — a genuine fix this round — yet AC-1 requires that problem to be
*solved*, and it is not.

Mainline Progress Verdict: STALLED
