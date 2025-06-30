import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (default host & user: root)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_mysql_password'  # Replace this with your actual password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
