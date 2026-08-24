# TPAC — Engineering Architecture v0.2

**Status:** Public research / engineering hypothesis  
**Date:** 2026-08-24  
**Purpose:** Expand the TPAC concept into a concrete, falsifiable laboratory architecture.

> **Important:** v0.2 is a proposed architecture, not a demonstrated device. Values marked *target* are engineering targets, not experimentally established specifications. The project must distinguish measured results from hypotheses at every stage.

---

## 1. Core proposition

TPAC proposes a computational substrate in which **optical, acoustic/phononic, material-phase, and directional transport states are coupled inside a reusable physical cell**.

The intended consequence is a cell in which:

- information can be stored as physical state;
- the stored state can alter subsequent computation;
- computation can occur through nonlinear physical evolution;
- routing can depend on physical state and geometry;
- memory, computation, and interconnect need not be separate layers.

The architecture is deliberately technology-neutral at the highest level. A practical implementation may ultimately be photonic, optoacoustic, phononic, electronic-phase, fluidic, quantum, or hybrid.

---

## 2. Architecture at a glance

```text
                         TPAC ARRAY
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
     OPTICAL                CONTROL              READOUT
      INPUT                  PLANE                 PLANE
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
              ┌──────────────────────────┐
              │      TPAC CELL FIELD     │
              │                          │
              │  ○──○──○──○──○──○        │
              │  │╲ │ ╱│╲ │ ╱│           │
              │  ○──○──○──○──○──○        │
              │  ╱│  ╲│  ╱│  ╲           │
              │  ○──○──○──○──○──○        │
              │                          │
              │ memory + dynamics +      │
              │ routing + computation    │
              └────────────┬─────────────┘
                           │
                           ▼
                         OUTPUT
```

The fundamental object is not a gate. It is a **stateful dynamical cell**.

---

## 3. TPAC cell architecture

```text
                      LASER / OPTICAL DRIVE
                              │
                              ▼
                     ┌────────────────┐
                     │ optical coupler│
                     └───────┬────────┘
                             │
                             ▼
               ┌───────────────────────────┐
               │      INTERACTION REGION   │
               │                           │
               │  optical mode ↔ acoustic │
               │            ↕              │
               │       phase medium        │
               │            ↕              │
               │       local state         │
               └───────────┬───────────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        directional                state readout
          router                       │
              │                         │
              └────────────┬────────────┘
                           ▼
                     NEXT CELL / I/O
```

### Functional blocks

1. **Optical coupler** — injects and extracts controlled optical modes.
2. **Interaction region** — maximizes optoacoustic/nonlinear coupling.
3. **Phase-state medium** — provides bistable or multistable physical states where feasible.
4. **Directional router** — provides state-dependent or geometry-dependent propagation asymmetry.
5. **Readout** — observes state without destroying it where possible.
6. **Control plane** — provides write/erase/reset operations and experiment synchronization.
7. **Interconnect** — couples cells into larger networks.

---

## 4. Candidate physical implementations

TPAC should be developed as a platform rather than locked prematurely to one material.

### Track A — frozen liquid-core fibre

Use a liquid-core optical fibre operated in a cryogenic regime where the core is frozen and optical/acoustic coupling becomes unusually strong.

**Primary question:** Can the strong optoacoustic interaction support reproducible stateful computation beyond the demonstrated memory behavior?

### Track B — solid-state optomechanical cavity

Use an integrated optical resonator coupled to a mechanical mode and a nonlinear or phase-changing material.

Advantages:

- potentially easier integration;
- easier array fabrication;
- no moving macroscopic parts;
- compatible with chip-scale photonics.

### Track C — phase-transition material

Use a material with controllable metastable/coexisting phases.

**Primary question:** Can phase configuration become a useful computational state rather than merely an observed physical phenomenon?

### Track D — phononic/photonic Tesla geometry

Construct a directional waveguide whose transmission depends on geometry, nonlinearity, or state.

**Primary question:** Can passive or weakly active asymmetry replace some conventional routing logic?

### Track E — hybrid cell

Combine A/B + C + D.

This is the full TPAC target architecture.

---

## 5. State vector

Represent the physical state of cell *i* as:

```text
Sᵢ = {Aopt, φopt, Aac, φac, P, T, R, D, H}
```

where, for example:

- `Aopt` = optical amplitude;
- `φopt` = optical phase;
- `Aac` = acoustic amplitude;
- `φac` = acoustic phase;
- `P` = material phase/order parameter;
- `T` = local temperature;
- `R` = resonance characteristics;
- `D` = directional-routing state;
- `H` = relevant history/internal variables.

This is a conceptual state representation. The experimentally useful subset must be determined empirically.

---

## 6. The central feedback loop

TPAC depends on a closed physical feedback chain:

```text
      optical input
           │
           ▼
     optical state
           │
           ▼
    acoustic response
           │
           ▼
     phase response
           │
           ▼
 altered propagation
           │
           ▼
 altered optical state
           │
           └───────────────►
```

This creates **history-dependent computation**.

The goal is not merely to amplify a signal. It is to make the physical system's current state determine what happens next.

---

## 7. Memory architecture

### 7.1 Binary mode

Two robust states:

```text
A ↔ B
```

### 7.2 Multistate mode

```text
A ↔ B ↔ C ↔ D ...
```

### 7.3 Spatial phase memory

```text
┌─────────────────────┐
│ A A A B B C C C     │
│ A A B B B C C C     │
│ A B B B C C C C     │
└─────────────────────┘
```

Information can potentially reside in domain configuration rather than a single scalar state.

### Required measurements

- retention;
- state separation;
- switching energy;
- switching latency;
- endurance;
- read disturbance;
- thermal drift;
- fabrication variation;
- error probability.

---

## 8. Computation architecture

TPAC should first identify the **natural computational primitives** of the physical system.

Candidate primitives:

- threshold;
- amplification;
- attenuation;
- interference;
- phase rotation;
- nonlinear mixing;
- frequency conversion;
- bistable switching;
- hysteresis;
- attractor selection;
- state-dependent routing.

Only afterward should conventional Boolean gates be synthesized.

### Boolean compatibility

If the physical primitives can reliably implement NAND or another universal basis, TPAC can emulate conventional digital logic.

If they cannot, TPAC may still be useful as an analog, reservoir, neuromorphic, or dynamical computer.

---

## 9. Directional-routing layer

The Tesla-valve principle is abstracted as:

> **Create strongly unequal propagation behavior in opposite directions through geometry, nonlinearity, or state.**

A conceptual wave router:

```text
FORWARD
──────────────────────────────►
          ╲       ╱
           ╲_____╱
              ╲
               ╲________

◄──────────────────────────────
REVERSE
```

The physical implementation must be tested rather than assumed to provide true nonreciprocity. Reciprocal systems can display asymmetric transmission under nonlinear or biased conditions without violating reciprocity, so measurements must distinguish genuine nonreciprocity from amplitude-dependent transmission asymmetry.

---

## 10. Cell-to-cell coupling

A scalable array requires controlled coupling:

```text
      C1 ───── C2 ───── C3
      │ ╲      │ ╲      │
      │  ╲     │  ╲     │
      C4 ───── C5 ───── C6
       ╲       │       ╱
        ╲      │      ╱
             C7
```

Coupling can be:

- optical;
- acoustic/phononic;
- electrical;
- thermal;
- phase-mediated;
- hybrid.

The system should characterize coupling matrices experimentally before attempting large-scale computation.

---

## 11. TPAC as a reservoir computer

A particularly plausible early workload is reservoir computing.

```text
INPUT
  │
  ▼
┌──────────────────────────┐
│      TPAC RESERVOIR      │
│                          │
│ ○─○─○──○─○─○──○          │
│ │╲│╱╲│╱╲│╱╲│╱            │
│ ○─○─○──○─○─○──○          │
│  ╲│╱╲│╱╲│╱╲│             │
│ ○─○─○──○─○─○──○          │
└───────────┬──────────────┘
            ▼
        TRAINED READOUT
            │
            ▼
          OUTPUT
```

The physical network supplies rich nonlinear dynamics; only the readout may need conventional training.

This is attractive because it does not require every microscopic transformation to be engineered into a clean digital gate.

---

## 12. TPAC as associative memory

A second early target is attractor computation.

```text
partial input
     │
     ▼
TPAC dynamics
     │
     ▼
stable attractor
     │
     ▼
reconstructed state
```

The relevant question is whether the physical network naturally forms robust attractors and whether those attractors can be programmed.

---

## 13. TPAC as an adaptive topology

The most ambitious extension is **state-dependent connectivity**.

Instead of:

```text
A ─ B ─ C
```

always remaining the same, physical state could determine whether a pathway is effectively open or suppressed:

```text
STATE 1:    A ─── B ─── C

STATE 2:    A     B ─── C
                 
STATE 3:    A ─── B     C
```

If demonstrated, this would allow the computational topology itself to become a memory-bearing variable.

That is one of the most important experiments in the project.

---

## 14. Control system

TPAC still needs a classical control layer during development.

```text
                    HOST COMPUTER
                          │
                    experiment API
                          │
                ┌─────────┴─────────┐
                │ CONTROL ELECTRONICS│
                └─────────┬─────────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
         optical       acoustic      thermal
          drive         drive        control
             │            │            │
             └────────────┼────────────┘
                          ▼
                     TPAC CELL
                          │
                    measurement
                          │
                          ▼
                    DATA ACQUISITION
```

The classical computer is **not the TPAC computer**. It is the laboratory instrument used to control and characterize the physical system.

---

## 15. P0 — single-cell experiment

### Objective

Demonstrate a reproducible coupled optical/acoustic state transition.

### Experimental sequence

1. establish baseline optical resonance;
2. establish acoustic resonance;
3. sweep optical excitation;
4. measure acoustic response;
5. sweep acoustic drive;
6. measure optical response;
7. map nonlinear response;
8. identify hysteresis or metastability;
9. test repeatability;
10. determine whether state transitions are controllable.

### Deliverable

A state-transition map:

```text
input → physical state → output
```

with uncertainty bounds.

---

## 16. P1 — memory cell

Demonstrate at least two stable states.

### Write

`A → B`

### Hold

`B → B`

### Read

`B → measured(B)`

### Reset

`B → A`

### Required result

The four operations must work repeatedly without requiring uncontrolled environmental changes.

---

## 17. P2 — directional cell

Introduce the Tesla-inspired geometry.

Measure:

- forward transmission;
- reverse transmission;
- insertion loss;
- frequency dependence;
- amplitude dependence;
- state dependence;
- temperature dependence.

Define:

`D = 10 log10(P_forward / P_reverse)`

as an experimental directional asymmetry metric, while separately testing whether the effect represents true nonreciprocity.

---

## 18. P3 — coupled cells

Build a 2-cell system, then 4-cell system.

Measure:

- coupling strength;
- cross-talk;
- propagation latency;
- state synchronization;
- error accumulation;
- dependence on topology.

Do not scale until the 2-cell behavior is understood.

---

## 19. P4 — computational primitives

Create a library of measured transformations.

```text
primitive_001
primitive_002
primitive_003
...
```

For each primitive record:

- input state;
- output state;
- control parameters;
- probability/error;
- latency;
- energy;
- environmental conditions;
- repeat count.

Then search for compositions capable of useful computation.

---

## 20. P5 — 10–100-cell array

Only after P4 should the architecture scale.

Measure:

- computational density;
- energy per operation;
- bandwidth;
- latency;
- thermal load;
- state fidelity;
- routing efficiency;
- fault tolerance;
- fabrication variance.

At this stage TPAC should be compared against conventional photonic and neuromorphic baselines.

---

## 21. P6 — first useful workload

Candidate demonstrations, in order of experimental accessibility:

1. signal filtering;
2. waveform classification;
3. pattern recognition;
4. associative recall;
5. reservoir classification;
6. nonlinear differential-equation approximation;
7. optimization/constraint search;
8. physical simulation.

The first useful workload should be selected based on measured strengths rather than marketing appeal.

---

## 22. Quantum branch

TPAC remains quantum-agnostic.

A quantum TPAC implementation would require evidence for a quantum computational resource such as:

- coherent quantum state preparation;
- controlled quantum evolution;
- entanglement or another relevant quantum resource;
- quantum measurement/readout;
- computational behavior attributable to the quantum resource.

Until demonstrated, TPAC should be described as a hybrid physical computing architecture rather than a quantum computer.

---

## 23. Simulation program

Before fabrication, create a multi-physics simulation stack:

### Level 1 — optical

Finite-element/FDTD or equivalent electromagnetic simulation of waveguide and resonator modes.

### Level 2 — acoustic

Mechanical eigenmode and driven-response simulation.

### Level 3 — coupled optoacoustic

Model interaction strength, detuning, nonlinear response, and mode conversion.

### Level 4 — phase dynamics

Model an order parameter using an appropriate phase-field or phenomenological model.

### Level 5 — network

Represent cells as stateful nodes with experimentally calibrated transition functions.

### Level 6 — computation

Test whether measured/simulated dynamics support useful workloads.

The simulation must preserve parameter provenance so that every model assumption can be traced to measurement or literature.

---

## 24. Experimental data model

Every experiment should record:

```text
experiment_id
cell_id
fabrication_batch
material
geometry_version
wavelength
acoustic_frequency
temperature
pressure
input_parameters
initial_state
output_state
raw_measurement
processed_measurement
uncertainty
operator
software_version
instrumentation
operator_notes
timestamp
provenance
```

This is essential. TPAC should produce an **evidence graph**, not merely a collection of attractive plots.

---

## 25. Minimum viable laboratory demonstrator

The first device does **not** need to be a computer.

It needs to demonstrate four things:

### A. Strong coupled dynamics

Optical excitation measurably affects an acoustic mode and/or vice versa.

### B. Statefulness

The response depends reproducibly on prior excitation history.

### C. Retention

At least two distinguishable states persist for a useful interval.

### D. Controlled transition

An external input can intentionally move the cell between states.

If all four are demonstrated, the project has crossed from conceptual architecture into an experimentally grounded computing platform.

---

## 26. Performance scorecard

TPAC should be evaluated against conventional alternatives using:

| Metric | Target direction |
|---|---|
| State density | higher |
| Switching energy | lower |
| Switching latency | lower |
| Retention | higher |
| Error rate | lower |
| Optical/acoustic loss | lower |
| Routing asymmetry | higher |
| Parallelism | higher |
| Thermal load | lower |
| Fabrication complexity | lower |
| Training cost | lower |
| Useful workload performance | higher |

No advantage should be claimed until benchmarked.

---

## 27. Failure modes

Potential failure modes include:

- insufficient coupling;
- thermal instability;
- phase-transition fatigue;
- uncontrolled hysteresis;
- acoustic damping;
- optical absorption;
- fabrication variation;
- state collapse;
- readout disturbance;
- cross-talk;
- scaling instability;
- routing asymmetry disappearing outside narrow conditions;
- energy overhead exceeding conventional computation;
- classical physics reproducing all useful behavior more cheaply;
- quantum claims failing experimental validation.

Every failure mode becomes a test condition.

---

## 28. The strongest possible TPAC claim

The project should **not** aim to prove that TPAC is revolutionary.

The strongest scientifically defensible claim would be:

> A reproducible physical cell can encode persistent state while simultaneously mediating nonlinear optical/acoustic transformation and state-dependent directional propagation; networks of such cells can perform useful computation with measured advantages on specified workloads.

Everything beyond that requires evidence.

---

## 29. Long-term architecture

If P0–P6 succeed, a mature TPAC system could look like:

```text
                           TPAC COMPUTER

     INPUT ─────────────────────────────────── OUTPUT
       │                                           ▲
       ▼                                           │
┌──────────────────────────────────────────────────────┐
│                    TPAC FABRIC                       │
│                                                      │
│   ○══○══○══○══○══○══○══○══○                        │
│   ║╲ ║╱ ║╲ ║╱ ║╲ ║╱ ║╲ ║                           │
│   ○══○══○══○══○══○══○══○══○                        │
│    ╲║╱ ╲║╱ ╲║╱ ╲║╱ ╲║╱                              │
│   ○══○══○══○══○══○══○══○══○                        │
│                                                      │
│  physical state = memory                            │
│  nonlinear dynamics = computation                    │
│  topology = routing                                  │
│  phase landscape = information                       │
│                                                      │
└──────────────────────────────────────────────────────┘
```

That is the architecture we should attempt to earn experimentally.

---

## 30. Research doctrine

TPAC development follows five rules:

1. **No demonstrated physics is presented as hypothetical.**
2. **No hypothesis is presented as demonstrated.**
3. **Every experimental result receives provenance.**
4. **Every major claim has a falsification condition.**
5. **A negative result is preserved as valuable evidence.**

The purpose of the architecture is therefore not to create a compelling story.

It is to create a machine that can answer the question.

> **Can engineered physical state itself become the computer?**

If the answer is yes, TPAC is the beginning of an architecture.

If the answer is no, the experiments tell us why.
