# Materials Atlas Entry Template

Each material or material stack should be captured as a reusable dossier.

## Template

```yaml
material_code:
name:
composition:
formula:
atomic_numbers: []
hte_classes: []
interval_walk: []

conventional_data:
  material_type:
  crystal_structure:
  phase:
  density:
  thermal_properties:
  electrical_properties:
  magnetic_properties:
  optical_properties:
  chemical_stability:
  known_applications: []
  references: []

hte_overlay:
  engine_version:
  calibration_profile:
  modal_field:
  modal_match:
  stability_score:
  coherence_estimate:
  pyknon_density:
  enharmonic_near_lock:
  gold_score:
  armor_score:
  piezo_score:
  shadow_score:
  darkness_residual:
  chrono_class:

state_interpretation:
  primary_state:
  secondary_states: []
  interpretation:
  risk_tags: []
  stabilizer_suggestions: []
  evidence_boundary:

experiments:
  proposed_tests: []
  completed_tests: []
  results: []

artifact_pathway:
  atlas_region:
  possible_artifacts: []
  next_action:
```

## Evidence boundary

HTE Atlas entries are exploratory overlays. Physical claims require conventional testing.

Examples:

- superconductivity requires zero resistance, Meissner effect, critical temperature, critical field, and replication
- literal transmutation requires isotope/nuclear evidence
- dark residual claims require subtractive audit and independent verification
- material-state labels are candidate classifications until tested
