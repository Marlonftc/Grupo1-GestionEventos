# Importamos la clase base EventoDTO para heredar sus atributos y métodos
from .evento_dto import EventoDTO

class BodaDTO(EventoDTO):
    """
    Clase que representa un evento de tipo 'Boda'.
    Hereda de EventoDTO e inicializa la categoría como 'boda'.
    """

    def __init__(self, id_evento, nombre, fecha, ubicacion):
        """
        Constructor de la clase BodaDTO.

        :param id_evento: Identificador único del evento.
        :param nombre: Nombre del evento (nombre de la boda).
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo la boda.
        """
        # Llamamos al constructor de la clase base (EventoDTO) con la categoría 'boda'
        super().__init__(id_evento, nombre, fecha, ubicacion, "boda")
