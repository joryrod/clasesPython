from tkinter import *

ventana=Tk()
ventana.geometry("400x500")

widget_uno=Frame()
widget_uno.grid(row=0, column=0,columnspan=2)
widget_uno.config(width='400', height='50')
widget_uno.config(bg='')

etiqueta1=Label(ventana,text="nombres y apellidos")
etiqueta1.grid(row=1,column=0)
espacioEtq1=Frame()
espacioEtq1.grid(row=2,column=0,columnspan=2)
espacioEtq1.config(width='400', height='10')

etiqueta2=Label(ventana,text="DNI")
etiqueta2.grid(row=3,column=0)
espacioEtq2=Frame()
espacioEtq2.grid(row=4,column=0,columnspan=2)
espacioEtq2.config(width='400', height='10')

etiqueta3=Label(ventana,text="celular")
etiqueta3.grid(row=5,column=0)
espacioEtq3=Frame()
espacioEtq3.grid(row=6,column=0,columnspan=2)
espacioEtq3.config(width='400', height='10')

cuadro_texto1=Entry()
cuadro_texto1.grid(row=1,column=1)

cuadro_texto2=Entry()
cuadro_texto2.grid(row=3,column=1)

cuadro_texto3=Entry()
cuadro_texto3.grid(row=5,column=1)

widget_dos=Frame()
widget_dos.grid(row=7, column=0,columnspan=2)
widget_dos.config(width='400', height='300')
widget_dos.config(bg='red')

ventana.mainloop()