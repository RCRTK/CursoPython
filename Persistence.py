from abc import *


class Persistence(metaclass = ABCMeta):

    @abstractmethod
    def Guardar(self, contacto):
        pass

    @abstractmethod
    def Listar(self):
        pass

    @abstractmethod
    def Buscar(self, argumento_busqueda):
        pass