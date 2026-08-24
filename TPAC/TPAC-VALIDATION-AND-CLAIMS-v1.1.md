# TPAC — Validation & Claims Protocol v1.1

**Status:** Evidence-control layer
**Date:** 2026-08-24

## 1. Purpose

Prevent TPAC from becoming a collection of exciting claims that cannot be independently distinguished from artifact, instrumentation error, model error, or ordinary known physics.

Every major claim receives an evidence record.

---

## 2. Claim classes

### C0 — Conceptual
A proposed mechanism with no experimental support.

### C1 — Simulated
Supported by a computational model.

### C2 — Observed
A reproducible physical signal has been measured.

### C3 — Mechanistically supported
Controls distinguish the proposed mechanism from plausible alternatives.

### C4 — Independently replicated
An independent implementation reproduces the result.

### C5 — Comparative advantage
The demonstrated mechanism provides a measured advantage over appropriate baselines.

No C0–C2 result should be marketed as C5.

---

## 3. Evidence packet

Every claim contains:

```text
claim_id
exact_claim
hypothesis
prior_art
experiment_ids
controls
raw_data_hashes
analysis_version
uncertainty
alternative_explanations
current_confidence
replication_status
```

---

## 4. Competing explanations

For every surprising result, explicitly enumerate alternatives.

Example:

```text
Observed directional response
├── intended nonreciprocal mechanism
├── detector mismatch
├── source mismatch
├── thermal gradient
├── ordinary interference
└── measurement artifact
```

The experiment must progressively eliminate alternatives.

---

## 5. Blind validation

Where feasible, analysis should be performed blind to experimental condition labels.

This reduces unconscious selection of favorable results.

---

## 6. Holdout experiments

Do not tune the model and evaluate it on the same observations used to tune it.

Partition data into:

```text
training/calibration
validation
held-out test
```

For physical systems, calibration runs must remain distinguishable from performance runs.

---

## 7. Pre-registration internally

Before high-value experiments, record:

- predicted result;
- success threshold;
- failure threshold;
- primary metric;
- controls;
- statistical method.

The record is timestamped before execution.

---

## 8. Uncertainty budget

Separate uncertainty sources:

```text
instrument
environment
fabrication
model
sampling
calibration
readout
analysis
```

Do not collapse all uncertainty into a single unexplained error bar.

---

## 9. Reproducibility matrix

| Level | Requirement |
|---|---|
| R0 | same run reconstructed |
| R1 | repeated same device |
| R2 | different device |
| R3 | different fabrication lot |
| R4 | independent laboratory |
| R5 | independent architecture implementation |

The strongest claims require the highest appropriate level.

---

## 10. Benchmark integrity

A TPAC benchmark must report complete system boundaries.

Required accounting:

```text
host compute
control electronics
physical fabric
cooling
optical sources
readout
calibration
communication
post-processing
```

Any excluded component must be explicitly disclosed.

---

## 11. Baseline selection

A baseline must be:

- technically appropriate;
- available at comparable maturity;
- configured competently;
- measured under equivalent workload conditions.

Weak baselines invalidate otherwise impressive comparisons.

---

## 12. Statistical stopping

Experiments should define stopping criteria before data collection where practical.

Avoid continuing trials solely until a preferred significance threshold appears.

---

## 13. Negative evidence

Evidence against a hypothesis is first-class data.

A failed prediction should produce:

```text
updated model
revised confidence
new experimental question
```

rather than being silently discarded.

---

## 14. Claim dependency graph

Claims should be represented as a directed graph:

```text
physical coupling
      ↓
state control
      ↓
state-dependent transformation
      ↓
network computation
      ↓
workload
      ↓
advantage
```

A downstream claim inherits uncertainty from upstream claims.

---

## 15. Provenance inheritance

If a benchmark depends on calibration model `M7`, and `M7` is later invalidated, every dependent benchmark is automatically flagged for review.

This creates a formal **provenance inheritance mechanism** for TPAC evidence.

---

## 16. Confidence states

```text
UNTESTED
HYPOTHESIZED
PRELIMINARY
SUPPORTED
REPLICATED
BENCHMARKED
ESTABLISHED
```

Status can move backward when contradictory evidence appears.

---

## 17. Public claim policy

Public-facing statements should use the strongest wording justified by evidence.

Examples:

Weak evidence:
> “We hypothesize that...”

Observed:
> “We observed...”

Mechanistically supported:
> “Controlled experiments support...”

Replicated:
> “Independent replication reproduced...”

Comparative:
> “Under the stated benchmark conditions, TPAC achieved...”

---

## 18. Quantum boundary

The term **quantum computer** must not be used merely because a proposed system involves photons, phonons, resonances, phase behavior, or microscopic effects.

A quantum-computing claim requires a defined computational degree of freedom and evidence that the relevant quantum resource is actually used and preserved sufficiently for the claimed operation.

If the architecture is primarily classical nonlinear wave computation, it should be described as such.

---

## 19. Commercial evidence gate

Commercial valuation begins only after a concrete customer-relevant advantage is demonstrated.

Conceptual novelty may justify research interest; it does not by itself justify a revenue forecast.

---

## 20. Final principle

The most valuable TPAC artifact is not the largest claim.

It is the strongest chain of evidence connecting:

```text
physical reality
→ reproducible mechanism
→ programmable computation
→ benchmarked utility
→ independently verifiable value
```

That chain is the project's scientific and commercial foundation.
