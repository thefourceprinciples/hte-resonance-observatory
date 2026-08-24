# TPAC Application Runtime v2.9

## Objective

Provide an application-facing execution layer that lets workloads target TPAC capabilities without exposing unnecessary hardware details.

## 1. Application contract

Applications declare:

```text
workload
input schema
output schema
precision
latency target
energy target
uncertainty bound
availability requirements
```

## 2. Compilation request

The runtime submits the workload to the compiler with the current device/resource snapshot.

## 3. Execution modes

```text
LOCAL
BATCH
STREAMING
INTERACTIVE
REALTIME
EXPERIMENTAL
```

## 4. Streaming mode

Inputs may be processed continuously without forcing every sample through a complete host-side transaction.

## 5. Stateful applications

Applications may request persistent physical state when the selected device supports defined state-retention semantics.

## 6. Checkpoint contract

A stateful workload can expose:

```text
checkpoint
restore
fork
reset
```

only where physical semantics support the operation.

## 7. Result API

Return:

```text
result
confidence
uncertainty
execution_id
hardware_id
performance
provenance
```

## 8. Asynchronous execution

Long-running physical jobs return a stable execution identifier and can be queried without keeping the application process attached.

## 9. Cancellation

Cancellation semantics are workload-specific. The runtime must distinguish:

```text
CANCEL_REQUESTED
SAFE_TO_STOP
ABORTED
COMPLETED
```

## 10. Error transparency

Applications receive physical failure classes rather than generic computation errors.

## 11. Capability fallback

If TPAC cannot satisfy a requested constraint, the runtime may optionally route the workload to a declared conventional fallback, but the result must identify the backend actually used.

## 12. Cost visibility

Applications can request estimated and measured latency/energy before and after execution.

## 13. Reproducibility

Applications can request a reproducibility manifest for completed runs.

## 14. Core invariant

**The application layer must never make a conventional fallback appear to be a TPAC computation.**
