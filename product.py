from db import connect_db

# Add Product
def add_product():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n===== Add Product =====")

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    sql = """
    INSERT INTO products(product_name, price, quantity)
    VALUES(%s, %s, %s)
    """

    values = (name, price, quantity)

    cursor.execute(sql, values)
    conn.commit()

    print("Product Added Successfully!")

    cursor.close()
    conn.close()


# View Products
def view_products():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    print("\n========== Product List ==========")

    if len(products) == 0:
        print("No Products Available.")
    else:
        for product in products:
            print("--------------------------------")
            print(f"Product ID : {product[0]}")
            print(f"Name       : {product[1]}")
            print(f"Price      : ₹{product[2]}")
            print(f"Quantity   : {product[3]}")

    cursor.close()
    conn.close()


# Update Product
def update_product():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n===== Update Product =====")

    pid = int(input("Enter Product ID: "))
    price = float(input("Enter New Price: "))
    quantity = int(input("Enter New Quantity: "))

    sql = """
    UPDATE products
    SET price=%s, quantity=%s
    WHERE product_id=%s
    """

    cursor.execute(sql, (price, quantity, pid))
    conn.commit()

    print("Product Updated Successfully!")

    cursor.close()
    conn.close()


# Delete Product
def delete_product():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n===== Delete Product =====")

    pid = int(input("Enter Product ID: "))

    cursor.execute("DELETE FROM products WHERE product_id=%s", (pid,))
    conn.commit()

    print("Product Deleted Successfully!")

    cursor.close()
    conn.close()
