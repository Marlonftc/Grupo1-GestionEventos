class EventoAcademicoDTO:
    """
    DTO (Data Transfer Object) para la categoría de eventos académicos.
    Este objeto almacena la información relevante de un evento académico y permite su conversión a diccionario.
    """

    def __init__(self, nombre, fecha, ubicacion, tipo, categoria):
        """
        Constructor de la clase EventoAcademicoDTO.

        :param nombre: Nombre del evento académico.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación donde se llevará a cabo el evento.
        :param tipo: Tipo específico de evento académico (ej. conferencia, seminario, taller).
        :param categoria: Categoría general del evento (ej. "académico").
        """
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.tipo = tipo
        self.categoria = categoria  # 🔹 Se espera que siempre sea "académico" o una subcategoría académica

    def to_dict(self):
        """
        Convierte el objeto a un diccionario para facilitar la serialización y el intercambio de datos.

        :return: Diccionario con los atributos del evento académico.
        """
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "ubicacion": self.ubicacion,
            "tipo": self.tipo,
            "categoria": self.categoria
        }
