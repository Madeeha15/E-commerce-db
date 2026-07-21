from db import connect_db

def buy_product():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n===== Buy Product =====")

    customer_id = int(input("Enter Customer ID: "))
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    # Check Product
    cursor.execute(
        "SELECT price, quantity FROM products WHERE product_id=%s",
        (product_id,)
    )

    product = cursor.fetchone()

    if product is None:
        print("Product Not Found!")
        cursor.close()
        conn.close()
        return

    price = product[0]
    stock = product[1]

    if quantity > stock:
        print("Insufficient Stock!")
        cursor.close()
        conn.close()
        return

    total = price * quantity

    # Insert Order
    cursor.execute("""
        INSERT INTO orders(customer_id, product_id, quantity, total_price)
        VALUES(%s,%s,%s,%s)
    """, (customer_id, product_id, quantity, total))

    # Update Stock
    cursor.execute("""
        UPDATE products
        SET quantity = quantity - %s
        WHERE product_id=%s
    """, (quantity, product_id))

    conn.commit()

    print("\nOrder Placed Successfully!")
    print("Total Amount = ₹", total)

    cursor.close()
    conn.close()


def view_orders():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            o.order_id,
            c.name,
            p.product_name,
            o.quantity,
            o.total_price,
            o.order_date
        FROM orders o
        JOIN customers c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON o.product_id = p.product_id
    """)

    orders = cursor.fetchall()

    print("\n========== Order History ==========")

    if not orders:
        print("No Orders Found.")
    else:
        for order in orders:
            print("-----------------------------------")
            print("Order ID     :", order[0])
            print("Customer     :", order[1])
            print("Product      :", order[2])
            print("Quantity     :", order[3])
            print("Total Amount : ₹", order[4])
            print("Date         :", order[5])

    cursor.close()
    conn.close()
