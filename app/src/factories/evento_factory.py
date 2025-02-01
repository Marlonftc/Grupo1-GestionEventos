from abc import ABC, abstractmethod

class EventoFactory(ABC):
    """Clase Abstracta para la creación de eventos"""
    
    @abstractmethod
    def crear_evento(self, tipo, nombre, fecha, ubicacion):
        """Método abstracto que debe ser implementado por las fábricas concretas"""
        pass

    @abstractmethod
    def obtener_eventos(self):
        """Método abstracto para obtener eventos de la base de datos"""
        pass
