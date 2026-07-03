"""HTE Resonance Observatory core package.

This package contains the grounded computational spine for the Observatory:
formula parsing, atomic-number-to-pitch-class mapping, harmonic signatures,
claim-boundary labels, and experiment ledger exports.
"""

from .formula import parse_formula
from .harmonic import build_hte_signature
from .ledger import build_run_ledger

__all__ = ["parse_formula", "build_hte_signature", "build_run_ledger"]
