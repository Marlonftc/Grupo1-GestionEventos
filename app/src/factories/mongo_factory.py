from pymongo import MongoClient  # ✅ Asegúrate de importar MongoClient
from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from ..DAO.mongo_evento_dao import MongoEventoDAO
from src.factories.evento_factory import EventoFactory  # ✅ Importa correctamente la clase base

class MongoEventoFactory(EventoFactory):
    def __init__(self, uri):
        super().__init__()  # ✅ Llamar al constructor de la clase base
        self.client = MongoClient(uri)               
        self.db = self.client["GestionEventos"]
        self.dao = MongoEventoDAO(self.db)

    def obtener_eventos(self):
        """Obtiene todos los eventos almacenados en MongoDB"""
        eventos = list(self.db["eventos"].find({}, {"_id": 0}))  # ✅ Ahora está correctamente indentado
        return eventos

    def crear_evento(self, tipo, id_evento, nombre, fecha, ubicacion):
        if tipo == "boda":
            evento = BodaDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "cumpleaños":
            evento = CumpleanosDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "conferencia":
            evento = ConferenciaDTO(id_evento, nombre, fecha, ubicacion)
        else:
            raise ValueError("Tipo de evento no soportado")

        self.db["Eventos"].insert_one(evento.to_dict())  # ✅ Inserta correctamente el evento en MongoDB


