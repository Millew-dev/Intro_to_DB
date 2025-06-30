import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (default host & user: root)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_mysql_password'  # Replace with your real password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the database (this won't throw error if it already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
