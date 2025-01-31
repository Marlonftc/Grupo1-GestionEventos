class MongoEventoDAO:
    def __init__(self, db):
        self.collection = db["Eventos"]

    def get_all(self):
        """Obtiene todos los eventos almacenados en MongoDB"""
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, event_id):
        """Obtiene un evento específico por ID"""
        return self.collection.find_one({"evento_id": event_id}, {"_id": 0})

    def insert(self, evento):
        """Inserta un nuevo evento con asistentes, servicios y presupuesto"""
        nuevo_evento = {
            "evento_id": evento["evento_id"],
            "asistentes": evento.get("asistentes", []),
            "servicios": evento.get("servicios", []),
            "presupuesto": evento.get("presupuesto", 0)
        }
        self.collection.insert_one(nuevo_evento)



