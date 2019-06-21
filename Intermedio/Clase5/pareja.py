from tkinter import *
ventana = Tk()
ventana.title("Cuestionario de la pareja ideal:")
ventana.geometry("500x500")


def eleccion():
	if opcion.get()==1:
		mensaje.set("Apto para un sugar.")

	elif opcion.get()==2:
		mensaje.set("Tienes buenos gustos.")

	elif opcion.get()==3:
		mensaje.set("SOOO SWEET")

	elif opcion.get()==4:
		#set muestra mensajes en pantalla
		mensaje.set("Siempre pensando en el futuro.")


#Recuperar la opción seleccionada por el usuario:
opcion = IntVar()
#Mensaje mostrado en pantalla:
mensaje = StringVar()
#Decorando pantalla:
etiqueta1 = Label(ventana, text="¿Qué ves en él/ella?").place(x=20,y=40)
etiqueta2 = Label(ventana, textvariable=mensaje).place(x=20,y=210)

op1 = Radiobutton(ventana, text="Tiene dinero.", value=1, variable=opcion).place(x=20,y=60)
op1 = Radiobutton(ventana, text="Es cientific@.", value=2, variable=opcion).place(x=20,y=80)
op1 = Radiobutton(ventana, text="Tiene bonitos sentimientos.", value=3, variable=opcion).place(x=20,y=100)
op1 = Radiobutton(ventana, text="Tiene buen apellido.", value=4, variable=opcion).place(x=20,y=120)

boton = Button(ventana, text="Intentar", command =eleccion).place(x=20,y=190)


ventana.mainloop()