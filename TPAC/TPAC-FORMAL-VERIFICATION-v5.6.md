# TPAC Formal Verification v5.6

## Objective

Connect TPAC requirements and semantics to mechanically checkable properties where feasible.

## Property classes

```text
SAFETY
INVARIANT
REACHABILITY
REFINEMENT
AUTHORIZATION
PROVENANCE
LIVENESS
```

## Safety properties

Forbidden physical states must be unreachable from authorized initial states under the modeled transition system.

## Invariant properties

Declared invariants must remain true after every valid transition.

## Authorization properties

A state-changing transition must have a valid authority context matching the resource capability.

## Provenance properties

Every derived artifact must have an upstream provenance path terminating in an acquisition, declared assumption, or externally supplied artifact.

## Refinement properties

An implementation must preserve the observable semantics required by its parent specification within declared tolerances.

## Liveness boundaries

Liveness requirements explicitly state the conditions under which progress is expected. Safety does not depend on assuming progress.

## Model checking

Finite-state components may be exhaustively checked. Larger systems use compositional or bounded verification where appropriate.

## Runtime verification

Properties that cannot be fully proven statically may be monitored during execution.

## Proof artifacts

Verification outputs record:

```text
property_id
model_version
checker_version
assumptions
result
counterexample
```

## Counterexamples

A failed property produces a reproducible counterexample where feasible rather than only a pass/fail label.

## Core invariant

**TPAC verification should produce evidence about why a property holds—or an inspectable counterexample showing where it fails.**
