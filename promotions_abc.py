from abc import ABC, abstractmethod


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
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Calculates the total cost after applying the promotion.

        :param product: (Product) The product to which the promotion is applied.
        :param quantity: (int) The number of units of the product being purchased.
        :return: (float) The total cost after applying the promotion.
        """
        pass

