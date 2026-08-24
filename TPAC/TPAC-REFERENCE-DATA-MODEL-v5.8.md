# TPAC Reference Data Model v5.8

## Objective

Provide canonical entities and relationships for interoperable TPAC implementations.

## Core entities

```text
Resource
Capability
Workload
Execution
Measurement
Artifact
Experiment
Claim
Decision
Event
```

## Required relationships

```text
Resource HAS_CAPABILITY Capability
Workload USES Resource
Execution REALIZES Workload
Execution PRODUCES Measurement
Artifact DERIVED_FROM Artifact
Measurement SUPPORTS Claim
Claim INFORMS Decision
Event MODIFIES Entity
```

## Identity

Every entity has a stable identifier and immutable creation identity. Mutable state is represented through versioned events.

## Temporal model

Entities may have both creation time and validity intervals. Wall-clock creation time must not be confused with physical validity time.

## Provenance

Derived entities retain explicit parent references. Deleting a parent from an active provenance chain is prohibited; retirement is represented as state.

## Units

Physical quantities carry explicit units and dimensional metadata.

## Uncertainty

Measurements may carry uncertainty models appropriate to their acquisition method.

## Compatibility

Unknown fields must be safely ignorable by consumers where the schema declares forward compatibility.

## Core invariant

**TPAC interoperability depends on shared identity, temporal, unit, and provenance semantics—not merely shared field names.**
