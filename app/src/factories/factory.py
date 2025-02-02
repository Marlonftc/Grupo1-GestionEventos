from abc import ABC, abstractmethod

class EventoFactory(ABC):
    """
    Clase Abstracta para la creación de eventos.
    Define la estructura base para las fábricas de eventos, asegurando que todas las fábricas concretas implementen
    los métodos necesarios.
    """

    @abstractmethod
    def crear_evento(self, id_evento, nombre, fecha, ubicacion):
        """
        Método abstracto para crear un evento.
        Debe ser implementado por las fábricas concretas.

        :param id_evento: Identificador único del evento.
        :param nombre: Nombre del evento.
        :param fecha: Fecha del evento en formato datetime o string compatible.
        :param ubicacion: Ubicación del evento.
        :return: Instancia del evento correspondiente.
        """
        pass

    @abstractmethod
    def obtener_eventos(self):
        """
        Método abstracto para obtener eventos de la base de datos.
        Debe ser implementado por las fábricas concretas para recuperar eventos desde SQL Server o MongoDB.

        :return: Lista de eventos en formato de diccionario o instancias de DTOs.
        """
        pass
