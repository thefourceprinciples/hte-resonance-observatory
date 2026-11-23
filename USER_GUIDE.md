# HTE Resonance Observatory — User Guide (v2.0 Data-Driven Rigor)

Welcome to the **HTE Resonance Observatory v2.0**, a data-driven materials exploration workbench. Unlike earlier exploratory versions (`v0.4 MAE`) that mapped elements via arbitrary modular arithmetic (`Z mod 12` and periodic group offsets), **v2.0 derives every angular coordinate, coherence metric, and statistical ranking directly from standardized chemical embeddings** and validates every claim against null models.

---

## 1. Understanding the Three-Layer Architecture

To prevent aesthetic or narrative metaphors from ever influencing numerical calculations, the workbench enforces a strict one-way pipeline across three distinct layers:

1. **Layer 1 — Data & Physics (Ground Truth):**
   - Loads L2-normalized elemental feature vectors (plus `E0` as an explicit zero-vector null baseline).
   - Projects high-dimensional vectors onto the unit circle $S^1$ ($\theta \in [0, 2\pi)$) via **Classical Multidimensional Scaling (MDS)** on pairwise cosine distances.
   - Computes stoichiometric weights ($w_i$), circular resultant coherence ($C_\theta$), Dirichlet bootstrap 95% confidence intervals, and periodic permutation $p$-values.
2. **Layer 2 — Visualization & Interaction:**
   - Renders the interactive circular manifold wheel, stoichiometric stacking bars, side-by-side comparison overlays, real-time doping sweeps, and continuous-$\theta$ Web Audio sonification ($f_i = 261.63 \times 2^{\theta_i / 2\pi}\text{ Hz}$).
   - Exposes a continuous coordinate bridge $p_i = \frac{6}{\pi}\theta_i \in [0, 12)$ purely for audio/visual continuity.
3. **Layer 3 — Interpretive Narrative (Optional & Post-Hoc):**
   - Translates Layer 1 metrics into plain-language qualitative regimes (*Tightly Clustered*, *Balanced Multi-Sublattice*, or *Polarized / High Chemical Contrast*).
   - **Strict Isolation:** Layer 3 never feeds back into Layer 1 numbers and disappears completely when **Rigor Mode** is turned on.

---

## 2. Quickstart Walkthrough (Browser Workbench)

Open `web/index.html` locally in any browser or visit the live GitHub Pages deployment:
`https://github.io`

### Step A: Choose or Compare Elemental Embeddings (Left Column)
- **Active Elemental Embedding:** Switch between four built-in 118-element representations:
  - **`Magpie-Physical-12D` (Default):** Standardized physical and electronic descriptors (Pauling electronegativity, covalent radius, valence orbitals, metallic character). Best for ionic/covalent splits and formation-energy baselines.
  - **`Pettifor-Scale-4D`:** Continuous harmonic encoding of the Pettifor Mendeleev chemical scale. Best for classical intermetallic structure-map transitions.
  - **`mat2vec-Semantic-16D`:** Literature co-occurrence semantic embedding grouping elements by functional materials roles and dopant families.
  - **`SkipAtom-Structure-16D`:** Crystal-structure graph embedding capturing local coordination geometry and site-substitution compatibility.
- **Inspect Projection Fidelity ($r_{\text{proj}}$ & Stress):** Check the top header pill whenever switching embeddings. $r_{\text{proj}}$ reports the Pearson correlation between true high-dimensional cosine similarities ($\mathbf{v}_i \cdot \mathbf{v}_j$) and circular chord similarities ($\cos(\theta_i - \theta_j)$). Lower stress and higher $r_{\text{proj}}$ indicate less 2D compression distortion.
- **Side-by-Side Comparison:** Select a second embedding in **Side-by-Side Comparison Embedding** to plot its elemental positions on a dashed inner ring (`R = 0.72`) inside the same wheel. This makes it immediately visible when two representations agree on chemical clustering versus when literature semantics diverge from physical descriptors.

### Step B: Evaluate Compounds & Run Doping Sweeps (Center Column)
- **Fractional Stoichiometries:** Enter any valid chemical formula—including decimal stoichiometries such as `La0.85Sr0.15CuO4` or `YBa2Cu3O7`—and click **Evaluate**.
- **Element-0 (`E0`) Null Baseline:** Test `E0` or mixed formulas like `Fe0.5E00.5` to verify null behavior. Because `E0` is anchored as a zero vector at $\theta = 0$, diluting an active compound with `E0` scales its resultant coherence $C_\theta$ linearly toward zero.
- **Stoichiometric Doping Sweep ($x$):** Drag the slider across $x \in [0.00, 1.00]$ for $\text{La}_{1-x}\text{Sr}_x\text{CuO}_4$ to watch the elemental weights, resultant coherence phasor (green vector), and bootstrap confidence intervals update in real time.
- **Sonify $\theta$:** Click **Sonify $\theta$** to hear each element's continuous angular position mapped smoothly across an octave (`261.63 Hz` to `523.25 Hz`) with amplitude proportional to its atomic fraction $w_i$.

### Step C: Toggle Rigor Mode (Top Header)
Click **Rigor Mode: OFF** to switch to **Rigor Mode: ON**:
- Hides all Layer 3 qualitative narrative panels and `0–12` pitch labels.
- Switches wheel tick marks from `p = 0..11` to exact radian multiples (`0.00π` to `1.83π`).
- Surfaces exact mathematical formulas (`|Σ w_i e^{iθ_i}|`, `Dirichlet(α=50w)`, `500 periodic shuffles`, `||Σ w_i v_i||_2`) directly inside the metric tiles.
- Click **Inspect Raw Vectors** in the left panel to view the exact L2-normalized feature vector and radian angle for every element in the active compound.

---

## 3. Running Null-Model & Ablation Audits

Before treating any circular cluster as a physically meaningful correlation, click **Run Null & Ablation Audit** in the left column:
1. Evaluates the active embedding across a benchmark set of Materials Project compounds with known formation energies ($\Delta H_f$).
2. Compares the real circular coherence correlation against a **Shuffled-Angle Null Model** (where elemental angles are randomly permuted across the periodic table).
3. Explicitly flags **`NULL/NEGATIVE RESULT`** whenever 2D circular compression fails to outperform random angle assignments on $\Delta H_f$, reminding you to use full-dimensional vectors (`||Σ w_i v_i||_2`) for quantitative regression.

---

## 4. Loading Custom Elemental Matrices (CSV or JSON)

You can drop any external elemental embedding (such as 200D `mat2vec`, `MatScholar`, `Oliynyk`, or `MEGNet` elemental tables) directly into the browser or Python CLI without changing code.

### Option 1: Browser Drag-and-Drop
Use the **Drop-In Custom Matrix (.csv or .json)** file picker in the left panel:
- **CSV Format:** First column must be IUPAC element symbols (`H`, `He`, `Li`, ...); remaining columns must be numeric feature values (header row is auto-detected).
- **JSON Format:** Either a flat dictionary `{"H": [0.1, -0.4, ...], "He": [...]}` or a structured Observatory bundle containing `"vectors": {...}`.
- The workbench automatically L2-normalizes each vector, injects `E0`, runs symmetric Jacobi eigendecomposition for Classical MDS, and computes $r_{\text{proj}}$ in milliseconds.

### Option 2: Python CLI Importer
Convert large external matrices into pre-audited Observatory JSON files from the command line:

```bash
python scripts/import_external_embedding.py path/to/external_matrix.csv \
  --output data/my_embedding.json \
  --name "My-Custom-Embedding" \
  --family "nlp-literature" \
  --description "Custom elemental vectors trained on domain literature." \
  --strengths "High resolution on transition-metal oxides." \
  --limitations "Unverified on intermetallics."
```

---

## 5. Exporting Reproducible Materials Atlas Ledgers

Every observation logged in the **Materials Atlas Ledger** (right column) captures full scientific provenance:
- Click **+ Log** to snapshot the current formula, stoichiometric weights, $C_\theta$, 95% bootstrap CI, permutation $p$-value, full-space norm, embedding name, SHA-256/FNV-1a matrix hash, projection $r_{\text{proj}}$, and raw element vectors.
- Export your session via **JSON** (`hte_atlas_reproducibility_ledger.json`) for programmatic replay or **MD** (`hte_atlas_reproducibility_ledger.md`) for clean Markdown audit tables.

---

## 6. Running the Python Rigor & Validation Suite

To run full cross-validated benchmarks (Ridge regression on circular features vs. full-dimensional composition baselines, shuffled-angle ablations, and leave-one-family-out cross-validation):

```bash
# Install package and test dependencies
pip install -e ".[dev]"

# Execute all unit, rigor, and HTML/JS smoke tests
pytest -v
```
---

### Interpreting Validation Outputs
* **`circular_features_mae` vs. `full_embedding_baseline_mae`:** Quantifies the exact predictive trade-off incurred when compressing a multi-dimensional elemental representation down to $S^1$.
* **`ablation_shuffled_circle_mae`:** Establishes whether the circular geometry carries genuine chemical ordering beyond random angle assignments.
* **`family_cv_mae`:** Tests out-of-distribution generalization when an entire structural class (such as perovskites, cuprates, or spinels) is held out during training.
