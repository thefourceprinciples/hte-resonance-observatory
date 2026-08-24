# TPAC — Systems Expansion v0.3

**Status:** Public research architecture / falsifiable systems proposal  
**Date:** 2026-08-24  
**Predecessors:** TPAC Prototype Specification v0.1; TPAC Engineering Architecture v0.2

## Abstract

TPAC is expanded here from a physical cell into a complete computing-system research program. The central proposition is that computation can be distributed across coupled physical state variables—optical, acoustic/phononic, material phase, topology, and memory—so that the substrate itself performs transformation, storage, routing, and collective dynamics.

This document adds the systems-level value that a cell specification alone cannot provide: programming models, compilation, operating concepts, calibration, observability, fault models, architecture variants, workload mapping, benchmarking, manufacturing pathways, security considerations, economic metrics, and a staged roadmap.

TPAC remains an unproven research hypothesis. Every advantage described below is a target for measurement, not an established result.

---

# 1. Design thesis

Conventional computing separates:

- compute;
- memory;
- interconnect;
- clocking;
- routing;
- state management.

TPAC asks whether these can be partially co-located in one physical dynamical substrate.

The architectural abstraction is:

```text
                 ┌─────────────────────────────┐
                 │         TPAC FABRIC         │
                 │                             │
 INPUT ────────► │ state → interaction → state │ ───────► OUTPUT
                 │      ↕          ↕            │
                 │    memory    topology        │
                 │      ↕          ↕            │
                 │   feedback ← dynamics       │
                 └─────────────────────────────┘
```

The program is therefore not necessarily a sequence of transistor operations. A program may be a **desired trajectory through physical state space**.

---

# 2. The TPAC abstraction stack

TPAC should be specified at seven layers.

## L0 — physics

Actual optical, acoustic, material, thermal, electrical, and quantum phenomena.

## L1 — cell

A calibrated physical state-transition element.

## L2 — network

Cells plus controlled coupling and directional pathways.

## L3 — computational primitives

Measured transformations exposed as machine operations.

## L4 — compiler/runtime

Maps workloads into sequences, fields, pulses, configurations, and readout operations.

## L5 — system

Input/output, scheduling, calibration, fault management, and host integration.

## L6 — application

Signal processing, pattern recognition, associative memory, optimization, simulation, and potentially general computation.

This separation prevents the common mistake of treating a physical phenomenon as though it were already a complete computer.

---

# 3. TPAC machine model

A TPAC instruction need not be an ordinary opcode. A useful first abstraction is:

```text
OP = {region, input_state, control_vector, duration, target_state, readout}
```

Example:

```text
WRITE
region = C17
input_state = A
control_vector = optical pulse P
expected_state = B
readout = interferometric
```

A second operation could be:

```text
ROUTE
source = C17
condition = phase(B)
path = east
readout = downstream detector
```

A third could be:

```text
RELAX
region = network_3
allow = natural dynamics
observe = attractor
```

The runtime can therefore intentionally exploit both **forced transitions** and **natural relaxation**.

---

# 4. Physical state as addressable memory

TPAC should distinguish four kinds of state.

### Persistent state

State retained without continuous external drive.

### Volatile dynamical state

State that persists only while the physical system remains energized or phase-locked.

### Coupling state

State that changes the effective relationship between cells.

### Topological state

The currently accessible propagation graph.

This gives a richer memory model than a conventional bit array.

```text
memory = node state + edge state + field state + history
```

---

# 5. The TPAC “instruction set” should emerge experimentally

Rather than inventing gates first, build a **physical primitive catalog**.

Candidate primitive families:

| Primitive | Physical action | Computational analogue |
|---|---|---|
| TRANSFER | move excitation | copy / communication |
| ATTENUATE | reduce amplitude | weighting |
| AMPLIFY | increase response | gain |
| INTERFERE | combine modes | addition / correlation |
| MIX | nonlinear frequency interaction | multiplication / feature map |
| THRESHOLD | cross state boundary | activation |
| LATCH | enter metastable state | memory |
| RELEASE | leave metastable state | reset |
| ROUTE | state-dependent propagation | switch |
| RELAX | evolve toward attractor | inference |
| COUPLE | change interaction | connectivity |
| READ | measure state | observation |

The real instruction set is whatever transformations survive calibration and replication.

---

# 6. Programming model

Three programming paradigms should be developed in parallel.

## 6.1 Digital TPAC

Treat calibrated states as symbols.

```text
A + B → C
```

Useful where deterministic behavior is sufficiently strong.

## 6.2 Analog TPAC

Treat physical amplitudes/phases as numerical variables.

```text
x(t) → physical evolution → y(t)
```

Useful for differential equations, signal processing, control, and optimization.

## 6.3 Dynamical TPAC

Treat the network itself as the computational object.

```text
input → perturbation → relaxation → attractor
```

Useful for reservoir and associative computing.

The system should not force all workloads into one paradigm.

---

# 7. Compilation

A future TPAC compiler could transform a high-level operation into physical control sequences.

```text
Python / DSL / workload
          ↓
     TPAC compiler
          ↓
 primitive graph
          ↓
 cell placement
          ↓
 routing solution
          ↓
 pulse schedule
          ↓
 calibration correction
          ↓
 hardware execution
          ↓
 readout decoding
```

Compilation must account for physical constraints such as:

- mode collision;
- thermal budget;
- crosstalk;
- phase drift;
- routing conflicts;
- maximum pulse energy;
- state-dependent latency.

This is where TPAC becomes a computer architecture rather than merely a device.

---

# 8. TPAC intermediate representation

Define a machine-independent graph:

```text
NODE
  state requirements
  operation
  tolerance

EDGE
  coupling requirement
  direction
  latency
  bandwidth
```

The compiler then maps this graph to actual cells.

This permits different physical implementations to execute the same abstract workload.

That is strategically important: the architecture survives even if the first material platform fails.

---

# 9. Calibration as part of computation

Unlike ideal digital gates, physical TPAC cells will vary.

Therefore every cell should have a calibration record:

```text
cell_id
fabrication_batch
resonant_modes
coupling_matrix
state_centroids
transition_probabilities
thermal_response
noise_profile
routing_profile
readout_model
calibration_timestamp
```

The compiler can use this information to choose robust operating regions.

Calibration is not merely maintenance. It becomes part of the architecture.

---

# 10. Self-characterization

A mature TPAC array should be able to run a diagnostic sequence and reconstruct its own computational map.

```text
probe → perturb → measure → infer model → update calibration
```

Potentially:

```text
TPAC ARRAY
    ↓
self-test pulses
    ↓
response measurements
    ↓
state/coupling estimation
    ↓
updated machine model
```

This creates a path toward adaptive manufacturing compensation.

---

# 11. Fault tolerance

TPAC should assume imperfect cells from the beginning.

Fault classes:

- dead cell;
- stuck phase;
- weak coupling;
- excessive loss;
- unstable resonance;
- readout failure;
- thermal runaway;
- routing degradation;
- calibration drift.

Possible mitigation:

```text
logical node
     ↓
multiple physical candidates
     ↓
calibrated routing
     ↓
majority / redundancy / attractor recovery
```

The system may eventually exploit physical redundancy rather than exact device uniformity.

---

# 12. Error model

Define error at multiple levels.

### Physical error

Measured state differs from intended state.

### Transition error

A requested transition lands in the wrong state.

### Routing error

Energy reaches an unintended cell/path.

### Readout error

The state is correct but measured incorrectly.

### Computational error

The resulting workload output is incorrect.

The architecture must report these separately.

---

# 13. Clocking philosophy

TPAC should not assume a global clock is necessary.

Three modes should be investigated:

### Synchronous

All cells update according to a shared timing reference.

### Event-driven

Cells transition when local thresholds are crossed.

### Relaxation-driven

Computation occurs through natural system evolution.

The last two are particularly important because they could eliminate some conventional clocking overhead.

No benefit should be claimed until measured.

---

# 14. Energy architecture

Energy accounting must include:

```text
input energy
+ modulation energy
+ state-switching energy
+ routing loss
+ cooling energy
+ readout energy
+ control energy
+ calibration energy
= total system energy
```

A low-energy physical transition is not automatically a low-energy computer if the control and cooling infrastructure dominate.

For every benchmark, report both:

**device energy**

and

**system energy**.

---

# 15. Thermal architecture

The frozen-core implementation makes thermal engineering especially important.

The system must measure:

- local temperature;
- thermal gradients;
- transition-induced heating;
- optical absorption;
- acoustic dissipation;
- cooldown cost;
- thermal recovery time.

A key design fork is therefore:

```text
cryogenic TPAC
       vs.
room-temperature TPAC
```

The first may provide superior coupling; the second may provide vastly better deployability.

The architecture should pursue both tracks until evidence selects one.

---

# 16. Materials program

Material selection should be treated as a search problem.

Score candidate platforms on:

- optical loss;
- acoustic loss;
- nonlinear coefficient;
- phase stability;
- transition energy;
- switching speed;
- metastability;
- fabrication compatibility;
- environmental stability;
- integration compatibility.

No single material should be assumed optimal.

---

# 17. Geometry program

Geometry may be as important as material.

Candidate structures:

- ring resonators;
- coupled cavities;
- Bragg structures;
- photonic-crystal waveguides;
- acoustic resonators;
- phononic crystals;
- microfluidic Tesla geometries;
- asymmetric metamaterial channels;
- hybrid resonator networks.

The research program should search geometry/material combinations rather than optimizing them independently.

---

# 18. Phase-field computing

If a phase-changing material supports multiple stable domains, the computational object can become a field:

```text
P(x,y,t)
```

rather than a scalar bit.

Then computation becomes the controlled evolution of:

```text
P(x,y,t₀) → P(x,y,t₁)
```

Possible applications include pattern recognition, image processing, optimization, and physical simulation.

The key question is whether the field dynamics can be made sufficiently controllable and reproducible.

---

# 19. Topological memory

The architecture should investigate whether **connectivity itself** can encode state.

For example:

```text
state A:
A → B → C

state B:
A → D → C

state C:
A → E → F → C
```

If physical phase or routing conditions can select among these paths, the network's graph becomes memory.

This is potentially much more expressive than a simple on/off element, but also much harder to engineer.

---

# 20. Reservoir mode

The network can be intentionally operated in a high-dimensional dynamical regime.

The desired behavior is not perfect gate-level determinism. It is a reproducible nonlinear transformation that creates useful separability in state space.

Training then occurs primarily at the readout.

Benchmark:

```text
input sequence
      ↓
TPAC reservoir
      ↓
state trajectory
      ↓
linear/nonlinear readout
      ↓
classification
```

Measure accuracy, latency, energy, and robustness against conventional digital reservoir implementations.

---

# 21. Associative-memory mode

Store attractors rather than explicit addresses.

Training:

```text
pattern → repeated controlled evolution → attractor
```

Recall:

```text
partial/noisy pattern → TPAC dynamics → attractor
```

Measure:

- basin size;
- recall fidelity;
- corruption tolerance;
- capacity;
- convergence time;
- energy per recall.

---

# 22. Optimization mode

Map an objective function onto physical energy/state dynamics where possible.

Conceptually:

```text
candidate configurations
          ↓
TPAC physical evolution
          ↓
low-energy / stable states
          ↓
candidate solutions
```

The architecture must compare total energy and wall-clock time against classical optimization methods.

---

# 23. Differential-equation mode

A physical dynamical system naturally implements differential equations.

A calibrated TPAC network could therefore be used as an analog solver:

```text
parameters → physical coupling → trajectory
```

Candidate workloads:

- coupled oscillators;
- wave equations;
- nonlinear dynamics;
- control systems;
- diffusion/reaction models.

The advantage, if any, would come from letting physics perform the evolution directly.

---

# 24. Security architecture

Physical computing introduces new attack surfaces.

Potential attacks:

- optical injection;
- acoustic injection;
- thermal perturbation;
- calibration poisoning;
- side-channel readout;
- phase-state manipulation;
- fault induction.

Defenses should include:

- challenge-response calibration;
- redundant sensing;
- anomaly detection;
- isolated control channels;
- cryptographic host communication;
- physical tamper detection.

Security should be designed before commercialization.

---

# 25. Observability architecture

Every TPAC machine should expose a machine-readable state history.

```text
experiment
  ├── configuration
  ├── calibration
  ├── input
  ├── physical state trajectory
  ├── routing events
  ├── readout
  ├── uncertainty
  └── result
```

This creates an auditable computational record.

A result without provenance should not be considered a valid benchmark result.

---

# 26. Digital twin

Build a software representation of each physical array.

```text
physical TPAC
      ↕
calibrated digital twin
```

The twin should reproduce measured distributions rather than merely idealized equations.

Uses:

- compiler testing;
- fault prediction;
- workload scheduling;
- experiment planning;
- fabrication optimization;
- anomaly detection.

---

# 27. Manufacturing ladder

### M0 — benchtop single device

One interaction region.

### M1 — packaged single cell

Stable optical/acoustic interfaces.

### M2 — 2–4 cell demonstrator

Controlled coupling.

### M3 — 10–100 cell array

Integrated network.

### M4 — wafer-scale research array

Fabrication variation becomes a primary research variable.

### M5 — packaged accelerator

External system integration.

Each stage requires new reliability metrics.

---

# 28. Manufacturing philosophy

The system should be designed around **calibrated imperfection**, not the assumption of perfect fabrication.

If cell-to-cell variation can be measured and incorporated into compilation, manufacturing tolerance can become a software problem rather than a purely lithographic problem.

This could materially change the economics of the architecture if demonstrated.

---

# 29. Benchmark suite

TPAC should publish a benchmark suite with at least:

### Physical benchmarks

- coupling strength;
- Q factor;
- loss;
- transition energy;
- transition latency;
- retention;
- endurance.

### Network benchmarks

- routing efficiency;
- cross-talk;
- bandwidth;
- scaling behavior.

### Computational benchmarks

- classification accuracy;
- recall accuracy;
- optimization quality;
- numerical error;
- throughput;
- energy/op;
- latency/op.

### System benchmarks

- calibration time;
- cooling overhead;
- packaging overhead;
- total cost per useful operation.

---

# 30. Comparison matrix

TPAC must be compared fairly against:

- CMOS CPUs;
- GPUs;
- FPGAs;
- photonic accelerators;
- neuromorphic hardware;
- analog computers;
- reservoir computers;
- quantum processors.

The comparison must use workload-specific metrics. No universal superiority claim is appropriate.

---

# 31. Commercialization branches

If successful, TPAC could be commercialized in several forms.

### Branch A — research instrument

Sell programmable TPAC experimental platforms.

### Branch B — photonic accelerator

Target signal processing and inference.

### Branch C — neuromorphic accelerator

Target pattern recognition and temporal data.

### Branch D — optimization accelerator

Target specialized optimization workloads.

### Branch E — analog scientific computer

Target simulation and differential equations.

### Branch F — general-purpose architecture

Only pursue if evidence supports it.

The first commercial product should follow demonstrated advantage rather than attempting to replace every computer.

---

# 32. Economic model

Track:

```text
materials
+ fabrication
+ packaging
+ control electronics
+ cooling
+ optical sources
+ detectors
+ calibration
+ maintenance
+ energy
```

against:

```text
useful operations
+ throughput
+ lifetime
+ workload advantage
```

The relevant metric is **cost per useful computation**, not component price alone.

---

# 33. Open hardware strategy

The research architecture can be published openly while implementation-specific engineering remains modular.

Recommended separation:

```text
open scientific specification
        ↓
open simulation model
        ↓
open benchmark suite
        ↓
reference implementation
        ↓
optional specialized commercial hardware
```

This allows independent replication and prevents the conceptual architecture from depending on one manufacturer.

---

# 34. Reproducibility protocol

Every published result should include:

1. geometry revision;
2. material batch;
3. operating conditions;
4. optical/acoustic drive parameters;
5. calibration state;
6. raw data;
7. processing code;
8. uncertainty analysis;
9. failed trials;
10. exact hardware/software versions.

The archive should preserve negative results.

---

# 35. Experimental decision tree

```text
Strong coupling?
       │
   NO ─┴─► change material/geometry
       │
      YES
       ▼
Persistent states?
       │
   NO ─┴─► investigate phase/hysteresis
       │
      YES
       ▼
Controlled transitions?
       │
   NO ─┴─► redesign control/readout
       │
      YES
       ▼
Useful cell primitive?
       │
   NO ─┴─► classify as memory/physics result
       │
      YES
       ▼
Coupled network?
       │
   NO ─┴─► solve interconnect problem
       │
      YES
       ▼
Useful workload?
       │
   NO ─┴─► revise architecture
       │
      YES
       ▼
Benchmark advantage
```

---

# 36. What would constitute a breakthrough?

A genuine breakthrough would not be merely observing strong optical/acoustic coupling.

It would require a chain of evidence:

1. reproducible stateful cell;
2. controlled physical transitions;
3. useful nonlinear transformation;
4. scalable cell coupling;
5. reliable routing;
6. measurable computational workload;
7. competitive system-level energy/latency/density;
8. independent replication.

The more links demonstrated, the stronger the claim.

---

# 37. What would falsify the architecture?

The architecture should be considered unsuccessful if:

- state retention is too weak;
- transition control is unreliable;
- routing asymmetry provides no useful advantage;
- coupling collapses at scale;
- calibration dominates computation;
- cooling dominates energy;
- fabrication is impractical;
- classical electronics performs the same workload more efficiently;
- no useful workload benefits from the physical dynamics.

Failure is not to be hidden. It is part of the scientific output.

---

# 38. Research roadmap

## Phase 0 — literature and prior art

Build a traceable evidence map of every physical component.

## Phase 1 — simulation

Build coupled optical/acoustic/phase models.

## Phase 2 — single-cell experiment

Demonstrate stateful coupled dynamics.

## Phase 3 — routing

Test asymmetric transport.

## Phase 4 — coupled network

Demonstrate multi-cell dynamics.

## Phase 5 — computational primitive library

Measure and classify transformations.

## Phase 6 — workload demonstration

Run a useful application.

## Phase 7 — independent replication

Release the design and invite reproduction.

## Phase 8 — engineering optimization

Only now optimize density, energy, speed, and cost.

---

# 39. Ultimate research question

TPAC is ultimately testing a deeper proposition:

> **Can information processing be engineered as a controlled physical ecology rather than as a sequence of isolated logical gates?**

If the answer is yes, then memory, computation, communication, and adaptation may be properties of the same substrate.

That is the architectural opportunity.

---

# 40. Immediate next experiments

The next work package should produce five artifacts:

1. **TPAC cell CAD concept** — dimensions and candidate geometries.
2. **Coupled-physics simulation specification** — variables, equations, boundary conditions, and observables.
3. **Experimental bill of materials** — minimum viable laboratory setup.
4. **TPAC machine-readable schema** — cells, states, transitions, couplings, experiments, provenance.
5. **Benchmark harness** — scripts/specification for comparing TPAC against classical baselines.

These five artifacts turn the architecture into an executable research program.

---

# 41. Governance of the research record

TPAC should preserve three distinctions in perpetuity:

```text
OBSERVED
   ≠
INFERRED
   ≠
PROPOSED
```

Every major statement in the archive should carry one of those statuses.

A fourth status may be added:

```text
REPLICATED
```

A replicated result should never be silently promoted from a single observation to a universal claim.

---

# 42. Final architecture statement

TPAC is not presently a demonstrated computer, and this document does not claim that it is.

It is a **research architecture for converting coupled physical state into computation**.

Its distinctive proposition is the deliberate co-design of:

```text
PHOTONS
   ↕
PHONONS
   ↕
PHASE
   ↕
MEMORY
   ↕
TOPOLOGY
   ↕
DYNAMICS
```

into one computational fabric.

The project succeeds scientifically if that proposition is tested rigorously enough that the answer becomes difficult to dispute—whether the answer is ultimately **yes** or **no**.
