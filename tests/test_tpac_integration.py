from TPAC.reference.integration import Resource, TPACRun


def build_valid_run() -> TPACRun:
    run = TPACRun("TPAC-TEST-001")
    run.register_resource(Resource("r1", "reference-execution"))
    run.schedule("r1", "smoke-test")
    run.execute("r1", "smoke-test", measurement=42)
    run.create_claim("The smoke test produced a recorded measurement.", evidence_event=4)
    return run


def test_end_to_end_vertical_slice_verifies():
    result = build_valid_run().verify()
    assert result["status"] == "PASS"
    assert result["event_count"] == 5
    assert result["claim_count"] == 1


def test_uncalibrated_resource_is_rejected():
    run = TPACRun("TPAC-TEST-002")
    try:
        run.register_resource(Resource("r1", "reference-execution", calibrated=False))
    except ValueError as exc:
        assert "not calibrated" in str(exc)
    else:
        raise AssertionError("uncalibrated resource was accepted")


def test_tampered_event_fails_verification():
    run = build_valid_run()
    run.events[2] = run.events[2].__class__(
        sequence=run.events[2].sequence,
        kind=run.events[2].kind,
        payload={"resource_id": "r1", "workload": "tampered"},
        digest=run.events[2].digest,
    )
    result = run.verify()
    assert result["status"] == "FAIL"
    assert any("digest mismatch" in failure for failure in result["failures"])
