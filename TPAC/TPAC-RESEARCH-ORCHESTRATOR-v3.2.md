# TPAC Research Orchestrator v3.2

## Objective

Turn the TPAC evidence architecture into an explicit experimental decision system.

## 1. Research state

Each hypothesis is assigned:

```text
HYPOTHESIS
DESIGNING
READY
RUNNING
ANALYZING
SUPPORTED
CONTESTED
FALSIFIED
REPLICATING
RETIRED
```

## 2. Hypothesis record

```text
hypothesis_id
statement
mechanism
predictions
required_measurements
controls
falsification_conditions
prior_evidence
status
```

## 3. Experiment selection

Prioritize experiments by a versioned utility function:

```text
information_gain
× feasibility
× safety
× reproducibility
```

The weighting is explicit and can be challenged.

## 4. Control generation

Every experiment automatically identifies:

- positive controls;
- negative controls;
- sham controls;
- environmental controls;
- instrumentation controls.

## 5. Evidence accumulation

Evidence is accumulated by claim, not by document volume.

A thousand observations of the same uncontrolled effect do not automatically outweigh one decisive confounder.

## 6. Contradiction handling

Contradictory results create a first-class branch in the research graph.

```text
CLAIM
 ↙    ↘
SUPPORT  CONTRADICTION
```

Both remain linked to their source measurements.

## 7. Experiment dependencies

A later experiment may depend on an earlier calibration or result. Dependency edges are recorded explicitly.

## 8. Stopping rules

An experiment may stop when:

- evidence reaches a predefined threshold;
- falsification occurs;
- uncertainty becomes irreducible under current instrumentation;
- safety limits are reached;
- expected information gain falls below threshold.

## 9. Replication planning

When a claim reaches `SUPPORTED`, the orchestrator can generate a replication plan that changes operator, device, environment, or analysis path where appropriate.

## 10. Publication package

A claim package includes:

```text
hypothesis
protocol
controls
raw-data references
analysis
uncertainty
counterevidence
replication status
```

## 11. Anti-confirmation rule

The orchestrator must surface experiments capable of disproving the current leading interpretation.

## 12. Core invariant

**The research system is optimized for learning what is true, not for maximizing the number of results that support a preferred hypothesis.**
