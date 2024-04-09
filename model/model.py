from dataclasses import dataclass
from typing import List


class Transaction:
    def __init__(
        self, name: str, count: int, unit_price: float, tax: float, subtotal: float
    ):
        self.name = name
        self.count = count
        self.unit_price = unit_price
        self.subtotal = subtotal
        self.tax = tax


class Bill:
    def __init__(self, id: int, line_items: List[Transaction]):
        self.id = id
        self.line_items = line_items
        self.total = 0
        self.total_taxes = 0
        self.count_items = 0
        for item in self.line_items:
            self.total += item.subtotal
            self.total_taxes += item.tax
            self.count_items += item.count

    def to_dict(self):
        return {
            "id": self.id,
            "line_items": [
                f"{item.name},{item.count},{item.unit_price}"
                for item in self.line_items
            ],
            "total": self.total,
            "total_taxes": self.total_taxes,
            "count_items": self.count_items,
        }
