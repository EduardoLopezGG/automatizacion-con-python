import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui import interface 

windows = interface.tk.Tk()
windows.title("Automatizador de Tareas con Python")
windows.geometry("400x300")

etiqueta = interface.tk.Label(windows, text="hola mundo, primera linea de mi interfaz grafica")
etiqueta.pack()

def saludar():
    etiqueta.config(text="hola desde tkinter")

boton = interface.tk.Button(windows, text="saludar", command=saludar)
boton.pack()

windows.mainloop()