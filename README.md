# HTE Resonance Observatory (`v0.3`)

**An interactive harmonic materials discovery & engineering workbench** that maps chemical formulas (`Z = 0..118` + `Element-0`) onto a 12-fold chromatic resonance wheel, evaluates `12 × 7` modal coherence (`CLV-HTE-001`), classifies compounds across **7 HTE Discovery States**, synthesizes live WebAudio chords, and exports structured experiment ledgers.

- **Launch Live Browser Workbench (No Install Required):** [https://github.io](https://github.io)
- **Companion Core Engine (`CLV-HTE-001`):** [thefourceprinciples/clavis-harmonica](https://github.com)

---

## What's New in `v0.3`

- **Full Element Table (`Z = 0..118` + `E0`):** Supports Hydrogen (`H`) through Oganesson (`Og`), `Element-0` (`E0`) substrate baseline, grouped parentheses (`Ca10(PO4)6(OH)2`), and fractional stoichiometries (`YBa2Cu3O6.9`).
- **Dual Mapping Modes (`Group-Phase v2` & `Raw Z mod 12 v1`):** Projects IUPAC periodic groups (`1–18`) onto `Z_12` (`+7.17σ` family clustering) alongside legacy `atomic_number mod 12` comparison.
- **`CLV-HTE-001` Modal Field & Fource Lock (`F`):** Evaluates all `84` modal frames (`12 tonics × 7 modes`) to infer the **Gold Halo** scale root, modal coherence (`C_modal`), and harmonic lock (`F`).
- **7-State Discovery Ladder & Interactive Glossary:** Classifies every atomic stack across *Substrate Zero, Singlet Seed, Gold Anchor, Piezo Tension, Armor Shield, Shadow Phase,* and *Plasma Flux* with kid-friendly metaphors and L2 engineering hypotheses.
- **Tactile Atom Stacking & Audio:** Click elements to stack and auto-increment counts (`H` → `H2` → `H3`), step backward with **`Undo (-1)`**, and hear real-time chords via **`Auto-Chime`** and **`Sonify`**.

---

## User Guide: How to Use the Observatory

### 1. The 12-Fold Standing-Wave Wheel & Delta Banner
- **Animated Standing-Wave Curve:** Sums the sine harmonics of every active element in your formula. The waveform color shifts dynamically to match your compound's **Discovered State**.
- **Solid Colored Dots (`●`):** Indicate the exact pitch classes (`0–11`, `C` through `B`) occupied by the elements currently in your stack.
- **Gold Outer Halo (`◎`):** Marks the **Inferred Modal Tonic**—the root note of the `12 × 7` scale that best frames your compound. *(For example, a single Hydrogen atom `H` sits as a solid dot on `C`, while `F#` receives the gold halo because `F# Locrian` frames an unbonded single note.)*
- **Delta Transition Banner:** Displays step-by-step sensitivity whenever you add or remove an atom, tracking state shifts and whether **Fource Lock** rose (`↑`), fell (`↓`), or held steady (`→`).

### 2. Controls & Formula Building

| Control | Function |
| :--- | :--- |
| **Formula Box** | Type any formula (`H2O`, `SiO2`, `BaTiO3`, `YBa2Cu3O6.9`, `E0`) and press **Enter** or click **Map**. |
| **Mapping Selector** | Toggle between **`Group-Phase (v2)`** (periodic family projection) and **`Raw Z mod 12 (v1)`**. |
| **Periodic Grid (`E0`–`Og`)** | Click tiles to stack atoms (clicking repeatedly increments stoichiometry); top borders are color-coded by pitch class. |
| **`Undo (-1)`** | Peels back the most recently added atom so you can step backward through phase transitions. |
| **`Sonify` & `Auto-Chime`** | Synthesizes an arpeggiated WebAudio chord using state-adaptive timbres (*triangle* = Piezo, *square* = Armor, *sine* = Gold/Other). |
| **`Log Entry` / `Export JSON`** | Appends timestamped runs to the **Materials Atlas Log** or downloads a structured `.json` experiment ledger. |
| **`Purge`** | Clears the formula input, stack history, and wheel back to `VOID`. |

### 3. The 7 HTE Discovery States

| State | Trigger Rule | Kid-Friendly Intuition | Engineering Hypothesis (Exploratory L2) |
| :--- | :--- | :--- | :--- |
| **`SUBSTRATE_ZERO`** | Only `E0` (`Z = 0`) present | *The Quiet Blank Canvas* | Null-reference background substrate (`Z=0, π=0, ω=0`) for baseline calibration. |
| **`SINGLET_SEED`** | `1` active pitch class | *One Lone Atom Looking for a Friend* | Unbonded elemental seed; high boundary tension awaiting a bonding partner. |
| **`GOLD_ANCHOR`** | Pitch class `7` (`G`) without tritone | *The Rock-Solid Bridge* | Fifth-anchored harmonic lock; candidate for high-symmetry bridging and low-friction stability. |
| **`PIEZO_TENSION`** | Tritone (`6` semitones apart) | *The Squeeze-and-Spark Spring* | Polar asymmetry across opposite wheel poles; candidate for electromechanical stress coupling. |
| **`ARMOR_SHIELD`** | `3+` classes on `{0, 5, 8, 10}` | *The Heavy Fortress Wall* | Subdominant mass clustering; candidate for mechanical damping and load absorption. |
| **`SHADOW_PHASE`** | Tritone-free, fifth-free dark cluster | *The Hidden Twin* | Asymmetric threshold pocket; candidate for metastable switching or band-gap hysteresis. |
| **`PLASMA_FLUX`** | `4+` classes with semitone (`m2`) | *The Lightning Cloud* | Multi-mode semitone excitation; candidate for superionic transport or catalytic flux. |

---

## Python API & Local Development

The Python backend (`src/hte_observatory/`) mirrors the browser engine and exposes FastAPI endpoints (`/health`, `/signature`, `/ledger`, `/compare`):

```bash
pip install -e .
uvicorn hte_observatory.api:app --reload
```

---

## Claim Boundaries (`L2 Exploratory Overlay`)

All signatures, modal fields, Fource lock scores, and 7-state classifications produced by the **HTE Resonance Observatory** are **Claim Level L2 (`derived_hte_mapping_only`)** exploratory overlays. They do not establish conventional physical, electronic, or chemical properties without external experimental measurement or quantum-mechanical calibration.
