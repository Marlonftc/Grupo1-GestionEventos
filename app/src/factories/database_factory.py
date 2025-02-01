from pymongo import MongoClient
import pyodbc

class DatabaseFactory:
    def __init__(self, db_type, **kwargs):
        """
        db_type: "sql" para SQL Server, "mongo" para MongoDB.
        kwargs: Parámetros para la conexión.
        """
        self.db_type = db_type
        self.connection = None

        if db_type == "sql":
            self.connection = pyodbc.connect(
                f"DRIVER={{SQL Server}};SERVER={kwargs['server']},{kwargs['port']};DATABASE={kwargs['database']};UID={kwargs['user']};PWD={kwargs['password']}"
            )
            self.cursor = self.connection.cursor()

        elif db_type == "mongo":
            self.client = MongoClient(kwargs['uri'])
            self.db = self.client[kwargs['database']]

        else:
            raise ValueError("Tipo de base de datos no soportado")

    def get_sql_cursor(self):
        if self.db_type == "sql":
            return self.cursor
        raise Exception("No es una conexión SQL")

    def get_mongo_collection(self, collection_name):
        if self.db_type == "mongo":
            return self.db[collection_name]
        raise Exception("No es una conexión MongoDB")

    def close_connection(self):
        if self.db_type == "sql":
            self.connection.close()
        elif self.db_type == "mongo":
            self.client.close()
