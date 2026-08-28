import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "activity"))

from data_access import (  # noqa: E402
    FakeDatabase,
    SimpleCache,
    get_order_lines_cached,
    get_orders_fixed,
    get_orders_naive,
    paginate_keyset,
)


def _sample_db(n: int = 5) -> FakeDatabase:
    return FakeDatabase({f"o-{i}": [{"sku": "SKU-1", "qty": i}] for i in range(n)})


def test_naive_version_issues_n_plus_one_queries():
    db = _sample_db(5)
    get_orders_naive(db)
    assert db.query_count == 1 + 5  # 1 for the id list, 5 for each order's lines


def test_fixed_version_issues_exactly_one_query():
    db = _sample_db(5)
    result = get_orders_fixed(db)
    assert db.query_count == 1
    assert set(result.keys()) == {f"o-{i}" for i in range(5)}


def test_fixed_and_naive_return_the_same_data():
    assert get_orders_fixed(_sample_db(5)) == get_orders_naive(_sample_db(5))


def test_paginate_keyset_first_page():
    items = [{"id": i, "v": i} for i in range(1, 11)]
    page = paginate_keyset(items, after_id=None, limit=3)
    assert [i["id"] for i in page] == [1, 2, 3]


def test_paginate_keyset_next_page():
    items = [{"id": i, "v": i} for i in range(1, 11)]
    page = paginate_keyset(items, after_id=3, limit=3)
    assert [i["id"] for i in page] == [4, 5, 6]


def test_paginate_keyset_last_partial_page():
    items = [{"id": i, "v": i} for i in range(1, 11)]
    page = paginate_keyset(items, after_id=9, limit=3)
    assert [i["id"] for i in page] == [10]


def test_cache_hit_avoids_a_database_call():
    db = _sample_db(5)
    cache = SimpleCache()

    first = get_order_lines_cached("o-0", db, cache)
    queries_after_first = db.query_count
    second = get_order_lines_cached("o-0", db, cache)

    assert first == second
    assert queries_after_first == 1
    assert db.query_count == 1  # unchanged — the second call was a cache hit
