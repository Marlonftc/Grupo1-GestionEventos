from pymongo import MongoClient

class MongoFactory:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["GestionEventos"]

    def get_all(self):
        return list(self.db["Clientes"].find({}, {"_id": 0}))
