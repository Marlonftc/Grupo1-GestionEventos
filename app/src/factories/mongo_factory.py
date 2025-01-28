from ..factories.factory import EventoFactory
from ..DAO.mongo_evento_dao import MongoEventoDAO
from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleañosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from pymongo import MongoClient

class MongoEventoFactory(EventoFactory):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["GestionEventos"]
        self.dao = MongoEventoDAO(self.db)

    def crear_evento(self, tipo, id_evento, nombre, fecha, ubicacion, extra):
        if tipo == "boda":
            evento = BodaDTO(id_evento, nombre, fecha, ubicacion, extra)
        elif tipo == "cumpleaños":
            evento = CumpleañosDTO(id_evento, nombre, fecha, ubicacion, extra)
        elif tipo == "conferencia":
            evento = ConferenciaDTO(id_evento, nombre, fecha, ubicacion, extra)
        else:
            raise ValueError("Tipo de evento no soportado")

        self.db["Eventos"].insert_one(evento.to_dict())

    def obtener_eventos(self):
        return self.dao.get_all()
