from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
    Abstract base class for different types of promotions that can be applied to a product.

    Attributes:
        label (str): The label describing the promotion.

    Methods:
        __init__(label): Initializes the Promotion with a label.
        apply_promotion(product, quantity): Calculates the total cost after applying the promotion.
    """

    def __init__(self, label: str):
        """
        Initializes the promotion with a label describing the promotion.

        :param label: (str) The label of the promotion.
        """
        self.label = label

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculates the total cost after applying the promotion.

        :param product: (Product) The product to which the promotion is applied.
        :param quantity: (int) The number of units of the product being purchased.
        :return: (float) The total cost after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the product price.

    Attributes:
        discount_percentage (float): The percentage discount to apply.

    Methods:
        __init__(label, percent): Initializes the promotion with a label and percentage discount.
        apply_promotion: Applies the percentage discount and returns the discounted total cost.
    """

    def __init__(self, label: str, percent: float):
        """
        Initializes the PercentDiscount promotion with a label and discount percentage.

        :param label: (str) The label describing the promotion.
        :param percent: (float) The discount percentage to apply.
        """
        super().__init__(label)
        self.discount_percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies the percentage discount to the product's price.

        :param product: (Product) The product to which the promotion is applied.
        :param quantity: (int) The number of units of the product being purchased.
        :return: (float) The total cost after applying the discount percentage.
        """
        discount_amount = product.price * (self.discount_percent / 100)
        return (product.price - discount_amount) * quantity


class SecondHalfPrice(Promotion):
    """
    Promotion that offers every second item at half price.

    Methods:
        apply_promotion: Calculates the total cost with every second item priced at half price.
    """

    def __init__(self, label: str):
        """
        Initializes the SecondHalfPrice promotion with a label.

        :param label: (str) The label describing the promotion.
        """
        super().__init__(label)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies the second item at half price promotion.

        :param product: (Product) The product to which the promotion is applied.
        :param quantity: (int) The total number of units of the product being purchased.
        :return: (float) The total cost after applying the promotion.
        """
        pairs = quantity // 2
        remaining = quantity % 2
        total_cost = (pairs * (product.price * 1.5)) + (remaining * product.price)
        return total_cost


class ThirdOneFree(Promotion):
    """
    Promotion that offers one free item for every three purchased.

    Methods:
        apply_promotion: Calculates the total cost with one free item for every set of three.
    """

    def __init__(self, label: str):
        """
        Initializes the ThirdOneFree promotion with a label.

        :param label: (str) The label describing the promotion.
        """
        super().__init__(label)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies the third item free promotion.

        :param product: (Product) The product to which the promotion is applied.
        :param quantity: (int) The number of units of the product being purchased.
        :return: (float) The total cost after applying the promotion.
        """
        groups_of_three = quantity // 3
        remaining = quantity % 3
        total_cost = (groups_of_three * 2 * product.price) + (remaining * product.price)
        return total_cost
