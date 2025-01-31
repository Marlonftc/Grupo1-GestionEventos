from abc import ABC, abstractmethod

class EventoDAO(ABC):
    """Interfaz DAO para manejar eventos en diferentes bases de datos"""

    @abstractmethod
    def get_all(self):
        """Obtiene todos los eventos"""
        pass

    @abstractmethod
    def get_by_id(self, event_id):
        """Obtiene un evento por ID"""
        pass

    @abstractmethod
    def insert(self, evento):
        """Inserta un nuevo evento"""
        pass

    @abstractmethod
    def update(self, event_id, evento):
        """Actualiza un evento existente"""
        pass

    @abstractmethod
    def delete(self, event_id):
        """Elimina un evento"""
        pass

