import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "activity"))

from pricing import (  # noqa: E402
    BulkDiscountPricing,
    Checkout,
    OrderEvents,
    SimpleOrder,
    StandardPricing,
)


def test_bulk_discount_applies_over_threshold():
    strategy = BulkDiscountPricing()
    assert strategy.price(SimpleOrder(600.0)) == 540.0


def test_bulk_discount_not_applied_under_threshold():
    strategy = BulkDiscountPricing()
    assert strategy.price(SimpleOrder(100.0)) == 100.0


def test_checkout_uses_injected_strategy():
    events = OrderEvents()
    checkout = Checkout(pricing=StandardPricing(), events=events)
    assert checkout.total(SimpleOrder(50.0)) == 50.0


def test_checkout_publishes_to_all_subscribers_in_order():
    events = OrderEvents()
    calls = []
    events.subscribe(lambda order, total: calls.append(("email", total)))
    events.subscribe(lambda order, total: calls.append(("inventory", total)))

    checkout = Checkout(pricing=BulkDiscountPricing(), events=events)
    checkout.total(SimpleOrder(1000.0))

    assert calls == [("email", 900.0), ("inventory", 900.0)]
