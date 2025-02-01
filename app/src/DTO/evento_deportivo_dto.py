class EventoDeportivoDTO:
    """DTO para la categoría de eventos deportivos"""
    def __init__(self, nombre, fecha, ubicacion, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo  # Ej: "maratón", "torneo"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo
        }