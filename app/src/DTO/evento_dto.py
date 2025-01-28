# app/src/dto/evento_dto.py
class EventoDTO:
    def __init__(self, id_evento, nombre, fecha, ubicacion):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion

    def to_dict(self):
        return {
            "id_evento": self.id_evento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
        }