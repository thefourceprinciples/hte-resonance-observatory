# TPAC Calibration Framework v2.4

## Objective

Treat calibration as a first-class computational dependency. A physical result is interpreted only relative to a known calibration state.

## 1. Calibration hierarchy

```text
INSTRUMENT
 ↓
CHANNEL
 ↓
CELL
 ↓
COUPLING
 ↓
MODULE
 ↓
SYSTEM
```

## 2. Calibration record

Every calibration receives:

```text
calibration_id
scope
method
reference_standard
parameters
uncertainty
validity_interval
operator/pipeline
source_measurements
```

## 3. Calibration states

```text
VALID
EXPIRING
STALE
INVALID
UNKNOWN
```

`UNKNOWN` blocks claims requiring calibrated interpretation.

## 4. Calibration drift

Monitor reference measurements over time and estimate parameter drift.

## 5. Automatic recalibration

Permitted only when:

- procedure is validated;
- reference standards are valid;
- resulting uncertainty meets the required bound.

## 6. Calibration dependency graph

A result records the complete calibration chain on which it depends.

## 7. Cross-device normalization

Comparisons across devices must identify which differences arise from calibration versus physical behavior.

## 8. Calibration holdout

Where model fitting is involved, reserve independent calibration observations for validation.

## 9. Calibration cost

Calibration time and energy become part of system-level performance accounting when they materially contribute to operation.

## 10. Calibration failure

If calibration cannot meet required uncertainty:

```text
mark device degraded
→ remove affected capabilities
→ notify scheduler
→ prevent invalid workloads
```

## 11. Calibration reproducibility

Independent calibration runs should report parameter distributions rather than only point estimates.

## 12. Core invariant

**Calibration is not housekeeping. It is part of the computational state of the physical machine.**
