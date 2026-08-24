# TPAC Verification Matrix v1.4

## Purpose

Convert the TPAC architecture into an auditable sequence of engineering gates. Every major claim must map to an observable measurement, a control, and a falsification condition.

| Gate | Claim | Required evidence | Control | Exit criterion |
|---|---|---|---|---|
| V0 | Cell is physically reproducible | repeated characterization | blank/reference device | bounded parameter distribution |
| V1 | Cell has controllable state | write/read cycles | sham excitation | statistically separable states |
| V2 | State persists | retention curve | reset/reference | predefined retention target |
| V3 | State changes transformation | identical input, different states | randomized state labels | output separation survives controls |
| V4 | Coupled cells interact | pairwise response | isolated cells | coupling estimate with uncertainty |
| V5 | Network computes | workload accuracy | digital/reference baseline | predefined benchmark threshold |
| V6 | Physical advantage exists | full-stack metrics | strongest practical baseline | advantage after all overhead |
| V7 | Advantage replicates | independent runs/devices | blinded/randomized trials | reproducible effect |
| V8 | Manufacturing is viable | lot-level yield | process-control dataset | defined yield/reliability target |

## Evidence classes

### E0 — observation

A measurable phenomenon exists.

### E1 — mechanism

The phenomenon is linked to the proposed physical mechanism through controls.

### E2 — computation

The mechanism performs a defined computational transformation.

### E3 — advantage

The transformation provides a measurable system-level advantage.

### E4 — replication

The result survives independent reproduction.

Claims must not skip evidence classes.

## Blind evaluation

Where feasible, classify outputs using blinded labels so analysis cannot depend on the expected physical state.

## Randomization

Randomize:

- trial order;
- state labels;
- device selection;
- input ordering.

This reduces systematic experimental bias.

## Holdout devices

Reserve devices that are not used during model selection or calibration-rule development. Evaluate final methods on the holdout population.

## Benchmark lock

Before a performance comparison, freeze:

- workload;
- metrics;
- baseline;
- success threshold;
- energy accounting boundary;
- latency boundary.

## Reproducibility package

A release candidate should contain:

```text
hardware revision
fabrication metadata
calibration profile
raw data
analysis code
compiler version
runtime version
benchmark definition
environment specification
result manifest
```

## Claim ledger

Each public claim receives:

```text
claim_id
statement
evidence_class
supporting_runs
supporting_data
uncertainty
known_counterevidence
status
```

Statuses:

```text
HYPOTHESIS
SUPPORTED
REPLICATED
CONTESTED
FALSIFIED
SUPERSEDED
```

## Stop conditions

A development branch stops advancing when a required gate fails repeatedly without a plausible mechanism for remediation. This prevents architecture expansion from substituting for evidence.

## Core principle

**Complexity is not evidence.** A larger architecture, more sophisticated compiler, or more elaborate physical model does not increase the truth of an underlying claim. Evidence must remain attached to the claim at every layer.
