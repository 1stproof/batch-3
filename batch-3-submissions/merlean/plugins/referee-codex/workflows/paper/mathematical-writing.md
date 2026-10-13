# Evidence-aware mathematical writing

Shared English contract for Claude and Codex, adapted from the author's general mathematical
writing guidelines. It supersedes conflicting absolute editorial prescriptions in the older
composition supplement, without weakening preservation, source, or research-grade boundaries.
Priority: mathematical accuracy and scope; reconstructible reasoning; reader order; concision.

Apply [reader-facing-paper.md](reader-facing-paper.md) throughout planning, drafting and review:
separate publication prose from faithful evidence records, explain needed bridges, use
TikZ figures only for concrete reader benefit, verify claim-specific citations, and retain useful detail.

## Assess the material before choosing a workflow

A Lean critical path is a navigation aid, not the authority for the paper's mathematical scope
or proof completeness. A project may contain Heavy-certified proofs, Lite natural-language
proofs, partial Lean formalization, literature results, conjectures, or a mixture. Read the
latest author-approved manuscript and actual supporting arguments before deciding what is ready.
Do not discard a valid natural-language result because no Lean node exists, or treat a compiled
node, plan status, claimed grade, or imported hypothesis as proof that the intended claim holds.

Create an evidence assessment per selected result: exact statement and public assumptions;
available natural-language, Lean, computational and literature evidence; actual proof status;
formalization status and recorded grade if any; missing inferences, unresolved hypotheses and
source/use-site questions; and permissible wording. Review unformalized reasoning mathematically,
not merely for agreement with a draft. Keep proof correctness distinct from formal certification.
If there is no usable graph, record why and reconstruct dependencies from the arguments. If a
graph exists, inspect its available ancestor closure and intended-object connections, not just
the longest chain, and note missing or stale nodes. Never silently change the target to fit it.

Writing may organize and explain existing evidence, but cannot promote Silver to Gold or disguise
a gap as a true hypothesis. An unresolved argument may be preserved as a clearly marked question
or incomplete draft, never reported as a proved theorem. Report newly found mathematical defects
and use Lite/Heavy for new proof work only when authorized. A faithful raw draft may contain
explicit research gaps; a raw-fidelity PASS is not a mathematical-validity or publication PASS.

## Objects, contribution, and section purpose

Before drafting, explain the question, objects, target readership, prior results, new conclusion,
and main difficulty in ordinary language. Distinguish borrowed theory, new definitions, results,
and auxiliary constructions. Research chronology, code directories, and proof plumbing do not
determine reading order; a new organization is not automatically a mathematical contribution.

Choose sections by function, not a mandatory template. Abstract: problem, main results, necessary
scope and method. Introduction: significance, difficulty, relation to prior work. Background:
only the prerequisites actually needed. Main proofs: the essential constructions and arguments.
Examples: concrete consequences or limitations. Appendices: supporting material with real
consumers, not everything removed from the body. Outlook: genuine limitations and questions,
not repeated contribution announcements. Keep important proofs visible even when long. Honor
an author-protected structure and use local repairs unless broader reorganization is authorized.

Contribution lists state the principal achievements at the level needed to understand their
significance. Retain qualifications needed for accuracy; give detailed guarantees their main
treatment where they are established, with a cross-reference when useful. Avoid repeating
implementation details or internal checklists in a high-level contribution summary.

## Terminology and reader dependencies

Prefer established field terminology, checking original meanings and conventions. Explain a
changed source convention where it affects the argument. An unfamiliar genuine technical term
is not defective. Name a new object only when repeated use, a useful formula abbreviation or a
necessary distinction justifies it; defining a name does not make it useful or standard. Prefer
saying what an auxiliary argument proves to inventing layers, frameworks, pipelines or modules.

Maintain an internal concept ledger: mathematical object, chosen technical term and notation,
source aliases, authoritative definition, first technical use, and scope. Review each occurrence
in context, including abstract, titles, figures and appendices. Do not mechanically replace
similar spellings, force every ordinary verb to be uniform, or conflate existence/construction,
equality/equivalence, an element/its space, or an object/its representation/index. Explain necessary
synonyms and then use the chosen technical expression. Separate local scopes may reuse notation
when the reset is explicit and interacting objects remain unambiguous.

Supply sufficient definitions, conventions, or explicit references before technical use. Use one
authoritative definition, helpful short reminders, and understandable introductory previews with
forward references. Shared setup belongs where useful; local auxiliaries belong near their use.
Do not pile all definitions at the beginning or enforce arbitrary subsection-distance rules.
After moving text, recheck first occurrences, pronouns, cross-references, and downstream consumers.
Transitions explain what was established and what is needed next; adding “therefore” is not a
missing implication. Explain an object's purpose before describing its implementation.

At first encounter, make the local mathematical objective clear when the purpose, objects,
or proof mechanism changes. For a consequential, non-obvious definition, explain how its
branches or terms serve that objective where the definition is introduced; a generic promise
of later use is not an explanation. The introductory block may supply this through nearby
prose, an immediate interpretation after the formula, or a short inference transparent to the
intended reader. Routine definitions and already clear transitions need no separate preamble.
Do not anticipate the full proof or duplicate an explanation that already works locally.
See `reader-proof-quality.md` for evidence and defect thresholds in applying this check.

Distinguish recalled theory from this paper's realization or application of it. Once a theory,
construction, or library has been established, explain the operations, properties, and hypotheses
used next. Revisit its construction or validation only when needed for the current argument.
This distinguishes section purposes without imposing a fixed structure or omitting proof bridges.

## Exact statements and complete arguments

Definitions specify domains; propositions specify quantifiers, hypotheses and conclusions.
Preserve all relevant topology, finiteness, positivity, regularity, normalization, coefficients,
and nondegeneracy. Make indices, sums, products and limiting ranges clear. Quantitative claims
state error measures and parameter dependence. Check relevant empty/zero/degenerate cases.
Standing setup may be referenced, but conditional conclusions remain recognizably conditional;
“claims only” does not authorize hiding an antecedent.

For long proofs give a useful roadmap, then actual identities, inequalities, constructions or
precisely specialized results at decisive steps. Method names such as induction, compactness
and duality need an identifiable object and role. Verify source hypotheses at the use site.
Distinguish an auxiliary algebraic fact from its identification with the intended bundle, map,
class, orientation or final conclusion. Standard steps can be briefly explained or accurately
cited, but no “standard argument” may conceal the paper-specific bridge. Do not narrate every
displayed algebraic operation twice. Give detailed calculations one principal location and refer
to them elsewhere. Length alone never sends a central proof to an appendix; no essential
inference may survive only in raw TeX or a private recovery ledger.

## Claims, economy, and presentation

Distinguish proved and conditional results, conjectures, computations and judgments. Summaries
must not exceed the theorem. Proving an implication and realizing its conditions are different
obligations. An example must instantiate what it is said to illustrate. Novelty, priority,
generality and optimality require a scoped comparison. Reviewers' agreement is not mathematical
evidence. For tools distinguish mathematical guarantees, implemented checks, human judgments,
and future designs; hashes and green gates cannot establish prose correctness or genuine memory
independence.

Lead with the fact, use clear subjects and verbs, split overloaded sentences, and give each
paragraph one purpose. Before deletion ask whether it supplies a definition, condition, evidence,
key explanation, credit or transition; preserve or relocate that function first. Remove genuine
duplication and unsupported self-evaluation, not scope riders or reasoning. Concision is not a
page quota. A detailed explanation has one main location, with purposeful summaries elsewhere.

Use stable labels rather than page-relative references. Cite the actual result used and relevant
locator/conventions. Citations do not replace required definitions or paper-specific arguments.
Organize background around the idea the reader needs, rather than listing systems one by one.
Group citations for a common approach only when each verified source supports the corresponding
claim. Keep individual attribution where differences, priority, or specific results matter;
do not attribute one source's distinctive feature to the entire group or obscure required credit.
Figures/tables use the same notation and explain arrows, abbreviations and comparison dimensions.
Inspect rendered output: layout must not hide assumptions, misleadingly split formulas or break
references. No unrelated visualization or fixed section template is required.

## Plan within the supplied page limit

When a page limit applies, record its source, counting rule and a provisional allocation in
`02-reader-route.md`. Reserve space first for the exact question/result, public assumptions,
necessary conventions, complete proof and known credit; then budget orientation, references and
any required supporting material. Author-mandated retention counts toward the same budget.
Do not expand a short complete answer to fill an allocation. Use the applicable exam policy for
its actual cap and an optional working reserve; our planning targets and ordinary layout choices
are not submission rules.

Keep the short causal explanations at non-obvious definitions and proof transitions described
above. Give each mechanism one principal explanation, using brief reminders or cross-references
elsewhere; trim repeated previews, theorem restatements and construction summaries first.
State conventions and mathematical proof limitations explicitly where needed. Keep formal
verification status in internal evidence by default: Lean is auxiliary, not a required section
or claim in an exam solution. Only an explicitly formalization-focused paper should discuss it.
Optional research chronology, diagnostic logs and nonessential
reductions belong in the existing raw/recovery artifacts with exact destinations and preservation
records when omitted. Do not claim an external archive exists without a real recovery anchor.
No required result, qualification, credit or load-bearing inference may survive only there.

Compile the first complete draft in the normal legible template and use its measured page count
at the existing pre-shrink gate to revise the allocation before polishing. If the remaining space
is small, flag that in the existing plan and prioritize duplication and optional material for
review. Moving text to an appendix does not save pages when the whole PDF counts. Recompile and
recount after revisions, including the second reader's repairs and final layout, and record the
final count and applicable cap in the release report. A semantic justification for retaining or
adding prose never waives a hard page limit. If complete readable delivery still cannot fit,
report the unresolved constraint; do not change the original scope or grade, hide proof steps,
or shrink type, spacing or margins to disguise it. These checks use the existing planning,
compression, two fresh-reader cycles and release gates, without adding a review stage.

## Revision and independent review

The latest approved paper remains the scope baseline, distinct from the immutable raw evidence
reconstruction. Understand each mathematical fact before rewriting it. Pure editing cannot add
premises, change proof routes or invent contributions. Mark issues resolved only after inspecting
the repair and its downstream effects. Inspect the final diff for scope drift, new terminology,
missing bridges, redundant explanation and misleading claims.

Separate mathematical fidelity/validity review (using all relevant evidence, not necessarily
Lean) from fresh-context sequential reading. The latter sees only the output `.tex` as scientific
input and the neutral exposition/attribution rubric as instructions, not the author's intended
fixes or private maps, and records first points of confusion. Preserve
actual reports and bind repaired-version rereads. The runtime records these reviews rather than
manufacturing them. Final checks ask whether objects, contribution and assumptions are clear;
terms are useful and consistent; definitions follow reader dependencies; key reasoning is
reconstructible; section roles, references and layout are coherent; scope and raw provenance
are preserved; and any remaining gap is honestly disclosed rather than certified away.

Near completion, perform exactly two scheduled editorial cycles: a new fresh-context Astra
reader reads the entire current output TeX under that neutral rubric, gives located feedback,
and the writer revises with an issue-by-issue disposition. Use a different fresh reader for
the second cycle, after the first revision; do not prime either with prior reports, author
intentions or proof maps. Then verify the second revision and run the independent mathematical,
reference and rendering checks. A justified no-op is acceptable; forced stylistic churn is not.
Two cycles bound ordinary polishing, not correctness: unresolved substantive defects block
release and must be repaired or explicitly reported. See `reader-proof-quality.md` and
`two-round-review-runtime.md` for the review and evidence contracts.
