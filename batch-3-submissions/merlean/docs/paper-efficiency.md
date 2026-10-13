# Paper context and efficient revision

A paper is a self-contained mathematical result, not a replay of its development.
Internal histories remain available for fidelity and source checks; the manuscript
presents the question, results, hypotheses, arguments, necessary limitations and
relevant literature. See `workflows/paper/reader-facing-paper.md`.

The implemented context reduction is deliberately lossless. Long artifact strings
that are byte-identical are included once in `artifacts`; `artifact_aliases` maps
each duplicate name to its exact target, UTF-8 SHA-256 and media type. Alias chains
and conflicting or changed content are rejected. Frozen `work/<name>` requests
resolve the same bytes from the saved stage input. Distinct historical inventories,
accepted proof text, hypotheses, source/use-site evidence, unresolved findings and
independent judgments are not summarized or discarded. Finalization includes the
coverage validator once under `validator_schemas["coverage.py"]`.

Full chronological replay is not required on every turn, but this version does not
implement lossy historical summaries or claim that a compact synopsis can replace
scientific evidence. Future role-specific context projections require evidence that
the omitted fields are irrelevant to that role, with original artifacts still
reachable and all mandatory scientific reads preserved.

For either author response to an independent reader, a justified no-op may omit
`tex` and return `unchanged_manuscript_sha256`, a substantive revision summary,
issue dispositions and a no-change reason. The host checks the current manuscript
hash and rejects a simultaneous `tex` field. The call still consumes its ordinary
allowance. Both fresh readers, second-reader verification, real compilation,
rendering, independent proof/source review and release checks remain required.
Unchanged sidecars need not be returned again.

An explicit independent reader-sidecar FAIL is surfaced immediately after the
proof audit is preserved, before broad finalization. The existing bounded author
repair receives the exact findings and report binding; it cannot modify independent
reports. A successful correction returns through full independent proof audit.
No review is automatically marked PASS and the four-repair limit is unchanged.
This narrows failure routing, not the mathematical or release standard.

Fixture size reductions measure serialized input bytes, not wall-clock performance
or model quality. No performance equivalence is claimed without actual evidence.

Author revision, polish and contextual repair also expose optional restoration
artifacts through scoped `read_artifact`: the saved raw manuscript, verified against
its frozen raw manifest, and a draft snapshot matching the host pre-shrink inventory
hash. Captured copies are immutable inputs for that call. Missing sources are reported
unavailable; the current manuscript is never substituted for a missing earlier one.
These optional files are not given to isolated readers and do not add mandatory
history reads. Reader task guidance explicitly checks terminology and omitted key
steps without changing the saved neutral rubric or adding another review round.
