# Paper checkpoints at cooperative drain

Cooperative drain is control flow, not an author repair request. The paper runner records interruption and does not dispatch a contextual repair. A call denied before admission restores its previous retrieval checkpoint; it does not consume or reset a retrieval turn. An existing admitted turn remains subject to normal transport reconciliation.

Older hosts could leave a zero-turn `repair-<stage>` marker after a pipeline drain followed by a denied contextual repair. Native paper restoration reconciles only this exact pattern: the original writer is authenticated, both drain errors exist, no evidence request or matching admission/call/transport exists, and all earlier calls have terminal ownership evidence. The zero marker is retained in a reconciliation receipt before removal. Missing, ambiguous or changed evidence fails closed. The next ordinary stage uses the same writer and the original allowance.

This source repair does not authorize live per-problem reentry. Deploy it through a separately audited native continuation only after the active stack is safely terminal or an authorized cooperative pause has completed. Research, paper findings, prior responses and the original exam clock remain unchanged.
