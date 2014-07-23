from Contacto import Contacto
from Fichero import Fichero

persistencia = Fichero("C:\\Users\\Nej\\Desktop\\CursoPython\\Agenda.txt")

eleccion = -1
while(eleccion != 0):
    print("1 Agregar contacto")
    print("2 Listar contactos")
    print("3 Buscar contacto")
    print("0 Salir")
    eleccion = int(input("Operación a realizar: "))
    print('\n')
    if (eleccion == 1):
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        telefono = input("Telefono: ")
        contacto = Contacto(nombre, apellidos, telefono)
        persistencia.Guardar(contacto)
    elif (eleccion == 2):
        listado = persistencia.Listar()
        for c in listado:
            print(c)
    elif (eleccion == 3):
        nombre = input("Nombre: ")
        contacto = Contacto(nombre, "", "")
        listado = persistencia.Buscar(contacto)
        if (len(listado) == 0):
            print("Contacto no encontrado")
        else:
            for c in listado:
                print(c)
    print('\n')