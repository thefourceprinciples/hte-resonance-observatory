# TPAC Cost and Resource Model v3.1

## Objective

Define a complete cost model so TPAC optimization cannot hide physical overhead behind a narrow device metric.

## 1. Cost domains

```text
CAPEX
FABRICATION
PACKAGING
CONTROL
COOLING
CALIBRATION
COMPUTE
INTERCONNECT
MAINTENANCE
FAILURE
```

## 2. Execution cost

For each workload:

```text
C_total = host + control + device + cooling + readout + calibration + interconnect + recovery
```

## 3. Capacity cost

Track resource occupancy over time:

```text
cell-seconds
channel-seconds
thermal-capacity-seconds
readout-seconds
```

## 4. Manufacturing cost

Record yield and scrap alongside nominal fabrication cost.

## 5. Reliability cost

Include replacement, downtime, recalibration, and recovery where relevant to the deployment model.

## 6. Cost per useful result

```text
C_useful = total lifecycle cost / accepted useful outputs
```

The denominator must use a declared correctness criterion.

## 7. Scenario model

Support:

```text
prototype
pilot
small production
large production
```

Each scenario uses independently documented assumptions.

## 8. Sensitivity analysis

Identify which parameters dominate projected cost. Sensitivity results remain labeled as forecasts.

## 9. Cost provenance

Every model output references:

```text
input dataset
assumption set
model version
calculation version
```

## 10. Benchmark separation

Scientific performance claims and economic projections are separate evidence classes. A projected cost advantage is not physical evidence.

## 11. Core invariant

**TPAC optimization must minimize the cost of obtaining correct, reproducible computation—not merely the cost of the active physical operation.**
