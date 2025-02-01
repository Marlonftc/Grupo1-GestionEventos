from src.factories.evento_factory import EventoFactory
from src.DTO.evento_deportivo_dto import EventoDeportivoDTO

class EventoDeportivoFactory(EventoFactory):
    """Fábrica para eventos deportivos"""

    def crear_evento(self, tipo, nombre, fecha, ubicacion, categoria):
        if tipo not in ["maratón", "torneo", "competencia atlética", "carrera ciclística",
    "partido de exhibición", "juegos intercolegiales", "campeonato nacional",
    "competencia de natación", "evento de crossfit"]:
            raise ValueError("Tipo de evento deportivo no soportado")
        
        return EventoDeportivoDTO(nombre, fecha, ubicacion, tipo, categoria)

    def obtener_eventos(self):
        """Conectar con SQL o MongoDB para obtener los eventos deportivos"""
        return [
            {"id_evento": 5, "nombre": "Maratón de Quito", "fecha": "2025-09-10", "ubicacion": "Quito", "tipo": "maratón"},
            {"id_evento": 6, "nombre": "Torneo de Fútbol", "fecha": "2025-10-15", "ubicacion": "Guayaquil", "tipo": "torneo"}
        ]
