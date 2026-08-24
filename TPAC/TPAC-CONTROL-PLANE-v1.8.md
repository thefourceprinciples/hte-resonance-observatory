# TPAC Control Plane v1.8

## Objective

Define the control-plane architecture required to translate high-level execution requests into bounded physical actions while preserving timing, safety, calibration, and provenance.

## 1. Control hierarchy

```text
HOST API
 ↓
JOB MANAGER
 ↓
RUNTIME
 ↓
SCHEDULER
 ↓
DEVICE CONTROLLER
 ↓
ACTUATORS
 ↓
PHYSICAL STATE
 ↓
SENSORS
```

## 2. Control domains

Separate:

- excitation control;
- state initialization;
- routing control;
- readout control;
- thermal control;
- safety control;
- calibration control.

Safety control has authority to override computational control.

## 3. Timing model

Every control event carries:

```text
event_id
target
effective_time
duration
amplitude
frequency
phase
precedence
```

## 4. Deterministic scheduling

Where the physical system permits deterministic timing, the scheduler should generate a reproducible event schedule.

For stochastic dynamics, the runtime records the realized timing and uncertainty.

## 5. Feedback channels

Feedback may include:

```text
state estimate
amplitude
phase
frequency
thermal state
error signal
```

Feedback policies must specify whether they are fixed, adaptive, or learned.

## 6. Controller states

```text
INIT
ARMED
READY
RUNNING
FEEDBACK
SAFE
FAULT
```

## 7. Command validation

Before actuation, validate:

- device identity;
- target capability;
- calibration freshness;
- safe operating envelope;
- resource ownership;
- timing validity;
- provenance metadata.

## 8. Atomic control groups

Related physical operations should be grouped into atomic control sequences where partial execution would create an invalid state.

## 9. Backpressure

If physical processing cannot accept new events, upstream software must receive an explicit backpressure signal rather than silently queueing unbounded work.

## 10. Clock architecture

The system may require multiple timing domains:

```text
host clock
controller clock
sensor clock
physical oscillation
```

Cross-domain synchronization must be measured and represented in execution metadata.

## 11. Calibration injection

Calibration procedures must use the same control pathway as normal execution where practical, so calibration measurements characterize the actual actuation chain.

## 12. Controller observability

Every command should be traceable to:

```text
job
execution
schedule
controller
hardware channel
measurement response
```

## 13. Control-loop stability

Closed-loop controllers require experimentally established stability margins. A controller that produces useful behavior in simulation but destabilizes the physical system is rejected.

## 14. Saturation handling

Actuator saturation is an explicit state. The controller must not assume commanded amplitude equals delivered amplitude.

## 15. Latency compensation

Measured control and readout latency should be incorporated into feedback policies rather than ignored.

## 16. Control replay

A completed execution should be replayable against simulation or a compatible device using the recorded control manifest.

## 17. Control-plane invariant

**Every physical action must be bounded, attributable, observable, and interruptible by a higher-priority safety mechanism.**
