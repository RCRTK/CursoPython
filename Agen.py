from tkinter import *
from Contacto import Contacto
from Fichero import Fichero
from Basededatos import Basededatos

ventana = Tk()
ventana.geometry('500x500')

entrada_nombre=StringVar()
entrada_apellido=StringVar()
entrada_telefono=StringVar()

label_nombre=Label(ventana, text='Nombre:', font='Helvetica -12 bold').pack(fill=Y, expand=1)


text_nombre=Entry(ventana,textvar=entrada_nombre).pack()

label_apellidos=Label(ventana, text='Apellidos:', font='Helvetica -12 bold').pack(fill=Y, expand=1)


text_apellido=Entry(ventana,textvar=entrada_apellido).pack()

label_telefono=Label(ventana, text='Telefono:', font='Helvetica -12 bold').pack(fill=Y, expand=1)


text_telefono = Entry(ventana,textvar=entrada_telefono).pack()

boton_salir = Button(ventana, text='Salir', command=ventana.quit, activeforeground='white',
              activebackground='red')

boton_agregar = Button(ventana, text='agregar', command=ventana.quit, activeforeground='white',
              activebackground='red')



mainloop()



