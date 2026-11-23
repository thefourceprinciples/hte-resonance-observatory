from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hte_observatory.atlas import build_element_atlas_entry, render_atlas_markdown
from hte_observatory.projection import project_to_circle_mds
from build_starter_embeddings import build_magpie_embedding


def test_atlas_entry_and_markdown_rendering() -> None:
    emb = build_magpie_embedding()
    proj = project_to_circle_mds(emb)
    entry = build_element_atlas_entry("SrTiO3", emb, proj, seed=42, notes="Perovskite check")

    assert entry["provenance"]["embedding_name"] == "Magpie-Physical-12D"
    assert entry["compound"]["formula"] == "SrTiO3"

    md = render_atlas_markdown([entry])
    assert "SrTiO3" in md
    assert "Magpie-Physical-12D" in md
