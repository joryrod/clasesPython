## importar tkinter
from tkinter import *

## instanciar la clase TK()
ventana=Tk()
ventana.geometry("500x600")

## CREAMOS LOS WIDGETS
widget_uno=Frame()
widget_uno.grid(row='0', column='0',columnspan =2)
widget_uno.config(width='100', height='100')
widget_uno.config(bg='')

widget_dos=Frame()
widget_dos.grid(row='0', column='2',columnspan =2)
widget_dos.config(width='100', height='100')
widget_dos.config(bg='')

## creacion de etiquetas
etiqueta=Label(ventana,text="HOLA SOY UNA ETIQUETA SEXY")
etiqueta.grid(row=1,column=2,columnspan=2)

## usar el metodo loop para que la ventana permanezca abierta
ventana.mainloop()
