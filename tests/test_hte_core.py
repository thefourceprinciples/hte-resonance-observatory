from __future__ import annotations

import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from hte_observatory import evaluate_compound, parse_stoichiometry, project_to_circle_mds
from build_starter_embeddings import build_magpie_embedding


def test_core_stoichiometry_and_coherence_bounds() -> None:
    weights = parse_stoichiometry("YBa2Cu3O7")
    assert pytest.approx(sum(weights.values()), rel=1e-9) == 1.0

    emb = build_magpie_embedding()
    proj = project_to_circle_mds(emb)
    res = evaluate_compound("YBa2Cu3O7", emb, proj, n_bootstrap=30, n_permutations=30)
    assert 0.0 <= res.modal_coherence <= 1.0
    assert 0.0 < res.null_permutation_p_value <= 1.0
