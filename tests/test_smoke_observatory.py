from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))


def test_dual_workbench_html_files_exist_and_link_together() -> None:
    v4_path = ROOT / "web" / "index.html"
    v5_path = ROOT / "web" / "v5.html"

    assert v4_path.exists(), "web/index.html (v0.4 MAE) must exist."
    assert v5_path.exists(), "web/v5.html (v5.0 Data-Driven Rigor) must exist."

    v4_html = v4_path.read_text(encoding="utf-8")
    v5_html = v5_path.read_text(encoding="utf-8")

    # Verify version switcher links connect v0.4 and v5.0
    assert "v5.html" in v4_html
    assert "index.html" in v5_html

    # Verify v5.0 Rigor UI elements and zero Z-mod-12 arithmetic
    assert "<!DOCTYPE html>" in v5_html
    assert "</html>" in v5_html
    assert 'id="rigorToggleBtn"' in v5_html
    assert 'id="embeddingSelect"' in v5_html
    assert 'id="compareSelect"' in v5_html
    assert 'id="customMatrixInput"' in v5_html
    assert 'id="wheelCanvas"' in v5_html
    assert 'id="dopingSlider"' in v5_html
    assert "Z % 12" not in v5_html
    assert "z % 12" not in v5_html


def test_v5_html_inline_js_syntax_with_node() -> None:
    node_bin = shutil.which("node")
    if node_bin is None:
        pytest.skip("Node.js not installed; skipping JS syntax check.")

    html = (ROOT / "web" / "v5.html").read_text(encoding="utf-8")
    start = html.find("<script>")
    end = html.rfind("</script>")
    assert start != -1 and end != -1 and end > start, "Missing inline <script> block in web/v5.html."

    js_code = html[start + len("<script>") : end]
    proc = subprocess.run(
        [node_bin, "--check", "-"],
        input=js_code,
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0, f"JavaScript syntax error in web/v5.html:\n{proc.stderr}"


def test_end_to_end_python_pipeline_smoke() -> None:
    from build_starter_embeddings import (
        build_magpie_embedding,
        build_mat2vec_embedding,
        build_pettifor_embedding,
        build_skipatom_embedding,
        build_starter_benchmark_dataset,
    )
    from hte_observatory.projection import project_to_circle_mds
    from hte_observatory.harmonic import evaluate_compound, build_reproducibility_ledger_entry
    from hte_observatory.validation import BenchmarkDatasetItem, run_validation_suite

    dataset = [
        BenchmarkDatasetItem(
            formula=str(d["formula"]),
            target_value=float(d["target_value"]),
            chemical_family=str(d["chemical_family"]),
        )
        for d in build_starter_benchmark_dataset()
    ]

    for builder in (
        build_magpie_embedding,
        build_pettifor_embedding,
        build_mat2vec_embedding,
        build_skipatom_embedding,
    ):
        emb = builder()
        proj = project_to_circle_mds(emb)
        assert -1.0 <= proj.pearson_r <= 1.0

        metrics = evaluate_compound("La0.85Sr0.15CuO4", emb, proj, n_bootstrap=20, n_permutations=20)
        assert 0.0 <= metrics.modal_coherence <= 1.0

        ledger = build_reproducibility_ledger_entry(metrics, emb, proj)
        assert ledger["provenance"]["embedding_name"] == emb.metadata.name

        report = run_validation_suite(emb, dataset)
        assert report.circular_features_mae > 0.0
