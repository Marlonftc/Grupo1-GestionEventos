from flask import Flask, jsonify, request
from .factories.sql_factory import SQLEventoFactory
from .factories.mongo_factory import MongoEventoFactory

app = Flask(__name__)

sql_factory = SQLEventoFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoEventoFactory("mongodb://mongodb:27017/")

@app.route('/eventos', methods=['POST'])
def crear_evento():
    data = request.json
    tipo_base = data.get("tipo_base")  # "sql" o "mongo"
    tipo_evento = data.get("tipo_evento")  # "boda", "cumpleaños", "conferencia"
    
    if tipo_base == "sql":
        sql_factory.crear_evento(tipo_evento, data["id_evento"], data["nombre"], data["fecha"], data["ubicacion"], data["extra"])
    else:
        mongo_factory.crear_evento(tipo_evento, data["id_evento"], data["nombre"], data["fecha"], data["ubicacion"], data["extra"])
    
    return jsonify({"mensaje": "Evento creado correctamente"}), 201
