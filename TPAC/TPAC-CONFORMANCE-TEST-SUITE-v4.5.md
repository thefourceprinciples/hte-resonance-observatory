# TPAC Conformance Test Suite v4.5

## Objective

Turn the TPAC specification into executable, falsifiable conformance criteria.

## Test families

```text
ISA
RESOURCE
SCHEDULING
CALIBRATION
INTERCONNECT
PROVENANCE
MEASUREMENT
SAFETY
REPRODUCIBILITY
```

## ISA tests

Verify opcode semantics, illegal-operation rejection, ordering, and measurement metadata requirements.

## Resource tests

Verify capability discovery, stale-resource rejection, exclusivity, degradation, and revision tracking.

## Scheduling tests

Inject conflicting workloads and verify that the scheduler respects physical, thermal, timing, and safety constraints.

## Calibration tests

Inject stale or invalid calibration state and verify affected workloads are blocked or degraded according to policy.

## Provenance tests

Mutate an upstream artifact and verify dependent results are distinguishable from results generated from the original artifact.

## Measurement tests

Verify raw measurements remain immutable and that transformations produce lineage records.

## Safety tests

Attempt commands beyond declared operating envelopes and verify refusal before actuation.

## Reproducibility tests

Run identical manifests through the same backend and compare artifacts under declared deterministic or stochastic semantics.

## Fault injection

Test component, controller, communication, thermal, timing, calibration, and measurement failures.

## Conformance report

Each implementation produces:

```text
test_id
implementation_version
hardware_class
pass/fail
observed_behavior
evidence_reference
```

## Non-conformance

A failed test is recorded rather than hidden. Partial conformance is permitted when capability boundaries are explicit.

## Core invariant

**TPAC claims become meaningful only where an implementation can be tested against independently inspectable requirements.**
