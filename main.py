import time

from products import Product
from store import Store
import sys


# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = Store(product_list)


def print_menu():
    # display menu
    print("\t----------")
    print("\tStore Menu")
    print("\t----------")
    print("1. List all products in the store.")
    print("2. Show total amount in the store.")
    print("3. Make an order")
    print("4. Quit")


def exit_func():
    print("Thanks for shopping at Best Buy!")
    sys.exit()


def start(store_obj: Store):
    print("Welcome to Best Buy!")

    dispatcher = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order,
        "4": exit_func,
    }
    while True:
        print_menu()
        choice = input("Please choose a number: ")

        action = dispatcher.get(choice)
        if action:
            result = action(store_obj)
            if result is False:
                break
        else:
            print("Invalid input! Please try again.")


def list_products(store: Store):
    products = store.get_all_products()
    if not products:
        print("No products available in the store")
    else:
        print("\n Available Products")
        for i, product in enumerate(products):
            print(f"{i+1}. {product.show()}")


def show_total_quantity(store: Store):
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of items in the store: {total_quantity}")


def make_order(store: Store):
    products = store.get_all_products()
    if not products:
        print("No products available for order")
        return

    shopping_list = []

    print("When you want to finish order, enter empty text.")

    while True:
        for i, product in enumerate(products):
            print(f"{i + 1}. {product.show()}")

        product_choice = input("Which product # do you want?\n>>> ")
        if not product_choice:
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(products):
                print("Error: Invalid product choice!")
                continue

            quantity = int(input(f"How many {products[product_index].name} would you like?\n>>> "))
            shopping_list.append((products[product_index], quantity))

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"Order made! Total payment: €{total_cost:.2f}")
            time.sleep(3)
        except Exception as e:
            print(f"Error placing order: {e}")
    else:
        print("No items in the shopping list.")


if __name__ == '__main__':
    start(best_buy)
