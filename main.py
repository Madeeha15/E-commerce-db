from customer import register_customer
from product import (
    add_product,
    view_products,
    update_product,
    delete_product
)
from order import (
    buy_product,
    view_orders
)

while True:

    print("\n===================================")
    print(" E-Commerce Management System")
    print("===================================")
    print("1. Register Customer")
    print("2. Add Product")
    print("3. View Products")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Buy Product")
    print("7. View Orders")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_customer()

    elif choice == "2":
        add_product()

    elif choice == "3":
        view_products()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        buy_product()

    elif choice == "7":
        view_orders()

    elif choice == "8":
        print("\nThank You for using the E-Commerce Management System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
