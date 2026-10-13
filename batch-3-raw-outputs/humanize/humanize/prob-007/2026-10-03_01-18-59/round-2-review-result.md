# Round 2 Review Result

## Verdict

Mainline Progress Verdict: ADVANCED (one gap newly surfaced; see below)

The round executed the contract faithfully on its **text-editing** items:
every discrete residue fix from the round-2 contract is present and
correct, the manuscript now compiles cleanly (verified independently, 0
errors / 0 undefined refs / 11 pages <= 16, AC-5 holds), and the entire
group-theoretic component analysis — which I re-derived from scratch and
confirm is **mathematically correct** — is now consistently stated.

But the round leaves **one unequivocal false statement** in
`lem:descend` (a proof that cites itself, circular, R1-F1(d)), and —
decisively for the completed-vs-stalled call — it **inherits from
round 0 a structural over-commitment that no round has ever repaired**:
`lem:sheets` writes the displayed equality `pi_0(D_f) = H\PMCG(B)` and
`thm:components` asserts `#pi_0(D_f) = [PMCG(B):H]`, while the
argument derives only that `D_f` is *a union of full cosets of H*.
"No selected coset is empty" (e.g. a fiber-surjectivity statement) is
never proved. The headline exact component count is therefore an
assertion, not a theorem — a defeat on AC-1's positive test ("a
specialist can verify line by line") and AC-3's negative test
("consistency of quantifiers"). This is the last remaining logical hole;
it was introduced in round 0, and rounds 0→1→2 each advanced past it
without fixing it. The trajectory is now zeroing in on the genuine
obstruction, so the mainline verdict is ADVANCED but not COMPLETE.

The most important reassurance I can give the next agent: **the "no
infinite orbit" conclusion (AC-4) appears robust to the repair** (see
Finding 3), so fixing Finding 1 should *strengthen*, not overturn, the
paper's verdict.

## Goal Alignment Summary

```
ACs: 2/5 fully met (AC-2, AC-5); AC-4 direction correct and appears
robust (see Finding 3); AC-1, AC-3 blocked by one inherited over-
commitment (component-count equality asserted, not proved) + one
self-referencing proof (circular). | Forgotten items: 0 |
Unjustified deferrals: 0
```

Capability Alignment Summary:
```
Capability anchor: N/A (plan has no Feature/Capability Map — correctly
recorded) | Dependency gaps: 0 | Scope drift: no
```

## What I verified independently (not trusting the worker's summary)

1. **Compile (AC-5)**: clean-room `pdflatex solution.tex` ×2 from a
   bare directory, exit 0 both passes, 0 undefined references, 0 hard
   errors, 11 pages <= 16. Confirmed.

2. **Value/census algebra (R1-F1(d) signs)**: exact rational arithmetic
   (my own `fractions` script). The four corrected table values are all
   right: `s0(1/2) = -1/4`, `s0(-1) = 5`, `s2(1) = 1`, `s2(-1) = -1`,
   `s3(1/2) = 1/4`, `s3(-1) = 7`, all `s_i(0) = ±1`. Ten punctures
   distinct (discriminants 5, 5, -3; no root in {0, 1/2, 1}). The
   exact-square identities (`R = -s0²/D`, `R-1 = -s2²/D`, `R-λ =
   -s3²/D`) re-verified as exact polynomial identities on samples.
   **The round-2 worker was correct**, and the round-1 *reviewer's* four
   claimed sign errors on the `s2` values were themselves wrong (the
   round-1 text had `s2(1/2)=-1/4, s2(1)=1, s2(-1)=-1` all correct); I
   accept the round-2 summary's correction. Only `s0(1/2) = -1/4` truly
   needed fixing, and it is now fixed.

3. **Residue sweep (R1-F1/R1-F2)**: grep confirms absence of
   "between 2 and 8", "Schreier", "x_0'", "either form", "t^a/x_1^b",
   "v-strand", "conjugation by", "invariant under conjugation", and the
   broken `u_3x_1)x_1^{-1}u_3` fragment. Presence of `2<=...<=4` bound
   everywhere (lines 186/200/872/909/915), `u_3` defined in setup
   (§1.2), and the parity table in `cor:Hstruct`(iii).

4. **Group theory (load-bearing, re-derived from scratch)**:
   (a) `H∩K ⊆ F = ch_0^{-1}(2Z)∩ch_2^{-1}(2Z)`: each of the seven
   census generators is a pure braid (5 strands = v and the four cycle
   pts); the push `x_i` linking v↔p_i has `(ch0,ch2)` exactly as
   tabulated; all values are even; `(ch0,ch2)` is a homomorphism on K.
   Hence H∩K ⊆ F, `[K:F]=4`, `[PMCG(B):H] = [K:H∩K] <= 4`. CORRECT.
   (b) `x_2 ∉ H`: `ch_2(x_2) = 1` odd ⇒ not in F ⇒ not in H∩K; `x_2∈K`,
   so `x_2 ∉ H`. CORRECT. (c) `x_2² ∈ H`: census (ii) — `R-1 = -s2²/D`
   has order exactly 2 at each `s2`-root (simple zero, `D(c)≠0`,
   verified), so `v` winds twice about `p2`, giving `T_{p2,v}² = x_2²`.
   CORRECT. (d) Projection onto PMCG(A): images `u_0, u_2` generate the
   free `F_2` (the `u_3` push of p_3 about p_1 = `T_{p0,p2}` collapses
   to `(u_0u_2)^{-1}` on the 4-punctured sphere; census (vii)
   establishes it). So `H` surjects PMCG(A). CORRECT. Hence
   `2 <= [PMCG(B):H] <= 4`, `T_γ²` fixes every H-component, `T_γ`
   acts with orbits of size ≤ 2 on the **sheet set** `H\PMCG(B)` — all
   independently confirmed.

   **Consequence of (4)**: the entire group-theoretic edifice
   (component count of the *covering* `π^{-1}(M_f)`, twist
   transitivity/orbits on that sheet set) is **sound**. The only
   unproved step is the *identification* of that sheet set with the
   actual component set `pi_0(D_f)` (Finding 1).

---

## FINDING 1 (Mainline Gap — BLOCKING): the equality
## `pi_0(D_f) = H\PMCG(B)` in `lem:sheets`(c), hence `#pi_0 =
## [PMCG(B):H]` in `thm:components`, asserts but never proves that the
## equalizer picks up **all** sheets of `π^{-1}(M_f)`

**Where:** `lem:sheets` (statement (c), the displayed
`pi_0(D_f) ≅ H\PMCG(B)`, line ~645; and the proof's (c) paragraph,
line ~663); downstream `thm:components` (line ~197, "the number of
components is `[PMCG(B):H]`"), `cor:index` (line ~914, "π_0(D_f) is a
finite set of `[PMCG(B):H]` elements"), and `cor:answer`'s
`2 <= #pi_0 <= 4`.

**What is wrong:** The proof of (c) establishes only:
> components of `π^{-1}(M_f)` are `H\PMCG(B)`; the equalizer selects a
> right-invariant subset — a union of full cosets of H.

That is correct. But the statement and the headline results then
identify *this union* with **all** cosets `H\PMCG(B)`. The missing
step is: **every sheet of the covering `π^{-1}(M_f)` lies in D_f**,
i.e. the two maps `f^*, i_* : Teich(B) → Teich(A)` coincide on *every*
component over `M_f`, not just on the one through `τ0`. Nothing in the
paper proves that. Covering theory gives only
`pi_0(D_f) ↔ {those cosets Hσ with f^*=i_* on the σ-sheet}`; a priori
this can be a *proper, nonempty* right-invariant subset. As written,
`thm:components`'s exact count `[PMCG(B):H]` and the displayed
bijection are **overstatements** — precisely the AC-1/AC-3 failure
(a specialist cannot verify the equality line by line because the
"all cosets" quantifier is discharged nowhere).

This is **not** the round-1/2 text residue; it is a *round-0 framing
gap* that has been carried, unfixed, across all three rounds. It was
flagged in passing in my round-1 addendum ("sweep that no displayed
equality `D_f = π^{-1}(M_f)` survives next to the proved
`D_f ⊆ π^{-1}(M_f)`") but never allocated as a repair task, and the
round-2 contract did not name it. I am now surfacing it as the primary
blocking finding.

**Required fix (singular directive — implement exactly this).** Prove
the equalizer is the whole covering, then the equality is free. The
cleanest available argument uses only facts already in the paper:

1. `π^{-1}(M_f) → M_f` has, over a fiber point, sheets indexed by
   `H\PMCG(B)`; the **finiteness** `[PMCG(B):H] = [K:H∩K] <= 4` is
   already proved (my check 4). So `π^{-1}(M_f)` has finitely many
   components: call the number `n <= 4`.
2. Show **`i_* : π^{-1}(M_f) → Teich(A)` has degree ≥ n over a generic
   value** (equivalently, all n sheets give distinct markings /
   distinct points of `Teich(A)` over the base point `i_*(τ0)`): hold
   the A-configuration fixed at the base value and let `v` vary over
   `M_f`; the forgetful fiber `M_f → π_1(A)-orbit` is a covering, and
   the monodromy `H` being transitive on `H\PMCG(B)` means the fiber of
   `i_*` over `i_*(τ0)` has exactly `n` points, one per sheet. (This is
   the point that needs *one careful sentence* — the fiber count at the
   base point, using that the sheets are permuted simply-transitively
   by `H\PMCG(B)`, so there are exactly `n` distinct lifts of the fixed
   A-structure to a B-structure over `M_f`.)
3. Since `D_f = {f^* = i_*} ⊂ π^{-1}(M_f)` is a *closed* subvariety
   (both `f^*`, `i_*` holomorphic; `Teich(A)` Hausdorff) that contains
   the sheet through `τ0` ("`τ0 ∈ D_f`" is asserted in lem:sheets's
   proof — **this membership itself must be justified; see note**), and
   `π^{-1}(M_f)` has *finitely many* components each mapping onto the
   same connected `M_f` with the fiber fully accounted for by sheet
   count, the equalizer — being a union of whole components that agrees
   with the full fiber degree — must be all of `π^{-1}(M_f)`.

   **Note on the hidden step:** the base membership `τ0 = [id] ∈ D_f`
   (i.e. `f^*([id]) = i_*([id])`, the tautology that the identity
   marking is fixed by the pullback = identity on the *same* rigid map
   `f`) is used implicitly everywhere and should be stated as a
   one-line lemma (it is `X_f = Y_f` at the base point for the
   *original* map, the starting hypothesis of the whole problem).

   If, on inspection, step 2's fiber count does **not** force all
   sheets into `D_f`, then the honest repair is the **weakening**:
   replace every `pi_0(D_f) = H\PMCG(B)` by
   `pi_0(D_f) ⊆ H\PMCG(B)` (right-invariant sub-union), `#pi_0(D_f)
   <= [PMCG(B):H]`, and recompute the *lower* bound (the
   lower bound `>= 2` currently comes from `x_2 ∉ H` on the *sheet*
   set, which only bounds the number of *sheets*, not of *selected*
   components — so a weakening would need a separate `>= 2` argument,
   e.g. that `T_γ` acts fixed-point-freely and pairs up the selected
   components). Either way, **do not keep the current asserted
   equality.**

4. Track through `cor:index` and `cor:answer` so that the count
   matches whichever of (all-sheets / sub-union) is proved.

## FINDING 2 (Mainline Gap — BLOCKING, R1-F1(d)): `lem:descend`'s proof
## is circular — it cites itself twice

**Where:** `lem:descend` (label `lem:descend`, line ~466) proof:
- line ~491: "computed exactly as in the proof of
  Lemma~\ref{lem:descend}", and
- line ~529: "so by Lemma~\ref{lem:descend} the descended twist on A is
  trivial",
both inside the proof **of** `lem:descend`.

**Why blocking:** This is a literal self-citation — a proof that rests
on its own conclusion, an unambiguous AC-1/AC-3 defect (it was
explicitly itemized in round-1 Finding 1(d) and re-listed in the
round-2 contract's success criteria as the "proof of Lemma lem:descend
self-reference" cleanup). The statement of `lem:descend` gives rise to
an actual circular dependency, not merely an awkward cross-reference.

**Required fix (singular directive):** The first citation (line 491)
means `prop:preimage` (the `{p2,v}` model computation) — replace
"the proof of Lemma~\ref{lem:descend}" by
"Proposition~\ref{prop:preimage}", since that is where the disc/branch
computation is actually done. The second (line 529) should not invoke
the lemma mid-proof; the correct citation for "descended twist trivial
when the branch side holds ≤ 1 point of A" is the *definition*
`def:descend` (peripheral ambiguity invisible on A) together with
`thm:halflift` (the d=2 annulus half-twist). Reword to
"...contains at most one point of A, so by the definition of the
descended class (Definition~\ref{def:descend}) the factor on A is
peripheral, hence trivial: Ψ(x_i^{∘2}) = e". After the edit, grep for
`Lemma~\ref{lem:descend}` and confirm it appears **only** in the
statement label and in *later* results, never inside its own proof.

## FINDING 3 (reassurance, not a task): the AC-4 "no infinite orbit"
## verdict appears robust to the Finding-1 repair

I checked the worst case. If the Finding-1 repair reveals that `D_f`
selects a *proper* sub-union of the sheet set, the following are still
rue:
- `T_γ² ∈ E_f` preserves `D_f` globally (`thm:halflift`, solid);
- every essential twist about a non-γ separating curve descends to a
  non-trivial element of PMCG(A) of infinite order, so **no** odd or
  non-squared power preserves any component (`prop:contenttable`,
  solid);
- `T_γ` pairs up the sheet set `H\PMCG(B)` with no fixed sheet (orbit
  size exactly 2, since `x_2 ∉ H`, `x_2² ∈ H`, and `ch_2`
  conjugacy-invariant — my check 4). Any chosen sub-union of *paired*
  sheets has `T_γ`-orbits of size ≤ 2.
Hence **no mapping class has an infinite orbit on `pi_0(D_f)`**, whether
or not all sheets are selected. So the paper's headline AC-4 conclusion
should *survive* the Finding-1 fix — the fix makes the component count
honest, it does not endanger the orbit conclusion. (Caveat: this is my
assessment of robustness; the new round must re-derive the exact count
after the fix, and must NOT assume the orbit conclusion is unaffected
without redoing the `<= 4` bound on the now-honest selection.)

## FINDING 4 (Queued Side Issue — must not take over next round)

- **(dangling no-fixed-point logic in `cor:index`)** — the sentence
  "`x_2` acts as a fixed-point-free involution up to cosets ... `Hg =
  Hg x_2` would give `g x_2 g^{-1} ∈ H ∩ K` ... `ch_2` is
  conjugacy-invariant on PMCG(B)" is correct **on the sheet set** but
  must be re-read against the honest (sub-union) component set after
  Finding 1; keep it queued, do not pre-empt the structural fix.
- The exact count `pi_0(D_f) ∈ {2,4}` remains **open and deliberately
  unpursued** (unused by every theorem once Finding 1 is honestly
  weakened, and untouched by the orbit verdict). Do NOT spend the next
  round pinning it down.
- `prop:contenttable`(b)'s "none of the conjugates of `H` contains
  `T_δ^{∘m}` with descended class trivial" is asserted, not shown; it
  is currently *only* used in the proof of (b), which the
  essential-twist argument already covers. Either prove the conjugacy
  clause or delete it as redundant (it is not load-bearing — queued,
  not blocking).

## Plan / AC bookkeeping

- The AC-4 route is legitimate, in-scope (immutable plan AC-4 licenses
  a rigorous disproof of the posed infinite-orbit clause), and — per
  Finding 3 — robustly correct in direction. Not an unjustified
  deferral; `Explicitly Deferred` is empty, correctly.
- No tasks were dropped (forgotten items = 0). No `FUT-*`/Future-Work
  gates anything.
- The round-2 contract's *text* success criteria are met, but the
  contract itself **missed** the round-0 structural gap (Finding 1); I
  am superseding criteria 1/4 by promoting Finding 1 to a blocking
  mainline task for round 3.
- Tracker: I corrected structural corruption in the MUTABLE log (three
  Plan-Evolution rows had been concatenated into a single row because
  the empty `Explicitly Deferred` table below them had no data row to
  stop a Markdown merge) and added the Finding-1/2 blocking row and the
  Finding-4 queued row. IMMUTABLE SECTION untouched. See "Goal Tracker
  updates performed" below.

## Classification of findings

- **Mainline Gaps (plan-derived AC work missing/incomplete):**
  FINDING 1 (component-count equality asserted, not proved — round-0
  heritage, now blocking) and FINDING 2 (circular self-proof in
  `lem:descend`, R1-F1(d) unfixed). Both directly gate AC-1 / AC-3.
- **Blocking Side Issues:** none beyond the two mainline gaps — the
  round's other residue items (signs, fragments, `u_3` hoist, conjugacy
  clause, `H=<7 gens>`) are all genuinely resolved.
- **Queued Side Issues:** FINDING 4 (re-read no-fixed-point argument
  post-Finding-1; leave exact count {2,4} alone; prove-or-delete the
  redundant `prop:contenttable`(b) conjugacy clause).

## Goal Tracker updates performed by this review

Edited only the MUTABLE SECTION of `goal-tracker.md`:
- **Plan Evolution Log:** separated the three run-on round-0/round-1/
  round-1(review) rows that had merged into one malformed row (root
  cause: the empty `Explicitly Deferred` table had no data row, so a
  Markdown table continued across the heading boundary); restored them
  as distinct rows.
- **Explicitly Deferred:** added the required `| — | — | — | — | — |`
  "no deferrals" data row so future edits cannot re-trigger the merge.
- **Blocking Side Issues:** marked R1-F1(a),(b),(c) and R1-F2 **RESOLVED
  (round 2)** with evidence; added new row for **R2-F1** (Finding 1,
  component-count equality unproved, round-0 heritage) and kept
  **R1-F1(d)** open but narrowed to the residual circular-citation item
  (signs/fragments/`u_3`/conjugacy all now fixed).
- **Queued Side Issues:** added the Finding-4 rows (no-fixed-point
  re-read; exact count stays unpursued; prove-or-delete redundant
  conjugacy clause in `prop:contenttable`(b)).
- **Plan Evolution Log (round 2 review):** recorded that R1-F1/R1-F2
  text residue is fixed in substance, but a round-0 structural gap —
  the unproved "equalizer = all sheets" step in `lem:sheets`(c) —
  surfaced and is now the sole mainline block, promoting it to round-3.

## What the next round must do (in order, all in `solution.tex`)

1. **Finding 1 (primary):** repair `lem:sheets`(c) per the directive —
   either prove the equalizer is all sheets (fiber-count/`n<=4`
   argument, with the one-line base-membership `τ0 ∈ D_f` stated as a
   lemma), or weaken `pi_0(D_f) = H\PMCG(B)` to a right-invariant
   sub-union `⊆ H\PMCG(B)` and re-derive `2 <= #pi_0` and the orbit
   statements on the honest selection. Track through `thm:components`,
   `cor:index`, `cor:answer`.
2. **Finding 2 (residual R1-F1(d)):** break the self-citation in
   `lem:descend`'s proof (line 491 → `prop:preimage`; line 529 →
   `def:descend`/`thm:halflift`), then grep to confirm no
   `Lemma~\ref{lem:descend}` inside its own proof.
3. Re-run `pdflatex` ×2 (0 errors / 0 undefined refs / ≤ 16 pages) and
   re-verify the `2 <= ... <= 4` display chain against whichever of
   (all-sheets / sub-union) step 1 proves.
4. If — and only if — step 1 selects a *proper* sub-union, re-establish
   the no-infinite-orbit verdict on the honest component set (expect it
   to survive per Finding 3, but re-prove, do not assume, the orbit
   bound).

NOT COMPLETE.
