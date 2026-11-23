from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List
import numpy as np
from scipy.stats import pearsonr

from .embeddings import ElementalEmbedding


@dataclass(frozen=True)
class CircularProjection:
    embedding_name: str
    embedding_sha256: str
    method: str
    angles_rad: Dict[str, float]          # theta in [0, 2*pi)
    pitch_coords_12: Dict[str, float]     # continuous 0-12 mapping: (6/pi)*theta
    coordinates_2d: Dict[str, List[float]]
    pearson_r: float                      # correlation(cos_sim_orig, cos(delta_theta))
    pearson_p_value: float
    stress: float                         # normalized Kruskal stress-1 on angular chord distances
    variance_explained_2d: float          # fraction of positive MDS eigenvalue energy captured

    def get_angle(self, symbol: str) -> float:
        if symbol not in self.angles_rad:
            raise KeyError(f"Element '{symbol}' not present in projection '{self.embedding_name}'.")
        return self.angles_rad[symbol]


def project_to_circle_mds(embedding: ElementalEmbedding) -> CircularProjection:
    """
    Project L2-normalized elemental embeddings onto S^1 via Classical MDS on cosine distances,
    followed by atan2 angular extraction and Pearson similarity preservation audit.
    """
    symbols, X = embedding.get_matrix(include_e0=False)
    n = len(symbols)
    if n < 3:
        raise ValueError("At least 3 elements are required for 2D circular MDS projection.")

    # Pairwise cosine similarity S and cosine distance D = 1 - S
    S = np.clip(X @ X.T, -1.0, 1.0)
    np.fill_diagonal(S, 1.0)
    D = np.maximum(0.0, 1.0 - S)

    # Classical MDS double-centering on squared distances
    D2 = D ** 2
    H = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * (H @ D2 @ H)

    eigvals, eigvecs = np.linalg.eigh(B)
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    pos_eigvals = np.maximum(eigvals, 0.0)
    total_energy = float(np.sum(pos_eigvals)) or 1.0
    var_explained = float((pos_eigvals[0] + pos_eigvals[1]) / total_energy)

    # Top 2 principal coordinates
    top2_vals = np.maximum(eigvals[:2], 1e-12)
    coords = eigvecs[:, :2] * np.sqrt(top2_vals)

    # Deterministic sign convention: align max-norm element to positive x-axis
    anchor_idx = int(np.argmax(np.linalg.norm(coords, axis=1)))
    anchor_angle = np.arctan2(coords[anchor_idx, 1], coords[anchor_idx, 0])
    rot = np.array([
        [np.cos(-anchor_angle), -np.sin(-anchor_angle)],
        [np.sin(-anchor_angle),  np.cos(-anchor_angle)],
    ])
    coords = coords @ rot.T

    angles = np.mod(np.arctan2(coords[:, 1], coords[:, 0]), 2.0 * np.pi)

    # Audit projection fidelity on upper-triangular pairs (i < j)
    iu = np.triu_indices(n, k=1)
    orig_sim = S[iu]
    delta_theta = angles[iu[0]] - angles[iu[1]]
    circ_sim = np.cos(delta_theta)

    if np.std(orig_sim) < 1e-12 or np.std(circ_sim) < 1e-12:
        r_val, p_val = 0.0, 1.0
    else:
        res = pearsonr(orig_sim, circ_sim)
        r_val, p_val = float(res.statistic), float(res.pvalue)

    # Normalized chord distance stress
    d_orig = 1.0 - orig_sim
    d_circ = 1.0 - circ_sim
    denom = float(np.sum(d_orig ** 2)) or 1.0
    stress = float(np.sqrt(np.sum((d_orig - d_circ) ** 2) / denom))

    angles_dict: Dict[str, float] = {"E0": 0.0}
    pitch_dict: Dict[str, float] = {"E0": 0.0}
    coords_dict: Dict[str, List[float]] = {"E0": [0.0, 0.0]}

    for sym, theta, xy in zip(symbols, angles, coords):
        t = float(theta)
        angles_dict[sym] = t
        pitch_dict[sym] = float((6.0 / np.pi) * t)
        coords_dict[sym] = [float(xy[0]), float(xy[1])]

    return CircularProjection(
        embedding_name=embedding.metadata.name,
        embedding_sha256=embedding.metadata.sha256,
        method="classical_mds_cosine_atan2",
        angles_rad=angles_dict,
        pitch_coords_12=pitch_dict,
        coordinates_2d=coords_dict,
        pearson_r=r_val,
        pearson_p_value=p_val,
        stress=stress,
        variance_explained_2d=var_explained,
    )
