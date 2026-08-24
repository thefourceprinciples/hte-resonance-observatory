# TPAC Safety and Failure Architecture v1.6

## Objective

Define hardware, software, experimental, and operational controls that prevent uncontrolled physical excitation, misleading measurements, and silent corruption of computational state.

## 1. Safety hierarchy

```text
PHYSICAL SAFETY
→ INSTRUMENT SAFETY
→ DEVICE INTEGRITY
→ DATA INTEGRITY
→ COMPUTATIONAL CORRECTNESS
```

A higher-layer success cannot compensate for a lower-layer failure.

## 2. Safe operating envelope

Each device publishes:

```text
max drive
max optical power
max acoustic amplitude
thermal limits
allowed frequencies
allowed transition rates
safe states
```

The runtime rejects commands outside the envelope.

## 3. Interlock classes

### Hard interlock

Immediately disables excitation when a physical safety boundary is exceeded.

### Soft interlock

Pauses execution and requests diagnostic evaluation.

### Advisory

Records a warning without interrupting execution.

## 4. Watchdogs

Independent watchdogs monitor:

- control process;
- temperature;
- excitation level;
- detector saturation;
- communication heartbeat;
- state divergence.

## 5. Fail-safe state

A fault should drive the system toward a known low-energy state whenever physically possible.

## 6. Fault containment

Partition the fabric so a failed cell or module cannot automatically propagate uncontrolled excitation through the entire system.

## 7. Data corruption protection

Measurements are written atomically with:

```text
timestamp
sequence number
checksum
instrument identity
calibration identity
```

Incomplete records are marked invalid rather than repaired silently.

## 8. Sensor disagreement

If redundant sensors disagree beyond a predefined tolerance:

```text
execution → PAUSED
state → UNKNOWN
operator/runtime → DIAGNOSTIC
```

The system must not choose the more convenient measurement without evidence.

## 9. Thermal runaway response

```text
threshold crossed
 ↓
reduce/disable drive
 ↓
measure temperature
 ↓
wait for recovery
 ↓
validate device
 ↓
resume or fail
```

## 10. Detector saturation

Saturated readout cannot be treated as a valid measurement. The run is flagged and repeated under an appropriate operating point.

## 11. Calibration corruption

If calibration integrity cannot be verified, the device is removed from normal execution until recalibration succeeds.

## 12. State uncertainty

When the physical state cannot be distinguished confidently, the logical state is explicitly represented as `UNKNOWN` rather than being coerced into a valid state.

## 13. Recovery levels

```text
R0 retry measurement
R1 repeat operation
R2 recalibrate
R3 reset module
R4 isolate module
R5 remove device from service
```

Escalation is evidence-driven.

## 14. Failure evidence

Every failure record contains:

```text
failure_id
first_detected
hardware_state
software_state
measurements
trigger
response
recovery
root_cause_status
```

## 15. Root-cause discipline

Root cause labels:

```text
CONFIRMED
PROBABLE
POSSIBLE
UNKNOWN
```

`UNKNOWN` is a valid scientific result.

## 16. Fault-injection program

Regularly test recovery using controlled failures:

- dropped control packet;
- detector loss;
- stale calibration;
- thermal excursion;
- disabled cell;
- corrupted metadata;
- communication timeout.

## 17. Recovery validation

A recovery mechanism is not considered functional until fault injection demonstrates that it produces the expected safe state.

## 18. Security boundary

Control interfaces must authenticate commands and distinguish observation privileges from physical-control privileges.

## 19. Audit trail

Safety events are append-only and linked to the affected execution and device.

## 20. Core invariant

**When TPAC does not know the physical state, it must represent that uncertainty explicitly and stop pretending certainty exists.**
