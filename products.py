import math
from promotions import Promotion


class Product:
    """
    This class creates a product object for a store.
    Attributes:
        name: (str) name of product
        price: (float) price of product
        quantity: (int) Quantity of product
        active: (bool) The status of product. True = available, False = unavailable
    -----
    Methods:
        __init__(self, name: str, price: float, quantity: int):
            Initializes a new Product instance with name, price, and quantity. Raises a ValueError if any attribute is invalid.

        get_quantity(self) -> int:
            Returns the current quantity of the product.

        set_quantity(self, quantity: int):
            Updates the product's quantity by adding the provided quantity value. Deactivates the product if the new quantity is 0 or less.

        is_active(self) -> bool:
            Returns True if the product is active, False otherwise.

        activate(self):
            Activates the product by setting the active status to True.

        deactivate(self):
            Deactivates the product by setting the active status to False.

        show(self) -> str:
            Returns a string representation of the product in the format: "ProductName, Price: X, Quantity: Y".

        buy(self, quantity: int) -> float:
            Processes the purchase of a given quantity of the product, updating the available stock.
            Returns the total price of the purchase. Raises ValueError if the requested quantity is invalid or exceeds available stock.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        initialises the product creating product object with a name price and quantity.
        Raises a ValueError if the name price or quantity are invalid.
        :param name: (str) The name of the product
        :param price: (float) The price of the product
        :param quantity: (int) the quantity of the product
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None
        if not self.name or self.name.isspace():
            raise ValueError("Invalid Name")
        if self.price < 1:
            raise ValueError("Invalid Price")
        if self.quantity < 1:
            raise ValueError("Invalid Quantity")

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def get_quantity(self) -> int:
        """
        returns the total quantity of the product
        :return: (int) total amount of the product
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        updates the total quantity of the product by adding given amount.
        deactivates the product if the quantity is or below 0.
        :param quantity: (int) amount to be added to quantity
        """
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        checks if the product is currently active
        :return: (bool) True for an active product and False for inactive
        """
        return self.active

    def activate(self):
        """
        activates the product by setting its status to True
        """
        self.active = True

    def deactivate(self):
        """Deactivates a product by setting its active status to False"""
        self.active = False

    def show(self) -> str:
        """
        returns an F-string of the product. showing the name price and quantity and promotion details.
        :return: (F-Str) Product details in format. (name), Price: (price), Quantity: (quantity), Promotion: (type)
        """
        promotion_info = f", Promotion: {self.promotion.label}" if self.promotion else ""
        return (f"{self.name}, "
                f"Price: {self.price}, "
                f"Quantity: {self.quantity}"
                f"{promotion_info}")

    def buy(self, quantity: int) -> float:
        """
        processes a purchase of the given products' quantity.
        updates the quantity and deactivates it if it is 0.
        returning the total cost of the quantity given.
        raises a ValueError if the purchase quantity is less or equal to 0.
        :param quantity: (int) quantity of a product to be purchased.
        :return: (float) total cost of said quantity of product.
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        # calculate price with promotions
        if self.promotion:
            price = self.promotion.apply_promotion(self, quantity)
        else:
            price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=1)
        self.quantity = math.inf

    def show(self) -> str:
        """
        returns an F-string of the product. showing the name price and Unlimited as this is a non-stocked product.
        :return: (F-Str) Product details in format. (name), Price: (price), Quantity: Unlimited
        """
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

    def get_quantity(self) -> str:
        """Returning unlimited as a string to show non-stocked status"""
        return "Unlimited"

    def set_quantity(self, quantity: int):
        """raises ValueError when trying to set quantity for non-stocked product"""
        raise ValueError("Cannot set quantity for a non-stocked product")

    def buy(self, quantity: int) -> float:
        """
        Allow the purchase of any quantity without reducing the stock.
        :param quantity: (int) quantity to be purchased
        :return: (float) total cost of the quantity
        :raise: ValueError if quantity <= 0
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        processes a purchase of the given products' quantity.
        updates the quantity and deactivates it if it is 0.
        returning the total cost of the quantity given.
        raises a ValueError if the purchase quantity is less or equal to 0.
        :param quantity: (int) quantity of a product to be purchased.
        :return: (float) total cost of said quantity of product.
        """
        if quantity <= 0:
            raise ValueError("Purchased quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if quantity > self.maximum:
            raise ValueError("The maximum amount per order is 1")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity

    def show(self) -> str:
        """
        returns an F-string of the product. showing the name price and Unlimited as this is a non-stocked product.
        :return: (F-Str) Product details in format. (name), Price: (price), Quantity: Unlimited
        """
        return f"{self.name}, Price: {self.price}, Limited to 1 per order!"




