from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import datetime
from src.factories.sql_factory import SQLEventoFactory
from src.factories.mongo_factory import MongoEventoFactory

app = Flask(__name__)
CORS(app)

# Configuración de conexión a SQL Server y MongoDB
sql_factory = SQLEventoFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoEventoFactory("mongodb://mongodb:27017/")

# Función para serializar fechas
def custom_serializer(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Tipo de dato {type(obj)} no serializable")

# 🔹 Obtener reportes combinados de SQL y MongoDB
@app.route('/reportes', methods=['GET'])
def obtener_reportes():
    try:
        # Obtener eventos desde SQL Server
        eventos_sql = sql_factory.dao.obtener_eventos()
        
        # Obtener información adicional desde MongoDB
        eventos_mongo = list(mongo_factory.db["eventos"].find({}, {"_id": 0}))  
        feedbacks = list(mongo_factory.db["feedback"].find({}, {"_id": 0}))

        reportes = []
        for evento in eventos_sql:
            evento_id = evento["id_evento"]

            # Buscar información en MongoDB
            datos_mongo = next((ev for ev in eventos_mongo if ev["event_id"] == evento_id), {})
            feedback_evento = [fb for fb in feedbacks if fb["event_id"] == evento_id]

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
                    {"cliente": fb["client_id"], "rating": fb["rating"], "comentario": fb["comments"]}
                    for fb in feedback_evento
                ] if feedback_evento else []
            }
            reportes.append(reporte)

        return Response(json.dumps(reportes, ensure_ascii=False, default=custom_serializer), mimetype="application/json")
    except Exception as e:
        return jsonify({"error": "Error al obtener reportes", "detalle": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
















