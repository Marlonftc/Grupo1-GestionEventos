from flask import Flask, jsonify, Response
from flask_cors import CORS
from src.factories.sql_factory import SQLEventoFactory
from src.factories.mongo_factory import MongoEventoFactory
from src.DAO.reporte_dao import ReporteDAO

app = Flask(__name__)
CORS(app)

# Configuración de conexión a SQL Server y MongoDB
sql_factory = SQLEventoFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoEventoFactory("mongodb://mongodb:27017/")

# Instancia de ReporteDAO
reporte_dao = ReporteDAO(sql_factory, mongo_factory)

# 🔹 Endpoint para obtener reportes combinados
@app.route('/reportes', methods=['GET'])
def obtener_reportes():
    reportes = reporte_dao.obtener_reportes()
    return Response(reportes, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)












