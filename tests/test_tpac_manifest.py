import json

from TPAC.reference.experiment_manifest import build_manifest, stable_hash, write_manifest


def test_stable_hash_is_order_independent():
    assert stable_hash({"b": 2, "a": 1}) == stable_hash({"a": 1, "b": 2})


def test_manifest_contains_reproducibility_fields(tmp_path):
    manifest = build_manifest(
        experiment_id="tpac-smoke-001",
        tpac_version="reference-0.1",
        commit_sha="abc123",
        configuration={"seed": 7, "mode": "deterministic"},
        inputs={"workload": "smoke"},
        event_log_hash="event-hash",
        expected_invariants=["deterministic replay", "provenance integrity"],
        observed_results={"status": "PASS"},
        fault_injections=[{"type": "payload_mutation", "detected": True}],
        replay_result={"status": "PASS"},
        conformance_verdict="PASS",
    )

    path = tmp_path / "manifest.json"
    write_manifest(manifest, str(path))
    data = json.loads(path.read_text())

    assert data["experiment_id"] == "tpac-smoke-001"
    assert data["configuration_hash"] == stable_hash({"seed": 7, "mode": "deterministic"})
    assert data["input_hash"] == stable_hash({"workload": "smoke"})
    assert data["event_log_hash"] == "event-hash"
    assert data["conformance_verdict"] == "PASS"
    assert data["runtime"]["python"]
