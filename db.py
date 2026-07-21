import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="ecommerce"
    )

    return connection
