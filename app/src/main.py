from flask import Flask, jsonify
from factories.sql_factory import SQLFactory
from factories.mongo_factory import MongoFactory

app = Flask(__name__)

sql_factory = SQLFactory("sqlserver", "1433", "GestionEventos", "sa", "Mftc@2412")
mongo_factory = MongoFactory("mongodb://mongodb:27017/")

@app.route('/eventos', methods=['GET'])
def listar_eventos():
    eventos = sql_factory.get_all()
    return jsonify(eventos)

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = mongo_factory.get_all()
    return jsonify(clientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
