# TPAC Safety Case v5.0

## Objective

Construct an explicit argument that TPAC can operate within defined physical safety boundaries.

## Safety argument structure

```text
CLAIM
→ SUBCLAIMS
→ EVIDENCE
→ ASSUMPTIONS
→ LIMITATIONS
```

## Hazard classes

```text
THERMAL
ELECTRICAL
MECHANICAL
RADIATIVE
CRYOGENIC
CONTROL
DATA-INTEGRITY
ENVIRONMENTAL
```

Only hazards relevant to a concrete implementation are activated.

## Safety requirements

Every physical actuator declares limits, interlocks, and failure behavior.

## Independent shutdown

Where practical, emergency shutdown must not depend exclusively on the software component responsible for ordinary operation.

## Safe states

Each physical module defines a validated bounded state for fault conditions.

## Evidence hierarchy

Safety evidence distinguishes:

```text
ANALYTICAL
SIMULATED
COMPONENT_TEST
INTEGRATED_TEST
OPERATIONAL
```

## Change impact

Hardware, firmware, calibration, or control changes trigger safety-case impact analysis.

## Residual risk

Unresolved hazards remain explicit with owner, mitigation status, and acceptance basis.

## Core invariant

**A TPAC system is not considered safe because it usually behaves safely; its safety argument must identify hazards, controls, evidence, and remaining uncertainty.**
