"""Run a canonical TPAC reference experiment from the executable integration engine."""

from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import json
from typing import Any

from TPAC.reference.integration import Resource, TPACRun
from TPAC.reference.replay import event_hash, replay


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def build_reference_run() -> TPACRun:
    run = TPACRun("TPAC-EXP-001")
    run.register_resource(Resource("r1", "reference-execution"))
    run.schedule("r1", "deterministic-smoke")
    run.execute("r1", "deterministic-smoke", measurement=42)
    run.create_claim(
        "The reference experiment produced a recorded measurement.",
        evidence_event=4,
    )
    return run


def project_events(run: TPACRun) -> list[dict[str, Any]]:
    """Project actual TPACRun events into the replay engine's canonical schema."""
    events: list[dict[str, Any]] = []
    previous = "0" * 64
    for event in run.events:
        kind = "claim_recorded" if event.kind == "claim_created" else event.kind
        projected: dict[str, Any] = {
            "kind": kind,
            "payload": dict(event.payload),
            "previous_hash": previous,
        }
        projected["hash"] = event_hash(projected)
        previous = projected["hash"]
        events.append(projected)
    return events


def run_experiment() -> dict[str, Any]:
    run = build_reference_run()
    native_verification = run.verify()
    events = project_events(run)
    replay_result = replay(events)
    event_log_hash = sha256(canonical(events).encode("utf-8")).hexdigest()

    return {
        "run": run,
        "native_verification": native_verification,
        "events": events,
        "replay": replay_result,
        "event_log_hash": event_log_hash,
        "configuration": {
            "resource": "r1",
            "capability": "reference-execution",
            "workload": "deterministic-smoke",
            "measurement": 42,
        },
        "inputs": {
            "run_id": run.run_id,
            "workload": "deterministic-smoke",
        },
    }
