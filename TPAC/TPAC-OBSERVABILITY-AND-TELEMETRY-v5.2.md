# TPAC Observability and Telemetry v5.2

## Objective

Make runtime behavior inspectable without conflating operational telemetry with scientific evidence.

## Telemetry domains

```text
DEVICE
CONTROL
THERMAL
NETWORK
RUNTIME
SCHEDULER
MEASUREMENT
SECURITY
```

## Event envelope

Every event contains:

```text
event_id
timestamp
source
resource_id
execution_id
schema_version
payload
provenance
```

## Clock discipline

Timestamp sources and synchronization quality are recorded. Cross-device timing claims require an explicit synchronization bound.

## Operational vs scientific data

Operational telemetry may diagnose execution but does not automatically qualify as scientific measurement.

## Sampling

Telemetry sampling rate, dropped events, aggregation, and retention are explicit.

## Health signals

Health state is derived from defined indicators and thresholds, with the underlying signals retained where feasible.

## Anomaly detection

Automated anomaly detection creates candidate events. It does not silently rewrite measurements or claim causation.

## Alert escalation

```text
INFO
→ WARNING
→ DEGRADED
→ CRITICAL
→ EMERGENCY
```

Thresholds are configuration artifacts with provenance.

## Telemetry integrity

Dropped, delayed, duplicated, or reordered events are detectable and represented explicitly.

## Core invariant

**Observability makes system behavior visible; it does not turn operational telemetry into scientific truth by default.**
