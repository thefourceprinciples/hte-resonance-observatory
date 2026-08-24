# TPAC Observability and Telemetry v2.3

## Objective

Make the entire physical-computational execution path inspectable without contaminating raw scientific measurements with derived interpretation.

## 1. Telemetry planes

```text
DEVICE
CONTROL
THERMAL
NETWORK
RUNTIME
DATA
SAFETY
```

## 2. Event model

Every significant event has:

```text
event_id
timestamp
device_id
execution_id
component
severity
state_before
state_after
payload_hash
```

## 3. Time synchronization

Telemetry records retain clock source and synchronization uncertainty.

## 4. Health metrics

Track:

- state fidelity;
- control error;
- detector health;
- thermal margin;
- calibration age;
- communication loss;
- execution retries;
- anomalous output rate.

## 5. Derived metrics

Derived health scores must reference their source measurements and calculation version.

## 6. Anomaly detection

Anomaly detectors operate in two modes:

```text
RULE_BASED
MODEL_BASED
```

Model-based alerts cannot silently rewrite raw measurements.

## 7. Observability tiers

```text
T0 critical safety
T1 execution
T2 device health
T3 research diagnostics
T4 development telemetry
```

## 8. Sampling policy

Telemetry sampling rates are versioned. Lossy telemetry must never be confused with lossy scientific measurement.

## 9. Alert lifecycle

```text
DETECTED → CORRELATED → TRIAGED → RESOLVED → REVIEWED
```

## 10. Correlation

Events should be joinable across controller, runtime, device, and measurement IDs.

## 11. Replay

An execution trace should permit reconstruction of software decisions and physical commands to the extent supported by recorded instrumentation.

## 12. Privacy/data minimization

Operational telemetry should contain only the information required for its function. Scientific provenance and operational logging should remain separable.

## 13. Retention classes

```text
RAW_SCIENTIFIC
DERIVED_SCIENTIFIC
SAFETY
OPERATIONAL
DEBUG
```

Retention policies are explicit and versioned.

## 14. Core invariant

**Observability increases accountability only when every derived interpretation remains traceable to the measurements from which it was produced.**
