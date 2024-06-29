import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    try:
        __cnx = mysql.connector.connect(host="localhost", user="root", password="", database="gs", port=3306)
        return __cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise

if __name__ == '__main__':
    try:
        connection = get_sql_connection()
        if connection:
            print("Connected to MySQL successfully!")
            # Example usage:
            # print(get_all_products(connection))
    except mysql.connector.Error as err:
        print(f"Error in main execution: {err}")
    finally:
        if __cnx:
            __cnx.close()
