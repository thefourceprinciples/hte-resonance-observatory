# TPAC Calibration Lifecycle v6.2

## Objective

Treat calibration as a first-class stateful dependency rather than an undocumented preprocessing step.

## States

```text
UNINITIALIZED
CALIBRATING
VALID
EXPIRING
EXPIRED
INVALID
QUARANTINED
RETIRED
```

## Calibration record

```text
calibration_id
resource_id
method
reference_standard
parameters
uncertainty
valid_from
valid_until
operator/process
software_revision
```

## Validity

A calibration is valid only within its declared resource, environmental, temporal, and methodological scope.

## Drift

Systems may monitor drift indicators and transition from VALID to EXPIRING before the formal validity boundary.

## Invalidation

Evidence of calibration failure creates an invalidation event and identifies affected executions and results.

## Dependency propagation

Results depending on invalidated calibration are flagged for review rather than silently discarded or accepted.

## Recalibration

Recalibration creates a new calibration identity; it does not overwrite historical calibration state.

## Traceability

Calibration references remain attached to measurements and executions for later reconstruction.

## Core invariant

**Calibration is part of the evidence chain: changing calibration state changes the conditions under which measurements can be interpreted.**
