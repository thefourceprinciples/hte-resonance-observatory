from TPAC.reference.replay import (
    event_hash,
    inject_delete,
    inject_duplicate,
    inject_payload_mutation,
    inject_reorder,
    replay,
)


def make_events():
    events = []
    previous = "0" * 64
    for kind, payload in [
        ("resource_registered", {"resource_id": "r1", "capacity": 1}),
        ("calibration_recorded", {"resource_id": "r1", "status": "valid"}),
        ("claim_recorded", {"claim_id": "c1", "value": 42}),
    ]:
        event = {"kind": kind, "payload": payload, "previous_hash": previous}
        event["hash"] = event_hash(event)
        previous = event["hash"]
        events.append(event)
    return events


def test_valid_history_replays():
    result = replay(make_events())
    assert result.valid
    assert result.state["resources"]["r1"]["capacity"] == 1
    assert result.state["claims"][0]["claim_id"] == "c1"


def test_deleted_event_is_detected():
    result = replay(inject_delete(make_events(), 1))
    assert not result.valid


def test_duplicate_event_is_detected():
    result = replay(inject_duplicate(make_events(), 1))
    assert not result.valid


def test_reordered_events_are_detected():
    result = replay(inject_reorder(make_events(), 0, 1))
    assert not result.valid


def test_payload_mutation_is_detected():
    result = replay(inject_payload_mutation(make_events(), 2, "value", 99))
    assert not result.valid
