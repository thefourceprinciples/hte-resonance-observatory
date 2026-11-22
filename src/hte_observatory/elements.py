"""Canonical element table for HTE mapping (v0.2).

Extends v0.1 through Og (Z=118) + Element-0 (E0) substrate, attaching IUPAC
group, period, block, octave index omega(Z), and periodic group-phase pi_group(Z)
while keeping ELEMENT_Z and atomic_number() 100% backward-compatible.
"""

from dataclasses import dataclass

# (Z, IUPAC Group 1..18, Period 1..7, Block)
# Group 0 / Period 0 reserved for Element-0 substrate; f-block mapped to Group 3.
ELEMENT_TABLE: dict[str, tuple[int, int, int, str]] = {
    "E0": (0, 0, 0, "substrate"),
    "H": (1, 1, 1, "s"), "He": (2, 18, 1, "s"),
    "Li": (3, 1, 2, "s"), "Be": (4, 2, 2, "s"), "B": (5, 13, 2, "p"), "C": (6, 14, 2, "p"),
    "N": (7, 15, 2, "p"), "O": (8, 16, 2, "p"), "F": (9, 17, 2, "p"), "Ne": (10, 18, 2, "p"),
    "Na": (11, 1, 3, "s"), "Mg": (12, 2, 3, "s"), "Al": (13, 13, 3, "p"), "Si": (14, 14, 3, "p"),
    "P": (15, 15, 3, "p"), "S": (16, 16, 3, "p"), "Cl": (17, 17, 3, "p"), "Ar": (18, 18, 3, "p"),
    "K": (19, 1, 4, "s"), "Ca": (20, 2, 4, "s"), "Sc": (21, 3, 4, "d"), "Ti": (22, 4, 4, "d"),
    "V": (23, 5, 4, "d"), "Cr": (24, 6, 4, "d"), "Mn": (25, 7, 4, "d"), "Fe": (26, 8, 4, "d"),
    "Co": (27, 9, 4, "d"), "Ni": (28, 10, 4, "d"), "Cu": (29, 11, 4, "d"), "Zn": (30, 12, 4, "d"),
    "Ga": (31, 13, 4, "p"), "Ge": (32, 14, 4, "p"), "As": (33, 15, 4, "p"), "Se": (34, 16, 4, "p"),
    "Br": (35, 17, 4, "p"), "Kr": (36, 18, 4, "p"),
    "Rb": (37, 1, 5, "s"), "Sr": (38, 2, 5, "s"), "Y": (39, 3, 5, "d"), "Zr": (40, 4, 5, "d"),
    "Nb": (41, 5, 5, "d"), "Mo": (42, 6, 5, "d"), "Tc": (43, 7, 5, "d"), "Ru": (44, 8, 5, "d"),
    "Rh": (45, 9, 5, "d"), "Pd": (46, 10, 5, "d"), "Ag": (47, 11, 5, "d"), "Cd": (48, 12, 5, "d"),
    "In": (49, 13, 5, "p"), "Sn": (50, 14, 5, "p"), "Sb": (51, 15, 5, "p"), "Te": (52, 16, 5, "p"),
    "I": (53, 17, 5, "p"), "Xe": (54, 18, 5, "p"),
    "Cs": (55, 1, 6, "s"), "Ba": (56, 2, 6, "s"),
    "La": (57, 3, 6, "f"), "Ce": (58, 3, 6, "f"), "Pr": (59, 3, 6, "f"), "Nd": (60, 3, 6, "f"),
    "Pm": (61, 3, 6, "f"), "Sm": (62, 3, 6, "f"), "Eu": (63, 3, 6, "f"), "Gd": (64, 3, 6, "f"),
    "Tb": (65, 3, 6, "f"), "Dy": (66, 3, 6, "f"), "Ho": (67, 3, 6, "f"), "Er": (68, 3, 6, "f"),
    "Tm": (69, 3, 6, "f"), "Yb": (70, 3, 6, "f"), "Lu": (71, 3, 6, "f"),
    "Hf": (72, 4, 6, "d"), "Ta": (73, 5, 6, "d"), "W": (74, 6, 6, "d"), "Re": (75, 7, 6, "d"),
    "Os": (76, 8, 6, "d"), "Ir": (77, 9, 6, "d"), "Pt": (78, 10, 6, "d"), "Au": (79, 11, 6, "d"),
    "Hg": (80, 12, 6, "d"), "Tl": (81, 13, 6, "p"), "Pb": (82, 14, 6, "p"), "Bi": (83, 15, 6, "p"),
    "Po": (84, 16, 6, "p"), "At": (85, 17, 6, "p"), "Rn": (86, 18, 6, "p"),
    "Fr": (87, 1, 7, "s"), "Ra": (88, 2, 7, "s"),
    "Ac": (89, 3, 7, "f"), "Th": (90, 3, 7, "f"), "Pa": (91, 3, 7, "f"), "U": (92, 3, 7, "f"),
    "Np": (93, 3, 7, "f"), "Pu": (94, 3, 7, "f"), "Am": (95, 3, 7, "f"), "Cm": (96, 3, 7, "f"),
    "Bk": (97, 3, 7, "f"), "Cf": (98, 3, 7, "f"), "Es": (99, 3, 7, "f"), "Fm": (100, 3, 7, "f"),
    "Md": (101, 3, 7, "f"), "No": (102, 3, 7, "f"), "Lr": (103, 3, 7, "f"),
    "Rf": (104, 4, 7, "d"), "Db": (105, 5, 7, "d"), "Sg": (106, 6, 7, "d"), "Bh": (107, 7, 7, "d"),
    "Hs": (108, 8, 7, "d"), "Mt": (109, 9, 7, "d"), "Ds": (110, 10, 7, "d"), "Rg": (111, 11, 7, "d"),
    "Cn": (112, 12, 7, "d"), "Nh": (113, 13, 7, "p"), "Fl": (114, 14, 7, "p"), "Mc": (115, 15, 7, "p"),
    "Lv": (116, 16, 7, "p"), "Ts": (117, 17, 7, "p"), "Og": (118, 18, 7, "p"),
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
    """Return full HTE octave-lattice and periodic group-phase coordinates."""
    if symbol not in ELEMENT_TABLE:
        raise ValueError(f"Unknown element symbol: {symbol}")
    z, grp, per, blk = ELEMENT_TABLE[symbol]
    pi_raw = z % 12
    pi_group = 0 if grp == 0 else int(round(((grp - 1) * 12) / 18.0)) % 12
    omega = z // 12
    return ElementCoordinates(
        symbol=symbol,
        Z=z,
        group=grp,
        period=per,
        block=blk,
        pi_raw=pi_raw,
        pi_group=pi_group,
        omega=omega,
    )
