import json
import datetime

class ReporteDAO:
    def __init__(self, sql_factory, mongo_factory):
        self.sql_factory = sql_factory
        self.mongo_factory = mongo_factory

    # 🔹 Función para serializar fechas
    def custom_serializer(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        raise TypeError(f"Tipo de dato {type(obj)} no serializable")

    # 🔹 Obtener reportes combinados de SQL y MongoDB
    def obtener_reportes(self):
        try:
            # Obtener eventos desde SQL Server
            eventos_sql = self.sql_factory.dao.obtener_eventos()

            # Obtener información adicional desde MongoDB
            eventos_mongo = list(self.mongo_factory.db["eventos"].find({}, {"_id": 0}))
            feedbacks = list(self.mongo_factory.db["feedback"].find({}, {"_id": 0}))

            reportes = []
            for evento in eventos_sql:
                evento_id = evento["id_evento"]

                # Buscar información en MongoDB
                datos_mongo = next((ev for ev in eventos_mongo if ev.get("event_id") == evento_id), {})

                # 🔹 Filtrar feedbacks que coincidan con event_id
                feedback_evento = [fb for fb in feedbacks if fb.get("event_id") == evento_id]

                # Construcción del reporte
                reporte = {
                    "id_evento": evento_id,
                    "nombre": evento["nombre"],
                    "fecha": evento["fecha"],
                    "ubicacion": evento["ubicacion"],
                    "asistentes": datos_mongo.get("asistentes", 0),
                    "servicios": datos_mongo.get("servicios", []),
                    "presupuesto": datos_mongo.get("presupuesto", 0),
                    "feedbacks": [
                        {
                            "cliente": fb["client_id"],
                            "rating": fb["rating"],
                            "comentario": fb["comments"]
                        }
                        for fb in feedback_evento
                    ]  # 🔹 Esto asegurará que se listen todos los feedbacks relacionados con el evento
                }
                reportes.append(reporte)

            return json.dumps(reportes, ensure_ascii=False, default=self.custom_serializer)

        except Exception as e:
            return json.dumps({"error": "Error al obtener reportes", "detalle": str(e)}), 500
