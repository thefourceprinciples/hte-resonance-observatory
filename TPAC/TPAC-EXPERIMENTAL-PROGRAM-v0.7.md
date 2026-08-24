# TPAC — Experimental Program v0.7

**Status:** Laboratory research plan
**Date:** 2026-08-24

## Objective

Convert the TPAC architecture into a sequence of controlled experiments where each result either establishes, constrains, or falsifies a specific hypothesis.

No experiment is considered successful merely because a signal is observed. The relevant question is whether the signal demonstrates the claimed physical mechanism with sufficient controls.

---

# 1. Experimental doctrine

Every experiment has:

```text
HYPOTHESIS
CONTROL
MEASUREMENT
NULL RESULT
SUCCESS CRITERION
FAILURE CRITERION
UNCERTAINTY
REPLICATION PLAN
```

A visually impressive trace is not evidence of computation by itself.

---

# 2. E0 — Baseline characterization

Measure the unperturbed system.

Record:

- resonances;
- losses;
- noise floor;
- thermal baseline;
- acoustic spectrum;
- optical spectrum;
- environmental sensitivity.

Purpose: establish the null model.

---

# 3. E1 — Optical characterization

Map optical response as a function of frequency, amplitude, polarization, and geometry.

Deliverable:

```text
optical transfer function H_o(f, P, geometry)
```

---

# 4. E2 — Acoustic characterization

Map acoustic modes and damping.

Deliverable:

```text
acoustic transfer function H_a(f, drive, geometry)
```

---

# 5. E3 — Optoacoustic coupling

Test whether optical excitation measurably modifies acoustic response and vice versa.

Controls:

- detuned optical source;
- geometry without intended overlap;
- reduced drive;
- independent acoustic excitation.

Deliverable:

```text
coupling coefficient + uncertainty
```

---

# 6. E4 — Nonlinearity

Measure whether response departs from the linear model.

Fit competing models:

```text
linear
quadratic
saturating
hysteretic
coupled nonlinear
```

Do not label a response “quantum” merely because it is nonlinear.

---

# 7. E5 — State formation

Search for reproducible states that differ in measurable output.

Protocol:

```text
initialize
→ drive
→ release
→ wait
→ read
→ repeat
```

Cluster the resulting states statistically.

---

# 8. E6 — Write/read cycle

Test:

```text
WRITE → HOLD → READ → HOLD → READ → RESET
```

Measure:

- fidelity;
- retention;
- energy;
- latency;
- endurance.

---

# 9. E7 — Multistability

Determine whether multiple stable/metastable states exist.

Test state count conservatively.

A continuum of noisy values is not automatically multilevel memory.

---

# 10. E8 — State-dependent transformation

Initialize two states and apply identical input.

Test whether:

```text
input + state A → output A
input + state B → output B
```

with statistically significant separation.

This is the first direct test of **stateful computation**.

---

# 11. E9 — Directional transport

Measure forward and reverse transmission under matched conditions.

Control for:

- ordinary loss;
- frequency response;
- source mismatch;
- detector mismatch;
- temperature gradients.

Only after these controls should asymmetry be interpreted.

---

# 12. E10 — State-dependent routing

Test whether changing cell state changes propagation path or transmission.

Desired observation:

```text
state A → path 1
state B → path 2
```

This establishes the physical basis for topology-as-state.

---

# 13. E11 — Two-cell coupling

Build the smallest network.

Measure:

- mutual influence;
- synchronization;
- coupling strength;
- cross-talk;
- correlated state transitions.

---

# 14. E12 — Three-cell topology

Introduce a third cell and test whether network behavior differs qualitatively from isolated cells.

Possible outcomes:

- propagation;
- collective modes;
- interference;
- attractor behavior;
- instability.

---

# 15. E13 — Network memory

Apply a sequence of inputs and determine whether output depends on history.

Formally test:

```text
output(t) ≠ f(input(t))
```

and instead:

```text
output(t) = f(input(t), history)
```

This is a key reservoir-computing criterion.

---

# 16. E14 — Reservoir benchmark

Use a standardized temporal classification workload.

Compare:

- TPAC reservoir;
- digital reservoir baseline;
- conventional ML baseline.

Report total system energy and latency.

---

# 17. E15 — Associative memory

Store patterns and test noisy recall.

Metrics:

```text
capacity
basin size
recall accuracy
convergence time
energy
```

---

# 18. E16 — Physical solver

Implement a simple dynamical equation with a known analytical or numerical solution.

Compare physical trajectory against reference solution.

Report error as a function of time and operating point.

---

# 19. E17 — Optimization

Encode a small combinatorial problem.

Compare TPAC relaxation against classical heuristic baselines.

Measure solution quality, energy, and time-to-solution.

---

# 20. E18 — Reconfiguration

Change network topology during execution.

Demonstrate:

```text
program A
 ↓
reconfigure
 ↓
program B
```

without physically replacing the device.

---

# 21. E19 — Fault injection

Intentionally perturb or disable selected cells.

Measure whether the compiler/runtime can reroute around faults.

---

# 22. E20 — Manufacturing variation

Test multiple nominally identical cells.

Measure distributions rather than best-case performance.

Key question:

> Can calibration-aware compilation recover useful performance from fabrication variation?

---

# 23. E21 — Scaling

Increase cell count systematically.

Fit empirical scaling laws for:

```text
error(N)
energy(N)
latency(N)
crosstalk(N)
calibration(N)
```

---

# 24. E22 — System-level benchmark

Only after previous gates succeed, compare a complete TPAC system against appropriate conventional systems.

Include all overhead.

---

# 25. Independent replication

Release:

- geometry;
- fabrication details;
- control sequence;
- raw data;
- analysis;
- uncertainty;
- failed trials.

Invite independent reproduction.

---

# 26. Experimental ledger

Every run receives a unique identifier.

```text
TPAC-YYYYMMDD-DEVICE-EXPERIMENT-RUN
```

Store immutable metadata and hashes for raw data.

---

# 27. Negative-result policy

Failed experiments remain in the archive.

They are categorized:

```text
HYPOTHESIS FAILED
CONTROL FAILED
INSTRUMENT FAILED
FABRICATION FAILED
MODEL INSUFFICIENT
INCONCLUSIVE
```

This prevents selective reporting.

---

# 28. Statistical policy

Use predefined analysis methods whenever possible.

Avoid changing success criteria after inspecting the data.

Report:

- effect size;
- uncertainty interval;
- sample count;
- replication count;
- model assumptions.

---

# 29. Model hierarchy

Use the simplest model that explains the data.

```text
M0 null
M1 linear
M2 nonlinear
M3 coupled
M4 history-dependent
M5 adaptive
```

Move upward only when measurements justify the additional complexity.

---

# 30. Final experimental criterion

TPAC should not be judged by whether the first device looks extraordinary.

It should be judged by whether a chain of independently controlled experiments demonstrates:

```text
physical coupling
      ↓
state
      ↓
controlled transition
      ↓
state-dependent transformation
      ↓
network computation
      ↓
useful workload
      ↓
measured system advantage
```

That chain is the evidentiary backbone of the project.
