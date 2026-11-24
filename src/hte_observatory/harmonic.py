from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
import numpy as np

from .embeddings import ElementalEmbedding
from .projection import CircularProjection

FORMULA_TOKEN_RE = re.compile(r"(E0|[A-Z][a-z]?)(\d*\.?\d*)")
SOFTWARE_VERSION = "2.0.0-rigor"


def parse_stoichiometry(formula: str) -> Dict[str, float]:
    """
    Parse chemical formulas including fractional stoichiometries (e.g., 'La0.85Sr0.15CuO4')
    and Element-0 null baselines ('E0' or 'Fe0.5E00.5') into normalized atomic fractions.
    """
    cleaned = formula.strip().replace(" ", "")
    if not cleaned:
        raise ValueError("Formula string cannot be empty.")

    tokens = FORMULA_TOKEN_RE.findall(cleaned)
    reconstructed = "".join(sym + count for sym, count in tokens)
    if reconstructed != cleaned:
        raise ValueError(f"Unrecognized syntax in chemical formula: '{formula}'")

    raw_counts: Dict[str, float] = {}
    for sym, count_str in tokens:
        val = float(count_str) if count_str else 1.0
        if val < 0:
            raise ValueError(f"Negative stoichiometry not allowed for {sym}: {val}")
        raw_counts[sym] = raw_counts.get(sym, 0.0) + val

    total = sum(raw_counts.values())
    if total <= 0.0:
        raise ValueError("Total stoichiometric weight must be positive.")

    return {sym: count / total for sym, count in raw_counts.items()}


@dataclass(frozen=True)
class CompoundMetrics:
    formula: str
    stoichiometry_weights: Dict[str, float]
    element_angles_rad: Dict[str, float]
    element_pitch_12: Dict[str, float]
    modal_coherence: float              # C_theta in: resultant circular vector length
    mean_resultant_angle_rad: float     # circular mean direction
    angular_dispersion: float           # 1 - C_theta (circular variance)
    weighted_cosine_contrast: float     # weighted pairwise 1 - cos(theta_i - theta_j)
    high_dim_cosine_coherence: float    # ground-truth cosine similarity in full embedding space
    coherence_ci_95: Tuple[float, float]
    null_permutation_p_value: float
    is_null_baseline: bool


def evaluate_compound(
    formula: str,
    embedding: ElementalEmbedding,
    projection: CircularProjection,
    n_bootstrap: int = 300,
    n_permutations: int = 500,
    seed: int = 42,
) -> CompoundMetrics:
    """
    Compute data-driven circular coherence, full-space baseline coherence, bootstrap confidence
    intervals, and permutation p-values for any fractional stoichiometry.
    """
    rng = np.random.default_rng(seed)
    weights_map = parse_stoichiometry(formula)

    # Separate active physical elements from E0 null weight
    e0_weight = weights_map.get("E0", 0.0)
    active_items = [(sym, w) for sym, w in weights_map.items() if sym != "E0" and w > 0.0]

    if not active_items or e0_weight >= 1.0 - 1e-12:
        return CompoundMetrics(
            formula=formula,
            stoichiometry_weights=weights_map,
            element_angles_rad={"E0": 0.0},
            element_pitch_12={"E0": 0.0},
            modal_coherence=0.0,
            mean_resultant_angle_rad=0.0,
            angular_dispersion=1.0,
            weighted_cosine_contrast=0.0,
            high_dim_cosine_coherence=0.0,
            coherence_ci_95=(0.0, 0.0),
            null_permutation_p_value=1.0,
            is_null_baseline=True,
        )

    symbols = [s for s, _ in active_items]
    weights = np.array([w for _, w in active_items], dtype=np.float64)
    angles = np.array([projection.get_angle(s) for s in symbols], dtype=np.float64)

    # Resultant phasor sum scaled by active physical fraction (1 - e0_weight)
    phasors = weights * np.exp(1j * angles)
    resultant = np.sum(phasors)
    coherence = float(np.abs(resultant))
    mean_angle = float(np.mod(np.angle(resultant), 2.0 * np.pi))

    # Pairwise weighted circular contrast
    contrast = 0.0
    for i in range(len(symbols)):
        for j in range(i + 1, len(symbols)):
            contrast += 2.0 * weights[i] * weights[j] * (1.0 - np.cos(angles[i] - angles[j]))

    # Full-dimensional embedding coherence (centroid norm in L2 space)
    vecs = np.vstack([embedding.vectors[s] for s in symbols])
    centroid = np.sum(weights[:, None] * vecs, axis=0)
    high_dim_coh = float(np.linalg.norm(centroid))

    # Bootstrap CI over stoichiometric sampling noise (Dirichlet perturbation)
    if len(symbols) > 1 and n_bootstrap > 0:
        alpha = np.maximum(weights * 50.0, 0.5)
        boot_weights = rng.dirichlet(alpha, size=n_bootstrap) * (1.0 - e0_weight)
        boot_res = np.abs(boot_weights @ np.exp(1j * angles))
        ci_low, ci_high = float(np.percentile(boot_res, 2.5)), float(np.percentile(boot_res, 97.5))
    else:
        ci_low, ci_high = coherence, coherence

    # Permutation null test: sample random element angles from the periodic table
    all_pool_angles = np.array(
        [theta for sym, theta in projection.angles_rad.items() if sym != "E0"],
        dtype=np.float64,
    )
    if len(symbols) > 1 and n_permutations > 0 and len(all_pool_angles) >= len(symbols):
        exceed_count = 0
        for _ in range(n_permutations):
            rand_angles = rng.choice(all_pool_angles, size=len(symbols), replace=False)
            null_coh = float(np.abs(np.sum(weights * np.exp(1j * rand_angles))))
            if null_coh >= coherence - 1e-12:
                exceed_count += 1
        p_val = float((exceed_count + 1) / (n_permutations + 1))
    else:
        p_val = 1.0

    return CompoundMetrics(
        formula=formula,
        stoichiometry_weights=weights_map,
        element_angles_rad={s: projection.get_angle(s) for s in weights_map},
        element_pitch_12={s: projection.pitch_coords_12[s] for s in weights_map},
        modal_coherence=coherence,
        mean_resultant_angle_rad=mean_angle,
        angular_dispersion=float(max(0.0, 1.0 - coherence)),
        weighted_cosine_contrast=float(contrast),
        high_dim_cosine_coherence=high_dim_coh,
        coherence_ci_95=(ci_low, ci_high),
        null_permutation_p_value=p_val,
        is_null_baseline=(e0_weight > 0.0),
    )


def build_reproducibility_ledger_entry(
    metrics: CompoundMetrics,
    embedding: ElementalEmbedding,
    projection: CircularProjection,
    seed: int = 42,
    notes: str = "",
) -> Dict[str, Any]:
    """
    Generate a self-contained reproducibility ledger record with full provenance.
    """
    raw_vectors = {
        sym: np.round(embedding.vectors[sym], 8).tolist()
        for sym in metrics.stoichiometry_weights
    }
    return {
        "schema_version": "hte-observatory-ledger-v2",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "software_version": SOFTWARE_VERSION,
        "random_seed": seed,
        "provenance": {
            "embedding_name": embedding.metadata.name,
            "embedding_family": embedding.metadata.family,
            "embedding_sha256": embedding.metadata.sha256,
            "embedding_dimensions": embedding.metadata.dimensions,
            "projection_method": projection.method,
            "projection_pearson_r": round(projection.pearson_r, 6),
            "projection_pearson_p": projection.pearson_p_value,
            "projection_stress": round(projection.stress, 6),
            "variance_explained_2d": round(projection.variance_explained_2d, 6),
        },
        "compound": asdict(metrics),
        "raw_element_vectors": raw_vectors,
        "notes": notes,
    }
