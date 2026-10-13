# Immutable raw reconstruction and editorial lineage

Read `mathematical-writing.md` first. The raw draft records the full mathematical account
supported by the assessed evidence before editorial optimization. Critical paths help locate
dependencies, but may be incomplete or unavailable. A Lite natural-language proof need not
have Lean coverage; its mathematical validity still needs review. Every research gap and
conditional premise must be identifiable. Raw-fidelity approval never awards a research grade.
Apply `reader-facing-paper.md`: preserve raw bytes and historical evidence faithfully, while
reviewing final prose for mathematical fidelity rather than repetition of workflow history.

## Three distinct artifacts

- Approved manuscript: the author's scope baseline, protected by normal refinement locks.
- `paper-raw.tex`: the preserved, evidence-backed natural-language reconstruction. Save it
  separately, including necessary proofs, source applications and explicit unresolved parts.
- `paper-vN.tex`: the editable version initialized from raw. Later `freeze-shrink` preserves
  a completed editorial draft before optional compression; it does not replace raw.

In refinement, derive N from the approved version, not from `paper-raw.tex`. Do not overwrite
an existing raw or skip a version. For later reconstructions choose a new explicitly recorded
raw output directory/version while preserving the original. If the old workflow did not save
raw, reconstruct it now and record `retrospective-reconstruction`; do not rename a polished
paper or claim it is a historical first draft. Reusing checked proof passages is legitimate
when their source and new reconstruction work are honestly recorded.

## Commands and actual evidence

After the critical-path/evidence-assessment gate and selection of scope, prepare the raw file
and its local dependencies. Obtain their hashes with:

```text
paperctl raw-inventory --source PAPER/paper-raw.tex
```

This bounded parser follows literal braced input/include/subfile, bibliography and graphics
paths and local class/package files; it is not a TeX interpreter. Use static root-relative
paths within the source directory. Unsupported routing must be made explicit before freezing;
never claim that an incomplete parser has captured arbitrary TeX behavior. Additional static
assets may be listed with `--asset PATH`. Compilation remains an independent check.

Main prepares evidence JSON containing actual records, not passing placeholders:

```json
{
  "schema_version": 1,
  "source_sha256": "<raw root hash>",
  "source_tree_sha256": "<raw-inventory tree hash>",
  "writer_ids": ["<actual raw writers>"],
  "selected_results": ["<formal or mathematical result identifiers>"],
  "source_records": [{
    "path": "<absolute source path>", "sha256": "<hash>",
    "kind": "natural-language",
    "findings": "<what was actually read and what it establishes>"
  }],
  "evidence_assessment": {"path": "<absolute path>", "sha256": "<hash>"},
  "reconstruction_map": {"path": "<absolute path>", "sha256": "<hash>"},
  "critical_path_unavailable_reason": "<only if no useful critical-path record exists>",
  "independent_audit": {"path": "<absolute path>", "sha256": "<hash>"}
}
```

Source kinds are `lean`, `natural-language`, `literature`, or `research-status`.
Lean records may add exact `declarations`. When a useful dependency record exists, use
`critical_path: {path, sha256}` instead of the unavailable reason. The reconstruction map
relates selected claims and necessary inferences to raw locations and supporting evidence;
classify available graph nodes without equating module imports with used declarations.
An absent Lean file is not a reason to fabricate one or omit a supported result.

The independent reviewer writes a typed report with `reviewer_id`, `verdict`,
`raw_source_sha256`, `raw_source_tree_sha256`, `unresolved_fidelity_issues`, `research_gaps`,
and substantive `findings`. A PASS has no unresolved fidelity issues; explicitly represented
research gaps can remain. Its author must differ from raw writers. The review must assess the
argument and status honestly; hashes and identity declarations do not authenticate independence.

```text
paperctl freeze-raw --state WORK/00-run-state.json --source PAPER/paper-raw.tex \
  --origin retrospective-reconstruction --evidence WORK/01-raw-evidence.json
paperctl start-from-raw --state WORK/00-run-state.json
```

Use `pre-editorial` for a genuinely current pre-editorial reconstruction. Freeze stores the
root, dependency files, evidence and a manifest under `WORK/raw/`. Both original inputs and
snapshot hashes are checked afterwards. Do not mutate evidence frozen with raw: append new
review records separately. `start-from-raw` seeds the still-reserved editable output and an
exclusive version-specific support directory, preserving approved baseline and raw. It is
not allowed to overwrite an already edited candidate. Legacy runs are readable, but cannot
claim this new raw guarantee without explicit reconstruction/migration and reopened gates.

## Final raw-to-edited review

In addition to the approved-baseline and fresh-reader checks, obtain an actual independent
`08-raw-preservation-audit.json` with `reviewer_id`, all editor `writer_ids`, `verdict: PASS`,
`unresolved_fidelity_issues: []`, `raw_manifest_sha256`, `baseline_sha256`, and
`candidate_source_tree_sha256` from `paperctl raw-inventory --state WORK/00-run-state.json` (including
static graphics and local classes/styles, not merely the prose inventory). Include concrete findings
for `hypotheses`, `proof_bridges`, `research_status`, and `omissions_and_relocations`.
This must explain where essential raw mathematics is retained or accurately cited, why any
omitted material is unnecessary, and whether status/conditions changed. Core arguments may
not exist solely in raw. A current independent PASS is required at preservation/final release.

The runtime protects recorded file integrity, seed lineage, and current audit bindings. It
cannot prove mathematical truth, recover lost historical text, or establish real reviewer
independence. Publishing an article with open proof gaps is not authorized by a raw PASS;
label incomplete drafts honestly and seek research authority when completion requires it.
