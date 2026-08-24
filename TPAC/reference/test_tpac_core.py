import unittest

from tpac_core import (
    Calibration,
    CalibrationState,
    Event,
    ProvenanceGraph,
    Resource,
    ResourceState,
    Scheduler,
    Workload,
    validate_calibration,
)


class TPACCoreTests(unittest.TestCase):
    def test_scheduler_is_deterministic(self):
        resources = [
            Resource("r-02", {"compute"}, ResourceState.AVAILABLE),
            Resource("r-01", {"compute"}, ResourceState.AVAILABLE),
        ]
        selected, reason = Scheduler().select(Workload("w-1", frozenset({"compute"})), resources)
        self.assertEqual(reason, "ALLOCATED")
        self.assertEqual(selected.resource_id, "r-01")

    def test_scheduler_rejects_missing_capability(self):
        resource = Resource("r-01", {"storage"}, ResourceState.AVAILABLE)
        selected, reason = Scheduler().select(Workload("w-1", frozenset({"compute"})), [resource])
        self.assertIsNone(selected)
        self.assertEqual(reason, "NO_VALID_RESOURCE")

    def test_provenance_requires_existing_predecessors(self):
        graph = ProvenanceGraph()
        with self.assertRaises(ValueError):
            graph.append(Event("e-2", "RESULT", "w-1", ("e-1",)))

    def test_provenance_lineage_is_reconstructable(self):
        graph = ProvenanceGraph()
        graph.append(Event("e-1", "INPUT", "w-1"))
        graph.append(Event("e-2", "EXECUTION", "w-1", ("e-1",)))
        graph.append(Event("e-3", "RESULT", "w-1", ("e-2",)))
        self.assertEqual(graph.lineage("e-3"), ["e-1", "e-2", "e-3"])

    def test_invalid_calibration_cannot_validate(self):
        calibration = Calibration(
            "cal-1", "r-1", CalibrationState.INVALID, "2026-01-01", "2027-01-01", "reference"
        )
        self.assertFalse(validate_calibration(calibration))


if __name__ == "__main__":
    unittest.main()
