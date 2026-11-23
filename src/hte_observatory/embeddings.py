from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import numpy as np

PERIODIC_SYMBOLS: List[str] = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
]


@dataclass(frozen=True)
class EmbeddingMetadata:
    name: str
    family: str  # e.g., "property-based", "nlp-literature", "structure-graph", "chemical-scale", "custom"
    description: str
    strengths: str
    limitations: str
    source_citation: str = ""
    sha256: str = ""
    dimensions: int = 0
    element_count: int = 0


@dataclass
class ElementalEmbedding:
    metadata: EmbeddingMetadata
    vectors: Dict[str, np.ndarray] = field(default_factory=dict)

    def __post_init__(self) -> None:
        normalized: Dict[str, np.ndarray] = {}
        dim: Optional[int] = None

        for symbol, vec in self.vectors.items():
            clean_sym = symbol.strip()
            arr = np.asarray(vec, dtype=np.float64).ravel()
            if dim is None:
                dim = arr.shape[0]
            elif arr.shape[0] != dim:
                raise ValueError(
                    f"Dimension mismatch for {clean_sym}: expected {dim}, got {arr.shape[0]}"
                )

            norm = np.linalg.norm(arr)
            if clean_sym == "E0" or norm == 0.0:
                normalized[clean_sym] = np.zeros(dim, dtype=np.float64)
            else:
                normalized[clean_sym] = arr / norm

        if dim is None:
            raise ValueError("Embedding cannot be empty.")

        # Always guarantee Element-0 (E0) exists as an explicit zero-vector null baseline
        if "E0" not in normalized:
            normalized["E0"] = np.zeros(dim, dtype=np.float64)

        self.vectors = normalized
        object.__setattr__(
            self,
            "metadata",
            EmbeddingMetadata(
                name=self.metadata.name,
                family=self.metadata.family,
                description=self.metadata.description,
                strengths=self.metadata.strengths,
                limitations=self.metadata.limitations,
                source_citation=self.metadata.source_citation,
                sha256=self._compute_sha256(),
                dimensions=dim,
                element_count=len([k for k in normalized if k != "E0"]),
            ),
        )

    def _compute_sha256(self) -> str:
        hasher = hashlib.sha256()
        for sym in sorted(self.vectors.keys()):
            hasher.update(sym.encode("utf-8"))
            hasher.update(np.round(self.vectors[sym], 10).tobytes())
        return hasher.hexdigest()

    def get_matrix(self, include_e0: bool = False) -> Tuple[List[str], np.ndarray]:
        symbols = sorted(
            [s for s in self.vectors.keys() if include_e0 or s != "E0"],
            key=lambda s: (
                0 if s == "E0" else 1,
                PERIODIC_SYMBOLS.index(s) if s in PERIODIC_SYMBOLS else 999,
                s,
            ),
        )
        matrix = np.vstack([self.vectors[s] for s in symbols])
        return symbols, matrix

    def cosine_similarity(self, el_a: str, el_b: str) -> float:
        if el_a == "E0" or el_b == "E0":
            return 0.0
        va = self.vectors[el_a]
        vb = self.vectors[el_b]
        return float(np.clip(np.dot(va, vb), -1.0, 1.0))


def load_embedding_from_json(path: str | Path) -> ElementalEmbedding:
    p = Path(path)
    raw = json.loads(p.read_text(encoding="utf-8"))

    if "vectors" in raw and "metadata" in raw:
        meta_raw = raw["metadata"]
        meta = EmbeddingMetadata(
            name=meta_raw.get("name", p.stem),
            family=meta_raw.get("family", "custom"),
            description=meta_raw.get("description", "User-provided JSON embedding."),
            strengths=meta_raw.get("strengths", "Custom domain representation."),
            limitations=meta_raw.get("limitations", "Unverified external matrix."),
            source_citation=meta_raw.get("source_citation", str(p.name)),
        )
        vectors = {k: np.asarray(v, dtype=np.float64) for k, v in raw["vectors"].items()}
    else:
        meta = EmbeddingMetadata(
            name=p.stem,
            family="custom",
            description="Flat dictionary JSON elemental embedding.",
            strengths="Direct drop-in custom embedding.",
            limitations="Metadata not supplied in file.",
            source_citation=str(p.name),
        )
        vectors = {k: np.asarray(v, dtype=np.float64) for k, v in raw.items()}

    return ElementalEmbedding(metadata=meta, vectors=vectors)


def load_embedding_from_csv(
    path: str | Path,
    name: Optional[str] = None,
    family: str = "custom",
    description: str = "User-provided CSV elemental embedding.",
) -> ElementalEmbedding:
    p = Path(path)
    vectors: Dict[str, np.ndarray] = {}

    with p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if r and any(cell.strip() for cell in r)]

    if not rows:
        raise ValueError(f"CSV file {p} is empty.")

    # Detect header row if second column cannot be parsed as float
    start_idx = 0
    try:
        float(rows[0][1])
    except (ValueError, IndexError):
        start_idx = 1

    for row in rows[start_idx:]:
        sym = row[0].strip()
        if not sym:
            continue
        vals = [float(x) for x in row[1:] if x.strip() != ""]
        vectors[sym] = np.asarray(vals, dtype=np.float64)

    meta = EmbeddingMetadata(
        name=name or p.stem,
        family=family,
        description=description,
        strengths="Drop-in tabular elemental feature matrix.",
        limitations="Requires validation against domain benchmarks.",
        source_citation=str(p.name),
    )
    return ElementalEmbedding(metadata=meta, vectors=vectors)
