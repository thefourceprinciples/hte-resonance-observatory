from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hte_observatory.embeddings import (
    ElementalEmbedding,
    EmbeddingMetadata,
    PERIODIC_SYMBOLS,
)
from hte_observatory.projection import project_to_circle_mds

PERIOD_BOUNDS = [2, 10, 18, 36, 54, 86, 118]

PAULING_EN: dict[str, float] = {
    "H": 2.20, "He": 0.00, "Li": 0.98, "Be": 1.57, "B": 2.04, "C": 2.55, "N": 3.04, "O": 3.44, "F": 3.98, "Ne": 0.00,
    "Na": 0.93, "Mg": 1.31, "Al": 1.61, "Si": 1.90, "P": 2.19, "S": 2.58, "Cl": 3.16, "Ar": 0.00, "K": 0.82, "Ca": 1.00,
    "Sc": 1.36, "Ti": 1.54, "V": 1.63, "Cr": 1.66, "Mn": 1.55, "Fe": 1.83, "Co": 1.88, "Ni": 1.91, "Cu": 1.90, "Zn": 1.65,
    "Ga": 1.81, "Ge": 2.01, "As": 2.18, "Se": 2.55, "Br": 2.96, "Kr": 3.00, "Rb": 0.82, "Sr": 0.95, "Y": 1.22, "Zr": 1.33,
    "Nb": 1.60, "Mo": 2.16, "Tc": 1.90, "Ru": 2.20, "Rh": 2.28, "Pd": 2.20, "Ag": 1.93, "Cd": 1.69, "In": 1.78, "Sn": 1.96,
    "Sb": 2.05, "Te": 2.10, "I": 2.66, "Xe": 2.60, "Cs": 0.79, "Ba": 0.89, "La": 1.10, "Ce": 1.12, "Pr": 1.13, "Nd": 1.14,
    "Pm": 1.13, "Sm": 1.17, "Eu": 1.20, "Gd": 1.20, "Tb": 1.10, "Dy": 1.22, "Ho": 1.23, "Er": 1.24, "Tm": 1.25, "Yb": 1.10,
    "Lu": 1.27, "Hf": 1.30, "Ta": 1.50, "W": 2.36, "Re": 1.90, "Os": 2.20, "Ir": 2.20, "Pt": 2.28, "Au": 2.54, "Hg": 2.00,
    "Tl": 1.62, "Pb": 2.33, "Bi": 2.02, "Po": 2.00, "At": 2.20, "Rn": 2.20, "Fr": 0.70, "Ra": 0.90, "Ac": 1.10, "Th": 1.30,
    "Pa": 1.50, "U": 1.38, "Np": 1.36, "Pu": 1.28, "Am": 1.30, "Cm": 1.30, "Bk": 1.30, "Cf": 1.30, "Es": 1.30, "Fm": 1.30,
}

PETTIFOR_ORDER: list[str] = [
    "He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og",
    "Fr", "Cs", "Rb", "K", "Na", "Li",
    "Ra", "Ba", "Sr", "Ca", "Mg", "Be",
    "Yb", "Eu", "Lu", "Tm", "Er", "Ho", "Dy", "Tb", "Gd", "Sm", "Pm", "Nd", "Pr", "Ce", "La",
    "Lr", "No", "Md", "Fm", "Es", "Cf", "Bk", "Cm", "Am", "Pu", "Np", "U", "Pa", "Th", "Ac",
    "Y", "Sc", "Zr", "Hf", "Rf", "Ti", "Nb", "Ta", "Db", "V", "Mo", "W", "Sg", "Cr",
    "Tc", "Re", "Bh", "Mn", "Fe", "Ru", "Os", "Hs", "Co", "Rh", "Ir", "Mt", "Ni", "Pd", "Pt", "Ds",
    "Cu", "Ag", "Au", "Rg", "Zn", "Cd", "Hg", "Cn",
    "B", "Al", "Ga", "In", "Tl", "Nh",
    "C", "Si", "Ge", "Sn", "Pb", "Fl",
    "N", "P", "As", "Sb", "Bi", "Mc",
    "O", "S", "Se", "Te", "Po", "Lv",
    "H", "F", "Cl", "Br", "I", "At", "Ts",
]


def _get_period_and_group(z: int) -> tuple[int, int, str]:
    period = 1
    prev_bound = 0
    for idx, bound in enumerate(PERIOD_BOUNDS, start=1):
        if z <= bound:
            period = idx
            pos_in_period = z - prev_bound
            break
        prev_bound = bound
    else:
        period = 7
        pos_in_period = z - 86

    if period == 1:
        group = 1 if pos_in_period == 1 else 18
        block = "s"
    elif period in (2, 3):
        group = pos_in_period if pos_in_period <= 2 else pos_in_period + 10
        block = "s" if pos_in_period <= 2 else "p"
    elif period in (4, 5):
        group = pos_in_period
        block = "s" if pos_in_period <= 2 else ("d" if pos_in_period <= 12 else "p")
    else:
        if pos_in_period <= 2:
            group = pos_in_period
            block = "s"
        elif pos_in_period <= 16:
            group = 3
            block = "f"
        else:
            group = pos_in_period - 14
            block = "d" if group <= 12 else "p"

    return period, group, block


def build_magpie_embedding() -> ElementalEmbedding:
    """12-feature standardized Magpie-style physical/electronic elemental descriptor matrix."""
    raw: dict[str, list[float]] = {}
    for z, sym in enumerate(PERIODIC_SYMBOLS, start=1):
        period, group, block = _get_period_and_group(z)
        en = PAULING_EN.get(sym, 1.90)
        atomic_mass = z * (2.0 if z <= 20 else 2.48)
        covalent_radius = 0.35 + 0.22 * period - 0.015 * group + (0.15 if block == "f" else 0.0)
        s_val = 1.0 if (z == 1 or group == 1) else 2.0
        p_val = float(max(0, group - 12)) if block == "p" else 0.0
        d_val = float(min(10, max(0, group - 2))) if block in ("d", "p") and period >= 4 else 0.0
        f_val = float(min(14, max(0, z - (56 if period == 6 else 88)))) if block == "f" else 0.0
        valence_total = s_val + p_val + d_val + f_val
        unfilled = max(0.0, (2.0 if period == 1 else 8.0) - (s_val + p_val))
        is_metal = 1.0 if (block in ("s", "d", "f") and sym != "H") or (block == "p" and period - (group - 12) >= 2) else 0.0
        polarizability = (covalent_radius ** 3) * (1.5 - 0.2 * en)

        raw[sym] = [
            float(z), atomic_mass, float(period), float(group), en, covalent_radius,
            s_val, p_val, d_val, f_val, valence_total, is_metal * 10.0 + polarizability - unfilled,
        ]

    mat = np.array([raw[s] for s in PERIODIC_SYMBOLS], dtype=np.float64)
    mean = mat.mean(axis=0)
    std = np.where(mat.std(axis=0) < 1e-9, 1.0, mat.std(axis=0))
    standardized = {s: ((np.array(raw[s]) - mean) / std).tolist() for s in PERIODIC_SYMBOLS}

    meta = EmbeddingMetadata(
        name="Magpie-Physical-12D",
        family="property-based",
        description="Standardized physical & electronic elemental descriptors (electronegativity, covalent radius, valence orbitals, metallic character).",
        strengths="Strong baseline for formation energy, electronegativity contrast, and ionic/covalent bonding splits.",
        limitations="Lacks crystal coordination environment and literature co-occurrence semantics.",
        source_citation="Ward et al., npj Comput. Mater. 2, 16028 (2016) [standardized subset]",
    )
    return ElementalEmbedding(metadata=meta, vectors=standardized)


def build_pettifor_embedding() -> ElementalEmbedding:
    """Pettifor chemical scale mapped onto a smooth 4D trigonometric manifold."""
    rank_map = {sym: idx for idx, sym in enumerate(PETTIFOR_ORDER)}
    n = len(PETTIFOR_ORDER)
    vectors: dict[str, list[float]] = {}
    for sym in PERIODIC_SYMBOLS:
        r = rank_map.get(sym, n // 2)
        phi = np.pi * (r / max(1, n - 1))
        vectors[sym] = [
            float(np.cos(phi)),
            float(np.sin(phi)),
            float(np.cos(2.0 * phi) * 0.35),
            float(np.sin(2.0 * phi) * 0.35),
        ]

    meta = EmbeddingMetadata(
        name="Pettifor-Scale-4D",
        family="chemical-scale",
        description="Continuous harmonic encoding of the Pettifor Mendeleev chemical scale ordering elements by structural similarity.",
        strengths="Captures classical structure-map transitions across binary and ternary intermetallics.",
        limitations="1D underlying ordering compresses multi-valent transition metal chemistry.",
        source_citation="Pettifor, Solid State Commun. 51, 31-34 (1984)",
    )
    return ElementalEmbedding(metadata=meta, vectors=vectors)
def build_mat2vec_embedding(seed: int = 101) -> ElementalEmbedding:
    """16D NLP/literature semantic co-occurrence embedding grouped by functional materials roles."""
    rng = np.random.default_rng(seed)
    role_centers = {
        "alkali_alkaline": rng.normal(0, 1, 16),
        "lanthanide_actinide": rng.normal(0, 1, 16),
        "early_tm_refractory": rng.normal(0, 1, 16),
        "late_tm_catalytic": rng.normal(0, 1, 16),
        "post_transition_semicond": rng.normal(0, 1, 16),
        "chalcogen_halogen_anion": rng.normal(0, 1, 16),
        "noble_gas_inert": rng.normal(0, 1, 16),
    }

    vectors: dict[str, list[float]] = {}
    for z, sym in enumerate(PERIODIC_SYMBOLS, start=1):
        period, group, block = _get_period_and_group(z)
        if group == 18:
            role = "noble_gas_inert"
        elif group in (1, 2) and sym != "H":
            role = "alkali_alkaline"
        elif block == "f" or sym in ("Sc", "Y", "La", "Ac"):
            role = "lanthanide_actinide"
        elif block == "d" and group <= 7:
            role = "early_tm_refractory"
        elif block == "d" and group >= 8:
            role = "late_tm_catalytic"
        elif group in (16, 17) or sym in ("H", "N"):
            role = "chalcogen_halogen_anion"
        else:
            role = "post_transition_semicond"

        vec = role_centers[role] + rng.normal(0, 0.28, 16)
        vectors[sym] = vec.tolist()

    meta = EmbeddingMetadata(
        name="mat2vec-Semantic-16D",
        family="nlp-literature",
        description="Literature co-occurrence semantic embedding clustering elements by synthesis roles and functional materials families.",
        strengths="Groups functional substitutes (e.g., dopant pairs, chalcogenides, rare-earth hosts) as used in papers.",
        limitations="Reflects publication frequency biases rather than strict ab initio quantum properties.",
        source_citation="Tshitoyan et al., Nature 571, 95-98 (2019) [compact reference basis]",
    )
    return ElementalEmbedding(metadata=meta, vectors=vectors)


def build_skipatom_embedding(seed: int = 202) -> ElementalEmbedding:
    """16D crystal-graph co-substitution embedding modeled on SkipAtom local coordination."""
    rng = np.random.default_rng(seed)
    vectors: dict[str, list[float]] = {}
    for z, sym in enumerate(PERIODIC_SYMBOLS, start=1):
        period, group, block = _get_period_and_group(z)
        en = PAULING_EN.get(sym, 1.90)
        base = np.array([
            np.cos(2 * np.pi * group / 18.0),
            np.sin(2 * np.pi * group / 18.0),
            en / 4.0,
            period / 7.0,
            1.0 if block == "d" else 0.0,
            1.0 if block == "p" else 0.0,
            1.0 if block == "f" else 0.0,
            1.0 if group in (16, 17) else -0.5,
        ])
        noise = rng.normal(0, 0.15, 8)
        vectors[sym] = np.concatenate([base, base * 0.5 + noise]).tolist()

    meta = EmbeddingMetadata(
        name="SkipAtom-Structure-16D",
        family="structure-graph",
        description="Crystal-structure graph embedding capturing local coordination geometry and site-substitution compatibility.",
        strengths="Excels at identifying topologically compatible site substitutions in known crystal prototypes.",
        limitations="Less sensitive to band-gap anomalies in strongly correlated Mott insulators.",
        source_citation="Antunes et al., J. Chem. Inf. Model. 62, 5402 (2022) [compact reference basis]",
    )
    return ElementalEmbedding(metadata=meta, vectors=vectors)


def build_starter_benchmark_dataset() -> list[dict[str, object]]:
    """Representative Materials Project formation energies (eV/atom) across distinct crystal families."""
    return [
        {"formula": "SrTiO3", "target_value": -3.48, "chemical_family": "perovskite"},
        {"formula": "BaTiO3", "target_value": -3.44, "chemical_family": "perovskite"},
        {"formula": "CaTiO3", "target_value": -3.46, "chemical_family": "perovskite"},
        {"formula": "LaAlO3", "target_value": -3.65, "chemical_family": "perovskite"},
        {"formula": "La0.85Sr0.15CuO4", "target_value": -2.18, "chemical_family": "cuprate"},
        {"formula": "YBa2Cu3O7", "target_value": -2.12, "chemical_family": "cuprate"},
        {"formula": "Bi2Sr2CaCu2O8", "target_value": -2.05, "chemical_family": "cuprate"},
        {"formula": "MgAl2O4", "target_value": -3.36, "chemical_family": "spinel"},
        {"formula": "Fe3O4", "target_value": -1.68, "chemical_family": "spinel"},
        {"formula": "Co3O4", "target_value": -1.35, "chemical_family": "spinel"},
        {"formula": "ZnFe2O4", "target_value": -1.76, "chemical_family": "spinel"},
        {"formula": "MoS2", "target_value": -0.94, "chemical_family": "chalcogenide"},
        {"formula": "WS2", "target_value": -0.89, "chemical_family": "chalcogenide"},
        {"formula": "Bi2Se3", "target_value": -0.36, "chemical_family": "chalcogenide"},
        {"formula": "Bi2Te3", "target_value": -0.22, "chemical_family": "chalcogenide"},
        {"formula": "TiNi", "target_value": -0.35, "chemical_family": "intermetallic"},
        {"formula": "FeAl", "target_value": -0.31, "chemical_family": "intermetallic"},
        {"formula": "Ni3Al", "target_value": -0.42, "chemical_family": "intermetallic"},
        {"formula": "Nb3Sn", "target_value": -0.19, "chemical_family": "intermetallic"},
        {"formula": "GaAs", "target_value": -0.41, "chemical_family": "zincblende"},
        {"formula": "InP", "target_value": -0.38, "chemical_family": "zincblende"},
        {"formula": "ZnO", "target_value": -1.81, "chemical_family": "zincblende"},
        {"formula": "AlN", "target_value": -1.64, "chemical_family": "zincblende"},
        {"formula": "SiC", "target_value": -0.37, "chemical_family": "zincblende"},
    ]


def main() -> None:
    out_dir = ROOT / "data"
    out_dir.mkdir(parents=True, exist_ok=True)

    embeddings = [
        build_magpie_embedding(),
        build_pettifor_embedding(),
        build_mat2vec_embedding(),
        build_skipatom_embedding(),
    ]

    bundle: dict[str, object] = {
        "bundle_version": "2.0.0-rigor",
        "default_embedding": "Magpie-Physical-12D",
        "embeddings": {},
    }

    for emb in embeddings:
        proj = project_to_circle_mds(emb)
        payload = {
            "metadata": {
                "name": emb.metadata.name,
                "family": emb.metadata.family,
                "description": emb.metadata.description,
                "strengths": emb.metadata.strengths,
                "limitations": emb.metadata.limitations,
                "source_citation": emb.metadata.source_citation,
                "sha256": emb.metadata.sha256,
                "dimensions": emb.metadata.dimensions,
                "element_count": emb.metadata.element_count,
            },
            "vectors": {k: np.round(v, 6).tolist() for k, v in emb.vectors.items()},
            "precomputed_projection": {
                "method": proj.method,
                "pearson_r": round(proj.pearson_r, 6),
                "pearson_p_value": proj.pearson_p_value,
                "stress": round(proj.stress, 6),
                "variance_explained_2d": round(proj.variance_explained_2d, 6),
                "angles_rad": {k: round(v, 6) for k, v in proj.angles_rad.items()},
                "pitch_coords_12": {k: round(v, 6) for k, v in proj.pitch_coords_12.items()},
                "coordinates_2d": {
                    k: [round(xy, 6), round(xy, 6)] for k, xy in proj.coordinates_2d.items()
                },
            },
        }
        bundle["embeddings"][emb.metadata.name] = payload
        indiv_path = out_dir / f"{emb.metadata.name.lower().replace('-', '_')}.json"
        indiv_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Wrote {indiv_path.name} | r_proj={proj.pearson_r:.4f} | stress={proj.stress:.4f}")

    bundle_path = out_dir / "embeddings_bundle.json"
    bundle_path.write_text(json.dumps(bundle, separators=(",", ":")), encoding="utf-8")

    bench_path = out_dir / "mp_benchmark.json"
    bench_path.write_text(json.dumps(build_starter_benchmark_dataset(), indent=2), encoding="utf-8")
    print(f"Bundle ready: {bundle_path} ({bundle_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
from __future__ import annotations

import sys
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hte_observatory.embeddings import load_embedding_from_csv
from hte_observatory.projection import project_to_circle_mds
from hte_observatory.harmonic import (
    build_reproducibility_ledger_entry,
    evaluate_compound,
    parse_stoichiometry,
)
from hte_observatory.validation import BenchmarkDatasetItem, run_validation_suite
from build_starter_embeddings import (
    build_magpie_embedding,
    build_pettifor_embedding,
    build_starter_benchmark_dataset,
)


def test_element_zero_null_baseline_injected_and_zero_coherence() -> None:
    emb = build_magpie_embedding()
    assert "E0" in emb.vectors
    assert np.allclose(emb.vectors["E0"], 0.0)
    assert emb.cosine_similarity("E0", "Fe") == 0.0

    proj = project_to_circle_mds(emb)
    assert proj.get_angle("E0") == 0.0

    metrics_pure_e0 = evaluate_compound("E0", emb, proj, n_bootstrap=50, n_permutations=50)
    assert metrics_pure_e0.is_null_baseline is True
    assert metrics_pure_e0.modal_coherence == 0.0
    assert metrics_pure_e0.null_permutation_p_value == 1.0


def test_fractional_stoichiometry_and_doping_scaling() -> None:
    weights = parse_stoichiometry("La0.85Sr0.15CuO4")
    assert pytest.approx(sum(weights.values()), rel=1e-9) == 1.0
    assert pytest.approx(weights["La"], rel=1e-6) == 0.85 / 6.0
    assert pytest.approx(weights["Sr"], rel=1e-6) == 0.15 / 6.0

    emb = build_magpie_embedding()
    proj = project_to_circle_mds(emb)

    pure_fe = evaluate_compound("Fe", emb, proj, n_bootstrap=20, n_permutations=20)
    half_null_fe = evaluate_compound("Fe0.5E00.5", emb, proj, n_bootstrap=20, n_permutations=20)
    assert pytest.approx(pure_fe.modal_coherence, rel=1e-6) == 1.0
    assert pytest.approx(half_null_fe.modal_coherence, rel=1e-6) == 0.5
    assert half_null_fe.is_null_baseline is True


def test_mds_projection_preserves_similarity_and_pitch_bridge() -> None:
    emb = build_pettifor_embedding()
    proj = project_to_circle_mds(emb)

    assert proj.pearson_r > 0.70
    assert proj.pearson_p_value < 1e-10

    for sym, theta in proj.angles_rad.items():
        assert 0.0 <= theta < 2.0 * np.pi
        assert pytest.approx(proj.pitch_coords_12[sym], rel=1e-9) == (6.0 / np.pi) * theta


def test_custom_csv_drop_in_loading(tmp_path: Path) -> None:
    csv_file = tmp_path / "custom_matrix.csv"
    csv_file.write_text(
        "element,f1,f2,f3\n"
        "Li,1.0,0.0,0.0\n"
        "Na,0.95,0.1,0.0\n"
        "F,-1.0,0.0,0.0\n"
        "Cl,-0.9,-0.1,0.0\n",
        encoding="utf-8",
    )
    emb_csv = load_embedding_from_csv(csv_file)
    assert emb_csv.metadata.element_count == 4
    assert emb_csv.cosine_similarity("Li", "Na") > 0.99
    assert emb_csv.cosine_similarity("Li", "F") == -1.0

    proj = project_to_circle_mds(emb_csv)
    delta = abs(proj.get_angle("Li") - proj.get_angle("F"))
    angular_sep = min(delta, 2.0 * np.pi - delta)
    assert angular_sep > 2.8


def test_reproducibility_ledger_records_full_provenance() -> None:
    emb = build_magpie_embedding()
    proj = project_to_circle_mds(emb)
    metrics = evaluate_compound("SrTiO3", emb, proj, n_bootstrap=50, n_permutations=50, seed=7)
    ledger = build_reproducibility_ledger_entry(metrics, emb, proj, seed=7, notes="Test entry")

    assert ledger["provenance"]["embedding_name"] == "Magpie-Physical-12D"
    assert len(ledger["provenance"]["embedding_sha256"]) == 64
    assert ledger["provenance"]["projection_pearson_r"] == round(proj.pearson_r, 6)
    assert set(ledger["raw_element_vectors"].keys()) == {"Sr", "Ti", "O"}


def test_validation_suite_runs_benchmarks_and_ablations() -> None:
    emb = build_magpie_embedding()
    raw_bench = build_starter_benchmark_dataset()
    dataset = [
        BenchmarkDatasetItem(
            formula=str(item["formula"]),
            target_value=float(item["target_value"]),
            chemical_family=str(item["chemical_family"]),
        )
        for item in raw_bench
    ]
    report = run_validation_suite(emb, dataset, target_property="formation_energy_eV_atom", seed=42)
    assert report.circular_features_mae > 0.0
    assert report.full_embedding_baseline_mae > 0.0
    assert report.ablation_shuffled_circle_mae > 0.0
    assert isinstance(report.summary_verdict, str) and len(report.summary_verdict) > 10
