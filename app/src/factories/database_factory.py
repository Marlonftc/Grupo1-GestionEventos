from pymongo import MongoClient
import pyodbc

class DatabaseFactory:
    """
    Clase Factory para manejar conexiones a bases de datos SQL Server y MongoDB.
    """

    def __init__(self, db_type, **kwargs):
        """
        Inicializa la conexión a la base de datos especificada.

        :param db_type: Tipo de base de datos ("sql" para SQL Server, "mongo" para MongoDB).
        :param kwargs: Parámetros de conexión (servidor, usuario, contraseña, etc.).
        """
        self.db_type = db_type
        self.connection = None

        if db_type == "sql":
            # 🔹 Conexión a SQL Server
            self.connection = pyodbc.connect(
                f"DRIVER={{SQL Server}};SERVER={kwargs['server']},{kwargs['port']};"
                f"DATABASE={kwargs['database']};UID={kwargs['user']};PWD={kwargs['password']}"
            )
            self.cursor = self.connection.cursor()  # 🔹 Se crea un cursor para ejecutar consultas SQL

        elif db_type == "mongo":
            # 🔹 Conexión a MongoDB
            self.client = MongoClient(kwargs['uri'])
            self.db = self.client[kwargs['database']]  # 🔹 Se obtiene la base de datos

        else:
            raise ValueError("Tipo de base de datos no soportado")  # 🔹 Manejo de error para tipos no válidos

    def get_sql_cursor(self):
        """
        Retorna el cursor para consultas SQL Server.

        :return: Cursor SQL Server.
        :raises Exception: Si la conexión no es de tipo SQL.
        """
        if self.db_type == "sql":
            return self.cursor
        raise Exception("No es una conexión SQL")

    def get_mongo_collection(self, collection_name):
        """
        Retorna una colección de MongoDB.

        :param collection_name: Nombre de la colección a obtener.
        :return: Objeto de colección MongoDB.
        :raises Exception: Si la conexión no es de tipo MongoDB.
        """
        if self.db_type == "mongo":
            return self.db[collection_name]
        raise Exception("No es una conexión MongoDB")

    def close_connection(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.db_type == "sql":
            self.connection.close()
        elif self.db_type == "mongo":
            self.client.close()
