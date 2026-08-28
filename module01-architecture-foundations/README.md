# Module 1 — Foundations of Enterprise Application Architecture

**Learning outcomes:** describe what distinguishes "enterprise-grade" software from a script; explain layered architecture and separation of concerns; refresh SOLID principles.

**Topics:** the five qualities of enterprise software; layered architecture (presentation, application, domain, infrastructure); the dependency-direction rule; coupling and cohesion; a SOLID refresher.

## Activity

`activity/tangled_shop.py` is a working single-file shop: business rules, storage, and formatting are all mixed into two functions. It isn't broken — but it's exactly the shape Module 1.2 warns about.

Refactor it into the `activity/shop/` package, split by responsibility:

- `shop/domain/orders.py` — `InvalidOrderError`, `validate_order(lines)`, `order_total(lines)`. **No imports from `infrastructure` or `api`.**
- `shop/infrastructure/repository.py` — `InMemoryOrderRepository` with `save()`/`get()`.
- `shop/api/handlers.py` — `place_order(repo, ...)` and `get_order_summary(repo, ...)`, producing the same output strings `tangled_shop.py` did.

Then check your work:

```bash
cd module01-architecture-foundations
pytest tests/ -v
```

One test (`test_domain_layer_has_no_outward_imports`) checks the architecture itself, not just behavior — it fails if `shop/domain/orders.py` imports anything from `infrastructure` or `api`.

## Knowledge check

- Why must dependencies point inward toward the domain layer, and not outward?
- Where would you add a new `PostgresOrderRepository` later — and why would that change never touch `shop/domain/orders.py`?
