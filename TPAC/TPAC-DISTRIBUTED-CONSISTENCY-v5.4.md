# TPAC Distributed Consistency v5.4

## Objective

Define consistency boundaries for distributed TPAC controllers, sensors, schedulers, and evidence services.

## Consistency classes

```text
STRONG
BOUNDED
EVENTUAL
OFFLINE
```

Each subsystem declares the class required for its operations.

## Control-plane consistency

Safety-critical authorization and device state require bounded, explicitly defined consistency guarantees.

## Measurement ordering

Measurement events carry sequence information sufficient to detect gaps, duplication, and reordering.

## Configuration snapshots

A run references an immutable configuration snapshot rather than independently reading mutable configuration across nodes.

## Distributed clocks

Events requiring causal ordering use logical or sequence metadata in addition to wall-clock timestamps.

## Partition behavior

Network partition behavior is explicit. A node must not continue state-changing operations merely because communication failed unless its lease and safety policy permit continuation.

## Conflict resolution

Conflicting control or configuration states are preserved as conflicts until an authorized resolution occurs.

## Evidence merge

Distributed evidence streams are merged without erasing source identity or event ordering information.

## Recovery

After partition recovery, stale state is reconciled against authoritative snapshots before normal execution resumes.

## Core invariant

**Distributed TPAC components may be asynchronous, but ambiguity about shared physical state must never be silently converted into certainty.**
