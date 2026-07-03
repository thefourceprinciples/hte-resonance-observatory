"""Lightweight chemical formula parser for the HTE Observatory.

Supported in v0.1:
- element symbols: H, Si, Fe
- integer counts: H2, Fe2O3
- grouped expressions: Ca10(PO4)6(OH)2

Out of scope for v0.1:
- hydrates, charges, isotopes, fractional occupancy, aliases, and alloys.
Those belong in the Materials Atlas connector layer.
"""

from __future__ import annotations

import re
from collections import defaultdict

from .elements import ELEMENT_Z

_TOKEN_RE = re.compile(r"([A-Z][a-z]?|\(|\)|\d+)")


def parse_formula(formula: str) -> dict[str, int]:
    """Parse a chemical formula into {element_symbol: integer_count}.

    This is deliberately small and auditable. It catches unknown elements and
    unbalanced parentheses rather than trying to be chemically omniscient.
    """
    clean = formula.strip()
    if not clean:
        raise ValueError("Formula cannot be empty")

    tokens = _TOKEN_RE.findall(clean)
    if "".join(tokens) != clean:
        raise ValueError(f"Unsupported formula syntax: {formula}")

    stack: list[defaultdict[str, int]] = [defaultdict(int)]
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
            multiplier = 1
            if i + 1 < len(tokens) and tokens[i + 1].isdigit():
                multiplier = int(tokens[i + 1])
                i += 1
            for symbol, count in group.items():
                stack[-1][symbol] += count * multiplier
            i += 1
            continue

        if token.isdigit():
            raise ValueError(f"Dangling multiplier {token} in: {formula}")

        symbol = token
        if symbol not in ELEMENT_Z:
            raise ValueError(f"Unknown element symbol: {symbol}")
        count = 1
        if i + 1 < len(tokens) and tokens[i + 1].isdigit():
            count = int(tokens[i + 1])
            i += 1
        stack[-1][symbol] += count
        i += 1

    if len(stack) != 1:
        raise ValueError(f"Unmatched opening parenthesis in: {formula}")

    return dict(stack[0])
