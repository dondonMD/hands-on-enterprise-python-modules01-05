"""
Module 5 activity: N+1 queries, keyset pagination, and caching.

Spinning up a real Postgres + Redis for a class activity isn't practical,
so FakeDatabase below plays the role of a database connection: every method
that would hit the network increments `query_count`, which is exactly what
you'd watch in SQLAlchemy's query log in the full lab (see README).
"""

from typing import Optional


class FakeDatabase:
    def __init__(self, orders: dict[str, list[dict]]) -> None:
        # orders: {order_id: [ {"sku": ..., "qty": ...}, ... ]}
        self._orders = orders
        self.query_count = 0

    def get_all_order_ids(self) -> list[str]:
        self.query_count += 1
        return sorted(self._orders.keys())

    def get_lines_for_order(self, order_id: str) -> list[dict]:
        """Simulates one round-trip per call — the N+1 trap."""
        self.query_count += 1
        return self._orders[order_id]

    def get_all_orders_with_lines_eager(self) -> dict[str, list[dict]]:
        """Simulates a single query with a JOIN / selectinload — one round-trip, period."""
        self.query_count += 1
        return dict(self._orders)


def get_orders_naive(db: FakeDatabase) -> dict[str, list[dict]]:
    """Already implemented — this is the N+1 bug you're fixing below."""
    result = {}
    for order_id in db.get_all_order_ids():
        result[order_id] = db.get_lines_for_order(order_id)
    return result


def get_orders_fixed(db: FakeDatabase) -> dict[str, list[dict]]:
    """
    TODO: return the same shape as get_orders_naive — {order_id: [lines]} —
    but using exactly ONE call to db.get_all_orders_with_lines_eager()
    instead of one call per order.
    """
    raise NotImplementedError


def paginate_keyset(items: list[dict], after_id: Optional[int], limit: int) -> list[dict]:
    """
    TODO: `items` is a list of dicts with an "id" key, already sorted
    ascending by id. Return the first `limit` items with id > after_id
    (or the first `limit` items overall, if after_id is None).

    This is the keyset-pagination equivalent of:
        WHERE id > :after_id ORDER BY id LIMIT :limit
    """
    raise NotImplementedError


class SimpleCache:
    """A minimal in-memory cache — already implemented."""

    def __init__(self) -> None:
        self._store: dict[str, list[dict]] = {}

    def get(self, key: str):
        return self._store.get(key)

    def set(self, key: str, value: list[dict]) -> None:
        self._store[key] = value


def get_order_lines_cached(order_id: str, db: FakeDatabase, cache: SimpleCache) -> list[dict]:
    """
    TODO: read-through caching (Module 5.5).

    Check the cache first; on a hit, return the cached value without
    touching `db` at all. On a miss, fetch via db.get_lines_for_order,
    store the result in the cache, and return it.
    """
    raise NotImplementedError
