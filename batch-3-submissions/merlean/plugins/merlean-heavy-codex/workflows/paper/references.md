# Reference protocol

Every new paper-writing run must search and consider relevant literature. This is a relevance
and attribution requirement, not a novelty assessment or a citation-count target. Search for
the constructions, methods and results actually used; select the most important citations
by relevance. Do not search for benchmark solutions. Record actual queries, considered
candidates, exact supported claims and inclusion/exclusion reasons. A search result or abstract
is discovery evidence, not evidence that the source establishes the cited result.

Before downloading, check the problem workspace's `refs/` and the existing registry. Reuse
matching identity/version, archive, source and export hashes; do not repeat valid downloads
or unchanged failed attempts. Apply the retrieval steps below only to missing or invalidated
material. A prior cached search also needs its actual query/result evidence, not a remembered
claim that the topic was searched.

1. Search the internet for an arXiv version. Confirm title, authors, and abstract on the abs page.
2. Download the complete source archive from `https://arxiv.org/e-print/<id>`.
3. Save the raw archive and SHA-256. Extract with `paperctl safe-extract-arxiv ARCHIVE DEST` into
   `PROJECT/refs/<id-with-underscores>/`. The command refuses existing destinations, traversal,
   links, devices, and oversized archives.
4. Follow `\input`/`\include` and inspect the actual TeX for the exact result being cited. Record the
   file, line/window or excerpt hash, claim, and decision. An abstract is discovery evidence only.
5. If the content is present and relevant, select it for citation; record why. Content being present
   does not require citing every candidate. Otherwise mark the candidate rejected and consider a
   similar arXiv paper. If no arXiv version exists, an authoritative public journal article or book
   is eligible: save its public source PDF, inspect the exact claim, and record source, evidence,
   and citation hashes using `source_type: article` or `source_type: book` as appropriate.
   If no public copy can be verified, apply the autonomous fallback below; do not request a human download.
6. Open “Export BibTeX citation” on the arXiv abs page. Save that block verbatim and its SHA-256;
   never hand-write an arXiv BibTeX entry. Reuse its exported citation key. Verify the rendered
   bibliography entry and in-text use against that export. For the single-TeX output, embed
   the bibliography's reader-facing entries in the TeX; keep the exported BibTeX separately as
   author-side evidence, not as extra input to the isolated reader.

Each arXiv `references-registry.json` entry needs `source_type: arxiv`, citation key, arXiv ID, canonical URLs, confirmed title,
authors, abstract confirmation, raw archive path/hash, extracted source directory, relevant TeX
location/evidence hash, exact supported claim, accepted/rejected status, BibTeX snapshot path/hash,
the candidate bibliography path, and verification date. Reuse cached material only when these paths
and hashes agree. A non-arXiv publication uses its exact type: `source_type: article` for a
journal article and `source_type: book` for a book. Both require a public URL, local public source
file/hash, evidence file/page/hash, exact claim, saved citation snapshot/hash, candidate bibliography
path, and verification date; neither pretends to have arXiv fields.

For native single-TeX output, a registry entry may use `bibliography_format: inline`,
`bibliography_path` equal to the output TeX, and the exact `rendered_entry` beginning with
its exported-key `\bibitem`. Its `rendered_bibliography_audit: {path, sha256}` references
the independent current source audit. That audit includes `bibliography_entries` binding
each `citation_key`, `bibtex_sha256`, `rendered_entry_sha256` and concrete comparison findings.
The export remains verbatim in its separate snapshot, not inserted as raw BibTeX in prose.

## Autonomous literature handling (default)

`literature-policy.json` defaults `assess_novelty` to `false` (exam mode) and
`request_human_authorization` and
`request_human_download` to `false`. Do not create a human authorization or download
wait during an authorized writing task. Use available tools to retrieve and verify sources
autonomously within the current network/tool permissions. This policy does not grant network
access to an offline research run, bypass an access restriction, or allow paid access.
An explicit offline constraint means use verified local material and record the constraint;
do not ask the user to lift it as a routine literature step.

If an optional source cannot be retrieved and verified autonomously, record its identity,
attempt/outcome (or the policy/tool constraint preventing an attempt), intended use and omission
in `03-literature-retrieval.md`, omit the unverified citation, and continue. Do not wait for
someone to download it. Zero selected references is possible after actual relevance review,
but self-contained proofs alone do not justify skipping search or deleting known credit.
Do not replace missing source evidence with an abstract, memory, fabricated
citation, or a claim that novelty was verified. Avoid repeated attempts at an unchanged failure.

This fallback never erases a substantive proof dependency, accepted axiom, public premise,
known attribution, or known overlap. Preserve established credit. Supply an already-supported
self-contained argument or verify an accessible equivalent source and its exact use site.
If neither is possible, record an unresolved mathematical dependency and follow the existing
research-gap procedure; a missing proof is not a successful paper release.
Separate content verification, credit, and bibliography metadata. A failed BibTeX export does
not erase established attribution: keep accurate supported prose credit while recording the
metadata limitation; do not fabricate a formal citation or mark it verified. Seek another
permitted, verified representation without repeating unchanged failures.

## Required relevance and input-credit records

Fresh runs record `literature_search_policy: search-read-v1` and
`attribution_policy: input-credit-v1`. `literature_search: {path, sha256}` binds a current
search/read record with actual query receipts, candidate identities and relevance decisions,
cached/downloaded evidence, content-read locations and findings, and official export evidence
for selected arXiv citations. Selected and content-rejected sources require actual primary
reading; discovery rejection and unavailable material must not be reported as read. A constrained
or pending search cannot pass as completed. Work on the draft may continue without a human wait;
the final report must state an unfinished gate rather than claim full writing completion.

Freeze `input_credit_census: {path, sha256}` against the actual scientific inputs in the raw
checkpoint and, for refinement, the baseline source tree. Census citation keys and substantive
prose credit; do not use an already stripped draft as the only input. An independent
`attribution_audit: {path, sha256}` binds that census and the final manuscript, with one
`keep`, `not-applicable`, or `unresolved` disposition per credit, concrete reasons and final
use sites. Re-proving a result does not erase origin credit. Distinguish proof dependency
from attribution and metadata availability. Unresolved essential credit prevents PASS.
These records are author-side evidence, not inputs to the isolated TeX reader. Machine checks
bind evidence and coverage, not the truth of a claim that a person or model read a source.
Historical runs keep their frozen contracts; do not forge retrospective search or reader evidence.

With `assess_novelty: false`, skip novelty searches and record `NOT_REQUESTED`.
Novelty is not an exam requirement: even a known equivalent result does not invalidate a
correct answer. Preserve known credit and remove unsupported priority claims. If novelty
assessment is explicitly enabled (`assess_novelty: true`) but available evidence cannot support
`CLEAR` or `ADJACENT`, record `NOT_ASSESSED`.
Keep the result and its proved scope, omit all priority/first/newness claims, and report limited
literature coverage in the release report. Unknown novelty alone is not a proof gap or a human
input requirement. A known overlap must still be recorded and any misleading originality framing corrected;
do not relabel it unknown. With novelty assessment enabled, `COLLISION` reopens result framing. Independently audit the final manuscript's claims, actual proof
dependencies and preserved credit. This is not permission to skip fidelity, reader or release gates.

For each composed result with `NOT_REQUESTED` or `NOT_ASSESSED`, retain normal result-lock fields and set
`priority_claim: false`, a substantive `novelty_limitations` explanation,
and `literature_audit: {path, sha256}` referencing the independent JSON report below. Paths are
absolute or relative to the work directory. This report may cover multiple selected results;
refresh it after manuscript or result-lock changes, preserving historical reports.

```json
{
  "verdict": "PASS",
  "reviewer_id": "actual-independent-reviewer",
  "writer_ids": ["actual-writer"],
  "candidate_source_tree_sha256": "ordinary inventory_tex source_tree_sha256",
  "result_ids": ["selected-result-id"],
  "novelty_status": "NOT_REQUESTED",
  "policy_record": {"path": "literature-policy.json", "sha256": "actual SHA-256"},
  "retrieval_record": {"path": "03-literature-retrieval.md", "sha256": "actual SHA-256"},
  "priority_claims_absent": true,
  "overlap_disposition": "Record known overlap and preserved credit, or that none is known without claiming a search.",
  "unresolved_proof_dependencies": [],
  "unresolved_attribution_issues": [],
  "findings": "Concrete independent findings on retrieval limits, claims, dependencies and credit."
}
```

The report binds the current manuscript tree, policy, status and exact selected result IDs.
The retrieval record may state that no novelty search was requested; this does not waive
the separate relevance-search gate for new runs. Do not invent retrieval attempts. Offline
runs may reuse valid cached search/read evidence; otherwise record the outstanding constraint.
This report does not certify
novelty. Do not include a self-referential main-results hash: the result lock hashes the report,
while the report binds the manuscript statements through the source-tree hash. Reviewer identity
must differ from every writer recorded in the report, raw checkpoint and reader records. Hash and
identity checks bind declared evidence; the host must still verify actual independent dispatch.
