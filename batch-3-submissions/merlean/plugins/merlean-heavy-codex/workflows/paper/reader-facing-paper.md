# Reader-facing paper contract

Apply this contract during planning, drafting, revision and the existing independent reader,
mathematical fidelity and rendering reviews. It adds no gate or review round and changes no
research acceptance, grade, proof obligation, page limit or source-verification requirement.

## Mathematical paper and faithful evidence

Write the final TeX/PDF as a self-contained mathematical manuscript suitable for an arXiv
reader: problem, results, exact hypotheses, proofs, relevant literature, and useful
explanations. It is a paper, not a chronological work log. Omit abandoned exploration and
unrelated debugging unless a negative result or limitation is itself necessary to answer the
mathematical question. Internal archive access helps the author establish the result; it does
not make that archive the paper's narrative.

Write the final TeX/PDF for an external mathematical reader. Omit internal acceptance and
grading labels (including SILVER/GOLD), controller records, tickets, run/session identifiers,
artifact hashes, audit verdicts, task bookkeeping and process diaries from its exposition.
Keep those records faithfully in the existing evidence assessment, reconstruction map,
raw/evidence archives, preservation ledgers and release reports. Never rewrite or sanitize
original evidence, frozen raw sources or historical audits to improve the final paper.

Treat Lean as an internal auxiliary tool by default. Do not add a formal-verification section,
kernel-check claim, proof-assistant name, or artifact-access caveat merely because Lean helped
produce the proof. The mathematical argument must stand on the page. Preserve build and
formalization records internally. If formalization is explicitly the paper's subject, discuss
it with supported scope and precise references; this exception is not a license to replace
mathematical reasoning by a verification assertion.

Preserve the exact mathematical scope, quantifiers, hypotheses, conditional conclusions,
unresolved proof gaps, counterexamples, dependencies and known credit in the paper itself.
Translate workflow status into its mathematical meaning: an unproved implication remains
explicitly unproved; failure to establish a needed hypothesis remains a stated limitation.
A missing administrative approval alone is not a mathematical gap, and removing a grade
label cannot turn an incomplete argument into a theorem. State only what inspected evidence
supports. Keep useful explanations, examples and mathematical discussion.

Independent fidelity review compares mathematical content and qualifications, not verbatim
workflow prose. Distinguish faithful raw reconstruction from publication wording. An audit
must not require final TeX/PDF to repeat internal history when its mathematical consequences
remain explicit and the history remains recoverable in sidecars. Use the existing coverage
and deletion ledgers for changed content; no required inference may survive only in a ledger.
This is contextual editorial guidance, not a keyword ban or an automatic text filter.
Retain legitimate mathematical uses, such as a gold standard in a stated comparison, a hash
function under study, a controller in control theory, or an acceptance probability.

## Explain the step the reader needs

At a non-obvious bridge, explain the objects and map, the change of representation or quotient,
the asserted identification or isomorphism, and why it supports the next conclusion, as
applicable. For a theorem application state the specialized objects and check its exact
hypotheses. A theorem name or the word “standard” is not a paper-specific argument. Explain
using the available proof; never invent a missing justification. If evidence does not supply
the bridge, disclose the gap and follow the existing research-gap procedure.

## Figures when they clarify

Consider a figure when geometry, structure, a correspondence or relations are hard to follow
in prose or formulas. Include it only when it materially helps the intended reader; no figure
is required in every paper. Every newly authored figure must use LaTeX `tikzpicture`, with
labels, arrows, conventions and a caption consistent with the text. Do not substitute external
raster images, ImageGen or Mermaid for author-generated figures. Keep original historical
assets unchanged in raw/evidence archives. A figure explains an argument and never replaces
its proof; do not add unsupported geometric or identification assumptions through its layout.
Do not imply unproved incidence, orientation, commutativity or scale; distinguish schematic
features from established relations.
Check every new figure in the existing compilation and rendered-page inspection.

## Claim-specific sources and useful length

Use external tools only for a concrete need: identify the question a web search, source download,
Python calculation or Lean check will resolve before calling it. Targeted reference search and
primary-content reading are mandatory under `references.md`; unrelated browsing, Python and
Lean reruns are not. Use the available bounded retrieval and cached outcomes; do not
loop on unavailable sources or wait for a human download. Continue independent work, omit
unavailable optional citations with a record, and preserve an honest gap when essential proof
evidence is unavailable. Tool failure is neither a proof nor permission to invent a citation.

For each citation identify the actual claim used and the inspected source version, with an
appropriate theorem, proposition, section or page locator. Check conventions and hypotheses
at the use site. BibTeX metadata is not content validation. Follow `references.md` unchanged:
for arXiv inspect the full source and actual cited claim and save the exported BibTeX verbatim;
use its established verified-source alternatives and offline fallback. This contract grants
no network access to offline research and never permits invented sources or lost attribution.
In the existing independent literature audit, compare the final typeset bibliography entry
and in-text use with the inspected source and citation export, including version, authors,
title and claim locator. A downloaded BibTeX block alone does not verify the rendered entry;
the native self-contained TeX path must preserve that correspondence without an external bibliography.

Choose length by reader benefit within the applicable page limit. Remove repetition and
ancillary process history before shortening explanations; retain what establishes scope,
proof, limitations or understanding. No arbitrary shortening target or expansion quota
overrides mathematical fidelity. Use one principal explanation with helpful cross-references.
Readers should flag located confusion, missing bridges, ambiguous figure relations, unsupported
citations or distracting repetition; they should not demand decorative figures or stylistic churn.
