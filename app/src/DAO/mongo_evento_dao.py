# app/src/dao/mongo_evento_dao.py
class MongoEventoDAO:
    def __init__(self, db):
        self.collection = db["Eventos"]

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))