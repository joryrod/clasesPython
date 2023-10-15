from tkinter import *

ventana=Tk()

widget_uno=Frame()
widget_uno.grid(row='0', column='0')
widget_uno.config(width='100', height='100')
widget_uno.config(bg='red')

widget_dos=Frame()
widget_dos.grid(row='0', column='1')
widget_dos.config(width='100', height='100')
widget_dos.config(bg='pink')

widget_tres=Frame()
widget_tres.grid(row='2', column='0')
widget_tres.config(width='200', height='50')
widget_tres.config(bg='orange')






ventana.mainloop()
