from .evento_dto import EventoDTO

class ConferenciaDTO(EventoDTO):
    def __init__(self, id_evento, nombre, fecha, ubicacion, conferencista):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self.conferencista = conferencista

    def to_dict(self):
        data = super().to_dict()
        data["conferencista"] = self.conferencista
        return data
