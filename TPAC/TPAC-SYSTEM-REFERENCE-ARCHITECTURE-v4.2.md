# TPAC System Reference Architecture v4.2

## Objective

Integrate the TPAC layers into a single reference architecture with explicit boundaries between physical execution, computation, evidence, and governance.

## 1. Planes

```text
APPLICATION PLANE
       ↓
COMPUTATION PLANE
       ↓
CONTROL PLANE
       ↓
PHYSICAL PLANE
       ↓
MEASUREMENT PLANE
       ↓
EVIDENCE PLANE
```

## 2. Cross-cutting planes

```text
SAFETY
SECURITY
PROVENANCE
OBSERVABILITY
CALIBRATION
RESOURCE MANAGEMENT
```

These services do not belong exclusively to one layer.

## 3. Physical plane

Contains cells, couplings, modules, sensors, actuators, interconnects, thermal systems, and environmental interfaces.

## 4. Measurement plane

Converts physical observables into calibrated measurements while preserving raw acquisition.

## 5. Computation plane

Contains compiler, ISA, runtime, scheduler, and workload abstractions.

## 6. Evidence plane

Contains:

```text
data lineage
evidence graph
claim registry
experiment manifests
reproducibility packages
decision ledger
```

## 7. Boundary rule

No evidence-plane artifact may alter raw physical measurements. No computation-plane artifact may silently rewrite evidence status.

## 8. Lifecycle

```text
HYPOTHESIS
→ EXPERIMENT MANIFEST
→ COMPILE
→ SCHEDULE
→ EXECUTE
→ MEASURE
→ CALIBRATE/ANALYZE
→ EVIDENCE GRAPH
→ CLAIM REGISTRY
→ DECISION
→ REPLICATION
```

## 9. Failure containment

A fault propagates upward only as far as necessary. Safety events can interrupt computation, while evidence capture remains available whenever physically possible.

## 10. Reference implementation strategy

Build the architecture incrementally:

```text
software simulation
→ hardware-in-loop
→ single physical module
→ multi-module fabric
```

Every stage consumes the same logical manifests where practical.

## 11. Verification gates

Each transition requires evidence appropriate to the layer being promoted. Simulation success does not constitute hardware validation.

## 12. Core invariant

**TPAC is an integrated physical-computational-evidentiary system: computation, measurement, provenance, and safety remain coupled by explicit interfaces rather than hidden assumptions.**
