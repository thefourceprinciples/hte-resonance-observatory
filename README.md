# HTE Resonance Observatory (`v0.4 MAE`)

- **Live Interactive Workbench:** [https://github.io](https://github.io)
- **Documentation & Walkthrough:** [User Guide (`USER_GUIDE.md`)](./USER_GUIDE.md)

An interactive computational physics, harmonic periodic mapping, and **Materials Atlas Engine (MAE)** workbench built on **Harmonic Table of Elements (HTE)** coordinates, **CUC relational constraints**, and **Fource Lock** modal field analysis across all **119 elements (`E0` and `Z = 1..118`)**.

---

## Core Capabilities (`v0.4 MAE`)

1. **119-Element Harmonic Coordinate & Isotope Engine (`E0`–`Og`):**
   - Maps **Element-0 (`E0`, Substrate Zero)** and elements **`Z = 1..118`** onto 12-fold pitch classes (`p ∈ {0..11}`) and octave layers (`o`), supporting both **Group-Phase (`v2`)** and **Raw `Z mod 12` (`v1`)** projections.
   - Tracks verified IUPAC/NNDC isotopic profiles (`(stable)`, `(primordial)`, `(radio)`) alongside the **HTE Isotope Invariance Rule** (isotopes diverge in neutron mass and nuclear stability while sharing identical atomic number `Z` and pitch class `p(Z)`).
   - Computes **Diatomic Unison Coherence (`C_HTE`)** and **6-Step Fifth Ladder Sequences** (`p_n = (p_0 + 7n) mod 12`, e.g. `H → O → P → Ti → Cu → Kr`).

2. **Interactive 3-Column Browser Workbench (`web/`):**
   - **Left Pane — 12-Fold Standing-Wave Wheel & Doping Phase Sweep:** Real-time harmonic waveform interference, gold modal-tonic halo, and interactive **Fource Lock Doping Sweep (`Base + x·Dopant`)** with presets (`YBCO`, `BaTiO3`, `SiO2`, `GaAs+In`).
   - **Center Pane — Multi-Element Stacking & Boundary Simulator:** Click element tiles to stack compounds, switch weighting (`Stoich`, `Pauling χ`, `Valence e⁻`), test **Interface Boundary Contexts** (`Free Bulk`, `Metal Host / Hydride`, `Ceramic Matrix`, `Cryo / Pressure`, `Plasma Excited`), and sonify chords via WebAudio.
   - **Right Pane — Docked Scrollable Materials Atlas Legend (`MATLAS-Exxx`):** Hover any periodic tile to preview its full multi-section dossier (Core & HTE Signature, Isotopic Identity, Storage/Containment Modes, CUC Relational Map, 7-State Activation, Interface Failure Modes, Darkness Remainder, and HTE Search Directions), pin/lock scrolling (`📌`), or copy publication-ready Markdown (`📋 Copy .md`).
3. **Materials Atlas Engine (`src/hte_observatory/atlas.py`):**
   - Two-tier evolving architecture combining **Tier-1 Auto-Synthesized `MATLAS` Profiles** across all 119 elements with **Tier-2 Curated Canonical Dossiers** (`MATLAS-E000-SUBSTRATE` for `E0`, `MATLAS-E001-HYDROGEN` for `H`).
   - Exports structured JSON records and publication-ready Markdown dossiers (`render_atlas_markdown`).

4. **7-State Overlay & Discovery System:**
   - Classifies single elements, compounds, and constrained interfaces across **Substrate Zero (`E0`)**, **Origin / Singlet (`H`)**, **Gold Anchor (`SiO2`)**, **Piezo Tension (`BaTiO3`)**, **Armor Shield (`Fe2O3`)**, **Shadow Phase (`GaAs` / Metal Hydrides)**, and **Plasma Flux (`YBa2Cu3O7`)**.

---

## Repository Structure

```text
hte-resonance-observatory/
├── web/
│   ├── index.html           # 3-column interactive Observatory & MAE Dossier UI
│   └── app.js               # 119-element isotope table, harmonic engine & WebAudio synth
├── src/hte_observatory/
│   ├── elements.py          # Deterministic 119-element HTE coordinate mapping
│   ├── harmonic.py          # Formula parser, modal field solver & Fource Lock metrics
│   ├── atlas.py             # Materials Atlas Engine (MAE) 17-section dossier generator
│   └── ...                  # TPAC manifest, calibration, replay & reproducibility modules
├── tests/
│   └── test_atlas_engine.py # Automated verification across E0, Hydrogen & all 119 elements
├── USER_GUIDE.md            # Step-by-step walkthrough of the workbench & Python MAE API
└── README.md                # Project overview & quickstart
```

---

## Running Tests Locally

```bash
pip install -e ".[dev]"
pytest
```

For full instructions on using the 3-column workbench, Doping Phase Sweep, Boundary Contexts, and Materials Atlas Dossier exports, see the **[User Guide](./USER_GUIDE.md)**.

*Claim Boundary: All HTE coordinates, Fifth Ladder sequences, and Materials Atlas classifications represent derived structural mappings and exploratory engineering hypotheses.*
