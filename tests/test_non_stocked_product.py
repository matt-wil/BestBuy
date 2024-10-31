import pytest
from products import NonStockedProduct


@pytest.fixture()
def sample_non_stocked_product():
    return NonStockedProduct("Software", 1000.00)


def test_non_stocked_product_price(sample_non_stocked_product):
    assert sample_non_stocked_product.price == 1000.00, "NonStockedProduct price is incorrect"


def test_non_stocked_product_purchase(sample_non_stocked_product):
    quantity = 10
    total_cost = sample_non_stocked_product.buy(quantity=quantity)
    expected_cost = sample_non_stocked_product.price * quantity
    assert total_cost == expected_cost, f"NonSockedProduct purchase calculation failed for quantity {quantity}"

    quantity_large = 100
    total_cost_large = sample_non_stocked_product.buy(quantity=quantity_large)
    expected_cost_large = sample_non_stocked_product.price * quantity_large
    assert total_cost_large == expected_cost_large, f"NonSockedProduct purchase calculation failed for quantity {quantity_large}"


def test_setter(sample_non_stocked_product):
    with pytest.raises(ValueError, match="Cannot set quantity for a non-stocked product"):
        sample_non_stocked_product.quantity = 100



