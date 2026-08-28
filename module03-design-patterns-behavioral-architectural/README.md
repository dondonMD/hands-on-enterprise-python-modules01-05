# Module 3 — Design Patterns II: Behavioral & Architectural Patterns

**Learning outcomes:** apply behavioral patterns to decouple logic; recognize architectural patterns used in enterprise Python systems.

**Topics:** Strategy; Observer; Command; Dependency Injection; the Repository pattern; MVC/MVT in Python web frameworks.

## Activity

Open `activity/pricing.py`. `StandardPricing` is done; implement:

1. **`BulkDiscountPricing.price`** — 10% off orders with `subtotal > 500`, otherwise the plain subtotal.
2. **`OrderEvents.subscribe` / `publish`** — a minimal pub/sub hub; `publish` calls every subscribed handler with `(order, total)`, in subscription order.
3. **`Checkout.total`** — delegates pricing to the injected `PricingStrategy`, publishes the result via the injected `OrderEvents`, and returns the total.

```bash
cd module03-design-patterns-behavioral-architectural
pytest tests/ -v
```

## Knowledge check

- `Checkout` receives both its `PricingStrategy` and its `OrderEvents` through the constructor rather than constructing them itself — why does that matter for testing (see Module 9)?
- What would adding a `SeasonalPromotionPricing` strategy require you to change in `Checkout`?
