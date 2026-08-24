# TPAC Reproducibility Package v3.8

## Objective

Define a portable package capable of reconstructing the computational and evidentiary conditions of a TPAC result.

## Required contents

```text
source
compiler version
ISA artifact
resource description
hardware passport
calibration records
control manifest
raw measurements
analysis code
analysis parameters
environment manifest
result manifest
```

## Environment capture

Record relevant:

- operating system;
- runtime dependencies;
- firmware;
- compiler;
- numerical libraries;
- configuration;
- clock/synchronization state.

## Deterministic replay

If execution is deterministic, replay must reproduce the declared artifact or explain environmental divergence.

## Stochastic replay

For stochastic execution, preserve seeds where meaningful and report expected distributions rather than requiring byte-identical output.

## Hardware replay

A replay package identifies whether it targets:

```text
same device
same hardware class
independent device
simulation
```

## Integrity

Package contents receive content-addressed identifiers and a manifest hash.

## Minimal reproduction

A smaller package may be generated containing only dependencies necessary to reproduce a specific claim.

## Independent reproduction

An independent reproduction should be able to identify which assumptions differ from the original execution.

## Publication

A result is publication-ready only when its reproducibility status is explicitly declared.

## Core invariant

**A result is not reproducible merely because its source code is available; the physical, computational, calibration, and data conditions must be recoverable as well.**
