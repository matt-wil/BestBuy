import math
from promotions import Promotion


class Product:
    """
    This class represents a product in a store's inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The current stock quantity of the product.
        active (bool): Indicates whether the product is active (available for purchase).
        promotion (Promotion or None): The promotion applied to the product, if any.

    Methods:
        __init__(name, price, quantity):
            Initializes a new product with the given attributes. Raises ValueError if any attribute is invalid.

        get_quantity():
            Returns the current quantity of the product.

        set_quantity(quantity):
            Sets the quantity of the product. Deactivates the product if quantity becomes 0 or less.

        is_active():
            Returns True if the product is active (available for purchase), False otherwise.

        activate():
            Activates the product, making it available for purchase.

        deactivate():
            Deactivates the product, making it unavailable for purchase.

        show():
            Returns a string representation of the product (name, price, and quantity).

        buy(quantity):
            Processes a purchase of the given quantity of the product, updating stock. Raises ValueError if quantity is invalid or exceeds available stock.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes the product with the given name, price, and quantity.

        :arg:
            name (str): The name of the product.
            price (float): The price of the product (must be greater than 0).
            quantity (int): The quantity of the product (must be greater than 0).

        :raises:
            ValueError: If any of the attributes (name, price, or quantity) are invalid.
        """
        self.name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        self._promotion = None
        if not self.name or self.name.isspace():
            raise ValueError("Invalid Name")
        if self._price < 1:
            raise ValueError("Invalid Price")
        if self._quantity < 1:
            raise ValueError("Invalid Quantity")

    @property
    def price(self):
        """Return price of Product"""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """
        Set the price of a Product if price is greater than 0

        :arg:
            new_price: (float) new price of product
        """
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid Price!")

    @property
    def promotion(self):
        """Returns current promotion on the Product."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion):
        """Sets a promotion for a product.
        :param promotion: (Promotion) the promotion class to be set on the product.
        """
        self._promotion = promotion

    @property
    def quantity(self) -> int:
        """
        Returns the total quantity of the product

        :return:
            (int) total amount of the product
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """
        Updates the total quantity of the product by adding given amount.
        deactivates the product if the quantity is or below 0.

        :arg:
            quantity: (int) amount to be added to quantity
        """
        self._quantity += quantity
        if self._quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is currently active

        :return:
            (bool) True for an active product and False for inactive
        """
        return self.active

    def activate(self):
        """Activates the product by setting its status to True"""
        self.active = True

    def deactivate(self):
        """Deactivates a product by setting its active status to False"""
        self.active = False

    def buy(self, quantity: int) -> float:
        """
        Processes the purchase of a specified quantity of the product.
        Updates the stock and deactivates the product if the stock reaches 0.
        Applies promotions if available.

        :arg:
            quantity (int): The quantity of the product to purchase. Must be greater than 0 and not exceed available stock.

        :return:
            float: The total price of the purchased quantity, potentially adjusted by promotions.

        :raises:
            ValueError: If the quantity is less than or equal to 0, or if there is insufficient stock.
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        if quantity > self._quantity:
            raise ValueError("Not enough stock available")

        # calculate price with promotions
        if self.promotion:
            price = self.promotion.apply_promotion(self, quantity)
        else:
            price = self._price * quantity

        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        return price

    # dunder methods
    def __str__(self) -> str:
        """
        Returns an F-string of the product. showing the name price and quantity and promotion details.

        :return:
            (F-Str) Product details in format. (name), Price: (price), Quantity: (quantity), Promotion: (type)
        """
        promotion_info = f", Promotion: {self.promotion.label}" if self.promotion else ""
        return (f"{self.name}, "
                f"Price: {self._price}, "
                f"Quantity: {self._quantity}"
                f"{promotion_info}")

    def __gt__(self, other):
        """
        Compare price of this product with other

        :param:
            other: (Product) another product.
        :return:
            (bool) True if greater than
        """
        return self._price > other._price

    def __lt__(self, other):
        """
        Compare price of this product with other

        :param:
            other: (Product) another product.
        :return:
            (bool) True if less than
        """
        return self._price < other._price


class NonStockedProduct(Product):
    """
    Represents a product with unlimited stock (non-stocked product).

    Methods:
        quantity: Returns 'Unlimited' as a string to indicate there is no stock limitation.
        buy(quantity): Allows the purchase of any quantity without affecting stock.
    """
    def __init__(self, name: str, price: float):
        """
        Initialize the Product with unlimited stock.

        :arg:
            name: (str) Product name
            price: (float) the price of the product
        """
        super().__init__(name, price, quantity=1)
        self._quantity = math.inf

    def __str__(self) -> str:
        """
        Returns a string representation of the product, indicating the price and 'Unlimited' stock.

        :return:
            str: A string describing the product's name, price, and stock status ("Unlimited").
        """
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

    @property
    def quantity(self) -> str:
        """Returning unlimited as a string to show non-stocked status"""
        return "Unlimited"

    @quantity.setter
    def quantity(self, quantity: int):
        """Raises ValueError when trying to set quantity for non-stocked product"""
        raise ValueError("Cannot set quantity for a non-stocked product")

    def buy(self, quantity: int) -> float:
        """
        Allow the purchase of any quantity without reducing the stock.

        :arg:
            quantity: (int) quantity to be purchased

        :return:
            (float) total cost of the quantity

        :raise:
            ValueError if quantity <= 0
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        return self.price * quantity


class LimitedProduct(Product):
    """
    Another child class of the Product class allowing only a limited number of the items purchase per order.

    Attribute:
        :maximum (int) controls the limit per order.
    """
    def __init__(self, name: str, price: float, quantity: int, maximum=1):
        """
        Initialize the LimitedProduct instance with a maximum purchase limit.

        :Args: name: (str) name of product.
               price: (float) price of product
               quantity: (int) quantity of the product
               maximum: (int) maximum limit purchase per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of the given products' quantity.
        updates the quantity and deactivates it if it is 0.
        returning the total cost of the quantity given.
        raises a ValueError if the purchase quantity is less or equal to 0.

        :arg:
            quantity: (int) quantity of a product to be purchased.
        :return:
            (float) total cost of said quantity of product.
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if quantity > self.maximum:
            raise ValueError(f"The maximum amount per order is {self.maximum}")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity

    def __str__(self) -> str:
        """
        Returns an F-string of the product. showing the name price and Unlimited as this is a non-stocked product.

        :return:
            (F-Str) Product details in format. (name), Price: (price), Order limit: (maximum)
        """
        return f"{self.name}, Price: {self._price}, Limited to {self.maximum} per order!"




