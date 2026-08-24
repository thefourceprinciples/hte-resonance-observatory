# TPAC Evidence Graph v3.6

## Objective

Represent the complete chain from observation to claim without collapsing measurements, interpretations, models, or decisions into one undifferentiated record.

## Node classes

```text
OBSERVATION
CALIBRATION
TRANSFORM
ANALYSIS
MODEL
HYPOTHESIS
CLAIM
COUNTEREVIDENCE
DECISION
```

## Edge classes

```text
MEASURES
CALIBRATES
DERIVES
SUPPORTS
CONTRADICTS
DEPENDS_ON
REPLICATES
FALSIFIES
```

## Claim discipline

A claim must identify its direct observations, intermediate transformations, assumptions, uncertainty, and contradictory evidence.

## Provenance closure

A claim is `PROVENANCE_CLOSED` only when every required upstream artifact is addressable and immutable.

## Evidence independence

The graph distinguishes repeated measurements from independent replications. Ten runs on one unchanged device are not automatically ten independent confirmations.

## Counterevidence

Contradictory observations remain first-class graph nodes and cannot be deleted merely because a later interpretation changes.

## Inheritance

Derived artifacts inherit provenance references from their inputs.

## Versioning

Changing an analysis method creates a new analysis node rather than rewriting the previous result.

## Core invariant

**No conclusion becomes stronger merely because its documentation becomes longer.**
