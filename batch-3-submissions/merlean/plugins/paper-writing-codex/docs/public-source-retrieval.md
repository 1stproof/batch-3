# Bounded public source retrieval

Public browsing is optional research infrastructure. Use it when a concrete mathematical
question or attribution need makes it useful; do not add a mandatory search or download phase.
Fresh runs default to browsing on. An explicit `internet_browse: false` or `--internet-browse off`
remains offline, including a saved run's unchanged policy. Do not seek official benchmark
answers, private material, or novelty claims as part of an exam answer.

Online scoped main and evidence-aware review stages retain their ordinary proof-document
capability and add two direct `merlean_documents` tools:

- `fetch_public_source({"url": "https://..."})` saves exact unauthenticated public bytes and
  returns an immutable source ID, hashes, paths and readable member index.
- `read_public_source({"source_id": "...", "member": "extracted/main.tex", "start": 0})`
  reads an indexed text member in chunks of at most 16,000 characters. Follow `next_start`
  until the necessary source has actually been inspected. The model cannot supply a file path.

The transport permits the existing native web tool or its audited literal web bridge for
search/open operations while preserving direct scoped document calls. The model metadata
field `supports_search_tool` remains false: it controls deferred tool discovery, not native
web browsing. Enabling it would hide the directly required document schemas. This does not enable
shell, patch, delegation, arbitrary execution or other MCP servers. Model roles are unchanged.
Offline scopes do not advertise or authorize public-source tools. Fresh manuscript-only
readers and visual reviews keep their existing limited inputs.

## Preserved citation standard

Follow `workflows/paper/references.md`: confirm the arXiv identity, retain the complete e-print
archive, inspect the exact result in its TeX source (including referenced inputs), and save
Export BibTeX verbatim. A public source fetch is evidence collection, never a `verified`
citation or a mathematical PASS. The writer and independent source auditor must inspect the
claim, source version, locator and use-site hypotheses. Metadata alone cannot establish this.
The public arXiv abs-page export button may select a publisher DOI export or arXiv's own
BibTeX endpoint; preserve the actual exported block and its provenance rather than inventing
an entry. If an endpoint refuses a request, record that outcome and follow the bounded fallback.

Raw bytes remain available for hashing and provenance. The reader exposes UTF-8 text, safely
extracted TeX/BibTeX and related textual source members. A PDF retains its original bytes;
when `pdftotext` is installed, bounded local conversion produces a separately hashed text
member. Missing conversion or unsupported encoding is explicit, not source verification.
Downloaded TeX is never executed. Compiling the authored manuscript remains a separate task.

## Limits and failure behavior

Each document store allows 16 unique URL admissions, at most 16 MiB per raw source, and a
64 MiB raw-byte budget. Redirects are limited to four. A fetch has a 30-second wall-time
budget; socket operations and PDF conversion have smaller limits within it. Archive extraction
uses the established safe extractor with tighter limits of 256 members and 24 MiB total
expanded content. PDF output has a 24 MiB file-size limit. These are retrieval safeguards,
not a cap on mathematical explanation or model reasoning.

Only credential-free HTTPS on port 443 is accepted. Every redirect and DNS result is checked;
private/local addresses are refused. The connection pins the checked IP while preserving
TLS hostname verification. No cookies, environment proxy credentials, authorization header,
paid access or signed private URLs are used.

A durable admission precedes each attempt. Success, refusal and timeout are cached. An
interrupted admission does not automatically retry. Unchanged failures do not trigger loops,
human download waits or repeated stage restarts. Use an accessible alternative within the
remaining finite budget when useful. Omit an unavailable optional citation under the existing
reference fallback. Preserve known credit; an essential dependency still needs a verified
alternative or already-supported self-contained argument. Otherwise disclose the unresolved
gap and continue other useful work without declaring the proof complete.

The download/archive worker and any subsequent PDF converter are separate direct children of
the MCP server and share the transport's process group. They do not create detached sessions.
The worker has no converter descendants, and each direct process is killed/reaped on its
own timeout. Transport cancellation reaches them through the existing stage process group.
A worker self-lifetime timer is a further bounded backstop. Lifecycle receipts remain host
process evidence; downloaded source JSON is untrusted data, never controller authority.

## Handoff and review

The cache lives at the host-chosen document store's `public-sources` directory. It is shared
across stages rather than reset per call. Research caches inside the problem directory enter
the immutable exam snapshot. Paper initialization can seed verified exact raw/text/receipt
bytes into its own stable cache without changing that snapshot. Failed and interrupted
admissions transfer too; a handoff does not refresh retry budgets. Source paths are computed
for the current cache while source IDs and content hashes remain stable.

Per-stage public-source calls have ordinary durable operation and model-visible-output
receipts, but never contribute to `required_artifact_coverage`. Reading new literature cannot
substitute for delivery of the original problem, proof, review or frozen research evidence.
