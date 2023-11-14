from tkinter import *

def enviar_boton(ventana,valor):
    if valor == "=":
        print("soy igual")
    elif valor == "C":
        ventana.operacion_label.config(text="")
        ventana.caja_operaciones.delete(0,END)
    elif valor == "<":
        print("te borro el chiquito")
    else:
        print(f"soy el valor {valor}")