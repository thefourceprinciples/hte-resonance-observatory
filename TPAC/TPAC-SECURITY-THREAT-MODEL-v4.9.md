# TPAC Security Threat Model v4.9

## Objective

Model threats against a physical-computational system whose software can influence physical state and whose measurements can influence subsequent decisions.

## Assets

```text
PHYSICAL_STATE
CONTROL_AUTHORITY
CALIBRATION_STATE
RAW_MEASUREMENTS
PROVENANCE
FIRMWARE
WORKLOADS
RESULTS
```

## Threat classes

```text
UNAUTHORIZED_CONTROL
DATA_TAMPERING
PROVENANCE_TAMPERING
CALIBRATION_TAMPERING
REPLAY
DENIAL_OF_SERVICE
SIDE_CHANNEL
SUPPLY_CHAIN
INSIDER
MODEL_MANIPULATION
```

## Attack surface

Identify interfaces at application, compiler, runtime, controller, interconnect, device, measurement, and evidence boundaries.

## Threat record

```text
threat_id
asset
entry_point
attacker_capability
precondition
impact
detection
mitigation
residual_risk
```

## Control priority

Safety-critical physical commands receive stronger controls than ordinary telemetry.

## Provenance attacks

A result whose lineage is altered must become distinguishable from the original result.

## Replay protection

State-changing commands carry execution context sufficient to prevent unsafe reuse of stale commands.

## Calibration integrity

Calibration records require integrity protection and validity checks before use in control or analysis.

## Supply-chain boundary

Hardware, firmware, dependencies, build artifacts, and configuration are included in the threat model.

## Incident response

```text
DETECT
→ CONTAIN
→ PRESERVE EVIDENCE
→ ASSESS
→ RECOVER
→ VALIDATE
→ REVIEW
```

## Core invariant

**Security failures must not be allowed to masquerade as physical phenomena, valid measurements, or successful computation.**
