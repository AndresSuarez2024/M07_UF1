from connection import connect

def read_products():
    conn = connect()
    # Verifica si se a conectado
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products;")
        # Recupera todas las filas obtenidas de la consulta SQL y devuelve una lista de tuplas con todos los registros.
        rows = cursor.fetchall()
        # Recorre cada fila y la imprime en consola.
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
