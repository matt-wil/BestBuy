# Test that creating a normal product works.
# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
# Test that when a product reaches 0 quantity, it becomes inactive.
# Test that product purchase modifies the quantity and returns the right output.
# Test that buying a larger quantity than exists invokes exception.

from products import Product
import pytest


class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        # set up my sample objects to test on
        self.setup_product1 = Product("Laptop", 999.99, 10)
        self.setup_product2 = Product("Phone", 200, 5)

    def test_product_initialisation_int(self):
        # set up my sample objects to test on
        self.product2 = Product("Phone", 200, 5)

        # check values
        assert self.product2.name == "Phone"
        assert self.product2.price == 200
        assert self.product2._quantity == 5
        assert self.product2.is_active() is True

    def test_product_initialisation_float(self):
        # set up my sample objects to test on
        self.product1 = Product("Laptop", 999.99, 10)

        # check values
        assert self.product1.name == "Laptop"
        assert self.product1.price == 999.99
        assert self.product1._quantity == 10
        assert self.product1.is_active() is True

    def test_invalid_name_initialization(self):
        with pytest.raises(ValueError, match="Invalid Name"):
            Product("", 1.250, 5)
        with pytest.raises(ValueError, match="Invalid Name"):
            Product(" ", 1.250, 5)
        with pytest.raises(ValueError, match="Invalid Name"):
            Product(None, 1.250, 5)

    def test_invalid_price_initialization(self):
        with pytest.raises(ValueError, match="Invalid Price"):
            Product("Phone", 0, 5)

        with pytest.raises(ValueError, match="Invalid Price"):
            Product("Handy", -55, 10)

    def test_invalid_quantity_initialization(self):
        with pytest.raises(ValueError, match="Invalid Quantity"):
            Product("Phone", 1.250, -5)

        with pytest.raises(ValueError, match="Invalid Quantity"):
            Product("Handy", 1.250, 0)

    def test_get_quantity(self):
        assert self.setup_product1.quantity == 10
        assert self.setup_product2.quantity == 5

    def test_set_quantity(self):
        self.setup_product1.quantity = 150
        assert self.setup_product1.quantity == 160

        self.setup_product2.quantity = 150
        assert self.setup_product2.quantity == 155

    def test_is_active(self):
        assert self.setup_product1.is_active() == True
        assert self.setup_product2.is_active() == True

    def test_activate(self):
        activation_test_product = Product("Camera", 499.00, 150)
        activation_test_product.deactivate()
        activation_test_product.activate()
        assert activation_test_product.is_active() == True

    def test_deactivate(self):
        activation_test_product = Product("Camera", 499.00, 150)
        activation_test_product.deactivate()
        assert activation_test_product.is_active() == False

    def test_show(self):
        check_show_1 = str(self.setup_product1)
        assert check_show_1 == f"Laptop, Price: 999.99, Quantity: 10"
        check_show_2 = str(self.setup_product2)
        assert check_show_2 == f"Phone, Price: 200, Quantity: 5"

    def test_valid_buy(self):
        assert Product.buy(self.setup_product1, 9) == 8999.91
        assert Product.buy(self.setup_product1, 1) == 999.99
        assert Product.buy(self.setup_product2, 4) == 800
        assert Product.buy(self.setup_product2, 1) == 200.00

    def test_invalid_buy(self):
        # Test that buying a larger quantity than exists invokes exception.
        with pytest.raises(ValueError, match="Not enough stock available"):
            Product.buy(self.setup_product1, 20)

        with pytest.raises(ValueError, match="Purchased quantity must be greater than 0"):
            Product.buy(self.setup_product1, -1)

        with pytest.raises(ValueError, match="Not enough stock available"):
            Product.buy(self.setup_product2, 22)

        with pytest.raises(ValueError, match="Purchased quantity must be greater than 0"):
            Product.buy(self.setup_product2, 0)

    def test_0_quantity(self):
        # Test that when a product reaches 0 quantity, it becomes inactive.
        test_0_quantity_product = Product("Mouse", 25.99, 5)
        test_0_quantity_product.buy(5)
        assert test_0_quantity_product._quantity == 0
        assert test_0_quantity_product.is_active() == False

    def test_quantity_modification(self):
        # Test that product purchase modifies the quantity and returns the right output.
        test_quantity_mod_product = Product("Keyboard", 30.00, 5)
        test_quantity_mod_product.buy(2)
        assert test_quantity_mod_product._quantity == 3

    def test_set_price(self):
        mac = Product("Handy", 1.250, 1)
        mac.price = -100 == 1.250
        mac.price = 1.150 == 1.150

    def test_set_price_negative(self, capsys):
        mac = Product("Handy", 1.250, 1)
        mac.price = -100

        captured = capsys.readouterr()
        assert captured.out == "Invalid Price!\n"

