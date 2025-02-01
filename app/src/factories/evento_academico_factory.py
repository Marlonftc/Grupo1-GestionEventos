from src.factories.evento_factory import EventoFactory
from src.DTO.evento_academico_dto import EventoAcademicoDTO

class EventoAcademicoFactory(EventoFactory):
    """Fábrica para eventos académicos"""

    def crear_evento(self, tipo, nombre, fecha, ubicacion, categoria):
        if tipo not in ["conferencia", "seminario", "taller", "simposio", "coloquio",
    "mesa redonda", "defensa de tesis", "congreso", "charla magistral",]:
            raise ValueError("Tipo de evento académico no soportado")
        
        return EventoAcademicoDTO(nombre, fecha, ubicacion, tipo, categoria)

    def obtener_eventos(self):
        """Conectar con SQL o MongoDB para obtener los eventos académicos"""
        return [
            {"id_evento": 1, "nombre": "Conferencia de IA", "fecha": "2025-03-15", "ubicacion": "Quito", "tipo": "conferencia"},
            {"id_evento": 2, "nombre": "Seminario de Blockchain", "fecha": "2025-04-10", "ubicacion": "Guayaquil", "tipo": "seminario"}
        ]
