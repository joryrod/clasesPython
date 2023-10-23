from tkinter import*
ventana=Tk()
ventana.geometry("250x300")
ventana.title("ventana")

def comprobar_datos():
    text1=text_usuario.get()
    text2=int(text_contra.get())
    if text1 == usuario and text2==contra:
        mensaje=Label(ventana,text="Bienvenido :)")      
        mensaje.pack()
    else:
        mensaje=Label(ventana,text="introduce tu nombre")      
        mensaje.pack()

usuario="jory"
contra=47686117

etiqueta1=Label(ventana,text="Introdusca su nombre de usuario")
etiqueta1.pack()

text_usuario=Entry(ventana)
text_usuario.config(bg="red",fg="white")
text_usuario.pack()

etiqueta2=Label(ventana,text="Ingrese su contraseña")
etiqueta2.pack()

text_contra=Entry(ventana)
text_contra.config(bg="red",fg="white")
text_contra.pack()
boton_capturar=Button(ventana,text="Comprovar",command=comprobar_datos)
boton_capturar.pack()

ventana.mainloop()