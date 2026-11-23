from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold, KFold

from .embeddings import ElementalEmbedding
from .harmonic import evaluate_compound, parse_stoichiometry
from .projection import CircularProjection, project_to_circle_mds


@dataclass(frozen=True)
class BenchmarkDatasetItem:
    formula: str
    target_value: float
    chemical_family: str  # e.g., "perovskite", "spinel", "chalcogenide", "intermetallic"


@dataclass(frozen=True)
class ValidationReport:
    embedding_name: str
    embedding_sha256: str
    target_property: str
    random_seed: int
    projection_pearson_r: float
    # Predictive benchmarks (MAE & R^2)
    circular_features_mae: float
    circular_features_r2: float
    full_embedding_baseline_mae: float
    full_embedding_baseline_r2: float
    ablation_shuffled_circle_mae: float
    ablation_shuffled_circle_r2: float
    # Leave-one-family-out cross-validation
    family_cv_mae: float
    family_cv_r2: float
    # Null model comparison on coherence vs target correlation
    coherence_target_spearman_r: float
    coherence_target_p_value: float
    null_random_angles_spearman_r: float
    # Explicit scientific audit flags (never hides negative/null outcomes)
    circular_retains_signal_vs_shuffled: bool
    circular_degradation_vs_full_mae: float
    summary_verdict: str

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


def _featurize_circular(
    formulas: List[str],
    projection: CircularProjection,
) -> np.ndarray:
    """
    Extract stoichiometry-weighted circular coordinates:
    [sum(w_i cos theta_i), sum(w_i sin theta_i), C_theta, weighted_contrast]
    """
    rows: List[List[float]] = []
    for f in formulas:
        w_map = parse_stoichiometry(f)
        cx = sum(w * np.cos(projection.get_angle(s)) for s, w in w_map.items() if s != "E0")
        sy = sum(w * np.sin(projection.get_angle(s)) for s, w in w_map.items() if s != "E0")
        coh = float(np.hypot(cx, sy))
        rows.append([cx, sy, coh, 1.0 - coh])
    return np.asarray(rows, dtype=np.float64)


def _featurize_full_embedding(
    formulas: List[str],
    embedding: ElementalEmbedding,
) -> np.ndarray:
    """
    Strong composition-only baseline: stoichiometry-weighted mean + std pooling
    over full-dimensional elemental vectors (Magpie/mat2vec style).
    """
    rows: List[np.ndarray] = []
    for f in formulas:
        w_map = parse_stoichiometry(f)
        active = [(s, w) for s, w in w_map.items() if s != "E0"]
        if not active:
            dim = embedding.metadata.dimensions
            rows.append(np.zeros(dim * 2, dtype=np.float64))
            continue
        vecs = np.vstack([embedding.vectors[s] for s, _ in active])
        weights = np.array([w for _, w in active], dtype=np.float64)
        weights = weights / np.sum(weights)
        mean_vec = np.sum(weights[:, None] * vecs, axis=0)
        var_vec = np.sum(weights[:, None] * ((vecs - mean_vec) ** 2), axis=0)
        rows.append(np.concatenate([mean_vec, np.sqrt(var_vec)]))
    return np.vstack(rows)


def run_validation_suite(
    embedding: ElementalEmbedding,
    dataset: List[BenchmarkDatasetItem],
    target_property: str = "formation_energy_eV_atom",
    seed: int = 42,
) -> ValidationReport:
    """
    Run pre-registered statistical & predictive validation:
    1. Circular 2D representation vs. full-dimensional composition baseline
    2. Ablation test with randomly permuted circular assignments
    3. Leave-one-chemical-family-out cross-validation
    4. Null correlation audit (always reports negative/null findings transparently)
    """
    if len(dataset) < 6:
        raise ValueError("Validation suite requires at least 6 benchmark compounds.")

    rng = np.random.default_rng(seed)
    projection = project_to_circle_mds(embedding)

    formulas = [d.formula for d in dataset]
    y = np.array([d.target_value for d in dataset], dtype=np.float64)
    families = np.array([d.chemical_family for d in dataset])

    X_circ = _featurize_circular(formulas, projection)
    X_full = _featurize_full_embedding(formulas, embedding)

    # Ablation: destroy circular topology by permuting elemental angles
    all_syms = list(projection.angles_rad.keys())
    shuffled_vals = rng.permutation([projection.angles_rad[s] for s in all_syms])
    shuffled_angles = dict(zip(all_syms, shuffled_vals))
    shuffled_proj = CircularProjection(
        embedding_name=projection.embedding_name + "_shuffled",
        embedding_sha256=projection.embedding_sha256,
        method="random_angle_ablation",
        angles_rad=shuffled_angles,
        pitch_coords_12={s: (6.0 / np.pi) * a for s, a in shuffled_angles.items()},
        coordinates_2d=projection.coordinates_2d,
        pearson_r=0.0,
        pearson_p_value=1.0,
        stress=1.0,
        variance_explained_2d=0.0,
    )
    X_ablation = _featurize_circular(formulas, shuffled_proj)

    def _eval_cv(X: np.ndarray, splitter) -> Tuple[float, float]:
        preds = np.zeros_like(y)
        for train_idx, test_idx in splitter:
            model = Ridge(alpha=1.0)
            model.fit(X[train_idx], y[train_idx])
            preds[test_idx] = model.predict(X[test_idx])
        return float(mean_absolute_error(y, preds)), float(r2_score(y, preds))

    n_splits = min(5, len(dataset))
    kf = list(KFold(n_splits=n_splits, shuffle=True, random_state=seed).split(X_circ))

    circ_mae, circ_r2 = _eval_cv(X_circ, kf)
    full_mae, full_r2 = _eval_cv(X_full, kf)
    abl_mae, abl_r2 = _eval_cv(X_ablation, kf)

    # Leave-one-chemical-family-out cross-validation
    unique_families = np.unique(families)
    if len(unique_families) >= 2:
        gkf = list(GroupKFold(n_splits=len(unique_families)).split(X_circ, y, groups=families))
        fam_mae, fam_r2 = _eval_cv(X_circ, gkf)
    else:
        fam_mae, fam_r2 = circ_mae, circ_r2

    # Spearman correlation between circular coherence and target property
    coherences = X_circ[:, 2]
    null_coherences = X_ablation[:, 2]
    sp_res = spearmanr(coherences, y)
    null_sp_res = spearmanr(null_coherences, y)

    sp_r = float(sp_res.statistic) if not np.isnan(sp_res.statistic) else 0.0
    sp_p = float(sp_res.pvalue) if not np.isnan(sp_res.pvalue) else 1.0
    null_sp_r = float(null_sp_res.statistic) if not np.isnan(null_sp_res.statistic) else 0.0

    retains_signal = bool(circ_mae < abl_mae * 0.95 and circ_r2 > abl_r2)
    degradation = float(circ_mae - full_mae)

    if not retains_signal:
        verdict = (
            f"NULL/NEGATIVE RESULT: 2D circular projection of {embedding.metadata.name} "
            f"(r_proj={projection.pearson_r:.2f}) did not significantly outperform random angle "
            f"assignment on {target_property} (MAE {circ_mae:.3f} vs shuffled {abl_mae:.3f})."
        )
    else:
        verdict = (
            f"VALIDATED SIGNAL: Circular projection retains predictive signal over random angles "
            f"(MAE {circ_mae:.3f} vs {abl_mae:.3f}), with {degradation:+.3f} MAE compression cost "
            f"relative to full {embedding.metadata.dimensions}D baseline ({full_mae:.3f})."
        )

    return ValidationReport(
        embedding_name=embedding.metadata.name,
        embedding_sha256=embedding.metadata.sha256,
        target_property=target_property,
        random_seed=seed,
        projection_pearson_r=projection.pearson_r,
        circular_features_mae=circ_mae,
        circular_features_r2=circ_r2,
        full_embedding_baseline_mae=full_mae,
        full_embedding_baseline_r2=full_r2,
        ablation_shuffled_circle_mae=abl_mae,
        ablation_shuffled_circle_r2=abl_r2,
        family_cv_mae=fam_mae,
        family_cv_r2=fam_r2,
        coherence_target_spearman_r=sp_r,
        coherence_target_p_value=sp_p,
        null_random_angles_spearman_r=null_sp_r,
        circular_retains_signal_vs_shuffled=retains_signal,
        circular_degradation_vs_full_mae=degradation,
        summary_verdict=verdict,
    )
