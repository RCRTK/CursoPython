import sqlite3 as bd
from Contacto import Contacto

class Basededatos(object):


    def __init__(self, ruta):
        self.ruta= ruta
        self.bbdd = bd.connect(ruta)
        self.bdcursor = self.bbdd.cursor()
        try:
            self.bdcursor.execute("""select * from contacto""")
        except:
            self.bdcursor.execute("""create table contacto (nombre text, apellidos text, telefono text)""")

    def Cerrar(self):
            self.bdcursor.close()
            self.bbdd.close()

    def Guardar(self, contacto):

        try:
            self.bbdd = bd.connect(self.ruta)
            self.bdcursor = self.bbdd.cursor()
            self.bdcursor.execute("""INSERT INTO contacto values(?,?,?)""",(contacto.nombre,contacto.apellido, contacto.telefono,))
            self.bbdd.commit()
        except:
            print("error guardar")


    def Buscar(self, parametro):

        try:
            #self.bbdd = bd.connect(self.ruta)
            #self.bdcursor = self.bbdd.cursor()
            self.bdcursor.execute("""SELECT * FROM contacto where nombre = ? OR 
            apellidos = ? OR telefono = ? """,(parametro.nombre,parametro.apellido
            , parametro.telefono))
            
            return self.bdcursor.fetchall()
        except:
            print("error")

    def Listar(self):

        try:
            self.bdcursor.execute("""SELECT * FROM contacto """)
            return self.bdcursor.fetchall()
        except:
            print("error")

