# TPAC Module Contract v5.7

## Objective

Define a uniform contract for physical and software modules so TPAC can scale without losing explicit interfaces.

## Module identity

Every module exposes:

```text
module_id
module_type
revision
capabilities
interfaces
constraints
health
provenance
```

## Inputs

Inputs declare type, units, validity range, timing semantics, and provenance requirements.

## Outputs

Outputs declare type, units, uncertainty, timing semantics, and lineage references.

## Control interface

State-changing commands declare authorization requirements and admissible operating ranges.

## Health interface

Health reports distinguish:

```text
HEALTHY
DEGRADED
UNKNOWN
FAULTED
QUARANTINED
```

## Capability negotiation

Consumers request capabilities rather than assuming a module implementation.

## Version compatibility

Breaking interface changes require a new contract version. Compatibility is machine-checkable where possible.

## Resource lifecycle

```text
DISCOVERED
VALIDATED
AVAILABLE
ALLOCATED
ACTIVE
DRAINING
RETIRED
```

## Failure behavior

A module declares how outputs, controls, and state behave during communication loss, internal fault, and emergency shutdown.

## Core invariant

**TPAC scalability depends on explicit module contracts, not implicit knowledge of individual devices.**
