import pymssql

class SQLFactory:
    def __init__(self, host, port, database, user, password):
        try:
            # Usamos 'server' en lugar de 'host'
            self.conn = pymssql.connect(  # pylint: disable=no-member
                server=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
            print("Conexión a la base de datos establecida correctamente.")
        except pymssql.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def get_all(self):
        try:
            cursor = self.conn.cursor(as_dict=True)
            cursor.execute("SELECT * FROM Eventos")
            return list(cursor)
        except pymssql.DatabaseError as e:
            print(f"Error al ejecutar la consulta: {e}")
            raise
        finally:
            cursor.close()

if __name__ == "__main__":
    factory = SQLFactory(
        host="sqlserver",
        port="1433",
        database="GestionEventos",
        user="sa",
        password="Mftc@2412"
    )
    print(factory.get_all())
