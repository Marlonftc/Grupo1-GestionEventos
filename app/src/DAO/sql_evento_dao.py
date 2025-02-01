from ..DTO.evento_dto import EventoDTO

class SQLEventoDAO:
    def __init__(self, connection):
        self.conn = connection

    def insertar_evento(self, evento):
        cursor = self.conn.cursor()
        query = """
        INSERT INTO Eventos (tipo, nombre, fecha, ubicacion, categoria) 
        OUTPUT INSERTED.id_evento VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, evento.categoria))
        evento_id = cursor.fetchone()["id_evento"]
        self.conn.commit()
        cursor.close()
        return evento_id

    def editar_evento(self, event_id, evento):
        """
        Actualiza un evento en SQL Server.
        """
        cursor = self.conn.cursor()
        query = """
            UPDATE Eventos
            SET categoria = %s, tipo = %s, nombre = %s, fecha = %s, ubicacion = %s
            WHERE id_evento = %s
        """
        cursor.execute(query, (evento.categoria, evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, event_id))
        self.conn.commit()
        cursor.close()

        return cursor.rowcount > 0  # Devuelve True si se actualizó correctamente


    def eliminar_evento(self, event_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM Eventos WHERE id_evento = %s"
        cursor.execute(query, (event_id,))
        filas_afectadas = cursor.rowcount  # 🔹 Verifica cuántas filas fueron afectadas
        self.conn.commit()
        cursor.close()
        
        return filas_afectadas > 0  # 🔹 Retorna True si se eliminó algún evento, False si no


    def get_all(self):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos")
        eventos = [EventoDTO(**row).to_dict() for row in cursor]
        cursor.close()
        return eventos

    def get_by_id(self, event_id):
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos WHERE id_evento = %s", (event_id,))
        row = cursor.fetchone()
        cursor.close()
        return EventoDTO(**row).to_dict() if row else None

    def obtener_eventos(self):
        """Obtiene todos los eventos almacenados en SQL Server"""
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Eventos")
        eventos = cursor.fetchall()
        cursor.close()
        return eventos
