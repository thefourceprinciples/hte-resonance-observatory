# HTE Resonance Observatory (`v0.4 MAE`) — User Guide

**Live Workbench:** [https://github.io](https://github.io)

This guide walks through every panel, control, physical/harmonic metric, and export workflow in the **HTE Resonance Observatory & Materials Atlas Engine (MAE)**.

---

## 1. Workbench Layout (3-Column View)

On desktop viewports (`> 1180px` wide; close DevTools if docked on the side), the Observatory is organized into three synchronized panes:

1. **Left Pane — 12-Fold Resonance Wheel & Doping Phase Sweep**
   - **12-Fold Standing-Wave Wheel:** Plots active elements onto pitch classes `C` (`0`) through `B` (`11`). Solid colored dots indicate active element notes; the **Gold Halo** marks the inferred modal tonic.
   - **Delta Banner:** Reports live state transitions (`Prev State → New State`), Unison Coherence (`C_HTE`), and directional Fource Lock shifts (`↑`, `↓`, `→`) after every edit.
   - **Doping Phase Sweep (`Base + x·Dopant`):** Slide `x` from `0.00` to `2.00` to trace how Fource Lock (`F`) evolves continuously across non-stoichiometric compositions (presets: **`YBCO`**, **`BaTiO3`**, **`SiO2`**, **`GaAs+In`**).

2. **Center Pane — Formula Composer, Boundary Simulator & Periodic Grid**
   - **Formula Input & Stacking:** Type any chemical formula (supports parentheses and decimals, e.g., `YBa2Cu3O6.9`, `Ca(OH)2`, `E0`) or click periodic tiles (`E0`–`Og`) to stack atoms one by one. Use **`Undo (-1)`** to step backward or **`Purge`** to reset.
   - **Projection & Weighting Selectors:**
     - *Mapping Mode:* **`Group-Phase (v2)`** (periodic-group harmonic mapping) or **`Raw Z mod 12 (v1)`** (atomic-number modulo 12).
     - *Weighting Mode:* **`Stoich`** (atom count), **`Pauling χ`** (electronegativity-weighted), or **`Valence e⁻`** (valence-weighted).
   - **Interface Boundary Context:** Simulates how identical bulk chemistry shifts under physical boundary conditions (**`Free Bulk`**, **`Metal Host / Hydride`**, **`Ceramic Matrix`**, **`Cryo / Pressure`**, **`Plasma Excited`**), updating both the **Overlay State** and **Interface Failure Risk**.
   - **WebAudio Sonification:** Click **`Sonify`** (or keep **`Chime`** checked) to hear each active element's pitch class and octave band synthesized in real time.

3. **Right Pane — Docked Materials Atlas Legend (`MATLAS-Exxx`)**
   - **Hover to Preview / Pin to Scroll:** Move your cursor over any tile (`E0`–`Og`) to preview its 9-section dossier immediately. Click **`📌 Unpinned`** (or click an element tile) to lock the panel while scrolling.
   - **Canonical Badges (`★`):** Elements marked with a gold star (`E0`, `H`) load curated **Tier-2 Canonical Dossiers**; all other elements load **Tier-1 Auto-Synthesized `MATLAS` Profiles** with verified `(stable)`, `(primordial)`, and `(radio)` isotope lists.
---

## 2. Understanding the Telemetry & 7-State Overlay System

| Metric / State | Physical & Harmonic Meaning |
| :--- | :--- |
| **HTE Coordinate `(p, o)`** | Pitch class `p ∈ {0..11}` and octave layer `o` (`o = 0` for `E0`; `o = ⌊(Z - 1)/12⌋ + 1` in MAE dossiers). |
| **Fifth Ladder** | 6-step recurrence `p_n = (p_0 + 7n) mod 12` linking elements separated by 7-step intervals (e.g. `H → O → P → Ti → Cu → Kr`). |
| **Bond Polarity (`Δχ`)** | Electronegativity spread across active elements: `< 0.4` Covalent/Metallic, `0.4–1.69` Polar Covalent, `≥ 1.7` Ionic. |
| **Modal Field & Fource (`F`)** | Best-fit 7-note modal field (`Ionian` through `Locrian`), coherence (`C_mod`), and **Fource Lock (`F`)** tension-to-anchor ratio. |
| **Unison Coherence (`C_HTE`)** | Pairwise interval consonance across active atoms (`+1.00` for pure unison/diatomic pairs like `H2`). |

### The 7 Overlay Discovery States
1. **Substrate Zero (`E0`):** Zero-nucleon calibration origin (`Z = 0, π = 0, ω = 0`).
2. **Origin / Singlet (`H`):** Single pitch-class seed awaiting bonding or boundary constraint.
3. **Gold Anchor (`SiO2`):** Fifth-anchored harmonic lock (`p = 7` or Ceramic/Proton Matrix).
4. **Piezo Tension (`BaTiO3`):** Contains a 6-semitone tritone axis (`Δp = 6`), modeling polar stress-to-charge coupling.
5. **Armor Shield (`Fe2O3`):** Subdominant mass clustering (`p ∈ {0, 5, 8, 10}`); dense structural barrier.
6. **Shadow Phase (`GaAs` / Metal Hydrides):** Interstitial/hydride storage or metastable band-gap switching hidden inside a host lattice.
7. **Plasma Flux (`YBa2Cu3O7`):** High-entropy multi-mode excitation (`≥ 4` pitch classes with semitone clusters) or Plasma Excitation boundary.

---

## 3. Exporting Dossiers & Running the Python MAE Engine

- **Browser Exports:**
  - Click **`📋 Copy .md`** in the right-hand dossier header to copy a complete, formatted Markdown entry ready for `r/SubspacePhysics` or documentation.
  - Click **`Log`** to append a timestamped snapshot to the session log, or **`Export JSON`** to download the active compound signature together with the active element dossier.
- **Python Programmatic Usage (`src/hte_observatory/atlas.py`):**

```python
from hte_observatory.atlas import build_element_atlas_entry, render_atlas_markdown

entry = build_element_atlas_entry("H")
print(entry["entry_id"])                     # MATLAS-E001-HYDROGEN
print(entry["fifth_ladder"]["pathway_text"]) # H -> O -> P -> Ti -> Cu -> Kr
print(render_atlas_markdown(entry))          # Full publication-ready Markdown
```
