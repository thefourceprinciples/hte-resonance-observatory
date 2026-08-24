# TPAC Compiler Specification v1.1

## 1. Compiler objective

Compile a workload into a physically executable TPAC program while preserving correctness constraints, physical limits, uncertainty, and provenance.

```text
SOURCE
 ↓
SEMANTIC IR
 ↓
PHYSICAL IR
 ↓
PLACEMENT
 ↓
ROUTING
 ↓
SCHEDULING
 ↓
CONTROL PLAN
 ↓
EXECUTION
```

## 2. Source model

A workload declares:

- inputs;
- outputs;
- state requirements;
- temporal constraints;
- precision requirements;
- energy constraints;
- acceptable uncertainty.

## 3. Physical capability discovery

Before compilation, query the device passport.

```text
available cells
available couplings
supported states
readout channels
thermal budget
calibration confidence
```

Unsupported programs fail before hardware execution.

## 4. Placement

Map logical nodes onto physical cells while minimizing a weighted cost:

```text
C = locality + routing + thermal + uncertainty + resource contention
```

## 5. Routing

Construct physical paths subject to:

- forbidden regions;
- coupling limits;
- timing constraints;
- crosstalk limits;
- readout conflicts.

## 6. Scheduling

Schedule excitation and measurement events against physical time.

The scheduler must account for recovery periods and thermal history.

## 7. Calibration-aware compilation

A nominally identical physical mapping may have different measured performance on two devices.

Therefore compilation consumes calibration data rather than only geometry.

## 8. Uncertainty propagation

Each physical primitive carries an uncertainty estimate.

The compiler propagates uncertainty through the execution graph and rejects workloads whose predicted uncertainty exceeds the requested bound.

## 9. Runtime adaptation

If measured confidence falls below the requested threshold:

```text
pause
→ diagnose
→ remap or recalibrate
→ resume/restart
```

## 10. Provenance emission

The compiler emits a manifest containing:

```text
source hash
compiler version
IR hash
device ID
calibration ID
mapping
schedule
control program
uncertainty model
```

## 11. Optimization levels

```text
-O0  deterministic/reference mapping
-O1  locality
-O2  latency
-O3  energy
-O4  workload-specific search
```

Higher optimization must never silently weaken correctness requirements.

## 12. Simulation gate

A candidate program should optionally execute against a digital twin before hardware submission.

Simulation is a screening mechanism, not evidence of physical performance.

## 13. Compilation cache

Cache keys include:

```text
program
compiler
device revision
calibration snapshot
optimization policy
```

A calibration change can invalidate a previously optimal mapping.

## 14. Kernel fusion

Adjacent compatible physical kernels may be fused to avoid unnecessary readout and reinitialization.

Example:

```text
filter → transform → reservoir
```

can potentially execute as one continuous physical trajectory.

## 15. Compilation failure taxonomy

```text
UNSUPPORTED_PHYSICS
INSUFFICIENT_STATE_CAPACITY
ROUTING_CONFLICT
THERMAL_LIMIT
UNCERTAINTY_LIMIT
READOUT_CONFLICT
CALIBRATION_STALE
RESOURCE_EXHAUSTION
```

Errors should identify the physical reason, not merely return a generic compilation failure.

## 16. Core invariant

The compiler is successful only when the generated physical program is executable **and** its measured result remains traceable to the source workload through the complete provenance chain.
