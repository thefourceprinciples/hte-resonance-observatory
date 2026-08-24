# TPAC Open Specification v4.4

## Objective

Define a vendor-neutral specification boundary so TPAC concepts can be implemented, tested, criticized, and independently reproduced without requiring one proprietary implementation.

## Normative layers

```text
MODEL
ISA
RESOURCE
CONTROL
INTERCONNECT
MEASUREMENT
PROVENANCE
EVIDENCE
```

## Conformance classes

```text
SIMULATION
HIL
SINGLE_MODULE
MULTI_MODULE
FABRIC
```

An implementation declares its highest validated class.

## Capability declarations

Implementations publish machine-readable capability profiles rather than claiming universal compatibility.

## Required transparency

A conforming implementation must expose enough metadata to distinguish:

- simulated behavior;
- measured behavior;
- fitted behavior;
- assumed behavior;
- projected behavior.

## Interoperability

Implementations should exchange portable manifests for workloads, resources, calibration state, experiments, and results.

## Reference tests

The specification defines conformance tests for ISA semantics, provenance preservation, resource constraints, safety boundaries, and result reporting.

## Extension mechanism

Experimental extensions use namespaced identifiers and cannot silently redefine normative semantics.

## Versioning

Breaking semantic changes increment the major specification version. Additive capabilities use minor versions where compatibility is preserved.

## Independent implementation

A conforming implementation must not depend on access to another vendor's private source code, model weights, or proprietary runtime internals.

## Core invariant

**TPAC is a specification that can outlive any single implementation, organization, hardware platform, or contributor.**
