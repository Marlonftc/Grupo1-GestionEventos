from pymongo import MongoClient  # ✅ Asegúrate de importar MongoClient
from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from ..DAO.mongo_evento_dao import MongoEventoDAO
from src.factories.evento_factory import EventoFactory  # ✅ Importa correctamente la clase base

class MongoEventoFactory:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["GestionEventos"]

    def insertar_evento(self, evento_id, asistentes, servicios, presupuesto):
        self.db["eventos"].insert_one({
            "evento_id": evento_id,
            "asistentes": asistentes,
            "servicios": servicios,
            "presupuesto": presupuesto
        })

    def actualizar_evento(self, evento_id, asistentes, servicios, presupuesto):
        self.db["eventos"].update_one(
            {"evento_id": evento_id},
            {"$set": {"asistentes": asistentes, "servicios": servicios, "presupuesto": presupuesto}}
        )

    def eliminar_evento(self, evento_id):
        self.db["eventos"].delete_one({"evento_id": evento_id})

    def obtener_eventos(self):
        return list(self.db["eventos"].find({}, {"_id": 0}))


