# Two fresh-reader revision cycles: runtime evidence

Near the end of writing, perform exactly two sequential cycles: a fresh-context Astra
reader reads only the current output TeX as scientific input, under a fixed neutral
exposition/attribution rubric, provides feedback,
and the writer revises or records justified no-op decisions. Use different readers in the
two cycles, both independent of the writers. The second reader then verifies the final
revision. This verification is not a third stylistic review. Unresolved substantive issues
block release; an open-ended sequence of additional stylistic rounds is not required.

The orchestrator must actually dispatch fresh contexts. The runtime checks recorded
provenance, identities, hashes, continuity and issue dispositions; it cannot authenticate
identities or independently establish what context an external model received. Never
generate a reviewer report on behalf of a reader or fabricate a PASS.

## Current contract (schema 2)

Fresh runs freeze `reader_round_policy: two-fresh-astra-v2`. The pilot also freezes
`reader_contract` on creation; resumed ledgers without that marker retain their old contract.
The scientific input is the exact self-contained output `.tex`, with inline bibliography,
not Lean, Markdown derivations, input manuscripts, source archives, maps, or previous reviews.
The `guideline` field holds only the fixed `READER_RUBRIC` instruction from
`src/paper_writing_codex/reader_rounds.py`. It is not extra scientific evidence. External
includes, bibliography, and custom content dependencies must not be silently excluded.
The native single-file route rejects unsupported dependencies instead of pretending to read them.

Use the ledger and report structure below with `schema_version: 2`, adding each round's
`manuscript_input: {path, sha256}` (an immutable copy of exactly the bytes read), and the
ledger's `final_manuscript_input` for post-revision verification. Each report binds
`manuscript_sha256` as well as the ordinary tree hash. Its provenance is exactly:

```json
{"kind":"fresh","prior_context":false,"sole_scientific_input":"manuscript","rubric_is_instruction":true}
```

Fresh and final reports include `axes` with exactly `exposition` and `attribution`, each
containing `verdict: PASS|FAIL`, substantive `findings`, and `unresolved_findings: []` or
actual outstanding findings. Located issues additionally contain `axis` and `location`.
Final verification requires approval on both axes. Existing mathematical correctness and
faithfulness checks are unchanged; this is not another correctness campaign. Do not require
journal novelty, arbitrary examples, or Lean-verification prose. Flag a concrete missing
inference as a reader obstacle, not a reason to invent new mathematics.

The second reader's final verification is explicitly **nonfresh**: it can inspect both
reports and dispositions. Never label this follow-up a third isolated reading. Preserve
all original reader findings, including failures, and bind the final verified revision.

## Legacy record format (schema 1)

The examples below describe the historical manuscript-and-guideline contract. They remain
valid only for runs retaining that contract, not as a shortcut for new schema-2 evidence.

## Hashes and checkpoints

Use the ordinary `paperctl inventory` hash for this review protocol, consistently with the
existing reader audit. This differs from the raw-checkpoint asset inventory; the separate
raw-preservation check continues to bind explicit assets.

Before each reader dispatch, save an inventory:

```text
paperctl inventory PAPER/paper-vN.tex --out WORK/08-round-1-before.json
paperctl inventory PAPER/paper-vN.tex --out WORK/08-round-2-before.json
```

Run the second command only after the first cycle's revision. Preserve both inventories,
the actual reader reports, and the writer's actual disposition reports. Use SHA-256 of each
artifact's file bytes in references. `before_source_tree_sha256` and
`after_source_tree_sha256` are the `source_tree_sha256` values from ordinary inventories.
The second round's before hash must equal the first round's after hash. The final
verification and the second round's after hash must match the current manuscript.

## Ledger

Save `WORK/08-reader-rounds.json` with this shape. Paths may be absolute or relative to WORK.
Values below describe fields; replace them with actual artifact paths and hashes.

```json
{
  "schema_version": 1,
  "guideline": {"path": "writing-guideline.md", "sha256": "GUIDELINE_FILE_SHA256"},
  "writer_ids": ["actual-writer-id"],
  "rounds": [
    {
      "reader_id": "fresh-reader-one",
      "before_source_tree_sha256": "FIRST_INPUT_TREE_SHA256",
      "before_inventory": {"path": "08-round-1-before.json", "sha256": "INVENTORY_FILE_SHA256"},
      "reader_report": {"path": "08-round-1-reader.json", "sha256": "READER_REPORT_FILE_SHA256"},
      "after_source_tree_sha256": "FIRST_REVISED_TREE_SHA256",
      "disposition_report": {"path": "08-round-1-disposition.json", "sha256": "DISPOSITION_FILE_SHA256"}
    },
    {
      "reader_id": "fresh-reader-two",
      "before_source_tree_sha256": "FIRST_REVISED_TREE_SHA256",
      "before_inventory": {"path": "08-round-2-before.json", "sha256": "INVENTORY_FILE_SHA256"},
      "reader_report": {"path": "08-round-2-reader.json", "sha256": "READER_REPORT_FILE_SHA256"},
      "after_source_tree_sha256": "FINAL_TREE_SHA256",
      "disposition_report": {"path": "08-round-2-disposition.json", "sha256": "DISPOSITION_FILE_SHA256"}
    }
  ],
  "final_verification": {"path": "08-round-2-verification.json", "sha256": "VERIFICATION_FILE_SHA256"}
}
```

Reader identities must differ after whitespace/case normalization, and neither may be a
writer recorded in the ledger, immutable raw evidence, or `07-reader-audit.json`.
When the existing `07-reader-audit.json` is present, its `reader_id` must be the second
round's reader. That reader supplies the existing first-pass/final-reread records as well
as the cycle records above; these may be separate actual reports satisfying the two
schemas. This does not introduce a third reader or authorize the writer to synthesize
reader evidence. In the legacy manuscript-only provenance, the required writing guideline
is permitted; author plans and reconstruction maps are not first-pass reading material.

## Actual reader report

Each independent reader supplies a JSON report with:

```json
{
  "reviewer_id": "fresh-reader-one",
  "model": "gpt-6-astra",
  "provenance": {"kind": "fresh", "prior_context": false, "manuscript_and_guideline_only": true},
  "source_tree_sha256": "REVIEWED_TREE_SHA256",
  "guideline_sha256": "GUIDELINE_FILE_SHA256",
  "findings": "The reader's substantive overall findings from the actual manuscript read.",
  "issues": [
    {"id": "R1-1", "severity": "substantive", "finding": "A specific mathematical or reading issue identified by the reader."}
  ]
}
```

`severity` is `substantive` or `style`; issue IDs are unique within a round. An empty issues
list is allowed when supported by actual overall findings. Findings must be actual text,
not a PASS token or arbitrary JSON coerced to text. The minimum machine check is 20
non-padding characters; this is a malformed-evidence check, not a quality score.

## Writer disposition after each read

```json
{
  "writer_id": "actual-writer-id",
  "reader_report_sha256": "ACTUAL_READER_REPORT_FILE_SHA256",
  "before_source_tree_sha256": "REVIEWED_TREE_SHA256",
  "after_source_tree_sha256": "REVISED_TREE_SHA256",
  "revision_summary": "What the writer actually revised or decided to preserve, and why.",
  "responses": [
    {"issue_id": "R1-1", "action": "revised", "reason": "The concrete revision and how it addresses the reader's finding."}
  ]
}
```

Cover every issue exactly once. Actions are `revised` or `justified-no-op`; a no-op needs a
substantive reason. If the entire manuscript is unchanged, also provide
`no_change_reason` with substantive text, and do not claim any issue was revised. No
editorial change is mandatory merely to make a hash differ.

## Final post-revision verification

The second reader supplies:

```json
{
  "reviewer_id": "fresh-reader-two",
  "model": "gpt-6-astra",
  "provenance": {"kind": "post-revision-verification", "stylistic_round": false},
  "source_tree_sha256": "FINAL_TREE_SHA256",
  "guideline_sha256": "GUIDELINE_FILE_SHA256",
  "disposition_report_sha256s": ["FIRST_DISPOSITION_FILE_SHA256", "SECOND_DISPOSITION_FILE_SHA256"],
  "verdict": "PASS",
  "unresolved_substantive_issues": [],
  "findings": "Actual verification of both issue dispositions against the final manuscript."
}
```

This is a bounded verification of the revisions and justified decisions. A substantive
failure must be repaired and reverified on the resulting manuscript; do not treat it as a
PASS or restart an unbounded stylistic review cycle. Any later manuscript change makes the
final verification stale.

## Gates and compatibility

`paperctl gate` requires the complete evidence at `preservation` and `final`.
`paperctl audit --state STATE --require-all-gates` also requires it. Runs that already claim
preservation/final PASS are checked during ordinary audits. New runs record
`reader_round_policy: two-fresh-astra-v2`; current raw-required runs and legacy runs cannot
gain new release certification without the two cycles. Preliminary legacy inspection and
resume remain available. Existing raw, baseline, source, compression, and reader checks
continue to apply.
