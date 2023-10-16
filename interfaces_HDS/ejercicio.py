from tkinter import *

ventana=Tk()

widget_uno=Frame()
widget_uno.grid(row='0', column='0',columnspan =2)
widget_uno.config(width='100', height='100')
widget_uno.config(bg='red')

widget_dos=Frame()
widget_dos.grid(row='0', column='2',columnspan =2)
widget_dos.config(width='100', height='100')
widget_dos.config(bg='pink')

widget_tres=Frame()
widget_tres.grid(row='2', column='0',columnspan =4)
widget_tres.config(width='200', height='50')
widget_tres.config(bg='orange')

widget_tres=Frame()
widget_tres.grid(row='3', column='0',columnspan =4)
widget_tres.config(width='200', height='50')
widget_tres.config(bg='blue')


widget_uno=Frame()
widget_uno.grid(row='4', column='0')
widget_uno.config(width='50', height='100')
widget_uno.config(bg='yellow')

widget_dos=Frame()
widget_dos.grid(row='4', column='1')
widget_dos.config(width='50', height='100')
widget_dos.config(bg='blue')


widget_uno=Frame()
widget_uno.grid(row='4', column='2')
widget_uno.config(width='50', height='100')
widget_uno.config(bg='black')

widget_dos=Frame()
widget_dos.grid(row='4', column='3')
widget_dos.config(width='50', height='100')
widget_dos.config(bg='red')

ventana.mainloop()
