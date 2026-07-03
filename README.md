# HTE Resonance Observatory

**A multimodal research platform for exploring material systems through harmonic topology, interactive visualization, sonification, experiment ledgers, and extensible analysis modules.**

> Return phrase: **Listen to the lattice.**

## What this is

HTE Resonance Observatory is an experimental, local-first research instrument for mapping materials into a layered coherence space.

It combines:

- **Materials Atlas entries** for conventional material identity and evidence
- **HTE harmonic mapping** using `atomic_number mod 12`
- **Formula parsing** for simple and grouped formulas such as `SiO2`, `Fe2O3`, and `Ca10(PO4)6(OH)2`
- **Lost-mode / modal coherence fields** inspired by Pythagorean and Greek modal systems
- **Matter-state overlay detection** for Gold, Armor, Piezo, Shadow, Plasma, and transition candidates
- **Darkness Functional residual auditing** using `Observed - Explained`
- **Browser-native sonification** using HTE-rendered pitch-class mappings
- **Experiment ledgers** that preserve source, formula, mapping, claim level, and evidence boundary
- **Extensible analysis tools** for future calibration against material datasets

This repository is a software and research-platform project. It does **not** claim that HTE replaces chemistry, proves new physics, proves dark matter, proves superconductivity, or validates literal transmutation. HTE is used here as an exploratory coordinate transform and coherence-overlay system.

## Core stack

```text
Materials data
  -> HTE harmonic coordinate layer
  -> Modal topology layer
  -> Matter-state overlay engine
  -> Darkness residual layer
  -> Visualization + sonification
  -> Materials Atlas log
  -> Exportable research artifacts
```

## Current milestone

**MVP v0.1:** local observatory scaffold.

Implemented foundation:

- Python package scaffold under `src/hte_observatory/`
- canonical element table through Ra / Z=88
- lightweight formula parser
- HTE harmonic signature builder
- experiment ledger generator
- FastAPI endpoints for signatures and ledgers
- browser prototype at `web/index.html`
- formula input, presets, 12-fold visual wheel, sonification, Atlas capture, and JSON ledger export
- basic tests and GitHub Actions workflow

Next capabilities:

- Materials Atlas source/provenance cards
- calibration profiles
- Materials Project connector
- Markdown / Google Docs report export
- richer modal field detection
- plugin API for hypothesis layers

## Quick start

Install locally:

```bash
python -m pip install -e '.[dev]'
pytest
```

Run the API:

```bash
uvicorn hte_observatory.api:app --reload
```

Open the browser prototype:

```text
web/index.html
```

## Claim boundary

Allowed framing:

> HTE Resonance Observatory is an exploratory interface for comparing materials through harmonic, modal, residual, and state-transition overlays.

Forbidden framing:

> This proves new physics, proves dark matter, proves superconductivity, or replaces conventional material science.

Every result should be treated as an **HTE overlay candidate** until tested by conventional methods.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── pyproject.toml
├── docs/
│   ├── architecture.md
│   ├── CLAIM_BOUNDARIES.md
│   ├── MVP_BUILD_PLAN.md
│   ├── SONIFICATION_SPEC.md
│   ├── calibration-layer.md
│   ├── materials-atlas-entry.md
│   └── roadmap.md
├── web/
│   └── index.html
├── examples/
│   └── materials/
│       └── quartz-ledger.json
├── experiments/
├── src/
│   └── hte_observatory/
│       ├── __init__.py
│       ├── api.py
│       ├── elements.py
│       ├── formula.py
│       ├── harmonic.py
│       └── ledger.py
├── tests/
│   └── test_hte_core.py
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
        └── python-tests.yml
```

## Development philosophy

1. Build a useful local prototype first.
2. Keep speculative modules clearly labeled.
3. Separate raw measurements from HTE overlays.
4. Make every mapping calibratable and versioned.
5. Preserve every meaningful run as a Materials Atlas entry.
6. Let the lattice be visual, audible, and auditable.

## License

Code is released under the MIT License unless otherwise noted.

Documentation, theory notes, and datasets may receive separate licenses in later releases.
