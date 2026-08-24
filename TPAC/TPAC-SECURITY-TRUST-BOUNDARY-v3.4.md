# TPAC Security and Trust Boundary v3.4

## Objective

Define security boundaries for a machine whose software can cause physical state changes.

## 1. Trust zones

```text
UNTRUSTED APPLICATION
→ POLICY GATE
→ COMPILER
→ VERIFIED CONTROL MANIFEST
→ DEVICE CONTROLLER
→ PHYSICAL SYSTEM
```

## 2. Principle of least privilege

Application processes receive no physical-control privilege unless explicitly required.

## 3. Signed artifacts

Where supported, authenticate:

- firmware;
- compiler artifacts;
- control manifests;
- calibration packages;
- device passports.

## 4. Physical command authorization

Before actuation verify:

```text
identity
authorization
capability
safety envelope
artifact integrity
calibration validity
```

## 5. Separation of observation and control

Read-only scientific observation should remain possible even when physical-control privileges are disabled.

## 6. Secure recovery

Recovery procedures must fail toward a bounded physical state rather than requiring unrestricted control access.

## 7. Audit events

Record authorization decisions, rejected commands, privilege changes, and emergency interventions.

## 8. Supply-chain provenance

Hardware, firmware, software, calibration, and configuration dependencies receive linked provenance records.

## 9. Compromise response

A suspected compromised component is quarantined and its outputs are marked accordingly until validated.

## 10. Core invariant

**No software layer should obtain more authority over the physical machine than is necessary for its declared function.**
