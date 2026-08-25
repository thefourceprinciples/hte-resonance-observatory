"""Deterministic reproducibility checks for TPAC reference experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .experiment_manifest import stable_hash
from .experiment import run_reference_experiment


@dataclass(frozen=True)
class ReproducibilityResult:
    first_hash: str
    second_hash: str
    reproducible: bool
    differences: tuple[str, ...] = ()


def _fingerprint(result: Any) -> str:
    """Hash the deterministic experiment outputs that should remain stable."""
    payload = {
        "events": [event.to_dict() for event in result.events],
        "claims": [claim.to_dict() for claim in result.claims],
        "verification": result.verification,
    }
    return stable_hash(payload)


def run_reproducibility_check() -> ReproducibilityResult:
    first = run_reference_experiment()
    second = run_reference_experiment()
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
