# TPAC Hardware Abstraction Layer v2.2

## Objective

Expose heterogeneous physical TPAC devices through a common interface without erasing the physical differences that matter to correctness and performance.

## 1. Logical capability model

A device advertises:

```text
state_count
state_precision
coupling_graph
control_bandwidth
readout_bandwidth
retention
latency
energy_profile
thermal_profile
uncertainty
```

## 2. Capability discovery

At initialization the HAL queries the device passport and constructs a capability graph.

## 3. Primitive interface

Logical primitives include:

```text
initialize
write_state
couple
propagate
measure
reset
calibrate
health_check
```

A primitive may be unsupported or partially supported. The HAL must report that explicitly.

## 4. Physical metadata preservation

The abstraction must retain access to:

- physical location;
- calibration version;
- uncertainty;
- operating envelope;
- hardware revision.

## 5. Heterogeneous execution

Two devices implementing the same logical primitive may have different cost and fidelity profiles.

The compiler can therefore optimize for the actual hardware rather than an imaginary uniform machine.

## 6. Version compatibility

A HAL version defines semantic compatibility, not identical physical behavior.

## 7. Emulation backend

A software backend implements the same interface for testing and digital-twin execution.

The backend must identify itself as simulated in every result manifest.

## 8. Hardware backend

The hardware backend binds logical primitives to actual controller operations.

## 9. Error model

Errors distinguish:

```text
UNSUPPORTED
OUT_OF_RANGE
UNAVAILABLE
CALIBRATION_REQUIRED
PHYSICAL_FAULT
READOUT_INVALID
TIMEOUT
```

## 10. Capability negotiation

Applications may specify minimum requirements rather than device-specific instructions.

Example:

```text
requires state_precision >= P
requires retention >= T
requires uncertainty <= U
```

The scheduler resolves these requirements against available hardware.

## 11. Device substitution

A workload may migrate between compatible devices if the runtime records the changed hardware and recalibrates any affected physical mapping.

## 12. Core invariant

**Abstraction should simplify programming without concealing the physical facts required to interpret a result.**
