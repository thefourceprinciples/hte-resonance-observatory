from __future__ import annotations

from typing import Any, Dict, List
from .embeddings import ElementalEmbedding
from .projection import CircularProjection
from .harmonic import (
    build_reproducibility_ledger_entry,
    evaluate_compound,
)


def build_element_atlas_entry(
    formula: str,
    embedding: ElementalEmbedding,
    projection: CircularProjection,
    seed: int = 42,
    notes: str = "",
) -> Dict[str, Any]:
    """Evaluate a compound under a data-driven circular projection and build a ledger entry."""
    metrics = evaluate_compound(formula, embedding, projection, seed=seed)
    return build_reproducibility_ledger_entry(
        metrics=metrics,
        embedding=embedding,
        projection=projection,
        seed=seed,
        notes=notes,
    )


def render_atlas_markdown(entries: List[Dict[str, Any]]) -> str:
    """Render a list of reproducibility ledger entries into a Markdown audit table."""
    lines = [
        "# HTE Resonance Observatory — Reproducibility Ledger",
        "",
        "| Timestamp (UTC) | Formula | Embedding | SHA-256 (prefix) | r_proj | C_theta | 95% CI | p-value |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in entries:
        prov = e["provenance"]
        comp = e["compound"]
        ci_low, ci_high = comp["coherence_ci_95"]
        lines.append(
            f"| {e['timestamp_utc']} | {comp['formula']} | {prov['embedding_name']} "
            f"| `{prov['embedding_sha256'][:12]}` | {prov['projection_pearson_r']:.3f} "
            f"| {comp['modal_coherence']:.4f} | [{ci_low:.3f}, {ci_high:.3f}] "
            f"| {comp['null_permutation_p_value']:.4f} |"
        )
    return "\n".join(lines)
