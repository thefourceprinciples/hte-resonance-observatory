# TPAC Resource Description v2.8

## Objective

Create a formal schema for describing physical resources to the compiler, scheduler, runtime, and benchmark system.

## 1. Resource identity

Every resource has:

```text
resource_id
type
parent
revision
status
```

## 2. Capability declaration

Capabilities declare supported operations, ranges, precision, latency, energy, and uncertainty.

## 3. Constraints

Resources may declare:

```text
exclusive
shared
ordered
capacity_limited
thermal_limited
calibration_limited
```

## 4. State semantics

A resource can be:

```text
EMPTY
INITIALIZED
OCCUPIED
DEGRADED
UNKNOWN
```

## 5. Cost model

Each resource exposes measured or bounded costs:

```text
latency
energy
thermal_cost
routing_cost
calibration_cost
uncertainty_cost
```

## 6. Composition

Resources can be composed into higher-level resources while preserving links to their constituents.

## 7. Availability

Availability is represented as a time-dependent state rather than a static boolean.

## 8. Degradation

A degraded resource may retain a subset of capabilities. The scheduler receives the reduced capability set automatically.

## 9. Discovery

The resource registry is generated from device passports and live health state.

## 10. Resource equivalence

Two resources are equivalent only with respect to a declared capability set. Physical identity is never collapsed.

## 11. Compiler use

The compiler consumes resource descriptions during placement and code generation.

## 12. Scheduler use

The scheduler consumes live resource descriptions to reserve and sequence execution.

## 13. Provenance

Every execution references the resource description revision used to compile and schedule it.

## 14. Core invariant

**Resource abstraction must preserve every physical constraint capable of changing the meaning, correctness, cost, or reproducibility of computation.**
