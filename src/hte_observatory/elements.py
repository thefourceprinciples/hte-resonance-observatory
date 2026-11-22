"""Canonical element table for HTE mapping (v0.3 — Physical Calibration).

Attaches IUPAC group, period, block, active valence electrons, and Pauling
electronegativity (chi) for Z = 0..118 while preserving full backward
compatibility with ELEMENT_Z, atomic_number(), and element_coordinates().
"""

from dataclasses import dataclass

# (Z, IUPAC Group 1..18, Period 1..7, Block, Valence Electrons, Pauling Electronegativity chi)
# Note: Synthetic superheavy elements (Z >= 104) use group-extrapolated reference estimates.
ELEMENT_TABLE: dict[str, tuple[int, int, int, str, int, float]] = {
    "E0": (0, 0, 0, "substrate", 0, 0.00),
    "H": (1, 1, 1, "s", 1, 2.20), "He": (2, 18, 1, "s", 2, 0.00),
    "Li": (3, 1, 2, "s", 1, 0.98), "Be": (4, 2, 2, "s", 2, 1.57),
    "B": (5, 13, 2, "p", 3, 2.04), "C": (6, 14, 2, "p", 4, 2.55),
    "N": (7, 15, 2, "p", 5, 3.04), "O": (8, 16, 2, "p", 6, 3.44),
    "F": (9, 17, 2, "p", 7, 3.98), "Ne": (10, 18, 2, "p", 8, 0.00),
    "Na": (11, 1, 3, "s", 1, 0.93), "Mg": (12, 2, 3, "s", 2, 1.31),
    "Al": (13, 13, 3, "p", 3, 1.61), "Si": (14, 14, 3, "p", 4, 1.90),
    "P": (15, 15, 3, "p", 5, 2.19), "S": (16, 16, 3, "p", 6, 2.58),
    "Cl": (17, 17, 3, "p", 7, 3.16), "Ar": (18, 18, 3, "p", 8, 0.00),
    "K": (19, 1, 4, "s", 1, 0.82), "Ca": (20, 2, 4, "s", 2, 1.00),
    "Sc": (21, 3, 4, "d", 3, 1.36), "Ti": (22, 4, 4, "d", 4, 1.54),
    "V": (23, 5, 4, "d", 5, 1.63), "Cr": (24, 6, 4, "d", 6, 1.66),
    "Mn": (25, 7, 4, "d", 7, 1.55), "Fe": (26, 8, 4, "d", 8, 1.83),
    "Co": (27, 9, 4, "d", 9, 1.88), "Ni": (28, 10, 4, "d", 10, 1.91),
    "Cu": (29, 11, 4, "d", 11, 1.90), "Zn": (30, 12, 4, "d", 2, 1.65),
    "Ga": (31, 13, 4, "p", 3, 1.81), "Ge": (32, 14, 4, "p", 4, 2.01),
    "As": (33, 15, 4, "p", 5, 2.18), "Se": (34, 16, 4, "p", 6, 2.55),
    "Br": (35, 17, 4, "p", 7, 2.96), "Kr": (36, 18, 4, "p", 8, 3.00),
    "Rb": (37, 1, 5, "s", 1, 0.82), "Sr": (38, 2, 5, "s", 2, 0.95),
    "Y": (39, 3, 5, "d", 3, 1.22), "Zr": (40, 4, 5, "d", 4, 1.33),
    "Nb": (41, 5, 5, "d", 5, 1.60), "Mo": (42, 6, 5, "d", 6, 2.16),
    "Tc": (43, 7, 5, "d", 7, 1.90), "Ru": (44, 8, 5, "d", 8, 2.20),
    "Rh": (45, 9, 5, "d", 9, 2.28), "Pd": (46, 10, 5, "d", 10, 2.20),
    "Ag": (47, 11, 5, "d", 11, 1.93), "Cd": (48, 12, 5, "d", 2, 1.69),
    "In": (49, 13, 5, "p", 3, 1.78), "Sn": (50, 14, 5, "p", 4, 1.96),
    "Sb": (51, 15, 5, "p", 5, 2.05), "Te": (52, 16, 5, "p", 6, 2.10),
    "I": (53, 17, 5, "p", 7, 2.66), "Xe": (54, 18, 5, "p", 8, 2.60),
    "Cs": (55, 1, 6, "s", 1, 0.79), "Ba": (56, 2, 6, "s", 2, 0.89),
    "La": (57, 3, 6, "f", 3, 1.10), "Ce": (58, 3, 6, "f", 4, 1.12),
    "Pr": (59, 3, 6, "f", 3, 1.13), "Nd": (60, 3, 6, "f", 3, 1.14),
    "Pm": (61, 3, 6, "f", 3, 1.13), "Sm": (62, 3, 6, "f", 3, 1.17),
    "Eu": (63, 3, 6, "f", 2, 1.20), "Gd": (64, 3, 6, "f", 3, 1.20),
    "Tb": (65, 3, 6, "f", 3, 1.10), "Dy": (66, 3, 6, "f", 3, 1.22),
    "Ho": (67, 3, 6, "f", 3, 1.23), "Er": (68, 3, 6, "f", 3, 1.24),
    "Tm": (69, 3, 6, "f", 3, 1.25), "Yb": (70, 3, 6, "f", 2, 1.10),
    "Lu": (71, 3, 6, "f", 3, 1.27), "Hf": (72, 4, 6, "d", 4, 1.30),
    "Ta": (73, 5, 6, "d", 5, 1.50), "W": (74, 6, 6, "d", 6, 2.36),
    "Re": (75, 7, 6, "d", 7, 1.90), "Os": (76, 8, 6, "d", 8, 2.20),
    "Ir": (77, 9, 6, "d", 9, 2.20), "Pt": (78, 10, 6, "d", 10, 2.28),
    "Au": (79, 11, 6, "d", 11, 2.54), "Hg": (80, 12, 6, "d", 2, 2.00),
    "Tl": (81, 13, 6, "p", 3, 1.62), "Pb": (82, 14, 6, "p", 4, 2.33),
    "Bi": (83, 15, 6, "p", 5, 2.02), "Po": (84, 16, 6, "p", 6, 2.00),
    "At": (85, 17, 6, "p", 7, 2.20), "Rn": (86, 18, 6, "p", 8, 2.20),
    "Fr": (87, 1, 7, "s", 1, 0.70), "Ra": (88, 2, 7, "s", 2, 0.90),
    "Ac": (89, 3, 7, "f", 3, 1.10), "Th": (90, 3, 7, "f", 4, 1.30),
    "Pa": (91, 3, 7, "f", 5, 1.50), "U": (92, 3, 7, "f", 6, 1.38),
    "Np": (93, 3, 7, "f", 5, 1.36), "Pu": (94, 3, 7, "f", 4, 1.28),
    "Am": (95, 3, 7, "f", 3, 1.13), "Cm": (96, 3, 7, "f", 3, 1.28),
    "Bk": (97, 3, 7, "f", 3, 1.30), "Cf": (98, 3, 7, "f", 3, 1.30),
    "Es": (99, 3, 7, "f", 3, 1.30), "Fm": (100, 3, 7, "f", 3, 1.30),
    "Md": (101, 3, 7, "f", 3, 1.30), "No": (102, 3, 7, "f", 2, 1.30),
    "Lr": (103, 3, 7, "f", 3, 1.30), "Rf": (104, 4, 7, "d", 4, 1.30),
    "Db": (105, 5, 7, "d", 5, 1.50), "Sg": (106, 6, 7, "d", 6, 1.90),
    "Bh": (107, 7, 7, "d", 7, 1.90), "Hs": (108, 8, 7, "d", 8, 2.00),
    "Mt": (109, 9, 7, "d", 9, 2.00), "Ds": (110, 10, 7, "d", 10, 2.00),
    "Rg": (111, 11, 7, "d", 11, 2.20), "Cn": (112, 12, 7, "d", 2, 2.00),
    "Nh": (113, 13, 7, "p", 3, 1.80), "Fl": (114, 14, 7, "p", 4, 2.00),
    "Mc": (115, 15, 7, "p", 5, 1.90), "Lv": (116, 16, 7, "p", 6, 2.00),
    "Ts": (117, 17, 7, "p", 7, 2.20), "Og": (118, 18, 7, "p", 8, 2.20),
}

# Backward-compatible symbol -> atomic number mapping
ELEMENT_Z: dict[str, int] = {sym: meta[0] for sym, meta in ELEMENT_TABLE.items()}

PITCH_NAMES: tuple[str, ...] = (
    "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"
)


@dataclass(frozen=True)
class ElementCoordinates:
    symbol: str
    Z: int
    group: int
    period: int
    block: str
    valence: int
    electronegativity: float
    pi_raw: int
    pi_group: int
    omega: int


def atomic_number(symbol: str) -> int:
    """Return atomic number for a symbol or raise a clear error."""
    try:
        return ELEMENT_Z[symbol]
    except KeyError as exc:
        raise ValueError(f"Unknown element symbol: {symbol}") from exc


def element_coordinates(symbol: str) -> ElementCoordinates:
    """Return full HTE octave-lattice, periodic group-phase, and physical coordinates."""
    if symbol not in ELEMENT_TABLE:
        raise ValueError(f"Unknown element symbol: {symbol}")
    z, grp, per, blk, val, chi = ELEMENT_TABLE[symbol]
    pi_raw = z % 12
    pi_group = 0 if grp == 0 else int(round(((grp - 1) * 12) / 18.0)) % 12
    omega = z // 12
    return ElementCoordinates(
        symbol=symbol,
        Z=z,
        group=grp,
        period=per,
        block=blk,
        valence=val,
        electronegativity=chi,
        pi_raw=pi_raw,
        pi_group=pi_group,
        omega=omega,
    )
