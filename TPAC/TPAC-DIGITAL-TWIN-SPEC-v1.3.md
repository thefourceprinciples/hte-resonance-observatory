# TPAC Digital Twin Specification v1.3

## 1. Purpose

The digital twin is a continuously calibrated computational model of a physical TPAC device.

It is not a substitute for measurement.

## 2. Model layers

```text
geometry
 ↓
material parameters
 ↓
cell dynamics
 ↓
coupling model
 ↓
network dynamics
 ↓
control response
 ↓
readout model
```

## 3. Parameter classes

### Directly measured

Values obtained from instruments.

### Inferred

Values estimated from measurements.

### Assumed

Values introduced as modeling assumptions.

These classes must never be conflated.

## 4. Calibration loop

```text
MODEL
 ↓
PREDICT
 ↓
EXPERIMENT
 ↓
COMPARE
 ↓
UPDATE PARAMETERS
 ↓
MODEL
```

## 5. Model versioning

Every prediction references:

```text
model version
parameter snapshot
training/calibration data
software version
```

## 6. Prediction confidence

Predictions should report confidence that reflects distance from experimentally validated operating regimes.

Extrapolation beyond measured regimes should be explicitly flagged.

## 7. Twin-to-hardware validation

Validation compares:

```text
predicted trajectory
measured trajectory
```

using predefined metrics.

## 8. Discovery mode

When measurements consistently disagree with the model, the discrepancy becomes an experimental target rather than being automatically treated as noise.

## 9. Anti-hallucination rule

The digital twin may propose hypotheses, but only physical measurement can promote a hypothesis into a hardware fact.

## 10. Core invariant

The twin exists to shorten the experiment-design loop while preserving a strict distinction between simulation and observation.
