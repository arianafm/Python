import tkinter as tk

ventana = tk.Tk()

ventana.title("Botones:")

ventana.geometry("1000x600")

boton1 = tk.Button(ventana, text = "Botón 1", activebackground = "black", font=("Avenir",30)).grid(row=0, column=0)
boton2 = tk.Button(ventana, text = "Botón 2", activebackground = "black", font=("Avenir",30)).grid(row=0, column=1)
boton3 = tk.Button(ventana, text = "Botón 3", activebackground = "black", font=("Avenir",30)).grid(row=0, column=2)
boton4 = tk.Button(ventana, text = "Botón 4",font=("Avenir",30)).grid(row=1, column=0)
boton5 = tk.Button(ventana, text = "Botón 5",font=("Avenir",30)).grid(row=1, column=1)
boton6 = tk.Button(ventana, text = "Botón 6",font=("Avenir",30)).grid(row=1, column=2)

ventana.mainloop()
