"""FastAPI surface for the HTE Resonance Observatory.

Run locally:
    uvicorn hte_observatory.api:app --reload
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .harmonic import build_hte_signature
from .ledger import build_run_ledger

app = FastAPI(
    title="HTE Resonance Observatory API",
    version="0.1.0",
    description="Formula parsing, HTE harmonic signatures, and experiment ledgers.",
)


class FormulaRequest(BaseModel):
    formula: str = Field(..., examples=["SiO2"])
    source: str = Field(default="api_manual_input")
    notes: str = Field(default="")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "hte-resonance-observatory"}


@app.post("/signature")
def signature(request: FormulaRequest) -> dict:
    return build_hte_signature(request.formula)


@app.post("/ledger")
def ledger(request: FormulaRequest) -> dict:
    return build_run_ledger(request.formula, source=request.source, notes=request.notes)
