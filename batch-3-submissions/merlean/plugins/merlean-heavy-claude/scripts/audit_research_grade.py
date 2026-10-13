#!/usr/bin/env python3
"""Fail-closed semantic grade audit for MerLean research manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from research_grade import audit_manifest, record_audited_gold, verify_kernel_runtime  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--record-gold", action="store_true")
    parser.add_argument("--plan-data", type=Path)
    parser.add_argument("--statement-id")
    args = parser.parse_args()
    recording_args = (args.plan_data is not None, args.statement_id is not None)
    if args.record_gold != all(recording_args) or (any(recording_args) and not args.record_gold):
        parser.error("--record-gold requires both --plan-data and --statement-id")
    manifest_bytes = args.manifest.read_bytes()
    data = json.loads(manifest_bytes)
    if args.record_gold:
        errors = record_audited_gold(
            data, args.manifest.parent, args.manifest, manifest_bytes,
            args.plan_data, args.statement_id,
        )
    else:
        runtime_errors = verify_kernel_runtime(data, args.manifest.parent)
        errors = runtime_errors + audit_manifest(
            data, args.manifest.parent, kernel_runtime_verified=not runtime_errors,
        )
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    from original_scope import claims_original_completion
    print("PASS")
    if claims_original_completion(data):
        print("Original-question scope: passed (proof verification and publication remain separate gates).")
    else:
        print("Original-question scope: NOT CERTIFIED; this PASS grades only the selected local result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
