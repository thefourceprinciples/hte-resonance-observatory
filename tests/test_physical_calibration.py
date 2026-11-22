"""Automated physical calibration & soft-state tests for HTE Observatory v0.3."""

import math

from hte_observatory.elements import ELEMENT_TABLE, element_coordinates
from hte_observatory.harmonic import build_hte_signature


def test_full_element_table_has_valence_and_electronegativity() -> None:
    assert len(ELEMENT_TABLE) == 119  # E0 + Z=1..118
    e0 = element_coordinates("E0")
    assert e0.Z == 0
    assert e0.valence == 0
    assert e0.electronegativity == 0.0

    oxygen = element_coordinates("O")
    assert oxygen.Z == 8
    assert oxygen.valence == 6
    assert math.isclose(oxygen.electronegativity, 3.44, rel_tol=1e-4)


def test_bond_polarity_tracks_chemical_ionicity() -> None:
    fe = build_hte_signature("Fe", mapping_mode="group")
    sio2 = build_hte_signature("SiO2", mapping_mode="group")
    batio3 = build_hte_signature("BaTiO3", mapping_mode="group")

    assert fe["physical_metrics"]["delta_chi"] == 0.0
    assert sio2["physical_metrics"]["delta_chi"] < batio3["physical_metrics"]["delta_chi"]
    assert batio3["state_probabilities"]["PIEZO_TENSION"] > fe["state_probabilities"]["PIEZO_TENSION"]


def test_soft_state_probabilities_sum_to_one_across_doping_series() -> None:
    for oxygen_stoich in ("6.0", "6.5", "6.9", "7.0"):
        sig = build_hte_signature(f"YBa2Cu3O{oxygen_stoich}", mapping_mode="group")
        probs = sig["state_probabilities"]
        assert len(probs) == 7
        assert math.isclose(sum(probs.values()), 1.0, abs_tol=1e-4)
        assert sig["discovery_state"] in probs
        assert sig["claim_boundary"] == "derived_hte_mapping_only"


def test_electronegativity_and_valence_weight_modes() -> None:
    sig_stoich = build_hte_signature("BaTiO3", mapping_mode="group", weight_mode="stoich")
    sig_chi = build_hte_signature("BaTiO3", mapping_mode="group", weight_mode="electronegativity")
    sig_val = build_hte_signature("BaTiO3", mapping_mode="group", weight_mode="valence")

    assert sig_stoich["weight_mode"] == "stoich"
    assert sig_chi["weight_mode"] == "electronegativity"
    assert sig_val["weight_mode"] == "valence"
    assert sig_stoich["modal_field"]["fource_lock"] != sig_chi["modal_field"]["fource_lock"]
    assert "modal_field_chi" in sig_stoich
