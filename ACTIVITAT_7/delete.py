from connection import connect

# # Definimos la función 'delete_product' que eliminará un producto de la base de datos.
# La función recibe como parámetro el 'id' del producto que se quiere eliminar
def delete_product(id):
    conn = connect()
    # Ejecuta la consulta SQL para eliminar el producto con el 'id' proporcionado.
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Producto eliminado correctamente.")
