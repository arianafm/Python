:#I N T E R F A Z  G R Á F I C A

from tkinter import *

ventana = Tk()

def quitar():
	ventana.destroy()

#Ancho x alto.
ventana.geometry("600x600")
boton = Button(ventana, text="H O L A", bg= "#B7DFEF", fg="#449CEF")
boton.place(x=250, y=250, width=180, height=65)

boton2 = Button(ventana, text="S A L I R", command=quitar)
boton2.place(x=20, y=70, width = 180, height = 25)

ventana.mainloop()