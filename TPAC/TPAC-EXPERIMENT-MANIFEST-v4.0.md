# TPAC Experiment Manifest v4.0

## Objective

Freeze the experimental conditions required to interpret a TPAC run before execution begins.

## Manifest sections

```text
IDENTITY
HYPOTHESIS
WORKLOAD
HARDWARE
ENVIRONMENT
CALIBRATION
CONTROLS
PROTOCOL
MEASUREMENTS
ANALYSIS_PLAN
STOPPING_RULES
SAFETY_LIMITS
```

## Pre-registration

The hypothesis, primary metric, controls, analysis method, and stopping rules should be frozen before outcome inspection whenever practical.

## Hardware lock

Record device passport revision, firmware, controller configuration, and resource description revision.

## Environment lock

Record environmental variables capable of affecting the result.

## Analysis lock

Predeclare primary and secondary analyses. Exploratory analyses remain explicitly labeled exploratory.

## Control matrix

Each experiment links every control to the confounder it is intended to detect.

## Measurement budget

Declare expected sample count, measurement resolution, saturation limits, and missing-data handling.

## Deviation record

Any deviation from the manifest produces a deviation event rather than silently modifying the original protocol.

## Blind execution

Where practical, analysis can be blinded to condition labels to reduce interpretation bias.

## Release states

```text
DRAFT
FROZEN
RUNNING
DEVIATED
COMPLETE
ANALYZING
ARCHIVED
```

## Core invariant

**The conditions under which evidence is generated must be frozen and inspectable before the result is used to support a claim.**
