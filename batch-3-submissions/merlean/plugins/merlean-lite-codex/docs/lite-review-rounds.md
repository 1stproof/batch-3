# Lite review-round receipts

`src/lite_review_rounds.py` validates the provenance and internal consistency of a MerLean
Lite route's review–repair history. It is a standard-library, zero-setup checker. It does not
launch an agent, call an API, decide whether mathematics is correct, mutate a plan, or award
BRONZE, SILVER, or GOLD.

The checker binds each review and actor disposition to exact ledger bytes. It rejects stale or
escaping paths, contradictory verdicts, incomplete objection dispositions, and broken lineage
between consecutive ledger versions. Identity and context strings are declarations made by the
run. They are always labelled `self_reported`; without a separately authenticated host receipt,
the checker cannot prove that a model session was fresh or that an identity was genuine.

## API and command

From Python:

```python
from lite_review_rounds import validate_lite_review_rounds

summary = validate_lite_review_rounds(evidence_root, manifest)
```

`manifest` may be a parsed dictionary or a relative manifest path below `evidence_root`.
Malformed or stale evidence raises `ValueError`. A successful summary remains advisory and
always includes `"freshness_verified": false`.

The module also has a small command-line interface:

```text
python3 src/lite_review_rounds.py EVIDENCE_ROOT RELATIVE_MANIFEST_PATH
```

It prints the advisory JSON summary and exits zero on success. It prints one error and exits 2
on validation failure. The manifest path and every artifact path must be relative to the bound
evidence root. Symlinks and non-regular artifacts are rejected.

## Manifest

The manifest has one route and a nonempty sequence of rounds. Round numbers start at one and
are consecutive.

```json
{
  "schema_version": 1,
  "route_id": "route-alpha",
  "identity_provenance": "self_reported",
  "rounds": [
    {
      "round": 1,
      "actor_id": "actor-a",
      "reviewer_id": "reviewer-a",
      "actor_context_id": "actor-context-a",
      "reviewer_context_id": "review-context-a",
      "input_ledger": {"path": "ledger-v0.md", "sha256": "..."},
      "review": {"path": "review-v1.json", "sha256": "..."},
      "disposition": {"path": "disposition-v1.json", "sha256": "..."},
      "output_ledger": {"path": "ledger-v1.md", "sha256": "..."}
    }
  ]
}
```

Context IDs are optional. When both are supplied for a round, its actor and reviewer context IDs
must differ. Reusing a declared reviewer context across rounds is allowed: mandating uniqueness
would silently select a fresh-every-round research strategy. The summary reports
`declared_reviewer_contexts_unique` as a diagnostic only and always reports
`freshness_verified: false`. Actor and reviewer IDs are required and must differ within each
round. None of these checks authenticate the strings or establish fresh context.

This is the checker's strategy-neutral schema. The current Lite workflow in
`workflows/lite-research.md` requires fresh review for each revised candidate; a valid receipt
does not waive that requirement. A replacement actor records its own identity and the loss of
session continuity, including when it records abandonment of a route the old actor cannot resume.
Never impersonate the previous actor to preserve a continuity claim.

Every reference has exactly `path` and `sha256`. The digest is the lowercase SHA-256 of the
referenced file. A later round's input digest must equal the preceding round's output digest.
Ledger snapshots therefore need immutable versioned files; overwriting `ledger.md` after recording
its digest correctly makes the old receipt stale.

## Review record

Each `review-vN.json` has this shape:

```json
{
  "schema_version": 1,
  "route_id": "route-alpha",
  "round": 1,
  "identity_provenance": "self_reported",
  "input_ledger_sha256": "...",
  "reviewer_id": "reviewer-a",
  "reviewer_context_id": "review-context-a",
  "verdict": "objections",
  "first_blocker": "O1",
  "objections": [
    {
      "id": "O1",
      "step": "S3",
      "severity": "gap",
      "scope": "step",
      "content": "The boundary case is not justified.",
      "resolve": "Prove that case under the frozen hypotheses."
    }
  ],
  "survived": [
    {
      "id": "S2-review",
      "step": "S2",
      "disposition": "resolved",
      "rationale": "The displayed implication follows from S1."
    }
  ],
  "resolutions": []
}
```

`severity` is `fatal`, `gap`, or `nitpick`; `scope` is `step` or `representation`.
`first_blocker` names the first listed fatal/gap objection, or is `null` when there is none.
Nitpicks therefore leave it `null`. Objections and survived findings carry stable IDs that are
unique within a review.

The verdict rules are deliberately strict:

- `closed` has no unresolved fatal/gap or `conceded_by_exhaustion` finding. Nitpicks are allowed
  and still require actor dispositions.
- `triage_required` has no unresolved fatal/gap and at least one unresolved
  `conceded_by_exhaustion` finding. Nitpicks are allowed.
- `objections` has at least one unresolved fatal/gap and no fatal representation objection.
- `route_fatal` has at least one fatal representation objection.

A survived step is either `resolved` or `conceded_by_exhaustion`. The latter is never silently
coerced to resolution or closure; it remains visible for Lite's existing weakest-link triage.

Fatal/gap objections and `conceded_by_exhaustion` findings remain outstanding across later rounds,
even when a later review omits them. A later reviewer clears one only through an explicit stable
ID and step match:

```json
"resolutions": [
  {
    "id": "O1",
    "step": "S3",
    "rationale": "The revised ledger now proves the boundary case."
  }
]
```

An unknown ID or a changed step is rejected. Actor actions such as `revised` and `rebutted` do
not establish reviewer resolution by themselves.

## Disposition record

Each `disposition-vN.json` binds the actor's response and output ledger to the exact review:

```json
{
  "schema_version": 1,
  "route_id": "route-alpha",
  "round": 1,
  "identity_provenance": "self_reported",
  "actor_id": "actor-a",
  "actor_context_id": "actor-context-a",
  "input_ledger_sha256": "...",
  "review_sha256": "...",
  "output_ledger_sha256": "...",
  "responses": [
    {
      "objection_id": "O1",
      "action": "revised",
      "reason": "Added the missing boundary argument and updated its consumers."
    }
  ]
}
```

Responses cover every objection exactly once. An action is `revised`, `rebutted`, `deferred`,
or `route_abandoned`. `route_abandoned` is permitted only after `route_fatal`, which requires at
least one fatal representation objection to receive that response. These are actor dispositions,
not reviewer confirmation that a repair is correct. Confirmation comes only from a later review
whose input is the prior output ledger. A `revised` response with identical input/output ledger
digests is contradictory and rejected. Once a `route_fatal` review receives `route_abandoned`, it
is terminal for that route manifest; a rival route needs a new route ID and manifest.

The validator deliberately leaves mathematical and grading gates unchanged. A valid receipt says
which bytes were reviewed, what was reported, how the actor responded, and which bytes followed.
It does not turn those declarations into proof or independent verification.
