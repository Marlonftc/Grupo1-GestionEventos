from pymongo import MongoClient  # ✅ Importamos MongoClient para conectar con MongoDB
from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from ..DAO.mongo_evento_dao import MongoEventoDAO
from src.factories.evento_factory import EventoFactory  # ✅ Importa correctamente la clase base

class MongoEventoFactory:
    """
    Fábrica para la gestión de eventos almacenados en MongoDB.
    Permite insertar, actualizar, eliminar y obtener eventos en la base de datos 'gestion-de-eventos'.
    """

    def __init__(self, uri):
        """
        Constructor de la fábrica de eventos en MongoDB.

        :param uri: URI de conexión a MongoDB.
        """
        self.client = MongoClient(uri)  # 🔹 Conexión a MongoDB usando la URI proporcionada
        self.db = self.client["gestion-de-eventos"]  # 🔹 Seleccionamos la base de datos 'gestion-de-eventos'

    def insertar_evento(self, evento_id, asistentes, servicios, presupuesto):
        """
        Inserta un nuevo evento en la base de datos MongoDB.

        :param evento_id: Identificador único del evento.
        :param asistentes: Número de asistentes al evento.
        :param servicios: Lista de servicios contratados para el evento.
        :param presupuesto: Presupuesto asignado al evento.
        """
        self.db["eventos"].insert_one({
            "evento_id": evento_id,
            "asistentes": asistentes,
            "servicios": servicios,
            "presupuesto": presupuesto
        })

    def actualizar_evento(self, evento_id, asistentes, servicios, presupuesto):
        """
        Actualiza un evento existente en MongoDB.

        :param evento_id: Identificador único del evento a actualizar.
        :param asistentes: Número de asistentes actualizado.
        :param servicios: Lista de servicios actualizados.
        :param presupuesto: Presupuesto actualizado.
        """
        self.db["eventos"].update_one(
            {"evento_id": evento_id},  # 🔹 Se busca el evento por su ID
            {"$set": {
                "asistentes": asistentes,
                "servicios": servicios,
                "presupuesto": presupuesto
            }}
        )

    def eliminar_evento(self, evento_id):
        """
        Elimina un evento de la base de datos MongoDB.

        :param evento_id: Identificador único del evento a eliminar.
        """
        self.db["eventos"].delete_one({"evento_id": evento_id})

    def obtener_eventos(self):
        """
        Obtiene todos los eventos almacenados en la base de datos MongoDB.

        :return: Lista de eventos en formato de diccionario.
        """
        return list(self.db["eventos"].find({}, {"_id": 0}))  # 🔹 Excluimos el campo `_id` de MongoDB en la consulta


