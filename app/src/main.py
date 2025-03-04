from flask import Flask, jsonify, Response, request
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flasgger import Swagger
from src.factories.sql_factory import SQLEventoFactory
from src.factories.mongo_factory import MongoEventoFactory
from src.DAO.reporte_dao import ReporteDAO
from src.routers.evento_factory_router import EventoFactoryRouter
from src.routers.evento_dao_router import EventoDAORouter
import datetime

app = Flask(__name__)
# 🔹 Habilitar CORS para TODOS los métodos y TODOS los orígenes
CORS(app, resources={r"/*": {"origins": "*"}},
     supports_credentials=True,
     allow_headers=["Origin", "Content-Length", "Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE"])


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

# Instancia de DAOs
reporte_dao = ReporteDAO(sql_factory, mongo_factory)
evento_router = EventoDAORouter(sql_factory, mongo_factory)

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

@app.route('/eventos', methods=['POST'])
def crear_evento():
    """
    Crear un nuevo evento en SQL Server o MongoDB
    ---
    tags:
      - Eventos
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            categoria:
              type: string
              example: "social"
            tipo:
              type: string
              example: "boda"
            nombre:
              type: string
              example: "Boda de Ana"
            fecha:
              type: string
              format: date
              example: "2025-03-15"
            ubicacion:
              type: string
              example: "Quito"
            origen:
              type: string
              enum: ["sql", "mongo"]
              example: "sql"
    responses:
      201:
        description: Evento creado exitosamente
      400:
        description: Error en los datos enviados
      500:
        description: Error interno del servidor
    """
    try:
        datos = request.json
        categoria = datos.get("categoria")
        tipo = datos.get("tipo")
        nombre = datos.get("nombre")
        fecha = datos.get("fecha")
        ubicacion = datos.get("ubicacion")
        origen = datos.get("origen")  # Decide dónde se almacenará ('sql' o 'mongo')

        if not categoria or not tipo or not nombre or not fecha or not ubicacion or not origen:
            return jsonify({"error": "Faltan datos"}), 400

        # Seleccionar la fábrica según la categoría
        fabrica = EventoFactoryRouter(categoria).obtener_factory()

        # Crear el evento usando la fábrica correspondiente
        evento = fabrica.crear_evento(tipo, nombre, fecha, ubicacion, categoria)

        # Guardar en la base de datos correcta
        evento_router.insertar_evento(evento, origen)

        return jsonify({"message": f"Evento creado en {origen}", "evento": evento.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

@app.route('/eventos/<int:event_id>', methods=['DELETE'])
def eliminar_evento(event_id):
    """
    Eliminar un evento de SQL Server o MongoDB
    ---
    tags:
      - Eventos
    parameters:
      - name: event_id
        in: path
        required: true
        type: integer
        example: 1
      - name: origen
        in: query
        required: true
        type: string
        enum: ["sql", "mongo"]
        example: "sql"
    responses:
      200:
        description: Evento eliminado exitosamente
      400:
        description: Falta el parámetro de origen
      404:
        description: Evento no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        origen = request.args.get("origen")
        if not origen:
            return jsonify({"error": "Se debe especificar el origen (sql o mongo)"}), 400

        eliminado = evento_router.eliminar_evento(event_id, origen)
        if eliminado:
            return jsonify({"message": f"Evento eliminado de {origen}"}), 200
        else:
            return jsonify({"error": "Evento no encontrado"}), 404  # 🔹 Maneja cuando no se encuentra el evento
    except Exception as e:
        return jsonify({"error": "Error al eliminar el evento", "detalle": str(e)}), 500
      
@app.route('/eventos/<int:evento_id>', methods=['PUT'])
def editar_evento(evento_id):
    """
    Editar un evento existente en SQL Server o MongoDB
    ---
    tags:
      - Eventos
    parameters:
      - name: evento_id
        in: path
        required: true
        type: integer
        description: ID del evento a actualizar
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            categoria:
              type: string
              example: "social"
            tipo:
              type: string
              example: "boda"
            nombre:
              type: string
              example: "Boda de Ana"
            fecha:
              type: string
              format: date
              example: "2025-03-15"
            ubicacion:
              type: string
              example: "Quito"
            origen:
              type: string
              enum: ["sql", "mongo"]
              example: "sql"
    responses:
      200:
        description: Evento actualizado exitosamente
      400:
        description: Error en los datos enviados
      404:
        description: Evento no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        datos = request.json
        categoria = datos.get("categoria")
        tipo = datos.get("tipo")
        nombre = datos.get("nombre")
        fecha = datos.get("fecha")
        ubicacion = datos.get("ubicacion")
        origen = datos.get("origen")

        if not categoria or not tipo or not nombre or not fecha or not ubicacion or not origen:
            return jsonify({"error": "Faltan datos"}), 400

        # Seleccionar la fábrica según la categoría
        fabrica = EventoFactoryRouter(categoria).obtener_factory()

        # Crear el objeto evento actualizado
        evento = fabrica.crear_evento(tipo, nombre, fecha, ubicacion, categoria)

        # Actualizar en la base de datos correspondiente
        actualizado = evento_router.editar_evento(evento_id, evento, origen)

        if actualizado:
            return jsonify({"message": f"Evento actualizado en {origen}"}), 200
        else:
            return jsonify({"error": "Evento no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

# Configuración de JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta"
jwt = JWTManager(app)

bcrypt = Bcrypt(app)

# Simulación de una base de datos de usuarios
usuarios = {
    "admin": bcrypt.generate_password_hash("admin123").decode("utf-8"),
    "usuario": bcrypt.generate_password_hash("usuario123").decode("utf-8"),
}

@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint para autenticar usuarios y generar un token JWT.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in usuarios and bcrypt.check_password_hash(usuarios[username], password):
        token = create_access_token(identity=username, expires_delta=datetime.timedelta(hours=1))
        return jsonify({"token": token, "user": username}), 200

    return jsonify({"message": "Credenciales incorrectas"}), 401

@app.route("/protegido", methods=["GET"])
@jwt_required()
def ruta_protegida():
    """
    Ruta protegida para probar autenticación.
    """
    usuario_actual = get_jwt_identity()
    return jsonify({"message": f"Bienvenido {usuario_actual}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
