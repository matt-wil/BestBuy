class Store:
    list_of_products = []

    def __init__(self, list_of_products):
        Store.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.list_of_products:
            total += product.quantity
        return total

    def get_all_products(self):
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):  # shopping_list = [(bose, 5),(mac, 30),(bose, 10)]:
        total_cost = 0.00
        for items in shopping_list:
            product, amount = items
            total_cost += product.price * amount
        return total_cost


