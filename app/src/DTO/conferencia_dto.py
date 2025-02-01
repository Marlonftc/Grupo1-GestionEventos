from .evento_dto import EventoDTO

class ConferenciaDTO(EventoDTO):
    def __init__(self, id_evento, nombre, fecha, ubicacion):
        super().__init__(id_evento, nombre, fecha, ubicacion, "conferencia")

