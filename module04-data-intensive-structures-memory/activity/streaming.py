"""
Module 4 activity: turn an eager CSV loader into a streaming pipeline.

Northwind Orders receives a nightly CSV of order updates: sku,unit_price,quantity
"""

import csv
import itertools
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


@dataclass(slots=True)
class OrderRow:
    sku: str
    unit_price: float
    quantity: int

    @property
    def line_total(self) -> float:
        return self.unit_price * self.quantity


def load_orders_eager(path: str | Path) -> list[OrderRow]:
    """The starting point: reads the whole file into memory at once."""
    rows = []
    with open(path, newline="") as f:
        for record in csv.DictReader(f):
            rows.append(
                OrderRow(record["sku"], float(record["unit_price"]), int(record["quantity"]))
            )
    return rows


def read_orders_streaming(path: str | Path) -> Iterator[OrderRow]:
    """
    TODO: a generator version of load_orders_eager. It must `yield` one
    OrderRow at a time rather than building a list, so the caller can
    process a file far larger than available memory.
    """
    raise NotImplementedError
    yield  # pragma: no cover  (keeps this a generator function once you edit it)


def batched(iterable: Iterable[OrderRow], size: int) -> Iterator[list[OrderRow]]:
    """
    TODO: yield successive lists of up to `size` items from `iterable`.
    The last batch may be shorter than `size`. An empty iterable yields
    nothing at all.

    Hint: itertools.islice(iterator, size) is useful here.
    """
    raise NotImplementedError
    yield  # pragma: no cover


def total_revenue_streaming(path: str | Path) -> float:
    """Already implemented, once read_orders_streaming works: constant-memory sum."""
    return sum(row.line_total for row in read_orders_streaming(path))
