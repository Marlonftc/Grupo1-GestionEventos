from src.factories.evento_social_factory import EventoSocialFactory
from src.factories.evento_academico_factory import EventoAcademicoFactory
from src.factories.evento_deportivo_factory import EventoDeportivoFactory

class EventoFactoryRouter:
    """
    Fábrica general que selecciona la sub-fábrica correcta según la categoría del evento.
    Implementa el patrón Factory Method para delegar la creación de eventos a las fábricas especializadas.
    """

    def __init__(self, categoria):
        """
        Constructor del enrutador de fábricas de eventos.

        :param categoria: Categoría del evento (ej. "social", "academico", "deportivo").
        """
        self.categoria = categoria

    def obtener_factory(self):
        """
        Retorna la fábrica correspondiente según la categoría del evento.

        :return: Instancia de la fábrica de eventos correspondiente.
        :raises ValueError: Si la categoría no es válida.
        """
        if self.categoria == "social":
            return EventoSocialFactory()  # 🔹 Retorna la fábrica de eventos sociales
        elif self.categoria == "academico":
            return EventoAcademicoFactory()  # 🔹 Retorna la fábrica de eventos académicos
        elif self.categoria == "deportivo":
            return EventoDeportivoFactory()  # 🔹 Retorna la fábrica de eventos deportivos
        else:
            raise ValueError(f"Categoría no soportada: {self.categoria}")
