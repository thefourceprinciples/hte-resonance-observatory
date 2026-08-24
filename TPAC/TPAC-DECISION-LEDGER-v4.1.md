# TPAC Decision Ledger v4.1

## Objective

Record consequential engineering and scientific decisions together with their evidence, alternatives, uncertainty, and reversibility.

## Decision record

```text
decision_id
question
options
selected_option
rationale
evidence
assumptions
uncertainty
reversibility
owner
status
```

## Decision classes

```text
ARCHITECTURAL
HARDWARE
SOFTWARE
EXPERIMENTAL
SAFETY
ECONOMIC
RESEARCH
```

## Alternatives

Rejected alternatives remain recorded with the reason for rejection.

## Evidence boundary

Distinguish:

```text
MEASURED
INFERRED
ASSUMED
PROJECTED
```

## Reversal cost

Record the expected cost of reversing a decision. High-cost irreversible decisions require stronger evidence than low-cost reversible experiments.

## Sunset conditions

A decision may specify conditions that trigger reassessment.

## Contradiction trigger

Material counterevidence automatically marks dependent decisions for review.

## Dependency graph

Decisions may depend on claims, hardware capabilities, costs, or safety conditions. Those dependencies are explicit.

## Core invariant

**A decision should remain accountable to the evidence and assumptions that justified it, even after those assumptions change.**
