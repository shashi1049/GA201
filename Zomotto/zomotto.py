menu = {}
orders = {}


def add_dish():
    dish_id = input("Enter dish ID: ")
    if dish_id in menu:
        print("Dish with ID", dish_id, "already exists!")
        return

    dish_name = input("Enter dish name: ")
    dish_price = float(input("Enter dish price: "))
    dish_stock = int(input("Enter dish stock: "))
    dish_availability = "Yes" if dish_stock > 0 else "No"
    menu[dish_id] = {"id": dish_id, "name": dish_name, "price": dish_price,
                     "stock": dish_stock, "availability": dish_availability}
    print("Dish added successfully!")


def update_dish():
    dish_id = input("Enter dish ID to update: ")
    if dish_id not in menu:
        print("Dish with ID", dish_id, "not found!")
        return

    dish = menu[dish_id]
    dish['name'] = input("Enter new dish name: ")
    dish['price'] = float(input("Enter new dish price: "))
    dish['stock'] = int(input("Enter new dish stock: "))
    dish['availability'] = "Yes" if dish['stock'] > 0 else "No"
    print("Dish updated successfully!")


def remove_dish():
    dish_id = input("Enter dish ID to remove: ")
    if dish_id not in menu:
        print("Dish with ID", dish_id, "not found!")
        return

    del menu[dish_id]
    print("Dish removed successfully!")


def take_order():
    customer_name = input("Enter customer name: ")
    dish_id = input("Enter dish ID to order: ")
    if dish_id not in menu:
        print("Dish with ID", dish_id, "not found!")
        return

    dish = menu[dish_id]
    if dish['availability'] == "Yes" and dish['stock'] > 0:
        dish['stock'] -= 1  # Decrease stock count by 1
        if dish['stock'] == 0:
            dish['availability'] = "No"
        dish['availability'] = "Ready"
        order_id = len(orders) + 1
        orders[order_id] = {"Customer Name": customer_name,
                            "Dish ID": dish_id, "Status": "Ready"}
        print("Order placed successfully! Order ID:", order_id)
    else:
        print("Sorry, the dish is not available or out of stock.")


def update_order_status():
    order_id = int(input("Enter order ID to update status: "))
    if order_id not in orders:
        print("Order with ID", order_id, "not found!")
        return

    order = orders[order_id]
    new_status = input(
        "Enter new status (Received, Pending, Ready, Delivered): ")
    order['Status'] = new_status
    print("Order status updated successfully!")


def review_orders():
    print("All Orders:")
    print("{:<10} {:<20} {:<10} {:<10}".format(
        "Order ID", "Customer Name", "Dish ID", "Status"))
    for order_id, order_details in orders.items():
        print("{:<10} {:<20} {:<10} {:<10}".format(
            order_id, order_details['Customer Name'], order_details['Dish ID'], order_details['Status']))
    print()


def view_menu():
    print("Menu:")
    print("{:<10} {:<20} {:<10} {:<10}".format(
        "Dish ID", "Dish Name", "Dish Price", "Availabilty"))
    for dish_id, dish in menu.items():
        print("{:<10} {:<20} {:<10} {:<10}".format(
            dish['id'], dish['name'], dish['price'], dish['availability']))
    print()


def exit_app():
    print("Thank you for using Zomato Chronicles: The Great Food Fiasco!")
    return


def show_menu():
    print("Zomato Chronicles: The Great Food Fiasco")
    print("1. Add a new dish")
    print("2. Update a dish")
    print("3. Remove a dish")
    print("4. Take an order")
    print("5. Update the status of an order")
    print("6. Review all orders")
    print("7. View Menu")
    print("8. Exit")


def handle_input(choice):
    if choice == '1':
        add_dish()
    elif choice == '2':
        update_dish()
    elif choice == '3':
        remove_dish()
    elif choice == '4':
        take_order()
    elif choice == '5':
        update_order_status()
    elif choice == '6':
        review_orders()
    elif choice == '7':
        view_menu()
    elif choice == '8':
        exit_app()
    else:
        print("Invalid choice!")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")
        handle_input(choice)
        print()


if __name__ == '__main__':
    main()

print(orders)
