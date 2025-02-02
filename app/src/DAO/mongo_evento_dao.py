# Importamos el DTO del evento para manejar la conversión a diccionario
from ..DTO.evento_dto import EventoDTO

class MongoEventoDAO:
    """
    Clase para manejar las operaciones CRUD de eventos en una base de datos MongoDB.
    """

    def __init__(self, db):
        """
        Constructor de la clase.
        
        :param db: Instancia de la base de datos MongoDB.
        """
        self.db = db
        self.collection = self.db["eventos"]  # Se define la colección donde se almacenarán los eventos

    def insertar_evento(self, evento):
        """
        Inserta un nuevo evento en la base de datos.
        
        :param evento: Instancia de EventoDTO con los datos del evento.
        """
        evento_dict = evento.to_dict()  # Convertimos el objeto evento a un diccionario
        evento_dict["event_id"] = evento.id_evento  # Agregamos un identificador único al evento
        
        # Insertamos el evento en la colección
        self.collection.insert_one(evento_dict)

    def editar_evento(self, event_id, evento):
        """
        Actualiza los datos de un evento existente en la base de datos.

        :param event_id: Identificador del evento a actualizar.
        :param evento: Instancia de EventoDTO con los datos actualizados.
        :return: True si el evento fue modificado, False si no se encontró o no se modificó.
        """
        result = self.db["eventos"].update_one(
            {"event_id": event_id},  # Buscamos el evento por su ID
            {"$set": {  # Definimos los campos a actualizar
                "categoria": evento.categoria,
                "tipo": evento.tipo,
                "nombre": evento.nombre,
                "fecha": evento.fecha,
                "ubicacion": evento.ubicacion
            }}
        )
        return result.modified_count > 0  # Retorna True si se modificó al menos un documento

    def eliminar_evento(self, event_id):
        """
        Elimina un evento de la base de datos.

        :param event_id: Identificador del evento a eliminar.
        """
        self.collection.delete_one({"event_id": event_id})  # Eliminamos el evento usando su ID

    def get_all(self):
        """
        Obtiene todos los eventos almacenados en la base de datos.

        :return: Lista de eventos como diccionarios.
        """
        eventos = list(self.collection.find({}, {"_id": 0}))  # Excluimos el campo _id de MongoDB
        return eventos

    def get_by_id(self, event_id):
        """
        Obtiene un evento por su identificador único.

        :param event_id: Identificador del evento a buscar.
        :return: Diccionario con los datos del evento o None si no se encuentra.
        """
        evento = self.collection.find_one({"event_id": event_id}, {"_id": 0})  # Buscamos el evento por ID
        return evento if evento else None  # Retornamos el evento o None si no existe
