from connection import connect

# Definimos la función 'create_product' que recibe los parámetros nombre, descripción, precio y cantidad.
def create_product(name, description, price, quantity):
    conn = connect()
    if conn:
        cursor = conn.cursor()
        # Ejecuta una consulta SQL para insertar un nuevo producto en la tabla 'products'.
        cursor.execute("""
        INSERT INTO products (name, description, price, quantity)
        VALUES (%s, %s, %s, %s)
        """, (name, description, price, quantity))
        conn.commit()
        cursor.close()
        conn.close()
        print("Producto creado correctamente.")
