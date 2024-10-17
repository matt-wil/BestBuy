class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        if self.name == "":
            raise ValueError("Invalid Name")
        if self.price < 1:
            raise ValueError("Invalid Price")
        if self.quantity < 1:
            raise ValueError("Invalid Quantity")

    def get_quantity(self):
        return f"There are {self.quantity} {self.name}`s available currently."

    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            cost = self.price * quantity
            return f"{quantity} {self.name}'s will cost: €{cost}"
        else:
            raise ValueError(f"Sorry we only have {self.quantity} {self.name}`s available.")


# Tester main
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    main()
