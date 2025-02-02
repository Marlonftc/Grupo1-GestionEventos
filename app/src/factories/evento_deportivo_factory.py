from src.factories.evento_factory import EventoFactory
from src.DTO.evento_deportivo_dto import EventoDeportivoDTO

class EventoDeportivoFactory(EventoFactory):
    """
    Fábrica para la creación de eventos deportivos.
    Hereda de EventoFactory y genera instancias de EventoDeportivoDTO.
    """

    def crear_evento(self, tipo, nombre, fecha, ubicacion, categoria):
        """
        Crea un evento deportivo validando su tipo.

        :param tipo: Tipo de evento deportivo (ej. "maratón", "torneo").
        :param nombre: Nombre del evento.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el evento.
        :param categoria: Categoría general del evento (ej. "deportivo").
        :return: Instancia de EventoDeportivoDTO.
        :raises ValueError: Si el tipo de evento no está permitido.
        """
        tipos_permitidos = [
            "maratón", "torneo", "competencia atlética", "carrera ciclística",
            "partido de exhibición", "juegos intercolegiales", "campeonato nacional",
            "competencia de natación", "evento de crossfit"
        ]

        if tipo not in tipos_permitidos:
            raise ValueError(f"Tipo de evento deportivo no soportado: {tipo}")

        return EventoDeportivoDTO(nombre, fecha, ubicacion, tipo, categoria)

    def obtener_eventos(self):
        """
        Simulación de consulta a la base de datos para obtener eventos deportivos.

        :return: Lista de eventos deportivos en formato de diccionario.
        """
        return [
            {
                "id_evento": 5,
                "nombre": "Maratón de Quito",
                "fecha": "2025-09-10",
                "ubicacion": "Quito",
                "tipo": "maratón"
            },
            {
                "id_evento": 6,
                "nombre": "Torneo de Fútbol",
                "fecha": "2025-10-15",
                "ubicacion": "Guayaquil",
                "tipo": "torneo"
            }
        ]
