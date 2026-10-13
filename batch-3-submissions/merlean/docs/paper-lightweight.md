# Lightweight exam papers

Fresh exam configurations select `paper_engine: lightweight-v1`. The original
research-to-paper boundary is 22.75 hours of the same 24-hour campaign. Saved clocks
and saved legacy paper engines are never changed by loading a newer release.

Before the boundary, paper writing requires native authenticated research completion
for the exact original question and selected answer. It reuses the existing original
scope reviews; it does not buy a duplicate scope-model call. Failed or stale research
acceptance prevents early writing. At the boundary an honest partial/unsolved answer
may be written, without reporting research complete or substituting another problem.
The final independent paper reviewer must explicitly recheck objects, quantifiers,
hypotheses and conclusion against that original question.

The default sequence is a tool-capable author, first fresh manuscript reader,
author revision, second fresh manuscript reader, author revision, second-reader
verification, separate mathematical/source reviewer, host compilation/rendering and
independent visual inspection. Both author dispositions can be justified no-ops.
Reviewer sessions are distinct from the writer; the second-reader verification uses
that reader's original session. A substantive failure returns to the original writer
within four contextual repairs, then obtains new reader checks. A scope mismatch
blocks publication; it is not repaired by cosmetic restatement.

The author edits a self-contained `author/paper.tex`, with source text/version and
bibliographic exports in `author/references/`. Scoped file/retrieval/compiler tools
provide useful author operations without unrestricted host shell access. Fresh
readers receive only the complete manuscript and neutral reading instructions. The
final reviewer additionally sees exact selected research and primary source evidence.
Full historical research is optional reference material, not a compulsory repeated
dossier. No generated inventory, seventeen-file ledger, validator-source dump or
model ledger-finalization stage is required.

The latest substantive guidance remains: correct complete reasoning; definitions and
key bridges; reconsideration of obscure invented terminology; useful brevity rather
than deletion of necessary steps; accurate source/use-site credit; and natural,
self-contained arXiv-style exposition rather than an audit diary. The author considers
relevant literature for both the problem and methods, checks actual primary PDF/TeX
content and retains official metadata exports when available. Optional retrieval
failure is reported honestly and does not cause an endless search loop. Essential
unsupported premises cannot receive independent publication PASS.

`light-paper-ledger.json` retains concise call identities, dispositions, source hashes,
independent reports and checkpoint state. A completed pending transport response is
reconciled before a new call; raw responses and the author workspace must match their
transport hashes. An ambiguous interrupted admission fails closed for native ownership
reconciliation. The host publishes `paper.tex` and `final.pdf` only with current source,
review and compilation bindings. `verify_completed(folder, host)` performs read-only
validation for observation and export. A review PASS is independent model evidence,
not a formal proof of mathematical correctness or a new research grade.

Historical `paper-ledger.json` uses the old engine and old gates unchanged. Selecting
the new engine against such a ledger is rejected; this release is a prospective
workflow replacement, not a silent migration or reset of unfinished legacy work.
