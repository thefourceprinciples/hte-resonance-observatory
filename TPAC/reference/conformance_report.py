"""Generate a deterministic TPAC conformance evidence report."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from TPAC.reference.replay import (
    event_hash,
    inject_delete,
    inject_duplicate,
    inject_payload_mutation,
    inject_reorder,
    replay,
)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def make_history() -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    previous = "0" * 64
    for kind, payload in [
        ("resource_registered", {"resource_id": "r1", "capacity": 1}),
        ("calibration_recorded", {"resource_id": "r1", "status": "valid"}),
        ("claim_recorded", {"claim_id": "c1", "value": 42}),
    ]:
        event: dict[str, object] = {
            "kind": kind,
            "payload": payload,
            "previous_hash": previous,
        }
        event["hash"] = event_hash(event)
        previous = str(event["hash"])
        events.append(event)
    return events


def main() -> int:
    events = make_history()
    baseline = replay(events)

    attacks = {
        "delete_event": replay(inject_delete(events, 1)),
        "duplicate_event": replay(inject_duplicate(events, 1)),
        "reorder_events": replay(inject_reorder(events, 0, 1)),
        "mutate_payload": replay(inject_payload_mutation(events, 2, "value", 99)),
    }

    report = {
        "schema": "tpac-conformance-evidence-v1",
        "tpac_version": "reference-v1",
        "commit_sha": os.environ.get("GITHUB_SHA", "local"),
        "baseline": {
            "valid": baseline.valid,
            "event_count": baseline.event_count,
            "state_hash": hashlib.sha256(canonical(baseline.state).encode()).hexdigest(),
            "errors": list(baseline.errors),
        },
        "fault_injection": {
            name: {
                "detected": not result.valid,
                "event_count": result.event_count,
                "errors": list(result.errors),
            }
            for name, result in attacks.items()
        },
        "event_log_hash": hashlib.sha256(canonical(events).encode()).hexdigest(),
    }

    if not baseline.valid or not all(item["detected"] for item in report["fault_injection"].values()):
        raise SystemExit("TPAC conformance evidence generation failed")

    output = Path("tpac-conformance-report.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
