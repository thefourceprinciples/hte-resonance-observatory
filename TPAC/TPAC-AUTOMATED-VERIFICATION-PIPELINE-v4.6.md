# TPAC Automated Verification Pipeline v4.6

## Objective

Continuously test TPAC artifacts as the architecture evolves.

## Pipeline

```text
CHANGE
→ SCHEMA CHECK
→ STATIC VALIDATION
→ CONFORMANCE TESTS
→ PROVENANCE CHECK
→ SIMULATION
→ FAULT INJECTION
→ REPRODUCIBILITY CHECK
→ REPORT
```

## Artifact classes

```text
SPEC
ISA
COMPILER
RESOURCE
CALIBRATION
EXPERIMENT
DATA
ANALYSIS
CLAIM
```

## Gates

A failed prerequisite blocks dependent stages rather than producing a misleading green result.

## Regression corpus

Maintain known-good and known-bad workloads, calibration states, resource states, and evidence graphs.

## Mutation testing

Deliberately corrupt selected manifests, provenance links, calibration records, timing constraints, and measurements to verify that validators detect the corruption.

## Differential execution

Compare reference and optimized implementations while preserving separate provenance.

## Artifact integrity

Every generated artifact receives a content identifier and parent references.

## Report

Each run emits:

```text
pipeline_id
commit
artifact_versions
tests_executed
failures
warnings
coverage
reproducibility_status
```

## Core invariant

**TPAC changes should continuously challenge the architecture rather than merely accumulate documentation.**
