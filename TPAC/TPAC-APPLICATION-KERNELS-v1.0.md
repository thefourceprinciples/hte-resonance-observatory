# TPAC — Application Kernels v1.0

**Status:** Workload architecture
**Date:** 2026-08-24

## Purpose

Define concrete computational kernels that can be used to determine where TPAC's physical dynamics are actually useful.

---

# 1. Kernel selection rule

A kernel belongs in the TPAC benchmark suite when its dominant operation maps naturally onto at least one demonstrated physical primitive.

The benchmark must compare against the strongest practical conventional baseline.

---

# 2. Spectral filter kernel

### Mathematical form

```text
Y(f) = H(f)X(f)
```

### Natural TPAC mapping

Resonant transmission/reflection.

### Measurements

- bandwidth;
- selectivity;
- insertion loss;
- energy per processed signal;
- tuning latency.

### Baselines

Digital FIR/IIR, FPGA DSP, conventional photonic filter.

---

# 3. Temporal reservoir kernel

### Input

Time series `x(t)`.

### Physical operation

Drive nonlinear network and sample transient state.

### Readout

Train only the external readout layer initially.

### Metrics

- classification accuracy;
- inference latency;
- energy;
- memory capacity;
- robustness to noise.

---

# 4. Associative recall kernel

Store patterns as attractors.

```text
noisy input
   ↓
physical evolution
   ↓
attractor
   ↓
recovered pattern
```

Measure capacity and basin size.

---

# 5. Dynamical-system solver

Encode parameters of:

```text
dx/dt = F(x)
```

into physical coupling.

Let the system evolve.

Decode the resulting state.

Compare against numerical reference.

---

# 6. Optimization kernel

Map a small objective landscape onto physical state.

Allow relaxation to identify low-energy configurations.

Measure:

- solution quality;
- time-to-solution;
- energy-to-solution;
- repeatability.

---

# 7. Pattern transformation kernel

Encode an input pattern into a physical state.

Apply nonlinear transformation.

Read transformed representation.

Benchmark feature separability.

---

# 8. State-dependent routing kernel

```text
state S0 → output A
state S1 → output B
```

Benchmark routing latency, energy, loss, and reliability.

---

# 9. In-memory transformation kernel

Store state and process an incoming signal without moving the state into external digital memory.

Measure total data-movement energy against conventional memory-plus-accelerator architecture.

---

# 10. Adaptive filter kernel

Use state-dependent resonance to alter filter characteristics dynamically.

```text
input statistics
      ↓
state update
      ↓
new transfer function
```

Benchmark adaptation speed and stability.

---

# 11. Physical matrix operation

Explore whether coupled propagation can implement a useful linear transformation:

```text
Y = WX
```

The physical network represents `W` through coupling parameters.

Measure accuracy, programmability, and reconfiguration cost.

---

# 12. Nonlinear feature map

Map input `x` into physical state:

```text
φ(x) = physical_evolution(x)
```

Evaluate whether a simple downstream classifier benefits from the resulting feature space.

This creates a direct benchmark for physical machine learning.

---

# 13. Event-driven kernel

Encode information as events rather than continuous streams.

Test whether asynchronous physical dynamics reduce energy or latency for sparse workloads.

---

# 14. Analog memory kernel

Test continuous or multilevel state storage.

Metrics:

- dynamic range;
- state distinguishability;
- drift;
- write energy;
- read disturbance.

---

# 15. Search kernel

Represent candidate solutions as physical configurations.

Use natural relaxation to eliminate high-cost states.

Measure scaling empirically rather than extrapolating from small demonstrations.

---

# 16. Hybrid kernel

Combine:

```text
CPU preprocessing
→ TPAC physical transformation
→ CPU/GPU decoding
```

Benchmark complete end-to-end performance.

This is likely to be the most realistic early deployment mode.

---

# 17. Kernel registry

Every benchmark implementation receives:

```text
kernel_id
version
physical_backend
workload_definition
input_encoding
output_encoding
baseline
metrics
provenance
```

---

# 18. Kernel maturity

```text
K0 conceptual
K1 simulated
K2 single-cell demonstrated
K3 network demonstrated
K4 replicated
K5 benchmarked
K6 product candidate
```

A kernel's maturity must never be inferred from another kernel's success.

---

# 19. Benchmark reporting

Every kernel report includes:

```text
correctness
latency
throughput
energy
memory/state cost
calibration cost
hardware cost
software overhead
uncertainty
baseline comparison
```

---

# 20. Kernel portfolio principle

TPAC does not need to win every computational workload.

A defensible architecture can be valuable if it produces strong advantages in a narrow class of workloads while conventional systems remain superior elsewhere.

The benchmark program therefore seeks the **natural computational niche** of the physical substrate.
