class EventoAcademicoDTO:
    """DTO para la categoría de eventos académicos"""
    def __init__(self, nombre, fecha, ubicacion, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo  # Ej: "conferencia", "seminario"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo
        }
