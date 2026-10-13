# Host-fed API usage and cost accounting

`src/api_accounting.py` provides a standard-library SQLite ledger for usage that a model host
reports. It does not dispatch requests, inspect model sessions, discover missing usage, or claim
that a subscription was billed at API rates. A watcher or controller must call it with the usage
events it actually observes.

The CLI accepts one event object with the Python `record` argument names from stdin:

```text
scripts/merlean-cost --db run/accounting.sqlite3 --price-card assets/api-prices-2026-09-16.json record < usage-event.json
scripts/merlean-cost --db run/accounting.sqlite3 --price-card assets/api-prices-2026-09-16.json summary --equivalent-tier fast
```

The bundled card is a dated snapshot of the official [API price table](https://developers.openai.com/api/docs/pricing)
and [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) /
[Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol) model pages. Verify or replace
the card before a new pricing-sensitive campaign; it is not a live price lookup. In particular,
the Sol promotional rates have a stated availability period. A card change requires a new
ledger rather than silently rewriting historical costs. The frozen `gpt-5.6-sol` rate does
not price `gpt-6-sol` or `gpt-6.1-sol` workers: supply a verified rate for the selected model; otherwise cost
remains unknown. Model dispatch defaults never rewrite a historical price card.

For real-time use, the host/controller calls `record` whenever provider usage arrives and
refreshes `summary`. A usage-free start is `in_flight`; a failed call without final usage
remains unmetered. On Codex, prefer exact per-response `token_usage_record.payload.usage`
with `response_id` as the call ID. Do not ingest `thread_token_usage` or `turn_token_usage`
as if they were new response deltas. A collector should separately list pending calls
whose response IDs are not yet exposed. These files can contain private session metadata
and belong in project runtime storage, not a distributable agent package.

```python
from api_accounting import APIAccountingLedger

ledger = APIAccountingLedger("run/accounting.sqlite3", "admin/price-card.json")
ledger.record(
    call_id="actor-p1-round1",
    module="actor",
    model="gpt-6-astra",
    usage={
        "input_tokens": 120000,
        "cached_input_tokens": 80000,
        "cache_write_input_tokens": 10000,
        "output_tokens": 9000,
        "reasoning_output_tokens": 7000,
        "total_tokens": 129000,
    },
    status="in_flight",
    basis="subscription_api_equivalent",
    service_tier="standard",
    usage_mode="cumulative",
    usage_format="codex_flat",
    event_id="usage-event-17",
    metadata={"problem": "p1", "arm": "opaque-cell-2"},
)
summary = ledger.summary(equivalent_service_tiers=["fast"])
```

`call_id` is the stable identity of one provider request. `module` is the experiment or product
component to which the call belongs. Reusing a call ID with another module, model, service tier,
accounting basis, usage format/mode, or metadata is rejected. SQLite WAL mode plus immediate write
transactions serialize concurrent writers. A repeated `event_id` with identical content is an
idempotent retry, including replay of an earlier in-flight event after the call became terminal;
the replay returns the current call state. Reuse with different content is an error.

## Usage formats and updates

The normalized format uses `input`, `cached_read`, `cache_write`, `output`, and
`reasoning_output`. The explicit `codex_flat` format accepts `input_tokens`,
`cached_input_tokens`, `cache_write_input_tokens`, `output_tokens`,
`reasoning_output_tokens`, and optional `total_tokens`.

Input is inclusive: cached reads and cache writes are disjoint subsets of input. The remaining
input is charged at the uncached-input rate. Output is inclusive: reasoning output is a subset of
output and is reported separately but never added again for pricing or total-token counts. Missing
fields remain unknown; callers must send an explicit zero when the host reported zero.

`usage_mode="cumulative"` means each supplied value is the request total observed so far. Values
merge monotonically and a decrease is rejected. Omitted fields retain their previous state.
`usage_mode="delta"` means each object is one increment and requires `event_id`. Deltas are added
once. A field omitted from any delta remains incomplete even if other deltas reported it, so the
final total is not silently treated as zero.

Supported statuses are `in_flight`, `unknown`, `complete`, `failed`, and `cancelled`. The latter
three are terminal. A terminal status cannot change. Usage fields already known at the terminal
transition are frozen; a later cumulative report may fill a previously unknown field, after which
that field is frozen too. A new delta cannot be added to a terminal call because it would change a
final counter, although replay of an already-recorded delta event remains idempotent. A same-status
update may also attach a delayed actual billed amount.

## Price-card and cost semantics

The database is bound to the byte hash and contents of one validated price-card snapshot. The
summary reports its SHA-256, source URLs, retrieval timestamp, unit, currency, and basis. Reopening
the database with a different card fails rather than repricing historical calls silently.

Long-context pricing is selected independently for each call when inclusive input is strictly
greater than the card's threshold. It is never selected from an aggregate across calls. Service
tier multipliers apply after model and long-context rates. Unknown models and service tiers remain
unpriced.

The tier stored on a call is the API-equivalent pricing scenario, not evidence about how a
subscription request was served. Record `standard` when standard API equivalence is the requested
default and retain an unknown actual tier in metadata. `summary(equivalent_service_tiers=["fast"])`
adds a side-by-side fast scenario to every aggregate using the same call records; it does not
duplicate token counts or claim the fast tier was used.

For each module, model, and the total, `summary()` distinguishes:

- `api_equivalent_usd`: an exact final equivalent only when every included call is terminal and
  has all cost-relevant usage and a known price;
- `api_equivalent_usd_observed_exact_subset`: exact observed cost for the subset of calls whose
  current usage can be priced, or `null` when no such subset exists;
- `api_equivalent_usd_observed_lower_bound`: a conservative value for reported token components,
  clearly not a final estimate;
- `actual_billed_usd`: exact only when the host supplied an actual billed amount for every terminal
  call;
- `actual_billed_usd_observed_lower_bound`: the sum of actual amounts supplied so far.

The same aggregates appear under `by_module`, `by_model`, and nested
`by_module_model[module][model]`; these are views over the same rows and do not add calls or tokens
to the total. For a terminal call with complete usage, its lower-bound cost contribution equals
its exact cost. Partial or in-flight calls retain conservative observed lower bounds.

Token summaries follow the same rule: an exact field and its `*_complete` flag require every
included call to be terminal and to report that field. The corresponding
`*_observed_lower_bound` remains available during live calls. `missing_usage_call_count` identifies
calls with no reported usage at all; they contribute `null`, rather than zero, to equivalent-cost
lower bounds. `unpriced_call_count` separately identifies calls whose model or pricing tier is
absent from the card. Status and in-flight/unknown-call counts make partial summaries visible. A
zero is emitted only when zero was reported or when an empty aggregation is mathematically zero.

For subscription calls, leave `actual_billed_usd` unset. Their API-equivalent amount is a comparison
scenario under the frozen price card, not an invoice or claim about marginal subscription cost.


## Codex pilot host integration

The optional Codex pilot automatically feeds this ledger at stage launch and
completion, including errors and cancellation. See [Codex pilot](codex-pilot.md)
for per-response evidence, stage-level unknown metering and optional frozen price
cards. `APIAccountingLedger(path, price_card=None)` records genuinely unpriced
usage without inventing a rate. A response subtotal does not imply all stages
have reported usage; consult the host summary's metering completeness fields.

### Dispatch purpose and phase attribution

The transport accepts optional host-owned `accounting_context` containing exactly
`phase`, `segment_id`, and `purpose`, each a nonempty string. The stage record
retains that context before dispatch. Exact response rows also retain the problem,
host role, actual response model, session, turn, stage and timestamp. Conflicting
attribution for an existing response ID is an accounting error, never a second
charge or a silent reassignment.

`ledger.purpose_summary()` groups the same response rows by phase, segment,
problem, host role, purpose, session and actual model, using the same frozen price
card and arithmetic as `summary()`. The pilot writes the additive view to
`host/accounting/role-cost-summary.json`, with stage receipts, response/stage
aliases, pending or unmetered stages, and a metering-completeness flag. These
groups are alternative views, not additional costs to add to the total.

Purposes describe the task commissioned by the host, not a speculative analysis
of token content. Separate referee, route-scout and Lean implementation calls
can therefore be measured separately. A main call combining mathematical
reasoning and Lean planning remains one mixed-purpose call: exact provider usage
does not reveal how many tokens or dollars went to each topic. Legacy calls
without dispatch purpose remain unknown; do not invent a retrospective split.
Sol remains the delegated execution model, including bounded Lean implementation
and compile-fix in Lite mode.

Phase boundaries belong in an explicit external manifest. Preserve sealed
ledgers and price cards; use read-only immutable connections for sealed databases
and read-only transactions for active ones. Reconcile response IDs across
segments before any combined total, and retain missing/censored stages as
unknown even when every observed response has an exact price. Maintenance and
audit conversations outside the pilot transport are excluded unless their own
exact usage is separately available.
