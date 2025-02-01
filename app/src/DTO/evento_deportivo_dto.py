class EventoDeportivoDTO:
    """DTO para la categoría de eventos deportivos"""
    def __init__(self, nombre, fecha, ubicacion, tipo, categoria):
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.categoria = categoria

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo,
            "categoria": self.categoria
        }