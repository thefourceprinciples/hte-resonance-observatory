# TPAC Resource and Scheduling Architecture v1.9

## Objective

Schedule physical workloads while accounting for resources that do not exist in conventional digital processors: coupling paths, state occupancy, thermal recovery, calibration age, and physical interference.

## 1. Resource classes

```text
CELL
EDGE
CONTROL_CHANNEL
READOUT_CHANNEL
THERMAL_CAPACITY
TIMING_WINDOW
CALIBRATION_PROFILE
```

## 2. Resource graph

The scheduler maintains a live resource graph rather than a static device description.

```text
available
reserved
occupied
degraded
blocked
unknown
```

## 3. Job specification

A job declares:

```text
required cells
required topology
execution duration
state-retention requirement
readout requirement
energy budget
uncertainty bound
priority
```

## 4. Scheduling objective

Minimize a configurable cost:

```text
C = α latency
  + β energy
  + γ routing
  + δ thermal recovery
  + ε uncertainty
  + ζ calibration overhead
```

Weights are workload-dependent and versioned.

## 5. Conflict classes

Detect:

- cell conflicts;
- edge conflicts;
- control conflicts;
- readout conflicts;
- thermal conflicts;
- timing conflicts;
- calibration conflicts.

## 6. Thermal-aware scheduling

Jobs that heat shared physical regions must include recovery time or be routed to alternate resources.

## 7. State-aware scheduling

A cell containing useful persistent state cannot be treated as free merely because its controller channel is idle.

## 8. Preemption

Preemption is permitted only where physical state semantics support it. Otherwise a job must complete, checkpoint, or be explicitly aborted.

## 9. Priority

Priority classes:

```text
SAFETY
CALIBRATION
REALTIME
INTERACTIVE
BATCH
EXPERIMENTAL
```

Safety always supersedes computation.

## 10. Scheduling fairness

Long-running experimental workloads must not indefinitely starve interactive or maintenance operations.

## 11. Queue provenance

Queue events are recorded so reported latency can distinguish:

```text
queue time
resource wait
physical execution
readout
postprocessing
```

## 12. Dynamic rescheduling

The scheduler may remap a job when:

- a device degrades;
- a thermal boundary is approached;
- calibration expires;
- a resource becomes unavailable.

Remapping creates a new mapping identifier while retaining the same logical job identity.

## 13. Reservation semantics

Reservations expire unless renewed. Stale reservations cannot permanently strand physical resources.

## 14. Scheduling simulation

Candidate schedules should be evaluated against the digital twin before hardware execution where the model is sufficiently validated.

## 15. Scheduler benchmark

Evaluate:

- throughput;
- end-to-end latency;
- resource utilization;
- energy;
- remapping frequency;
- failed admissions;
- thermal violations;
- fairness.

## 16. Core invariant

**A TPAC scheduler must schedule physical state and physical constraints, not merely computational instructions.**
