# TPAC — Physical Machine Specification v0.4

**Status:** Research engineering specification / falsifiable
**Date:** 2026-08-24
**Purpose:** Define a concrete physical implementation envelope for TPAC and the experiments required to determine whether the architecture can exist.

> No parameter in this document is asserted as an experimentally optimized value. Dimensions, materials, frequency ranges, and operating conditions are candidate design spaces. They must be selected by simulation and measurement.

---

## 1. System definition

The TPAC physical machine is defined as a tiled array of coupled cells. Each cell contains, at minimum:

1. an optical propagation structure;
2. an acoustic/phononic mode;
3. a nonlinear interaction region;
4. a state-bearing material or effective metastable degree of freedom;
5. a controllable input mechanism;
6. a non-destructive or minimally destructive readout;
7. a directional coupling structure;
8. thermal/environmental sensing.

The preferred first implementation is a **single-chip or packaged hybrid optomechanical demonstrator**, while the frozen liquid-core fibre remains an independent high-coupling experimental branch.

---

# 2. Reference cell

```text
                  OPTICAL IN
                      │
                      ▼
              ┌───────────────┐
              │ input coupler │
              └───────┬───────┘
                      │
                      ▼
        ╔════════════════════════════╗
        ║      TPAC INTERACTION      ║
        ║                            ║
        ║  optical mode              ║
        ║      ↕                     ║
        ║  acoustic mode             ║
        ║      ↕                     ║
        ║  phase/state medium        ║
        ║      ↕                     ║
        ║  local history             ║
        ╚═══════╤══════════╤════════╝
                │          │
          state readout    │ directional path
                │          │
                ▼          ▼
             detector   NEXT CELL
```

The cell is a **stateful nonlinear transducer** rather than a simple switch.

---

# 3. Candidate geometry families

## G1 — coupled ring

Two optical resonators coupled to a mechanical resonator.

```text
       _______       _______
     /         \---/         \
    |   OPT 1   | |   OPT 2   |
     \_________/   \_________/
           \       /
            \ MECH/
```

Use: high-Q resonance and controllable mode coupling.

## G2 — photonic-crystal cavity

A localized optical mode coupled to a localized mechanical mode.

Use: strong field confinement and small footprint.

## G3 — waveguide + mechanical resonator

A propagating optical mode interacts with an engineered acoustic mode.

Use: easier cell-to-cell networking.

## G4 — phase-change interaction region

Optical/acoustic field overlaps a material capable of reproducible state transitions.

Use: persistent or multistable memory.

## G5 — directional hybrid channel

A nonlinear asymmetric waveguide is placed between cells.

Use: state-dependent routing.

The final cell may combine G2/G4/G5.

---

# 4. Physical state variables

The minimum measured state vector is:

```text
X = [P, A_o, φ_o, A_a, φ_a, R, T, D]
```

where:

- `P`: phase/order state;
- `A_o`: optical amplitude;
- `φ_o`: optical phase;
- `A_a`: acoustic amplitude;
- `φ_a`: acoustic phase;
- `R`: resonance state;
- `T`: temperature;
- `D`: directional-routing condition.

Additional variables may be introduced only when measurement demonstrates that they materially affect state evolution.

---

# 5. Minimal dynamical model

The first model should be phenomenological and calibrated before increasing complexity.

A generic coupled-mode representation can be written as:

```text
da/dt = f(a, b, P, u, T)

db/dt = g(a, b, P, u, T)

dP/dt = h(P, |a|², |b|², T, u)
```

where:

- `a` is an optical complex amplitude;
- `b` is an acoustic complex amplitude;
- `P` is a material/order parameter;
- `u` is external control.

The exact equations must be selected from the physical platform and validated against measurements.

---

# 6. State-transition map

The central laboratory artifact is a measured transition map:

```text
                control u
                    │
                    ▼
             ┌─────────────┐
             │   STATE A   │
             └──────┬──────┘
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        STATE B   STATE C   STATE A
```

For every transition record:

- initial state;
- control vector;
- transition probability;
- transition latency;
- final state;
- energy;
- environmental conditions.

This transition graph becomes the basis for the TPAC instruction set.

---

# 7. Memory specification

A candidate memory state must satisfy:

```text
WRITE → HOLD → READ → HOLD → READ → RESET
```

with state fidelity remaining above a predefined experimental threshold.

Important distinction:

**metastability is not automatically useful memory.**

The state must be sufficiently reproducible, distinguishable, controllable, and robust for the intended workload.

---

# 8. Multilevel state protocol

Test whether the system naturally supports:

```text
S0
S1
S2
S3
...
Sn
```

rather than forcing binary operation.

For each state measure the separability of the readout distributions.

A state is operationally valid only when its probability distribution can be distinguished from neighboring states with the required error rate.

---

# 9. Phase-field implementation

For a spatially extended phase medium define:

```text
P = P(x,y,z,t)
```

The computational state can then be represented by domain topology and geometry.

Candidate information features:

- domain count;
- domain area;
- domain boundary length;
- domain orientation;
- phase fraction;
- connected components;
- domain motion;
- transition history.

This creates a potential high-dimensional state space without requiring a corresponding number of discrete transistors.

---

# 10. Directional router

The TPAC router is specified initially as a **directional transmission experiment**, not assumed to be a true nonreciprocal device.

Measure:

```text
T_forward(f, P, A)
T_reverse(f, P, A)
```

and define:

```text
R_dir = T_forward / T_reverse
```

Then independently test reciprocity using an appropriate measurement protocol.

The project must distinguish:

- nonlinearity;
- asymmetric geometry;
- bias-induced asymmetry;
- true nonreciprocity.

---

# 11. Wave-Tesla geometry search

Search asymmetric geometries computationally before fabrication.

Parameterize:

- channel width;
- branch angle;
- cavity volume;
- branch length;
- resonator placement;
- loss distribution;
- coupling coefficient.

Objective function:

```text
maximize useful forward/reverse contrast
subject to:
  acceptable insertion loss
  acceptable bandwidth
  acceptable fabrication tolerance
```

A geometry that only works at one infinitesimal parameter point is not a viable architecture.

---

# 12. Cell interconnect

Each cell should expose four logical ports:

```text
             NORTH
               │
        WEST ─ CELL ─ EAST
               │
             SOUTH
```

Physical implementation may use fewer or more ports.

Port availability can itself be state-dependent.

This permits reconfigurable computational graphs.

---

# 13. Network topology

Candidate topologies:

### Grid

Useful for spatial processing.

### Small-world

Potentially useful for associative dynamics.

### Random reservoir

Useful for reservoir computing.

### Hierarchical

Useful for modular computation.

### Adaptive graph

The most ambitious configuration, where physical state changes effective connectivity.

All topology claims must be benchmarked against equivalent fixed-topology networks.

---

# 14. Write mechanisms

Candidate write channels:

1. optical pulse;
2. modulated continuous optical drive;
3. acoustic excitation;
4. electrical bias;
5. thermal pulse;
6. combined optical-acoustic drive.

The preferred mechanism minimizes total system energy while maintaining state fidelity.

---

# 15. Read mechanisms

Candidate readout:

- transmitted optical power;
- reflected optical power;
- optical phase;
- resonance shift;
- Raman/Brillouin signatures where appropriate;
- acoustic response;
- electrical state;
- interferometric measurement.

Readout must be characterized for back-action.

---

# 16. Control pulse library

Every successful physical transition should be assigned a pulse family:

```text
PULSE_ID
carrier frequency
bandwidth
amplitude
phase
shape
duration
repetition rate
energy
expected transition
```

A machine controller can then invoke calibrated physical operations rather than raw experimental parameters.

---

# 17. Cell controller

```text
                  HOST
                   │
             command packet
                   ▼
           ┌──────────────┐
           │ TPAC CONTROL │
           └──────┬───────┘
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 optical DAC   acoustic DAC   bias
      │           │           │
      └───────────┼───────────┘
                  ▼
                CELL
                  │
              detectors
                  │
                  ▼
              ADC / DSP
```

The controller remains conventional during development.

The research question is how much of its work can eventually be replaced by the physical substrate itself.

---

# 18. Synchronization

Three synchronization modes:

```text
GLOBAL CLOCK
EVENT CLOCK
NO GLOBAL CLOCK
```

A no-global-clock mode is particularly valuable if local relaxation naturally determines computation timing.

Required measurements:

- jitter;
- phase drift;
- synchronization error;
- event latency;
- cascade stability.

---

# 19. Laboratory instrument stack

A reference laboratory should provide, as appropriate to the selected platform:

- tunable optical source;
- optical modulation;
- polarization control;
- optical power monitoring;
- interferometric phase measurement;
- spectrum analysis;
- high-speed photodetection;
- RF/acoustic drive and detection;
- high-bandwidth oscilloscope;
- temperature sensing;
- cryogenic control where required;
- precision electrical bias;
- automated data acquisition;
- vibration isolation;
- optical isolation and safety systems.

Exact equipment selection follows the selected physical implementation.

---

# 20. Experimental automation

Every experiment should be executable from a machine-readable configuration:

```yaml
experiment: TPAC-P1-001
cell: C001
initial_state: S0
optical:
  wavelength: calibrated
  amplitude: calibrated
acoustic:
  frequency: calibrated
control:
  pulse: P07
measurement:
  channels: [optical_power, phase, acoustic_response, temperature]
repetitions: N
```

The system should automatically:

1. configure the instrument;
2. execute the pulse sequence;
3. capture raw data;
4. attach metadata;
5. run preprocessing;
6. calculate uncertainty;
7. update the state-transition database.

---

# 21. Evidence database

Each measured transition becomes an immutable record:

```text
transition_id
cell_id
experiment_id
initial_state
control
final_state
probability
latency
energy
noise
conditions
raw_data_hash
analysis_version
operator
timestamp
```

This creates a machine-readable **physical provenance graph**.

---

# 22. Digital twin implementation

The twin should expose:

```text
Cell.state()
Cell.transition(control)
Cell.measure()
Cell.calibrate()
Cell.route(direction)
Network.evolve(duration)
Network.readout()
```

The API is conceptual until the physical state model is experimentally calibrated.

---

# 23. Compiler mapping

High-level operation:

```text
classify(signal)
```

could compile to:

```text
normalize input
→ inject optical waveform
→ propagate through reservoir
→ sample physical state
→ decode readout
```

A digital operation:

```text
store(x)
```

could compile to:

```text
select cell
→ apply write pulse
→ verify state
→ mark calibrated state
```

A dynamical operation:

```text
solve(system)
```

could compile to:

```text
initialize network
→ apply parameter field
→ release dynamics
→ wait/converge
→ read attractor
```

---

# 24. Runtime scheduler

A scheduler must understand that TPAC operations have physical durations and conflicts.

```text
JOB
 ├─ required cells
 ├─ required modes
 ├─ required energy
 ├─ duration
 ├─ state constraints
 └─ readout requirements
```

The scheduler must avoid simultaneous operations that cause destructive mode interference, thermal overload, or unacceptable crosstalk.

---

# 25. Fault-aware compilation

Compilation should avoid unreliable cells.

```text
logical node
     ↓
eligible physical cells
     ↓
reliability score
     ↓
energy score
     ↓
routing cost
     ↓
selected mapping
```

A TPAC compiler can therefore trade device imperfections against topology and workload requirements.

---

# 26. Self-calibrating array

A mature system should periodically perform:

```text
probe → measure → compare model → recalibrate → verify
```

Calibration drift becomes another physical state variable that the runtime monitors.

---

# 27. Fault recovery

If a cell fails:

```text
FAILED CELL
     │
     ▼
identify alternate cell
     │
     ▼
re-route graph
     │
     ▼
recalibrate
     │
     ▼
resume computation
```

The goal is graceful degradation rather than total system failure.

---

# 28. Workload classes

TPAC should be optimized initially for workloads matching its natural physics.

### Temporal signals

Time-dependent information naturally interacts with acoustic memory.

### Spectral processing

Resonant structures naturally implement frequency-selective transformations.

### Pattern recognition

Nonlinear collective dynamics may create useful feature spaces.

### Associative recall

Attractor dynamics may provide natural pattern completion.

### Physical simulation

The substrate can directly emulate dynamical systems.

### Optimization

State-space relaxation may encode candidate solutions.

General-purpose computing remains a later question.

---

# 29. Performance model

Define total useful throughput as:

```text
throughput = useful_results / total_system_time
```

and system energy efficiency as:

```text
energy_efficiency = useful_results / total_system_energy
```

where total system energy includes cooling, optical sources, control electronics, detectors, and calibration.

---

# 30. Density model

Define physical density:

```text
cells / mm²
```

but also computational density:

```text
useful_operations / mm² / second
```

A physically dense array that cannot be reliably controlled is not computationally dense.

---

# 31. Latency model

Report separately:

- physical propagation latency;
- state-switch latency;
- readout latency;
- control latency;
- calibration latency;
- end-to-end workload latency.

This prevents a fast physical phenomenon from being advertised as a fast computer when its surrounding electronics dominate.

---

# 32. Reliability model

Report:

```text
P(correct transition)
P(correct readout)
P(correct route)
P(correct workload output)
```

These are different probabilities and must not be conflated.

---

# 33. Scaling law program

Measure how each metric changes with cell count `N`:

```text
coupling(N)
loss(N)
error(N)
energy(N)
latency(N)
calibration_cost(N)
```

The architecture only becomes compelling if scaling remains favorable over a meaningful range.

---

# 34. Thermal scaling

For cryogenic architectures, measure:

```text
cooling_load(N)
transition_heat(N)
recovery_time(N)
```

A small cell may have excellent device physics while the array remains impractical because cooling scales poorly.

---

# 35. Fabrication tolerance

Generate intentional geometry/material variation and measure performance distributions.

The objective is not merely the best cell.

It is:

> **acceptable performance across a manufacturing distribution.**

---

# 36. Security boundary

TPAC control packets should be authenticated at the host interface.

The physical layer should additionally monitor for unexpected:

- optical power;
- acoustic excitation;
- temperature;
- resonance shifts;
- state transitions.

Unexpected physical transitions become security events as well as hardware faults.

---

# 37. IP boundary

Maintain a clean distinction among:

- published scientific observations;
- public architectural concepts;
- implementation-specific engineering;
- experimental data;
- independently developed improvements.

No novelty or patentability conclusion should be inferred from publication alone.

---

# 38. First reference implementation

The first reference implementation should target the smallest architecture capable of demonstrating:

```text
OPTICAL INPUT
      ↓
COUPLED OPTICAL/ACOUSTIC STATE
      ↓
PERSISTENT OR METASTABLE STATE
      ↓
STATE-DEPENDENT OUTPUT
```

The directional router can initially be external to the cell if integration would obscure the fundamental experiment. It should then be integrated in a subsequent revision.

---

# 39. Reference experiment sequence

```text
E0  baseline optical characterization
E1  baseline acoustic characterization
E2  optical → acoustic coupling
E3  acoustic → optical coupling
E4  nonlinear response
E5  hysteresis / metastability
E6  state write
E7  state retention
E8  state read
E9  state reset
E10 directional transmission
E11 state-dependent transmission
E12 two-cell coupling
E13 network dynamics
E14 computational workload
```

Every experiment should have a predefined success/failure criterion before data collection.

---

# 40. Reference data products

Each stage produces:

- raw time series;
- spectra;
- state-transition maps;
- calibration tables;
- uncertainty estimates;
- processed datasets;
- reproducible analysis scripts;
- experiment configuration;
- hardware revision identifiers.

The research record should preserve all of them.

---

# 41. Architecture branches

TPAC should remain a family of architectures:

```text
                   TPAC
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   OPTOACOUSTIC   PHASE-FIELD   HYBRID
       │            │            │
       ▼            ▼            ▼
   reservoir     attractor     general
   computing     computing     experimental
```

This prevents failure of one physical implementation from invalidating the broader computational abstraction.

---

# 42. Quantum branch

If future experiments demonstrate genuine quantum coherence and quantum computational resources, the same architecture can be extended with quantum state variables.

Until then:

**TPAC is not classified as a quantum computer.**

The architecture may nevertheless serve as a hybrid interface around quantum components if that becomes experimentally useful.

---

# 43. Scientific decision gates

### Gate A

Strong, reproducible coupled dynamics.

### Gate B

Persistent controllable state.

### Gate C

Useful nonlinear transformation.

### Gate D

Useful directional routing.

### Gate E

Stable multi-cell network.

### Gate F

Computational workload.

### Gate G

System-level advantage.

No stage should be skipped merely because a later stage appears commercially attractive.

---

# 44. Minimum success condition

The smallest scientifically meaningful TPAC success is:

> A physical cell whose measured state can be intentionally written, retained, read, and used to alter a subsequent optical/acoustic transformation.

Everything beyond this is scale and architecture.

---

# 45. Maximum research objective

The maximum objective is a programmable physical network in which:

```text
state
  +
interaction
  +
routing
  +
phase
  +
feedback
  ↓
computation
```

and where the resulting machine demonstrates a reproducible advantage for at least one meaningful workload over the best appropriate conventional baseline.

---

# 46. Design principle

**Do not build a smaller conventional computer out of exotic physics.**

Build a machine whose architecture takes advantage of what the physics naturally does well.

That means allowing:

- continuous state;
- multistability;
- collective dynamics;
- asynchronous evolution;
- resonance;
- phase transitions;
- physical routing;
- parallel propagation;
- attractor behavior.

The architecture should exploit these properties rather than suppress them in the pursuit of transistor-like behavior.

---

# 47. Final specification

TPAC v0.4 defines the target physical machine as:

```text
┌───────────────────────────────────────────────┐
│                 TPAC FABRIC                   │
│                                               │
│  PHOTON ──↔── PHONON ──↔── PHASE             │
│     │           │           │                │
│     └───────────┼───────────┘                │
│                 │                             │
│              MEMORY                           │
│                 │                             │
│              TOPOLOGY                         │
│                 │                             │
│              FEEDBACK                          │
│                 │                             │
│             DYNAMICS                           │
│                 │                             │
│            COMPUTATION                        │
│                                               │
└───────────────────────────────────────────────┘
```

The architecture is intentionally broad enough to survive material substitution and strict enough to be experimentally falsifiable.

The objective is not to predict the outcome.

The objective is to make the outcome measurable.
