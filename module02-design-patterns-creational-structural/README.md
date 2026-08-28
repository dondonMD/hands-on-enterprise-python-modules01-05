# Module 2 — Design Patterns I: Creational & Structural Patterns

**Learning outcomes:** explain the purpose of design patterns and identify when (and when not) to use one; implement creational and structural patterns in idiomatic Python.

**Topics:** why design patterns exist and their cost/benefit trade-offs; Factory Method; Builder; Singleton (and why Python modules often replace it); Adapter; Decorator; Facade.

## Activity

Open `activity/payments.py`. `ModernGateway` already satisfies the `PaymentGateway` protocol directly. `LegacyPaymentSdk` is a stand-in for a third-party SDK with an incompatible method shape (`make_payment(cents, card_token) -> dict`).

Implement:

1. **`LegacyPaymentAdapter.charge`** — adapt the legacy SDK's shape to `PaymentGateway`: convert `amount` (dollars, float) to an integer number of cents, call `self._sdk.make_payment(...)`, and return the `"ok"` value.
2. **`payment_gateway_factory(provider)`** — a Factory that returns a `ModernGateway()` for `"modern"`, a `LegacyPaymentAdapter` wrapping a fresh `LegacyPaymentSdk()` for `"legacy"`, and raises `ValueError` otherwise.

```bash
cd module02-design-patterns-creational-structural
pytest tests/ -v
```

## Knowledge check

- Why is `PaymentGateway` a `Protocol` rather than an abstract base class both providers must inherit from?
- If Northwind Orders adds a third payment provider next quarter, which files change — and which don't?
