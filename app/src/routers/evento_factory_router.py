from src.factories.evento_social_factory import EventoSocialFactory
from src.factories.evento_academico_factory import EventoAcademicoFactory
from src.factories.evento_deportivo_factory import EventoDeportivoFactory

class EventoFactoryRouter:
    """Fábrica general que selecciona la sub-fábrica correcta"""

    def __init__(self, categoria):
        self.categoria = categoria

    def obtener_factory(self):
        if self.categoria == "social":
            return EventoSocialFactory()
        elif self.categoria == "academico":
            return EventoAcademicoFactory()
        elif self.categoria == "deportivo":
            return EventoDeportivoFactory()
        else:
            raise ValueError("Categoría no soportada")
