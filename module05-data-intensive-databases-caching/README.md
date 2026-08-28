# Module 5 — Data-Intensive Applications II: Databases, Batching & Caching at Scale

**Learning outcomes:** design data-access code that scales; apply batching, pooling, and caching strategies.

**Topics:** ORMs vs. raw SQL; connection pooling; the N+1 query problem; bulk operations and keyset pagination; read-through caching with Redis.

## Activity

`activity/data_access.py` uses a `FakeDatabase` that counts every round-trip in `query_count`, standing in for the query log you'd watch against a real Postgres instance. Implement:

1. **`get_orders_fixed`** — the same result as `get_orders_naive`, but in exactly one query instead of 1+N.
2. **`paginate_keyset`** — `WHERE id > :after_id ORDER BY id LIMIT :limit`, implemented over a plain list.
3. **`get_order_lines_cached`** — read-through caching: check `SimpleCache` first, fall back to the database on a miss, and populate the cache.

```bash
cd module05-data-intensive-databases-caching
pytest tests/ -v
```

**Using this against a real database:** swap `FakeDatabase` for a SQLAlchemy `Session`, replace `get_all_orders_with_lines_eager` with `select(OrderModel).options(selectinload(OrderModel.lines))`, and replace `SimpleCache` with a `redis.Redis` client using `cache.set(key, value, ex=300)` for a 5-minute TTL — see Module 5.3 and 5.5 in the course notes for the full code.

## Knowledge check

- Why does `get_orders_naive` issue `1 + N` queries, and what does that cost look like at 10,000 orders instead of 5?
- What's the risk of caching without a TTL — and how would you add one to `SimpleCache`?
