import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            database="BBDDPostgres",
            user="andres",
            password="Coco120604",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error al conectar a la base de datos", e)
        return None