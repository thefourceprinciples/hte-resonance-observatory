from hte_observatory import build_hte_signature, parse_formula
from hte_observatory.ledger import build_run_ledger


def test_parse_simple_formula():
    assert parse_formula("SiO2") == {"Si": 1, "O": 2}


def test_parse_grouped_formula():
    assert parse_formula("Ca10(PO4)6(OH)2") == {"Ca": 10, "P": 6, "O": 26, "H": 2}


def test_build_signature_uses_atomic_number_mod_12():
    signature = build_hte_signature("SiO2")
    assert signature["pitch_class_histogram"] == {"2": 1, "8": 2}
    assert signature["mapping_rule"] == "pitch_class = atomic_number mod 12"
    assert signature["claim_boundary"] == "derived_hte_mapping_only"


def test_ledger_claim_boundary():
    ledger = build_run_ledger("H2O")
    assert ledger["claim_level"] == "L2"
    assert "does not establish" in ledger["evidence_boundary"]
