from abc import ABC, abstractmethod

class EventoFactory(ABC):
    @abstractmethod
    def crear_evento(self, id_evento, nombre, fecha, ubicacion):
        pass

    @abstractmethod
    def obtener_eventos(self):
        pass

