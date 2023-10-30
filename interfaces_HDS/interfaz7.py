from tkinter import *
class Operaciones:

    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry("290x220")
        self.ventana.title("Operaciones Aritmeticas")
        self.ventana.config(bg="lightblue")

# radiobuttons

        self.info=IntVar()

        self.radio_sumar=Radiobutton(self.ventana,text="Suma",value=0,variable=self.info)
        self.radio_sumar.grid(row=2,column=3)

        self.radio_resta=Radiobutton(self.ventana,text="Resta",value=1,variable=self.info)
        self.radio_resta.grid(row=4,column=3)

        self.radio_multi=Radiobutton(self.ventana,text="Multiplicar",value=2,variable=self.info)
        self.radio_multi.grid(row=6,column=3)
    
        self.radio_divi=Radiobutton(self.ventana,text="Dividir",value=3,variable=self.info)
        self.radio_divi.grid(row=8,column=3)

# widget invisibles

        invisible=Label(self.ventana,text="  ")
        invisible.grid(row=0,rowspan=11,column=0)
        self.ventana.config(bg="lightblue")

        invisible_1=Label(self.ventana,text="",font=("Helvetica",1))
        invisible_1.grid(row=0,column=1)
        self.ventana.config(bg="lightblue")

        invisible_2=Label(self.ventana,text="  ")
        invisible_2.grid(row=0,rowspan=11,column=4)

        invisible_3=Label(self.ventana,text="",font=("Helvetica",1))
        invisible_3.grid(row=3,column=1)
        self.ventana.config(bg="lightblue")

        invisible_4=Label(self.ventana,text="",font=("Helvetica",1))
        invisible_4.grid(row=6,column=1)
        self.ventana.config(bg="lightblue")

        invisible_5=Label(self.ventana,text="",font=("Helvetica",1))
        invisible_5.grid(row=9,column=1)
        self.ventana.config(bg="lightblue")

        invisible_6=Label(self.ventana,text="",font=("Helvetica",1))
        invisible_6.grid(row=11,column=1)
        self.ventana.config(bg="lightblue")

        invisible_7=Label(self.ventana,text="             ")
        invisible_7.grid(row=0,rowspan=11,column=2)
        self.ventana.config(bg="lightblue")  

# widget de texto

        frame=Label(self.ventana,text="Ingrese un numero")
        frame.grid(row=1,column=1)

        frame_1=Label(self.ventana,text="Ingrese un numero")
        frame_1.grid(row=4,column=1)

        frame_2=Label(self.ventana,text="Total")
        frame_2.grid(row=7,column=1)

# cuadros de texto
    
        self.cuadro_text=Entry(self.ventana)
        self.cuadro_text.config(bg="black",fg="white")
        self.cuadro_text.grid(row=2,column=1)

        self.cuadro_text1=Entry(self.ventana,bg="blue")
        self.cuadro_text1.config(bg="black",fg="white")
        self.cuadro_text1.grid(row=5,column=1)

        self.cuadro_text2=Entry(self.ventana)
        self.cuadro_text2.config(bg="Yellow",fg="black")
        self.cuadro_text2.grid(row=8,column=1)
  
# botones

        self.boton_calcular=Button(self.ventana,text="Calcular",command=self.realizar_operacion)
        self.boton_calcular.grid(row=10,column=1)

        self.boton_limpiar=Button(self.ventana,text="Limpiar",command=self.limpiar_dato)
        self.boton_limpiar.grid(row=10,column=3)

# FUNCIONES

    def realizar_operacion(self):
         numero1=int(self.cuadro_text.get())
         numero2=int(self.cuadro_text1.get())
         operacion=self.info.get()

         if operacion == 0:  # Suma
            resultado = numero1 + numero2
         elif operacion == 1:  # Resta
            resultado = numero1 - numero2
         elif operacion == 2:  # Multiplicación
            resultado = numero1 * numero2
         elif operacion == 3:  # División
            if numero2 != 0:  # Evitar división por cero
                resultado = numero1 / numero2
            else:
                resultado = "División por cero no permitida"

         self.cuadro_text2.delete(0, "end")
         self.cuadro_text2.insert(0, resultado)

    def limpiar_dato(self):
        self.cuadro_text.delete(0, "end")
        self.cuadro_text1.delete(0, "end")
        self.cuadro_text2.delete(0, "end")

if __name__=="__main__":
        app=Operaciones()
        app.ventana.mainloop()