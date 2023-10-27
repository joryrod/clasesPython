# primero importar libreria
from tkinter import *

# instanciamos nuestra clase tk()
ventana=Tk() # clase para crear una ventana
ventana.title("clase radiobutton") # haciendo uso del metodo title para el titulo de mi ventana
ventana.geometry("400x300") # haciendo uso del metodo geometry para asignarle un tamaño de ventana

# instanciamos mi clase label
etiqueta=Label(ventana,text="radio buttons") # clase para crear una etiqueta

#indicar la parte de mi ventana que deseo que se muestre
# puedeo usar los metodos grid o pack
etiqueta.config(fg="#EB6828",font=50)
etiqueta.pack()

info=IntVar()

def mostrar_radio():
    # respuesta="eres masculino" if info.get()==1 else "eres femenino"
    # etiquetaRespeusta=Label(ventana,text=respuesta)
    # etiquetaRespeusta.pack
    if info.get()==1:
        etiquetaRespuesta=Label(ventana,text="eres masculino")
        etiquetaRespuesta.pack()
    else:
        etiquetaRespuesta=Label(ventana,text=("eres femenino"))
        etiquetaRespuesta.pack()

# instanciar la clase radiobutton
radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radioFemenino.pack()


#instanciamos la clase button
boton=Button(ventana,text="enviar",command=mostrar_radio)
boton.pack()

# llamar al metodo de Tk que me permite tener persistencia al mostrar la ventana
ventana.mainloop()