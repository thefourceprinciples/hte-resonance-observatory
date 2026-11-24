from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple
import numpy as np
from scipy.stats import pearsonr
from .embeddings import ElementalEmbedding


@dataclass(frozen=True)
class CircularProjection:
    """
    2D Classical MDS projection of an ElementalEmbedding onto S^1 (theta in [0, 2*pi)),
    paired with explicit pairwise similarity fidelity diagnostics.
    """
    embedding_name: str
    embedding_sha256: str
    method: str
    angles_rad: Dict[str, float]
    pitch_coords_12: Dict[str, float]
    coordinates_2d: Dict[str, Tuple[float, float]]
    pearson_r: float
    pearson_p_value: float
    stress: float
    variance_explained_2d: float

    def get_angle(self, symbol: str) -> float:
        if symbol not in self.angles_rad:
            raise KeyError(f"Element '{symbol}' not present in projection '{self.embedding_name}'.")
        return self.angles_rad[symbol]

    def get_continuous_pitch(self, symbol: str) -> float:
        """Continuous [0, 12) bridge coordinate p_i = (6/pi) * theta_i for downstream sonification."""
        if symbol not in self.pitch_coords_12:
            raise KeyError(f"Element '{symbol}' not present in projection '{self.embedding_name}'.")
        return self.pitch_coords_12[symbol]


def project_to_circle_mds(
    embedding: ElementalEmbedding,
    anchor_symbol: str | None = None,
) -> CircularProjection:
    """
    Project L2-normalized elemental vectors onto S^1 via Classical Multidimensional Scaling (MDS)
    on cosine dissimilarities d_ij = 1 - (v_i . v_j).
    """
    symbols = embedding.symbols
    n = len(symbols)
    if n < 3:
        raise ValueError(f"At least 3 non-null elements are required for 2D MDS projection; got {n}.")

    mat = embedding.matrix  # shape (n, d), L2-normalized rows
    sim_matrix = np.clip(mat @ mat.T, -1.0, 1.0)
    dist_matrix = np.maximum(0.0, 1.0 - sim_matrix)

    # Classical MDS double-centering of squared distance matrix
    d_sq = dist_matrix ** 2
    row_means = d_sq.mean(axis=1, keepdims=True)
    col_means = d_sq.mean(axis=0, keepdims=True)
    grand_mean = d_sq.mean()
    gram = -0.5 * (d_sq - row_means - col_means + grand_mean)

    eigvals, eigvecs = np.linalg.eigh(gram)
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    pos_eigvals = np.maximum(eigvals, 0.0)
    total_var = float(pos_eigvals.sum())
    var_2d = float((pos_eigvals[0] + pos_eigvals[1]) / total_var) if total_var > 0.0 else 0.0

    coords = np.zeros((n, 2), dtype=np.float64)
    for k in range(min(2, n)):
        scale = np.sqrt(max(eigvals[k], 1e-12))
        coords[:, k] = eigvecs[:, k] * scale

    # Deterministic orientation anchoring (removes arbitrary orthogonal sign/rotation ambiguity)
    if anchor_symbol is not None and anchor_symbol in symbols:
        anchor_idx = symbols.index(anchor_symbol)
    else:
        radii = np.linalg.norm(coords, axis=1)
        anchor_idx = int(np.argmax(radii))

    anchor_angle = float(np.arctan2(coords[anchor_idx, 1], coords[anchor_idx, 0]))
    cos_a, sin_a = np.cos(-anchor_angle), np.sin(-anchor_angle)
    rot = np.array([[cos_a, -sin_a], [sin_a, cos_a]], dtype=np.float64)
    coords_rot = coords @ rot.T

    # Wrap angles strictly into [0, 2*pi) with floating-point boundary guard
    angles_rad = np.mod(np.arctan2(coords_rot[:, 1], coords_rot[:, 0]), 2.0 * np.pi)
    angles_rad = np.where(np.isclose(angles_rad, 2.0 * np.pi, atol=1e-12), 0.0, angles_rad)

    # Fidelity audit: compare high-D cosine similarity vs. circular similarity cos(theta_i - theta_j)
    tri_idx = np.triu_indices(n, k=1)
    orig_sim_pairs = sim_matrix[tri_idx]
    circ_sim_matrix = np.cos(angles_rad[:, None] - angles_rad[None, :])
    circ_sim_pairs = circ_sim_matrix[tri_idx]

    if orig_sim_pairs.size >= 2 and np.std(orig_sim_pairs) > 1e-12 and np.std(circ_sim_pairs) > 1e-12:
        r_val, p_val = pearsonr(orig_sim_pairs, circ_sim_pairs)
        pearson_r = float(r_val)
        pearson_p = float(p_val)
    else:
        pearson_r, pearson_p = 0.0, 1.0

    orig_dist_pairs = 1.0 - orig_sim_pairs
    circ_dist_pairs = 1.0 - circ_sim_pairs
    denom = float(np.sum(orig_dist_pairs ** 2))
    stress = float(np.sqrt(np.sum((orig_dist_pairs - circ_dist_pairs) ** 2) / denom)) if denom > 0.0 else 0.0

    # Inject Element-0 null baseline at theta = 0.0
    angles_dict: Dict[str, float] = {"E0": 0.0}
    pitch_dict: Dict[str, float] = {"E0": 0.0}
    coords_dict: Dict[str, Tuple[float, float]] = {"E0": (0.0, 0.0)}

    for idx, sym in enumerate(symbols):
        theta = float(angles_rad[idx])
        angles_dict[sym] = theta
        pitch_dict[sym] = float((6.0 / np.pi) * theta)
        coords_dict[sym] = (float(coords_rot[idx, 0]), float(coords_rot[idx, 1]))

    return CircularProjection(
        embedding_name=embedding.metadata.name,
        embedding_sha256=embedding.metadata.sha256,
        method="classical_mds_cosine",
        angles_rad=angles_dict,
        pitch_coords_12=pitch_dict,
        coordinates_2d=coords_dict,
        pearson_r=pearson_r,
        pearson_p_value=pearson_p,
        stress=stress,
        variance_explained_2d=var_2d,
    )
