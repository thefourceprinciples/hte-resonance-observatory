# TPAC Anomaly and Root-Cause Protocol v6.3

## Objective

Separate detection of abnormal behavior from attribution of its cause.

## Anomaly record

```text
anomaly_id
execution_id
signal
baseline
threshold
observed_interval
severity
related_resources
```

## Investigation stages

```text
DETECT
→ CHARACTERIZE
→ CORRELATE
→ HYPOTHESIZE
→ TEST
→ ATTRIBUTE
→ VERIFY
```

## Attribution rule

Correlation does not establish causation. A causal explanation requires a discriminating test, established mechanism, or other declared evidentiary basis.

## Competing hypotheses

Multiple plausible explanations remain active until evidence eliminates or ranks them.

## Root-cause confidence

Report confidence separately from anomaly severity.

## Evidence preservation

Raw signals and execution state remain immutable while investigation proceeds.

## Regression conversion

Confirmed failure mechanisms become permanent regression tests where practical.

## Unknown cause

An anomaly may remain unresolved. `UNKNOWN` is a valid outcome and must not be replaced by speculative attribution.

## Core invariant

**TPAC must be able to say “something happened” without pretending it already knows why.**
