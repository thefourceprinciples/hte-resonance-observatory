# TPAC Physical Instruction Set Architecture v2.5

## Objective

Define a minimal machine-level vocabulary that can represent physical operations without prematurely committing to a particular hardware implementation.

## 1. Instruction classes

```text
STATE
COUPLE
DRIVE
WAIT
MEASURE
ROUTE
RESET
SYNC
CALIBRATE
BRANCH
```

## 2. STATE

Initialize or modify a logical physical state under device constraints.

## 3. COUPLE

Enable, disable, or configure interaction between physical elements.

## 4. DRIVE

Apply a bounded physical excitation.

## 5. WAIT

Allow physical evolution to proceed without an explicit control event.

This is computationally meaningful when dynamics themselves perform transformation.

## 6. MEASURE

Acquire physical observables and attach calibration and uncertainty metadata.

## 7. ROUTE

Change the physical path through which information or energy propagates.

## 8. RESET

Return a defined physical region toward a specified baseline state.

## 9. SYNC

Establish a synchronization barrier between control domains or physical trajectories.

## 10. CALIBRATE

Invoke a validated calibration primitive and produce a new calibration state.

## 11. BRANCH

Condition subsequent execution on a measured physical result.

## 12. Instruction metadata

Each instruction includes:

```text
opcode
operands
physical target
constraints
expected duration
provenance
uncertainty budget
```

## 13. Semantic distinction

An instruction describes an intended physical operation. The execution record must separately capture what the hardware actually delivered.

## 14. Illegal operations

The ISA rejects operations that exceed device capability or safety envelope before actuation.

## 15. Optimization

Instruction fusion is allowed only when fused execution preserves observable semantics and provenance.

## 16. Determinism

Instructions whose physical outcome is stochastic must declare stochastic semantics rather than pretending deterministic execution.

## 17. ISA portability

Programs target capability classes, not individual device coordinates, whenever possible.

## 18. Core invariant

**The TPAC ISA describes physical computation as controlled state evolution, measurement, and interaction—not merely arithmetic instructions mapped onto unfamiliar hardware.**
