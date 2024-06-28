import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="gs")

if connection.is_connected():
    print("connected successfully")
else:
    print("Failed to connect")