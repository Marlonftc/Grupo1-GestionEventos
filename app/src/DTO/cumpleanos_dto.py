# Importamos la clase base EventoDTO para heredar sus atributos y métodos
from .evento_dto import EventoDTO

class CumpleanosDTO(EventoDTO):
    """
    Clase que representa un evento de tipo 'Cumpleaños'.
    Hereda de EventoDTO e inicializa la categoría como 'cumpleaños'.
    """

    def __init__(self, id_evento, nombre, fecha, ubicacion):
        """
        Constructor de la clase CumpleanosDTO.

        :param id_evento: Identificador único del evento.
        :param nombre: Nombre del cumpleañero/a o del evento.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el cumpleaños.
        """
        # Llamamos al constructor de la clase base (EventoDTO) y establecemos la categoría como 'cumpleaños'
        super().__init__(id_evento, nombre, fecha, ubicacion, "cumpleaños")
