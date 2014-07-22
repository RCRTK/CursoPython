from Contacto import Contacto

class Fichero(object):

    def __init__(self, ruta):

        self.ruta = ruta


    def Guardar(self, contacto):

        cadena_contacto = contacto.nombre + "," + contacto.apellido + "," + contacto.telefono


        try:
            archivo = open(self.ruta,"a")


        except IOError:

            archivo = open(self.ruta, "w")

        finally:

            archivo.write(cadena_contacto)
            archivo.close



    def Listar(self):

        listado = []

        try:

            archivo = open(self.ruta,"r")
            while True:
                linea=archivo.readline()
                if not linea:
                    break
                else:
                    datos=linea.split(",")
                    listado.append(Contacto(datos[0],datos[1],datos[2]))

        except IOError:

            archivo = open(self.ruta, "w")


        finally:

            archivo.close
            return listado

    def buscar(self, argumento_busqueda):

            listado=[]

            archivo = open(self.ruta,"w")

            while True:
                linea = archivo.readline()
                if not linea:
                    break
                else:
                    datos = linea.slipt(",")
                    for i in linea:
                        if i.lower() == argumento_busqueda.lower():
                            listado.append(Contacto(datos[0],datos[1],datos[2]))
                            break

            return listado













