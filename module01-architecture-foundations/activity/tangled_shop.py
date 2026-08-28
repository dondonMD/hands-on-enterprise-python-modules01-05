"""
Module 1 activity — starting point.

This is a tiny, deliberately tangled single-file "shop" module: business
rules, in-memory storage, and presentation are all mixed together in one
place. Nothing here is broken; it works. Your job is architectural, not
functional (see README.md).
"""


class InvalidOrderError(Exception):
    pass


_ORDERS: dict[str, dict] = {}


def place_order(order_id: str, customer_id: str, lines: list[dict]) -> str:
    # business rule, storage, and formatting all live in one function
    if not lines:
        raise InvalidOrderError("An order must contain at least one line item.")

    total = sum(line["unit_price"] * line["quantity"] for line in lines)
    _ORDERS[order_id] = {
        "customer_id": customer_id,
        "lines": lines,
        "total": total,
    }
    return f"Order {order_id} placed for {customer_id}: ${total:.2f}"


def get_order_summary(order_id: str) -> str:
    order = _ORDERS[order_id]
    return f"Order {order_id}: ${order['total']:.2f} ({len(order['lines'])} line(s))"
