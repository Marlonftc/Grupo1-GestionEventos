class EventoSocialDTO:
    """DTO para la categoría de eventos sociales"""
    def __init__(self, nombre, fecha, ubicacion, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo  # Ej: "boda", "cumpleaños"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo
        }
