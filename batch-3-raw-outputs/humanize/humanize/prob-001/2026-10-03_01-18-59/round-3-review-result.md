# Round 3 Review Result — prob-001

Reviewer: moonshotai/Kimi-k3 (max effort), reviewing Round 3 commit
3b00c07 (worker "Claude" per the RLCR loop). Scope checked against
plan.md AC-1..AC-5, problem.tex (verbatim), round-3-prompt.md /
round-3-contract.md (Steps 3.1-3.4), the full solution.tex (read; the
changed Section-4 region — lem:sieve, lem:restrict, prop:vanish —
audited at proof level), the worker's round-3 summary, and the
round-3/goal tracker state.

Reviewer recompile: pdflatex twice, **0 errors, 0 undefined references,
15 pages** (limit 16); harmless hyperref PDF-string warnings only.
Greps: no `iffalse`, no "Stacks", no "same class", no TODO/hmm/wait.
Tree clean (round committed as 3b00c07).

## Part 1 — Verification of the Round-3 directive (Success Criteria 1-5)

| Criterion | Directive | Status |
|---|---|---|
| 1 (Step 3.1) | Step 1 asserts ONLY dead-sector coboundary hygiene; no false pin; Step 2 keeps/uses fold-image equality | **DONE-AND-STRONGER**: after sieve(i), z_f=0, so Step 2's conclusion 0=0 needs no substitution — the directive's harder display was never required. Step 1's (*) correctly asserts only coboundary-ness. Verified sound. |
| 2 (Step 3.2) | lem:sieve(i) re-proved via per-ray contractible strands; false single-pin deleted; sieve(ii) retained | **DONE**. New (i) proof verified line by line (fin.rays ✓, strand def ✓, differential-closedness ✓, identity transports via lem:nerve(i) Case A / lem:mixed(C1) ✓, lem:constcx ✗see M-5 below, disjoint union + repeated lem:subquot ✓, dead sector untouched ✓). sieve(ii) unchanged and previously verified. |
| 3 (Step 3.3) | Step 3 via lem:sieve(ii) + two-fold display (†) + kill of ẑ_K; floating parentheticals deleted; rank-one/P={0} by named references | **PARTIAL — mainline-still-open**: (a)/(b) done correctly (with the (†) display rigorously justifiable; see analysis below). (c) the final kill is a petitio principii + circularity (M-6 below): the worker flags it honestly, but the directive demanded forcing it transparently or falling back to AC-4 restatement. q-skippedcases part (d): done with named references (lem:const R_min=R_max=iB; lem:dead). |
| 4 | recompile clean ≤16pp | **DONE** (15 pp). |
| 5 | tracker update, commit, summary | **DONE** (round-3 Plan-Evolution row present; commit done; summary written). |

No regressions detected in Sections 2-3 on re-read of the audited
parts (plenary re-verification of those sections was done R0-R2 and
nothing changed there this round: git diff 38ee82a..3b00c07 touches
only lem:sieve onward).

## Part 1 (cont.) — Findings

### MAINLINE GAPS

**M-6 (AC-1; prop:vanish Step 3 final kill is unsound as written —
worker-flagged, reviewer-confirmed, with the fatal direction
pinpointed).** The "Then the constant itself dies" paragraph contains
two independent fractures:

(a) *Circular sheaf citation.* In this proposition b is GENERIC and
G_K := G_F|_{i(b) over i(P/K)} = G_{F_K} with F_K = F∘(quot of B_P),
so the D(K) hypothesis on the face slice closes by logic alone; but
the worker's sentence cites "Theorem thm:descent with T=i(P/K)" for
"the initial-object slice" — thm:descent applies to b=P (T=i(b)),
whose D-step is the INDUCTION TARGET (b arbitrary), hence circular as
cited. Strike the citation; the D(K) closure is the "F→F_K" functor
argument, which must be stated in its place.

(b) *The actual gap (fatal).* After D(K) and refinement, "what remains
on the slice is the single class ẑ_K carried by i(P/K)" — for q≥2,
that remaining class is the pinned value living in DEGREE ≥1 of the
restricted complex on the one-object K-exact strand, which by
lem:constcx HAS NO nonzero degree ≥0 ≥... i.e., any such class is a
COBOUNDARY within the slice; and — the decisive point — the residual
class after analogous "kills" in degrees ≥2 of the ambient cover is
zero on the nose within one cover, as the base-case computation
demonstrates (on the constant strand with minimum H, every cocycle
supported on it is ∂(its own contraction h), i.e., zero after
subtracting a coboundary INSIDE the same cover). The sentence as
written does not know whether it claims "ẑ_K is a coboundary on the
slice" (true, harmless) or "ẑ_K=0 in F(P/K)" (needs an injectivity
the text never establishes). (†) annihilates only the IMAGE
F(π_{K→P})(ẑ_K) in F(b_P); nothing in the document turns
image-annihilation into element-annihilation, and for q≥2 the element
need not be determined by its image (F is arbitrary). The paragraph
is NOT a proof; the worker's honest flag is upheld.

**M-7 (AC-1; structural: the document proves the f.g. case but the
question, per problem.tex, is unrestricted; AC-4's honest-diagnosis
branch is the only legitimately closeable outcome this round).**
Round-1 review ratified the "Scope hypothesis" as honest PROVIDED the
general case is described as obstructed with the two exact
obstructions named (f.p. of P→P/K; infinite face poset) — which the
document does (Scope paragraph, rem:nonfg). The R1/R2 tracker rows
accordingly describe AC-1 as "scope honest". Since NO round has
attempted or been directed to lift f.g., the theorem as literally
asked (arbitrary P) remains un-answered. The authoritative closure
for the deliverable is AC-4: state thm:main for f.g. P (proved, once
M-6 is fixed) + a Closing Remark for arbitrary P with the two
obstructions, general-case acyclicity reduced verbatim to a
bi-rated/saturation statement that no round claims, and the verdict
"not decided by this note". The template is in Part 4B below.

### BLOCKING SIDE ISSUES (on the mainline route)

**M-5 (lem:sieve(i) cites lem:constcx through a condition that
fails).** The proof says "by the constant-complex Lemma lem:constcx
with anchor H=f_r it is acyclic". lem:constcx's hypothesis requires a
differential-closed family on which EVERY piece receives a structure
map from the minimum H. The r-fold strand = {tuples containing f_r,
no other ray}: on the sub-family {f_r itself}, H=f_r is a minimum and
lem:constcx literally applies ✓. On tuples containing f_r AND iB:
f_r⊗iB and iB do NOT receive a structure map from f_r (f_r→iB exists
only at the B-level via B(f_r)=b_P→b, NOT in the slice A_P/b;
ker(f_r)=J=ker(iB) would force the putative structure map to an
ISOMORPHISM by lem:nervemaps, which it is not). The hypothesis fails.
The argument meant, and the reviewer's R2 directive prescribed, the
CONTRACTION notation (insert f_r in front, exactly the h of
lem:constcx's proof): for τ a strand tuple, (he)_τ := e_{(f_r,τ)}
(=0 on repetition), well-defined since f_r⊗τ̄ has kernel J
(lem:mixed(C1)) with identity transitions; ∂h+h∂=id on
strand-supported cochains — a SELF-CONTAINED two-line identity that
must be WRITTEN OUT (it is lem:constcx's display with H glued in
front; "internal adjoinability" is not a hypothesis of lem:constcx).
Fix: expand the one sentence into the two-line display, citing
lem:mixed(C1) and lem:nerve(i)-Case-A for the identity transports,
and do not cite lem:constcx. Two-line repair; mathematics unchanged.

**M-8 (THM-level dependency audit: the answer to the question on
i(b) NEVER exceeds degree 1 — this is the same observation as M-6(b)
and is the route the next round must take).** Work per-degree q with
prior degrees already closed; the residual after lem:sieve(i) +
sieve-support is the iB-K/J-constant strand with minimum iB; ANY
(q≥1)-cocycle supported on it is ∂ of its own contraction (the h
formula) — zero coboundary-inside-one-cover, q.e.d. This kills
sieve(ii), lem:restrict, (†), and the entire face induction in one
stroke (counterpart specialized at q=1 gives back collapse). The
worker declined to adopt this route in R3 on the ground that it
"abandons the executed review directive", but the R2 directive's OWN
fallback clause (Step 3.3's "Approved alternative ... choose ONE")
invites replacing the K-induction by a single three-level filter
{folds}<{K/J-constant residuum}; the specialization above IS that
alternative, at all faces at once. Next-round directive below.

### QUEUED SIDE ISSUES

- q-accounting: after M-8 lands, lem:filter will have NO remaining
  citations (lem:sieve(i) uses the explicit contraction; the old
  q-accounting rationale evaporates). Queue: delete lem:filter or
  cite it once for the (r-ray union) lem:subquot loop; non-blocking
  cosmetic decision.
- q-dead-sector: permanently moot on the M-8 route (no dead value at
  an ALTERNATING q≥2 tuple is ever needed at non-dead pieces; the
  values used are only the 0/face-vanishing hypotheses of the sieve).
  Close as WONTFIX once M-8 lands.
- q-skippedcases: CLOSED this round (named references given).
- Q-3 (rest), final typography pass: final round.
- q-scope-lifting (new): the general (non-f.g.) case is NOT claimed;
  if a later round wants it, the two obstructions (rem:nonfg) are the
  exact entry points. Explicitly out of scope; do NOT attempt.

## Part 2 — Goal Alignment Summary

AC-1: inner statement (f.g. P) blocked ONLY on M-6(b)/M-8 (last 3
sentences of prop:vanish) + M-5 (citation fracture, 2-line fix);
outer statement (arbitrary P) blocked on M-7 (AC-4 closure required).
AC-2: OK. AC-3: blocked on M-5/M-6 (citation-failures; the q-degree
inductive bookkeeping is never made precise as written). AC-4: **this
round must trigger its honest branch** (f.g. theorem + general-case
diagnosis; the counterexample route stays rejected — no
counterexample has ever been produced, and the R2 wrong-map analysis
stands ratified). AC-5: OK (15 pp, clean compile).

ACs: 2/5 fully addressed (AC-2, AC-5); AC-1/AC-3 blocked on the
final-kill fragment + sieve citation; AC-4 must fire the
honest-restatement clause for the non-f.g. case | Forgotten items: 0
| Unjustified deferrals: 0 (the worker flagged rather than deferred;
the review now converts the flag into the directive)

Tracker changes I (reviewer) am applying in goal-tracker.md: Plan
Evolution Log — new Round-3 review row (M-5..M-8; q-skippedcases
closed; q-dead-sector → wontfix-pending-M-8; AC-4-fg branch
authorized); B-8 stays PARTIALLY-resolved (sieve(i) fracture M-5
re-opened at citation level; sieve(ii) becomes unused-draft once
M-8 lands); q-restriction-lemma / q-accounting → closed-as-superseded
by M-8 once landed (the restriction lemma's only scheduled use was
the fragment being replaced); Active T2-R3 marked "partially — final
kill still open (M-6/M-8)"; new Queued item q-scope-lifting recorded
out of scope. The worker's implicit request to mark T2-R3 complete
is REJECTED (M-6 open), and its self-flagged "expect review scrutiny"
is confirmed as REQUIRED, not optional.

## Part 3 — Capability Map Summary

Capability anchor: N/A (plan.md has no feature/capability map) |
Dependency gaps: 0 | Scope drift: no (the round stayed on the
prop:vanish mainline; the only off-mainline paragraph — the
counterexample analysis — was NOT attempted, as directed)

## Part 4 — Directive for the next round (singular; execute as written)

Mainline objective: make prop:vanish a proof, by REPLACING the
K-induction fragment with the degree-inductive residuum calculation
(M-8), repairing the lem:sieve(i) citation (M-5), and closing the
document at AC-4's f.g. branch (M-7). All mathematics needed is
already in the document and reviewer-verified.

**Step A (M-5; 2-line surgical repair; do FIRST).** In
lem:sieve(i)'s proof replace the sentence "by the constant-complex
Lemma~\ref{lem:constcx} with anchor H=fr ... component on it is
∂w_r" by the contraction written out: define
(w_r)_σ := z_{(f_r,σ)} (zero on repetition; well-defined: every
σ-vertex has kernel ⊆ J on the r-strand, so f_r⊗σ̄ has kernel J by
lem:mixed(C1) and lem:nerve(i)-Case-A, and both structure maps
induce id); for a strand-supported degree-q cocycle verify
(∂w_r)_τ = z_τ − (w_r∂)_τ, hence z = ∂w_r on the strand
(display the two-term identity, copying lem:constcx's display);
note z−∂(Σ_r w_r) is supported off the fold terraces by
differential-closedness + disjointness (already present), and the
lem:subquot loop is unchanged. Remove the lem:constcx citation from
this proof.

**Step B (M-6/M-8; the real work; replaces prop:vanish Steps 1-4).**
Restructure prop:vanish as an explicit induction on the DEGREE q (the
old descending face induction is DELETED, and with it sieve(ii),
lem:restrict, and the (dagger) machinery): visibly induct on q,
assuming H^k(i(b'), G_{F'}) = 0 for 1 <= k <= q-1, every b' in B_P and
every presheaf F' (the induction is over all F, which is legitimate
because the hypotheses quantify over F = the given presheaf; for the
stages below the induction hypothesis is needed only in the explicit
places marked [*D-hyp*]).
  B1. Keep Step 1 (dead-sector hygiene) word-for-word; it is sound:
      after a common refinement (lem:sandwich), every value at a nerve
      piece mapping to D is a coboundary value with coefficients in
      F(b_P) (lem:dead + the contraction displayed in lem:constcx,
      anchored at H=D on the D-slice; cite the contraction, not the
      lemma's hypothesis-form).
  B2. Keep Step 2's opening exactly through "replace z by this
      representative" (sieve(i)). DELETE the rest of old Step 2: the
      distinct-ray availability clause, the (f,f')/(f,D)/(f',D) dead
      pairs, and the trivial 0=0 terminal-image sentence — none of it
      constraints anything anymore. (If the lem:dlemma citation is
      needed anywhere else, move it into lem:nerve(i) Case B, where it
      is actually proved and used.)
  B3 (residuum kill, replacing old Steps 3-4): with dead-hygiene
      bought in B1, refine once more so the following
      hold simultaneously (all refinements by lem:sandwich, all
      transfers by rem:transfer): (i) z vanishes on every tuple
      containing a kernel-J fold [B2]; (ii) the depth filtration
      (lem:depth) orders all remaining nerve pieces; (iii) SUB-STEP
      (depth induction, the verified sieve(ii) DISPLAY relocated to
      where its hypothesis holds): run descending depth induction on
      faces K. Hypothesis: z vanishes at every position of level
      strictly larger than K. For a K-exact position W, the chain
      W, i(P/K), iB has overlaps W otimes i(P/K) at level >= K
      (lem:nerve(ii), lem:mixed(C2)) and i(P/K) otimes iB at level K
      (lem:nerve(i) Case A (K=J clause... NO: lem:nerve(i) first
      clause with K the face in question gives Phi = K, and the
      iB-side overlap is lem:nerve(i)'s iB-case)). With strictly-larger
      values zero by hypothesis, the cocycle equation at the pair
      (W, i(P/K)) reads z_W = F(quot B(W) ->> P/K)-transport(z_{i(P/K)})
      and at the pair (i(P/K), iB) reads
      F(quot P/K ->> b)(z_{i(P/K)}) = z_{iB}; [*D-hyp*] marks that for
      q >= 2 the last two equations are value-level equalities in the
      stated groups — NO higher-vanishing is invoked. Descending all
      the way to K = J: every surviving non-dead value is a transport
      of the single value z_{iB}, i.e., z restricted to the residuum
      is a CONSTANT cocycle on the face-poset poset of pieces
      {iB, i(P/K)} with minimum iB and quotient transitions.
      (iv) SUB-STEP (residuum kill, zero on the nose within one cover):
      by lem:const (R_min = R_max = iB on the residuum family) the
      residuum restriction is the contraction-h coboundary elementwise:
      writing h as in lem:constcx's display with anchor iB, z = partial h
      on residuum tuples; extend h by zero off the residuum and subtract
      partial h; the dead-sector discrepancy thereby created at level-P
      pieces is exactly a coboundary value by B1's (*), already allowed
      to be nonzero-but-coboundary, hence absorbable by B1's w (one
      line: replace w by w plus the transported discrepancy; the
      algebra is the same F(b_P)-valued coboundary calculus).
      Conclusion: [z] = 0 in colim_R HH^q(R; G). This closes degree q
      and the induction.
  B4. DELETIONS: sieve(ii) statement and proof (it has been consumed
      verbatim into B3(iii), which is the one place its hypothesis is
      genuinely available); lem:restrict (statement and proof) — its
      only scheduled use was the deleted fragment; the "(dagger)"
      display and the "initial-object slice (Theorem thm:descent with
      T=i(P/K))" sentence; old Steps 3 and 4 headings. Rename
      lem:sieve to "Sieve: fold terraces" (drop "(i)"). Keep
      lem:dead, lem:const, lem:constcx, lem:subquot, lem:depth,
      rem:transfer, lem:sandwich, def:square, lem:filter (cited now by
      nothing — leave the statement in place, it costs one page-third
      and remains available; if the page budget tightens past 16,
      lem:filter is the first deletion — queue that as typography).
  B5. The degree-0 conclusion stays thm:descent + prop:adj with the
      existing no-circularity sentence. Explicitly state the q=1 base
      of the degree induction (it is B1-B4 with no [*D-hyp*]
      invocation needed at all — say so in one sentence).
  After editing: grep "\ref{lem:sieve}" counts are consistent; no
  dangling references to lem:restrict/sieve(ii); rem:transfer is
  cited at EVERY pullback sentence (B1's refinement, B3's opening
  refinement, the discrepancy-absorption line).

**Step C (M-7; AC-4 closure; LAST).** After thm:main-end's proof,
insert a short Closing Remark (≤ 12 lines): (1) theorem established
for finitely generated P; (2) problem.tex asks arbitrary P; the two
exact obstructions (quote rem:nonfg: f.p. of P→P/K can fail; the face
poset can be infinite, breaking the depth induction's finiteness and
the finitely-many-rays clause of the sieve); (3) the argument does
NOT decide the general case, and no counterexample is known to this
note; verdict: open with the named obstructions. Keep the title /
thm:main-scope sentence as they are (already honest), but make the
remark the definitive AC-4 record.

**Step D (closeout).** Recompile twice: 0 errors / 0 undefined refs /
≤16 pages (deletions free ~1 page; additions should land ≤ 15).
Grep: no "i(P/K))" left orphaned, no "restrict" label, rem:transfer
cited exactly where pullbacks occur. Tracker: T2-R3 → completed only
if Steps A-C are ALL landed; B-8 → resolved (sieve (i) repaired and
(ii) retired); M-6/M-5/M-7 → resolved; q-dead-sector → closed
(wontfix, superseded); q-restriction/q-accounting → closed
(superseded by B4); q-scope-lifting stays explicitly out of scope.
Commit + summary. If Step B3's residuum propagation cannot be written
soundly (the reviewer sees no obstruction: the deleted sieve(ii)
display IS the propagation), the ONLY fallback is AC-4-dishonest
retraction of prop:vanish's q>0 — which would collapse thm:main; do
NOT take it without exhausting B3.

## Verdict

Mainline Progress Verdict: ADVANCED
(lem:sieve(i) genuinely re-proved on the correct ray-by-ray footing
with the false M-2 pin deleted — a real mainline repair; dead-sector
hygiene correctly demoted to coboundary-ness; q-skippedcases closed;
wrong-map counterexample route definitively abandoned. The round's
residual is the LAST three sentences of the proof (M-6(b)) plus one
citation fracture (M-5) plus the pending AC-4 outer-scope closure
(M-7) — narrower than at any previous round, but AC-1/AC-4 remain
open, so the job is not complete.)

INCOMPLETE
