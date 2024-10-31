from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for different types of promotions able to be placed on a product
        Attributes:
                label (str): the label to describe the promotion.
        Methods:
            apply_promotion: Abstract method to calculate the total cost after applying the promotion
    """
    def __init__(self, label: str):
        """
        initialize the promotion with the label to describe the promotion.
        :param label:
        """
        self.label = label

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Calculates the discount price based on promotion and returns the total cost
        :param product: (Product) the product which the promotion is applied
        :param quantity: (int) the number of units of the product being purchased
        :return: (float): total cost after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Child class of Promotion that adds a certain percentage discount to the product price.
    Attribute:
        discount_percentage (float): the percentage discount applied - float for percentage calculations without casting
    Methods:
        apply_promotion: Applies the percentage discount and returns the discounted total cost.
    """
    def __init__(self, label: str, percent: float):
        """
        initialize the PercentageDiscount promotion with a label and discount percentage.
        :param label: (str) The label describing the promotion
        :param percent: (float) the discount percentage to apply.
        """
        super().__init__(label)
        self.discount_percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies percentage discount to the products price
        :param product: (Product) the product to which the promotion is applied
        :param quantity: (int) the number of units of the product being purchased.
        :return: (float) total cost after discount percentage applied.
        """
        discount_amount = product.price * (self.discount_percent / 100)
        return (product.price - discount_amount) * quantity


class SecondHalfPrice(Promotion):
    """
    Child class of Promotion offers every second item at half price
    Methods:
        apply_promotion: Calculates the total cost with every second item priced at half price
    """
    def __init__(self, label: str):
        """
        initializes the SecondHalfPrice promotion with a label
        :param label: (str) the label describing the promotion.
        """
        super().__init__(label)

    def apply_promotion(self, product, quantity) -> float:
        """
        applied the second item at half price promotion
        :param product: (Product) the product to which the promotion is applied
        :param quantity: (int) total amount of units of the product being purchased
        :return: (float) total cost of the order after promotion applied.
        """
        pairs = quantity // 2
        remaining = quantity % 2
        total_cost = (pairs * (product.price * 1.5)) + (remaining * product.price)
        return total_cost


class ThirdOneFree(Promotion):
    """
    Child class of Promotion that offers 1 free item for every 3 purchased.
    Methods:
        apply_promotion: calculates total cost with one free item for every sset of three
    """
    def __init__(self, label: str):
        """
        initializes the ThirdOneFree promotion
        :param label: (str) label describing the promotion
        """
        super().__init__(label)

    def apply_promotion(self, product, quantity) -> float:
        """
        applied the third item free promotion
        :param product: (Product) the product to which the promotion is applied
        :param quantity: (int) the number of units of the product being purchased
        :return: (float) the total cost of the order after promotion applied.
        """
        groups_of_three = quantity // 3
        remaining = quantity % 3
        total_cost = (groups_of_three * 2 * product.price) + (remaining * product.price)
        return total_cost


