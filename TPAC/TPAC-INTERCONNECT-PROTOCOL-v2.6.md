# TPAC Interconnect Protocol v2.6

## Objective

Define a transport layer for communicating state, control, timing, and measurement information between TPAC modules.

## 1. Channel classes

```text
CONTROL
STATE
DATA
TIMING
TELEMETRY
SAFETY
```

## 2. Packet envelope

```text
protocol_version
source_module
destination_module
sequence_id
timestamp
payload_type
payload_length
payload
integrity_tag
```

## 3. Ordering

Packets that affect physical state declare ordering requirements. The runtime must not reorder state-changing operations unless the ISA explicitly permits it.

## 4. Backpressure

A receiver can advertise:

```text
READY
BUSY
DEGRADED
BLOCKED
UNKNOWN
```

## 5. Flow control

Flow control operates independently from computational semantics so congestion does not silently alter a workload.

## 6. Timing

Timing messages carry synchronization uncertainty. Hardware timestamps remain authoritative for physical measurements.

## 7. Integrity

Control and state-changing messages require integrity verification before execution.

## 8. Safety channel

Safety messages have priority over ordinary computation and may terminate excitation.

## 9. Fault handling

```text
lost packet → retry or fail according to operation semantics
invalid packet → reject
out-of-order state command → reject
unknown sender → reject
```

## 10. Provenance

Every state-changing message can be traced to the execution and ISA instruction that produced it.

## 11. Cross-domain translation

When translating between electrical, optical, acoustic, or other physical domains, the translator records the transformation and associated uncertainty.

## 12. Performance metrics

Benchmark:

- bandwidth;
- latency;
- jitter;
- packet loss;
- energy per transfer;
- synchronization error;
- fault recovery time.

## 13. Core invariant

**Interconnect behavior is part of computation whenever transport changes timing, state, energy, or physical coupling.**
