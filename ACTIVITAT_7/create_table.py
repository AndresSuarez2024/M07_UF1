from connection import connect

def create_table():
    conn = connect()
    if conn:
        cursor = conn.cursor()
        # Ejecuta la consulta SQL para crear la tabla 'products'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            price NUMERIC(10, 2),
            quantity INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        # Guarda la creación de la tabla de manera permanent
        conn.commit()
        cursor.close()
        # Cierra la conexión con la base de datos.
        conn.close()
        print("Tabla creada correctamente.")

# Verifica si el script se ejecuta directamente, si es así se ejecuta la función create_table().
if __name__ == "__main__":
    create_table()
