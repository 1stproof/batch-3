# Reading research activity and evidence status

Use the deterministic observer command against an existing problem directory:

```sh
scripts/merlean-evidence-status --problem /path/to/run/campaign/problems/problem-id --output /path/outside-run/evidence-status.json
```

This explicit offline command reads existing records and creates one exclusive report outside the input run. It makes no model or network calls, adds no prompt or evidence tokens, and does not alter research, grades, calls, deadlines, counters, dispatch, or stop policy. Both provider bundles contain the same tool. This document is operator guidance, not an added runtime prompt or review requirement.

## Separate five kinds of observation

| Recorded dimension | What it establishes | What it does not establish |
| --- | --- | --- |
| Process activity | Stored call statuses and counts | Accepted output, scientific progress, or resource cost |
| Retained work | Number of archived research and auxiliary records | Independent novelty, nonredundancy, correctness, or gap closure |
| Artifact state | Current binding and distinct archived candidate bindings | Mathematical improvement; different bytes need not mean different substance |
| Independent evidence records | Current recorded observation references and recorded deficit statuses | Fresh authentication of those receipts or newly established independence |
| Acceptance | No acceptance is inferred by this tool | Activity, delivered input, a submitted candidate, or closed recorded deficits alone never award a grade |

Required-material delivery receipts record the delivery protocol's result. They do not prove comprehension, attention, or complete retained model context. A worker's context-loss self-report can coexist with a successful delivery receipt; neither automatically rewrites the other. A completed transport call is not an accepted independent review.

A timeout or exhausted bounded review without a verdict is not a mathematical rejection. Dispatch deduplication compares its authorized request/evidence key, not the content or usefulness of all subsequent thinking. Distinct self-check records can leave the candidate unchanged. Conversely, a long unchanged plateau can precede a genuine discovery: its length is not a mathematical stopping rule.

## Limits and operational decisions

The report summarizes records, not current scientific truth. It does not authenticate the review-exhaustion derivation, re-run independence checks, or calculate acceptance. Missing, malformed, oversized, or changing records produce explicit partial/unknown dimensions rather than zero. The compact convergence archive index and current candidate record are supported without loading all scientific bodies. The current record content hash is checked; the whole archived state and referenced reviewer records are not reconstructed or reauthenticated. Each input is capped at 32 MiB (up to six snapshots, 192 MiB total); an oversized host-progress file yields an unknown activity dimension while compact state remains reportable. Inputs are individually bounded and read twice; they are not an atomic campaign snapshot. Different current bindings across files are flagged. Counts cover the saved files, which may contain inherited history; they are not automatically counts for a current run or time window. Call identity duplicates are rejected rather than counted twice.

The current and continuation candidate hashes may agree while other records change between reads. Agreement is not proof of an atomic snapshot. Whole-file hashes bind the observed bytes; no raw scientific text, tool arguments, or session identities enter the report. Output is deterministic for identical input bytes and analyzer versions. The command refuses overwrite and output inside the input problem/run; keep reports in a separate observation directory.

An unchanged-binding count is an observation, not escalation authority. When scientific work is unchanged but required independent service remains unavailable, an operator should distinguish that operational blockage from an established mathematical gap. This tool does not automatically stop research, reopen exhausted review, prescribe a new strategy, or authorize a retry. Automatic suspension/escalation thresholds and new unchanged-review authority remain deferred policy questions. Never edit a proof cosmetically or manufacture a finding to obtain admission. Existing evidence, original-scope, independence, acceptance, and user-interruption rules remain authoritative.
