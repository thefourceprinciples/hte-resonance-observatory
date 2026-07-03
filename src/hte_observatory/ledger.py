"""Experiment ledger helpers for HTE Observatory runs."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from .harmonic import build_hte_signature


CLAIM_LADDER = {
    "L0": "raw_input",
    "L1": "parsed_formula",
    "L2": "derived_hte_mapping",
    "L3": "matched_material_data",
    "L4": "statistical_correlation",
    "L5": "experimentally_replicated_or_source_backed",
}


def build_run_ledger(formula: str, source: str = "manual_input", notes: str = "") -> dict:
    """Create a versioned run ledger for one HTE mapping session."""
    signature = build_hte_signature(formula)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return {
        "run_id": f"HTE-RUN-{uuid4().hex[:10].upper()}",
        "created_at": now,
        "observatory_version": "0.1.0",
        "source": source,
        "formula": formula,
        "signature": signature,
        "claim_level": "L2",
        "claim_level_label": CLAIM_LADDER["L2"],
        "evidence_boundary": (
            "This ledger records an HTE-derived exploratory mapping. It does not establish "
            "a conventional material property without external data or experiment."
        ),
        "notes": notes,
    }


def ledger_to_markdown(ledger: dict) -> str:
    """Render a run ledger as simple Markdown for GitHub or Google Docs export."""
    sig = ledger["signature"]
    lines = [
        f"# {ledger['run_id']}",
        "",
        f"- Created: {ledger['created_at']}",
        f"- Formula: `{ledger['formula']}`",
        f"- Source: {ledger['source']}",
        f"- Claim level: {ledger['claim_level']} / {ledger['claim_level_label']}",
        f"- Overlay state: {sig['overlay_state']}",
        "",
        "## Composition",
        "",
    ]
    for symbol, count in sig["composition"].items():
        lines.append(f"- {symbol}: {count}")
    lines.extend([
        "",
        "## HTE signature",
        "",
        f"- Mapping rule: `{sig['mapping_rule']}`",
        f"- Weighted chord: `{sig['weighted_chord']}`",
        f"- Pitch-class histogram: `{sig['pitch_class_histogram']}`",
        f"- Interval walk: `{sig['interval_walk']}`",
        "",
        "## Evidence boundary",
        "",
        ledger["evidence_boundary"],
    ])
    if ledger.get("notes"):
        lines.extend(["", "## Notes", "", ledger["notes"]])
    return "\n".join(lines) + "\n"
