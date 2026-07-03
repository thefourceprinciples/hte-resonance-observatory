# Calibration Layer

The Calibration Engine keeps the Observatory disciplined.

## Purpose

Separate:

```text
raw data
```

from:

```text
HTE-derived overlays
visual mappings
audio mappings
matter-state scores
residual thresholds
```

## Why calibration matters

The Observatory can render the same material in many ways. Without calibration profiles, two users could see or hear different results without knowing why.

Calibration profiles make every mapping explicit and versioned.

## Calibration profile fields

```yaml
profile_id: hte-default-v0.1
profile_name: HTE Default Prototype Calibration
version: 0.1
status: experimental

geometry:
  node_radius_scale: 1.0
  edge_weight_curve: linear
  pyknon_cluster_threshold: 0.33

audio:
  base_frequency_hz: 110
  tuning_system: equal_temperament_12
  coherence_to_purity_curve: linear
  shadow_to_subharmonic_gain: 0.5
  pyknon_to_beating_gain: 0.5

states:
  gold_threshold: 0.52
  armor_threshold: 0.42
  piezo_threshold: 0.40
  shadow_threshold: 0.65

residuals:
  darkness_low: 0.10
  darkness_medium: 0.25
  darkness_high: 0.50

chrono:
  enabled: false
  gamma_default: 0.06
  theta_mapping: rounded_mod_12
```

## Core rule

No visualization, sound, or matter-state label should be treated as meaningful unless the calibration profile used to generate it is known.

## Output requirement

Every Materials Atlas log entry should include:

```text
calibration_profile_id
engine_version
source_data_version
timestamp
```

## Claim boundary

Calibration does not validate HTE as physical law. It makes HTE outputs reproducible, comparable, and auditable.
