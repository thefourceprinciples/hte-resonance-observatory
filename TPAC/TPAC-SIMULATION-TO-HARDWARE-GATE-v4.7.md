# TPAC Simulation-to-Hardware Gate v4.7

## Objective

Prevent simulation results from being promoted to physical claims without explicit validation gates.

## Promotion ladder

```text
MODEL
→ SIMULATION
→ HARDWARE-IN-LOOP
→ SINGLE-MODULE
→ MULTI-MODULE
→ FABRIC
```

## Required comparison

At each promotion level compare:

```text
predicted behavior
measured behavior
uncertainty
model discrepancy
failure modes
resource costs
```

## Predefined predictions

Predictions are frozen before the corresponding validation run whenever practical.

## Promotion criteria

A level advances only when predefined acceptance criteria are satisfied or a documented exception is approved.

## Discrepancy registry

Unexpected differences become explicit discrepancy records rather than informal tuning notes.

## Extrapolation boundary

Results outside validated operating regimes are labeled extrapolations.

## Hardware divergence

When hardware disagrees with simulation, the system preserves both records and opens a model-review path.

## Core invariant

**Simulation accelerates discovery; it does not inherit the evidentiary authority of physical measurement.**
