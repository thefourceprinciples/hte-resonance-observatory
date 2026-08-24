# TPAC System Requirements v5.1

## Objective

Convert the architecture into testable system-level requirements.

## Requirement format

```text
REQ-ID
STATEMENT
RATIONALE
VERIFICATION_METHOD
DEPENDENCIES
STATUS
```

## Functional requirements

### TPAC-F-001
The system shall identify every physical resource participating in an execution.

Verification: execution-manifest inspection.

### TPAC-F-002
The system shall preserve raw measurements independently from derived transformations.

Verification: lineage test.

### TPAC-F-003
The system shall reject control operations outside declared device capabilities.

Verification: negative conformance test.

### TPAC-F-004
The system shall associate results with the hardware, calibration, software, and analysis revisions that produced them.

Verification: provenance reconstruction test.

### TPAC-F-005
The system shall distinguish simulation, hardware-in-loop, and physical execution results.

Verification: result-schema test.

## Non-functional requirements

### TPAC-N-001
Critical state-changing operations shall have explicit authorization boundaries.

### TPAC-N-002
Material system changes shall be versioned.

### TPAC-N-003
The verification system shall detect intentional corruption of provenance and calibration metadata.

### TPAC-N-004
The system shall expose uncertainty for quantitative physical measurements where applicable.

### TPAC-N-005
The architecture shall support independent implementation of the normative specification.

## Requirement traceability

Each requirement links to one or more:

```text
SPECIFICATION
IMPLEMENTATION
TEST
EVIDENCE
CLAIM
```

## Status model

```text
PROPOSED
IMPLEMENTED
VERIFIED
FAILED
DEPRECATED
```

## Core invariant

**Every important TPAC promise must eventually become a testable requirement with an explicit verification path.**
