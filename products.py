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
        """return price of Product"""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """
        set the price of a Product if price is greater than 0
        :param new_price: (float) new price of product
        """
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid Price!")

    @property
    def promotion(self):
        """returns current promotion on the Product."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion):
        """sets a promotion for a product.
        :param promotion: (Promotion) the promotion class to be set on the product.
        """
        self._promotion = promotion

    @property
    def quantity(self) -> int:
        """
        returns the total quantity of the product
        :return: (int) total amount of the product
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """
        updates the total quantity of the product by adding given amount.
        deactivates the product if the quantity is or below 0.
        :param quantity: (int) amount to be added to quantity
        """
        self._quantity += quantity
        if self._quantity <= 0:
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
        returns an F-string of the product. showing the name price and quantity and promotion details.
        :return: (F-Str) Product details in format. (name), Price: (price), Quantity: (quantity), Promotion: (type)
        """
        promotion_info = f", Promotion: {self.promotion.label}" if self.promotion else ""
        return (f"{self.name}, "
                f"Price: {self._price}, "
                f"Quantity: {self._quantity}"
                f"{promotion_info}")

    def __gt__(self, other):
        """
        compare price of this product with other
        :param other: (Product) another product.
        :return: (bool) True if greater than
        """
        return self._price > other._price

    def __lt__(self, other):
        """
        compare price of this product with other
        :param other: (Product) another product.
        :return: (bool) True if less than
        """
        return self._price < other._price


class NonStockedProduct(Product):
    """
    This class is a child class of the Product class for products with "Unlimited" stock of Non-stocked Products.
    Methods:
        quantity: Returns "Unlimited" as a string
        buy: Process the purchase of any quantity of the product without reducing stock.
    """
    def __init__(self, name: str, price: float):
        """
        initialize the Product with unlimited stock.
        :param name: (str) Product name
        :param price: (float) the price of the product
        """
        super().__init__(name, price, quantity=1)
        self._quantity = math.inf

    def __str__(self) -> str:
        """
        returns an F-string of the product. showing the name price and Unlimited as this is a non-stocked product.
        :return: (F-Str) Product details in format. (name), Price: (price), Quantity: Unlimited
        """
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

    @property
    def quantity(self) -> str:
        """Returning unlimited as a string to show non-stocked status"""
        return "Unlimited"

    @quantity.setter
    def quantity(self, quantity: int):
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
    """
    another child class of the Product class allowing only a limited number of the items purchase per order.
    Attribute:
        :maximum (int) controls the limit per order.
    """
    def __init__(self, name: str, price: float, quantity: int, maximum=1):
        """
        initialize the LimitedProduct instance with a maximum purchase limit.
        :param name: (str) name of product.
        :param price: (float) price of product
        :param quantity: (int) quantity of the product
        :param maximum: (int) maximum limit purchase per order.
        """
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
            raise ValueError(f"The maximum amount per order is {self.maximum}")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity

    def __str__(self) -> str:
        """
        returns an F-string of the product. showing the name price and Unlimited as this is a non-stocked product.
        :return: (F-Str) Product details in format. (name), Price: (price), Order limit: (maximum)
        """
        return f"{self.name}, Price: {self._price}, Limited to {self.maximum} per order!"




