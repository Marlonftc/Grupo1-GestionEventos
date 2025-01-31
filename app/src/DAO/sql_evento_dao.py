from ..DTO.evento_dto import EventoDTO

class SQLEventoDAO:
    def __init__(self, connection):
        self.conn = connection

    def get_all(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos")
        return [EventoDTO(**row).to_dict() for row in cursor]

    def get_by_id(self, event_id):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos WHERE id_evento = %s", (event_id,))
        row = cursor.fetchone()
        return EventoDTO(**row).to_dict() if row else None

    def obtener_eventos(self):  # <-- Se eliminó el espacio extra antes de "def"
        """Obtiene todos los eventos almacenados en SQL Server"""
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT id_evento, nombre, fecha, ubicacion FROM Eventos")
        eventos = cursor.fetchall()
        cursor.close()
        return eventos


