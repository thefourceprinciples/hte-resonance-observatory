"""FastAPI surface for the HTE Resonance Observatory (v0.2).

Run locally:
    uvicorn hte_observatory.api:app --reload
"""

from __future__ import annotations

import math
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .harmonic import build_hte_signature
from .ledger import build_run_ledger

app = FastAPI(
    title="HTE Resonance Observatory API",
    version="0.2.0",
    description="Formula parsing, CLV-HTE-001 modal coherence signatures, A/B comparison, and experiment ledgers.",
)


class FormulaRequest(BaseModel):
    formula: str = Field(..., examples=["SiO2"])
    mapping_mode: Literal["raw", "group"] = Field(default="raw")
    source: str = Field(default="api_manual_input")
    notes: str = Field(default="")


class CompareRequest(BaseModel):
    formula_a: str = Field(..., examples=["YBa2Cu3O6.0"])
    formula_b: str = Field(..., examples=["YBa2Cu3O7.0"])
    mapping_mode: Literal["raw", "group"] = Field(default="group")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "hte-resonance-observatory", "version": "0.2.0"}


@app.post("/signature")
def signature(request: FormulaRequest) -> dict:
    try:
        return build_hte_signature(request.formula, mapping_mode=request.mapping_mode)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/ledger")
def ledger(request: FormulaRequest) -> dict:
    try:
        return build_run_ledger(
            request.formula,
            source=request.source,
            notes=request.notes,
            mapping_mode=request.mapping_mode,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/compare")
def compare(request: CompareRequest) -> dict:
    try:
        sig_a = build_hte_signature(request.formula_a, mapping_mode=request.mapping_mode)
        sig_b = build_hte_signature(request.formula_b, mapping_mode=request.mapping_mode)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    hm_a = [val for row in sig_a["modal_field"]["heatmap_12x7"] for val in row]
    hm_b = [val for row in sig_b["modal_field"]["heatmap_12x7"] for val in row]
    norm_a = math.sqrt(sum(x * x for x in hm_a))
    norm_b = math.sqrt(sum(x * x for x in hm_b))
    cosine_sim = sum(a * b for a, b in zip(hm_a, hm_b)) / (norm_a * norm_b) if (norm_a > 0 and norm_b > 0) else 0.0

    f_a = sig_a["modal_field"]["fource_lock"]
    f_b = sig_b["modal_field"]["fource_lock"]
    c_a = sig_a["modal_field"]["c_modal"]
    c_b = sig_b["modal_field"]["c_modal"]

    return {
        "mapping_mode": request.mapping_mode,
        "formula_a": request.formula_a,
        "formula_b": request.formula_b,
        "heatmap_cosine_similarity": round(cosine_sim, 6),
        "delta_fource": round(f_b - f_a, 6),
        "delta_c_modal": round(c_b - c_a, 6),
        "signature_a": sig_a,
        "signature_b": sig_b,
    }
