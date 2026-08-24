# TPAC Runtime Specification v1.2

## 1. Runtime role

The runtime is the control system between compiled programs and physical hardware.

```text
JOB
 ↓
RESOURCE RESERVATION
 ↓
CALIBRATION CHECK
 ↓
PHYSICAL EXECUTION
 ↓
READOUT
 ↓
VALIDATION
 ↓
RESULT
```

## 2. Resource manager

Resources include:

- cells;
- coupling paths;
- control channels;
- readout channels;
- thermal budget;
- timing windows.

## 3. Job lifecycle

```text
QUEUED
→ ADMITTED
→ RESERVED
→ INITIALIZING
→ EXECUTING
→ READING
→ VALIDATING
→ COMPLETE
```

Exceptional states:

```text
PAUSED
RETRYING
RECOVERING
FAILED
CANCELLED
```

## 4. Admission control

Reject a job when:

- required physical capabilities are unavailable;
- calibration is stale;
- thermal capacity is insufficient;
- uncertainty cannot meet the requested bound;
- required isolation cannot be guaranteed.

## 5. Execution modes

### Open-loop

Precomputed controls execute without feedback.

### Closed-loop

Measurements modify subsequent control.

### Adaptive

The runtime can select alternate mappings or operating points according to measured state.

## 6. State checkpoint

Checkpoint when physically meaningful:

```text
logical state
physical state estimate
measurement timestamp
calibration version
thermal state
```

## 7. Fault recovery

```text
FAULT
 ↓
STOP EXCITATION
 ↓
ISOLATE
 ↓
READ
 ↓
RESET/RECOVER
 ↓
RECALIBRATE
 ↓
RETRY OR FAIL
```

## 8. Result object

A TPAC result should contain:

```text
value
confidence
uncertainty
latency
energy
hardware ID
provenance ID
execution status
```

## 9. Measurement integrity

Raw measurements are immutable inputs to analysis. Derived values must reference the raw measurement identifier.

## 10. Runtime invariant

No physical result is considered final until its execution status, measurement integrity, and provenance record are complete.
