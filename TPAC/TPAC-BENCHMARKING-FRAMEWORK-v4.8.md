# TPAC Benchmarking Framework v4.8

## Objective

Create fair comparisons between TPAC implementations and alternative computational systems.

## Benchmark dimensions

```text
CORRECTNESS
LATENCY
THROUGHPUT
ENERGY
THERMAL COST
RESOURCE OCCUPANCY
CALIBRATION OVERHEAD
RECOVERY
REPRODUCIBILITY
```

## Workload classes

Use representative workloads rather than a single favorable demonstration.

## Baselines

Every benchmark identifies the baseline system, implementation version, hardware configuration, and optimization state.

## Boundary disclosure

Report whether measurements include:

```text
host
control
cooling
calibration
readout
interconnect
recovery
```

## Statistical reporting

Report distributions and uncertainty. Avoid selecting only peak observations unless the benchmark explicitly measures peak performance.

## Warm-up and initialization

Separate initialization, calibration, warm-up, steady-state, and shutdown costs.

## Repeated trials

Record trial count, failed runs, exclusions, and exclusion criteria.

## Scaling benchmarks

Measure scaling empirically across workload and hardware size. Do not infer scaling from a single point.

## Reproducibility

Publish benchmark manifests and result provenance sufficient for independent reruns where possible.

## Core invariant

**A performance claim is meaningful only when its measurement boundary and comparison baseline are explicit.**
