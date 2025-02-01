from src.factories.evento_factory import EventoFactory
from src.DTO.evento_social_dto import EventoSocialDTO

class EventoSocialFactory(EventoFactory):
    """Fábrica para eventos sociales"""

    def crear_evento(self, tipo, nombre, fecha, ubicacion):
        if tipo not in ["boda", "cumpleaños", "graduación", "aniversario", "baby shower",
    "despedida de soltero", "fiesta de quinceañera", "reunión familiar",]:
            raise ValueError("Tipo de evento social no soportado")

        return EventoSocialDTO(nombre, fecha, ubicacion, tipo)

    def obtener_eventos(self):
        """Conectar con SQL o MongoDB para obtener los eventos sociales"""
        return [
            {"id_evento": 3, "nombre": "Boda de Ana", "fecha": "2025-06-20", "ubicacion": "Cuenca", "tipo": "boda"},
            {"id_evento": 4, "nombre": "Cumpleaños de Pedro", "fecha": "2025-07-10", "ubicacion": "Loja", "tipo": "cumpleaños"}
        ]
