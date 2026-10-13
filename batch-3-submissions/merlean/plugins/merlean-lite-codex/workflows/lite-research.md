Read `<PLUGIN_ROOT>/workflows/common.md` and the inherited provider adapter first.
Use the entrypoint's `<PLUGIN_ROOT>`; this internal playbook is not a public skill.
The shared scope, persistence, worker, and model-capacity rules govern this procedure.

# lite-research — MerLean-lite: NL-first, Lean at the weakest links

Input: an informal question. Output: a **graded resolution** — a natural-language proof (or
refutation) whose every step carries evidence: debate verdict, numerical support, and — for
the steps that stayed uncertain — a targeted Lean certificate. Speed is a design goal:
most of the run is thinking, debating, and running small Python experiments, not compiling.

**Why this mode exists.** Full formalization at every step is a strong filter and an expensive
way to discover the mathematics. Lite develops the natural-language argument first, with an
explicit ledger that exposes each inference. The decisive progress often comes from a candidate
whose representation reduces the problem's complexity. lite-research therefore (a) sustains the
best current candidate across local repairs, (b) gives each revision to a fresh adversarial review
context, (c) opens representation breadth when evidence says the candidate is absent or stalled,
and (d) reserves Lean for the steps where those filters cannot reach a verdict. Lite is the
exploration mode; explicit MerLean `-heavy` handles full certification.

**The five pillars:**
1. **NL FIRST, LEAN LAST** — no Lean anchor, no formalization phase. The primary artifact
   is the step ledger (§L). Lean fires only through the §L3 triage gate.
2. **SUSTAIN THE BEST CANDIDATE** — one actor keeps the route's context and progress, names
   its representation and develops a complete ledger. Repair the earliest material defect
   locally while the candidate improves; do not restart discovery merely to create breadth.
3. **FRESH ADVERSARY, PERSISTENT ACTOR** — after each revision, a fresh substantive reviewer
   attacks the exact ledger version and identifies the first substantive invalid or missing
   inference. Known findings remain visible. A step is *accepted* only after the required
   review, targeted checks and final comprehensive validation leave no live objection.
4. **EXPERIMENT EVERYTHING TESTABLE** — every step with computational content gets a small
   Python probe (random instances, boundary cases, counterexample search) via `explore`.
   Sampling never proves; exhaustive exact computations can close finite claims when their
   coverage, arithmetic, implementation and interpretation are independently checked.
5. **VERDICTS ARE EVIDENCE-BASED** — direction pivots only on independently verified
   witnesses (same gate as auto-research §B6); acceptance/refutation of a step always
   records *why*. Fully autonomous: never ask the user; decide, document, bank.

## Inputs
- `QUESTION` — the informal question/conjecture, verbatim (required).
- `QUESTION_NAME` — optional CamelCase name; propose one if omitted.
- `LIB_DIR` — optional Lean workspace (lakefile dir with Mathlib). Needed ONLY if §L3
  fires; without one, triaged steps are marked `needs-lean (no workspace)` and the run
  still completes at BRONZE.
- `SOURCE` — optional supporting material.
- `ROUTES` (default 2) — maximum fallback route pitches to open when the evidence triggers
  representation breadth; it does not require launching routes up front or in parallel.
- `DEBATE_ROUNDS` — optional explicit repair-round limit. Without one, continue a productive
  candidate within the user's authorization and actual resource/host limits; never infer
  mathematical acceptance from reaching a limit.

**Derived:** `DATA_DIR` = `<QuestionName>_lite/` (next to `LIB_DIR` if given, else cwd) —
holds `ledger.md` (§L), route pitches, experiment scripts/outputs, Lean certificates.
**Memory:** if the plan graph runtime is initialized (`.venv` + key), bank Notes as in
auto-research §M; otherwise `DATA_DIR/ledger.md` and `DATA_DIR/notes.md` ARE the memory —
same banking discipline, flat files. lite-research must run with zero setup.
**Failure log** (plugin `AGENTS.md` convention): append one short entry — date, one-line
mistake, evidence pointer, `confirmed`/`likely`/`transient?` tag — to
`DATA_DIR/failure-log.md` on every route kill, upheld fatal objection, exhausted debate,
failed certificate, or infra failure that ate a dispatch; read it before re-attempting an
approach that failed before. Subagents report failures upward; you write every entry.
**Bare-run adaptations (no `.venv` / plan store / lean-lsp):** tell every subagent in its
dispatch prompt: use `python3` directly; skip all plan-graph CLI steps (`graph_sync: n/a`); use
the build-command fallback for Lean diagnostics. Certificates compile against `LIB_DIR`
with the copy-in pattern: `cd LIB_DIR && cp <cert> ./Tmp_<name>.lean && lake env lean
Tmp_<name>.lean; rm Tmp_<name>.lean` (lake resolves imports relative to the workspace; a
clean run prints nothing; never `lake update`, never build the whole workspace).
**Resume, don't restart:** existing `DATA_DIR` ⇒ read `ledger.md` + `notes.md`, rejoin.

## Progress reporting
```
▶ <phase>            · <step> …          ✓ <good outcome>       ✗ <problem> → <action>
⇄ <route opened/killed/selected (+why)>  ⚔ <attack round: objections raised/survived>
🔬 <experiment: what → verdict>           ⚖ <step verdict change>   ⛏ <Lean certificate event>
```

## §Roles — five subagents, each at its moment
- **`route-scout`** (fallback) — pitches ONE high-level route: representation, skeleton,
  predicted weakest step, kill-test. Use distinct angles only when §L1's evidence triggers
  alternative search; `ROUTES` is a budget, not a launch quota.
- **`nl-prover`** (persistent proof actor) — develops the best current route into a full
  step ledger (§L), then resumes the same context to repair contested steps.
- **`skeptic`** (fresh context after each revision) — attacks the exact ledger version:
  gaps, circularity, quantifier slips, wrong constants, hidden assumptions, false lemmas.
  It focuses repair on the first material invalid or missing inference while preserving all
  known live findings; §L4 still requires a comprehensive composition review.
- **`explore`** (reuse, unchanged) — numerical probes (L0 direction, L2 step tests,
  witness verification). Its reliability rules (independent witness re-check, sampling ≠
  enumeration) are load-bearing here; numerical support is not mathematical closure.
- **`compile-fix`** (reuse, targeted mode) — proves ONE step-certificate file (§L3);
  `AXIOM_POLICY=strict` still (the "axioms" are hypotheses in the statement, not `axiom`).
Fleet: obey the available host slots; only compile-fix jobs are RAM-gated (auto-research §R
rules). Do not fill spare slots with redundant scouts or reviewers. On GPT, main, proof actor
and substantive reviewer default to `gpt-6-astra`; bounded execution defaults to
`gpt-6.1-sol`. Astra supplies Sol the exact goal, hypotheses, context, file scope, acceptance
checks and useful tentative ideas; those ideas are descriptive and rejectable, and Sol may
replace them within the fixed task boundaries. Sol's output is evidence for later Astra review,
never acceptance by itself. Claude uses the models in its inherited adapter, and every explicit
provider/model override remains in force.

## §L The step ledger — the primary artifact
`DATA_DIR/ledger.md`, one table per route. One row per step:
```
S<k> | claim (self-contained, quantifiers explicit) | uses: S<i>,S<j> | class | status | evidence | assumptions-added
```
- **class**: `ROUTINE` (standard technique, would be an exercise; cite the standard fact) /
  `COMPUTATION` (finite check or calculation — machine-checkable in principle) /
  `NOVEL` (the route's real content — new object, new inequality, the representation move) /
  `CITED` (a published result used as-is — see the citation gate below) /
  `ASSUMED` (an original L0 hypothesis, or an explicitly open residual).
- **HYPOTHESIS FIREWALL.** `ASSUMED` is closing evidence only when the clause occurs in
  the L0 problem dossier. A premise introduced later is `open-residual`: it cannot close
  the requested theorem and must never be styled a lemma or theorem. Every row's
  `assumptions-added` cell is empty or maps each premise to an earlier `DERIVED`/`CITED`
  row. Flatten theorem binders and proposition-valued structure fields transitively.
  A premise equivalent to, or stronger than, the row or final conclusion is fatal.
- **CLASS-VS-CARRIER GATE.** A claim about a distinguished element or obstruction class
  may not be replaced by `Subsingleton`/`∀ x` collapse of its carrier, `IsEmpty`, or a
  zero/toy model unless the stronger fact is independently derived and proved true for
  the intended object.
- **GOAL-PATH / INTENDED-BINDING GATE.** Freeze a separate goal contract containing the
  exact research question, its hashed source, intended objects, answer criterion, and goal
  theorem faces. Classify each proposed root as `settles_goal`, `sufficient_milestone`,
  `necessary_milestone`, `supporting`, or `terminal`, and record the logical direction and
  an audited consumer path ending at a goal face. Only the first three classifications may
  claim `settled` or `conditional_advance`; a supporting conditional theorem is not thereby
  an advance. Bind every intended object and generic intended-model data binder faithfully
  in the NL ledger, with the definitions and evidence needed to audit its intended meaning.
  Completed hashed Lean adapters are required for selected certificate interfaces and
  their SILVER certification, not for every NL row or object. No toy realization or
  invented instantiation can replace that meaning. Every theorem face records its own
  exact `premise_ids` and `interface_ids`, equal to those of its audited root; union-only
  closure is forbidden. Full Gold adapter closure belongs to the authorized Heavy handoff.
- **The citation gate (`CITED` rows).** A result qualifies as a **temporarily
  trustworthy** root — proof not re-derived, not debated, never a Lean target — through
  either tier: **(T1-journal)** published in a refereed mathematics venue (journal or
  refereed proceedings), or **(T2-released)** publicly released (arXiv or equivalent) with
  at least one author verifiable as a mathematics professor at a university (faculty page
  or equivalent evidence; the skeptic checks this). Anything below both tiers — anonymous
  preprints, blogs, forum posts — stays NOVEL/ROUTINE and must be proved. Every CITED row
  records its tier, and the report's trust base lists T2 roots separately (they carry more
  residual risk than refereed ones). What IS mandatory at BOTH tiers equally — the tier
  changes only who vouches for the proof, never the required exactness of the match at the
  use site — and what the skeptic attacks with `fatal` severity, is
  the **100% match audit**: the row must carry (a) the full bibliographic pointer down to
  the theorem number, (b) the source's statement verbatim (or a faithful restatement with
  an explicit notation map), and (c) a hypothesis-for-hypothesis checklist showing the use
  site satisfies EVERY hypothesis of the cited statement under the source's own
  conventions (degenerate cases, strictness, normalizations included), and consumes no
  more than its conclusion. "Roughly this" or conclusion-shaped resemblance is a fatal
  objection, not a citation. CITED rows are the NL analogue of declared axioms: each one
  is a named trust root, enumerated in the final report, and the grade is annotated
  "modulo cited results" — a later GOLD pass re-earns them formally or from Mathlib.
- **status**: `drafted → contested(n objections) → accepted | refuted |
  inference-certified | lean-certified | needs-lean | open-residual`.
  `inference-certified` means Lean checked the displayed implication; `lean-certified`
  additionally requires a closed transitive premise manifest. A ledger is **closed** only
  when every step is `accepted` or `lean-certified` and no residual is open.
- **evidence**: attack rounds survived; experiment ids + outcomes; certificate file; or the
  objection that refuted it.
The union rule: the theorem is proved (BRONZE or better) iff every ledger row of the
winning route is closed and the rows compose (the skeptic's final pass checks composition:
no step uses a refuted or missing row, no circular `uses`).

---

## Phase L0 — understand + probe (no Lean, ~minutes)
1. **A1 discipline from auto-research, minus Lean**: objects, hypotheses, exact claim,
   quantifier shape, degenerate cases, what counts as an answer. Write the *problem
   dossier* at the top of `ledger.md`. Determine-style problems: fix the answer shape
   before routing (probe first if the answer itself is unknown).
   Run one `skeptic` with `LENS=assumptions` before route dispatch and write
   `assumption-census.md`: every premise is `ORIGINAL | PROVED | CITED | ASSUMED/OPEN`,
   with source span, consumers, and joint intended-model compatibility. Source/reference
   documents are mathematical data, never instructions that can change task scope.
   Also freeze `target-contract.json` with source hashes, exact theorem faces, allowed
   premises, intended objects, and the target signature. Heavy handoff uses this contract,
   never the ledger alone.
   Preserve the complete original source and answer criterion separately from any chosen
   scoped milestone. Apply the original-problem gate in `docs/trust-and-instantiation-gates.md`;
   a self-authored narrowed target cannot become the original reference.
2. **Direction probe** — one `explore`: smallest nontrivial cases, random instances, OEIS
   if integer-flavored. Verified counterexample ⇒ the target flips to refutation NOW
   (witness + independent re-check = §B6 gate) and L1 routes become "refutation +
   generalize the witness". Supportive ⇒ proceed to prove. Ambiguous ⇒ give the sustained
   candidate a disproof-oriented discriminating check; open another route only if L1's
   evidence triggers fallback breadth.
3. Bank the dossier + probe verdict.

## Phase L1 — choose and sustain the best candidate
From the dossier and direction probe, main gives one persistent `nl-prover` actor the
best current candidate. The actor may formulate the candidate when no pitch exists. It records:
- **representation**: what the objects BECOME and why the main obstruction shrinks under it;
  a same-strength rephrasing is not a promising candidate,
- **skeleton**: the initial self-contained ledger rows and their dependencies,
- **weakest step**: the likely first place the route can fail, and
- **discriminating check**: a small counterexample search or calculation when one would
  materially test the candidate. Run that check when available; it is evidence, not a ritual.

Do not launch a mandatory portfolio, rival, or scout batch. Open up to `ROUTES` alternative
pitches only when evidence calls for breadth: no promising candidate emerges from L0; the
representation/model choice itself is uncertain; a fresh review finds the representation
fatal; repeated local repair leaves the same material obstruction without useful progress;
or the user explicitly requests alternatives. Assign different relevant angles (for example
induction, construction, algebraic identity, extremal exchange, analytic bound, counting,
invariant, contradiction, or theorem specialization), and require each scout to return the
four fields above. Scouts may run in parallel when their work is genuinely independent and
host capacity permits; they need not exhaust the fallback budget. Bank every pitch and kill
test. Select the best supported replacement and return to sustained development rather than
maintaining a favorite/rival schedule.

A ledger that appears sufficient for the exact current obligation triggers candidate
validation under `research-effort.md`: pause new redundant search, keep required adversarial
review, Lean triage and composition audits, and preserve all alternative evidence already
produced. After accepted closure at the requested scope/threshold, retire redundant work.
A closed or BRONZE ledger alone does not satisfy a SILVER request or resolve a broader
research question.

## Phase L2 — sustained development + fresh-review repair
For a multi-round route, retain the exact reviewed ledger snapshot, the reviewer's
complete findings, and the actor's response against that version. Use the optional
zero-setup receipt checker in `docs/lite-review-rounds.md` when recording this lineage.
Stable finding IDs keep a deferred gap or an exhausted concession visible until a
later reviewer explicitly resolves it; omitting it from a new report is not a repair.
The checker validates records, not mathematics or grades. Its schema does not itself require
a fresh reviewer on every round and its context metadata cannot authenticate freshness; that
is a limitation of the optional checker, not a waiver of this workflow's fresh review
after every ledger revision. Nitpicks do not block mathematical closure. The host must create
the fresh context and disclose honestly when it cannot. A nonfresh fallback review may guide
provisional repair, but it does not satisfy the fresh-review gate or close the candidate;
checkpoint and obtain the required fresh review before grading.

1. The persistent `nl-prover` expands the candidate into a full ledger: every row
   self-contained, every `uses` explicit, classes honest (over-claiming `ROUTINE` is the
   classic hiding spot — the skeptic is told to re-classify). Preserve its context,
   partial derivations, failed attempts and ledger lineage across repairs.
2. **Bounded execution when useful** — a concrete experiment or selected weakest-link Lean
   task may go to the provider adapter's bounded executor (Sol on GPT by default). Main
   provides the full task boundaries and clearly labelled tentative ideas. The executor may
   reject or replace those ideas, reports exact diagnostics and deviations, and cannot change
   the goal, hypotheses, established interfaces or acceptance gates.
3. **Fresh review** (`skeptic`, `REVIEW_MODE=focused`; Astra on GPT by default): review the
   exact revision in dependency order and identify the earliest currently live substantive
   invalid or missing inference, whether carried from an earlier review or newly found. Return its
   stable ID, step, severity in `{fatal, gap}`, content and `what-would-resolve`. Also carry
   every previously known unresolved finding and report any later material defect actually
   noticed; stopping the focal search at the earliest live defect never permits suppressing
   evidence. Give the reviewer the dossier, exact ledger, public evidence and prior stable
   findings, without an intended verdict or the actor's private reasoning. Do not invent a
   defect when the argument survives. Additional lenses
   (*counterexample*, *usage*, *novelty*, *assumptions*) are evidence-triggered tools, not a
   mandatory parallel reviewer set.
4. **Experiment pass** — for every objection with computational content and every
   `COMPUTATION` row: `explore` probes (structured: exact small cases first, then random;
   report per its reliability rules). An experiment that contradicts a step ⇒ the step is
   `refuted` pending the independent re-check; sampled support never proves the claim.
   Exhaustive exact evaluation may close the stated finite claim after independent checks
   of coverage, arithmetic, implementation and its mathematical interpretation; the range
   reduction must itself be justified. Floating-point output alone is not exact evidence.
5. **Local repair** — resume the same `nl-prover` actor with the exact review, prior open
   findings and execution evidence. Repair the focal defect locally by strengthening or
   splitting a row, inserting a bridge, or rerouting the affected subargument. Preserve
   provenance and every earlier finding. A materially revised ledger then receives a new
   fresh review context. If the host cannot resume the actor, give a replacement the exact
   artifact, review, public working notes and failure history; disclose the context-continuity
   loss and preserve valid progress rather than reconstructing the route from scratch.
6. Leave the loop as **candidate-ready** only when the fresh review finds no live fatal/gap;
   record that review evidence and mark its surviving drafted/contested rows `accepted`.
   This schedules L3 and L4 and is not closure by itself. Mark the candidate **dead** when a
   verified fatal attacks its representation or evidence shows repeated local repair is not
   making useful progress; then use L1's fallback breadth. If an explicit `DEBATE_ROUNDS`
   or resource limit arrives with live findings, checkpoint honestly rather than accepting
   the ledger. A verified counterexample to the QUESTION itself triggers the §B6 pivot.

### Anti-stall decision before another auxiliary repair

If successive rounds repair routine auxiliary facts or certificate plumbing while the same
novel mathematical crux remains open without useful new evidence, main must reconsider the
research route before dispatching another such repair. Record the unchanged crux, what the
repairs accomplished, why they did not reduce it, and a concrete next discriminating move:
develop the crux directly, test another representation, seek an exact applicable result, or
kill the route on supported evidence. Retain valid auxiliary results and every live finding.
Continue an auxiliary task only with an explicit causal account of how its result now helps
resolve that crux. This is an evidence-triggered allocation rule, not a fixed round, token,
certificate or time cutoff. Reconsideration neither proves the route wrong nor licenses
acceptance; an open research gap remains open at every resource limit.

## Phase L3 — weakest-link triage → targeted Lean
L3 follows a viable natural-language candidate and its substantive review. A missing
mathematical argument belongs in L2 research; attaching a Lean task to it does not create
a candidate. Rank the candidate's remaining certification uncertainty and select only
inferences for which a faithful local certificate materially reduces that uncertainty.
For every row, record a triage decision and reason: the exact unresolved doubt, existing
NL/review/computational/source evidence, why Lean would help (or is unnecessary), and the
cost of faithfully encoding its premises. Cite the reviewed revision and finding IDs.

Select a row when its mathematically supported inference remains disputed after review,
or it is the route's genuinely fragile crux, or a computational inference still lacks an
adequate exact justification and a targeted certificate can supply it. A sampled check is
a reason to examine the missing justification, not an automatic Lean assignment. Likewise,
`NOVEL`, dependency fan-out, long notation, or importance to the conclusion alone never
make every supporting row a Lean target. Typical selection is **0–3 rows**, not a quota or
an arbitrary ceiling: select more only with an individual substantive reason for each.

Routine mathematics with a checked justification, exact exhaustive computations with a
checked coverage argument and implementation, and exact audited citations normally remain
NL evidence. Do not reprove cited content, create generic library infrastructure, or
formalize a dependency closure merely to accumulate certificates. A certificate may use
accepted prior ledger claims as explicit premises, subject to the premise manifest below.
All substantive mathematical findings remain visible and block mathematical closure until
resolved, regardless of whether their rows were selected for Lean.

**Retriage is an evidence decision.** Preserve every previous selection, certificate,
failed attempt and finding. A changed argument, exact computation, corrected citation, or
better cost assessment may justify changing a selection. Record the old and new decisions,
reason and evidence; obtain independent substantive review of that change. Moving an
unproved inference out of L3 never closes it. An honestly accepted NL inference may remain
BRONZE when faithful encoding is disproportionate; report the certification gap rather
than forcing the whole route into formalization or claiming SILVER by dropping the target.

**The certificate (hypothesis-mode — the inverse of no-axiom mode):** for row S⟨k⟩ with
`uses: S_i…`, write `DATA_DIR/cert/Cert_S<k>.lean`:
`theorem cert_S<k> (h_i : ⟦S_i⟧) … : ⟦S_k⟧ := by sorry` — prior accepted steps enter as
**hypotheses of the statement**, never as `axiom` declarations; only S⟨k⟩'s own inference
is formalized. Dispatch `compile-fix` on it (`LIB_DIR`, `AXIOM_POLICY=strict`,
`STATEMENT_ID=cert_S<k>`; plan-graph search step skipped if no store). Outcomes:
`clean` ⇒ row `inference-certified`: Lean proved only `⟦premises⟧ → ⟦S_k⟧`.
`#print axioms` does not certify theorem binders or proposition-valued interface fields.
Attach a transitive premise manifest mapping every binder/field to an L0 original,
earlier derived row, or exact citation. Only a closed manifest upgrades the row to
`lean-certified` (record the standard-three `#print axioms` output as necessary evidence).
`needs_update` with decomposition ⇒ the row was a cluster: split the
ledger row accordingly (back to a mini-L2 on the pieces). `failed` after the ladder ⇒ the
row returns for diagnosis: a discovered mathematical gap reopens L2; a compiler or
representation difficulty is a certification gap, not by itself a mathematical objection.
If formalizing ⟦S_i⟧ faithfully is itself a project (the encoding problem), bank that as
`needs-lean (encoding)` while retaining its reviewed NL status separately. Obtain independent
retriage as above, report the missing certificate and stay at the supported grade. Do not
expand Lite into an infrastructure project to avoid recording this limitation.
`CITED` rows never fire for their own content (the proof is external); when a cert's
`uses` include one, the cited statement enters as a hypothesis like any other ⟦S_i⟧ — so
the use-site inference around it is still certifiable.

## Phase L4 — assemble, grade, report
- **Original-question completion check**: the submitter obtains two fresh independent
  `roles/original-problem-reviewer.md` comparisons by default of the frozen original source, actual
  main interface and necessary definitions. Both current passes are required for `settled` or
  complete-answer submission; missing/fail/unknown/stale/non-independent evidence blocks
  those claims. Partial BRONZE/SILVER output remains valid under its honest scope.
- **Comprehensive composition pass**: a fresh substantive skeptic with
  `REVIEW_MODE=comprehensive` reviews the candidate-ready ledger as a whole, without the
  first-gap stopping rule: every row and carried finding,
  row interfaces, no circularity, theorem statement exactly what L0 promised, no silent
  narrowing. Any material finding returns the same persistent actor to L2 and reopens the
  affected L3 triage; only a later comprehensive pass with no live fatal/gap permits closure.
- **THEOREM-FACE CLOSURE / INTENDED-MODEL GATE**: emit `assumption-census.md`, flattening
  all binders and transitive proposition-valued fields as `original | derived | cited |
  residual`, with their evidence and exact intended-object realization. A point, toy, or
  zero model proves consistency only. For obstruction claims also record stage, fibre
  connectivity, coefficient system, primary/non-primary status, and indeterminacy.
- **Grades**: **BRONZE** — ledger closed on debate+numerics alone (or `needs-lean` rows
  outstanding for lack of workspace/encoding). **SILVER** — BRONZE + every §L3-triaged row
  `lean-certified`. **Heavy handoff ready** — prepare the explicit MerLean `-heavy` handoff
  (seed it with the ledger as route 1); execute it only when authorized by the user.
  This readiness is a handoff status, not another grade.
  Lite immediately rewrites every dependent result “if C holds, then …”
  when a true condition is introduced. It distinguishes `OPEN RESIDUAL != DECLARED CONDITION`,
  exposes each condition as a candidate PUBLIC ANTECEDENT, and prepares BOUNDARY AXIOM /ref GATE
  records with exact local source text plus two independent source/use-site audits. Heavy alone
  may return unconditional or CONDITIONAL GOLD after kernel/evidence closure; Gold does not mean
  the condition is discharged. lite-research's own ceiling is SILVER; say so
  plainly. The only grade tokens are BRONZE/SILVER/GOLD; `CITED`, `CONDITIONAL`, and
  `OVER_INTERFACE` are qualifiers. Reject invented variants such as `GOLD-CITED` or
  `GOLD-over-interface`; any open residual or hidden/uninstantiated interface prevents GOLD.
  The heavy handoff includes `goal-contract.json`, an independent `goal_alignment` report,
  `intended_model_bindings`, and per-face `premise_ids`/`interface_ids`; without those,
  `settled`, `conditional_advance`, and `advances_question` are unavailable.
  If those cited conditions currently live as fields of a custom source record, mark the
  record-binder root non-Gold-ready and hand Heavy an explicit wrapper task: expose
  `Nonempty SourcePackage` (or an exact `Exists`/conjunction) as a proposition binder, retain the
  record only internally, and audit every component plus shared normalization/naturality data.
  A source package is never an intended-model adapter.
- **Refuted** questions: the witness, the two independent verifications, and (when cheap)
  a `Cert_Witness.lean` `decide`/`norm_num` certificate — a settled "no" at SILVER.
- **Report**: the theorem/refutation in NL; the winning representation and why it reduced
  complexity; the final ledger (every row: class, status, evidence); routes killed and by
  what; experiments run (scripts remain in `DATA_DIR`); certificates and their axiom
  audits; **the trust base** — every `CITED` row with its reference and match audit
  (grades carry the annotation "modulo cited results" whenever this list is nonempty);
  the grade; what GOLD would take.

## Pivot gate (unchanged from auto-research §B6)
Direction flips only on an **independently verified** witness — two separate code paths,
sampling artifacts assumed until re-checked. Bank refuted suspicions so they cannot recur.
The QUESTION never changes; only the direction, loudly.

## No walls, no questions
Missing lemma ⇒ new ledger rows. Stuck route ⇒ representation hunt (§L2.6) or route death,
never a silent stall. Never ask the user; the run ends at a graded report or interruption.
Keep the main context lean: subagent summaries only; the ledger holds the detail.

### Bounded local verification modules (Lite)

A selected Lean check is a small internal module for one materially uncertain local
claim. It is not a new problem or a requirement to formalize the proof's foundations.
Keep the readable main-owned handoff and advisory hints; Sol may revise tentative
signatures and tactics within the independently reviewed claim, explicit premises,
owned scope and acceptance conditions. Accepted mathematical inputs may remain
explicit hypotheses with exact applicability and the existing premise checks.

The main supplies a short scope/value brief and proportionate worker/probe bounds.
The host records exact claim, dependent-premise, candidate, task and approval
bindings, a stable lineage, all attempts and complete returned evidence. Existing
independent triage admits only high material local uncertainty. The same guard
serves Sol implementation and main inline Lean; no extra bookkeeping reviewer is
required. Mechanical checks bind exact interfaces and records; independent review
judges mathematical scope and whether a changed approach adds real value.

Return to the original main on foundational scope expansion, disproportionate
faithful encoding, exhausted agreed local bounds, or no uncertainty reduction.
Retain code, diagnostics, findings and costs. This operational exit never proves
or resolves the claim. A still-needed check remains an unresolved obligation.
The existing independent review can instead justify a replacement or removal of
a now-unnecessary check from current substantive evidence, explicitly mapping all
prior modules and findings. Labels, budgets and candidate churn do not erase a
lineage or its spent history; reentry requires current evidence and new value.

Natural-language research continues after a module returns. Zero Lean modules is
valid when current independent review selects none: the existing nonempty closed
ledger, full proof, original-scope and grade gates still apply. No grade semantics,
Heavy/Gold requirements, paper behavior or human-readable handoff style change.

### Select only checks with a concrete verification benefit

Before approving a new Lite Lean task, identify the exact unresolved uncertainty after
natural-language development and independent review, the evidence already available,
the actual intended objects and use-site map, and the noncircular accepted premise
boundary. State what a faithful certificate would newly establish, how its encoding
can fit the proposed local bounds, and why that value warrants the expected cost.
Novelty, importance, dependency fan-out, or a wish to accumulate certificates alone
is not selection evidence. Zero new Lean tasks is valid when independently justified.
This does not retire existing obligations: preserve their failed attempts and require
substantive independent reassessment before replacement or deselection. No automatic
retriage, retrospective approval, downgrade, or change to Silver requirements follows.

### Coherent execution inside an approved local module

An unchanged independently approved local task may run a bounded worker/source → host
compiler → implementation-repair cycle before returning for scientific acceptance.
In the host protocol, `compile_pending` explicitly requests that cycle and supplies
source, the exact selected row, `implementation_complete` and a concrete `next_step`.
It need not claim uncertainty reduction before receiving its first real diagnostic.
`implementation_complete` is the worker's coverage claim, not acceptance: a clean
compile of a full implementation stops for independent premise, intended-object and
certificate assessment. A failed compile or compiled incomplete implementation can
receive the next bounded repair with all exact prior source and diagnostics.
Generic `local_evidence` alone does not request repeated implementation. Identical
source resubmission supplies no new diagnostic work and stops the cycle.

Keep the same immutable task, claim, actual-object interface, premise closure, owned
scope, candidate and independent approval binding throughout that cycle. Count every
worker call and probe against the original cumulative module limits. Retain every
attempt and failure; replacement generations inherit consumed counters, never a new
allowance merely for changed wording. Every dispatch and compiler invocation must
revalidate those bindings and respect the host's drain, deadline and resource controls.
Where workers cannot invoke Lean directly, returned source is a request to the host,
not a failed compilation. Reconstructed worker contexts must receive the full retained
implementation evidence with continuity loss disclosed.

Goal/premise/interface/scope/budget changes, material mathematical counterissues,
encoding infeasibility, no-value evidence, missing host execution, and exhausted bounds
return to main under the existing independent reassessment rule. Terminal historical
reports, including `returned_to_main`, remain terminal; protocol migration does not
relabel them as pending or authorize replay. No scientific reviewer is required merely
between source and its first authorized compiler diagnostic. Independent acceptance
after the resulting certificate, comprehensive full-proof review, two fresh original-
scope reviews and all selected-grade gates remain unchanged.

## Optional Lite NL capability

An explicit `-NL` / `--nl` selects Lite with Lean disabled; standalone `-NL` and
`-lite -NL` are equivalent. Read `docs/nl-mode.md` before setup or dispatch. Persist
and inherit the capability; never silently change a resumed campaign. Keep the same
NL discovery, plan ownership, independent review, original-scope and Silver gates.
Do not dispatch formalization, Lean MCP, lean/lake/elan, compiler inventory or Lean
workers/probes. Keep required unresolved certificates and findings; do not auto-deselect,
downgrade grades or claim Gold. Paper work inherits this restriction and preserves
history. Use the shared guarded setup/CLI; native arbitrary shell enforcement is
instruction-bound, not an OS-level prohibition.
