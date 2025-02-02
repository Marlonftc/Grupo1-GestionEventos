class EventoDTO:
    """
    DTO (Data Transfer Object) para representar un evento genérico.
    Esta clase base encapsula la información común a todos los eventos y permite la conversión a diccionario.
    """

    def __init__(self, id_evento, nombre, fecha, ubicacion, tipo):
        """
        Constructor de la clase EventoDTO.

        :param id_evento: Identificador único del evento.
        :param nombre: Nombre del evento.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el evento.
        :param tipo: Tipo de evento (ej. "boda", "conferencia", "deportivo", etc.).
        """
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo  # 🔹 Define el tipo de evento (puede ser usado por subclases)

    def to_dict(self):
        """
        Convierte el objeto a un diccionario para facilitar la serialización y el intercambio de datos.

        :return: Diccionario con los atributos del evento.
        """
        return {
            "id_evento": self.id_evento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo
        }
