"""HTE harmonic mapping & CLV-HTE-001 physical calibration engine (v0.3).

Combines v0.1 raw Z mod 12 interval-walk & overlay classification with
CLV-HTE-001 12x7 modal inference, Pauling electronegativity (chi) & valence
weighting, bond polarity delta_chi, and continuous 7-state phase probabilities.

This module produces exploratory signatures only (Claim Level L2). It does not
infer conventional material properties without external calibration data.
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
    valence: int = 0
    electronegativity: float = 0.0
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
    """Return the v0.1 backward-compatible exploratory state tag."""
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


def compute_soft_states(norm_h: list[float], nodes: list[HTENode], delta_chi: float = 0.0) -> dict:
    """Compute continuous 7-state phase probabilities and dominant discovery state."""
    active_pcs = [i for i, w in enumerate(norm_h) if w > 1e-9]
    if not active_pcs:
        probs = {
            "SUBSTRATE_ZERO": 0.0, "SINGLET_SEED": 0.0, "GOLD_ANCHOR": 0.0,
            "PIEZO_TENSION": 0.0, "ARMOR_SHIELD": 0.0, "SHADOW_PHASE": 0.0, "PLASMA_FLUX": 0.0,
        }
        return {"dominant_state": "VOID", "state_probabilities": probs}

    if len(nodes) == 1 and nodes[0].element == "E0":
        probs = {
            "SUBSTRATE_ZERO": 1.0, "SINGLET_SEED": 0.0, "GOLD_ANCHOR": 0.0,
            "PIEZO_TENSION": 0.0, "ARMOR_SHIELD": 0.0, "SHADOW_PHASE": 0.0, "PLASMA_FLUX": 0.0,
        }
        return {"dominant_state": "SUBSTRATE_ZERO", "state_probabilities": probs}

    tritone_energy = 0.0
    semitone_energy = 0.0
    fifth_energy = 0.0
    for i in range(12):
        for j in range(i + 1, 12):
            iv = _circular_distance(i, j)
            pair = norm_h[i] * norm_h[j]
            if iv == 6:
                tritone_energy += pair
            elif iv == 1:
                semitone_energy += pair
            elif iv == 5:
                fifth_energy += pair

    entropy = -sum(w * math.log(w) for w in norm_h if w > 1e-12)
    singlet_raw = math.exp(-3.0 * entropy)

    polarity_factor = 1.0 + 0.25 * min(delta_chi, 3.5)
    piezo_raw = 4.0 * tritone_energy * polarity_factor
    gold_raw = 1.8 * norm_h[7] + 1.5 * fifth_energy
    armor_mass = sum(norm_h[p] for p in (0, 5, 8, 10))
    armor_raw = 1.4 * armor_mass * min(1.0, len(active_pcs) / 3.0)
    plasma_raw = 5.0 * semitone_energy * max(0.0, (len(active_pcs) - 2) / 2.0)
    shadow_raw = 0.45 * (1.0 - singlet_raw) * max(0.0, 1.0 - 2.0 * tritone_energy - norm_h[7])

    raw_scores = {
        "SUBSTRATE_ZERO": 0.0,
        "SINGLET_SEED": singlet_raw,
        "GOLD_ANCHOR": gold_raw,
        "PIEZO_TENSION": piezo_raw,
        "ARMOR_SHIELD": armor_raw,
        "SHADOW_PHASE": shadow_raw,
        "PLASMA_FLUX": plasma_raw,
    }
    total = sum(raw_scores.values())
    probs = {k: round(v / total, 6) if total > 0 else 0.0 for k, v in raw_scores.items()}
    dominant = max(probs.items(), key=lambda kv: kv[1])[0]
    return {"dominant_state": dominant, "state_probabilities": probs}
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


def _normalize(vec: list[float]) -> list[float]:
    total = sum(vec)
    return [x / total for x in vec] if total > 0 else vec


def build_hte_signature(
    formula: str,
    mapping_mode: str = "raw",
    weight_mode: str = "stoich",
) -> dict:
    """Build a physically calibrated HTE signature from a formula string.

    Args:
        formula: Chemical formula (e.g. 'SiO2', 'BaTiO3', 'YBa2Cu3O6.9', 'E0').
        mapping_mode: 'raw' (Z mod 12) or 'group' (periodic group-phase).
        weight_mode: 'stoich' (atom count), 'electronegativity' (count * chi),
                     or 'valence' (count * valence electrons).
    """
    composition = parse_formula(formula)
    nodes: list[HTENode] = []
    weighted_pitch_classes: list[int] = []

    raw_hist = [0.0] * 12
    group_hist = [0.0] * 12
    chi_hist = [0.0] * 12
    val_hist = [0.0] * 12

    chis: list[float] = []
    total_atoms = 0.0
    total_valence = 0.0
    chi_weighted_sum = 0.0

    for symbol, count in sorted(composition.items(), key=lambda item: atomic_number(item[0])):
        coords = element_coordinates(symbol)
        z = coords.Z
        pitch_class = coords.pi_group if mapping_mode == "group" else coords.pi_raw
        int_count = max(1, int(round(count))) if count > 0 else 0
        weighted_pitch_classes.extend([pitch_class] * int_count)

        w_stoich = float(count)
        w_chi = float(count) * (coords.electronegativity if coords.electronegativity > 0 else 0.1)
        w_val = float(count) * (coords.valence if coords.valence > 0 else 0.1)

        raw_hist[coords.pi_raw] += w_stoich
        group_hist[coords.pi_group] += w_stoich
        chi_hist[pitch_class] += w_chi
        val_hist[pitch_class] += w_val

        if coords.electronegativity > 0:
            chis.append(coords.electronegativity)
            chi_weighted_sum += float(count) * coords.electronegativity
        total_atoms += float(count)
        total_valence += float(count) * coords.valence

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
                valence=coords.valence,
                electronegativity=coords.electronegativity,
                group_pitch_class=coords.pi_group,
                group_pitch_name=PITCH_NAMES[coords.pi_group],
            )
        )

    histogram = Counter(weighted_pitch_classes)
    unique = sorted(histogram)

    base_hist = group_hist if mapping_mode == "group" else raw_hist
    if weight_mode == "electronegativity":
        active_hist = chi_hist
    elif weight_mode == "valence":
        active_hist = val_hist
    else:
        active_hist = base_hist

    norm_active = _normalize(active_hist)
    norm_raw = _normalize(raw_hist)
    norm_grp = _normalize(group_hist)
    norm_chi = _normalize(chi_hist)

    delta_chi = round(max(chis) - min(chis), 4) if len(chis) >= 2 else 0.0
    mean_chi = round(chi_weighted_sum / total_atoms, 4) if total_atoms > 0 else 0.0
    valence_per_atom = round(total_valence / total_atoms, 4) if total_atoms > 0 else 0.0

    soft_states = compute_soft_states(norm_active, nodes, delta_chi=delta_chi)

    return {
        "formula": formula,
        "composition": composition,
        "mapping_mode": mapping_mode,
        "weight_mode": weight_mode,
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
        "discovery_state": soft_states["dominant_state"],
        "state_probabilities": soft_states["state_probabilities"],
        "physical_metrics": {
            "delta_chi": delta_chi,
            "mean_chi": mean_chi,
            "total_valence": round(total_valence, 4),
            "valence_per_atom": valence_per_atom,
        },
        "modal_field": evaluate_modal_field(norm_active),
        "modal_field_raw": evaluate_modal_field(norm_raw),
        "modal_field_group": evaluate_modal_field(norm_grp),
        "modal_field_chi": evaluate_modal_field(norm_chi),
        "claim_boundary": "derived_hte_mapping_only",
    }
