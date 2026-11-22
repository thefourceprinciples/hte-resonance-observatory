"""HTE harmonic mapping & CLV-HTE-001 modal coherence engine (v0.2).

Combines v0.1 raw Z mod 12 interval-walk & Matter-State overlay classification
with CLV-HTE-001 unit-norm 12x7 modal inference, C_modal = O * E * H * X,
Fource functional F, and periodic group-phase coordinates.

This module produces exploratory signatures only. It does not infer material
properties without calibration data.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import asdict, dataclass

from .elements import PITCH_NAMES, atomic_number, element_coordinates
from .formula import parse_formula


@dataclass(frozen=True)
class HTENode:
    element: str
    atomic_number: int
    count: float
    pitch_class: int
    pitch_name: str
    octave_band: int
    group: int = 0
    period: int = 0
    block: str = ""
    group_pitch_class: int = 0
    group_pitch_name: str = "C"


@dataclass(frozen=True)
class ModeSpec:
    name: str
    intervals: tuple[int, ...]
    characteristic_degree: int
    third_degree: int
    fifth_degree: int
    field_type: str
    cognitive_signature: str


MODES: dict[str, ModeSpec] = {
    "Ionian": ModeSpec("Ionian", (0, 2, 4, 5, 7, 9, 11), 11, 4, 7, "Structural Clarity Field", "stable prediction, closure"),
    "Dorian": ModeSpec("Dorian", (0, 2, 3, 5, 7, 9, 10), 9, 3, 7, "Restoration Field", "recovery under load"),
    "Phrygian": ModeSpec("Phrygian", (0, 1, 3, 5, 7, 8, 10), 1, 3, 7, "Boundary / Threshold Field", "boundary alertness"),
    "Lydian": ModeSpec("Lydian", (0, 2, 4, 6, 7, 9, 11), 6, 4, 7, "Expansion / Levitation Field", "upward spatiality"),
    "Mixolydian": ModeSpec("Mixolydian", (0, 2, 4, 5, 7, 9, 10), 10, 4, 7, "Continuity Field", "social continuity"),
    "Aeolian": ModeSpec("Aeolian", (0, 2, 3, 5, 7, 8, 10), 8, 3, 7, "Memory / Gravitational Field", "reflective descent"),
    "Locrian": ModeSpec("Locrian", (0, 1, 3, 5, 6, 8, 10), 6, 3, 6, "Fracture / Collapse Field", "center-loss"),
}


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


def _unit_template_vector(tonic: int, mode: ModeSpec) -> list[float]:
    vec = [0.0] * 12
    for deg in mode.intervals:
        vec[(tonic + deg) % 12] = 1.0
    vec[tonic] = 2.0
    vec[(tonic + mode.fifth_degree) % 12] += 0.5
    vec[(tonic + mode.characteristic_degree) % 12] += 0.6
    vec[(tonic + mode.third_degree) % 12] += 0.3
    norm = math.sqrt(sum(v * v for v in vec))
    return [v / norm for v in vec] if norm > 0 else vec


def evaluate_modal_field(h: list[float], epsilon: float = 0.05) -> dict:
    """Run CLV-HTE-001 12x7 modal inference, C_modal = O*E*H*X, and Fource lock F."""
    norm_h = math.sqrt(sum(x * x for x in h))
    mode_names = list(MODES.keys())
    heatmap: list[list[float]] = []

    best_score = -1.0
    best_t = 0
    best_m = "Ionian"
    best_detail: dict = {}

    for t in range(12):
        row: list[float] = []
        for m_name in mode_names:
            mode = MODES[m_name]
            template_pcs = {(t + deg) % 12 for deg in mode.intervals}
            t_vec = _unit_template_vector(t, mode)

            cos_sim = sum(a * b for a, b in zip(h, t_vec)) / norm_h if norm_h > 0 else 0.0
            off_mass = sum(h[k] for k in range(12) if k not in template_pcs)
            match_score = max(0.0, cos_sim - 0.5 * off_mass)

            h_root = h[t]
            h_fifth = h[(t + mode.fifth_degree) % 12]
            h_third = h[(t + mode.third_degree) % 12]
            h_char = h[(t + mode.characteristic_degree) % 12]

            O = min(1.0, (0.50 * h_root + 0.30 * h_fifth + 0.20 * h_third) * 2.0)
            E = 1.0 - off_mass
            H = 1.0
            X = min(1.0, 0.25 + 1.5 * h_char)
            c_modal = O * E * H * X

            m2_pressure = 0.0
            tri_pressure = 0.0
            for i in range(12):
                for j in range(i + 1, 12):
                    interval = (j - i) % 12
                    pair_mass = h[i] * h[j]
                    if interval in (1, 11):
                        m2_pressure += pair_mass
                    elif interval == 6:
                        tri_pressure += pair_mass

            fource = (h_root * (h_char + 0.15 * h_fifth)) / (epsilon + off_mass + m2_pressure + tri_pressure)
            selection_score = match_score + 0.05 * math.tanh(fource)
            row.append(round(selection_score, 6))

            if selection_score > best_score:
                best_score = selection_score
                best_t = t
                best_m = m_name
                best_detail = {
                    "match_score": round(match_score, 6),
                    "c_modal": round(c_modal, 6),
                    "coherence_components": {
                        "O": round(O, 4),
                        "E": round(E, 4),
                        "H": round(H, 4),
                        "X": round(X, 4),
                    },
                    "fource_lock": round(fource, 6),
                    "friction": {
                        "off_template": round(off_mass, 4),
                        "minor_second": round(m2_pressure, 4),
                        "tritone": round(tri_pressure, 4),
                    },
                }
        heatmap.append(row)

    spec = MODES[best_m]
    return {
        "optimal_tonic": best_t,
        "optimal_tonic_name": PITCH_NAMES[best_t],
        "optimal_mode": best_m,
        "field_type": spec.field_type,
        "cognitive_signature": spec.cognitive_signature,
        **best_detail,
        "heatmap_modes": mode_names,
        "heatmap_12x7": heatmap,
    }


def build_hte_signature(formula: str, mapping_mode: str = "raw") -> dict:
    """Build an HTE signature from a formula string.

    Supports mapping_mode='raw' (Z mod 12, default for v0.1 compatibility)
    or mapping_mode='group' (periodic group-phase projection onto Z_12).
    """
    composition = parse_formula(formula)
    nodes: list[HTENode] = []
    weighted_pitch_classes: list[int] = []
    raw_hist = [0.0] * 12
    group_hist = [0.0] * 12

    for symbol, count in sorted(composition.items(), key=lambda item: atomic_number(item[0])):
        coords = element_coordinates(symbol)
        z = coords.Z
        pitch_class = coords.pi_group if mapping_mode == "group" else coords.pi_raw
        int_count = max(1, int(round(count))) if count > 0 else 0
        weighted_pitch_classes.extend([pitch_class] * int_count)

        raw_hist[coords.pi_raw] += float(count)
        group_hist[coords.pi_group] += float(count)

        octave_band = 0 if z == 0 else ((z - 1) // 12) + 1
        nodes.append(
            HTENode(
                element=symbol,
                atomic_number=z,
                count=count,
                pitch_class=pitch_class,
                pitch_name=PITCH_NAMES[pitch_class],
                octave_band=octave_band,
                group=coords.group,
                period=coords.period,
                block=coords.block,
                group_pitch_class=coords.pi_group,
                group_pitch_name=PITCH_NAMES[coords.pi_group],
            )
        )

    histogram = Counter(weighted_pitch_classes)
    unique = sorted(histogram)

    active_hist = group_hist if mapping_mode == "group" else raw_hist
    total_w = sum(active_hist)
    norm_h = [x / total_w for x in active_hist] if total_w > 0 else active_hist

    total_raw = sum(raw_hist)
    norm_raw = [x / total_raw for x in raw_hist] if total_raw > 0 else raw_hist
    total_grp = sum(group_hist)
    norm_grp = [x / total_grp for x in group_hist] if total_grp > 0 else group_hist

    return {
        "formula": formula,
        "composition": composition,
        "mapping_mode": mapping_mode,
        "mapping_rule": (
            "pitch_class = periodic_group_phase(Z) mod 12"
            if mapping_mode == "group"
            else "pitch_class = atomic_number mod 12"
        ),
        "nodes": [asdict(node) for node in nodes],
        "weighted_chord": weighted_pitch_classes,
        "pitch_class_histogram": {str(k): histogram[k] for k in unique},
        "interval_walk": _interval_walk(unique),
        "dominant_pitch_class": histogram.most_common(1)[0][0] if histogram else None,
        "overlay_state": classify_overlay_state(unique),
        "modal_field": evaluate_modal_field(norm_h),
        "modal_field_raw": evaluate_modal_field(norm_raw),
        "modal_field_group": evaluate_modal_field(norm_grp),
        "claim_boundary": "derived_hte_mapping_only",
    }
