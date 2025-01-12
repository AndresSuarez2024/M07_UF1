from connection import connect

# Definimos la función 'update_product' que se utilizará para actualizar los detalles de un producto.
# La función recibe el 'id' del producto a actualizar y los nuevos valores para 'name', 'description', 
# 'price' y 'quantity', todos los cuales son opcionales
def update_product(id, name=None, description=None, price=None, quantity=None):
    conn = connect()
    if conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE products SET name = %s WHERE id = %s", (name, id))
        if description:
            cursor.execute("UPDATE products SET description = %s WHERE id = %s", (description, id))
        if price:
            cursor.execute("UPDATE products SET price = %s WHERE id = %s", (price, id))
        if quantity:
            cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (quantity, id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Producto actualizado correctamente.")
