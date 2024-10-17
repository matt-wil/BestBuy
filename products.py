class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True
        if self.name == "":
            raise ValueError("Invalid Name")
        if self.price < 1:
            raise ValueError("Invalid Price")
        if self.quantity < 1:
            raise ValueError("Invalid Quantity")

    def get_quantity(self):
        return self.quantity

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
            return cost
        else:
            raise ValueError(f"Sorry we only have {self.quantity} {self.name}`s available.")

