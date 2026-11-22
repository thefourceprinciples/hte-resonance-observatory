"""Automated verification of the Materials Atlas Engine (MAE) across all 119 elements."""

from hte_observatory.atlas import build_element_atlas_entry, render_atlas_markdown
from hte_observatory.elements import ELEMENT_TABLE


def test_element_zero_canonical_matlas_entry() -> None:
    e0 = build_element_atlas_entry("E0")
    assert e0["entry_id"] == "MATLAS-E000-SUBSTRATE"
    assert e0["status"] == "canonical_draft"
    assert e0["hte_signature"]["coordinate_raw"]["tuple"] == [0, 0]
    assert "None" in e0["core_identity"]["isotopes"][0]


def test_hydrogen_canonical_matlas_entry() -> None:
    h_entry = build_element_atlas_entry("H", entry_date="2026-05-04")
    assert h_entry["entry_id"] == "MATLAS-E001-HYDROGEN"
    assert h_entry["status"] == "canonical_draft"
    assert h_entry["hte_signature"]["coordinate_raw"]["tuple"] == [1, 1]
    assert h_entry["hte_signature"]["c_hte_unison"] == 1.0
    assert h_entry["fifth_ladder"]["pathway_text"] == "H -> O -> P -> Ti -> Cu -> Kr"
    assert len(h_entry["state_activation"]) == 7

    md = render_atlas_markdown(h_entry)
    assert "MATLAS-E001-HYDROGEN" in md
    assert "H -> O -> P -> Ti -> Cu -> Kr" in md


def test_all_119_elements_generate_valid_atlas_entries() -> None:
    for symbol in ELEMENT_TABLE:
        entry = build_element_atlas_entry(symbol)
        assert entry["core_identity"]["symbol"] == symbol
        assert len(entry["fifth_ladder"]["sequence"]) >= 1
        assert len(entry["state_activation"]) == 7
        assert entry["claim_boundary"] == "derived_hte_mapping_only"
