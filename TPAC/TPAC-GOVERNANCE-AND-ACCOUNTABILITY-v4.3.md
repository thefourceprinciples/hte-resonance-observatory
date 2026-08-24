# TPAC Governance and Accountability v4.3

## Objective

Make authority, evidence, decisions, provenance, and intervention rights explicit throughout the TPAC system.

## Authority model

```text
OBSERVE
→ ANALYZE
→ PROPOSE
→ AUTHORIZE
→ ACTUATE
→ VERIFY
```

No layer silently inherits authority from another.

## Separation of powers

Distinct roles should exist for:

- experiment design;
- physical authorization;
- execution;
- analysis;
- evidence review;
- release/publication.

For small deployments, combined roles are permitted only when the combination is explicitly recorded.

## Intervention rights

Safety systems can interrupt execution. Research systems can reject unsupported claims. Operators can stop physical execution within their authorization scope.

## Evidence access

Raw measurements remain distinguishable from interpretations, derived datasets, and claims.

## Change control

Material changes to hardware, software, calibration, protocols, or analysis create versioned events.

## Accountability record

Every consequential action records:

```text
action
actor/process
authority basis
timestamp
affected resources
result
```

## Conflict handling

If evidence and a governing assumption conflict, the conflict is preserved and routed for review rather than silently resolved by rewriting either side.

## Auditability

A reviewer should be able to reconstruct why a result was produced, who or what authorized relevant actions, and which evidence supported the resulting decision.

## Core invariant

**Authority must be explicit, evidence must remain inspectable, and consequential decisions must remain attributable.**
