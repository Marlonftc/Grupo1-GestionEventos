from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO
from ..DAO.sql_evento_dao import SQLEventoDAO

class SQLEventoFactory(EventoFactory):
    def __init__(self, host, port, database, user, password):
        self.conn = pymssql.connect(
            server=host,
            port=int(port),
            database=database,
            user=user,
            password=password,
            as_dict=True
        )
        self.dao = SQLEventoDAO(self.conn)

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
