from src.factories.evento_factory import EventoFactory
from src.DTO.evento_academico_dto import EventoAcademicoDTO

class EventoAcademicoFactory(EventoFactory):
    """
    Fábrica para la creación de eventos académicos.
    Hereda de EventoFactory y genera instancias de EventoAcademicoDTO.
    """

    def crear_evento(self, tipo, nombre, fecha, ubicacion, categoria):
        """
        Crea un evento académico validando su tipo.

        :param tipo: Tipo de evento académico (ej. "conferencia", "seminario").
        :param nombre: Nombre del evento.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el evento.
        :param categoria: Categoría general del evento (ej. "académico").
        :return: Instancia de EventoAcademicoDTO.
        :raises ValueError: Si el tipo de evento no está permitido.
        """
        tipos_permitidos = [
            "conferencia", "seminario", "taller", "simposio", "coloquio",
            "mesa redonda", "defensa de tesis", "congreso", "charla magistral"
        ]

        if tipo not in tipos_permitidos:
            raise ValueError(f"Tipo de evento académico no soportado: {tipo}")

        return EventoAcademicoDTO(nombre, fecha, ubicacion, tipo, categoria)

    def obtener_eventos(self):
        """
        Simulación de consulta a la base de datos para obtener eventos académicos.

        :return: Lista de eventos académicos en formato de diccionario.
        """
        return [
            {
                "id_evento": 1,
                "nombre": "Conferencia de IA",
                "fecha": "2025-03-15",
                "ubicacion": "Quito",
                "tipo": "conferencia"
            },
            {
                "id_evento": 2,
                "nombre": "Seminario de Blockchain",
                "fecha": "2025-04-10",
                "ubicacion": "Guayaquil",
                "tipo": "seminario"
            }
        ]
