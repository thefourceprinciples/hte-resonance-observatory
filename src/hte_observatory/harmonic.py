"""HTE harmonic mapping engine.

Core invariant:
    pitch_class = atomic_number mod 12

This module produces exploratory signatures only. It does not infer material
properties without calibration data.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass

from .elements import PITCH_NAMES, atomic_number
from .formula import parse_formula


@dataclass(frozen=True)
class HTENode:
    element: str
    atomic_number: int
    count: int
    pitch_class: int
    pitch_name: str
    octave_band: int


def _circular_distance(a: int, b: int) -> int:
    delta = abs(a - b) % 12
    return min(delta, 12 - delta)


def _interval_walk(pitch_classes: list[int]) -> list[int]:
    if len(pitch_classes) < 2:
        return []
    unique = sorted(set(pitch_classes))
    return [((unique[(i + 1) % len(unique)] - unique[i]) % 12) for i in range(len(unique))]


def _has_tritone(pitch_classes: list[int]) -> bool:
    unique = sorted(set(pitch_classes))
    return any(_circular_distance(a, b) == 6 for i, a in enumerate(unique) for b in unique[i + 1 :])


def classify_overlay_state(pitch_classes: list[int]) -> str:
    """Return a conservative exploratory state tag.

    These are HTE overlay states, not conventional material classes.
    """
    unique = sorted(set(pitch_classes))
    if not unique:
        return "VOID"
    if _has_tritone(unique):
        return "PIEZO_OVERLAY_CANDIDATE"
    if 7 in unique:
        return "GOLD_OVERLAY_CANDIDATE"
    if len(unique) >= 3 and any(pc in {0, 5, 8, 10} for pc in unique):
        return "ARMOR_OVERLAY_CANDIDATE"
    return "MIXED_OVERLAY"


def build_hte_signature(formula: str) -> dict:
    """Build an HTE signature from a formula string."""
    composition = parse_formula(formula)
    nodes: list[HTENode] = []
    weighted_pitch_classes: list[int] = []

    for symbol, count in sorted(composition.items(), key=lambda item: atomic_number(item[0])):
        z = atomic_number(symbol)
        pitch_class = z % 12
        weighted_pitch_classes.extend([pitch_class] * count)
        nodes.append(
            HTENode(
                element=symbol,
                atomic_number=z,
                count=count,
                pitch_class=pitch_class,
                pitch_name=PITCH_NAMES[pitch_class],
                octave_band=((z - 1) // 12) + 1,
            )
        )

    histogram = Counter(weighted_pitch_classes)
    unique = sorted(histogram)

    return {
        "formula": formula,
        "composition": composition,
        "mapping_rule": "pitch_class = atomic_number mod 12",
        "nodes": [asdict(node) for node in nodes],
        "weighted_chord": weighted_pitch_classes,
        "pitch_class_histogram": {str(k): histogram[k] for k in unique},
        "interval_walk": _interval_walk(unique),
        "dominant_pitch_class": histogram.most_common(1)[0][0] if histogram else None,
        "overlay_state": classify_overlay_state(unique),
        "claim_boundary": "derived_hte_mapping_only",
    }
