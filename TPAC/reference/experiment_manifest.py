"""Generate reproducibility manifests for TPAC reference experiments."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


def stable_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()
    return hashlib.sha256(payload).hexdigest()


@dataclass
class ExperimentManifest:
    experiment_id: str
    tpac_version: str
    commit_sha: str
    runtime: dict[str, str]
    configuration_hash: str
    input_hash: str
    event_log_hash: str
    expected_invariants: list[str]
    observed_results: dict[str, Any]
    fault_injections: list[dict[str, Any]] = field(default_factory=list)
    replay_result: dict[str, Any] = field(default_factory=dict)
    conformance_verdict: str = "INDETERMINATE"
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_manifest(
    *,
    experiment_id: str,
    tpac_version: str,
    commit_sha: str,
    configuration: Any,
    inputs: Any,
    event_log_hash: str,
    expected_invariants: list[str],
    observed_results: dict[str, Any],
    fault_injections: list[dict[str, Any]],
    replay_result: dict[str, Any],
    conformance_verdict: str,
) -> ExperimentManifest:
    return ExperimentManifest(
        experiment_id=experiment_id,
        tpac_version=tpac_version,
        commit_sha=commit_sha,
        runtime={
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "executable": sys.executable,
        },
        configuration_hash=stable_hash(configuration),
        input_hash=stable_hash(inputs),
        event_log_hash=event_log_hash,
        expected_invariants=expected_invariants,
        observed_results=observed_results,
        fault_injections=fault_injections,
        replay_result=replay_result,
        conformance_verdict=conformance_verdict,
    )


def write_manifest(manifest: ExperimentManifest, path: str) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(manifest.to_dict(), handle, indent=2, sort_keys=True)
        handle.write("\n")
