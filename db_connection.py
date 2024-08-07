import mysql.connector
import os
from mysql.connector import Error


def create_connection():
    try:
        print("DB_HOST:", os.environ.get("DB_HOST"))
        print("DB_USER:", os.environ.get("DB_USER"))
        print("DB_PASSWORD:", os.environ.get("DB_PASSWORD"))
        print("DB_DATABASE:", os.environ.get("DB_DATABASE"))

        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE"),
        )
        if connection.is_connected():
            print("Connection to MySQL DB is successful")
            return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return


# Create a connection
connection = create_connection()
