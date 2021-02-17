from typing import List

from src.model import Stock, Item


class Checkout:
    operative: str
    current_stock_list: dict

    def __init__(self, operative_name: str) -> None:
        self.operative = operative_name
        self.current_stock_list = {}
        print(f"'{operative_name}' is ready for work!")

    def create_lookup(self, stock_list: List[Stock]) -> None:
        self.current_stock_list = {item.SKU: item for item in stock_list}

    def count_items(self):
        return len(self.current_stock_list)

    def basic_sub_total(self, basket: List[Item]) -> float:
        return sum([self.current_stock_list.get(item.SKU).UnitPrice for item in basket])
