# TPAC Data Lineage v3.7

## Objective

Make every transformed datum traceable from raw acquisition through published result.

## Pipeline

```text
RAW
→ CLEANED
→ SYNCHRONIZED
→ CALIBRATED
→ FEATURED
→ ANALYZED
→ AGGREGATED
→ REPORTED
```

## Immutable raw layer

Raw measurements are never overwritten by cleaning or normalization.

## Transformation manifest

Every transformation records:

```text
input IDs
output IDs
algorithm version
parameters
software version
operator/runtime
timestamp
```

## Missingness

Missing, censored, saturated, corrupted, and unavailable values use distinct states.

## No silent repair

Interpolation, imputation, filtering, denoising, or outlier removal must be explicit and reproducible.

## Branching analyses

Alternative preprocessing pipelines may coexist and remain linked to the same raw observations.

## Aggregation

Aggregates retain references to contributing observations and the rule used to generate the aggregate.

## Dataset snapshots

Published datasets receive immutable snapshot identifiers.

## Lineage queries

The system should answer both:

```text
What raw evidence supports this result?
What results depend on this raw measurement?
```

## Core invariant

**Data transformation changes interpretation; it must never erase the history of what was originally measured.**
