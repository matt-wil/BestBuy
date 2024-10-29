from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, label: str):
        self.label = label

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Calculates the discount price based on promotion and returns the total cost"""
        pass


class PercentDiscount(Promotion):
    def __init__(self, label: str, percent: float):
        super().__init__(label)
        self.discount_percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """Applies percentage discount to the products price"""
        discount_amount = product.price * (self.discount_percent / 100)
        return (product.price - discount_amount) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, label: str):
        super().__init__(label)

    def apply_promotion(self, product, quantity) -> float:
        pairs = quantity // 2
        remaining = quantity % 2
        total_cost = (pairs * (product.price * 1.5)) + (remaining * product.price)
        return total_cost


class ThirdOneFree(Promotion):
    def __init__(self, label: str):
        super().__init__(label)

    def apply_promotion(self, product, quantity) -> float:
        groups_of_three = quantity // 3
        remaining = quantity % 3
        total_cost = (groups_of_three * 2 * product.price) + (remaining * product.price)
        return total_cost


