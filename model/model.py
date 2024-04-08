from dataclasses import dataclass
from typing import List




class Transaction:
    def __init__(self, name: str, count: int, unit_price: float, subtotal: float):
        self.name = name
        self.count = count
        self.unit_price = unit_price
        self.subtotal = subtotal
    
class Bill:
    def __init__(self,id:int, total: float, total_taxes: float, count_items: int, line_items: List[Transaction]):
        self.id = id
        self.total = total
        self.total_taxes = total_taxes
        self.count_items = count_items
        self.line_items = line_items
