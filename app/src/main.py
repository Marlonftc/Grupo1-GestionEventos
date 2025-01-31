from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import datetime
from factories.sql_factory import SQLEventoFactory
from factories.mongo_factory import MongoEventoFactory

app = Flask(__name__)
CORS(app)

# Conectar a SQL Server y MongoDB
sql_factory = SQLEventoFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoEventoFactory("mongodb://mongodb:27017/")

# Serializador para fechas
def custom_serializer(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Tipo de dato {type(obj)} no serializable")

# 🔹 Obtener todos los eventos combinados
@app.route('/reportes', methods=['GET'])
def obtener_reportes():
    try:
        eventos_sql = sql_factory.obtener_eventos()
        eventos_mongo = mongo_factory.obtener_eventos()
        feedbacks = list(mongo_factory.db["feedback"].find({}, {"_id": 0}))

        reportes = []
        for evento in eventos_sql:
            evento_id = evento["id_evento"]
            datos_mongo = next((ev for ev in eventos_mongo if ev["evento_id"] == evento_id), None)
            feedback = [fb for fb in feedbacks if fb["event_id"] == str(evento_id)]

            reporte = {
                "id_evento": evento_id,
                "nombre": evento["nombre"],
                "fecha": evento["fecha"],
                "ubicacion": evento["ubicacion"],
                "asistentes": datos_mongo["asistentes"] if datos_mongo else [],
                "servicios": datos_mongo["servicios"] if datos_mongo else [],
                "presupuesto": datos_mongo["presupuesto"] if datos_mongo else 0,
                "feedbacks": feedback
            }
            reportes.append(reporte)

        return Response(json.dumps(reportes, ensure_ascii=False, default=custom_serializer), mimetype="application/json")
    except Exception as e:
        return jsonify({"error": "Error al obtener reportes", "detalle": str(e)}), 500

# 🔹 Crear un nuevo evento
@app.route('/eventos', methods=['POST'])
def crear_evento():
    try:
        datos = request.json
        if not datos.get("nombre") or not datos.get("fecha") or not datos.get("ubicacion"):
            return jsonify({"error": "Faltan datos"}), 400

        evento_id = sql_factory.dao.insert({
            "nombre": datos["nombre"],
            "fecha": datos["fecha"],
            "ubicacion": datos["ubicacion"]
        })

        mongo_factory.dao.insert({
            "evento_id": evento_id,
            "asistentes": datos.get("asistentes", []),
            "servicios": datos.get("servicios", []),
            "presupuesto": datos.get("presupuesto", 0)
        })

        return jsonify({"message": "Evento creado", "id_evento": evento_id}), 201
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

# 🔹 Actualizar un evento
@app.route('/eventos/<int:event_id>', methods=['PUT'])
def actualizar_evento(event_id):
    try:
        datos = request.json
        if not datos.get("nombre") or not datos.get("fecha") or not datos.get("ubicacion"):
            return jsonify({"error": "Faltan datos"}), 400

        sql_factory.dao.update(event_id, {
            "nombre": datos["nombre"],
            "fecha": datos["fecha"],
            "ubicacion": datos["ubicacion"]
        })

        mongo_factory.dao.update(event_id, {
            "asistentes": datos.get("asistentes", []),
            "servicios": datos.get("servicios", []),
            "presupuesto": datos.get("presupuesto", 0)
        })

        return jsonify({"message": "Evento actualizado"}), 200
    except Exception as e:
        return jsonify({"error": "Error al actualizar evento", "detalle": str(e)}), 500

# 🔹 Eliminar un evento
@app.route('/eventos/<int:event_id>', methods=['DELETE'])
def eliminar_evento(event_id):
    try:
        sql_factory.dao.delete(event_id)
        mongo_factory.dao.delete(event_id)
        return jsonify({"message": "Evento eliminado"}), 200
    except Exception as e:
        return jsonify({"error": "Error al eliminar evento", "detalle": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)







