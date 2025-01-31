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

