# TPAC Reference Implementation

This directory turns the TPAC specifications into a minimal executable conformance target.

## Current scope

- typed resource states;
- capability-based scheduling;
- deterministic resource selection;
- calibration validity;
- append-only provenance events;
- reconstructable lineage;
- canonical serialization;
- conformance tests.

## Run

From this directory:

```text
python -m unittest -v
```

No third-party dependencies are required.

## Design rule

The reference implementation is intentionally smaller than the full TPAC specification. It implements only invariants that can be tested directly and leaves hardware adapters, transport, persistence, and policy engines to later modules.

## Conformance principle

A TPAC implementation should not claim conformance because it resembles the specification. It must demonstrate the required invariants through executable tests.

## Next implementation layers

1. immutable event store;
2. schema validation;
3. resource reservation/expiry;
4. calibration dependency propagation;
5. failure-injection harness;
6. benchmark runner;
7. reproducible experiment manifests;
8. machine-readable claim/review records;
9. hardware adapter interface;
10. reference simulator.
