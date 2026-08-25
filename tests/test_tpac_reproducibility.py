from TPAC.reference.reproducibility import run_reproducibility_check


def test_reference_experiment_is_deterministically_reproducible():
    result = run_reproducibility_check()
    assert result.reproducible is True
    assert result.first_hash == result.second_hash
    assert result.differences == ()
