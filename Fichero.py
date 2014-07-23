from Contacto import Contacto
from Persistence import Persistence


class Fichero(Persistence):

    def __init__(self, ruta):

        self.ruta = ruta

    def Guardar(self, contacto):

        cadena_contacto = contacto.nombre + "," + contacto.apellido + "," + contacto.telefono

        try:
            archivo = open(self.ruta, "a")

        except IOError:

            archivo = open(self.ruta, "w")

        finally:

            archivo.write(cadena_contacto + '\n')
            archivo.close()

    def Listar(self):

        listado = []

        try:

            archivo = open(self.ruta, "r")
            while True:
                linea = archivo.readline()
                if not linea:
                    break
                else:
                    datos = linea.split(",")
                    listado.append(Contacto(datos[0], datos[1], datos[2]))
            archivo.close()

        except IOError:
            print("Error abriendo el archivo")
            #archivo = open(self.ruta, "w")

        finally:

            return listado

    def Buscar(self, argumento_busqueda):

        listado = []

        try:

            archivo = open(self.ruta, "r")

            while True:
                linea = archivo.readline()
                if not linea:
                    break
                else:
                    datos = linea.split(",")
                    for i in datos:
                        if i.lower() == argumento_busqueda.nombre.lower():
                            listado.append(Contacto(datos[0], datos[1], datos[2]))
                            break
            archivo.close()

        except IOError:
            print("Error abriendo el archivo")
            #archivo = open(self.ruta, "w")

        finally:
            return listado











