from db import connect_db

def register_customer():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n----- Customer Registration -----")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    sql = """
    INSERT INTO customers(name,email,phone)
    VALUES(%s,%s,%s)
    """

    values = (name,email,phone)

    cursor.execute(sql,values)
    conn.commit()

    print("Customer Registered Successfully!")

    cursor.close()
    conn.close()
