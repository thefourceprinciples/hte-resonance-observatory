# TPAC Research Review Gate v6.0

## Objective

Create a formal boundary between internally generated evidence and claims released for external reliance.

## Review states

```text
INTERNAL
READY_FOR_REVIEW
UNDER_REVIEW
CONTESTED
APPROVED
REJECTED
SUPERSEDED
```

## Review packet

A review packet contains:

```text
claim
scope
experiment_manifest
data_snapshot
analysis
uncertainty
counterevidence
provenance_graph
reproduction_status
limitations
```

## Independence

Where practical, critical claims receive review by a process or person not responsible for generating the original analysis.

## Challenge requirement

Reviewers must be able to record objections, alternative interpretations, and requested tests without modifying the underlying evidence.

## Release criteria

Approval requires explicit disposition of material objections. Silence is not approval.

## Post-release correction

New contradictory evidence creates a versioned correction or supersession event; historical claims are not silently rewritten.

## Scope discipline

Approval applies only to the stated claim and validation regime. It does not automatically authorize broader interpretation.

## Core invariant

**Review is a challenge mechanism over evidence and reasoning, not a ceremonial confirmation of conclusions already reached.**
