# importar la libreria
from tkinter import *
#instanciamos una clase tk()
# creo una clase para crear una ventana
ventana=Tk()
ventana.title('clase radiobutton') # haciendo uso del metodo title para el titulo de mi ventana 
# haciendo uso del metodo geometry para asignarle un tamaño determinado a la ventana
ventana.geometry('400x400')

# insntanciar mi clase label, es decir almacenarlo dentro de una variable
# las clases siempre van la primera letra en mayuscula
# recibe dos parametros, mi clase  variable y un texto que queremos mostrar
# todas las clases usan un metodo o mas dependioendo su funcion
etiqueta=Label(ventana,text='clase radiobutton')# clase para crear una etiqueta

# adobe color para obtener mas colores y su codigo
# fg=letra, height=espacio, font=tamaño de letra, 
etiqueta.config(fg='#EB6828',font=50,) 

#existen dos metodos para mostrar pack o grid
# indicamos que parte de la ventana queremos mostrar 
# para modificar la parte visual usamos config parara darle color fondo, color letra, tamaño, etc
etiqueta.pack()

info=IntVar()

def mostrar_radio():
    # inn=info.get()
    # if inn == 1:
    #     mensaje1=Label(ventana,text=f'''Seleccionaste la opcion Masculino''') 
    #     mensaje1.pack()
    # if inn == 0:
    #     mensaje2=Label(ventana,text=f'''Seleccionaste la opcion Femenino''') 
    #     mensaje2.pack()
    # otra forma
    respuesta = 'eres masculino' if info.get()==1 else'eres femenino'
    etiqueta_resp=Label(ventana,text=respuesta)
    etiqueta_resp.pack()


#instanciar la clase RadioButton
## parametros, la variable de mi clase, un texto y un valor y variable
radiom=Radiobutton(ventana,text='masculino',value=1,variable=info)
radiom.pack()
# asocio los dos valores con una varible, si uno se ucmple o no, ese valor de almacena en la variable, sea 1 o 0, o los dos
radiof=Radiobutton(ventana,text='femenino',value=0,variable=info)
radiof.pack()

# instanciar la clase button
boton=Button(ventana,text='enviar',command=mostrar_radio)
boton.pack()


## llamar al metodo de Tk que me permite tener persistencia al mostrar la ventana
ventana.mainloop()