# TPAC Simulation and Benchmark Harness v1.7

## Objective

Create a common harness for comparing physical TPAC execution, its digital twin, and conventional computational baselines without changing workload definitions between systems.

## 1. Benchmark layers

```text
L0 mathematical reference
L1 numerical simulation
L2 digital twin
L3 physical prototype
L4 packaged module
L5 production candidate
```

## 2. Workload specification

Each workload freezes:

```text
input distribution
output definition
precision target
termination condition
metric
baseline
energy boundary
latency boundary
```

## 3. Reference implementation

Every kernel has a trusted reference implementation used to generate expected outputs or independently verify correctness.

## 4. Simulation parity

Simulation and hardware use identical workload inputs where possible.

Differences in physical operating conditions are recorded explicitly.

## 5. Accuracy metrics

Select metrics appropriate to the workload:

- absolute error;
- relative error;
- classification accuracy;
- correlation;
- fidelity;
- convergence error.

## 6. Performance metrics

```text
latency
throughput
energy/job
energy/output
memory/state footprint
calibration overhead
setup time
```

## 7. Full-stack boundary

A performance claim must specify whether it includes:

```text
host preprocessing
transfer
TPAC execution
readout
decoding
postprocessing
calibration
cooling
```

## 8. Baseline selection

Baselines should be practical implementations rather than artificially weakened competitors.

Where multiple baselines are reasonable, report all of them.

## 9. Statistical protocol

For stochastic workloads:

- fix random seeds where appropriate;
- report number of trials;
- report confidence intervals;
- preserve individual trial results;
- avoid reporting only the best run.

## 10. Scaling harness

Run identical workloads over increasing:

```text
problem size
cell count
network depth
state count
```

Fit empirical scaling curves only over observed regimes.

## 11. Energy harness

Measure energy at the wall/system boundary appropriate to the claim.

Separate:

```text
active energy
idle energy
calibration energy
cooling energy
host energy
```

## 12. Latency harness

Report:

```text
queue latency
initialization
calibration
execution
readout
decode
end-to-end
```

## 13. Reproducibility mode

A benchmark run can be exported as a self-contained manifest containing workload, hardware, software, calibration, randomization, and analysis identifiers.

## 14. Regression testing

Every compiler/runtime/device revision runs a fixed regression suite before being promoted.

Regression categories:

```text
correctness
performance
energy
stability
provenance
safety
```

## 15. Drift detection

Compare current benchmark distributions against historical distributions.

A statistically significant degradation creates a regression event even if the result remains above the minimum acceptance threshold.

## 16. Benchmark anti-gaming rule

A benchmark optimization may not alter the workload, metric, accounting boundary, or baseline without creating a new benchmark version.

## 17. Result visualization

The harness should produce machine-readable results first and visual summaries second.

## 18. Benchmark status

```text
DRAFT
LOCKED
RUNNING
VALIDATED
REPLICATED
RETIRED
```

## 19. Promotion gate

A physical advantage moves from `VALIDATED` to `REPLICATED` only after execution on independent runs and, where practical, independent devices.

## 20. Core invariant

**TPAC performance is meaningful only when correctness, energy, latency, overhead, and baseline choice are all visible in the same accounting frame.**
