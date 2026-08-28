"""
Run with:  pytest tests/ -v

These tests exercise the refactored shop.* package, not tangled_shop.py.
They also assert the layering rule itself: shop.domain must not import
shop.infrastructure or shop.api.
"""
import ast
import sys
from pathlib import Path

ACTIVITY = Path(__file__).resolve().parents[1] / "activity"
sys.path.insert(0, str(ACTIVITY))

import pytest  # noqa: E402
from shop.domain.orders import InvalidOrderError, order_total, validate_order  # noqa: E402
from shop.infrastructure.repository import InMemoryOrderRepository  # noqa: E402
from shop.api.handlers import get_order_summary, place_order  # noqa: E402


def test_validate_order_rejects_empty():
    with pytest.raises(InvalidOrderError):
        validate_order([])


def test_order_total_sums_lines():
    lines = [{"unit_price": 10.0, "quantity": 2}, {"unit_price": 5.0, "quantity": 1}]
    assert order_total(lines) == 25.0


def test_place_and_summarize_order():
    repo = InMemoryOrderRepository()
    lines = [{"unit_price": 9.99, "quantity": 3}]
    msg = place_order(repo, "o-1", "cust-1", lines)
    assert "o-1" in msg and "cust-1" in msg
    summary = get_order_summary(repo, "o-1")
    assert "o-1" in summary and "1 line(s)" in summary


def test_domain_layer_has_no_outward_imports():
    """The critical rule from Module 1.2: dependencies point inward only."""
    source = (ACTIVITY / "shop" / "domain" / "orders.py").read_text()
    tree = ast.parse(source)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0] + "." + (node.module.split(".")[1] if "." in node.module else ""))
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name)
    forbidden = {name for name in imported if "infrastructure" in name or "api" in name}
    assert not forbidden, f"domain/orders.py must not import: {forbidden}"
