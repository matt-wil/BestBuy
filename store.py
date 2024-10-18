from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, list_of_products: List[Product]):
        self.list_of_products = list_of_products

    def add_product(self, product: Product):
        self.list_of_products.append(product)

    def remove_product(self, product: Product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.list_of_products:
            total += product.quantity
        return total

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list: List[Tuple[Product, int]]) -> float:  # shopping_list = [(bose, 5),(mac, 30),(bose, 10)]:
        total_cost = 0.00
        for product, amount in shopping_list:
            total_cost += product.buy(amount)
        return total_cost


