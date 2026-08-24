# TPAC Resource Scheduler Specification v6.1

## Objective

Define deterministic, auditable allocation of constrained physical and computational resources.

## Resource states

```text
DISCOVERED
VALIDATED
AVAILABLE
RESERVED
ALLOCATED
ACTIVE
DRAINING
QUARANTINED
RETIRED
```

## Scheduling inputs

```text
workload requirements
resource capabilities
safety constraints
thermal constraints
timing constraints
calibration validity
authorization
priority
```

## Allocation rule

A workload may be allocated only when all mandatory constraints are satisfiable under the declared resource snapshot.

## Reservation

Reservations have explicit expiry and ownership. Expired reservations cannot silently become active allocations.

## Priority

Priority affects scheduling order only within safety and authorization boundaries.

## Preemption

Preemption records the interrupted execution state and required recovery procedure.

## Fairness

Long-running queues should expose starvation metrics and configurable fairness policies.

## Determinism

Given identical scheduler inputs and deterministic policy, scheduling decisions should be reproducible.

## Audit record

```text
request_id
resource_snapshot
policy_version
selected_resources
rejected_resources
reason_codes
timestamp
```

## Core invariant

**Scheduling is a constrained decision process whose inputs and exclusions remain inspectable after allocation.**
