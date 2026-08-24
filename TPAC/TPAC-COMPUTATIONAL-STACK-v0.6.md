# TPAC — Computational Stack v0.6

**Status:** Research architecture
**Date:** 2026-08-24

## 0. Scope

This document specifies the software and control stack required to turn a TPAC physical fabric into a programmable machine.

The stack is deliberately designed around physical dynamics rather than pretending the substrate behaves like conventional CMOS.

---

# 1. Complete stack

```text
APPLICATION
    ↓
TPAC DSL / API
    ↓
COMPILER
    ↓
PHYSICAL IR
    ↓
PLACER / ROUTER
    ↓
PULSE SCHEDULER
    ↓
CALIBRATION ENGINE
    ↓
CONTROL FIRMWARE
    ↓
INSTRUMENT INTERFACE
    ↓
TPAC FABRIC
    ↓
SENSORS
    ↓
READOUT / DECODER
    ↓
RESULT + PROVENANCE
```

The machine is incomplete if any layer is missing.

---

# 2. TPAC programming abstraction

A program describes desired physical transformations.

Example:

```text
reservoir(signal)
store(state)
route(condition)
relax(network)
read(region)
```

These are compiled into calibrated physical actions.

---

# 3. TPAC DSL

Candidate syntax:

```text
fabric F;
cell C1, C2, C3;

input C1 <- waveform;

couple C1 -> C2 strength 0.42;
couple C2 -> C3 strength 0.31;

state C1 = S2;

relax C1:C3 for 200 ns;

read C1:C3 -> output;
```

The DSL should expose physical concepts directly rather than hiding them behind artificial transistor abstractions.

---

# 4. Physical intermediate representation

Every compiled program becomes a graph:

```text
NODE {
  cell
  state
  operation
  tolerance
}

EDGE {
  source
  destination
  coupling
  direction
  timing
}
```

This IR is independent of any specific material implementation.

---

# 5. Compiler passes

## Pass 1 — semantic lowering

Translate application operations into physical primitives.

## Pass 2 — topology selection

Choose a network configuration.

## Pass 3 — placement

Map logical nodes to physical cells.

## Pass 4 — routing

Select physical paths.

## Pass 5 — pulse synthesis

Generate control waveforms.

## Pass 6 — calibration correction

Modify parameters according to measured device variation.

## Pass 7 — safety analysis

Reject schedules exceeding physical limits.

## Pass 8 — execution

Emit hardware commands.

## Pass 9 — decode

Convert physical observations into logical outputs.

---

# 6. Physical scheduler

The scheduler treats time, state, energy, and topology as resources.

A job can reserve:

```text
cells
modes
ports
energy budget
temperature budget
time window
readout channels
```

This is fundamentally different from a conventional instruction scheduler.

---

# 7. Calibration database

The runtime maintains a live model:

```text
cell → states → transitions → distributions
cell ↔ cell → coupling matrix
route → transmission distribution
condition → thermal response
```

Calibration confidence should accompany every physical parameter.

---

# 8. Probabilistic execution

If physical transitions are stochastic, the runtime should expose probability rather than hide it.

Example:

```text
transition A→B = 0.997 ± uncertainty
```

A workload may request:

```text
minimum transition fidelity = 0.999
```

and the compiler can reject mappings that cannot satisfy it.

---

# 9. Adaptive execution

The runtime can retry operations using alternate mappings.

```text
execute
  ↓
read confidence
  ↓
confidence low?
 /          \
no          yes
 |            |
finish      remap/retry
```

This allows the machine to operate statistically rather than requiring every physical event to be perfect.

---

# 10. Reservoir compiler

For reservoir workloads, the compiler need not synthesize a precise logical gate network.

Instead it chooses:

- topology;
- coupling strengths;
- operating point;
- input encoding;
- sampling interval;
- readout features.

The optimization target becomes workload performance rather than gate fidelity.

---

# 11. Attractor compiler

For associative computation, the compiler attempts to shape the energy/dynamical landscape.

Conceptually:

```text
desired pattern
     ↓
parameter constraints
     ↓
physical landscape
     ↓
attractor basin
```

This is a fundamentally different compilation problem from Boolean logic synthesis.

---

# 12. Analog compiler

Analog workloads compile mathematical operators into physical dynamics.

Example:

```text
dx/dt = F(x)
```

becomes a network whose measured evolution approximates `F`.

Compiler output includes an error bound:

```text
expected numerical error ≤ ε
```

where ε is experimentally validated for the operating regime.

---

# 13. Topology compiler

If coupling is state-dependent, the compiler can treat topology as a mutable resource.

```text
G(t0) → G(t1) → G(t2)
```

A program can therefore change its own physical computational graph during execution.

This should be treated as a distinct programming primitive:

```text
RECONFIGURE(graph_condition)
```

---

# 14. Physical garbage collection

Persistent physical states may need to be reset.

The runtime therefore tracks:

```text
allocated states
stale states
reset-required cells
thermal recovery
```

A future TPAC operating system may need a physical equivalent of garbage collection.

---

# 15. Thermal scheduling

The scheduler maintains a thermal map:

```text
T(x,y,t)
```

Operations that would cause unsafe or performance-degrading thermal accumulation are delayed or relocated.

Thermal state becomes a scheduling constraint rather than an external engineering detail.

---

# 16. Physical memory hierarchy

Potential hierarchy:

```text
fast volatile dynamical state
        ↓
metastable cell state
        ↓
phase-field state
        ↓
external digital memory
```

Different levels can be used for different retention requirements.

---

# 17. Data movement minimization

Because TPAC may process information in-place, the compiler should prefer:

```text
compute where data exists
```

over:

```text
move data → compute → move data back
```

This is a major architectural hypothesis to benchmark against conventional memory/accelerator systems.

---

# 18. Workload graph

Every application becomes a graph of data dependencies.

The compiler should search for mappings that maximize physical locality and parallel propagation.

```text
logical graph
      ↓
physical graph
      ↓
propagation schedule
```

---

# 19. Compiler cost function

A candidate mapping can be scored as:

```text
C = wE·energy
  + wL·latency
  + wX·crosstalk
  + wR·routing_cost
  + wT·thermal_cost
  + wQ·error
```

Weights are workload-specific.

The compiler searches for mappings minimizing C while satisfying correctness constraints.

---

# 20. Machine learning for compilation

Measured hardware data can train a predictor of:

```text
geometry + state + control
        ↓
transition probability
```

The predictor can accelerate compilation, but every model prediction should remain distinguishable from direct measurement.

The calibration database remains authoritative.

---

# 21. Digital twin training loop

```text
simulation
   ↓
experiment
   ↓
measurement
   ↓
model correction
   ↓
new simulation
```

This creates a continuously improving physical model.

---

# 22. Provenance-aware execution

Every result should be reconstructible from:

```text
program hash
compiler version
IR hash
mapping
calibration snapshot
hardware revision
raw readout hash
analysis version
```

This makes computational provenance a first-class system property.

---

# 23. Reproducibility levels

### R0
Same machine, same configuration.

### R1
Same machine, independently repeated.

### R2
Different array on same fabrication process.

### R3
Independent laboratory.

### R4
Independent physical implementation.

A TPAC claim becomes increasingly strong as it advances through these levels.

---

# 24. Benchmark harness

The benchmark system should automatically execute:

```text
baseline CPU
baseline GPU
baseline FPGA
baseline conventional photonic implementation
TPAC
```

using matched workload definitions and report:

- correctness;
- latency;
- energy;
- throughput;
- density;
- calibration cost;
- total system cost.

---

# 25. Benchmark anti-cheating rules

TPAC benchmarks must include all required overhead.

No benchmark may omit:

- data loading;
- initialization;
- calibration when required;
- cooling;
- readout;
- post-processing;
- host-device communication.

Otherwise comparisons become meaningless.

---

# 26. API architecture

A host API could expose:

```python
fabric = TPAC.connect()
job = fabric.compile(program)
result = fabric.run(job)
result.provenance()
result.uncertainty()
```

The API should never conceal whether a result came from measured hardware or simulation.

---

# 27. Simulation API

```python
model = TPAC.simulate(configuration)
trajectory = model.evolve(duration)
model.measure()
model.export_provenance()
```

Simulation and hardware should share as much of the programming interface as practical.

---

# 28. Hardware abstraction

The runtime should support multiple TPAC backends:

```text
TPAC-SIM
TPAC-LAB
TPAC-CRYO
TPAC-PHOTONIC
TPAC-PHASE
TPAC-HYBRID
```

Programs should remain portable when physical primitives are compatible.

---

# 29. Runtime observability

Expose live:

- state confidence;
- temperature;
- mode occupancy;
- routing condition;
- error rate;
- calibration age;
- energy consumption.

The operator should be able to see the physical machine rather than only its logical output.

---

# 30. Security model

Threat classes:

```text
software command injection
calibration poisoning
physical input injection
side-channel extraction
fault induction
model poisoning
```

Every control layer requires validation.

---

# 31. Safe-state architecture

A fault condition should drive the machine toward a known low-energy state.

```text
FAULT
 ↓
stop excitation
 ↓
isolate region
 ↓
read state
 ↓
thermal recovery
 ↓
recalibrate
```

---

# 32. TPAC operating system concept

A mature machine may require an OS-like layer managing:

- physical resources;
- cell allocation;
- calibration;
- thermal state;
- topology;
- jobs;
- provenance;
- recovery.

The OS is therefore partly a **physical resource manager**.

---

# 33. Physical virtualization

If the runtime can map logical fabrics onto different physical regions, multiple logical TPAC machines can coexist on one physical array.

```text
physical array
 ├── logical fabric A
 ├── logical fabric B
 └── logical fabric C
```

Isolation requirements must be experimentally demonstrated.

---

# 34. Multi-tenant constraint

Potential future cloud-style TPAC systems require isolation of:

- optical modes;
- acoustic modes;
- thermal budgets;
- state memory;
- readout channels.

Physical cross-talk becomes analogous to a software isolation failure.

---

# 35. Distributed TPAC

Multiple chips can be connected through conventional optical/electrical links.

```text
TPAC node A
     ↕
network
     ↕
TPAC node B
     ↕
TPAC node C
```

The distributed runtime can combine physical accelerators with classical infrastructure.

---

# 36. Hybrid classical/TPAC execution

Most realistic early systems will be heterogeneous:

```text
CPU/GPU
   ↕
TPAC accelerator
   ↕
external memory
```

The objective is not to eliminate conventional computers but to delegate suitable operations to the physical substrate.

---

# 37. Compiler profiling

Every workload execution should generate a profile:

```text
% time physical evolution
% time control
% time readout
% time calibration
% time data transfer
% energy by subsystem
```

This reveals where optimization actually matters.

---

# 38. Architecture search

The compiler can eventually search over:

- topology;
- cell operating points;
- coupling strengths;
- state encodings;
- sampling strategy;
- readout configuration.

This makes the TPAC computer partially self-optimizing.

---

# 39. Experiment-to-compiler loop

The long-term loop is:

```text
PHYSICAL EXPERIMENT
        ↓
NEW PRIMITIVE DISCOVERED
        ↓
PRIMITIVE DATABASE
        ↓
COMPILER SUPPORT
        ↓
WORKLOAD TEST
        ↓
PERFORMANCE DATA
        ↓
NEXT EXPERIMENT
```

The machine's instruction set evolves from evidence.

---

# 40. Core architectural insight

The TPAC computational stack should not ask:

> “How do we make this physical system imitate a transistor?”

It should ask:

> “Which computations does this physical system perform naturally, and how do we expose, compose, control, and verify them?”

That is the software architecture's central principle.
