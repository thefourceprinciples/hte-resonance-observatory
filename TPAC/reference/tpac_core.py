"""Minimal TPAC reference implementation.

Pure-stdlib reference model for resource identity, provenance, calibration,
execution state, and deterministic scheduling. It is intentionally small and
non-hardware-specific: the purpose is to make the TPAC contracts executable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import json
from typing import Any


class ResourceState(str, Enum):
    DISCOVERED = "DISCOVERED"
    VALIDATED = "VALIDATED"
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    ALLOCATED = "ALLOCATED"
    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    QUARANTINED = "QUARANTINED"
    RETIRED = "RETIRED"


class CalibrationState(str, Enum):
    UNINITIALIZED = "UNINITIALIZED"
    CALIBRATING = "CALIBRATING"
    VALID = "VALID"
    EXPIRING = "EXPIRING"
    EXPIRED = "EXPIRED"
    INVALID = "INVALID"
    QUARANTINED = "QUARANTINED"
    RETIRED = "RETIRED"


class ExecutionState(str, Enum):
    CREATED = "CREATED"
    VALIDATED = "VALIDATED"
    ALLOCATED = "ALLOCATED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    QUARANTINED = "QUARANTINED"


@dataclass(frozen=True)
class Capability:
    name: str
    version: str = "1"


@dataclass
class Resource:
    resource_id: str
    capabilities: set[str]
    state: ResourceState = ResourceState.DISCOVERED
    calibration_id: str | None = None

    def can_run(self, required: set[str]) -> bool:
        return self.state == ResourceState.AVAILABLE and required <= self.capabilities


@dataclass(frozen=True)
class Calibration:
    calibration_id: str
    resource_id: str
    state: CalibrationState
    valid_from: str
    valid_until: str
    method: str
    uncertainty: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Event:
    event_id: str
    event_type: str
    subject_id: str
    predecessors: tuple[str, ...] = ()
    payload: dict[str, Any] = field(default_factory=dict)

    def digest(self) -> str:
        body = {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "subject_id": self.subject_id,
            "predecessors": list(self.predecessors),
            "payload": self.payload,
        }
        encoded = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
        return sha256(encoded).hexdigest()


@dataclass(frozen=True)
class Workload:
    workload_id: str
    required_capabilities: frozenset[str]
    priority: int = 0


class ProvenanceGraph:
    def __init__(self) -> None:
        self.events: dict[str, Event] = {}

    def append(self, event: Event) -> str:
        missing = [p for p in event.predecessors if p not in self.events]
        if missing:
            raise ValueError(f"missing provenance predecessors: {missing}")
        if event.event_id in self.events:
            raise ValueError(f"duplicate event_id: {event.event_id}")
        self.events[event.event_id] = event
        return event.digest()

    def lineage(self, event_id: str) -> list[str]:
        if event_id not in self.events:
            raise KeyError(event_id)
        result: list[str] = []
        seen: set[str] = set()

        def visit(eid: str) -> None:
            if eid in seen:
                return
            seen.add(eid)
            for parent in self.events[eid].predecessors:
                visit(parent)
            result.append(eid)

        visit(event_id)
        return result


class Scheduler:
    """Deterministic capability scheduler with explicit rejection reasons."""

    def select(self, workload: Workload, resources: list[Resource]) -> tuple[Resource | None, str]:
        candidates = [r for r in resources if r.can_run(set(workload.required_capabilities))]
        if not candidates:
            return None, "NO_VALID_RESOURCE"
        # Stable ordering makes equal inputs reproducible.
        candidates.sort(key=lambda r: r.resource_id)
        selected = candidates[0]
        selected.state = ResourceState.ALLOCATED
        return selected, "ALLOCATED"


def validate_calibration(calibration: Calibration) -> bool:
    return calibration.state == CalibrationState.VALID and bool(calibration.calibration_id)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
