# TPAC — System Architecture v0.8

**Status:** Integrated architecture specification
**Date:** 2026-08-24

## 1. System decomposition

TPAC is decomposed into nine planes:

```text
P0  MATERIAL / PHYSICS
P1  CELL
P2  FABRIC
P3  CONTROL
P4  COMPUTATION
P5  SOFTWARE
P6  PROVENANCE
P7  OBSERVABILITY
P8  APPLICATION
```

Each plane has an explicit interface to the planes above and below it.

---

## 2. P0 — Physical substrate

Defines:

- material composition;
- geometry;
- optical properties;
- acoustic properties;
- phase behavior;
- thermal behavior;
- fabrication tolerances.

P0 produces measurable physical primitives, not software abstractions.

---

## 3. P1 — Cell abstraction

A cell exposes:

```text
INPUT
STATE
TRANSITION
COUPLING
OUTPUT
THERMAL
HEALTH
```

The abstraction is valid only when each interface corresponds to a measurable physical quantity.

---

## 4. P2 — Fabric

The fabric is a graph:

```text
G = (V,E,S)
```

where:

- `V` = cells;
- `E` = couplings;
- `S` = cell and edge state.

Unlike a conventional static circuit, `S` may alter the effective graph.

---

## 5. P3 — Control plane

The control plane translates desired transitions into physical excitation.

```text
logical request
      ↓
validated control
      ↓
physical pulse
      ↓
measured response
```

Closed-loop operation is preferred over open-loop operation whenever state uncertainty is significant.

---

## 6. P4 — Computation plane

TPAC supports four computational modes:

### Transformation

Input waveform → transformed waveform.

### State

Input → persistent state.

### Propagation

State/input → spatial evolution.

### Relaxation

Initial configuration → attractor/solution.

A workload may combine all four.

---

## 7. P5 — Software plane

Components:

```text
SDK
DSL
compiler
IR
mapper
scheduler
runtime
simulator
benchmark suite
```

The software plane must expose physical uncertainty rather than pretending the substrate is deterministic when it is not.

---

## 8. P6 — Provenance plane

Every operation receives a provenance chain:

```text
program
→ compiler
→ IR
→ mapping
→ calibration
→ hardware
→ raw measurement
→ analysis
→ result
```

A result without a provenance chain is considered incomplete.

---

## 9. P7 — Observability plane

Monitor:

- state;
- temperature;
- optical power;
- acoustic amplitude;
- coupling;
- error rate;
- calibration age;
- resource utilization.

The system should make physical degradation visible before it becomes logical failure.

---

## 10. P8 — Application plane

Applications should target demonstrated computational advantages rather than generic “AI acceleration” claims.

Candidate domains include temporal processing, spectral processing, associative memory, physical simulation, optimization, and sensing.

---

## 11. Interface contracts

Each plane publishes a versioned contract.

Example:

```text
Cell API v1
Fabric API v1
Control API v1
Runtime API v1
Provenance API v1
```

Changing a physical implementation should not silently invalidate higher layers.

---

## 12. State machine

The entire system can be represented as:

```text
DISCOVER
   ↓
CALIBRATE
   ↓
CONFIGURE
   ↓
EXECUTE
   ↓
MEASURE
   ↓
VALIDATE
   ↓
COMMIT RESULT
   ↓
UPDATE MODEL
```

This makes measurement part of computation rather than an afterthought.

---

## 13. Configuration states

```text
OFF
SAFE
CALIBRATING
READY
EXECUTING
MEASURING
RECOVERING
FAULT
```

Transitions must have explicit conditions.

---

## 14. Physical transaction model

A TPAC operation can be treated as a transaction:

```text
BEGIN
  reserve resources
  verify calibration
  apply excitation
  read state
  validate result
COMMIT
```

If validation fails, the runtime can rollback by restoring a known state where physically possible.

---

## 15. Checkpointing

Checkpoint data should include:

- cell states;
- topology;
- calibration version;
- thermal state;
- active jobs;
- control configuration.

This allows interrupted physical computation to resume when state retention permits.

---

## 16. Distributed checkpointing

For multi-chip TPAC:

```text
node state
 +
network state
 +
clock/event state
 +
calibration state
```

must be coordinated before a global checkpoint is declared valid.

---

## 17. Physical consistency

A software state snapshot is not sufficient if the physical state can evolve during capture.

The system therefore needs a measured consistency window:

```text
capture start → physical stability → capture complete
```

or a model-based reconstruction with explicitly reported uncertainty.

---

## 18. Energy accounting

Total energy:

```text
E_total = E_drive
        + E_control
        + E_readout
        + E_memory
        + E_cooling
        + E_network
        + E_calibration
```

No system-level energy claim should omit a material subsystem.

---

## 19. Cost accounting

Total cost of ownership should include:

- fabrication;
- packaging;
- control electronics;
- optical sources;
- detectors;
- cooling;
- maintenance;
- calibration;
- replacement;
- software infrastructure.

Device-level cost alone is insufficient.

---

## 20. Scaling architecture

Scale along three independent axes:

```text
cell density
network size
number of physical nodes
```

The architecture should be benchmarked separately at each scale.

---

## 21. Heterogeneous cells

Not all cells need to be identical.

A fabric may contain:

```text
memory cells
routing cells
reservoir cells
readout cells
interface cells
```

This resembles heterogeneous biological tissue more than homogeneous logic gates.

---

## 22. Specialized physical kernels

A future TPAC system could expose physical kernels such as:

```text
KERNEL_FILTER
KERNEL_RESERVOIR
KERNEL_ATTRACTOR
KERNEL_SOLVER
KERNEL_ROUTE
KERNEL_MEMORY
```

The compiler composes kernels into workloads.

---

## 23. Hardware/software co-design

Optimization must operate across layers:

```text
material
↕
geometry
↕
cell
↕
topology
↕
compiler
↕
workload
```

A better workload may permit a simpler physical device; a better physical primitive may eliminate substantial software complexity.

---

## 24. Discovery-driven instruction set

The TPAC instruction set should emerge from demonstrated physical primitives.

Candidate classes:

```text
EXCITE
COUPLE
STORE
READ
ROUTE
RELAX
RECONFIGURE
RESET
MEASURE
```

The final instruction set should not be frozen before experimental evidence exists.

---

## 25. Research-to-product boundary

Separate three modes:

```text
RESEARCH
PROTOTYPE
PRODUCTION
```

Research hardware may tolerate manual calibration.

Prototype hardware automates repeatable operations.

Production hardware requires quantified manufacturing, reliability, safety, and cost models.

---

## 26. Productization gate

A TPAC subsystem becomes a candidate product only after:

1. reproducible physical behavior;
2. defined workload advantage;
3. stable manufacturing pathway;
4. quantified reliability;
5. system-level energy measurement;
6. software interface;
7. customer-relevant benefit.

---

## 27. Open experimental architecture

The reference implementation should publish enough information for independent reproduction where legally and strategically appropriate:

- interfaces;
- measurement methodology;
- benchmarks;
- data schema;
- reference software;
- validation procedures.

This makes claims independently testable.

---

## 28. Architecture invariant

Across implementations, preserve the core invariant:

> **A controllable physical state must influence subsequent physical information transformation in a measurable and programmable way.**

Everything else is implementation detail until experimentally established.

---

## 29. Falsification conditions

The broader TPAC architecture should be reconsidered if repeated experiments show that:

- useful state cannot be retained;
- state cannot be reliably controlled;
- network scaling destroys fidelity;
- energy overhead overwhelms physical advantage;
- conventional systems outperform TPAC across all natural workloads;
- fabrication variation makes calibration ineffective.

These are legitimate outcomes, not project failures.

---

## 30. Architecture success condition

The strongest defensible success claim is not “TPAC is a revolutionary computer.”

It is:

> **A reproducible physical computing architecture demonstrates a measurable advantage for a defined workload because its native dynamics perform part of the computation directly.**

That statement is specific enough to test and broad enough to survive implementation changes.
