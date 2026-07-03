# HTE Resonance Observatory v0.1 Build Plan

Return phrase: **Listen to the lattice.**

## Goal

Build a local-first observatory loop that turns a chemical formula into an HTE harmonic signature, renders it visually, sonifies it, and exports a traceable run ledger.

```text
formula input
  -> formula parser
  -> atomic-number mod 12 HTE mapping
  -> 12-fold wheel / chord view
  -> browser sonification
  -> JSON + Markdown run ledger
```

## v0.1 acceptance criteria

- User can enter a formula such as `SiO2`, `Fe2O3`, or `Ca10(PO4)6(OH)2`.
- The app parses element counts and flags unsupported syntax.
- Each element maps to `pitch_class = atomic_number mod 12`.
- The interface displays the weighted chord, pitch-class histogram, interval walk, and conservative HTE overlay state.
- The browser can play an HTE-rendered sonification.
- A run can be exported as JSON.
- All outputs carry a claim boundary: HTE-derived exploratory mapping only.

## Build phases

### Phase 1 — Core spine

- [x] Add Python package scaffold.
- [x] Add element table.
- [x] Add formula parser.
- [x] Add HTE signature builder.
- [x] Add experiment ledger generator.
- [x] Add basic tests.

### Phase 2 — Browser prototype

- [ ] Add formula input.
- [ ] Add 12-fold harmonic wheel.
- [ ] Add sonification button.
- [ ] Add JSON ledger export.
- [ ] Add example presets.

### Phase 3 — Materials Atlas grounding

- [ ] Add local material cards.
- [ ] Add source/provenance fields.
- [ ] Add optional Materials Project connector.
- [ ] Add calibration targets.

### Phase 4 — Public research package

- [ ] Add GitHub Pages site.
- [ ] Add Google Docs export path.
- [ ] Add one-page whitepaper draft.
- [ ] Add contribution guide.

## Guardrail

The v0.1 instrument may generate HTE signatures, visualizations, sounds, and ledgers. It may not claim conventional material properties unless those claims are externally sourced, calibrated, or experimentally supported.
