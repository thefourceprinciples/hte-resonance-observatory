from __future__ import annotations

import csv
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Mapping, Sequence
import numpy as np

PERIODIC_SYMBOLS: tuple[str, ...] = (
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
)

VALID_SYMBOLS = frozenset(PERIODIC_SYMBOLS) | {"E0"}


@dataclass
class EmbeddingMetadata:
    name: str
    family: str = "custom"
    description: str = ""
    strengths: str = ""
    limitations: str = ""
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
        dim: int | None = None

        for raw_sym, raw_vec in self.vectors.items():
            sym = raw_sym.strip()
            if sym not in VALID_SYMBOLS:
                continue
            arr = np.asarray(raw_vec, dtype=np.float64).ravel()
            if arr.size == 0:
                continue
            if dim is None:
                dim = int(arr.size)
            elif int(arr.size) != dim:
                raise ValueError(f"Dimension mismatch for {sym}: expected {dim}, got {arr.size}.")

            norm = float(np.linalg.norm(arr))
            if sym == "E0" or norm <= 1e-12:
                normalized[sym] = np.zeros(dim, dtype=np.float64)
            else:
                normalized[sym] = arr / norm

        if dim is None:
            raise ValueError("ElementalEmbedding requires at least one valid numeric vector.")

        if "E0" not in normalized:
            normalized["E0"] = np.zeros(dim, dtype=np.float64)

        self.vectors = normalized
        self.metadata.dimensions = dim
        self.metadata.element_count = len([s for s in normalized if s != "E0"])

        canonical = json.dumps(
            {k: np.round(v, 8).tolist() for k, v in sorted(normalized.items())},
            separators=(",", ":"),
        )
        self.metadata.sha256 = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    @property
    def symbols(self) -> List[str]:
        """Ordered list of active non-null element symbols."""
        order_map = {s: i for i, s in enumerate(PERIODIC_SYMBOLS)}
        return sorted(
            [s for s in self.vectors if s != "E0"],
            key=lambda s: order_map.get(s, 999),
        )

    @property
    def matrix(self) -> np.ndarray:
        """2D numpy array of shape (len(self.symbols), dimensions) aligned with self.symbols."""
        return np.vstack([self.vectors[s] for s in self.symbols])

    def get_vector(self, symbol: str) -> np.ndarray:
        if symbol not in self.vectors:
            raise KeyError(f"Element '{symbol}' not found in embedding '{self.metadata.name}'.")
        return self.vectors[symbol]

    def cosine_similarity(self, sym_a: str, sym_b: str) -> float:
        va = self.get_vector(sym_a)
        vb = self.get_vector(sym_b)
        return float(np.clip(np.dot(va, vb), -1.0, 1.0))


def load_embedding_from_csv(
    path: str | Path,
    name: str | None = None,
    family: str = "custom",
    description: str = "",
) -> ElementalEmbedding:
    p = Path(path)
    raw: Dict[str, Sequence[float]] = {}
    with p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or not row[0].strip():
                continue
            sym = row[0].strip()
            if sym not in VALID_SYMBOLS:
                continue
            raw[sym] = [float(x) for x in row[1:] if x.strip() != ""]

    meta = EmbeddingMetadata(
        name=name or p.stem,
        family=family,
        description=description or f"Loaded from {p.name}.",
        source_citation=p.name,
    )
    return ElementalEmbedding(metadata=meta, vectors={k: np.array(v, dtype=np.float64) for k, v in raw.items()})


def load_embedding_from_json(path: str | Path) -> ElementalEmbedding:
    p = Path(path)
    payload = json.loads(p.read_text(encoding="utf-8"))
    if "vectors" in payload and isinstance(payload["vectors"], Mapping):
        meta_dict = payload.get("metadata", {})
        vec_dict = payload["vectors"]
    else:
        meta_dict = {}
        vec_dict = payload

    meta = EmbeddingMetadata(
        name=str(meta_dict.get("name", p.stem)),
        family=str(meta_dict.get("family", "custom")),
        description=str(meta_dict.get("description", f"Loaded from {p.name}.")),
        strengths=str(meta_dict.get("strengths", "")),
        limitations=str(meta_dict.get("limitations", "")),
        source_citation=str(meta_dict.get("source_citation", p.name)),
    )
    return ElementalEmbedding(
        metadata=meta,
        vectors={str(k): np.array(v, dtype=np.float64) for k, v in vec_dict.items()},
    )
