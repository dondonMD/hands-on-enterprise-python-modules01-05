import csv
import inspect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "activity"))

from streaming import (  # noqa: E402
    OrderRow,
    batched,
    read_orders_streaming,
    total_revenue_streaming,
)


def _write_sample_csv(path: Path, n: int = 5) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sku", "unit_price", "quantity"])
        for i in range(n):
            writer.writerow([f"SKU-{i}", "10.00", str(i + 1)])


def test_read_orders_streaming_is_a_generator_function():
    assert inspect.isgeneratorfunction(read_orders_streaming)


def test_read_orders_streaming_reads_rows_correctly(tmp_path):
    csv_path = tmp_path / "orders.csv"
    _write_sample_csv(csv_path, n=3)

    rows = list(read_orders_streaming(csv_path))

    assert rows == [
        OrderRow("SKU-0", 10.0, 1),
        OrderRow("SKU-1", 10.0, 2),
        OrderRow("SKU-2", 10.0, 3),
    ]


def test_total_revenue_streaming(tmp_path):
    csv_path = tmp_path / "orders.csv"
    _write_sample_csv(csv_path, n=3)
    # totals: 10*1 + 10*2 + 10*3 = 60
    assert total_revenue_streaming(csv_path) == 60.0


def test_batched_groups_with_partial_last_batch():
    rows = [OrderRow(f"SKU-{i}", 1.0, 1) for i in range(5)]
    batches = list(batched(rows, 2))
    assert [len(b) for b in batches] == [2, 2, 1]
    assert batches[0] == rows[0:2]
    assert batches[-1] == rows[4:5]


def test_batched_empty_input_yields_nothing():
    assert list(batched([], 10)) == []
