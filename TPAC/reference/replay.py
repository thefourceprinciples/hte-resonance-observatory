"""Deterministic replay and fault-injection utilities for TPAC reference runs."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any, Iterable


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def event_hash(event: dict[str, Any]) -> str:
    payload = dict(event)
    payload.pop("hash", None)
    return sha256(canonical_json(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ReplayResult:
    valid: bool
    event_count: int
    state: dict[str, Any]
    errors: tuple[str, ...]


def verify_chain(events: Iterable[dict[str, Any]]) -> tuple[bool, list[str]]:
    previous = "0" * 64
    errors: list[str] = []
    for index, event in enumerate(events):
        if event.get("previous_hash") != previous:
            errors.append(f"event {index}: previous_hash mismatch")
        expected = event_hash(event)
        if event.get("hash") != expected:
            errors.append(f"event {index}: hash mismatch")
        previous = event.get("hash", "")
    return not errors, errors


def replay(events: list[dict[str, Any]]) -> ReplayResult:
    valid_chain, errors = verify_chain(events)
    state: dict[str, Any] = {"resources": {}, "calibrations": {}, "claims": []}

    for index, event in enumerate(events):
        kind = event.get("kind")
        payload = event.get("payload", {})
        if kind == "resource_registered":
            resource_id = payload.get("resource_id")
            if not resource_id:
                errors.append(f"event {index}: missing resource_id")
            else:
                state["resources"][resource_id] = dict(payload)
        elif kind == "calibration_recorded":
            resource_id = payload.get("resource_id")
            if resource_id not in state["resources"]:
                errors.append(f"event {index}: calibration references unknown resource")
            else:
                state["calibrations"][resource_id] = dict(payload)
        elif kind == "claim_recorded":
            state["claims"].append(dict(payload))
        elif kind is None:
            errors.append(f"event {index}: missing kind")

    return ReplayResult(not errors and valid_chain, len(events), state, tuple(errors))


def inject_delete(events: list[dict[str, Any]], index: int) -> list[dict[str, Any]]:
    result = [dict(event) for event in events]
    del result[index]
    return result


def inject_duplicate(events: list[dict[str, Any]], index: int) -> list[dict[str, Any]]:
    result = [dict(event) for event in events]
    result.insert(index, dict(result[index]))
    return result


def inject_reorder(events: list[dict[str, Any]], first: int, second: int) -> list[dict[str, Any]]:
    result = [dict(event) for event in events]
    result[first], result[second] = result[second], result[first]
    return result


def inject_payload_mutation(events: list[dict[str, Any]], index: int, key: str, value: Any) -> list[dict[str, Any]]:
    result = [dict(event) for event in events]
    payload = dict(result[index].get("payload", {}))
    payload[key] = value
    result[index]["payload"] = payload
    return result
