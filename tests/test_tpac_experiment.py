from TPAC.reference.experiment import build_reference_run, project_events, run_experiment
from TPAC.reference.replay import replay


def test_reference_experiment_uses_real_integration_run():
    run = build_reference_run()
    result = run.verify()
    assert result["status"] == "PASS"
    assert run.run_id == "TPAC-EXP-001"
    assert len(run.events) == 5


def test_projected_reference_history_replays():
    run = build_reference_run()
    events = project_events(run)
    result = replay(events)
    assert result.valid
    assert result.event_count == len(run.events)
    assert result.state["claims"]


def test_experiment_reports_native_and_replay_success():
    result = run_experiment()
    assert result["native_verification"]["status"] == "PASS"
    assert result["replay"].valid
    assert result["event_log_hash"]
