from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from ..DAO.mongo_evento_dao import MongoEventoDAO

class MongoEventoFactory(EventoFactory):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["GestionEventos"]
        self.dao = MongoEventoDAO(self.db)

    def crear_evento(self, tipo, id_evento, nombre, fecha, ubicacion):
        if tipo == "boda":
            evento = BodaDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "cumpleaños":
            evento = CumpleanosDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "conferencia":
            evento = ConferenciaDTO(id_evento, nombre, fecha, ubicacion)
        else:
            raise ValueError("Tipo de evento no soportado")

        self.db["Eventos"].insert_one(evento.to_dict())

