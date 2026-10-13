#!/usr/bin/env python3
"""Audit rendered referee prose against rendered target-paper vocabulary.

Vocabulary and unattested phrases are suggestions by default. Use --strict-vocabulary
only when exact target-paper word membership is explicitly required. Em dashes remain
hard failures in either mode; PDF/source build validation always applies.
PDF text is extracted with ``pdftotext`` so TeX macros cannot hide words from the audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


COLLOCATION_STOPWORDS = frozenset(
    """
    a about above after again against all also am an and any are as at be because been before
    being below between both but by can cannot could did do does doing down during each few for
    from further had has have having he her here hers herself him himself his how i if in into
    is it its itself just me more most my myself no nor not now of off on once only or other our
    ours ourselves out over own same she should so some such than that the their theirs them
    themselves then there these they this those through to too under until up very was we were
    what when where which while who whom why will with would you your yours yourself yourselves
    every give gives given make makes made need needs needed provide provides provided state
    states stated show shows shown use uses used using
    """.split()
)

EM_DASH_PATTERNS = (
    ("unicode-em-dash", "\N{EM DASH}"),
    ("tex-three-hyphens", "---"),
    ("tex-textemdash", r"\textemdash"),
    ("tex-emdash", r"\emdash"),
)


@dataclass(frozen=True)
class Token:
    word: str
    line: int
    segment: int


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def raw_rendered_text(path: Path) -> str:
    """Extract a PDF or read a UTF-8 plain-text attachment, failing closed."""

    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".pdf":
        executable = shutil.which("pdftotext")
        if executable is None:
            raise RuntimeError("pdftotext is required to audit rendered PDF prose")
        result = subprocess.run(
            [executable, "-raw", str(path), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
        text = result.stdout
    else:
        text = path.read_text(encoding="utf-8", errors="strict")
    if not any(character.isalpha() for character in text):
        raise RuntimeError(f"rendered text extraction produced no words: {path}")
    return text


def normalize_rendered_text(text: str, *, join_line_hyphens: bool) -> str:
    """Normalize accents and choose one interpretation of PDF line-end hyphens."""

    text = unicodedata.normalize("NFKC", text)
    replacement = r"\1\2" if join_line_hyphens else r"\1 \2"
    return re.sub(r"([^\W\d_])-[ \t]*\n[ \t]*([^\W\d_])", replacement, text)


def rendered_text(path: Path, *, join_line_hyphens: bool = True) -> str:
    """Return normalized rendered text from a PDF or plain-text attachment."""

    return normalize_rendered_text(
        raw_rendered_text(path), join_line_hyphens=join_line_hyphens
    )


def normalize_report_text(text: str, target_words: set[str]) -> str:
    """Resolve each report line-end hyphen using the target vocabulary."""

    text = unicodedata.normalize("NFKC", text)

    def replace(match: re.Match[str]) -> str:
        left, right = match.group(1), match.group(2)
        if (left + right).casefold() in target_words:
            return left + right + "\n"
        if left.casefold() in target_words and right.casefold() in target_words:
            return left + " " + right + "\n"
        return left + right + "\n"

    return re.sub(
        r"([^\W\d_]+)-[ \t]*\n[ \t]*([^\W\d_]+)",
        replace,
        text,
        flags=re.UNICODE,
    )


def expanded_target_source(root_tex: Path) -> str:
    """Expand the exact root TeX include graph."""

    if not root_tex.is_file():
        raise FileNotFoundError(root_tex)
    latexpand = shutil.which("latexpand")
    if latexpand is None:
        raise RuntimeError("latexpand is required for target PDF hyphenation")
    expanded = subprocess.run(
        [latexpand, "--fatal", str(root_tex)],
        cwd=root_tex.parent,
        check=True,
        capture_output=True,
        text=True,
    )
    return expanded.stdout


def detex_target_source(expanded: str, root_tex: Path) -> str:
    """Extract visible prose from expanded target TeX."""

    detex = shutil.which("detex")
    if detex is None:
        raise RuntimeError("detex is required for target PDF hyphenation")
    extracted = subprocess.run(
        [detex, "-n", "-l"],
        cwd=root_tex.parent,
        input=expanded,
        check=True,
        capture_output=True,
        text=True,
    )
    if not any(character.isalpha() for character in extracted.stdout):
        raise RuntimeError(f"target TeX extraction produced no words: {root_tex}")
    return unicodedata.normalize("NFKC", extracted.stdout)


def target_source_text(root_tex: Path) -> str:
    """Extract visible prose from the exact root TeX and its actual include graph."""

    expanded = expanded_target_source(root_tex)
    return detex_target_source(expanded, root_tex)


def resolve_target_pdf_text(text: str, root_tex: Path) -> str:
    """Resolve PDF line-end hyphens from words and pairs in the exact root TeX."""

    expanded = expanded_target_source(root_tex)
    source_tokens = tokenize(detex_target_source(expanded, root_tex))
    loose_source = unicodedata.normalize("NFKC", expanded)
    loose_source = loose_source.replace(r"\-", "")
    loose_source = re.sub(
        r"\\(?:cite\w*|label|ref|eqref|pageref|url|path|includegraphics)"
        r"\*?(?:\s*\[[^\]]*\])?\s*\{[^{}]*\}",
        " ",
        loose_source,
    )
    loose_source = re.sub(r"\\[A-Za-z@]+\*?", "", loose_source)
    loose_source = re.sub(r"[{}$]", "", loose_source)
    source_tokens.extend(tokenize(loose_source))
    source_words = {token.word for token in source_tokens}
    source_pairs = {
        (left.word, right.word)
        for left, right in zip(source_tokens, source_tokens[1:])
        if left.segment == right.segment
    }
    text = unicodedata.normalize("NFKC", text)

    def replace(match: re.Match[str]) -> str:
        left, right = match.group(1), match.group(2)
        joined = (left + right).casefold()
        split = (left.casefold(), right.casefold())
        join_attested = joined in source_words
        split_attested = split in source_pairs
        if join_attested == split_attested:
            raise RuntimeError(
                "ambiguous target PDF line-end hyphen "
                f"{left}-{right} against {root_tex}"
            )
        return (left + right if join_attested else left + " " + right) + "\n"

    return re.sub(
        r"([^\W\d_]+)-[ \t]*\n[ \t]*([^\W\d_]+)",
        replace,
        text,
        flags=re.UNICODE,
    )


def tokenize(prose: str) -> list[Token]:
    """Tokenize prose while preserving inflection and ignoring visual line wrapping."""

    prose = prose.replace("\N{LEFT SINGLE QUOTATION MARK}", "'")
    prose = prose.replace("\N{RIGHT SINGLE QUOTATION MARK}", "'")
    tokens: list[Token] = []
    segment = 0
    previous_end = 0
    line = 1
    word_pattern = r"[^\W\d_]+(?:'[^\W\d_]+|')?"
    for match in re.finditer(word_pattern, prose, flags=re.UNICODE):
        between = prose[previous_end : match.start()]
        line += between.count("\n")
        if re.search(r"[.!?;:]|\n\s*\n", between):
            segment += 1
        word = match.group(0)
        opened_by_quote = match.start() > 0 and prose[match.start() - 1] == "'"
        if word.endswith("'") and (opened_by_quote or not word[-2].casefold() == "s"):
            word = word[:-1]
        tokens.append(Token(word=word.casefold(), line=line, segment=segment))
        previous_end = match.end()
    return tokens


def input_rendered_files(paths: Iterable[Path]) -> list[Path]:
    """Validate explicit rendered-paper files while preserving source-root order."""

    files: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(path)
        resolved = path.resolve()
        if resolved not in seen:
            files.append(path)
            seen.add(resolved)
    return files


def content_phrases(tokens: list[Token]) -> dict[tuple[str, ...], list[int]]:
    """Collect adjacent two- to four-word content phrases within rendered segments."""

    phrases: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for width in range(2, 5):
        for start in range(0, len(tokens) - width + 1):
            window = tokens[start : start + width]
            if any(token.segment != window[0].segment for token in window):
                continue
            if any(
                token.word in COLLOCATION_STOPWORDS or len(token.word) < 3
                for token in window
            ):
                continue
            phrase = tuple(token.word for token in window)
            phrases[phrase].append(window[0].line)
    return phrases


def validate_report_build(
    report_rendered: Path, report_source: Path, manifest_path: Path | None
) -> dict[str, object] | None:
    """Bind a compiled report PDF to its source and successful build record."""

    if report_rendered.suffix.lower() != ".pdf":
        return None
    if manifest_path is None:
        raise RuntimeError("a report build manifest is required for a rendered PDF")
    try:
        manifest = json.loads(
            manifest_path.read_text(encoding="utf-8", errors="strict")
        )
    except json.JSONDecodeError as error:
        raise RuntimeError(f"invalid report build manifest: {manifest_path}") from error
    expected = {
        "report_source_sha256": sha256(report_source),
        "report_rendered_sha256": sha256(report_rendered),
        "compile_exit_code": 0,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise RuntimeError(f"report build manifest mismatch for {key}")
    command = manifest.get("compile_command")
    if (
        not isinstance(command, list)
        or not command
        or not all(isinstance(item, str) and item for item in command)
    ):
        raise RuntimeError(
            "report build manifest needs a nonempty compile_command list"
        )
    return manifest


def audit(
    targets: list[Path],
    report_rendered: Path,
    report_source: Path,
    max_collocations: int,
    report_build_manifest: Path | None = None,
    target_source_roots: list[Path] | None = None,
    strict_vocabulary: bool = False,
) -> dict[str, object]:
    """Check report integrity and return optional vocabulary and phrase suggestions."""

    build_manifest = validate_report_build(
        report_rendered, report_source, report_build_manifest
    )
    source_roots = target_source_roots or []
    has_target_pdf = any(target.suffix.lower() == ".pdf" for target in targets)
    if (
        has_target_pdf
        and (strict_vocabulary or source_roots)
        and len(source_roots) != len(targets)
    ):
        raise RuntimeError(
            "one exact --target-source-root is required for each rendered target PDF"
        )
    extraction_notes: list[str] = []
    target_documents: list[list[Token]] = []
    for index, target in enumerate(targets):
        raw_target = raw_rendered_text(target)
        if target.suffix.lower() == ".pdf":
            resolved = normalize_rendered_text(raw_target, join_line_hyphens=True)
            if source_roots:
                try:
                    resolved = resolve_target_pdf_text(raw_target, source_roots[index])
                except (RuntimeError, subprocess.CalledProcessError) as error:
                    if strict_vocabulary:
                        raise
                    extraction_notes.append(f"{target}: PDF text fallback; {error}")
            else:
                extraction_notes.append(
                    f"{target}: PDF text only; line-end hyphenation is approximate."
                )
        else:
            resolved = unicodedata.normalize("NFKC", raw_target)
        target_documents.append(tokenize(resolved))
    target_words = {token.word for document in target_documents for token in document}
    report_rendered_raw = raw_rendered_text(report_rendered)
    report_rendered_text = normalize_report_text(report_rendered_raw, target_words)
    report_tokens = tokenize(report_rendered_text)
    report_raw = report_source.read_text(encoding="utf-8", errors="strict")

    missing: dict[str, list[int]] = defaultdict(list)
    for token in report_tokens:
        if token.word not in target_words:
            missing[token.word].append(token.line)

    target_phrases: set[tuple[str, ...]] = set()
    for document in target_documents:
        target_phrases.update(content_phrases(document))
    report_phrases = content_phrases(report_tokens)
    all_unattested = [
        {"phrase": " ".join(phrase), "lines": sorted(set(lines))}
        for phrase, lines in sorted(report_phrases.items())
        if phrase not in target_phrases
    ]
    total_unattested = len(all_unattested)
    truncated = max_collocations >= 0 and total_unattested > max_collocations
    unattested = (
        all_unattested if max_collocations < 0 else all_unattested[:max_collocations]
    )

    em_dashes: list[dict[str, object]] = []
    for kind, pattern in EM_DASH_PATTERNS:
        for line_number, line_text in enumerate(report_raw.splitlines(), start=1):
            if pattern in line_text:
                em_dashes.append(
                    {"kind": kind, "line": line_number, "origin": "source"}
                )
    for line_number, line_text in enumerate(report_rendered_raw.splitlines(), start=1):
        if "\N{EM DASH}" in line_text:
            em_dashes.append(
                {"kind": "unicode-em-dash", "line": line_number, "origin": "rendered"}
            )

    return {
        "hard_checks_pass": not em_dashes and (not strict_vocabulary or not missing),
        "strict_vocabulary": strict_vocabulary,
        "manual_phrase_review_required": strict_vocabulary and total_unattested > 0,
        "phrase_review_suggested": total_unattested > 0,
        "target_extraction_notes": extraction_notes,
        "target_rendered_files": [str(path) for path in targets],
        "target_rendered_sha256": {str(path): sha256(path) for path in targets},
        "target_source_roots": [str(path) for path in source_roots],
        "target_source_sha256": {str(path): sha256(path) for path in source_roots},
        "report_rendered": str(report_rendered),
        "report_rendered_sha256": sha256(report_rendered),
        "report_source": str(report_source),
        "report_source_sha256": sha256(report_source),
        "report_build_manifest": (
            str(report_build_manifest) if report_build_manifest is not None else None
        ),
        "report_build_manifest_sha256": (
            sha256(report_build_manifest) if report_build_manifest is not None else None
        ),
        "report_build_manifest_validated": build_manifest is not None,
        "report_word_count": len(report_tokens),
        "target_vocabulary_size": len(target_words),
        "missing_words": [
            {"word": word, "lines": sorted(set(lines))}
            for word, lines in sorted(missing.items())
        ],
        "em_dashes": em_dashes,
        "unattested_content_phrases": unattested,
        "unattested_content_phrases_total": total_unattested,
        "unattested_content_phrases_truncated": truncated,
        "phrase_note": (
            "Review phrase candidates under the explicitly selected strict policy; "
            "an unattested phrase is not an automatic error."
            if strict_vocabulary
            else "Optional wording suggestions only; no per-phrase review or ledger is required."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target-rendered",
        type=Path,
        nargs="+",
        required=True,
        help="Exact target-version PDF or rendered plain-text file(s).",
    )
    parser.add_argument(
        "--target-source-root",
        type=Path,
        nargs="+",
        help="Optional exact root TeX files in target order; required for target PDFs in strict mode.",
    )
    parser.add_argument(
        "--report-rendered",
        type=Path,
        required=True,
        help="Current compiled report PDF or final plain-ASCII report.",
    )
    parser.add_argument(
        "--report-source",
        type=Path,
        required=True,
        help="Current TeX or plain-ASCII report source, used for source-level dash checks.",
    )
    parser.add_argument(
        "--report-build-manifest",
        type=Path,
        help="Required JSON build record when --report-rendered is a PDF.",
    )
    parser.add_argument(
        "--strict-vocabulary",
        action="store_true",
        help="Make outside-target words hard failures and require exact TeX evidence for target PDFs.",
    )
    parser.add_argument(
        "--max-collocations",
        type=int,
        default=-1,
        help="Maximum phrase candidates to print; the default -1 prints all.",
    )
    parser.add_argument(
        "--json", action="store_true", help="Print structured JSON output."
    )
    parser.add_argument(
        "--json-out", type=Path, help="Write structured JSON to this file."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        targets = input_rendered_files(args.target_rendered)
        result = audit(
            targets,
            args.report_rendered,
            args.report_source,
            args.max_collocations,
            args.report_build_manifest,
            args.target_source_root,
            args.strict_vocabulary,
        )
    except (
        FileNotFoundError,
        RuntimeError,
        UnicodeError,
        subprocess.CalledProcessError,
    ) as error:
        raise SystemExit(f"language audit failed: {error}") from error
    rendered_json = json.dumps(result, indent=2, sort_keys=True)
    if args.json_out is not None:
        args.json_out.write_text(rendered_json + "\n", encoding="utf-8")
    if args.json:
        print(rendered_json)
    elif args.json_out is None:
        print("HARD CHECKS PASS" if result["hard_checks_pass"] else "HARD CHECKS FAIL")
        print(result["phrase_note"])
        print(f"missing words: {len(result['missing_words'])}")
        for item in result["missing_words"]:
            print(f"  {item['word']}: lines {item['lines']}")
        print(f"em dashes: {len(result['em_dashes'])}")
        for item in result["em_dashes"]:
            print(f"  {item['kind']}: line {item['line']}")
        print(
            "unattested content phrase candidates: "
            f"{len(result['unattested_content_phrases'])} of "
            f"{result['unattested_content_phrases_total']}"
        )
        for item in result["unattested_content_phrases"]:
            print(f"  {item['phrase']}: lines {item['lines']}")
    raise SystemExit(0 if result["hard_checks_pass"] else 1)


if __name__ == "__main__":
    main()
