from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        """Método para extrair dados, deve ser implementado pelas subclasses"""
        pass
