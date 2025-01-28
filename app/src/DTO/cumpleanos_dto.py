from .evento_dto import EventoDTO

class CumpleanosDTO(EventoDTO):
    def __init__(self, id_evento, nombre, fecha, ubicacion, edad):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self.edad = edad

    def to_dict(self):
        data = super().to_dict()
        data["edad"] = self.edad
        return data
