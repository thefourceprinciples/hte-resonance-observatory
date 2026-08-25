"""TPAC reference integration engine.

This module provides a deliberately small vertical slice through the TPAC
architecture: resource registration, scheduling, execution, measurement,
provenance, claim creation, and deterministic verification.

It is a reference implementation, not a claim that the physical TPAC
architecture has been experimentally demonstrated.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any


@dataclass(frozen=True)
class Resource:
    resource_id: str
    capability: str
    calibrated: bool = True


@dataclass(frozen=True)
class Event:
    sequence: int
    kind: str
    payload: dict[str, Any]
    digest: str


@dataclass
class TPACRun:
    run_id: str
    resources: dict[str, Resource] = field(default_factory=dict)
    events: list[Event] = field(default_factory=list)
    claims: list[dict[str, Any]] = field(default_factory=list)

    def _append(self, kind: str, payload: dict[str, Any]) -> Event:
        sequence = len(self.events) + 1
        canonical = f"{sequence}|{kind}|{payload}"
        previous = self.events[-1].digest if self.events else "GENESIS"
        digest = sha256(f"{previous}|{canonical}".encode()).hexdigest()
        event = Event(sequence, kind, payload, digest)
        self.events.append(event)
        return event

    def register_resource(self, resource: Resource) -> None:
        if resource.resource_id in self.resources:
            raise ValueError(f"resource already registered: {resource.resource_id}")
        if not resource.calibrated:
            raise ValueError(f"resource is not calibrated: {resource.resource_id}")
        self.resources[resource.resource_id] = resource
        self._append("resource_registered", {"resource_id": resource.resource_id})

    def schedule(self, resource_id: str, workload: str) -> None:
        resource = self.resources.get(resource_id)
        if resource is None:
            raise ValueError(f"unknown resource: {resource_id}")
        if not resource.calibrated:
            raise ValueError(f"resource is not calibrated: {resource_id}")
        self._append(
            "work_scheduled",
            {"resource_id": resource_id, "workload": workload},
        )

    def execute(self, resource_id: str, workload: str, measurement: Any) -> None:
        if resource_id not in self.resources:
            raise ValueError(f"unknown resource: {resource_id}")
        self._append(
            "execution_completed",
            {"resource_id": resource_id, "workload": workload},
        )
        self._append(
            "measurement_recorded",
            {"resource_id": resource_id, "workload": workload, "value": measurement},
        )

    def create_claim(self, statement: str, evidence_event: int) -> dict[str, Any]:
        if evidence_event < 1 or evidence_event > len(self.events):
            raise ValueError("claim must reference an existing event")
        claim = {
            "statement": statement,
            "evidence_event": evidence_event,
            "claim_level": "L1",
        }
        self.claims.append(claim)
        self._append("claim_created", claim)
        return claim

    def verify(self) -> dict[str, Any]:
        failures: list[str] = []
        expected_previous = "GENESIS"
        for event in self.events:
            canonical = f"{event.sequence}|{event.kind}|{event.payload}"
            expected = sha256(f"{expected_previous}|{canonical}".encode()).hexdigest()
            if event.digest != expected:
                failures.append(f"event {event.sequence}: digest mismatch")
            expected_previous = event.digest

        sequences = [event.sequence for event in self.events]
        if sequences != list(range(1, len(sequences) + 1)):
            failures.append("event sequence is not contiguous")

        for claim in self.claims:
            if not 1 <= claim["evidence_event"] <= len(self.events):
                failures.append("claim references missing evidence")

        return {
            "run_id": self.run_id,
            "status": "PASS" if not failures else "FAIL",
            "event_count": len(self.events),
            "claim_count": len(self.claims),
            "failures": failures,
        }
