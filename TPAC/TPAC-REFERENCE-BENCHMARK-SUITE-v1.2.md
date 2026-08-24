# TPAC — Reference Benchmark Suite v1.2

**Status:** Benchmark specification
**Date:** 2026-08-24

## 1. Benchmark philosophy

The benchmark suite is designed to answer one question:

> Where does the physical architecture produce an objectively useful computational advantage?

It is explicitly not designed to make TPAC win every benchmark.

---

## 2. Benchmark classes

```text
B1 spectral
B2 temporal
B3 memory
B4 nonlinear transformation
B5 optimization
B6 dynamical simulation
B7 routing
B8 sensing
B9 adaptive control
B10 end-to-end application
```

---

## 3. B1 — Spectral processing

Tasks:

- filtering;
- resonance identification;
- frequency discrimination;
- adaptive filtering.

Primary metrics:

```text
error
latency
energy
bandwidth
tuning time
```

---

## 4. B2 — Temporal processing

Tasks:

- sequence classification;
- prediction;
- anomaly detection;
- temporal pattern recall.

The benchmark must distinguish raw physical memory from learned readout capacity.

---

## 5. B3 — Memory

Measure:

```text
retention
write latency
read latency
write energy
read energy
endurance
state count
state separability
```

For multilevel memory, report effective information capacity rather than nominal state count.

---

## 6. B4 — Nonlinear transformation

Measure the ability to map inputs into separable physical states.

Use fixed downstream classifiers so the physical transformation itself can be evaluated.

---

## 7. B5 — Optimization

Use standardized small problems first.

Metrics:

- best solution;
- median solution;
- time-to-target;
- energy-to-target;
- success probability.

Report distributions, not only the best run.

---

## 8. B6 — Dynamical simulation

Compare physical evolution against reference numerical integration.

Metrics:

```text
trajectory error
stability
parameter sensitivity
runtime
energy
```

---

## 9. B7 — Routing

Measure reconfigurable signal routing.

Metrics:

- switching latency;
- insertion loss;
- isolation;
- crosstalk;
- energy;
- state retention.

---

## 10. B8 — Sensing

Use TPAC dynamics as a sensor rather than forcing a conventional-computing workload.

Measure:

- sensitivity;
- specificity;
- response time;
- energy;
- drift;
- environmental robustness.

---

## 11. B9 — Adaptive control

Close the loop:

```text
sensor
 ↓
TPAC processing
 ↓
controller
 ↓
physical system
 ↓
sensor
```

Measure stability and response under changing conditions.

---

## 12. B10 — End-to-end

Select a real application where one or more previous kernels demonstrate an advantage.

Measure the complete system from input acquisition to useful output.

---

## 13. Reference hardware baselines

Depending on workload, compare against appropriate combinations of:

```text
CPU
GPU
FPGA
ASIC
DSP
photonic processor
analog accelerator
reservoir computer
quantum processor
```

The quantum baseline is included only where the workload genuinely admits a meaningful comparison.

---

## 14. Full-stack accounting

Every benchmark reports:

```text
compute
memory
communication
control
cooling
calibration
readout
host overhead
```

---

## 15. Throughput normalization

Report both:

```text
raw physical throughput
end-to-end application throughput
```

The latter is the product-relevant number.

---

## 16. Energy normalization

Report:

```text
energy / operation
energy / inference
energy / solved instance
energy / bit processed
```

Select the unit appropriate to the workload.

---

## 17. Latency decomposition

Break latency into:

```text
input
encoding
physical evolution
readout
decoding
host transfer
```

This prevents hidden overhead from disappearing inside a single number.

---

## 18. Scaling curves

Every mature benchmark should provide performance as a function of:

- number of cells;
- workload size;
- precision;
- operating temperature;
- calibration age.

A single demonstration size is insufficient for architecture claims.

---

## 19. Robustness suite

Repeat benchmarks under:

- temperature variation;
- device variation;
- input noise;
- calibration drift;
- partial cell failure;
- control perturbation.

---

## 20. Reproducibility package

A benchmark release should contain:

```text
workload definition
input dataset
software version
compiler configuration
hardware identity
calibration snapshot
raw output
analysis code
results
uncertainty
```

---

## 21. Benchmark maturity

```text
D0 proposed
D1 simulated
D2 laboratory
D3 replicated
D4 independent
D5 comparative
D6 production-relevant
```

No benchmark should skip maturity levels silently.

---

## 22. Decision matrix

After measurement, each workload is classified:

```text
TPAC ADVANTAGE
TPAC PARITY
CONVENTIONAL ADVANTAGE
INCONCLUSIVE
```

The architecture roadmap is updated from this matrix.

---

## 23. Natural-niche discovery

The benchmark suite is itself an experiment.

The final objective is to discover the intersection:

```text
physical strengths
∩
computational requirements
∩
customer value
```

That intersection defines TPAC's real market rather than a predetermined one.
