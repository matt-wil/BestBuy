import pytest
from products import LimitedProduct


@pytest.fixture()
def sample_limited_product():
    return LimitedProduct("Shipping", 10.00, 250, 1)


def test_limited_buy(sample_limited_product):
    with pytest.raises(ValueError, match=f"The maximum amount per order is {sample_limited_product.maximum}"):
        sample_limited_product.buy(2)