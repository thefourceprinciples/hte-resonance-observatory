from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hte_observatory import BenchmarkDatasetItem, run_validation_suite
from build_starter_embeddings import build_magpie_embedding, build_starter_benchmark_dataset


def test_physical_calibration_benchmark_runs_cleanly() -> None:
    emb = build_magpie_embedding()
    dataset = [
        BenchmarkDatasetItem(
            formula=str(item["formula"]),
            target_value=float(item["target_value"]),
            chemical_family=str(item["chemical_family"]),
        )
        for item in build_starter_benchmark_dataset()
    ]
    report = run_validation_suite(emb, dataset, seed=42)
    assert report.projection_pearson_r > 0.3
    assert report.circular_features_mae > 0.0
