# HTE Resonance Observatory (`v0.4 MAE`) — Comprehensive User & Architecture Guide

- **Live Interactive Workbench:** [https://github.io](https://github.io)
- **Repository Root:** [https://github.com](https://github.com)

The **HTE Resonance Observatory (`v0.4 MAE`)** is an integrated computational physics, harmonic periodic mapping, and **Materials Atlas Engine (MAE)** platform. It unifies **Harmonic Table of Elements (HTE)** lattice coordinates, **7-mode musical field theory**, **CUC relational boundary constraints**, and a **119-element isotopic & engineering dossier system** across both a zero-install browser workbench (`web/`) and a deterministic Python engine (`src/hte_observatory/`).

---

## 1. System Architecture: How the MAE Interfaces With the Build

The Observatory operates as a **dual-surface synchronized engine**:

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                 HARMONIC TABLE & ISOTOPE SUBSTRATE (E0..Og)                  │
│   • 119 Elements (Z = 0..118), Periodic Group, Valence, Pauling χ, Mass, STP │
│   • Verified IUPAC/NNDC Isotopes tagged (stable) / (primordial) / (radio)    │
└──────────────────────┬───────────────────────────────────┬───────────────────┘
                       │                                   │
        ┌──────────────▼──────────────┐     ┌──────────────▼──────────────┐
        │   BROWSER WORKBENCH (web/)  │     │   PYTHON MAE ENGINE (src/)  │
        │  • index.html + app.js      │     │  • elements.py & harmonic.py│
        │  • 12-Fold Canvas Wave Scope│     │  • atlas.py (17-Section MAE)│
        │  • Live Doping Phase Chart  │     │  • TPAC Calibration & Replay│
        │  • WebAudio Chord Synth     │     │  • 25-Test CI Suite (pytest)│
        │  • Docked MATLAS Side-Pane  │     │  • JSON & Markdown Exporters│
        └─────────────────────────────┘     └─────────────────────────────┘
```

### How Data Flows Across a Single User Interaction
1. **Element Hover (`onmouseenter`):** Moving the cursor over any periodic tile (`E0`–`Og`) queries `getElementDossier(sym)` in `web/app.js`. If the element has a curated **Tier-2 Canonical Entry** (`CANONICAL_DOSSIERS`, marked with `★`), it renders that deep dossier; otherwise it dynamically synthesizes a **Tier-1 `MATLAS` Profile** from the element's atomic constants, isotope array, and 6-step Fifth Ladder.
2. **Atom Click / Formula Entry (`stackElement` / `mapFormula`):**
   - Parses arbitrary stoichiometry (including nested parentheses and fractional doping like `YBa2Cu3O6.9` or `Ca(OH)2`).
   - Projects active atoms onto the **12-fold pitch circle** (`C` through `B`), solves for the optimal **7-note Modal Field (`Ionian`–`Locrian`)**, computes **Fource Lock (`F`)**, **Modal Coherence (`C_mod`)**, and **Unison Coherence (`C_HTE`)**, and classifies the compound into one of the **7 Overlay States**.
   - Simultaneously syncs the **Doping Phase Sweep** base formula, updates the **12-fold standing-wave canvas**, pins that element's **Materials Atlas Dossier** on the right, and triggers a real-time **WebAudio harmonic chime** (if `Chime` is enabled).
---

## 2. Detailed Walkthrough of the 3-Column Browser Workbench

*(Tip: On desktop screens wider than `1180px`, all three panes sit side-by-side. If DevTools is docked on the side, close it with `F12` to restore the full 3-column layout.)*

### Pane A (Left): 12-Fold Standing-Wave Wheel & Doping Phase Sweep
- **12-Fold Harmonic Wheel (`#scope`):** Renders a continuous radial standing wave modulated by every active element's pitch class (`p ∈ {0..11}`) and octave layer.
  - **Solid Colored Dots:** Active element pitch classes present in the formula.
  - **Gold Halo Ring:** The inferred modal tonic (`optimal_tonic`) that maximizes Fource Lock (`F`) across all 12 tonics and 7 musical modes (`12 × 7 = 84` candidate fields).
- **Live Delta Banner (`#deltaBanner`):** Tracks every incremental change (`Added O`, `Removed H`, `Doped YBa2Cu3O6 + 0.90 O`), showing exact transitions in **Overlay State**, **`C_HTE` Unison Coherence**, and **Fource Lock (`↑`, `↓`, `→`)**.
- **Doping Phase Sweep (`#dopingChart`):** Sweeps a dopant concentration `x ∈ [0.00, 2.00]` in `0.05` increments across `Base + x·Dopant`, plotting the continuous **Fource Lock (`F`) phase curve** with a gold marker at the active `x` value. Includes instant presets for **`YBCO`** (`YBa2Cu3O6 + x·O`), **`BaTiO3`**, **`SiO2`**, and **`GaAs+In`**.

### Pane B (Center): Formula Composer, Boundary Simulator & Periodic Grid
- **Formula Bar & Stacking Controls:** Type any formula and press `Enter` or **`Map`**, click tiles on the **119-element grid (`E0`–`Og`)** to stack atoms sequentially, use **`Undo (-1)`** to step backward, or **`Purge`** to clear the stack.
- **Projection & Weighting Controls:**
  - **Group-Phase (`v2`):** Maps periodic groups `1..18` smoothly around the 12-fold circle (`π_group = round(((g - 1) × 12) / 18) mod 12`) so chemically homologous elements share harmonic roles.
  - **Raw `Z mod 12` (`v1`):** Maps atomic numbers directly (`π_raw = Z mod 12`), preserving exact **Fifth Ladder** arithmetic (`+7` steps in `Z`).
  - **Weighting (`Stoich` / `Pauling χ` / `Valence e⁻`):** Weights each pitch class by atom count, Pauling electronegativity, or valence electron count.
- **Interface Boundary Context (`#boundarySelect`):** Demonstrates **CUC Relational Constraint Theory**—the same chemical formula shifts overlay state and failure mode depending on its physical environment:
  - **`Free Bulk`:** Unconstrained baseline phase.
  - **`Metal Host / Hydride`:** Shifts into **`SHADOW_PHASE`** and flags **High Hydrogen Embrittlement Risk** at metal grain boundaries.
  - **`Ceramic Matrix`:** Locks into **`GOLD_ANCHOR`** protonic/dielectric transfer channels.
  - **`Cryo / Pressure`:** Shifts into **`SHADOW_PHASE`** with cryogenic boil-off and seal permeation warnings.
  - **`Plasma Excited`:** Shifts into **`PLASMA_FLUX`** with ionization and thermal wall-erosion telemetry.
- **WebAudio Chord Synthesizer (`Sonify` / `Chime`):** Converts each active element's pitch class and octave band into acoustic frequencies (`f = 440 × 2^((MIDI - 69)/12)`), switching oscillator timbre by overlay state (`triangle` for Piezo Tension, `square` for Armor Shield, `sine` for Harmonic/Origin states).
### Pane C (Right): Docked Scrollable Materials Atlas Legend (`MATLAS-Exxx`)
- **Live Hover + Pin Lock (`📌`):** Hover over any periodic tile (`E0`–`Og`) to preview its dossier immediately; click **`📌 Unpinned`** (or click any tile) to lock the panel while reading or scrolling.
- **9-Section Structured Dossier:**
  1. **Core Identity & HTE Signature:** Material class, HTE role, atomic weight (`u`), STP phase at 20°C, valence, Pauling `χ`, atomic/diatomic chord (`{p}` and `{p, p}`), unison coherence `C_HTE`, and 6-step **Fifth Ladder**.
  2. **Isotopic Identity (Pitch-Invariant):** Lists verified `(stable)`, `(primordial)`, and `(radio)` isotopes and states the **HTE Isotope Invariance Rule** (isotopes diverge in neutron mass and nuclear stability while sharing identical `Z` and pitch class `p(Z)`).
  3. **Constraint, Thermal & Energy Fields:** Dominant containment constraints, cryogenic/refractory thermal character, and primary energy-carrier role.
  4. **Storage & Containment Modes:** Practical physical storage pathways (compressed gas, cryogenic liquid, metal hydride, chemical carrier, adsorbent, solid matrix, radiological shielding).
  5. **CUC Relational Constraint Map:** Shows how the same element shifts behavior across chemical and boundary contexts (`H₂` gas, `H⁺` proton, `H⁻` hydride, `D` fusion isotope, `Metal-H` interstitial) paired with its **Fource Phrase**.
  6. **7-State Activation Profile:** Element-specific activation across *Origin, Gold, Shadow, Plasma, Armor, Piezo,* and *Fifth Ladder*.
  7. **Interface Behavior & Failure Modes:** Surface adsorption, interstitial diffusion, grain-boundary effects, and physical failure hazards.
  8. **Darkness Remainder & Measurement Stack:** Contrasts *Visible Accounting* (`Z`, mass, `χ`) against the *Hidden Remainder* (permeation, embrittlement, defect trapping) alongside laboratory characterization metrics.
  9. **HTE Search Directions:** Actionable research targets along the element's Fifth Ladder and host lattices.
- **One-Click Exports:** Click **`📋 Copy .md`** to copy the complete Markdown dossier to your clipboard, or **`Export JSON`** in the center footer to download a combined compound + element JSON ledger.

---

## 3. Two-Tier Dossier System (`★` Gold Star vs. Auto-Derived) & Extending the Atlas

To keep all **119 elements (`E0` and `Z = 1..118`)** explorable from day one while allowing deep, domain-specific curation at your own pace, the MAE uses a **two-tier architecture**:

| Tier | Badge & Status | How It Works |
| :--- | :--- | :--- |
| **Tier-2: Canonical Dossier** | **`★` Gold Star** (`canonical draft`) | Hand-curated entries stored in `CANONICAL_DOSSIERS` (`E0`, `H`, and future promoted elements) with deep physical mechanisms, specific chemical species, exact failure thresholds, and tailored lab metrics. |
| **Tier-1: Auto-Derived Profile** | No star (`auto_derived_v1`) | Synthesized automatically from each element's atomic number `Z`, periodic group, block, STP phase, Pauling electronegativity `χ`, and verified IUPAC/NNDC isotope list. |

### How to Promote Any Element to a Gold Star (`★`)
1. Open `web/app.js` (and `src/hte_observatory/atlas.py` if syncing Python tests) and locate `CANONICAL_DOSSIERS`.
2. Copy the **`H`** entry block, change the symbol key (e.g., `O`, `C`, `Si`, or `Ti`), update `entry_id` (e.g., `MATLAS-E008-OXYGEN`), and tailor its narrative fields (`isoNote`, `cuc`, `states`, `iface`, `fails`, `lock`).
3. Commit the file—the gold **`★`** badge and **`canonical draft`** status appear automatically on the periodic grid.

---

## 4. Python MAE Engine & Automated Test Suite (`src/hte_observatory/`)

Every browser calculation is mirrored by a deterministic Python package tested across **Ubuntu, macOS, and Windows**:

```python
from hte_observatory.atlas import build_element_atlas_entry, render_atlas_markdown
from hte_observatory.harmonic import build_hte_signature

# Inspect a 119-element Materials Atlas Entry
h_dossier = build_element_atlas_entry("H")
print(h_dossier["entry_id"])                     # MATLAS-E001-HYDROGEN
print(h_dossier["fifth_ladder"]["pathway_text"]) # H -> O -> P -> Ti -> Cu -> Kr
print(render_atlas_markdown(h_dossier))          # Full publication-ready Markdown

# Analyze a multi-element compound
ybco = build_hte_signature("YBa2Cu3O6.9", mapping_mode="group", weight_mode="stoich")
print(ybco["overlay_state"], ybco["modal_field_group"])
```

Run the full 25-test verification suite locally with `pytest`.

*Claim Boundary: All HTE coordinates, Fifth Ladder sequences, and Materials Atlas classifications represent derived structural mappings and exploratory engineering hypotheses.*
