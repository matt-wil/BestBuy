from typing import List, Tuple
from products import Product, NonStockedProduct


class Store:
    """
    A class representing a store that holds a list of products.
    Provides methods for managing products, including adding, removing,
    viewing total quantities, getting active products, and placing orders.

    Attributes:
        list_of_products (List[Product]): A list of products available in the store.

    Methods:
        __init__(list_of_products):
            Initializes the store with a list of products.

        add_product(product):
            Adds a product to the store's list of products.

        remove_product(product):
            Removes a product from the store's list of products if it exists.

        get_total_quantity():
            Returns the total quantity of all stockable products in the store.

        get_all_products():
            Returns a list of active products in the store.

        order(shopping_list):
            Processes an order of multiple products and calculates the total cost.

        __contains__(item):
            Checks if a specific product is available in the store.

        __add__(other):
            Combines the products of two stores into a new store instance.
    """
    def __init__(self, list_of_products: List[Product]):
        """
        Initialising the store with a list of products.

        :arg:
            list_of_products: (List[Product]) a list of Product(objects) to initialise the store
        """
        self.list_of_products = list_of_products

    def add_product(self, product: Product):
        """
        Adds a Product to the stores list of products

        :arg:
            product: Product(object) the product to be added to the store
        """
        self.list_of_products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the stores list of products.

        :arg:
            product: Product(object) the product to be removed from the store
        """
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        :return:
            (int) total number of items in the store
        """
        total = 0
        for product in self.list_of_products:
            if isinstance(product, NonStockedProduct):
                continue  # skip the non-stocked products
            total += product._quantity
        return total

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all the active products currently in the store.

        :return:
            (List[Product]) a list of active Product(object) in the store.
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

        :arg:
            shopping_list: (List[Tuple[Product, int]]) a list of tuples containing the [(product, quantity)]

        :return:
            (float) total cost of the complete order.
        """
        total_cost = 0.00
        for product, amount in shopping_list:
            total_cost += product.buy(amount)
        return total_cost

    # dunder methods
    def __contains__(self, item):
        """
        Checks if a product is in the stores list of products.

        :arg:
            item: (Product) The product to the check for in the store

        :return:
            (bool) True if the product is in the store else False
        """
        return item in self.list_of_products

    def __add__(self, other):
        """
        Combines the products from two store creating a new Store object

        :arg:
            other: (Store) the other store instance to combine with this store

        :return:
            (Store) a new Store instance containing the products from both stores
        """
        combined_stores = self.list_of_products + other.list_of_products
        return Store(combined_stores)
