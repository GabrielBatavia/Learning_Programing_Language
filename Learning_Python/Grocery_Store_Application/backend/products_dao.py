import mysql.connector
from sql_connection import get_sql_connection

def get_all_product(connection):
    cursor = connection.cursor()

    query = """
    SELECT product.product_id, product.product_name, product.uom_id, product.price, uom.uom_name 
    FROM product 
    INNER JOIN uom ON product.uom_id = uom.uom_id
    """

    cursor.execute(query)

    response = []

    for (product_id, product_name, uom_id, price, uom_name) in cursor:
        response.append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "uom_id": uom_id,
                "price": price,
                "uom_name": uom_name
            }
        )

    cursor.close()
    return response

if __name__ == '__main__':
    try:
        connection = get_sql_connection()
        if connection:
            print("Connected to MySQL successfully!")
            # Example usage
            products = get_all_product(connection)
            print("Products retrieved:", products)
    except mysql.connector.Error as err:
        print(f"Error in main execution: {err}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")
