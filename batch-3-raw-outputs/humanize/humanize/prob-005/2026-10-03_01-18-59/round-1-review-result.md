# Round 1 — Review Result

## Verdict

**NOT COMPLETE.** The round-1 deliverable implements Option B faithfully:
the enumeration, the false cube-subgroup claim, and all proof-by-citation
content are gone; Section 1–3 proofs are clean; the free case is isolated
as a precisely stated Elevation Problem; no "yes" is asserted. All of
that is exactly what Option B prescribes, and I verified it (compile,
content, audits below). However, AC-1 is immutable and is **not met**:
the original question is answered only conditionally, with the
substantive (free) case left as an explicitly open problem. Per the
review protocol, a conditional theorem with the open core case is not
COMPLETE. Claude's own summary concedes this ("AC-1 is NOT met"; "The
reviewer may judge AC-1 unmet").

The downgrade is *provisionally* justified — Option A is legitimately
hard and several tempting sublemmas are genuinely false — but Claude's
"genuine effort" ledger has identifiable, concrete gaps, and at least one
of its claimed falsity results supports a *weaker* conclusion than
stated. Round 2 must attack the routes itemized below before Option B
can be accepted as final.

## Required summaries

```
ACs: 2 of 5 substantively addressed (AC-2 now essentially met; AC-5 met);
     AC-1 FAILS (free case open as the Elevation Problem — AC-1 negative
     test still triggers verbatim); AC-3 met for what IS in the document
     (no numerical evidence used as a proof step); AC-4 met (honest
     conditional statement, conjecture labelled as judgement not proof).
Forgotten items: 0
Unjustified deferrals: 1 (the Elevation Problem — currently deferred
     "until a new proof idea"; it is the mainline AC-1 objective and may
     not remain open while concrete untried routes exist)
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
Mainline Progress Verdict: STALLED
     (per the Option-A/B fork this round's result is admissible only if
     Option A truly resists after genuine effort; the effort, while broad,
     has identifiable gaps and one over-strong falsity claim — see M1)
```

## Verification of the round-1 claims (what I checked myself)

- **Compile**: `pdflatex` × 2 — exit 0, "Output written on solution.pdf
  (5 pages)", no undefined references. AC-5 met. ✓
- **Forbidden content**: the reviewer's delete-list is *mostly* absent,
  but two items remain in the PDF: "enumeration" line 11 (abstract:
  "no enumeration, computation, or external theorem is used as a proof
  step") and "exchange" line 263 (Remark 5.1(c): "a value-level exchange
  argument"). These are meta-statements, not proof steps, so they do not
  violate AC-1/AC-3; but the instruction list said "delete every
  occurrence". Trivial cleanup — Queued Q3.
- **Proof audit** (line by line, against (H1)–(H4) from Definition 1.1):
  - `lem:basic` (i)–(v): CORRECT (B3.2 fix in (iv) is now coherent).
  - `lem:atoms` (A1),(A2),(A3): CORRECT.
  - `prop:degen`: CORRECT (B3.3 typo gone).
  - `lem:collapse`, `cor:collapse`: CORRECT (the singleton-pairsum
    shortcut eq:star is valid; A2 → 1∈g⊞u step is fine).
  - `lem:scale`: CORRECT.
  - `lem:towers`, `lem:prop`: CORRECT.
  - Thm 2.1 stated only conditionally; equivalence argument in
    `prob:elevation` is numerically sound (I verified
    `λ³w = −ab` ⇒ `λ³(−w) = ab` on the stated scaling).
  - Disclaimers (abstract, Remark 4.3, Remark 5.1(c)) honestly demarcate
    proved from un-proved. AC-4 met.
- **Git**: commits match the claimed history; worktree clean except the
  freshly rebuilt artifacts (gitignored). ✓
- **Independent mathematical experiments** (own scripts in scratchpad,
  not used as proof content — only to adjudicate Option A's residual
  difficulty and Claude's claims):
  - Verified all (H1)–(H4) axioms for the order-4 hyperfields K_p =
    F_p/{cubes} for 11 primes p≡1 (mod 3), and confirmed the Elevation
    Problem holds on every free instance there (all such K_p are
    enriched at p≢1 mod 9, so those instances actually collapse;
    consistent with Claude's findings).
  - Confirmed the tempting sublemma **"cube of every value in a⊞b lies
    in a³⊞b³" is FALSE** (counterinstance in K₇: class 3 ∉ {0,3}).
    Likewise my own candidate "Frobenius/cube capture" route
    (ab·(a⊞b) ⊆ a³⊞b³) is FALSE in K₁₃ (image contains class 1 ∉
    {0,2,3}). These genuinely kill several naive closures; Claude's
    caution is partially warranted.
  - Verified the singleton-cancellation law (H4-collapse: if
    c⊞d = {1} then t∈c⊞T ⇒ d∈T) holds ∧ that the resulting sublemma
    premises are satisfied numerically in K₁₃ — but these remain
    **unproved in general**, hence unusable until Claude proves them.

## Mainline Gaps

### M1. AC-1: the free case is still open (the only remaining gap; it IS the mainline)

The deliverable proves the original problem only modulo the Elevation
Problem (E): `1∈a⊞b ⇒ 0∈a^{⊞3}⊞b^{⊞3}⊞(−1)⊞(ab)^{⊞3}`. Claude logged
six failed Option-A calculi and switched to Option B. That is permitted
*only* if Option A resists "after genuine effort". My independent
re-derivation found the following routes that were **not exhausted**, and
one falsity claim whose conclusion was over-stated. Until these are
closed (proved or shown impossible), Option B stays provisional and AC-1
unmet.

**Binding direction for Round 2 — prove the Elevation Problem by the
following ordered plan. Attempt (1) fully before (2), etc.; prove or
refute each named sublemma from (H1)–(H4) alone; document refutations.**

1. **Induction schemes on the doubles cubes (highest value, untried).**
   The extra cube copies in `a^{⊞3}` come from `1⊞1` and its translates.
   Claude's witness-family calculus #5 covered 82.6%; the residual 17.4%
   are precisely instances whose witness needs mixed
   `∑v_i ∈ (1⊞1)^{⊞3}` patterns. Define the saturation operator
   `Sat(S) := S ⊞ (1⊞1)` closure and seek an identity
   `a^{⊞3} ⊞ b^{⊞3} = ⋃_{v∈V(1⊞1)} (a·v)^{⊞3} ⊞ … ` — concretely:
   (a) prove the lemma `1 ∈ u ⊞ (-1) ⊞ (1⊞1)` whenever `u ∈ 1⊞1` (if true
       from (H1),(H4); refute otherwise), then
   (b) use (A1) with `c := -1` on membership `1 ∈ a⊞b` together with the
       doubles-induced identities `a^{⊞3} ⊇ a³ ⊞ (a·(1⊞1))^{…}` to
       *generate* the three missing `(ab)` terms one at a time. This is
       the one cube-injection mechanism calculi #1–#6 never used.
2. **Permutation-adjusted tower (✽✽).** Replace the 6-term tower
   `0 ∈ a⊞b⊞d⊞e⊞d⊞e` (which gives the bad `(ab)^{⊞3}⊞(−ab)^{⊞3}` tail)
   by the 5-term identity `0 ∈ a⊞b⊞c₁⊞c₂⊞c₃` with the multiset
   `{c₁,c₂,c₃} = {d,d,e}` (one permutation instead of two). Work out the
   resulting cube expansion: it yields exactly two mixed blocks
   `(c₁²c₂⊞c₁c₂²)` and `(c₂²c₃⊞c₂c₃²)` with tails `(c₁c₂)^{⊞3}` and
   `(c₂c₃)^{⊞3}` — mixed ab-sign terms instead of the monolithic
   self-cancelling tail of (✽). Combine with the cubing atoms (A2) to
   kill these tails *individually* (each tail now has a matched
   `0 ∈ c_i ⊞ c_j ⊞ …` relation). Claude's calculus #2 tried the
   uniform (✽) tail only; the permuted version changes the parity of the
   tail signs and was not tried.
3. **Prove the two conditional sublemmas, or refute them.** Both are
   numerically true on every verified model and, if proved, close (E):
   (i) *H4-collapse*: if `c⊞d = {1}` then `t ∈ c⊞T ⇒ d ∈ T` (proof idea:
       feed `t ∈ c⊞s`, `s∈T`, into (H4) applied to `1∈c⊞d`; track the
       canonical singleton), and
   (ii) *Delta condition*: `−g ⊞ z^{⊞3} ⊆ a^{⊞3} ⊞ b^{⊞3}` whenever
       `g ∈ a⊞b⊞d`. If (i) is provable, combine with towers (i),(ii) and
       the set-identity `(XY)^{⊞3} = (X²Y)^{⊞3} ⊞ (XY²)^{⊞3}` (true when
       `X²Y⊞XY² = {XY}`, i.e. the collapse case — generalize via (ii)).
   Item (ii) is the exact place K₁₃ kills the *simpler* variants; do not
   assume it — prove or refute.
4. **Correct Claude's calculus-#3 falsity quantifier.** The summary
   claims "`1∈g⊞m ⟹ 0∈g⊞(−1)⊞(ab)^{⊞3}` is numerically false in ~7% of
   canonical (F3-produced) witnesses, so the reviewer's suggested chain
   does NOT close either." The value-swap *at the level of a single
   arbitrary* `m∈M` may indeed fail; but (E) needs only the *existence*
   of one good `(g,m)`. Claude's own data: no instance of (E) failed —
   so existential closure is still open, and the "reviewer's chain is
   dead" conclusion was over-strong. Restate precisely in the doc.

If — and only if — every item above is genuinely proved impossible, with
each refutation recorded as a precise mathematical statement (as round 1
began doing), the Option-B verdict may stand in a later round. That bar
is not yet met.

## Blocking Side Issues

- None *new*. The existing blocker (free case unproved) is restated as
  M1 and is the sole mainline item.

## Queued Side Issues

- Q1. `bitlesson-selector` binary absent (informational; bitlesson.md
  read directly). Unchanged.
- Q2. Git history retains the superseded round-0 draft (no action).
- Q3. **Editorial** (AC-3/AC-2 hygiene, not AC-1): the PDF still
  contains the strings "enumeration" (abstract) and "exchange" (Remark
  5.1(c)); the round-0 reviewer's delete-list said "delete every
  occurrence". Since they appear only in meta-statements, this is
  cosmetic; fix in round 2 pass with no other content change. Remark
  5.1(c) also asserts the field identity as "the corresponding
  assertion holds" — fine as context, but ensure it is visibly labelled
  as motivation, not as a theorem invoked.

## Classification of Claude's own narrative (accuracy check)

- True: Option A via the six listed calculi failed; enumeration/false
  claims fully excised; proofs present are correct; verdict not
  over-claimed (no "yes"); AC-1 explicitly conceded unmet; "Option B was
  implemented exactly as prescribed."
- Over-stated: "the reviewer's suggested chain in Option A does NOT
  close either" (see M1.4 — false at single-witness level, unproven at
  existential level).
- Imprecise: "proven equivalent there to the original problem in the
  free case" — the equivalence is *per instance* under the scaling
  λ = −z⁻¹, and an affirmative answer to (E) for the scaled pair does
  yield the free case, so the claim is substantively fine, but the doc's
  "conversely" sentence in `prob:elevation` ("(E) with inputs … and
  scaling back yields the free case") is the same direction twice; tidy
  wording in round 2 (Queued, cosmetic).

## One-line answer to the problem (for the record)

Unknown/provisional: the assertion is very likely true (consistent with
all verified models and with the field identity), but as of this round
there is no axiom-level proof of the free case; the document honestly
says so. Acceptance of Option B as *final* requires the Round-2 routes
above to be exhausted and their refutations written down.

Mainline Progress Verdict: STALLED
