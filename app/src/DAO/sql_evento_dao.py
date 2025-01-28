# app/src/dao/sql_evento_dao.py

from ..DTO.evento_dto import EventoDTO
class SQLEventoDAO:
    def __init__(self, connection):
        self.conn = connection

    def get_all(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos")
        return [EventoDTO(**row).to_dict() for row in cursor]