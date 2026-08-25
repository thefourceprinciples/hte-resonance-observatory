"""Deterministic reproducibility checks for TPAC reference experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .experiment import run_experiment
from .experiment_manifest import stable_hash


@dataclass(frozen=True)
class ReproducibilityResult:
    first_hash: str
    second_hash: str
    reproducible: bool
    differences: tuple[str, ...] = ()


def _fingerprint(result: dict[str, Any]) -> str:
    """Hash deterministic outputs, excluding environment- and time-dependent metadata."""
    payload = {
        "events": result["events"],
        "claims": result["run"].claims,
        "native_verification": result["native_verification"],
        "replay": {
            "valid": result["replay"].valid,
            "event_count": result["replay"].event_count,
            "state": result["replay"].state,
            "errors": result["replay"].errors,
        },
        "event_log_hash": result["event_log_hash"],
    }
    return stable_hash(payload)


def run_reproducibility_check() -> ReproducibilityResult:
    first = run_experiment()
    second = run_experiment()
    first_hash = _fingerprint(first)
    second_hash = _fingerprint(second)
    differences: list[str] = []
    if first_hash != second_hash:
        differences.append("reference experiment output fingerprint differs")
    return ReproducibilityResult(
        first_hash=first_hash,
        second_hash=second_hash,
        reproducible=not differences,
        differences=tuple(differences),
    )
