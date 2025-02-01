from src.DAO.sql_evento_dao import SQLEventoDAO
from src.DAO.mongo_evento_dao import MongoEventoDAO

class EventoDAORouter:
    """Clase que elige dinámicamente el DAO correcto según el origen de datos"""

    def __init__(self, sql_factory, mongo_factory):
        self.sql_dao = SQLEventoDAO(sql_factory.conn)
        self.mongo_dao = MongoEventoDAO(mongo_factory.db)

    def insertar_evento(self, evento, origen):
        """
        Inserta un evento en la base de datos correspondiente
        :param evento: Objeto evento generado por la fábrica
        :param origen: 'sql' para SQL Server o 'mongo' para MongoDB
        """
        if origen == "sql":
            return self.sql_dao.insertar_evento(evento)
        elif origen == "mongo":
            return self.mongo_dao.insertar_evento(evento)
        else:
            raise ValueError("Origen no soportado, debe ser 'sql' o 'mongo'")

    def actualizar_evento(self, event_id, evento, origen):
        """
        Actualiza un evento en la base de datos correspondiente
        :param event_id: ID del evento a actualizar
        :param evento: Datos del evento actualizados
        :param origen: 'sql' para SQL Server o 'mongo' para MongoDB
        """
        if origen == "sql":
            return self.sql_dao.actualizar_evento(event_id, evento)
        elif origen == "mongo":
            return self.mongo_dao.actualizar_evento(event_id, evento)
        else:
            raise ValueError("Origen no soportado, debe ser 'sql' o 'mongo'")

    def eliminar_evento(self, event_id, origen):
        """
        Elimina un evento de la base de datos correspondiente
        :param event_id: ID del evento a eliminar
        :param origen: 'sql' para SQL Server o 'mongo' para MongoDB
        """
        if origen == "sql":
            return self.sql_dao.eliminar_evento(event_id)
        elif origen == "mongo":
            return self.mongo_dao.eliminar_evento(event_id)
        else:
            raise ValueError("Origen no soportado, debe ser 'sql' o 'mongo'")

