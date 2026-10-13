# Saved request-only writer continuation

A completed writer response containing only `evidence_requests` is a retrieval instruction, never a substantive revision or an accepted paper. The request-only handler authenticates the saved raw response, transport, original writer, capability, scoped bytes and tool-delivery receipts before resuming it. Historical errors and rejected responses remain unchanged.

A pending `repair-<stage>` belongs to that exact semantic paper stage and resumes the original writer. Exact numbered call identities prevent a `repair-release-audit` call from being confused with `release-audit`. The next dispatch consumes the next turn from the original four-turn allowance; it does not allocate another allowance. Release gates and contextual repair validation still run normally.

Writers should read work artifacts already included in `stage-input.artifacts` there. For targeted delivery, `work/<exact key>` can identify a string member of that authenticated saved object. The host materializes only those exact UTF-8 bytes into a fixed text artifact and records the source-object and member hashes. It never substitutes a same-named live work file. Missing members remain explicitly unavailable. The next substantive answer requires complete delivery of the resulting scope.

Native continuation retains original capabilities and transport receipts. The handler maps only their confined, hash-identical copied artifacts into the successor's paper directory; the ancestor need not remain accessible. Restoring the same request is idempotent and does not consume a dispatch. A completed substantive correction found after a crash is not automatically replayed or accepted: the existing fail-closed substantive-response guard remains in force, retaining the consumed turn and requiring explicit reconciliation.

This supports protocol correction, not scientific editing by the host. An operations agent may investigate and deploy this generic lifecycle repair using native stopped-parent continuation. The original author must produce any revision, and all independent and release checks remain authoritative.
