# TPAC Failure Injection Catalog v5.9

## Objective

Systematically test whether TPAC detects, contains, and records failures rather than interpreting them as successful operation.

## Fault domains

```text
POWER
THERMAL
TIMING
COMMUNICATION
CALIBRATION
SENSOR
ACTUATOR
FIRMWARE
SOFTWARE
PROVENANCE
SECURITY
```

## Injection record

```text
fault_id
target
precondition
injection_method
expected_detection
expected_safe_state
evidence_required
recovery_path
```

## Categories

### Transient
Short-lived faults that recover without persistent state corruption.

### Persistent
Faults requiring repair, reconfiguration, or quarantine.

### Latent
Faults that remain undetected until a dependent operation exercises the affected component.

### Byzantine
Incorrect or contradictory outputs that remain syntactically valid.

## Evidence requirement

A successful fault test records both the injected condition and the system's observed response.

## Safety boundary

Fault injection must never bypass independent safety controls merely to demonstrate a failure mode.

## Recovery verification

Recovery is not considered successful until state, calibration, provenance, and capability checks pass.

## Regression

Previously detected faults become permanent regression cases.

## Core invariant

**A resilient TPAC system is demonstrated by controlled failure, detection, containment, evidence preservation, and verified recovery.**
