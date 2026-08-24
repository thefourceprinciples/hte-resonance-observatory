# TPAC Orchestration State Machine v5.3

## Objective

Define execution lifecycle transitions so workloads cannot silently skip required gates.

## States

```text
CREATED
VALIDATING
AUTHORIZED
COMPILED
SCHEDULED
CALIBRATING
READY
RUNNING
PAUSED
RECOVERING
COMPLETED
FAILED
QUARANTINED
CANCELLED
```

## Transition rule

Every transition records:

```text
previous_state
next_state
trigger
actor/process
validation evidence
timestamp
```

## Preconditions

A transition may execute only when its declared prerequisites are satisfied.

## Pause semantics

Pause is distinct from failure. The system records whether physical state is stable, evolving, or unknown while paused.

## Recovery semantics

Recovery cannot directly produce `COMPLETED`; it must pass through required validation and execution states.

## Unknown state

If physical state cannot be reliably determined, the resource enters a quarantine-compatible state until revalidated.

## Cancellation

Cancellation records whether physical execution stopped safely and whether residual state remains.

## State persistence

Execution state is durable enough to reconstruct the lifecycle after process or host failure.

## Core invariant

**A TPAC execution cannot become successful merely because its control process terminated without reporting an error.**
