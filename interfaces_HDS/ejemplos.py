from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter as tk
import os

#CREACIÓN DE LA VENTANA:
canvas = tk.Tk()
canvas.geometry("550x660")
canvas.title("NOTA♥☺")
canvas.config(bg = "pink")
ventana= tk.Tk()

def saludar():
    etiqueta.config(text="¡Hola, Maria♥!")
    etiqueta.config(bg = "pink")

boton = tk.Button(ventana, text="Saludo", command=saludar)
boton.pack()


etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()