# TPAC Thermal and Energy Model v2.0

## Objective

Treat energy and heat as first-class computational resources rather than after-the-fact performance annotations.

## 1. Energy ledger

Every execution records:

```text
host_energy
control_energy
excitation_energy
readout_energy
cooling_energy
calibration_energy
idle_energy
```

## 2. Accounting boundary

Every published energy result explicitly identifies its boundary:

```text
DEVICE
MODULE
SYSTEM
FACILITY
```

## 3. Thermal state

Represent each physical region with:

```text
temperature
thermal_capacity
thermal_resistance
heat_generation
recovery_rate
confidence
```

## 4. Thermal debt

Define thermal debt as accumulated deviation from the preferred operating state.

A scheduler can use thermal debt to predict future availability.

## 5. Energy-aware scheduling

The scheduler may trade latency against energy:

```text
minimize α·latency + β·energy
```

The selected weights are recorded with the schedule.

## 6. Cooling overhead

Cooling infrastructure must be included whenever the claim concerns system-level energy efficiency.

If cooling cannot be measured directly, it must be modeled with disclosed assumptions and uncertainty.

## 7. Energy per useful result

The primary application metric should often be:

```text
E_useful = total energy / accepted correct outputs
```

rather than energy consumed by the active device alone.

## 8. Thermal throttling

When temperature approaches an operating boundary:

```text
reduce duty cycle
→ reduce excitation
→ migrate workload
→ pause
```

The action is recorded as part of execution history.

## 9. Thermal characterization

Measure:

- step response;
- steady-state temperature;
- cooldown curve;
- spatial gradients;
- hysteresis;
- thermal cross-coupling.

## 10. Energy calibration

Instrumentation used for energy measurement receives its own calibration record and uncertainty budget.

## 11. Idle baseline

Measure idle consumption separately so workload energy can be distinguished from infrastructure baseline.

## 12. Energy reproducibility

Report distributions across repeated executions rather than a single favorable measurement.

## 13. Optimization guardrail

Energy optimization may not violate correctness, uncertainty, or physical safety requirements.

## 14. Core invariant

**A TPAC energy advantage exists only after the complete relevant energy boundary has been accounted for.**
