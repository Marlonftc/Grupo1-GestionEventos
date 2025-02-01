from ..DTO.evento_dto import EventoDTO

class MongoEventoDAO:
    def __init__(self, db):
        self.db = db
        self.collection = self.db["eventos"]

    def insertar_evento(self, evento):
        evento_dict = evento.to_dict()
        evento_dict["event_id"] = evento.id_evento
        self.collection.insert_one(evento_dict)

    def actualizar_evento(self, event_id, evento):
        self.collection.update_one(
            {"event_id": event_id},
            {"$set": {
                "tipo": evento.tipo,
                "nombre": evento.nombre,
                "fecha": evento.fecha,
                "ubicacion": evento.ubicacion
            }}
        )

    def eliminar_evento(self, event_id):
        self.collection.delete_one({"event_id": event_id})

    def get_all(self):
        eventos = list(self.collection.find({}, {"_id": 0}))
        return eventos

    def get_by_id(self, event_id):
        evento = self.collection.find_one({"event_id": event_id}, {"_id": 0})
        return evento if evento else None
