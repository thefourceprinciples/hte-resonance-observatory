# TPAC Digital Twin Contract v3.5

## Objective

Define the minimum contract required for a digital twin to remain scientifically useful without being mistaken for the physical machine.

## 1. Twin layers

```text
GEOMETRY
MATERIAL
DYNAMICS
CONTROL
THERMAL
READOUT
FAILURE
```

Each layer declares its validation status.

## 2. Parameter provenance

Every model parameter references its source:

```text
measured
calibrated
fitted
assumed
forecast
```

## 3. Validation hierarchy

```text
component
→ cell
→ coupling
→ cluster
→ module
→ workload
```

A model validated at one level cannot automatically be treated as validated at the next.

## 4. Prediction registry

Before a physical comparison, record model predictions so post-hoc parameter adjustment cannot masquerade as prediction.

## 5. Parameter fitting

Fitted parameters use training data distinct from holdout validation data whenever practical.

## 6. Uncertainty propagation

Propagate parameter uncertainty into predicted outputs. Point predictions without uncertainty are insufficient for claims requiring quantitative agreement.

## 7. Model discrepancy

Maintain a separate discrepancy term for behavior not captured by the model.

## 8. Twin-to-hardware divergence

Track divergence over time and by operating regime.

## 9. Twin update policy

A model update records:

```text
old version
new version
changed parameters
reason
new evidence
validation results
```

## 10. Anti-circularity rule

Hardware data used to validate the twin cannot simultaneously be presented as independent evidence for the twin's prediction.

## 11. Core invariant

**A digital twin is a hypothesis-bearing model of the machine, not a substitute for measurement of the machine.**
