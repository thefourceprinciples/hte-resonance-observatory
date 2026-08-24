# TPAC Fault-Tolerance Architecture v3.0

## Objective

Extend TPAC from single-device recovery to fabric-level fault tolerance without concealing degraded physical behavior.

## 1. Fault domains

```text
cell → cluster → module → rack → fabric
```

Each domain has independent health, isolation, recovery, and provenance state.

## 2. Redundancy modes

- spatial redundancy;
- temporal repetition;
- replicated modules;
- alternate routing;
- checkpoint/restart.

The selected mode is recorded in the execution manifest.

## 3. Degraded execution

A workload may continue under reduced capability only if its declared correctness and uncertainty requirements remain satisfied.

## 4. Voting

For replicated computations, voting policies must distinguish:

```text
majority agreement
weighted agreement
uncertain disagreement
```

Disagreement is retained as evidence rather than discarded.

## 5. Quarantine

A suspect physical resource is removed from scheduling while preserving its historical data for diagnosis.

## 6. Failover

Failover sequence:

```text
fault detection
→ state assessment
→ resource quarantine
→ alternate placement
→ recalibration check
→ execution
→ provenance merge
```

## 7. State migration

Migration is permitted only for state representations with experimentally validated transfer semantics.

## 8. Recovery correctness

Recovery must be benchmarked against the same workload without injected faults.

## 9. Availability metrics

Track:

```text
MTBF
MTTR
successful recovery rate
silent-error rate
unavailable capacity
fault propagation radius
```

## 10. Silent-error prevention

A computation that completes but violates its error budget is not a successful recovery.

## 11. Fault injection

Test controlled:

- cell failure;
- sensor failure;
- controller failure;
- interconnect failure;
- calibration corruption;
- thermal excursion;
- timing loss.

## 12. Core invariant

**Fault tolerance preserves explicit uncertainty and provenance; it does not manufacture correctness from disagreement.**
