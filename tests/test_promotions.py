import pytest
from promotions import PercentDiscount, ThirdOneFree, SecondHalfPrice
from products import Product


@pytest.fixture()
def sample_product():
    return Product("Linux", 1000.00, 100)


def test_percentage_discount(sample_product):
    discount = PercentDiscount("10% Off", 10)
    quantity = 5
    discounted_price = discount.apply_promotion(sample_product, quantity)
    expected_price = sample_product.price * 0.9 * quantity
    assert discounted_price == expected_price, "PercentDiscount calculation failed"

    # edge case
    no_discount = PercentDiscount("No Discount", 0)
    assert no_discount.apply_promotion(sample_product, quantity) == sample_product.price * quantity, "PercentageDiscount with 0% failed"


def test_second_half_price_even(sample_product):
    discount = SecondHalfPrice("Second One is Half Price")

    quantity_even = 4
    discounted_price_even = discount.apply_promotion(sample_product, quantity_even)
    expected_price_even = (2 * sample_product.price * 1.5)
    assert discounted_price_even == expected_price_even, "SecondHalfPrice calculation failed for even quantity"


def test_second_half_price_odd(sample_product):
    discount = SecondHalfPrice("Second One is Half Price")

    quantity_odd = 5
    discounted_price_odd = discount.apply_promotion(sample_product, quantity_odd)
    expected_price_odd = (2 * sample_product.price * 1.5) + sample_product.price
    assert discounted_price_odd == expected_price_odd, "SecondHalfPrice calculation failed for even quantity"


def test_third_one_free_even(sample_product):
    discount = ThirdOneFree("Every Third One is Free")

    quantity_even = 6
    discounted_price_even = discount.apply_promotion(sample_product, quantity_even)
    expected_price_even = 4 * sample_product.price
    assert discounted_price_even == expected_price_even, "ThirdOneFree calculation failed for even quantity"


def test_third_one_free_odd(sample_product):
    discount = ThirdOneFree("Every Third One is Free")

    quantity_odd = 5
    discounted_price_odd = discount.apply_promotion(sample_product, quantity_odd)
    expected_price_odd = 4 * sample_product.price
    assert discounted_price_odd == expected_price_odd, "ThirdOneFree calculation failed for even quantity"


