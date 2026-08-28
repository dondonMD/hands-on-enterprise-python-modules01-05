# Module 4 — Data-Intensive Applications I: Efficient Data Structures & Memory

**Learning outcomes:** choose appropriate data structures for large datasets; write memory-efficient, streaming Python code.

**Topics:** Big-O refresher; generators and `itertools` for streaming; `__slots__` and memory-conscious classes; measuring memory with `tracemalloc`.

## Activity

Open `activity/streaming.py`. `load_orders_eager` loads an entire CSV into a `list` — it works, but it doesn't scale to a multi-gigabyte nightly file. Implement:

1. **`read_orders_streaming`** — a generator that yields one `OrderRow` at a time instead of building a list.
2. **`batched`** — group any iterable into lists of up to `size` items, with a shorter final batch when the input doesn't divide evenly.

```bash
cd module04-data-intensive-structures-memory
pytest tests/ -v
```

Want to see the memory difference for yourself? Generate a large CSV and compare `load_orders_eager` vs. `total_revenue_streaming` under `tracemalloc` — see Module 4.5 in the course notes.

## Knowledge check

- Why does `read_orders_streaming` keep memory roughly constant regardless of file size, while `load_orders_eager` does not?
- `OrderRow` uses `@dataclass(slots=True)`. What would change if you removed `slots=True`, and when would that trade-off not be worth it?
