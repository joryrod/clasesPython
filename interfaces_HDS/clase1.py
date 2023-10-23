from tkinter import *
ventana= Tk()
# crear una ventaana a la medida que deseas 
ventana.geometry("300x350")
# metodo para cambiar titulo de la ventana 
ventana.title("ventana de suma")

def captura_dato():
    text=text_nombre.get()
    Mensaje=Label(ventana,text=f"hola,{text}")
    Mensaje.pack()

etiqueta=Label(ventana,text="INTRODUCE TU NOMBRE : ")
etiqueta.pack()

text_nombre = Entry(ventana)
text_nombre.config(bg="blue",fg="yellow")
text_nombre.pack()

boton_caturar=Button(ventana,text="Enviar",command=captura_dato)
boton_caturar.pack()

ventana.mainloop()