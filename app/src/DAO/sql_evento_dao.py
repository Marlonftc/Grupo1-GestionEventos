# Importamos el DTO para manejar los eventos como objetos
from ..DTO.evento_dto import EventoDTO

class SQLEventoDAO:
    """
    Clase para manejar las operaciones CRUD de eventos en SQL Server.
    """

    def __init__(self, connection):
        """
        Constructor de la clase.

        :param connection: Objeto de conexión a SQL Server.
        """
        self.conn = connection

    def insertar_evento(self, evento):
        """
        Inserta un nuevo evento en la base de datos y devuelve su ID.

        :param evento: Instancia de EventoDTO con los datos del evento.
        :return: ID del evento insertado.
        """
        cursor = self.conn.cursor()
        query = """
        INSERT INTO Eventos (tipo, nombre, fecha, ubicacion, categoria) 
        OUTPUT INSERTED.id_evento VALUES (%s, %s, %s, %s, %s)
        """  # 🔹 La cláusula OUTPUT INSERTED.id_evento devuelve el ID generado automáticamente
        cursor.execute(query, (evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, evento.categoria))
        evento_id = cursor.fetchone()["id_evento"]  # 🔹 Obtenemos el ID del evento insertado
        self.conn.commit()  # 🔹 Guardamos los cambios en la base de datos
        cursor.close()  # 🔹 Cerramos el cursor para liberar recursos
        return evento_id

    def editar_evento(self, event_id, evento):
        """
        Actualiza los datos de un evento existente en la base de datos.

        :param event_id: ID del evento a actualizar.
        :param evento: Instancia de EventoDTO con los datos actualizados.
        :return: True si se actualizó correctamente, False si no.
        """
        cursor = self.conn.cursor()
        query = """
            UPDATE Eventos
            SET categoria = %s, tipo = %s, nombre = %s, fecha = %s, ubicacion = %s
            WHERE id_evento = %s
        """  # 🔹 Consulta para actualizar el evento por su ID
        cursor.execute(query, (evento.categoria, evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, event_id))
        self.conn.commit()
        filas_afectadas = cursor.rowcount  # 🔹 Verificamos cuántas filas fueron modificadas
        cursor.close()

        return filas_afectadas > 0  # 🔹 Retorna True si se modificó al menos una fila

    def eliminar_evento(self, event_id):
        """
        Elimina un evento de la base de datos.

        :param event_id: ID del evento a eliminar.
        :return: True si se eliminó correctamente, False si no.
        """
        cursor = self.conn.cursor()
        query = "DELETE FROM Eventos WHERE id_evento = %s"
        cursor.execute(query, (event_id,))
        filas_afectadas = cursor.rowcount  # 🔹 Verificamos cuántas filas fueron afectadas
        self.conn.commit()
        cursor.close()
        
        return filas_afectadas > 0  # 🔹 Retorna True si se eliminó el evento, False si no

    def get_all(self):
        """
        Obtiene todos los eventos de la base de datos y los devuelve como una lista de diccionarios.

        :return: Lista de eventos en formato diccionario.
        """
        cursor = self.conn.cursor(as_dict=True)  # 🔹 Configuramos el cursor para devolver los resultados como diccionarios
        cursor.execute("SELECT * FROM Eventos")
        eventos = [EventoDTO(**row).to_dict() for row in cursor]  # 🔹 Convertimos cada fila en un objeto EventoDTO
        cursor.close()
        return eventos

    def get_by_id(self, event_id):
        """
        Obtiene un evento por su ID.

        :param event_id: ID del evento a buscar.
        :return: Diccionario con los datos del evento o None si no se encuentra.
        """
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos WHERE id_evento = %s", (event_id,))
        row = cursor.fetchone()  # 🔹 Obtenemos el evento si existe
        cursor.close()
        return EventoDTO(**row).to_dict() if row else None  # 🔹 Retornamos el evento en formato diccionario

    def obtener_eventos(self):
        """
        Obtiene todos los eventos almacenados en SQL Server.

        :return: Lista de eventos en formato diccionario.
        """
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos")
        eventos = cursor.fetchall()  # 🔹 Obtenemos todos los eventos
        cursor.close()
        return eventos
