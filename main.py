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
    """
    Displaying the shop menu options.
    print statements displaying all options available for the user.
    """
    print("\t----------")
    print("\tStore Menu")
    print("\t----------")
    print("1. List all products in the store.")
    print("2. Show total amount in the store.")
    print("3. Make an order")
    print("4. Quit")


def exit_func():
    """
    Exit function to safely quit the program
    printing a farewell message and using sys.exit()"""
    print("Thanks for shopping at Best Buy!")
    sys.exit()


def start(store_obj: Store):
    """
    starting the main program loop to interact with the user.
    display the menu, takes the users input and uses a dispatcher dictionary to activate the correct
    functions based on the users input.
    :param store_obj: Store(object) store object that holds product inventory and supports the shop operations.
    """
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
    """
    Lists all the active products in the store.
    fetches active products from the store and prints them numbered.
    if there are no products available a message is printed.
    :param store: Store(object) containing the product inventory.
    """
    products = store.get_all_products()
    if not products:
        print("No products available in the store")
    else:
        print("\n Available Products")
        for i, product in enumerate(products):
            print(f"{i+1}. {product.show()}")


def show_total_quantity(store: Store):
    """
    shows the quantity of items available in the store.
    runs the get_total_quantity() function from the store
    printing a formatted string to display total number of available items.
    :param store: Store(object) containing product inventory.
    :return:
    """
    total_quantity = store.get_total_quantity()
    print(f"\nTotal quantity of items in the store: {total_quantity}")


def make_order(store: Store):
    """
    Handles the product ordering process.
    display a list of numbered active products and the quantity of said item available.
    asks the user to input which number product and the quantity they would like to purchase.
    appending the selections to the shopping list, once the user is done they enter an empty string as an input
    in order to process the purchase order. The total cost is calculated and then displayed to the user
    If any invalid inputs are entered the appropriate print statements are printed.
    :param store: Store(object) the object where the order is being placed.
    """
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
            if quantity > products[product_index].get_quantity():
                print(f"I'm sorry we only have {products[product_index].get_quantity()} available.")
                time.sleep(2)
                continue

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
