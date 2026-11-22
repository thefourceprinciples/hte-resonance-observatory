"""Chemical formula parser for the HTE Observatory (v0.2).

Supported:
- element symbols: H, Si, Fe, Og (Z=1..118)
- Element-0 substrate symbol: E0 (Z=0)
- integer and fractional occupancy counts: H2, Fe2O3, YBa2Cu3O6.9
- grouped expressions: Ca10(PO4)6(OH)2

Out of scope:
- hydrates, charges, isotopes, and aliases (belong in Materials Atlas layer).
"""

from __future__ import annotations

import re
from collections import defaultdict

from .elements import ELEMENT_Z

_TOKEN_RE = re.compile(r"(E0|[A-Z][a-z]?|\(|\)|\d+\.\d+|\d+)")


def _parse_number(tok: str) -> int | float:
    return float(tok) if "." in tok else int(tok)


def _is_number(tok: str) -> bool:
    return tok.isdigit() or bool(re.fullmatch(r"\d+\.\d+", tok))


def parse_formula(formula: str) -> dict[str, int | float]:
    """Parse a chemical formula into {element_symbol: count}.

    Preserves integer counts for whole-number stoichiometries while supporting
    fractional doping (e.g., YBa2Cu3O6.9) and the Element-0 substrate (E0).
    """
    clean = formula.strip()
    if not clean:
        raise ValueError("Formula cannot be empty")

    tokens = _TOKEN_RE.findall(clean)
    if "".join(tokens) != clean:
        raise ValueError(f"Unsupported formula syntax: {formula}")

    stack: list[defaultdict[str, int | float]] = [defaultdict(int)]
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "(":
            stack.append(defaultdict(int))
            i += 1
            continue

        if token == ")":
            if len(stack) == 1:
                raise ValueError(f"Unmatched closing parenthesis in: {formula}")
            group = stack.pop()
            multiplier: int | float = 1
            if i + 1 < len(tokens) and _is_number(tokens[i + 1]):
                multiplier = _parse_number(tokens[i + 1])
                i += 1
            for symbol, count in group.items():
                val = count * multiplier
                stack[-1][symbol] += int(val) if isinstance(val, float) and val.is_integer() else val
            i += 1
            continue

        if _is_number(token):
            raise ValueError(f"Dangling multiplier {token} in: {formula}")

        symbol = token
        if symbol not in ELEMENT_Z:
            raise ValueError(f"Unknown element symbol: {symbol}")
        count: int | float = 1
        if i + 1 < len(tokens) and _is_number(tokens[i + 1]):
            count = _parse_number(tokens[i + 1])
            i += 1
        val = stack[-1][symbol] + count
        stack[-1][symbol] = int(val) if isinstance(val, float) and val.is_integer() else val
        i += 1

    if len(stack) != 1:
        raise ValueError(f"Unmatched opening parenthesis in: {formula}")

    return dict(stack[0])
