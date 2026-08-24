# TPAC Claim Registry v3.9

## Objective

Create a machine-readable boundary between what TPAC has demonstrated, what remains hypothetical, and what is merely proposed.

## Claim states

```text
PROPOSED
TESTABLE
MEASURED
REPLICATED
SUPPORTED
CONTESTED
FALSIFIED
RETIRED
```

## Claim record

```text
claim_id
statement
scope
status
observations
controls
analysis
uncertainty
counterevidence
replications
model_dependencies
```

## Evidence threshold

A claim cannot advance state merely because additional documents repeat the same interpretation. Advancement requires new qualifying evidence.

## Scope locking

A claim records the operating regime in which it was evaluated:

```text
hardware
problem_size
environment
calibration
software
measurement_method
```

Evidence does not automatically generalize beyond that scope.

## Counterclaim support

Competing explanations receive their own records and may reference the same observations.

## Claim inheritance

Derived claims inherit explicit dependency edges. The registry must distinguish direct evidence from inherited evidence.

## Uncertainty

Every quantitative claim carries an uncertainty representation appropriate to the measurement.

## Audit

Claim status changes require an event containing:

```text
previous_status
new_status
triggering_evidence
actor_or_process
timestamp
```

## Core invariant

**TPAC records what the evidence establishes, not what the architecture hopes to establish.**
