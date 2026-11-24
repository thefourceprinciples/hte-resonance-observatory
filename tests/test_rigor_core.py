from __future__ import annotations

import sys
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parent.parent
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
