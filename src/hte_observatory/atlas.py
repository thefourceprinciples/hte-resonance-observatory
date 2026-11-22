"""Materials Atlas Engine (MAE) — 17-section element & compound dossier generator.

Combines deterministic HTE lattice coordinates, C_HTE unison coherence, and
6-step Fifth Ladder sequences with curated canonical dossiers (such as
MATLAS-E000-SUBSTRATE and MATLAS-E001-HYDROGEN) and periodic-family engineering
intelligence across all 119 elements (E0 and Z = 1..118).
"""

from __future__ import annotations

from datetime import date
from .elements import ELEMENT_TABLE, PITCH_NAMES, element_coordinates
from .harmonic import build_hte_signature

# Curated canonical overrides (Tier 2 dossiers)
CANONICAL_DOSSIERS: dict[str, dict] = {
    "E0": {
        "entry_id": "MATLAS-E000-SUBSTRATE",
        "status": "canonical_draft",
        "name": "Element-0 (Substrate Zero)",
        "material_class": "sub-nucleonic reference substrate / vacuum carrier floor",
        "hte_role": "Substrate Zero / zero-octave calibration origin",
        "isotopes": list(("None (zero-nucleon reference substrate; Z=0, A=0)",)),
        "canonical_phrase": "Element-0 is the unperturbed carrier floor from which discrete baryonic matter emerges.",
        "fource_phrase": "Element-0 is the silence that makes the first note audible.",
        "one_line_lock": "Element-0 = Substrate Zero: the unperturbed carrier medium before discrete atomic boundary conditions.",
        "state_activation": {
            "Origin": "baseline — pre-nucleonic zero point prior to Z=1.",
            "Gold": "null — unexcited reference medium.",
            "Shadow": "null — no lattice structure.",
            "Plasma": "null — un-ionized reference floor.",
            "Armor": "null — zero boundary mass.",
            "Piezo": "null — zero stress gradient.",
            "Fifth Ladder": "E0 Substrate calibration origin.",
        },
        "interface_behavior": list(("Provides unperturbed continuous reference medium (pi=0, omega=0)",)),
        "failure_modes": list(("Zero-matter baseline — no physical containment failure modes",)),
        "darkness_remainder": {
            "visible_accounting": "Zero nucleonic mass (Z=0, valence=0, chi=0.00).",
            "hidden_remainder": "Ambient carrier medium enabling gradient and wave propagation.",
        },
    },
    "H": {
        "entry_id": "MATLAS-E001-HYDROGEN",
        "status": "canonical_draft",
        "name": "Hydrogen",
        "material_class": "element / gas / plasma-forming carrier / hydride former / isotope platform",
        "hte_role": "Origin Node / carrier seed / Fifth-Ladder root",
        "isotopes": list(("1H (protium, stable)", "2H (deuterium, stable)", "3H (tritium, radio)")),
        "canonical_phrase": "Hydrogen is the first carrier: the smallest material unit of elemental identity, the seed point from which the HTE lattice begins.",
        "fource_phrase": "Hydrogen is the first note of matter, but it only becomes a song under constraint.",
        "one_line_lock": "Hydrogen = Origin Carrier: the first HTE note, the smallest material actor, and the most boundary-sensitive seed of energy, storage, plasma, and lattice interaction.",
        "state_activation": {
            "Origin": "very high — Z=1, first pitch-class root and lattice seed.",
            "Gold": "conditional — active in fuel cells, PEM proton transfer, and redox pathways.",
            "Shadow": "high — stored, trapped, or absorbed as interstitial hydrides.",
            "Plasma": "very high — simplest ionized plasma and fusion seed.",
            "Armor": "low / negative at interfaces — weakens metal grain boundaries via embrittlement.",
            "Piezo": "indirect — converts pressure/proton transport stress inside host lattices.",
            "Fifth Ladder": "canonical root — H -> O -> P -> Ti -> Cu -> Kr.",
        },
        "interface_behavior": list((
            "Adsorbs onto catalytic surfaces and dissociates from H2 into atomic H",
            "Diffuses rapidly into metals and occupies interstitial lattice sites",
            "Forms metal hydrides and weakens grain boundaries (embrittlement)",
            "Participates in proton conduction and alters local electronic structure",
        )),
        "failure_modes": list((
            "Hydrogen Embrittlement (reduces tensile strength, ductility, and fracture toughness)",
            "Leakage and Permeation through seals and defects due to tiny molecular radius",
            "Flammability / Ignition Risk in air (wide flammable range, ~500°C autoignition)",
            "Cryogenic Risk (boil-off pressure rise and thermal contraction near -252.9°C)",
        )),
        "darkness_remainder": {
            "visible_accounting": "Smallest element, light diatomic gas (H2), simple 1s1 structure.",
            "hidden_remainder": "Embrittlement, seal permeation, storage difficulty, plasma potential, protonic transport, isotope divergence.",
        },
        "measurement_stack": {
            "basic_identity": list(("purity", "isotope ratio", "molecular form", "pressure", "temperature")),
            "storage_behavior": list(("leak rate", "permeation rate", "adsorption capacity", "desorption hysteresis", "cycling stability")),
            "material_compatibility": list(("embrittlement response", "crack growth rate", "tensile strength change", "ductility change")),
            "energy_and_interface": list(("reaction enthalpy", "proton conductivity", "plasma threshold", "surface dissociation", "diffusion coefficient")),
        },
    },
}

_Z_TO_SYMBOL: dict[int, str] = {meta[0]: sym for sym, meta in ELEMENT_TABLE.items()}



def fifth_ladder_from_z(root_z: int, steps: int = 6) -> list[dict]:
    """Compute the n-step Fifth Ladder sequence p_n = (p_0 + 7n) mod 12."""
    if root_z <= 0:
        return list(({"step": 0, "Z": 0, "symbol": "E0", "pitch_raw": 0, "pitch_name": "C"},))
    ladder: list[dict] = list()
    for n in range(steps):
        z_step = root_z + 7 * n
        sym = _Z_TO_SYMBOL.get(z_step, f"Z{z_step}")
        p_raw = z_step % 12
        ladder.append({
            "step": n,
            "Z": z_step,
            "symbol": sym,
            "pitch_raw": p_raw,
            "pitch_name": PITCH_NAMES[p_raw],
        })
    return ladder
def _auto_family_profile(symbol: str, z: int, group: int, block: str, chi: float) -> dict:
    """Synthesize Tier-1 engineering & interface rules for any element Z = 0..118."""
    if group == 1:
        role = "Alkali electron donor / high-mobility ionic carrier"
        iface = list(("Rapid surface oxidation & moisture reaction", "Intercalates into layered host cathodes (e.g. Li/Na batteries)"))
        fails = list(("Dendrite formation under high current density", "Exothermic hydrolysis / thermal runaway in air or water"))
    elif group == 17:
        role = "Halogen electron acceptor / high-polarity bond terminator"
        iface = list(("Forms strong ionic/polar covalent surface passivation layers", "High electronegativity charge withdrawal"))
        fails = list(("Halide stress-corrosion cracking & outgassing toxicity",))
    elif group == 18:
        role = "Noble closed-shell buffer / plasma discharge medium"
        iface = list(("Chemically inert boundary gas; forms ionized plasma under high-voltage excitation",))
        fails = list(("Inert-gas bubble swelling / grain-boundary blistering under implantation",))
    elif block == "d":
        role = "Transition-metal d-orbital host / catalytic & hydride lattice"
        iface = list(("Hosts interstitial light carriers (H/D/O) in d-band vacancies", "Catalyzes surface molecular dissociation"))
        fails = list(("Interstitial embrittlement, phase fatigue, and grain-boundary decohesion",))
    elif block == "f":
        role = "Inner-shell f-orbital magnetic / high-density energy actor"
        iface = list(("Localized f-electron spin coupling & high-Z lattice mass",))
        fails = list(("Oxidation sensitivity, thermal brittleness, or radiotoxic containment (actinides)",))
    else:
        role = "Main-group covalent / semiconductor network former"
        iface = list(("Forms directional sp-hybridized covalent bonds and dielectric/semiconductor interfaces",))
        fails = list(("Brittle fracture under tensile shock & interface trap-state defects",))

    return {
        "material_class": f"element / group-{group} {block}-block actor (chi={chi:.2f})",
        "hte_role": role,
        "interface_behavior": iface,
        "failure_modes": fails,
        "darkness_remainder": {
            "visible_accounting": f"Z={z}, Group {group}, {block}-block, Pauling chi={chi:.2f}.",
            "hidden_remainder": "Interface charge transfer, lattice defect trapping, and boundary-dependent phase shifts.",
        },
        "one_line_lock": f"{symbol} (Z={z}) = Group-{group} {block}-block actor whose bulk chord shifts under boundary and interface constraints.",
    }


def build_element_atlas_entry(symbol: str, entry_date: str | None = None) -> dict:
    """Build a full 17-section Materials Atlas Entry (MAE) for any element E0..Og."""
    coords = element_coordinates(symbol)
    z = coords.Z
    o_matlas = 0 if z == 0 else ((z - 1) // 12) + 1
    override = CANONICAL_DOSSIERS.get(symbol, {})
    auto = _auto_family_profile(symbol, z, coords.group, coords.block, coords.electronegativity)

    sig_single = build_hte_signature(symbol, mapping_mode="raw")
    diatomic_formula = symbol if z == 0 else f"{symbol}2"
    sig_diatomic = build_hte_signature(diatomic_formula, mapping_mode="raw")
    ladder = fifth_ladder_from_z(z, steps=6)

    entry_id = override.get("entry_id", f"MATLAS-E{z:03d}-{symbol.upper()}")
    status = override.get("status", "auto_derived_v1")
    name = override.get("name", symbol)

    default_states = {
        "Origin": "very high" if z <= 1 else "low",
        "Gold": "high" if coords.pi_group == 7 or coords.pi_raw == 7 else "conditional",
        "Shadow": "high" if coords.block in ("d", "f") else "conditional",
        "Plasma": "high" if coords.group in (1, 18) or z == 1 else "conditional",
        "Armor": "high" if coords.block == "d" and coords.group in (6, 8, 10) else "conditional",
        "Piezo": "high" if coords.electronegativity >= 2.5 or coords.group in (4, 17) else "indirect",
        "Fifth Ladder": "canonical root" if z == 1 else f"step-0 node ({' -> '.join(s['symbol'] for s in ladder)})",
    }

    return {
        "entry_id": entry_id,
        "date": entry_date or date.today().isoformat(),
        "status": status,
        "material_class": override.get("material_class", auto["material_class"]),
        "hte_role": override.get("hte_role", auto["hte_role"]),
        "core_identity": {
            "name": name,
            "symbol": symbol,
            "atomic_number": z,
            "period": coords.period,
            "group": coords.group,
            "block": coords.block,
            "valence_electrons": coords.valence,
            "pauling_electronegativity": coords.electronegativity,
            "isotopes": override.get("isotopes", list((f"Standard isotopes of {symbol} share Z={z} and pi_raw={coords.pi_raw}",))),
        },
        "hte_signature": {
            "coordinate_raw": {"p": coords.pi_raw, "o": o_matlas, "tuple": list((coords.pi_raw, o_matlas))},
            "coordinate_group": {"p": coords.pi_group, "o": o_matlas, "tuple": list((coords.pi_group, o_matlas))},
            "pitch_name_raw": PITCH_NAMES[coords.pi_raw],
            "pitch_name_group": PITCH_NAMES[coords.pi_group],
            "atomic_chord": list((coords.pi_raw,)),
            "diatomic_formula": diatomic_formula,
            "diatomic_chord": list((coords.pi_raw, coords.pi_raw)) if z > 0 else list(),
            "c_hte_unison": 1.0,
            "modal_field_group": sig_single["modal_field_group"],
            "modal_field_diatomic": sig_diatomic["modal_field_group"],
        },
        "fifth_ladder": {
            "recurrence": "p_n = (p_0 + 7n) mod 12",
            "sequence": ladder,
            "pathway_text": " -> ".join(s["symbol"] for s in ladder),
        },
        "state_activation": override.get("state_activation", default_states),
        "interface_behavior": override.get("interface_behavior", auto["interface_behavior"]),
        "failure_modes": override.get("failure_modes", auto["failure_modes"]),
        "darkness_remainder": override.get("darkness_remainder", auto["darkness_remainder"]),
        "measurement_stack": override.get("measurement_stack", {
            "basic_identity": list(("purity", "stoichiometry", "crystal phase", "pressure", "temperature")),
            "interface_and_compatibility": list(("surface adsorption", "diffusion coefficient", "grain-boundary stability")),
        }),
        "canonical_phrase": override.get("canonical_phrase", auto["one_line_lock"]),
        "fource_phrase": override.get("fource_phrase", auto["one_line_lock"]),
        "one_line_lock": override.get("one_line_lock", auto["one_line_lock"]),
        "claim_boundary": "derived_hte_mapping_only",
    }


def render_atlas_markdown(entry: dict) -> str:
    """Render any MAE dictionary into a publication-ready Markdown dossier."""
    cid = entry["core_identity"]
    sig = entry["hte_signature"]
    states = "\n".join(f"- **{k}:** {v}" for k, v in entry["state_activation"].items())
    ifaces = "\n".join(f"- {item}" for item in entry["interface_behavior"])
    fails = "\n".join(f"- {item}" for item in entry["failure_modes"])
    return (
        f"# Materials Atlas Entry: {cid['name']}\n"
        f"**ENTRY ID:** `{entry['entry_id']}` | **DATE:** {entry['date']} | **STATUS:** `{entry['status']}`\n"
        f"**CLASS:** {entry['material_class']}\n"
        f"**HTE ROLE:** {entry['hte_role']}\n\n"
        f"## Core & HTE Signature\n"
        f"- **Symbol / Z:** {cid['symbol']} (Z = {cid['atomic_number']}, Group {cid['group']}, Period {cid['period']}, {cid['block']}-block, χ = {cid['pauling_electronegativity']})\n"
        f"- **HTE Coordinate (Raw / Group):** `{tuple(sig['coordinate_raw']['tuple'])}` ({sig['pitch_name_raw']}) / `{tuple(sig['coordinate_group']['tuple'])}` ({sig['pitch_name_group']})\n"
        f"- **Diatomic Unison Coherence:** `C_HTE({sig['diatomic_formula']}) = +{sig['c_hte_unison']:.2f}`\n"
        f"- **Fifth Ladder Pathway:** `{entry['fifth_ladder']['pathway_text']}`\n\n"
        f"## 7-State Activation Profile\n{states}\n\n"
        f"## Interface Behavior & Failure Modes\n{ifaces}\n\n**Failure Modes:**\n{fails}\n\n"
        f"## Darkness Functional Reading & One-Line Lock\n"
        f"- **Visible Accounting:** {entry['darkness_remainder']['visible_accounting']}\n"
        f"- **Hidden Remainder:** {entry['darkness_remainder']['hidden_remainder']}\n"
        f"- **One-Line Lock:** *{entry['one_line_lock']}*\n"
    )
