class EventoSocialDTO:
    """
    DTO (Data Transfer Object) para la categoría de eventos sociales.
    Este objeto encapsula la información relevante de un evento social y permite su conversión a diccionario.
    """

    def __init__(self, nombre, fecha, ubicacion, tipo, categoria):
        """
        Constructor de la clase EventoSocialDTO.

        :param nombre: Nombre del evento social.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el evento.
        :param tipo: Tipo de evento social (ej. "cumpleaños", "boda", "reunión").
        :param categoria: Categoría general del evento (ej. "social").
        """
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.categoria = categoria  # 🔹 Se espera que sea "social" o una subcategoría específica

    def to_dict(self):
        """
        Convierte el objeto a un diccionario para facilitar la serialización y el intercambio de datos.

        :return: Diccionario con los atributos del evento social.
        """
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo,
            "categoria": self.categoria
        }
