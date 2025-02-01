import pymssql
from src.DTO.boda_dto import BodaDTO
from src.DTO.cumpleanos_dto import CumpleanosDTO
from src.DTO.conferencia_dto import ConferenciaDTO
from src.DAO.sql_evento_dao import SQLEventoDAO
from src.factories.evento_factory import EventoFactory  # ✅ Corrección

 # Importar EventoFactory

class SQLEventoFactory(EventoFactory):
    def __init__(self, host, port, database, user, password):
        self.conn = pymssql.connect(
            server="sqlserver",
            port=int(1433),
            database="GestionEventos",
            user="sa",
            password="Mftc@2412",
            as_dict=True
        )
        self.dao = SQLEventoDAO(self.conn)

    # 🔹 Crear un evento en la BD
    def crear_evento(self, tipo, id_evento, nombre, fecha, ubicacion):
        if tipo == "boda":
            evento = BodaDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "cumpleaños":
            evento = CumpleanosDTO(id_evento, nombre, fecha, ubicacion)
        elif tipo == "conferencia":
            evento = ConferenciaDTO(id_evento, nombre, fecha, ubicacion)
        else:
            raise ValueError("Tipo de evento no soportado")

        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Eventos (nombre, fecha, ubicacion, tipo) VALUES (%s, %s, %s, %s)",
            (evento.nombre, evento.fecha, evento.ubicacion, evento.tipo)
        )
        self.conn.commit()
        cursor.close()
    
    # 🔹 Obtener todos los eventos
    def obtener_eventos(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT id_evento, nombre, fecha, ubicacion, tipo FROM Eventos")
        eventos = cursor.fetchall()
        cursor.close()
        return eventos
    
    # 🔹 Obtener un evento por ID
    def obtener_evento_por_id(self, id_evento):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT id_evento, nombre, fecha, ubicacion, tipo FROM Eventos WHERE id_evento = %s", (id_evento,))
        evento = cursor.fetchone()
        cursor.close()
        return evento
    
    # 🔹 Actualizar un evento
    def actualizar_evento(self, id_evento, nombre, fecha, ubicacion):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE Eventos SET nombre = %s, fecha = %s, ubicacion = %s WHERE id_evento = %s",
            (nombre, fecha, ubicacion, id_evento)
        )
        self.conn.commit()
        cursor.close()
    
    # 🔹 Eliminar un evento
    def eliminar_evento(self, id_evento):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Eventos WHERE id_evento = %s", (id_evento,))
        self.conn.commit()
        cursor.close()
