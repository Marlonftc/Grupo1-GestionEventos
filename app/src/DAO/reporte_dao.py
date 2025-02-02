import json
import datetime

class ReporteDAO:
    """
    Clase para gestionar la obtención de reportes combinando datos de SQL Server y MongoDB.
    """

    def __init__(self, sql_factory, mongo_factory):
        """
        Constructor de la clase ReporteDAO.

        :param sql_factory: Fábrica de acceso a SQL Server (Abstract Factory para DAO SQL).
        :param mongo_factory: Fábrica de acceso a MongoDB (Abstract Factory para DAO MongoDB).
        """
        self.sql_factory = sql_factory
        self.mongo_factory = mongo_factory

    # 🔹 Función para serializar fechas en formato JSON
    def custom_serializer(self, obj):
        """
        Serializa objetos datetime a formato ISO 8601 para ser compatible con JSON.

        :param obj: Objeto a serializar.
        :return: Representación en string del objeto si es fecha/hora.
        :raises TypeError: Si el tipo de dato no es serializable.
        """
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()  # Convierte la fecha en una cadena ISO 8601 (YYYY-MM-DDTHH:MM:SS)
        raise TypeError(f"Tipo de dato {type(obj)} no serializable")

    # 🔹 Obtener reportes combinados de SQL y MongoDB
    def obtener_reportes(self):
        """
        Obtiene los reportes combinando datos de SQL Server y MongoDB.

        :return: JSON con los reportes de eventos.
        :raises Exception: Captura y devuelve errores en formato JSON si ocurre un fallo.
        """
        try:
            # 🔹 Obtener eventos almacenados en SQL Server
            eventos_sql = self.sql_factory.dao.obtener_eventos()

            # 🔹 Obtener datos adicionales desde MongoDB
            eventos_mongo = list(self.mongo_factory.db["eventos"].find({}, {"_id": 0}))  # Eliminamos el campo _id de MongoDB
            feedbacks = list(self.mongo_factory.db["feedback"].find({}, {"_id": 0}))  # Eliminamos el campo _id para compatibilidad

            reportes = []
            for evento in eventos_sql:
                evento_id = evento["id_evento"]  # ID del evento en SQL Server

                # 🔹 Buscar información en MongoDB asociada al evento
                datos_mongo = next((ev for ev in eventos_mongo if ev.get("event_id") == evento_id), {})

                # 🔹 Filtrar feedbacks que coincidan con event_id
                feedback_evento = [fb for fb in feedbacks if fb.get("event_id") == evento_id]

                # 🔹 Construcción del reporte final con datos combinados
                reporte = {
                    "id_evento": evento_id,
                    "nombre": evento["nombre"],
                    "fecha": evento["fecha"],
                    "ubicacion": evento["ubicacion"],
                    "categoria": evento["categoria"],
                    "tipo": evento["tipo"],
                    "asistentes": datos_mongo.get("asistentes", 0),  # Valor por defecto: 0 si no hay datos
                    "servicios": datos_mongo.get("servicios", []),  # Lista vacía si no hay datos
                    "presupuesto": datos_mongo.get("presupuesto", 0),  # Valor por defecto: 0
                    "feedbacks": [
                        {
                            "cliente": fb["client_id"],
                            "rating": fb["rating"],
                            "comentario": fb["comments"]
                        }
                        for fb in feedback_evento
                    ]  # 🔹 Lista con feedbacks relacionados con el evento
                }
                reportes.append(reporte)  # Agregar el reporte a la lista

            # 🔹 Convertimos la lista de reportes a formato JSON asegurando compatibilidad con fechas
            return json.dumps(reportes, ensure_ascii=False, default=self.custom_serializer)

        except Exception as e:
            # 🔹 Captura y manejo de errores, retornando una respuesta JSON con detalles del problema
            return json.dumps({"error": "Error al obtener reportes", "detalle": str(e)}), 500
