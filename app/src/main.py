from flask import Flask, jsonify, Response
from flask_cors import CORS
from flasgger import Swagger
from src.factories.sql_factory import SQLEventoFactory
from src.factories.mongo_factory import MongoEventoFactory
from src.DAO.reporte_dao import ReporteDAO

app = Flask(__name__)
CORS(app)

# 🔹 Configuración personalizada de Swagger con enlace a GitHub
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Gestión de Eventos",
        "description": "Documentación de la API para la gestión de eventos en SQL Server y MongoDB.\n\n"
                       "**📌 [Repositorio en GitHub](https://github.com/Marlonftc/Grupo1-GestionEventos)**",
        "version": "1.0.0",
        "license": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT"
        }
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http"]
}

# Inicializar Flasgger con la configuración personalizada
swagger = Swagger(app, template=swagger_template)

# 🔹 Configuración de conexión a SQL Server y MongoDB
sql_factory = SQLEventoFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoEventoFactory("mongodb://mongodb:27017/")

# Instancia de ReporteDAO
reporte_dao = ReporteDAO(sql_factory, mongo_factory)

# 🔹 Endpoint para obtener reportes combinados
@app.route('/reportes', methods=['GET'])
def obtener_reportes():
    """
    Obtener reportes combinados de SQL Server y MongoDB
    ---
    tags:
      - Reportes
    responses:
      200:
        description: Lista de reportes combinados
    """
    reportes = reporte_dao.obtener_reportes()
    return Response(reportes, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
