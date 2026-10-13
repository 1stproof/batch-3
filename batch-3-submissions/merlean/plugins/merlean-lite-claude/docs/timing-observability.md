# Offline timing observation

Run this explicit command outside a research agent to summarize existing transport
records. It does not launch a model, request a tool read, change a run, or insert
anything into a prompt or scientific evidence.

```sh
scripts/merlean-timing /path/to/run/host/runtime/problem/001-proof-review \
  /path/to/run/host/runtime/problem/002-proof-review \
  --output /outside-the-run/timing-report.json
```

The output must be new and outside every input run. Inputs are bounded,
no-follow, twice-identical prefixes. Appends, incomplete final lines, caps,
missing records, unmatched calls and invalid clocks are explicit. A growing
stream is not an atomic snapshot. The command never retries an unstable input
or overwrites an output; inspect a later snapshot explicitly.

The report uses existing stage-local `elapsed_s` event clocks. Paired document
call start/completion envelopes yield **client-observed intervals**, not actual
server service, network latency or model thinking time. It reports both summed
intervals and their union/overlap; outside the union remains unclassified.
Missing horizons are unknown, not zero. Contradictory clocks suppress duration
attribution. Recorded UTC stage boundaries are a separate clock domain, not an
anchor for reconstructing every monotonic timestamp. Duplicate inherited stage
copies are excluded only when their identity and snapshot hashes agree.

Coverage is reported from the existing document audit, without granting new
coverage or acceptance authority. A last read completion is not proof of full
input delivery. Fresh sessions and recorded same-reviewer recovery remain
separate. Timeouts and cancellations are censored observations, never zero cost.
Unrecorded host preparation, provider queue, model reading/inference, network
and server-exclusive time remain unavailable.

The core report is deterministic for fixed input snapshots, limits and analyzer
bytes. Its deduplication key binds those inputs and limits. CLI stdout separately
reports offline analysis/serialization/write wall time and output size; that
cost excludes interpreter startup and receipt output. No hot-path tracer was
added, so there is no runtime tracing-on/off claim. At most128 stage paths and256 numeric document-interval details per stage are
reported; omitted detail counts and aggregate gap statistics remain explicit.
Memory/input limits default
to128MiB per file,100,000 complete event lines and8MiB per line; smaller limits
are available via `--max-bytes`, `--max-lines` and `--max-line-bytes`. Elapsed values must be finite, nonnegative and no greater than10^12seconds
(an analyzer numeric-safety bound, not a research time limit). Caps never
turn partial observations into complete records. Reports contain bounded IDs,
counts and durations, not prompt, argument or result contents.

For periodic use, a host supervisor may select newly terminal stages and cache
by the report's deduplication key, outside the campaign. Do not infer avoidable
overhead or reasoning quality from elapsed time alone. No scientific, billing,
acceptance or performance-equivalence conclusion follows from this report.
