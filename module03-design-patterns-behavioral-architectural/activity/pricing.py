"""
Module 3 activity: Strategy + Observer.

Northwind Orders needs a pluggable pricing engine (Strategy) that notifies
interested parties whenever an order is priced (Observer).
"""

from typing import Protocol


class Order(Protocol):
    subtotal: float


class SimpleOrder:
    def __init__(self, subtotal: float) -> None:
        self.subtotal = subtotal


class PricingStrategy(Protocol):
    def price(self, order: Order) -> float: ...


class StandardPricing:
    """Already implemented — no discount, just the subtotal."""

    def price(self, order: Order) -> float:
        return order.subtotal


class BulkDiscountPricing:
    """
    TODO: 10% off orders with a subtotal over $500, otherwise no discount.
    """

    def price(self, order: Order) -> float:
        raise NotImplementedError


class Checkout:
    """
    TODO: total(order) should delegate to self._pricing.price(order) and
    then call self._events.publish(order, total) before returning the total.
    """

    def __init__(self, pricing: PricingStrategy, events: "OrderEvents") -> None:
        self._pricing = pricing
        self._events = events

    def total(self, order: Order) -> float:
        raise NotImplementedError


class OrderEvents:
    """
    TODO: a minimal publish/subscribe hub.

    - subscribe(handler): remember a handler (any callable taking
      (order, total)).
    - publish(order, total): call every subscribed handler with
      (order, total), in the order they subscribed.
    """

    def __init__(self) -> None:
        self._subscribers: list = []

    def subscribe(self, handler) -> None:
        raise NotImplementedError

    def publish(self, order: Order, total: float) -> None:
        raise NotImplementedError
