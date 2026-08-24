# TPAC Data Schema v1.5

## 1. Objective

Define a canonical data model so physical measurements, device identity, computation, analysis, and provenance remain joinable across the lifetime of the project.

## 2. Run identifier

Every experiment receives a globally unique identifier:

```text
TPAC-YYYYMMDD-DEVICE-EXPERIMENT-RUN
```

## 3. Core entities

```text
Device
FabricationLot
Calibration
Experiment
Trial
Measurement
Workload
Execution
Analysis
Claim
```

## 4. Device record

```yaml
device_id:
revision:
lot_id:
cell_count:
geometry_revision:
material_revision:
manufacturing_timestamp:
status:
```

## 5. Calibration record

```yaml
calibration_id:
device_id:
software_version:
parameter_set:
measurement_ids:
valid_from:
valid_until:
confidence:
operator_or_automation_id:
```

## 6. Experiment record

```yaml
experiment_id:
hypothesis_id:
protocol_version:
device_id:
calibration_id
workload_id:
control_configuration:
environment:
start_time:
end_time:
status:
```

## 7. Trial record

Each trial references exactly one experiment and preserves the randomized trial order.

```yaml
trial_id:
experiment_id:
sequence_index:
input_id:
state_label:
control_hash:
measurement_ids:
result_id:
```

## 8. Measurement record

Measurements are immutable.

```yaml
measurement_id:
device_id
timestamp
instrument_id
channel
sample_rate
units
raw_data_uri
checksum
quality_flags
```

## 9. Execution record

```yaml
execution_id
workload_id
compiler_version
runtime_version
device_id
calibration_id
mapping_hash
schedule_hash
start_time
end_time
energy
latency
status
```

## 10. Analysis record

```yaml
analysis_id
input_measurements
analysis_code_version
parameters
model
output_artifacts
uncertainty
analyst_or_pipeline_id
```

## 11. Claim linkage

A claim must point to the exact analysis and underlying measurements supporting it.

```text
Claim
 ↓
Analysis
 ↓
Measurement
 ↓
Trial
 ↓
Experiment
 ↓
Device
 ↓
FabricationLot
```

## 12. Immutable hashes

Hash:

- raw measurements;
- control programs;
- source workloads;
- compiled artifacts;
- analysis scripts;
- result manifests.

## 13. Data tiers

```text
RAW       immutable instrument output
DERIVED   transformed measurement data
ANALYSIS  statistical/model output
CLAIM     human-readable interpretation
```

Derived and interpretive layers must never overwrite raw data.

## 14. Missing data

Missing values are explicit.

Permitted status values:

```text
NOT_COLLECTED
NOT_APPLICABLE
LOST
INVALID
WITHHELD
```

A missing measurement must not silently become zero or null without explanation.

## 15. Failed experiments

Failed runs remain addressable and linked to the same provenance graph as successful runs.

## 16. Interoperability

Prefer open, machine-readable representations for metadata and measurements. Store units explicitly and avoid implicit coordinate systems.

## 17. Dataset release

A public dataset should contain enough metadata to reconstruct:

```text
what happened
where it happened
when it happened
with which hardware
under which calibration
using which control program
how the result was calculated
```

## 18. Data integrity invariant

**No result is more trustworthy than the provenance chain connecting it to the raw physical measurement.**
