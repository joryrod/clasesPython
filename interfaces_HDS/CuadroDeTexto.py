## importar tkinter
from tkinter import *

## instanciar la clase TK()
ventana=Tk()
ventana.geometry("500x600")

## CREAMOS LOS WIDGETS
widget_uno=Frame()
widget_uno.grid(row='0', column='0')
widget_uno.config(width='500', height='600')
widget_uno.config(bg='')

## creacion de etiquetas
etiqueta=Label(ventana,text="ingrese su nombre")
etiqueta.grid(row=0,column=0)

## creacion de cuadro de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=0,column=0)


ventana.mainloop()