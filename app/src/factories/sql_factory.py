import pymssql

from ..factories.factory import EventoFactory
from ..DAO.sql_evento_dao import SQLEventoDAO
from ..DTO.boda_dto import BodaDTO
from ..DTO.cumpleanos_dto import CumpleanosDTO
from ..DTO.conferencia_dto import ConferenciaDTO


class SQLEventoFactory(EventoFactory):
    def __init__(self, host, port, database, user, password):
        try:
            self.conn = pymssql.connect(
                        server="sqlserver",
                        port=1433,  # Se debe usar como número entero, sin comillas
                        database="GestionEventos",
                        user="sa",
                        password="Mftc@2412",
                        as_dict=True,  # Devuelve los resultados como diccionarios
                        autocommit=True  # Habilita autocommit para evitar locks
            )

            print(" Conexión exitosa a SQL Server")
        except pymssql.DatabaseError as e:
            print(f" Error al conectar a la base de datos: {e}")
            raise

        self.dao = SQLEventoDAO(self.conn)

    def crear_evento(self, tipo, id_evento, nombre, fecha, ubicacion, extra):
        try:
            if tipo == "boda":
                evento = BodaDTO(id_evento, nombre, fecha, ubicacion, extra)
            elif tipo == "cumpleaños":
                evento = CumpleanosDTO(id_evento, nombre, fecha, ubicacion, extra)
            elif tipo == "conferencia":
                evento = ConferenciaDTO(id_evento, nombre, fecha, ubicacion, extra)
            else:
                raise ValueError(" Tipo de evento no soportado")

            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Eventos (nombre, fecha, ubicacion) VALUES (%s, %s, %s)",
                (evento.nombre, evento.fecha, evento.ubicacion)
            )
            cursor.close()  # Cierra el cursor después de usarlo

            print(f" Evento '{tipo}' insertado correctamente")
        except pymssql.DatabaseError as e:
            print(f" Error al insertar evento en SQL Server: {e}")
            raise

    def obtener_eventos(self):
        try:
            eventos = self.dao.get_all()
            print(" Eventos obtenidos correctamente")
            return eventos
        except pymssql.DatabaseError as e:
            print(f" Error al obtener eventos: {e}")
            raise


