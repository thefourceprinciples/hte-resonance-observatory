# TPAC — Prototype Specification v0.1

**Status:** Public research draft / falsifiable engineering hypothesis  
**Date:** 2026-08-24  
**Author:** Gage Fry / thefourceprinciples research archive  
**Scope:** Hybrid photonic–acoustic–phase-state computational cell and scalable architecture

> This document is a research proposal, not a claim that a working TPAC computer has already been constructed. The first objective is experimental falsification.

## 1. Executive summary

TPAC proposes a computational architecture in which information is represented and transformed by coupled physical states rather than by conventional transistor switching alone. The initial cell combines:

1. a guided optical channel;
2. a mechanically/acoustically active medium;
3. a nonlinear interaction region;
4. controllable phase/state transitions;
5. directional transport or isolation inspired by Tesla-valve geometries;
6. optical, acoustic, or electrical readout;
7. feedback/control capable of driving the cell between metastable states.

The central hypothesis is that strongly coupled optical and acoustic modes, combined with controllable material phases, can provide useful memory, nonlinear transformation, routing, and computation in one physical element.

The architecture is deliberately agnostic about whether the eventual implementation is classical, analog, neuromorphic, photonic, quantum, or hybrid. A quantum-computing designation must be earned experimentally by demonstrating an actual quantum computational resource and model; it is not assumed here.

## 2. Physical motivation

Recent work provides two relevant physical demonstrations.

### 2.1 Frozen liquid-core optical fibre

Researchers at the Max Planck Institute for the Science of Light, Leibniz University Hannover, and the Leibniz Institute of Photonic Technology reported a liquid-core optical fibre whose core is frozen at cryogenic temperature. The frozen section continues to guide light and hypersonic sound, while the optical/acoustic coupling becomes more than 1,000 times stronger than in standard optical fibre. The team demonstrated optoacoustic memory and identified potential applications in photonic neuromorphic computing and quantum signal processing.

TPAC treats this as a candidate physical substrate, not as evidence that TPAC itself exists.

### 2.2 Coexisting electronic phases

MIT researchers reported time-resolved observation of two charge-density-wave phases in erbium tritelluride. One phase recovered gradually, while the other reassembled from localized pockets that expanded through the material. The work demonstrates that a material can host coexisting electronic phases with different transition dynamics and that external excitation can selectively disturb and observe those phases.

TPAC treats controllable phase coexistence and phase-transition dynamics as a possible computational state space.

## 3. Tesla-valve principle

A Tesla valve is a passive fluidic geometry that produces asymmetric flow resistance without moving mechanical parts. TPAC does not assume that a literal fluidic Tesla valve should be placed inside the optical cell.

Instead, the Tesla-valve concept is used as an architectural analogy and candidate routing mechanism:

- permit low-loss propagation in one effective direction;
- strongly suppress or reshape reverse propagation;
- create path-dependent state evolution;
- produce nonlinear routing without a conventional moving gate.

Possible physical realizations include fluidic, acoustic, phononic, photonic, metamaterial, or engineered waveguide geometries.

## 4. TPAC cell

A minimal cell is represented as:

```text
                OPTICAL INPUT
                     │
                     ▼
             ┌───────────────┐
             │ Optical guide │
             └───────┬───────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │  NONLINEAR INTERACTION  │
        │                         │
        │  optical ↔ acoustic     │
        │  phase/state medium     │
        │                         │
        └───────┬─────────┬───────┘
                │         │
          acoustic       state
             mode       transition
                │         │
                ▼         ▼
          ┌──────────────────┐
          │ metastable state │
          └────────┬─────────┘
                   │
              directional
                routing
                   │
                   ▼
                OUTPUT
```

### Candidate state variables

A cell may encode information in one or more of:

- optical phase;
- optical amplitude;
- acoustic amplitude;
- acoustic phase;
- resonance frequency;
- material phase;
- local strain;
- charge-density-wave order parameter;
- polarization;
- coupled combinations of the above.

The first prototype should use the smallest experimentally accessible state space rather than attempting to optimize every variable simultaneously.

## 5. Memory hypothesis

The cell should be tested for at least two reproducible metastable states:

`A → perturbation → A`

and

`A → controlled transition → B`

followed by:

`B → perturbation → B`

A useful memory element requires measurable state separation, retention, repeatability, and a controllable write/read process.

Important measurements:

- retention time;
- state fidelity;
- switching energy;
- switching time;
- readout signal-to-noise ratio;
- write/read disturbance;
- cycle endurance;
- temperature dependence;
- sensitivity to fabrication variation.

## 6. Computation hypothesis

TPAC does not begin by imposing Boolean gates on the medium. Instead, experimentally observed state transformations are catalogued first.

Candidate transformations include:

- thresholding;
- amplification/suppression;
- phase rotation;
- frequency conversion;
- interference;
- nonlinear mixing;
- bistable switching;
- hysteretic state selection;
- directional routing;
- attractor formation;
- associative state evolution.

Boolean operations can then be synthesized if the physical transformation set is computationally universal or sufficiently expressive for the target workload.

## 7. Coupled-cell architecture

A second-stage system connects cells:

```text
     ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐
IN → │ C1  │ ↔── │ C2  │ ↔── │ C3  │ ↔── │ C4  │ → OUT
     └──┬──┘     └──┬──┘     └──┬──┘     └──┬──┘
        │           │           │           │
        └───────────┴───────────┴───────────┘
                    control / feedback
```

The key experiment is whether useful computation emerges from controlled collective dynamics rather than merely from independent cells acting as ordinary gates.

## 8. Proposed prototype sequence

### P0 — single-cell physics

Demonstrate optical/acoustic coupling and measure the available nonlinear response.

**Pass criteria:** reproducible coupling, measurable state dependence, and a controllable perturbation/readout pathway.

### P1 — bistable or multistable cell

Demonstrate two or more distinguishable physical states.

**Pass criteria:** repeatable state transitions and measurable retention.

### P2 — directional cell

Introduce a passive or active asymmetric routing structure inspired by Tesla-valve behavior.

**Pass criteria:** statistically significant forward/reverse propagation asymmetry under controlled conditions.

### P3 — coupled cells

Connect 2–4 cells and measure state-to-state influence.

**Pass criteria:** controllable inter-cell coupling exceeding uncontrolled cross-talk.

### P4 — logic synthesis

Determine whether observed physical transformations can implement a useful computational basis.

### P5 — memory array

Scale to 10–100 cells and measure density, error rate, energy, latency, and thermal stability.

### P6 — architectural demonstration

Implement a small real workload such as pattern classification, signal processing, associative recall, or optical/acoustic reservoir computation.

## 9. Instrumentation

A first laboratory demonstrator would require, depending on implementation:

- tunable optical source;
- modulation and detection hardware;
- cryogenic or controlled-temperature environment if a frozen-core implementation is used;
- acoustic/phononic excitation and detection;
- spectrum analyzer or equivalent optical/electrical spectral measurement;
- high-speed oscilloscope;
- interferometric phase measurement where required;
- temperature and pressure monitoring;
- precision control electronics;
- data acquisition and automated parameter sweeps.

## 10. Falsification criteria

TPAC should be considered unsuccessful in its proposed form if experiments show that:

1. coupling cannot be controlled reproducibly;
2. state transitions cannot be distinguished from noise;
3. metastable states cannot retain information for a useful interval;
4. directional behavior disappears under realistic operating conditions;
5. scaling produces no useful computational advantage;
6. energy, cooling, fabrication, or readout overhead overwhelms the proposed benefit;
7. all observed behavior is adequately reproduced by conventional photonic/electronic components without requiring the TPAC architecture.

A negative result is a valid research outcome.

## 11. Quantum-computing boundary

TPAC is **not designated a quantum computer at v0.1**.

A future implementation could become quantum if it demonstrates, for example, a well-defined quantum state space, coherent control, entanglement or another computationally relevant quantum resource, and an algorithmic or computational advantage attributable to those resources.

If those conditions are not met, TPAC should instead be classified according to its demonstrated physics: photonic, optoacoustic, neuromorphic, analog, nonlinear, or hybrid computing.

## 12. Engineering objective

The immediate objective is not to build a room-sized computer.

It is to answer one question experimentally:

> **Can a single engineered physical cell use coupled optical, acoustic, and phase-state dynamics to store and transform information in a controllable way that is materially useful for computation?**

If yes, the architecture becomes an engineering problem.

If no, the hypothesis is falsified and the failure modes become part of the research record.

## 13. Provenance and attribution

This specification is a public research draft derived from the Gage Fry / thefourceprinciples research archive and subsequent development discussions.

The publication of this document is intended to establish a public timestamp and enable independent scrutiny. It does not assert that every component described here is novel, patentable, or free of prior art. Prior-art analysis must be performed independently before any legal claim of novelty is made.

## 14. Open research questions

1. What material maximizes usable optoacoustic nonlinearity while remaining manufacturable?
2. Can phase-state switching be driven optically rather than thermally?
3. Can the Tesla-valve concept be implemented as a phononic or photonic asymmetric waveguide?
4. Can memory and computation occupy the same physical degree of freedom?
5. Can multiple phases coexist and serve as a multilevel state space?
6. Can a network of cells perform useful computation without conventional transistor logic at every node?
7. What is the minimum energy per state transition?
8. What is the maximum useful cell density?
9. What is the dominant noise/decoherence mechanism?
10. Does any experimentally demonstrated configuration provide an advantage over existing photonic, neuromorphic, analog, or quantum architectures?

## 15. Current scientific status

**Established inputs:** published demonstrations of extremely strong optoacoustic coupling in frozen liquid-core fibres and time-resolved observation of coexisting electronic phases.

**Proposed synthesis:** using those physical phenomena, together with asymmetric routing concepts inspired by Tesla-valve geometry, as components of a computational cell.

**Unproven claim:** that the resulting integrated architecture can function as a practically useful computer.

That distinction is deliberate.
