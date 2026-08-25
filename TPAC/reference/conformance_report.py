"""Generate deterministic TPAC conformance and reproducibility evidence."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from TPAC.reference.experiment import run_experiment
from TPAC.reference.experiment_manifest import build_manifest, write_manifest
from TPAC.reference.replay import (
    inject_delete,
    inject_duplicate,
    inject_payload_mutation,
    inject_reorder,
    replay,
)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def main() -> int:
    experiment = run_experiment()
    events = experiment["events"]
    baseline = experiment["replay"]
    native = experiment["native_verification"]

    attacks = {
        "delete_event": replay(inject_delete(events, 1)),
        "duplicate_event": replay(inject_duplicate(events, 1)),
        "reorder_events": replay(inject_reorder(events, 0, 1)),
        "mutate_payload": replay(inject_payload_mutation(events, 2, "value", 99)),
    }

    fault_results = {
        name: {
            "detected": not result.valid,
            "event_count": result.event_count,
            "errors": list(result.errors),
        }
        for name, result in attacks.items()
    }

    conformance_verdict = (
        "PASS"
        if native["status"] == "PASS"
        and baseline.valid
        and all(item["detected"] for item in fault_results.values())
        else "FAIL"
    )

    event_log_hash = experiment["event_log_hash"]
    report = {
        "schema": "tpac-conformance-evidence-v1",
        "experiment_id": experiment["run"].run_id,
        "tpac_version": "reference-v1",
        "commit_sha": os.environ.get("GITHUB_SHA", "local"),
        "native_verification": native,
        "baseline_replay": {
            "valid": baseline.valid,
            "event_count": baseline.event_count,
            "state_hash": hashlib.sha256(canonical(baseline.state).encode()).hexdigest(),
            "errors": list(baseline.errors),
        },
        "fault_injection": fault_results,
        "event_log_hash": event_log_hash,
    }

    if conformance_verdict != "PASS":
        raise SystemExit("TPAC conformance evidence generation failed")

    output = Path("tpac-conformance-report.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest = build_manifest(
        experiment_id=experiment["run"].run_id,
        tpac_version="reference-v1",
        commit_sha=os.environ.get("GITHUB_SHA", "local"),
        configuration=experiment["configuration"],
        inputs=experiment["inputs"],
        event_log_hash=event_log_hash,
        expected_invariants=[
            "native integration verification passes",
            "projected history replays deterministically",
            "event deletion is detected",
            "event duplication is detected",
            "event reordering is detected",
            "payload mutation is detected",
        ],
        observed_results=report["native_verification"],
        fault_injections=fault_results,
        replay_result={
            "status": "PASS" if baseline.valid else "FAIL",
            "errors": list(baseline.errors),
            "event_count": baseline.event_count,
        },
        conformance_verdict=conformance_verdict,
    )
    write_manifest(manifest, "tpac-experiment-manifest.json")

    print(output)
    print("tpac-experiment-manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
