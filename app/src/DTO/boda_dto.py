from .evento_dto import EventoDTO

class BodaDTO(EventoDTO):
    def __init__(self, id_evento, nombre, fecha, ubicacion, pareja):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self.pareja = pareja

    def to_dict(self):
        data = super().to_dict()
        data["pareja"] = self.pareja
        return data
