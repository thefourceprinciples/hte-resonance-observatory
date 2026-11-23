from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))


def test_web_index_html_structure_and_rigor_elements() -> None:
    index_path = ROOT / "web" / "index.html"
    assert index_path.exists(), "web/index.html must exist for GitHub Pages deployment."
    html = index_path.read_text(encoding="utf-8")

    # Verify complete HTML framing and three-layer UI controls
    assert "<!DOCTYPE html>" in html
    assert "</html>" in html
    assert 'id="rigorToggleBtn"' in html
    assert 'id="embeddingSelect"' in html
    assert 'id="compareSelect"' in html
    assert 'id="customMatrixInput"' in html
    assert 'id="wheelCanvas"' in html
    assert 'id="dopingSlider"' in html

    # Verify zero legacy Z-mod-12 arbitrary arithmetic remains in frontend
    assert "Z % 12" not in html
    assert "z % 12" not in html


def test_web_index_html_inline_js_syntax_with_node() -> None:
    node_bin = shutil.which("node")
    if node_bin is None:
        pytest.skip("Node.js not installed; skipping JS syntax check.")

    html = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
    start = html.find("<script>")
    end = html.rfind("</script>")
    assert start != -1 and end != -1 and end > start, "Missing inline <script> block in web/index.html."

    js_code = html[start + len("<script>") : end]
    proc = subprocess.run(
        [node_bin, "--check", "-"],
        input=js_code,
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0, f"JavaScript syntax error in web/index.html:\n{proc.stderr}"


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
