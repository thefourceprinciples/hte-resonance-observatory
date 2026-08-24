# TPAC Formal Semantics v5.5

## Objective

Define a compact semantic foundation for TPAC artifacts so implementations can be compared without relying on prose alone.

## State model

A system state is:

```text
S = (R, C, E, M, P)
```

where:

- `R` = physical resources;
- `C` = control/configuration state;
- `E` = execution state;
- `M` = measurement state;
- `P` = provenance state.

## Transition

A transition is:

```text
T : (S, command) → (S', evidence)
```

A valid transition must satisfy declared resource, safety, authorization, and provenance preconditions.

## Observation

An observation maps physical state into a measurement with uncertainty:

```text
O : S → (measurement, uncertainty, provenance)
```

## Claim

A claim is a proposition over observations and declared assumptions. It is not equivalent to an observation.

## Invariants

Implementations declare invariants that must hold across valid transitions.

Examples:

```text
resource capability
safety envelope
provenance continuity
state authorization
measurement integrity
```

## Refinement

A lower-level implementation refines a higher-level specification only when its observable behavior satisfies the higher-level contract within declared tolerance and scope.

## Nondeterminism

Where multiple valid physical outcomes exist, the specification describes an allowed outcome set rather than falsely requiring one exact state.

## Failure semantics

Failures are explicit transitions, not undefined behavior.

## Core invariant

**TPAC semantics distinguish state, transition, observation, evidence, and claim so that an implementation cannot satisfy a specification merely by changing terminology.**
