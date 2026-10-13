"""Writing profiles preserve full polishing and proof/release gates."""
from __future__ import annotations

PROFILES = ("standard", "exam")


def profile_defaults(name: str) -> dict:
    if name not in PROFILES:
        raise ValueError(f"unknown writing profile: {name}")
    return {
        "schema_version": 1, "profile": name,
        "readability_required": True, "compression_required": True,
        "polishing": "full",
    }



def literature_defaults() -> dict:
    return {
        "schema_version": 1, "assess_novelty": False,
        "request_human_authorization": False, "request_human_download": False,
        "unavailable_optional_source": "omit",
        "novelty_without_sufficient_evidence": "NOT_ASSESSED",
    }
