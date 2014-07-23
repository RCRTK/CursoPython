class Contacto(object):

    def __init__(self, nombre, apellido, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    def Get_nombre(self):
        return self.__nombre

    def Set_nombre(self, nombre):
        self.__nombre = nombre

    def Get_apellido(self):
        return self.__apellido

    def Set_apellido(self, apellido):
        self.__apellido = apellido

    def Get_telefono(self):
        return self.__telefono

    def Set_telefono(self, telefono):
        self.__telefono = telefono

    nombre = property(Get_nombre, Set_nombre)
    apellido = property(Get_apellido, Set_apellido)
    telefono = property(Get_telefono, Set_telefono)

    def __str__(self):
        return("Nombre: %s Apellidos: %s Telefono: %s" % (self.nombre,
        self.apellido, self.telefono))

