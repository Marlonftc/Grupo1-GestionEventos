class EventoDTO:
    def __init__(self, id_evento, nombre, fecha, ubicacion, tipo):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo  # 🔹 Agregar tipo de evento

    def to_dict(self):
        return {
            "id_evento": self.id_evento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo
        }

