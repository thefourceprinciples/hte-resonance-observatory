# TPAC Device Passport v2.7

## Objective

Create a machine-readable identity and capability record for every physical TPAC device and module.

## 1. Identity

```text
device_id
module_id
hardware_revision
fabrication_lot
assembly_revision
firmware_revision
```

## 2. Physical configuration

```text
cell_count
topology
material_stack
geometry_revision
interconnect_type
sensor_configuration
actuator_configuration
```

## 3. Capability profile

```text
state_space
precision
retention
coupling_range
control_bandwidth
readout_bandwidth
operating_frequency
```

## 4. Operating envelope

```text
minimum_temperature
maximum_temperature
maximum_drive
allowed_frequency_range
maximum_duty_cycle
```

## 5. Calibration state

Reference active calibration IDs and validity intervals.

## 6. Health state

```text
HEALTHY
DEGRADED
MAINTENANCE
QUARANTINED
RETIRED
```

## 7. Reliability history

Record:

- total operating hours;
- completed runs;
- faults;
- recoveries;
- calibration events;
- replaced components.

## 8. Performance profile

Store measured distributions rather than single nominal values.

## 9. Compatibility

Declare supported ISA, compiler, runtime, protocol, and firmware versions.

## 10. Provenance

The passport links hardware identity to fabrication and characterization records.

## 11. Passport immutability

Historical passport states are append-only. Current status is derived from the latest valid state rather than overwriting history.

## 12. Export

The passport can travel with a module so experiments performed outside the primary development environment retain hardware context.

## 13. Core invariant

**A TPAC result must identify the physical machine that produced it, not merely the software that requested it.**
