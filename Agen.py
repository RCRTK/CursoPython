from tkinter import *
from Contacto import Contacto
from Fichero import Fichero
from Basededatos import Basededatos

persistencia = Basededatos("Agenda.dat")

def agregar():

    nombre = entrada_nombre.get()
    apellidos = entrada_apellido.get()
    telefono = entrada_telefono.get()
    contacto = Contacto(nombre, apellidos, telefono)
    persistencia.Guardar(contacto)

def listar():

    resultado.delete("1.0", END)
    listado = persistencia.Listar()
    for resul in listado:
        resultado.insert(INSERT, str(resul)+ "\n")

def cerrar():
    
    persistencia.Cerrar()
    ventana.quit()

def buscar():
    
    resultado.delete("1.0", END)
    nombre = entrada_nombre.get()
    apellidos = entrada_apellido.get()
    telefono = entrada_telefono.get()
    contacto = Contacto(nombre, apellidos, telefono)
    listado =  persistencia.Buscar(contacto)
    for resul in listado:
        resultado.insert(INSERT, str(resul)+ "\n")
    
    

ventana = Tk()
ventana.geometry('500x500')

entrada_nombre=StringVar()
entrada_apellido=StringVar()
entrada_telefono=StringVar()
r=StringVar()

label_nombre=Label(ventana, text='Nombre:', font='Helvetica -12 bold').grid(row=1,column=1)
text_nombre=Entry(ventana, textvar=entrada_nombre).grid(row=1, column=10)

label_apellidos=Label(ventana, text='Apellidos:', font='Helvetica -12 bold').grid(row=3, column=1)
text_apellido=Entry(ventana,textvar=entrada_apellido).grid(row=3, column=10)

label_telefono=Label(ventana, text='Telefono:', font='Helvetica -12 bold').grid(row=6, column=1)
text_telefono = Entry(ventana,textvar=entrada_telefono).grid(row=6, column = 10)

boton_salir = Button(ventana, text='Salir', command=cerrar, activeforeground='white',
              activebackground='red').grid(row=9, column = 1)
boton_agregar = Button(ventana, text='agregar', command=agregar, activeforeground='white',
              activebackground='red').grid(row=9, column = 2)

boton_buscar = Button(ventana, text='buscar', command=buscar, activeforeground='white',
              activebackground='red').grid(row=9, column = 3)


boton_listar = Button(ventana, text='listar_todos', command=listar, activeforeground='white',
              activebackground='red').grid(row=9, column = 4, columnspan=10)
              
resultado = Text(ventana)
resultado.grid(row=60, column = 1, columnspan=50)











mainloop()



