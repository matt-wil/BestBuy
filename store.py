from typing import List, Tuple
from products import Product


class Store:
    """
    A class representing a store that holds a list of products.
    Provides methods for managing products, including adding, removing,
    viewing total quantities, getting active products, and placing orders.
    """
    def __init__(self, list_of_products: List[Product]):
        """
        initialising the store with a list of products.
        :param list_of_products: (List[Product]) a list of Product(objects) to initialise the store
        """
        self.list_of_products = list_of_products

    def add_product(self, product: Product):
        """
        adds a Product to the stores list of products
        :param product: Product(object) the product to be added to the store
        """
        self.list_of_products.append(product)

    def remove_product(self, product: Product):
        """
        removes a product from the stores list of products.
        :param product: Product(object) the product to be removed from the store
        """
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        :return: (int) total number of items in the store
        """
        total = 0
        for product in self.list_of_products:
            total += product.quantity
        return total

    def get_all_products(self) -> List[Product]:
        """
        returns a list of all the active products currently in the store.
        :return: (List[Product]) a list of active Product(object) in the store.
        """
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list: List[Tuple[Product, int]]) -> float:  # shopping_list = [(bose, 5),(mac, 30),(bose, 10)]:
        """
        Processing an order of multiple products from the store.
        the method receives a list of tuples containing the [(Product(object), (int)quantity)] of the purchase.
        calculating the total cost of the order and returning that number as a float.
        :param shopping_list: (List[Tuple[Product, int]]) a list of tuples containing the [(product, quantity)]
        :return: (float) total cost of the complete order.
        """
        total_cost = 0.00
        for product, amount in shopping_list:
            total_cost += product.buy(amount)
        return total_cost


